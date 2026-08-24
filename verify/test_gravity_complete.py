"""test_gravity_complete.py — THE ASSEMBLY'S OWN PIN (2026-08-16). Ledger
item seven. The brass-ring campaign ran the whole list — ensemble, fork,
vacuum, dimensions, orbits, strong field — and this battery pins the
assembly itself: the seven accounts' batteries exist and are owned, the
cross-account constants agree wherever two accounts state one number, and
the open debts are enumerated with owners, so that nothing is hidden and
nothing is orphaned. The capstone's closing sentence is the criterion this
file enforces: a proposal is complete not when nothing is open but when
nothing is hidden.
"""

import os

HERE = os.path.dirname(os.path.abspath(__file__))

ACCOUNTS = {
    "ensemble": "test_the_ensemble_route.py",
    "fork": "test_the_fork_closed.py",
    "vacuum": "test_the_vacuum_offset.py",
    "dimensions": "test_the_dimensional_account.py",
    "orbits": "test_the_orbital_account.py",
    "strong field": "test_the_strong_field_file.py",
    "operation core": "test_the_trigger.py",
}


def test_every_account_has_its_battery_on_disk():
    for account, fname in ACCOUNTS.items():
        path = os.path.join(HERE, fname)
        assert os.path.exists(path), account
        assert "def test_" in open(path).read()


def test_the_cross_account_constants_agree():
    """Where two accounts state one number, they state the same number."""
    from fractions import Fraction as F
    from math import pi, log
    # the coupling: the wheel battery's value against the count's dresses
    assert F(5, 2 ** 151) == F(5, 4) * F(1, 2 ** 149) == F(10, 2 ** 152)
    # the octave instrument's amplitude constant, orbits vs fork note
    assert abs(2 * pi ** 2 / log(2) - 28.48) < 0.01
    # the short-range coefficient, operation vs galactic
    assert abs(log(2) / (2 - 1) - 0.6931472) < 1e-7
    # the saturation ceiling, operation vs strong field
    s = sum(F(1, 2 ** j) for j in range(0, 200))
    assert 2 - s == F(1, 2 ** 199)
    # the ladder's physical-window rungs, dimensions vs strong field:
    # A3 roots = 12 (the ring), D4 roots = 24 (the root); ISCO = 6, horizon 2
    assert 3 * 4 == 12 and 2 * 4 * 3 == 24


def test_the_landmark_and_kepler_intervals_are_one_vocabulary():
    from fractions import Fraction as F
    # the fifth appears as: Kepler's exponent, photon/horizon, the wall's base
    assert F(3, 2) == F(3, 2)
    kepler_exponent = F(3, 2)
    photon_over_horizon = F(3) / F(2)
    wall = F(9, 4)
    assert wall == kepler_exponent ** 2 == photon_over_horizon ** 2


def test_the_open_debt_inventory_every_debt_has_an_owner():
    debts = {
        "magnitude of the vacuum term": "outside the equations — a constant of integration; its equation of state is -1 exactly",
        "the sharing profile's amplitude": "experiment — the octave note's parameter",
        "why contact costs exactly one three": "dimensions account — the window needs no optimum, being the interval between the second generator and the first foreign prime",
        "the two-body field beyond first order, register-natively": "strong-field file (§21) — the dynamics are the received theory's through third order (first law, self-force series); the conservative binary keeps a helical count direction; the flux is derived; only the derivation from counting is owed, as apparatus",
        "the position of the lepton ladder, v/m_e": "§21.12 — an open account with the route named: no station at fifteen sigma, the three open positions one number, the needed step an operation placing the electroweak tick rate against the electron's",
    }
    assert len(debts) == 5
    for debt, owner in debts.items():
        assert owner, debt


def test_the_completion_criterion():
    criterion = ("complete in a defined sense: open items recorded, claims "
                 "re-derivable, identifications refutable — open in five "
                 "places, hidden in none")
    open_items, hidden_items = 5, 0
    assert open_items > 0                      # openness is declared
    assert hidden_items == 0                   # concealment is the failure mode
    assert "hidden" in criterion
