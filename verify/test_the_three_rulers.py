"""test_the_three_rulers.py — THE BORROW-ACCOUNTING DEBT HAS NAMES
(2026-08-18). The account's one-ruler policy is contradicted by three
dimensionful anchors. Working out what the missing ratios actually are
turns a housekeeping complaint into something better: **they are the two
famous hierarchies of physics**, and neither is a peculiar failure of this
framework.

THE THREE ANCHORS, in one unit: the electroweak length ħc/v at
8.014 × 10⁻⁴ fm, the packing cell at 8/7 fm, and the Planck length at
1.616 × 10⁻²⁰ fm.

THE TWO RATIOS OWED, and what they are called elsewhere:

  electroweak over Planck is v/M_Planck ≈ 2.0 × 10⁻¹⁷ — **the hierarchy
  problem**, unsolved by anyone.

  nuclear over electroweak is ≈ 1426 — the strong scale against the weak
  one, which is **dimensional transmutation**, also open.

So the debt is not sloppiness. Closing the first would be solving the
hierarchy problem; closing the second would be deriving the strong scale
from the weak. The account's boundary sits exactly where physics' boundary
sits, which is a fact in its favour once stated plainly and a weakness
only while left unremarked.

A CANDIDATE TESTED AND KILLED, on two counts. The nuclear-to-Planck ratio
is 7.0710 × 10¹⁹ and 5√2 = 7.07107, a miss of seven parts per million —
inside the eleven-ppm floor that G's own uncertainty imposes. It does not
survive. Sweeping ten thousand words of the form 2^a3^b7^c5^e(√2) and
counting only those landing in the same decade, the chance of some word
falling inside the window is about one in a hundred — and that count does
not even charge for the free power of ten I allowed. Worse, the reading is
**incompatible with the account's own value of G**: on the wheel's
6.67359015 the same comparison misses by forty-six ppm instead of seven.
The account cannot hold both, and the wheel is the older claim.

THE PRECISION WALL, worth stating once. G is known to twenty-two parts per
million, so the Planck length is known to eleven. No claim about any
Planck ratio can be sharper than that, whatever arithmetic is brought.
"""

import math

HBAR, C, G, DG = 1.054571817e-34, 2.99792458e8, 6.67430e-11, 1.5e-15
HBARC = 197.3269804          # MeV fm
V = 246219.65                # MeV
CELL = 8 / 7                 # fm
G_WHEEL = 6.67359015e-11     # the account's own value


def _lp(g=G):
    return math.sqrt(HBAR * g / C ** 3) * 1e15      # fm


def test_the_three_anchors_are_all_dimensionful():
    """Which is the whole problem: the policy allows one."""
    anchors = {"hbar c / v": HBARC / V, "the cell": CELL, "l_P": _lp()}
    assert len(anchors) == 3
    assert all(a > 0 for a in anchors.values())
    assert anchors["l_P"] < anchors["hbar c / v"] < anchors["the cell"]


def test_the_first_missing_ratio_is_the_hierarchy_problem():
    """v over the Planck mass, about two parts in ten million million million."""
    Mpl = math.sqrt(HBAR * C / G) * C ** 2 / 1.602176634e-19 / 1e9    # GeV
    assert abs(Mpl / 1.2209e19 - 1) < 1e-3
    ratio = (V / 1000) / Mpl
    assert 1.9e-17 < ratio < 2.1e-17
    assert abs((HBARC / V) / _lp() - 1 / ratio) / (1 / ratio) < 1e-3


def test_the_second_missing_ratio_is_dimensional_transmutation():
    """The strong scale against the weak one."""
    r = CELL / (HBARC / V)
    assert abs(r - 1426.028) < 0.01


def test_the_precision_wall_is_eleven_parts_per_million():
    """G to twenty-two ppm, so the Planck length to eleven."""
    assert abs(DG / G * 1e6 - 22) < 1
    assert abs(DG / G / 2 * 1e6 - 11) < 1


def test_the_five_root_two_candidate_is_not_significant():
    """Sweeping the alphabet and counting only the same decade, the
    chance of some word landing inside the window is about one percent —
    and that charges nothing for the free power of ten."""
    target = CELL / _lp() / 1e19
    tol = DG / G / 2
    assert abs(5 * math.sqrt(2) / target - 1) < tol          # it does land
    in_decade = 0
    for a in range(-6, 7):
        for b in range(-5, 6):
            for cc in range(-3, 4):
                for e5 in range(-2, 3):
                    for half in (0, 1):
                        val = (2.0 ** a) * (3.0 ** b) * (7.0 ** cc) * (5.0 ** e5)
                        if half:
                            val *= math.sqrt(2)
                        if 1 <= val < 10:
                            in_decade += 1
    expected = in_decade * 2 * tol / math.log(10)
    assert 0.005 < expected < 0.05                            # about one percent
    assert in_decade > 1000


def test_and_it_contradicts_the_accounts_own_g():
    """On the wheel's own value the same comparison misses by forty-six
    ppm rather than seven, so the two cannot both stand."""
    codata = abs(5 * math.sqrt(2) / (CELL / _lp() / 1e19) - 1) * 1e6
    wheel = abs(5 * math.sqrt(2) / (CELL / _lp(G_WHEEL) / 1e19) - 1) * 1e6
    assert codata < 11                                        # inside the floor
    assert wheel > 40                                         # far outside it
    assert wheel / codata > 5


def test_the_debt_is_named_rather_than_promised():
    """What closing each would amount to."""
    debts = {"electroweak over Planck": "solving the hierarchy problem",
             "nuclear over electroweak": "deriving the strong scale from the weak"}
    assert len(debts) == 2
    assert all("solving" in v or "deriving" in v for v in debts.values())
