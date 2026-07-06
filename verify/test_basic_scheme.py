"""test_basic_scheme.py — the forced spine of THE-BASIC-SCHEME as tests.

Every test here is a ◆ claim. If this file is green, the basic scheme
re-derives itself on this machine, today, from exact arithmetic.
CHOICE-dependent statements are tested only for their forced part.
"""

from fractions import Fraction as F

from gtheory import (CARDINALS, CARRIERS, CHARGE_SIGN, CHOICES, HEXAD,
                     bounce, c_rest, cascade, cascade_polarity, chord_arc,
                     chord_axis, composites, degree, derive_137,
                     doubling_orbit, expansion_digits, factorize, generation,
                     halving_order, octave_spiral, reptend, rounded_seventh,
                     transform, wheel_scales)


# --- 0 · frame -------------------------------------------------------------
def test_reptend_is_forced():
    assert reptend(7) == "142857"
    assert len(reptend(7)) == 6            # full reptend: ord_7(10) = 6


def test_hexad_is_doubling_orbit():
    assert tuple(doubling_orbit()) == HEXAD
    assert set(HEXAD) & {3, 6, 9} == set()  # triad never visited


def test_halving_bottoms_at_vector():
    assert [s for s, _ in octave_spiral(24)] == [24, 12, 6, 3]


def test_bounds_assemble_the_one():
    assert int("000001") + int("999999") == 10 ** 6


def test_reptend_and_binary_are_same_set_two_orderings():
    assert sorted("142857") == sorted("124875")


# --- I · the transform -----------------------------------------------------
def test_transform_ledger():
    t = transform()
    assert t["out"] == "124875"
    assert t["down"] == (42, 24, -18)
    assert t["up"] == (57, 75, +18)
    assert t["net"] == 0                    # neutral operation
    assert t["internal_15"] == 15 and t["internal_51"] == 51
    assert t["sum_pre"] == t["sum_post"] == 99
    assert t["internal_51"] - t["internal_15"] == 36
    assert 42 * 24 == 1008 and 36 * 51 == 1836


# --- II · the cascade ------------------------------------------------------
def test_cascade_keeps_every_step():
    assert cascade(24) == [24, 6]           # one fall  (shallow, -)
    assert cascade(42) == [42, 6]
    assert cascade(75) == [75, 12, 3]       # two falls (deep, +)
    assert cascade(57) == [57, 12, 3]


def test_cascade_charge_signs():
    assert cascade_polarity(42) == cascade_polarity(24) == "-"
    assert cascade_polarity(57) == cascade_polarity(75) == "+"
    assert cascade_polarity(99) == "n"


def test_spiral_alternates_sides():
    sides = [side for _, side in octave_spiral(24)]
    assert all(a != b for a, b in zip(sides, sides[1:]))   # forced alternation
    # absolute naming is CHOICES["SIDE_ASSIGNMENT"], not asserted here


# --- III · the bounce -> 1/137 ----------------------------------------------
def test_bounce_net_is_internal_difference():
    b = bounce()
    assert (b["lo"], b["hi"]) == (27, 72)
    assert b["net_off_original"] == (15, 15)   # 42-27, 72-57
    assert b["neutrals"] == 99


def test_block_is_1_over_137():
    b = bounce()
    assert b["block"] == "00729927"
    assert b["fsc_check"] == "00729927"        # long division, exact


def test_137_identities():
    d = derive_137()
    assert d["block_arrival"]["equals_1_over_137"]
    assert d["additive_identity"]["2^7 + 3^2"] == 137
    assert d["spine_identity"]["8*17 + 1"] == 137
    assert d["spine_identity"]["17"] == 17
    assert d["c_rest_carries_137"]


# --- IV · rest frame & generations ------------------------------------------
def test_c_rest_factorization():
    assert c_rest() == 299999997
    assert factorize(c_rest()) == {3: 3, 11: 1, 73: 1, 101: 1, 137: 1}


def test_rounding_ladder_generations():
    g3, g4, g5 = generation(3), generation(4), generation(5)
    assert g3["value"] == F("144.144") and g3["charge"] == "+"
    assert g4["value"] == F("144.0432") and g4["charge"] == "n"
    assert g5["value"] == F("144.00288") and g5["charge"] == "-"
    # carriers {2,8,5} lift to {3,9,6}
    assert (g3["carrier"], g4["carrier"], g5["carrier"]) == (2, 8, 5)
    assert (g3["lifted"], g4["lifted"], g5["lifted"]) == (3, 9, 6)


