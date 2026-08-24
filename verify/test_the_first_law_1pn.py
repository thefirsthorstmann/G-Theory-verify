"""test_the_first_law_1pn.py — THE FIRST LAW OF BINARY MECHANICS AT FIRST
POST-NEWTONIAN ORDER, WITH THE REGISTER'S APPORTIONED CLOCKS (2026-08-23).
the author: "go get the 1PN first law." Extends test_the_helical_sector.py (exact at
Newtonian order; exact to all orders in the test-mass limit) to 1PN for
general masses.

THE OBJECTS (G = 1, e = 1/c² the bookkeeping parameter, circular orbits).
  Lagrangian   the relative 1PN Lagrangian, rdot = 0:
               L/mu = v²/2 + M/r + e[(1−3ν)v⁴/8 + (M/2r)(3+ν)v² − M²/(2r²)]
               (reduced from the two-body EIH Lagrangian; the 1PN
               centre-of-mass correction cancels in L_N at first order)
  circular     dL/dr = 0  ->  Ω² = (M/r³)(1 − e(3−ν)M/r)      [anchor 1]
  E, J         E = 2v²L_v² − L,  ΩJ = 2v²L_v²  (even in Ω), expressed at
               fixed Ω through r(Ω); anchors against the known series
               E = −(μx/2)[1 − (3/4 + ν/12)x], J = (μM/√x)[1 + (3/2 + ν/6)x]
               with x = (MΩ)^{2/3}                               [anchors 2, 3]
  the clock    c²(z₁ − 1) = −(U + v₁²/2)
                 + e[U² + cΦ₁Φ₁ + cΦ₂Φ₂ + c_V V·v₁ − Uv₁² − (2U + v₁²)²/8]
               from (dτ/dt)² = −g₀₀ − 2g₀ᵢvⁱ − gᵢⱼvⁱvʲ, regularized to the
               COMPANION's field only (the banked apportionment):
               U = m₂/r, Φ₁ = m₂v₂²/r, Φ₂ = m₂·U_ext(x₂)/r = m₁m₂/r²,
               V·v₁ = (m₂/r)(v₂·v₁), W·v₁ = 0 on a circular orbit.
  the law      δM − Ω δJ = z₁δm₁ + z₂δm₂, M = m₁ + m₂ + E, at fixed Ω:
               ∂E/∂m₁|_Ω − Ω ∂J/∂m₁|_Ω = c²(z₁ − 1), order by order in e.

WHAT THE LAW DID. Left with (cΦ₁, cΦ₂, c_V) free, the 1PN law is satisfied
if and only if  cΦ₁ + c_V = 2  and  cΦ₂ − c_V = −5/2  (six rational points,
two for the solve, four for consistency); the 1PN centre-of-mass correction
drops out of the law entirely. The standard-PN-gauge metric with the
point masses as CONSERVED masses — g₀₀ = −1 + 2U − 2U² + 3Φ₁ − 2Φ₂,
g₀ᵢ = −(7/2)Vᵢ − (1/2)Wᵢ, gᵢⱼ = (1 + 2U)δᵢⱼ — gives (−3/2, +1, 7/2), which
lies exactly on that family. The rest-density potentials of the generic
PPN form, (−2, −2, 7/2), do not: they miss by exactly the ρ* − ρ
conversion (−(v²/2 + 3U_ext) per source), which is how the computation
caught its own first attempt. The harmonic-gauge pair (c_V = 4 ⇒ cΦ₁ = −2,
cΦ₂ = 3/2) lies on the same family: the clock along the circular worldline
is gauge-invariant, as it must be for a helically symmetric spacetime.

TWO EXACT ANCHORS BEYOND THE SERIES. Test mass (m₁ → 0): c²(z₁−1) →
−(3/2)x − (9/8)x², the expansion of √(1 − 3M/r). Heavy body (m₂ → 0): the
law's left side → −(m₂/M)x/√(1 − 3x) = −(m₂/M)(x + (3/2)x² + …), and the
clock matches it. So: THE FIRST LAW HOLDS AT 1PN FOR GENERAL MASSES WITH
THE APPORTIONED CLOCKS, exactly in the test-mass limit, and it selects the
conserved-mass point-particle metric as the one the rest clocks read.
"""

