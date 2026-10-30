"""The census of the twelve transform classes, charted and open (9 October 2026, at CC's word: "lets identify the ones that
perform the functions, isolate them ... Then lets group the non correspondent forms ... a map of what we dont know").

CC's rule for this exercise, verbatim in substance: of every result, say "this may or may not be physics in terms of our
current understanding, but that does not mean it isnt physics"; never "this isn't physics" (Maxwell could not have been
told of the Higgs boson).

Classes are the orbits of the sixty forms under the figure's own arithmetic symmetries (x -> ux, x -> u/x), equivalently
the essentially different transforms out of the matter form (verify/test_the_twelve_classes_of_forms.py). Pinned here, for
each class, properties that do not depend on which transform in the class is taken (the mirror is central in the
symmetry group, and the colour split is kept by every symmetry):
  * whether the transform out of matter commutes with the mirror (keeps the Midy pairs; the board of 8 October computed
    the mirror as charge conjugation): exactly the two balanced classes, matter's own and rest's. Of the eleven
    non-trivial classes, the first operation's is the only one;
  * whether it keeps the colour split (squares {1,4,7} against {2,5,8}): exactly matter's class, the harmonic class of
    124578, and the chiral pair of 127548, whose steps alternate doubling and the mirror;
  * whether the class contains an involution (a transform that is its own inverse, as the first operation is): all but
    four classes, each of size six;
  * charted, by the rule fixed in advance (a published record gives a member a physical role): matter (the circulation
    face), rest with force and spine (the read face), the harmonic order (the sevenths as nodes along a string); open:
    the other nine classes, fifty-three forms.
"""

from itertools import permutations

UNITS = [1, 2, 4, 5, 7, 8]
MATTER = (1, 2, 4, 8, 7, 5)


def _chords(seq):
    return frozenset(frozenset((seq[i], seq[(i + 1) % 6])) for i in range(6))


def _census():
    canon = lambda s: min(s, (s[0],) + tuple(reversed(s[1:])))
    forms = {}
    for p in permutations(UNITS[1:]):
        forms.setdefault(_chords((1,) + p), canon((1,) + p))
    sym = ([{x: (u * x) % 9 for x in UNITS} for u in UNITS] +
           [{x: (u * pow(x, -1, 9)) % 9 for x in UNITS} for u in UNITS])
    act = lambda g, E: frozenset(frozenset(g[x] for x in c) for c in E)
    seen, classes = set(), []
    for E in forms:
        if E not in seen:
            orbit = {act(g, E) for g in sym}
            seen |= orbit
            classes.append(sorted(forms[F] for F in orbit))
    return classes, sym


def _profile(cls, sym):
    rep = cls[0]
    sigma = dict(zip(MATTER, rep))
    mirror = {x: 9 - x for x in UNITS}
    compose = lambda f, g: {x: f[g[x]] for x in UNITS}
    coset = [compose(compose(a, sigma), b) for a in sym for b in sym]
    if all(rep[i] + rep[(i + 3) % 6] == 9 for i in range(6)):
        kind = "balanced"
    else:
        kind = "harmonic" if _chords(tuple(9 - x for x in rep)) == _chords(rep) else "chiral"
    return dict(size=len(cls), kind=kind, sym=12 // len(cls),
                c_respecting=all(sigma[mirror[x]] == mirror[sigma[x]] for x in UNITS),
                keeps_colour={sigma[x] for x in (1, 4, 7)} in ({1, 4, 7}, {2, 5, 8}),
                involution=any(all(t[t[x]] == x for x in UNITS) for t in coset))


def test_the_twelve_classes_by_size_kind_and_symmetry():
    classes, sym = _census()
    shapes = sorted((p["size"], p["kind"], p["sym"]) for p in (_profile(c, sym) for c in classes))
    assert shapes == sorted([(1, "balanced", 12), (2, "chiral", 6), (3, "harmonic", 4), (3, "balanced", 4),
                             (3, "harmonic", 4), (6, "harmonic", 2)] + [(6, "chiral", 2)] * 5 + [(12, "chiral", 1)])


def test_only_the_first_operations_class_respects_the_mirror_among_the_nontrivial():
    classes, sym = _census()
    respecting = [c for c in classes if _profile(c, sym)["c_respecting"]]
    assert sorted(len(c) for c in respecting) == [1, 3]
    rest = (1, 4, 2, 8, 5, 7)
    assert any(_chords(f) == _chords(rest) for c in respecting for f in c)


def test_the_colour_keeping_classes_are_matter_the_harmonic_order_and_one_chiral_pair():
    classes, sym = _census()
    keeping = [c for c in classes if _profile(c, sym)["keeps_colour"]]
    reps = {tuple(c[0]) for c in keeping}
    assert reps == {(1, 2, 4, 8, 7, 5), (1, 2, 4, 5, 7, 8), (1, 2, 7, 5, 4, 8)}


def test_four_classes_carry_no_involution_and_all_have_six_members():
    classes, sym = _census()
    without = [c for c in classes if not _profile(c, sym)["involution"]]
    assert len(without) == 4 and all(len(c) == 6 for c in without)
    assert {c[0] for c in without} == {(1, 2, 5, 4, 7, 8), (1, 2, 5, 8, 4, 7), (1, 2, 7, 4, 5, 8), (1, 2, 8, 5, 4, 7)}


def test_three_classes_are_charted_and_nine_open_holding_fifty_three_forms():
    classes, _ = _census()
    charted_forms = {_chords(s) for s in [(1, 2, 4, 8, 7, 5), (1, 4, 2, 8, 5, 7), (1, 2, 4, 5, 7, 8)]}
    charted = [c for c in classes if any(_chords(f) in charted_forms for f in c)]
    open_ = [c for c in classes if c not in charted]
    assert len(charted) == 3 and len(open_) == 9 and sum(len(c) for c in open_) == 53
