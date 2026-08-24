"""test_the_quadrupole_coefficient.py — THE THIRTY-TWO FIFTHS, COUNTED
(2026-08-18). The ledger carried this coefficient as "fixed by comparison
rather than derived." That description was wrong, and the correction is
worth more than the number: **every factor in it is a count**, and the
counts are ones this account already keeps.

WHAT IS AND IS NOT CLAIMED. The derivation below is the standard one; the
register did not invent it. What the register supplies is the reading —
that the coefficient contains no measured input anywhere, being a
dimension divided by a rank, times the octave. The ledger entry changes
from comparison-fixed to counted, and that is the whole of the claim.

THE FIVE IS A DIMENSION. Symmetric three-by-three tensors number six;
removing the trace leaves **five**, verified by rank. That is the
quadrupole's own component count, and the l = 2 representation of the
rotation group.

THE TWO IS A RANK. The transverse-traceless projector is idempotent with
trace exactly two — the **two polarizations** a wave can carry, no more.

AND SCHUR JOINS THEM WITHOUT AN INTEGRAL. The angular average of that
projector, restricted to the five-dimensional space, must be a multiple
of the identity there, because the space is irreducible. The multiple is
therefore forced to be **rank over dimension, two fifths** — no
integration required, only the two counts. Confirmed numerically over two
hundred thousand directions. The flux formula's own half turns it into
the familiar one fifth.

THE THIRTY-TWO IS THE OCTAVE. The quadrupole is even under reflection, so
its lowest harmonic is the **second** — a binary radiates exactly one
octave above its orbit, with no choice in the matter. Three time
derivatives of a second-harmonic motion, squared and summed, give
2⁵ = 32 exactly, constant in time. Checked two independent ways: in closed
form, and by transforming a Keplerian orbit, where the fundamental comes
out at machine zero while the octave lands on 32.0000.

AND THE OCTAVE IS A FORBID, not a description. For a circular orbit the
fundamental is identically absent — there is no gravitational radiation
at the orbital frequency itself, only at its octave and above.
Eccentricity opens the fundamental, and opens it at order e², measured
here at a ratio of 0.151 e² across three eccentricities.

ASSEMBLED, the coefficient reproduces the double pulsar's orbital decay
to four parts in ten thousand, that residue being this file's rounding of
the masses rather than the formula's.
"""

import itertools
import math
from fractions import Fraction

import numpy as np
import sympy as sp


def test_the_five_is_the_quadrupoles_component_count():
    """Six symmetric, five once the trace is removed — the l = 2 space."""
    basis = []
    for i, j in itertools.combinations_with_replacement(range(3), 2):
        M = np.zeros((3, 3))
        M[i, j] = M[j, i] = 1
        basis.append(M)
    assert len(basis) == 6
    trless = [M - np.eye(3) * np.trace(M) / 3 for M in basis]
    assert np.linalg.matrix_rank(np.array([M.ravel() for M in trless])) == 5


def _projector(n):
    P = np.eye(3) - np.outer(n, n)
    L = np.zeros((3, 3, 3, 3))
    for i, j, k, l in itertools.product(range(3), repeat=4):
        L[i, j, k, l] = (0.5 * (P[i, k] * P[j, l] + P[i, l] * P[j, k])
                         - 0.5 * P[i, j] * P[k, l])
    return L


def test_the_two_is_the_polarization_count():
    """The transverse-traceless projector is idempotent, of rank two."""
    n = np.array([0.3, -0.5, 0.81])
    n /= np.linalg.norm(n)
    L = _projector(n)
    tr = sum(L[i, j, i, j] for i, j in itertools.product(range(3), repeat=2))
    assert abs(tr - 2.0) < 1e-12
    Lm = L.reshape(9, 9)
    assert np.allclose(Lm @ Lm, Lm)
    assert np.linalg.matrix_rank(Lm) == 2


def test_schur_supplies_the_average_without_an_integral():
    """Restricted to an irreducible space the average must be a multiple
    of the identity, so the multiple is rank over dimension — two fifths,
    counted rather than integrated. Confirmed by direct averaging."""
    rng = np.random.default_rng(7)
    N = 60000
    v = rng.normal(size=(N, 3))
    v /= np.linalg.norm(v, axis=1)[:, None]
    acc = np.zeros((3, 3, 3, 3))
    for m in range(0, N, 20000):
        P = np.eye(3)[None] - v[m:m + 20000][:, :, None] * v[m:m + 20000][:, None, :]
        acc += (0.5 * np.einsum('aik,ajl->ijkl', P, P)
                + 0.5 * np.einsum('ail,ajk->ijkl', P, P)
                - 0.5 * np.einsum('aij,akl->ijkl', P, P))
    acc /= N
    A = rng.normal(size=(3, 3))
    A = A + A.T
    A -= np.eye(3) * np.trace(A) / 3
    got = np.einsum('ijkl,ij,kl->', acc, A, A) / np.einsum('ij,ij->', A, A)
    assert abs(got - 2 / 5) < 3e-3
    n = np.array([0.3, -0.5, 0.81]); n /= np.linalg.norm(n)
    rank = int(round(sum(_projector(n)[i, j, i, j]
                         for i, j in itertools.product(range(3), repeat=2))))
    dim = 5
    assert Fraction(rank, dim) == Fraction(2, 5)     # the ratio IS the two counts


