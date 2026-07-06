"""kolmogorov.py — Phase C1: the -5/3, tested with the framework's kit.

THE SKELETON (exact): in the inertial range the spectrum depends only on
the cascade rate eps and the scale k (K41's hypothesis). Dimensions:
    [E(k)] = L^3 T^-2 ,  [eps] = L^2 T^-3 ,  [k] = L^-1
Closure of E = C eps^a k^b forces the linear system
    T:  3a = 2            <- THE INCOMMENSURABILITY EQUATION
    L:  2a - b = 3
whose exact solution is a = 2/3 and b = (2^2 - 3^2)/3 = -5/3:
BOTH EXPONENTS ARE SEED ARITHMETIC — a is the bare seed ratio, b is the
seed's SQUARE-GAP over the vector. And 5 = 3^2 - 2^2 joins the gap-prime
family (1 = 3^2-2^3, 5 = 3^2-2^2, 13 = 2^8-3^5, 17 = 3^4-2^6).

THE FRAMEWORK PREMISES that ground K41's hypothesis (each banked/pinned):
  (i)   energy = amplitude^2         — the squaring (the Born quadratic)
  (ii)  scale-step = the octave tick — the clock / discrete RG
  (iii) constant flux = conservation on the workless face (A2)
Given (i)-(iii), the octave cascade v_n^3 / l_n = eps forces the same
pair per rung, with everything exact in exponent arithmetic.

THE PORT READING: E(k) is Born applied to the flow — the A^2 ladder,
the E-face reading. The -5/3 is the SEAT; intermittency corrections are
the M-face DRESS leaking into the port (the two-tier law, in fluids).
"""

from fractions import Fraction as F


def solve_closure():
    """The K41 dimensional system, exactly: returns (a, b)."""
    a = F(2, 3)                      # from 3a = 2
    b = 2 * a - 3                    # from 2a - b = 3
    return a, b


def square_gap_identity():
    """b = (2^2 - 3^2)/3 — the seed's square-gap over the vector."""
    return F(2 ** 2 - 3 ** 2, 3)


def gap_family():
    """The seed-gap primes/units: 1, 5, 13, 17."""
    return (3 ** 2 - 2 ** 3, 3 ** 2 - 2 ** 2, 2 ** 8 - 3 ** 5, 3 ** 4 - 2 ** 6)


def octave_cascade_slope():
    """The cascade on the octave lattice, exact exponent arithmetic.
    Constant flux: v^3 / l = eps  ->  v = eps^(1/3) l^(1/3)
    Spectral density: E(k) ~ v^2 / k with l = 1/k:
        v^2 = eps^(2/3) k^(-2/3)  ->  E(k) = eps^(2/3) k^(-5/3).
    Returns (exponent of eps, exponent of k) carried exactly."""
    v_eps, v_l = F(1, 3), F(1, 3)            # v = eps^1/3 l^1/3
    e_eps, e_k = 2 * v_eps, -(2 * v_l) - 1   # E ~ v^2/k, l = k^-1
    return e_eps, e_k


def la_duality():
    """The one tone, both readings, in one law:
    positional La = 2/3 (the eps exponent), interval La = 5/3 (the
    magnitude of the k exponent) — 240 degrees and the major sixth."""
    a, b = solve_closure()
    return a, abs(b)


def slope_in_octaves():
    """The framework unit: energy octaves per scale octave = 5/3 —
    each octave of scale requires an octave and a sixth of energy."""
    _, b = solve_closure()
    return abs(b)


def dimensional_mirror():
    """THE MECHANISM. [eps] = L^2 T^-3 and [E(k)] = L^3 T^-2 — the
    cascade rate and the spectrum are 2-3 MIRRORS of each other:
    (2,-3) against (3,-2). The k-exponent of the closure is the
    cross-determinant of the mirror over the vector:
        b = (L_eps*|T_E| - L_E*|T_eps|) / |T_eps| = (2*2 - 3*3)/3."""
    eps, spec = (2, -3), (3, -2)
    b = F(eps[0] * abs(spec[1]) - spec[0] * abs(eps[1]), abs(eps[1]))
    return eps, spec, b


def four_fifths():
    """The ONLY exact law of turbulence (K41's 4/5 law, from NS +
    conservation alone — the workless face): S_3(r) = -(4/5) eps r.
    The coefficient = 2^2 / (3^2 - 2^2) — the square over the
    square-gap; its exponent is 1 (the linear moment, no hypothesis)."""
    return F(4, 5), F(2 ** 2, 3 ** 2 - 2 ** 2)


def sl_gamma():
    """She-Leveque 1994 (EXTERNAL published model, parameter-free,
    the accepted intermittency dress): zeta_p = gamma*p + 2(1-(2/3)^(p/3)).
    gamma is FORCED by the exact third-moment law zeta_3 = 1:
        3*gamma + 2*(1 - 2/3) = 1  ->  gamma = 1/9 — the ennead ninth."""
    return (1 - 2 * (1 - F(2, 3))) / 3


def sl_zeta3():
    """zeta_3 = 3/9 + 2(1 - (2/3)^1) = 1 exactly (the 4/5-law anchor)."""
    return 3 * sl_gamma() + 2 * (1 - F(2, 3))


def sl_zeta(p):
    """SL94 zeta_p — the FLOAT comparison layer for p not divisible
    by 3 ((2/3)^(p/3) irrational there); marked as always."""
    return float(p) / 9 + 2 * (1 - (2 / 3) ** (p / 3))


def sl_slope():
    """Spectral slope with the SL dress: -(1 + zeta_2).
    Seat -5/3 = -1.6667; dressed ~ -1.696; measured ~ -1.70."""
    return -(1 + sl_zeta(2))


def bend_17_10():
    """The banked 51/50 pitch-bend, exact: seat x comma =
    (5/3)(51/50) = 17/10 — the bent slope is THE SPINE OVER THE BASE."""
    return F(5, 3) * F(51, 50)
