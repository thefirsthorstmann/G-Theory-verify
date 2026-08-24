"""test_the_clause_coefficient.py — THE QUADRUPOLE CLAUSE'S COEFFICIENT IS
FIXED BY THE STATIONARY FIELD EQUATIONS, NOT BY COMPARISON (2026-08-22,
session). the author: "see if you can get any further with what's open." This
was the second of three open items in §21.12.

THE STANDING BEFORE TODAY (§21.5, test_the_quadrupole.py). At second order
in spin the deficit gains the difference-face charge squared, 2M/r ->
2M/r − (a/r)², so the deficit polynomial is r² − 2Mr + c·a² with c = 1 —
and the one was READ OFF the charged solution's r² − 2Mr + Q². The paper
said so plainly: "a calibration against known geometry rather than a
derivation from the register, and the register supplies no independent
reason for the one."

THE REASON WAS ALREADY IN THE ACCOUNT. The stationary sector's field
equations, verified in test_the_twist.py (f∇²f = (∇f)² − (∇χ)², all
sixteen Ricci components annihilated), are Ernst's equations. Write the
two faces as one potential on the prolate chart — the sum face linear in
the radial coordinate, the difference face linear in the angular one:

    ξ = p x − i q y,   x = (r − M)/(M p),  y = cos θ,
    M p = the horizon's offset from the mass,  q = a/M.

The Ernst equation (ξξ̄ − 1)∇²ξ = 2ξ̄(∇ξ)² then has residual EXACTLY

    2 (p x + i q y) (p² + q² − 1),

so the potential solves the equations if and only if p² + q² = 1. And on
the equator the deficit polynomial — the negative determinant of the
(t, φ) block, which is ρ² — is (r − M)² − M²p² = r² − 2Mr + M²(1 − p²).
Matching r² − 2Mr + c·a² gives c = (1 − p²)/q², which is one exactly on
the circle. THE COEFFICIENT IS THE UNIT NORM OF THE TWO FACES' POTENTIAL:
the horizon offset Mp and the difference charge a = Mq are the legs of a
right triangle whose hypotenuse is the sum charge M, (M² − a²) + a² = M²,
and the Kerr bound |a| ≤ M is the same circle read as p² ≥ 0.

The comparison with the charged solution is thereby demoted from source
to check: the difference-face charge sits in the electric charge's slot
with the same coefficient because both are unit-norm completions of the
same polynomial. Grade: derived within the construction — a theorem of
the equations the account already holds, nothing admitted.
"""

import math
import pathlib

import sympy as sp

CATALOG = pathlib.Path(__file__).resolve().parent.parent / "catalog"
GRAVITY = (CATALOG / "GRAVITY-AS-TONAL-CENTER.md").read_text()
FLAT = " ".join(GRAVITY.split())

x, y = sp.symbols("x y", real=True)
p, q, M, r = sp.symbols("p q M r", positive=True)


def _ernst_residual(xi):
    """(ξξ̄ − 1)∇²ξ − 2ξ̄(∇ξ)² in prolate spheroidal coordinates; the common
    factor 1/(k²(x² − y²)) cancels between the two sides and is dropped."""
    xib = sp.conjugate(xi)
    lap = sp.diff((x ** 2 - 1) * sp.diff(xi, x), x) + sp.diff((1 - y ** 2) * sp.diff(xi, y), y)
    grad2 = (x ** 2 - 1) * sp.diff(xi, x) ** 2 + (1 - y ** 2) * sp.diff(xi, y) ** 2
    return sp.expand((xi * xib - 1) * lap - 2 * xib * grad2)


# --- the theorem: the linear potential solves the equations iff p² + q² = 1 -------

def test_the_residual_is_exactly_two_xibar_times_the_circle_defect():
    xi = p * x - sp.I * q * y
    res = _ernst_residual(xi)
    assert sp.simplify(res - 2 * (p * x + sp.I * q * y) * (p ** 2 + q ** 2 - 1)) == 0


def test_on_the_unit_circle_the_residual_vanishes_identically():
    for pv, qv in ((sp.Rational(3, 5), sp.Rational(4, 5)), (sp.Rational(5, 13), sp.Rational(12, 13)),
                   (sp.Rational(1), sp.Rational(0))):
        res = _ernst_residual(pv * x - sp.I * qv * y)
        assert sp.simplify(res) == 0


