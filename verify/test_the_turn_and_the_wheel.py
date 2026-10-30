"""THE TURN AND THE WHEEL — CC's floor, the overblow, and the seat image that
dissolves into the reptend (2026-08-31, the drops campaign's first sitting).

THE OBJECTS.  On the tail axis, in units of 1e-6 below rest .036:

    rest             0
    the floor        1          (.035999 -- the prefix every determination shares)
    measured image   1.0467     ((m_p+m_n)/2 / 28, CODATA-22, razor)
    the seat image   15/14      (1.00797/28 -- the banked seat, bridged; EXACT)
    the war          0.794 - 0.954   (Berkeley, g-2, CODATA, Paris: all inside)

THE WHEEL (CC's noticing, verified exact):  1.00797/28 = 100797/2800000 =

    .035998 | 9 | 285714 285714 285714 ...
     [turn]  [nine]  [the reptend, forever]

  = .0359989 + (2/7) x 1e-7 exactly.  Past the turn the seat's value is not
  more digits of the object -- it is the sevenths wheel turning.  And the two
  station gaps are the banked mass objects, bridged: rest - seat_image =
  3/2800000 = (15/14) x 1e-6 = the offsets' mean -3, divided by 28; the
  floor - seat_image = (1/14) x 1e-6 = the fork's 2-unit mass gap, divided by
  28.  The 30-vs-28 fork IS the 1/14.

SEMANTICS, held apart and then unified.  Truncation reads the measured image at
.035998 (digit 8, occupancy 0.953: the limit-cell, nearly full).  The
turn-statement (rounding at the register's own one-turn depth, ledger Sec.6)
reads it .035999 -- dead on the floor, CC's "exact ... perfect".  The banked
unification is the seat-held-from-below pattern (7.99999...; the FSC paper's
"the run of nines IS the borrow in flight"): one object, two shadows.

GRADES.  Every identity below: exact, forced arithmetic.  The reading -- a
decimal value is a turn-statement riding the wheel, and instruments probing
past the turn read wheel-plus-drive rather than object (the overblow, CC's
flute) -- is a CONJECTURE with named teeth: the alpha war resolving floor-ward
(Berkeley-ward) is its confirmation direction; reconciliation at the Paris-side
centers strands it; any determination landing outside (.035999, .036) kills
the window census.  The g-2 route is the stated wrinkle: no recoil to overblow,
yet it sits mid-pack; its drive would have to be the depth of the QED series
itself.  THE SWEEP: the pre-registered candidate set (commas, halves, banked
stations placed) misses both razor residues 0.691 / 1.309 -- nearest is ln 2 at
6 sigma, EXCLUDED -- so the residues stay underived and the ledger's crown
stays open, said plainly.
"""

from fractions import Fraction as F

MP, MN = 1.0072764665789, 1.00866491606     # u, CODATA-22; unc 8e-12 / 4e-10
AVG = (MP + MN) / 2
UNIT = F(1, 10**6)
REST, FLOOR = F(36, 1000), F(35999, 10**6)
SEAT_IMG = F(100797, 2800000)               # 1.00797 / 28


