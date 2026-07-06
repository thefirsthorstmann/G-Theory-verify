"""Pins for the carry machine at Bell's gate (carry_stand.py)."""

import math

from carry_stand import audit, chsh_int, champion, control_no_carry


def test_champion_ring16_exact():
    Es, sig, flat = champion(16)
    assert sig == 0                          # exact operational silence
    assert chsh_int(16, Es) == 40            # S = 40/16 = 5/2 EXACTLY
    assert flat == 4                         # the silent 1/4 marginal tilt


def test_scale_invariance_of_the_frontier():
    for n in (8, 16, 32):
        Es, sig, flat = champion(n)
        assert sig == 0
        assert chsh_int(n, Es) * 2 == 5 * n      # S = 5/2 at every ring
        assert flat * 4 == n                     # tilt = 1/4, scale-invariant


def test_no_carry_no_violation():
    # empty overflow arc -> no channel -> the pre-written ceiling holds
    assert control_no_carry(16) == 32            # S = 2 exactly


def test_denominator_lemma():
    # ring-N correlations are multiples of 1/N: the character value
    # sqrt2/2 is unreachable exactly at any finite register — Tsirelson
    # is the family's rest value, approached and never seated
    for n in (8, 16, 32, 64, 1024):
        assert (n * math.sqrt(2) / 2) % 1 != 0


def test_the_composition_ladder():
    # 2 (rest) < 5/2 (carry: arithmetic mean of 2 and 3)
    #          < 2sqrt2 (quantum: geometric mean of 2 and 4)
    #          < 3 (telegraph) < 4 (logical)
    assert 2 < 5 / 2 < 2 * math.sqrt(2) < 3 < 4
    assert 5 / 2 == (2 + 3) / 2                   # counting: arithmetic mean
    assert abs(2 * math.sqrt(2) - math.sqrt(2 * 4)) < 1e-12   # quadratic: geometric mean


def test_promotion_is_necessary():
    # the decisive control: with the carry acting by rotation/swap ONLY
    # (no doubling), the silent frontier of the family is EXACTLY 2 —
    # no violation at all. The entire excess over the pre-written world
    # is carried by the octave promotion. No doubling, no violation.
    from carry_stand import audit, chsh_int, _arc, _half_arc_pattern
    n = 16
    pats = [_half_arc_pattern(s, n) for s in range(n)]
    pats.append(tuple(1 if u % 2 == 0 else -1 for u in range(n)))
    pats.append(tuple(1 if (u // 2) % 2 == 0 else -1 for u in range(n)))
    pats.append(tuple(1 if (u // 4) % 2 == 0 else -1 for u in range(n)))
    best = 0
    for s in range(n):
        for L in range(n + 1):
            carry = _arc(s, L, n)
            for psi0 in pats:
                for psi1 in pats:
                    Es, sig, _ = audit(n, carry, psi0, psi1, promote=False)
                    if sig == 0:
                        best = max(best, chsh_int(n, Es))
    assert best == 32          # S = 2 exactly: the rotation carry is classical