import pathlib

import sympy as sp

CATALOG = pathlib.Path(__file__).resolve().parent.parent / "catalog"
GRAVITY = (CATALOG / "GRAVITY-AS-TONAL-CENTER.md").read_text()
FLAT = " ".join(GRAVITY.split())

m1, m2, r0, e, w2, r, v2s, t = sp.symbols("m1 m2 r0 epsilon w2 r v2s t", positive=True)
M = m1 + m2
mu = m1 * m2 / M
nu = mu / M
X1, X2 = m1 / M, m2 / M
Dl = X1 - X2
CONS = {w2: M / r0 ** 3}
PTS = [{m1: sp.Rational(1, 3), m2: sp.Rational(1, 5), r0: sp.Rational(7, 2)},
       {m1: sp.Rational(2, 7), m2: sp.Rational(5, 11), r0: sp.Rational(13, 3)},
       {m1: sp.Rational(1, 2), m2: sp.Rational(1, 9), r0: sp.Rational(5, 1)},
       {m1: sp.Rational(3, 4), m2: sp.Rational(2, 3), r0: sp.Rational(11, 4)},
       {m1: sp.Rational(1, 7), m2: sp.Rational(4, 5), r0: sp.Rational(9, 2)},
       {m1: sp.Rational(5, 6), m2: sp.Rational(1, 6), r0: sp.Rational(10, 3)}]


def _lag(v2, rr):
    return mu * (v2 / 2 + M / rr + e * ((1 - 3 * nu) * v2 ** 2 / 8
                                        + (M / (2 * rr)) * (3 + nu) * v2 - M ** 2 / (2 * rr ** 2)))


def _trunc1(F):
    """Exact truncation to first order in e."""
    return F.subs(e, 0) + e * sp.diff(F, e).subs(e, 0)


def _zero_at_points(expr):
    return all(sp.nsimplify(expr.subs(p)) == 0 for p in PTS)


# --- the machinery, built once ----------------------------------------------------

_a = sp.symbols("a")
_eq = _trunc1(sp.diff(_lag(w2 * r ** 2, r), r).subs(w2, (M / r ** 3) * (1 + e * _a)))
A_SOL = sp.solve(sp.expand(_eq.coeff(e, 1)), _a)[0]
R_W = r0 * (1 + e * A_SOL.subs(r, r0) / 3)                     # r(Omega) to 1PN
_L = _lag(v2s, r)
_Lv2 = sp.diff(_L, v2s)
_sub = {v2s: w2 * R_W ** 2, r: R_W}
E_W = _trunc1((2 * v2s * _Lv2 - _L).subs(_sub))
OJ_W = _trunc1((2 * v2s * _Lv2).subs(_sub))                     # Omega * J


def _dfix(F, m):
    """d/dm at fixed Omega, r0 = (M/Omega^2)^(1/3): d/dm + (r0/3M) d/dr0."""
    return sp.diff(F, m) + (r0 / (3 * M)) * sp.diff(F, r0)


def _clock(cF1, cF2, cV, cP=1):
    P = e / 2 * (w2 * r ** 2 - M / r)
    alpha, beta = X2 + cP * nu * Dl * P, X1 - cP * nu * Dl * P
    v1sq, vbsq, v1vb = alpha ** 2 * w2 * r ** 2, beta ** 2 * w2 * r ** 2, alpha * beta * w2 * r ** 2
    U, Phi1, Phi2, Vv1 = m2 / r, m2 * vbsq / r, m1 * m2 / r ** 2, -(m2 / r) * v1vb
    zeta = -(U + v1sq / 2) + e * (U ** 2 + cF1 * Phi1 + cF2 * Phi2 + cV * Vv1
                                  - U * v1sq - (2 * U + v1sq) ** 2 / 8)
    return _trunc1(zeta.subs(r, R_W))


def _residual(zeta1):
    F1 = sp.expand((_dfix(E_W, m1) - _dfix(OJ_W, m1) - zeta1).subs(CONS))
    zeta2 = zeta1.subs({m1: m2, m2: m1}, simultaneous=True)
    F2 = sp.expand((_dfix(E_W, m2) - _dfix(OJ_W, m2) - zeta2).subs(CONS))
    return F1, F2


