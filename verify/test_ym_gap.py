"""test_ym_gap.py — Phase C2 pinned: the Casimir thirds and the
gap criterion. No magnitude claimed anywhere (Scale Theorem held)."""

from fractions import Fraction as F

from rg_octave import b0
from ym_gap import (T_F, abelian_b0, b0_from_casimirs, casimir_adjoint,
                    casimir_fundamental, casimir_gap, casimir_scaling,
                    flavor_ceiling, landing_scale, octave_budget)


def test_the_casimir_thirds_are_the_tones():
    """C_F(3) = 4/3 Fa; C_A = 3 the vector; T_F = 1/2 the half."""
    assert casimir_fundamental(3) == F(4, 3)
    assert casimir_adjoint(3) == 3
    assert T_F == F(1, 2)


def test_the_casimir_gap_is_la():
    """C_A - C_F = 5/3 for the 3-group — La as the Casimir gap."""
    assert casimir_gap(3) == F(5, 3)
    assert casimir_gap(3) == F(3 ** 2 + 1, 2 * 3)   # (N^2+1)/2N


def test_casimir_scaling_is_sol_squared():
    """C_A/C_F = 9/4 = (3/2)^2 — the measured adjoint/fundamental ratio."""
    assert casimir_scaling(3) == F(9, 4) == F(3, 2) ** 2


def test_the_reciprocal_fa_pair():
    """SU(2) and SU(3) fundamental Casimirs: 3/4 and 4/3, product 1."""
    assert casimir_fundamental(2) == F(3, 4)
    assert casimir_fundamental(2) * casimir_fundamental(3) == 1


def test_gluon_count_is_the_ring():
    """3^2 - 1 = 8 adjoint states (banked: the structural 9 = dim U(3))."""
    assert 3 ** 2 - 1 == 8 and 3 ** 2 == 9


def test_b0_is_the_casimir_algebra():
    """(11/3)C_A - (4/3)T_F n_f reproduces the engine's b0 exactly."""
    for nf in range(0, 17):
        assert b0_from_casimirs(3, nf) == b0(3, nf)
    assert F(4, 3) * T_F == F(2, 3)              # the matter third per flavor


def test_the_flavor_ceiling_is_33_over_2():
    """Asymptotic freedom (the gap side): b0 > 0 <=> n_f < 33/2."""
    assert flavor_ceiling(3) == F(33, 2)
    assert b0(3, 16) > 0 and b0(3, 17) < 0       # straddles the ceiling


def test_the_abelian_side_is_gapless_sign():
    """C_A = 0 kills the 11/3 term: b0 < 0 for any matter — no landing."""
    for nf in range(1, 7):
        assert abelian_b0(nf) < 0


def test_the_octave_budget_is_finite_and_lands():
    """Float layer (marked): alpha_s(M_Z) = 0.1179, b0 = 23/3 ->
    n* ~ 10 octaves; Lambda in the 50-200 MeV ballpark (one-loop)."""
    n_star = octave_budget(1 / 0.1179, b0(3, 5))
    assert 9 < n_star < 11
    lam = landing_scale(91.1876, 1 / 0.1179, b0(3, 5))
    assert 0.05 < lam < 0.2                       # GeV; ruler borrowed
