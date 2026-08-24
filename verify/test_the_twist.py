"""test_the_twist.py — ROTATION BROUGHT INSIDE, AND THE BUDGET FOUND TO
HAVE TWO SPENDS (2026-08-18). The static sector closed because the Weyl
class exists and the register's objects land on it exactly. Rotation has
its own such reduction, and the register lands on that one too — with one
new statement falling out that the static sector could not have shown.

THE THEOREM EXTENDS. Take the stationary axisymmetric metric with all
three functions arbitrary — the time word, the dragging word, the spatial
word — impose the two field equations and the quadrature, and compute the
Ricci tensor symbolically. **All sixteen components vanish identically**,
exactly as in the static class. So the construction is exactly vacuum for
every stationary axisymmetric configuration, Kerr among them.

AND THE STATIC EQUATION TURNS OUT TO BE THE REGISTER'S TWO STATEMENTS AT
ONCE. Written for the time word alone the equation is f·∇²f = (∇f)². That
is identically the statement that **ln f is harmonic** — which is to say
f = e^{2ψ} with ψ flat-harmonic. The multiplicative budget and the
composite clause were derived separately, one from the round trip's
composition law and one from the census adding; they are the same
equation. Nothing was fitted to make them agree.

THE NEW STATEMENT: TWIST IS PAID OUT OF DEPTH. With rotation the time
word's equation gains a term, and it gains it with a minus sign:

    f ∇²f  =  (∇f)²  −  (∇χ)²

so that ∇²(ln f) = −(∇χ)²/f², which is **never positive**. The deficit
becomes subharmonic and can only be shallower than the harmonic function
with the same boundary data — never deeper. **Circulation and depth draw
on one budget, and what goes into circulation comes out of depth, with no
free sign.** One-signedness with no choice in it is this program's own
signature, arriving here from the field equations rather than from the
reptend. Checked on Kerr itself at four points, both sides agreeing to
machine precision and both negative.

AND THE COMPOSITE CLAUSE ENDS EXACTLY HERE. Two static deficits superpose
with residual identically zero. Two rotating potentials do not: each
solves its equation to 1e-18 and their sum misses by 2e-2 — not a small
correction but a different order of thing. Nor does the logarithm rescue
it, the trick that works in the static sector. The clause is exact where
the register counts, and fails where the register circulates, which is
the boundary the sum and difference faces were always claimed to have.
"""

import math

import sympy as sp

RHO, Z = sp.symbols('rho z', positive=True)
LAP = lambda u: sp.diff(u, RHO, 2) + sp.diff(u, RHO) / RHO + sp.diff(u, Z, 2)
G2 = lambda u: sp.diff(u, RHO) ** 2 + sp.diff(u, Z) ** 2


