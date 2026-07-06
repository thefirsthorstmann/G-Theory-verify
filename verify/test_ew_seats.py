"""test_ew_seats.py — Phase D4 pinned: the whole-tone anatomy + polarimeter."""

from fractions import Fraction as F

from ew_seats import (COS2_SEAT, DRESS, SIN2_SKELETON, polarimeter,
                      seat_mw_over_mz)


def test_the_skeleton_is_the_whole_tone():
    """1 - 17/81 = (8/9)^2: the Z sits one whole tone above the W."""
    assert 1 - SIN2_SKELETON == F(64, 81) == F(8, 9) ** 2
    assert F(9, 8) == 1 / F(8, 9)                 # the overshoot, Re


def test_the_spines_birth_identity():
    """sin^2 skeleton = (3^4 - 2^6)/3^4 — the 17 IS its defining gap."""
    assert SIN2_SKELETON == F(3 ** 4 - 2 ** 6, 3 ** 4)
    assert 17 == 3 ** 4 - 2 ** 6


def test_both_gap_primes_in_one_construction():
    """Seat pair (2^6, 3^4) -> 17; dress coefficient 13 = 2^8 - 3^5,
    at the third register (10^3)."""
    assert DRESS == F(2 ** 8 - 3 ** 5, 10 ** 3)
    assert COS2_SEAT == F(62947, 81000)


def test_the_polarimeter_columns():
    """Floats, marked (measured values memory-flagged): sub-cent vs
    PDG; ~1 cent vs CDF; the construction takes the PDG side."""
    p = polarimeter()
    assert abs(p["vs_pdg_cents"]) < 0.5           # SUB-CENT: two-tier holds
    assert -1.2 < p["vs_cdf_cents"] < -0.8
    assert 1.2 < p["field_split_cents"] < 1.6
    assert abs(p["vs_pdg_cents"]) < abs(p["vs_cdf_cents"])   # side: PDG


def test_the_skeleton_is_not_the_seat():
    """Honesty pin: the raw 9/8 sits ~15 cents out — the whole tone is
    the skeleton; the dressed construction is the seat. The angle
    inherits the mass dress amplified ~x7."""
    p = polarimeter()
    assert 13 < p["raw_tone_cents"] < 17
    assert 6.5 < p["angle_amplification"] < 7.5


def test_the_residual_is_statistically_zero():
    """CC's interrogation (a): the +0.36c residual is ~1.3 sigma of the
    W-mass meter — consistent with ZERO; the construction may be exact."""
    from ew_seats import sigma_cents
    s = sigma_cents()
    assert 0.25 < s < 0.32
    assert abs(polarimeter()["vs_pdg_cents"]) / s < 1.5


def test_the_rival_seat_identities():
    """CC's interrogation (d): x = 1/75 (the chirality span) gives
    cos^2 = 1573/2025 with 1573 = 11^2 x 13 and 2025 = 45^2 —
    m_W/m_Z = 11 sqrt(13)/45. Lands within 0.05 cents of PDG central;
    the two rivals differ by ~0.37 cents (~17 MeV): adjudicable."""
    from ew_seats import (M_W_PDG, M_Z, RIVAL_COS2, cents, rival_seat,
                          seat_mw_over_mz)
    assert RIVAL_COS2 == F(1573, 2025)
    assert 1573 == 11 ** 2 * 13 and 2025 == 45 ** 2
    assert abs(cents(rival_seat() / (M_W_PDG / M_Z))) < 0.05
    gap = abs(cents(rival_seat() / seat_mw_over_mz()))
    assert 0.3 < gap < 0.45


def test_the_ladder_and_the_split():
    """CC's interrogation (c, e): the near-miss rung gaps are
    1, 5, 17, 13, 139; the construction uses rungs 1-17-13 and the
    PDG-CDF split ratio is 1.0008 (= 1251/1250, carrying 9 x 139 —
    the NEXT rung) whose transit read completes the family
    1.008 -> 2, 1.001 -> 9/8, 1.0008 -> 3/2."""
    from ew_seats import M_W_CDF, M_W_PDG, ladder_rungs
    from transit import transit
    assert ladder_rungs() == (1, 5, 17, 13, 139)
    assert 1.00079 < M_W_CDF / M_W_PDG < 1.00081
    assert 1251 == 9 * 139 and F(1251, 1250) == F(10008, 10000)
    assert 1 + transit("0008") == F(3, 2)
