"""test_five_halves_fold.py — THE FIVE-HALVES FOLD (CC's overnight conjecture, 2026-07-17).

CC: "5/2 is the proportion of the upper group of sevenths (4/7, 5/7, 6/7) to the
lower group (1/7, 2/7, 3/7)." Verified cold and generalized. The identity is
exact; the family it opens puts the Bell ladder's rest ceilings at its own
endpoints, with the seed prime seated uniquely at the midpoint.

Grades: the identities below are FORCED (pinned here). The identification of
the carry machine's Bell value WITH the fold-mass ratio remains a READING —
supported by the shared fold symmetry (the machine's silent arcs are one
antipode orbit; the antipode is the Midy fold) and by the banked functional
split (the upper sevenths are the ROUNDING group, and the carry is rounding's
messenger) — but no derivation yet connects the machine's E-table to these
masses. Stated as such in THE-FIVE-HALVES-FOLD.md.
"""

import sys
from fractions import Fraction as F
from math import gcd, isclose, sqrt

import carry_stand as C


def fold_ratio(p):
    """Upper-to-lower mass ratio of the fractions k/p across the Midy fold."""
    m = (p - 1) // 2
    lo = sum(F(k, p) for k in range(1, m + 1))
    up = sum(F(k, p) for k in range(m + 1, p))
    return up / lo


def test_the_identity():
    """CC's conjecture, exact: (4/7+5/7+6/7)/(1/7+2/7+3/7) = 5/2."""
    upper = sum(F(k, 7) for k in (4, 5, 6))
    lower = sum(F(k, 7) for k in (1, 2, 3))
    assert upper == F(15, 7) and lower == F(6, 7)
    assert upper / lower == F(5, 2)


def test_the_split_of_the_three():
    """The six sevenths sum to 3; the fold splits that 3 into 5/7 and 2/7 of
    itself — the sevenths reappear at the level of their own total — in quanta
    of 3/7: five above, two below, 5 + 2 = 7."""
    upper = sum(F(k, 7) for k in (4, 5, 6))
    lower = sum(F(k, 7) for k in (1, 2, 3))
    whole = upper + lower
    assert whole == 3
    assert upper / whole == F(5, 7) and lower / whole == F(2, 7)
    assert upper == 5 * F(3, 7) and lower == 2 * F(3, 7)


def test_the_centroid_pair():
    """The group centroids are 5/7 and 2/7 — themselves a Midy pair (sum 1) —
    and their ratio is again 5/2."""
    cu = sum(F(k, 7) for k in (4, 5, 6)) / 3
    cl = sum(F(k, 7) for k in (1, 2, 3)) / 3
    assert (cu, cl) == (F(5, 7), F(2, 7))
    assert cu + cl == 1
    assert cu / cl == F(5, 2)


def test_the_family_closed_form():
    """For odd p, the fold-mass ratio is (3p-1)/(p+1) exactly."""
    for p in (3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 43, 47):
        assert fold_ratio(p) == F(3 * p - 1, p + 1)


def test_the_ladder_endpoints_and_the_seed_seat():
    """The family's endpoints are the Bell ladder's rest ceilings — f(3) = 2
    (the pre-written ceiling) and f(p) -> 3 (the telegraph ceiling) — and the
    carry machine's 5/2 is f at the SEED PRIME: the unique p with f(p) = 5/2,
    which is exactly the family's midpoint, the arithmetic mean of its own
    endpoints. The banked 'arithmetic mean of two and three' is structural."""
    assert fold_ratio(3) == 2
    assert fold_ratio(7) == F(5, 2)
    # monotone increasing toward 3, never reaching it
    prev = F(0)
    for p in (3, 5, 7, 11, 13, 17, 19, 23, 29):
        r = fold_ratio(p)
        assert prev < r < 3
        prev = r
    # uniqueness: 6p - 2 = 5p + 5  ->  p = 7, and only 7
    assert [p for p in range(3, 10_000) if F(3 * p - 1, p + 1) == F(5, 2)] == [7]
    # the midpoint identity
    assert F(3 * 7 - 1, 7 + 1) == (F(2) + F(3)) / 2


def test_the_octave_register_integers():
    """At the octave register the machine's raw CHSH pair equals the p = 7
    fold pair UNREDUCED: chsh_int = 20 = 3p-1 on ring 8 = p+1. Register-
    specific (n = 16 gives (40, 16), family-at-15 would give (44, 16)) —
    pinned as the octave fact it is, nothing more."""
    Es, sig, _ = C.champion(8)
    assert sig == 0
    assert (C.chsh_int(8, Es), 8) == (3 * 7 - 1, 7 + 1) == (20, 8)


