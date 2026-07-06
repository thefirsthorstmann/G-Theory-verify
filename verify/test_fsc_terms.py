"""Pins for "The Fine-Structure Constant on Discrete Terms" (fsc_terms.py)."""

from fractions import Fraction

from fsc_terms import (spellings, ord10, period_primes, reptend,
                       midy_halves, family_affair, two_forms,
                       borrow_signature, displacement_ppm,
                       spelling_census, octave_primes_below,
                       MEASURED, M_P_U, M_N_U)


def test_three_spellings():
    a, b, c = spellings()
    assert a == 137 and b == 137 and c == 17


def test_ring_theorem():
    # ord_137(10) = 8, hence 17 families: the closure equation IS 8*17+1
    assert ord10(137) == 8
    assert (137 - 1) // ord10(137) == 17


def test_octave_scarcity():
    # the period-8 primes in all of arithmetic: exactly {73, 137}
    assert period_primes(8) == [73, 137]
    assert 73 * 137 == 10001
    # the sevenths' class for comparison: period 6 = {7, 13}
    assert period_primes(6) == [7, 13]
    # and the harmonic constant is lossless (full period, one family)
    assert ord10(7) == 6 and (7 - 1) // ord10(7) == 1


def test_backbone_midy():
    b = reptend(137)
    assert b == "00729927"
    a, z, s = midy_halves(b)
    assert (a, z, s) == (72, 9927, 9999)
    # all four digit-pairs across the split sum to nine
    assert all(int(x) + int(y) == 9 for x, y in zip(b[:4], b[4:]))
    # twos-blocks 00|72|99|27: the transform pair about the central 99
    assert b[2:4] == "72" and b[4:6] == "99" and b[6:8] == "27"
    assert 72 + 27 == 99
    # the sevenths obey the same law one octave-class down
    assert midy_halves(reptend(7)) == (142, 857, 999)
    # CC's reflection center: complements pivot on half the all-nines —
    # the register's all-nines brought down one octave (999/8*4 = 999/2)
    assert (142 + 857) / 2 == 499.5 == 999 / 2 == 999 / 8 * 4
    assert (72 + 9927) / 2 == 4999.5 == 9999 / 2


def test_backbone_family():
    # every fraction over 137 carries the four-nines complement
    for k in (1, 2, 3, 7):
        block = str(10**8 * k // 137).zfill(8)
        assert midy_halves(block)[2] == 9999


def test_family_affair_exact():
    product, tail, avg = family_affair()
    assert product == Fraction(1008, 1000)      # 28 x .036 = 1.008 exactly
    assert tail == Fraction(9, 250)             # .036 = 9/250
    assert 28 == 7 * 8 // 2                     # 28 = T(7)
    assert avg == -3                            # (-72 + 66)/2 — the gap of three again
    # base 1008 = 42 x 24; offsets land on the measured dyad at the 1e-5
    # scale — the residuals (3.5e-6, 4.9e-6) are the truncation residue of
    # reading -72.35/+66.49 as -72/+66, flagged in the ledger as read,
    # not derived
    assert 1008 == 42 * 24
    assert abs((1.008 - 72e-5) - M_P_U) < 5e-6
    assert abs((1.008 + 66e-5) - M_N_U) < 5e-6
    # the starred banked result: (p+n)/2 matches 28 x measured-tail to 5 digits
    assert abs((M_P_U + M_N_U) / 2 - 28 * 0.0359990) < 3e-5
    # the settled block transports (CC): 28 x 0.035999 = 1.007972 EXACTLY
    # (integer core: 28 x 35999 = 1007972), meeting the dyad mean at 1.3 ppm
    assert 28 * 35999 == 1007972
    assert abs(28 * 0.035999 - (M_P_U + M_N_U) / 2) < 2e-6
    # and the block gap carried through the factor tracks the dyad offset
    assert abs(28 * 1e-6 - abs((M_P_U + M_N_U) / 2 - 1.008)) < 2e-6


def test_two_forms_gap_three():
    obs, rest, gap = two_forms()
    assert obs == {2: 8, 3: 1, 5: 8}            # carries no 137
    assert rest == {3: 3, 11: 1, 73: 1, 101: 1, 137: 1}
    assert gap == 3


def test_borrow_signature():
    # 0.036 - 794e-9 = 0.035999206: the Paris value digit-exact;
    # the run of nines is the borrow in flight
    assert borrow_signature(794) == "0.035999206"
    assert borrow_signature(954) == "0.035999046"   # Berkeley
    assert borrow_signature(0) == "0.036000000"


def test_tension_exhibit_float_layer():
    # all three determinations agree through the nines and sit strictly
    # below the rest form, displaced +0.0058..0.0070 ppm
    for m in MEASURED:
        assert str(m).startswith("137.035999")
        assert m < 137.036
        assert 0.0055 < displacement_ppm(m) < 0.0072
    # they disagree with each other only from decimal 7 onward
    assert max(MEASURED) - min(MEASURED) < 2e-7
    assert max(MEASURED) - min(MEASURED) > 1e-7   # the >5-sigma spread is real


def test_pricing_censuses():
    # the razor: the odds each register meets by chance
    assert spelling_census() == [113, 131, 137, 145, 155]   # 5 of 101
    p8, nprimes = octave_primes_below(150)
    assert p8 == [73, 137] and nprimes == 35                # 2 of 35
