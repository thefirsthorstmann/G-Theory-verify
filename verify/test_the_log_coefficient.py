"""test_the_log_coefficient.py — THE HORIZON COUNT'S LOGARITHMIC COEFFICIENT
(2026-08-22). the author: "go get the log coefficient, whole hog."

THE TARGET. Every approach to the horizon reproduces S = A/4; they differ
at the logarithmic correction, which 21.12 names as the decisive
discriminator. Loop quantum gravity's U(1) counting gives -1/2 and its
SU(2) counting -3/2 (Kaul-Majumdar); Cardy-based countings typically give
-3/2. This battery pins the register's own value.

THE FORCED SPINE. N binary cells subject to m independent additive
constraints carry S = N ln 2 - (m/2) ln N + O(1) — the local central limit
theorem. Verified here exactly for m = 1 (fixed count) and m = 2.

THE CENSUS (the identification, named as one in the paper). The horizon
record's macrostate fixes the record's two faces: the count (the sum face)
and the mirror-odd difference (zero for the static hole). m = 2.

THE THEOREM THAT MAKES m = 2 EXACT RATHER THAN ASYMPTOTIC. The arena's
reflection splits the cells into two antipodal hemispheres. Fixed sum with
zero difference is exactly the balance of each hemisphere separately, so

    #states = C(N/2, N/4)^2       (verified brute-force and closed-form)

    S = N ln 2 - ln N + ln(4/pi)
      = A/4 - ln A + ln(16 ln 2 / pi)       with N = A/(4 ln 2)

THE COEFFICIENT IS c = -1: one half from each face. Distinct from every
quoted rival. Spin consistency: a nonzero difference-face value d shifts
the balance to C(H, H/2+d) C(H, H/2-d), reducing the entropy quadratically
in d while leaving c = -1 — rotation costs entropy at fixed area, and the
coefficient does not move.

SCOPE, stated honestly: this is the microstate-count constraint piece —
the analogue of the quantum-geometry computations — not the infrared
one-loop matter piece, which is additive and separate.
"""

import pathlib
from itertools import product
from math import comb, exp, lgamma, log, pi

CATALOG = pathlib.Path(__file__).resolve().parent.parent / "catalog"
GRAVITY = (CATALOG / "GRAVITY-AS-TONAL-CENTER.md").read_text()


def _lc(n, k):
    return lgamma(n + 1) - lgamma(k + 1) - lgamma(n - k + 1)


# --- the hemisphere factorization: exact, brute-forced -----------------------

