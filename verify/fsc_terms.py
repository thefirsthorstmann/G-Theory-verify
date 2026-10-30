"""fsc_terms.py — The Fine-Structure Constant on Discrete Terms, version 2.

The integer of the coupling as a fact about its decimal ring, the rest value 137.036 above the
measured approach, and the relation of the block to the nucleon masses.

THE EXACT LAYER (integer and rational arithmetic, no floats):
  (1) the three spellings: 137 = 2^7 + 3^2 = 8*17 + 1, with 17 = 3^4 - 2^6
  (2) the ring theorem: ord_137(10) = 8, hence 136/8 = 17 cyclic families; the identity
      137 = 8*17 + 1 is the closure equation p - 1 = period * families
  (3) the scarcity: the primes of decimal period eight are exactly {73, 137}, since each must
      divide 10^8 - 1; their product is 10001
  (4) the backbone 00729927: its halves sum to 9999, each of the four digit-pairs across the
      split sums to nine, and read in twos it is 00|72|99|27 with 72 + 27 = 99
  (5) 28 * 36/1000 = 1008/1000 exactly (28 = T(7), 36/1000 = 9/250); the stations -72 and +66
      about the base 1008 average -3
  (6) the two integers: 3*10^8 = 2^8*3*5^8, which does not contain 137, and
      3*(10^8 - 1) = 3^3*11*73*101*137, which does; they differ by exactly 3
  (7) the borrow: 0.036 - 7.94e-7 = 0.035999206, exact as decimal strings
  (8) the censuses: five integers in [100, 200] are of the form 2^a + 3^b; two of the
      thirty-five primes below 150 have period eight

THE COMPARISON LAYER (measured central values, entered as their sources print them, and compared
in exact rational arithmetic):
  (9) every determination lies below 137.036, by 5.8 to 7.0 parts per billion; from the CODATA
      2022 value the gap is 6.0, and from that of 2018 it was 6.7. The same gap counted in
      standard deviations runs from 35 to 72, because the divisor differs by laboratory and year
 (10) twenty-eight times the settled block, 0.035999, is 1.007972: 1.3 parts per million above
      the mean of the proton and neutron masses, and equal at five decimal places to that mean
      and to the average of 1.00728 and 1.00866, which is 1.00797 exactly. With the
      determinations' further digits, which differ from one another, the product stands 2.6 to
      7.0 parts per million above the mean (6.2 on the CODATA 2022 value)
 (11) Wyler's value, 137.0360824, stands 0.6 parts per million above the 2022 value

The rest value 137.036 is a reading. It is defined at zero excitation and reached only by
calculation; what an instrument returns is the measured value.
"""

import math
from fractions import Fraction

# --- measured values, as their sources print them ----------------------------------------------
# inverse fine-structure constant: (central value, uncertainty in the last digits)
ALPHA_INV = {
    "Berkeley 2018": ("137.035999046", 27),   # Parker et al., Science 360 (2018) 191, caesium
    "Paris 2020": ("137.035999206", 11),      # Morel et al., Nature 588 (2020) 61, rubidium
    "Harvard 2023": ("137.035999166", 15),    # Fan et al., Phys. Rev. Lett. 130 (2023) 071801
    "CODATA 2018": ("137.035999084", 21),     # Tiesinga et al., Rev. Mod. Phys. 93 (2021) 025010
    "CODATA 2022": ("137.035999177", 21),     # Mohr et al., Rev. Mod. Phys. 97 (2025) 025002
}
DETERMINATIONS = ("Berkeley 2018", "Paris 2020", "Harvard 2023")
ALPHA_INV_BERKELEY = float(ALPHA_INV["Berkeley 2018"][0])
ALPHA_INV_PARIS = float(ALPHA_INV["Paris 2020"][0])
ALPHA_INV_HARVARD = float(ALPHA_INV["Harvard 2023"][0])
MEASURED = (ALPHA_INV_BERKELEY, ALPHA_INV_PARIS, ALPHA_INV_HARVARD)

# proton and neutron masses in unified atomic mass units, CODATA 2022
M_P = Fraction("1.0072764665789")    # (83)
M_N = Fraction("1.00866491606")      # (40)
M_P_U, M_N_U = float(M_P), float(M_N)

REST = Fraction(137036, 1000)        # the rest value
REST_BLOCK = Fraction(36, 1000)      # its first decimal block
BASE = Fraction(1008, 1000)          # 28 times the rest block


