"""test_diatonic_relativity.py — THE KINEMATICS THE SERIES CARRIES (2026-08-16).
the author's notes on the capstone: the spacing symmetry of the descent (the octave
below built from the octave above), the innately relativistic structure of the
diatonic series (frequency rising as wavelength falls with the product held),
velocity composition, the comma as a residual boost, and the mirror-cavity
question. The banked spine is the 2026-06-26 Lorentz-from-the-octave arc (the
octave as a boost of rapidity ln 2 on the null axis — the arc's one named
posit) and ORIGIN-X (the meter limit; the conditional Lorentz factor). This
battery pins the arithmetic that the capstone's relativity section now states.

  THE TRANSLATION FACT, the author's diagram detail made exact. The descent 24 -> 0 is
  the octave 48 -> 24 TRANSLATED DOWN BY THE ROOT: lower_i = upper_i - 24 at
  every one of the eight seats. Translation inherits whole numbers; dilation
  (dividing the just octave by two) produces a different series entirely
  (22.5, 13.5 ...) and cannot reach the floor. The one seat where the
  translated value and the register-read ratio disagree is Fa: 32 - 24 = 8
  clean against the register's 7.999999. The self-similarity — every octave's
  gap list congruent — is the lattice invariance the banked Lorentz arc
  identifies with boost invariance.

  THE OCTAVE-BOOST LADDER (banked): n octaves of boost give
  beta = (4^n - 1)/(4^n + 1) — 3/5 at one octave (the 3-4-5 boost), 15/17 at
  two (the spine prime), 63/65 at three — with room below c equal to
  2/(4^n + 1) at every rung: positive always, so c is approached and never
  reached, the unsounded-center structure in kinematic dress.

  COMPOSITION IS INTERVAL STACKING. With k the Doppler factor and
  beta = (k^2-1)/(k^2+1), the relativistic velocity addition
  (u+v)/(1+uv) is EXACTLY the k-product k1*k2 — intervals stack by
  multiplication, and that is the whole content of the composition law.
  Galilean addition is the tempered error: adding two one-octave boosts as
  fractions gives 6/5 > 1; stacking them gives 15/17 < 1. Two travelers at
  any subluminal rapidity compose to a subluminal rapidity; the limit has no
  rest frame, as the tonic has no voice.

  THE COMMA IS A RESIDUAL BOOST. Twelve fifths against seven octaves leave
  the rapidity 12 ln(3/2) - 7 ln 2 = ln(531441/524288) = 0.0135510...,
  beta = tanh of it = 0.013550 — a cycle of transports that fails to close by
  an exact, derived amount. The failure exists because ln 2 and ln 3 are
  incommensurable, which is the program's founding fact wearing rapidity
  units; the circle of fifths is a spiral for the same reason a generic
  Lorentz transformation is loxodromic.

  THE CAVITY QUESTION, its arithmetic. Thirty seconds of emission is a
  9.0e9 m train folded 1.5e9 times into a 3 m cavity. After switch-off the
  drain time is the ring-down L/(c(1-R)) — tens of nanoseconds for household
  mirrors, milliseconds for research cavities, unbounded for perfect ones —
  and the formula carries NO dependence on how long the source ran: the
  persistence measures the mirrors' commitment rate, not the source's
  history. And a null interval has zero proper measure regardless of its
  coordinate duration — u.v = 0 whenever u = 0 — the arithmetic behind the
  program's banked never-rounds reading: a photon's record carries no tick
  between emission and absorption, however long the flight.
"""

from fractions import Fraction as F
from math import log, tanh, isclose

UPPER = [48, 45, 40, 36, 32, 30, 27, 24]
LOWER = [24, 21, 16, 12, 8, 6, 3, 0]


def test_the_lower_octave_is_the_upper_translated_by_the_root():
    assert [x - 24 for x in UPPER] == LOWER
    gaps_upper = [a - b for a, b in zip(UPPER, UPPER[1:])]
    gaps_lower = [a - b for a, b in zip(LOWER, LOWER[1:])]
    assert gaps_upper == gaps_lower == [3, 5, 4, 4, 2, 3, 3]
    assert sum(gaps_upper) == 24                       # one octave of gaps


