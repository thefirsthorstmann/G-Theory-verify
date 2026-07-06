"""genesis_x.py — Chapter X (Relativity and the SM): the exact claims.

THE CONDITIONAL LORENTZ LEMMA. Declare the premise openly: the
operation budget of a moving system partitions QUADRATICALLY between
translation and internal evolution (the same squaring as the Born
port — the program's one squaring, everywhere). Then with beta the
translational fraction, the internal rate is

    rate = sqrt(1 - beta^2)

— the Lorentz factor, from budget accounting. The premise is declared,
not derived: it is the honesty chapter's named conditional.

THE TRIPLE LATTICE (exact frames): the dilation is EXACT RATIONAL
ARITHMETIC precisely on the Pythagorean triples —
    beta = 3/5  -> rate = 4/5
    beta = 5/13 -> rate = 12/13
    beta = 8/17 -> rate = 15/17
— the same Euclid identity (a^2-b^2)^2 + (2ab)^2 = (a^2+b^2)^2 that
carries the program's two-slit duality. The frames where the count
closes exactly are the triple frames.

THE SPEED LIMIT, STRUCTURAL: motion is re-addressing, one address
step per tick maximum — nothing outruns the count. The DOUBLE-COVER
SHAPE: the ring's full return at 8 with the antipode at 4 (the Midy
half-shift) is the spinor's structural seat: position restored at the
half, identity only at the whole.

THE REFUSAL: the numerical value of c (299,792,458 m/s) is EXACT BY
DEFINITION of the metre (1983) — a fact about the ruler, not about
light — and the construction refuses it on principle (the boundary).
Internally, the rest form 3 x (10^8 - 1) = 299,999,997 factors as
3^3 x 11 x 73 x 101 x 137 (noted, internal grade).
"""

import math
from fractions import Fraction as F


def internal_rate(beta: F):
    """sqrt(1 - beta^2); exact Fraction when (num, den) is a triple leg."""
    val = 1 - F(beta) ** 2
    root_num = math.isqrt(val.numerator)
    root_den = math.isqrt(val.denominator)
    if root_num ** 2 == val.numerator and root_den ** 2 == val.denominator:
        return F(root_num, root_den)
    return math.sqrt(float(val))


def triple_frames() -> list:
    """The exact-arithmetic frames: (beta, rate) on the triple lattice."""
    return [(F(3, 5), internal_rate(F(3, 5))),
            (F(5, 13), internal_rate(F(5, 13))),
            (F(8, 17), internal_rate(F(8, 17))),
            (F(20, 29), internal_rate(F(20, 29)))]


def c_rest_form() -> dict:
    n = 3 * (10 ** 8 - 1)
    from gtheory import factorize
    return {"value": n, "factors": factorize(n)}


def massless_dispersion_error(k: float) -> float:
    """THE ANSWER (X open problem #2, and the LIV watch's first datum).
    The unit-ratio lattice wave recurrence has dispersion
    cos(omega) = cos(k): the massless mode propagates at EXACTLY c
    for ALL k to the zone edge — zero lattice dispersion, zero LIV,
    in 1+1D. (The 3+1D off-axis case is the named remaining open.)"""
    import math
    return math.acos(math.cos(k)) - k


def massive_dispersion(k: float, mu: float) -> tuple:
    """The discrete Klein-Gordon dispersion, EXACT in the sine domain:
    4 sin^2(w/2) = 4 sin^2(k/2) + mu^2 — Pythagoras, because the wave
    operator is SECOND-ORDER: the port's square. Returns (omega,
    residual, beta = k/w, rate = mu/w, gamma_check = w/mu)."""
    import math
    w = 2 * math.asin(math.sqrt(math.sin(k / 2) ** 2 + (mu / 2) ** 2))
    resid = 4 * math.sin(w / 2) ** 2 - 4 * math.sin(k / 2) ** 2 - mu ** 2
    return w, resid, k / w, mu / w, w / mu


def double_cover_shape() -> bool:
    """The ring returns at 8; the antipode (Midy half-shift) at 4:
    position at the half, identity at the whole."""
    from polar_wave import tick
    state = [(1, k) for k in range(8)]
    s = state
    for _ in range(8):
        s = tick(s)
    full_return = s == state
    half = state
    for _ in range(4):
        half = tick(half)
    half_differs = half != state
    return full_return and half_differs
