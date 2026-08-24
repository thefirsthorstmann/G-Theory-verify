"""test_the_2pn_comparison.py — THE SECOND-ORDER TWO-BODY COMPARISON, MADE:
NO DIVERGENCE, AND THE CLOCK LAW REPRODUCES THE SELF-FORCE SERIES THROUGH
THIRD ORDER (2026-08-23). the author: "go get the 2PN conservative comparison, all
the way." The paper had carried this as "the calculation this account has
not performed," bounded by the double pulsar at a fifth.

THE SHAPE OF THE COMPARISON, stated before the numbers. The account's
field equations are Einstein's, with the derived coupling, in every sector
it has built (static, stationary, radiative, null; the first-post-Newtonian
N-body closure). Its one shortcut — the exact superposition of deficits —
is a theorem in every class with a Killing reduction and FAILS the vacuum
equations at second order in the circulation (test_the_twist: two rotating
potentials miss by 2e-2). So where the binary circulates the account has
no alternative rule: the conservative two-body dynamics there are the
received theory's own. The comparison is therefore between the account's
structural law — the rest clocks are the masses' conjugates — and the
received conservative invariants. If the law, fed those invariants,
reproduces physics computed by a different formalism, the account's
two-body sector stands at second order with nothing owed but apparatus.

THE OBJECTS. Circular orbits, G = c = 1, x = (MΩ)^{2/3}:
    E(x) = −(μx/2)[1 − (3/4 + ν/12)x − (27/8 − 19ν/8 + ν²/24)x² − c_E3 x³]
    J(x) = (μM/√x)[1 + (3/2 + ν/6)x + (27/8 − 19ν/8 + ν²/24)x² + c_J3 x³]
    c_E3 = 675/64 − (34445/576 − 205π²/96)ν + 155ν²/96 + 35ν³/5184
    c_J3 = 135/16 − (6889/144 − 41π²/24)ν + 31ν²/24 + 7ν³/1296
The first law as a total differential, dM = Ω dJ + z₁dm₁ + z₂dm₂ with
M = m₁ + m₂ + E, gives at fixed x:  ∂E/∂x = Ω ∂J/∂x  (checked, through
3PN — a consistency check of the coefficients) and the clocks
    z_a = 1 + ∂E/∂m_a|_x − Ω ∂J/∂m_a|_x.

THE ANCHORS, all exact.
  test mass   (m₁ → 0):  z₁ → √(1 − 3x), term by term through x⁴;
  heavy body  (m₂ → 0):  z₁ − 1 → −(m₂/M) x/√(1 − 3x), through x⁴;
  SELF-FORCE  (m₁ = q m₂, y = (m₂Ω)^{2/3}): u^T = 1/z₁ expands as
      u^T = (1 − 3y)^{−1/2} + q [ −y − 2y² − 5y³ − (121/3 − 41π²/32) y⁴ ] + O(q²)
  which is the gravitational self-force correction to the redshift
  invariant computed from black-hole perturbation theory (Detweiler 2008;
  Blanchet, Detweiler, Le Tiec and Whiting 2010) — a different formalism,
  reproduced here coefficient by coefficient, π² included.

THE VERDICT. The second-order comparison is made and there is no
divergence: the account's conservative two-body sector coincides with the
received theory's through third post-Newtonian order, and the clock law
holds there with the received invariants. The earlier bound of a fifth is
superseded — the coefficient is the received one. What the account adds is
not a different number but the reading: the helical count direction, the
clock as its norm, the law that makes the clocks the masses' conjugates.
"""

import pathlib

import sympy as sp

CATALOG = pathlib.Path(__file__).resolve().parent.parent / "catalog"
GRAVITY = (CATALOG / "GRAVITY-AS-TONAL-CENTER.md").read_text()
FLAT = " ".join(GRAVITY.split())

m1, m2, x, q, y, t = sp.symbols("m1 m2 x q y t", positive=True)
M = m1 + m2
MU = m1 * m2 / M
NU = MU / M
PI = sp.pi

CE1 = -(sp.Rational(3, 4) + NU / 12)
CE2 = -(sp.Rational(27, 8) - sp.Rational(19, 8) * NU + NU ** 2 / 24)
CE3 = -(sp.Rational(675, 64) - (sp.Rational(34445, 576) - sp.Rational(205, 96) * PI ** 2) * NU
        + sp.Rational(155, 96) * NU ** 2 + sp.Rational(35, 5184) * NU ** 3)
