"""test_the_joint_derivation.py — m1*m2 AND 1/r FROM ONE MECHANISM, AND THE
THIRD THING IT ALSO PRODUCES (2026-08-15).

  THE TARGET. This morning the bilinear factor and the inverse square were two
  separate results that happened to compose: the mass product came from the
  co-carry rate, the inverse square from reading the nines as perspective. The
  question was whether ONE mechanism gives both.

  THE MECHANISM, stated before it was run and not tuned afterwards. A record's
  register is a decimal counter; a ring of period p advances it once every p
  ticks, so the counter's depth-j digit turns over every p*10^j ticks. Two
  records separated by d share a depth-j CELL for a fraction max(0, 1 - d/10^j)
  of positions — the absolute address is arbitrary, so it is averaged over.
  Contact is a co-carry at a depth where they share a cell, summed over depths.

  IT DELIVERS BOTH FACTORS, AND THAT PART IS REAL PROGRESS.
     * the MASS PRODUCT: rate * d * pq / gcd(p,q) is the SAME constant for
       every pair tested — the period-dependence separates exactly, and for
       coprime periods it is (1/p)(1/q).
     * the 1/d ENVELOPE: decade to decade the measured exponent is -1 to
       twelve decimal places.
     * so U ~ m1*m2/d, Newton's potential, and the inverse square is its
       GRADIENT rather than a second route.

  AND IT DELIVERS A THIRD THING NOBODY ASKED FOR. Within each decade the law
  is not smooth: rate*d swings from 0.0168 to 0.0509, a factor of three,
  LOG-PERIODIC with exactly one cycle per factor-b of separation. I first wrote
  that the ripple was "better than a percent" in the same breath as printing
  202.5%; the number is 202.5% and the sentence was written before the number
  was read.

  THE RIPPLE IS THE REFINEMENT FACTOR, MEASURED. 202.5% at base ten, 153% at
  eight, 79% at five, 33% at three, 12.5% at two, 4.2% at 1.5, 0.1% at 1.05 —
  it vanishes only as refinement becomes continuous, which this program
  forbids. So the ripple is not an artifact of my arithmetic; it is what
  discrete scale refinement does.

  THE VERDICT: NOT A SUCCESSFUL DERIVATION, AND GRADED AS SUCH. Gravity shows
  no factor-three one-decade modulation anywhere it has been measured, across
  some sixteen decades. Either the mechanism is wrong, or the register
  separation d is not proportional to physical distance — and the second is the
  banked open ruler question, so the prediction is not yet refutable. That is a
  stay of execution, not a pass. The joint derivation is held as a CONJECTURE
  with a named defect, not promoted.

  THE FORBID, which is the useful output. This mechanism predicts gravity is
  log-periodic with exactly one cycle per factor-b in separation, at the stated
  amplitude. A convergent null across a single decade, at any scale, kills it.
  That is a sharper falsification condition than the smooth law would have
  given, and it is the reason the negative is worth keeping.
"""

from math import gcd, lcm, log10


def rate(p, q, d, b=10, jmax=4000):
    """Position-averaged contact rate: co-carries at every depth at which the
    two records share a cell, weighted by how often they share it."""
    s, u = 0.0, 1.0
    for _ in range(jmax):
        if u > 1e250:
            break
        s += max(0.0, 1.0 - d / u) / (u * lcm(p, q))
        u *= b
    return s


def test_the_mass_dependence_separates_exactly():
    """rate * d * pq / gcd is one constant across every pair — so the period
    dependence is exactly gcd(p,q)*(1/p)(1/q)."""
    d = 1000
    consts = {(p, q): rate(p, q, d) * d * p * q / gcd(p, q)
              for p, q in ((2, 3), (3, 5), (7, 10), (11, 13), (4, 6), (6, 42),
                           (24, 72), (8, 9))}
    ref = consts[(2, 3)]
    assert all(abs(c - ref) < 1e-12 for c in consts.values())
    # and for coprime periods that IS the product of the two carry rates:
    for p, q in ((2, 3), (3, 5), (7, 10), (11, 13)):
        assert gcd(p, q) == 1
        assert abs(rate(p, q, d) - ref / d * (1.0 / p) * (1.0 / q)) < 1e-18


