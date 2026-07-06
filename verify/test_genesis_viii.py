"""test_genesis_viii.py — Chapter VIII pinned: the piano, the port, the wall."""

from genesis_viii import (duality_is_euclid, factorial_wall,
                          port_discards_exactly_half, surviving_modes)


def test_the_node_touch_selection_rule():
    """Touch at 1/2: the even harmonics survive. Touch at 1/3: the
    multiples of three. Collapse is arithmetic filtering."""
    assert surviving_modes(2, 12) == [2, 4, 6, 8, 10, 12]
    assert surviving_modes(3, 12) == [3, 6, 9, 12]
    assert surviving_modes(7, 24) == [7, 14, 21]      # the seed's family


def test_the_port_discards_exactly_half():
    """The Born reading: n of 2n integers survive — the pinned theorem."""
    assert port_discards_exactly_half()


def test_the_duality_is_euclids_identity():
    """P^2 + V^2 = 1 exactly, across the amplitude grid."""
    assert duality_is_euclid()


def test_the_factorial_wall():
    """Coherence across N constituents scales as N!: twenty already
    exceed 10^18 — why dust is classical."""
    assert factorial_wall(20) > 10 ** 18
    assert factorial_wall(10) == 3628800              # a mere ten: 3.6 million