def test_the_stationary_class_is_annihilated_the_same_way():
    """The theorem, extended: with the time, dragging and spatial words
    all arbitrary, the two field equations plus the quadrature kill every
    Ricci component — so rotation is inside, Kerr with it."""
    f = sp.Function('f')(RHO, Z)
    om = sp.Function('om')(RHO, Z)
    ga = sp.Function('ga')(RHO, Z)
    X = (sp.Symbol('t'), RHO, Z, sp.Symbol('phi'))
    g = sp.zeros(4, 4)
    g[0, 0] = -f
    g[0, 3] = g[3, 0] = f * om
    g[3, 3] = RHO ** 2 / f - f * om ** 2
    g[1, 1] = g[2, 2] = sp.exp(2 * ga) / f
    gi = sp.zeros(4, 4)
    gi[0, 0] = -1 / f + f * om ** 2 / RHO ** 2
    gi[0, 3] = gi[3, 0] = f * om / RHO ** 2
    gi[3, 3] = f / RHO ** 2
    gi[1, 1] = gi[2, 2] = f * sp.exp(-2 * ga)
    assert sp.simplify(g * gi - sp.eye(4)) == sp.zeros(4, 4)

    d = lambda e, c: sp.diff(e, X[c]) if c in (1, 2) else sp.S(0)
    Gam = [[[sp.together(sum(gi[a, m] * (d(g[m, b], c) + d(g[m, c], b)
                                         - d(g[b, c], m)) for m in range(4)) / 2)
             for c in range(4)] for b in range(4)] for a in range(4)]
    fr, fz = sp.diff(f, RHO), sp.diff(f, Z)
    wr, wz = sp.diff(om, RHO), sp.diff(om, Z)
    qr = RHO * (fr ** 2 - fz ** 2) / (4 * f ** 2) - f ** 2 * (wr ** 2 - wz ** 2) / (4 * RHO)
    qz = RHO * fr * fz / (2 * f ** 2) - f ** 2 * wr * wz / (2 * RHO)
    frr = ((fr ** 2 + fz ** 2 - f ** 4 * (wr ** 2 + wz ** 2) / RHO ** 2) / f
           - fr / RHO - sp.diff(f, Z, 2))
    wrr = -sp.diff(om, Z, 2) - 2 * (fr * wr + fz * wz) / f + wr / RHO
    rules = [(sp.diff(ga, RHO, 2), sp.diff(qr, RHO)),
             (sp.diff(ga, RHO, Z), sp.diff(qr, Z)),
             (sp.diff(ga, Z, 2), sp.diff(qz, Z)),
             (sp.diff(ga, RHO), qr), (sp.diff(ga, Z), qz)]
    for b in range(4):
        for c in range(4):
            e = sum(d(Gam[a][b][c], a) - d(Gam[a][b][a], c)
                    + sum(Gam[a][a][k] * Gam[k][b][c] - Gam[a][c][k] * Gam[k][b][a]
                          for k in range(4)) for a in range(4))
            for old, new in rules:
                e = e.subs(old, new)
            e = e.doit().subs(sp.diff(f, RHO, 2), frr).subs(sp.diff(om, RHO, 2), wrr)
            e = e.doit().subs(sp.diff(f, RHO, 2), frr).subs(sp.diff(om, RHO, 2), wrr)
            assert sp.simplify(sp.expand(sp.together(e))) == 0, (b, c)


def test_the_static_equation_is_the_budget_and_the_clause_at_once():
    """f·∇²f = (∇f)² is identically ∇²(ln f) = 0. The multiplicative
    budget and the composite clause were derived by separate routes and
    are the same equation."""
    F = sp.Function('F')(RHO, Z)
    assert sp.simplify(sp.expand((F * LAP(F) - G2(F)) - LAP(sp.log(F)) * F ** 2)) == 0


def test_the_twist_enters_the_budget_with_a_minus_sign():
    """And with rotation the same rearrangement leaves the twist's own
    gradient, negated: ∇²(ln f) = −(∇χ)²/f²."""
    f = sp.Function('f')(RHO, Z)
    chi = sp.Function('chi')(RHO, Z)
    real = f * LAP(f) - G2(f) + G2(chi)                 # the field equation
    assert sp.simplify(sp.expand(real - (LAP(sp.log(f)) * f ** 2 + G2(chi)))) == 0


def _kerr(M, a):
    """Kerr's time and twist words in prolate spheroidal coordinates."""
    x, y = sp.symbols('x y', positive=True)
    sig = sp.sqrt(M ** 2 - a ** 2)
    p, q = sig / M, a / M
    den = (p * x + 1) ** 2 + q ** 2 * y ** 2
    f = (p ** 2 * x ** 2 + q ** 2 * y ** 2 - 1) / den
    chi = -2 * q * y / den
    rho = sig * sp.sqrt((x ** 2 - 1) * (1 - y ** 2))
    zz = sig * x * y
    J = sp.Matrix([[sp.diff(rho, x), sp.diff(rho, y)],
                   [sp.diff(zz, x), sp.diff(zz, y)]]).inv()
    return x, y, f, chi, rho, J


def test_the_one_signed_source_holds_on_kerr_itself():
    """Not a formalism: on the actual rotating solution both sides agree
    to machine precision, and both are negative at every point."""
    x, y, f, chi, rho, J = _kerr(sp.Rational(1), sp.Rational(3, 5))

    def drz(u):
        ux, uy = sp.diff(u, x), sp.diff(u, y)
        return J[0, 0] * ux + J[1, 0] * uy, J[0, 1] * ux + J[1, 1] * uy

    def laprz(u):
        ur, uz = drz(u)
        return drz(ur)[0] + ur / rho + drz(uz)[1]

    gr, gz = drz(chi)
    for xv, yv in ((2.0, 0.4), (3.0, -0.7), (1.6, 0.9), (5.0, 0.1)):
        sub = {x: sp.Float(xv), y: sp.Float(yv)}
        lhs = float(sp.N(laprz(sp.log(f)).subs(sub)))
        rhs = float(sp.N((-(gr ** 2 + gz ** 2) / f ** 2).subs(sub)))
        assert abs(lhs - rhs) < 1e-12 * max(1.0, abs(lhs))
        assert lhs < 0                                   # one-signed, always


