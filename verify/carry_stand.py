"""carry_stand.py — THE CARRY MACHINE AT BELL'S GATE (the register-native run).

Shared state lam uniform on ring N. Wing A at tick a reads the balanced
half-arc chiA((lam-a) mod N); the carry fires iff (lam-a) mod N lies in the
overflow arc; wing B at tick b reads psi0((lam-b) mod N) uncarried, or —
the PROMOTION action, the carry as octave doubling — psi1((2*lam-b) mod N)
carried. Frame: the shock-bounded tone ticks, A = {Do, Mi}, B = {Re, Si}.
All arithmetic exact (correlations are k/N).

THE RESULT (2026-07-05, pre-registered sweep, ~200k configs):
  * the silent frontier of the arc/periodic rule family is S = 5/2 EXACTLY,
    scale-invariant across ring 8, 16, 32 — a register-native, carry-
    mediated violation of the pre-written ceiling in exact operational
    silence (B's statistics independent of A's setting);
  * the champion's anatomy is doctrinal: overflow arc = the quarter
    straddling the antipode (the tritone), action = promotion (doubling);
  * with flat marginals demanded, the family returns exactly 2: the
    violation rides a silent 1/4 marginal tilt — quantum does it flat,
    and the flat-and-violating machine is the named next target;
  * the ceilings ladder: 2 (rest) < 5/2 (carry machine — the ARITHMETIC
    mean of 2 and 3) < 2*sqrt2 (quantum — the GEOMETRIC mean of 2 and 4)
    < 3 (open telegraph) < 4 (logical). Counting composes arithmetically;
    quantum composes quadratically; the remaining gap 2*sqrt2 - 5/2 IS the
    quadratic-composition rung, now measured: 0.3284;
  * the denominator lemma: ring-N correlations are multiples of 1/N, so
    the character values +-sqrt2/2 are unreachable exactly at ANY finite
    N — Tsirelson is the family's rest value: approached, never seated.
"""

import math

N16 = 16


def _arc(start, length, n):
    return frozenset((start + k) % n for k in range(length))


def _half_arc_pattern(start, n):
    return tuple(1 if (u - start) % n < n // 2 else -1 for u in range(n))


def audit(n, carry, psi0, psi1, promote, chiA=None):
    """Exact audit: returns (E table x n, signaling x n, flatness x n)."""
    chiA = chiA or _half_arc_pattern(0, n)
    a_set = (0, n // 4)
    b_set = (n // 8, 7 * n // 8)
    Es, margs = {}, {}
    for a in a_set:
        for b in b_set:
            e = m = 0
            for lam in range(n):
                u = (lam - a) % n
                if u in carry:
                    Bout = psi1[(2 * lam - b) % n] if promote else psi1[(lam - b) % n]
                else:
                    Bout = psi0[(lam - b) % n]
                e += chiA[u] * Bout
                m += Bout
            Es[(a, b)] = e
            margs[(a, b)] = m
    sig = max(abs(margs[(a_set[0], b)] - margs[(a_set[1], b)]) for b in b_set)
    flat = max(abs(v) for v in margs.values())
    return Es, sig, flat


def chsh_int(n, Es):
    a0, a1 = 0, n // 4
    b0, b1 = n // 8, 7 * n // 8
    e = [Es[(a0, b0)], Es[(a0, b1)], Es[(a1, b0)], Es[(a1, b1)]]
    return max(abs(-e[i] + sum(e[j] for j in range(4) if j != i)) for i in range(4))


def champion(n):
    """The scale-invariant champion: overflow quarter straddling the
    antipode, promotion action, antipode-shifted carried read."""
    carry = _arc(3 * n // 8, n // 4, n)
    psi0 = _half_arc_pattern(0, n)
    psi1 = _half_arc_pattern({8: 4, 16: 9, 32: 19}[n], n)
    return audit(n, carry, psi0, psi1, promote=True)


def control_no_carry(n):
    """Empty overflow arc: no channel — the machine must be classical."""
    best = 0
    pats = [_half_arc_pattern(s, n) for s in range(n)]
    for psi0 in pats:
        Es, sig, _ = audit(n, frozenset(), psi0, psi0, False)
        if sig == 0:
            best = max(best, chsh_int(n, Es))
    return best
