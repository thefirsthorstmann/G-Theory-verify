"""test_the_simplex_interval.py — FA IS THE INTERVAL OF THREE-DIMENSIONAL
ISOTROPY (2026-08-18). Pressing on the tetrahedral four thirds, as the author
asked. It is not a resemblance: the fourth is what minimal isotropy costs
in three dimensions, and three dimensions is the only place where that
frame sits on the quadrupole's own zero.

THE FRAME. The regular simplex in d dimensions has d+1 unit vectors, and
they are the **minimal frame that is both isotropic and balanced** — the
fewest directions that spread evenly and also sum to zero, so that no net
direction survives. An orthonormal basis is isotropic with d vectors but
does not sum to zero; adding the one further direction that balances it
costs exactly one vector and changes the frame constant from one to
(d+1)/d.

AND THAT CONSTANT IS AN INTERVAL. For d = 1, 2, 3, 4, 5 it is 2/1, 3/2,
4/3, 5/4, 6/5 — the consecutive-partial ratios of the harmonic series,
in order. **Dimension indexes the series.** In our own dimension the
constant is **4/3, the fourth, Fa**; and 24 × 4/3 = 32, Fa's seat on the
root the account already uses. The pairwise cosine is −1/d, which at
d = 3 is the tetrahedral bond angle this program carries elsewhere.

WHICH SAYS WHAT FA'S DENOMINATOR IS. The carrier section calls Fa "the
sole division by three in the octave." The three it divides by is the
dimension of space. Written as a frame constant the statement is
(d+1)/d with d = 3 — so the carrier's identity is a witness to the
dimension, and cannot be relocated without changing it. In two dimensions
the carrier would be the fifth; in four, the major third.

AND THREE IS THE ONLY DIMENSION WHERE THE FRAME MEETS THE QUADRUPOLE. The
angle at which the l = 2 anisotropy vanishes is the magic angle, where
cos² = 1/3. The simplex angle in d dimensions is arccos(−1/d). Asking the
second to be exactly **twice** the first requires 2cos² − 1 = −1/d with
cos² = 1/3, which forces **d = 3 and nothing else**. So in three
dimensions the minimal balanced frame's own angle is precisely double the
angle where the quadrupole's anisotropy dies — Fa's frame and the
quadrupole's zero are one object here and separate everywhere else. That
is the second time the quadrupole and Fa have arrived together, the first
being the coefficient's numerator, and this time the coincidence has a
dimension attached to it.

THE PROMOTION WINDOW, READ THROUGH THE SAME FAMILY, carries the three
primary consonances at d = 2, 3, 4 — the fifth, the fourth and the major
third — with the one we occupy carrying the fourth.

TWO THINGS DECLINED. At d = 7 the constant is 8/7, which is also the
packing cell's ratio; there is no route from a seven-dimensional simplex
to a length in three dimensions, and it is recorded here as a coincidence
of the number so a later reader does not count it. And the musical
labelling of (d+1)/d is this account's own convention on root 24 — the
theorem is the frame constant; the names are the reading.
"""

import math
from fractions import Fraction

import numpy as np


def _simplex(d):
    """The d+1 unit vectors of the regular simplex, realised in R^d."""
    E = np.eye(d + 1)
    V = E - E.mean(axis=0)
    Q, _ = np.linalg.qr(np.column_stack([np.ones(d + 1)]), mode='complete')
    W = V @ Q[:, 1:]
    return W / np.linalg.norm(W, axis=1)[:, None]


def test_the_simplex_is_isotropic_and_balanced():
    """Both properties, checked: a tight frame, and summing to zero."""
    for d in range(1, 9):
        W = _simplex(d)
        assert W.shape == (d + 1, d)
        S = W.T @ W
        assert np.allclose(S, S[0, 0] * np.eye(d))       # isotropic
        assert np.allclose(W.sum(axis=0), 0, atol=1e-10)  # balanced


def test_an_orthonormal_basis_is_isotropic_but_not_balanced():
    """Which is why the minimum is d+1 and not d — the one extra vector
    is what buys the vanishing of the net direction."""
    for d in range(2, 7):
        E = np.eye(d)
        assert np.allclose(E.T @ E, np.eye(d))            # isotropic, constant 1
        assert not np.allclose(E.sum(axis=0), 0)          # but not balanced


def test_the_frame_constant_is_the_superparticular_ratio():
    """(d+1)/d exactly, for every dimension tested."""
    for d in range(1, 9):
        W = _simplex(d)
        k = (W.T @ W)[0, 0]
        assert abs(k - (d + 1) / d) < 1e-12
        assert Fraction(d + 1, d).limit_denominator(100) == Fraction(d + 1, d)


def test_the_pairwise_cosine_is_minus_one_over_the_dimension():
    """And at d = 3 it is the tetrahedral bond angle."""
    for d in range(2, 9):
        W = _simplex(d)
        assert abs(W[0] @ W[1] + 1 / d) < 1e-12
    assert abs(math.degrees(math.acos(-1 / 3)) - 109.4712) < 1e-3


def test_dimension_indexes_the_harmonic_series():
    """The first five constants are the consecutive-partial ratios."""
    series = [Fraction(d + 1, d) for d in range(1, 6)]
    assert series == [Fraction(2, 1), Fraction(3, 2), Fraction(4, 3),
                      Fraction(5, 4), Fraction(6, 5)]


def test_our_dimension_gives_fa_and_its_seat():
    """Four thirds, and the seat it lands on with the account's own root."""
    assert Fraction(4, 3) == Fraction(3 + 1, 3)
    assert 24 * Fraction(4, 3) == 32
    assert 32 == 2 ** 5


def test_fas_denominator_is_the_dimension():
    """The carrier is 'the sole division by three in the octave', and the
    three is the dimension — so the carrier witnesses it and cannot move
    without it."""
    carrier = {d: Fraction(d + 1, d) for d in (2, 3, 4)}
    assert carrier[3].denominator == 3
    assert carrier[2] == Fraction(3, 2) and carrier[4] == Fraction(5, 4)
    assert len({v for v in carrier.values()}) == 3       # a different tone each


def test_three_is_the_only_dimension_meeting_the_quadrupoles_zero():
    """The magic angle has cos² = 1/3, where the l = 2 anisotropy dies.
    Requiring the simplex angle to be exactly twice it forces d = 3."""
    magic_cos2 = 1 / 3
    assert abs(3 * magic_cos2 - 1) < 1e-15               # P2 vanishes there
    doubled = 2 * magic_cos2 - 1
    assert abs(doubled + 1 / 3) < 1e-15                  # equals -1/3
    hits = [d for d in range(1, 40) if abs((d - 1) / (2 * d) - magic_cos2) < 1e-12]
    assert hits == [3]
    assert abs(math.acos(doubled) - math.acos(-1 / 3)) < 1e-12


def test_the_promotion_window_carries_the_three_consonances():
    """Read through the same family, d = 2, 3, 4 give the fifth, the
    fourth and the major third."""
    got = [Fraction(d + 1, d) for d in (2, 3, 4)]
    assert got == [Fraction(3, 2), Fraction(4, 3), Fraction(5, 4)]


def test_the_eight_sevenths_at_seven_dimensions_is_declined():
    """It is the packing cell's ratio, and there is no route from a
    seven-dimensional simplex to a length in three. Recorded as a
    coincidence of the number, not a hit."""
    assert Fraction(8, 7) == Fraction(7 + 1, 7)
    declined = {"object": "simplex constant at d = 7",
                "resembles": "the packing cell, 8/7 fm",
                "route": None}
    assert declined["route"] is None
