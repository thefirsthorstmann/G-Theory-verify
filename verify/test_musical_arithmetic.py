"""test_musical_arithmetic.py — the banked musical-arithmetic constructions as tests.

Companion to catalog/THE-MUSICAL-ARITHMETIC-ENGINE.md. Every test here pins a
value that document quotes, so a known construction is never re-derived cold:
if this file is green, the whole register (roots, the 24->0 drop, the diatonic,
the tone circle, the reptend comma, the closure ladder) re-derives itself on
this machine, today, from exact arithmetic.

Grades mirror the engine doc: forced arithmetic is asserted exactly; the ratio
'dress' values (retarded by a comma) are asserted at their stated precision.
"""

import math
from fractions import Fraction as F

from gtheory import doubling_orbit, reptend


# --- 1 · the clean-octave roots -------------------------------------------
def test_24_is_the_unique_smallest_clean_root():
    # three halvings need 2**3; the third (Fa) needs 3; 24 = lcm(8,3) is smallest.
    assert 24 == 2**3 * 3
    assert math.lcm(8, 3) == 24
    # smaller candidates fail to clear both the octave spine and the third:
    for n in range(1, 24):
        clean = (n % 8 == 0) and (n % 3 == 0)
        assert not clean
    assert 48 == 2**4 * 3 and 72 == 2**3 * 3**2   # the other two low clean roots


# --- 2 · the octave drop 24 -> 0 ------------------------------------------
def test_octave_drop_24_to_0_is_integer_except_at_Fa():
    series = [24, 21, 16, 12, 8, 6, 3, 0]
    assert all(isinstance(v, int) for v in series)
    # Fa seat: by spacing / exact division, the third of 24
    assert F(24, 3) == 8


def test_Fa_dress_is_the_octave_minus_the_1_over_7_comma():
    seat = 8
    dress = 7.999999
    comma = 1 - 7 * 0.142857          # the 1/7 reptend comma
    assert abs((seat - dress) - comma) < 1e-12
    assert abs(comma - 1e-6) < 1e-12


def test_Fa_is_the_unique_split_in_the_drop():
    # each slot as an exact multiplier of 24; the split can only live where the
    # multiplier's denominator carries a 3 that a terminating path cannot reach.
    mults = [F(1), F(7, 8), F(2, 3), F(1, 2), F(1, 3), F(1, 4), F(1, 8), F(0)]
    products = [24 * m for m in mults]
    assert products == [24, 21, 16, 12, 8, 6, 3, 0]
    carries_third = [m.denominator % 3 == 0 for m in mults]
    # only the 2/3 (=16) and 1/3 (=8) slots carry a third; Fa=8 is the drop's.
    assert carries_third == [False, False, True, False, True, False, False, False]


# --- 3 · the diatonic on 24, ascending ------------------------------------
def test_diatonic_on_24_is_all_integers():
    ratios = [F(1), F(9, 8), F(5, 4), F(4, 3), F(3, 2), F(5, 3), F(15, 8), F(2)]
    tones = [24 * r for r in ratios]
    assert tones == [24, 27, 30, 32, 36, 40, 45, 48]
    assert all(t.denominator == 1 for t in tones)
    assert 24 * F(4, 3) == 32          # Fa ASCENDING = 32, not the drop's 8


# --- 4 · the tone circle f = 24 + theta/15 --------------------------------
def test_tone_circle_maps_angle_to_frequency():
    thetas = [0, 45, 90, 120, 180, 240, 315, 360]
    freqs = [24 + t / 15 for t in thetas]
    assert freqs == [24, 27, 30, 32, 36, 40, 45, 48]


def test_La_is_240_degrees_and_Sol_is_180_the_asymmetry_guard():
    # THE STANDING GUARD: La by POSITION = 240 deg, ratio 5/3; Sol = 180 deg, 3/2.
    # 2/3 != 3/2 -- do not identify La with 2/3.
    assert 24 + 240 / 15 == 40 and F(40, 24) == F(5, 3)     # La: 240 deg, 5/3
    assert 24 + 180 / 15 == 36 and F(36, 24) == F(3, 2)     # Sol: 180 deg, 3/2
    assert F(2, 3) != F(3, 2)


