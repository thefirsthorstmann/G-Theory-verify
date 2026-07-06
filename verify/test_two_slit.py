"""test_two_slit.py — the polar two-slit's forced spine, pinned."""

from fractions import Fraction as F

from two_slit import (duality_sum, intensity8, predictability, triple,
                      visibility, which_path_rounding)


def test_duality_is_the_pythagorean_identity():
    """P^2 + V^2 = 1 EXACTLY for every integer amplitude pair —
    (a^2-b^2)^2 + (2ab)^2 = (a^2+b^2)^2, Euclid's triple identity."""
    for a in range(1, 12):
        for b in range(1, 12):
            assert duality_sum(a, b) == 1


def test_the_345_triangle_is_the_two_to_one_slit():
    assert triple(2, 1) == (3, 4, 5)
    assert predictability(2, 1) == F(3, 5)
    assert visibility(2, 1) == F(4, 5)


def test_equal_slits_pure_wave():
    assert visibility(1, 1) == 1 and predictability(1, 1) == 0


def test_fringe_ladder_is_quantized():
    """Octave ring: exactly five intensity levels for unit amplitudes."""
    levels = {intensity8(1, 1, d) for d in range(8)}
    assert levels == {(4, 0), (2, 1), (2, 0), (2, -1), (0, 0)}
    # antipodal screen positions pair to twice the mean intensity:
    for d in range(8):
        a1, b1 = intensity8(1, 1, d)
        a2, b2 = intensity8(1, 1, d + 4)
        assert (a1 + a2, b1 + b2) == (4, 0)


def test_which_path_rounding_kills_the_fringes():
    """Reading the node = rounding its phase: the screen goes flat —
    the discarded half (the phase, the M-face) WAS the fringe."""
    assert which_path_rounding(1, 1) == 2          # flat, no d anywhere
    varying = {intensity8(1, 1, d) for d in range(8)}
    assert len(varying) > 1                        # fringes existed before
