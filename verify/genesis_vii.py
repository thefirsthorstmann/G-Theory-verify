"""genesis_vii.py — Chapter VII (The Path to the Present): the claims.

THE BUDGET: the seats Omega_Lambda = 2/3, Omega_dm = 4/15,
Omega_b = 1/15 — denominated in FIFTEENTHS, the first operation's own
internal interval (57 - 42 = 15) — CLOSE TO UNITY EXACTLY:
2/3 + 4/15 + 1/15 = 1. Flatness is not fine-tuned; it is closure.
The dark-matter seat is built from the sevenths:
(1/7 + 3/7) / (15/7) = 4/15.

THE DECELERATION: q0 = Omega_m/2 - Omega_Lambda = 1/6 - 2/3 = -1/2
exactly at the seats.

THE CREST, EXACT (new — the banked ~0.59/~0.26 are closed forms):
acceleration begins where (1+z)^3 = 2 Omega_Lambda/Omega_m = 4, so
    z_accel = 4^(1/3) - 1  (~0.587)
and Lambda-matter equality where (1+z)^3 = 2, so
    z_equal = 2^(1/3) - 1  (~0.260).
THE TURNING POINTS ARE OCTAVE THIRDS: the expansion turned when the
count crossed the cube roots of two and four. The "why now"
coincidence is a forced rung, not an anthropic accident.

THE HONESTY PIN: the baryon cell CLASHES — 1/15 = 6.67% vs the
measured 4.93% (a ~35% discrepancy) — and the suite itself asserts
the clash is real. It stays on the page, as banked.

THE HUBBLE CURIOSITY (parked): 73.0/67.4 = 1.0831 vs 13/12 = 1.0833
— the two instruments' ratio sits on the tridecimal step; noted,
parked, wake condition = the tension survives systematics.
"""

from fractions import Fraction as F

OMEGA_LAMBDA = F(2, 3)
OMEGA_DM = F(4, 15)
OMEGA_B = F(1, 15)
OMEGA_M = OMEGA_DM + OMEGA_B                   # = 1/3

# measured (Planck 2018; memory-flagged for source re-check)
MEAS = {"lambda": 0.6847, "dm": 0.2589, "b": 0.0493}
H0_LOCAL, H0_CMB = 73.04, 67.4


def budget_closes() -> bool:
    return OMEGA_LAMBDA + OMEGA_DM + OMEGA_B == 1


def dm_from_sevenths() -> F:
    return (F(1, 7) + F(3, 7)) / F(15, 7)


def q0_seat() -> F:
    return OMEGA_M / 2 - OMEGA_LAMBDA


def crest() -> tuple:
    """(1+z)^3 at acceleration onset and at equality — exact."""
    accel_cube = 2 * OMEGA_LAMBDA / OMEGA_M    # = 4
    equal_cube = OMEGA_LAMBDA / OMEGA_M        # = 2
    return accel_cube, equal_cube


def crest_redshifts() -> tuple:
    a, e = crest()
    return float(a) ** (1 / 3) - 1, float(e) ** (1 / 3) - 1


def baryon_clash_pct() -> float:
    """The pinned honesty: the seat exceeds the measurement by ~35%."""
    return (float(OMEGA_B) - MEAS["b"]) / MEAS["b"] * 100


def hubble_ratio_vs_13_12() -> float:
    return H0_LOCAL / H0_CMB - float(F(13, 12))
