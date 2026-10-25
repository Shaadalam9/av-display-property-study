import itertools
import json

import numpy as np
import pytest

from avprops.analysis import analyse
from avprops.common import load_config, load_properties, load_scenes
from avprops.crowd import read_documents, read_rows, rows_to_records
from avprops.design import build_design, bws_version
from simulate import simulate


@pytest.fixture(scope="module")
def config():
    cfg = load_config()
    cfg["bws_design_versions"] = 10
    return cfg


@pytest.fixture(scope="module")
def design(config):
    return build_design(config, load_properties(config), load_scenes(config))


def records_from(documents, config):
    rows = [row for doc in documents for row in doc["data"]]
    return rows_to_records(rows, config["attention_max_wrong"])


@pytest.mark.parametrize("n_items,k,r", [(21, 4, 3), (14, 4, 4), (12, 5, 3), (5, 5, 2)])
def test_bws_version_is_balanced(n_items, k, r):
    blocks = bws_version(n_items, k, r, np.random.default_rng(0))
    counts = np.bincount([i for b in blocks for i in b], minlength=n_items)
    assert all(len(set(b)) == k for b in blocks), "an item appears twice in one trial"
    assert counts.min() >= r and counts.max() - counts.min() <= 1


def test_bws_pairs_are_spread(design):
    ids = [p["id"] for p in design["properties"]]
    for version in design["bws"]["versions"]:
        pairs = {pair: 0 for pair in itertools.combinations(sorted(ids), 2)}
        for block in version:
            for pair in itertools.combinations(sorted(block), 2):
                pairs[pair] += 1
        assert max(pairs.values()) <= 2


def test_screened_out_properties_are_not_shown(config, design):
    dropped = {p["id"] for p in load_properties(config, screened_only=False) if not p["screened_in"]}
    shown = {i for v in design["bws"]["versions"] for b in v for i in b}
    assert dropped and not dropped & shown


def test_mongoexport_lines_and_array_are_read_alike(tmp_path, design, config):
    documents, _ = simulate(design, n=3, seed=1)
    lines, array = tmp_path / "lines.json", tmp_path / "array.json"
    lines.write_text("\n".join(json.dumps(d | {"_id": {"$oid": str(i)}}) for i, d in enumerate(documents)))
    array.write_text(json.dumps(documents))
    assert len(read_documents(lines)) == len(read_documents(array)) == 3
    assert read_rows([lines]) == read_rows([array])


def test_rows_become_one_record_per_worker(design, config):
    documents, _ = simulate(design, n=4, seed=2)
    # the browser sends a participant's rows in several batches; a resent batch must not duplicate rows
    split = []
    for doc in documents:
        rows = doc["data"]
        split += [{"data": rows[:10]}, {"data": rows[10:]}, {"data": rows[5:10]}]
    records = records_from(split, config)
    assert len(records) == 4
    rec = records[0]
    assert rec["finished"] and rec["consent"]
    assert len(rec["bws"]) == len(design["bws"]["versions"][rec["bws_version"]])
    assert len(rec["ab"]) == design["ab"]["pairs_per_participant"]


def test_analysis_recovers_simulated_truth(config, design):
    documents, truth = simulate(design, n=150, seed=3)
    summary = analyse(records_from(documents, config), load_properties(config), config)["summary"]
    true_imp = [truth[p]["importance"] for p in summary.index]
    true_pref = [truth[p]["prefer_high"] for p in summary.index]
    assert np.corrcoef(summary["bws_score"], true_imp)[0, 1] > 0.9
    assert np.corrcoef(summary["prefer_high_share"], true_pref)[0, 1] > 0.85
    assert 1 <= summary["selected"].sum() <= config["select_n"]
    assert summary["status"].notna().all()


def test_selected_properties_meet_every_rule(config, design):
    documents, _ = simulate(design, n=150, seed=4)
    summary = analyse(records_from(documents, config), load_properties(config), config)["summary"]
    chosen = summary[summary["selected"]]
    assert (chosen["noticed_share"] >= config["noticed_min_share"]).all()
    assert (chosen["majority_share"] <= config["disagreement_max_majority_share"]).all()


def test_exclusions(config, design):
    documents, _ = simulate(design, n=20, seed=5)
    rows0, rows1, rows2, rows3 = (documents[i]["data"] for i in range(4))
    for row in rows0:
        if row["task"] == "attention":
            row["correct"] = False
    for row in rows1:
        row["debug"] = True
    for row in rows2:
        if row["task"] == "bws":
            row["rt"] = 200
    documents[3]["data"] = [row for row in rows3 if row["task"] != "final"]
    result = analyse(records_from(documents, config), load_properties(config), config)
    excluded = set(result["exclusions"].query("excluded")["pid"])
    assert {"sim0000", "sim0001", "sim0002", "sim0003"} <= excluded
