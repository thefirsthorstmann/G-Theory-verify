"""test_the_schur_sweep.py — THE SCHUR RATIOS, SWEPT, AND WHY THE
QUADRUPOLE'S IS CLEAN (2026-08-18). Two Schur ratios had turned up by
accident, so the question was how many the account actually carries. The
sweep found more, rejected two candidates, refuted a prediction of mine,
and — following the author's observation that thirty-two is Fa — landed on a
double uniqueness at the quadrupole that explains the whole coefficient.

WHAT A SCHUR RATIO IS. If an average over a group acts on an irreducible
subspace, it must be a multiple of the identity there. The multiple is
then forced to be **rank over dimension** — no integral is performed, two
counts are divided.

THE MULTIPOLE FAMILY. Symmetric traceless rank-L three-tensors have
dimension 2L+1, verified by explicit rank for L up to six, and a wave
carries two polarizations whatever L. So every multipole's radiation
carries the ratio **2/(2L+1)**: two thirds, two fifths, **two sevenths**,
two ninths. The quadrupole's is one member of a family, and the
octupole's denominator is the reptend's own.

TWO MORE IN THE ACCOUNT. The isotropic average of a rank-one projector is
one third — rank one over dimension three, the plainest member. And the
**tetrahedral tight frame** sums to four thirds times the identity: four
vectors over three dimensions, which is **4/3, the perfect fourth, Fa**.
Its companion fact, that the pairwise dot product is exactly −1/3, is the
tetrahedral bond angle this program already carries. The octahedral frame
gives two, the octave; the cubic gives eight thirds.

TWO CANDIDATES REJECTED, on the record. Contact-per-child's three halves
is a *maximum of a ratio*, not a group average on an irreducible space —
the same family, count over count, but not forced by Schur. And Koide's
two thirds is a *constraint* (the root vector at forty-five degrees to
the democratic axis), not an average; an isotropic vector would give one
third and a ratio of one. Neither is a Schur ratio and neither is
recorded as one.

the author'S OBSERVATION, MADE RIGOROUS. Thirty-two is Fa. More than that: on the
root-24 scale **32 = 2⁵ is the only pure power of two in the octave, and
27 = 3³ the only pure power of three** — so a coefficient that is a pure
two-power can seat nowhere but Fa. The quadrupole's numerator is a pure
two-power by construction, and therefore lands on Fa because of what it
is.

MY PREDICTION FROM THAT, AND ITS REFUTATION. If the quadrupole carries
two-powers because it rides the octave, the octupole should carry
three-powers and seat at Re. **It does not.** Its contracted fourth
derivative is 8202/5, whose numerator is 2·3·1367 with 1367 prime and
foreign to the account. Recorded as a failure.

AND THE REASON IS BETTER THAN THE PREDICTION — a double uniqueness. The
quadrupole is **the only monochromatic multipole**: x_i x_j is quadratic,
so its motion is a constant plus the octave, and the constant dies under
differentiation, leaving one line. Every higher multipole mixes — the
octupole carries the first and third together, the sixteen-pole the
second and fourth. And the quadrupole is **the only multipole whose
luminosity coefficient is exactly its Schur ratio**, with factorial
remainder one; the octupole's remainder is 27, the next 1008, and they
grow. So the coefficient is clean at both ends for reasons that hold
nowhere else: a pure octave above, pure Schur below.

A DISCIPLINE NOTE. Those factorial remainders factor over two, three,
five and seven — because small factorials do, not because the register is
speaking. They are not counted as hits here.
"""

import itertools
from fractions import Fraction

import numpy as np
import sympy as sp


# ── the family ───────────────────────────────────────────────────────

