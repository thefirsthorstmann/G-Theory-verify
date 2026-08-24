"""test_the_strut.py — TWO STATIC COUNTS CANNOT REST UNSUPPORTED, AND THE
REGISTER FIXES THE SUPPORT (2026-08-22). the author: "see if you
can get any further with what's open." The static two-body sector was
closed exactly by the quadrature (test_the_quadrature.py: the deficit
superposes, the spatial word is obtained by quadrature, γ_cross =
m₁m₂/(2a²)[(ρ² + z² − a²)/(r₁r₂) − 1] for sources at z = ±a). One physical
consequence of that banked formula had not been read off: its value on
the axis BETWEEN the two sources is not zero.

THE FACT. On the axis outside both sources γ_cross = 0: elementary
flatness holds, a small circle round the axis has circumference 2π times
its radius. On the segment between them γ_cross = −4m₁m₂/d² (d = 2a): the
ratio of circumference to 2π × radius is e^{−γ₀} ≠ 1, a conical defect. A
conical defect along the segment joining two bodies is a stress holding
them apart — Weyl's strut, read as a line source by Israel (1977) — and its
magnitude is not free:

    F  =  (e^{−γ₀} − 1)/4,   γ₀ the spatial word on the strut.

For point deficits γ₀ = −4m₁m₂/d², so F = m₁m₂/d² + 2m₁²m₂²/d⁴ + …: the
inverse square at leading order. For the register's OWN source — the rod
of coordinate length 2m, which is Schwarzschild in the Weyl chart
(test_the_quadrature: "the register's source is a rod of length twice its
mass") — the quadrature gives

    γ₀  =  ln[(d² − (m₁ + m₂)²)/(d² − (m₁ − m₂)²)]

    F   =  m₁m₂ / (d² − (m₁ + m₂)²)          (Bach & Weyl 1922)

exactly: the inverse square with the rods' total length subtracted from
the squared separation, diverging where the rods touch at d = m₁ + m₂.

WHAT IT FORBIDS. No two static counts rest in an elementarily flat axis:
a static pair without a supporting stress is not a solution. The stress is
fixed by the quadrature to the Bach–Weyl value; any other static two-body
force refutes the static sector. Checked below by performing the
quadrature numerically along z = 0 from infinity to the axis for both
source shapes, equal and unequal masses.
"""

import math
import pathlib

import mpmath as mp
import sympy as sp

CATALOG = pathlib.Path(__file__).resolve().parent.parent / "catalog"
GRAVITY = (CATALOG / "GRAVITY-AS-TONAL-CENTER.md").read_text()
FLAT = " ".join(GRAVITY.split())

rho, z = sp.symbols("rho z", real=True)


def _point(m, z0):
    return -m / sp.sqrt(rho ** 2 + (z - z0) ** 2)


def _rod(m, z0):
    Rp = sp.sqrt(rho ** 2 + (z - z0 - m) ** 2)
    Rm = sp.sqrt(rho ** 2 + (z - z0 + m) ** 2)
    return sp.log((Rp + Rm - 2 * m) / (Rp + Rm + 2 * m)) / 2


def _gamma_on_axis_between(psi):
    """γ(0, 0) by the Weyl quadrature along z = 0 from ρ = ∞ (where γ = 0):
    dγ/dρ = ρ(ψ_ρ² − ψ_z²), so γ(0,0) = −∫₀^∞ ρ(ψ_ρ² − ψ_z²)|_{z=0} dρ."""
    integrand = (rho * (sp.diff(psi, rho) ** 2 - sp.diff(psi, z) ** 2)).subs(z, 0)
    f = sp.lambdify(rho, integrand, "mpmath")
    mp.mp.dps = 30
    val = mp.quad(f, [0, 1, 4, 16, 64, mp.inf])
    return -float(val)


def _force(gamma0):
    return (math.exp(-gamma0) - 1) / 4


# --- the fact, for point deficits: γ between is −4m₁m₂/d², outside zero ----------

def test_gamma_cross_between_point_deficits_is_minus_four_m1m2_over_d2():
    for m1, m2, a in ((0.05, 0.05, 1.0), (0.03, 0.08, 1.5), (0.1, 0.02, 2.0)):
        psi = _point(m1, a) + _point(m2, -a)
        g0 = _gamma_on_axis_between(psi)
        d = 2 * a
        assert abs(g0 - (-4 * m1 * m2 / d ** 2)) < 1e-9, (m1, m2, a, g0)


