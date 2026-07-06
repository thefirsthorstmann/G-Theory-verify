"""Pins for THE RULER-RATIO LADDER (bridge.py) — the bridge to
magnitudes. Float layer 🟡 (memory-sourced CODATA 2018); identities
pinned as ratios at 1e-6 bands."""

import math

from bridge import (ALPHA, ruler_web, rydberg_over_compton,
                    bohr_times_rydberg, hartree_over_rest_energy,
                    si_ledger, SI_FIXED)


def test_rydberg_compton_link():
    # R_inf / (m_e c / h) = alpha^2 / 2 — the first rung
    assert math.isclose(rydberg_over_compton(), ALPHA ** 2 / 2,
                        rel_tol=1e-6)


def test_bohr_rydberg_link():
    # a_0 * R_inf = alpha / 4pi — the flux-closure rung
    assert math.isclose(bohr_times_rydberg(), ALPHA / (4 * math.pi),
                        rel_tol=1e-6)


def test_hartree_link():
    # E_h = alpha^2 m_e c^2 — the chemistry ruler
    assert math.isclose(hartree_over_rest_energy(), ALPHA ** 2,
                        rel_tol=1e-6)


def test_web_all_links_close():
    for name, (measured, forced) in ruler_web().items():
        assert math.isclose(measured, forced, rel_tol=1e-6), name


def test_si_ledger_closure():
    # seven units, seven fixed exchange rates; every unit's recipe
    # draws only from the fixed set; the second is pure count
    ledger = si_ledger()
    assert len(ledger) == 7 and len(SI_FIXED) == 7
    for unit, (_, rates) in ledger.items():
        assert all(r in SI_FIXED for r in rates), unit
    assert ledger["second"][1] == ("delta_nu_Cs",)