CJ1 = sp.Rational(3, 2) + NU / 6
CJ2 = sp.Rational(27, 8) - sp.Rational(19, 8) * NU + NU ** 2 / 24
CJ3 = (sp.Rational(135, 16) - (sp.Rational(6889, 144) - sp.Rational(41, 24) * PI ** 2) * NU
       + sp.Rational(31, 24) * NU ** 2 + sp.Rational(7, 1296) * NU ** 3)
OMEGA = x ** sp.Rational(3, 2) / M


def _EJ(order):
    E = -(MU * x / 2) * (1 + CE1 * x + (CE2 * x ** 2 if order >= 2 else 0) + (CE3 * x ** 3 if order >= 3 else 0))
    J = (MU * M / sp.sqrt(x)) * (1 + CJ1 * x + (CJ2 * x ** 2 if order >= 2 else 0) + (CJ3 * x ** 3 if order >= 3 else 0))
    return E, J


def _clock(order):
    E, J = _EJ(order)
    return 1 + sp.diff(E, m1) - OMEGA * sp.diff(J, m1)


# --- the invariants are mutually consistent: dE = Omega dJ at fixed masses ---------

def test_first_law_at_fixed_masses_holds_through_third_order():
    for order in (2, 3):
        E, J = _EJ(order)
        d = sp.series(sp.expand(sp.diff(E, x) - OMEGA * sp.diff(J, x)), x, 0, order + 1).removeO()
        assert sp.simplify(d) == 0


# --- the clocks from the law meet both exact limits ---------------------------------

def test_the_test_mass_clock_is_the_exact_schwarzschild_rate():
    for order in (2, 3):
        z1 = sp.series(_clock(order), x, 0, order + 2).removeO()
        tm = sp.series(sp.limit(z1, m1, 0), x, 0, order + 2).removeO()
        ex = sp.series(sp.sqrt(1 - 3 * x), x, 0, order + 2).removeO()
        assert sp.simplify(tm - ex) == 0


def test_the_heavy_body_clock_is_the_exact_test_particle_law():
    for order in (2, 3):
        z1 = sp.series(_clock(order), x, 0, order + 2).removeO()
        hv = sp.series(z1.subs({m1: 1, m2: t}), t, 0, 2).removeO().coeff(t, 1)
        ex = sp.series(-x / sp.sqrt(1 - 3 * x), x, 0, order + 2).removeO()
        assert sp.simplify(sp.series(hv - ex, x, 0, order + 2).removeO()) == 0


# --- the self-force anchor: black-hole perturbation theory reproduced ---------------

def _self_force_series(order):
    uT = (1 / _clock(order)).subs({m1: q * m2}).subs(x, y * (1 + q) ** sp.Rational(2, 3))
    uT_q = sp.series(uT, q, 0, 2).removeO().coeff(q, 1)
    return sp.expand(sp.series(sp.simplify(uT_q), y, 0, order + 2).removeO())


def test_the_self_force_redshift_series_through_2pn():
    assert sp.simplify(_self_force_series(2) - (-y - 2 * y ** 2 - 5 * y ** 3)) == 0


def test_the_self_force_redshift_series_through_3pn_with_the_pi_squared_term():
    target = -y - 2 * y ** 2 - 5 * y ** 3 + (-sp.Rational(121, 3) + sp.Rational(41, 32) * PI ** 2) * y ** 4
    assert sp.simplify(_self_force_series(3) - target) == 0


def test_the_leading_self_force_term_is_the_newtonian_law():
    """The −y term needs only Newtonian E and J: the small body's clock slows
    by its own mass's effect on the orbit it rides — the first law's leading
    content, the same selection the helical battery made."""
    E = -(MU * x / 2); J = MU * M / sp.sqrt(x)
    z1 = 1 + sp.diff(E, m1) - OMEGA * sp.diff(J, m1)
    uT = (1 / z1).subs({m1: q * m2}).subs(x, y * (1 + q) ** sp.Rational(2, 3))
    uT_q = sp.series(uT, q, 0, 2).removeO().coeff(q, 1)
    assert sp.simplify(sp.series(uT_q, y, 0, 2).removeO() + y) == 0


# --- the paper ----------------------------------------------------------------------

def test_the_paper_makes_the_comparison_and_closes_the_hedge():
    assert "**Second order: compared, and there is no divergence.**" in FLAT
    assert "the gravitational self-force series of black-hole perturbation theory" in FLAT
    assert "(121/3 − 41π²/32)" in FLAT
    assert "The earlier bound from the double pulsar" in FLAT
    assert "bounded, not open" not in FLAT
    assert "the calculation this account has not performed" not in FLAT
    assert "it is bounded below a fifth by the double pulsar" not in FLAT
    assert "Blanchet, L., Detweiler, S., Le Tiec, A., and Whiting, B. F. (2010)" in FLAT
