"""coupled_rings.py — the marker extension: two rings, exact arithmetic.

THE SETUP: the two-slit mode (amplitudes A1, A2) is coupled to a MARKER
ring — each node imprints a marker state M_k, a vector of Gaussian
integers (complex integers, the ring n = 4 where w = i). Which-way
information lives in how distinguishable M1 and M2 are.

THE RESULT (the pure-state complementarity ledger, exact):
    P^2 + V^2 + C^2 = 1
where P = predictability (the particle leg), V = fringe visibility
(the wave leg, reduced by the marker overlap), and C = the coherence
stored in the marker — THE ENTANGLEMENT LEG. The triple identity of
the bare two-slit becomes a PYTHAGOREAN QUADRUPLE:
    (A1^2-A2^2)^2 + (2 A1 A2 |c|)^2 + (2 A1 A2 sqrt(1-|c|^2))^2
        = (A1^2+A2^2)^2
with |c| the normalized marker overlap. Every marked two-slit is a
Pythagorean quadruple; entanglement is the third leg.
"""

from fractions import Fraction as F


def gmul(x, y):
    """(a+bi)(c+di) as integer pairs."""
    return (x[0] * y[0] - x[1] * y[1], x[0] * y[1] + x[1] * y[0])


def gconj(x):
    return (x[0], -x[1])


def overlap(M1, M2):
    """<M1|M2> = sum conj(M1_j) * M2_j — a Gaussian integer."""
    s = (0, 0)
    for a, b in zip(M1, M2):
        p = gmul(gconj(a), b)
        s = (s[0] + p[0], s[1] + p[1])
    return s


def norm2(M):
    """<M|M> — an integer."""
    return sum(a * a + b * b for a, b in M)


def c_squared(M1, M2):
    """|<M1|M2>|^2 / (<M1|M1><M2|M2>) — exact rational."""
    o = overlap(M1, M2)
    return F(o[0] * o[0] + o[1] * o[1], norm2(M1) * norm2(M2))


def ledger(A1, A2, M1, M2):
    """The complementarity ledger (P^2, V^2, C^2) — exact rationals."""
    S = A1 * A1 + A2 * A2
    P2 = F(A1 * A1 - A2 * A2, S) ** 2
    wave2 = F(2 * A1 * A2, S) ** 2
    c2 = c_squared(M1, M2)
    V2 = wave2 * c2                    # visibility: the surviving wave leg
    C2 = wave2 * (1 - c2)              # coherence stored in the marker
    return P2, V2, C2
