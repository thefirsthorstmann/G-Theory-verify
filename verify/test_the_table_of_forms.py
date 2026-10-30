"""The table of the twelve classes: an address for every class (9 October 2026, the open map continued).

Pinned, all exact. Each class of forms has a three-part address, the same for every member:
  * its colour flow (alternating, blocked or mixed: verify/test_the_colour_flow_and_symmetry_of_the_classes.py);
  * how many of its six chords join mirror partners (x and 9 - x, a quark-class digit with its own partner): 0 to 3;
  * its symmetry profile (fixed by the mirror and an inversion, by the mirror alone, by a mirror-times-inversion alone,
    or by nothing).
The first two parts separate ten classes; the profile separates the last two pairs (rest's class from #9, #8 from #12).
Two cells of the flow-by-partner grid are empty by force: an alternating form cannot have exactly one partner chord (its
left-out pairing is a permutation of three, which cannot fix exactly two), and a blocked form cannot have three (only its
two joins run between the blocks). The blocked forms are also fixed by their middles and joins: rest's class has the two
middle digits partnered and neither join on partners; #5 the middles and both joins partnered; #9 neither; #11 one join.
READING, open: a partner chord is a link that the mirror (charge conjugation) maps to itself, the figure's neutral line.
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


def _flow(s):
    b = "".join("q" if x in QUARK else "a" for x in s)
    turns = [b[i:] + b[:i] for i in range(6)]
    m = min(turns + [t[::-1] for t in turns])
    return {"aaaqqq": "blocked", "aqaqaq": "alternating"}.get(m, "mixed")


def _partners(s):
    return sum(s[i] + s[(i + 1) % 6] == 9 for i in range(6))


def _profile(s):
    keep = [{x: (u * x) % 9 for x in UNITS} for u in (1, 4, 7)] + \
           [{x: (u * pow(x, -1, 9)) % 9 for x in UNITS} for u in (1, 4, 7)]
    act = lambda g: frozenset(frozenset(g[x] for x in c) for c in _chords(s))
    mirror = lambda g: {x: (8 * g[x]) % 9 for x in UNITS}
    inversions = keep[3:]
    c_even = act(mirror(keep[0])) == _chords(s)
    p_even = any(act(g) == _chords(s) for g in inversions)
    cp_even = any(act(mirror(g)) == _chords(s) for g in inversions)
    if c_even and p_even:
        return "full"
    if c_even:
        return "C only"
    return "CP only" if cp_even else "none"


GRID = {1: ("alternating", 0, "full"), 2: ("alternating", 3, "CP only"), 3: ("alternating", 2, "full"),
        4: ("blocked", 0, "full"), 5: ("blocked", 2, "full"), 6: ("mixed", 0, "CP only"), 7: ("mixed", 2, "C only"),
        8: ("mixed", 1, "CP only"), 9: ("blocked", 0, "CP only"), 10: ("mixed", 3, "CP only"),
        11: ("blocked", 1, "CP only"), 12: ("mixed", 1, "none")}


def test_every_class_has_one_address_and_no_two_share_it():
    classes = _classes()
    for i, cls in enumerate(classes, 1):
        assert {(_flow(s), _partners(s), _profile(s)) for s in cls} == {GRID[i]}
    assert len(set(GRID.values())) == 12


def test_flow_and_partner_chords_alone_collide_exactly_twice():
    seen = {}
    for i, (flow, partners, _) in GRID.items():
        seen.setdefault((flow, partners), []).append(i)
    assert {k: v for k, v in seen.items() if len(v) > 1} == {("blocked", 0): [4, 9], ("mixed", 1): [8, 12]}


def test_the_two_empty_cells_are_empty_by_force():
    forms = {s for cls in _classes() for s in cls}
    assert not any(_flow(s) == "alternating" and _partners(s) == 1 for s in forms)
    assert not any(_flow(s) == "blocked" and _partners(s) == 3 for s in forms)
    assert max(_partners(s) for s in forms if _flow(s) == "blocked") == 2


def test_the_blocked_forms_by_their_middles_and_joins():
    def middles_and_joins(s):
        i = next(i for i in range(6) if all(s[(i + k) % 6] in QUARK for k in range(3)))
        q = [s[(i + k) % 6] for k in range(3)]
        a = [s[(i + 3 + k) % 6] for k in range(3)]
        return (9 - a[1] == q[1], (q[2] + a[0] == 9) + (a[2] + q[0] == 9))
    classes = _classes()
    found = {i: {middles_and_joins(s) for s in classes[i - 1]} for i in (4, 5, 9, 11)}
    assert found == {4: {(True, 0)}, 5: {(True, 2)}, 9: {(False, 0)}, 11: {(False, 1)}}