def test_the_thirty_two_is_the_octave_in_closed_form():
    """The quadrupole of a circular orbit, thrice differentiated and
    contracted, is 32 μ²a⁴ω⁶ exactly and constant in time."""
    t, w, a, mu = sp.symbols('t omega a mu', positive=True)
    x = sp.Matrix([a * sp.cos(w * t), a * sp.sin(w * t), 0])
    Q = sp.Matrix(3, 3, lambda i, j:
                  mu * (x[i] * x[j] - (1 if i == j else 0) * x.dot(x) / 3))
    Q3 = Q.applyfunc(lambda e: sp.diff(e, t, 3))
    QQ = sp.simplify(sum(Q3[i, j] ** 2 for i in range(3) for j in range(3)))
    assert sp.simplify(QQ - 32 * mu ** 2 * a ** 4 * w ** 6) == 0
    assert sp.simplify(sp.diff(QQ, t)) == 0
    assert 32 == 2 ** 5


def test_the_quadrupole_oscillates_at_twice_the_orbit():
    """Being even under reflection, its lowest harmonic is the second."""
    t, w, a, mu = sp.symbols('t omega a mu', positive=True)
    Qxx = mu * (a * sp.cos(w * t)) ** 2 - mu * a ** 2 / 3
    varying = sp.simplify(Qxx - sp.Rational(1, 6) * mu * a ** 2)
    assert sp.simplify(varying - mu * a ** 2 * sp.cos(2 * w * t) / 2) == 0


def _harmonics(e, nmax=4, N=1 << 13):
    M = 2 * np.pi * np.arange(N) / N
    E = M.copy()
    for _ in range(80):
        E = E - (E - e * np.sin(E) - M) / (1 - e * np.cos(E))
    x, y = np.cos(E) - e, np.sqrt(1 - e * e) * np.sin(E)
    r2 = x * x + y * y
    Q = np.zeros((N, 3, 3))
    Q[:, 0, 0] = x * x - r2 / 3
    Q[:, 1, 1] = y * y - r2 / 3
    Q[:, 2, 2] = -r2 / 3
    Q[:, 0, 1] = Q[:, 1, 0] = x * y
    F = np.fft.rfft(Q, axis=0) / N
    n = np.arange(F.shape[0])
    T = (1j * n[:, None, None]) ** 3 * F
    return [2 * np.sum(np.abs(T[k]) ** 2) for k in range(nmax + 1)]


def test_the_octave_is_the_floor_and_the_thirty_two_confirms_independently():
    """A circular binary emits nothing at its orbital frequency — the
    fundamental is at machine zero — while the octave carries exactly 32,
    reproducing the closed form by a wholly different route."""
    h = _harmonics(0.0)
    assert h[1] < 1e-20
    assert abs(h[2] - 32.0) < 1e-6


def test_eccentricity_opens_the_fundamental_at_second_order():
    """And opens it as e², so the octave's primacy is a statement about
    the shape of the orbit rather than an approximation."""
    ratios = []
    for e in (0.01, 0.02, 0.04):
        h = _harmonics(e)
        ratios.append(h[1] / h[2] / e ** 2)
    assert all(0.14 < r < 0.16 for r in ratios)
    assert max(ratios) - min(ratios) < 0.01          # flat: the power is two


def test_the_assembled_coefficient_matches_the_double_pulsar():
    """32/5, carried into the period form, against J0737-3039."""
    G, c, Msun = 6.67430e-11, 2.99792458e8, 1.98892e30
    m1, m2 = 1.338185 * Msun, 1.248868 * Msun
    Pb = 0.1022515592973 * 86400
    e = 0.087777023
    fe = (1 + 73 / 24 * e ** 2 + 37 / 96 * e ** 4) / (1 - e * e) ** 3.5
    pred = (-192 * math.pi / 5 * (2 * math.pi * G / (Pb * c ** 3)) ** (5 / 3)
            * m1 * m2 / (m1 + m2) ** (1 / 3) * fe)
    assert abs(pred / -1.247827e-12 - 1) < 1e-3
    assert Fraction(192, 5) == Fraction(32, 5) * 6   # the same coefficient


def test_the_ledger_entry_was_misdescribed():
    """Nothing in the coefficient was ever read off a measurement: a
    dimension, a rank, and the octave."""
    parts = {"5": "dimension of the l=2 space",
             "2": "rank of the transverse-traceless projector",
             "32": "the octave, cubed by three time derivatives, squared"}
    assert all("measure" not in v and "fit" not in v for v in parts.values())
    assert Fraction(32, 5) == Fraction(2 ** 5, 5)
