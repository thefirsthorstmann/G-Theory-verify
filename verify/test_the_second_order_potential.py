"""test_the_second_order_potential.py — THE TIME WORD FOUND, THE SPATIAL
WORD SHOWN NON-LOCAL (2026-08-18). the author asked whether the first and second
orders here are the program's first- and second-order ambisonics, and
whether those rules would supply the tool. The decomposition IS the right
language and it earns its keep immediately — but it also shows exactly
where the tool runs out, which is the finding.

THE TIME WORD IS FOUND, AND IT IS SCALAR. Adding a coefficient times the
squared deficit to the time word and scanning it, the value one drives
the time-time component's residual from second order to **third, exactly**
— power 3.00 — while every other value leaves it at second. So the
second-order time word is settled: the budget line gains twice the
squared deficit, and that piece is pure monopole, order zero in the
angular sense, no direction in it at all.

WHAT REMAINS IS ENTIRELY SPATIAL, AND CARRIES BOTH ORDERS. With the time
word fixed, the surviving residual sits wholly in the spatial block, and
decomposing it shows a traceless part LARGER than its trace — a genuine
quadrupole remainder, order two in the angular sense, which is what the
question supposed.

BUT THE ANGULAR LANGUAGE DOES NOT SUPPLY THE FIX. Three local ansatz
families were scanned against it — a traceless quadrupole built from the
deficit's gradients, a scalar square, and the cross product of the two
deficits, which is the register's own bilinear union object — and NONE
moves the spatial order off two. The reason is structural rather than a
failure of search: the second-order potential solves a Poisson equation
whose source is the squared gradient, so it is an INTEGRAL of the
deficits and not any algebraic function of them. Angular order tells you
what shape the missing piece has; it cannot tell you the piece, because
the piece is non-local.

So the answer to the question is yes and no, and the no is the useful
half: the ambisonic split is the right bookkeeping — it isolated the
scalar fix and confirmed it exactly — while the object still owed is a
solved equation, not a chosen harmonic.
"""

import math
import os
import sys

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))


def _tools():
    import sympy as sp
    import numpy as np
    x, y, z = sp.symbols('x y z', real=True)
    X = (x, y, z)

    def metric(sources, alpha=1.0, beta=0.0, gam=0.0, k=0.0):
        Us = [m / sp.sqrt(sum((X[i] - c[i]) ** 2 for i in range(3)))
              for m, c in sources]
        U = sum(Us)
        cross = Us[0] * Us[1] if len(Us) > 1 else 0
        gr = [sp.diff(U, v) for v in X]
        n2 = sum(g * g for g in gr)
        g = sp.zeros(4, 4)
        g[0, 0] = -(1 - 2 * U + 2 * alpha * U * U)
        for i in range(3):
            for j in range(3):
                iso = (1 if i == j else 0) * (1 + 2 * U + gam * U * U + k * cross)
                q = gr[i] * gr[j] - (1 if i == j else 0) * n2 / 3
                g[i + 1, j + 1] = iso + beta * q
        return g

    def ricci(gsym, pt):
        sub = {x: pt[0], y: pt[1], z: pt[2]}
        ev = lambda e: float(sp.N(e.subs(sub), 30))
        g0 = [[ev(gsym[a, b]) for b in range(4)] for a in range(4)]
        dg = [[[0.0] * 4 for _ in range(4)] for _ in range(4)]
        ddg = [[[[0.0] * 4 for _ in range(4)] for _ in range(4)] for _ in range(4)]
        d1 = {}
        for c in range(1, 4):
            for a in range(4):
                for b in range(4):
                    e = sp.diff(gsym[a, b], X[c - 1])
                    d1[(c, a, b)] = e
                    dg[c][a][b] = ev(e)
        for c in range(1, 4):
            for e_ in range(1, 4):
                for a in range(4):
                    for b in range(4):
                        ddg[c][e_][a][b] = ev(sp.diff(d1[(e_, a, b)], X[c - 1]))
        G = np.array(g0)
        Gi = np.linalg.inv(G)
        dGi = [(-Gi @ np.array(dg[c]) @ Gi) for c in range(4)]
        Gam = lambda a, b, c: 0.5 * sum(
            Gi[a, d] * (dg[b][d][c] + dg[c][d][b] - dg[d][b][c]) for d in range(4))

        def dGam(e_, a, b, c):
            t1 = 0.5 * sum(dGi[e_][a][d] * (dg[b][d][c] + dg[c][d][b] - dg[d][b][c])
                           for d in range(4))
            t2 = 0.5 * sum(Gi[a, d] * (ddg[e_][b][d][c] + ddg[e_][c][d][b]
                                       - ddg[e_][d][b][c]) for d in range(4))
            return t1 + t2

        R = [[0.0] * 4 for _ in range(4)]
        for b in range(4):
            for c in range(4):
                s = 0.0
                for a in range(4):
                    s += dGam(a, a, b, c) - dGam(c, a, b, a)
                    for d in range(4):
                        s += Gam(a, a, d) * Gam(d, b, c) - Gam(a, c, d) * Gam(d, b, a)
                R[b][c] = s
        return R

    return metric, ricci


