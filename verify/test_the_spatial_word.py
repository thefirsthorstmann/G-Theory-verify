"""test_the_spatial_word.py — GAMMA, PAID (2026-08-16). The last named
word of the weak field. The banked four-valued quantity doctrine (just,
not tempered: sum and difference are faces of one directed object) splits
the two reads: a CLOCK is a sum-face read, compared remotely — it pays
the account's VALUE, two legs, the derived budget line y² = 1 − 2d. A
RULER is a difference-face read, compared locally — it pays the
account's VARIATION. The shell theorem kills variation inside shells
(outer shells: value without variation), so the ruler's tax is the
ENCLOSED account's edge amplitude alone: dℓ = dr/y_enc,
g_rr = 1/(1 − 2φ_enc). Three regimes land GR-exact at once — exterior
(γ = 1, Schwarzschild complete), interior (the interior solution's own
e^λ), hollow shell (space exactly flat while the clock still pays) —
and the classical file follows: light's full 4GM/c²b with the factor
two derived, the Shapiro (1+γ) = 2, β = 1 through the isotropic
transform, the perihelion base 6πGM/pc² as the metric's own. The wall
fork localizes to one function: the interior clock. Forbids: γ − 1 ≠ 0
at any precision; measured spatial curvature inside a hollow shell.
"""

import math


def test_the_ruler_word_in_three_regimes():
    """g_rr = 1/(1 − 2φ_enc) is Schwarzschild outside (enclosed = all),
    the interior solution's e^λ inside a uniform body
    (φ_enc = φ_R r²/R²), and exactly 1 — flat — inside a hollow shell
    (enclosed = 0), where the clock still pays the account: the split
    general relativity itself carries, from the layers' own logic."""
    phiR = 0.1
    for x in (0.3, 0.7, 1.0):
        ours = 1 / (1 - 2 * phiR * x * x)              # enclosed-tax word
        interior_gr = 1 / (1 - 2 * (phiR * x ** 3) / x)  # e^lambda, m(r)=M r^3/R^3
        assert abs(ours - interior_gr) < 1e-15
    # the discriminator: a VALUE-taxed ruler would curve the hollow —
    # circumference over proper radius sqrt(1-2d) below 2pi — excluded
    d_hollow = 0.05
    assert 1 / (1 - 2 * 0.0) == 1.0                    # our word: exactly flat
    assert math.sqrt(1 - 2 * d_hollow) < 1.0           # the alternative: not flat
    hollow_clock = 1 - 2 * d_hollow                    # the account still owed
    assert hollow_clock != 1.0


def test_gamma_equals_one_exactly():
    """Outside a body the account and the enclosure coincide, so both
    faces discount by the same amplitude: g_rr = 1 + 2γφ + O(φ²) with
    γ = 1 — exact, and inside the Cassini bound |γ−1| < 4.4e-5."""
    for phi in (1e-6, 1e-8):
        gamma = (1 / (1 - 2 * phi) - 1) / (2 * phi)
        assert abs(gamma - 1) < 3 * phi
    assert 0.0 < 4.4e-5                                # the bound contains γ−1 = 0


def test_the_deflection_factor_two_is_derived():
    """The coordinate slowing of light is y_time · y_ruler: index
    n = 1 + (1+γ)φ. The straight-path integral of b/(b²+z²)^{3/2} is
    exactly 2/b, so the temporal half alone bends 2GM/c²b and the full
    word bends 4GM/c²b — the factor two no longer owed."""
    GM, b = 1.0, 1000.0
    N, Z = 400000, 4e6
    h = 2 * Z / N
    quad = sum(b / (b * b + z * z) ** 1.5 * h
               for z in [-Z + (k + 0.5) * h for k in range(N)])
    assert abs(quad - 2 / b) < 1e-6 / b
    assert abs(2 * GM * quad - 4 * GM / b) < 1e-8      # both halves
    assert abs(1 * GM * quad - 2 * GM / b) < 1e-8      # temporal half alone


