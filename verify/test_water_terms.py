"""Pins for WATER ON DISCRETE TERMS (water_terms.py)."""

import math
from fractions import Fraction

from water_terms import tetrahedral_cos, ideal_ca_squared, mathieu_growth


def test_the_third_in_the_bond_angle():
    assert tetrahedral_cos() == Fraction(-1, 3)          # exact
    theta = math.degrees(math.acos(-1/3))
    assert abs(theta - 109.4712) < 1e-3


def test_the_same_third_in_the_stacking():
    assert ideal_ca_squared() == Fraction(8, 3)
    assert abs(math.sqrt(8/3) - 1.63299) < 1e-4


def test_water_answers_an_octave_below():
    # principal parametric resonance: drive at 2x natural -> growth
    # (surface answers at HALF the drive); drive at natural -> quiet
    resonant = mathieu_growth(2.0)
    off = mathieu_growth(1.0)
    assert resonant > 10.0                               # explosive growth
    assert off < 4.0                                     # weak secondary only
    assert resonant > off + 10.0                         # clean separation


def test_quiet_at_the_neighboring_ratios():
    # off the instability tongues entirely: no growth at all (2026-08-25)
    for om in (1.4, 2.6, 3.2):
        assert mathieu_growth(om) < 2.0


def test_the_hexad_of_ice_as_integer_arithmetic():
    """The hexagonal lattice's sixfold symmetry is an order-6 integer
    matrix, and its half turn is minus the identity (2026-08-25)."""
    def mul(A, B):
        return tuple(tuple(sum(A[i][k] * B[k][j] for k in range(2))
                           for j in range(2)) for i in range(2))
    M = ((1, -1), (1, 0))
    P = ((1, 0), (0, 1))
    powers = []
    for _ in range(6):
        P = mul(P, M)
        powers.append(P)
    assert powers[2] == ((-1, 0), (0, -1))               # the half turn is negation
    assert powers[5] == ((1, 0), (0, 1))                 # order six exactly
    assert all(Q != ((1, 0), (0, 1)) for Q in powers[:5])


def test_the_paper_carries_its_pins_and_its_gift():
    import pathlib
    doc = (pathlib.Path(__file__).resolve().parent.parent / "catalog"
           / "WATER-ON-DISCRETE-TERMS.md").read_text()
    flat = " ".join(doc.split())
    assert "cos θ = −1/3, exactly" in flat
    assert "√(8/3)" in flat
    assert "half the driving frequency" in flat
    assert "an octave divider" in flat
    assert "verify/test_water_terms.py" in flat
    for q in ("layering statistics", "octave test", "charge ledger",
              "two-state signature"):
        assert q.split()[0] in flat.lower()
    assert "stated falsification condition" in flat     # the four questions' form
    # the polar-flip sharpening (CC, 2026-08-25): four sign changes, one flip;
    # and the flip's anatomy matching the banked hexad transform (the Midy
    # half fixed, the triad orientation reversed — test_the_hexad_orientation)
    assert "four meters, one flip, four polarity reversals" in flat
    assert "fixes the two-structure and acts on the three-structure" in flat
    assert "intramolecular structure alone" in flat      # the reading's refutation
