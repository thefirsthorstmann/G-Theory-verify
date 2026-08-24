"""test_the_quadrature.py — THE STATIC SECTOR, EXACT AND GENERAL, AND THE
SOURCE FOUND TO BE A ROD (2026-08-18, amended the same day). The ledger's
last structural item is closed. It was first closed too narrowly — as a
verification at sampled points for two point sources — and the amendment
both strengthens it into a general theorem and corrects which solution the
register is actually building.

THE MAPPING. A static axisymmetric field is a Weyl field, and the Weyl
equations say two things. First, the time potential is flat-harmonic —
which is exactly the composite clause, deficits summing with nothing
added. Second, the remaining spatial word is not free but obtained by
quadrature from that potential. Set the Weyl potential equal to the
register's deficit and the time word to the multiplicative budget, and
the dictionary is complete with nothing left to choose.

THE THEOREM, AND IT IS GENERAL. Take the Weyl metric with BOTH functions
arbitrary and compute the Ricci tensor symbolically. Impose only Laplace
on the deficit and the two quadrature equations on the spatial word:
**all sixteen components vanish identically.** So the construction is
exactly vacuum for every static axisymmetric configuration whatever — any
number of sources, of any shape. The two-source check below is one
instance of it, not the result.

THE QUADRATURE'S INTEGRABILITY IS ALSO GENERAL. The cross equations'
integrability condition reduces, by Laplace alone, to zero for ANY pair
of harmonic deficits. So the spatial word always exists; only its closed
form depends on the sources.

AND THE SOURCE IS A ROD, NOT A POINT — the correction. Which member of
the class the register builds is fixed by the shape of its source read in
Weyl coordinates, and the register's own one-source answer settles it:
that answer is Schwarzschild, whose Weyl potential is the potential of a
uniform ROD of coordinate length 2m — reproduced here to the last digit,
while the point potential is not. The register's point mass is not a
point in this chart; it is the segment the horizon maps to. The two-point
closed form found first is therefore the Curzon member — a real vacuum
solution, but not the register's body. The two differ only at third order
in m/r, so the weak field and the post-Newtonian faces are untouched by
the correction; what changes is which exact solution is being named.

WHICH RESOLVES THE FORK RATHER THAN MEASURING IT. The earlier worry was
that exact superposition must disagree with a theory whose field sources
itself. The subtlety is what superposes: the DEFICIT does, being the
harmonic potential, while the metric does not, the quadrature supplying a
cross term that is nothing like a sum. The composite clause was right and
the apparent conflict was a confusion between the two. What remains
outside is motion and radiation, the non-static sector.
"""

import math
import os
import sys

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))


def _tools():
    import sympy as sp
    import numpy as np
    rho, z, a, m1, m2 = sp.symbols('rho z a m1 m2', positive=True)
    C = (None, rho, z, None)

    def pieces(M1, M2, A):
        r1 = sp.sqrt(rho ** 2 + (z - A) ** 2)
        r2 = sp.sqrt(rho ** 2 + (z + A) ** 2)
        psi = -M1 / r1 - M2 / r2
        g1 = -M1 ** 2 * rho ** 2 / (2 * r1 ** 4)
        g2 = -M2 ** 2 * rho ** 2 / (2 * r2 ** 4)
        g12 = M1 * M2 / (2 * A ** 2) * ((rho ** 2 + z ** 2 - A ** 2) / (r1 * r2) - 1)
        return psi, g1 + g2 + g12

    def metric(M1, M2, A):
        psi, gam = pieces(M1, M2, A)
        g = sp.zeros(4, 4)
        g[0, 0] = -sp.exp(2 * psi)
        g[1, 1] = sp.exp(2 * (gam - psi))
        g[2, 2] = sp.exp(2 * (gam - psi))
        g[3, 3] = rho ** 2 * sp.exp(-2 * psi)
        return g

    def ricci_max(gsym, pt):
        sub = {rho: pt[0], z: pt[1]}
        ev = lambda e: float(sp.N(e.subs(sub), 40))
        g0 = [[ev(gsym[i, j]) for j in range(4)] for i in range(4)]
        dg = [[[0.0] * 4 for _ in range(4)] for _ in range(4)]
        ddg = [[[[0.0] * 4 for _ in range(4)] for _ in range(4)] for _ in range(4)]
        d1 = {}
        for c in (1, 2):
            for i in range(4):
                for j in range(4):
                    e = sp.diff(gsym[i, j], C[c])
                    d1[(c, i, j)] = e
                    dg[c][i][j] = ev(e)
        for c in (1, 2):
            for e_ in (1, 2):
                for i in range(4):
                    for j in range(4):
                        ddg[c][e_][i][j] = ev(sp.diff(d1[(e_, i, j)], C[c]))
        G = np.array(g0)
        Gi = np.linalg.inv(G)
        dGi = [(-Gi @ np.array(dg[c]) @ Gi) for c in range(4)]
        Gam = lambda A_, b, c: 0.5 * sum(
            Gi[A_, d] * (dg[b][d][c] + dg[c][d][b] - dg[d][b][c]) for d in range(4))

        def dGam(e_, A_, b, c):
            t1 = 0.5 * sum(dGi[e_][A_][d] * (dg[b][d][c] + dg[c][d][b] - dg[d][b][c])
                           for d in range(4))
            t2 = 0.5 * sum(Gi[A_, d] * (ddg[e_][b][d][c] + ddg[e_][c][d][b]
                                        - ddg[e_][d][b][c]) for d in range(4))
            return t1 + t2

        best = 0.0
        for b in range(4):
            for c in range(4):
                s = 0.0
                for A_ in range(4):
                    s += dGam(A_, A_, b, c) - dGam(c, A_, b, A_)
                    for d in range(4):
                        s += Gam(A_, A_, d) * Gam(d, b, c) - Gam(A_, c, d) * Gam(d, b, A_)
                best = max(best, abs(s))
        return best

    return sp, (rho, z, a, m1, m2), metric, ricci_max


