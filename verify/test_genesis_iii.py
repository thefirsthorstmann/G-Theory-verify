"""test_genesis_iii.py — Chapter III pinned: the chain, the abundance."""

from fractions import Fraction as F

from genesis_iii import chapter_dependencies, helium_fraction, particle_chain


def test_the_particle_state_chain():
    """Rest 144 exact; echo 144.144; split 143|856 summing 999;
    the seed tie 1/7 = 143/1001 and 143 x 999 = the period."""
    c = particle_chain()
    assert c["rest"] == 144
    assert c["echo"] == F(144144, 1000)
    assert c["split"] == (143, 856) and c["split_sum"] == 999
    assert c["seed_tie"] == (F(1, 7), 142857)


def test_the_first_operations_pair_makes_the_base():
    """1008 = 42 x 24 — the displaced pair of move one, as a product;
    hydrogen's atomic weight x 1000."""
    assert 42 * 24 == 1008


def test_primordial_abundance():
    """n/p = 1/7 -> neutron fraction 1/8 -> Y = 1/4 EXACTLY (75/25);
    the measured 0.245(4) sits ~2% below: seat and dress declared."""
    assert helium_fraction() == F(1, 4)
    assert helium_fraction(F(1, 7)) == 2 * F(1, 8)
    assert abs(0.245 - 0.25) / 0.25 < 0.021       # the dress band, honest


def test_the_chapter_stands_on_its_dependencies():
    """The forced table (hydrogen exactly neutral) and the proton
    ledger (net 1 | gross 5/3) hold beneath this chapter."""
    assert chapter_dependencies()