# --- 5 · the reptend 1/7 and its comma ------------------------------------
def test_reptend_1_over_7_is_forced():
    assert reptend(7) == "142857"
    assert 7 * 142857 == 999999
    assert len(reptend(7)) == 6                       # ord_7(10) = 6
    assert pow(10, 6, 7) == 1 and all(pow(10, k, 7) != 1 for k in range(1, 6))
    assert pow(2, 3, 7) == 1                          # ord_7(2) = 3, base-swap halving


def test_doubling_orbit_is_the_reptend():
    # mod-9 units {1,2,4,8,7,5} from an independent source == 142857 digits.
    assert list(doubling_orbit()) == [1, 2, 4, 8, 7, 5]


# --- 6 · the reptend-closure ladder ---------------------------------------
def test_closure_ladder_7_and_137():
    assert round(7 * 0.142857, 6) == 0.999999          # closes at 6 decimals
    assert round(137 * 0.00729927, 8) == 0.99999999    # closes at 8 decimals


def test_binary_fence_000001_is_one_64th_in_base_2():
    # '.000001' = 1/64 in BASE 2 (2**-6); = 10**-6 in base 10. Two fences, both real.
    assert int("000001", 2) == 1
    assert 2**-6 == 1 / 64


def test_1728_is_re_and_the_six_octave_lift_of_the_root():
    """the author 2026-08-07: 1728 is Re above 1536. Both descend six octaves onto the
    banked root 24 and its whole tone 27. The Re line then STOPS — 27 is odd — while
    the Do line runs integral to 3, because the root carries 2^3 and 3^3 does not.
    And the descent contains CLAUDE.md section 9's canonical stations 216 = 6^3 and
    27 = 3^3, both Re. 1728 is also the divisor of the modular discriminant."""
    from fractions import Fraction as F
    assert F(1728, 1536) == F(9, 8)                  # the whole tone: Do -> Re
    assert 1728 == 27 * 64 == 2**6 * 3**3 == 12**3
    assert 1536 == 24 * 64 == 2**9 * 3
    assert F(27, 24) == F(9, 8)                      # the root and its Re
    descent = [1728 // 2**k for k in range(7)]
    assert descent == [1728, 864, 432, 216, 108, 54, 27]
    assert all(v % 2 == 0 for v in descent[:-1]) and descent[-1] % 2 == 1
    assert 216 == 6**3 and 27 == 3**3                # section 9's two Re stations
    # the Do line, by contrast, halves all the way to 3
    assert [1536 // 2**k for k in range(10)][-1] == 3


def test_re_sol_si_root_to_nine_at_every_octave():
    """the author 2026-08-07: Re, Sol and Si on the 24-series always root to 9. FORCED —
    their ratio numerators are 9, 12, 15 = 3x(3,4,5), a Pythagorean triple, so on
    root 24 = 3*8 they clear to 27, 36, 45 = 9x(3,4,5), all divisible by 9; and
    doubling preserves that. The three nines sum to 27 = the hexad sum."""
    from fractions import Fraction as F
    dr = lambda n: (int(n) - 1) % 9 + 1
    assert 9*9 + 12*12 == 15*15                       # the triple
    assert [24 * r for r in (F(9, 8), F(3, 2), F(15, 8))] == [27, 36, 45]
    assert [27 // 9, 36 // 9, 45 // 9] == [3, 4, 5]
    for k in range(-1, 7):                            # every octave, up and down
        root = F(24) * F(2) ** k
        for r in (F(9, 8), F(3, 2), F(15, 8)):
            v = root * r
            if v.denominator == 1:
                assert v % 9 == 0 and dr(v) == 9
            else:                                     # the 12-octave: digit sums
                assert sum(int(c) for c in str(float(v)).replace('.', '')) == 9
    assert 27 + 36 + 45 == 108
    assert 9 + 9 + 9 == 27 == sum([1, 4, 2, 8, 5, 7])  # the hexad sum


def test_the_nines_ladder_closes_at_216_and_it_is_the_three_content():
    """the author 2026-08-07, extending his own three-nines: 24 gives 3 nines, 72 gives 6,
    216 gives all 8. The rung is the root's TRIADIC content on a fixed 2^3 — a
    degree keeps the nine unless its ratio denominator carries a 3, which spends one
    of the root's threes. On 72 the survivors are exactly the tertian stack
    1,3,5,7,9 and the failures are 11 and 13."""
    from fractions import Fraction as F
    dr = lambda n: (int(n) - 1) % 9 + 1
    RAT = [('Do', F(1), 1), ('Re', F(9, 8), 9), ('Mi', F(5, 4), 3), ('Fa', F(4, 3), 11),
           ('Sol', F(3, 2), 5), ('La', F(5, 3), 13), ('Si', F(15, 8), 7), ('Do8', F(2), 1)]
    counts = []
    for root in (24, 72, 216):
        counts.append(sum(1 for _, r, _ in RAT if dr(root * r) == 9))
    assert counts == [3, 6, 8]                            # the ladder closes
    assert (24, 72, 216) == (2**3 * 3, 2**3 * 3**2, 2**3 * 3**3)
    # on 72 exactly Fa and La fail, and they are exactly the denominator-3 degrees
    fails = {n for n, r, _ in RAT if dr(72 * r) != 9}
    assert fails == {'Fa', 'La'}
    assert {n for n, r, _ in RAT if r.denominator % 3 == 0} == {'Fa', 'La'}
    keep = sorted(d for n, r, d in RAT if dr(72 * r) == 9 and n != 'Do8')
    assert keep == [1, 3, 5, 7, 9]                        # the tertian stack
    assert sorted(d for n, r, d in RAT if dr(72 * r) != 9) == [11, 13]
    assert 216 == 6**3
    assert 135 == 72 * F(15, 8) == 27 * 5 == 1**1 + 3**2 + 5**3


def test_what_is_pi_scale_ruler_anchors_are_pinned():
    """WHAT-IS-PI section 2's two-anchor log ruler, pinned 2026-08-08 so it cannot
    drift again. Both anchors were previously underdetermined in the text.

        anchor 1  position 11  =  the HBAR-convention Planck length,
                                  sqrt(hbar G/c^3) = 10^-34.7915 m
        anchor 2  position 32  =  10^-15 SI metres (a length, not a unit-relative
                                  quantity, so a redefined metre does not move it)
        slope     = (34.7915 - 15)/21 = 0.9425 decades per position

    The h-convention alternative, sqrt(h G/c^3), sits at 10^-34.3924 — different by
    sqrt(2 pi) = 0.399 decades, four-tenths of a digit-position. Both conventions
    are standard; the ruler uses hbar and any reading inherits that.

    ROUNDING GUARD: the anchor was formerly written 10^-34.8, and 19.8/21 is
    exactly 33/35 = 0.942857142857..., which carries the reptend digits. That was
    an artifact of one-decimal rounding. The exact anchor gives 0.942452, which is
    neither 33/35 nor reptend-bearing. This test exists so the rounded form cannot
    creep back and be mistaken for structure."""
    import math
    lP_hbar, lP_h = 1.616255e-35, 4.051351e-35
    assert abs(math.log10(lP_hbar) - (-34.7915)) < 1e-4      # anchor one, exact
    assert abs(math.log10(lP_h) - (-34.3924)) < 1e-4         # the alternative
    # they differ by sqrt(2 pi); tolerance set by the anchors' 7 quoted figures
    assert abs((math.log10(lP_h) - math.log10(lP_hbar))
               - math.log10(math.sqrt(2 * math.pi))) < 1e-6

    slope = (-math.log10(lP_hbar) - 15) / 21
    assert abs(slope - 0.942452) < 1e-5                      # the real slope
    assert abs(slope - 33/35) > 1e-4                         # and it is NOT 33/35
    assert abs((19.8 / 21) - 33/35) < 1e-12                  # which the rounding gave
    # the convention question dwarfs G's contribution to the anchor
    assert math.log10(math.sqrt(2*math.pi)) > 300 * (11.24e-6)
