"""Write synthetic participant data with a known ground truth.

    uv run python simulate.py --n 150
    uv run python analysis.py --data data/simulated/entries.jsonl --out _output/simulated

Each property gets a true importance, a probability of being noticed and a population
share preferring its high level. Participants answer the BWS trials of a design
version (best = highest noisy utility, worst = lowest) and the A/B pairs from those
truths. The output has the shape the server stores (``{"data": [jsPsych rows]}`` per
line), so the whole path from raw rows to the selection is checked before any real
data exists. The truth is written to data/simulated/truth.json.
"""

from __future__ import annotations

import argparse
import json

import numpy as np

from avprops.common import load_config, resolve, PROJECT_ROOT

RATING_KEYS = ("understanding", "safety", "load")


def simulate(design: dict, n: int, seed: int) -> tuple[list[dict], dict]:
    """Return documents ``{"data": rows}`` (one per participant) and the truth."""
    rng = np.random.default_rng(seed)
    props = [p["id"] for p in design["properties"]]
    scenes = [s["id"] for s in design["scenes"]]
    truth = {
        p: {
            "importance": float(rng.normal(0, 1)),
            "notice_prob": float(rng.uniform(0.5, 0.98)),
            "prefer_high": float(rng.uniform(0.1, 0.9)),
        }
        for p in props
    }
    points = design["ab"]["scale_points"]
    documents = []
    for i in range(n):
        code = f"sim{i:04d}"
        rows: list[dict] = []

        def add(task: str, **fields) -> None:
            rows.append({"trial_index": len(rows), "worker_code": code, "study_id": design["study_id"],
                         "design_generated_at": design["generated_at"], "debug": False, "task": task, **fields})

        utility = {p: truth[p]["importance"] + rng.normal(0, 0.7) for p in props}
        version = int(rng.integers(len(design["bws"]["versions"])))
        add("instructions", bws_version=version)
        add("consent", response={"consent": "Yes"}, rt=3000)
        add("demographics", response={"age": "30", "nationality": "Dutch", "country_residence": "Netherlands"})
        add("open_question", scene=design["baseline_scene"], response={"open": "Show why it brakes."},
            rt=20000, hidden=False)
        for t, items in enumerate(design["bws"]["versions"][version]):
            noisy = {p: utility[p] + rng.gumbel() for p in items}
            add("bws", trial=t, items=items, best=max(noisy, key=noisy.get), worst=min(noisy, key=noisy.get),
                rt=int(rng.integers(2500, 12000)), hidden=False)
        for k, p in enumerate(rng.permutation(props)[: design["ab"]["pairs_per_participant"]]):
            noticed = bool(rng.random() < truth[p]["notice_prob"])
            level = ("high" if rng.random() < truth[p]["prefer_high"] else "low") if noticed \
                else ("high" if rng.random() < 0.5 else "low")
            a_level = "low" if rng.random() < 0.5 else "high"
            add("ab", index=k, property=str(p), scene=scenes[k % len(scenes)], a_level=a_level,
                b_level="high" if a_level == "low" else "low", noticed=noticed,
                preferred_option="A" if level == a_level else "B", preferred_level=level,
                importance=int(np.clip(round((points + 1) / 2 + 1.2 * utility[p]), 1, points)),
                ratings={lvl: {key: int(rng.integers(1, points + 1)) for key in RATING_KEYS}
                         for lvl in ("low", "high")},
                rt=int(rng.integers(8000, 40000)), hidden=False)
        for _ in range(5):
            add("attention", correct=bool(rng.random() < 0.97))
        add("final", response={"comment": ""})
        documents.append({"data": rows})
    return documents, truth


def main() -> None:
    parser = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    parser.add_argument("--n", type=int, default=150, help="number of synthetic participants")
    parser.add_argument("--seed", type=int, default=1)
    args = parser.parse_args()

    config = load_config()
    design = json.loads(resolve(config["design_output"]).read_text(encoding="utf-8"))
    documents, truth = simulate(design, args.n, args.seed)

    out = PROJECT_ROOT / "data" / "simulated"
    out.mkdir(parents=True, exist_ok=True)
    with (out / "entries.jsonl").open("w", encoding="utf-8") as fh:
        for doc in documents:
            fh.write(json.dumps(doc) + "\n")
    (out / "truth.json").write_text(json.dumps(truth, indent=1), encoding="utf-8")
    print(f"Wrote {len(documents)} participants to {out / 'entries.jsonl'} and the truth to {out / 'truth.json'}")


if __name__ == "__main__":
    main()