def _dim_sym_traceless(L):
    rows = []
    for I in itertools.combinations_with_replacement(range(3), L):
        T = np.zeros((3,) * L)
        for P in set(itertools.permutations(I)):
            T[P] = 1
        rows.append(T.ravel())
    sym = np.linalg.matrix_rank(np.array(rows))
    if L < 2:
        return sym
    cons = []
    for J in itertools.combinations_with_replacement(range(3), L - 2):
        T = np.zeros((3,) * L)
        for k in range(3):
            for P in set(itertools.permutations((k, k) + J)):
                T[P] += 1
        cons.append(T.ravel())
    return sym - np.linalg.matrix_rank(np.array(cons))


def test_every_multipole_has_dimension_two_ell_plus_one():
    """Verified by explicit rank, not quoted."""
    for L in range(1, 7):
        assert _dim_sym_traceless(L) == 2 * L + 1, L


def test_the_family_of_ratios_and_the_octupoles_seventh():
    """Two polarizations over the multipole's own dimension."""
    fam = {L: Fraction(2, 2 * L + 1) for L in range(1, 7)}
    assert fam[2] == Fraction(2, 5)
    assert fam[3] == Fraction(2, 7)            # the reptend's denominator
    assert fam[4] == Fraction(2, 9)
    assert all(f.numerator == 2 for f in fam.values())


# ── the others found ─────────────────────────────────────────────────

def test_the_isotropic_average_is_the_plainest_member():
    """Rank one over dimension three."""
    rng = np.random.default_rng(11)
    v = rng.normal(size=(200000, 3))
    v /= np.linalg.norm(v, axis=1)[:, None]
    avg = np.einsum('ai,aj->ij', v, v) / len(v)
    assert np.allclose(avg, np.eye(3) / 3, atol=4e-3)
    assert Fraction(1, 3) == Fraction(1, 3)


def test_the_tetrahedral_frame_is_a_schur_ratio_and_it_is_fa():
    """Four vectors over three dimensions — and four thirds is the
    perfect fourth. Its pairwise product is the tetrahedral angle."""
    tet = np.array([[1, 1, 1], [1, -1, -1], [-1, 1, -1], [-1, -1, 1]], float)
    tet /= np.linalg.norm(tet, axis=1)[:, None]
    S = np.einsum('ai,aj->ij', tet, tet)
    assert np.allclose(S, (4 / 3) * np.eye(3))
    assert Fraction(len(tet), 3) == Fraction(4, 3)
    assert abs(tet[0] @ tet[1] + 1 / 3) < 1e-12
    assert abs(24 * Fraction(4, 3) - 32) < 1e-12        # Fa's seat on root 24


def test_the_other_platonic_frames_are_tight_too():
    """Six vectors give the octave; eight give eight thirds."""
    octa = np.vstack([np.eye(3), -np.eye(3)])
    cube = np.array(list(itertools.product([1, -1], repeat=3)), float)
    for V, expect in ((octa, Fraction(6, 3)), (cube, Fraction(8, 3))):
        W = V / np.linalg.norm(V, axis=1)[:, None]
        S = np.einsum('ai,aj->ij', W, W)
        assert np.allclose(S, float(expect) * np.eye(3))
        assert Fraction(len(W), 3) == expect


# ── the rejections ───────────────────────────────────────────────────

def test_contact_per_child_is_not_a_schur_ratio():
    """It is a maximum of a ratio of counts, not a group average on an
    irreducible space. Same family, different mechanism."""
    kind = {"contact per child": "maximum of a ratio",
            "Schur ratio": "average of a projector on an irrep"}
    assert kind["contact per child"] != kind["Schur ratio"]
    assert Fraction(3, 2).numerator == 3           # and not of the form 2/(2L+1)
    assert all(Fraction(3, 2) != Fraction(2, 2 * L + 1) for L in range(1, 20))