def test_the_seat_image_is_the_wheel():
    assert SEAT_IMG == F(359989, 10**7) + F(2, 7) * F(1, 10**7)
    digits = str(SEAT_IMG.numerator * 10**25 // SEAT_IMG.denominator)
    assert digits.startswith("359989" + "285714285714")   # turn | nine... wait: 9 then wheel
    # the nine sits at digit seven, the wheel from digit eight:
    assert digits[:7] == "3599892"                        # ...header check below instead
    tail = str(SEAT_IMG.numerator * 10**31 // SEAT_IMG.denominator)[7:]
    assert tail[:18] == "857142" * 3                      # the reptend, rotating, forever


def test_the_gaps_are_the_banked_objects_bridged():
    assert REST - SEAT_IMG == F(15, 14) * UNIT            # = 30/28: the -3, bridged
    assert FLOOR - SEAT_IMG == F(1, 14) * UNIT            # = 2/28: the fork, bridged
    assert F(15, 14) - F(1, 14) == 1                      # floor sits one unit below rest


def test_the_ladder_orders_and_the_measured_sits_between():
    deficit = (0.036 - AVG / 28) * 1e6                    # units below rest
    assert 1.0 < deficit < 15 / 14                        # between the floor and the seat image
    assert abs(deficit - 1.0467) < 0.002


def test_the_two_semantics_of_the_measured_image():
    img = AVG / 28
    assert int(img * 10**6) == 35998                      # truncation: the 8-cell
    assert round(img, 6) == 0.035999                      # turn-statement: the floor, exactly
    occupancy = img * 10**6 - 35998
    assert occupancy > 0.94                               # nearly full: the limit-cell signature


def test_the_war_census_every_determination_inside_the_last_unit():
    for v in (0.035999046, 0.035999074, 0.035999084, 0.035999139,
              0.035999166, 0.035999177, 0.035999206):
        assert 0.035999 < v < 0.036


def test_the_overblow_is_one_signed_above_the_measured_image():
    img = AVG / 28
    for v, u in ((0.035999046, 2.7e-8), (0.035999166, 1.5e-8),
                 (0.035999177, 2.1e-8), (0.035999206, 1.1e-8)):
        assert (v - img) / u > 3.3                        # every camp, >= 3.4 sigma above


def test_the_seal_survives_in_the_measured_image():
    """Digit seven is the triad's 9 in BOTH images: turn | seal | sub-turn content.
    The seat's content past the seal is pure hexad (the wheel); the measured
    value keeps the seal and deforms only what follows it."""
    seat_digits = str(F(100797, 2800000).numerator * 10**12 // 2800000)
    # seat_digits = "35998928571": leading decimal zero dropped, so decimal
    # place 7 is string index 5 (and the wheel begins at index 6 with the 2)
    assert str((MP + MN) / 2 / 28)[8] == "9"              # measured image, place 7
    assert seat_digits[5] == "9"                          # seat image, place 7
    assert seat_digits[6:] == "28571"                     # then the wheel


def test_the_dress_family_is_razor_boxed_and_closes_nowhere():
    """The 2026-08-31 sweep, pinned so it is not re-run by hand: 2,198 licensed
    candidates (the 2-perp-3-perp-7 currencies k/q for q in the web, the commas,
    the banked stations at two place-shifts) against the four dress values at
    their CODATA-22 razor bars.  Result: NULL -- no candidate within 3 sigma of
    proton, composite, or split; the single 3-sigma item on the neutron (59/12,
    +1.5 sigma) is reported and unexplained — no licensed structure carries it,
    and no threshold rule is invoked (the 2026-09-01 board retired the >20
    performer cutoff as inconsistent: 23/32 itself carries 32).  The dress is NOT
    a static station of the web.  Under the turn-and-wheel reading this is the
    expected sign: the wheel is the seat's circulation, and the dress is
    development -- the dynamical residue the ledger's crown demands derived, not
    matched.  The proton's -3.533421(8) is the sharpest underived number in the
    program and the crown's named numerical target."""
    d_p = (MP - 1.00728) * 1e6
    d_n = (MN - 1.00866) * 1e6
    d_c = (d_p + d_n) / 2
    d_s = d_n - d_p
    assert abs(d_p - -3.533421) < 2e-5
    assert abs(d_n - 4.916060) < 1e-4
    assert abs(d_c - 0.691320) < 1e-4
    assert abs(d_s - 8.449481) < 2e-4
    # the nearest licensed miss on each razor object, pinned as exclusions:
    assert abs(-7 / 2 - d_p) / 8.3e-6 > 3          # -3.5 is thousands of sigma away
    assert abs(2 / 3 - d_c) / 2.45e-4 > 3
    assert abs(0.7 - d_c) / 2.45e-4 > 3
    assert abs(17 / 2 - d_s) / 4.9e-4 > 3
    assert abs(59 / 12 - d_n) / 4.0e-4 < 3         # the lone 3-sigma item: reported,
    # unexplained, carried by no structure — no threshold rule is applied


def test_the_residues_sum_to_two_and_the_sweep_is_null():
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
    mbar = (MP + MN) / 2
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
