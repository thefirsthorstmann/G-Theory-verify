"""test_genesis_vi.py — Chapter VI pinned: the lattice in the sky."""

from fractions import Fraction as F

from genesis_vi import (KIRKWOOD_MEASURED, collapse_is_budgeted,
                        kirkwood_radius, laplace_relation,
                        neptune_pluto_dress_pct)


def test_the_laplace_chain_is_exact_in_the_sky():
    """n1 - 3 n2 + 2 n3 = 0 measured to ~1e-4 deg/day — parts in ten
    million of the motions: the octave chain 1:2:4, librating."""
    assert abs(laplace_relation()) < 1e-3


def test_neptune_pluto_sits_on_the_fifth():
    """The 3:2 seat; measured dress well under one percent."""
    assert abs(neptune_pluto_dress_pct()) < 0.5


def test_the_kirkwood_clearings_land_on_keplers_map():
    """The exact ratios 3:1, 5:2, 7:3, 2:1 map to the measured gap
    radii within a percent — the lattice clearing its seats."""
    for ratio, measured in KIRKWOOD_MEASURED.items():
        assert abs(kirkwood_radius(ratio) - measured) / measured < 0.01


def test_collapse_is_budgeted():
    """The universal form bars the attained singularity: the free-fall
    octave schedule crosses the ML floor at finite depth."""
    assert collapse_is_budgeted()
