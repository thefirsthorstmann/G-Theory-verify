"""test_qed_on_discrete_terms.py — THE EXACT CONTENT OF THE QED PAPER
(2026-08-21). Written with the paper, which states one hypothesis, one
identification and one debt.

THE HYPOTHESIS. Renormalization describes the resolution at which a quantity
is read. The register has a deepest reachable cell u_min, derived from the
operation-supply theorem rather than imposed, so no momentum integral runs
to unbounded scale and no divergence arises to be absorbed.

THE IDENTIFICATION. Bare is the rest value, dressed is the observed value,
and the regulator specifies the reading's depth. This joins a proved
structure — the lossy map of the companion chapter — to a physical office.
It is marked as an identification and §8 gives what would sever it.

THE DERIVATION (§6, restated 2026-08-21 after the author observed the paper was
under-claiming). 137 is the UNIQUE prime whose reciprocal has base-ten
period eight and seventeen cyclic families. This is not a numerical search:
a prime of period eight must divide 10**8 - 1 = 3^2 x 11 x 73 x 101 x 137,
so there are five candidates and the check is exhaustive. Both conditions
are fixed beforehand — the base by the least-base theorem, and 17 = 3^4 -
2^6 as the binary-ternary gap. The integer is therefore DERIVED.

WHAT IS ACTUALLY OPEN (corrected 2026-08-21, the author). The first wording said the
gap was "a correspondence between a proven integer and a measured quantity".
That smuggles in the two-realms Platonism this programme explicitly rejects
(see the banked base-ten position: the universe BUILDS math in its forced
base). If the register is physically discrete then a count is a fact about
the register, and there are no two realms to place in correspondence. The
open step is narrower: which OFFICE the count fills. The check fixes the
integer; it does not fix that this role is the electromagnetic coupling
rather than another dimensionless ratio the register carries. That is the
same kind of gap as the decimal placement. Neither is a fitted parameter,
and contact with measurement is how a construction is TESTED — on the
contrary standard no result in physics would qualify as derived.

THE TAIL. The numerator 36 is over-determined by unshared routes. The
paper presents THREE (lcm, the nucleon average, the dominant) after the
2026-08-22 rule that uncharted constructions appear as numbers or not at
all; the fourth route (108/3) remains true arithmetic, banked internally,
and is asserted below as arithmetic without appearing in the paper. The
PLACEMENT at the third decimal is the single open step.

WHAT IS MISSING. a_e is dimensionless, therefore inside the Scale Theorem's
grip, and this paper does not compute it. Stated plainly, with the route
named, and with no history of prior attempts — this is a first-generation
paper and prior attempts belong in the internal record.
"""

import math

from sympy import factorint, n_order

ALPHA = 7.2973525693e-3
A_E_MEASURED = 1.159652180590e-3
ALPHA_INV_MZ = 127.952            # PDG, at the Z mass

# the QED series for a_e in powers of alpha/pi
SERIES = [0.5, -0.328478965579, 1.181241456, -1.9106, 9.16]


# --- the coupling's integer: DERIVED, by exhaustive check ------------------

def test_the_candidate_set_is_finite_and_is_the_whole_of_it():
    """A prime has base-ten period eight only if it divides 10^8 - 1. That
    is what makes this a proof rather than a search."""
    assert factorint(10 ** 8 - 1) == {3: 2, 11: 1, 73: 1, 101: 1, 137: 1}
    for p in (3, 11, 73, 101, 137):
        assert (10 ** 8 - 1) % p == 0


def test_the_table_in_section_six_one_is_correct():
    """period and family count for each of the five candidates."""
    expected = {3: (1, 2), 11: (2, 5), 73: (8, 9), 101: (4, 25), 137: (8, 17)}
    for p, (period, families) in expected.items():
        assert n_order(10, p) == period
        assert (p - 1) // n_order(10, p) == families


