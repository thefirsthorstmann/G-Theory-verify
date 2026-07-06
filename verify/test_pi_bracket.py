"""
THE PI BRACKET.   GRADE: the bracket and the midpoint identity are FORCED ◆ (exact
rationals);  the ~47 ppm closeness to pi is the reading.

The framework brackets pi between two 2-3-clean rationals and reads its rest value as
the exact midpoint:

  201/64  <  pi  <  22/7
  rest-pi = (201/64 + 22/7) / 2 = 2815/896 ~ 3.1417411,   about 47 ppm above pi.

Both the bracket and the midpoint identity 2815/896 = mean(201/64, 22/7) are exact
arithmetic. pi itself, being a fact about the circle, is bracketed and approached,
never seated.

Source: catalog/03-GENESIS-INDEX (rest-pi = 2815/896 = avg(22/7, 201/64));
THE-FULL-POSITION-INTERNAL §18 (pi as the Archimedes midpoint).
"""
import math
from fractions import Fraction


def test_bracket_holds():
    lo, hi = Fraction(201, 64), Fraction(22, 7)
    assert lo < math.pi < hi
    assert float(lo) == 3.140625


def test_rest_pi_is_the_exact_midpoint():
    lo, hi = Fraction(201, 64), Fraction(22, 7)
    rest_pi = (lo + hi) / 2
    assert rest_pi == Fraction(2815, 896)        # exact identity, no rounding


def test_rest_pi_is_about_47_ppm_from_pi():
    rest_pi = Fraction(2815, 896)
    ppm = abs(float(rest_pi) - math.pi) / math.pi * 1e6
    assert 45 < ppm < 50
