"""test_pi_structure.py — the pi digit-facts of the proton cluster, pinned.

These are ◆ FORCED as digit-arithmetic (decimal expansion of pi, exact).
The IDENTIFICATION of the streams with the charge radii in femtometres
is NOT asserted here — that is a Reading (borrowed-metre morphology,
01-METHODS:52 discipline) and lives in the catalog with its grade.
"""

from fractions import Fraction as F

from mpmath import mp

mp.dps = 70
D = mp.nstr(mp.pi, 65)[2:]           # pi decimals; position n = D[n-1]


def test_first_zero_at_32():
    assert "0" not in D[:31]
    assert D[31] == "0"               # the first zero: position 32


def test_shell_0288_after_the_zero():
    assert D[31:35] == "0288"         # 2-8-8 shell loading / Sol 288
    assert 2 + 8 + 8 == 18            # the transform displacement


def test_biphase_deinterleave():
    block = D[32:50]                  # the 18 digits after the zero
    assert block == "288419716939937510"
    assert block[0::2] == "281763971"     # electron stream 2.8176397|1
    assert block[1::2] == "849199350"     # proton   stream .84919935|0
    assert block[0::2][-1] == "1" and block[1::2][-1] == "0"   # two faces


def test_five_over_four_compression():
    assert F(50, 40) == F(5, 4)       # 50 units -> 32 + 8 = 40: Mi


def test_conserved_sum_at_three_digits():
    assert F("2.817") + F("0.849") == F("3.666")   # 11/3 truncated (T3)
    full = F("2.8176397") + F("0.84919935")
    assert abs(full - F(11, 3)) / F(11, 3) < F(1, 20000)   # 0.005%


def test_05820_follows():
    assert D[49:54] == "05820"        # positions 50-54 (the 2/7-5/7 chord)
