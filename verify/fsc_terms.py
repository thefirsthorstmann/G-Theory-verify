"""fsc_terms.py — THE FINE-STRUCTURE CONSTANT ON DISCRETE TERMS.

The coupling's integer as a decimal-ring fact, the rest form above the
measured approach, and the family affair with the nucleon dyad.

EXACT CORE (integer arithmetic, no floats):
  (1) the three spellings: 137 = 2^7 + 3^2 = 8*17 + 1, with 17 = 3^4 - 2^6
  (2) the ring theorem: ord_137(10) = 8, hence 136/8 = 17 cyclic families
      — the identity 137 = 8*17 + 1 IS the closure equation p-1 = ord*families
  (3) the scarcity: the period-8 primes in all of arithmetic are exactly
      {73, 137} (both must divide 10^8 - 1); their product is 10001
  (4) the backbone 00729927: Midy halves 0072+9927 = 9999, all four
      digit-pairs across the split sum to 9, twos-blocks 00|72|99|27
      with 72 + 27 = 99
  (5) the family affair: 28 * 36/1000 = 1008/1000 exactly (28 = T(7),
      36/1000 = 9/250); offsets -72/+66 about base 1008 average -3
  (6) the two forms: 3*10^8 = 2^8*3*5^8 (carries no 137, remainder 3);
      3*(10^8-1) = 3^3*11*73*101*137 (carries 137); gap exactly 3
  (7) the borrow signature: 0.036 - 7.94e-7 = 0.035999206 (digit-exact
      as decimal strings; the nines are the borrow in flight)

FLOAT LAYER (memory-sourced measured values, bands sized generously):
  (8) the tension exhibit: Berkeley-2018 Cs 137.035999046(27),
      Paris-2020 Rb 137.035999206(11), Harvard-2023 g-2 137.035999166(15)
      — all agree through the nines (dec 4-6), all sit STRICTLY BELOW
      137.036, displaced +0.0058 to +0.0070 ppm; they disagree with one
      another at >5 sigma only from decimal 7 onward
  (9) the pricing censuses: five integers in [100,200] spell as 2^a+3^b;
      two of the 35 primes below 150 close at the octave

The .036 reading is STRIKING / selection-bearing, never Forced — the
rigor ledger's standing correction. The rest form is 72 sigma from the
best single measurement: an ideal, not a measurement-prediction, per
the shield (rest values are reached only by calculation).
"""

from fractions import Fraction

# --- measured values (float layer; memory-sourced CODATA/experiment) ---
ALPHA_INV_BERKELEY = 137.035999046   # Parker et al. 2018, Cs interferometry
ALPHA_INV_PARIS = 137.035999206      # Morel et al. 2020, Rb interferometry
ALPHA_INV_HARVARD = 137.035999166    # Fan et al. 2023, electron g-2 route
MEASURED = (ALPHA_INV_BERKELEY, ALPHA_INV_PARIS, ALPHA_INV_HARVARD)
M_P_U = 1.0072765                    # proton mass, atomic units (ratio)
M_N_U = 1.0086649                    # neutron mass, atomic units (ratio)


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
    """ALL primes whose decimal period is exactly k — every one must
    divide 10^k - 1, so the census is a factorization, closed."""
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
    """28 x .036 = 1.008 exactly, as fractions; and the offset average."""
    product = 28 * Fraction(36, 1000)          # = Fraction(1008, 1000)
    tail = Fraction(36, 1000)                  # = 9/250
    avg_offset = Fraction(-72 + 66, 2)         # = -3
    return product, tail, avg_offset


def two_forms():
    """The two forms of the light-unit and their gap."""
    observed, rest = 3 * 10**8, 3 * (10**8 - 1)
    return _factor(observed), _factor(rest), observed - rest


def borrow_signature(eps_tenmillionths):
    """0.036 minus eps (in units of 1e-9), as an exact decimal string —
    the run of nines is the borrow in flight."""
    val = Fraction(36, 1000) - Fraction(eps_tenmillionths, 10**9)
    # render to 9 decimal places exactly
    scaled = val * 10**9
    return "0." + str(int(scaled)).zfill(9)


def displacement_ppm(measured):
    """How far a measured alpha^-1 sits below the rest form, in ppm."""
    return (137.036 - measured) / measured * 1e6


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