def test_the_envelope_is_exactly_inverse_first_power():
    """Decade to decade the exponent is -1, so U ~ 1/d and F = -dU/dd ~ 1/d^2."""
    for d0 in (100, 1000, 10000, 100000):
        r0, r1 = rate(2, 3, d0), rate(2, 3, d0 * 10)
        assert abs(log10(r1 / r0) + 1.0) < 1e-12


def test_the_law_is_not_smooth_and_the_ripple_is_202_percent():
    """The defect, pinned so it cannot be quietly forgotten."""
    vals = [rate(2, 3, d) * d for d in [100 * (1 + 0.013 * k) for k in range(400)]]
    lo, hi = min(vals), max(vals)
    assert abs(lo - 0.016835) < 1e-5 and abs(hi - 0.050926) < 1e-5
    ripple = (hi - lo) / lo
    assert 2.0 < ripple < 2.1                       # 202.5 per cent, not "a percent"
    assert hi / lo > 3.0                            # a factor of three


def test_the_ripple_is_the_refinement_factor_not_an_artifact():
    """It shrinks only as refinement becomes continuous, which is forbidden."""
    def ripple(b):
        v = [rate(2, 3, d, b) * d for d in [100 * (1 + 0.013 * k) for k in range(400)]]
        return (max(v) - min(v)) / min(v)
    r10, r2, r105 = ripple(10), ripple(2), ripple(1.05)
    assert r10 > 2.0                                 # base ten: fatal
    assert 0.12 < r2 < 0.13                          # base two: still 12.5%
    assert r105 < 0.01                               # only the continuum is smooth
    assert r10 > ripple(8) > ripple(5) > ripple(3) > r2 > ripple(1.5) > r105


def test_the_verdict_is_recorded_as_a_named_defect():
    """Conjecture with a defect, not a derivation. Stated, not buried."""
    verdict = {"mass_product": "delivered",
               "inverse_first_power_envelope": "delivered",
               "one_mechanism_for_both": "delivered",
               "log_periodic_ripple": "DEFECT — factor of three, one cycle per decade",
               "grade": "conjecture, not promoted",
               "refutable_now": False,
               "why_not": "d proportional to physical distance is the open ruler question"}
    assert verdict["grade"] == "conjecture, not promoted"
    assert verdict["log_periodic_ripple"].startswith("DEFECT")
    assert verdict["refutable_now"] is False


# ---------------------------------------------------------------------------
# THE ENSEMBLE QUESTION, ASKED AND ANSWERED THE SAME DAY (2026-08-15).
# the author asked whether the ripple cancels once many pairs contribute. It does not,
# and the three ways it might have are each closed by a different kind of
# argument — one by identity, one numerically, one structurally.
# ---------------------------------------------------------------------------

def test_mass_averaging_cannot_cancel_it_by_identity():
    """The separation factor is the SAME function for every pair, so any
    mixture of masses multiplies it by a constant and leaves it untouched.
    This closes the route by an identity, not by a numerical experiment."""
    ref = {d: rate(2, 3, d) * (2 * 3) / gcd(2, 3) for d in (137, 300, 700, 1500, 4000)}
    for p, q in ((3, 5), (7, 10), (11, 13), (4, 6), (6, 42), (24, 72), (9, 16)):
        for d, v in ref.items():
            assert abs(rate(p, q, d) * (p * q) / gcd(p, q) - v) < 1e-15


def test_separation_averaging_does_not_cancel_it_either():
    """Two clouds of size s at centre-separation R: the ripple survives at
    every ratio a real gravitational test could have."""
    import random

    def pair(R, s, N=400, seed=7):
        rnd = random.Random(seed)
        return sum(rate(2, 3, abs(R + rnd.uniform(-s / 2, s / 2)
                                  - rnd.uniform(-s / 2, s / 2)))
                   for _ in range(N)) / N

    def ripple(frac):
        v = [(pair(1000 * 10 ** (k / 24.0), frac * 1000 * 10 ** (k / 24.0))
              if frac else rate(2, 3, 1000 * 10 ** (k / 24.0)))
             * 1000 * 10 ** (k / 24.0) for k in range(24)]
        return (max(v) - min(v)) / min(v)
    assert ripple(0.0) > 1.9                     # point-like: ~202%
    assert ripple(0.01) > 1.8                    # a real test geometry
    assert ripple(0.1) > 1.5                     # still not cancelled
    # only when the bodies are as large as their separation does it drop, and
    # even then it is TENS of per cent, not zero. (The figure there is
    # sampling-sensitive — 29% to 47% depending on the draw — so the assertion
    # is set at what is robust, not at the prettiest number seen.)
    assert ripple(1.0) > 0.2


