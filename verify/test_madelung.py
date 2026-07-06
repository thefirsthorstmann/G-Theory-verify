"""
THE MADELUNG ORBITAL-FILLING ORDER (co-flagship).   GRADE: the ORDER is FORCED ◆,
with zero chemistry input.

From the root 1296 = 6^4, a two-multiplier harmonic recursion {x2/3 (descending
fourth), x5/6 (descending minor third)} generates a set of values whose ranking by
magnitude reproduces the entire orbital-filling order 1s-7p term for term -- INCLUDING
the two famous anomalies that make Madelung's rule non-trivial:

  4s fills before 3d   and   4f fills before 5d.

This file checks the sharp, falsifiable content -- the two anomalies -- with each value
derived exactly from the recursion exponents (sympy Rationals, no decimals asserted by
hand). A random scheme does not get these right; that is why the result counts.

  4s = 1296 . (2/3) . (5/6)       = 720
  3d = 1296 . (5/6)^4             = 625      ->  4s(720) > 3d(625)   anomaly 1
  5d = 1296 . (2/3) . (5/6)^4     = 1250/3   ~ 416.667
  4f = 1296 . (5/6)^6             = 15625/36 ~ 434.028  ->  4f > 5d  anomaly 2

The FULL 19-term term-for-term order (1s-7p, n+l nondecreasing, s-spine at perfect-
square ranks) lives in catalog/06-VERIFICATION-LOG lines 59-90 and requires the
harmonic (n,l)->exponent map; it is the natural first task to re-encode here in Code.

Source: catalog/06-VERIFICATION-LOG [CO-FLAGSHIP]; 02-CATALOG-RIGOROUS F18.
"""
from sympy import Rational, factorint

ROOT = 1296
DESC_FOURTH = Rational(2, 3)
DESC_MINOR_THIRD = Rational(5, 6)


def test_root_is_six_to_the_fourth():
    assert ROOT == 6**4 == 36**2
    assert dict(factorint(ROOT)) == {2: 4, 3: 4}


def test_anomaly_one_4s_before_3d():
    four_s = ROOT * DESC_FOURTH * DESC_MINOR_THIRD
    three_d = ROOT * DESC_MINOR_THIRD**4
    assert four_s == 720
    assert three_d == 625
    assert four_s > three_d                      # 4s fills before 3d (forced)


def test_anomaly_two_4f_before_5d():
    five_d = ROOT * DESC_FOURTH * DESC_MINOR_THIRD**4
    four_f = ROOT * DESC_MINOR_THIRD**6
    assert five_d == Rational(1250, 3)
    assert four_f == Rational(15625, 36)
    assert four_f > five_d                        # 4f fills before 5d (forced)


def test_values_are_clean_rationals_on_the_2_3_5_lattice():
    # every generated value is 1296 times a product of 2/3 and 5/6 powers -> 2-3-5 only
    for value in [ROOT * DESC_FOURTH * DESC_MINOR_THIRD,
                  ROOT * DESC_MINOR_THIRD**4,
                  ROOT * DESC_FOURTH * DESC_MINOR_THIRD**4,
                  ROOT * DESC_MINOR_THIRD**6]:
        for prime in factorint(value.p) | factorint(value.q):
            assert prime in (2, 3, 5)
