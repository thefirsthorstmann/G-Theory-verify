"""Pins for "Schrodinger's Piano" (piano_terms.py)."""

from piano_terms import (duffing_frequency, rest_pitch,
                         dipole_radius_reading, TRUE_DIPOLE_SLOPE,
                         ALPHA_INV_ZERO_Q, ALPHA_INV_AT_Z)


def test_struck_tone_is_sharp():
    # the sounded frequency exceeds the rest pitch at every amplitude
    f0 = rest_pitch()
    f_loud = duffing_frequency(0.5)
    f_mid = duffing_frequency(0.25)
    f_soft = duffing_frequency(0.05)
    assert f_loud > f_mid > f_soft > f0
    # and settles to the rest pitch only as the strike vanishes
    assert (f_loud - f0) / f0 > 0.02          # a loud strike is audibly sharp
    assert (f_soft - f0) / f0 < 0.0005        # a gentle one nearly silent-true
    # the rest tone is a limit, not a sounding: even the gentlest
    # strike leaves the reading above rest
    assert f_soft > f0


def test_harder_probe_larger_reading():
    # the coupling's measured running: the field-theory sharp tone
    # (float layer; scheme band generous)
    assert ALPHA_INV_ZERO_Q == 137.036
    assert 127.0 < ALPHA_INV_AT_Z < 129.5
    assert ALPHA_INV_AT_Z < ALPHA_INV_ZERO_Q   # harder probe -> larger coupling


def test_radius_reached_only_by_calculation():
    # every finite-Q^2 reading undershoots the defined value and rises
    # toward it monotonically as the probe softens
    readings = [dipole_radius_reading(x) for x in (0.5, 0.2, 0.1, 0.01, 0.001)]
    assert all(r < TRUE_DIPOLE_SLOPE for r in readings)
    assert readings == sorted(readings)               # softer probe, higher reading
    assert TRUE_DIPOLE_SLOPE - readings[-1] < 0.02    # the limit is the definition
    # the rest value sits above every reading — reached by extrapolation
    assert dipole_radius_reading(0) == TRUE_DIPOLE_SLOPE
