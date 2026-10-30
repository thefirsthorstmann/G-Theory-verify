"""The colour column of the Feynman table (9 October 2026, at CC's word: "yeaboi! lets keep rollin").

The standard machinery tested against: the colour-flow basis of amplitudes with three quarks and three antiquarks. For three
colours the colour-singlet space of q q q qbar qbar qbar is six-dimensional, spanned by the six flows delta_pi that connect
quark k's colour to antiquark pi(k)'s (the colour-flow decomposition; 't Hooft's double-line notation). Each alternating form
leaves out one quark-antiquark pairing (verify/test_class_two_the_cyclic_pairing.py), read through the mirror's pairing as a
permutation pi; the dictionary used is the board's (mirror = charge conjugation) and the record's (triality classes).

Pinned, all exact, with N = 3:
  * the six alternating forms, read as colour flows, are a basis of the colour-singlet space (their overlap matrix has
    entries 3^cycles and a non-zero determinant);
  * each class's overlap with the singlet pairing (each quark with its own mirror partner) is 3^(closed colour loops):
    matter 27 (three loops), the harmonic class 9 (two), class #2 3 (one loop through all six);
  * the baryon-antibaryon colour structure eps_ijk eps^lmn is the six flows summed with the sign of the pairing: matter and
    class #2 with plus, the harmonic class with minus;
  * the three classes are the conjugacy classes of S3, and its character table turns them into the three colour channels:
    symmetric (rank 1), antisymmetric, the baryon-antibaryon singlet (rank 1), and mixed, octet against octet (rank 4).
READING, open (may or may not be physics in terms of our current understanding): matter is three separate quark-antiquark
singlets (three mesons), class #2 one colour loop through all six legs; the blocked flow (rest's class) is the baryon-
antibaryon arrangement, whose colour structure is the signed sum above; the first operation, matter to rest, then reads as the
rearrangement between three mesons and a baryon-antibaryon pair, the colour picture of proton-antiproton annihilation into
three mesons.
"""

from itertools import permutations

import numpy as np

N = 3
PERMS = list(permutations(range(3)))


def _flow(pi):
    t = np.zeros((N,) * 6)
    for i in np.ndindex(N, N, N):
        j = [0, 0, 0]
        for k in range(3):
            j[pi[k]] = i[k]
        t[i + tuple(j)] = 1
    return t


def _cycles(pi):
    seen, c = set(), 0
    for s in range(3):
        if s not in seen:
            c += 1
            x = s
            while x not in seen:
                seen.add(x)
                x = pi[x]
    return c


def _sign(pi):
    return (-1) ** (3 - _cycles(pi))


def _pairing_of(form):
    """The left-out pairing of an alternating form, as a permutation of the quark labels 1, 4, 7 -> 0, 1, 2, read through the
    mirror (an antiquark a stands for its partner 9 - a)."""
    quark, anti = (1, 4, 7), (2, 5, 8)
    used = {frozenset((form[i], form[(i + 1) % 6])) for i in range(6)}
    left = {frozenset((q, a)) for q in quark for a in anti} - used
    partner = {next(x for x in c if x in quark): next(x for x in c if x in anti) for c in left}
    index = {1: 0, 4: 1, 7: 2}
    return tuple(index[9 - partner[q]] for q in quark)


def test_the_alternating_forms_read_as_colour_flows_are_a_basis():
    gram = np.array([[np.sum(_flow(a) * _flow(b)) for b in PERMS] for a in PERMS])
    expected = np.array([[N ** _cycles(tuple(b[a.index(k)] for k in range(3))) for b in PERMS] for a in PERMS])
    assert np.array_equal(gram, expected)
    assert round(np.linalg.det(gram)) == 119439360


def test_each_class_overlaps_the_singlet_pairing_by_three_to_its_colour_loops():
    singlet = _flow((0, 1, 2))
    classes = {"matter": [(1, 2, 4, 8, 7, 5)], "class #2": [(1, 2, 7, 5, 4, 8), (1, 5, 4, 2, 7, 8)],
               "harmonic": [(1, 2, 4, 5, 7, 8), (1, 2, 7, 8, 4, 5), (1, 5, 7, 2, 4, 8)]}
    overlaps = {name: {int(np.sum(_flow(_pairing_of(f)) * singlet)) for f in forms} for name, forms in classes.items()}
    assert overlaps == {"matter": {27}, "class #2": {3}, "harmonic": {9}}


def test_the_baryon_antibaryon_structure_is_the_sign_weighted_sum_of_the_flows():
    eps = np.zeros((N, N, N))
    for p in PERMS:
        eps[p] = _sign(p)
    assert np.allclose(np.einsum("abc,def->abcdef", eps, eps), sum(_sign(pi) * _flow(pi) for pi in PERMS))
    assert {_sign(_pairing_of(f)) for f in [(1, 2, 4, 8, 7, 5), (1, 2, 7, 5, 4, 8), (1, 5, 4, 2, 7, 8)]} == {1}
    assert {_sign(_pairing_of(f)) for f in [(1, 2, 4, 5, 7, 8), (1, 2, 7, 8, 4, 5), (1, 5, 7, 2, 4, 8)]} == {-1}


