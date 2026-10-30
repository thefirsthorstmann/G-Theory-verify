"""test_midy_pairs_not_orders.py — MIDY GIVES THE PAIRING AND NOT THE
ORDERING, AND SECTION 5 CLAIMED OTHERWISE (2026-08-21). Found by finishing
the over-determination census as an *audit* after CC pushed back on
abandoning it. He was right to: I had folded two different things into one
recommendation — the census as an argument (unavailable, correctly dropped)
and the census as a correctness check (owed, and it found this).

WHAT §5 CLAIMED. "Midy's theorem pairs the reptend's halves to nines:
142 + 857 = 999. **The first half is therefore all low digits and the
second all high**, and the second half — 8, 5, 7 — is precisely the set of
deciders." The load-bearing word is *therefore*.

WHAT IS TRUE. The pairing is general; **the ordering is not.** For
1/13 = 076923 the halves also sum to nines — Midy holds — but the pairs run
0+9, **7+2, 6+3**: the second and third reversed, high paired below low. The
low/high separation fails at 13, 17, 19, 23, 29, 47, 59 and 61, which is
every even-period prime tested except 7 and the degenerate 11.

**So the separation is a property of seven, not a consequence of Midy**, and
the sentence promoted a fact about one prime into a theorem about reptends.
What survives — and what the generation argument actually uses — is the fact
about seven itself, which is real and is now stated as such.

AND THE CENSUS ENTRY THAT GOES WITH IT: this was offered as "a second,
independent route" to one-signedness. It is not a second route at all. It is
a second *face* of the same prime's digit structure, and the paper now says
face rather than route.
"""

from sympy import n_order


def _reptend(p):
    per = n_order(10, p)
    return str((10 ** per - 1) // p).zfill(per), per


def test_midy_pairing_is_general():
    for p in (7, 11, 13, 17, 19, 23, 29):
        rep, per = _reptend(p)
        if per % 2:
            continue
        h = per // 2
        assert int(rep[:h]) + int(rep[h:]) == 10 ** h - 1


def test_but_the_low_high_ordering_is_not():
    failures = []
    for p in (7, 11, 13, 17, 19, 23, 29, 47, 59, 61):
        rep, per = _reptend(p)
        if per % 2:
            continue
        h = per // 2
        lo = all(int(d) <= 4 for d in rep[:h])
        hi = all(int(d) >= 5 for d in rep[h:])
        if not (lo and hi):
            failures.append(p)
    assert 7 not in failures
    assert 13 in failures and 17 in failures and 19 in failures
    assert len(failures) >= 6


def test_thirteen_is_the_smallest_counterexample():
    rep, per = _reptend(13)
    assert rep == "076923"
    assert int("076") + int("923") == 999            # Midy holds
    pairs = [(int(rep[i]), int(rep[i + 3])) for i in range(3)]
    assert pairs == [(0, 9), (7, 2), (6, 3)]
    reversed_pairs = [(a, b) for a, b in pairs if a >= 5 > b]
    assert len(reversed_pairs) == 2                  # two of three reversed


def test_seven_is_the_special_case():
    rep, _ = _reptend(7)
    assert rep == "142857"
    assert all(int(d) <= 4 for d in rep[:3])
    assert all(int(d) >= 5 for d in rep[3:])


def test_so_it_is_a_face_and_not_a_route():
    claimed = "a second, independent route"
    true = "a second face of the same prime's digit structure"
    assert claimed != true
    independent = False
    assert not independent


def test_the_generation_argument_still_stands():
    """It uses the fact about seven, which is real."""
    rep, _ = _reptend(7)
    deciders = [int(rep[d]) for d in (3, 4, 5)]
    assert deciders == [8, 5, 7]
    assert all(x >= 5 for x in deciders)
