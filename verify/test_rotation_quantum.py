"""test_rotation_quantum.py — the author, 2026-08-04: the reading depth is dimensioned.

I had written "the value changes with depth, so it is not fixed", listing depths
3,4,5,6,7,9 as though d were a free real knob. the author caught it: that IS the
continuum, admitted through the reading rather than through the object. The
address has a PERIOD, and the period is the quantum of reading.

  (1) THE ROTATION QUANTUM: a decimal reading of 1/q in base B carries a ROTATION
      COUNT, quantized by ord_q(B). Reading at a non-multiple of the period is
      reading MID-TURN, and a value quoted there is a value of the cut, not of
      the object. For 1/7 in base ten, ord_7(10) = 6: six digits IS one rotation.
  (2) SO 2.999997 IS NOT A DEPTH-6 ARTEFACT. It is THE ONE-ROTATION VALUE — the
      minimal complete reading of the six-rotation array, and the only one
      available below two turns.
  (3) AND THE DEFICIT IS QUANTIZED WITH IT: at every whole rotation m the array
      falls short of 3 by exactly 3 x 10^(-6m) — ALWAYS EXACTLY THREE UNITS OF
      THE FINAL PLACE. Scale-free in rotations, not merely depth-dependent.
  (4) THE DEFICIT'S ANATOMY (the polarity reading the author demanded): each row is k/7
      truncated, so each LOSES (k/7) of a final unit, all DOWN, one polarity; the
      six losses sum to (1+2+...+6)/7 = 21/7 = 3 EXACTLY. The residue of the whole
      figure is the bare 3-move at the seed. The poles 0/7 and 7/7 are exact and
      lose nothing — the fence, not truncations.
  (5) THE ROUNDING SPLIT IS THE REST-SET: only rows 4, 5, 6 round up (7th digits
      5, 7, 8), taking their last digits 8, 5, 2 -> 9, 6, 3 — the {2,5,8} triangle
      going to the {3,6,9} axis — while {1,4,7} never moves, which is the banked
      "one, four and seven come to rest and cannot be rounded off". Digit sums:
      12 + 15 = 27 (Re), 12 + 18 = 30 (Mi).
"""

from fractions import Fraction as F
from decimal import Decimal, getcontext
from sympy import n_order

getcontext().prec = 60


def _block(depth):
    return sum(F(k * 10 ** depth // 7, 10 ** depth) for k in range(1, 7))


def test_the_rotation_quantum():
    assert n_order(10, 7) == 6                       # six digits is one rotation
    for q, p in [(3, 1), (7, 6), (11, 2), (13, 6), (127, 42)]:
        assert n_order(10, q) == p


def test_the_deficit_is_three_final_units_every_rotation():
    for m in (1, 2, 3, 4):
        d = 6 * m
        assert 3 - _block(d) == F(3, 10 ** d)        # exactly three units of the last place
    assert _block(6) == F(2999997, 10 ** 6)          # the one-rotation value


def test_the_deficit_is_twentyone_sevenths():
    total = F(0)
    for k in range(1, 7):
        loss = F(k, 7) - F(k * 142857, 10 ** 6)
        assert loss == F(k, 7) * F(1, 10 ** 6)       # each row loses k/7 of a unit, DOWN
        total += loss
    assert total == F(21, 7) * F(1, 10 ** 6) == F(3, 10 ** 6)
    assert F(21, 7) == 3                             # the bare 3-move at the seed
    assert F(0, 7) == 0 and F(7, 7) == 1             # the poles lose nothing


def test_the_rounding_split_is_the_rest_set():
    rounds_up = []
    for k in range(1, 7):
        s = str(Decimal(k) / Decimal(7))[2:9]
        if int(s[6]) >= 5:
            rounds_up.append((k, int(s[5]), int(s[5]) + 1))
    assert [r[0] for r in rounds_up] == [4, 5, 6]
    assert [r[1] for r in rounds_up] == [8, 5, 2]    # the {2,5,8} triangle
    assert [r[2] for r in rounds_up] == [9, 6, 3]    # -> the {3,6,9} axis
    assert sum({1, 4, 7}) == 12 and sum({2, 5, 8}) == 15 and sum({3, 6, 9}) == 18
    assert 12 + 15 == 27 and 12 + 18 == 30           # Re -> Mi
