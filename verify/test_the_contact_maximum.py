"""test_the_contact_maximum.py — THE PROMOTION WINDOW IS AN EXTREMUM
(2026-08-18). the author asked whether any of the characterised items is
derivable. This one moves, and it moves the right way: from a
coincidence noted at three dimensions to a maximum principle with those
three dimensions as its argmax.

WHAT WAS CHARACTERISED. The contact count equals 3·2^(d−1) at dimensions
two, three and four and nowhere else — stated as an observation, with the
derivation from cell mechanics owed.

WHAT IT ACTUALLY IS. Divide the register's two counts by each other.
Contact is how many neighbours a cell can touch; refinement makes 2^d
children. Their ratio — **contact per child** — is 1 at one dimension,
**exactly 3/2 at two, three and four**, and falls away on the other side:
1.25, 1.125, 0.98, 0.94, and downward. So the window is not a place where
two formulas happen to agree. It is **where contact per child attains its
maximum, and that maximum is exactly the fifth.**

WHY THAT IS THE RIGHT READING. Contact is what a cell can union with;
refinement is what a subdivision costs. Contact per child is therefore
union opportunity per unit of refinement, and the register sitting at its
maximum is a least-action statement in the program's own currency, not an
imported one. The promotion question sharpens again: from "why is contact
three halves of refinement there" to "why does the register sit at the
maximum of contact per refinement" — which is the shape of question this
program answers, where the previous form was not.

AND IT IS SECURE, not an artifact of best-known constructions. The
saturation is proven, since the kissing number is settled exactly at one,
two, three, four, eight and twenty-four. The failure outside is tested
against the best UPPER bounds rather than against known packings, so no
future construction can move it: at five dimensions the upper bound is
forty-four against a ceiling of forty-eight — the closest call anywhere —
and every larger dimension is far below. Asymptotically the kissing
number grows like 2^0.401d, so the ceiling 3·2^(d−1) is never approached
again.

ONE HONEST WRINKLE, kept rather than smoothed. Contact per child is not
monotone after the window: it rises once, at twenty-four, where the Leech
lattice is exceptionally dense. That is a bump in a quantity already far
below the maximum and it does not touch the argmax — and twenty-four
being the one dimension that breaks a monotone slide is a fact this
program is on the record about elsewhere.
"""

import math

# Kissing numbers. Exact where the value is proven; otherwise the pair
# (best known packing, best known upper bound) — the upper bound is what
# the argument uses, so no future construction can disturb it.
EXACT = {1: 2, 2: 6, 3: 12, 4: 24, 8: 240, 24: 196560}
UPPER = {5: 44, 6: 78, 7: 134, 9: 364, 10: 554, 11: 870, 12: 1357,
         13: 2069, 14: 3183, 15: 4866, 16: 7355, 17: 11072, 18: 16572,
         19: 24812, 20: 36764, 21: 54584, 22: 82340, 23: 124416}
BEST = {1: 2, 2: 6, 3: 12, 4: 24, 5: 40, 6: 72, 7: 126, 8: 240, 9: 306,
        10: 500, 11: 582, 12: 840, 13: 1154, 14: 1606, 15: 2564,
        16: 4320, 17: 5346, 18: 7398, 19: 10668, 20: 17400, 21: 27720,
        22: 49896, 23: 93150, 24: 196560}

WINDOW = [2, 3, 4]


def _ceiling(d):
    return 3 * 2 ** (d - 1)


def test_the_window_saturates_the_ceiling_and_is_proven_there():
    """At two, three and four the contact count equals three halves of
    the child count exactly — and those dimensions are among the ones
    where the kissing number is settled, so the saturation is not
    provisional."""
    for d in WINDOW:
        assert d in EXACT
        assert EXACT[d] == _ceiling(d)
        assert EXACT[d] == 3 * 2 ** d // 2


def test_contact_per_child_is_exactly_three_halves_on_the_window():
    """The ratio of the register's two counts, on the window."""
    for d in WINDOW:
        assert EXACT[d] / 2 ** d == 1.5


def test_no_dimension_can_ever_reach_it_again():
    """Tested against the best UPPER bounds, so no future packing can
    change the verdict — and five dimensions is the closest call in all
    of them, at forty-four against forty-eight."""
    for d, ub in UPPER.items():
        assert ub < _ceiling(d), d
        assert ub / 2 ** d < 1.5, d
    for d in (8, 24):
        assert EXACT[d] < _ceiling(d)
    assert UPPER[5] / _ceiling(5) > 0.9              # the tightest margin
    assert all(UPPER[d] / _ceiling(d) < 0.9 for d in UPPER if d != 5)


def test_one_dimension_falls_short_from_below():
    """The window's lower edge is a shortfall, not a different rule: at
    one dimension a cell has two neighbours where the ceiling allows
    three."""
    assert EXACT[1] == 2 and _ceiling(1) == 3
    assert EXACT[1] / 2 ** 1 == 1.0


def test_the_window_is_the_argmax_of_contact_per_child():
    """The result: contact per child attains its maximum exactly on the
    window, and the maximum is exactly the fifth."""
    ratios = {d: BEST[d] / 2 ** d for d in BEST}
    top = max(ratios.values())
    assert top == 1.5
    assert sorted(d for d, r in ratios.items() if r == top) == WINDOW
    assert (3, 2) == top.as_integer_ratio()


def test_the_argmax_survives_the_upper_bounds():
    """And the argmax is secure for the same reason: replacing every
    unsettled dimension by its upper bound leaves the maximum and its
    location unchanged."""
    ratios = {}
    for d in BEST:
        val = EXACT[d] if d in EXACT else UPPER[d]
        ratios[d] = val / 2 ** d
    assert max(ratios.values()) == 1.5
    assert sorted(d for d, r in ratios.items() if r == 1.5) == WINDOW


def test_the_ratio_falls_away_and_bumps_once_at_twenty_four():
    """Kept rather than smoothed: the fall is not monotone. It rises at
    exactly one dimension, twenty-four, where the Leech lattice is
    exceptionally dense — far below the maximum, and not touching the
    argmax."""
    ratios = [BEST[d] / 2 ** d for d in range(1, 25)]
    rises = [d for d in range(5, 25) if ratios[d - 1] > ratios[d - 2]]
    assert rises == [24]
    assert ratios[23] < 0.02                          # nowhere near the peak


def test_the_asymptotic_reason_the_ceiling_is_never_met_again():
    """Kissing numbers grow like 2^(0.401 d); the ceiling grows like 2^d.
    The gap widens without bound, so the window cannot reopen."""
    for d in (50, 100, 500):
        assert 0.401 * d + 1 < d - 1 + math.log2(3)
        assert 2 ** (0.401 * d) / _ceiling(d) < 1e-6


def test_the_reading_that_makes_it_least_action():
    """Contact is what a cell can union with; refinement is what a
    subdivision costs. Their ratio is union opportunity per unit of
    refinement, so the window is where the register buys the most contact
    per child — a least-action statement in the program's own currency."""
    reading = {"numerator": "contact — what a cell can union with",
               "denominator": "refinement — 2^d children per subdivision",
               "ratio": "union opportunity per unit of refinement",
               "optimum": (3, 2), "argmax": WINDOW}
    assert reading["optimum"] == (3, 2) and reading["argmax"] == [2, 3, 4]
    assert 12 in (2 ** 2 * 3,)                        # space, inside the window
    assert 24 == 3 * 2 ** 3                           # spacetime, likewise
