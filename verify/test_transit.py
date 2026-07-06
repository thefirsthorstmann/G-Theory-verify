"""test_transit.py — the transit read pinned (CC's hybrid-state arc)."""

from fractions import Fraction as F

from gtheory import c_rest, rounded_seventh
from transit import (LADDER_TAILS, ladder_down, ladder_up,
                     seven_filter_count, transit, transit_rep)


def test_finite_reads_and_the_dyadic_null():
    """CC's readings — and every finite read is dyadic by construction."""
    assert transit("005") == F(5, 8)
    assert transit("008") == 1                    # one whole suspended unit
    assert transit("036") == F(3, 2)              # the FSC tail in transit: Sol
    assert transit("36") == 3
    for s in ("005", "008", "036", "1429", "999"):
        den = transit(s).denominator
        assert den & (den - 1) == 0               # power of 2: niceness built in


def test_the_reptend_in_transit_is_23_ninths():
    """161/63 -> the 7 cancels itself; the residue pair rebuilds 207."""
    s, v = transit_rep("142857")
    assert (s, v) == (161, F(23, 9)) and s == 7 * 23
    assert 23 * 9 == 207                          # the banked muon block


def test_the_banked_family_reads_in_ninths():
    assert transit_rep("124875")[1] == F(7, 3)    # the transform order
    assert transit_rep("152847")[1] == F(25, 9) == F(5, 3) ** 2   # La squared
    assert transit_rep("147852")[1] == F(28, 9)


def test_the_seven_filter_passes_a_fifth():
    """Exactly 144 of 720 orderings cancel the seed — the 144 itself."""
    assert seven_filter_count() == 144


def test_the_midy_comma_is_the_depth3_rounding_exactly():
    """rounded(1/7, 3) = (1/7) x 1001/1000; depth 6 rounds down by 10^-6;
    depths 4, 5 are dirty. The clean pair is Midy's own (+1 | -1)."""
    assert rounded_seventh(3) * 7 == F(1001, 1000)
    assert rounded_seventh(6) * 7 == F(10 ** 6 - 1, 10 ** 6)
    assert rounded_seventh(4) * 7 - 1 == F(3, 10 ** 4)      # dirty
    assert rounded_seventh(5) * 7 - 1 == F(2, 10 ** 5)      # dirty
    assert 1001 % 7 == 0 and 142 + 857 == 999               # Midy's engine
    assert 10 ** 6 - 1 == 999 * 1001


def test_the_1001_anatomy_and_register_family():
    assert 1001 == 7 * 11 * 13 and 143 == 11 * 13
    assert 1000 == (2 * 5) ** 3
    assert 1 + transit("001") == F(9, 8)          # 1.001 in transit = Re
    assert c_rest() % 101 == 0                    # 101 = 10^2+1 sits in c_rest
    assert 1001 ** 2 == 1002001 and 1001 ** 3 == 1003003001   # Pascal registers


def test_the_ladder_projections():
    """Down on 24: {3, 9/2, 3/2, -3/8} = 3 x {1, 3/2, 1/2, -1/8};
    up: {8, 48, 64, -64}. Depth 6 = MINUS THE CLOCK RATIO."""
    assert [ladder_down(k) for k in (3, 4, 5, 6)] == \
        [3, F(9, 2), F(3, 2), F(-3, 8)]
    assert ladder_down(4) == 3 * F(3, 2)          # Sol over the vector
    assert ladder_down(6) == -F(3, 8)             # the clock ratio, down face
    assert [ladder_up(k) for k in (3, 4, 5, 6)] == [8, 48, 64, -64]


def test_ccs_240_chain():
    """240 / transit(.005) = 384 = 3 x 2^7; 8/5 = the inverted Mi."""
    assert 240 / transit("005") == 384 == 3 * 2 ** 7
    assert F(2) / F(5, 4) == F(8, 5)


