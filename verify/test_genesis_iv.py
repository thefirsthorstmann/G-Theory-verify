"""test_genesis_iv.py — Chapter IV pinned: the seam, the span, the epoch."""

from fractions import Fraction as F

from genesis_iv import (comma_cents, cooling_octaves, ew_epoch_skeleton,
                        held_chord_facts, transparency_is_the_charge_theorem)


def test_the_held_chord_and_its_comma():
    """63/32 = 2 - 1/32; gap to the octave = 64/63 (~27.3 cents) —
    the septimal comma the Higgs construction carries."""
    exact, gap_is_comma = held_chord_facts()
    assert exact and gap_is_comma
    assert 27.0 < comma_cents() < 27.5


def test_the_cooling_span():
    """Electroweak scale to CMB: ~50 octaves (comparison layer)."""
    assert 49.0 < cooling_octaves() < 51.0


def test_the_electroweak_epoch_skeleton():
    """One whole tone between the faces' carriers, before the dress."""
    assert ew_epoch_skeleton()


def test_transparency_is_the_charge_theorem():
    """The universe goes transparent because hydrogen closes exactly."""
    assert transparency_is_the_charge_theorem()
