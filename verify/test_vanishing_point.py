"""Pins for THE VANISHING POINT (vanishing_point.py)."""

from fractions import Fraction

from vanishing_point import stage, digital_root, gap_ratio, is_epimoric


def test_the_form_never_varies():
    for n in range(1, 200):
        nines = 10 ** n - 1                  # the numeral 9...9
        assert digital_root(nines) == 9
    assert digital_root(1) == 1              # no stage crosses


def test_the_staircase_of_tones():
    prev = None
    for n in range(1, 60):
        q = gap_ratio(n)
        assert q == Fraction(10 ** n, 10 ** n - 1)
        assert is_epimoric(q)                # every stair superparticular
        assert q > 1                         # never unison
        if prev: assert q < prev             # strictly descending
        prev = q
    assert gap_ratio(1) == Fraction(10, 9)   # the first stair: minor whole tone


def test_the_shifted_tail():
    for n in range(2, 60):
        assert 10 * stage(n) == 9 + stage(n - 1)          # exact, every stage
        assert 10 * stage(n) != 9 + stage(n)              # the folk equation fails
        assert (9 + stage(n)) - 10 * stage(n) == Fraction(9, 10 ** n)  # by the last digit


def test_the_vanishing_point():
    for k in (1, 3, 6, 12):
        tol = Fraction(1, 10 ** k)
        for n in range(k + 1, k + 5):
            assert 1 - stage(n) < tol        # passes every k-precision test 1 passes
            assert stage(n) != 1             # and is not 1, at any stage
