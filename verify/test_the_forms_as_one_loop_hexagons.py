"""The forms as one-loop hexagons: the start of the Feynman table (9 October 2026, at CC's question: "Is it possible to start
building up a table of correspondnt forms to the Feyman diagrams with these?").

Pinned, all exact:
  * the count: a one-loop diagram with six external legs is fixed by the cyclic order in which the legs attach to the
    loop; up to rotation and reversal (reversal is Furry's pairing of the two orientations of the loop, which add for an
    even number of legs) there are (6-1)!/2 = 60 orderings, the number of closed forms;
  * read in dual coordinates (the digits as the points between adjacent legs, in logarithms base two modulo nine, and
    each step as the external momentum, the difference of neighbouring points), every form's momenta sum to zero modulo
    six: closure is momentum conservation;
  * the legs carrying the half-turn momentum 3 (the one momentum equal to its own negative) are exactly the form's chords
    joining mirror partners (verify/test_the_table_of_forms.py);
  * on the doubling hexagon, where the figure's arithmetic symmetries act as rotations and reflections, squared chords
    are 1, 3 and 4, and each form's three hexagon cross-ratios u_i = x(i,i+2) x(i+3,i+5) / (x(i,i+3) x(i+2,i+5)) are
    the same for every member of its class and different for every two classes: one triple identifies each class. Every
    value is a ratio of powers of two and three.
READING, open (may or may not be physics in terms of our current understanding): in planar gauge theory the six-point
amplitude is the first whose value depends on the hexagon's cross-ratios (the remainder function, from two loops); four
and five points are fixed by dual conformal symmetry. There the dual points are light-like separated, here they sit on a
regular hexagon, so the correspondence is of structure, not of kinematics.
"""

from fractions import Fraction as F
from itertools import permutations
from math import factorial

UNITS = [1, 2, 4, 5, 7, 8]
LOG = {pow(2, k, 9): k for k in range(6)}
SQUARED_CHORD = {0: 0, 1: 1, 5: 1, 2: 3, 4: 3, 3: 4}

CROSS_RATIOS = {
    1: ("9/16", "9/16", "9/16"), 2: ("9", "9", "9"), 3: ("9/4", "9/4", "9"), 4: ("1/16", "1/16", "9/16"),
    5: ("1/4", "1/4", "9"), 6: ("1/4", "1/4", "16/9"), 7: ("1/9", "1/4", "1/4"), 8: ("1/9", "4", "4"),
    9: ("1/4", "9/4", "16"), 10: ("1/9", "1", "1"), 11: ("4", "4", "9"), 12: ("4/9", "1", "4")}


def _chords(seq):
    return frozenset(frozenset((seq[i], seq[(i + 1) % 6])) for i in range(6))


def _classes():
    canon = lambda s: min(s, (s[0],) + tuple(reversed(s[1:])))
    forms = {}
    for p in permutations((2, 4, 5, 7, 8)):
        forms.setdefault(_chords((1,) + p), canon((1,) + p))
    sym = ([{x: (u * x) % 9 for x in UNITS} for u in UNITS] +
           [{x: (u * pow(x, -1, 9)) % 9 for x in UNITS} for u in UNITS])
    act = lambda g, E: frozenset(frozenset(g[x] for x in c) for c in E)
    seen, out = set(), []
    for E in forms:
        if E not in seen:
            orbit = {act(g, E) for g in sym}
            seen |= orbit
            out.append(sorted(forms[G] for G in orbit))
    return sorted(out, key=lambda o: (len(o), o[0]))


def _momenta(s):
    return [(LOG[s[(i + 1) % 6]] - LOG[s[i]]) % 6 for i in range(6)]


def _cross_ratios(s):
    k = [LOG[x] for x in s]
    x2 = lambda i, j: SQUARED_CHORD[(k[i % 6] - k[j % 6]) % 6]
    return tuple(sorted(F(x2(i, i + 2) * x2(i + 3, i + 5), x2(i, i + 3) * x2(i + 2, i + 5)) for i in range(3)))


def test_sixty_forms_are_the_one_loop_orderings_of_six_legs():
    assert sum(len(c) for c in _classes()) == factorial(6 - 1) // 2 == 60


def test_every_form_conserves_momentum_and_its_half_turn_legs_are_its_partner_chords():
    for cls in _classes():
        for s in cls:
            p = _momenta(s)
            assert sum(p) % 6 == 0
            assert p.count(3) == sum(s[i] + s[(i + 1) % 6] == 9 for i in range(6))


def test_the_cross_ratios_identify_every_class():
    classes = _classes()
    for i, cls in enumerate(classes, 1):
        assert {_cross_ratios(s) for s in cls} == {tuple(F(v) for v in CROSS_RATIOS[i])}
    assert len(set(CROSS_RATIOS.values())) == 12


def test_every_cross_ratio_is_a_ratio_of_twos_and_threes():
    def smooth(n):
        for p in (2, 3):
            while n % p == 0:
                n //= p
        return n == 1
    for values in CROSS_RATIOS.values():
        assert all(smooth(F(v).numerator) and smooth(F(v).denominator) for v in values)


def test_the_winding_is_defined_exactly_when_no_leg_carries_the_half_turn():
    """Each half-turn leg is a diameter of the doubling hexagon and can be read as +3 or -3, so the loop's winding about
    the centre is defined only for forms with no such leg: matter, rest's class and #6 wind once, #9 not at all."""
    from itertools import product
    def windings(s):
        steps = [((LOG[s[(i + 1) % 6]] - LOG[s[i]] + 2) % 6) - 2 for i in range(6)]
        half = [i for i, v in enumerate(steps) if v == 3]
        out = set()
        for signs in product((3, -3), repeat=len(half)):
            t = list(steps)
            for i, v in zip(half, signs):
                t[i] = v
            out.add(abs(sum(t)) // 6)
        return out
    classes = _classes()
    defined = {i: windings(c[0]) for i, c in enumerate(classes, 1) if len(windings(c[0])) == 1}
    assert defined == {1: {1}, 4: {1}, 6: {1}, 9: {0}}
    for i, cls in enumerate(classes, 1):
        half_turn_legs = _momenta(cls[0]).count(3)
        assert (len(windings(cls[0])) == 1) == (half_turn_legs == 0)
