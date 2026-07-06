"""test_sm_wiring.py — the Stage-3 gauntlet scorecard, pinned.

45/45 cells with the full rule set; 38/45 from banked machinery alone.
The 7 non-banked cells are named: 5 assembled-today (EW sector pairs +
W,H selfs) and 2 color-input (g-Q, g self). If a rule change ever
shifts this split, these tests catch it.
"""

from sm_wiring import (ASSEMBLED_CELLS, INPUT_CELLS, TARGET_EDGES,
                       predicted_edges, score)


def test_full_ruleset_reproduces_the_plate():
    s = score()
    assert s["cells"] == 45
    assert s["right"] == 45
    assert s["wrong"] == []


def test_predicted_equals_target_exactly():
    assert predicted_edges() == TARGET_EDGES


def test_provenance_split_is_pinned():
    s = score()
    assert s["banked_only_right"] == 38
    assert ASSEMBLED_CELLS == {
        frozenset(("W", "Z")), frozenset(("W", "H")), frozenset(("Z", "H")),
        frozenset(["W"]), frozenset(["H"]),
    }
    assert INPUT_CELLS == {frozenset(("g", "Q")), frozenset(["g"])}


def test_the_two_faces_asymmetry():
    """W self-couples, Z does not — the transform's +-18 vs net-0 faces."""
    pred = predicted_edges()
    assert frozenset(["W"]) in pred
    assert frozenset(["Z"]) not in pred


def test_the_never_round_set_has_no_higgs_edge():
    pred = predicted_edges()
    for massless in ("A", "g"):
        assert frozenset((massless, "H")) not in pred
    assert frozenset(("N", "H")) not in pred    # unrounded-nu call (dia flag)