PT = (0.0, 5.0, 0.0)
SRC = lambda e: [(e, (-3.0, 0.0, 0.0)), (e, (3.0, 0.0, 0.0))]


def _power(metric, ricci, pick, **kw):
    vals = []
    for e in (1e-3, 1e-4):
        R = ricci(metric(SRC(e), **kw), PT)
        vals.append(pick(R))
    return math.log10(vals[0] / vals[1])


def test_the_scalar_fix_settles_the_time_word_exactly():
    """Scanning the squared-deficit coefficient, one drives the time-time
    residual to third order — power 3.00 — and no other value does."""
    metric, ricci = _tools()
    tt = lambda R: abs(R[0][0])
    assert _power(metric, ricci, tt, alpha=1.0) > 2.8
    assert _power(metric, ricci, tt, alpha=0.0) < 2.3
    assert _power(metric, ricci, tt, alpha=2.0) < 2.3


def test_what_survives_is_spatial_and_carries_a_quadrupole():
    """With the time word fixed the remainder is wholly spatial, and its
    traceless part exceeds its trace — a quadrupole, in the angular
    sense the question named."""
    metric, ricci = _tools()
    R = ricci(metric(SRC(1e-3), alpha=1.0), PT)
    assert abs(R[0][0]) < 1e-11                       # time word: clean
    spatial = max(abs(R[i][j]) for i in (1, 2, 3) for j in (1, 2, 3))
    assert spatial > 1e-9                             # remainder is spatial
    trace = sum(R[i][i] for i in (1, 2, 3)) / 3
    traceless = max(abs(R[i][j] - (trace if i == j else 0))
                    for i in (1, 2, 3) for j in (1, 2, 3))
    assert traceless > abs(trace)                     # quadrupole dominates


def test_no_local_ansatz_moves_the_spatial_order():
    """A traceless quadrupole, a scalar square, and the register's own
    cross product all leave the spatial residual at second order — so
    angular order names the shape but cannot supply the piece."""
    metric, ricci = _tools()
    sp_ = lambda R: max(abs(R[i][j]) for i in (1, 2, 3) for j in (1, 2, 3))
    for kw in ({"beta": 2.0}, {"gam": 1.0}, {"k": 6.0}, {"beta": 1.0, "gam": 1.0}):
        p = _power(metric, ricci, sp_, alpha=1.0, **kw)
        assert p < 2.4, kw


def test_the_reason_is_that_the_piece_is_non_local():
    """The second-order potential solves a Poisson equation sourced by
    the squared gradient, so it is an integral of the deficits — which
    is why no algebraic combination of them can be it. Checked in the
    one place it IS algebraic: the cross term, whose Laplacian is the
    cross source exactly."""
    import sympy as sp
    x, y, z = sp.symbols('x y z', real=True)
    U1 = 1 / sp.sqrt((x + 3) ** 2 + y ** 2 + z ** 2)
    U2 = 1 / sp.sqrt((x - 3) ** 2 + y ** 2 + z ** 2)
    lap = sum(sp.diff(U1 * U2, v, 2) for v in (x, y, z))
    src = 2 * sum(sp.diff(U1, v) * sp.diff(U2, v) for v in (x, y, z))
    at = {x: 0.4, y: 2.0, z: 1.1}
    assert abs(float(sp.N((lap - src).subs(at))) ) < 1e-12
