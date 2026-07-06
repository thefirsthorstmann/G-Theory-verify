"""test_rg_octave.py — Phase B1 pinned: the framework thirds and the tick."""

import math
from fractions import Fraction as F

from rg_octave import (GAUGE_PER_CASIMIR, MATTER_THIRDS, TWO_LOOP_SPINE, b0,
                       octaves, run_alpha_inv)


def test_the_forced_coefficients_are_framework_numbers():
    assert GAUGE_PER_CASIMIR == F(11, 3)          # charge-thread / vector
    assert TWO_LOOP_SPINE == F(34, 3) == F(2 * 17, 3)   # the spine on loop 2
    assert MATTER_THIRDS == (F(4, 3), F(2, 3), F(1, 3))  # the triad-thirds
    assert b0(3, 5) == F(23, 3) and b0(3, 6) == 7  # QCD values, exact


def test_gauge_part_at_three_colors_is_eleven():
    """11/3 per Casimir x C_A = 3 -> the bare 11: the charge thread."""
    assert GAUGE_PER_CASIMIR * 3 == 11


def test_one_octave_step_is_the_tick():
    """Delta(alpha^-1) for one octave = b0 ln2 / 2pi — one tick's share."""
    step = run_alpha_inv(0.0, 1.0, F(23, 3))
    assert abs(step - float(F(23, 3)) * math.log(2) / (2 * math.pi)) < 1e-15


def test_ballpark_run_MZ_to_tau():
    """Comparison layer (floats, marked): alpha_s(M_Z) = 0.1179 run DOWN
    ~5.7 octaves at one loop lands in the PDG ballpark at m_tau."""
    n = octaves(1.77686, 91.1876)                 # ~5.68 octaves
    a_inv_tau = run_alpha_inv(1 / 0.1179, -n, b0(3, 5))
    a_tau = 1 / a_inv_tau
    assert 0.24 < a_tau < 0.36                    # PDG ~0.31-0.33: ballpark ✓
