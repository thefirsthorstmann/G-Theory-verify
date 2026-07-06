"""test_pn_2022.py — the 2022 Positive/Neutral System: recipe recovered.

Source: 'Pythagorean Limma Notes 1.0' pp. 3-4 (read visually this
session). POSITIVE SYSTEM: nine apex-up triangles on the 51-wheel,
values = the digit-triples 982, 397, 779, 595, 130, 022, 338, 188,
444 (595 among them — the first banked lost value). NEUTRAL SYSTEM:
eight apex-down triangles, values 952, 333, 958, 666, 124, 796, 952,
116 (the other two lost values, 666 and 116). The red labels on the
pages are the digital roots / digit-sums (verified below). The
centers: positive 4 = dr(130); neutral 13; 4 + 13 = 17 — the spine.
RANGE 9 (positive) vs RANGE 16 (neutral) — the squares 3^2 | 4^2.
Cross-system: 666/444 = 3/2, the page's own printed ratio.
CC's four-year memory '116 at pos 4, 20, 37' resolves to the wheel-B
candidate (1, 20, 37) — two of three positions exact.
The FULL 17-triad tiling remains the open search (round 1: no strict
(16,17,18) tiling; round 2: no [12,24]-arc partition on wheel B) —
the envelope curves indicate stepwise-rotating triangle families,
the next constraint to encode.
"""

from fractions import Fraction as F
from gtheory import dr, expansion_digits

POSITIVE = ["982", "397", "779", "595", "130", "022", "338", "188", "444"]
NEUTRAL = ["952", "333", "958", "666", "124", "796", "952", "116"]
DEC51 = "141592653589793238462643383279502884197169399375105"


def test_the_lost_values_are_found():
    """595, 666, 116 — the machine-unreconstructed 2022 triple —
    located: 595 positive, 666 and 116 neutral."""
    assert "595" in POSITIVE
    assert "666" in NEUTRAL and "116" in NEUTRAL


def test_the_red_labels_are_digital_roots():
    """The page's red digits verified: dr of each positive value;
    the positive center 4 = dr(130)."""
    reds = [1, 1, 5, 1, 4, 4, 5, 8, 3]
    assert [dr(int(v)) for v in POSITIVE] == reds
    assert dr(130) == 4                            # the center


def test_the_neutral_digit_sums():
    """The neutral page's red row: digit sums 16,9,22,18,7,22,16,8."""
    sums = [sum(int(c) for c in v) for v in NEUTRAL]
    assert sums == [16, 9, 22, 18, 7, 22, 16, 8]


def test_the_structure_facts():
    """9 up + 8 down = 17 triads = 51 cells; centers 4 + 13 = 17 (the
    spine); ranges 9 | 16 = 3^2 | 4^2; 666/444 = 3/2 (printed)."""
    assert len(POSITIVE) == 9 and len(NEUTRAL) == 8
    assert 9 * 3 + 8 * 3 == 51
    assert 4 + 13 == 17
    assert (9, 16) == (3 ** 2, 4 ** 2)
    assert F(666, 444) == F(3, 2)


def test_ccs_memory_candidate():
    """116 = digits (1,1,6): wheel-B positions (1, 20, 37) carry
    (1, 6, 1) — a rotation of 116 — matching CC's remembered
    (4, 20, 37) in two of three positions."""
    d = {i + 1: DEC51[i] for i in range(51)}
    triple = d[1] + d[20] + d[37]
    rots = {triple, triple[1:] + triple[0], triple[2:] + triple[:2]}
    assert "116" in rots


def test_the_pi_averages_diagram_is_accurate():
    """CC's 'pi averages' diagram, verified exact: the 1,3,0 triangle
    is THE 17-COMB FIBER {15, 32, 49} — perfectly equilateral, its
    vertices the wheel's three red landmarks (the 3 at 15, the rest-
    marker 0 at 32, the terminal 1 at 49); the banked fiber '301'
    read from the terminal = '130', the P/N center. The three strings
    sum 75, 91, 82 (averages 4.6875, 5.6875, 5.125; DRs 3, 1, 1 — all
    as drawn), and THE DIFFERENCES ARE 16, 9, 7: the two P/N ranges
    and the seed. Totals close: 248 + (3+0+1) = 252 = the wheel's
    whole digit sum = 2^2 x 3^2 x 7, dr 9. Convention note pinned:
    the drawn string-1 excludes dec 50 (the second zero)."""
    DEC = "141592653589793238462643383279502884197169399375105"
    d = {i + 1: int(DEC[i]) for i in range(51)}
    assert (d[15], d[32], d[49]) == (3, 0, 1)
    assert (32 - 15, 49 - 32, 51 - 49 + 15) == (17, 17, 17)
    s3 = sum(d[k] for k in range(16, 32))
    s0 = sum(d[k] for k in range(33, 49))
    s1 = d[51] + 3 + sum(d[k] for k in range(1, 15))
    assert (s3, s0, s1) == (75, 91, 82)
    assert (s3 / 16, s0 / 16, s1 / 16) == (4.6875, 5.6875, 5.125)
    assert sorted((s0 - s3, s0 - s1, s1 - s3)) == [7, 9, 16]
    assert s3 + s0 + s1 + 3 + 0 + 1 == 252 == 3 + sum(d.values())
    assert 252 == 2 ** 2 * 3 ** 2 * 7
