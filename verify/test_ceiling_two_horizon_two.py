"""test_ceiling_two_horizon_two.py — CEILING-2 → HORIZON-2 (2026-08-16).
The dig the G file pointed at: derive the Schwarzschild coefficient from
the register instead of reading it. The parent that works is the MIRROR:
an observation is a round trip across the antipodal pair (§3's arena),
its two legs each spend the one-way deficit φ = GM/rc², and counting is
linear — so the observed budget is exactly 1 − 2φ, §21's half-power read
y = √Φ is its amplitude, and the budget dies at φ = 1/2: r = 2GM/c².
The coefficient of the horizon is the number of legs in an observation.
From the budget line + φ = M/r (banked) + the areal subtense r² + \
stationarity, four of the six landmarks DERIVE by extremal calculus —
no radial spatial word ever enters, because circular records never move
radially. The wall (interior) and the spatial word γ stay owed, by name.
"""

from fractions import Fraction as F
import math


def E2(p):
    """Circular-orbit energy², timelike, from the budget line alone."""
    return (1 - 2 * p) ** 2 / (1 - 3 * p)


def test_the_budget_line_and_the_horizon():
    """Two legs × φ, linear counting: budget = 1 − 2φ exactly. Death at
    φ = 1/2 — the horizon at r = 2GM/c², coefficient = the mirror's two."""
    phi = F(1, 2)
    assert 1 - 2 * phi == 0
    assert 1 / phi == 2                       # r in units of GM/c²
    for p in (F(1, 10), F(1, 100)):           # weak field: one-way = 1 − φ + O(φ²)
        one_way = math.sqrt(1 - 2 * p)        # the amplitude, §21's y = √Φ
        assert abs(one_way - (1 - p)) < 2 * float(p) ** 2


def test_kepler_survives_from_the_gradient_balance():
    """Circular stationarity balances the budget gradient against the
    subtense gradient: d(1−2φ)/dr = d(r²)/dr · Ω² with φ = M/r gives
    Ω² = M/r³ — Kepler's third law exact at every depth of the strong
    field, in the areal read. No radial metric word appears."""
    M = F(1)
    for r in (F(3), F(4), F(6), F(50), F(1000)):
        lhs = 2 * M / r ** 2                  # d(1−2M/r)/dr
        omega2 = M / r ** 3
        rhs = 2 * r * omega2                  # d(r²)/dr · Ω²
        assert lhs == rhs


def test_the_photon_sphere_and_the_shadow():
    """The local orbital speed² is φ/(1−2φ): it reaches light at exactly
    φ = 1/3 — the photon sphere at r = 3. Equivalently the null figure
    (1−2φ)φ² peaks there: derivative 2φ(1−3φ). The capture parameter
    b² = 1/(φ²(1−2φ)) evaluates to 27 at the peak: b = 3√3, the shadow,
    27 = 3³ — Re's seat, exactly as the ladder's table reads it."""
    assert F(F(1, 3), 1 - 2 * F(1, 3)) == 1
    d = lambda p: 2 * p * (1 - 3 * p)
    assert d(F(1, 3)) == 0
    assert 1 / (F(1, 3) ** 2 * (1 - 2 * F(1, 3))) == 27


def test_the_marginal_bound_and_the_isco():
    """E² = (1−2φ)²/(1−3φ). E = 1 forces 4φ² = φ: the marginally bound
    circle at φ = 1/4, r = 4. The stability edge is the factorization
    dE²/dφ ∝ (1−2φ)(6φ−1) — the hexad's coefficient — zero at φ = 1/6:
    the innermost stable orbit at r = 6, with E² = 8/9 exactly (the
    whole tone, inverted: one tone of intensity below rest) and
    L² = 12 (GM/c)² — A3's ring. Binding fraction 1 − √(8/9) = 5.72%,
    the non-rotating accretion efficiency."""
    assert E2(F(1, 4)) == 1
    for p in (F(1, 7), F(2, 11), F(3, 13), F(1, 5)):
        h = F(1, 10 ** 9)
        numeric = (E2(p + h) - E2(p - h)) / (2 * h)
        closed = (1 - 2 * p) * (6 * p - 1) / (1 - 3 * p) ** 2
        assert abs(numeric - closed) < F(1, 10 ** 6)
    assert (1 - 2 * F(1, 6)) * (6 * F(1, 6) - 1) == 0
    assert E2(F(1, 6)) == F(8, 9)
    assert 1 / (F(1, 6) * (1 - 3 * F(1, 6))) == 12
    assert abs((1 - math.sqrt(8 / 9)) - 0.0572) < 0.0001


def test_the_ladder_is_harmonic_in_the_deficit():
    """The landmarks in deficit units: φ = 1/2, 4/9, 1/3, 1/4, 1/6.
    The four derived rungs are the string's two-and-three partials —
    the fifth partial absent as the algebra demands — and the read wall is (2/3)².
    The ratios are the intervals the file already states: photon to
    horizon 3/2 the fifth, ISCO to photon 2 the octave, wall to horizon
    9/8 the tone."""
    derived = [F(1, 2), F(1, 3), F(1, 4), F(1, 6)]
    assert [1 / p for p in derived] == [2, 3, 4, 6]        # 3-smooth, no 5
    wall = F(4, 9)
    assert wall == F(2, 3) ** 2 and 1 / wall == F(9, 4)
    r = {"horizon": F(2), "photon": F(3), "isco": F(6), "wall": F(9, 4)}
    assert r["photon"] / r["horizon"] == F(3, 2)
    assert r["isco"] / r["photon"] == 2
    assert r["wall"] / r["horizon"] == F(9, 8)


def test_the_three_twos_are_one_number():
    """The working parent is the mirror's two — the legs of a round
    trip. The octave's two and the tower's two are the same number by
    exact identity: the doubling equals the sum of all halvings,
    Σ 2⁻ʲ = 2, with the finite register stopping 2⁻¹⁹⁹ short at depth
    200 — the ceiling the strong-field file already pins. The tower
    totals of other bases (3/2, 10/9) are recorded as the dress's
    arithmetic, with no physical claim riding on them here."""
    tower = sum(F(1, 2 ** j) for j in range(0, 200))
    assert 2 - tower == F(1, 2 ** 199)
    assert sum(F(1, 2 ** j) for j in range(0, 60)) < 2     # never attained
    assert F(3, 3 - 1) == F(3, 2) and F(10, 10 - 1) == F(10, 9)


def test_the_never_attained_clause_is_a_supertask():
    """Approaching the horizon halves the remaining budget one register
    depth at a time: after N steps the remainder is exactly 2⁻ᴺ of the
    start — geometric, positive at every finite depth. Resolving φ = 1/2
    exactly is the same unfinishable census that excludes the
    singularity in §12, one level up: the floor is approached forever
    and occupied never, in every outside read."""
    gap = F(1, 4)                              # start at φ = 1/4, gap to 1/2
    for n in range(1, 120):
        gap = gap / 2
        assert gap == F(1, 4) / 2 ** n and gap > 0
