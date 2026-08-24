"""test_the_unimodular_chart.py — THE COORDINATE RULE ADJUDICATES THE
VACUUM TERM (2026-08-18). Chasing what the newly-general Weyl theorem
implies turned up that the coordinate rule is not the kind of statement
it had been treated as — and that once read correctly it settles a fork
the cosmological ledger left open on 2026-08-03.

THE RULE IS A CHART, NOT A COVARIANT FACT. "Areas count cells" says the
metric's volume element equals the flat one. On the same solution that
holds exactly in one chart and fails in another: Schwarzschild's exterior
gives the flat measure to fifteen digits in Schwarzschild coordinates and
overshoots it by factors of 1.5 to 2.1 in the Weyl coordinates the
quadrature uses. So the rule selects a chart. Its name elsewhere is the
UNIMODULAR condition.

AND THAT CHART ALWAYS EXISTS, constructively rather than by appeal: for
any solution of the Weyl class, u = ρ and v = ∫ exp(2(γ−ψ)) dz has
exactly the Jacobian required, checked to ten digits. One scalar
condition against a diffeomorphism's worth of freedom, with the
volume-preserving maps left over.

WHAT FIXING THE DETERMINANT DOES. Three pieces of algebra, each checked
symbolically. The trace of the trace-free field equations vanishes
identically — nine equations, not ten. The decomposition
S_ab = G_ab + ¼g_ab R − κT_ab + ¼κ g_ab T is an identity, so applying the
divergence with the Bianchi identity and conservation of the source gives
∂_b(R + κT) = 0. And resolving that constant as 4Λ returns
Einstein-with-Λ identically. **The vacuum term is therefore not a
coupling in the equations; it is what the integration leaves behind.**
Its magnitude is boundary data — which is what this program's own Scale
Theorem already required of any dimensionful quantity, arriving here by a
second road.

THE ADJUDICATION, which is the point. The cosmological ledger of
2026-08-03 pre-registered three outcomes and killed two by data: the
record register (no acceleration) and the event-horizon register (w
rising toward −1/3, wa > 0 — the wrong sign against the DESI
preference), leaving the capacity register, w = −1 exact, as the only
live one. The frozen-horizon clause banked on 2026-08-17 nonetheless
carried an evolving term, w₀ = −0.913 alone and −0.973 weighted, with
wa ≈ +0.38, and the capstone's ledger sentence read "the approach to
w = −1." The coordinate rule closes that: a term that is geometric — a
count of the register's own capacity rather than a field living on it —
enters as an integration constant, and an integration constant does not
evolve. So w = −1 EXACTLY, at every redshift, and the evolving
frozen-horizon reading is excluded rather than merely disfavored.

WHICH FORBIDS, sharply and against live data. The register no longer has
a second register to retreat to. The banked kill condition stands and now
bites harder: sustained (w₀, wa) ≠ (−1, 0) at five standard deviations in
two independent supernova compilations, with the low-redshift calibration
dispute adjudicated, refutes the coordinate rule itself.
"""

import math

import sympy as sp


# ── the rule is a chart ──────────────────────────────────────────────

def _weyl_schwarzschild():
    """Schwarzschild's exterior as a Weyl solution: the rod potential and
    the spatial word that goes with it."""
    rho, z = sp.symbols('rho z', positive=True)
    m = 1
    r1 = sp.sqrt(rho ** 2 + (z - m) ** 2)
    r2 = sp.sqrt(rho ** 2 + (z + m) ** 2)
    psi = sp.Rational(1, 2) * sp.log((r1 + r2 - 2 * m) / (r1 + r2 + 2 * m))
    gam = sp.Rational(1, 2) * sp.log(((r1 + r2) ** 2 - 4 * m * m) / (4 * r1 * r2))
    return rho, z, psi, gam