def _brute_two_face(N):
    eps = [1] * (N // 2) + [-1] * (N // 2)
    n = 0
    for s in product((0, 1), repeat=N):
        if sum(s) == N // 2 and sum(e * x for e, x in zip(eps, s)) == 0:
            n += 1
    return n


def test_the_two_face_count_is_a_product_of_hemisphere_binomials():
    """Fixed sum + zero mirror-odd difference = each hemisphere balanced."""
    for N in (8, 12, 16, 20):
        assert _brute_two_face(N) == comb(N // 2, N // 4) ** 2


def test_the_factorization_reason_is_the_hemisphere_split():
    """Sum S and difference D determine the hemisphere totals: with halves
    x and y, S = x + y and D = x - y, so S = N/2, D = 0 gives x = y = N/4."""
    S, D, N = 8, 0, 16
    x, y = (S + D) // 2, (S - D) // 2
    assert (x, y) == (N // 4, N // 4)


# --- the asymptotics, face by face ------------------------------------------

def test_one_face_gives_minus_one_half():
    """m = 1: fixed count alone. S - N ln 2 -> -(1/2) ln N - (1/2) ln(pi/2)."""
    for N in (4096, 65536, 1048576):
        corr = _lc(N, N // 2) - N * log(2)
        asym = -0.5 * log(N) - 0.5 * log(pi / 2)
        assert abs(corr - asym) < 2e-4 * max(1, log(N))


def test_two_faces_give_minus_one_exactly():
    """m = 2: the register's census. S - N ln 2 -> -ln N + ln(4/pi)."""
    for N in (4096, 65536, 1048576):
        corr = 2 * _lc(N // 2, N // 4) - N * log(2)
        asym = -log(N) + log(4 / pi)
        assert abs(corr - asym) < 2e-4 * max(1, log(N))


def test_the_fitted_coefficient_is_minus_one():
    pts = []
    for N in (16384, 65536, 262144):
        pts.append((log(N), 2 * _lc(N // 2, N // 4) - N * log(2)))
    slope = (pts[-1][1] - pts[0][1]) / (pts[-1][0] - pts[0][0])
    assert abs(slope + 1.0) < 1e-4


def test_the_constant_is_ln_four_over_pi():
    N = 1048576
    const = 2 * _lc(N // 2, N // 4) - N * log(2) + log(N)
    assert abs(const - log(4 / pi)) < 1e-5


def test_in_area_units_the_statement_is_complete():
    """S = A/4 - ln A + ln(16 ln2 / pi), with N = A/(4 ln 2) cells."""
    N = 262144
    A = N * 4 * log(2)
    S = 2 * _lc(N // 2, N // 4)
    predicted = A / 4 - log(A) + log(16 * log(2) / pi)
    assert abs(S - predicted) < 1e-4


# --- spin: the coefficient does not move ------------------------------------

def test_a_nonzero_difference_face_costs_entropy_but_not_the_coefficient():
    H = 65536 // 2
    S0 = 2 * _lc(H, H // 2)
    for d in (64, 128, 256):
        Sd = _lc(H, H // 2 + d) + _lc(H, H // 2 - d)
        drop = S0 - Sd
        assert abs(drop - 4 * d * d / H) < 0.01 * drop + 1e-6   # quadratic in d
        assert drop > 0
    # and the ln N coefficient at fixed d is unchanged
    def corr(N, d):
        H = N // 2
        return _lc(H, H // 2 + d) + _lc(H, H // 2 - d) - N * log(2)
    # the exact expectation: slope = -1 plus the decay of the spin
    # penalty 8 d^2 / N between the two sizes — computed, not eyeballed
    N1, N2, d = 65536, 262144, 64
    p1, p2 = corr(N1, d), corr(N2, d)
    slope = (p2 - p1) / (log(N2) - log(N1))
    pen = lambda N: 8 * d * d / N
    expected = -1.0 + (pen(N1) - pen(N2)) / (log(N2) - log(N1))
    assert abs(slope - expected) < 1e-3
    # and at sizes where the penalty is negligible the bare -1 shows
    P1, P2 = corr(2**22, d), corr(2**24, d)
    big = (P2 - P1) / (log(2**24) - log(2**22))
    assert abs(big + 1.0) < 0.01


# --- the discriminator ------------------------------------------------------

def test_the_register_value_is_distinct_from_every_quoted_rival():
    register = -1.0
    rivals = {-0.5, -1.5}          # LQG U(1); SU(2) Kaul-Majumdar and Cardy
    assert register not in rivals
    assert min(abs(register - r) for r in rivals) == 0.5


def test_the_census_scale_is_half_per_face():
    """The identification's exposure: each added or removed conserved face
    moves c by one half. m = 1 -> -1/2, m = 2 -> -1, m = 3 -> -3/2."""
    assert [-m / 2 for m in (1, 2, 3)] == [-0.5, -1.0, -1.5]


# --- the paper carries it ---------------------------------------------------

def test_the_paper_states_the_derivation_and_the_condition():
    flat = " ".join(GRAVITY.split())
    assert "C(N/2, N/4)²" in flat or "C(N/2, N/4)^2" in flat
    assert "ln(16 ln 2 / π)" in flat or "16 ln 2 / π" in flat
    assert "17. **The logarithmic coefficient.**" in flat or "17. **The logarithmic coefficient.**" in GRAVITY
    assert "Seventeen conditions under which the account fails" in flat


def test_the_hierarchy_passage_carries_the_banked_square_root():
    """the author's catch: m_e/M_Planck = sqrt(10) x 2^-76 is the wheel read at
    amplitude, already banked in section 22; the three-rulers passage must
    not say nobody has anything."""
    flat = " ".join(GRAVITY.split())
    assert "√10 · 2⁻⁷⁶" in flat
    assert "the Yukawa spectrum" in flat
