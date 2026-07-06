"""test_sm_map.py — the SM content layer, pinned."""

from fractions import Fraction as F

from sm_map import (CARRIERS, PARAMETERS, TYPES, charge_sums, full_roster,
                    generation_polarity, manifest_roster)


def test_36_equals_12_plus_24():
    r = full_roster()
    assert len(r["manifest"]) == 12          # 3 generations x 4 types
    assert len(r["vectors"]) == 24           # the +- pairs
    assert r["total"] == 36                  # banked Forced-structural count


def test_generation_polarities_are_the_roundup_triple():
    assert {g: generation_polarity(g) for g in (1, 2, 3)} == \
        {1: "+", 2: "n", 3: "-"}             # depths 3/4/5 (T3, banked)


def test_quark_charges_are_la_and_fa():
    assert TYPES["up"]["q"] == F(2, 3)       # La 240 = 2/3  [banked]
    assert TYPES["down"]["q"] == F(1, 3)     # Fa 120 = 1/3
    assert TYPES["nu"]["q"] == 0             # the 9-axis


def test_roster_names_cover_the_sm():
    names = {m["name"] for m in manifest_roster()}
    assert names == {"u", "d", "e", "nu_e", "c", "s", "mu", "nu_mu",
                     "t", "b", "tau", "nu_tau"}


def test_charge_sum_anomaly_observation():
    s = charge_sums()
    assert s["without_color"] == F(-2, 3)    # does not vanish
    assert s["with_color"] == 0              # the owed x3 closes it exactly


def test_carrier_roster():
    assert {k: v["sm"] for k, v in CARRIERS.items()} == {
        "A": "photon", "H": "Higgs", "W": "W+-", "Z": "Z0",
        "g": "gluons x8", "G": "graviton"}
    assert CARRIERS["G"]["spin"] == 2 and CARRIERS["H"]["spin"] == 0


def test_parameter_layer_present():
    assert {"alpha^-1", "Koide Q", "PMNS th23", "Higgs lambda",
            "muon m/e", "proton m/e"} <= set(PARAMETERS)
