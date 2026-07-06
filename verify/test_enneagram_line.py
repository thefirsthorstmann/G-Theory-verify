"""test_enneagram_line.py — the Line Theorem pinned, all five parts."""

from enneagram_line import (is_one_line, midy_reflection_shift, path_points,
                            reptend_classes, the_two_strokes_of_13)
from gtheory import doubling_orbit, transform


def test_m1_one_line_iff_full_reptend():
    """One stroke iff one reptend class: 7 yes (first), 13 NO (two),
    17 yes, 11 no (five classes of period 2)."""
    assert reptend_classes(7) == 1 and is_one_line(7)
    assert reptend_classes(13) == 2 and not is_one_line(13)
    assert reptend_classes(17) == 1 and is_one_line(17)
    assert reptend_classes(11) == 5 and not is_one_line(11)


def test_part_i_and_ii_the_line_covers_the_hexad():
    """Six distinct points; exactly the doubling orbit mod 9."""
    pts = path_points(7)
    assert len(pts) == len(set(pts)) == 6            # unicursal: no repeats
    assert set(pts) == set(doubling_orbit()) == {1, 2, 4, 5, 7, 8}


def test_part_iii_the_complement_is_the_triad():
    """The triangle the line never touches: the conservation axis."""
    assert set(range(1, 10)) - set(path_points(7)) == {3, 6, 9}


def test_part_iv_midy_is_the_figures_symmetry():
    """The point reflection d <-> 9-d is the half-period shift."""
    assert midy_reflection_shift(7)


def test_part_v_the_transform_joins_the_two_hamiltonian_cycles():
    """The positional line and the multiplicative line are the
    figure's two cycles; Chapter I's involution maps one to the other."""
    positional = "".join(str(d) for d in path_points(7))
    multiplicative = "".join(str(d) for d in doubling_orbit())
    assert positional == "142857" and multiplicative == "124875"
    assert transform(positional)["out"] == multiplicative


def test_the_contrast_two_strokes_for_13():
    """The two cycles of 13: 076923 and 153846 — two lines needed."""
    assert the_two_strokes_of_13() == ("076923", "153846")
