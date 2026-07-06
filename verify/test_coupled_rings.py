"""test_coupled_rings.py — the marker-Englert quadruple, pinned."""

from fractions import Fraction as F

from coupled_rings import c_squared, ledger

# marker configurations (Gaussian-integer vectors on the i-ring)
PARALLEL = ([(1, 0), (1, 0)], [(1, 0), (1, 0)])       # |c|^2 = 1: no marking
ORTHO    = ([(1, 0), (1, 0)], [(1, 0), (-1, 0)])      # |c|^2 = 0: full which-way
HALF     = ([(1, 0), (1, 0)], [(1, 0), (0, 1)])       # |c|^2 = 1/2: partial


def test_marker_overlaps_exact():
    assert c_squared(*PARALLEL) == 1
    assert c_squared(*ORTHO) == 0
    assert c_squared(*HALF) == F(1, 2)


def test_the_quadruple_identity():
    """P^2 + V^2 + C^2 = 1 exactly — every amplitude pair, every marker."""
    for A1 in range(1, 9):
        for A2 in range(1, 9):
            for M1, M2 in (PARALLEL, ORTHO, HALF):
                P2, V2, C2 = ledger(A1, A2, M1, M2)
                assert P2 + V2 + C2 == 1


def test_limits_recover_the_bare_slit():
    """|c| = 1: no entanglement, the triple identity returns (C = 0);
    |c| = 0: full which-way — the wave leg moves wholly into the marker."""
    P2, V2, C2 = ledger(2, 1, *PARALLEL)
    assert (P2, V2, C2) == (F(9, 25), F(16, 25), 0)    # the (3,4,5) again
    P2, V2, C2 = ledger(2, 1, *ORTHO)
    assert (P2, V2, C2) == (F(9, 25), 0, F(16, 25))    # fringe -> entanglement
    assert V2 == 0                                      # screen flat


def test_partial_marking_splits_the_wave_leg():
    """|c|^2 = 1/2 on equal slits: the wave leg splits evenly between
    visible fringe and stored coherence — Englert's tradeoff, exact."""
    P2, V2, C2 = ledger(1, 1, *HALF)
    assert (P2, V2, C2) == (0, F(1, 2), F(1, 2))


def test_englert_inequality_holds_with_slack_only_via_P():
    """V^2 + D^2 <= 1 with D^2 = P^2 + C^2 (distinguishability =
    predictability + marker information): equality for pure states."""
    for A1, A2 in ((1, 1), (2, 1), (3, 2), (5, 1)):
        for M1, M2 in (PARALLEL, ORTHO, HALF):
            P2, V2, C2 = ledger(A1, A2, M1, M2)
            D2 = P2 + C2
            assert V2 + D2 == 1                        # pure case: saturated
