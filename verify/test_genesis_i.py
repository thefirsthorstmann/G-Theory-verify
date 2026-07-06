"""test_genesis_i.py — Chapter I pinned: the three moves, exact."""

from fractions import Fraction as F

from genesis_i import (commitment_ladder, first_operation, is_involution,
                       multiplicative_order, no_closure, positional_order)
from gtheory import rounded_seventh


def test_the_two_canonical_orders():
    """The first complete period admits exactly the positional order
    (division's) and the multiplicative order (the doubling orbit) —
    and THE TRANSFORM'S OUTPUT IS THE DOUBLING ORBIT AS DIGITS."""
    assert positional_order() == "142857"
    assert multiplicative_order() == "124875"
    assert first_operation()["out"] == multiplicative_order()


def test_the_first_operation_is_free():
    """An involution is its own inverse: invertible, Landauer-free.
    Least action at the origin is an observation."""
    assert is_involution()


def test_the_first_ledger():
    """Displacement +-18 and its conservation, born in one move."""
    t = first_operation()
    assert t["down"] == (42, 24, -18)
    assert t["up"] == (57, 75, 18)
    assert t["net"] == 0
    assert t["sum_pre"] == t["sum_post"] == 99


def test_the_contest_never_closes():
    """2^a = 3^b has no positive solution — the seed pair is
    incommensurable; succession cannot terminate."""
    assert no_closure()


def test_the_commitment_ladder():
    """Depths 3, 4, 5 round the carriers 2, 8, 5 up to 3, 9, 6; the
    depth-3 commitment is EXACT: x 1001/1000 (7 divides 10^3 + 1)."""
    assert commitment_ladder() == [(3, 2, 3), (4, 8, 9), (5, 5, 6)]
    assert rounded_seventh(3) * 7 == F(1001, 1000)
    assert (10 ** 3 + 1) % 7 == 0


def test_time_needs_the_carry_and_the_ring():
    """The 3-walk on the 8-ring closes only at lcm(3,8) = 24 — the
    escapement (the clock's own pins carry the traversal)."""
    import math
    assert math.lcm(3, 8) == 24
    walk, seen = 0, set()
    for _ in range(8):
        walk = (walk + 3) % 8
        seen.add(walk)
    assert len(seen) == 8                          # the 3-step visits all
