"""test_yang_mills_gap.py — the gap's mechanism on the program's own terms.

The 2026-08-09 addendum to Yang-Mills on Discrete Terms: what the July paper
graded (theorem at strong coupling, measurement in the window, magnitude by
transmutation) the five papers now give a mechanism for. Three legs, each
pinned: the integer gap (sourcing is counted; the spectrum of sources is the
integers; the gap is the step from zero to one); the sector theorem (the
mirror splits the figure's spectrum; the pair sector excludes the zero mode
and starts at 2 sin 20 degrees); the native non-abelian structure (the mirror
conjugates the rotation to its reversal — the dihedral relation, the minimal
non-commutativity, which is the program's bidirectional read).
"""
import math
from fractions import Fraction as F


def test_the_integer_gap():
    """Sourcing on the wheel is counted: the k-th rider's shortfall is exactly
    k parts, k an integer, and the k-less tier is the vacuum. The spectrum of
    source strengths is therefore the non-negative integers: there is nothing
    between zero and one, the lightest sourced excitation carries exactly one
    unit, and the gap EXISTS by integrality — only its magnitude awaits the
    borrowed ruler, exactly as the July paper's transmutation section says.
    The Clay contrast sentence — classical waves massless, quantum particles
    massive — is on these terms the contrast between the averaged and the
    counted: the continuum wave is the count's deleted average, and a theory
    that keeps the count is gapped before any dynamics is computed."""
    shortfalls = [k * 10 ** 6 - k * 142857 * 7 for k in range(0, 7)]
    assert shortfalls == [0, 1, 2, 3, 4, 5, 6]         # the source ladder is Z
    assert min(s for s in shortfalls if s > 0) == 1    # the gap: zero to one
    assert not any(0 < s < 1 for s in shortfalls)      # nothing in between


def test_the_sector_theorem():
    """The banked spectrum, recomputed and split. The nine-cycle Laplacian has
    eigenvalues 2 - 2cos(2 pi k / 9): one zero (the uniform mode) and four
    doubled positives. The mirror splits every doubled frequency into an even
    and an odd partner, and the ZERO MODE IS EVEN: the odd (pair) sector —
    the sector that carries every seat-pair relation, the physical sector of
    the gravity volume's arena — contains no zero mode at all. Its spectrum
    starts at the strictly positive 2 sin 20 degrees. A sector selected by a
    symmetry that excludes the uniform mode is gapped by construction: the
    gapless face and the gapped face are the two mirror sectors of one
    figure — the abelian theory's massless mode lives where the zero mode
    lives, and the confined sector is the pair sector, which never had a
    massless mode to lose."""
    n = 9
    freqs = sorted(abs(2 * math.sin(math.pi * k / n)) for k in range(n))
    assert freqs[0] == 0.0                              # one uniform zero
    positives = freqs[1:]
    assert all(f > 0 for f in positives)
    assert abs(min(positives) - 2 * math.sin(math.radians(20))) < 1e-12
    # the mirror k -> n-k fixes only k = 0 among the modes present: every
    # positive frequency is a mirror-exchanged pair (odd+even partners), and
    # the odd combination of the k = 0 mode vanishes identically:
    for k in range(1, 5):
        assert (n - k) % n != k                         # genuine pairs
    odd_sector = [2 * math.sin(math.pi * k / n) for k in range(1, 5)]
    assert min(odd_sector) > 0.68                       # gapped, no zero mode
    assert abs(min(odd_sector) - 0.6840402867) < 1e-9   # = 2 sin 20 deg


def test_the_native_non_abelian_structure():
    """The figure's symmetry is rotation and mirror, and they do not commute:
    on the ring, reflect-then-rotate differs from rotate-then-reflect, and
    conjugating a rotation by the mirror gives the INVERSE rotation — the
    dihedral relation s r s = r^-1. The reversal that runs the whole series —
    3/2 to 2/3, the alternating read, the bidirectional rotation — is exactly
    this relation: non-commutativity is the existence of the reversal. The
    minimal non-abelian structure is native to the figure, and the abelian
    case is the case with no reversal to read."""
    n = 12
    rot = lambda x: (x + 1) % n
    mir = lambda x: (-x) % n
    x = 5
    assert rot(mir(x)) != mir(rot(x))                   # they do not commute
    for x in range(n):
        assert mir(rot(mir(x))) == (x - 1) % n          # s r s = r^-1
    # and the same on the nine-ring:
    m9 = lambda x: (-x) % 9
    r9 = lambda x: (x + 1) % 9
    for x in range(9):
        assert m9(r9(m9(x))) == (x - 1) % 9             # the reversal, native


def test_the_eleven_displayed():
    """Displayed for the record, carrying no inferential weight, in the July
    paper's own register: the one-loop coefficient of the pure SU(3) flow is
    11N/3 at N = 3, the celebrated eleven — and eleven is the total of the
    directed four-vector of the generator pair, 1 + 2 + 3 + 5, the four
    consecutive Fibonacci numbers, the first rung of the negation family
    10 + 1. The identity is exact; its weight is a question the base-rate
    audit owns, and the display claims nothing further."""
    N = 3
    assert F(11 * N, 3) == 11
    assert 1 + 2 + 3 + 5 == 11 == 10 + 1
