"""Analyse the crowdsourced data and apply the selection rules.

    uv run python analysis.py                                   # files_heroku in path_data
    uv run python analysis.py --data data/entries.jsonl         # local runs without MongoDB
    uv run python analysis.py --data data/simulated/entries.jsonl --out _output/simulated

With ``download_data`` true in config, the MongoDB collection is first exported into
the first of ``files_heroku`` (needs mongoexport and ``mongodb_uri`` in secret).

Writes to the output folder:
    participants.csv   every participant: finished, attention, excluded and why
    summary.csv        one row per property: BWS score + CI, A/B results, status
    redundant.csv      property pairs judged alike (|r| >= redundancy_min_abs_r)
    open_answers.csv   the open-question answers, for thematic coding
    report.md          the selected properties and where every other one stopped
"""

from __future__ import annotations

import argparse
from pathlib import Path

import pandas as pd

from avprops.analysis import analyse
from avprops.common import load_config, load_properties, load_secret, resolve
from avprops.crowd import download, read_rows, rows_to_records


def write_report(result: dict, config: dict, path: Path) -> None:
    summary = result["summary"]
    lines = [
        f"# Property selection: {config['study_id']}",
        "",
        f"Participants: {result['n_records']} records, {result['n_kept']} kept after exclusions.",
        "",
        "## Selected",
        "",
    ]
    selected = summary[summary["selected"]]
    if selected.empty:
        lines.append("No property passed every rule.")
    for prop, row in selected.iterrows():
        lines.append(f"- **{row['name']}** (`{prop}`): BWS {row['bws_score']:+.2f} "
                     f"[{row['bws_ci_low']:+.2f}, {row['bws_ci_high']:+.2f}], "
                     f"noticed {row['noticed_share']:.0%}, majority preference {row['majority_share']:.0%}")
    lines += ["", "## All properties", "",
              "| Property | BWS score | Noticed | Majority pref. | Status |",
              "| --- | --- | --- | --- | --- |"]
    for prop, row in summary.iterrows():
        def pct(v):
            return "" if pd.isna(v) else f"{v:.0%}"
        lines.append(f"| {row['name']} | {row['bws_score']:+.2f} | {pct(row['noticed_share'])} | "
                     f"{pct(row['majority_share'])} | {row['status']} |")
    lines += ["", "Rules (from the config): noticed by at least "
              f"{config['noticed_min_share']:.0%}; in the top {config['matters_top_fraction']:.0%} by BWS "
              "or a rating effect at p < .05; majority preference at most "
              f"{config['disagreement_max_majority_share']:.0%}; not redundant at |r| >= "
              f"{config['redundancy_min_abs_r']}; top {config['select_n']} by BWS score.", ""]
    path.write_text("\n".join(lines), encoding="utf-8")


def main() -> None:
    config = load_config()
    parser = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    parser.add_argument("--data", nargs="+", help="data files (default: files_heroku in path_data)")
    parser.add_argument("--out", default=config["output_dir"], help="output folder")
    args = parser.parse_args()

    if args.data:
        files = [resolve(f) for f in args.data]
    else:
        files = [resolve(config["path_data"]) / f for f in config["files_heroku"]]
        if config["download_data"]:
            download(load_secret()["mongodb_uri"], files[0])
    missing = [str(f) for f in files if not f.exists()]
    if missing:
        raise SystemExit(f"data file(s) not found: {', '.join(missing)}")

    records = rows_to_records(read_rows(files), config["attention_max_wrong"])
    if not records:
        raise SystemExit("no participant data in " + ", ".join(str(f) for f in files))
    result = analyse(records, load_properties(config), config)

    out = resolve(args.out)
    out.mkdir(parents=True, exist_ok=True)
    participants = pd.DataFrame([{
        "pid": r["pid"], "finished": r.get("finished"), "debug": r.get("debug"),
        "attention_wrong": (r.get("attention") or {}).get("wrong"),
        "bws_trials": len(r.get("bws", [])), "ab_pairs": len(r.get("ab", [])),
    } for r in records]).merge(result["exclusions"], on="pid")
    participants.to_csv(out / "participants.csv", index=False)
    result["summary"].to_csv(out / "summary.csv", index_label="property")
    result["redundant"].to_csv(out / "redundant.csv", index=False)
    result["open_answers"].to_csv(out / "open_answers.csv", index=False)
    write_report(result, config, out / "report.md")

    print(f"{result['n_kept']} of {result['n_records']} participants kept")
    print(result["summary"][["name", "bws_score", "noticed_share", "majority_share", "status"]]
          .to_string(float_format=lambda v: f"{v:.2f}"))
    print(f"\nWrote {out}")


if __name__ == "__main__":
    main()
