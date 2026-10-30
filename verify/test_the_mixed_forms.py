"""The mixed forms on the mirror's pairing: the last piece of the table (9 October 2026, the open map continued).

Pinned, all exact. Every mixed form reads, in exactly one rotation and direction, as a a q a q q: a pair of antiquark-class
digits, a single quark-class digit, a single antiquark-class digit, a pair of quark-class digits, joined back to the
first pair. Its four quark-antiquark links are the middle (single quark to single antiquark), the two inner joins (the
singles to the pairs) and the outer join (quark pair back to antiquark pair). The mirror's pairing is a perfect matching
of the three quark-class digits with the three antiquark-class digits, six in all; which links it uses fixes the class:
  * none: #6 (124785) · the middle only: #8 (125748) · the middle and the outer join: #7 (125478)
  * one inner join only: #12 (124587; the two one-inner matchings are mirror images of the frame, so this class is
    twice the size and has no symmetry) · both inner joins and the outer join: #10 (127458)
The other combinations are impossible, because three partner pairs force one another: a partnered middle excludes both
inner joins; both inner joins force the outer join; the outer join alone forces the middle or both inner joins.
With the alternating forms (verify/test_class_two_the_cyclic_pairing.py) and the blocked forms
(verify/test_the_table_of_forms.py), every one of the twelve classes now has a structural reason.
READING, open: the mixed flow is an antidiquark, a quark, an antiquark and a diquark around a ring, and a partner link is a
neutral line (one the mirror maps to itself).
"""

from itertools import permutations

QUARK = {1, 4, 7}
UNITS = [1, 2, 4, 5, 7, 8]


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
            out.append(sorted(forms[F] for F in orbit))
    return sorted(out, key=lambda o: (len(o), o[0]))


def _frames(s):
    out = []
    for seq in (s, tuple(reversed(s))):
        for i in range(6):
            t = seq[i:] + seq[:i]
            if "".join("q" if x in QUARK else "a" for x in t) == "aaqaqq":
                out.append(t)
    return out


def _links(t):
    a1, a2, q3, a4, q5, q6 = t
    inner = (a2 + q3 == 9) + (a4 + q5 == 9)
    return ("middle" if q3 + a4 == 9 else "", inner, "outer" if q6 + a1 == 9 else "")


def test_every_mixed_form_has_exactly_one_frame():
    forms = [s for cls in _classes() for s in cls]
    counts = [len(_frames(s)) for s in forms]
    assert counts.count(1) == 36 and set(counts) == {0, 1}


def test_the_mixed_classes_by_their_partner_links():
    classes = _classes()
    found = {i: {_links(_frames(s)[0]) for s in classes[i - 1]} for i in (6, 7, 8, 10, 12)}
    assert found == {6: {("", 0, "")}, 7: {("middle", 0, "outer")}, 8: {("middle", 0, "")},
                     10: {("", 2, "outer")}, 12: {("", 1, "")}}


def test_the_other_combinations_are_impossible():
    seen = set()
    for q in permutations((1, 4, 7)):
        for a in permutations((2, 5, 8)):
            seen.add(_links((a[0], a[1], q[0], a[2], q[1], q[2])))
    assert seen == {("", 0, ""), ("middle", 0, "outer"), ("middle", 0, ""), ("", 2, "outer"), ("", 1, "")}
