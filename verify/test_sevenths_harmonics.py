"""Pins for THE SEVENTH (sevenths_harmonics.py)."""

from fractions import Fraction as F

from sevenths_harmonics import (REPTEND, rotations, full_period_primes_below,
                                octave_reduce, collapse, PITCH)


def test_one_wheel():
    rots = rotations()
    doubled = REPTEND * 2
    assert all(r in doubled for r in rots)      # every period is a rotation
    assert len(set(rots)) == 6                   # all six distinct


def test_seven_is_least_full_period_prime():
    assert full_period_primes_below(20) == [7, 17, 19]


def test_no_smaller_denominator_gives_six_labels():
    # divisors below 7: terminate, short-period, or repeat under reduction
    for d in range(2, 7):
        classes = {F(k, d) for k in range(1, d)}
        assert len(classes) < 6


def test_the_collapse_do_fa_la():
    reduced, classes = collapse()
    assert set(reduced) == {F(1), F(2, 3), F(5, 6)}   # 1/2 == 1 under octave equivalence: Do
    assert classes == ["Do", "Fa", "La"]
    # the four unvisited positions
    assert not {F(3, 4), F(5, 8)} & set(reduced)   # Sol, Mi never visited


def test_midy():
    assert int(REPTEND[:3]) + int(REPTEND[3:]) == 999
    assert int(REPTEND) * 7 == 999999


def test_transform_octave_realization():
    # the second face: digitwise octave-pair substitution about {1,8}
    sub = {'1': '1', '8': '8', '4': '2', '2': '4', '5': '7', '7': '5'}
    assert ''.join(sub[d] for d in '142857') == '124875'
    assert 2 * 2 % 9 == 4 and 7 * 2 % 9 == 5      # swapped pairs are octave pairs
    assert 1 + 8 == 9                              # the neutral axis is the Midy pair
