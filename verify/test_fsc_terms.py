"""The Fine-Structure Constant on Discrete Terms: every exhibit of the paper, pinned (fsc_terms.py).

Sections 2 to 7 of the paper, in its order. The exact layer is integer and rational arithmetic.
The comparison layer takes the measured central values as their sources print them and compares
in exact rational arithmetic, so that a figure such as "6.0 parts per billion" is the rounding of
a number this file states and not a number typed in.
"""

from fractions import Fraction

from fsc_terms import (spellings, ord10, period_primes, reptend, midy_halves, family_affair, two_forms,
                       borrow_signature, spelling_census, octave_primes_below, alpha_inv, gap_ppb, gap_in_sigma,
                       nucleon_mean, nucleon_relation_ppm, tail, wyler, ALPHA_INV, DETERMINATIONS, MEASURED,
                       M_P, M_N, M_P_U, M_N_U, REST)


# --- sections 2 and 3: the spellings and the ring ----------------------------------------------

def test_three_spellings():
    a, b, c = spellings()
    assert a == 137 and b == 137 and c == 17


def test_ring_theorem():
    # ord_137(10) = 8, hence 17 families: the closure equation is 8*17 + 1
    assert ord10(137) == 8
    assert (137 - 1) // ord10(137) == 17


def test_octave_scarcity():
    # the primes of period eight, among all primes: exactly {73, 137}
    assert period_primes(8) == [73, 137]
    assert 73 * 137 == 10001
    # the class of the sevenths for comparison: period six = {7, 13}
    assert period_primes(6) == [7, 13]
    # and seven has the full period, in one family
    assert ord10(7) == 6 and (7 - 1) // ord10(7) == 1


def test_the_census_of_the_short_periods():
    """Period one {3}, two {11}, three {37}, four {101}, five {41, 271}, six {7, 13},
    seven {239, 4649}, eight {73, 137}: as the paper prints it."""
    assert [period_primes(k) for k in range(1, 9)] == [
        [3], [11], [37], [101], [41, 271], [7, 13], [239, 4649], [73, 137]]
    # six and eight are the neighbouring EVEN periods; seven lies between them
    assert period_primes(7) != []


# --- section 4: the backbone -------------------------------------------------------------------

def test_backbone_midy():
    b = reptend(137)
    assert b == "00729927"
    a, z, s = midy_halves(b)
    assert (a, z, s) == (72, 9927, 9999)
    # all four digit-pairs across the split sum to nine
    assert all(int(x) + int(y) == 9 for x, y in zip(b[:4], b[4:]))
    # read in twos, 00|72|99|27, with 72 + 27 = 99
    assert b[2:4] == "72" and b[4:6] == "99" and b[6:8] == "27"
    assert 72 + 27 == 99
    # the sevenths obey the same law at period six
    assert midy_halves(reptend(7)) == (142, 857, 999)
    # the centre of the law: complements reflect through half the all-nines, which is the
    # all-nines one octave down
    assert (142 + 857) / 2 == 499.5 == 999 / 2
    assert (72 + 9927) / 2 == 4999.5 == 9999 / 2


