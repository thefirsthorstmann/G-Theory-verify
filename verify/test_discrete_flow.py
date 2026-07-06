"""Pins for THE DISCRETE FLOW CALCULUS (discrete_flow.py)."""

from fractions import Fraction

from discrete_flow import (forced_weights, viscosity, rank4_isotropic,
                           rank3_vanishes, forced_hexad, shear_wave_decay,
                           CRYSTALLOGRAPHIC_ORDERS)


def test_constants_forced_and_23_smooth():
    w = forced_weights()
    assert w["cs2"] == Fraction(1, 3)
    assert (w["w0"], w["w1"], w["w2"]) == (
        Fraction(4, 9), Fraction(1, 9), Fraction(1, 36))
    # normalization and second moment close exactly
    assert w["w0"] + 4 * w["w1"] + 4 * w["w2"] == 1
    assert 2 * w["w1"] + 4 * w["w2"] == w["cs2"]


def test_viscosity_in_thirds():
    assert viscosity(Fraction(4, 5)) == Fraction(1, 10)
    assert viscosity(Fraction(1, 2)) == 0          # the zero-dial floor


def test_each_rival_dies_by_its_own_clause():
    assert not rank3_vanishes(3)                   # triangle: parity
    assert rank3_vanishes(4) and not rank4_isotropic(4)   # square: isotropy
    assert rank3_vanishes(5) and rank4_isotropic(5)       # pentagon: tiling
    assert rank3_vanishes(6) and rank4_isotropic(6)       # six: passes all


def test_hexad_forced():
    # crystallographic restriction = the 2-3 family; unique fit is 6
    assert all(n in (1, 2, 3, 4, 6) for n in CRYSTALLOGRAPHIC_ORDERS)
    assert forced_hexad() == 6


def test_engine_matches_exact_ns_decay():
    amp, exact = shear_wave_decay()
    assert abs(amp / exact - 1) < 2e-3             # measured ~7e-4
