"""test_the_wheel_count.py — THE COUNT'S SELECTION ARITHMETIC, PINNED
(2026-08-16). The capstone's adversarial read-through found that the wheel's
selection theorems — irreducibility, the period's cyclotomic birth, the
promotion chain, the costume table, the G conversion, and the exclusivity
scan — were asserted in the papers but pinned nowhere in the suite. The
paper's most attackable number was its least pinned. This battery closes that,
replicating the published scan on its published terms (blocks x <= 16,
periods k <= 200).
"""

from fractions import Fraction as F
from math import gcd, pi

HBAR = 1.054571817e-34
C = 2.99792458e8
M_E = 9.1093837015e-31
M_P = 1.67262192369e-27
M_MU = 1.883531627e-28
G_CODATA18 = 6.67430e-11                       # +- 22 ppm
ALPHA = 7.2973525693e-3


def _ord2(m):
    k, t = 1, 2 % m
    while t != 1:
        t = t * 2 % m
        k += 1
    return k


def test_the_wheel_value_and_the_costume_table():
    """One lattice point, four costumes; the wheel form is the -1 dress."""
    assert F(5, 2 ** 151) == F(5, 4) / 2 ** 149 == F(5, 2) / 2 ** 150 == F(10, 2 ** 152)
    # wheel vs bare power: a relative 2^-151, thirty-nine orders below metrology
    assert abs(5 / (2 ** 151 - 1) / (5 * 2.0 ** -151) - 1) < 1e-44


def test_irreducibility_selects_exactly_one_block():
    """ord_2(5) = 4 divides 152 but not 151: the five-block is irreducible,
    the ten-block dissolves, and the fractional costumes have no wheel at all."""
    assert _ord2(5) == 4
    assert 151 % 4 != 0 and gcd(5, 2 ** 151 - 1) == 1     # five survives
    assert 152 % 4 == 0 and (2 ** 152 - 1) % 5 == 0       # ten dissolves
    # 5/2 and 5/4 are not integers, so they are not blocks:
    assert F(5, 2).denominator != 1 and F(5, 4).denominator != 1


def test_the_period_is_born_at_the_joint_closure():
    """2^15 - 1 = 7 x 31 x Phi_15(2); the novel factor is 151, order 15."""
    assert 2 ** 3 - 1 == 7 and 2 ** 5 - 1 == 31           # the two ancestors
    assert 2 ** 15 - 1 == 7 * 31 * 151
    phi15 = (2 ** 15 - 1) * (2 ** 1 - 1) // ((2 ** 3 - 1) * (2 ** 5 - 1))
    assert phi15 == 151                                    # the cyclotomic part
    assert _ord2(151) == 15                                # born there, not before
    for d in range(1, 15):
        assert (2 ** d - 1) % 151 != 0                     # no ancestor minted it


def test_the_promotion_chain_is_the_figures_own_law():
    """value-becomes-depth from 2: the Catalan-Mersenne rungs, all prime."""
    x = 2
    chain = [x]
    for _ in range(3):
        x = 2 ** x - 1
        chain.append(x)
    assert chain == [2, 3, 7, 127]
    for n in chain[1:]:
        assert all(n % q for q in range(2, int(n ** 0.5) + 1))


def test_the_G_prediction_and_its_distance_from_codata():
    G_pred = 5 / (2 ** 151 - 1) * HBAR * C / M_E ** 2
    assert abs(G_pred - 6.6735902e-11) < 1e-17
    ppm = (G_CODATA18 - G_pred) / G_CODATA18 * 1e6
    assert 105.0 < ppm < 108.0                             # 106.4 ppm below center
    assert 4.5 < ppm / 22.0 < 5.1                          # ~4.8 sigma at 22 ppm


def _best_wheel(target, xmax=16, kmax=200):
    """The published scan: best |x/(2^k-1) - target| / target over the grid."""
    best = None
    for k in range(2, kmax + 1):
        den = 2 ** k - 1
        x = round(target * den)
        for xx in (x - 1, x, x + 1):
            if 1 <= xx <= xmax:
                dev = abs(xx / den / target - 1)
                if best is None or dev < best[0]:
                    best = (dev, xx, k)
    return best


def test_the_exclusivity_scan_on_its_published_terms():
    """Four couplings, one wheel: only the electron's admits a small block."""
    aG_e = G_CODATA18 * M_E ** 2 / (HBAR * C)
    aG_p = G_CODATA18 * M_P ** 2 / (HBAR * C)
    aG_mu = G_CODATA18 * M_MU ** 2 / (HBAR * C)
    dev_e, x_e, k_e = _best_wheel(aG_e)
    dev_a, x_a, k_a = _best_wheel(ALPHA)
    dev_p, x_p, k_p = _best_wheel(aG_p)
    dev_m, x_m, k_m = _best_wheel(aG_mu)
    # the electron's wheel is the published one, at the published accuracy:
    assert (x_e, k_e) == (5, 151) and dev_e < 110e-6
    # the published runner-up forms and their fortyfold-worse deviations:
    assert (x_a, k_a) == (15, 11) and dev_a > 3000e-6
    assert (x_p, k_p) == (1, 127) and dev_p > 3000e-6
    assert (x_m, k_m) == (13, 137) and dev_m > 3000e-6
    assert min(dev_a, dev_p, dev_m) / dev_e > 30           # fortyfold, roughly


def test_the_hierarchy_number_reads_as_an_interval():
    """5/(2^151-1) = (5/4) x 2^-149: 149 octaves down, sharp by a just third."""
    assert F(5, 2 ** 151) == F(5, 4) * F(1, 2 ** 149)
    assert 149 == 151 - 2                                  # the third's two octaves
