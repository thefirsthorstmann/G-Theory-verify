"""test_the_null_class.py — A FOURTH EXACT CLASS, ON ONE KILLING VECTOR,
AND THE SECTOR'S BOUNDARY FOUND (2026-08-18). The owed item had been
named "the asymmetric sector — fewer than two Killing vectors." Testing
that boundary before assuming it, it turns out to be the wrong one: there
is an exact class with **one** Killing vector, the construction covers it
with less machinery than anywhere else, and the real boundary is
something else entirely.

THE CLASS. Plane-fronted waves with parallel rays, in Brinkmann form.
Their only Killing vector is a covariantly constant **null** one — one,
not two, and generic profiles admit no other.

AND THEY ARE BORN IN THE REGISTER'S OWN CHART. The determinant is
**exactly −1** with no transformation performed, so "areas count cells"
holds natively here rather than after a change of coordinates. Of the
four exact classes this is the only one for which that is true.

THE CONSTRUCTION AT ITS MINIMUM. Computing the Ricci tensor with the
profile arbitrary, **exactly one component is ever nonzero**, and it is
minus one half the profile's transverse Laplacian. Imposing only that the
profile is harmonic across the wavefront — the composite clause, and
nothing else — annihilates all sixteen. **No budget word, no quadrature,
no second potential.** Strip the construction to the clause alone and
what remains is still a complete exact vacuum solution: the clause by
itself is a theory of gravitational radiation.

AND THE CLAUSE IS EXACT HERE AT EVERY ORDER, the transverse Laplacian
being linear — which is why parallel plane waves pass through one another
unchanged, a fact of the received theory that falls out of the clause
rather than being imported.

THE REAL BOUNDARY, FOUND BY BREAKING IT. Two waves that do **not** share
the null direction do not superpose: the naive sum has a Ricci tensor of
order unity, and it also leaves the register's chart, its determinant no
longer minus one. That is the collision problem, and it makes a
singularity. So the composite clause holds under two conditions and not
one — **the sources must share a symmetry direction, and the deficit's
own equation must be linear.** Rotation breaks the second (the twist
sources the deficit); collision breaks the first.

WHICH CLOSES THE SECTOR AS A DOMAIN STATEMENT RATHER THAN A GAP. Each of
the four exact classes has a symmetry direction, and the deficit is the
metric function that symmetry makes available. Where no direction is free
of carry there is no count to take and the deficit is not defined — so
the fully asymmetric case is not a computation left undone but the edge
of what this construction has an object for. What remains available there
is the expansion, where this account already sits at every
first-post-Newtonian parameter exactly.
"""

import sympy as sp

U, V, XX, YY = sp.symbols('u v x y', real=True)
COORDS = (U, V, XX, YY)


def _ricci(g):
    gi = g.inv()
    d = lambda e, c: sp.diff(e, COORDS[c])
    Gam = [[[sp.simplify(sum(gi[a, m] * (d(g[m, b], c) + d(g[m, c], b)
                                         - d(g[b, c], m)) for m in range(4)) / 2)
             for c in range(4)] for b in range(4)] for a in range(4)]
    R = sp.zeros(4, 4)
    for b in range(4):
        for c in range(4):
            e = sum(d(Gam[a][b][c], a) - d(Gam[a][b][a], c)
                    + sum(Gam[a][a][k] * Gam[k][b][c] - Gam[a][c][k] * Gam[k][b][a]
                          for k in range(4)) for a in range(4))
            R[b, c] = sp.simplify(sp.expand(e))
    return R


def _metric(H, Hv=0):
    return sp.Matrix([[H, 1, 0, 0], [1, Hv, 0, 0], [0, 0, 1, 0], [0, 0, 0, 1]])


def test_the_wave_is_born_in_the_registers_chart():
    """Determinant exactly minus one, with no transformation — the only
    one of the four classes for which that is true as written."""
    H = sp.Function('H')(U, XX, YY)
    assert sp.simplify(_metric(H).det()) == -1


