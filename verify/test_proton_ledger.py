"""test_proton_ledger.py — CC's five-thirds catch pinned exact."""

from fractions import Fraction as F

from proton_ledger import (charge_ledger, ledger, moments, proton_terms,
                           straight_twenty)


def test_wavefunction_norm_is_18():
    assert sum(c * c for c in proton_terms().values()) == 18


def test_the_spin_ledger_five_thirds_netting_to_one():
    """CC's sentence, exact: net 1, gross 5/3; g_A = the gross."""
    L = ledger()
    assert L["du"] == F(4, 3) and L["dd"] == F(-1, 3)
    assert L["net"] == 1                      # 'doubles back to 1'
    assert L["gross"] == F(5, 3)              # 'five total units of 1/3'
    assert L["g_A"] == F(5, 3) == L["gross"]  # signs oppose: measured = gross


def test_charge_wears_the_same_anatomy():
    """CC's 2005 genesis triangle: 2/3 + 2/3 - 1/3."""
    C = charge_ledger()
    assert C["net"] == 1 and C["gross"] == F(5, 3)


def test_moments_ride_the_same_weights():
    """(4 mu_u - mu_d)/3: mu_p = 1, mu_n = -2/3, ratio -3/2 (SU(6))."""
    M = moments()
    assert M["mu_p"] == 1 and M["mu_n"] == F(-2, 3)
    assert M["ratio"] == F(-3, 2)


def test_la_duality_identity():
    """Interval La = the unit + positional La; the drop is one turn."""
    assert F(5, 3) == 1 + F(2, 3)
    assert F(5, 3) * 360 == 600 == 360 + 240  # lands on La's 240


def test_the_straight_twenty():
    """La = 20 exact on the 12->24 octave; both readings at once."""
    T = straight_twenty()
    assert T["la"] == 20 == 4 * 5 == 2 ** 2 * (3 ** 2 - 2 ** 2)
    assert 20 == 8 + 7 + 5                      # the banked heavy half
    assert sorted(int(v) for v in T["integers"].values()) == \
        [12, 15, 16, 18, 20, 24]
    assert set(T["non_integers"]) == {"Re", "Ti"}   # the comma-carriers
    assert T["split"] == (8, 4)                 # ring | half-ring
    assert T["position"] == F(2, 3)             # positional La, linearly
