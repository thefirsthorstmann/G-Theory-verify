"""Class #2 of the map, gamed in detail: the cyclic pairing (9 October 2026, the open map, at CC's word: "Ok, lets keep
going").

Pinned, all exact. The six alternating forms (quark and antiquark classes alternating around the cycle) are the closed
paths of the complete quark-antiquark graph; each leaves out three quark-antiquark chords, a perfect pairing of the
classes. Read through the mirror's own pairing (q <-> 9 - q), the six pairings are the six permutations of three things:
  * matter is the identity: every quark-class digit sits opposite its own mirror partner;
  * class #2 (127548 and 154278) is the two 3-cycles, inverse to each other;
  * the harmonic class (124578, 127845, 157248) is the three transpositions;
so the alternating classes of sizes 1, 2, 3 are the conjugacy classes of S3. Class #2's steps alternate doubling and the
mirror, and every two steps make x7, a rotation inside each triality class; its transform out of matter is the
involution (4 7)(5 8), which keeps the triality classes; the mirror and the inversion x -> 1/x send each member to the
other alike, and their composite fixes each.
READING, open (may or may not be physics in terms of our current understanding): if the pairing is read as colour against
anticolour, matter pairs each colour with its own anticolour, the arrangement of the colour singlet, and class #2 pairs
each colour with the anticolour of the next, cyclically, in its two orientations, the arrangement of the off-diagonal
colour-octet combinations taken around the cycle. The record assigns no individual colours to digits, so this stays a
reading.
"""

from itertools import permutations

QUARK, ANTI = (1, 4, 7), (2, 5, 8)


def _chords(seq):
    return frozenset(frozenset((seq[i], seq[(i + 1) % 6])) for i in range(6))


def _alternating():
    out = {}
    for p in permutations((2, 4, 5, 7, 8)):
        s = (1,) + p
        if all((s[i] in QUARK) != (s[(i + 1) % 6] in QUARK) for i in range(6)):
            out.setdefault(_chords(s), s)
    return out


def _pairing(chords):
    left_out = {frozenset((q, a)) for q in QUARK for a in ANTI} - set(chords)
    partner = {next(x for x in c if x in QUARK): next(x for x in c if x in ANTI) for c in left_out}
    return tuple(9 - partner[q] for q in QUARK)                    # the permutation of QUARK, through the mirror


def test_the_six_alternating_forms_are_the_six_pairings():
    alts = _alternating()
    assert len(alts) == 6
    assert sorted(_pairing(E) for E in alts) == sorted(permutations(QUARK))


def test_the_alternating_classes_are_the_conjugacy_classes_of_s3():
    alts = _alternating()
    fixed = lambda pi: sum(a == b for a, b in zip(pi, QUARK))
    kind = {s: {3: "identity", 1: "transposition", 0: "3-cycle"}[fixed(_pairing(E))] for E, s in alts.items()}
    assert kind[(1, 2, 4, 8, 7, 5)] == "identity"
    assert {s for s, k in kind.items() if k == "3-cycle"} == {(1, 2, 7, 5, 4, 8), (1, 5, 4, 2, 7, 8)}
    assert {s for s, k in kind.items() if k == "transposition"} == {(1, 2, 4, 5, 7, 8), (1, 2, 7, 8, 4, 5),
                                                                     (1, 5, 7, 2, 4, 8)}


def test_class_two_steps_alternate_doubling_and_the_mirror():
    s = (1, 2, 7, 5, 4, 8)
    step = lambda a, b: next(u for u in (1, 2, 4, 5, 7, 8) if (a * u) % 9 == b)
    steps = [step(s[i], s[(i + 1) % 6]) for i in range(6)]
    assert steps == [2, 8, 2, 8, 2, 8]
    assert [(steps[i] * steps[i + 1]) % 9 for i in (0, 2, 4)] == [7, 7, 7]
    sigma = dict(zip((1, 2, 4, 8, 7, 5), s))
    assert {k: v for k, v in sigma.items() if k != v} == {4: 7, 7: 4, 5: 8, 8: 5}


def test_the_mirror_and_the_inversion_swap_the_pair_alike():
    s, partner = (1, 2, 7, 5, 4, 8), (1, 5, 4, 2, 7, 8)
    mirror = _chords(tuple(9 - x for x in s))
    inversion = _chords(tuple(pow(x, -1, 9) for x in s))
    assert mirror == inversion == _chords(partner) != _chords(s)
    both = _chords(tuple(9 - pow(x, -1, 9) for x in s))
    assert both == _chords(s)