def test_the_self_term_is_confirmed_by_its_own_quadrature():
    """The single-source spatial word satisfies both first-order Weyl
    equations identically — no integration constant, no choice."""
    sp, (rho, z, a, m1, m2), _, _ = _tools()
    r1 = sp.sqrt(rho ** 2 + (z - a) ** 2)
    psi = -m1 / r1
    gr = rho * (sp.diff(psi, rho) ** 2 - sp.diff(psi, z) ** 2)
    gz = 2 * rho * sp.diff(psi, rho) * sp.diff(psi, z)
    cand = -m1 ** 2 * rho ** 2 / (2 * r1 ** 4)
    assert sp.simplify(sp.diff(cand, rho) - gr) == 0
    assert sp.simplify(sp.diff(cand, z) - gz) == 0


def test_the_cross_term_is_integrable_and_solved():
    """Its integrability condition vanishes, as harmonicity guarantees,
    and the closed form satisfies both equations identically."""
    sp, (rho, z, a, m1, m2), _, _ = _tools()
    r1 = sp.sqrt(rho ** 2 + (z - a) ** 2)
    r2 = sp.sqrt(rho ** 2 + (z + a) ** 2)
    p1, p2 = -m1 / r1, -m2 / r2
    gr = 2 * rho * (sp.diff(p1, rho) * sp.diff(p2, rho)
                    - sp.diff(p1, z) * sp.diff(p2, z))
    gz = 2 * rho * (sp.diff(p1, rho) * sp.diff(p2, z)
                    + sp.diff(p1, z) * sp.diff(p2, rho))
    assert sp.simplify(sp.diff(gr, z) - sp.diff(gz, rho)) == 0
    cross = m1 * m2 / (2 * a ** 2) * ((rho ** 2 + z ** 2 - a ** 2) / (r1 * r2) - 1)
    assert sp.simplify(sp.diff(cross, rho) - gr) == 0
    assert sp.simplify(sp.diff(cross, z) - gz) == 0


def test_the_assembled_two_source_metric_is_exactly_vacuum():
    """Deficits superposed, the time word multiplicative, the spatial
    word the solved quadrature: the Ricci tensor vanishes to machine
    precision, for equal and unequal masses alike."""
    _, _, metric, ricci_max = _tools()
    for M1, M2, A in ((1.0, 1.0, 1.0), (1.0, 0.4, 1.5)):
        g = metric(M1, M2, A)
        for pt in ((2.0, 0.0), (1.5, 1.2), (0.7, 3.0)):
            assert ricci_max(g, pt) < 1e-12, (M1, M2, A, pt)


def test_it_is_exact_and_not_merely_second_order():
    """No mass scan is needed to see the order: the residual does not
    fall with the masses because it is already zero at full strength."""
    _, _, metric, ricci_max = _tools()
    strong = ricci_max(metric(1.0, 1.0, 1.0), (1.5, 1.2))
    weak = ricci_max(metric(1e-2, 1e-2, 1.0), (1.5, 1.2))
    assert strong < 1e-12 and weak < 1e-12
    assert strong / max(weak, 1e-300) < 1e6            # no power law: both zero


