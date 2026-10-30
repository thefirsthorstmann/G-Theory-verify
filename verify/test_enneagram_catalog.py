"""test_enneagram_catalog.py — structural catalog of the reptend figure, 2026-08-07.

Extends THE-ENNEAGRAM-IS-A-THEOREM sideways rather than repeating it. That paper
gives the Line Theorem (strokes = (p-1)/ord_p(b), unicursal iff full reptend) and
five completeness facts for the pair (7,10). Here: the third ordering's own mirror
law, and the completeness condition generalised across bases.
"""

from math import gcd
from sympy import n_order, totient, isprime, primerange


def _digits(p, b, L):
    r, out = 1, []
    for _ in range(L):
        r *= b
        out.append(r // p)
        r %= p
    return out


def test_the_harmonic_order_has_its_own_midy():
    """NEW. The paper notes the harmonic (node) order — the leading digits of k/p,
    floor(b*k/p) — is not a Hamiltonian reading, and leaves it there. But it carries
    a mirror law of its own:

        floor(bk/p) + floor(b(p-k)/p) = b - 1   for every k

    because bk/p is never an integer (p prime, p does not divide b), so the ceiling
    is the floor plus one. That is the third ordering's Midy, and unlike the
    reptend's it holds in EVERY base for EVERY prime, full period or not."""
    for b in (10, 2, 3, 7, 12, 16):
        for p in primerange(3, 60):
            if b % p == 0:
                continue
            harm = [(b * k) // p for k in range(1, p)]
            for k in range((p - 1) // 2):
                assert harm[k] + harm[p - 2 - k] == b - 1


def test_completeness_is_almost_never_available():
    """The figure is COMPLETE when it is one stroke visiting exactly the units mod
    (b-1) — so the untouched set is the non-units, which for base ten is the
    triangle {3,6,9}. Searched over every base to 1000: it happens at 3, 5, 10 and
    730 only, and nontrivially (period > 2) at 10 and 730 alone."""
    hits = []
    for b in range(3, 1001):
        m = b - 1
        ph = int(totient(m))
        p = ph + 1
        if not isprime(p) or b % p == 0:
            continue
        try:
            L = int(n_order(b, p))
        except ValueError:
            continue
        if L != p - 1:
            continue
        units = {u for u in range(1, m + 1) if gcd(u, m) == 1}
        if {x if x else m for x in _digits(p, b, L)} == units:
            hits.append((b, ph))
    assert [h[0] for h in hits] == [3, 5, 10, 730]
    assert [h[0] for h in hits if h[1] > 2] == [10, 730]


def test_the_family_is_the_powers_of_three_and_the_triangle_generalises():
    """Both nontrivial members have ring b-1 = 3^k — nine and 729. In that family
    the units mod 3^k are exactly the non-multiples of 3, so THE UNTOUCHED SET IS
    ALWAYS THE MULTIPLES OF THREE: the enneagram's triangle {3,6,9} is the k=2
    instance of a general fact. Within the family the condition holds at k = 2 and
    k = 6 and nowhere else up to k = 12."""
    assert 9 == 3**2 and 729 == 3**6
    for k in (2, 6):
        m = 3**k
        non_units = {x for x in range(1, m + 1) if gcd(x, m) > 1}
        assert non_units == {x for x in range(1, m + 1) if x % 3 == 0}
    assert {3, 6, 9} == {x for x in range(1, 10) if x % 3 == 0}      # the triangle
    good = []
    for k in range(1, 13):
        m = 3**k
        b = m + 1
        p = int(totient(m)) + 1
        if not isprime(p) or b % p == 0:
            continue
        try:
            L = int(n_order(b, p))
        except ValueError:
            continue
        if L != p - 1:
            continue
        units = {u for u in range(1, m + 1) if gcd(u, m) == 1}
        if {x if x else m for x in _digits(p, b, L)} == units:
            good.append(k)
    assert good == [2, 6]


def test_why_the_condition_is_thin():
    """p must be phi(b-1)+1, prime, and have b as a primitive root. When b-1 is
    PRIME, phi(b-1) = b-2 so p = b-1, and then b = 1 (mod p) — the order collapses
    to 1 and the figure cannot be one stroke. So b-1 must be composite, which is
    why the family lives on prime POWERS."""
    for b in (4, 6, 8, 12, 14, 18, 20, 24):
        if not isprime(b - 1):
            continue
        p = b - 1
        assert int(totient(b - 1)) + 1 == p
        assert b % p == 1                       # b = 1 mod p, order collapses
        assert int(n_order(b, p)) == 1 if b % p == 1 else True
