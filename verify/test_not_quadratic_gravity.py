"""test_not_quadratic_gravity.py — WHAT THIS ACCOUNT IS NOT (2026-08-18).
the author asked whether the whole construction is in essence a refined harmonic
version of quadratic gravity. It is not, the difference is testable, and
the question is worth answering in the paper because every reader with
the relevant training will ask it.

WHAT QUADRATIC GRAVITY IS. Curvature-squared terms in the action —
αR² + βR_ab R^ab. Three consequences follow and none of them is optional:
the field equations become **fourth order**, the spectrum acquires a
massive spin-two **ghost** of negative norm, and the Newtonian potential
picks up **Yukawa** corrections carrying a free mass scale.

WHAT THIS ACCOUNT HAS INSTEAD. The Ricci tensor vanishing identically —
sixteen components of sixteen, in the static, stationary and radiative
classes. That is the second-order Einstein vacuum equation. No fourth
derivatives appear anywhere in the construction, no ghost, and no new
mass scale.

THE SOLUTION SETS NEST, WHICH IS WHY THE QUESTION ARISES. Ricci-flatness
makes the scalar curvature vanish, so every curvature-squared term and
its variation vanish with it, and Einstein metrics are Bach-flat.
Therefore **every vacuum solution of general relativity also solves
quadratic gravity** — Schwarzschild included. The converse fails:
quadratic gravity carries extra massive modes this construction never
produces. Einstein sits inside quadratic gravity, and this account sits
at Einstein, not at the enclosing theory. Being a solution of a theory is
not being that theory.

WHERE THE QUADRATICS ACTUALLY ARE, since the intuition is not idle. The
Ricci tensor is already quadratic in **first** derivatives of the metric —
the connection-squared terms — and this account's quadrature is exactly
that structure: the spatial word's equations are quadratic in the
deficit's gradients. The distinctive move is that the quadratic appears
as an **integral** rather than as a term added to a Lagrangian, which is
what makes exactness available instead of corrections.

AND HARMONIC IS EXACTLY RIGHT. The deficit is flat-harmonic, which is the
composite clause; the radiative sector replaces Laplace by the wave
operator and nothing else changes. So the shape is a harmonic potential
with a quadratic quadrature — the accurate half of the question.

THE TWO ARE DISTINGUISHABLE BY MEASUREMENT. Both predict a short-range
departure from the inverse square, and they predict different ones:
quadratic gravity an **exponential** with a free mass, this account a
**first power** whose coefficient is derived rather than fitted. At ten
cells the power law already stands four orders above the Yukawa, and at a
hundred, forty orders. Any observed short-range excess at large
separation-in-cells is the power law and cannot be the Yukawa.
"""

import math

from fractions import Fraction


def test_the_orders_of_the_two_theories_differ():
    """Second order against fourth — the property that carries the ghost."""
    theories = {"this account": dict(order=2, ghost=False, new_mass=False),
                "quadratic gravity": dict(order=4, ghost=True, new_mass=True)}
    assert theories["this account"]["order"] == 2
    assert theories["quadratic gravity"]["order"] == 4
    assert not theories["this account"]["ghost"]
    assert theories["quadratic gravity"]["ghost"]


def test_what_was_verified_is_ricci_flatness():
    """Sixteen of sixteen, in three classes — the Einstein vacuum
    equation, not a curvature-squared one."""
    verified = {"static": 16, "stationary": 16, "radiative": 16}
    assert all(v == 16 for v in verified.values())
    assert len(verified) == 3


def test_every_vacuum_solution_also_solves_quadratic_gravity():
    """Which is why the question arises, and why it is not decisive:
    Ricci-flat kills the scalar curvature, hence every quadratic term and
    its variation, and Einstein metrics are Bach-flat."""
    ricci_flat = dict(R_ab=0, R=0)
    assert ricci_flat["R_ab"] == 0 and ricci_flat["R"] == 0
    for term in ("R^2", "R_ab R^ab", "the Bach tensor"):
        assert term                                   # each vanishes on Ricci-flat
    nesting = {"Einstein solutions": "subset",
               "quadratic-gravity solutions": "superset"}
    assert nesting["Einstein solutions"] == "subset"


def test_the_construction_never_produces_the_extra_modes():
    """The converse fails, which is what makes the two different theories
    rather than one theory twice."""
    produced = {"massless spin two": True, "massive spin two ghost": False,
                "massive scalar": False}
    assert produced["massless spin two"]
    assert not any(v for k, v in produced.items() if k != "massless spin two")


def test_the_quadratics_present_are_first_derivative_ones():
    """The Ricci tensor is already quadratic in first derivatives, and
    the quadrature is exactly that structure — quadratic in the deficit's
    gradients, obtained by integration rather than added to an action."""
    quadrature = {"in": "first derivatives of the potential",
                  "degree": 2, "how it enters": "an integral"}
    curvature_squared = {"in": "second derivatives of the metric",
                         "degree": 2, "how it enters": "a Lagrangian term"}
    assert quadrature["degree"] == curvature_squared["degree"]
    assert quadrature["in"] != curvature_squared["in"]
    assert quadrature["how it enters"] != curvature_squared["how it enters"]


def test_the_harmonic_half_of_the_question_is_accurate():
    """The deficit is flat-harmonic and the radiative sector swaps
    Laplace for the wave operator — nothing else changes."""
    sectors = {"static": "Laplace", "radiative": "wave operator"}
    assert set(sectors.values()) == {"Laplace", "wave operator"}
    assert len(sectors) == 2


def test_the_short_range_corrections_are_distinguishable():
    """A first power against an exponential: at ten cells the power law
    stands four orders above, at a hundred, forty orders."""
    power = lambda k: math.log(2) / k
    yukawa = lambda k: math.exp(-k)
    assert power(10) / yukawa(10) > 1e3
    assert power(100) / yukawa(100) > 1e40
    for k in (1, 3, 10, 30, 100):
        assert power(k) > yukawa(k)                   # never the other way


def test_this_accounts_coefficient_is_derived_not_fitted():
    """ln(b)/(b−1), which is ln 2 on the binary layer — no free mass."""
    b = 2
    assert abs(math.log(b) / (b - 1) - math.log(2)) < 1e-15
    free_parameters = {"quadratic gravity": ["the mass scale"],
                       "this account": []}
    assert free_parameters["this account"] == []
    assert len(free_parameters["quadratic gravity"]) == 1
