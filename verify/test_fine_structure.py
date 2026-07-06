"""
THE FINE-STRUCTURE INTEGER 137  —  the electrical sibling of the sevenths.  GRADE: FORCED ◆
(the INTEGER and its arithmetic. The measured tail .035999 is the diffused exhibition,
NOT derived. The whole-coupling claim is held outside the forced column.)

What is forced, cold:
  137 is prime and equals 8·17 + 1   (the octave times the spine, plus the unit)
  136 = 8·17, and ord_137(10) = 8  ->  exactly 17 cyclic families of fractions
  the spine 17 = 3^4 - 2^6 = 81 - 64
  the 8-digit block of 1/137 is 00729927, halves 0072 + 9927 = 9999, digit-sum 36
  the reptend's Fourier spectrum has its EVEN harmonics exactly zero (the Fourier door)

Source: catalog/THE-FULL-POSITION-INTERNAL §18; CHAPTER-fine-structure-constant.
"""
import cmath
from sympy import isprime, n_order


def reptend_digits(p, length):
    digits, r = [], 1
    for _ in range(length):
        r *= 10
        digits.append(r // p)
        r %= p
    return digits


def test_137_decomposition():
    assert isprime(137)
    assert 137 == 8 * 17 + 1
    assert 136 == 8 * 17


def test_spine_17_is_81_minus_64():
    assert 17 == 3**4 - 2**6 == 81 - 64


def test_order_eight_gives_seventeen_families():
    assert n_order(10, 137) == 8          # 137 | 10^8 - 1
    assert (10**8 - 1) % 137 == 0
    assert 136 // n_order(10, 137) == 17   # 136 fractions / period 8 = 17 cosets


def test_the_block_and_its_midy_halves():
    d = reptend_digits(137, 8)
    assert d == [0, 0, 7, 2, 9, 9, 2, 7]            # 00729927
    assert 72 + 9927 == 9999                         # 0072 + 9927 (the four-nines complement)
    assert sum(d) == 36 == 4 * 9                      # digit-sum = the baseline 36


def test_reptend_spectrum_even_harmonics_vanish():
    """
    THE FOURIER DOOR (FORCED ◆).  The 8-point DFT of the digits [0,0,7,2,9,9,2,7]:
    the even harmonics k = 2,4,6 are EXACTLY zero, forced by the Midy half-period
    relation d[n+4] = 9 - d[n].  DC (k=0) = the digit-sum 36.  Odd-only structure.
    """
    d = reptend_digits(137, 8)
    N = 8
    X = [sum(d[n] * cmath.exp(-2j * cmath.pi * k * n / N) for n in range(N)) for k in range(N)]
    # the forced half-period antisymmetry:
    for n in range(4):
        assert d[n + 4] == 9 - d[n]
    # even harmonics vanish (machine-zero):
    for k in (2, 4, 6):
        assert abs(X[k]) < 1e-9
    # DC term is the digit-sum:
    assert abs(X[0].real - 36) < 1e-9 and abs(X[0].imag) < 1e-9
    # odd harmonics are NOT zero (there is real structure there):
    for k in (1, 3, 5, 7):
        assert abs(X[k]) > 1.0
