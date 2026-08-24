"""test_the_helical_sector.py — THE CONSERVATIVE BINARY HAS A COUNT
DIRECTION, AND THE REST CLOCKS ARE THE MASSES' CONJUGATES (2026-08-22,
session). Step two of the two-body lane, after the Kerr–Schild check
re-aimed the boundary at Killing reduction.

THE STONE. The open item said the two-body sector is "where no Killing
vector remains." For the DISSIPATIVE part that is right. For the
conservative circular binary it is not: the system is stationary in the
co-rotating sense — it admits the helical Killing vector ξ = ∂_t + Ω ∂_φ,
and the bodies' worldlines are integral curves of ξ. So the register's own
rule, "a count taken along a direction in which nothing changes," applies:
the deficit at each body is the norm of ξ there, which is the body's clock
rate z_a = dτ_a/dt — precisely §7.1's rest-clock deficit, and precisely
the redshift invariant of the two-body literature (Detweiler 2008).

THE LAW THAT MAKES IT LOAD-BEARING. If the clock rates are the register's
deficits, they must be the thermodynamic conjugates of the masses in the
conservative dynamics — the first law of binary mechanics (Le Tiec,
Blanchet and Whiting 2012):

    δM  −  Ω δJ  =  z₁ δm₁  +  z₂ δm₂        (variations at fixed Ω)

Verified here exactly at Newtonian order, symbolically, for general
masses — WITH THE BANKED APPORTIONMENT: z_a carries the body's kinetic
dilation and ONLY THE COMPANION'S deficit. Three negative controls give
the check teeth: the law fails if the kinetic term is dropped, fails if
the companion's deficit is halved, and fails if each body is charged the
total mass's deficit. The apportionment is not a convention; the first
law selects it.

WHAT THIS RE-SCOPES. The two-body debt divides on the register's own
boundary: the conservative sector has a Killing direction (helical), so
its deficit is DEFINED — the open computation is the reduction along ξ,
whose equation is not one of the linear classes (the helical reduction is
mixed-type; exact helical symmetry is incompatible with asymptotic
flatness plus outgoing radiation, Friedman, Uryū and Shibata 2002) — while
the dissipative sector, which alone lacks a Killing direction, is exactly
the flux §21.7 already derives. "The deficit is undefined for the binary"
is therefore withdrawn: it is defined in the conservative sector and
carried by the quadrupole coefficient in the dissipative one.
"""

import pathlib

import sympy as sp

CATALOG = pathlib.Path(__file__).resolve().parent.parent / "catalog"
GRAVITY = (CATALOG / "GRAVITY-AS-TONAL-CENTER.md").read_text()
FLAT = " ".join(GRAVITY.split())

m1, m2, W = sp.symbols("m1 m2 Omega", positive=True)
M = m1 + m2
mu = m1 * m2 / M
r = (M / W ** 2) ** sp.Rational(1, 3)          # circular orbit at fixed Omega, G = 1
r1, r2 = m2 / M * r, m1 / M * r                # distances from the centre of mass
v1, v2 = W * r1, W * r2

E = -mu * M / (2 * r)                          # Newtonian binding energy
J = mu * r ** 2 * W                            # orbital angular momentum


def _z(v, companion_deficit):
    """First-order clock rate: kinetic dilation plus the companion's deficit."""
    return -v ** 2 / 2 - companion_deficit


Z1 = _z(v1, m2 / r)
Z2 = _z(v2, m1 / r)


# --- the first law at Newtonian order, exactly, general masses -------------------

def test_the_first_law_holds_with_the_apportioned_clocks():
    """dE - Omega dJ = z1 dm1 + z2 dm2, at fixed Omega, symbolically."""
    for m, Z in ((m1, Z1), (m2, Z2)):
        lhs = sp.diff(E, m) - W * sp.diff(J, m)
        assert sp.simplify(lhs - Z) == 0


def test_the_law_fails_without_the_kinetic_dilation():
    lhs = sp.diff(E, m1) - W * sp.diff(J, m1)
    assert sp.simplify(lhs - (-m2 / r)) != 0


