"""ew_seats.py — Phase D4: the electroweak seats, anatomized.

THE DECOMPOSITION (exact): the banked construction
    (m_W/m_Z)^2 = 1 - 17/81 - 13/1000
was secretly saying:
    1 - 17/81 = 64/81 = (8/9)^2
so the SKELETON is cos(theta_W) = 8/9 — i.e. m_Z/m_W = 9/8: THE Z SITS
ONE WHOLE TONE ABOVE THE W (the escapement's overshoot, Re; the same
9/8 the 1.001 comma reads in transit). The angle's skeleton is then
    sin^2(theta_W) = 17/81 = (3^4 - 2^6)/3^4
— THE SPINE'S OWN BIRTH IDENTITY: the 17 that appears is the gap that
defines it. And the dress coefficient is THE OTHER GAP PRIME at the
third register: 13 = 2^8 - 3^5, over 10^3. Both banked gap primes,
one construction: seat from the (2^6, 3^4) pair, dress from the
(2^8, 3^5) pair, register width 3.

THE POLARIMETER (floats, marked; measured values memory-sourced and
flagged for re-check): seat = sqrt(62947/81000) = 0.8815461.
    vs PDG-2024 m_W (80.3692, sans CDF): +0.36 cents — SUB-CENT: the
       two-tier law reaches the EW sector;
    vs CDF-II (80.4335): -1.02 cents; the field is split by 1.38
       cents and THE CONSTRUCTION SIDES WITH PDG (as with r_M: a side
       is taken, falsification band pre-registered).
The raw whole tone alone is +14.7 cents from measurement: the 9/8 is
the SKELETON, not the seat; the seat is the dressed construction.
The angle inherits the mass dress amplified by 2cos^2/sin^2 ~ 7.

THE 3/13 DEMOTION: sin^2 = 3/13 matched a SCHEME-DEPENDENT value
(MS-bar-ish); the scheme spread (on-shell vs MS-bar ~ +3.6%) is two
orders above the construction dress. The framework's own scheme is
ON-SHELL — masses are its objects — so the angle cell is the
mass-ratio construction, and 3/13 is superseded. Demoted.
"""

import math
from fractions import Fraction as F

# --- exact layer ------------------------------------------------------------
SIN2_SKELETON = F(17, 81)                 # = (3^4 - 2^6)/3^4
DRESS = F(13, 1000)                       # mirror gap-prime, third register
COS2_SEAT = 1 - SIN2_SKELETON - DRESS     # = 62947/81000


def seat_mw_over_mz() -> float:
    return math.sqrt(float(COS2_SEAT))


# --- comparison layer (floats, marked; memory-sourced, re-check owed) -------
M_Z = 91.1876                             # LEP
M_W_PDG = 80.3692                         # PDG 2024 average (sans CDF-II)
M_W_CDF = 80.4335                         # CDF-II 2022


def cents(ratio: float) -> float:
    return 1200 * math.log2(ratio)


def polarimeter() -> dict:
    s = seat_mw_over_mz()
    return {
        "seat": s,
        "vs_pdg_cents": cents(s / (M_W_PDG / M_Z)),
        "vs_cdf_cents": cents(s / (M_W_CDF / M_Z)),
        "field_split_cents": cents(M_W_CDF / M_W_PDG),
        "raw_tone_cents": cents((M_Z / M_W_PDG) / 1.125),
        "angle_amplification": 2 * float(COS2_SEAT) / (1 - float(COS2_SEAT)),
    }


# --- the dress interrogation (CC, same day) ---------------------------------
SIGMA_W = 0.0133                          # PDG m_W uncertainty (GeV)


def sigma_cents() -> float:
    """One sigma of the W mass, in cents on the ratio."""
    return cents(1 + SIGMA_W / M_Z / (M_W_PDG / M_Z))


RIVAL_DRESS = F(1, 75)                    # the chirality span
RIVAL_COS2 = F(64, 81) - RIVAL_DRESS      # = 1573/2025; 1573 = 11^2 x 13


def rival_seat() -> float:
    """cos(theta_W) = 11 sqrt(13) / 45 — charge-thread, mirror, the 45."""
    return 11 * math.sqrt(13) / 45


def ladder_rungs() -> tuple:
    """|2^a - 3^b| at the near-miss rungs, in rung order:
    (3,2), (5,3), (6,4), (8,5), (11,7). The construction uses the
    tone [rung 1], the 17 [rung 3], the 13 [rung 4 — the limma rung
    256|243]; the field split carries 9 x 139 [rung 5]."""
    return (3 ** 2 - 2 ** 3, 2 ** 5 - 3 ** 3, 3 ** 4 - 2 ** 6,
            2 ** 8 - 3 ** 5, 3 ** 7 - 2 ** 11)
