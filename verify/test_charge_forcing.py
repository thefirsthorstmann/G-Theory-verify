"""test_charge_forcing.py — Phase D1+D2 pinned: the charge table forced."""

from fractions import Fraction as F

from charge_forcing import (closure_residual, composites, solve_charges,
                            uniqueness_scan)


def test_the_unique_solution_is_the_observed_table():
    """(C1)-(C4) force q_u = 2/3, q_d = -1/3, q_e = -1, q_nu = 0."""
    q = solve_charges()
    assert q == {"u": F(2, 3), "d": F(-1, 3), "e": F(-1), "nu": F(0)}
    assert closure_residual(q) == 0


def test_the_forced_values_land_on_the_banked_tones():
    """La = 2/3 and Fa = 1/3 (magnitudes): the tones were the reading,
    the closure is the forcing — they agree exactly."""
    q = solve_charges()
    assert q["u"] == F(2, 3) and abs(q["d"]) == F(1, 3)
    assert abs(q["e"]) == 1                       # the unit (Do)


def test_the_composites_are_corollaries():
    """Proton +1, neutron 0, HYDROGEN EXACTLY NEUTRAL — closure, not
    coincidence. And the proton wears the banked net-1/gross-5/3."""
    c = composites(solve_charges())
    assert c["proton"] == 1 and c["neutron"] == 0
    assert c["hydrogen"] == 0
    assert c["proton_gross"] == F(5, 3)           # the same-day anatomy


def test_the_weak_step_is_the_unit_everywhere():
    q = solve_charges()
    assert q["u"] - q["d"] == 1 == q["nu"] - q["e"]


def test_triad_is_the_only_tone_landing_multiplicity():
    """Scan m = 1..12: only m = 3 yields the third-lattice pair
    (2/3, -1/3); every other multiplicity misses the banked tones."""
    scan = uniqueness_scan()
    assert scan[3] == (F(2, 3), F(-1, 3))
    for m, (qu, qd) in scan.items():
        if m != 3:
            assert (qu, qd) != (F(2, 3), F(-1, 3))
            assert qu.denominator != 3 or qd.denominator != 3
