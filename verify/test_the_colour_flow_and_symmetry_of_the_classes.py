"""The twelve classes profiled by colour flow and by the symmetries that fix them (9 October 2026, the first round of the
map of what we do not know, at CC's word: "great my man, super cool, lets go").

Dictionary used, and only this: the mirror x -> 8x is charge conjugation (the board of 8 October); the classes {1,4,7} and
{2,5,8} are triality one and two (THE-ENNEAGRAM-IS-A-THEOREM s17, an identification). The figure's arithmetic symmetry
group splits as the mirror times the six maps that keep each triality class (x -> ux and x -> u/x, u a square). READING,
not established: the inversions x -> u/x as parity, on CC's lead (the perspective reversal, the one involution of the
figure that keeps triality, as parity must), so that the mirror composed with an inversion reads as CP.

Pinned here, all arithmetic:
  * colour flow, the sequence of triality classes around a form: alternating (qa qa qa) on 6 forms, blocked (qqq|aaa) on
    18, mixed (two adjacent quarks and two adjacent antiquarks apart) on 36; the colour-keeping transforms out of matter
    are exactly those onto the six alternating forms; the first operation takes matter's alternating flow to rest's
    blocked flow;
  * the symmetries fixing each class: matter all twelve; the pair of 127548 the class rotations and the mirror-times-
    inversions but not the mirror; the three classes of three (the harmonic order, rest's, 145827) the mirror and one
    inversion; the harmonic class of six the mirror alone; five classes of six one mirror-times-inversion each; the class
    of twelve nothing. Under the reading: mirror-even classes 1, 3, 4, 5, 7; CP-even but not mirror-even 2, 6, 8, 9, 10,
    11; none 12. Every open class carries the status "may or may not be physics in terms of our current understanding".
"""

from itertools import permutations

UNITS = [1, 2, 4, 5, 7, 8]
QUARK = {1, 4, 7}
SQUARES = (1, 4, 7)


def _chords(seq):
    return frozenset(frozenset((seq[i], seq[(i + 1) % 6])) for i in range(6))


ROT = {f"x{u}": {x: (u * x) % 9 for x in UNITS} for u in SQUARES}
INV = {f"{u}/x": {x: (u * pow(x, -1, 9)) % 9 for x in UNITS} for u in SQUARES}
KEEP = ROT | INV
MIRROR = {x: (8 * x) % 9 for x in UNITS}
SYM = KEEP | {"C." + k: {x: MIRROR[g[x]] for x in UNITS} for k, g in KEEP.items()}


def _act(g, chords):
    return frozenset(frozenset(g[x] for x in c) for c in chords)


def _classes():
    canon = lambda s: min(s, (s[0],) + tuple(reversed(s[1:])))
    forms = {}
    for p in permutations(UNITS[1:]):
        forms.setdefault(_chords((1,) + p), canon((1,) + p))
    seen, out = set(), []
    for E in forms:
        if E not in seen:
            orbit = {_act(g, E) for g in SYM.values()}
            seen |= orbit
            out.append(sorted(forms[F] for F in orbit))
    return sorted(out, key=lambda o: (len(o), o[0])), forms


def _flow(seq):
    b = "".join("q" if x in QUARK else "a" for x in seq)
    turns = [b[i:] + b[:i] for i in range(6)]
    m = min(turns + [t[::-1] for t in turns])
    return {"aaaqqq": "blocked", "aqaqaq": "alternating"}.get(m, "mixed")


def test_the_three_colour_flows_and_their_counts():
    _, forms = _classes()
    counts = {}
    for s in forms.values():
        counts[_flow(s)] = counts.get(_flow(s), 0) + 1
    assert counts == {"alternating": 6, "blocked": 18, "mixed": 36}


def test_colour_keeping_transforms_land_exactly_on_the_alternating_forms():
    _, forms = _classes()
    matter = (1, 2, 4, 8, 7, 5)
    for s in forms.values():
        sigma = dict(zip(matter, s))
        keeps = {sigma[x] for x in QUARK} in ({1, 4, 7}, {2, 5, 8})
        assert keeps == (_flow(s) == "alternating")
    assert _flow(matter) == "alternating" and _flow((1, 4, 2, 8, 5, 7)) == "blocked"


def test_the_symmetries_that_fix_each_class():
    classes, _ = _classes()
    stab = lambda rep: frozenset(k for k, g in SYM.items() if _act(g, _chords(rep)) == _chords(rep))
    found = {c[0]: stab(c[0]) for c in classes}
    assert found[(1, 2, 4, 8, 7, 5)] == frozenset(SYM)
    assert found[(1, 2, 7, 5, 4, 8)] == frozenset(ROT) | {"C." + k for k in INV}
    for rep, inv in (((1, 2, 4, 5, 7, 8), "4/x"), ((1, 2, 5, 8, 7, 4), "7/x"), ((1, 4, 5, 8, 2, 7), "1/x")):
        assert found[rep] == {"x1", "C.x1", inv, "C." + inv}
    assert found[(1, 2, 5, 4, 7, 8)] == {"x1", "C.x1"}
    for rep in [(1, 2, 4, 7, 8, 5), (1, 2, 5, 7, 4, 8), (1, 2, 5, 8, 4, 7), (1, 2, 7, 4, 5, 8), (1, 2, 8, 5, 4, 7)]:
        s = found[rep]
        assert len(s) == 2 and "x1" in s and next(iter(s - {"x1"})).startswith("C.") and "C.x1" not in s
    assert found[(1, 2, 4, 5, 8, 7)] == {"x1"}


def test_under_the_reading_the_classes_split_by_charge_parity():
    classes, _ = _classes()
    stab = lambda rep: {k for k, g in SYM.items() if _act(g, _chords(rep)) == _chords(rep)}
    c_even = [i for i, c in enumerate(classes, 1) if "C.x1" in stab(c[0])]
    cp_only = [i for i, c in enumerate(classes, 1) if "C.x1" not in stab(c[0]) and len(stab(c[0])) > 1]
    none = [i for i, c in enumerate(classes, 1) if len(stab(c[0])) == 1]
    assert (c_even, cp_only, none) == ([1, 3, 4, 5, 7], [2, 6, 8, 9, 10, 11], [12])


def test_if_parity_is_in_the_figures_group_it_is_an_inversion():
    """Of the figure's twelve arithmetic symmetries, seven are involutions (the mirror, the three inversions, the three
    mirror-times-inversions), and the only ones that keep each triality class are the three inversions, conjugate to one
    another by the class rotations. Board of 11 October 2026: this does not make them parity. They do not commute with the
    class rotations (parity is central), and on the doubling hexagon they are exactly the Weyl reflections of A2; on the
    momentum hexagon they are spatial reflections with energy kept, and the planar figure cannot separate the two readings
    (catalog/BOARD-THE-PARITY-READING-2026-10-11.md)."""
    identity = SYM["x1"]
    involutions = {k for k, g in SYM.items() if g != identity and all(g[g[x]] == x for x in UNITS)}
    assert involutions == {"C.x1", "1/x", "4/x", "7/x", "C.1/x", "C.4/x", "C.7/x"}
    keeps_triality = {k for k in involutions if all((SYM[k][x] in QUARK) == (x in QUARK) for x in UNITS)}
    assert keeps_triality == {"1/x", "4/x", "7/x"}
    conj = lambda r, g: {x: r[g[next(y for y in UNITS if r[y] == x)]] for x in UNITS}
    assert {frozenset(conj(SYM[r], SYM["1/x"]).items()) for r in ("x1", "x4", "x7")} == \
           {frozenset(SYM[k].items()) for k in ("1/x", "4/x", "7/x")}
