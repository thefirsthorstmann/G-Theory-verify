"""genesis_ii.py — Chapter II (The Dipole): the exact claims.

THE FIRST FORM THAT POINTS. The general first-order directivity
pattern is D(theta) = a + b cos(theta) (the standard omni-to-dipole
family of acoustics and antenna theory). Null structure, exact:

    a > b : no null      (blurred omni: no direction distinguished)
    a = b : ONE null     (the CARDIOID — the unique single-null member)
    a < b : two nulls    (the figure-eight side: an axis, not a direction)

Pointing requires a null; distinguishing ONE direction requires
exactly one. THE CARDIOID IS THE LEAST STRUCTURE THAT POINTS —
direction is born at equal mixture of the first two multipoles.

THE LADDER AND THE SQUARE. At order m the equal mix 1 + cos(m theta)
has exactly m nulls (the m-cusp forms: cardioid m = 1, the two-cusp
class m = 2, ...). And at m = 2 the pattern is IDENTICALLY the square
of the dipole term:  1 + cos(2 theta) = 2 cos^2(theta).
The quadrupole face is the dipole face squared — the structure the
amplitudes program found from the other side (gravity = gauge^2,
the BCJ double copy), and the GEM factor 4 = 2^2.

THE RADIATION LADDER. Charge conservation (the net-0 ledger of the
first operation) forbids monopole radiation of the charge face;
momentum conservation plus equivalence forbids dipole radiation of
the mass face: the first lawful radiating multipole is l = 1 for
charge and l = 2 for mass — first-rung logic, one rung apart.
"""

from fractions import Fraction as F


def null_count(a: F, b: F, m: int = 1) -> int:
    """Zeros of a + b cos(m theta) on [0, 2pi), a, b >= 0, exact.
    cos(m theta) = -a/b needs a <= b; equality gives m solutions
    (the antipodes), strict inequality two per cos-period: 2m."""
    a, b = F(a), F(b)
    if b == 0 or a > b:
        return 0
    if a == b:
        return m
    return 2 * m


def square_identity(samples: int = 360) -> bool:
    """1 + cos(2t) == 2 cos(t)^2 — the double-angle fact, checked on a
    dense grid (the algebraic identity: cos 2t = 2 cos^2 t - 1)."""
    import math
    return all(abs((1 + math.cos(2 * t)) - 2 * math.cos(t) ** 2) < 1e-12
               for t in (2 * math.pi * k / samples for k in range(samples)))


def cusp_ladder(m_max: int = 5) -> list:
    """Null counts of the equal-mix family: m nulls at order m."""
    return [null_count(1, 1, m) for m in range(1, m_max + 1)]


def gem_factor() -> int:
    """The gravito-electromagnetic factor: 4 = 2^2 — the square."""
    return 2 ** 2
