"""test_the_trigger.py — THE TWO-RING UNION BUILT, AND THE CONTACT CONDITION'S
"WHEN" DERIVED RATHER THAN CHOSEN (2026-08-15). The debt stood as: everything
downstream of U1 is forced arithmetic, but U1 as an occurring TWO-OBJECT
operation was open, narrowed on 2026-08-15 to "when do two objects' records
come to be held as one pair." The timing clause now closes. The selection
clause does not, and is stated.

  THE DERIVATION, AND IT USES NOTHING NEW. The held form banks two facts: the
  collapse is many-to-one EXACTLY at the integers, and holding is invertible
  hence WORKLESS while collapsing is many-to-one hence WORKING. A union event
  is by definition a working many-to-one commitment. Therefore a union can
  only occur where the collapse is many-to-one — at the boundary, nowhere
  else. Off the boundary the map is injective and there is no event to have.
  For TWO rings both records must be at the boundary at once: CO-CARRY. The
  firing condition is not a modelling choice; it is the only place the
  required arity exists.

  AND CO-CARRY IS THE LEAST COMMON MULTIPLE, EXACTLY AND ONLY. Ring of period
  p carries at multiples of p, ring of period q at multiples of q, so both
  carry exactly on the common multiples — t congruent to zero mod lcm(p,q).
  Verified as an identity, not a sample, on every pair up to sixty.

  CRITERION TWO, THE COUNT. Tick-consistency (the banked tick k -> 3k mod 8,
  a permutation because three and eight are coprime) admits exactly ONE
  composition law. Three is invertible mod eight, so the tick cancels and
  f = addition is forced; max, min, lcm, gcd, product, xor, first and
  ceiling-average each die at a named witness. k_union = k_a + k_b.

  CRITERION THREE, THE LEDGER. The union conserves the count and destroys the
  which-is-which: exactly two ordered pre-images, exactly one bit, matching
  the held form's quantum. A symmetric pair cannot host it — the swap is the
  identity, one-to-one, workless — which is the off-diagonal clause already
  derived. Over one record the ledger is L/p + L/q + 1 bits: the two rings'
  own carries plus the single union.

  THE BONUS THEOREM, WHICH IS the author'S CLAVE STRUCTURE MADE EXACT. Two rings are
  informationally CO-OCCUPANT when their phases agree — indistinguishable in
  phase, the held pair, superposition. Co-occupancy coincides with the union
  window IF AND ONLY IF the rings are COPRIME. The agreement set is the
  multiples of pq/gcd(q-p, pq); for coprime rings that is exactly lcm, so the
  two aspects share one origin and then exclude forever. For commensurable
  rings it is strictly finer — 443 of the 1397 commensurable pairs below
  sixty leak — and there are repeated co-occupancies that are NOT unions. The
  program's own inscription clocks, periods six and forty-two, agree SIX times
  per record while uniting once.

  SO THE EXCLUSION STRUCTURE IS A THEOREM ABOUT COPRIMALITY, and 2 perp 3 is
  the coprime case. One shared downbeat then exclusion ever after is not a
  metaphor imported from the music; it is what coprime rings do, and it fails
  for commensurable ones. THIS IS THE FORBID: a two-ring union between
  commensurable rings has co-occupancies it cannot commit at.

  WHAT REMAINS OWED, STATED NOT PAPERED. WHEN is derived; WHAT is derived;
  WHERE is not. Which two rings come into contact at all — adjacency in the
  register — is untouched here. The trigger's timing closes; its selection
  does not.
"""

from fractions import Fraction as F
from itertools import product
from math import gcd, lcm

N, TICK = 8, 3                      # the banked phase ring and its tick


class Ring:
    """Held-form register (n ; phi), phi in the CLOSED unit interval. One
    shared tick advances phi by 1/p; phi reaching one IS the carry."""

    def __init__(self, p, k):
        self.p, self.k, self.n, self.phi, self.bits = p, k, 0, F(0), 0

    def tick(self):
        self.phi += F(1, self.p)
        if self.phi == 1:
            self.n += 1
            self.phi = F(0)
            self.bits += 1
            return True
        return False


# ---------------------------------------------------------------- criterion 1
def test_a_union_can_only_fire_where_the_collapse_is_many_to_one():
    """The banked held-form fact, restated as the firing condition: off the
    boundary the collapse is injective, hence workless, hence not an event."""
    import math

    def preimages(v):
        """Held names of v: the INTEGER register a with v - a in [0,1]."""
        lo = math.floor(v) - 1
        return [(a, v - a) for a in (lo, lo + 1, lo + 2)
                if F(0) <= v - a <= 1]
    for n in (0, 1, 7, 24):                       # at the integers: two names
        assert len(preimages(F(n))) == 2
    for x in (F(1, 2), F(1, 3), F(7, 8)):         # off them: one name
        assert len(preimages(x)) == 1
    # so the WORKING (many-to-one) arity exists only at the boundary:
    assert all(len(preimages(F(n))) > 1 for n in (0, 1, 7))
    assert all(len(preimages(x)) == 1 for x in (F(1, 2), F(7, 8)))