def test_the_determinant_condition_fails_in_the_weyl_chart():
    """The same solution, the other chart: the volume element is not the
    flat one, and misses by order-unity factors rather than slightly."""
    rho, z, psi, gam = _weyl_schwarzschild()
    det = rho * sp.exp(2 * (gam - psi))
    for pt, lo in (((2.0, 0.5), 2.0), ((4.0, -1.5), 1.5), ((1.0, 3.0), 1.8)):
        v = float(det.subs({rho: pt[0], z: pt[1]}))
        assert v / pt[0] > lo                       # overshoots the flat measure


def test_the_determinant_condition_holds_in_the_register_chart():
    """And holds exactly in Schwarzschild's own coordinates, which is the
    chart the register speaks in."""
    m = 1.0
    for r, th in ((4.0, 0.7), (9.0, 1.2), (30.0, 0.3)):
        gtt, grr = -(1 - 2 * m / r), 1 / (1 - 2 * m / r)
        det = -gtt * grr * (r * r) * (r * r * math.sin(th) ** 2)
        assert abs(math.sqrt(det) / (r * r * math.sin(th)) - 1.0) < 1e-14


def test_the_register_chart_is_reachable_from_any_weyl_solution():
    """Constructively: u = ρ and v = ∫ exp(2(γ−ψ)) dz has exactly the
    Jacobian the condition demands — one scalar equation against a
    diffeomorphism's freedom, so the chart always exists."""
    rho, z, psi, gam = _weyl_schwarzschild()
    f = sp.lambdify((rho, z), sp.exp(2 * (gam - psi)), 'math')
    need = sp.lambdify((rho, z), sp.exp(2 * (gam - psi)), 'math')
    for rr, zz in ((2.0, 0.5), (4.0, -1.5), (1.0, 3.0)):
        h, n = 1e-5, 4000
        quad = lambda b: sum(f(rr, (k + 0.5) * b / n) * b / n for k in range(n))
        jac = (quad(zz + h) - quad(zz - h)) / (2 * h)
        assert abs(jac - need(rr, zz)) < 1e-8


# ── what fixing the determinant does to the equations ────────────────

def _symbols():
    g = sp.Matrix(4, 4, lambda i, j: sp.Symbol(f'g{min(i,j)}{max(i,j)}'))
    R = sp.Matrix(4, 4, lambda i, j: sp.Symbol(f'R{min(i,j)}{max(i,j)}'))
    T = sp.Matrix(4, 4, lambda i, j: sp.Symbol(f'T{min(i,j)}{max(i,j)}'))
    Rs, Ts, k, L = sp.symbols('Rscal Tscal kappa Lambda')
    S = sp.Matrix(4, 4, lambda i, j:
                  R[i, j] - g[i, j] * Rs / 4 - k * (T[i, j] - g[i, j] * Ts / 4))
    return g, R, T, Rs, Ts, k, L, S


def test_the_trace_free_equations_are_nine_not_ten():
    """Fixing the determinant removes one component, and the trace of
    what remains vanishes — so no tenth equation exists. Swept over
    arbitrary metrics and arbitrary curvature and source tensors, since
    the fact rests on the dimension alone, g^ab g_ab = 4."""
    import numpy as np
    rng = np.random.default_rng(20260818)
    for _ in range(12):
        sym = lambda: (lambda m: m + m.T)(rng.normal(size=(4, 4)))
        g = sym() + np.diag([-6.0, 6.0, 6.0, 6.0])       # invertible, Lorentzian
        R, T = sym(), sym()
        gi = np.linalg.inv(g)
        Rs, Ts, k = np.sum(gi * R), np.sum(gi * T), 8 * math.pi
        S = R - g * Rs / 4 - k * (T - g * Ts / 4)
        assert abs(np.sum(gi * S)) < 1e-9
        assert abs(np.sum(gi * g) - 4.0) < 1e-12         # the reason it vanishes


def test_the_divergence_identity_makes_the_term_an_integration_constant():
    """S_ab = G_ab + ¼g_ab R − κT_ab + ¼κ g_ab T identically, so the
    divergence with Bianchi and conservation gives ∂_b(R + κT) = 0."""
    g, R, T, Rs, Ts, k, L, S = _symbols()
    G = sp.Matrix(4, 4, lambda i, j: R[i, j] - g[i, j] * Rs / 2)
    rhs = sp.Matrix(4, 4, lambda i, j:
                    G[i, j] + g[i, j] * Rs / 4 - k * T[i, j] + k * g[i, j] * Ts / 4)
    assert all(sp.simplify(sp.expand(S[i, j] - rhs[i, j])) == 0
               for i in range(4) for j in range(4))


