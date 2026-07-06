"""two_slit.py — the polar two-slit (exact arithmetic).

THE ONTOLOGY (CC, Distant-Perspective 2025 / G2 p58): the two slits are
NOT two paths of one particle — they are TWO NODES OF ONE MODE. The
state is a single mode holding an amplitude at each node:
    Psi = (A1, m1) at node 1  +  (A2, m2) at node 2
Screen position enters as the path-difference d (in ring slots): the
node-2 phasor arrives rotated by d. Born reads the squared magnitude.

THE RESULT: with I_max = (A1+A2)^2 and I_min = (A1-A2)^2,
    V = 2 A1 A2 / (A1^2 + A2^2)          (fringe visibility  — the wave face)
    P = (A1^2 - A2^2) / (A1^2 + A2^2)    (path predictability — the particle face)
    P^2 + V^2 = 1   EXACTLY, because
    (A1^2 - A2^2)^2 + (2 A1 A2)^2 = (A1^2 + A2^2)^2
— Euclid's parametrization of the Pythagorean triples. Wave-particle
duality (Greenberger–Yasin) is the triple identity, holding in integers.

Cyclotomic exactness on the octave ring (n = 8): the cross-term
w^d + w^-d takes values in Z[sqrt2]: {2, s2, 0, -s2, -2} — represented
as pairs (a, b) meaning a + b*sqrt(2). The fringe ladder is QUANTIZED:
five levels, antipodal levels pairing to twice the mean intensity.
"""

from fractions import Fraction as F

# omega^d + omega^-d on the octave ring, as (a, b) = a + b*sqrt(2)
CROSS8 = {0: (2, 0), 1: (0, 1), 2: (0, 0), 3: (0, -1), 4: (-2, 0),
          5: (0, -1), 6: (0, 0), 7: (0, 1)}


def intensity8(A1, A2, d):
    """Screen intensity at path-difference d (octave ring), exact:
    returns (a, b) meaning a + b*sqrt(2)."""
    c = CROSS8[d % 8]
    return (A1 * A1 + A2 * A2 + A1 * A2 * c[0], A1 * A2 * c[1])


def visibility(A1, A2):
    return F(2 * A1 * A2, A1 * A1 + A2 * A2)


def predictability(A1, A2):
    return F(abs(A1 * A1 - A2 * A2), A1 * A1 + A2 * A2)


def duality_sum(A1, A2):
    """P^2 + V^2 — exactly 1 for every integer amplitude pair."""
    return predictability(A1, A2) ** 2 + visibility(A1, A2) ** 2


def which_path_rounding(A1, A2):
    """Full which-path reading = rounding a node's phase: the relative
    phase is destroyed, the cross-term averages to zero over the ring
    (sum of all omega^k = 0): fringes gone, V -> 0, P -> 1 knowledge."""
    # average intensity over the unknown phase: cross-term sums to zero
    return A1 * A1 + A2 * A2          # flat screen: no d-dependence


def triple(A1, A2):
    """The Pythagorean triple this two-slit IS."""
    return (abs(A1 * A1 - A2 * A2), 2 * A1 * A2, A1 * A1 + A2 * A2)
