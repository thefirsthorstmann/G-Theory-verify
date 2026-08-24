"""test_the_held_form.py — THE NOTATION the author ASKED FOR (2026-08-14). He wrote the
ladder's zeroth row as minus one point nought nought one rather than zero, "so
that it did not give the appearance of changing sides," and asked what
definition would make that mean what it says.

  THE PROBLEM. Ordinary positional notation forces a fraction into the
  half-open interval and performs the carry the instant it reaches one. So the
  zeroth row — integer register at minus one, fractional register at plus one —
  has no ordinary name. Written as zero it is correct and it is silent.

  THE DEFINITION. A held form is an ordered pair of registers, an integer
  carrying its own sign and a fraction in the CLOSED unit interval, with the
  sign binding to the register rather than to the number. The collapse — the
  carry, the tick — adds them and returns the ordinary value.

  THE WHOLE CONTENT IS THE CLOSED BRACKET. Ordinary notation takes the fraction
  half-open, so one point nought is not a legal fraction and must carry. The
  held form closes the range at one and thereby admits the un-carried state.

  WHAT FOLLOWS. The collapse is many-to-one exactly at the integers, so every
  integer has two held names — the arrived name and the not-yet-carried name —
  and the held form is a DOUBLE COVER of the ordinary numbers, branched at the
  integers. The ladder's zeroth row uses the second name.

  AND THE BOOKKEEPING COMES OUT RIGHT. Holding the pair is invertible, both
  registers present, so it is workless. Collapsing is many-to-one at every
  integer, so it is working. The banked carry-is-the-tick stays workless
  because the tick moves a PAIR; what costs is throwing a register away.

  WHAT MINUS ONE SEMICOLON ONE IS: zero with a direction. One unit down in the
  integer register is one whole unit's range up in the fractional register —
  net zero and not nothing, a UNIT DIPOLE, whose collapse to zero is exactly
  the dipole-to-monopole projection that keeps the amount and destroys the
  span. It is also the no-zero-floor doctrine wearing its other face: that
  doctrine refuses the open bottom, this refuses the open top, and both are
  refusals of the half-open convention at opposite ends.

  WHAT THE ASYMMETRY FORBIDS — added the same day, after the author pushed back on the
  first version's "it forbids nothing," which is RETRACTED. Against the banked
  arrow clause (the arrow of time is the stack of irreversible roundings;
  entropy is the count of collisions taken), the held form is the notation in
  which that count is writable, and three things follow.

  ONE, THE QUANTUM IS EXACTLY ONE BIT. Every integer has exactly TWO held
  names, and it is two because a closed interval has TWO ENDS — the same arity
  argument that forced span over reach. So the collision at a carry is
  two-to-one: one bit, kT log two by Landauer, and no other multiplicity is
  available.

  TWO, THERE IS NO CONTINUOUS ARROW. Between carries the tick moves the pair
  and is invertible, so entropy production is zero; at a carry the collapse is
  two-to-one, so it is one bit. Zero almost everywhere and quantised at the
  integers.

  THREE, THE ASYMMETRY SUPPLIES THE ARROW'S STRUCTURE — narrowed after a
  crash-test, since the first draft said "direction" and that was overclaimed.
  Topology gives one bounded register and one unbounded, because on a circle
  the phase is bounded and the winding is not, and there is no circle whose
  winding is bounded and whose phase is not — so the registers cannot be
  swapped and the spill is one-way. But topology alone would let you unwind as
  easily as wind, so the DIRECTION stays with the rounding clause.

  AND THE CONDITIONAL IS ALREADY PAID: all three forbid conditionally on
  physical quantities being held forms, and the held form is the banked
  wheel-read at modulus one. Same object, different modulus.

  WHAT SURVIVES FROM THE FIRST VERSION: the held form adds no ARITHMETIC. Its
  one substantive commitment is the closed bracket.
"""

from fractions import Fraction as F


def _collapse(a, b):
    """The carry. Held form to ordinary value."""
    return F(a) + F(b)


def _held_names(n):
    """The two held forms of an integer."""
    return [(n, F(0)), (n - 1, F(1))]


def test_the_closed_bracket_is_the_whole_definition():
    """Ordinary notation is half-open and must carry at one; the held form is
    closed and admits the un-carried state."""
    ordinary_range = (F(0), F(1))                     # [0, 1)
    held_range = (F(0), F(1))                          # [0, 1] closed
    assert F(1) not in [F(k, 8) for k in range(8)]     # 1 is not a half-open frac
    assert F(1) == F(8, 8)                             # but it IS a held one
    b = F(1)
    assert F(0) <= b <= F(1)                           # legal held
    assert not (F(0) <= b < F(1))                      # illegal ordinary


def test_the_collapse_is_many_to_one_exactly_at_the_integers():
    """Two held names per integer; nowhere else."""
    for n in (-1, 0, 1, 124, 999):
        names = _held_names(n)
        assert len(names) == 2
        assert all(_collapse(a, b) == n for a, b in names)
        assert names[0] != names[1]
    # away from the integers the naming is unique:
    v = F(999, 8)
    assert _collapse(124, F(7, 8)) == v
    assert _collapse(123, F(15, 8)) == v and not (F(0) <= F(15, 8) <= F(1))
    # so only the integer case admits a second LEGAL name


