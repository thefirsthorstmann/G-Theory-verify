"""lattice_density.py — F1: MECHANIZED SKEPTICISM as an engine primitive.

The survey's first improvement: the look-elsewhere justification must scale
with the toolkit. This module makes rival-counting automatic — every
future seat claim gets a density column the way every arithmetic
claim gets a test.

  nearest_rival(x, qmax)   the closest distinct rational at height <= qmax
  rivals_in(x, w, qmax)    every rational inside the window (the crowd)
  farey_expected(w, qmax)  the expected crowd size (3/pi^2 density law)
  uniqueness_sigma(x,qmax) the measurement sigma at which x becomes the
                           UNIQUE lattice point in its +-2 sigma band
                           (= half the distance to the nearest rival)

Validation anchor: the g_A scan (2026-07-03) — 33 rivals in +-1 sigma
at q <= 200 around 1.2754, Farey-predicted 31.6 — reproduces exactly.
"""

import math
from fractions import Fraction as F


def nearest_rival(x: F, qmax: int):
    """Closest rational != x with denominator <= qmax. Exact."""
    best, bd = None, None
    for q in range(1, qmax + 1):
        base = round(float(x) * q)
        for p in (base - 1, base, base + 1):
            r = F(p, q)
            if r == x:
                continue
            d = abs(r - x)
            if bd is None or d < bd:
                best, bd = r, d
    return best, bd


def rivals_in(x: float, halfwidth: float, qmax: int) -> list:
    """Every distinct rational with q <= qmax inside +-halfwidth."""
    out = set()
    for q in range(1, qmax + 1):
        base = round(x * q)
        for p in (base - 1, base, base + 1):
            if abs(p / q - x) < halfwidth:
                out.add(F(p, q))
    return sorted(out)


def farey_expected(width: float, qmax: int) -> float:
    """Expected count of distinct rationals (q <= qmax) in a window of
    the given full width: width * (3/pi^2) * qmax^2."""
    return width * (3 / math.pi ** 2) * qmax ** 2


def uniqueness_sigma(x: F, qmax: int) -> float:
    """The sigma at which x is the unique lattice point in +-2 sigma."""
    _, d = nearest_rival(x, qmax)
    return float(d) / 2
