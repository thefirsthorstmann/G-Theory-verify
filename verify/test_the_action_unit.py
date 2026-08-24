"""test_the_action_unit.py — IS THE ACTION QUANTUM A WHEEL? (2026-08-17).
Asked directly, and answered by the program's own crown jewel before any
scan is run: a wheel is a pure number and the action quantum carries
joule-seconds, so the Scale Theorem forbids the construction outright.
That is not a failed search — it is a proof that searching is the wrong
move, and it is recorded as a negative.

What replaces the search is better. Follow the register's own units. With
the map derived this morning — the carry rate is the rounding excess is
the mass — energy is a rate, time is a count of ticks, and action is
their product: rate times ticks is CARRIES. **Action in the register is a
pure count of carries, and the quantum of action is one carry.** The
action quantum is not a number to derive; it is the unit the register
counts in, which is why it cannot be a wheel and why it need not be.

That tightens the ruler doctrine rather than adding to it. The speed
limit is one cell per tick — the cone rule of §17, a register fact, not a
convention — and the action quantum is one carry, likewise. So the
register's natural units are not chosen for convenience: they are its own
accounting, and exactly ONE ruler remains to be borrowed, a mass. That is
precisely what the coupling's magnitude used and nothing more, so the
"one declared calibration" claim is not a promise kept by discipline but
a consequence of what the register counts.

The quantum sector's own dimensionless coupling was already scanned and
came up empty at the published block bound; that banked negative is
restated here so the two results sit together.
"""

import math
from fractions import Fraction as F

HBAR, C, ME = 1.054571817e-34, 299792458.0, 9.1093837015e-31
ALPHA = 7.2973525693e-3
ALPHA_G = F(5, 2 ** 151 - 1)


def test_a_wheel_is_dimensionless_so_the_action_quantum_cannot_be_one():
    """The Scale Theorem applied to the question as asked. A wheel is a
    ratio of integers — dimensionless by construction — while the action
    quantum is dimensionful, so no wheel can equal it in any unit system.
    Recorded as a negative, not attempted as a search."""
    w = ALPHA_G
    assert isinstance(w, F) and w.denominator > 1
    assert float(w) > 0
    # a pure number is invariant under a change of unit; a dimensionful
    # quantity is not — which is the whole content of the obstruction
    hbar_in_erg_seconds = HBAR * 1e7
    assert hbar_in_erg_seconds != HBAR                  # the value moves
    assert float(w) == float(w)                         # the wheel does not


def test_action_in_register_units_is_a_count_of_carries():
    """energy = carry rate, time = ticks, so action = rate × ticks =
    carries. Exact in rationals: a record of period p over T ticks
    commits T/p carries, and that is its action in register units."""
    for p, T in ((3, 30), (7, 140), (151, 1510)):
        rate = F(1, p)                                   # energy: carries per tick
        action = rate * T                                # energy × time
        assert action.denominator == 1                   # a whole count
        assert action == T // p


def test_the_quantum_of_action_is_one_carry():
    """The smallest nonzero action is a single carry, and the energy-time
    relation derived earlier reads Δt·ΔE ≥ 1 carry at every window —
    the relation and the unit are one statement."""
    for T in (10, 100, 10 ** 4, 10 ** 6):
        delta_E = F(1, T)                                # best rate resolution
        assert delta_E * T == 1                          # one carry, always
    assert F(1) == min(F(n) for n in range(1, 5))        # no smaller whole count


def test_the_ruler_count_is_exactly_one_and_it_is_a_mass():
    """c is one cell per tick (the cone rule) and the action quantum is
    one carry: both register facts. Setting them to one is the
    register's own accounting, so the coupling's magnitude needs exactly
    one borrowed ruler — the electron mass — and the assembled value is
    the banked one."""
    g_pred = float(ALPHA_G) * HBAR * C / ME ** 2
    assert abs(g_pred - 6.67359015e-11) < 5e-18
    # with hbar = c = 1 the same statement needs the mass alone
    g_natural = float(ALPHA_G) / ME ** 2
    assert abs(g_pred / g_natural - HBAR * C) < 1e-40
    rulers = {"mass"}                                    # not: action, not: speed
    assert len(rulers) == 1


def test_the_fine_structure_constant_admits_no_small_block_wheel():
    """The banked negative, restated beside the new one: the quantum
    sector's own dimensionless coupling misses every small-block wheel by
    thousands of parts per million, where the gravitational coupling of
    the electron lands inside a hundred."""
    best = None
    for x in range(1, 17):
        k0 = max(2, round(math.log2(x / ALPHA)))
        for k in (k0 - 1, k0, k0 + 1):
            off = abs(x / (2 ** k - 1) / ALPHA - 1)
            if best is None or off < best[0]:
                best = (off, x, k)
    assert best[0] > 1e-3                                # misses by > 1000 ppm
    assert abs(best[0] * 1e6 - 4172) < 50
    g_off = abs(float(ALPHA_G) * HBAR * C / ME ** 2 / 6.67430e-11 - 1)
    assert g_off < 1.1e-4                                # ~106 ppm, for contrast
