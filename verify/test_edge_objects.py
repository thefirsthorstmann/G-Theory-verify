"""Pins for ZERO AND INFINITY (edge_objects.py)."""

from fractions import Fraction

from edge_objects import (halving_depth, octave_class,
                          cardioid_constancy)


def test_no_infinite_descent_in_Z():
    # halving terminates for every nonzero integer: the floor is a theorem
    for n in list(range(1, 4097)) + [10**12, 3 * 2**40]:
        d = halving_depth(n)
        assert n % 2**d == 0 and (n // 2**d) % 2 == 1
    assert halving_depth(3 * 2**40) == 40


def test_the_root_seats_the_doubling_infinity():
    # the entire two-sided ladder {2^n} is ONE octave class: the root
    for n in range(0, 60):
        assert octave_class(Fraction(2) ** n) == 1
        assert octave_class(Fraction(1, 2) ** n) == 1
    # and no other integer class collapses there
    assert octave_class(Fraction(3)) != 1


def test_the_cardioid_is_the_edge_drawn_in_thirds():
    # the doubling-chord envelope is EXACTLY the cardioid
    # r = (2/3)(1 + cos phi) about the cusp axis point (-1/3, 0):
    # the continuum's image of doubling, parametrized in thirds
    spread, k = cardioid_constancy()
    assert spread < 1e-6
    assert abs(k - 2.0 / 3.0) < 1e-6
