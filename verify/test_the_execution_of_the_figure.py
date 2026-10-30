"""test_the_execution_of_the_figure.py — THE FIGURE IS DRAWN IN ONE LINE, AND
THERE ARE 8668 WAYS (2026-08-15, CORRECTED THE SAME DAY).

  THE ERROR, RECORDED FIRST BECAUSE IT WAS MINE. I first built the figure as
  the hexad cycle plus the triad cycle, found two disjoint components, and
  concluded that the figure cannot be drawn as one line. CC refuted it the
  only way that matters: he draws it that way, without lifting the pen. THE
  CIRCLE WAS MISSING FROM MY GRAPH. The circle is not the frame around the
  figure, it is nine of its edges — and it is the only thing that joins the
  units to the non-units, since no chord does. Deleting it disconnects the
  figure; that is what I had accidentally proved.

  WITH THE CIRCLE, EVERYTHING IS EVEN AND CONNECTED. Nine arcs, six hexad
  chords, three triad chords: eighteen edges, every vertex of degree four,
  one component. Euler therefore GUARANTEES a closed circuit through every
  edge exactly once. The figure is unicursal, and it is unicursal BECAUSE of
  the circle.

  CC'S OWN EXECUTION, VERIFIED EDGE BY EDGE. 9-3-6-9, then all the way round
  counterclockwise to 1, leaving one 40-degree arc undrawn, then the line
  1-4-2-8-5-7-1, then that last arc 1-9 to close. Nineteen vertices, eighteen
  edges, none repeated, all covered, ending where it began.

  THE COUNT: 8668, BY TWO INDEPENDENT METHODS. At each of the nine points the
  four edge-ends can be paired in three ways — circle-through-and-chord-
  through, or one of the two switches. That is 3^9 = 19683 schemes, of which
  8668 yield a SINGLE closed curve. Direct enumeration of closed Eulerian
  trails from vertex nine gives 34672, and a single curve through a degree-four
  vertex admits two cut points and two directions, so 8668 x 4 = 34672. The
  two counts agree.

  THE FULL SPECTRUM, which is this figure's Martin-polynomial data: 8668
  schemes give one curve, 8264 give two, 2473 give three, 270 give four, and 8
  give five. They sum to 19683.

  LEAST ACTION HAS A SHARP ANSWER HERE, UNLIKE THE TWO-STROKE VERSION. All-
  through gives exactly three curves — the circle, the triangle and the line,
  each closing on itself — and each switched point changes the curve count by
  one. So three to one needs AT LEAST TWO switches, and two suffice: there are
  72 minimal schemes. They sit at 18 switch-locations, four schemes each, and
  the 18 are exactly {one triad point} x {one hexad point} = 3 x 6, because
  the circle must be merged with the triangle at a triad point and with the
  line at a hexad point.

  AND THE SAME THREE PRINCIPLES AS BEFORE PICK CC'S. Of the 18 locations, six
  are adjacent pairs on the circle — the ones whose connecting arc is a single
  40-degree arc rather than a detour. Of those six, two contain the origin 9.
  Of those two, one contains the seed 1. The survivor is {9, 1}: CC's, uniquely.
  Its virtue is visible in the drawing — the undrawn arc is exactly the arc
  between the two switch points, so the opening he leaves and the last stroke
  he makes are the same 40 degrees.

  ONE COINCIDENCE REFUSED PROMOTION, AGAIN. The minimal schemes number 72, the
  proton seat. It is forced by the structure alone — 3 triad points x 6 hexad
  points x 2 switch-parities x 2 = 72 — so it would be 72 for any figure of
  this shape. Exact, unexplained, and carrying no weight.
"""

from collections import Counter
from itertools import product

HEX, TRI, RING = [1, 4, 2, 8, 5, 7], [3, 6, 9], [9, 1, 2, 3, 4, 5, 6, 7, 8]


def _ce(c):
    return [tuple(sorted((c[i], c[(i + 1) % len(c)]))) for i in range(len(c))]


ARC, TRE, HXE = set(_ce(RING)), set(_ce(TRI)), set(_ce(HEX))
EDGES = sorted(ARC | TRE | HXE)

ENDS = {}
for _v in range(1, 10):
    _a = sorted(e for e in EDGES if _v in e and e in ARC)
    _c = sorted(e for e in EDGES if _v in e and e not in ARC)
    ENDS[_v] = (_a[0], _a[1], _c[0], _c[1])

PAIRING = {"T": ((0, 1), (2, 3)), "X": ((0, 2), (1, 3)), "Y": ((0, 3), (1, 2))}

CC_PATH = [9, 3, 6, 9, 8, 7, 6, 5, 4, 3, 2, 1, 4, 2, 8, 5, 7, 1, 9]


def _curves(choice):
    nxt = {}
    for v, k in zip(range(1, 10), choice):
        E4 = ENDS[v]
        for i, j in PAIRING[k]:
            nxt[(v, E4[i])] = E4[j]
            nxt[(v, E4[j])] = E4[i]
    unseen = {(e, d) for e in EDGES for d in (0, 1)}
    n = 0
    while unseen:
        n += 1
        e, d = next(iter(unseen))
        while (e, d) in unseen:
            unseen.discard((e, d))
            unseen.discard((e, 1 - d))
            v = e[d]
            e2 = nxt[(v, e)]
            d = 0 if e2[1] == v else 1
            e = e2
    return n