def test_off_the_circle_it_does_not_and_the_defect_is_linear_in_p2_plus_q2():
    for pv, qv in ((sp.Rational(3, 5), sp.Rational(3, 5)), (sp.Rational(1), sp.Rational(1, 2)),
                   (sp.Rational(1, 2), sp.Rational(1, 2))):
        res = _ernst_residual(pv * x - sp.I * qv * y)
        val = complex(res.subs({x: sp.Rational(7, 3), y: sp.Rational(1, 4)}))
        expect = complex(2 * (pv * sp.Rational(7, 3) + sp.I * qv * sp.Rational(1, 4)) * (pv ** 2 + qv ** 2 - 1))
        assert abs(val) > 1e-6
        assert abs(val - expect) < 1e-12


# --- the map to the clause: c = (1 − p²)/q² ---------------------------------------

def _c_of(pv, qv):
    return (1 - pv ** 2) / qv ** 2


def test_the_deficit_polynomials_constant_term_is_M2_times_one_minus_p2():
    """ρ² on the equator is (r − M)² − M²p², the negative determinant of the
    (t, φ) block, so the polynomial is r² − 2Mr + M²(1 − p²)."""
    rho2 = (r - M) ** 2 - M ** 2 * p ** 2
    assert sp.expand(rho2 - (r ** 2 - 2 * M * r + M ** 2 * (1 - p ** 2))) == 0


def test_the_coefficient_is_one_exactly_on_the_circle_and_only_there():
    for pv, qv in ((sp.Rational(3, 5), sp.Rational(4, 5)), (sp.Rational(5, 13), sp.Rational(12, 13))):
        assert _c_of(pv, qv) == 1
    for pv, qv in ((sp.Rational(3, 5), sp.Rational(3, 5)), (sp.Rational(1, 2), sp.Rational(1, 2)),
                   (sp.Rational(3, 5), sp.Rational(1))):
        c = _c_of(pv, qv)
        assert c != 1
        assert sp.simplify(c - 1 - (1 - pv ** 2 - qv ** 2) / qv ** 2) == 0     # c − 1 = −(circle defect)/q²


def test_the_derived_words_are_the_potentials_equatorial_face_for_any_p():
    """The sum face on the equator, f = (p²x² − 1)/(px + 1)² with r = M(1 + px),
    is 1 − 2M/r whatever p is: the derived word does not fix the coefficient,
    which is why it had to be fixed elsewhere — and the equations do it."""
    f = (p ** 2 * x ** 2 - 1) / (p * x + 1) ** 2
    rr = M * (1 + p * x)
    assert sp.simplify(f - (1 - 2 * M / rr)) == 0


# --- the reading of the one: a unit norm, and the Kerr bound as the same circle -----

def test_the_horizon_offset_and_the_difference_charge_are_the_legs():
    for Mv, av in ((1.0, 0.3), (1.0, 0.9), (2.5, 1.7)):
        pv, qv = math.sqrt(Mv ** 2 - av ** 2) / Mv, av / Mv
        assert abs(pv ** 2 + qv ** 2 - 1) < 1e-15
        assert abs((Mv * pv) ** 2 + av ** 2 - Mv ** 2) < 1e-12             # legs² sum to the hypotenuse²
        rp, rm = Mv + Mv * pv, Mv - Mv * pv
        assert abs(rp ** 2 - 2 * Mv * rp + av ** 2) < 1e-12                 # the horizons are the roots
        assert abs(rm ** 2 - 2 * Mv * rm + av ** 2) < 1e-12


def test_the_kerr_bound_is_p_squared_nonnegative():
    for av in (0.0, 0.5, 0.999, 1.0):
        assert 1 - av ** 2 >= 0                         # p² = 1 − q² ≥ 0  ⇔  |a| ≤ M
    assert 1 - 1.2 ** 2 < 0                             # beyond: no real p, no horizon


# --- the paper carries it and the open list shrinks -------------------------------

def test_the_paper_states_the_derivation_and_closes_the_item():
    assert "The coefficient is fixed by the stationary field equations of §21.6 rather than by comparison." in FLAT
    assert "if and only if p² + q² = 1" in FLAT
    assert "2(px + iqy)(p² + q² − 1)" in FLAT
    assert "the unit norm of the two faces' potential" in FLAT
    assert "a consequence rather than the source" in FLAT
    assert "comparison-fixed coefficient" not in FLAT
    assert "the register supplies no independent reason for the one" not in FLAT
    assert "**Open, named.** Two items." in FLAT
    assert "The quadrupole clause's coefficient, fixed by comparison rather than derived." not in FLAT