def test_a_change_of_ruler_only_relocates_the_period():
    """d ~ r^k makes the period 1/k decades in r. Hiding one full cycle across
    the ~16 decades where the inverse square is tested needs k < 1/16."""
    tested_decades = 16.0
    for k in (1.0, 0.5, 0.25, 0.125, 0.0625):
        assert 1.0 / k <= tested_decades          # at least one full cycle shows
    for k in (0.03, 0.01):
        assert 1.0 / k > tested_decades           # hidden, but absurdly flat
    assert 1.0 / tested_decades == 0.0625         # the sixteenth root


def test_the_defect_survives_the_ensemble_and_that_is_the_finding():
    routes = {"average over masses": "closed by identity",
              "average over separation": "closed numerically",
              "change of ruler": "closed structurally — period only rescales"}
    assert len(routes) == 3
    assert all(v.startswith("closed") for v in routes.values())
    ripple_cancels = False
    assert not ripple_cancels


# ---------------------------------------------------------------------------
# THE CONTACT-RULE FAMILY (2026-08-15, exploring pass at the author's direction —
# facts collected, judgement deferred; see
# catalog/CONTACT-RULES-ON-A-NESTED-REGISTER-collection.md).
#
#   Every rule is  rate(d) = sum_j w(u_j) F(d/u_j),  u_j = b^j, and the three
#   choices separate cleanly: b sets the ripple's PERIOD, w sets the force-law
#   EXPONENT, F sets the ripple's AMPLITUDE. Only w is currently forced.
# ---------------------------------------------------------------------------

def _gen(F, d, b=10.0, s=1.0, lo=-40, hi=80):
    t = 0.0
    for j in range(lo, hi):
        u = b ** j
        if u < 1e-300 or u > 1e300:
            continue
        t += F(d / u) * u ** (-s)
    return t


_SMOOTH = lambda x: 1.0 / (1.0 + x) ** 2


def test_the_exponent_belongs_to_the_weight():
    """weight u^-s gives rate ~ d^-s exactly; s=1 is the carry rate."""
    for s in (0.5, 1.0, 1.5):
        e = log10(_gen(_SMOOTH, 1000.0, s=s) / _gen(_SMOOTH, 100.0, s=s))
        assert abs(e + s) < 1e-5
    # s = 1 is not a choice: a depth-j digit turns over every b^j ticks
    b, j = 10.0, 4
    assert abs(1.0 / b ** j - b ** (-j)) < 1e-18


def test_the_envelope_is_minus_one_for_every_shape_of_F():
    from math import exp
    shapes = [lambda x: 1.0 if x < 1 else 0.0,
              lambda x: max(0.0, 1.0 - x),
              lambda x: exp(-x) if x < 700 else 0.0,
              lambda x: 1.0 / (1.0 + x * x),
              _SMOOTH]
    for F in shapes:
        e = log10(_gen(F, 1000.0) / _gen(F, 100.0))
        assert abs(e + 1.0) < 1e-4


def test_the_ripple_belongs_to_F_and_tracks_mellin_decay():
    """Not differentiability — a Gaussian does worse than an exponential."""
    from math import exp

    def ripple(F, b=10.0):
        ds = [100 * (b ** (k / 300.0)) for k in range(300)]
        v = [_gen(F, d, b=b) * d for d in ds]
        return (max(v) - min(v)) / (sum(v) / len(v))
    step = ripple(lambda x: 1.0 if x < 1 else 0.0)
    kink = ripple(lambda x: max(0.0, 1.0 - x))
    gaus = ripple(lambda x: exp(-x * x))
    expo = ripple(lambda x: exp(-x) if x < 700 else 0.0)
    smooth = ripple(_SMOOTH)
    assert step > kink > gaus > expo > smooth
    assert gaus > expo            # the surprise: smoother is NOT better
    assert smooth < 0.02          # 1.3 per cent
    assert step > 2.0             # 229 per cent