def test_the_mod_four_split_count():
    """gcd(3p-1, p+1) = gcd(4, p+1), so for p ≡ 3 (mod 4) the REDUCED ratio's
    numerator and denominator sum to p itself: 5 + 2 = 7. The seed prime
    counts its own split."""
    for p in (3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 43, 47):
        assert gcd(3 * p - 1, p + 1) == gcd(4, p + 1)
        fr = F(3 * p - 1, p + 1)
        total = fr.numerator + fr.denominator
        assert total == (p if p % 4 == 3 else 2 * p)
    assert F(3 * 7 - 1, 7 + 1) == F(5, 2) and 5 + 2 == 7


def _committed(p, L):
    """Truncate every k/p at depth L (a multiple of the period), then round:
    returns (dict of committed values as exact fractions, set of rounders)."""
    t = {k: F((k * 10**L) // p, 10**L) for k in range(1, p)}
    r = {k: t[k] + (F(1, 10**L) if F(k, p) - t[k] > F(1, 2 * 10**L) else 0)
         for k in range(1, p)}
    return r, {k for k in range(1, p) if r[k] > t[k]}


def test_the_committed_whole():
    """CC's reading (2026-07-18), verified: sum the committed system — lower
    group truncated, upper group's last digits rounded — and it totals the
    whole EXACTLY. At p = 7: 0.857142 + 2.142858 = 3.000000, the rounders
    being exactly {4, 5, 6}. The repair identity underneath: the truncation
    deficit of all six sevenths is 3e-6, and the upper group's three round-ups
    restore exactly 3e-6 — the rounding group closes the system's truncation
    deficit to the unit. General theorem: for every odd p at period depth,
    #rounders = deficit in last-digit units, so the committed total is
    (p-1)/2 exactly."""
    r, rounders = _committed(7, 6)
    assert rounders == {4, 5, 6}                       # the upper group rounds
    assert sum(r[k] for k in (1, 2, 3)) == F(857142, 10**6)
    assert sum(r[k] for k in (4, 5, 6)) == F(2142858, 10**6)
    assert sum(r.values()) == 3                        # the whole, seated exactly
    # the repair identity at p = 7
    t = {k: F((k * 10**6) // 7, 10**6) for k in range(1, 7)}
    assert sum(F(k, 7) - t[k] for k in range(1, 7)) == F(3, 10**6)
    # the general theorem across primes at their period depths
    for p, L in [(3, 1), (7, 6), (11, 2), (13, 6), (17, 16), (19, 18), (23, 22)]:
        r, rounders = _committed(p, L)
        assert sum(r.values()) == F(p - 1, 2)
        assert len(rounders) == (p - 1) // 2


def test_the_three_threes():
    """Three distinct 3-objects, reconciled (no conflict with the 5/2):
    (a) the ring-SLOT fold ratio is 3 for EVERY p — slots are seed-blind;
    (b) the label-family ceiling f(p) -> 3;
    (c) the WHOLE sum(k/p) = (p-1)/2 equals 3 iff p = 7 — only at the seed
    does the system's whole coincide with the family's ceiling."""
    for p in (7, 11, 13, 19, 23):
        m = (p - 1) // 2
        lo = sum(range(1, m + 1))
        up = sum(range(m + 2, p + 1))
        assert F(up, lo) == 3                          # (a) universal slot ratio
    P = 10**6 + 3                                      # (b) via the closed form,
    fP = F(3 * P - 1, P + 1)                           # itself pinned above
    assert fP < 3 and 3 - fP < F(1, 10**5)             # approached from below, arbitrarily closely
    assert [p for p in range(3, 10_000) if F(p - 1, 2) == 3] == [7]   # (c)


def test_the_guards():
    """The five-halves belongs to the sevenths as LABELS, not slots (the slot
    ratio is universally 3 — see test_the_three_threes). And the family is
    rational at every p, so 2√2 is never seated — crossed between p = 19 and
    p = 23 (the denominator lemma's theme again)."""
    assert F(5 + 6 + 7, 1 + 2 + 3) == 3
    assert float(fold_ratio(19)) < 2 * sqrt(2) < float(fold_ratio(23))
    for p in (3, 5, 7, 11, 13, 17, 19, 23):
        r = fold_ratio(p)
        assert not isclose(float(r), 2 * sqrt(2))  # rational family, irrational bound
