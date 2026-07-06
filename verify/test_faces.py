"""test_faces.py — Phase A2: the workless/working classification, pinned.

THE CRITERION (exact): an operation is WORKLESS (M-face) iff it is
INVERTIBLE — it turns, permutes, or re-phases, losing nothing; it is
WORKING (E-face) iff it is NON-INVERTIBLE — it rounds, truncates, or
reads, manufacturing excess and destroying information.

Corollaries pinned here:
  * conservation laws live with the invertible operations;
  * the arrow of time is the stack of irreversible roundings —
    the workless clock ticks reversibly; the carries accumulate.
"""

from fractions import Fraction as F

from gtheory import round_at, transform
from polar_wave import born, clock, shift, tick


# ---- the M-face: invertible / workless -------------------------------------

def test_transform_is_an_involution():
    """142857 -> 124875 -> 142857: the duality rotation undoes itself."""
    out = transform("142857")["out"]
    assert out == "124875"
    assert transform(out)["out"] == "142857"


def test_tick_is_invertible():
    """rate-3 tick has the rate-5 inverse (3 + 5 = 8 = 0 on the ring)."""
    psi = [(k + 1, (3 * k) % 8) for k in range(8)]
    assert tick(tick(psi, 3), 5) == psi


def test_shift_and_clock_are_invertible():
    psi = [(k + 2, (5 * k) % 8) for k in range(8)]
    assert shift(shift(shift(shift(shift(shift(shift(shift(psi)))))))) == psi
    c = psi
    for _ in range(8):
        c = clock(c)
    assert c == psi                                  # clock^8 = identity


def test_bounce_is_a_translation():
    """75 -> 72 and 24 -> 27: +-3 translations — invertible arithmetic."""
    assert 72 + 3 == 75 and 27 - 3 == 24


# ---- the E-face: non-invertible / working ----------------------------------

def test_rounding_collides():
    """Distinct values, one rounded output: information destroyed."""
    assert round_at(F("0.1449"), 2) == round_at(F("0.1440"), 2) == F("0.14")


def test_digit_root_collides():
    """The cascade endpoint is many-to-one: the mass-sign operation works."""
    from gtheory import dr
    assert dr(6) == dr(15) == dr(24) == 6


def test_born_collides():
    """The readout is many-to-one (already the phase-blind theorem)."""
    a = [(2, 0), (3, 1)]
    b = [(2, 3), (3, 5)]
    assert a != b and born(a) == born(b)