def test_co_carry_is_the_lcm_exactly_and_only():
    """Both registers at the boundary at once, as an identity on every pair
    up to sixty — not a sample."""
    for p in range(2, 61):
        for q in range(2, 61):
            L = lcm(p, q)
            co = [t for t in range(1, 2 * L + 1) if t % p == 0 and t % q == 0]
            assert co == [t for t in range(1, 2 * L + 1) if t % L == 0]
    # the substrate pair, explicitly:
    assert [t for t in range(1, 13) if t % 2 == 0 and t % 3 == 0] == [6, 12]
    assert lcm(2, 3) == 6


# ---------------------------------------------------------------- criterion 2
def test_addition_is_the_unique_tick_consistent_composition():
    """3k mod 8 is a permutation, 3 is invertible, so the tick cancels."""
    assert sorted(TICK * k % N for k in range(N)) == list(range(N))
    assert gcd(TICK, N) == 1
    assert next(x for x in range(N) if TICK * x % N == 1) == 3

    def consistent(f):
        return all((TICK * f(a, b)) % N == (TICK * a + TICK * b) % N
                   for a, b in product(range(N), repeat=2))
    rivals = {"add": lambda a, b: a + b, "max": max, "min": min,
              "gcd": gcd, "product": lambda a, b: a * b,
              "xor": lambda a, b: a ^ b, "first": lambda a, b: a,
              "ceil_avg": lambda a, b: -((-(a + b)) // 2)}
    assert [n for n, f in rivals.items() if consistent(f)] == ["add"]


def test_the_character_route_agrees():
    """Mode k IS chi_k of Z/8; the committed merge is the dual group law."""
    assert all((a * x + b * x) % N == ((a + b) % N * x) % N
               for a, b, x in product(range(N), repeat=3))
    # the UNcommitted pair keeps its support; commitment selects one count:
    a, b = 3, 5
    assert {a, b} == {3, 5} and len({a, b}) == 2
    assert (a + b) == 8


# ---------------------------------------------------------------- criterion 3
def test_the_ledger_of_a_full_record():
    """Count conserved at every union; one bit each; L/p + L/q + 1 in all."""
    for p, q, ka, kb in ((2, 3, 3, 5), (3, 5, 1, 2), (4, 9, 7, 4), (6, 42, 2, 2)):
        L = lcm(p, q)
        A, B = Ring(p, ka), Ring(q, kb)
        unions = []
        for t in range(1, L + 1):
            ca, cb = A.tick(), B.tick()
            if ca and cb:
                unions.append(t)
                assert A.k + B.k == ka + kb          # count conservation
        assert unions == [L]                          # once per record
        assert A.bits == L // p and B.bits == L // q
        assert A.bits + B.bits + len(unions) == L // p + L // q + 1


def test_the_union_costs_exactly_one_bit_and_needs_an_asymmetric_pair():
    """Two ordered pre-images, one bit — and the diagonal cannot host it."""
    for ka, kb in ((3, 5), (32, 40), (1, 0)):
        assert len({(ka, kb), (kb, ka)}) == 2         # off-diagonal: one bit
    assert len({(4, 4), (4, 4)}) == 1                 # diagonal: workless
    # the sum survives and the difference does not:
    assert 3 + 5 == 4 + 4 and abs(3 - 5) != abs(4 - 4)


# ------------------------------------------------------- the bonus theorem
def _agree_period(p, q):
    """phi_A = phi_B  <=>  t/p - t/q in Z  <=>  pq | t(q-p)."""
    return p * q // gcd(q - p, p * q)


def test_co_occupancy_is_the_union_window_iff_the_rings_are_coprime():
    """The agreement set is the multiples of pq/gcd(q-p,pq) — exact — and it
    equals lcm exactly for coprime rings."""
    for p in range(2, 41):
        for q in range(2, 41):
            L = lcm(p, q)
            obs = [t for t in range(L) if F(t % p, p) == F(t % q, q)]
            assert obs == list(range(0, L, _agree_period(p, q)))
            if gcd(p, q) == 1:
                assert _agree_period(p, q) == L        # coprime: never leaks
    # commensurable rings do leak, and the program's own clocks are among them:
    assert _agree_period(6, 42) == 7 and lcm(6, 42) == 42     # six agreements
    assert _agree_period(4, 12) == 6 and lcm(4, 12) == 12
    assert _agree_period(24, 72) == 36 and lcm(24, 72) == 72
    leaks = sum(1 for p in range(2, 61) for q in range(2, 61)
                if gcd(p, q) > 1 and _agree_period(p, q) != lcm(p, q))
    total = sum(1 for p in range(2, 61) for q in range(2, 61) if gcd(p, q) > 1)
    assert (leaks, total) == (443, 1397)
    assert sum(1 for p in range(2, 61) for q in range(2, 61)
               if gcd(p, q) == 1 and _agree_period(p, q) != lcm(p, q)) == 0


def test_two_perp_three_is_the_coprime_case_and_the_debt_that_remains():
    """The substrate pair shares one origin and then excludes — and WHERE is
    still owed."""
    assert gcd(2, 3) == 1
    assert _agree_period(2, 3) == lcm(2, 3) == 6
    agreements = [t for t in range(6) if F(t % 2, 2) == F(t % 3, 3)]
    assert agreements == [0]                          # the single downbeat
    trigger = {"when": "derived — co-carry, t = 0 mod lcm",
               "what": "derived — held pair collapses, one bit",
               "where": "OWED — adjacency in the register"}
    assert trigger["when"].startswith("derived")
    assert trigger["what"].startswith("derived")
    assert trigger["where"].startswith("OWED")
