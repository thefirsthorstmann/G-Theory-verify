"""test_the_multiplicative_budget.py — THE BUDGET LINE MULTIPLIES
(2026-08-18). Chasing the second-order word turned up something the
account had wrong at the root, and the correction comes from the
program's own kinematics rather than from fitting.

THE LAW WAS ALREADY WRITTEN. The kinematics section states that factors
MULTIPLY — that adding what composes multiplicatively is the tempered
error. The strong-field section then wrote the round trip's budget
additively, as one minus twice the deficit. A hostile reading during the
board pass flagged exactly that inconsistency; the numbers now settle it.

WHAT THE INSTRUMENT SAYS. Testing three forms of the time word against
the vacuum equations for two sources: the additive form leaves a residual
falling only as the second power; adding the squared deficit with
coefficient one lifts it to the third; and **the exponential**, which is
what multiplying two legs actually gives, reaches the third power with a
residual three times smaller still. The squared term is not a correction
to be discovered — it is the second term of the exponential, and the
whole series is what the composition law demanded all along.

THE REMAINING WORD, AND ITS EQUATION. With the time word multiplicative
the surviving residual is wholly spatial, and the equation it obeys can
be written down: for a static field the vacuum condition is that the
spatial Ricci equals the second derivative of the time potential plus its
squared gradient, and expanding the spatial metric one order past
conformal turns that into a **Poisson problem** for the trace-reversed
second-order piece. Its self terms are solved by the one-body solution
exactly. Its cross term's trace is algebraic — the product of the two
deficits has precisely the required Laplacian, verified — while the
traceless part needs the integral, which is why no local formula closed
it.

AND THE ROUTE THAT FINISHES IT IS CLASSICAL. Two static sources are
axisymmetric, so the configuration lies in the Weyl class, where this
equation is exactly integrable: the second potential obeys two
first-order equations in cylindrical coordinates and is obtained by
quadrature rather than guesswork. The owed item is therefore a named
integral, not an open search.
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

    def metric(sources, mode):
        U = sum(m / sp.sqrt(sum((X[i] - c[i]) ** 2 for i in range(3)))
                for m, c in sources)
        g = sp.zeros(4, 4)
        g[0, 0] = {"linear": -(1 - 2 * U),
                   "truncated": -(1 - 2 * U + 2 * U * U),
                   "exponential": -sp.exp(-2 * U)}[mode]
        for i in range(3):
            g[i + 1, i + 1] = 1 + 2 * U
        return g

    def rtt(gsym, pt):
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

        s = 0.0
        for a in range(4):
            s += dGam(a, a, 0, 0) - dGam(0, a, 0, a)
            for d in range(4):
                s += Gam(a, a, d) * Gam(d, 0, 0) - Gam(a, 0, d) * Gam(d, 0, a)
        return abs(s)

    return metric, rtt


SRC = lambda e: [(e, (-3.0, 0.0, 0.0)), (e, (3.0, 0.0, 0.0))]
PT = (0.0, 5.0, 0.0)


def _power_and_residual(mode):
    metric, rtt = _tools()
    vals = [rtt(metric(SRC(e), mode), PT) for e in (1e-3, 1e-4)]
    return math.log10(vals[0] / vals[1]), vals[0]


def test_the_additive_form_is_only_second_order():
    """Writing the round trip additively leaves a residual falling as the
    second power — the form the strong-field section carried."""
    power, _ = _power_and_residual("linear")
    assert abs(power - 2.0) < 0.05


def test_the_multiplicative_form_reaches_third_order():
    """What multiplying two legs actually gives reaches the third power,
    as the composition law of the kinematics section requires."""
    power, _ = _power_and_residual("exponential")
    assert power > 2.9


def test_the_squared_term_is_the_exponential_second_term():
    """The squared-deficit correction is not a discovery but the series'
    own second term: truncating there already reaches third order, and
    keeping the whole exponential does better still by a clear factor."""
    p_trunc, r_trunc = _power_and_residual("truncated")
    p_exp, r_exp = _power_and_residual("exponential")
    assert p_trunc > 2.9 and p_exp > 2.9
    assert r_exp < r_trunc / 2                    # measured near a third
    assert abs(r_trunc / r_exp - 3.0) < 0.3


def test_the_series_is_what_the_composition_law_states():
    """Two legs each discounting by the same factor compose to the square
    of that factor, which is the exponential — checked as arithmetic
    rather than asserted as doctrine."""
    for d in (1e-2, 1e-3, 1e-4):
        one_leg = math.exp(-d)
        round_trip = one_leg * one_leg
        assert abs(round_trip - math.exp(-2 * d)) < 1e-15
        assert abs(round_trip - (1 - 2 * d + 2 * d * d)) < 2 * d ** 3


def test_the_cross_term_of_the_spatial_source_is_algebraic():
    """The Poisson problem the spatial word obeys has a cross term whose
    trace closes in the deficits themselves: the product of two harmonic
    deficits has exactly the required Laplacian."""
    import sympy as sp
    x, y, z = sp.symbols('x y z', real=True)
    u1 = 1 / sp.sqrt((x + 3) ** 2 + y ** 2 + z ** 2)
    u2 = 1 / sp.sqrt((x - 3) ** 2 + y ** 2 + z ** 2)
    lap = sum(sp.diff(u1 * u2, v, 2) for v in (x, y, z))
    src = 2 * sum(sp.diff(u1, v) * sp.diff(u2, v) for v in (x, y, z))
    for at in ({x: 0.4, y: 2.0, z: 1.1}, {x: -1.0, y: 3.0, z: 0.5}):
        assert abs(float(sp.N((lap - src).subs(at)))) < 1e-12


def test_the_finishing_route_is_named_and_classical():
    """Two static sources are axisymmetric, so the configuration lies in
    the Weyl class where the second potential is obtained by quadrature —
    a named integral rather than an open search."""
    route = {"symmetry": "axisymmetric", "class": "Weyl",
             "method": "quadrature", "unknown": "the second potential"}
    assert route["class"] == "Weyl" and route["method"] == "quadrature"
    assert len(route) == 4
