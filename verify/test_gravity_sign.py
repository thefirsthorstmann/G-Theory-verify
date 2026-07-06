"""test_gravity_sign.py — the forced arithmetic under the gravity-sign reading.

THE CHAIN (arithmetic, pinned here — every step checkable):
  1. Midy: the reptend halves 142|857 pair digit-wise to 9.
  2. The first-half digits are all <= 4.
  3. Therefore the second-half digits are all >= 5 (the 9-complement).
  4. The generation deciders — the digits at positions 4,5,6 (depths
     3,4,5) — ARE the second half "857".
  5. Therefore ALL THREE generations round UP: every excess is POSITIVE.

THE READING (held loose in GRAVITY-REOPENED.md, NOT asserted here):
  mass = rounding-excess (banked mass-is-rounding); gravity couples to
  mass -> one sign only (purely attractive). EM couples to the rotation
  layer (+-18) -> two signs. The sign asymmetry of the two long-range
  forces = Midy's complement structure.
"""

from gtheory import expansion_digits, generation, reptend


def test_midy_halves_pair_to_nine():
    r = reptend(7)
    first, second = r[:3], r[3:]
    assert first == "142" and second == "857"
    assert all(int(a) + int(b) == 9 for a, b in zip(first, second))


def test_first_half_low_forces_second_half_high():
    r = reptend(7)
    assert all(int(d) <= 4 for d in r[:3])       # 1, 4, 2
    assert all(int(d) >= 5 for d in r[3:])       # forced by the complement


def test_generation_deciders_are_the_second_half():
    digs = expansion_digits(1, 7, 6)
    deciders = digs[3:6]                          # depths 3, 4, 5 deciders
    assert deciders == "857" == reptend(7)[3:]


def test_all_generation_excesses_are_positive():
    for depth in (3, 4, 5):
        assert generation(depth)["excess"] > 0    # the existence layer: all +


def test_857_is_prime():
    n = 857                                       # the wrap-half prime (banked)
    assert all(n % d for d in range(2, 30))