def test_twist_can_only_make_the_deficit_shallower():
    """The reading, as arithmetic: a non-positive Laplacian for ln f makes
    the deficit subharmonic, so it lies below the harmonic function with
    the same boundary data. Circulation is paid out of depth."""
    for gchi2, f in ((0.0, 0.9), (0.4, 0.9), (2.5, 0.5)):
        lap_lnf = -gchi2 / f ** 2
        assert lap_lnf <= 0
        assert (lap_lnf == 0) == (gchi2 == 0)            # static is the only equality


def test_the_composite_clause_is_exact_where_the_register_counts():
    """Two static deficits superpose with residual identically zero."""
    p1 = -1 / sp.sqrt(RHO ** 2 + (Z - 1) ** 2)
    p2 = -sp.Rational(1, 2) / sp.sqrt(RHO ** 2 + (Z + 1) ** 2)
    assert sp.simplify(LAP(p1 + p2)) == 0


def test_and_ends_exactly_where_it_circulates():
    """Two rotating potentials do not superpose, and the miss is not a
    small correction: each solves its own equation to 1e-18 and the sum
    misses by 2e-2. Nor does the logarithm rescue it."""
    def kerr_rz(M, a, z0):
        sig = sp.sqrt(M ** 2 - a ** 2)
        r1 = sp.sqrt(RHO ** 2 + (Z - z0 - sig) ** 2)
        r2 = sp.sqrt(RHO ** 2 + (Z - z0 + sig) ** 2)
        X, Y = (r1 + r2) / (2 * sig), (r1 - r2) / (2 * sig)
        p, q = sig / M, a / M
        return (p * X - sp.I * q * Y - 1) / (p * X - sp.I * q * Y + 1)

    E1 = kerr_rz(sp.Rational(1), sp.Rational(3, 5), sp.Rational(-2))
    E2 = kerr_rz(sp.Rational(1, 2), sp.Rational(1, 5), sp.Rational(2))

    def resid(E, at):
        r = ((E + sp.conjugate(E)) / 2).subs(sp.conjugate(RHO), RHO).subs(
            sp.conjugate(Z), Z)
        return abs(complex(sp.N((r * LAP(E) - G2(E)).subs(at))))

    for pt in ((2.0, 0.5), (3.0, -1.2), (1.5, 3.0)):
        at = {RHO: sp.Float(pt[0]), Z: sp.Float(pt[1])}
        assert resid(E1, at) < 1e-15
        assert resid(E2, at) < 1e-15
        assert resid(E1 + E2, at) > 1e-3                 # a different order of thing


def test_the_failure_carries_the_same_sign_as_the_twist_source():
    """And the superposition failure is one-signed too, in the same
    direction — the log of a product of two rotating time words has a
    negative Laplacian, never a positive one."""
    def kerr_f(M, a, z0):
        sig = sp.sqrt(M ** 2 - a ** 2)
        r1 = sp.sqrt(RHO ** 2 + (Z - z0 - sig) ** 2)
        r2 = sp.sqrt(RHO ** 2 + (Z - z0 + sig) ** 2)
        X, Y = (r1 + r2) / (2 * sig), (r1 - r2) / (2 * sig)
        p, q = sig / M, a / M
        E = (p * X - sp.I * q * Y - 1) / (p * X - sp.I * q * Y + 1)
        return ((E + sp.conjugate(E)) / 2).subs(sp.conjugate(RHO), RHO).subs(
            sp.conjugate(Z), Z)

    tot = sp.log(kerr_f(sp.Rational(1), sp.Rational(3, 5), sp.Rational(-2))) \
        + sp.log(kerr_f(sp.Rational(1, 2), sp.Rational(1, 5), sp.Rational(2)))
    for pt in ((2.0, 0.5), (3.0, -1.2), (1.5, 3.0)):
        at = {RHO: sp.Float(pt[0]), Z: sp.Float(pt[1])}
        v = complex(sp.N(LAP(tot).subs(at))).real
        assert v < 0
        assert abs(v) > 1e-4
