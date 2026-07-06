"""ym_gap.py — Phase C2: the Yang-Mills gap as the first rung above
the forbidden zero. Inside the Scale Theorem boundary throughout: no
magnitude is derived; the gap's EXISTENCE criterion and its MECHANISM
(the clock's finite octave budget) are the claims.

THE CASIMIR THIRDS (exact): SU(N) invariants —
    C_F = (N^2-1)/2N   C_A = N   T_F = 1/2
For the 3-group these ARE the framework's tones:
    C_F(3) = 4/3 (Fa — and it IS the b0 matter coefficient)
    C_A(3) = 3   (the vector)
    C_A - C_F = 5/3 (La — the Casimir gap, same day as THE-FIVE-THIRDS)
    C_A / C_F = 9/4 = (3/2)^2 (Sol squared — Casimir scaling, measured
                               in adjoint string tension / jet quenching)
    C_F(2) = 3/4 and C_F(3) = 4/3 — the two smallest gauge groups carry
    reciprocal Fa-pair Casimirs (product exactly 1)
    gluons = 3^2 - 1 = 8 = the ring (banked structural 9 = dim U(3))
    asymptotic freedom ceiling: b0 > 0  <=>  n_f < 33/2 (= 11*3/2)

THE CRITERION: gapped <=> the carrier is charged (non-abelian, C_A > 0)
<=> the 11/3 gauge term exists <=> b0 > 0 (below the 33/2 ceiling)
<=> the octave budget alpha^-1 * 2pi / (b0 ln 2) is FINITE. Abelian:
C_A = 0, no 11/3 term, b0 < 0 — infinite budget, no landing, gapless.
A2 reading: the uncharged carrier is workless (never reads itself);
the charged carrier must register its own output — self-reading is an
E-face engagement, so every excitation requires at least one carry.

DIMENSIONAL TRANSMUTATION = THE CLOCK: the pure number alpha^-1(mu) is
an octave COUNT; the scale where the count runs out, Lambda =
mu * 2^(-n*), is the gap's home. The ratio 2^(-n*) is dimensionless
(gripped); the GeV value needs the one borrowed ruler (the theorem
CONFIRMED, as banked — not a door).
"""

import math
from fractions import Fraction as F

from rg_octave import b0


def casimir_fundamental(n: int) -> F:
    """C_F = (N^2 - 1) / 2N, exact."""
    return F(n * n - 1, 2 * n)


def casimir_adjoint(n: int) -> int:
    """C_A = N."""
    return n


T_F = F(1, 2)


def casimir_gap(n: int) -> F:
    """C_A - C_F = (N^2 + 1)/2N — for N = 3: 5/3, La."""
    return casimir_adjoint(n) - casimir_fundamental(n)


def casimir_scaling(n: int) -> F:
    """C_A / C_F = 2N^2/(N^2-1) — for N = 3: 9/4 = Sol squared."""
    return F(casimir_adjoint(n), 1) / casimir_fundamental(n)


def b0_from_casimirs(n: int, nf: int) -> F:
    """b0 = (11/3) C_A - (4/3) T_F n_f — the framework thirds are the
    Casimir algebra; must equal rg_octave.b0 for N = 3."""
    return F(11, 3) * casimir_adjoint(n) - F(4, 3) * T_F * nf


def flavor_ceiling(n: int = 3) -> F:
    """b0 > 0  <=>  n_f < 11N/4... for the counting (11 Nc - 2 nf)/3 > 0:
    n_f < 11N/2 — at N = 3 the ceiling is 33/2."""
    return F(11 * n, 2)


def abelian_b0(nf: int) -> F:
    """The abelian side: C_A = 0, no gauge term — matter only, negative
    for any nf >= 1 (the gapless side; QED runs the other way)."""
    return F(11, 3) * 0 - F(4, 3) * T_F * nf


def octave_budget(alpha_inv: float, b0_val: F) -> float:
    """n* = 2 pi alpha^-1 / (b0 ln 2): the octave count from the ruler
    mu down to the landing rung. FINITE iff b0 > 0. Float layer."""
    return 2 * math.pi * alpha_inv / (float(b0_val) * math.log(2))


def landing_scale(mu: float, alpha_inv: float, b0_val: F) -> float:
    """Lambda = mu * 2^(-n*) — the rung where the count runs out.
    One-loop, no thresholds: a ballpark, marked. The RATIO 2^(-n*) is
    the dimensionless content; mu is the borrowed ruler."""
    return mu * 2 ** (-octave_budget(alpha_inv, b0_val))
