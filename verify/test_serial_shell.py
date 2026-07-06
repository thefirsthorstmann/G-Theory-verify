"""test_serial_shell.py — Theorem 1 (the supertask/depletion bound) pinned."""

from fractions import Fraction as F

from serial_shell import (coherence_depth, demand, exponential_beats_linear,
                          supertask_ratio_bound, supply)


def test_demand_is_exact_sevenths():
    """D(N) = (8^(N+1)-1)/7 for all N — the ring-sum counted in sevenths."""
    for n in range(21):
        assert 7 * demand(n) == 8 ** (n + 1) - 1
    assert demand(10) == 1_227_133_513            # > 10^9 cells by rung 10


def test_the_supertask_is_kinematically_open():
    """The rational chain: 4 > 27/8 => 2^(2/3) > 3/2 => r < 2/3 =>
    Sum tau_n < 3 tau_0 — infinitely many turnovers fit in finite time.
    This is the concession made honestly: the continuum leaves the
    door open; the METER is what closes it."""
    lhs, rhs, bound = supertask_ratio_bound()
    assert lhs > rhs                              # 4 > 27/8, exact
    assert bound == 3                             # sum < 3 tau_0
    # float sanity (marked): the true ratio and sum
    r = 2 ** (-2 / 3)
    assert r < 2 / 3 and 1 / (1 - r) < 3


def test_exponential_demand_beats_linear_supply():
    """8^n > a*n eventually, for any linear rate a — pinned instance +
    the induction ratio (8^(n+1) = 8 * 8^n vs a(n+1) < 2an for n>=1)."""
    assert exponential_beats_linear(100, 3, 50)
    assert exponential_beats_linear(10 ** 6, 8, 50)
    for n in range(1, 30):                        # the ratio strictly worsens
        assert 8 ** (n + 1) * n >= 2 * 8 ** n * (n + 1)


def test_the_reach_is_logarithmic():
    """Concrete meters: even 10^15 serial ops reach depth 16; x1000 the
    budget yields THREE octaves more. Tao's choreography needs ALL depths."""
    assert coherence_depth(10 ** 15) == 16
    assert coherence_depth(10 ** 18) == 19
    assert coherence_depth(10 ** 21) == 23
    # bounded parallelism does not rescue the supertask:
    assert coherence_depth(10 ** 15, p=1000) == 19


def test_real_flows_sit_inside_the_budget():
    """The statistical cascade is untouched: ~(3/4)log2(Re) octaves;
    Re = 10^8 -> ~20 rungs; demand(20) ~ 10^18 ops spread over the
    flow's UNBOUNDED time — only finite-time UNBOUNDED depth is barred."""
    import math
    rungs = int(0.75 * math.log2(10 ** 8))
    assert rungs == 19 and demand(rungs) < 10 ** 18


def test_no_finite_depth_completes_the_choreography():
    """The singularity requires every depth: for ANY finite budget B
    there is a depth whose demand exceeds B — the supertask fails."""
    for budget in (10 ** 6, 10 ** 12, 10 ** 24, 10 ** 48):
        n = coherence_depth(budget)
        assert demand(n + 1) > budget             # always a first unmet shell


def test_bkm_integral_counts_shells():
    """tau_n * omega_n = 1 identically — the BKM integral through depth
    N equals N+1 units: divergence <=> unbounded depth, exactly."""
    from serial_shell import bkm_shell_terms
    terms = bkm_shell_terms(30)
    assert all(t == 1 for t in terms)
    assert sum(terms) == 31
    terms_k41 = bkm_shell_terms(30, r=F(2, 3))   # any ratio: still exact
    assert all(t == 1 for t in terms_k41)


def test_the_rate_leg_closes_the_concentrated_collapse():
    """The loophole: a single-filament self-similar collapse has LINEAR
    demand (O(1) cells per shell) and evades the census count. The
    rate leg closes it: the ML minimum transition time floors the
    shrinking turnover schedule at a finite depth (~187 octaves for
    the reference fluid at its own turnover tau_0 = l_0/v_0 = 0.1 s —
    the referee-pass correction of the earlier 191, which had conflated
    the elapsed time T = 1 s with tau_0) — still infinitely short of
    the BKM census."""
    from serial_shell import rate_depth_cap
    cap = rate_depth_cap(5e4, 0.1)
    assert 183 < cap < 190                        # ~187: finite; blow-up needs infinity
    assert rate_depth_cap(9e13, 1.0) < 250        # even 1 g of mc^2: finite


def test_the_universal_form_kills_every_schedule():
    """Referee-pass strengthening: the rate leg is SCHEDULE-UNIVERSAL.
    Any summable schedule (geometric, polynomial, anything) has
    tau_n -> 0, so it crosses the ML floor at a finite stage — the
    supertask fails with no scaling assumption at all."""
    from serial_shell import universal_stage_cap
    t_min = 3.31e-39                              # pi hbar / 2E for 5e4 J
    k41 = lambda n: 1.0 * 2 ** (-2 * n / 3)      # the K41 geometric schedule
    poly = lambda n: 1.0 / (n + 1) ** 2          # a non-geometric summable one
    slow = lambda n: 1.0 / (n + 1) ** 1.01       # barely-summable
    assert universal_stage_cap(k41, t_min) == 192          # matches the cap
    assert universal_stage_cap(poly, 1e-6) == 1000         # 1/(n+1)^2 < 1e-6
    assert universal_stage_cap(slow, 1e-3) == 933
    # and a NON-summable schedule never finishes in finite time anyway:
    # infinite total time is not a supertask — outside the theorem's scope.


def test_the_physical_meters():
    """Margolus-Levitin instantiation (floats, marked): a cubic meter of
    water at 10 m/s holds ~5e4 J kinetic; its quantum operation ceiling
    over one second allows depth 42. Lloyd's bound for the whole
    observable universe (~1e120 ops) allows depth 132. The physical
    cascade of that water (Re ~ 1e7) runs at depth 17 — comfortably
    real. The choreography requires depth INFINITY."""
    from serial_shell import kolmogorov_depth, ml_ops
    ops = ml_ops(5e4, 1.0)
    assert 1e38 < ops < 1e39
    assert coherence_depth(int(ops)) == 42
    assert coherence_depth(10 ** 120) == 132
    assert kolmogorov_depth(1e7) == 17
    assert kolmogorov_depth(1e7) < 42             # nature fits its budget
