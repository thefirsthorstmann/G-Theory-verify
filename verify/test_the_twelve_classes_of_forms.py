"""The sixty forms up to the figure's own arithmetic: twelve classes, so twelve essentially different transforms (9 October
2026, at CC's question: "we havent really spent much of any time on transforms except for the main one ... 12 total
harmonic forms and 60 total figures implies a huge range of function that we havent really looked at ... Are we limiting
this questions answer by not accounting for these other functions?").

Roped up: THE-ENNEAGRAM-IS-A-THEOREM sections 12 and 14 bank the sixty closed forms on the six units modulo nine, sorted by
the mirror into four balanced, twelve harmonic and forty-four chiral, and name five (rest 142857, matter 124875, force
147852, spine 152847, harmonic 124578). The transforms between forms were not surveyed.

Pinned here:
  * the figure's own arithmetic symmetries are the twelve maps x -> u x and x -> u / x (u a unit): the symmetries of the
    doubling hexagon, which is the matter form. Under them the sixty forms fall into exactly twelve classes, of sizes
    1, 2, 3, 3, 3, 6, 6, 6, 6, 6, 6, 12: the balanced forms in two classes, the harmonic in three, the chiral in seven.
    Because they are the matter form's own symmetries, the classes count the essentially different transforms out of
    matter, up to that symmetry on both sides (the double cosets); the first operation, matter <-> rest, is one of them.
  * matter is the one form that every arithmetic symmetry fixes; rest, force and spine are one class, multiples of one
    another digit by digit (force = 4 x rest, spine = 2 x rest), the mirror fixing each;
  * read as step words (the logarithm, base two modulo nine, of the multiplier at each step), matter is the constant
    word +1 six times, and rest, force and spine are one word, +2, -1, +2 twice, started at three different points.
"""

from itertools import permutations

UNITS = [1, 2, 4, 5, 7, 8]
LOG = {pow(2, k, 9): k for k in range(6)}
NAMED = {"rest": (1, 4, 2, 8, 5, 7), "matter": (1, 2, 4, 8, 7, 5), "force": (1, 4, 7, 8, 5, 2),
         "spine": (1, 5, 2, 8, 4, 7), "harmonic": (1, 2, 4, 5, 7, 8)}


def _chords(seq):
    return frozenset(frozenset((seq[i], seq[(i + 1) % 6])) for i in range(6))


def _forms():
    out = {}
    for p in permutations(UNITS[1:]):
        out.setdefault(_chords((1,) + p), (1,) + p)
    return out


def _act(g, chords):
    return frozenset(frozenset(g(x) for x in c) for c in chords)


SYMMETRIES = ([lambda x, u=u: (u * x) % 9 for u in UNITS] +
              [lambda x, u=u: (u * pow(x, -1, 9)) % 9 for u in UNITS])


def _class_of(seq, chords):
    if all(seq[i] + seq[(i + 3) % 6] == 9 for i in range(6)):
        return "balanced"
    return "harmonic" if _act(lambda x: 9 - x, chords) == chords else "chiral"


def test_the_sixty_forms_and_their_three_classes_under_the_mirror():
    forms = _forms()
    assert len(forms) == 60
    counts = {}
    for chords, seq in forms.items():
        counts[_class_of(seq, chords)] = counts.get(_class_of(seq, chords), 0) + 1
    assert counts == {"balanced": 4, "harmonic": 12, "chiral": 44}


def test_the_arithmetic_symmetries_sort_the_sixty_into_twelve_classes():
    forms = _forms()
    seen, orbits = set(), []
    for chords in forms:
        if chords not in seen:
            orbit = {_act(g, chords) for g in SYMMETRIES}
            seen |= orbit
            orbits.append(orbit)
    assert len(orbits) == 12
    assert sorted(len(o) for o in orbits) == [1, 2, 3, 3, 3, 6, 6, 6, 6, 6, 6, 12]
    by_class = {}
    for o in orbits:
        kinds = {_class_of(forms[c], c) for c in o}
        assert len(kinds) == 1                                     # each class sits inside one mirror class
        by_class.setdefault(kinds.pop(), []).append(len(o))
    assert {k: sorted(v) for k, v in by_class.items()} == {"balanced": [1, 3], "harmonic": [3, 3, 6],
                                                          "chiral": [2, 6, 6, 6, 6, 6, 12]}
    named = {_chords(s): n for n, s in NAMED.items()}
    orbit_of = {c: frozenset(named[x] for x in o if x in named) for o in orbits for c in o}
    assert orbit_of[_chords(NAMED["matter"])] == {"matter"}
    assert orbit_of[_chords(NAMED["rest"])] == {"rest", "force", "spine"}


def test_force_and_spine_are_rest_multiplied_and_matter_is_fixed_by_every_multiplication():
    times = lambda u, seq: _chords(tuple((u * x) % 9 for x in seq))
    assert times(4, NAMED["rest"]) == times(5, NAMED["rest"]) == _chords(NAMED["force"])
    assert times(2, NAMED["rest"]) == times(7, NAMED["rest"]) == _chords(NAMED["spine"])
    assert times(8, NAMED["rest"]) == _chords(NAMED["rest"])
    assert all(times(u, NAMED["matter"]) == _chords(NAMED["matter"]) for u in UNITS)


def test_the_balanced_forms_are_the_constant_word_and_one_word_in_three_phases():
    word = lambda s: tuple((LOG[s[(i + 1) % 6]] - LOG[s[i]]) % 6 for i in range(6))
    assert word(NAMED["matter"]) == (1,) * 6
    assert word(NAMED["rest"]) == (2, 5, 2, 2, 5, 2)                 # +2, -1, +2 twice
    rotations = {word(NAMED["rest"])[k:] + word(NAMED["rest"])[:k] for k in range(6)}
    assert {word(NAMED["force"]), word(NAMED["spine"])} <= rotations and len(rotations) == 3
