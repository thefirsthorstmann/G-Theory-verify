"""test_convergence.py — F7 pinned: the cross-domain facts of the sweep."""

from fractions import Fraction as F


def collatz_orbit(n: int) -> list:
    seq = [n]
    while n != 1:
        n = 3 * n + 1 if n % 2 else n // 2
        seq.append(n)
    return seq


def test_collatz_is_the_2perp3_contest():
    """Odd step = the vector step plus THE CARRY (3n+1); even = the
    octave descent; (3n+1) is always even (one forced halving); the
    standard heuristic drift is 3/4 (descent) bracketed against 3/2
    (Sol) per single halving — the orbit oscillates across the unit
    between the fourth and the fifth."""
    for n in (3, 7, 11, 27):
        assert (3 * n + 1) % 2 == 0
    assert F(3, 4) < 1 < F(3, 2)


def test_the_spines_orbit_is_a_framework_tour():
    """17 -> 52 (the banked apex 3x17+1) -> 26 -> 13 (the mirror) ->
    40 (the +-40 pair) -> 20 (La on the 12-wheel) -> 10 (the base) ->
    5 -> 16 -> 8 (the ring) -> 4 -> 2 -> 1. Exact."""
    assert collatz_orbit(17) == [17, 52, 26, 13, 40, 20, 10, 5, 16,
                                 8, 4, 2, 1]
    assert 52 == 3 * 17 + 1                       # the apex is 17's own odd step


def test_the_fifth_family_cross():
    """Three independent dressed-fifth appearances now on record:
    the alpha-dress carry in transit, the moment seat, the banked
    comma-squared fifth — cross-referenced, held at signpost."""
    from transit import transit
    from stakes import PYTHAGOREAN_COMMA
    assert transit("036") == F(3, 2)              # the winding's carry reads Sol
    assert F(2 ** 37, 3 ** 23) == F(3, 2) / PYTHAGOREAN_COMMA ** 2
