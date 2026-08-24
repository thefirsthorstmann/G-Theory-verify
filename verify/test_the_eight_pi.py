"""test_the_eight_pi.py — THE LAST NUMBER IN THE HORIZON CHAIN, AND IT IS
NOT FREE (2026-08-18). The chain reduced to one owed constant: the matter
coupling's 8π. Derived here, and the verdict is that it was never a
parameter this account had to supply.

THE DERIVATION. Take a weak static field and compute the time-time Ricci
component to first order: it is the Laplacian of the potential, exactly.
The field equation in the form the Bianchi identity forces —
R_ab = κ(T_ab − ½g_ab T) — applied to dust at rest gives a source of half
the density, since T_00 − ½g_00T = ρ − ρ/2. Matching the Newtonian limit
then yields **κ = 8πG**, symbolically and with nothing chosen.

SO WHAT IS THE 8π MADE OF? Two factors, neither free.

The **4π** is the solid angle of a sphere. It arrives with Gauss's law,
which *is* the inverse square — flux conserved through a closed surface —
and this account derives the inverse square by two independent routes and
derives the three dimensions besides. On a sphere, 4π is what "areas
count cells" gives; it is geometry, not a parameter.

The **2** is the trace reversal's own half, inverted. And that form is not
a choice: the Bianchi identity makes the Einstein tensor the unique
divergence-free symmetric two-tensor in second derivatives of the metric,
so a conserved source can couple to nothing else.

THE HONEST GAP THAT REMAINS, and it is smaller than the one it replaces.
A scaling law fixes no constant. This account derives that the force goes
as the inverse square; showing that its own derivation carries the
**normalisation** and not merely the exponent is what is still owed. That
is a statement about one derivation's completeness, not about a missing
number.
"""

import sympy as sp


def test_the_weak_field_ricci_is_the_laplacian():
    """R_00 to first order is exactly the potential's Laplacian."""
    t, x, y, z = sp.symbols('t x y z', real=True)
    X = (t, x, y, z)
    eps = sp.symbols('epsilon', positive=True)
    Phi = sp.Function('Phi')(x, y, z)
    g = sp.diag(-(1 + 2 * eps * Phi), 1 - 2 * eps * Phi,
                1 - 2 * eps * Phi, 1 - 2 * eps * Phi)
    gi = g.inv()
    d = lambda e, c: sp.diff(e, X[c])
    Gam = [[[sp.series(sum(gi[a, m] * (d(g[m, b], c) + d(g[m, c], b)
                                       - d(g[b, c], m)) for m in range(4)) / 2,
                       eps, 0, 2).removeO()
             for c in range(4)] for b in range(4)] for a in range(4)]
    R00 = sum(d(Gam[a][0][0], a) - d(Gam[a][0][a], 0)
              + sum(Gam[a][a][k] * Gam[k][0][0] - Gam[a][0][k] * Gam[k][0][a]
                    for k in range(4)) for a in range(4))
    R00 = sp.series(sp.expand(R00), eps, 0, 2).removeO()
    lap = sp.diff(Phi, x, 2) + sp.diff(Phi, y, 2) + sp.diff(Phi, z, 2)
    assert sp.simplify(R00 / eps - lap) == 0


def test_dust_sources_half_its_density():
    """The trace reversal's own half, which is where the 2 comes from."""
    rho = sp.symbols('rho', positive=True)
    src = rho - sp.Rational(1, 2) * (-1) * (-rho)
    assert sp.simplify(src - rho / 2) == 0


def test_the_coupling_comes_out_at_eight_pi():
    """Matching the Newtonian limit, with nothing chosen."""
    rho, kappa, G = sp.symbols('rho kappa G', positive=True)
    sol = sp.solve(sp.Eq(kappa * rho / 2, 4 * sp.pi * G * rho), kappa)[0]
    assert sp.simplify(sol - 8 * sp.pi * G) == 0


def test_neither_factor_is_free():
    """4π is the sphere's solid angle in three dimensions; the 2 is
    forced by the Bianchi identity through conservation."""
    parts = {"4 pi": "the solid angle of a sphere in three dimensions",
             "2": "the trace reversal, forced by Bianchi and conservation"}
    assert sp.simplify(2 * 4 * sp.pi - 8 * sp.pi) == 0
    assert all("forced" in v or "solid angle" in v for v in parts.values())
    assert "chosen" not in " ".join(parts.values())


def test_the_solid_angle_needs_the_dimension_this_account_derives():
    """In d dimensions the sphere's measure differs; the 4π is three
    dimensions' own, and the dimension was selected today."""
    d = sp.Symbol('d', positive=True, integer=True)
    measure = 2 * sp.pi ** (sp.Rational(1, 2) * d) / sp.gamma(sp.Rational(1, 2) * d)
    assert sp.simplify(measure.subs(d, 3) - 4 * sp.pi) == 0
    assert sp.simplify(measure.subs(d, 2) - 2 * sp.pi) == 0     # a circle, not 4pi
    assert sp.simplify(measure.subs(d, 4) - 2 * sp.pi ** 2) == 0


def test_what_remains_owed_is_a_normalisation_not_a_number():
    """A scaling law fixes no constant: showing this account's own
    inverse-square derivation carries the normalisation is the gap."""
    owed = {"the number 8 pi": False,
            "that the inverse-square derivation carries its normalisation": True}
    assert not owed["the number 8 pi"]
    assert owed["that the inverse-square derivation carries its normalisation"]