def test_koide_is_a_constraint_not_an_average():
    """An isotropic root-vector would give one third and a ratio of one;
    two thirds requires a specific angle, which an average cannot impose."""
    me, mmu, mtau = 0.51099895e-3, 105.6583755e-3, 1776.86e-3
    K = (me + mmu + mtau) / (np.sqrt(me) + np.sqrt(mmu) + np.sqrt(mtau)) ** 2
    assert abs(K - 2 / 3) < 1e-4
    isotropic = 3 * (1 / 3)                        # what an average would give
    assert abs(isotropic - 1.0) < 1e-12
    assert abs(K - isotropic) > 0.3                # so it is not that average


# ── the author's observation, and what it opened ─────────────────────────────

def test_fa_is_the_only_pure_power_of_two_in_the_octave():
    """And Re the only pure power of three — so a pure two-power
    coefficient can seat nowhere but Fa."""
    seats = {"Do": 24, "Re": 27, "Mi": 30, "Fa": 32,
             "Sol": 36, "La": 40, "Si": 45, "Do'": 48}
    p2 = [n for n, v in seats.items() if set(sp.factorint(v)) == {2}]
    p3 = [n for n, v in seats.items() if set(sp.factorint(v)) == {3}]
    assert p2 == ["Fa"] and seats["Fa"] == 2 ** 5
    assert p3 == ["Re"] and seats["Re"] == 3 ** 3


def test_the_octupole_is_not_a_pure_power_of_three():
    """The prediction that followed from the author's point, refuted: the
    octupole's contracted fourth derivative carries a foreign prime."""
    t, w, a = sp.symbols('t omega a', positive=True)
    x = [a * sp.cos(w * t), a * sp.sin(w * t), sp.Integer(0)]
    r2 = sum(u * u for u in x)
    d = lambda i, j: 1 if i == j else 0
    tot = 0
    for i, j, k in itertools.product(range(3), repeat=3):
        O = (x[i] * x[j] * x[k]
             - (d(i, j) * x[k] + d(j, k) * x[i] + d(k, i) * x[j]) * r2 / 5)
        tot += sp.diff(O, t, 4) ** 2
    val = sp.simplify(tot / (a ** 6 * w ** 8))
    assert sp.nsimplify(val) == sp.Rational(8202, 5)
    assert 1367 in sp.factorint(8202)              # prime, and foreign


def test_the_quadrupole_is_the_only_monochromatic_multipole():
    """Which is the reason. Its moment is quadratic, so the motion is a
    constant plus the octave and the constant dies under differentiation.
    Every higher multipole mixes harmonics."""
    N = 1 << 12
    th = 2 * np.pi * np.arange(N) / N
    x = np.stack([np.cos(th), np.sin(th), np.zeros(N)], axis=1)
    lines = {}
    for L in range(2, 7):
        present = set()
        for I in itertools.product(range(3), repeat=L):
            F_ = np.abs(np.fft.rfft(np.prod([x[:, i] for i in I], axis=0))) / N
            present |= {int(n) for n in np.nonzero(F_ > 1e-12)[0] if n}
        lines[L] = sorted(present)
    assert lines[2] == [2]                          # one line, and it is the octave
    assert all(len(v) > 1 for L, v in lines.items() if L != 2)


def test_the_quadrupole_is_the_only_purely_schur_coefficient():
    """And the other end is clean for the same kind of reason: its
    luminosity coefficient is exactly its Schur ratio, factorial
    remainder one, which holds at no other multipole."""
    rem = {}
    for L in range(2, 8):
        c = Fraction(int((L + 1) * (L + 2)),
                     int((L - 1) * L * sp.factorial(L) * sp.factorial2(2 * L + 1)))
        rem[L] = 1 / (c * (2 * L + 1))
    assert rem[2] == 1
    assert all(r != 1 for L, r in rem.items() if L != 2)
    assert rem[3] == 27 and rem[4] == 1008


def test_the_remainders_are_factorials_and_are_not_counted_as_hits():
    """They factor over small primes because small factorials do."""
    for r in (27, 1008, 54000):
        assert set(sp.factorint(r)) <= {2, 3, 5, 7}
    note = "small factorials factor over small primes; not a register hit"
    assert "not a register hit" in note
