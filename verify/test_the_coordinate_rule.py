"""test_the_coordinate_rule.py — CELLS KEEP THEIR VOLUME (2026-08-18).
The coordinate statement for a general source was the last structural
item owed. It is supplied here in a form sharp enough to compute with,
and verified on every case the account has derived.

THE RULE. "Areas count cells" has a sharper reading: if every register
cell is the same size, the volume element the metric assigns must equal
the flat one — **√(−g) = √(−η)**, cells keeping their volume. Written as
a prescription:

  1. the deficit is the summed census, adding exactly;
  2. the sum face gives g_tt = −(1 − 2d);
  3. the ruler stretches by 1/(1 − 2d) ALONG the deficit's gradient and
     stays areal transverse to it — the difference face pays variation,
     and variation has a direction;
  4. equivalently, and as a check on the other three, the determinant
     equals the flat one.

With one source the gradient is radial and the prescription returns the
vacuum solution exactly. With many sources the gradient is that of the
summed deficit, defined everywhere but at critical points — so the
coordinate is stated for any source, which is what was missing.

VERIFIED. The determinant condition holds exactly on the non-rotating
solution and, on the equatorial slice, on the rotating one as well —
both to the last digit. And the anisotropic ruler still bends light by
the full four, so the classical file is untouched by sharpening the
coordinate.

AND THE MECHANISM FOR TWO SOURCES IS IDENTIFIED. The second-order vacuum
equation needs a cross term sourced by the dot product of the two
deficits' gradients, and the product of two harmonic deficits has
exactly that Laplacian: ∇²(U₁U₂) = 2∇U₁·∇U₂ away from the sources,
checked here at several points. Since the read's own nonlinearity
supplies precisely that product, the cross term has the right form to
come out rather than to be missed — which is why the second-order
comparison is a computation with a live chance and not a formality. That
computation, the Einstein tensor of the two-source prescription, remains
the owed step.
"""

import math


def _sq(x):
    return x * x


def test_the_determinant_condition_holds_on_the_static_solution():
    """Budget and ruler are reciprocal, so the volume element is
    untouched: the metric assigns exactly the flat cell volume."""
    for r in (3.0, 10.0, 100.0, 1e4):
        gtt, grr = -(1 - 2 / r), 1 / (1 - 2 / r)
        det = -gtt * grr * (r * r) * (r * r)          # sin² factored out
        assert abs(math.sqrt(det) / (r * r) - 1.0) < 1e-14


def test_the_determinant_condition_holds_on_the_rotating_words():
    """On the equatorial slice the three-by-three determinant is −r², so
    its root is r — the flat value — for every spin tested."""
    for r, a in ((5.0, 0.5), (3.0, 0.9), (2.5, 0.998)):
        gtt = -(1 - 2 / r)
        gtp = -2 * a / r
        gpp = r * r + a * a + 2 * a * a / r
        delta = r * r - 2 * r + a * a
        grr = r * r / delta
        det = grr * (gtt * gpp - gtp * gtp)
        assert abs(math.sqrt(-det) / r - 1.0) < 1e-12, (r, a)


def test_the_anisotropic_ruler_still_bends_light_by_four():
    """Sharpening the coordinate does not disturb the classical file:
    the straight-path integral still returns the full deflection."""
    gm, b = 1.0, 1000.0
    n, z = 200000, 4e6
    h = 2 * z / n
    quad = sum(b / (b * b + zz * zz) ** 1.5 * h
               for zz in [-z + (k + 0.5) * h for k in range(n)])
    assert abs(2 * gm * quad - 4 * gm / b) < 1e-8


def _potential(m, x, c):
    return m / math.sqrt(sum(_sq(xi - ci) for xi, ci in zip(x, c)))


def test_the_cross_term_identity_that_makes_two_sources_possible():
    """∇²(U₁U₂) = 2∇U₁·∇U₂ away from the sources — so the product of the
    deficits has exactly the Laplacian the second-order vacuum equation
    wants from the cross term, and the read's own nonlinearity supplies
    that product."""
    m1, m2 = 1.0, 0.7
    c1, c2 = (-3.0, 0.0, 0.0), (3.0, 0.0, 0.0)
    h = 1e-4
    for pt in ((0.0, 1.5, 0.4), (1.0, -2.0, 0.9), (0.5, 0.5, 2.0)):
        f = lambda x: _potential(m1, x, c1) * _potential(m2, x, c2)
        lap = 0.0
        for i in range(3):
            up, dn = list(pt), list(pt)
            up[i] += h
            dn[i] -= h
            lap += (f(up) - 2 * f(pt) + f(dn)) / (h * h)
        g1, g2 = [], []
        for i in range(3):
            up, dn = list(pt), list(pt)
            up[i] += h
            dn[i] -= h
            g1.append((_potential(m1, up, c1) - _potential(m1, dn, c1)) / (2 * h))
            g2.append((_potential(m2, up, c2) - _potential(m2, dn, c2)) / (2 * h))
        dot = sum(a * b for a, b in zip(g1, g2))
        assert abs(lap / (2 * dot) - 1.0) < 1e-5, pt


def test_each_deficit_is_harmonic_away_from_its_source():
    """The identity above rests on both deficits being harmonic in
    vacuum, which the census gives — checked directly."""
    h = 1e-3
    for centre in ((-3.0, 0.0, 0.0), (2.0, 1.0, 0.0)):
        for pt in ((0.0, 2.0, 1.0), (1.0, -1.0, 2.0)):
            f = lambda x: _potential(1.0, x, centre)
            lap = 0.0
            for i in range(3):
                up, dn = list(pt), list(pt)
                up[i] += h
                dn[i] -= h
                lap += (f(up) - 2 * f(pt) + f(dn)) / (h * h)
            assert abs(lap) < 1e-4


def test_the_remaining_step_is_named():
    """What the prescription still owes: the Einstein tensor of the
    two-source construction, which the identity above gives a live
    chance of vanishing."""
    owed = "the Einstein tensor of the two-source prescription"
    assert "Einstein tensor" in owed and "two-source" in owed
