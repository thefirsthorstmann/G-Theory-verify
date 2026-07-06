"""enneagram_line.py — THE LINE THEOREM (the maths module's crown).

CC's claim, formalized: the enneagram figure is A TRULY UNITARY
EXPRESSION CARRYING THE WHOLE CONSTRUCTION — one closed line.

THEOREM M1 (the line). The digit path of 1/p in base b is a single
closed line through distinct points iff the reptend is FULL — i.e.
iff the number of reptend classes (p-1)/ord_p(b) equals one, i.e.
iff b is a primitive root mod p. The selection-word 'FULL' of the
seed choice IS the one-stroke property, made visible.

FOR (p, b) = (7, 10), THE COMPLETE FIGURE, all parts exact:
  (i)   the path 1 -> 4 -> 2 -> 8 -> 5 -> 7 -> 1 is one closed line
        through six distinct points (unicursal);
  (ii)  the six points are EXACTLY the doubling orbit mod 9 (the
        hexad): the line covers one face of the seed completely;
  (iii) the complement in {1..9} is exactly the triad {3, 6, 9} —
        the triangle the line never touches: the conservation axis;
  (iv)  the figure's point reflection (d <-> 9 - d) maps the line
        onto itself three digits ahead: MIDY'S THEOREM IS THE
        FIGURE'S SYMMETRY (antipodal pairs sum to 9);
  (v)   the transform of Chapter I is the involution between the
        figure's two Hamiltonian cycles — the positional line
        (142857) and the multiplicative line (124875).

THE CONTRAST: p = 13 in base 10 has ord = 6 of a possible 12 — TWO
reptend classes (076923 and 153846): the figure needs two strokes.
One theory, one figure, one line — because the seed's reptend is full.
"""

from fractions import Fraction as F

from chosen_three import ord_mod
from gtheory import doubling_orbit, expansion_digits, reptend, transform


def reptend_classes(p: int, base: int = 10) -> int:
    """Number of distinct reptend cycles: (p-1)/ord_p(base)."""
    return (p - 1) // ord_mod(base, p)


def is_one_line(p: int, base: int = 10) -> bool:
    """THE LINE CRITERION: one closed stroke iff one reptend class."""
    return reptend_classes(p, base) == 1


def path_points(p: int = 7) -> list:
    """The digit path of 1/p as points on the residue circle."""
    return [int(d) for d in reptend(p)]


def the_two_strokes_of_13() -> tuple:
    """1/13 and 2/13 belong to different cycles: the two lines."""
    return (expansion_digits(1, 13, 6), expansion_digits(2, 13, 6))


def midy_reflection_shift(p: int = 7) -> bool:
    """(iv): d_i + d_{i+3} = 9 — the point reflection is a 3-shift."""
    d = path_points(p)
    half = len(d) // 2
    return all(d[i] + d[i + half] == 9 for i in range(half))
