"""test_watch_condition.py — THE IDEAL NUMBER IN CLOSED FORM, AND THE WATCH
CONDITION MADE A STANDING OBJECT (2026-08-12). Tool: internal tools/watch.py.

  the author ASKED FOR THE IDEAL NUMBER EVEN IF IT IS NOT REAL, AND IT HAS A CLOSED
  FORM. The cell at eight sevenths of a femtometre fixes the saturation
  density at three times seven cubed over two to the eleventh times pi —
  0.1599321 per cubic femtometre. Every factor is named and none is spare:
  the three from the sphere's volume, the seven cubed from the cell's
  denominator cubed, the two to the eleventh from four times the cell's
  numerator cubed. And in the rest-pi register it goes EXACTLY RATIONAL,
  three times seven to the fourth over forty-five thousand and forty, since
  rest-pi's own denominator is two to the seventh times seven and the sevens
  cancel into the numerator.

  AND THE IDEAL SITS FOUR HUNDREDTHS OF A PERCENT FROM THE ROUND SIXTEEN
  HUNDREDTHS, which is why this is a live claim and not a curiosity: the
  conventional value nuclear physics has quoted for decades and the value
  this framework forces agree to four parts in ten thousand.

  THE WATCH CONDITION, POSED SO SOMEONE ELSE'S PAPER DECIDES IT. Chiral
  effective field theory computes infinite symmetric matter directly and is
  systematically improvable, so its central value and its bar both move as
  the order rises. Today it stands at 0.164 with a bar of 0.007 — two and a
  half percent above the ideal and only six tenths of a sigma away, because
  the bar is four and a half percent and cannot yet discriminate. Hold the
  centre fixed and tighten: at a bar of 0.002 it is two sigma, at 0.0016 two
  and a half, at 0.0013 THREE and the claim is dead.

  SO THE SENTENCE TO WATCH FOR IS "we obtain n0 = 0.164 +/- 0.0013". A bar of
  eight tenths of a percent at the present centre ends this, and eight tenths
  is inside what the next chiral order is aiming at. The claim is therefore
  at risk from a calculation nobody in this programme controls, on a
  timescale nobody here sets — which is the condition a prediction is
  supposed to be in.

  THE OTHER SIDE OF THE WATCH. The expansion rate decides it too and is
  already sharper against one camp: the microwave value sits five sigma from
  the ideal and the ladder value two and nine tenths. Both cannot be right;
  whichever survives the tension's resolution is the one that matters, and
  the standing prediction is that neither does — that it resolves near
  seventy.
"""

import math
from fractions import Fraction as F

C, MPC, I_SEATS, DEPTH = 2.99792458e8, 3.0856775814913673e22, 4.327363498, 1e42
CELL = F(8, 7)
REST_PI = F(2815, 896)


def _h0(cell):
    return 2 * C * I_SEATS / (DEPTH * float(cell) * 1e-15) * MPC / 1000


def test_the_ideal_density_has_a_closed_form_with_nothing_spare():
    """Three from the sphere, seven cubed from the cell's denominator, two to
    the eleventh from four times its numerator cubed."""
    n0 = 3 * 7 ** 3 / (2 ** 11 * math.pi)
    assert abs(n0 - 3 / (4 * math.pi * float(CELL) ** 3)) < 1e-15
    assert abs(n0 - 0.1599321) < 1e-7
    assert 2 ** 11 == 4 * 8 ** 3                        # the four-pi and 8 cubed
    assert 7 ** 3 == CELL.denominator ** 3
    assert 3 * 7 ** 3 == 1029 and 2 ** 11 == 2048


def test_in_the_rest_pi_register_the_ideal_is_exactly_rational():
    """Rest-pi's denominator is two to the seventh times seven, so the sevens
    cancel upward and the density becomes a rational number."""
    n_rest = 3 / (4 * REST_PI * CELL ** 3)
    assert isinstance(n_rest, F)                        # exactly rational
    assert n_rest == F(3 * 7 ** 4, 45040)
    assert 3 * 7 ** 4 == 7203
    assert 45040 == 2 ** 4 * 5 * 563                    # 563 inherited from rest-pi
    assert REST_PI.denominator == 896 == 2 ** 7 * 7
    n_true = 3 * 7 ** 3 / (2 ** 11 * math.pi)
    assert abs((float(n_rest) / n_true - 1) * 1e6 + 47.2) < 0.5   # -47 ppm


def test_the_ideal_sits_four_hundredths_of_a_percent_from_the_round_value():
    """Why this is a live claim: the conventional quoted density and the
    forced one agree to four parts in ten thousand."""
    n0 = 3 * 7 ** 3 / (2 ** 11 * math.pi)
    assert abs(n0 - 0.16) / 0.16 < 5e-4
    assert 0.0004 < abs(n0 - 0.16) / 0.16 < 0.00045
    assert abs(_h0(CELL) - 70.05) < 0.01


def test_the_kill_threshold_is_eight_tenths_of_a_percent():
    """Hold the chiral centre fixed and tighten the bar. Three sigma arrives
    at a bar of about 0.0013, which is 0.8 percent."""
    n0 = 3 * 7 ** 3 / (2 ** 11 * math.pi)
    centre = 0.164
    assert abs(centre - n0) / 0.007 < 1.0               # today: cannot discriminate
    for bar, floor in ((0.005, 0.7), (0.003, 1.3), (0.002, 1.9), (0.0016, 2.4)):
        assert abs(centre - n0) / bar > floor
    kill = abs(centre - n0) / 3
    assert 0.00130 < kill < 0.00140                     # the bar that ends it
    assert 0.008 < kill / n0 < 0.009                    # eight tenths of a percent
    assert abs(centre - n0) / kill >= 3.0


def test_the_expansion_side_of_the_watch_is_already_sharper_against_one_camp():
    """Both camps are compared to the same ideal; they cannot both be right,
    and the standing prediction is that neither is."""
    ideal = _h0(CELL)
    planck, sh0es = abs(ideal - 67.36) / 0.54, abs(ideal - 73.04) / 1.04
    assert planck > 4.5                                 # five sigma
    assert 2.5 < sh0es < 3.2                            # two and nine tenths
    assert planck > sh0es                               # microwave side is sharper
    # and the nuclear range brackets the ideal while excluding both camps.
    # NB denser matter means a SMALLER cell and so a HIGHER rate:
    lo = _h0((3 / (4 * math.pi * 0.150)) ** (1 / 3))     # sparsest -> slowest
    hi = _h0((3 / (4 * math.pi * 0.170)) ** (1 / 3))     # densest  -> fastest
    assert abs(lo - 68.57) < 0.05 and abs(hi - 71.49) < 0.05
    assert hi > ideal > lo
    assert lo > 67.36 and hi < 73.04
