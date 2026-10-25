"""Analysis of the participant records and the pre-registered selection rules.

Inputs are participant records built from the crowdsourced rows by avprops.crowd.
The steps mirror the study design:

1. Exclusions: debug sessions, unfinished sessions, too many wrong attention answers,
   implausibly fast BWS answers, A/B pairs answered with the tab hidden too often.
2. Task A (BWS): per participant, (times best - times worst) / times shown for each
   property; the property's score is the mean over participants with a bootstrap CI.
3. Task B (A/B pairs): share who noticed the difference; among those who noticed,
   the share preferring the high level and the majority share; mean importance; and
   the high-minus-low difference of each rating with a Wilcoxon signed-rank test.
4. Selection: noticeable -> matters -> people disagree -> not redundant, then the top
   ``select_n`` by BWS score. Every property gets a status saying where it stopped.
"""

from __future__ import annotations

from typing import Any

import numpy as np
import pandas as pd
from scipy import stats

RATING_KEYS = ("understanding", "safety", "load")


def apply_exclusions(records: list[dict], config: dict) -> tuple[list[dict], pd.DataFrame]:
    """Return the kept records and a table of every participant with the reason excluded."""
    kept, rows = [], []
    for rec in records:
        reasons = []
        if config["exclude_debug"] and rec.get("debug"):
            reasons.append("debug session")
        if config["exclude_unfinished"] and rec.get("finished") is False:
            reasons.append("did not finish")
        attention = rec.get("attention") or {}
        if not attention.get("passed", False):
            reasons.append(f"more than {config['attention_max_wrong']} wrong attention answers")
        rts = [t["rt_ms"] for t in rec.get("bws", [])]
        if rts and float(np.median(rts)) < config["min_median_bws_rt_ms"]:
            reasons.append("BWS answered too fast")
        ab = rec.get("ab", [])
        if ab and np.mean([bool(p.get("hidden")) for p in ab]) > config["max_hidden_ab_share"]:
            reasons.append("tab hidden during too many A/B pairs")
        rows.append({"pid": rec.get("pid"), "excluded": bool(reasons), "reasons": "; ".join(reasons)})
        if not reasons:
            kept.append(rec)
    return kept, pd.DataFrame(rows, columns=["pid", "excluded", "reasons"])


def bws_individual(records: list[dict], prop_ids: list[str]) -> pd.DataFrame:
    """Participants x properties matrix of (best - worst) / shown, NaN where never shown."""
    rows = {}
    for rec in records:
        shown = dict.fromkeys(prop_ids, 0)
        score = dict.fromkeys(prop_ids, 0)
        for trial in rec.get("bws", []):
            for item in trial["items"]:
                if item in shown:
                    shown[item] += 1
            if trial["best"] in score:
                score[trial["best"]] += 1
            if trial["worst"] in score:
                score[trial["worst"]] -= 1
        rows[rec["pid"]] = {p: (score[p] / shown[p] if shown[p] else np.nan) for p in prop_ids}
    return pd.DataFrame.from_dict(rows, orient="index", columns=prop_ids)


def bws_summary(individual: pd.DataFrame, n_boot: int, seed: int) -> pd.DataFrame:
    rng = np.random.default_rng(seed)
    values = individual.to_numpy(dtype=float)
    n = len(values)
    means = np.nanmean(values, axis=0) if n else np.full(values.shape[1], np.nan)
    if n > 1:
        boots = np.array([np.nanmean(values[rng.integers(0, n, n)], axis=0) for _ in range(n_boot)])
        lo, hi = np.nanpercentile(boots, [2.5, 97.5], axis=0)
    else:
        lo = hi = np.full(values.shape[1], np.nan)
    out = pd.DataFrame({
        "bws_score": means,
        "bws_ci_low": lo,
        "bws_ci_high": hi,
        "bws_n": np.sum(~np.isnan(values), axis=0),
    }, index=individual.columns)
    out["bws_rank"] = out["bws_score"].rank(ascending=False, method="min")
    return out


def _wilcoxon_p(diffs: list[float]) -> float:
    diffs = [d for d in diffs if d != 0]
    if len(diffs) < 6:
        return np.nan
    return float(stats.wilcoxon(diffs).pvalue)


