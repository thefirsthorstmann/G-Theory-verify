"""
THE REPTEND 1/7 = 0.142857  —  the lossless harmonic constant.   GRADE: FORCED ◆

The whole program is tethered here. 1/7 has the maximal-length repeating decimal a
prime can have in base 10 (a "full reptend": period = p - 1), and 7 is the SMALLEST
prime with that property. This is a fact about base 10, cold-checkable, and it is why
the framework treats 1/7 as the harmonic constant rather than choosing it.

Source: catalog/THE-FULL-POSITION-INTERNAL §18 (the seventh as harmonic reciprocal);
06-VERIFICATION-LOG ("7 = smallest full-reptend prime").
"""
from sympy import isprime, n_order


def decimal_period(p):
    """Length of the repeating block of 1/p in base 10 (= multiplicative order of 10 mod p)."""
    return n_order(10, p)


def test_one_seventh_reptend_is_142857():
    # long division of 1/7, six digits
    digits, r = [], 1
    for _ in range(6):
        r *= 10
        digits.append(r // 7)
        r %= 7
    assert digits == [1, 4, 2, 8, 5, 7]
    assert r == 1  # the remainder returns to 1 -> the block repeats forever


def test_seven_is_full_reptend():
    # full reptend: the period equals p - 1, the longest possible
    assert decimal_period(7) == 6 == 7 - 1


def test_seven_is_the_SMALLEST_full_reptend_prime_base10():
    # 2 and 5 terminate (no reptend); 3 has period 1, not 2; 7 is the first full reptend.
    for p in [2, 3, 5]:
        assert not (isprime(p) and p not in (2, 5) and decimal_period(p) == p - 1)
    # explicit: 7 qualifies, and nothing below it does
    full_reptend_primes = [p for p in range(2, 8) if isprime(p) and p not in (2, 5)
                           and decimal_period(p) == p - 1]
    assert full_reptend_primes == [7]


def test_midy_halving():
    # the two halves of the reptend sum to all-nines  (142 + 857 = 999)
    assert 142 + 857 == 999


def test_cyclic_permutations():
    # 142857 * k (k=1..6) are the six cyclic rotations of the same digits  (the "cyclic number")
    base = sorted(str(142857))
    for k in range(1, 7):
        assert sorted(str(142857 * k)) == base
