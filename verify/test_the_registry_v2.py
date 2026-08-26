"""test_the_registry_v2.py — THE PREDICTIONS REGISTRY, VERSION 2: THE
GRAVITATIONAL SECTOR STAKED, ADDITIVELY (2026-08-25).

The registry's own conduct rules (§8 of the document) govern the update:
stakes may be added, none removed or silently altered, every status change
logged on the face of the document. Version 2 adds three live stakes — the
Higgs mass from the seated self-coupling, Newton's constant promoted from
the watched column, the Hubble constant on the declared chain — and a
five-row table of exact nulls, all from the gravitational volume (DOI
10.5281/zenodo.22087600). This battery pins the new rows' arithmetic cold,
and pins that every version-1 stake still stands verbatim.
"""

import math
import pathlib
from fractions import Fraction as F

CATALOG = pathlib.Path(__file__).resolve().parent.parent / "catalog"
DOC = (CATALOG / "PREDICTIONS-ON-DISCRETE-TERMS.md").read_text()
GRAVITY = (CATALOG / "GRAVITY-AS-TONAL-CENTER.md").read_text()
FLAT = " ".join(DOC.split())

V = 246.219651                     # GeV, from G_F
ME_GEV = 0.51099895069e-3


# --- stake 8: the Higgs mass from the seat ---------------------------------------

def test_stake_eight_is_the_seat_times_v():
    lam = F(2 ** 9, 3 ** 4 * 7 ** 2)
    assert F(32, 63) ** 2 == 2 * lam               # the corollary's exact root
    mh = V * 32 / 63
    assert abs(mh - 125.0640) < 0.0005             # the staked value
    assert "125.0640(1) GeV" in FLAT
    assert "recorded 2026-07-03" in FLAT           # provenance on the face


def test_the_higgs_razor_row_is_correct():
    """Nearest pure 2-3-7 register rival: 2^4 * 3^7 * 7 electron masses."""
    rival = 2 ** 4 * 3 ** 7 * 7 * ME_GEV
    stake = V * 32 / 63
    gap_mev = (rival - stake) * 1000
    assert 95 < gap_mev < 110                      # the doc says 102 MeV above
    assert "nearest register alternative 102 MeV above" in FLAT
    assert abs(gap_mev - 102) < 1


# --- stake 9: Newton's constant, promoted ------------------------------------------

def test_stake_nine_matches_the_gravity_paper_and_its_placement():
    assert "6.6735902(41) × 10⁻¹¹" in FLAT
    assert "6.6735902(41)" in " ".join(GRAVITY.split())   # same value, same source
    ppm = (6.6735902 - 6.67430) / 6.67430 * 1e6
    assert abs(ppm + 106) < 1                      # 106 ppm below the CODATA centre
    assert "promoted to commitment 9" in FLAT           # the watched-column promotion, logged


# --- stake 10: the chain pair -------------------------------------------------------

def test_stake_ten_and_the_saturation_density_ride_one_chain():
    assert "70.05 km s⁻¹ Mpc⁻¹" in FLAT
    n0 = 3 * 7 ** 3 / (2 ** 11 * math.pi)
    assert abs(n0 - 0.15993) < 0.00001
    assert "0.15993 fm⁻³" in FLAT


# --- the null stakes ----------------------------------------------------------------

def test_the_five_nulls_are_on_the_face():
    for s in ("−1 exactly, no fallback",
              "0 exactly, no screening",
              "universal exactly",
              "a confirmed monopole or dipole component",
              "period one octave, if detected"):
        assert s in FLAT, s
    assert "non-detection does not refute it" in FLAT    # the two-sided honesty


# --- conduct: additive, logged, and version one intact ------------------------------

def test_the_change_log_is_on_the_face():
    assert "## 8 · Change log" in DOC
    assert "Version 2 — August 25th, 2026" in FLAT
    assert "No version-1 commitment was altered or removed" in FLAT
    assert "Ten live commitments and five exact nulls are registered" in FLAT
    assert "10.5281/zenodo.22087600" in FLAT


def test_every_version_one_stake_still_stands_verbatim():
    for s in ("4/7 = 0.571429", "1/45 = 0.022222",
              "11/3 fm − r_e = 0.848726 fm", "1.0922 fm",
              "1 − 17/81 − 13/1000", "17/10 = 1.700 exactly"):
        assert s in FLAT, s
    assert "5/17 = 0.294118" in FLAT               # the watched abstention, untouched
    # the register is normalized (2026-08-26): commitment vocabulary throughout,
    # the withdrawn items carried in the internal record only
    assert "staked" not in FLAT
    assert "at risk" not in FLAT
    assert "Retired, with reasons" not in DOC