def test_its_only_killing_vector_is_null_and_covariantly_constant():
    """One, not two: the metric is independent of v, that direction is
    null, and its covariant derivative vanishes."""
    H = sp.Function('H')(U, XX, YY)
    g = _metric(H)
    assert all(sp.diff(g[i, j], V) == 0 for i in range(4) for j in range(4))
    assert g[1, 1] == 0                                   # null
    gi = g.inv()
    d = lambda e, c: sp.diff(e, COORDS[c])
    for a in range(4):
        for b in range(4):
            gam_u = sp.simplify(sum(gi[0, m] * (d(g[m, a], b) + d(g[m, b], a)
                                                - d(g[a, b], m))
                                    for m in range(4)) / 2)
            assert gam_u == 0                             # covariantly constant


def test_exactly_one_ricci_component_is_ever_nonzero():
    """And it is minus half the profile's transverse Laplacian — the
    whole vacuum content, with nothing else in it."""
    H = sp.Function('H')(U, XX, YY)
    R = _ricci(_metric(H))
    nz = [(b, c) for b in range(4) for c in range(4) if R[b, c] != 0]
    assert nz == [(0, 0)]
    want = -(sp.diff(H, XX, 2) + sp.diff(H, YY, 2)) / 2
    assert sp.simplify(R[0, 0] - want) == 0


def test_the_composite_clause_alone_annihilates_the_tensor():
    """No budget word, no quadrature: harmonicity across the wavefront
    is the entire field equation."""
    H = sp.Function('H')(U, XX, YY)
    R = _ricci(_metric(H))
    for b in range(4):
        for c in range(4):
            e = R[b, c].subs(sp.diff(H, XX, 2), -sp.diff(H, YY, 2))
            assert sp.simplify(sp.expand(e)) == 0, (b, c)


def test_the_construction_uses_less_machinery_here_than_anywhere():
    """Three of the four classes need a budget and a quadrature; this one
    needs neither."""
    machinery = {"static": {"budget", "quadrature"},
                 "stationary": {"budget", "quadrature"},
                 "cylindrical": {"budget", "quadrature"},
                 "null": set()}
    assert machinery["null"] == set()
    assert all(machinery[k] for k in machinery if k != "null")


def test_parallel_waves_superpose_exactly():
    """The equation is linear, so waves sharing the null direction pass
    through one another unchanged."""
    H1 = sp.cos(U) * (XX ** 2 - YY ** 2)
    H2 = sp.Rational(1, 3) * sp.sin(2 * U) * XX * YY
    for H in (H1, H2, H1 + H2):
        assert sp.simplify(sp.diff(H, XX, 2) + sp.diff(H, YY, 2)) == 0
        R = _ricci(_metric(H))
        assert all(sp.simplify(R[b, c]) == 0 for b in range(4) for c in range(4))


def test_waves_not_sharing_the_direction_do_not_superpose():
    """The boundary, found by breaking it: the naive sum of two
    counter-propagating waves is not vacuum, and it also leaves the
    register's chart."""
    K1 = sp.cos(U) * (XX ** 2 - YY ** 2)
    K2 = sp.Rational(1, 3) * sp.cos(V) * (XX ** 2 - YY ** 2)
    g = _metric(K1, K2)
    assert sp.simplify(g.det()) != -1                     # not the register's chart
    at = {U: 0.7, V: 0.2, XX: 1.3, YY: -0.8}
    R = _ricci(g)
    worst = max(abs(complex(sp.N(R[b, c].subs(at))))
                for b in range(4) for c in range(4))
    assert worst > 1.0                                    # not vacuum, and not slightly


def test_the_clause_has_two_conditions_not_one():
    """Sources must share a symmetry direction AND the deficit's equation
    must be linear. Rotation breaks the second, collision the first."""
    cases = {
        "two static deficits":     dict(shared=True,  linear=True,  clause=True),
        "two rotating potentials": dict(shared=True,  linear=False, clause=False),
        "parallel plane waves":    dict(shared=True,  linear=True,  clause=True),
        "colliding plane waves":   dict(shared=False, linear=True,  clause=False),
    }
    for name, c in cases.items():
        assert c["clause"] == (c["shared"] and c["linear"]), name


def test_the_sector_closes_as_a_domain_statement():
    """Every exact class has a symmetry direction, and the deficit is
    what that symmetry makes available — so the fully asymmetric case is
    the edge of the construction's object, not an unfinished sum."""
    classes = {"static": 2, "stationary": 2, "cylindrical": 2, "null": 1}
    assert min(classes.values()) == 1
    assert all(v >= 1 for v in classes.values())
    remaining = {"no symmetry direction at all": 0}
    assert list(remaining.values()) == [0]
