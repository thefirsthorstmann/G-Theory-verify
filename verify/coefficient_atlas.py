"""coefficient_atlas.py — THE COEFFICIENT ATLAS (CC's commission).

THE THESIS: physics' pi-coefficients are PROCESS SIGNATURES, not
furniture. Equality-by-value (the extensional collapse inherited from
analysis) erased their provenance; this atlas restores the
intensional reading: each coefficient rendered with its construction
route and the physical process the route signs. The individual
integrals are textbook; THE OBJECT — the systematic signature table —
is, as far as we know, unbuilt elsewhere (flagged, not boasted).

THE ATLAS:
  2 pi        one closure (the circle's own period)     | hbar = h/2pi
  4 pi        azimuth closure x polar diameter (2pi x 2)| Gauss/Coulomb
  8 pi        DOUBLED flux (the metric's two sheets)    | Einstein 8 pi G
  pi^2 / 6    the integer lattice's second sum, zeta(2) | Basel; Casimir
  16 pi^2     flux SQUARED, (4pi)^2                     | the one-loop factor
  sqrt(pi)    one dimension's share of a 2D closure     | diffusion; Ch IX
  2 pi^2      the 3-sphere's measure (closure in 4D)    | compact volumes
  pi^4 / 15   the fourth lattice sum x 6, thermal modes | blackbody
"""

import math


def polar_diameter() -> float:
    """int_0^pi sin(theta) d(theta) = -(cos pi - cos 0) = 2, exactly:
    the polar half of the solid angle."""
    return -(math.cos(math.pi) - math.cos(0.0))


def solid_angle() -> float:
    """4 pi = (2 pi) x (polar diameter): the route, not a value."""
    return 2 * math.pi * polar_diameter()


def einstein_route() -> float:
    """8 pi = 2 x (4 pi): the doubled flux (g_00 = 1 + 2 phi)."""
    return 2 * solid_angle()


def basel(n_terms: int = 200000) -> float:
    """zeta(2) = sum 1/k^2 -> pi^2/6: the lattice's second sum."""
    return sum(1.0 / k ** 2 for k in range(1, n_terms + 1))


def gauss_integral(steps: int = 400000, span: float = 12.0) -> float:
    """int e^{-x^2} dx = sqrt(pi): one dimension's share of the 2D
    closure (the polar trick squares it to a full circle)."""
    h = 2 * span / steps
    return h * sum(math.exp(-(-span + i * h) ** 2) for i in range(steps + 1))

def loop_factor() -> float:
    """(4 pi)^2 = 16 pi^2: the one-loop momentum closure."""
    return solid_angle() ** 2


def sphere_measure(n: int) -> float:
    """Surface of S^n: 2 pi^{(n+1)/2} / Gamma((n+1)/2); S^3 = 2 pi^2."""
    return 2 * math.pi ** ((n + 1) / 2) / math.gamma((n + 1) / 2)


def blackbody(steps: int = 200000, span: float = 60.0) -> float:
    """int_0^inf x^3/(e^x - 1) dx = pi^4/15: thermal mode counting."""
    h = span / steps
    total = 0.0
    for i in range(1, steps + 1):
        x = i * h
        total += x ** 3 / math.expm1(x)
    return h * total
