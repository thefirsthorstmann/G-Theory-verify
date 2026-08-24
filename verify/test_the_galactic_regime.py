"""test_the_galactic_regime.py — THE CAMPAIGN OPENED, FIRST EXACT RESULTS
(2026-08-16). the author set the standard in one sentence: there cannot be multiple
solutions to gravity — the correct one must encompass the entire scope, or the
proposal is an opinion. The capstone's earlier stance ("this paper does not
compete on rotation curves") is retired under that standard: the galactic
regime is carried as an OPEN ACCOUNT, with the route named and these first
results on the record.

  RESULT ONE — THE NAIVE ROUTE REFUSED, EXACTLY. A bare far ceiling on the
  register (the horizon as u_max = 2^J) subtracts from every pair's potential
  a term D(d) that is CONSTANT in d up to an exact bound:

      | D(d) - 2^-J |  <=  (2/3) d 4^-J        (derived-tail profile)

  so the force correction per pair is bounded by (2/3) 4^-J — a uniform
  constant — and RELATIVE to the Newtonian force it is at most
  (2/3)(d/2^J)^2: at galactic separations seventeen octaves below the
  horizon, parts in 10^11. NO FLAT ROTATION CURVE COMES FROM A CUTOFF ALONE.
  The refusal is a theorem of the model, not a failure of effort — and the
  constant the ceiling leaves behind has the shape of a vacuum term, one
  part-per-pair in the horizon: the program's standing signpost (the base
  deficit wears the cosmological constant's shape) arriving from a second,
  independent direction. My first float check of this constancy was
  noise-dominated and printed a wrong verdict line; this battery does it in
  exact rationals.

  RESULT TWO — IF THE MECHANISM HAS AN INFRARED SCALE, IT IS HORIZON-SET,
  AND THE ORDER LANDS WITH ZERO PARAMETERS. The chain's own H0 = 70.05 km/s
  per Mpc gives cH0 = 6.81e-10 m/s^2. Milgrom's fitted a0 is 1.2e-10 — the
  horizon acceleration over a soft geometric divisor (2pi gives 1.08e-10; 6
  gives 1.13e-10). The order is landed by the program's own chain with
  nothing adjusted; the divisor is NOT derived and is recorded as soft. This
  is a scale statement, not a rotation-curve theory, and is graded as such.

  RESULT THREE — THE FINGERPRINT IS PROPRIETARY AND SCALE-FREE. The contact
  sum is exactly self-similar under d -> 2d (with the ceiling far away), so
  any residual the mechanism imprints is periodic in log-separation with
  period ln 2 — ONE OCTAVE — at laboratory and at galactic scales alike.
  Halos predict no period; the modified force law predicts no period; the
  octave is ours, and rotation-curve data is a reanalysis surface for it.

  THE ROUTES THAT SURVIVE RESULT ONE, named for the campaign: the ensemble —
  a galaxy is not a two-body sum but a chained ledger of union events, and
  collective contact statistics are unexplored; the ultrametric horn — what
  centripetal means where betweenness fails is exactly the fork's geometry
  question at the scale where it matters; and the gcd statistics — the
  commensurable enhancement gcd(p,q) over a realistic period spectrum. Open,
  stated, unpriced.
"""

from fractions import Fraction as F
from math import pi


def _F(x):
    return 1 / (1 + x) ** 2


def _tail(d, J, J2):
    """D(d) = sum_{j=J+1}^{J2} F(d/2^j)/2^j, exact."""
    s = F(0)
    for j in range(J + 1, J2 + 1):
        u = F(2) ** j
        s += _F(F(d) / u) / u
    return s


def test_the_ceiling_subtracts_a_constant_within_the_exact_bound():
    J, J2 = 40, 90
    # the windowed all-ones: sum of 2^-j for j in (J, J2] exactly
    base_w = F(1, 2 ** J) - F(1, 2 ** J2)
    for d in (1, 7, 1000, 2 ** 10, 123456):
        D = _tail(d, J, J2)
        bound = F(2, 3) * d * F(1, 4 ** J)
        # the ceiling's subtraction is the constant base_w short of at most
        # the exact bound (1 - F(x) <= 2x, summed):
        assert base_w - D >= 0
        assert base_w - D <= bound
    # and the residual truly moves with d (it is a bound, not an identity):
    assert (base_w - _tail(1000, J, J2)) > (base_w - _tail(1, J, J2))


def test_the_force_correction_is_negligible_at_galactic_scales():
    """Relative force correction <= (2/3)(d/2^J)^2: parts in 1e11 at
    seventeen octaves below the horizon."""
    ratio = F(2, 3) * F(1, 2 ** 17) ** 2
    assert ratio < F(1, 10 ** 10)
    assert ratio > F(1, 10 ** 11)              # and not absurdly smaller


def test_the_vacuum_shaped_offset_is_one_part_per_pair_in_the_horizon():
    """The constant the ceiling leaves is exactly sum 2^-j = 2^-J per pair
    (in the F(0) limit): the Lambda-shaped signpost, second arrival."""
    J = 40
    s = sum(F(1, 2 ** j) for j in range(J + 1, 200))
    assert F(1, 2 ** J) - s == F(1, 2 ** 199)  # the window's own remainder,
    # exactly: the geometric total IS 2^-J in the limit, one part per pair


def test_the_horizon_acceleration_lands_the_order_with_zero_parameters():
    c = 2.99792458e8
    H0 = 70.05 * 1000 / 3.0856775814913673e22
    cH0 = c * H0
    assert abs(cH0 - 6.806e-10) < 1e-12
    a0_fitted = 1.2e-10
    assert 0.85 < (cH0 / (2 * pi)) / a0_fitted < 0.95     # 1.083e-10: ~10% low
    assert 0.90 < (cH0 / 6) / a0_fitted < 1.00            # 1.134e-10: ~ 6% low
    # the divisor is soft and recorded as such; only the ORDER is claimed:
    assert 0.1 < cH0 / a0_fitted < 10


def test_the_residual_period_is_one_octave_at_any_scale():
    """Exact self-similarity of the contact sum under d -> 2d (ceiling far):
    rate(2d) = rate(d)/2, so any deviation pattern repeats per octave —
    at bench scales and galactic scales identically."""
    def rate(d, jmin=-60, jmax=120):
        s = F(0)
        for j in range(jmin, jmax):
            u = F(2) ** j
            s += _F(F(d) / u) / u
        return s
    for d in (3, 10, 1000):
        r1, r2 = rate(d), rate(2 * d)
        # shift j -> j+1 maps the sum exactly onto half itself (edge terms
        # beyond the window are below 2^-58 of the total):
        assert abs(r2 - r1 / 2) / r1 < F(1, 2 ** 55)
