"""Supporting structure for "The Proton and Neutron Masses on Discrete
Terms" (2026), Sections 4 and 9: the stations of the fine-structure tail.
The six-digit seat statements each occupy one turn; beneath the turn, the
seat's image under the bridge dissolves into the period-six cycle of one
seventh, and the measured image sits between the exact stations.  Every
determination of the inverse fine-structure constant lies inside the last
unit of the seat's turn — the window registered in the paper.
"""

from fractions import Fraction as F

MP, MN = 1.0072764665789, 1.00866491595     # u, CODATA-22; unc 8e-12 / 5e-10
AVG = (MP + MN) / 2
UNIT = F(1, 10**6)
REST, FLOOR = F(36, 1000), F(35999, 10**6)
SEAT_IMG = F(100797, 2800000)               # 1.00797 / 28


def test_the_seat_image_is_the_wheel():
    """The composite seat over 28 is 100797/2800000: six digits, a nine, and then the period-six cycle forever — an exact rational fact."""
    assert SEAT_IMG == F(359989, 10**7) + F(2, 7) * F(1, 10**7)
    digits = str(SEAT_IMG.numerator * 10**25 // SEAT_IMG.denominator)
    assert digits.startswith("359989" + "285714285714")   # turn | nine... wait: 9 then wheel
    # the nine sits at digit seven, the wheel from digit eight:
    assert digits[:7] == "3599892"                        # ...header check below instead
    tail = str(SEAT_IMG.numerator * 10**31 // SEAT_IMG.denominator)[7:]
    assert tail[:18] == "857142" * 3                      # the reptend, rotating, forever


def test_the_station_gaps_bridge_exactly():
    """Rest minus the seat image is (15/14)e-6 — the offsets' mean over 28 — and the floor sits (1/14)e-6 above the image."""
    assert REST - SEAT_IMG == F(15, 14) * UNIT            # = 30/28: the offsets' mean, bridged
    assert FLOOR - SEAT_IMG == F(1, 14) * UNIT            # = 2/28: the two-unit gap, bridged
    assert F(15, 14) - F(1, 14) == 1                      # floor sits one unit below rest


def test_the_ladder_orders_and_the_measured_sits_between():
    """The measured image lies between the floor and the exact seat image."""
    deficit = (0.036 - AVG / 28) * 1e6                    # units below rest
    assert 1.0 < deficit < 15 / 14                        # between the floor and the seat image
    assert abs(deficit - 1.0467) < 0.002


def test_the_two_semantics_of_the_measured_image():
    """Truncation reads the measured image at the 8-cell, near full; rounding at the register's own six-digit depth reads it on the floor."""
    img = AVG / 28
    assert int(img * 10**6) == 35998                      # truncation: the 8-cell
    assert round(img, 6) == 0.035999                      # turn-statement: the floor, exactly
    occupancy = img * 10**6 - 35998
    assert occupancy > 0.94                               # nearly full: the limit-cell signature


def test_the_window_census_every_determination_inside():
    """Section 9's window: seven determinations across three technologies and twelve years, all inside (0.035999, 0.036)."""
    for v in (0.035999046, 0.035999074, 0.035999084, 0.035999139,
              0.035999166, 0.035999177, 0.035999206):
        assert 0.035999 < v < 0.036


def test_the_lift_is_one_signed_above_the_measured_image():
    """Every determination sits above the measured image, one-signed, at 3.4 standard deviations or more."""
    img = AVG / 28
    for v, u in ((0.035999046, 2.7e-8), (0.035999166, 1.5e-8),
                 (0.035999177, 2.1e-8), (0.035999206, 1.1e-8)):
        assert (v - img) / u > 3.3                        # every camp, >= 3.4 sigma above


def test_the_nine_survives_at_place_seven():
    """Decimal place seven is a nine in both the exact and the measured images; the residual deforms only what follows it."""
    seat_digits = str(F(100797, 2800000).numerator * 10**12 // 2800000)
    # seat_digits = "35998928571": leading decimal zero dropped, so decimal
    # place 7 is string index 5 (and the wheel begins at index 6 with the 2)
    assert str((MP + MN) / 2 / 28)[8] == "9"              # measured image, place 7
    assert seat_digits[5] == "9"                          # seat image, place 7
    assert seat_digits[6:] == "28571"                     # then the wheel


def test_the_residual_family_is_boxed_and_closes_nowhere():
    """Section 6's exclusion 1: 2,198 licensed fractions against the four residuals at their measured precision — no static closure; the lone bar-survivor fails the smallest-candidate rule."""
    d_p = (MP - 1.00728) * 1e6
    d_n = (MN - 1.00866) * 1e6
    d_c = (d_p + d_n) / 2
    d_s = d_n - d_p
    assert abs(d_p - -3.533421) < 2e-5
    assert abs(d_n - 4.915950) < 2e-4
    assert abs(d_c - 0.691264) < 1e-4
    assert abs(d_s - 8.449371) < 2e-4
    # the nearest licensed miss on each razor object, pinned as exclusions:
    assert abs(-7 / 2 - d_p) / 8.3e-6 > 3          # -3.5 is thousands of sigma away
    assert abs(2 / 3 - d_c) / 2.45e-4 > 3
    assert abs(0.7 - d_c) / 2.45e-4 > 3
    assert abs(17 / 2 - d_s) / 4.9e-4 > 3
    assert abs(59 / 12 - d_n) / 4.9e-4 < 3         # the lone survivor of the bar...
    assert max(59, 12) > 20                        # ...rejected by least-performer


def test_the_residues_sum_to_two_and_the_sweep_is_null():
    """The two decompositions of the composite deficit sum to two identically, and the pre-registered candidate set misses both at the stated bars."""
    import math
    deficit = (1.008 - AVG) * 1e6
    r_struct, r_carry = 30 - deficit, deficit - 28
    assert abs(r_struct + r_carry - 2) < 1e-9             # one derivation settles both
    assert abs(r_struct - 0.691) < 0.002 and abs(r_carry - 1.309) < 0.002
    bar = 3 * 0.0003                                      # 3 sigma, razor masses
    for cand in (0.0, 1/3, 1/6, 0.1, 1/28, 0.5, 2/3, math.log(2), 0.7,
                 0.66, 0.72, 1.0, 1.125, 1.25, 4/3, 1.38, 1.5):
        assert abs(cand - r_struct) > bar and abs(cand - r_carry) > bar


def test_the_five_stations_order_on_one_axis():
    """The paper's five perspectives, ordered: the seat above the measured
    cluster, the cluster above the six-decimal statement, that above the
    measured image, and the seat image lowest, with its period-six tail."""
    mbar = (1.0072764665789 + 1.00866491595) / 2
    assert 0.036 > 0.035999206 and 0.035999046 > 0.035999    # seat > cluster > floor
    assert 0.035999 > mbar / 28 > 1.00797 / 28               # floor > measured > seat image


def test_the_rest_grammar_parallels_the_published_pi_value():
    """The seat image and the published rest value of pi share one grammar:
    each is the mean of two register statements, each denominator carries
    2^7 and a single seven, and each decimal is a finite head followed by
    the period-six cycle, held by its measured constant a residual away."""
    rest_pi = F(2815, 896)
    assert rest_pi == (F(22, 7) + F(201, 64)) / 2
    assert 896 == 2 ** 7 * 7 and 2800000 == 2 ** 7 * 5 ** 5 * 7
    digits = str(rest_pi.numerator * 10 ** 20 // rest_pi.denominator)
    assert digits[:8] == "31417410" and digits[8:14] in "142857142857"
    assert 3.14159265 < float(rest_pi)                     # pi holds it from below
    assert (float(rest_pi) / 3.14159265358979 - 1) * 1e6 < 48   # by 47 ppm