def test_the_law_fails_with_half_the_companions_deficit():
    lhs = sp.diff(E, m1) - W * sp.diff(J, m1)
    assert sp.simplify(lhs - _z(v1, m2 / (2 * r))) != 0


def test_the_law_fails_if_each_body_is_charged_the_total():
    lhs = sp.diff(E, m1) - W * sp.diff(J, m1)
    assert sp.simplify(lhs - _z(v1, M / r)) != 0


# --- the helical direction and the clock as its norm ------------------------------

def test_the_circular_worldline_is_an_integral_curve_of_the_helical_vector():
    """x(t) = (r1 cos Wt, r1 sin Wt): the coordinate velocity is exactly the
    helical vector's spatial part, so the body moves along xi = d_t + W d_phi."""
    t = sp.symbols("t")
    x = r1 * sp.cos(W * t); y = r1 * sp.sin(W * t)
    # in polar terms the worldline has dphi/dt = W and dr/dt = 0
    phi = sp.atan2(y, x)
    assert sp.simplify(sp.diff(sp.sqrt(x ** 2 + y ** 2), t)) == 0
    assert sp.simplify(sp.diff(phi, t) - W) == 0


def test_the_deficit_at_the_body_is_the_helical_norm():
    """dtau/dt = sqrt(1 - 2 U_companion - v^2) expands to 1 + z at first
    order: the rest-clock deficit of §7.1 is the norm of the count
    direction, with the companion's deficit and the body's own motion the
    two contributions."""
    eps = sp.symbols("epsilon", positive=True)
    norm = sp.sqrt(1 - eps * (2 * m2 / r) - eps * v1 ** 2)
    first = sp.series(norm, eps, 0, 2).removeO().coeff(eps, 1)
    assert sp.simplify(first - Z1) == 0


# --- the test-mass limit: the law is exact to all orders --------------------------

def test_in_the_test_mass_limit_the_law_is_exact_to_all_orders():
    """Circular geodesic of Schwarzschild: E = (1-2M/r)/sqrt(1-3M/r),
    L = sqrt(Mr)/sqrt(1-3M/r), Omega = sqrt(M/r^3). Then E - Omega L =
    sqrt(1-3M/r) EXACTLY - and sqrt(1-3M/r) is dtau/dt, the helical norm
    along the worldline. The register's clock is the mass's conjugate to
    all orders, not merely at Newtonian order."""
    Ms, rs = sp.symbols("M r", positive=True)
    E = (1 - 2 * Ms / rs) / sp.sqrt(1 - 3 * Ms / rs)
    L = sp.sqrt(Ms * rs) / sp.sqrt(1 - 3 * Ms / rs)
    Om = sp.sqrt(Ms / rs ** 3)
    z = sp.sqrt(1 - 3 * Ms / rs)
    assert sp.simplify(E - Om * L - z) == 0
    # and along the sequence at fixed mass the law closes: dE = Omega dL
    assert sp.simplify(sp.diff(E, rs) - Om * sp.diff(L, rs)) == 0


def test_the_exact_clock_reduces_to_the_apportioned_first_order_rate():
    """sqrt(1 - 3M/r) = sqrt(1 - 2M/r - v^2) with v^2 = M/r the circular
    speed: the companion's deficit and the kinetic dilation, the same two
    contributions the Newtonian law selected."""
    Ms, rs, eps = sp.symbols("M r epsilon", positive=True)
    exact = sp.sqrt(1 - eps * (2 * Ms / rs) - eps * (Ms / rs))
    first = sp.series(exact, eps, 0, 2).removeO().coeff(eps, 1)
    assert sp.simplify(first - (-(Ms / rs) - (Ms / rs) / 2)) == 0


# --- the paper carries the re-scoping --------------------------------------------

def test_the_paper_states_the_helical_sector_and_the_first_law():
    assert "helical Killing vector" in FLAT
    assert "the redshift invariant of the two-body literature" in FLAT
    assert "first law of binary mechanics" in FLAT
    assert "δM − Ω δJ = z₁δm₁ + z₂δm₂" in FLAT
    assert "the first law selects it" in FLAT
    assert "Detweiler, S. (2008)" in FLAT
    assert "Le Tiec, A., Blanchet, L., and Whiting, B. F. (2012)" in FLAT
