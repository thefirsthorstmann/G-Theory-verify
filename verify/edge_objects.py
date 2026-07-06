"""edge_objects.py — pins for ZERO AND INFINITY ON DISCRETE TERMS.

(1) THE FLOOR IS A THEOREM IN Z: halving terminates for every nonzero
    integer (finite 2-adic valuation) — no infinite descent to zero
    exists inside the integers.
(2) THE ROOT SEATS THE DOUBLING INFINITY: under octave equivalence the
    entire two-sided ladder {2^n} is one class — the root.
(3) THE CARDIOID IS THE SHAPE OF THE EDGE: the envelope of the chord
    family joining angle t to 2t on the circle is a cardioid — the
    continuum's image of discrete doubling, computed numerically here
    by intersecting neighboring chords and testing the polar form
    r/(1 + cos phi) = const about the cusp axis.
"""

import math
from fractions import Fraction


def halving_depth(n: int) -> int:
    """2-adic valuation: steps of halving before the odd core."""
    d = 0
    while n % 2 == 0:
        n //= 2
        d += 1
    return d


def octave_class(x: Fraction) -> Fraction:
    while x > 1:
        x /= 2
    while x <= Fraction(1, 2):
        x *= 2
    return x


def chord_envelope_point(t: float, eps: float = 1e-6):
    """Intersection of the chords (t -> 2t) and (t+eps -> 2t+2eps):
    a point of the envelope of the doubling-chord family."""
    def line(a):
        x1, y1 = math.cos(a), math.sin(a)
        x2, y2 = math.cos(2 * a), math.sin(2 * a)
        # line coefficients: A x + B y = C
        A, B = y2 - y1, x1 - x2
        C = A * x1 + B * y1
        return A, B, C
    A1, B1, C1 = line(t)
    A2, B2, C2 = line(t + eps)
    det = A1 * B2 - A2 * B1
    return ((C1 * B2 - C2 * B1) / det, (A1 * C2 - A2 * C1) / det)


def cardioid_constancy(samples: int = 60):
    """Max relative spread of r/(1+cos phi) about the fitted cusp center
    (2/3, 0) over the envelope — near zero iff the envelope is the
    cardioid r = k (1 + cos phi)."""
    cx = -1.0 / 3.0                       # the cusp axis point: minus one third
    vals = []
    for i in range(1, samples):
        t = 0.25 + (2 * math.pi - 0.5) * i / samples
        x, y = chord_envelope_point(t)
        r = math.hypot(x - cx, y)
        phi = math.atan2(y, x - cx)
        d = 1 + math.cos(phi)
        if d > 0.2:
            vals.append(r / d)
    m = sum(vals) / len(vals)
    return max(abs(v - m) / m for v in vals), m
