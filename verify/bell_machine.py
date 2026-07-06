"""bell_machine.py — THE TWO-TOUCH COMPUTATION (the VIII machine at Bell's gate).

The pinned collapse mechanism of Volume VIII — touch at reduced position
p/q, mode m survives iff q | m — run on one shared mode read by two wings,
sequenced by the serial order. Outcomes: +1 = the mode survives my touch,
-1 = it does not (or was already silenced). Mode m uniform; correlations
have exact closed forms in the divisor densities (p_a = 1/q_a,
p_ab = 1/lcm), so every verdict below is a fraction, not an estimate.

THE DICHOTOMY (the result, pre-registered and confirmed):
  * two-ledger control (each wing filters its own copy): CHSH = 2 exactly —
    the machine in its factorized form is Bell-classical, as the theorem
    demands;
  * one string, serial touches: CHSH reaches 19/7 = 2 + 5/7 on the natural
    menu q in {2..7} — but only at settings where wing B's marginal shifts
    by exactly 6/7 with A's choice: the machine violates only by
    telegraphing, which nature refuses (no-signaling);
  * the non-signaling slice of the same machine: CHSH = 2 exactly;
  * serial order hidden (randomized): no-signaling returns, CHSH = 2 exactly.
  VERDICT: the chord reading as pinned does NOT source quantum correlations.
  An honest negative, kept on the record with its arithmetic.

THE DOOR (also machine-checked):
  * pure divisibility filters are diagonal in the mode basis — they all
    commute; the blocks are parallel; no 90 degrees exists in the filter
    machine (this is WHY it is classical);
  * the program's own strike law — no reading is free, the probe injects —
    adds a rank-1 excitation with the hammer profile sin(m*pi*x); touch
    operations then fail to commute, linearly in the strike strength;
  * and the right angle is supplied by the seed itself:
    sin(m*pi/2) is EXACTLY orthogonal to sin(m*pi/3) over full periods —
    the 2-touch and 3-touch strike profiles meet at 90 degrees because
    two-against-three makes them so.
  The owed rung, refined: an outcome rule for the strike-machine that
  converts this real non-commutation into CHSH > 2 WITHOUT signaling
  (formal gate: Fine's theorem — counterfactual joint outcomes must fail
  to coexist; sequential re-preparation is the candidate mechanism).
"""

import itertools
import math
from fractions import Fraction as F


def _lcm(a, b):
    return a * b // math.gcd(a, b)


# ---- exact correlation closed forms (mode m uniform over a full lcm cycle) ----

def E_ledger(qa, qb):
    """Two copies, independent filters: the pre-written two-ledger model."""
    return 1 - 2 * F(1, qa) - 2 * F(1, qb) + 4 * F(1, _lcm(qa, qb))


def E_serial(qa, qb):
    """One mode, A touches first, B touches what remains."""
    return 2 * F(1, _lcm(qa, qb)) - 2 * F(1, qa) + 1


def B_marginal_serial(qa, qb):
    """Wing B's mean outcome — the signaling witness (depends on qa!)."""
    return 2 * F(1, _lcm(qa, qb)) - 1


def E_rand(qa, qb):
    """Serial order hidden: half A-first, half B-first."""
    return 2 * F(1, _lcm(qa, qb)) - F(1, qa) - F(1, qb) + 1


def chsh(E, qa, qa2, qb, qb2):
    return abs(E(qa, qb) - E(qa, qb2) + E(qa2, qb) + E(qa2, qb2))


def max_chsh(E, menu):
    return max((chsh(E, *t), t) for t in itertools.product(menu, repeat=4))


def nonsignaling_max(menu):
    """Max CHSH of the serial machine over quadruples whose B-marginals
    are unmoved by A's setting choice."""
    best = F(0)
    for t in itertools.product(menu, repeat=4):
        qa, qa2, qb, qb2 = t
        if all(B_marginal_serial(qa, q0) == B_marginal_serial(qa2, q0)
               for q0 in (qb, qb2)):
            best = max(best, chsh(E_serial, *t))
    return best


# ---- the commutation diagnosis (the door) ----

N_MODES = 24


def touch_matrix(p, q, eta):
    """Touch at x = p/q on the amplitude space: divisibility filter plus
    the strike law's rank-1 injection with hammer profile sin(m*pi*x)."""
    x = p / q
    v = [math.sin((m + 1) * math.pi * x) for m in range(N_MODES)]
    return [[(1.0 if (i == j and (i + 1) % q == 0) else 0.0) + eta * v[i] * v[j]
             for j in range(N_MODES)] for i in range(N_MODES)]