def test_the_character_table_turns_the_classes_into_the_three_colour_channels():
    relabel = lambda g, pi: tuple(pi[g.index(k)] for k in range(3))
    rep = lambda g: np.array([[1.0 if relabel(g, b) == a else 0.0 for b in PERMS] for a in PERMS])
    characters = {"symmetric": (1, lambda g: 1), "antisymmetric": (1, _sign),
                  "mixed": (2, lambda g: {3: 2, 2: 0, 1: -1}[_cycles(g)])}
    ranks = {name: np.linalg.matrix_rank(d / 6 * sum(chi(g) * rep(g) for g in PERMS))
             for name, (d, chi) in characters.items()}
    assert ranks == {"symmetric": 1, "antisymmetric": 1, "mixed": 4}


def _all_forms():
    def chords(s):
        return frozenset(frozenset((s[i], s[(i + 1) % 6])) for i in range(6))
    canon = lambda s: min(s, (s[0],) + tuple(reversed(s[1:])))
    forms = {}
    for p in permutations((2, 4, 5, 7, 8)):
        forms.setdefault(chords((1,) + p), canon((1,) + p))
    return forms


def _contained_flows(chord_set):
    """The complete quark-antiquark pairings that lie inside a form's own chords, as permutations through the mirror."""
    quark, anti = (1, 4, 7), (2, 5, 8)
    index = {1: 0, 4: 1, 7: 2}
    found = []
    for a in permutations(anti):
        if all(frozenset((q, x)) in chord_set for q, x in zip(quark, a)):
            found.append(tuple(index[9 - x] for x in a))
    return found


def test_the_flow_patterns_count_the_colour_flows_a_form_contains():
    """Alternating forms contain two complete colour flows, mixed forms one, blocked forms none; an alternating form's two
    flows and its left-out flow are one of the two ways of weaving all nine quark-antiquark links into three flows, the
    even weaving (identity and the two 3-cycles: matter and class #2) or the odd (the three transpositions: the harmonic
    class)."""
    quark = {1, 4, 7}
    def flow(s):
        b = "".join("q" if x in quark else "a" for x in s)
        turns = [b[i:] + b[:i] for i in range(6)]
        m = min(turns + [t[::-1] for t in turns])
        return {"aaaqqq": "blocked", "aqaqaq": "alternating"}.get(m, "mixed")
    for chord_set, s in _all_forms().items():
        assert len(_contained_flows(chord_set)) == {"alternating": 2, "mixed": 1, "blocked": 0}[flow(s)]
    weaving = lambda s: frozenset(_contained_flows(_all_forms_chords(s)) + [_pairing_of(s)])
    even = frozenset(p for p in PERMS if _sign(p) == 1)
    odd = frozenset(p for p in PERMS if _sign(p) == -1)
    for s in [(1, 2, 4, 8, 7, 5), (1, 2, 7, 5, 4, 8), (1, 5, 4, 2, 7, 8)]:
        assert weaving(s) == even
    for s in [(1, 2, 4, 5, 7, 8), (1, 2, 7, 8, 4, 5), (1, 5, 7, 2, 4, 8)]:
        assert weaving(s) == odd


def _all_forms_chords(s):
    return frozenset(frozenset((s[i], s[(i + 1) % 6])) for i in range(6))


def test_within_the_mixed_forms_cp_follows_the_parity_of_the_contained_flow():
    """The classes that keep CP (#6, #8, #10) contain an even colour flow, the two that break it (#7, #12) an odd one. The
    reason is the next test."""
    reps = {6: (1, 2, 4, 7, 8, 5), 8: (1, 2, 5, 7, 4, 8), 10: (1, 2, 7, 4, 5, 8), 7: (1, 2, 5, 4, 7, 8),
            12: (1, 2, 4, 5, 8, 7)}
    parity = {i: _sign(_contained_flows(_all_forms_chords(s))[0]) for i, s in reps.items()}
    assert parity == {6: 1, 8: 1, 10: 1, 7: -1, 12: -1}


def test_why_cp_follows_parity_in_the_mixed_forms():
    """Theorem. A CP symmetry (the mirror composed with an inversion x -> u/x) fixes a mixed form a1 a2 q3 a4 q5 q6 only by
    turning its frame around (a1 <-> q6, a2 <-> q5, q3 <-> a4); the pairing it induces is the contained flow
    {q3-a2, q5-a4, q6-a1} with a2 and a4 exchanged, of opposite parity; and the three CP symmetries induce exactly the three
    odd pairings (through the mirror the inversions are reflections). So CP fixes a mixed form exactly when its contained
    flow is even."""
    quark = (1, 4, 7)
    cp = {u: {x: (8 * u * pow(x, -1, 9)) % 9 for x in (1, 2, 4, 5, 7, 8)} for u in (1, 4, 7)}
    index = {1: 0, 4: 1, 7: 2}
    def sign(match):
        return _sign(tuple(index[9 - match[q]] for q in quark))
    assert all(sign({q: g[q] for q in quark}) == -1 for g in cp.values())
    checked = 0
    for p in permutations((2, 4, 5, 7, 8)):
        s = (1,) + p
        chord_set = _all_forms_chords(s)
        for seq in (s, tuple(reversed(s))):
            for i in range(6):
                t = seq[i:] + seq[:i]
                if "".join("q" if x in quark else "a" for x in t) != "aaqaqq":
                    continue
                a1, a2, q3, a4, q5, q6 = t
                fixers = [g for g in cp.values() if _all_forms_chords(tuple(g[x] for x in s)) == chord_set]
                assert bool(fixers) == (sign({q3: a2, q5: a4, q6: a1}) == 1)
                for g in fixers:
                    assert (g[a1], g[a2], g[q3]) == (q6, q5, a4)
                    assert {q: g[q] for q in quark} == {q3: a4, q5: a2, q6: a1}
                checked += 1
    assert checked == 72                                            # 36 mixed forms, each met in two directions