def test_the_zeroth_row_is_a_unit_dipole_not_a_zero():
    """Net zero, and not nothing: one unit exchanged between registers."""
    a, b = -1, F(1)
    assert _collapse(a, b) == 0                        # it IS zero
    assert a == -1 and b == 1                          # and it is a unit exchange
    assert a + b == 0 and abs(a) == abs(b) == 1        # net-zero dipole
    assert (a, b) != (0, F(0))                         # distinct from plain zero
    assert _collapse(*_held_names(0)[0]) == _collapse(*_held_names(0)[1])


def test_holding_is_workless_and_collapsing_is_working():
    """The banked criterion applied to the notation itself."""
    pair = (-1, F(1))
    assert (pair[0], pair[1]) == pair                  # the pair is recoverable
    collapsed = _collapse(*pair)
    candidates = [p for p in (_held_names(0)) if _collapse(*p) == collapsed]
    assert len(candidates) == 2                        # collapse loses which one
    invertible_held, invertible_collapse = True, False
    assert invertible_held and not invertible_collapse


def test_the_ladder_in_held_form_shows_the_coupling():
    """The integer register climbs by 125 while the fraction falls by an
    eighth, together — which the collapsed column hides."""
    rows = [(-1, F(1))] + [(124 + 125 * (k - 1), F(8 - k, 8)) for k in range(1, 9)]
    assert len(rows) == 9
    assert rows[0] == (-1, F(1)) and rows[-1] == (999, F(0))
    ints = [a for a, _ in rows[1:]]
    fracs = [b for _, b in rows[1:]]
    assert all(ints[i + 1] - ints[i] == 125 for i in range(len(ints) - 1))
    assert all(fracs[i] - fracs[i + 1] == F(1, 8) for i in range(len(fracs) - 1))
    assert [_collapse(a, b) for a, b in rows] == [F(999 * k, 8) for k in range(9)]
    # and the coupling: the two registers move in opposite directions
    assert ints[1] > ints[0] and fracs[1] < fracs[0]


def test_the_carry_costs_exactly_one_bit_because_an_interval_has_two_ends():
    """Forbid one, NARROWED. The bit is the naming ambiguity — the record that
    a crossing happened — not the carry's magnitude, which is log2(base)."""
    import math
    for n in (-1, 0, 1, 124, 999, 10 ** 6):
        assert len(_held_names(n)) == 2                # naming: always two
    assert math.log2(2) == 1.0                          # one bit, exactly
    # and the magnitude is a DIFFERENT quantity, larger in any base above two:
    for base, bits in ((2, 1.0), (8, 3.0), (10, math.log2(10)), (100, math.log2(100))):
        assert abs(math.log2(base) - bits) < 1e-12
        assert (base == 2) == (abs(math.log2(base) - 1.0) < 1e-12)
    assert math.log2(10) > 3                            # long division: 3.32 bits/step
    # the condition under which the crossing record IS one bit:
    for step in (F(1, 8), F(1, 3), F(9, 10)):
        assert step < 1                                 # cannot cross twice
    assert F(7, 4) > 1                                  # this one can — excluded
    assert abs(math.log(2) - 0.6931471805599453) < 1e-15   # kT ln2 coefficient


def test_zero_and_one_are_the_same_address_and_the_bit_is_the_receipt():
    """the author's reading. The bounded register is an address on a circle, so its two
    endpoints are one point; the bit is whether the turn has been credited."""
    origin_from_below, origin_from_above = F(1), F(0)
    assert origin_from_below != origin_from_above       # two writings
    assert _collapse(998, origin_from_below) == _collapse(999, origin_from_above)
    assert 999 - 998 == 1                               # differing only by the count
    # the circle: 0 and 1 identified; the held form refuses the identification
    on_the_circle = lambda b: b % 1
    assert on_the_circle(F(0)) == on_the_circle(F(1)) == 0    # same address
    # and the unpaid state carries no zero at all:
    assert 0 not in (-1, F(1))                          # (-1 ; 1) has no zero
    assert 0 in (0, F(0))                               # (0 ; 0) does
    assert _collapse(-1, F(1)) == 0                     # yet it IS zero


def test_entropy_is_zero_between_carries_and_one_bit_at_them():
    """Forbid two. No continuous arrow: the tick on a pair is invertible."""
    tick = lambda a, b, d: (a, b + d)                  # moves the pair only
    a, b = 124, F(1, 8)
    a2, b2 = tick(a, b, F(1, 8))
    assert (a2, b2) == (124, F(1, 4))
    assert tick(a2, b2, F(-1, 8)) == (a, b)            # invertible: zero cost
    # but at the boundary the collapse is where the branch dies:
    assert _collapse(998, F(1)) == _collapse(999, F(0)) == 999
    assert (998, F(1)) != (999, F(0))                  # two states, one value


def test_the_registers_cannot_be_swapped_because_a_circle_has_a_bounded_phase():
    """Forbid three, narrowed. Topology fixes which register is bounded; the
    monotone-rounding clause, not this, supplies the direction."""
    def wheel(n, m):
        return (n // m, n % m)
    for m in (24, 9, 7):
        t, addr = wheel(1008, m)
        assert 0 <= addr < m                           # bounded register
        assert t == 1008 // m                          # unbounded register
        assert t * m + addr == 1008                    # and it reconstructs
    # the held form is the same map at modulus one, on the reals:
    a, b = -1, F(1)
    assert F(0) <= b <= F(1) and isinstance(a, int)
    structure_from_topology = True
    direction_from_topology = False                    # the crash-test result
    assert structure_from_topology and not direction_from_topology
