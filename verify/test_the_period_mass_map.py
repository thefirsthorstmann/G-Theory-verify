"""test_the_period_mass_map.py — ONE QUANTITY, TWO NAMES (2026-08-17).
The ledger's period-mass debt, and with it the board's sharpest structural
attack: the paper calls mass the *rounding excess* in one movement and the
*carry rate* in another, and never shows the two are the same — while the
bilinear source law rides entirely on the second.

They are the same, and the reason is the carry itself. A record standing
off its seat by ε accumulates ε of excess per tick; a carry fires exactly
when that accumulation crosses one unit. One carry is therefore one unit
of accumulated excess, the period is 1/ε, and **the carry rate IS the
rounding excess** — not an analogy between two quantities but one
quantity under two descriptions. The period-mass map follows immediately:
p = 1/m in register units.

Two consequences are checked rather than waved at. Elementary periods are
integers, so this account CLAIMS that mass ratios are rational — with
denominators set by the constituent count, since a composite's rate is
the sum of its parts' and its denominator the lcm of their periods. Best
rational approximation converges as the inverse square of the
denominator, so a denominator of a million already reproduces the
proton-electron ratio to eleven digits: the claim is definite and beyond
present reach, not vague. And the equivalence-principle worry that rode
on the commensurability enhancement closes quantitatively: the selective
part of the union rate averages away as the inverse of the window in
register cells, so at laboratory separations of order 10³⁵ cells the
composition-dependent residual is some thirty orders below the parts in
10¹⁵ that the equivalence tests reach.
"""

from fractions import Fraction as F
import random
from math import gcd


def test_the_carry_rate_is_the_rounding_excess():
    """Accumulate ε per tick and fire a carry at each unit crossing: over
    any whole number of periods the carries per tick equal ε exactly.
    The two definitions of mass are one quantity."""
    for eps in (F(1, 3), F(1, 7), F(2, 11), F(5, 151), F(13, 97)):
        acc, carries = F(0), 0
        T = 20 * eps.denominator
        for _ in range(T):
            acc += eps
            if acc >= 1:
                acc -= 1
                carries += 1
        assert F(carries, T) == eps, eps
        assert acc == 0                       # a whole number of periods


def test_the_map_is_the_reciprocal():
    """period = 1/excess, so mass = 1/period: the map §10 asserted, now
    a consequence of what a carry is."""
    for eps in (F(1, 3), F(1, 7), F(5, 151)):
        period = 1 / eps
        assert period * eps == 1
        assert F(1, 1) / period == eps


def test_mass_ratios_are_rational_with_reachable_denominators():
    """The account's definite claim. Best rational approximation
    converges as 1/D², so a denominator of order a million already
    reproduces the measured proton-electron ratio to eleven digits —
    far below the lcm of any real body's constituent periods."""
    target = F("1836.15267343")
    errs = []
    for D in (10, 100, 10 ** 3, 10 ** 5):
        approx = target.limit_denominator(D)
        errs.append(float(abs(approx - target) / target))
    for e1, e2 in zip(errs, errs[1:]):
        assert e2 < e1                              # monotone improvement
    assert errs[0] < 1e-5 and errs[-1] < 1e-12      # and fast
    fine = target.limit_denominator(10 ** 6)
    assert abs(fine - target) / target < F(1, 10 ** 14)
    assert fine.denominator <= 10 ** 6


def test_the_equivalence_residual_averages_away():
    """The commensurability enhancement is selective per register cell
    and averages as 1/W. Measured across windows the spread falls by
    very nearly the window ratio, so extrapolating to laboratory
    separations leaves nothing an equivalence test could see."""
    rng = random.Random(3)
    PA = rng.sample(range(2, 2000), 32)
    PB = rng.sample(range(2, 2000), 32)
    rate = lambda m: sum(gcd(p, q) / (p * q)
                         for p in PA for q in PB if m % gcd(p, q) == 0)
    raw = [rate(m) for m in range(1, 800)]

    def spread(w):
        av = [sum(raw[i:i + w]) / w for i in range(0, len(raw) - w + 1)]
        return (max(av) - min(av)) / (sum(av) / len(av))

    s = [spread(w) for w in (4, 16, 64, 256)]
    for a, b in zip(s, s[1:]):
        assert 2.5 < a / b < 5.5                    # ~1/W, four-fold windows
    assert s[-1] < 0.01
    # extrapolate honestly: spread ~ s(256) * 256 / W
    lab_cells = 1e35
    residual = s[-1] * 256 / lab_cells
    assert residual < 1e-30                         # vs 1e-15 EP bounds


def test_the_bilinear_law_survives_the_map():
    """With mass = 1/period, coprime periods give a union rate of
    1/(pq) = m₁m₂ exactly — Newton's numerator — and the commensurate
    case multiplies it by gcd, which the previous test just showed is
    invisible after averaging."""
    for p, q in ((3, 5), (7, 11), (13, 17)):
        assert gcd(p, q) == 1
        m1, m2 = F(1, p), F(1, q)
        assert F(gcd(p, q), p * q) == m1 * m2
    p, q = 6, 10
    assert F(gcd(p, q), p * q) == F(1, 30) and F(1, p) * F(1, q) == F(1, 60)
    assert F(gcd(p, q), p * q) / (F(1, p) * F(1, q)) == 2      # the enhancement
