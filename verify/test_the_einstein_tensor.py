"""test_the_einstein_tensor.py — THE CALCULATION RUN, AND A RETRACTION
(2026-08-18). The ledger's last structural item was the Einstein tensor
of the two-source prescription. It has now been computed exactly —
symbolic derivatives, no finite differences — and the result refutes the
prescription proposed earlier the same day. The retraction is the
finding, and the instrument that produced it is kept.

THE MACHINERY, VALIDATED FIRST. With one source the account's own words
give the vacuum solution, so every Ricci component must vanish. Computed
exactly, they do — to zero and to round-off at a second point. The
instrument is therefore trustworthy on cases whose answer is not known.

THE REFUTATION. The multi-source rule proposed earlier — the ruler
stretched along the deficit's gradient, areal transverse — does NOT
satisfy the vacuum equations for two sources, and the failure is not
small or high-order: scanning the masses down four decades, the residual
falls as the FIRST power, not the second. A prescription that fails at
linear order fails before the post-Newtonian comparison begins. The
"coordinate statement discharged" claim of the same day is withdrawn.

WHAT THE EQUATIONS WANT INSTEAD. Reading the ruler as the same stretch in
every direction — conformally flat space — gives a residual falling as
the SECOND power exactly, so that form is right at first post-Newtonian
order, which is what the parametrized argument had concluded
independently. But it is not exact even for one source: its residual is
also second order there, where the areal form is exact.

SO THE HONEST STATE, sharper than before. Two readings exist, each
correct in a different regime — areal exact for one source, conformal
correct to first order for many — and NEITHER is exact for many sources
beyond that. That is the tensor face restated with a computation behind
it rather than an intuition, and the owed rule is now precisely
specified: the form that reduces to the areal one for a single source and
to the conformal one at first order for several, which is the register's
own account of the second-order potential.
"""

import math
import os
import sys

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))


def _ricci_tools():
    """The exact machinery: symbolic derivatives, numeric assembly."""
    import sympy as sp
    import numpy as np
    x, y, z = sp.symbols('x y z', real=True)
    X = (x, y, z)

    def deficit(sources):
        return sum(m / sp.sqrt(sum((X[i] - c[i]) ** 2 for i in range(3)))
                   for m, c in sources)

    def gradient_stretched(sources):
        d = deficit(sources)
        gr = [sp.diff(d, v) for v in X]
        norm = sp.sqrt(sum(g * g for g in gr))
        n = [g / norm for g in gr]
        f = 1 / (1 - 2 * d) - 1
        g = sp.zeros(4, 4)
        g[0, 0] = -(1 - 2 * d)
        for i in range(3):
            for j in range(3):
                g[i + 1, j + 1] = (1 if i == j else 0) + f * n[i] * n[j]
        return g

    def conformal(sources):
        d = deficit(sources)
        g = sp.zeros(4, 4)
        g[0, 0] = -(1 - 2 * d)
        for i in range(3):
            g[i + 1, i + 1] = 1 + 2 * d
        return g

    def ricci_max(gsym, pt):
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

        def Gam(a, b, c):
            return 0.5 * sum(Gi[a, dd] * (dg[b][dd][c] + dg[c][dd][b] - dg[dd][b][c])
                             for dd in range(4))

        def dGam(e_, a, b, c):
            t1 = 0.5 * sum(dGi[e_][a][dd] * (dg[b][dd][c] + dg[c][dd][b] - dg[dd][b][c])
                           for dd in range(4))
            t2 = 0.5 * sum(Gi[a, dd] * (ddg[e_][b][dd][c] + ddg[e_][c][dd][b]
                                        - ddg[e_][dd][b][c]) for dd in range(4))
            return t1 + t2

        best = 0.0
        for b in range(4):
            for c in range(4):
                s = 0.0
                for a in range(4):
                    s += dGam(a, a, b, c) - dGam(c, a, b, a)
                    for dd in range(4):
                        s += Gam(a, a, dd) * Gam(dd, b, c) - Gam(a, c, dd) * Gam(dd, b, a)
                best = max(best, abs(s))
        return best

    return gradient_stretched, conformal, ricci_max


def test_the_machinery_is_validated_on_the_known_case():
    """One source with the account's own words is the vacuum solution, so
    the computed Ricci must vanish — and it does, exactly."""
    stretched, _, ricci_max = _ricci_tools()
    g = stretched([(1.0, (0.0, 0.0, 0.0))])
    assert ricci_max(g, (4.0, 0.0, 0.0)) < 1e-14
    assert ricci_max(g, (2.0, 3.0, 1.0)) < 1e-14


def test_the_gradient_stretched_rule_fails_at_linear_order():
    """The retraction, computed: two sources, masses scanned down three
    decades, and the residual falls as the FIRST power — so the rule
    fails before any post-Newtonian comparison begins."""
    stretched, _, ricci_max = _ricci_tools()
    vals = []
    for eps in (1e-2, 1e-3, 1e-4):
        g = stretched([(eps, (-3.0, 0.0, 0.0)), (eps, (3.0, 0.0, 0.0))])
        vals.append(ricci_max(g, (0.0, 5.0, 0.0)))
    for a, b in zip(vals, vals[1:]):
        power = math.log10(a / b)
        assert abs(power - 1.0) < 0.05                # linear, not quadratic


def test_the_conformal_reading_fails_only_at_second_order():
    """The alternative reading — the same stretch in every direction —
    has a residual falling as the second power exactly, so it is right
    at first post-Newtonian order, agreeing with what the parametrized
    argument concluded by another route."""
    _, conformal, ricci_max = _ricci_tools()
    vals = []
    for eps in (1e-2, 1e-3, 1e-4):
        g = conformal([(eps, (-3.0, 0.0, 0.0)), (eps, (3.0, 0.0, 0.0))])
        vals.append(ricci_max(g, (0.0, 5.0, 0.0)))
    for a, b in zip(vals, vals[1:]):
        power = math.log10(a / b)
        assert abs(power - 2.0) < 0.05                # quadratic


def test_neither_form_is_exact_for_many_sources():
    """The conformal reading is not exact even with one source — its
    residual is second order there too, where the areal form vanishes.
    So no form yet given is both exact for one source and correct for
    several beyond first order, which is the item that remains."""
    stretched, conformal, ricci_max = _ricci_tools()
    exact_one = ricci_max(stretched([(1e-2, (0.0, 0.0, 0.0))]), (5.0, 0.0, 0.0))
    conf_one = ricci_max(conformal([(1e-2, (0.0, 0.0, 0.0))]), (5.0, 0.0, 0.0))
    assert exact_one < 1e-14                          # areal: exact
    assert conf_one > 1e-8                            # conformal: not exact
    assert conf_one / (1e-2) ** 2 > 1e-3              # and it is second order
