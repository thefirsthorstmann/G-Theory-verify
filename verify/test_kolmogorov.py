"""test_kolmogorov.py — Phase C1 pinned: the -5/3 mechanism.

The banked bar (journal, GAUNTLET/SIX-OBJECTS): '5/3 = La major sixth
ratio-match needs a MECHANISM'. The mechanism pinned here: the cascade
rate and the spectrum are dimensional 2-3 MIRRORS, and closure over the
mirror forces the pair (2/3, -5/3) — both exponents seed arithmetic.
"""

from fractions import Fraction as F

from kolmogorov import (bend_17_10, dimensional_mirror, four_fifths,
                        gap_family, la_duality, octave_cascade_slope,
                        sl_gamma, sl_slope, sl_zeta3, solve_closure,
                        square_gap_identity)


def test_closure_forces_the_pair():
    """T: 3a = 2 (the incommensurability equation); L: 2a - b = 3."""
    a, b = solve_closure()
    assert a == F(2, 3) and b == F(-5, 3)
    assert 3 * a == 2 and 2 * a - b == 3        # the system, verified back


def test_square_gap_identity_and_family():
    """-5/3 = (2^2 - 3^2)/3; the five joins the seed-gap family."""
    assert solve_closure()[1] == square_gap_identity() == F(2**2 - 3**2, 3)
    assert gap_family() == (1, 5, 13, 17)       # 3^2-2^3, 3^2-2^2, 2^8-3^5, 3^4-2^6


def test_the_dimensional_mirror():
    """[eps] = (2,-3), [E(k)] = (3,-2) — mirrors; b = the cross-determinant."""
    eps, spec, b = dimensional_mirror()
    assert eps == (2, -3) and spec == (3, -2)
    assert (spec[0], abs(spec[1])) == (abs(eps[1]), eps[0])  # L<->T swapped
    assert b == F(-5, 3) == solve_closure()[1]


def test_octave_cascade_reproduces_the_pair():
    """Constant flux per rung (workless face) -> the same exponents."""
    assert octave_cascade_slope() == (F(2, 3), F(-5, 3))


def test_la_duality_is_the_solution_pair():
    """Positional La 2/3 and interval La 5/3 = the two forced exponents."""
    assert la_duality() == (F(2, 3), F(5, 3))


def test_four_fifths_is_the_square_over_the_gap():
    """The only exact law's coefficient: 4/5 = 2^2/(3^2-2^2)."""
    plain, framed = four_fifths()
    assert plain == framed == F(4, 5)


def test_sl_gamma_forced_to_the_ennead_ninth():
    """SL94's linear coefficient: forced by zeta_3 = 1 to exactly 1/9."""
    assert sl_gamma() == F(1, 9)
    assert sl_zeta3() == 1                       # the anchor holds exactly


def test_the_dress_lands_in_the_measured_band():
    """Float comparison layer (marked): SL-dressed slope ~ -1.696 and the
    banked 51/50 bend = exactly -17/10; measured ~ -1.70."""
    assert -1.71 < sl_slope() < -1.69
    assert bend_17_10() == F(17, 10)             # the spine over the base
    assert sl_slope() < -5 / 3 < 0               # the dress STEEPENS (falling side)
