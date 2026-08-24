"""test_the_contact_window_interval.py — THE WINDOW NEEDS NO MAXIMISATION
(2026-08-18). The last piece of the promotion question was why the
register should sit at the maximum of contact per child. It does not have
to: the window has a second characterisation with no optimisation in it
at all, and the maximum is a consequence of that rather than a preference
the register obeys.

THE SECOND CHARACTERISATION. Read the contact counts in the register's
own two generators. At one dimension the count is 2 — pure doubling, no
three. At two, three and four it is 2^a·3 — **exactly one three**. At
five a **five** appears, which the register does not have. So the window
is the half-open interval

    [ the first appearance of the second generator ,
      the first appearance of a foreign prime )   =   [2, 5)

and that is the promotion window exactly, stated without maximising
anything. The register does not choose the window. It can only spell
contact counts in the generators it has, and this is the stretch over
which contact is spellable.

WHAT CLOSES THE DOOR IS THE FIVE, NOT THE SECOND THREE. Six dimensions
would also close it, seventy-two carrying two threes — but the five
arrives first, at five dimensions, so a prime foreign to the register is
what actually ends the window.

SIX CANDIDATE PRINCIPLES WERE TESTED AND FOUR REJECTED. Being a
two-three word admits six dimensions as well; contact merely keeping up
with refinement admits one through six; the kissing number being proven
exactly admits eight; a half-integer ratio admits one. Only the extremum
and the spelling condition select the window and nothing else, and they
are independent of one another — one is an optimisation, the other is
arithmetic in the alphabet.

WHAT IS STILL NOT DERIVED. Why contact should cost exactly one three
rather than none or two is a question about the register's generators,
and is nearer the mechanics than "why two, three and four" was — but it
is not answered here, and the promotion item is recorded as moved rather
than closed.
"""

import sympy as sp
from fractions import Fraction

CONTACT = {1: 2, 2: 6, 3: 12, 4: 24, 5: 40, 6: 72, 7: 126, 8: 240,
           9: 306, 10: 500, 11: 582, 12: 840}
WINDOW = [2, 3, 4]


def test_the_window_is_a_half_open_interval_between_two_arrivals():
    """The second generator arrives at two; a foreign prime at five."""
    first_three = min(d for d in CONTACT if sp.factorint(CONTACT[d]).get(3, 0) >= 1)
    first_foreign = min(d for d in CONTACT
                        if set(sp.factorint(CONTACT[d])) - {2, 3})
    assert first_three == 2 and first_foreign == 5
    assert list(range(first_three, first_foreign)) == WINDOW


def test_the_window_carries_exactly_one_three():
    """Spelled in the register's generators and nothing else."""
    for d in WINDOW:
        f = sp.factorint(CONTACT[d])
        assert set(f) <= {2, 3}
        assert f[3] == 1
    assert sp.factorint(CONTACT[1]).get(3, 0) == 0        # below: none
    assert sp.factorint(CONTACT[6])[3] == 2               # above: two


def test_the_five_closes_it_before_the_second_three_would():
    """Six dimensions would also fail, but five gets there first."""
    assert 5 in [d for d in CONTACT if set(sp.factorint(CONTACT[d])) - {2, 3}]
    assert sp.factorint(CONTACT[6])[3] == 2 and not (set(sp.factorint(72)) - {2, 3})
    assert 5 < 6


def test_only_two_of_six_candidate_principles_select_it():
    """And they are independent: an extremum and a spelling condition."""
    best = max(Fraction(CONTACT[d], 2 ** d) for d in CONTACT)
    cands = {
        "maximise contact per child":
            [d for d in CONTACT if Fraction(CONTACT[d], 2 ** d) == best],
        "contact is a two-three word":
            [d for d in CONTACT if set(sp.factorint(CONTACT[d])) <= {2, 3}],
        "contact carries exactly one three":
            [d for d in CONTACT if set(sp.factorint(CONTACT[d])) <= {2, 3}
             and sp.factorint(CONTACT[d]).get(3, 0) == 1],
        "contact keeps up with refinement":
            [d for d in CONTACT if Fraction(CONTACT[d], 2 ** d) >= 1],
        "kissing number proven exactly": [1, 2, 3, 4, 8],
        "ratio is a half-integer":
            [d for d in CONTACT if Fraction(CONTACT[d], 2 ** d).denominator <= 2],
    }
    selecting = [k for k, v in cands.items() if v == WINDOW]
    assert sorted(selecting) == ["contact carries exactly one three",
                                 "maximise contact per child"]
    assert len(selecting) == 2


def test_the_maximum_is_a_consequence_not_a_preference():
    """Given the spelling condition, the ratio is forced to three halves —
    so nothing has to be optimised for the maximum to appear."""
    for d in WINDOW:
        a = sp.factorint(CONTACT[d])[2]
        assert a == d - 1                                  # 2^(d-1) x 3
        assert Fraction(CONTACT[d], 2 ** d) == Fraction(3, 2)


def test_what_remains_owed_is_named():
    """Why one three rather than none or two — a question about the
    generators, nearer the mechanics, and not answered here."""
    owed = "why contact costs exactly one three"
    assert "one three" in owed
    status = {"why dimensions two three four": "answered as an interval",
              "why exactly one three": "open"}
    assert status["why exactly one three"] == "open"
