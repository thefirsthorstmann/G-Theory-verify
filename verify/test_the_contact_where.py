"""test_the_contact_where.py — THE TRIGGER'S LAST CLAUSE: WHERE (2026-08-15).
WHEN and WHAT closed earlier today; WHERE — which two objects come to be held
as one pair — was the remaining debt. It closes as a COLLISION IN THE ADDRESS
REGISTER, and the rate that falls out has a shape worth the whole exercise.

  THE PIECES ARE ALL BANKED. ORIGIN-IX: position is an ADDRESS at a resolution;
  locality is ADJACENCY in the register; entropy COUNTS COLLISIONS. The held
  form: the collapse is many-to-one exactly at the integers. Derived this
  morning: the union fires at co-carry. Nothing new is imported below.

  WHERE, STATED. A record's address advances only when its register carries.
  Two records are held as one pair exactly when they occupy ONE address — a
  collision — and a collision can only BEGIN on a carry, because nothing else
  moves an address. So WHERE and WHEN are not two conditions: contact IS the
  carry, seen from the register instead of from the phase. That much is a
  consequence of the model rather than a discovery, and is recorded as such.

  THE RATE IS THE RESULT. A ring of period p carries once every p ticks, so its
  carry rate is 1/p. Two rings co-carry every lcm(p,q) ticks, so the contact
  rate is 1/lcm(p,q) — and 1/lcm(p,q) = gcd(p,q)/(pq) exactly. For COPRIME
  periods that is (1/p)(1/q): THE PRODUCT OF THE TWO RINGS' OWN RATES.

  AND MASS-IS-ROUNDING IS BANKED. A rounding is a carry, so a ring's carry rate
  is its mass, and the contact rate between two rings is the PRODUCT OF THE TWO
  MASSES — the bilinear source form, Newton's numerator, arrived at rather than
  assumed. GRADE, stated precisely: the arithmetic is forced; mass-is-rounding
  is a banked identification held loose, so the physics reading inherits that
  grade and is NOT Forced. What is forced is that the co-incidence rate of two
  independent carry-clocks factorises exactly when they are coprime.

  THE FORBID IS THE gcd. The product law is exact ONLY for coprime periods.
  Commensurable pairs contact MORE often, by exactly gcd(p,q) — a stated,
  bounded exception to bilinearity rather than a universal law. Checked on all
  2374 commensurable pairs below eighty: the enhancement is exactly the gcd,
  never anything else.

  AND IT IS THE SAME CONDITION AS THE MORNING'S. Informational co-occupancy
  coincides with the union window iff the rings are coprime; the contact rate
  factorises into a product iff the rings are coprime. One condition, two
  consequences, reached from two directions on the same day.

  WHAT THIS DOES NOT DO, SAID PLAINLY. It supplies no dependence on separation.
  The inverse square is banked separately and by a different route — the
  deficit 1/(d+1) read as perspective extension, with energy quadratic in
  displacement. m1*m2 and 1/r^2 are TWO results that compose; they were not
  derived together, and no joint derivation is claimed here.
"""

from fractions import Fraction as F
from math import gcd, lcm


def _addr(t, p, off=0):
    """A record's address: it advances only when the register carries."""
    return t // p + off


def test_an_address_moves_only_on_a_carry():
    for p in range(2, 14):
        for t in range(1, 6 * p):
            moved = _addr(t, p) != _addr(t - 1, p)
            assert moved == (t % p == 0)


def test_a_collision_can_only_begin_on_a_carry():
    """Contact IS a carry event, seen from the register."""
    onsets = bad = 0
    for p in range(2, 13):
        for q in range(2, 13):
            for off in range(-3, 4):
                prev = None
                for t in range(0, 4 * lcm(p, q) + 1):
                    now = _addr(t, p) == _addr(t, q, off)
                    if prev is not None and now and not prev:
                        onsets += 1
                        if not (t % p == 0 or t % q == 0):
                            bad += 1
                    prev = now
    assert onsets == 1680 and bad == 0


def test_the_contact_rate_is_one_over_the_lcm():
    for p, q in ((2, 3), (3, 4), (4, 9), (3, 5), (6, 42)):
        L = lcm(p, q)
        co = [t for t in range(1, 3 * L + 1) if t % p == 0 and t % q == 0]
        assert co == [L, 2 * L, 3 * L]
        assert F(len(co), 3 * L) == F(1, L)


def test_the_rate_factorises_exactly_when_the_periods_are_coprime():
    """gcd(p,q)/(pq) is the rate; it is (1/p)(1/q) iff gcd = 1."""
    for p in range(2, 80):
        for q in range(2, 80):
            assert F(1, lcm(p, q)) == F(gcd(p, q), p * q)
            assert (F(1, lcm(p, q)) == F(1, p) * F(1, q)) == (gcd(p, q) == 1)
    cop = [(p, q) for p in range(2, 80) for q in range(2, 80) if gcd(p, q) == 1]
    non = [(p, q) for p in range(2, 80) for q in range(2, 80) if gcd(p, q) > 1]
    assert len(cop) == 3710 and len(non) == 2374
    assert all(F(1, lcm(p, q)) == F(1, p) * F(1, q) for p, q in cop)
    # the forbid: commensurable pairs are enhanced by EXACTLY the gcd
    assert all(F(1, lcm(p, q)) == gcd(p, q) * F(1, p) * F(1, q) for p, q in non)


def test_the_enhancement_is_the_stated_exception_to_bilinearity():
    """Named cases, including the program's own commensurable pairs."""
    for p, q, k in ((4, 6, 2), (6, 42, 6), (24, 72, 24), (8, 12, 4)):
        assert gcd(p, q) == k
        assert F(1, lcm(p, q)) == k * F(1, p) * F(1, q)
    # and 2 perp 3, the substrate, is the clean bilinear case:
    assert gcd(2, 3) == 1 and F(1, lcm(2, 3)) == F(1, 2) * F(1, 3) == F(1, 6)


def test_the_separation_dependence_is_absent_and_that_is_recorded():
    """m1*m2 here; 1/r^2 is banked elsewhere; no joint derivation is claimed."""
    rate_depends_on = {"periods": True, "separation": False}
    assert rate_depends_on["periods"] and not rate_depends_on["separation"]
    # the rate is unchanged by moving either record's address offset:
    p, q = 3, 5
    for off in (-4, 0, 7, 100):
        co = [t for t in range(1, 3 * lcm(p, q) + 1)
              if _addr(t, p) != _addr(t - 1, p) and _addr(t, q, off) != _addr(t - 1, q, off)]
        assert co == [15, 30, 45]