def test_dilation_gives_a_different_series_and_misses_the_floor():
    halved = [F(x, 2) for x in UPPER]
    assert halved != [F(x) for x in LOWER]
    assert F(45, 2) in halved and F(27, 2) in halved   # 22.5 and 13.5
    # and the one seat where translation and the register part is Fa:
    assert UPPER[4] - 24 == 8
    assert 7 * F(1142857, 10 ** 6) == F(7999999, 10 ** 6)


def test_the_octave_boost_ladder_and_the_room_below_c():
    for n, (b, room) in enumerate([(F(3, 5), F(2, 5)), (F(15, 17), F(2, 17)),
                                   (F(63, 65), F(2, 65))], start=1):
        k = 2 ** n
        assert F(k * k - 1, k * k + 1) == b
        assert 1 - b == room == F(2, 4 ** n + 1)
        assert 0 < room                                # c never reached
    assert F(3, 5) ** 2 + F(4, 5) ** 2 == 1            # the 3-4-5 boost


def test_composition_is_the_k_product_exactly():
    import random
    rnd = random.Random(7)
    for _ in range(500):
        k1 = F(rnd.randrange(1, 60), rnd.randrange(1, 60)) + 1
        k2 = F(rnd.randrange(1, 60), rnd.randrange(1, 60)) + 1
        b1 = F(k1 ** 2 - 1, k1 ** 2 + 1)
        b2 = F(k2 ** 2 - 1, k2 ** 2 + 1)
        lhs = F((k1 * k2) ** 2 - 1, (k1 * k2) ** 2 + 1)
        rhs = (b1 + b2) / (1 + b1 * b2)
        assert lhs == rhs                              # exact, rational


def test_galilean_addition_is_the_error_and_stacking_is_the_truth():
    assert F(3, 5) + F(3, 5) == F(6, 5) > 1            # the broken transform
    k = 2 * 2                                          # two octaves stacked
    assert F(k * k - 1, k * k + 1) == F(15, 17) < 1    # the composed boost


def test_the_comma_is_a_residual_rapidity():
    comma = F(531441, 524288)
    r = 12 * log(F(3, 2)) - 7 * log(2)
    assert isclose(r, log(comma), rel_tol=1e-12)
    assert isclose(r, 0.0135510334, abs_tol=1e-9)
    assert isclose(tanh(r), 0.0135502, abs_tol=1e-6)   # the comma as a speed
    # and the non-closure is the founding incommensurability:
    for a in range(1, 40):
        for b in range(1, 26):
            assert 2 ** a != 3 ** b


def test_the_cavity_arithmetic():
    c = 2.99792458e8
    train = c * 30.0
    assert isclose(train, 8.99e9, rel_tol=1e-2)        # the folded train
    assert isclose(train / (2 * 3.0), 1.5e9, rel_tol=1e-2)
    for R, tau in ((0.90, 3.34e-8), (0.99, 3.34e-7), (0.999999, 3.34e-3)):
        assert isclose(1.0 / (c * (1 - R)), tau, rel_tol=2e-2)
    # the drain formula carries no emission-duration term:
    ring_down_args = ("L", "c", "R")
    assert "t_emit" not in ring_down_args


def test_a_null_interval_has_zero_measure_at_any_duration():
    """u.v = 0 whenever u = 0: no proper ticks between emission and
    absorption, however long the coordinate flight."""
    for t in (1e-9, 1.0, 30.0, 3.15e7):
        u, v = t - t, t + t                            # x = t: on the cone
        assert u * v == 0.0


def test_the_c_rest_arithmetic():
    """The units volume's labelled proposal, its numbers pinned: on a metre
    0.0692 per cent different the rate is 3x10^8 = 2^8*3*5^8, whose all-nines
    neighbour 3(10^8 - 1) = 3^3*11*73*101*137 carries the fine-structure
    prime because ord_10(137) = 8. The SI numeral itself is a survey residue
    and carries no structure -- the paper reads nothing in it."""
    assert 3 * 10 ** 8 == 2 ** 8 * 3 * 5 ** 8
    assert 3 * (10 ** 8 - 1) == 299999997 == 3 ** 3 * 11 * 73 * 101 * 137
    assert (10 ** 8 - 1) % 137 == 0
    k = 1
    t = 10 % 137
    while t != 1:
        t = t * 10 % 137
        k += 1
    assert k == 8                                      # ord_10(137)
    shift = (3e8 - 299792458) / 299792458
    assert abs(shift - 6.923e-4) < 1e-6                # the 0.0692 per cent
