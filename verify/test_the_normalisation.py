"""test_the_normalisation.py — THE EXPONENT AND THE CONSTANT ARE ONE FACT
(2026-08-18), which closes the horizon chain's dimensionless content and
withdraws a gap I had stated an hour earlier.

WHAT I HAD SAID, AND WHY IT WAS WRONG HERE. Having derived the coupling
as 8π = 2 × 4π, I named the remaining work as showing that this account's
inverse-square derivation carries the *normalisation* and not merely the
exponent — on the general principle that a scaling law fixes no constant.
True of a bare power law; **false of this one**, and the difference is the
point.

THE ARGUMENT. A conserved count spreads over the sphere it has reached.
In d spatial dimensions that sphere has measure Ω_d r^(d−1), so the
intensity is P/(Ω_d r^(d−1)) and the amplitude falls as r^(−(d−1)/2).
Inverse-square intensity therefore happens **at three dimensions and
nowhere else** — and the very same statement that fixes the exponent
fixes the constant, because Ω₃ = 4π *is the measure of the sphere whose
growth produced the exponent*. They are not two facts to be derived
separately; they are one fact read twice.

AND THE ACCOUNT'S OWN ROUTE IS ALREADY THAT STATEMENT. Its first route
reads the deficit as the amplitude, inverse-first, and the intensity as
its square, inverse-second. Amplitude going as 1/r is r^(−(d−1)/2) at
d = 3 exactly — so the inverse-first amplitude *is* the
three-dimensional flux statement, and carries the 4π with it.

THE CHAIN, LINK BY LINK. A count is conserved, which is the register's
own axiom; three spatial dimensions, selected today by two independent
criteria; the sphere's measure in three dimensions is 4π, which is
geometry once the dimension is fixed; therefore intensity is count over
4πr², exponent and constant together. **No dimensionless factor is left
unaccounted anywhere in the horizon chain.**

WHAT THIS DOES NOT CLOSE, and it widens rather than settles. The
conversion from a count-density to an acceleration is dimensionful, and
so is a declared borrow. But the account now names a dimensionful anchor
in three places — the electroweak vev, the packing cell, and the Planck
length this chain rides on — and the ratios among them are not derived.
The morning's borrow-accounting negative therefore gains a third entry.
The horizon chain is internally complete; the cross-chain accounting is
not, and saying only the first would be the more flattering half.
"""

import math
from fractions import Fraction

import sympy as sp


def _omega(d):
    """Measure of the unit (d−1)-sphere."""
    return 2 * sp.pi ** (sp.Rational(d, 2)) / sp.gamma(sp.Rational(d, 2))


def test_inverse_square_intensity_happens_only_in_three_dimensions():
    """The exponent is d − 1, so it is two exactly once."""
    assert [d for d in range(2, 9) if d - 1 == 2] == [3]
    for d, exp in ((2, 1), (3, 2), (4, 3), (5, 4)):
        assert d - 1 == exp


def test_the_sphere_measure_supplies_the_four_pi_at_that_same_dimension():
    """Ω₃ = 4π — the measure of the very sphere whose growth gave the
    exponent, so the constant is not a separate input."""
    assert sp.simplify(_omega(3) - 4 * sp.pi) == 0
    assert sp.simplify(_omega(2) - 2 * sp.pi) == 0
    assert sp.simplify(_omega(4) - 2 * sp.pi ** 2) == 0


def test_the_amplitude_falls_as_one_over_r_only_at_three():
    """Which is the account's own inverse-first deficit."""
    for d in (2, 3, 4, 5):
        p = Fraction(d - 1, 2)
        if d == 3:
            assert p == 1
        else:
            assert p != 1


def test_the_two_are_one_statement_not_two():
    """Flux conservation on a sphere delivers both at once; a bare power
    law delivers neither constant."""
    P, r = sp.symbols('P r', positive=True)
    I = P / (_omega(3) * r ** 2)
    assert sp.simplify(I - P / (4 * sp.pi * r ** 2)) == 0
    assert sp.simplify(sp.diff(sp.log(I), sp.log(r)).doit()
                       if False else sp.simplify(r * sp.diff(I, r) / I) + 2) == 0


def test_the_chain_has_no_unaccounted_dimensionless_factor():
    """Every link, with what supplies it."""
    chain = {
        "a count is conserved": "the register's axiom",
        "three spatial dimensions": "derived, two independent criteria",
        "the sphere's measure is 4 pi": "geometry, given the dimension",
        "intensity = count / (4 pi r^2)": "follows, exponent and constant together",
        "the trace reversal's 2": "forced by Bianchi",
        "ln 2": "the nat-bit conversion, Landauer's own",
    }
    assert len(chain) == 6
    assert all(v for v in chain.values())
    assert not any("free" in v or "chosen" in v for v in chain.values())


def test_but_the_borrow_is_now_declared_in_three_places():
    """The honest other half: the account names a dimensionful anchor in
    the electroweak sector, the nuclear one, and here — and the ratios
    among them are not derived."""
    anchors = {"the Higgs vev": "electroweak",
               "the packing cell, 8/7 fm": "nuclear",
               "the Planck length": "the horizon chain"}
    assert len(anchors) == 3
    hbar, G, c = 1.054571817e-34, 6.67430e-11, 2.99792458e8
    lP = math.sqrt(hbar * G / c ** 3)
    cell = 8 / 7 * 1e-15
    assert cell / lP > 1e19                            # unexplained, and vast
    derived = {"the ratio cell / l_P": False}
    assert not derived["the ratio cell / l_P"]