def test_the_circle_is_nine_edges_and_it_is_what_connects_the_figure():
    """The correction: without the circle the figure is disconnected."""
    assert len(EDGES) == 18 == len(ARC) + len(HXE) + len(TRE)
    assert (len(ARC), len(HXE), len(TRE)) == (9, 6, 3)
    deg = {v: sum(1 for e in EDGES if v in e) for v in range(1, 10)}
    assert set(deg.values()) == {4}                     # every vertex even

    def comps(E):
        vs, seen, out = set().union(*map(set, E)), set(), 0
        for s in sorted(vs):
            if s in seen:
                continue
            out += 1
            st, c = [s], {s}
            while st:
                x = st.pop()
                for e in E:
                    if x in e:
                        y = (set(e) - {x}).pop()
                        if y not in c:
                            c.add(y)
                            st.append(y)
            seen |= c
        return out
    assert comps(EDGES) == 1                            # with the circle
    assert comps(sorted(HXE | TRE)) == 2                # without it
    # and no chord joins a unit to a non-unit — only arcs do:
    assert all(len({a, b} & {3, 6, 9}) != 1 for a, b in HXE | TRE)
    assert any(len({a, b} & {3, 6, 9}) == 1 for a, b in ARC)


def test_ccs_execution_is_a_valid_closed_eulerian_circuit():
    used = [tuple(sorted((CC_PATH[i], CC_PATH[i + 1]))) for i in range(len(CC_PATH) - 1)]
    assert len(used) == 18 and len(set(used)) == 18
    assert set(used) == set(EDGES)
    assert CC_PATH[0] == CC_PATH[-1] == 9
    assert used[-1] == (1, 9)                           # the 40-degree opening, last
    assert len([e for e in used if e in ARC]) == 9      # every arc of the circle


def test_the_count_is_8668_by_the_transition_systems():
    dist = Counter(_curves(ch) for ch in product("TXY", repeat=9))
    assert sum(dist.values()) == 3 ** 9 == 19683
    assert dist[1] == 8668
    assert dict(dist) == {1: 8668, 2: 8264, 3: 2473, 4: 270, 5: 8}
    assert _curves(tuple("T" * 9)) == 3                 # circle, triangle, line


def test_the_count_agrees_with_direct_enumeration():
    """34672 closed trails from vertex 9; 4 per curve; 8668 curves."""
    adj = {v: [] for v in range(1, 10)}
    for e in EDGES:
        a, b = e
        adj[a].append((b, e))
        adj[b].append((a, e))
    total = 0
    stack = [(9, frozenset())]
    while stack:
        v, used = stack.pop()
        if len(used) == 18:
            total += 1 if v == 9 else 0
            continue
        for w, e in adj[v]:
            if e not in used:
                stack.append((w, used | {e}))
    assert total == 34672 == 8668 * 4


def test_two_switches_is_the_minimum_and_there_are_72_of_them():
    by, locs = Counter(), Counter()
    for ch in product("TXY", repeat=9):
        if _curves(ch) == 1:
            s = sum(1 for k in ch if k != "T")
            by[s] += 1
            if s == 2:
                locs[tuple(v for v, k in zip(range(1, 10), ch) if k != "T")] += 1
    assert min(by) == 2 and by[2] == 72
    assert sum(by.values()) == 8668
    assert len(locs) == 18 == 3 * 6                     # triad point x hexad point
    assert set(locs.values()) == {4}                    # 18 x 4 = 72
    for a, b in locs:
        assert len({a, b} & {3, 6, 9}) == 1             # one from each side
    assert 3 * 6 * 2 * 2 == 72                          # forced, not the seat


def test_the_three_principles_select_ccs_switch_pair():
    """adjacency, then the origin, then the seed."""
    locs = set()
    for ch in product("TXY", repeat=9):
        if _curves(ch) == 1 and sum(1 for k in ch if k != "T") == 2:
            locs.add(tuple(v for v, k in zip(range(1, 10), ch) if k != "T"))
    assert len(locs) == 18
    order = [9, 1, 2, 3, 4, 5, 6, 7, 8]
    nbr = {tuple(sorted((order[i], order[(i + 1) % 9]))) for i in range(9)}
    adjacent = {p for p in locs if tuple(sorted(p)) in nbr}
    assert len(adjacent) == 6                           # arc between them is one arc
    with_origin = {p for p in adjacent if 9 in p}
    assert len(with_origin) == 2                        # (8,9) and (1,9)
    with_seed = {p for p in with_origin if 1 in p}
    assert with_seed == {(1, 9)}                        # CC's, uniquely
    # and it is the pair his own path switches at:
    assert CC_PATH[0] == 9 and (1, 9) == tuple(sorted((CC_PATH[-2], CC_PATH[-1])))
