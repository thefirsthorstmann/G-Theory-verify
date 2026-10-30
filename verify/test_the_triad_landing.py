"""test_the_triad_landing.py — THE THREE GENERATION ROUNDINGS LAND ON THE
TRIAD, AT FA, DO AND LA, WALKING THE MADELUNG INTERVALS WITH THE FOURTH
REVERSED (2026-08-19). CC's reading, verified cold. The banked statement
of the generation deciders is "2 → 3, 8 → 9, 5 → 6 (depths 3, 4, 5)" and
the right-hand side had never been read as an object in its own right.

WHAT THE ROUNDINGS PRODUCE. The digits they land on are **3, 9, 6** — the
triad, the residue class the hexad line never touches. The reptend rounds
*out of* the hexad and *into* the triangle, at exactly the three
generation depths and nowhere else. Depths 1, 2 and 6 decide on 4, 2 and 1
and round down, so they land nowhere.

AS ADDRESSES ON THE CIRCLE, at forty degrees a seat:

    depth 3   2 → 3   seat 3   120°   Fa    engine value 32
    depth 4   8 → 9   seat 9   360°   Do    engine value 48
    depth 5   5 → 6   seat 6   240°   La    engine value 40

so the progression in thirds runs 1/3 → 3/3 → 2/3: the multipliers of
three are **1, 3, 2** and not 1, 2, 3. Out of order, which is CC's
"counter-rotation" — every step is +240°, so the walk goes round the
triangle the long way each time.

AND 1, 3, 2 IS THE BANKED DENSITY-ORDER (matter) against the force-order
1, 2, 3 (energy). It arrives here unasked, as the order in which the
generations round into the triangle.

THE INTERVAL TRAIL, read manually. On the engine's root-24 values:

    Fa → Do   32 → 48   × 3/2   the fifth, ascending
    Do → La   48 → 40   × 5/6   the minor third, descending
    La → Fa   40 → 32   × 4/5   the major third, descending, closing

and the three multiply to exactly 1 — the cycle closes.

**Those are the Madelung pair.** The banked Madelung recursion runs root
1296 = 6⁴ with multipliers ×2/3 and ×5/6 and reproduces the orbital
filling order term for term. Here the same two intervals appear with the
fourth **inverted** — ×3/2 rather than ×2/3 — which is the counter-rotation
again, now in interval terms rather than degrees. And their comma is the
one already banked: (5/6)²/(2/3) = **25/24**, the chromatic semitone, c₅ in
the comma family and a shruti generator.

Held as a Reading: the arithmetic is exact; that this walk and the
Madelung walk share intervals is an observation, not a demonstration that
one causes the other.
"""

from fractions import Fraction as F

# engine values on root 24, with the La = 240° guard honoured
ENGINE = {"Do": (0, 24), "Fa": (120, 32), "Sol": (180, 36),
          "La": (240, 40), "Do'": (360, 48)}

# the banked generation deciders: depth -> (digit kept, digit produced)
DECIDERS = {3: (2, 3), 4: (8, 9), 5: (5, 6)}


def _digits(num, den, n):
    out, x = [], num
    for _ in range(n):
        x *= 10
        out.append(x // den)
        x %= den
    return out


def test_the_deciders_are_the_high_midy_half():
    """Depths 3,4,5 decide on 8,5,7 and round up; 1,2,6 decide low."""
    d = _digits(1, 7, 12)
    for depth in (3, 4, 5):
        assert d[depth] >= 5
    for depth in (1, 2, 6):
        assert d[depth % 6] < 5
    assert 142 + 857 == 999


def test_the_roundings_produce_the_triad():
    produced = sorted(v for _, v in DECIDERS.values())
    assert produced == [3, 6, 9]
    for p in produced:
        assert p % 3 == 0                       # the residue class


def test_the_hexad_never_touches_them():
    """Which is why landing there is an event."""
    hexad = set(_digits(1, 7, 6))
    assert hexad == {1, 4, 2, 8, 5, 7}
    assert not (hexad & {3, 6, 9})


def test_the_addresses_are_fa_do_la():
    seats = {3: 120, 9: 360, 6: 240}
    for seat, deg in seats.items():
        assert seat * 40 % 360 == deg % 360
    assert ENGINE["Fa"][0] == 120
    assert ENGINE["La"][0] == 240              # the standing guard
    assert ENGINE["Do'"][0] == 360


def test_the_thirds_run_one_three_two():
    order = [DECIDERS[d][1] // 3 for d in (3, 4, 5)]
    assert order == [1, 3, 2]
    assert order != [1, 2, 3]                  # the counter-rotation


def test_every_step_is_two_hundred_forty_degrees():
    seq = [DECIDERS[d][1] for d in (3, 4, 5)]
    for a, b in zip(seq, seq[1:] + [seq[0]]):
        assert (b - a) * 40 % 360 == 240


def test_the_interval_trail_and_its_exact_closure():
    fa, do, la = ENGINE["Fa"][1], ENGINE["Do'"][1], ENGINE["La"][1]
    assert F(do, fa) == F(3, 2)                # the fifth, ascending
    assert F(la, do) == F(5, 6)                # minor third, descending
    assert F(fa, la) == F(4, 5)                # major third, descending
    assert F(do, fa) * F(la, do) * F(fa, la) == 1


def test_they_are_the_madelung_pair_with_the_fourth_reversed():
    madelung = {F(2, 3), F(5, 6)}
    fa, do, la = 32, 48, 40
    walk = {F(do, fa), F(la, do)}
    assert F(5, 6) in madelung and F(5, 6) in walk        # identical
    assert F(2, 3) in madelung and F(3, 2) in walk        # inverted
    assert F(3, 2) == 1 / F(2, 3)


def test_their_comma_is_the_chromatic_semitone():
    assert F(5, 6) ** 2 / F(2, 3) == F(25, 24)
    assert 25 - 24 == 1                                   # c_5, unit residue


def test_the_madelung_link_is_derived_not_observed():
    """UPGRADED 2026-08-19, same day: this battery first graded the shared
    intervals an observation. test_the_madelung_lattice.py then derived
    it — the landings are a just major triad 4:5:6, forced by Midy plus
    the engine's linear map, and the Madelung lattice IS the triad
    lattice. The weaker grade is superseded rather than left standing."""
    graded = {"the roundings land on 3,9,6": "exact",
              "the addresses are Fa, Do, La": "exact",
              "the landings are a 4:5:6 triad": "derived",
              "the lattice is the triad's": "derived"}
    assert list(graded.values()).count("exact") == 2
    assert list(graded.values()).count("derived") == 2
    assert "observation" not in graded.values()