def ab_summary(records: list[dict], prop_ids: list[str]) -> pd.DataFrame:
    by_prop: dict[str, list[dict]] = {p: [] for p in prop_ids}
    for rec in records:
        for pair in rec.get("ab", []):
            if pair["property"] in by_prop:
                by_prop[pair["property"]].append(pair)

    rows = {}
    for prop, pairs in by_prop.items():
        noticed = [p for p in pairs if p["noticed"]]
        prefer_high = [p["preferred_level"] == "high" for p in noticed]
        share_high = float(np.mean(prefer_high)) if prefer_high else np.nan
        row = {
            "ab_n": len(pairs),
            "noticed_share": float(np.mean([p["noticed"] for p in pairs])) if pairs else np.nan,
            "pref_n": len(noticed),
            "prefer_high_share": share_high,
            "majority_share": max(share_high, 1 - share_high) if prefer_high else np.nan,
            "majority_level": ("high" if share_high >= 0.5 else "low") if prefer_high else "",
            "importance_mean": float(np.mean([p["importance"] for p in pairs])) if pairs else np.nan,
        }
        for key in RATING_KEYS:
            diffs = [p["ratings"]["high"][key] - p["ratings"]["low"][key]
                     for p in pairs if p.get("ratings")]
            row[f"{key}_diff_mean"] = float(np.mean(diffs)) if diffs else np.nan
            row[f"{key}_diff_p"] = _wilcoxon_p(diffs)
        rows[prop] = row
    return pd.DataFrame.from_dict(rows, orient="index")


def redundant_pairs(individual: pd.DataFrame, min_abs_r: float, min_n: int = 10) -> pd.DataFrame:
    """Property pairs whose individual BWS scores correlate strongly across participants."""
    rows = []
    cols = list(individual.columns)
    for i, a in enumerate(cols):
        for b in cols[i + 1:]:
            both = individual[[a, b]].dropna()
            if len(both) < min_n or both[a].std() == 0 or both[b].std() == 0:
                continue
            r = float(np.corrcoef(both[a], both[b])[0, 1])
            if abs(r) >= min_abs_r:
                rows.append({"property_a": a, "property_b": b, "r": r, "n": len(both)})
    return pd.DataFrame(rows, columns=["property_a", "property_b", "r", "n"])


def select_properties(summary: pd.DataFrame, redundant: pd.DataFrame, config: dict) -> pd.DataFrame:
    """Apply the pre-registered rules; add a ``status`` column and the final ``selected`` flag."""
    summary = summary.sort_values("bws_score", ascending=False).copy()
    n_top = int(np.ceil(len(summary) * config["matters_top_fraction"]))
    top = set(summary.index[:n_top])
    alpha = 0.05

    partners: dict[str, set[str]] = {}
    for row in redundant.itertuples():
        partners.setdefault(row.property_a, set()).add(row.property_b)
        partners.setdefault(row.property_b, set()).add(row.property_a)

    status, chosen = {}, []
    for prop, row in summary.iterrows():
        rating_effect = any(row.get(f"{k}_diff_p", np.nan) < alpha for k in RATING_KEYS)
        if not row["noticed_share"] >= config["noticed_min_share"]:
            status[prop] = "not noticed"
        elif prop not in top and not rating_effect:
            status[prop] = "does not matter"
        elif pd.isna(row["majority_share"]):
            status[prop] = "no preference data"
        elif row["majority_share"] > config["disagreement_max_majority_share"]:
            status[prop] = f"consensus: fix at {row['majority_level']}"
        elif partners.get(prop, set()) & set(chosen):
            status[prop] = "redundant with " + ", ".join(sorted(partners[prop] & set(chosen)))
        elif len(chosen) < config["select_n"]:
            chosen.append(prop)
            status[prop] = "selected"
        else:
            status[prop] = "eligible, below cut-off"
    summary["status"] = pd.Series(status)
    summary["selected"] = summary["status"] == "selected"
    return summary


def analyse(records: list[dict], properties: list[dict], config: dict) -> dict[str, Any]:
    prop_ids = [p["id"] for p in properties]
    kept, exclusions = apply_exclusions(records, config)
    individual = bws_individual(kept, prop_ids)
    summary = bws_summary(individual, config["bootstrap_samples"], config["bootstrap_seed"])
    summary = summary.join(ab_summary(kept, prop_ids))
    summary.insert(0, "name", [next(p["name"] for p in properties if p["id"] == i) for i in summary.index])
    redundant = redundant_pairs(individual, config["redundancy_min_abs_r"])
    summary = select_properties(summary, redundant, config)
    return {
        "n_records": len(records),
        "n_kept": len(kept),
        "exclusions": exclusions,
        "summary": summary,
        "redundant": redundant,
        "open_answers": pd.DataFrame(
            [{"pid": r["pid"], "baseline": (r.get("open_question") or {}).get("text", ""),
              "final_comment": r.get("final_comment", "")} for r in kept],
            columns=["pid", "baseline", "final_comment"]),
    }
