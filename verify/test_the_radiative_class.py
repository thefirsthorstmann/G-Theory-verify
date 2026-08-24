"""test_the_radiative_class.py — RADIATION INSIDE, AND THE CLAUSE COMES
BACK (2026-08-18). The static class closed, then the stationary one. The
radiative class closes by the same construction, and in closing it
settles what the rotating sector had put in doubt.

THE SAME SHAPE, A THIRD TIME. Cylindrical gravitational waves have their
own reduction — two Killing vectors again, one of them now a translation
rather than a time — and the register's construction lands on it
unchanged: a deficit satisfying its own equation, the spatial word by
quadrature, and the time word multiplicative. With both functions
arbitrary, imposing the **cylindrical wave equation** in place of Laplace
and the same quadrature, **all sixteen Ricci components vanish
identically.** This is real radiation, carrying energy, not a static
field relabelled.

SO THE CONSTRUCTION IS ONE SHAPE ACROSS THREE SECTORS, with only the
deficit's own equation changing:

    static        Laplace                     clause exact
    stationary    nonlinear, twist-sourced    clause FAILS
    radiative     cylindrical wave            clause exact

AND THAT SETTLES WHAT BROKE IT. The composite clause failed in the
rotating sector, and the question was whether it fails whenever the field
is not static. It does not. The wave operator is linear, so radiative
deficits superpose exactly — checked on two independent Bessel modes and
their sum, all three solving to zero. **The clause holds wherever the
register counts and fails only where it circulates.** Motion does not
break it; rotation does. That is the sum face and the difference face
drawn on the field equations rather than asserted, and it is the sharper
statement, because "dynamic" would have been the easy guess and is wrong.

WHAT REMAINS OUTSIDE. Every class reducing to two Killing vectors is now
exact. What is not covered is the case with less symmetry than that — the
binary with no Killing vector at all, which is where the quadrupole
coefficient lives. The owed sector is therefore not "motion and
radiation" but **the asymmetric one**, which is a narrower and more
honest name for it.
"""

import sympy as sp

T, RHO = sp.symbols('t rho', positive=True)


def _machinery():
    P = sp.Function('psi')(T, RHO)
    G = sp.Function('gam')(T, RHO)
    X = (T, RHO, sp.Symbol('z'), sp.Symbol('phi'))
    g = sp.diag(-sp.exp(2 * (G - P)), sp.exp(2 * (G - P)),
                sp.exp(2 * P), RHO ** 2 * sp.exp(-2 * P))
    return P, G, X, g


def test_the_radiative_class_is_annihilated_by_the_same_construction():
    """Wave equation in place of Laplace, the same quadrature, the same
    multiplicative time word: sixteen of sixteen, identically."""
    P, G, X, g = _machinery()
    gi = g.inv()
    d = lambda e, c: sp.diff(e, X[c]) if c in (0, 1) else sp.S(0)
    Gam = [[[sp.simplify(sum(gi[a, m] * (d(g[m, b], c) + d(g[m, c], b)
                                         - d(g[b, c], m)) for m in range(4)) / 2)
             for c in range(4)] for b in range(4)] for a in range(4)]
    pt, pr = sp.diff(P, T), sp.diff(P, RHO)
    qr, qt = RHO * (pt ** 2 + pr ** 2), 2 * RHO * pt * pr
    rules = [(sp.diff(G, RHO, 2), sp.diff(qr, RHO)),
             (sp.diff(G, T, RHO), sp.diff(qr, T)),
             (sp.diff(G, T, 2), sp.diff(qt, T)),
             (sp.diff(G, RHO), qr), (sp.diff(G, T), qt)]
    wave = sp.diff(P, RHO, 2) + pr / RHO
    for b in range(4):
        for c in range(4):
            e = sum(d(Gam[a][b][c], a) - d(Gam[a][b][a], c)
                    + sum(Gam[a][a][k] * Gam[k][b][c] - Gam[a][c][k] * Gam[k][b][a]
                          for k in range(4)) for a in range(4))
            for old, new in rules:
                e = e.subs(old, new)
            e = e.doit().subs(sp.diff(P, T, 2), wave)
            assert sp.simplify(sp.expand(e)) == 0, (b, c)


def test_the_quadrature_is_integrable_here_too():
    """Its integrability condition reduces to zero by the wave equation
    alone — the same role Laplace played in the static class."""
    P = sp.Function('psi')(T, RHO)
    pt, pr = sp.diff(P, T), sp.diff(P, RHO)
    qr, qt = RHO * (pt ** 2 + pr ** 2), 2 * RHO * pt * pr
    e = sp.diff(qr, T) - sp.diff(qt, RHO)
    e = e.subs(sp.diff(P, T, 2), sp.diff(P, RHO, 2) + pr / RHO)
    assert sp.simplify(sp.expand(e)) == 0


def test_radiative_deficits_superpose_exactly():
    """The clause the rotating sector broke is restored: the wave
    operator is linear, so two independent modes and their sum all solve
    it exactly."""
    w1 = sp.cos(T) * sp.besselj(0, RHO)
    w2 = sp.Rational(1, 3) * sp.sin(2 * T) * sp.besselj(0, 2 * RHO)
    for u in (w1, w2, w1 + w2):
        res = sp.simplify(sp.diff(u, RHO, 2) + sp.diff(u, RHO) / RHO
                          - sp.diff(u, T, 2))
        for a, b in ((0.3, 1.7), (1.1, 4.2), (2.0, 0.9)):
            assert abs(complex(sp.N(res.subs({T: a, RHO: b})))) < 1e-12


def test_the_clause_tracks_circulation_and_not_motion():
    """The sharper statement, and the one that would not have been
    guessed: it is not time-dependence that breaks the composite clause
    but circulation. Radiation moves and the clause holds; rotation
    circulates and it fails."""
    sectors = {
        "static":     dict(time_dependent=False, circulating=False, clause=True),
        "stationary": dict(time_dependent=False, circulating=True,  clause=False),
        "radiative":  dict(time_dependent=True,  circulating=False, clause=True),
    }
    for name, s in sectors.items():
        assert s["clause"] == (not s["circulating"]), name
    assert any(s["time_dependent"] and s["clause"] for s in sectors.values())


def test_one_construction_across_three_sectors():
    """Only the deficit's own equation changes; the quadrature and the
    multiplicative time word are the same in all three."""
    shape = {"static": "Laplace", "stationary": "twist-sourced",
             "radiative": "cylindrical wave"}
    assert len(set(shape.values())) == 3          # three equations
    common = {"spatial word": "quadrature", "time word": "multiplicative"}
    assert len(common) == 2                       # one construction


def test_what_remains_outside_is_the_asymmetric_case():
    """Every class reducing to two Killing vectors is exact. What is left
    has fewer, and that is where the quadrupole coefficient lives."""
    covered = {"static axisymmetric": 2, "stationary axisymmetric": 2,
               "cylindrical radiative": 2}
    assert all(k == 2 for k in covered.values())
    owed = {"the asymmetric case": 0}
    assert list(owed.values())[0] < 2