def comm_norm(P, Q):
    C = [[sum(P[i][k] * Q[k][j] - Q[i][k] * P[k][j] for k in range(N_MODES))
          for j in range(N_MODES)] for i in range(N_MODES)]
    return math.sqrt(sum(C[i][j] ** 2 for i in range(N_MODES) for j in range(N_MODES)))


def strike_profile_overlap(n=N_MODES):
    """The seed's right angle: sin(m*pi/2) . sin(m*pi/3). Exact zero
    precisely when the register closes on the hexad (n = 0 mod 6);
    a broken register leaks sin(pi/3) = sqrt(3)/2 per dangling mode."""
    v = [math.sin((m + 1) * math.pi / 2) for m in range(n)]
    w = [math.sin((m + 1) * math.pi / 3) for m in range(n)]
    return sum(a * b for a, b in zip(v, w))


# ---- the observation audit and the ladder of wings (CC, 2026-07-05) ----

def _kron2(P, Q):
    n, m = len(P), len(Q)
    return [[P[i // m][j // m] * Q[i % m][j % m] for j in range(n * m)]
            for i in range(n * m)]


def _norm_h(P, iters=800):
    n = len(P)
    v = [complex(1, 0.1 * k) for k in range(n)]
    m = 0.0
    for _ in range(iters):
        w = [sum(P[i][j] * v[j] for j in range(n)) for i in range(n)]
        m = math.sqrt(sum(abs(x) ** 2 for x in w))
        v = [x / m for x in w]
    return m


def mermin3_ceilings():
    """Three wings: the pre-written (rest) ceiling by enumeration, and the
    physical ceiling as the Mermin operator norm  M = XXX - XYY - YXY - YYX."""
    X = [[0, 1], [1, 0]]
    Y = [[0, -1j], [1j, 0]]
    k3 = lambda A, B, C: _kron2(_kron2(A, B), C)
    sub = lambda P, Q: [[P[i][j] - Q[i][j] for j in range(len(P))]
                        for i in range(len(P))]
    M = sub(sub(sub(k3(X, X, X), k3(X, Y, Y)), k3(Y, X, Y)), k3(Y, Y, X))
    rest = max(abs(a * b * c - a * b2 * c2 - a2 * b * c2 - a2 * b2 * c)
               for a in (1, -1) for a2 in (1, -1) for b in (1, -1)
               for b2 in (1, -1) for c in (1, -1) for c2 in (1, -1))
    return rest, _norm_h(M)


def sharpness_threshold():
    """Soften the strike: unsharp readings of sharpness eta scale the
    correlations by eta^2, so S(eta) = eta^2 * 2*sqrt(2); the violation
    vanishes below eta = 2^(-1/4) — a quarter-octave down from unit."""
    return 2 ** -0.25


def mk4_ceilings():
    """Four wings (Mermin-Klyshko, X/Y at every site): the pre-written
    ceiling by full enumeration of all 256 strategies through the same
    recursion, and the physical ceiling as the MK4 operator norm."""
    import itertools as it
    X = [[0, 1], [1, 0]]
    Y = [[0, -1j], [1j, 0]]
    addm = lambda P, Q: [[P[i][j] + Q[i][j] for j in range(len(P))] for i in range(len(P))]
    subm = lambda P, Q: [[P[i][j] - Q[i][j] for j in range(len(P))] for i in range(len(P))]
    half = lambda P: [[0.5 * P[i][j] for j in range(len(P))] for i in range(len(P))]
    M, Mp = X, Y
    for _ in range(3):
        Mn = half(addm(_kron2(M, addm(X, Y)), _kron2(Mp, subm(X, Y))))
        Mpn = half(addm(_kron2(Mp, addm(X, Y)), _kron2(M, subm(Y, X))))
        M, Mp = Mn, Mpn
    rest = 0
    for bits in it.product((1, -1), repeat=8):
        m1, m1p = bits[0], bits[1]
        for k in (2, 4, 6):
            u, u2 = bits[k], bits[k + 1]
            m1, m1p = (0.5 * (m1 * (u + u2) + m1p * (u - u2)),
                       0.5 * (m1p * (u + u2) + m1 * (u2 - u)))
        rest = max(rest, abs(m1))
    return rest, _norm_h(M, iters=1200)
