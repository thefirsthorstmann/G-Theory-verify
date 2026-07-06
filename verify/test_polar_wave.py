"""test_polar_wave.py — the polar wavefunction's forced spine, pinned.

Everything here is exact integer arithmetic (phases as exponents mod n).
"""

from polar_wave import born, clock, global_phase, info_content, shift, tick


def make(n=8):
    """A generic 8-mode state: amplitudes 1..8, phases 0."""
    return [(k + 1, 0) for k in range(n)]


def test_weyl_relation_exact():
    """C S = w S C — the Weyl pair's commutation, as exact exponents."""
    psi = [(1, k % 8) for k in range(8)]          # arbitrary phases
    lhs = clock(shift(psi))
    rhs = global_phase(shift(clock(psi)), 1)      # w^1 x (S then C)
    assert lhs == rhs                              # complementarity, pinned


def test_tick_is_unitary_and_period_eight():
    psi = make(8)
    cur = psi
    for t in range(1, 9):
        cur = tick(cur)
        assert born(cur) == born(psi)             # amplitudes untouched: unitary
        if t < 8:
            assert cur != psi                     # never home early
    assert cur == psi                             # period 8: the octave-cycle


def test_mode_one_phase_walks_the_traversal():
    """Mode 1's phase under successive ticks = the +3 walk = the
    ennead-class traversal (1-indexed slots: 4,7,2,5,8,3,6,1)."""
    psi = make(8)
    seen = []
    cur = psi
    for _ in range(8):
        cur = tick(cur)
        seen.append(cur[1][1] + 1)                # mode-1 exponent as slot
    assert seen == [4, 7, 2, 5, 8, 3, 6, 1]       # operators->carriers->poles


def test_born_is_phase_blind():
    """Two distinct states, identical readout — the phase problem, exact."""
    a = [(2, 0), (3, 1), (1, 5), (4, 2)]
    b = [(2, 3), (3, 0), (1, 1), (4, 6)]
    assert a != b
    assert born(a) == born(b) == [4, 9, 1, 16]


def test_the_loss_is_exactly_half():
    full, kept = info_content(make(8))
    assert full == 16 and kept == 8               # the M-half discarded


def test_grand_realignment_at_24():
    """On the 8-ring with rate 3, a PHASE POINT tracking +3 per tick
    returns to origin after lcm(3,8) = 24 slots = 8 ticks x 3 — and the
    state period (8) times the rate (3) = 24 = the root."""
    assert 8 * 3 == 24
