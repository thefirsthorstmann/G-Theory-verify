"""test_tick_contact.py — THE TICK-CONTACT THEOREM, pinned.

Named as a candidate pin at THE-THIRD-WAVE-2026-07-26.md:93 and owed since;
re-verified cold by the 2026-08-02 gravity assault (angle A, skeptic-gated
2/2). One tick of the pinned clock (rate 3 on the ring of 8):
  (a) moves EXACTLY the modes k >= 1 — the exists-carrier set; the
      forbidden zero (mode 0) is untouched;
  (b) reads every count injectively — k -> 3k mod 8 is a permutation;
  (c) BOTH properties hold  <=>  gcd(rate, 8) = 1 — the 2-perp-3
      incommensurability is why no existent escapes the clock;
  (d) contact is workless — the Born read is unchanged by a tick.
"""

from math import gcd

from polar_wave import born, tick


def _unit_state(n=8):
    # amplitude 1, phase 0 at every mode
    return [(1, 0) for _ in range(n)]


def test_tick_moves_exactly_the_existents():
    state = _unit_state()
    after = tick(state)
    moved = {k for k, ((_, m0), (_, m1)) in enumerate(zip(state, after)) if m1 != m0}
    assert moved == set(range(1, 8))          # every k >= 1 moves
    assert after[0] == state[0]               # mode 0 untouched


def test_tick_reads_every_count_injectively():
    advances = [(3 * k) % 8 for k in range(8)]
    assert sorted(advances) == list(range(8))  # a permutation: no aliasing


def test_both_properties_iff_rate_coprime():
    for rate in range(1, 8):
        advances = [(rate * k) % 8 for k in range(8)]
        universal = all(a != 0 for a in advances[1:])
        injective = len(set(advances)) == 8
        assert (universal and injective) == (gcd(rate, 8) == 1)


def test_contact_is_workless():
    state = [(a, 0) for a in range(1, 9)]
    assert born(tick(state)) == born(state)