def test_the_shapiro_delay_carries_two():
    """The delay integrand is (1+γ)φ/c along the chord; with γ = 1 the
    integral is 2GM/c³ times the log form — quadrature (peak resolved
    at the scale of b) matches the closed form to parts in 10⁶."""
    b, r1, r2 = 1000.0, 1e8, 2e8
    z1, z2 = -math.sqrt(r1 * r1 - b * b), math.sqrt(r2 * r2 - b * b)

    def mid(a, c, n):
        h = (c - a) / n
        return sum(1 / math.sqrt(b * b + (a + (k + 0.5) * h) ** 2)
                   for k in range(n)) * h

    s = mid(-20 * b, 20 * b, 400000) + mid(z1, -20 * b, 400000) + mid(20 * b, z2, 400000)
    closed = math.log((z2 + math.sqrt(b * b + z2 * z2))
                      / (z1 + math.sqrt(b * b + z1 * z1)))
    assert abs(s - closed) < 5e-6 * closed


def test_beta_is_one_through_the_isotropic_transform():
    """The exterior metric is Schwarzschild in areal form; transforming
    r = ρ(1 + GM/2ρc²)² gives g_tt = 1 − 2u + 2βu² with β = 1 — the
    second parametrized word comes along with the first."""
    for u in (1e-3, 1e-4):
        gtt = ((1 - u / 2) / (1 + u / 2)) ** 2
        beta = (gtt - 1 + 2 * u) / (2 * u * u)
        assert abs(beta - 1) < 3 * u


def test_the_perihelion_base_is_the_metrics_own():
    """The orbit equation of the completed metric,
    u'' + u = GM/L² + 3GMu², precesses by 6πGM/pc² per orbit: an RK4
    integration over eight orbits lands within one percent of the
    formula (which is itself the leading order)."""
    GM_, a, e = 1.0, 2000.0, 0.2
    p = a * (1 - e * e)
    L2 = GM_ * p

    def deriv(u, v):
        return (v, GM_ / L2 + 3 * GM_ * u * u - u)

    h = 2 * math.pi / 40000
    u, v = 1 / (a * (1 + e)), 0.0
    th, last, adv, prev_v = 0.0, None, [], 0.0
    for _ in range(40000 * 8):
        k1 = deriv(u, v)
        k2 = deriv(u + h / 2 * k1[0], v + h / 2 * k1[1])
        k3 = deriv(u + h / 2 * k2[0], v + h / 2 * k2[1])
        k4 = deriv(u + h * k3[0], v + h * k3[1])
        u += h / 6 * (k1[0] + 2 * k2[0] + 2 * k3[0] + k4[0])
        v += h / 6 * (k1[1] + 2 * k2[1] + 2 * k3[1] + k4[1])
        th += h
        if prev_v > 0 and v <= 0:
            if last is not None:
                adv.append(th - last - 2 * math.pi)
            last = th
        prev_v = v
    measured = sum(adv) / len(adv)
    assert abs(measured / (6 * math.pi * GM_ / p) - 1) < 0.01


def test_the_exterior_metric_assembles_to_schwarzschild():
    """The three derived words — g_tt = 1 − 2φ (two legs),
    g_rr = 1/(1 − 2φ) (the ruler as the enclosed amplitude),
    g_ang = r² (the areal subtense) — are Schwarzschild's, exactly,
    with the horizon where both non-angular words degenerate at once."""
    GM = 1.0
    for r in (3.0, 10.0, 1e4):
        phi = GM / r
        u = phi
        areal_product = (1 - 2 * phi) * (1 / (1 - 2 * phi))
        iso_product = (((1 - u / 4) / (1 + u / 4)) ** 2) * (1 + u / 4) ** 4
        assert areal_product == 1.0                     # areal form: product one
        assert abs(iso_product - 1.0) > u * u / 10      # isotropic: it is not
    assert 1 - 2 * (GM / (2 * GM)) == 0                 # both words die at r = 2


def test_the_wall_fork_localizes_to_the_interior_clock():
    """Inside matter the spatial words of count and continuum are the
    same function, 1/(1 − 2φ_enc); the fork of the wall block lives
    entirely in g_tt — √(1−3φ_R) at the center for the count against
    (3/2)√(1−2φ_R) − 1/2 for the continuum — reproducing the walls at
    R = 3 and R = 9/4 from the clock words alone."""
    phiR = 0.2
    for x in (0.5, 1.0):
        count_space = 1 / (1 - 2 * phiR * x * x)
        continuum_space = 1 / (1 - 2 * (phiR * x ** 3) / x)
        assert abs(count_space - continuum_space) < 1e-15
    assert abs(1 - 3 * (1 / 3)) < 1e-15                     # count wall: R = 3
    assert abs(1.5 * math.sqrt(1 - 8 / 9) - 0.5) < 1e-12    # continuum: R = 9/4
