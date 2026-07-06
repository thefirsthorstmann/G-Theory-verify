"""test_genesis_ix.py — Chapter IX pinned: diffusion by counting."""

from fractions import Fraction as F

from genesis_ix import (mean_square_displacement, path_count,
                        return_weight_vs_envelope, total_paths)


def test_pascal_counts_every_path():
    """The kernel is exact enumeration: 2^n paths, all counted."""
    for n in (1, 5, 10, 20):
        assert total_paths(n) == 2 ** n
    assert path_count(10, 5) == 252


def test_the_diffusion_law_is_a_counting_identity():
    """Mean-square displacement = n EXACTLY, for every n — Fick's law
    with no randomness anywhere: the dice were never needed."""
    for n in range(1, 40):
        assert mean_square_displacement(n) == n


def test_pi_emerges_as_the_envelope_of_counting():
    """C(2n,n)/4^n -> 1/sqrt(pi n): within 0.5% by n = 100 and
    tightening — the Gaussian conceded as the instrument it is."""
    r100 = return_weight_vs_envelope(100)
    r400 = return_weight_vs_envelope(400)
    assert abs(r100 - 1) < 0.005
    assert abs(r400 - 1) < abs(r100 - 1)          # tightening


def test_the_walk_is_symmetric_and_written():
    """The kernel is symmetric (no drift without cause) and every
    step is a committed entry: C(n,k) = C(n,n-k)."""
    for n in (7, 12, 21):
        assert all(path_count(n, k) == path_count(n, n - k)
                   for k in range(n + 1))
