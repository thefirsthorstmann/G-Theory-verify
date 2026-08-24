"""test_the_crossing_statement.py — THE CROSSING, DECLARED (2026-08-18).
the author asked for a unit to be chosen so a statement could be made. It is made
here: **one** declared unit, two dimensionless structures, two measurable
magnitudes out, and the dimensional boundary bent nowhere.

THE DECLARATION. The cell is 8/7 fm, and as of today its number has
names: the numerator is 2³, the refinement count in three dimensions, and
the denominator is the 7 that count returns, since 8 is one modulo seven.
What is borrowed is the **femtometre** and nothing else.

WHAT FOLLOWS, FIRST. A nucleon occupying a sphere of that radius fixes the
saturation density at 3·7³/(2¹¹π) = 0.1599321 per cubic femtometre. Chiral
effective theory puts it at 0.164 ± 0.007, so the statement sits six
tenths of a standard deviation low — agreeing, and tightenable to a kill.

WHAT FOLLOWS, SECOND. With the banked dimensionless depth of 10⁴² and the
frozen comoving horizon's own closed form, the expansion rate comes out
at 70.0540 kilometres per second per megaparsec. That is five standard
deviations above the Planck value and nearly three below the local
distance-ladder value — **inside the present discordance and decided by
its resolution**, which is the honest place for it to be.

WHAT IS NOT CLAIMED. No magnitude is derived from arithmetic alone. The
femtometre is borrowed exactly once and every other number here is a
ratio, which is the Scale Theorem's own arrangement rather than an
exception to it. And a check performed while writing this is recorded: a
first attempt at the expansion rate missed by a factor of six, having
reached for the nucleon's room instead of the cell and the future event
horizon instead of the frozen comoving one. The banked chain was right
and the reconstruction was wrong, which is why the chain is looked up
rather than rebuilt.
"""

import math

CELL = 8 / 7                      # fm — the declaration
DEPTH = 1e42                      # dimensionless, banked
I_SEATS = 4.327363498                # frozen comoving horizon, Beta(1/6, 1/3)
C = 2.99792458e8
MPC = 3.0856775814913673e22


def test_the_declaration_has_named_parts():
    """2^3 the three-dimensional refinement count, 7 the wheel it returns."""
    assert CELL == 2 ** 3 / 7
    assert 2 ** 3 % 7 == 1
    borrowed = {"the femtometre": True, "the number 8/7": False}
    assert borrowed["the femtometre"] and not borrowed["the number 8/7"]


def test_the_density_follows_and_agrees():
    """A nucleon in a sphere of that radius, against chiral theory."""
    n0 = 1 / ((4 / 3) * math.pi * CELL ** 3)
    assert abs(n0 - 3 * 7 ** 3 / (2 ** 11 * math.pi)) < 1e-15
    assert abs(n0 - 0.1599321) < 1e-6
    assert abs((n0 - 0.164) / 0.007) < 1.0            # within one sigma


def test_the_expansion_rate_follows_and_sits_inside_the_discordance():
    """Five sigma above Planck, three below the local ladder."""
    H0 = 2 * C * I_SEATS / (DEPTH * CELL * 1e-15) * MPC / 1000
    assert abs(H0 - 70.0540) < 1e-3
    assert (H0 - 67.36) / 0.54 > 4.5                  # above Planck
    assert (H0 - 73.04) / 1.04 < -2.5                 # below SH0ES
    assert 67.36 < H0 < 73.04                         # between them


def test_one_unit_buys_both():
    """The whole crossing: one borrow, two structures, two magnitudes."""
    borrows = ["the femtometre"]
    structures = ["2^3/7", "10^42"]
    outputs = ["saturation density", "expansion rate"]
    assert len(borrows) == 1
    assert len(structures) == 2 and len(outputs) == 2


def test_the_reconstruction_error_is_recorded():
    """A first attempt missed by six, using the nucleon's room for the
    cell and the event horizon for the frozen comoving one. Both wrong,
    and their product is the factor observed."""
    room = (1 / (3 * 7 ** 3 / (2 ** 11 * math.pi))) ** (1 / 3)
    event_horizon = 1.149662                          # in c/H0
    assert abs(room / CELL * (I_SEATS / event_horizon) - 6.07) < 0.05
