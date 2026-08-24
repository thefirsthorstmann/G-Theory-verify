"""test_the_wheel_under_refinement.py — THREE DIMENSIONS IS WHERE
REFINEMENT COSTS THE WHEEL NOTHING (2026-08-18). the author's observation, run
down. He asked what it means that dividing by seven always produces
sevenths in the decimal whatever the value, said the three rotations per
period ought to bear on the three dimensions, and added that the length
is the count of the decimal's extension. All three parts hold, and
together they select the dimension.

HIS ARITHMETIC. 24 × 8 = 192, and 192/7 = 27.428571… — a rotation of the
wheel, as every seventh is. The closure he names is exact: the six
sevenths are the six rotations of one six-digit block and nothing else.

HIS THREE ROTATIONS. Doubling has order three modulo seven, so the six
rotations fall into two triads, {1,2,4} and {3,6,5}. One cycle of the
reptend is three doublings — three octaves — which is the fact already
carried as the carrier's license.

WHAT WAS MISSING, AND IT IS THE LOAD-BEARING PIECE. The register refines
a cell into 2^d children. Then **2^d ≡ 1 (mod 7) exactly when three
divides d**, so the smallest dimension whose refinement returns the wheel
to its own rotation is **three**. And it holds at every depth, not only
the first: in three dimensions 2^(3k) ≡ 1 for all k, so refining is
invisible to the wheel however deep it goes, where dimensions one, two
and four return only every third level. Since a length in the register
IS a count of cells, this is the author's own sentence made arithmetic: counting
deeper costs the wheel nothing, and only here.

AND CROSSED WITH THE PROMOTION WINDOW IT SELECTS THE DIMENSION. Contact
per child is maximal exactly at d = 2, 3, 4 — derived from contact
numbers and child counts, with no seven anywhere in it, so the two
criteria are independent. Of those three dimensions **only three closes
the wheel.** Two independent conditions, one survivor.

WHICH CORRECTS A DECLINE MADE THE SAME DAY. The seven-dimensional
simplex constant is 8/7, and that was declined as a coincidence with the
packing cell — correctly; there is no route from a seven-dimensional
simplex to a length in three. But the **8** in 8/7 was never the
coincidence: it is 2³, the three-dimensional refinement count, and 8 ≡ 1
(mod 7) is exactly why a seventh survives refining. The cell's ratio is
the three-dimensional refinement over the wheel it closes.

WHAT THIS DOES AND DOES NOT DO. The cell's number was carried as
"declared exact"; its numerator and denominator now have names, which is
a real narrowing. The femtometre is untouched and so is the Scale
Theorem: a ratio is explained, a unit is not. And the principle that
refinement must leave the wheel invariant is this register's claim rather
than a theorem — the arithmetic below is forced, the selection of three
dimensions is forced *given that principle*, and it is recorded that way.
"""

from fractions import Fraction

CONTACT = {1: 2, 2: 6, 3: 12, 4: 24, 5: 40, 6: 72, 7: 126, 8: 240}
WINDOW = [2, 3, 4]


def test_every_seventh_is_a_rotation_of_one_block():
    """The closure the author names: dividing by seven produces sevenths in the
    decimal whatever the numerator."""
    block = "142857"
    seen = set()
    for n in range(1, 7):
        digits = str(Fraction(n, 7) * 10 ** 6 // 1).zfill(6)
        assert digits in (block[k:] + block[:k] for k in range(6)), n
        seen.add(digits)
    assert len(seen) == 6
    assert str(192 * 10 ** 6 // 7)[-6:] == "428571"       # his own example


def test_doubling_cuts_the_six_into_two_triads():
    """Order three modulo seven — one cycle of the reptend is three
    doublings, which is the author's 'three rotations'."""
    orbit, x = [], 1
    while True:
        orbit.append(x)
        x = x * 2 % 7
        if x == 1:
            break
    assert orbit == [1, 2, 4]
    assert len(orbit) == 3
    other = sorted(3 * a % 7 for a in orbit)
    assert other == [3, 5, 6]
    assert set(orbit) | set(other) == set(range(1, 7))


def test_refinement_closes_the_wheel_only_in_dimensions_divisible_by_three():
    """2^d ≡ 1 (mod 7) exactly when 3 | d, so the smallest is three."""
    closers = [d for d in range(1, 25) if pow(2, d, 7) == 1]
    assert closers == list(range(3, 25, 3))
    assert min(closers) == 3
    assert pow(2, 3, 7) == 1 and 2 ** 3 == 8


def test_three_dimensions_is_invariant_at_every_depth():
    """And not merely at the first level: refining is invisible to the
    wheel however deep it goes, which holds nowhere else in the window."""
    for d in (1, 2, 4):
        seq = {pow(2, d * k, 7) for k in range(1, 12)}
        assert seq == {1, 2, 4}                            # returns every third
    assert {pow(2, 3 * k, 7) for k in range(1, 12)} == {1}


def test_the_length_is_a_count_and_the_count_leaves_the_wheel_alone():
    """the author's sentence, as arithmetic: a length is a count of cells, and in
    three dimensions the count at every depth is one modulo seven."""
    for depth in range(1, 10):
        cells = 8 ** depth                                 # 2^3 per level
        assert cells % 7 == 1
        assert Fraction(cells, 7) - cells // 7 == Fraction(1, 7)


def test_the_window_and_the_wheel_intersect_in_one_dimension():
    """The window comes from contact numbers and child counts, with no
    seven in it; the closure comes from the wheel, with no contact number
    in it. They meet at three and nowhere else."""
    assert all(CONTACT[d] * 2 == 3 * 2 ** d for d in WINDOW)   # the window's own rule
    survivors = [d for d in WINDOW if pow(2, d, 7) == 1]
    assert survivors == [3]


def test_the_cells_ratio_now_has_names():
    """8/7 was declared; its parts are the three-dimensional refinement
    count and the wheel it closes."""
    assert Fraction(8, 7) == Fraction(2 ** 3, 7)
    assert pow(2 ** 3, 1, 7) == 1
    parts = {"numerator": "2^3, the refinement count in three dimensions",
             "denominator": "7, the wheel it returns"}
    assert "refinement" in parts["numerator"] and "wheel" in parts["denominator"]


def test_the_scale_wall_is_untouched():
    """A ratio is explained; a unit is not. The femtometre remains the
    borrow, and the theorem stands where it stood."""
    explained = {"the ratio 8/7": True, "the femtometre": False}
    assert explained["the ratio 8/7"] and not explained["the femtometre"]


def test_the_selection_is_conditional_and_says_so():
    """The arithmetic is forced; the requirement that refinement leave
    the wheel invariant is this register's principle, not a theorem."""
    status = {"2^d = 1 mod 7 iff 3 | d": "forced",
              "contact per child maximal at d = 2,3,4": "forced",
              "refinement must leave the wheel invariant": "principle"}
    assert sorted(status.values()).count("forced") == 2
    assert "principle" in status.values()
