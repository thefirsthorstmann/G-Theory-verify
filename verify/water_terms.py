"""water_terms.py — pins for WATER ON DISCRETE TERMS.

(1) THE THIRD IN THE BOND ANGLE: the tetrahedral angle satisfies
    cos(theta) = -1/3 EXACTLY (rational, from the tetrahedron's own
    coordinates) — the geometry of 4-coordination is seated on a third.
(2) THE SAME THIRD IN THE STACKING: ideal tetrahedral (wurtzite-type)
    stacking has c/a = sqrt(8/3) — ice Ih's oxygen frame inherits the
    identical -1/3.
(3) WATER ANSWERS AN OCTAVE BELOW: the parametric (Faraday) instability
    responds at HALF the drive frequency — pinned by integrating the
    Mathieu oscillator: principal resonance at drive = 2*natural
    (response f/2), no growth at drive = natural.
"""

import math
from fractions import Fraction


def tetrahedral_cos() -> Fraction:
    """Exact: unit tetrahedron vertices (1,1,1),(1,-1,-1),(-1,1,-1),
    (-1,-1,1); cos between any two bond directions = -1/3."""
    a = (1, 1, 1)
    b = (1, -1, -1)
    dot = sum(x * y for x, y in zip(a, b))
    norm2 = sum(x * x for x in a)
    return Fraction(dot, norm2)


def ideal_ca_squared() -> Fraction:
    """Ideal tetrahedral stacking: (c/a)^2 = 8/3, exactly."""
    return Fraction(8, 3)


def mathieu_growth(drive_ratio: float, eps: float = 0.3,
                   periods: int = 40, steps: int = 4000) -> float:
    """Integrate x'' + (1 + eps*cos(w t)) x = 0 with w = drive_ratio
    (natural frequency 1). Returns log of amplitude gain — positive
    growth iff parametrically resonant."""
    w = drive_ratio
    T = 2 * math.pi * periods
    h = T / steps
    x, v = 1e-3, 0.0
    peak = abs(x)
    for i in range(steps):
        t = i * h
        def acc(x_, t_):
            return -(1 + eps * math.cos(w * t_)) * x_
        k1v = acc(x, t);            k1x = v
        k2v = acc(x + h/2*k1x, t + h/2); k2x = v + h/2*k1v
        k3v = acc(x + h/2*k2x, t + h/2); k3x = v + h/2*k2v
        k4v = acc(x + h*k3x, t + h);     k4x = v + h*k3v
        x += h/6*(k1x + 2*k2x + 2*k3x + k4x)
        v += h/6*(k1v + 2*k2v + 2*k3v + k4v)
        peak = max(peak, abs(x))
    return math.log(peak / 1e-3)
