"""Pins for THE-CURVATURE-OF-THE-LADDER-2026-08-02.md — the quadratic chain
c_n = n^2/(n^2-1) as the second-difference (discrete Laplacian) column of the
harmonic ladder, its telescoping closure at the octave, the remainder law, and
the additive/multiplicative (wavelength/frequency) duality."""

import math
from fractions import Fraction as F


def test_comma_is_second_difference_of_log():
    # c_n = s_n - s_{n+1} = -Δ²(ln) at n, and every rung is positive (ln concave)
    for n in range(2, 200):
        s_n = math.log(n / (n - 1))
        s_n1 = math.log((n + 1) / n)
        c_n = math.log(n * n / (n * n - 1))
        lap = math.log(n + 1) - 2 * math.log(n) + math.log(n - 1)
        assert abs((s_n - s_n1) - c_n) < 1e-13
        assert abs(c_n + lap) < 1e-13
        assert c_n > 0


def test_total_curvature_is_the_octave_and_remainder_is_next_step():
    # Π_{n=2..N} n²/(n²−1) = 2N/(N+1) exactly; remainder to 2 = (N+1)/N exactly
    P = F(1)
    for N in range(2, 500):
        P *= F(N * N, N * N - 1)
        assert P == F(2 * N, N + 1)
        assert F(2, 1) / P == F(N + 1, N)


def test_additive_multiplicative_duality():
    # Σ_{k=1..K} 2/(k(k+1)) = Π_{n=2..K} n²/(n²−1) = 2K/(K+1) exactly
    for K in range(1, 200):
        add = sum(F(2, k * (k + 1)) for k in range(1, K + 1))
        mul = F(1)
        for n in range(2, K + 1):
            mul *= F(n * n, n * n - 1)
        assert add == mul == F(2 * K, K + 1)


def test_named_rungs():
    # the program's comma family, indexed by its own square root
    assert F(2 * 2, 2 * 2 - 1) == F(4, 3)        # the fourth
    assert F(3 * 3, 3 * 3 - 1) == F(9, 8)        # the whole tone, Re
    assert F(5 * 5, 5 * 5 - 1) == F(25, 24)      # chromatic semitone, regions/vertices
    assert F(7 * 7, 7 * 7 - 1) == F(49, 48)      # septimal diesis at the seed 7
    assert F(8 * 8, 8 * 8 - 1) == F(64, 63)      # lambda's comma at the octave register
    assert F(9 * 9, 9 * 9 - 1) == F(81, 80)      # the syntonic comma at the modulus 9
    assert 127 * 127 - 1 == 2**8 * 3**2 * 7      # gravity-depth rung: tower monomial


def test_staircase_is_the_just_ladder():
    # partial products: fourth, fifth, both sixths, both septimal sevenths ...
    expected = [F(4, 3), F(3, 2), F(8, 5), F(5, 3), F(12, 7), F(7, 4), F(16, 9), F(9, 5)]
    P = F(1)
    got = []
    for n in range(2, 10):
        P *= F(n * n, n * n - 1)
        got.append(P)
    assert got == expected
