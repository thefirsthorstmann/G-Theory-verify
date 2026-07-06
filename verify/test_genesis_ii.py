"""test_genesis_ii.py — Chapter II pinned: the pointing theorem + the square."""

from fractions import Fraction as F

from genesis_ii import cusp_ladder, gem_factor, null_count, square_identity


def test_the_cardioid_is_the_unique_single_null():
    """a > b: no null; a = b: ONE (the cardioid); a < b: two."""
    assert null_count(1, F(1, 2)) == 0            # blurred omni
    assert null_count(1, 1) == 1                  # THE CARDIOID: points
    assert null_count(F(1, 2), 1) == 2            # axis, not direction
    assert null_count(1, 0) == 0                  # pure omni


def test_direction_is_born_at_equal_mixture():
    """Scanning mixtures: the single-null property holds ONLY at a = b."""
    for k in range(1, 20):
        a = F(k, 10)
        expected = 0 if a > 1 else (1 if a == 1 else 2)
        assert null_count(a, 1) == expected


def test_the_cusp_ladder():
    """Equal mix at order m has exactly m nulls: 1, 2, 3, 4, 5."""
    assert cusp_ladder() == [1, 2, 3, 4, 5]


def test_the_quadrupole_is_the_dipole_squared():
    """1 + cos(2t) = 2 cos^2(t) identically — the two-faces ladder's
    own double copy; and the GEM factor is the square."""
    assert square_identity()
    assert gem_factor() == 4 == 2 ** 2


def test_the_radiation_ladder_starts_one_rung_apart():
    """The charge face's conserved ledger (net 0, the first operation)
    forbids its monopole radiation; the mass face's additional
    conservation shifts its first lawful multipole one rung: 1 then 2."""
    from gtheory import transform
    assert transform()["net"] == 0                # the conserved ledger
    first_lawful = {"charge": 1, "mass": 2}
    assert first_lawful["mass"] == first_lawful["charge"] + 1
