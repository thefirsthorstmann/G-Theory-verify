"""pi_terms.py — engine for the public paper "pi on Discrete Terms"
(DOI #2 of the series).

Four pinned exhibits, all classical mathematics, assembled:

(1) THE ARCHIMEDES OVERSHOOT ◆: for the inscribed/circumscribed
    polygon bracket I_n < pi < C_n (hexagon-doubling recurrence),
    the midpoint (I_n + C_n)/2 sits ABOVE pi at every stage, and the
    excess-to-deficit ratio (C_n - pi)/(pi - I_n) tends to 2: the
    circumscribed error is asymptotically TWICE the inscribed one.
    Every "average of the classical bounds" overshoots — a theorem
    about brackets, not a revision of pi.

(2) THE REGISTER BRACKET ◆(definition displayed): 22/7 is the best
    upper bound with denominator 7 (the first continued-fraction
    convergent beyond 3); 201/64 is the best lower bound with
    denominator 64 (six binary places). Their midpoint is EXACTLY
    2815/896 (denominator 2^7 x 7), rational and constructible,
    sitting ~47 ppm above pi — the overshoot property inherited.
    The choice of the two registers is a DEFINITION and the paper
    says so; the arithmetic downstream of it is exact.

(3) PI FROM PURE COUNTING ◆: the central binomial C(2n,n)/4^n
    approaches 1/sqrt(pi n): pi emerges as the envelope of fair-toss
    counting, with no circle drawn anywhere (companion to
    genesis_ix.py).

(4) FINITE-PRECISION INDISTINGUISHABILITY ◆: for every precision
    10^-k there is a rational agreeing with pi to that precision
    (exhibited constructively via truncation) — no finite set of
    finite-precision measurements certifies the seated limit.
"""

import math
from fractions import Fraction

PI_60 = Fraction(  # pi to ~60 digits as an exact rational reference
    314159265358979323846264338327950288419716939937510582097494,
    10 ** 59)


def polygon_bracket(doublings: int) -> list:
    """Archimedes from the hexagon: I_6 = 3, C_6 = 2/sqrt(3)*3.
    Recurrence: C_{2n} = harmonic mean(C_n, I_n); I_{2n} =
    geometric mean(I_n, C_{2n}). Returns [(n, I_n, C_n), ...]."""
    n, i_n, c_n = 6, 3.0, 2 * math.sqrt(3)
    out = [(n, i_n, c_n)]
    for _ in range(doublings):
        c_n = 2 * c_n * i_n / (c_n + i_n)
        i_n = math.sqrt(i_n * c_n)
        n *= 2
        out.append((n, i_n, c_n))
    return out


def midpoint_overshoots(doublings: int = 20) -> bool:
    """(I_n + C_n)/2 > pi at every stage."""
    return all((i + c) / 2 > math.pi for _, i, c in polygon_bracket(doublings))


def excess_deficit_ratio(doublings: int = 20) -> float:
    """(C_n - pi)/(pi - I_n) at the deepest stage — tends to 2."""
    _, i_n, c_n = polygon_bracket(doublings)[-1]
    return (c_n - math.pi) / (math.pi - i_n)


def best_bounds() -> tuple:
    """22/7: least q=7 upper bound; 201/64: greatest q=64 lower bound.
    Both FORCED once the denominators are named (floor/ceil of q*pi)."""
    upper = Fraction(math.ceil(Fraction(22, 7) * 0 + PI_60 * 7), 7)   # ceil(7 pi)/7
    lower = Fraction(math.floor(PI_60 * 64), 64)                       # floor(64 pi)/64
    return lower, upper


def rest_pi() -> Fraction:
    """The register-bracket midpoint, exact: 2815/896."""
    lower, upper = best_bounds()
    return (lower + upper) / 2


def rest_pi_overshoot_ppm() -> float:
    """How far above pi the midpoint sits, in parts per million."""
    return float((rest_pi() - PI_60) / PI_60) * 1e6


def counting_envelope(n: int) -> float:
    """(C(2n,n)/4^n)^-2 / n -> pi: pi from fair-toss counting alone."""
    w = math.comb(2 * n, n) / 4 ** n
    return 1 / (w * w * n)


def rational_witness(k: int) -> Fraction:
    """A rational agreeing with pi to 10^-k (constructive truncation):
    finite precision never certifies the seated limit."""
    q = 10 ** k
    r = Fraction(math.floor(PI_60 * q), q)
    assert abs(r - PI_60) < Fraction(1, q)
    return r


def rest_pi_expansion(places: int = 30) -> str:
    """Decimal expansion of 2815/896 by exact long division: the head
    3.1417410 then the pure reptend of 1/7 (714285 repeating) — the
    rest value settles into a six-place cycle where pi never settles."""
    n, d = 2815, 896
    digits = [str(n // d)]
    r = n % d
    frac = []
    for _ in range(places):
        r *= 10
        frac.append(str(r // d))
        r %= d
    return digits[0] + "." + "".join(frac)