def test_laplace_and_quadrature_make_the_whole_class_vacuum():
    """The general theorem, and the actual result: with BOTH Weyl
    functions arbitrary, imposing only Laplace on the deficit and the two
    quadrature equations on the spatial word annihilates all sixteen
    Ricci components identically — so every static axisymmetric
    configuration, of any number of sources of any shape, is exactly
    vacuum by construction."""
    import sympy as sp
    rho, z = sp.symbols('rho z', positive=True)
    P = sp.Function('psi')(rho, z)
    G = sp.Function('gam')(rho, z)
    X = (sp.Symbol('t'), rho, z, sp.Symbol('phi'))
    g = sp.diag(-sp.exp(2 * P), sp.exp(2 * (G - P)),
                sp.exp(2 * (G - P)), rho ** 2 * sp.exp(-2 * P))
    gi = g.inv()
    d = lambda e, c: sp.diff(e, X[c]) if c in (1, 2) else sp.S(0)
    Gam = [[[sp.simplify(sum(gi[a, m] * (d(g[m, b], c) + d(g[m, c], b)
                                         - d(g[b, c], m)) for m in range(4)) / 2)
             for c in range(4)] for b in range(4)] for a in range(4)]
    pr, pz = sp.diff(P, rho), sp.diff(P, z)
    qr, qz = rho * (pr ** 2 - pz ** 2), 2 * rho * pr * pz
    rules = [(sp.diff(G, rho, 2), sp.diff(qr, rho)),
             (sp.diff(G, rho, z), sp.diff(qr, z)),
             (sp.diff(G, z, 2), sp.diff(qz, z)),
             (sp.diff(G, rho), qr), (sp.diff(G, z), qz)]
    for b in range(4):
        for c in range(4):
            e = sum(d(Gam[a][b][c], a) - d(Gam[a][b][a], c)
                    + sum(Gam[a][a][f] * Gam[f][b][c]
                          - Gam[a][c][f] * Gam[f][b][a] for f in range(4))
                    for a in range(4))
            for old, new in rules:
                e = e.subs(old, new)
            e = e.doit().subs(sp.diff(P, rho, 2), -pr / rho - sp.diff(P, z, 2))
            assert sp.simplify(sp.expand(e)) == 0, (b, c)


def test_the_cross_quadrature_is_integrable_for_any_harmonic_pair():
    """Its integrability condition reduces to zero by Laplace alone, with
    no assumption about the sources — so the spatial word always exists
    and only its closed form is source-specific."""
    import sympy as sp
    rho, z = sp.symbols('rho z', positive=True)
    A, B = sp.Function('a')(rho, z), sp.Function('b')(rho, z)
    ar, az, br, bz = (sp.diff(A, rho), sp.diff(A, z),
                      sp.diff(B, rho), sp.diff(B, z))
    gr = 2 * rho * (ar * br - az * bz)
    gz = 2 * rho * (ar * bz + az * br)
    e = sp.diff(gr, z) - sp.diff(gz, rho)
    e = e.subs(sp.diff(A, rho, 2), -ar / rho - sp.diff(A, z, 2))
    e = e.subs(sp.diff(B, rho, 2), -br / rho - sp.diff(B, z, 2))
    assert sp.simplify(sp.expand(e)) == 0


def test_the_registers_source_is_a_rod_of_length_twice_its_mass():
    """The correction. Which member the register builds is fixed by its
    own one-source answer, which is Schwarzschild: read in Weyl
    coordinates that answer is the potential of a uniform rod of
    coordinate length 2m, to the last digit — and NOT the point
    potential. The register's point mass is not a point in this chart."""
    m = 1.0
    for r, th in ((4.0, 0.7), (8.0, 1.3), (20.0, 0.4), (100.0, 1.1)):
        rr = math.sqrt(r * r - 2 * m * r) * math.sin(th)
        zz = (r - m) * math.cos(th)
        rp = math.hypot(rr, zz - m)
        rm = math.hypot(rr, zz + m)
        rod = 0.5 * math.log((rp + rm - 2 * m) / (rp + rm + 2 * m))
        point = -m / math.hypot(rr, zz)
        schw = 0.5 * math.log(1 - 2 * m / r)
        assert abs(rod - schw) < 1e-14                  # the rod IS Schwarzschild
        assert abs(point - schw) > 1e-8                 # the point is not


def test_rod_and_point_agree_only_below_third_order():
    """Both are harmonic, so both lie inside the theorem; they part at
    third order in the mass ratio, which is why the weak field and the
    post-Newtonian faces are untouched by naming the right one."""
    m = 1.0
    diffs = []
    for r in (10.0, 100.0, 1000.0):
        rr = math.sqrt(r * r - 2 * m * r)
        zz = 0.0
        rp = math.hypot(rr, zz - m)
        rm = math.hypot(rr, zz + m)
        rod = 0.5 * math.log((rp + rm - 2 * m) / (rp + rm + 2 * m))
        diffs.append(abs(rod + m / math.hypot(rr, zz)))
    for a, b in zip(diffs, diffs[1:]):
        assert 2.9 < math.log10(a / b) < 3.2            # third order, not second


def test_what_superposes_is_the_deficit_not_the_metric():
    """The resolution of the apparent conflict: the deficit sums exactly,
    being harmonic, while the spatial word does not — its cross term is
    nothing like a sum, and it is what the quadrature supplies."""
    sp, (rho, z, a, m1, m2), _, _ = _tools()
    r1 = sp.sqrt(rho ** 2 + (z - a) ** 2)
    r2 = sp.sqrt(rho ** 2 + (z + a) ** 2)
    psi = -m1 / r1 - m2 / r2
    lap = sp.simplify(sp.diff(psi, rho, 2) + sp.diff(psi, rho) / rho
                      + sp.diff(psi, z, 2))
    assert sp.simplify(lap) == 0                        # the deficit is harmonic
    cross = m1 * m2 / (2 * a ** 2) * ((rho ** 2 + z ** 2 - a ** 2) / (r1 * r2) - 1)
    assert sp.simplify(cross) != 0                      # the metric's part is not a sum
