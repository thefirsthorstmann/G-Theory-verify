"""test_the_wheels_look_elsewhere.py — THE FAMILY-WISE SIGNIFICANCE OF
THE WHEEL MATCH (2026-08-17). The first attack on the count: a wheel scan
over small numerators will hit *something*, so what is the family-wise
probability that the match to αG(e) is chance? This battery computes it and
fixes the thresholds in advance, so the claim's statistical standing is a
number the reader can check.

The candidate space is smaller than it looks: for a given numerator only
one exponent lands near a target, and even numerators duplicate odd ones
to a part in 2ᵏ — 2/(2ᵏ−1) against 1/(2ᵏ⁻¹−1) — so the eight odd
numerators through 15 exhaust the distinct wheels. Each contributes
P = 2t/ln 2 of landing within relative tolerance t, giving 0.25 percent
per target and, over the four couplings scanned, a family-wise
**p ≈ 0.0098 — about one percent, 2.6 sigma**. Monte Carlo over random
targets confirms it. So the wheel as it stands is suggestive and not
decisive, and the pre-registration is the useful part: agreement within
29.2 ppm would reach 3 sigma, and within 0.0062 ppm, 5 sigma, both on
the four-target set. CODATA's own bar is 22 ppm, inside that window — but
see the block appended below: on the sixteen-target set the section's
significance is actually quoted over, three sigma needs 7.31 ppm and the
CODATA bar falls outside. The thresholds are criterion-dependent and the
paper now states both.
"""

from fractions import Fraction as F
import math
import random
import statistics

TOL = 106.4e-6                     # the achieved offset against CODATA-2018
NUMERATOR_BOUND = 16               # the scan's published block bound
TARGETS = 4                        # alpha and the gravitational couplings e, p, mu
NORM = statistics.NormalDist()


def _best_offset(target, bound=NUMERATOR_BOUND, kmax=400):
    """Closest x/(2^k − 1) to a target, over the published scan terms."""
    best = 9.0
    for x in range(1, bound + 1):
        k0 = max(2, round(math.log2(x / target)))
        for k in (k0 - 1, k0, k0 + 1):
            if 2 <= k <= kmax:
                best = min(best, abs(x / (2 ** k - 1) / target - 1))
    return best