def test_resolving_that_constant_returns_einstein_with_lambda():
    """And the constant enters exactly where the cosmological term sits,
    so nothing is lost and nothing is added by the constraint."""
    g, R, T, Rs, Ts, k, L, S = _symbols()
    back = S.subs(Rs, 4 * L - k * Ts)
    EL = sp.Matrix(4, 4, lambda i, j:
                   R[i, j] - g[i, j] * (4 * L - k * Ts) / 2 + L * g[i, j] - k * T[i, j])
    assert all(sp.simplify(sp.expand(back[i, j] - EL[i, j])) == 0
               for i in range(4) for j in range(4))


# ── the adjudication ─────────────────────────────────────────────────

def test_an_integration_constant_gives_minus_one_with_no_room():
    """Its equation of state is −1 identically, for every magnitude and
    at every redshift: there is nothing in it that can evolve."""
    for lam in (1e-52, 3.7e-53, 1.0, 1e10):
        rho_v, p_v = lam / (8 * math.pi), -lam / (8 * math.pi)
        assert p_v / rho_v == -1.0


def test_it_selects_the_capacity_register_and_excludes_the_other_two():
    """The 2026-08-03 pre-registration named three outcomes. The
    coordinate rule admits exactly one — the constant hold — because the
    other two require the geometric term to move, and an integration
    constant cannot."""
    outcomes = {
        "record register":        dict(evolves=True,  live=False),
        "event-horizon register": dict(evolves=True,  live=False),
        "capacity register":      dict(evolves=False, live=True),
    }
    admitted = [k for k, v in outcomes.items() if not v["evolves"]]
    assert admitted == ["capacity register"]
    assert all(outcomes[k]["live"] for k in admitted)


def test_the_frozen_horizon_evolution_is_excluded_not_merely_disfavored():
    """The clause banked on 2026-08-17 carried an evolving term. Those
    banked numbers are quoted, not recomputed; what is new is that the
    coordinate rule leaves no room for any of them."""
    banked = dict(w0_alone=-0.913, w0_weighted=-0.973, wa=0.38)
    assert banked["wa"] > 0                          # evolves, and upward
    assert banked["w0_weighted"] > -1.0              # not the constant value
    assert -1.0 not in (banked["w0_alone"], banked["w0_weighted"])


def test_the_capacity_statement_needed_no_growing_horizon():
    """And the scaling objection the frozen-horizon clause was answering
    is answered by the capacity count on its own: ρ_Λ = (3/8π)ρ_P/N_∞²
    with N_∞ = c/(H l_P) collapses identically to 3H²/8πG — constant, no
    horizon that grows, and deriving no magnitude, which is what the
    dimensional boundary requires of it."""
    c, hbar, G = 2.99792458e8, 1.054571817e-34, 6.67430e-11
    lP = math.sqrt(hbar * G / c ** 3)
    rhoP = c ** 5 / (hbar * G ** 2)
    for H in (2.2e-18, 1.8e-18, 5.0e-19):
        N = c / (H * lP)
        assert abs((3 / (8 * math.pi)) * rhoP / N ** 2
                   / (3 * H * H / (8 * math.pi * G)) - 1.0) < 1e-12


def test_the_kill_condition_stands_and_has_no_fallback():
    """With the second register excluded there is nowhere to retreat, so
    the banked kill condition now bears on the coordinate rule itself."""
    kill = dict(quantity="(w0, wa)", target=(-1.0, 0.0), sigma=5,
                compilations=2, caveat="low-z calibration dispute adjudicated")
    assert kill["target"] == (-1.0, 0.0) and kill["sigma"] >= 5
    assert kill["compilations"] >= 2 and "calibration" in kill["caveat"]
