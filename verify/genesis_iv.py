"""genesis_iv.py — Chapter IV (Plasmas): the exact claims.

THE COOLING CLOCK: on discrete terms cooling is octave descent — the
scale-step is the halving, and the RG-per-octave of the companion
program is the thermal history's own clock. The span from the
electroweak scale to the microwave background is ~50 octaves
(comparison layer, marked).

THE HELD CHORD: 63/32 = 2 - 1/32 — one part in sixty-four short of
the octave: the metastable seam. Its gap to closure is 64/63, the
septimal comma (~27.3 cents) — the same comma the program's Higgs
self-coupling construction carries. The plasma epoch is the long
occupancy of this near-closed seam.

THE ELECTROWEAK EPOCH: the two faces' carriers sit one whole tone
apart at the skeleton level — (m_W/m_Z)^2 = (8/9)^2 - 13/1000, i.e.
m_Z/m_W = 9/8 before the dress (the chapter inherits the EW seat and
its PDG-side stake).

RECOMBINATION AS COROLLARY: the universe becomes transparent because
hydrogen is EXACTLY neutral — Chapter III's closure corollary. Light
decouples from matter when matter's committed form has zero residual
charge; transparency is the charge theorem, observed.
"""

import math
from fractions import Fraction as F

from charge_forcing import composites, solve_charges
from ew_seats import COS2_SEAT, SIN2_SKELETON

HELD_CHORD = F(63, 32)
SEPTIMAL_COMMA = F(64, 63)

# comparison layer (marked; memory-flagged constants)
VEV_GEV = 246.0                        # electroweak scale
CMB_EV = 2.348e-4                      # kT of 2.725 K in eV


def held_chord_facts() -> tuple:
    """63/32 = 2 - 1/32; the gap to the octave is the septimal comma."""
    gap = F(2) / HELD_CHORD
    return HELD_CHORD == 2 - F(1, 32), gap == SEPTIMAL_COMMA


def comma_cents() -> float:
    return 1200 * math.log2(float(SEPTIMAL_COMMA))


def cooling_octaves() -> float:
    """Octave count, electroweak scale down to the CMB (float layer)."""
    return math.log2(VEV_GEV * 1e9 / CMB_EV)


def ew_epoch_skeleton() -> bool:
    """The whole-tone skeleton beneath the EW seat (inherited)."""
    return 1 - SIN2_SKELETON == F(8, 9) ** 2


def transparency_is_the_charge_theorem() -> bool:
    """Recombination's corollary: hydrogen exactly neutral."""
    return composites(solve_charges())["hydrogen"] == 0