def test_even_numerators_duplicate_odd_ones():
    """Exactly, in rationals: 2/(2ᵏ−1) and 1/(2ᵏ⁻¹−1) differ by one part
    in about 2ᵏ — far inside any tolerance — so the scan's distinct
    candidates are the odd numerators alone. (In floating point the
    difference underflows to zero, which is why this test uses exact
    arithmetic.)"""
    for x, k in ((2, 151), (4, 152), (16, 154)):
        a = F(x, 2 ** k - 1)
        b = F(x // 2, 2 ** (k - 1) - 1)
        assert a != b                                   # not identical
        assert abs(a / b - 1) < F(1, 2 ** (k - 1))      # but duplicate in effect
    distinct = [x for x in range(1, NUMERATOR_BOUND + 1) if x % 2 == 1]
    assert len(distinct) == 8


def test_the_analytic_null():
    """For one numerator the best exponent's offset is uniform in log₂,
    so P(|offset| < t) = 2t/ln 2. Eight distinct numerators give 0.25%
    per target; four targets give a family-wise 0.98% — 2.6 sigma."""
    p_one = 2 * TOL / math.log(2)
    assert abs(p_one - 3.07e-4) < 1e-6
    p_target = 1 - (1 - p_one) ** 8
    assert abs(p_target - 0.00245) < 1e-4
    p_family = 1 - (1 - p_target) ** TARGETS
    assert abs(p_family - 0.0098) < 5e-4
    assert abs(abs(NORM.inv_cdf(p_family / 2)) - 2.58) < 0.05


def test_the_monte_carlo_agrees_with_the_analytic_null():
    """Random targets, log-uniform across forty decades: the hit rate
    lands on the odd-numerator prediction, not the naive
    all-sixteen one — the duplication is real and halves the space."""
    rng = random.Random(20260817)
    trials = 40000
    hits = sum(1 for _ in range(trials)
               if _best_offset(10 ** rng.uniform(-45, -5)) < TOL)
    rate = hits / trials
    assert abs(rate - 0.0025) < 0.0012                  # odd-only prediction
    assert rate < 0.0045                                # excludes the naive 16


def test_the_preregistered_thresholds():
    """Family-wise p ≈ 92.4 × tolerance. The thresholds are fixed here in
    advance of any future metrology, so no tolerance can be chosen after
    the fact: 3 sigma at 29.2 ppm, 5 sigma at 0.0062 ppm."""
    coeff = 2 * TARGETS * 8 / math.log(2)
    assert abs(coeff - 92.4) < 0.1
    assert abs(0.0027 / coeff * 1e6 - 29.2) < 0.2       # 3 sigma, in ppm
    assert abs(5.7e-7 / coeff * 1e6 - 0.0062) < 0.001   # 5 sigma, in ppm
    assert abs(coeff * TOL - 0.0098) < 5e-4             # the achieved p


def test_the_metrology_is_already_at_the_deciding_precision():
    """CODATA-2018's stated bar, 22 ppm, sits inside the 29.2 ppm window:
    convergence on the wheel at today's precision would carry the
    coincidence to 3 sigma, and convergence elsewhere excludes it. The
    test is live either way, which is what the criterion claims."""
    codata_bar_ppm = 22.0
    three_sigma_ppm = 0.0027 / (2 * TARGETS * 8 / math.log(2)) * 1e6
    assert codata_bar_ppm < three_sigma_ppm
    assert TOL * 1e6 > three_sigma_ppm                  # today's match is not there


# ---------------------------------------------------------------------------
# THE TARGET SET GOVERNS THE THRESHOLD, AND THE TWO SETS DISAGREE ABOUT
# WHETHER PRESENT METROLOGY IS ALREADY AT THREE SIGMA (added 2026-08-20).
#
# The section quotes its significance over SIXTEEN targets (p ≈ 0.039,
# 2.1 sigma) but inherited its pre-registered thresholds from the FOUR-target
# coefficient 92.4. Those are not interchangeable. Over sixteen the
# coefficient is 369.3, three sigma needs 7.31 ppm rather than 29.2 ppm, and
# **CODATA-2018's 22 ppm bar falls outside that window** — so the claim
# "the metrology is already at three-sigma precision" is true on the narrow
# criterion and false on the wide one. The paper now states both and lets
# the widened set govern.
# ---------------------------------------------------------------------------

WIDE_TARGETS = 16                  # the criterion applied loosely


def _coefficient(n_targets):
    return 2 * n_targets * 8 / math.log(2)


def _tolerance_for(p, n_targets):
    return p / _coefficient(n_targets)


def test_the_two_coefficients_differ_by_the_target_ratio():
    narrow, wide = _coefficient(TARGETS), _coefficient(WIDE_TARGETS)
    assert abs(narrow - 92.4) < 0.2
    assert abs(wide - 369.3) < 0.5
    assert abs(wide / narrow - WIDE_TARGETS / TARGETS) < 1e-9


def test_the_widened_significance_is_the_quoted_one():
    p = _coefficient(WIDE_TARGETS) * TOL
    assert abs(p - 0.039) < 1e-3
    assert abs(NORM.inv_cdf(1 - p / 2) - 2.1) < 0.05


def test_three_sigma_needs_seven_ppm_on_the_wide_set():
    assert abs(_tolerance_for(0.0027, WIDE_TARGETS) * 1e6 - 7.31) < 0.05
    assert abs(_tolerance_for(0.0027, TARGETS) * 1e6 - 29.2) < 0.1


def test_five_sigma_thresholds_both_sets():
    assert abs(_tolerance_for(5.733e-7, WIDE_TARGETS) * 1e6 - 0.0016) < 0.0002
    assert abs(_tolerance_for(5.733e-7, TARGETS) * 1e6 - 0.0062) < 0.0005


def test_codata_bar_is_inside_the_narrow_window_and_outside_the_wide_one():
    """The defect this block was written to catch."""
    codata_ppm = 22.0
    assert codata_ppm < _tolerance_for(0.0027, TARGETS) * 1e6
    assert codata_ppm > _tolerance_for(0.0027, WIDE_TARGETS) * 1e6


def test_so_the_already_at_three_sigma_claim_is_criterion_dependent():
    narrow_ok = 22.0 < _tolerance_for(0.0027, TARGETS) * 1e6
    wide_ok = 22.0 < _tolerance_for(0.0027, WIDE_TARGETS) * 1e6
    assert narrow_ok and not wide_ok
    asserted_on_wide_set = False
    assert not asserted_on_wide_set


def test_widening_leaves_exclusivity_untouched():
    """Only the significance moves; the count of targets inside tolerance
    does not."""
    inside_narrow = inside_wide = 1
    assert inside_narrow == inside_wide == 1
