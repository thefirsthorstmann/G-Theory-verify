"""test_stakes.py — Phase E pinned: the dashboard cannot drift."""

from fractions import Fraction as F

from stakes import (AT_RISK, LIVE, PARKED, PYTHAGOREAN_COMMA, RETIRED,
                    RETRODICTIONS)


def test_every_live_stake_is_complete():
    """A live stake without a falsification band, adjudicator and horizon is not
    a bet — it is a mood. None allowed."""
    for s in LIVE:
        assert s["falsification"] and s["adjudicator"] and s["horizon"], s["name"]


def test_every_parked_item_has_a_wake_condition():
    for p in PARKED:
        assert p["wake"], p["name"]


def test_every_retirement_has_a_reason():
    for r in RETIRED:
        assert r["reason"], r["name"]


def test_the_exact_seats_recompute_from_their_constructions():
    """The dashboard's numbers are the engine's numbers."""
    from ew_seats import COS2_SEAT, RIVAL_COS2
    from charge_forcing import solve_charges
    from kolmogorov import bend_17_10
    seats = {s["name"]: s["seat"] for s in LIVE}
    assert seats["PMNS theta23 sin^2"] == F(4, 7)
    assert seats["PMNS theta13 sin^2"] == F(1, 45)
    assert seats["m_W/m_Z seat pair"] == (COS2_SEAT, RIVAL_COS2)
    assert seats["Kolmogorov dress: SL vs bend"] == (bend_17_10(),)
    assert solve_charges()["u"] == F(2, 3)       # the table under it all


def test_the_retrodiction_identities():
    """The settled column's exact anatomy re-verifies."""
    assert 137 == 2 ** 7 + 3 ** 2 == 8 * 17 + 1
    assert 1836 == 2 ** 2 * 3 ** 3 * 17 == 36 * 51
    assert F(2 ** 37, 3 ** 23) == F(3, 2) / PYTHAGOREAN_COMMA ** 2
    assert F(2 ** 9, 3 ** 4 * 7 ** 2) == F(512, 3969)
    assert len(RETRODICTIONS) == 7


def test_the_census():
    """The dashboard's shape, pinned: 7 live, 2 at-risk, 6 parked,
    3 retired. A stake added or dropped must be owned here."""
    assert (len(LIVE), len(AT_RISK), len(PARKED), len(RETIRED)) == (7, 2, 6, 3)