def test_backbone_family():
    # every fraction over 137 carries the four-nines complement: all 136, as the paper says
    for k in range(1, 137):
        block = str(10**8 * k // 137).zfill(8)
        assert midy_halves(block)[2] == 9999
    assert str(10**8 * 2 // 137).zfill(8) == "01459854" and 145 + 9854 == 9999
    assert str(10**8 * 3 // 137).zfill(8) == "02189781" and 218 + 9781 == 9999


# --- section 5: the censuses -------------------------------------------------------------------

def test_the_censuses():
    assert spelling_census() == [113, 131, 137, 145, 155]   # 5 of 101
    p8, nprimes = octave_primes_below(150)
    assert p8 == [73, 137] and nprimes == 35                # 2 of 35


def test_the_grid_step():
    """The third row of the table: the measured tail lies within one step of the millesimal
    grid, from below, at 0.8 millionths on the CODATA 2022 value (0.9 on that of 2018)."""
    below = Fraction(36, 1000) - tail("CODATA 2022")
    assert below == Fraction(823, 10**9) and round(float(below) * 10**6, 1) == 0.8
    assert round(float(Fraction(36, 1000) - tail("CODATA 2018")) * 10**6, 1) == 0.9
    assert Fraction(1, 2000) < below / Fraction(1, 1000) < Fraction(1, 1000)      # about 1 in 1000 of a step


# --- section 6: the tail -----------------------------------------------------------------------

def test_the_numerator_is_over_determined():
    from math import lcm
    assert lcm(9, 12) == 36 and 1008 // 28 == 36 and 28 * 36 == 1008 and Fraction(24 * 3, 2) == 36
    assert 36 == 4 * 9 and Fraction(36, 1000) == Fraction(9, 250)
    # through the second route the placement arrives with the numerator: 1.008 / 28 = 0.036
    assert Fraction(1008, 1000) / 28 == Fraction(36, 1000)


def test_six_parts_per_billion():
    """137.036 stands 6.0 parts per billion above the CODATA 2022 value. The figure printed
    until version 2, 6.7, was the gap from the 2018 value."""
    assert round(float(gap_ppb("CODATA 2022")), 1) == 6.0
    assert round(float(gap_ppb("CODATA 2018")), 1) == 6.7
    assert REST - alpha_inv("CODATA 2022") == Fraction(823, 10**9)


def test_the_determinations_lie_below():
    # all three agree through the run of nines and lie strictly below the rest value,
    # by 5.8 to 7.0 parts per billion
    for m in MEASURED:
        assert str(m).startswith("137.035999") and m < 137.036
    gaps = sorted(round(float(gap_ppb(s)), 1) for s in DETERMINATIONS)
    assert gaps == [5.8, 6.1, 7.0]
    # the two interferometry values differ by more than five standard deviations
    d = (alpha_inv("Paris 2020") - alpha_inv("Berkeley 2018")) * 10**9
    assert d == 160 and d**2 > 5**2 * (27**2 + 11**2)
    # and every modern value lies inside the window the companion record registers
    for source in ALPHA_INV:
        assert Fraction("137.035999") < alpha_inv(source) < Fraction("137.036000")


def test_the_count_in_standard_deviations_is_not_stable():
    """The gap is fixed and the divisor is not: 35 to 72 across four sources."""
    counts = {s: float(gap_in_sigma(s)) for s in ("Berkeley 2018", "CODATA 2022", "Harvard 2023", "Paris 2020")}
    assert [int(counts[s]) for s in counts] == [35, 39, 55, 72]
    assert max(counts.values()) / min(counts.values()) > 2


def test_borrow_signature():
    # 0.036 - 794e-9 = 0.035999206, the Paris value digit for digit
    assert borrow_signature(794) == "0.035999206"
    assert borrow_signature(954) == "0.035999046"   # Berkeley
    assert borrow_signature(0) == "0.036000000"


def test_family_affair_exact():
    product, block, avg = family_affair()
    assert product == Fraction(1008, 1000)      # 28 x .036 = 1.008 exactly
    assert block == Fraction(9, 250)            # .036 = 9/250
    assert 28 == 7 * 8 // 2                     # 28 = T(7)
    assert 36 == 8 * 9 // 2 and 28 * 36 == 1008  # 36 = T(8), and the base is their product
    assert 1008 == 42 * 24
    assert 28 * 35999 == 1007972                # 28 x 0.035999 = 1.007972 exactly


def test_the_settled_block_carries_over_to_the_nucleon_mean():
    """Twenty-eight times the settled block, the six digits every determination shares, is
    1.007972 exactly, 1.3 parts per million above the measured mean of the two masses.

    Beyond the block the determinations differ from one another, and with their further digits
    the product stands 2.6 to 7.0 parts per million above the mean. The proton and neutron
    record states the same thing from the other side: the image of the mean, m/28, is
    0.0359989533, it rounds to the settled block at six decimals, and every determination
    stands above it by 0.09 to 0.25 millionths."""
    mean = nucleon_mean()
    assert mean == Fraction("1.00797069131945") and round(float(mean), 7) == 1.0079707
    assert 28 * Fraction("0.035999") == Fraction("1.007972")
    assert round(float(nucleon_relation_ppm("0.035999")), 1) == 1.3
    across = sorted(round(float(nucleon_relation_ppm(tail(s))), 1) for s in DETERMINATIONS)
    assert across == [2.6, 5.9, 7.0]
    assert round(float(nucleon_relation_ppm(tail("CODATA 2022"))), 1) == 6.2
    image = mean / 28
    assert round(float(image), 10) == 0.0359989533 and f"{float(image):.6f}" == "0.035999"
    above = sorted(float(tail(s) - image) * 10**6 for s in DETERMINATIONS)
    assert 0.09 < above[0] < 0.10 and 0.25 < above[-1] < 0.26


def test_the_offset_carries_over():
    """The block's offset is one unit of the sixth decimal. Carried through the factor it is
    2.8e-5, against the mean's own offset from its base, 2.9e-5, and the stations' average, 3."""
    block_offset = Fraction(36, 1000) - Fraction("0.035999")
    assert block_offset == Fraction(1, 10**6) and 28 * block_offset == Fraction(28, 10**6)
    below_base = Fraction(1008, 1000) - nucleon_mean()
    assert round(float(below_base) * 10**5, 1) == 2.9 and Fraction(-72 + 66, 2) == -3
    # with a determination's further digits the carried offset is smaller: 2.3e-5 on CODATA 2022
    assert round(float(28 * (Fraction(36, 1000) - tail("CODATA 2022"))) * 10**5, 1) == 2.3


# --- section 7: the block and the nucleon masses -----------------------------------------------

def test_the_stations():
    assert Fraction(1008, 1000) - Fraction(72, 10**5) == Fraction("1.00728")
    assert Fraction(1008, 1000) + Fraction(66, 10**5) == Fraction("1.00866")
    assert Fraction(-72 + 66, 2) == -3
    # the stations are read from the measured masses at three digits; what the truncation
    # leaves is 3.5 and 4.9 parts per million
    assert round(float((Fraction("1.00728") - M_P) / M_P) * 10**6, 1) == 3.5
    assert round(float((M_N - Fraction("1.00866")) / M_N) * 10**6, 1) == 4.9
    assert abs((1.008 - 72e-5) - M_P_U) < 5e-6 and abs((1.008 + 66e-5) - M_N_U) < 5e-6
    # the signs: the bare proton below bound hydrogen's 1.008, the free neutron above
    assert M_P < Fraction(1008, 1000) < M_N
    # three numbers meet at 1.00797: the average of 1.00728 and 1.00866, exactly; the measured
    # mean; and twenty-eight times the settled block. The base, 1.00800, does not.
    assert (Fraction("1.00728") + Fraction("1.00866")) / 2 == Fraction("1.00797")
    settled = 28 * Fraction("0.035999")
    assert f"{float(nucleon_mean()):.5f}" == f"{float(settled):.5f}" == "1.00797" != f"{1.008:.5f}"
    assert (f"{float(nucleon_mean()):.6f}", f"{float(settled):.6f}") == ("1.007971", "1.007972")
    # with the further digits of three of the four sources the product rounds to 1.00798:
    # the agreement at five places is a statement about the settled block
    assert [f"{float(28 * tail(x)):.5f}" for x in ("Berkeley 2018", "Harvard 2023", "CODATA 2022", "Paris 2020")] \
        == ["1.00797", "1.00798", "1.00798", "1.00798"]


def test_two_forms_gap_three():
    round_form, all_nines, gap = two_forms()
    assert round_form == {2: 8, 3: 1, 5: 8}            # does not contain 137
    assert all_nines == {3: 3, 11: 1, 73: 1, 101: 1, 137: 1}
    assert gap == 3
    # the SI numeral is 0.07 percent below both
    for n in (3 * 10**8, 3 * (10**8 - 1)):
        assert round((n - 299792458) / n * 100, 2) == 0.07


# --- section 1: the literature -----------------------------------------------------------------

def test_wyler():
    """Wyler's expression gives 137.0360824. It stands 0.6 parts per million above the CODATA
    2022 value, which excludes it by some four thousand standard deviations. Against the
    adjustment of his day, 137.03602(21) with its 1.5 parts per million (Taylor, Parker and
    Langenberg, 1969), it lay 0.46 parts per million away, inside the uncertainty."""
    w = wyler()
    assert abs(w - 137.0360824) < 5e-8
    now = float(alpha_inv("CODATA 2022"))
    assert round((w - now) / now * 1e6, 1) == 0.6
    assert (w - now) / 21e-9 > 3900
    then, then_err = 137.03602, 0.00021
    assert round(then_err / then * 1e6, 1) == 1.5
    assert abs(w - then) < then_err and round(abs(w - then) / then * 1e6, 2) == 0.46
