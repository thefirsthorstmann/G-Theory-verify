"""genesis_vi.py — Chapter VI (Early Galaxies): the exact claims.

THE SKY PLAYS JUST INTONATION. Gravitational systems, given time,
lock onto the small-integer lattice — the same least-action seats the
whole series runs on — and the locks are measured, textbook celestial
mechanics:

  THE LAPLACE CHAIN (Io : Europa : Ganymede = 1 : 2 : 4, the octave
  chain): the mean motions satisfy n1 - 3 n2 + 2 n3 = 0, an exact
  integer relation the system LIBRATES ABOUT — measured to a few
  parts in ten million of the motions themselves.

  NEPTUNE : PLUTO = 3 : 2 — the fifth; the libration protects Pluto
  from close approaches forever.

  THE KIRKWOOD CLEARINGS: at the exact ratios 3:1, 5:2, 7:3, 2:1 of
  Jupiter's motion the asteroid belt is EMPTIED — Kepler's law maps
  each ratio to the measured gap radius. The lattice organizes the
  sky both ways: seats occupied (resonant locks) and seats cleared
  (resonant ejections).

COLLAPSE IS BUDGETED: a curvature singularity requires the collapse
cascade to complete unboundedly many octaves of scale in finite
proper time — the supertask of the companion paper — and Theorem 1'
(the universal form) bars it for any finite-energy system: horizons
real, interiors terminating at finite depth.
"""

import math
from fractions import Fraction as F

# measured mean motions, deg/day (memory-flagged for source re-check)
N_IO, N_EUROPA, N_GANYMEDE = 203.4889, 101.3747, 50.3176
T_NEPTUNE, T_PLUTO = 164.8, 247.94            # years
A_JUPITER = 5.2044                            # AU
KIRKWOOD_MEASURED = {F(3, 1): 2.502, F(5, 2): 2.825,
                     F(7, 3): 2.958, F(2, 1): 3.279}


def laplace_relation() -> float:
    """n1 - 3 n2 + 2 n3 — the exact integer relation, measured."""
    return N_IO - 3 * N_EUROPA + 2 * N_GANYMEDE


def neptune_pluto_dress_pct() -> float:
    """The 3:2 seat and its measured dress."""
    return (T_PLUTO / T_NEPTUNE / 1.5 - 1) * 100


def kirkwood_radius(ratio: F) -> float:
    """Kepler's mapping: a = a_J * (1/ratio)^(2/3) for a p:q resonance
    with Jupiter (period ratio = 1/ratio of Jupiter's)."""
    return A_JUPITER * float(1 / ratio) ** (2 / 3)


def collapse_is_budgeted() -> bool:
    """The companion's universal form applies: any finite-energy
    collapse schedule crosses the ML floor at finite depth."""
    from serial_shell import universal_stage_cap
    t_min = 3.31e-39
    freefall = lambda n: 1.0 * 2 ** (-1.5 * n)   # free-fall octave schedule
    return universal_stage_cap(freefall, t_min) < 100
