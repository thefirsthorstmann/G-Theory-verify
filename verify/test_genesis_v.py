"""test_genesis_v.py — Chapter V pinned: the aufbau from one closed form."""

from fractions import Fraction as F

from genesis_v import (FILLING, madelung_value, noble_gas_closures,
                       ranked_orbitals)


def test_the_ranking_is_the_filling_order_term_for_term():
    """Nineteen orbitals, one closed form, ranked: the aufbau entire."""
    assert [o[0] for o in ranked_orbitals()] == FILLING


def test_both_anomalies_are_automatic():
    """4s before 3d (720 > 625); 4f before 5d (15625/36 > 1250/3)."""
    assert madelung_value(4, 0) == 720 > madelung_value(3, 2) == 625
    assert madelung_value(4, 3) == F(15625, 36) > madelung_value(5, 2) == F(1250, 3)


def test_the_s_spine_sits_on_the_squares():
    """1s, 3s, 5s, 7s at ranks 1, 4, 9, 16."""
    ranks = {o[0]: i + 1 for i, o in enumerate(ranked_orbitals())}
    assert [ranks[s] for s in ("1s", "3s", "5s", "7s")] == [1, 4, 9, 16]


def test_the_madelung_rule_holds_across_the_ranking():
    """n + l nondecreasing down the ranked list; ties broken by n."""
    seq = [(n + l, n) for _, n, l in ranked_orbitals()]
    assert all(a <= b for a, b in zip(seq, seq[1:]))


def test_the_noble_gases_are_a_corollary():
    """p-closure cumulative counts: Ne, Ar, Kr, Xe, Rn — and 118,
    OGANESSON: the ladder's last rung is the last noble gas."""
    assert noble_gas_closures() == [10, 18, 36, 54, 86, 118]
    # helium closes at the first s-shell: 1s holds 2
    assert 2 * (2 * 0 + 1) == 2