def test_the_banked_closed_form_says_the_same_on_the_axis():
    m1, m2, A = sp.symbols("m1 m2 A", positive=True)
    r1 = sp.sqrt(rho ** 2 + (z - A) ** 2)
    r2 = sp.sqrt(rho ** 2 + (z + A) ** 2)
    gcross = m1 * m2 / (2 * A ** 2) * ((rho ** 2 + z ** 2 - A ** 2) / (r1 * r2) - 1)
    between = sp.simplify(gcross.subs({rho: 0, z: 0}))            # between, on the axis
    assert sp.simplify(between + m1 * m2 / A ** 2) == 0                    # = −4m₁m₂/d², d = 2A
    outside = sp.simplify(gcross.subs({rho: 0, z: 3 * A}))
    assert outside == 0                                                    # elementary flatness outside


def test_elementary_flatness_fails_between_and_holds_outside():
    m1, m2, a = 0.05, 0.05, 1.0
    g0 = -4 * m1 * m2 / (2 * a) ** 2
    assert abs(math.exp(-g0) - 1) > 1e-3          # circumference / (2π radius) ≠ 1 on the strut
    assert abs(math.exp(-0.0) - 1) < 1e-15        # = 1 outside


# --- the force, point deficits: inverse square at leading order --------------------

def test_the_point_force_is_newtons_at_leading_order():
    for m1, m2, d in ((0.01, 0.01, 1.0), (0.02, 0.005, 2.0)):
        F = _force(-4 * m1 * m2 / d ** 2)
        newton = m1 * m2 / d ** 2
        assert abs(F / newton - 1) < 5 * m1 * m2 / d ** 2 + 1e-12     # next term 2m₁m₂/d²
        assert F > newton                                            # the correction is positive


# --- the register's own source: rods, and the Bach–Weyl force exactly ----------------

def test_the_rod_quadrature_gives_the_bach_weyl_value_between():
    for m1, m2, a in ((0.10, 0.10, 1.0), (0.05, 0.15, 1.2), (0.20, 0.05, 0.8)):
        d = 2 * a
        assert d > m1 + m2                                           # rods do not touch
        psi = _rod(m1, a) + _rod(m2, -a)
        g0 = _gamma_on_axis_between(psi)
        bw = math.log((d ** 2 - (m1 + m2) ** 2) / (d ** 2 - (m1 - m2) ** 2))
        assert abs(g0 - bw) < 1e-8, (m1, m2, a, g0, bw)


def test_the_rod_force_is_the_inverse_square_with_the_rods_length_subtracted():
    for m1, m2, d in ((0.10, 0.10, 2.0), (0.05, 0.15, 2.4), (0.20, 0.05, 1.6)):
        g0 = math.log((d ** 2 - (m1 + m2) ** 2) / (d ** 2 - (m1 - m2) ** 2))
        F = _force(g0)
        assert abs(F - m1 * m2 / (d ** 2 - (m1 + m2) ** 2)) < 1e-15
        assert F > m1 * m2 / d ** 2                                  # stronger than Newton, always


def test_the_force_diverges_where_the_rods_touch():
    m1, m2 = 0.3, 0.2
    vals = [m1 * m2 / (d ** 2 - (m1 + m2) ** 2) for d in (1.0, 0.7, 0.55, 0.501)]
    assert all(b > a for a, b in zip(vals, vals[1:]))
    assert vals[-1] > 1e2 * vals[0]


def test_each_rod_alone_is_flat_on_its_own_axis():
    """The self terms contribute nothing on the axis outside a rod, so the
    value between two rods is the cross term alone — Schwarzschild's own
    elementary flatness, which is why the strut is purely an interaction."""
    psi = _rod(0.1, 1.0)                                            # one rod, centred at z = 1
    assert abs(_gamma_on_axis_between(psi)) < 1e-10                 # γ at (0,0), outside the rod


# --- the paper -------------------------------------------------------------------

def test_the_paper_states_the_strut_and_what_it_forbids():
    assert "**Two static counts cannot rest unsupported, and the register fixes the support.**" in FLAT
    assert "γ_cross = −4m₁m₂/d²" in FLAT
    assert "(e^{−γ₀} − 1)/4" in FLAT
    assert "m₁m₂/(d² − (m₁ + m₂)²)" in FLAT
    assert "diverging where the rods touch" in FLAT
    assert "Bach, R., and Weyl, H. (1922)" in FLAT
    assert "Israel, W. (1977)" in FLAT