def test_the_1008_anatomy():
    """CC's rationale: the pair IS 33 +- 9, so the product is the mean
    squared minus the Midy-nine squared — the 33 pushes the multiplication."""
    assert (42, 24) == (33 + 9, 33 - 9)
    assert 42 * 24 == 1008 == 33 ** 2 - 9 ** 2
    assert 24 + 42 + 33 == 99 == 3 * 33          # dependent: pair+mean = 3*mean
    assert (42 // 3, 24 // 3) == (14, 8)         # thirds: reptend head | ring
    assert 42 == 6 * 7 and 24 == 8 * 3           # faces (6|8) on cofactors (7|3)


def test_the_144_seat():
    """Sol of 96 (first 3-digit Sol); 12^2 with mirrored square 441 = 21^2;
    F(12) = 144 (index = root; unique square Fibonacci > 1, Cohn 1964)."""
    assert [x * 3 // 2 for x in (24, 48, 96)] == [36, 72, 144]
    assert 144 == 12 ** 2 and 441 == 21 ** 2     # squareness itself mirrors
    a, b = 1, 1
    for _ in range(10):
        a, b = b, a + b
    assert b == 144                               # F(12)


def test_the_two_pair_makers():
    """The width-3 register: x1001 echoes (a|a, NEUTRAL twin), x999
    splits (a-1 | 1000-a, complements summing to 999) — for all 3-digit a."""
    assert 144 * 1001 == 144144                   # 144|144 the echo
    assert 144 * 999 == 143856 and 143 + 856 == 999
    for a in (100, 143, 500, 857, 999):
        assert a * 1001 == a * 1000 + a
        assert (a * 999) // 1000 + (a * 999) % 1000 == 999


def test_the_seventh_ties_the_faces():
    """1/7 = 143/1001 (the +1 face carries the rounded numerator);
    143 x 999 = 142857 (the -1 face unrolls the reptend); 143 = 12^2 - 1;
    rest 144 exact vs observed echo 144.144."""
    assert F(143, 1001) == F(1, 7)
    assert 143 * 999 == 142857
    assert 143 == 12 ** 2 - 1 == 11 * 13
    assert 1008 - 1001 == 7                       # 7x144 vs 7x143: one seed apart
    assert F(1008, 7) == 144                      # the rest value, exact
    assert F(1008) * F(143, 1000) == F(144144, 1000)   # the echo twin


def test_the_144_passers_characterized():
    """ANSWERED (open-problem ledger): pass <=> the distance-3 pair-sums hit one of
    five multisets (all summing 27); THE MIDY PAIRING (9,9,9) IS THE
    UNIQUE SLOT-FREE PASSER (48 any-arrangement); the other four pass
    only cyclically (24 each): 144 = 48 + 4 x 24."""
    from itertools import permutations
    counts = {}
    for p in permutations((1, 4, 2, 8, 5, 7)):
        s = (p[0] + p[3], p[1] + p[4], p[2] + p[5])
        if (4 * s[0] + 2 * s[1] + s[2]) % 7 == 0:
            counts[tuple(sorted(s))] = counts.get(tuple(sorted(s)), 0) + 1
    assert counts[(9, 9, 9)] == 48
    assert sorted(counts.values()) == [24, 24, 24, 24, 48]
    assert all(sum(k) == 27 for k in counts)
    assert sum(counts.values()) == 144


def test_the_transit_transform_law():
    """ANSWERED (open-problem ledger): the transform's transit shift in closed form
    — Delta(block-sum) = 8(d3 - d2) + (d6 - d5); the reptend shifts by
    exactly -2/9 (23/9 -> 21/9)."""
    for block in ("142857", "152847"):
        d = [int(c) for c in block]
        out = f"{d[0]}{d[2]}{d[1]}{d[3]}{d[5]}{d[4]}"
        delta = transit_rep(out)[0] - transit_rep(block)[0]
        assert delta == 8 * (d[2] - d[1]) + (d[5] - d[4])
    assert transit_rep("124875")[1] - transit_rep("142857")[1] == F(-2, 9)
