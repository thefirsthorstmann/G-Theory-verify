"""The line selects its arithmetic (11 October 2026; CC: "what would it be like if a line of the symbol was more fundamental
than number, that number came to be the most accurate description and differentiation of what maybe at first were much
more akin the qualitative rather than quantitative expressions of the universe").

The proposal, given a computable form: define the figure by its line properties alone, without its numbers, and ask which
arithmetic realizes it. The enneagram's line properties (ORIGIN-M-MATHEMATICAL-COMPANION, Theorem M2, parts 1-3) are: a
single closed stroke (one line: b a primitive root modulo p); the stroke as long as the digit ring Z/(b - 1) has units
(p - 1 = phi(b - 1)); and the stroke exhausting those units, so that the untouched digits are the non-units (an ideal when
b - 1 is a prime power). The Midy mirror follows from the even period.

Pinned, exact:
  * among all bases b <= 1000, the one-line figures as long as their ring has units are many, and exactly four exhaust the
    units: (p, b) = (2, 3), (3, 5), (7, 10) and (487, 730), with digit rings Z/2, Z/4, Z/9 and Z/729; the untouched sets are
    {0}, {0, 2}, {0, 3, 6} and the multiples of three; (b <= 3000 in the lab run: 272 candidates, the same four hits);
  * the rings are prime powers q^j, and for such a ring b = q^(j-1) (mod p) exactly, with p = (q - 1) q^(j-1) + 1; when
    j - 1 is even, b is a square modulo p and cannot be a primitive root: the odd powers of three and the rings 8, 32, 512
    are excluded by structure; the 2-series has exactly the members 2 and 4 among the Fermat-type cases; the 3-series has
    3^2 and 3^6 and fails at 3^10 and 3^18 (p = 2 3^9 + 1 and 2 3^17 + 1 prime, base not a primitive root) and at 3^14 (p
    composite); nothing with q = 5 or 7 below the same bounds;
  * so the enneagram, (7, 10) on Z/9, is the smallest complete figure with more than two points, and the only one in base
    ten; the next is (487, 730) on Z/729 with 486 points. Number comes after the line in the logical order: the line's
    properties select (7, 10). Corollary: the complete figures live in bases 3, 5, 10 and 730, so base ten is the smallest
    base whose digit ring carries a complete figure with more than two points, and the next such base is 730.
READING, open (may or may not be physics in terms of our current understanding): the figure before its coordinates is
Klein's stance (the figure is its symmetry group; the parity board found that group to be Aut(A2)); that counting is born
of the line is CC's, and the theorem above is its first forced consequence. Whether physics rests on the figure is the
capacity ledger's question and is not decided here. Section 10: 729 = 3^6 appears as the sixth power of three in a
prime-power series and is not read.
"""

from math import gcd

from sympy import factorint, isprime, n_order, totient


def _cycle_digits(p, b):
    r, digits = 1, []
    for _ in range(n_order(b, p)):
        r *= b
        digits.append(r // p)
        r %= p
    return digits


def _units(k):
    return sorted(u for u in range(1, k) if gcd(u, k) == 1)


def test_exactly_four_lines_exhaust_their_rings_units_below_base_1000():
    candidates, hits = 0, []
    for b in range(3, 1001):
        k = b - 1
        p = int(totient(k)) + 1
        if not isprime(p) or b % p == 0 or n_order(b, p) != p - 1:
            continue
        candidates += 1
        d = _cycle_digits(p, b)
        if (k == 2 and d == [1]) or sorted(set(x % k for x in d)) == _units(k):
            hits.append((p, b, k))
    assert candidates > 80
    assert hits == [(2, 3, 2), (3, 5, 4), (7, 10, 9), (487, 730, 729)]
    assert [factorint(k) for _, _, k in hits] == [{2: 1}, {2: 2}, {3: 2}, {3: 6}]
    assert _cycle_digits(7, 10) == [1, 4, 2, 8, 5, 7]
    assert sorted(set(range(9)) - set(_cycle_digits(7, 10))) == [0, 3, 6]
    untouched_729 = set(range(729)) - set(x % 729 for x in _cycle_digits(487, 730))
    assert untouched_729 == set(range(0, 729, 3))


def test_the_prime_power_series_and_the_square_obstruction():
    for q in (2, 3, 5, 7):
        for j in range(1, 12):
            k = q ** j
            b, p = k + 1, (q - 1) * q ** (j - 1) + 1
            assert b % p == (q ** (j - 1)) % p
    status = {}
    for q in (2, 3):
        for j in range(1, 12):
            k = q ** j
            b, p = k + 1, (q - 1) * q ** (j - 1) + 1
            if not isprime(p):
                status[(q, j)] = "p not prime"
            elif j > 1 and (j - 1) % 2 == 0:
                status[(q, j)] = "square"
            else:
                status[(q, j)] = "full" if n_order(b % p, p) == p - 1 else "short"
    assert [j for j in range(1, 12) if status[(2, j)] == "full"] == [1, 2]
    assert [j for j in range(1, 12) if status[(3, j)] == "full"] == [2, 6]
    assert status[(3, 10)] == "short"
    for n, expect_prime, expect_full in ((9, True, False), (13, False, None), (17, True, False)):
        p = 2 * 3 ** n + 1
        assert isprime(p) == expect_prime
        if expect_prime:
            assert (n_order((3 ** (n + 1) + 1) % p, p) == p - 1) == expect_full
