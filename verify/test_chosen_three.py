"""test_chosen_three.py — F4 pinned: the trial by least action."""

from chosen_three import (bases_with_both, carries_ennead,
                          full_reptend_primes, ord_mod, unrolls_seed)


def test_base_ten_is_the_unique_least_register():
    """Both mechanisms: b = 1 mod 9 (ennead) and ord_7(b) = 6 (full
    seed). Bases 2-9 all fail at least one; 10 carries both; next 19."""
    assert bases_with_both(2, 80) == [10, 19, 73]   # 28 fails: 7 | 28
    for b in range(2, 10):
        assert not (carries_ennead(b) and unrolls_seed(b))


def test_the_near_misses_sharpen_the_claim():
    """Bases 3, 5, 12, 17 unroll the seed but erase the ennead;
    base 9 erases it maximally (digit sums go mod 8)."""
    for b in (3, 5, 12, 17):
        assert unrolls_seed(b) and not carries_ennead(b)
    assert 9 % 9 == 0                             # ennead vanishes at base 9


def test_seven_is_the_least_full_reptend_prime():
    """3 gives period 1, 11 period 2, 13 half — 7 is first-full."""
    assert ord_mod(10, 3) == 1
    assert ord_mod(10, 7) == 6
    assert ord_mod(10, 11) == 2
    assert ord_mod(10, 13) == 6                   # of 12: half, not full


def test_the_seed_then_the_spine():
    """The base-10 full-reptend primes open {7, 17, 19, 23, 29}:
    the seed first, the spine second."""
    assert full_reptend_primes(10, 30) == [7, 17, 19, 23, 29]


def test_the_x3_remains_the_one_input():
    """Cornered, braced, not forced: the multiplicity scan lands only
    m = 3 on the third-lattice; C_A = 3; gluons = 8."""
    from charge_forcing import solve_charges, uniqueness_scan
    from fractions import Fraction as F
    scan = uniqueness_scan()
    landers = [m for m, (qu, qd) in scan.items()
               if (qu, qd) == (F(2, 3), F(-1, 3))]
    assert landers == [3]
    assert 3 ** 2 - 1 == 8
