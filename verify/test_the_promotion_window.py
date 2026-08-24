"""test_the_promotion_window.py — THE WINDOW CHARACTERISED (2026-08-18).
The dimensional account asks a stated yes-or-no question: why does the
register's contact structure realise the ladder at dimensions two, three
and four and not elsewhere. This does not answer it from cell mechanics —
it characterises the window in the program's own arithmetic, which moves
the question one step nearer the register and is graded as that and not
more.

THE CHARACTERISATION. Across dimensions one to eight the contact counts
are 2, 6, 12, 24, 40, 72, 126, 240. In exactly dimensions two, three and
four — and nowhere else — the count equals **3·2^(d−1)**: three times a
power of two, the program's two generators and nothing besides. Outside
the window a foreign prime enters immediately: forty carries a five, one
hundred twenty-six a seven, two hundred forty a five again. Note the test
is stricter than mere smoothness, since seventy-two at dimension six is
itself a two-three word yet does not take the form.

AND THE RATIO IS THE FIFTH. The register refines a cell into 2^d children
— banked, eight in three dimensions, the same count that regulates the
cascade — so in the window the contact count is exactly three halves of
the child count, at every one of the three dimensions and at none of the
others. The window is where contact and refinement stand a fifth apart.

WHAT IT IS: a characterisation. The promotion question sharpens from "why
does the ladder promote at two, three and four" to "why is contact three
halves of refinement there." WHAT IT IS NOT: a derivation from carry,
union and cell mechanics, which the account still owes. Both physical
slots sit inside the window — twelve in space, twenty-four in spacetime —
with the window's own edges at two and four.
"""

CONTACT = {1: 2, 2: 6, 3: 12, 4: 24, 5: 40, 6: 72, 7: 126, 8: 240}


def _factors(n):
    out, m, d = [], n, 2
    while d * d <= m:
        while m % d == 0:
            out.append(d)
            m //= d
        d += 1
    if m > 1:
        out.append(m)
    return out


def test_the_window_is_exactly_two_three_four():
    """The form 3·2^(d−1) holds at those three dimensions and nowhere
    else in the tested range."""
    window = [d for d in CONTACT if CONTACT[d] == 3 * 2 ** (d - 1)]
    assert sorted(window) == [2, 3, 4]
    assert CONTACT[1] == 2 and 3 * 2 ** 0 == 3            # one misses
    assert CONTACT[5] == 40 and 3 * 2 ** 4 == 48          # five misses


def test_outside_the_window_a_foreign_prime_enters():
    """The window is where the contact count stays inside the program's
    own arithmetic; beyond it a five or a seven appears."""
    for d in (2, 3, 4):
        assert set(_factors(CONTACT[d])) <= {2, 3}, d
    for d, prime in ((5, 5), (7, 7), (8, 5)):
        assert prime in _factors(CONTACT[d]), d


def test_the_test_is_stricter_than_smoothness():
    """Dimension six's seventy-two is a two-three word yet fails the
    form, so the window is not merely 'where the count is smooth'."""
    assert set(_factors(CONTACT[6])) <= {2, 3}
    assert CONTACT[6] != 3 * 2 ** 5
    assert CONTACT[6] == 72 and 3 * 2 ** 5 == 96


def test_the_ratio_to_refinement_is_the_fifth():
    """The register refines a cell into 2^d children; in the window the
    contact count is exactly three halves of that, and at no other
    dimension."""
    for d in (2, 3, 4):
        assert CONTACT[d] * 2 == 3 * 2 ** d
        assert abs(CONTACT[d] / 2 ** d - 1.5) < 1e-12
    for d in (1, 5, 6, 7, 8):
        assert abs(CONTACT[d] / 2 ** d - 1.5) > 1e-9


def test_both_physical_slots_sit_inside_the_window():
    """Twelve in space and twenty-four in spacetime, with the window's
    own edges at two and four — so the dimensions the account needs are
    interior to the characterisation rather than assumed into it."""
    assert CONTACT[3] == 12 and CONTACT[4] == 24
    window = [d for d in CONTACT if CONTACT[d] == 3 * 2 ** (d - 1)]
    assert 3 in window and 4 in window
    assert min(window) == 2 and max(window) == 4
    assert CONTACT[4] == 2 * CONTACT[3] == 4 * CONTACT[2]      # the doubling
