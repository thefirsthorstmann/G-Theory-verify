"""Pins for WATER ON DISCRETE TERMS (water_terms.py)."""

import math
from fractions import Fraction

from water_terms import tetrahedral_cos, ideal_ca_squared, mathieu_growth


def test_the_third_in_the_bond_angle():
    assert tetrahedral_cos() == Fraction(-1, 3)          # exact
    theta = math.degrees(math.acos(-1/3))
    assert abs(theta - 109.4712) < 1e-3


def test_the_same_third_in_the_stacking():
    assert ideal_ca_squared() == Fraction(8, 3)
    assert abs(math.sqrt(8/3) - 1.63299) < 1e-4


def test_water_answers_an_octave_below():
    # principal parametric resonance: drive at 2x natural -> growth
    # (surface answers at HALF the drive); drive at natural -> quiet
    resonant = mathieu_growth(2.0)
    off = mathieu_growth(1.0)
    assert resonant > 10.0                               # explosive growth
    assert off < 4.0                                     # weak secondary only
    assert resonant > off + 10.0                         # clean separation