def spellings():
    """The three spellings of the integer, exact."""
    return 2**7 + 3**2, 8*17 + 1, 3**4 - 2**6


def ord10(p):
    """Multiplicative order of 10 mod p (p coprime to 10)."""
    if p in (2, 5) or p % 2 == 0 or p % 5 == 0:
        raise ValueError("p must be coprime to 10")
    k, x = 1, 10 % p
    while x != 1:
        x = x * 10 % p
        k += 1
    return k


def _factor(n):
    f, d = {}, 2
    while d * d <= n:
        while n % d == 0:
            f[d] = f.get(d, 0) + 1
            n //= d
        d += 1
    if n > 1:
        f[n] = f.get(n, 0) + 1
    return f


def period_primes(k):
    """All primes whose decimal period is exactly k. Every one must divide 10^k - 1, so the
    census is a factorization, and it is closed."""
    return sorted(p for p in _factor(10**k - 1) if ord10(p) == k)


def reptend(p, k=None):
    """The repeating block of 1/p as a digit string."""
    k = k or ord10(p)
    return str(10**k // p).zfill(k)


def midy_halves(block):
    """The two halves of an even block and their sum."""
    h = len(block) // 2
    a, b = int(block[:h]), int(block[h:])
    return a, b, a + b


def family_affair():
    """28 x .036 = 1.008 exactly, as fractions; and the average of the two stations."""
    product = 28 * REST_BLOCK                  # = Fraction(1008, 1000)
    tail = REST_BLOCK                          # = 9/250
    avg_station = Fraction(-72 + 66, 2)        # = -3
    return product, tail, avg_station


def two_forms():
    """The integers 3 x 10^8 and 3 x (10^8 - 1), factored, and their gap."""
    round_form, all_nines = 3 * 10**8, 3 * (10**8 - 1)
    return _factor(round_form), _factor(all_nines), round_form - all_nines


def borrow_signature(eps_billionths):
    """0.036 minus eps (in units of 1e-9), as an exact decimal string: the run of nines is the
    borrow of the subtraction."""
    val = REST_BLOCK - Fraction(eps_billionths, 10**9)
    return "0." + str(int(val * 10**9)).zfill(9)


def alpha_inv(source):
    """The central value of a source, exact."""
    return Fraction(ALPHA_INV[source][0])


def gap_ppb(source):
    """How far a source's value lies below the rest value 137.036, in parts per billion of
    the value. Exact."""
    a = alpha_inv(source)
    return (REST - a) / a * 10**9


def gap_in_sigma(source):
    """The same gap in that source's own standard deviations. It is not a stable figure: the
    numerator is fixed and the divisor differs by laboratory and by year."""
    return (REST - alpha_inv(source)) * 10**9 / ALPHA_INV[source][1]


def nucleon_mean():
    """The mean of the proton and neutron masses, CODATA 2022, in u. Exact."""
    return (M_P + M_N) / 2


def nucleon_relation_ppm(tail):
    """Twenty-eight times a tail, against the mean of the two masses, in parts per million of
    the mean. Exact. A positive value means the product stands above the mean."""
    mean = nucleon_mean()
    return (28 * Fraction(tail) - mean) / mean * 10**6


def tail(source):
    """The decimal part of a source's value: its distance above the integer 137."""
    return alpha_inv(source) - 137


def wyler():
    """Wyler's value of the inverse constant, from his expression
    alpha = (9 / 8 pi^4) (pi^5 / 2^4 5!)^(1/4)."""
    alpha = 9 / (8 * math.pi**4) * (math.pi**5 / (2**4 * math.factorial(5))) ** 0.25
    return 1 / alpha


def spelling_census(lo=100, hi=200):
    """Integers in [lo, hi] expressible as 2^a + 3^b, a,b >= 1."""
    s = {2**a + 3**b for a in range(1, 12) for b in range(1, 8)}
    return sorted(n for n in s if lo <= n <= hi)


def octave_primes_below(n=150):
    """Primes below n with decimal period exactly 8, and the prime count."""
    def isprime(m):
        if m < 2:
            return False
        d = 2
        while d * d <= m:
            if m % d == 0:
                return False
            d += 1
        return True
    primes = [p for p in range(2, n) if isprime(p)]
    p8 = [p for p in primes if p not in (2, 5) and ord10(p) == 8]
    return p8, len(primes)
