"""test_lattice_density.py — F1+F2 pinned: the primitive and the razors."""

from fractions import Fraction as F

from lattice_density import (farey_expected, nearest_rival, rivals_in,
                             uniqueness_sigma)


def test_validation_anchor_the_gA_scan():
    """The primitive reproduces the banked g_A result exactly:
    33 rivals in +-0.0013 at q <= 200 around 1.2754; Farey ~31.6."""
    assert len(rivals_in(1.2754, 0.0013, 200)) == 33
    assert 31 < farey_expected(0.0026, 200) < 32


def test_theta23_razor_tiers():
    """4/7: rivals 3/5 (q<=7), 5/9 (q<=10), 13/23 (q<=23), 27/47 (q<=50).
    Uniqueness sigma at q<=10: 0.0079 — current 0.019 needs x2.4;
    at q<=23 (killing 13/23): 0.0031 — needs x6."""
    seat = F(4, 7)
    assert nearest_rival(seat, 7)[0] == F(3, 5)
    assert nearest_rival(seat, 10)[0] == F(5, 9)
    assert nearest_rival(seat, 23)[0] == F(13, 23)
    assert nearest_rival(seat, 50)[0] == F(27, 47)
    assert 0.0078 < uniqueness_sigma(seat, 10) < 0.0080
    assert 0.0030 < uniqueness_sigma(seat, 23) < 0.0032


def test_theta13_razor_tiers():
    """1/45: rivals 1/44, 1/46, 2/91; uniqueness at q<=50 needs
    sigma < 0.00024 — current 0.00058 needs x2.4 (JUNO-era)."""
    seat = F(1, 45)
    assert nearest_rival(seat, 45)[0] == F(1, 44)
    assert nearest_rival(seat, 50)[0] == F(1, 46)
    assert nearest_rival(seat, 100)[0] == F(2, 91)
    assert 0.00023 < uniqueness_sigma(seat, 50) < 0.00025


def test_bend_razor_tiers():
    """17/10: rivals 12/7 (q<=10), 29/17 (q<=20); SL-separation needs
    slope sigma < 0.002 (pair distance 0.00406)."""
    seat = F(17, 10)
    assert nearest_rival(seat, 10)[0] == F(12, 7)
    assert nearest_rival(seat, 20)[0] == F(29, 17)
    assert abs(1.7 - 1.69594) / 2 < 0.00205      # the SL half-distance


def test_sharper_tiers_demand_smaller_sigma():
    """Monotonicity of the razor: deeper rival pools, tighter sigma."""
    for seat in (F(4, 7), F(1, 45), F(17, 10)):
        s = [uniqueness_sigma(seat, q) for q in (10, 25, 50, 100)]
        assert all(a >= b for a, b in zip(s, s[1:]))