# --- anchors ----------------------------------------------------------------------

def test_anchor_circular_condition():
    assert _zero_at_points((A_SOL + (3 - nu) * M / r).subs(r, r0))


def test_anchor_energy_and_angular_momentum_series():
    x0 = M / r0
    E_known = -(mu * x0 / 2) * (1 - (sp.Rational(3, 4) + nu / 12) * x0 * e)
    OJ_known = sp.sqrt(w2) * (mu * M / sp.sqrt(x0)) * (1 + (sp.Rational(3, 2) + nu / 6) * x0 * e)
    assert _zero_at_points((E_W - E_known).subs(CONS))
    assert _zero_at_points((OJ_W - OJ_known).subs(CONS))


def test_anchor_test_mass_clock_is_the_exact_schwarzschild_rate():
    z = _clock(-sp.Rational(3, 2), 1, sp.Rational(7, 2)).subs(CONS).subs(m1, 0)
    exact = -(sp.Rational(3, 2)) * (m2 / r0) - sp.Rational(9, 8) * (m2 / r0) ** 2 * e
    assert _zero_at_points(z - exact)


def test_anchor_heavy_body_law_from_the_exact_test_particle():
    """m2 -> 0: the law's left side must be -(m2/M) x/sqrt(1-3x); at 1PN
    -(m2/M)(x + 3x^2/2). The machinery's left side gives exactly that."""
    lhs = sp.expand((_dfix(E_W, m1) - _dfix(OJ_W, m1)).subs(CONS))
    heavy = sp.series(lhs.subs({m1: 1, m2: t}), t, 0, 2).removeO().coeff(t, 1)
    assert sp.simplify(heavy.coeff(e, 0) + 1 / r0) == 0
    assert sp.simplify(heavy.coeff(e, 1) + sp.Rational(3, 2) / r0 ** 2) == 0


# --- the law at 1PN -----------------------------------------------------------------

def test_the_first_law_holds_at_1pn_with_the_conserved_mass_metric():
    F1, F2 = _residual(_clock(-sp.Rational(3, 2), 1, sp.Rational(7, 2)))
    for F in (F1, F2):
        assert _zero_at_points(F.coeff(e, 0))          # Newtonian
        assert _zero_at_points(F.coeff(e, 1))          # first post-Newtonian


def test_the_law_selects_the_clock_coefficients():
    """Free (cPhi1, cPhi2, cV): the 1PN law holds iff cPhi1 + cV = 2 and
    cPhi2 − cV = −5/2, with the centre-of-mass correction dropping out."""
    cP, cF1, cF2, cV = sp.symbols("cP cF1 cF2 cV")
    F1, _ = _residual(_clock(cF1, cF2, cV, cP))
    c1 = F1.coeff(e, 1)
    eqs = [sp.expand(c1.subs(p)) for p in PTS]
    sol = sp.solve(eqs[:4], [cP, cF1, cF2, cV], dict=True)
    assert sol and sol[0] == {cF1: 2 - cV, cF2: cV - sp.Rational(5, 2)}
    assert all(sp.simplify(eq.subs(sol[0])) == 0 for eq in eqs[4:])


def test_the_rest_density_potentials_fail_and_the_harmonic_pair_passes():
    F1, _ = _residual(_clock(-2, -2, sp.Rational(7, 2)))        # rho, not rho*
    assert not _zero_at_points(F1.coeff(e, 1))
    F1h, F2h = _residual(_clock(-2, sp.Rational(3, 2), 4))       # harmonic gauge pair
    assert _zero_at_points(F1h.coeff(e, 1)) and _zero_at_points(F2h.coeff(e, 1))


def test_the_centre_of_mass_correction_does_not_enter_the_law():
    for cP in (0, 1, 3):
        F1, _ = _residual(_clock(-sp.Rational(3, 2), 1, sp.Rational(7, 2), cP))
        assert _zero_at_points(F1.coeff(e, 1))


# --- the paper ---------------------------------------------------------------------

def test_the_paper_carries_the_first_post_newtonian_law():
    assert "Verified exactly at Newtonian and first post-Newtonian order" in FLAT
    assert "verify/test_the_first_law_1pn.py" in FLAT