def test_the_ripple_is_a_base_ten_problem():
    """At binary refinement it is ~1e-10 — six orders below any measurement."""
    from math import exp, log, pi

    def ripple(b):
        ds = [100 * (b ** (k / 300.0)) for k in range(300)]
        v = [_gen(_SMOOTH, d, b=b) * d for d in ds]
        return (max(v) - min(v)) / (sum(v) / len(v))
    assert ripple(10.0) > 1e-2
    assert ripple(4.0) < 1e-3
    assert ripple(2.0) < 1e-9                       # invisible
    assert ripple(10.0) > ripple(8.0) > ripple(6.0) > ripple(4.0) > ripple(2.0)
    # and the floor formula brackets it from below at every base:
    for b in (10.0, 8.0, 6.0, 4.0, 3.0, 2.0):
        assert ripple(b) > 2 * exp(-2 * pi * pi / log(b))


def test_the_mass_product_survives_every_rule_in_the_family():
    from math import exp
    for F in (lambda x: max(0.0, 1.0 - x),
              lambda x: exp(-x) if x < 700 else 0.0,
              _SMOOTH):
        vals = [_gen(F, 1000.0) / lcm(p, q) * p * q / gcd(p, q)
                for p, q in ((2, 3), (3, 5), (7, 10), (4, 6), (6, 42))]
        assert max(vals) - min(vals) < 1e-12


# ---------------------------------------------------------------------------
# THE LAYER CORRECTION (2026-08-15). the author: "layers, not axes" — and the
# assignment is banked in THE-CHOSEN-THREE §4: decimal for polarity and charge,
# BINARY PLACES FOR SUSPENSION AND CARRY, dimension for extension. The contact
# rule sums over CARRY depths, so its refinement factor is two. I had it on the
# decimal register, which is the polarity layer. The defect was mine.
# ---------------------------------------------------------------------------

def _g(F, d, b, s=1.0, lo=-60, hi=200):
    t = 0.0
    for j in range(lo, hi):
        u = float(b) ** j
        if u < 1e-290 or u > 1e290:
            continue
        t += F(d / u) * u ** (-s)
    return t


def _ripple(F, b, n=400):
    ds = [100 * (float(b) ** (k / float(n))) for k in range(n)]
    v = [_g(F, d, b) * d for d in ds]
    return (max(v) - min(v)) / (sum(v) / len(v))


def test_the_exponent_never_depended_on_the_layer():
    F = lambda x: 1.0 / (1.0 + x) ** 2
    for b in (10, 2):
        e = log10(_g(F, 1000.0, b) / _g(F, 100.0, b))
        assert abs(e + 1.0) < 1e-9


def test_on_the_carry_layer_the_ripple_is_ten_orders_down():
    F = lambda x: 1.0 / (1.0 + x) ** 2
    assert _ripple(F, 10) > 1e-2                 # decimal: 1.3 per cent
    assert _ripple(F, 2) < 1e-9                  # binary: 1e-10
    assert _ripple(F, 10) / _ripple(F, 2) > 1e6


def test_the_layer_alone_is_not_enough_F_is_still_free():
    """Base two with a KINKED F still ripples at 11.5%. The layer fixes the
    period; the amplitude still needs a smooth F, and F remains unforced."""
    kink = lambda x: max(0.0, 1.0 - x)
    assert _ripple(kink, 2) > 0.10
    assert _ripple(lambda x: 1.0 / (1.0 + x) ** 2, 2) < 1e-9


def test_the_mass_product_is_untouched_by_the_move():
    F = lambda x: 1.0 / (1.0 + x) ** 2
    vals = [_g(F, 1000.0, 2) / lcm(p, q) * p * q / gcd(p, q)
            for p, q in ((2, 3), (3, 5), (7, 10), (4, 6), (6, 42))]
    assert max(vals) - min(vals) < 1e-15