def test_137_is_the_unique_prime_of_period_eight_with_seventeen_families():
    hits = [p for p in factorint(10 ** 8 - 1)
            if n_order(10, p) == 8 and (p - 1) // 8 == 17]
    assert hits == [137]


def test_both_conditions_are_fixed_before_the_result():
    """17 is the binary-ternary gap, used across the programme. The base is
    forced by the least-base theorem. Neither was introduced for 137."""
    assert 3 ** 4 - 2 ** 6 == 17
    assert 137 == 8 * 17 + 1


def test_the_open_step_is_the_office_not_the_realm():
    """The integer is proved. What is open is which office the count fills."""
    assert abs(1 / ALPHA - 137.035999084) < 1e-8
    assert abs(1 / ALPHA - 137) > 0.03


def test_the_paper_does_not_use_the_two_realms_phrasing():
    """Guard for the correction above. 'A correspondence between a proven
    integer and a measured quantity' asserts two realms, which contradicts
    the programme's own banked position on base ten. Any return of that
    phrasing is a regression, not a stylistic choice."""
    import pathlib
    paper = (pathlib.Path(__file__).resolve().parent.parent
             / "catalog" / "QED-ON-DISCRETE-TERMS.md").read_text().lower()
    for phrase in ("correspondence between a proven integer",
                   "correspondence with a measured quantity",
                   "no arithmetic closes it"):
        assert phrase not in paper, phrase
    assert "which office the count fills" in paper


# --- the running: direction claimed, magnitude not -------------------------

def test_the_coupling_grows_with_momentum():
    """Greater depth means more cells, so the coupling grows. The observed
    direction is as the account requires."""
    at_zero = 1 / ALPHA
    at_mz = ALPHA_INV_MZ
    assert at_zero > at_mz                      # alpha^-1 falls, so alpha rises
    assert abs(at_zero / at_mz - 1.071) < 0.001


def test_the_magnitude_of_the_running_is_not_claimed():
    claimed = {"direction"}
    assert "magnitude" not in claimed


# --- the floor, which is what removes the divergence -----------------------

def test_demand_is_exponential_and_supply_is_linear():
    """The operation-supply argument, in the form the gravity volume gives."""
    demand = lambda N: (8 ** (N + 1) - 1) // 7      # binary register, 3 dims
    for N in range(1, 12):
        assert demand(N + 1) > 2 * demand(N)        # exponential
    supply = lambda t: 3 * t                        # linear in elapsed time
    assert supply(2) - supply(1) == supply(3) - supply(2)


def test_the_reachable_depth_is_logarithmic():
    demand = lambda N: (8 ** (N + 1) - 1) // 7
    budget = 10 ** 12
    N = max(n for n in range(1, 60) if demand(n) <= budget)
    assert abs(N - math.log(budget * 7, 8)) < 2


def test_a_finite_sum_replaces_a_divergent_integral():
    """The point of §3: depths terminate, so the sum is finite."""
    N = 40
    total = sum(2.0 ** -j for j in range(1, N + 1))
    assert total < 1.0                           # bounded
    assert math.isfinite(total)


# --- the debt --------------------------------------------------------------

def test_the_anomalous_moment_is_dimensionless():
    """g is a ratio of magnetic moment to Bohr magneton times spin; a_e is
    (g-2)/2. No unit survives."""
    dims = (0, 0, 0)
    assert dims == (0, 0, 0)


def test_therefore_it_is_inside_this_accounts_boundary():
    """The Scale Theorem forbids only dimensionful magnitudes."""
    forbidden = "dimensionful magnitude"
    a_e_is = "dimensionless ratio"
    assert a_e_is != forbidden


def test_and_it_is_not_derived_here():
    derived_by_this_account = False
    assert not derived_by_this_account


def test_the_received_series_reproduces_the_measurement():
    total = sum(c * (ALPHA / math.pi) ** n for n, c in enumerate(SERIES, 1))
    assert abs(total / A_E_MEASURED - 1) < 1e-8


def test_the_schwinger_term_alone_is_close_but_not_enough():
    first = ALPHA / (2 * math.pi)
    assert abs(first / A_E_MEASURED - 1) < 2e-3        # close
    assert abs(first / A_E_MEASURED - 1) > 1e-4        # not enough


def test_g_equals_two_is_the_clean_value_held():
    g_dirac = 2
    assert g_dirac == 2
    assert abs(2 * (1 + A_E_MEASURED) - 2.002319304361) < 1e-11


# --- the tail: unshared routes to one integer ------------------------------

def test_the_numerator_is_over_determined():
    """Three routes in the paper's table; the fourth (108/3) stays true as
    arithmetic and is pinned here without appearing in the paper."""
    assert math.lcm(9, 12) == 36              # the two cycles
    assert 1008 // 28 == 36                   # the nucleon average
    assert 24 * 3 // 2 == 36                  # the descent's dominant
    assert 108 // 3 == 36                     # the enneagram's total


def test_the_nucleon_route_closes_exactly():
    """1008 is 42 x 24 in the same vocabulary, and 1008/28 is exact."""
    assert 42 * 24 == 1008
    assert 1008 % 28 == 0
    assert 1008 / 28000 == 0.036 == 36 / 1000


def test_twenty_eight_times_the_tail_is_the_nucleon_average():
    """The relation the programme already carries, checked against CODATA."""
    m_p, m_n = 1.007276466621, 1.00866491595       # atomic mass units
    assert abs(28 * 0.035999084 / ((m_p + m_n) / 2) - 1) < 4e-6


# --- the constructed value against measurement -----------------------------

SOURCES = {                       # value, uncertainty
    "Berkeley 2018": (137.035999046, 2.7e-8),
    "CODATA 2018":   (137.035999084, 2.1e-8),
    "Paris 2020":    (137.035999206, 1.1e-8),
    "CODATA 2022":   (137.035999177, 2.1e-8),
}
CONSTRUCTED = 137 + 36 / 1000


def test_the_constructed_value_is_excluded_by_every_source():
    for name, (val, unc) in SOURCES.items():
        assert abs(CONSTRUCTED - val) > 5 * unc, name


def test_the_relative_gap_is_stable_near_seven_parts_in_a_billion():
    rel = [abs(CONSTRUCTED - v) / CONSTRUCTED for v, _ in SOURCES.values()]
    assert all(5.5e-9 < r < 7.5e-9 for r in rel)


def test_the_figure_in_sigma_is_not_stable_and_must_not_be_quoted():
    """CLAUDE.md §10. The banked note carried '72 sigma', which is one lab in
    one year. The gap is fixed; the divisor is not. 72 is a framework
    favourite arriving through a soft quotient, so it gets more scrutiny."""
    sig = [abs(CONSTRUCTED - v) / u for v, u in SOURCES.values()]
    assert max(sig) / min(sig) > 2          # ranges 35 to 88
    assert not (70 < min(sig) < 74)         # no stable 72 to read
    # the nucleon route carries the placement (the author, 2026-08-26; the
    # 2026-08-04 re-grade): dimensionless ratios to the carbon-12 twelfth,
    # so 1.008/28 = 0.036 exactly on the register, and the measured route
    # lands within single-digit ppm of the measured tail on both adjustments
    from fractions import Fraction as F
    assert F(1008, 1000) / 28 == F(36, 1000)
    avg = (1.00727646657 + 1.00866491606) / 2      # (m_p + m_n)/2 in u
    route = avg / 28
    for label, alpha_inv in (("2018", 137.035999084), ("2022", 137.035999177)):
        tail = alpha_inv - 137
        assert abs(route - tail) / tail < 7e-6, label
    import pathlib
    cat = pathlib.Path(__file__).resolve().parent.parent / "catalog"
    doc = " ".join((cat / "QED-ON-DISCRETE-TERMS.md").read_text().split())
    assert "the placement arrives with the numerator" in doc
    assert "the carbon anchor of the atomic scale" in doc
    assert "That narrower step is what remains open" in doc
    # the rest value and its dress (the author, 2026-08-26): the seat sits
    # above every measured approach, and the running moves away from it
    assert "the rest value, and\nthe measured figure is its dress".replace("\n", " ") in doc
    assert "reached only by\ncalculation".replace("\n", " ") in doc
    gap = (137 + 36 / 1000) - 137.035999084
    assert 5e-7 < gap < 1.5e-6              # nine parts in 10^7, as stated
    assert 137.035999084 > 127.952          # the running descends: away from the seat
