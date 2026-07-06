"""Pins for THE TICK ITSELF (caesium_tick.py). Float layer — bands
sized to survive memory-sourced late-digit drift."""

import math

from caesium_tick import (hydrogen_21cm, schwinger_dress, NU_H,
                          atomic_factor, fermi_segre_estimate, manifest)


def test_hydrogen_rung_56ppm():
    # the closed-form skeleton lands within 1e-4 of the measured line;
    # the actual residue is +56 ppm (proton structure, named)
    resid = hydrogen_21cm() / NU_H - 1
    assert abs(resid) < 1e-4
    assert 4e-5 < resid < 7e-5          # the residue's sign and size


def test_dress_is_one_closure():
    # g_e/2 - 1 = alpha/2pi to within the known alpha^2 term
    excess, schwinger = schwinger_dress()
    assert abs(excess - schwinger) < 2e-6


def test_atomic_factor_extracted():
    # A_Cs = 12.230 — a ratio of measured quantities, displayed
    assert math.isclose(atomic_factor(), 12.2298, rel_tol=1e-3)


def test_fermi_segre_ballpark():
    # the semi-empirical estimate lands within 15% of the extraction
    est, ext = fermi_segre_estimate(), atomic_factor()
    assert abs(est / ext - 1) < 0.15


def test_manifest_partition():
    m = manifest()
    assert set(m) == {"seated", "composite", "convention"}
    assert len(m["seated"]) == 5 and len(m["composite"]) == 3
    assert "9,192,631,770" in m["convention"]