def test_exact_seventh_is_dimensionless_144():
    assert 1008 * F(1, 7) == 144 == 12 ** 2


def test_truncated_upper_sevenths_deficit():
    total = (F("0.571428") + F("0.714285") + F("0.857142"))
    assert total == F("2.142855")           # truncation manufactures deficit
    assert F(15, 7) - total == F(15, 7) - F(2142855, 10 ** 6)  # short of 15/7


# --- V · Midy / the four sequences ------------------------------------------
def test_midy_halves():
    assert 142 + 857 == 999
    r = reptend(7)
    assert all(int(r[i]) + int(r[i + 3]) == 9 for i in range(3))


def test_four_sequence_differences():
    assert 152847 - 142857 == 9990 and 9990 // 2 == 4995
    assert 152847 - 147852 == 4995
    assert 147852 - 142857 == 4995          # errata: order as stated here
    assert 142857 - 124875 == 17982
    assert F(17982, 4995) == F(18, 5)       # = 3.6 exactly


# --- VI · the 60-degree vacuum ----------------------------------------------
def test_three_chords_share_offlattice_axis():
    assert chord_arc(9, 3) == 120
    assert chord_arc(8, 4) == 200
    assert chord_arc(7, 5) == 280           # arcs step +80
    assert chord_axis(9, 3) == chord_axis(8, 4) == chord_axis(7, 5) == 60
    assert F(60, 40) == F(3, 2)             # position 1.5 — off-lattice
    assert (60 + 180) % 360 == 240          # antipode = position 6 (La)


# --- IV.b · the cardinal tetrad ---------------------------------------------
def test_harmonic_tetrad_quarters_the_circle():
    assert degree(CARDINALS["Do"]) == 0
    assert degree(CARDINALS["Mi"]) == 90
    assert degree(CARDINALS["Sol"]) == 180
    assert degree(CARDINALS["H7"]) == 270   # 7/4 — the harmonic seventh
    # 1/1 : 5/4 : 3/2 : 7/4  =  4 : 5 : 6 : 7
    assert [x * 4 for x in CARDINALS.values()] == [4, 5, 6, 7]


def test_diatonic_step_past_the_bounce():
    assert 24 * F(9, 8) == 27               # bounce target IS Re
    assert 24 * F(5, 4) == 30               # Mi
    assert 72 - 30 == 42                    # origin composite reappears
    assert 30 - 27 == 3


def test_two_thirty_degree_gaps():
    assert degree(F(4, 3)) - degree(F(5, 4)) == 30     # Mi -> Fa
    assert 270 - degree(F(5, 3)) == 30                  # La -> H7


# --- VII · multiple scales / the muon composite ------------------------------
def test_wheel_orders():
    assert doubling_orbit() == [1, 2, 4, 8, 7, 5]
    assert halving_order() == [1, 5, 7, 8, 4, 2]


def test_muon_composite():
    w = wheel_scales()
    assert w["up"][5] == 768 and w["down"][5] == 206
    assert w["muon"] == "206.768"
    assert 768 == 2 ** 8 * 3


def test_207_block_structure():
    assert sum({1, 2, 4}) == 7 and sum({8, 7, 5}) == 20      # -> "20|7"
    assert 53 + 52 + 51 + 51 == 207
    assert F(201, 64) == F("3.140625")       # lower rest-pi bound (typo fixed)


# --- collatz sheet -----------------------------------------------------------
def test_collatz_sheet_facts():
    assert 999999 // 99 == 10101
    assert int("10101", 2) == 21 == 3 * 7    # 10101 read in binary
    assert 3 + 2 + 1 == 6                    # the gap-sum
    assert 66 == 15 + 51 == 42 + 24 == (57 + 75) // 2


# --- choices registry (the honest heart) -------------------------------------
def test_choices_are_named():
    assert {"BASE", "SEED_DIVISOR", "ROUNDING_RULE",
            "SIDE_ASSIGNMENT", "DEGREE_MAP"} <= set(CHOICES)
