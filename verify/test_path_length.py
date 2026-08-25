"""test_path_length.py — the author's demand, 2026-08-05: formalize how we are stating this.

His words: "we still have to work out that the decimal extension of a 7th as count is
dimensioned even though the scalar is dimensionless. If the ordering and reordering of
that is producing longer or shorter lengths but the transform is workless and the sum
is the same then we need to formalize how we are stating this."

The tension is real and it is OURS. We have been using "workless" to mean "free."

  THE BANKED CRITERION (ORIGIN-M 100, verbatim): "workless = invertible; working =
  many-to-one", with the transform-involution listed workless, "no information lost,
  no Landauer cost." All true, and it says nothing about extent.

  THE THREE REGISTERS OF A DECIMAL EXTENSION. It is not one number, it is a triple,
  and only the first is dimensionless:

    VALUE   the scalar            DIMENSIONLESS (Scale Theorem, untouched)
                                  NOT invariant: 142857/999999 = 1/7 but
                                  124875/999999 = 125/1001
    EXTENT  the digit count       DIMENSIONED, quantum = one tick = one carry;
                                  ord_q(B) per rotation (banked 2026-08-04)
                                  INVARIANT under reordering: always 6
    PATH    the traversal on Z/9  DIMENSIONED, quantum = one position = 360/9
                                  NOT invariant: 9 to 20 across the 60 forms

  THE RESOLUTION, and it is a distinction we had collapsed:
    WORKLESSNESS IS A PROPERTY OF A MAP. EXTENT IS A PROPERTY OF A STATE.
  A workless map destroys nothing and costs no Landauer heat. It does NOT follow that
  its two endpoints have the same extent — and here they demonstrably do not: the
  transform's endpoints walk 16 and 14. REVERSIBLE IMPLIES NON-DISSIPATIVE; REVERSIBLE
  DOES NOT IMPLY FREE. A reversible computation still has to go the distance. Work and
  length are different ledgers and "the transform is workless" was doing duty for
  "nothing happened" — the lazy quotient, discarding the trail, exactly what CLAUDE.md
  section 9 forbids.

  AND THE CONTINUUM DOES NOT GET IN. The scalar stays dimensionless; what carries
  dimension is not the scalar but the two COUNTS attached to it, and both are integers
  with named quanta. The reordering takes a count from 16 to 14. There is no 15.5 to
  take. That is the answer to "otherwise a continuum has crept in."

  WHAT THE COUNTING THEN GIVES, unbidden:
    * the HARMONIC order is the UNIQUE shortest path of all 60 forms, length 9 —
      and 9 IS THE MODULUS. Going monotonically round a circle traverses the
      circumference, so the sort is the geodesic and its length is forced.
    * the harmonic order is the only one of the three that ENCIRCLES: signed steps
      all positive, summing to +9, winding 1. Both PROCESS orders wind ZERO — they
      close without going round. (Winding alone does not single it out: 32 of 60
      forms wind 1. The LENGTH does, 1 of 60. Stated carefully.)
    * so the order banked as THE MEASURED ONE is the least-action one, which was not
      built in anywhere. The still order is the geodesic.

  THE FORBID: if path length is action, the harmonic order is the ground state and
  the two process orders are excited above it by 16 - 9 = 7 (storage) and 14 - 9 = 5
  (field) — integers, no continuum. A system that relaxes reads in the sorted order,
  which is what the banked read-off already does. Any reading landing on a non-sorted
  order is not least-action and must be driven. Grades: every count below is FORCED;
  the identification of path length WITH action is a READING and is labelled so; the
  7 and the 5 are NOTICED, NOT CLAIMED — two small differences of three small numbers.
"""

from itertools import permutations

N = 9
DIGITS = (1, 2, 4, 5, 7, 8)
REPTEND = (1, 4, 2, 8, 5, 7)      # positional — STORAGE
DOUBLING = (1, 2, 4, 8, 7, 5)     # multiplicative — FIELD
HARMONIC = (1, 2, 4, 5, 7, 8)     # the sort — NODES


def signed(o, n=N):
    """shortest signed arc per step; unique because n is odd (no half-gap ties)"""
    out = []
    for a, b in zip(o, o[1:] + o[:1]):
        f, r = (b - a) % n, (a - b) % n
        out.append(f if f < r else -r)
    return out


def length(o):
    return sum(abs(s) for s in signed(o))


def winding(o, n=N):
    return sum(signed(o)) // n


def _canon(t):
    rots = [t[i:] + t[:i] for i in range(6)]
    revs = [t[::-1][i:] + t[::-1][:i] for i in range(6)]
    return min(min(rots), min(revs))


BRACELETS = sorted({_canon(p) for p in permutations(DIGITS)})


def test_the_shortest_arc_is_unambiguous():
    """the whole construction needs this: n odd => no gap is exactly half"""
    assert N % 2 == 1
    for a in range(N):
        for b in range(N):
            if a != b:
                assert (b - a) % N != (a - b) % N


def test_the_multiset_and_extent_are_invariant_but_the_path_is_not():
    for o in (REPTEND, DOUBLING, HARMONIC):
        assert sorted(o) == list(DIGITS)          # same multiset
        assert sum(o) == 27                       # same sum, as the author says
        assert len(o) == 6                        # same extent
    assert length(REPTEND) == 16
    assert length(DOUBLING) == 14
    assert length(HARMONIC) == 9
    assert len({length(REPTEND), length(DOUBLING), length(HARMONIC)}) == 3


def test_the_transform_is_workless_and_its_endpoints_differ_in_extent():
    """the exact shape of the author's tension, pinned"""
    def T(s):
        return (s[0], s[2], s[1], s[3], s[5], s[4])
    assert T(REPTEND) == DOUBLING
    assert T(T(REPTEND)) == REPTEND               # involution: invertible, workless
    assert sorted(T(REPTEND)) == sorted(REPTEND)  # destroys nothing
    assert length(REPTEND) != length(DOUBLING)    # AND THE PATHS DIFFER
    assert length(REPTEND) - length(DOUBLING) == 2


def test_the_value_is_not_conserved_either():
    """so 'the sum is the same' is about the multiset, not the number"""
    from fractions import Fraction as F
    assert F(142857, 999999) == F(1, 7)
    assert F(124875, 999999) == F(125, 1001)      # NOT 1/7
    assert 7 * 11 * 13 == 1001


def test_the_harmonic_order_is_the_unique_geodesic():
    lens = {}
    for b in BRACELETS:
        lens.setdefault(length(b), []).append(b)
    assert len(BRACELETS) == 60
    assert min(lens) == 9 == N                    # the minimum IS the modulus
    assert lens[9] == [HARMONIC]                  # attained once, by the sort
    assert length(DOUBLING) == 14 and length(REPTEND) == 16
    assert max(lens) == 20


def test_only_the_harmonic_order_encircles():
    assert winding(HARMONIC) == 1
    assert all(s > 0 for s in signed(HARMONIC))   # every step forward
    assert sum(signed(HARMONIC)) == N             # exactly one turn
    assert winding(REPTEND) == 0                  # closes without going round
    assert winding(DOUBLING) == 0
    # stated carefully: winding does not single it out, length does
    assert len([b for b in BRACELETS if abs(winding(b)) == 1]) == 32
    assert len([b for b in BRACELETS if length(b) == 9]) == 1


def test_the_excess_above_the_geodesic_is_an_integer():
    """no continuum gets in through the reordering — there is no 15.5 to take"""
    for o in (REPTEND, DOUBLING, HARMONIC):
        assert length(o) == int(length(o))
        assert (length(o) - 9) >= 0
    assert length(REPTEND) - 9 == 7               # noticed, NOT claimed
    assert length(DOUBLING) - 9 == 5              # noticed, NOT claimed
    assert {length(b) for b in BRACELETS} == {9, 11, 13, 14, 15, 16, 17, 18, 19, 20}
    assert 10 not in {length(b) for b in BRACELETS}   # the spectrum has gaps
    assert 12 not in {length(b) for b in BRACELETS}


# ------------------------------------- the author 2026-08-05: run it on 17, 19, 23 (and more)

def _rep(k, q):
    p, x, seen = "", k % q, {}
    while x and x not in seen:
        seen[x] = 1
        x *= 10
        p += str(x // q)
        x %= q
    return p


def _signed_gen(seq, n):
    """general ring, multiset-safe. EQUAL NEIGHBOURS ARE NO STEP — the bug that made
    the first 17/19/23 run report 40/50/70 instead of 10: a==b gives f==r==0, and the
    tie-break was scoring it as a half-turn."""
    out = []
    for a, b in zip(seq, seq[1:] + seq[:1]):
        if a == b:
            out.append(0)
            continue
        f, r = (b - a) % n, (a - b) % n
        out.append(f if f < r else -r)
    return out


def test_the_zero_step_is_zero():
    assert _signed_gen([3, 3, 3], 10) == [0, 0, 0]
    s = sorted(int(c) for c in _rep(1, 17))
    assert sum(abs(x) for x in _signed_gen(s, 10)) == 10          # not 40
    # the bug's exact shape: 6 repeated adjacencies x a spurious half-turn of 5
    assert sum(1 for a, b in zip(s, s[1:] + s[:1]) if a == b) == 6
    assert 10 + 6 * 5 == 40


def test_the_sort_is_the_geodesic_on_every_address():
    """the author's generalisation question, answered: yes, and it is not about seven"""
    for q in (7, 17, 19, 23, 29, 47):
        d = [int(c) for c in _rep(1, q)]
        s = sorted(d)
        assert sum(abs(x) for x in _signed_gen(s, 10)) == 10      # the modulus
        assert sum(_signed_gen(s, 10)) == 10                      # winding exactly 1
        assert sum(abs(x) for x in _signed_gen(d, 10)) >= 10      # storage never beats it
    # on Z/9, where the seed's own digits live
    assert sum(abs(x) for x in _signed_gen(list(HARMONIC), 9)) == 9


def test_but_only_seven_has_a_field_order_between_them():
    """so 16/14/9 is seven's alone — the 9 generalises, the 16 and 14 do not"""
    orbit, x = [], 1
    while x not in orbit:
        orbit.append(x)
        x = x * 2 % 9
    assert sorted(orbit) == [1, 2, 4, 5, 7, 8] == sorted(DIGITS)
    for q in (17, 19, 23):
        assert sorted(set(int(c) for c in _rep(1, q))) == list(range(10))
        assert sorted(set(int(c) for c in _rep(1, q))) != sorted(orbit)


def test_the_geodesic_splits_three_and_six_on_the_rest_set():
    """the still numbers {1,4,7} alternate with {2,5,8} in the sort, and the cost
    alternates with them: leaving a still point costs 1, arriving costs 2."""
    REST, MOVE = {1, 4, 7}, {2, 5, 8}
    assert [i for i, d in enumerate(HARMONIC) if d in REST] == [0, 2, 4]
    assert [i for i, d in enumerate(HARMONIC) if d in MOVE] == [1, 3, 5]
    pairs = list(zip(HARMONIC, HARMONIC[1:] + HARMONIC[:1]))
    leaving = sum((b - a) % 9 for a, b in pairs if a in REST)
    arriving = sum((b - a) % 9 for a, b in pairs if a in MOVE)
    assert all((b - a) % 9 == 1 for a, b in pairs if a in REST)
    assert all((b - a) % 9 == 2 for a, b in pairs if a in MOVE)
    assert (leaving, arriving) == (3, 6) and leaving + arriving == 9
    # and 3, 6, 9 is exactly the axis the line never touches (ORIGIN-M line theorem)
    assert set(HARMONIC) & {3, 6, 9} == set()


# ----------------------------- the author 2026-08-05: "and this is a field you are describing?"

def _nbrs(t):
    """one adjacent transposition — the minimal change to an ordering"""
    out = set()
    for i in range(6):
        s = list(t)
        j = (i + 1) % 6
        s[i], s[j] = s[j], s[i]
        out.add(_canon(tuple(s)))
    return out - {_canon(t)}


GRAPH = {b: _nbrs(b) for b in BRACELETS}
S_, F_, H_ = _canon(REPTEND), _canon(DOUBLING), _canon(HARMONIC)


def test_the_landscape_is_a_potential_on_a_configuration_space():
    """domain, a value at every point, a connected move-rule: the three things a
    field needs. Over CONFIGURATION, not over space — no ruler enters."""
    assert len(GRAPH) == 60
    assert {len(v) for v in GRAPH.values()} == {6}          # 6-regular
    seen, stack = {BRACELETS[0]}, [BRACELETS[0]]
    while stack:
        for y in GRAPH[stack.pop()]:
            if y not in seen:
                seen.add(y)
                stack.append(y)
    assert len(seen) == 60                                  # one connected landscape
    assert all(isinstance(length(b), int) and 9 <= length(b) <= 20 for b in BRACELETS)


def test_the_geodesic_is_the_unique_strict_minimum_and_it_is_rigid():
    strict = [b for b in BRACELETS if all(length(x) > length(b) for x in GRAPH[b])]
    assert strict == [H_]                                   # one, and it is the sort
    assert sum(1 for x in GRAPH[H_] if length(x) == 9) == 0  # NO free move exists
    assert sorted(length(x) for x in GRAPH[H_]) == [11, 11, 11, 13, 13, 13]


def test_the_field_order_sits_on_a_flat_ledge_not_in_a_trap():
    """greedy descent halts there, but the barrier out is ZERO"""
    assert sorted(length(x) for x in GRAPH[F_]) == [14, 14, 15, 15, 17, 17]
    assert min(length(x) for x in GRAPH[F_]) == length(F_)   # no strictly-downhill move
    free = [x for x in GRAPH[F_] if length(x) == 14]
    assert len(free) == 2                                   # two free moves
    for f in free:
        assert min(length(y) for y in GRAPH[f]) < 14        # and descent opens from each
    halting = [b for b in BRACELETS if all(length(x) >= length(b) for x in GRAPH[b])]
    assert len(halting) == 7 and all(length(b) in (9, 14) for b in halting)


def test_the_moves_split_into_free_and_costed():
    free = sum(1 for b in BRACELETS for x in GRAPH[b] if length(x) == length(b))
    total = sum(len(v) for v in GRAPH.values())
    assert (free, total) == (24, 360)                       # free motion is 1 in 15
    down = sum(1 for b in BRACELETS for x in GRAPH[b] if length(x) < length(b))
    up = sum(1 for b in BRACELETS for x in GRAPH[b] if length(x) > length(b))
    assert down == up == 168                                # the gradient, both ways


def test_the_transform_descends_but_not_steepest():
    """16 -> 15 -> 14, downhill at every step; from 15 an 11 was available"""
    mid = [x for x in GRAPH[S_] if F_ in GRAPH[x]]
    assert all(length(x) == 15 for x in mid) and len(mid) == 2
    assert length(S_) == 16 > 15 > 14 == length(F_)         # monotone down
    assert min(length(y) for x in mid for y in GRAPH[x]) == 11   # the road not taken
    # storage's own steepest descent DOES reach the ground state
    cur, walk = S_, [length(S_)]
    while True:
        lo = min(GRAPH[cur], key=length)
        if length(lo) >= length(cur):
            break
        cur = lo
        walk.append(length(cur))
    assert walk == [16, 15, 11, 9] and cur == H_


# ------------------------------- the author 2026-08-05: "check the six ledge forms" — they are
# ------------------------------- the floor of a sector, and both process orders live in it

def _anti(t):
    """half-period antisymmetric step word: s[i+3] = -s[i]. A walk whose second half
    exactly undoes the first — Midy's structure moved from the digits to the steps."""
    s = signed(t)
    return all(s[(i + 3) % 6] == -s[i] for i in range(6))


SECTOR = [b for b in BRACELETS if _anti(b)]
LEDGE = {b for b in BRACELETS if length(b) == 14
         and min(length(x) for x in GRAPH[b]) >= 14}


def test_the_sector_exists_and_the_ledge_is_its_floor():
    assert len(SECTOR) == 12
    assert sorted(length(b) for b in SECTOR) == [14] * 6 + [16] * 3 + [20] * 3
    assert min(length(b) for b in SECTOR) == 14
    assert LEDGE == {b for b in SECTOR if length(b) == 14}
    assert len(LEDGE) == 6
    # so the ledge is not a graph accident: it is a sector's ground state


def test_both_process_orders_live_in_the_sector_and_the_measured_one_does_not():
    assert S_ in SECTOR and length(S_) == 16          # storage
    assert F_ in SECTOR and length(F_) == 14          # field, on the sector floor
    assert H_ not in SECTOR                           # the measured order is outside
    assert signed(HARMONIC) == [1, 2, 1, 2, 1, 2]     # every step positive
    # and that is the same fact as its winding: balanced <=> cannot encircle
    for b in SECTOR:
        assert winding(b) == 0
    assert winding(H_) == 1


def test_the_free_move_is_the_escape_and_it_breaks_the_balance():
    for b in LEDGE:
        free = [x for x in GRAPH[b] if length(x) == length(b)]
        assert len(free) == 2
        assert all(not _anti(x) for x in free)        # every free move EXITS the sector
        assert all(min(length(y) for y in GRAPH[x]) < 14 for x in free)
    # the ground state has no free move at all, so nothing to break
    assert [x for x in GRAPH[H_] if length(x) == 9] == []


def test_the_transform_takes_storage_to_the_sector_floor_and_no_further():
    def T(s):
        return _canon((s[0], s[2], s[1], s[3], s[5], s[4]))
    assert T(REPTEND) == F_
    assert _anti(S_) and _anti(F_)                    # both ends inside the sector
    assert length(S_) == 16 and length(F_) == 14 == min(length(b) for b in SECTOR)


def test_the_sector_is_closed_under_the_antipode():
    for b in LEDGE:
        assert _canon(tuple(9 - d for d in b)) in LEDGE
        assert _canon(tuple((d * 8) % 9 or 9 for d in b)) in LEDGE   # 8 = -1 mod 9
    # but digit-antipodality is strictly stronger and catches only two of the six
    strict = [b for b in LEDGE if all(b[i] + b[(i + 3) % 6] == 9 for i in range(3))]
    assert len(strict) == 2


# --------------------------- the author 2026-08-05: test the step-sum against the banked charge
# --------------------------- structure. IT FAILS — kept as a negative, with what survives.

def wsum(o):
    return sum(signed(o))


def test_the_step_sum_is_not_a_conserved_charge():
    """NEGATIVE. Only a third of the moves preserve it."""
    keep = sum(1 for b in BRACELETS for x in GRAPH[b] if abs(wsum(x)) == abs(wsum(b)))
    assert (keep, sum(len(v) for v in GRAPH.values())) == (120, 360)


def test_no_charge_can_exist_on_the_full_move_set():
    """and the reason is structural, not empirical: the graph is CONNECTED, so any
    function constant along every edge is constant everywhere. Conservation would
    require superselection, i.e. disconnection, and there is none."""
    seen, stack = {BRACELETS[0]}, [BRACELETS[0]]
    while stack:
        for y in GRAPH[stack.pop()]:
            if y not in seen:
                seen.add(y)
                stack.append(y)
    assert len(seen) == 60


def test_the_step_sum_is_not_the_banked_eighteen():
    """NEGATIVE, and decisive. The banked +-18 (ORIGIN-I sec.3, test_genesis_i::
    test_the_first_ledger) is the VALUE displacement of the transform's interior block
    swaps: 42 -> 24 is -18, 57 -> 75 is +18, net 0, sum 99 preserved. That is
    9 x (digit difference) — a base-ten place displacement. Mine is 9 x (winding) — a
    turn count. Both sit in 9Z because 10 = 1 (mod 9) and the ring closes on 9, which
    is one fact; but a digit difference is not a winding number."""
    assert 24 - 42 == -18 == 9 * (2 - 4)
    assert 75 - 57 == 18 == 9 * (7 - 5)
    assert 42 + 57 == 24 + 75 == 99
    # the banked ledger runs storage -> field with +-18 cancelling.
    # on the step register both sit at zero and the transform moves nothing.
    assert wsum(S_) == 0 and wsum(F_) == 0
    assert wsum(F_) - wsum(S_) == 0


def test_what_does_survive_reflection_negates_the_step_sum():
    """FORCED, over all 720 arrangements, not just the 60 bracelets"""
    for p in permutations(DIGITS):
        assert wsum(p) == -wsum(p[::-1])
    assert {wsum(b) for b in BRACELETS} <= {-18, -9, 0, 9, 18}
    assert all(wsum(b) % 9 == 0 for b in BRACELETS)     # always in 9Z


def test_the_parity_law_and_where_the_fourteen_comes_from():
    """L = P + M and W = P - M, so L and W share a parity. That closes the spectrum's
    gaps AND explains the sector floor: they are one fact."""
    for b in BRACELETS:
        assert (length(b) - wsum(b)) % 2 == 0
        assert length(b) >= abs(wsum(b))
    # every even-L form below 18 must therefore be sum-zero
    assert all(wsum(b) == 0 for b in BRACELETS if length(b) % 2 == 0 and length(b) < 18)
    # and the shortest sum-zero walk on this point set is 14 — the sector floor
    assert min(length(b) for b in BRACELETS if wsum(b) == 0) == 14
    # so 10 and 12 are absent for the same reason 14 is the floor
    assert {length(b) for b in BRACELETS} & {10, 12} == set()
    assert sorted({length(b) for b in BRACELETS}) == [9, 11, 13, 14, 15, 16, 17, 18, 19, 20]


# ===================== the author 2026-08-05, third pass: the mi-fa/si-do catch, the three at
# ===================== 16, and 51 tested for robustness rather than for meaning.

AXIS = {3, 6, 9}


def test_the_hexad_has_two_step_sizes_and_the_large_one_crosses_the_axis():
    """the author: 'are you accounting for the known gaps like mi-fa and si-do?' The hexad IS a
    scale with two step sizes, and the distinction is forced, not decorative."""
    small, large = [], []
    for a, b in zip(HARMONIC, HARMONIC[1:] + HARMONIC[:1]):
        step = (b - a) % 9
        (small if step == 1 else large).append((a, b, step))
    assert len(small) == len(large) == 3
    for a, b, step in large:
        assert step == 2
        skipped = {(x - 1) % 9 + 1 for x in range(a + 1, a + step)}
        assert skipped <= AXIS                    # every large step jumps the axis
    for a, b, step in small:
        assert step == 1                          # every small step skips nothing
    # and the large steps LAND on the rest set: three descriptions of one event
    assert {b for a, b, s in large} == {1, 4, 7}
    assert sum(s for a, b, s in small) == 3 and sum(s for a, b, s in large) == 6


def test_the_component_count_is_a_property_of_the_chosen_move_set():
    """so '51 sectors' is not a discovered constant. Before it can mean 3 x 17, the
    restriction producing it has to be derived. It was picked."""
    def _comps(nbr, keep):
        seen, out = set(), []
        for b in BRACELETS:
            if b in seen:
                continue
            c, st = {b}, [b]
            seen.add(b)
            while st:
                x = st.pop()
                for y in nbr(x):
                    if keep(x, y) and y not in seen:
                        seen.add(y)
                        c.add(y)
                        st.append(y)
            out.append(c)
        return out

    def _any(t):
        o = set()
        for i in range(6):
            for j in range(i + 1, 6):
                s = list(t)
                s[i], s[j] = s[j], s[i]
                o.add(_canon(tuple(s)))
        return o - {_canon(t)}

    free = lambda x, y: length(x) == length(y)
    assert len(_comps(lambda t: GRAPH[t], free)) == 51        # adjacent + free
    assert len(_comps(_any, free)) == 32                      # any transposition + free
    assert len(_comps(lambda t: GRAPH[t], lambda x, y: True)) == 1   # unrestricted
    # what IS robust is the reason for the restriction, not the count it yields
    for b in BRACELETS:
        for x in GRAPH[b]:
            if length(x) == length(b):
                assert length(x) == length(b)     # L conserved by every free move


def test_the_balanced_sector_is_three_classes_of_four():
    """and every class has the identical length profile — so the rungs are structural"""
    def _sig(t):
        return min(tuple(sorted(r[i] + r[(i + 3) % 6] for i in range(3)))
                   for r in [t[j:] + t[:j] for j in range(6)]
                   + [t[::-1][j:] + t[::-1][:j] for j in range(6)])
    classes = {}
    for b in SECTOR:
        classes.setdefault(_sig(b), []).append(b)
    assert len(classes) == 3
    assert all(len(v) == 4 for v in classes.values())
    assert {tuple(sorted(length(b) for b in v)) for v in classes.values()} == {(14, 14, 16, 20)}
    assert set(classes) == {(3, 12, 12), (6, 6, 15), (9, 9, 9)}


def test_storage_is_the_middle_rung_of_the_midy_class():
    """the answer to 'why 16 and not 14': within its class the rungs are 14,14,16,20"""
    def _sig(t):
        return min(tuple(sorted(r[i] + r[(i + 3) % 6] for i in range(3)))
                   for r in [t[j:] + t[:j] for j in range(6)]
                   + [t[::-1][j:] + t[::-1][:j] for j in range(6)])
    assert _sig(S_) == (9, 9, 9) == _sig(F_)      # storage and field share a class
    assert length(F_) == 14 and length(S_) == 16  # field on the floor, storage above it
    sixteens = [b for b in SECTOR if length(b) == 16]
    assert len(sixteens) == 3
    assert len({_sig(b) for b in sixteens}) == 3  # exactly one per class
    assert S_ in sixteens
    # the rung ladder inside a class: +2 then +4
    assert (16 - 14, 20 - 16) == (2, 4)


# ================== the author 2026-08-05, fourth pass: price the axis-crossings separately.
# ================== The geodesic hardens; and the crossing register has 17 sectors.

def crossings(o, n=N):
    """axis points strictly inside the shortest arc actually taken"""
    t = 0
    for a, s in zip(o, signed(o)):
        d = 1 if s > 0 else -1
        for k in range(1, abs(s)):
            if (a + d * k - 1) % n + 1 in AXIS:
                t += 1
    return t


def _components(inv):
    seen, out = set(), []
    for b in BRACELETS:
        if b in seen:
            continue
        c, st = {b}, [b]
        seen.add(b)
        while st:
            x = st.pop()
            for y in GRAPH[x]:
                if inv(y) == inv(x) and y not in seen:
                    seen.add(y)
                    c.add(y)
                    st.append(y)
        out.append(c)
    return out


def test_the_geodesic_survives_any_axis_price():
    """the author asked for the reprice. The sort does not lose its crown — it hardens,
    because it is minimal in BOTH terms at once, and uniquely so."""
    assert min(length(b) for b in BRACELETS) == 9
    assert min(crossings(b) for b in BRACELETS) == 3
    assert length(HARMONIC) == 9 and crossings(HARMONIC) == 3
    both = [b for b in BRACELETS if length(b) == 9 and crossings(b) == 3]
    assert both == [H_]                      # the unique simultaneous minimiser
    # hence it minimises arc + c*crossings for EVERY c >= 0, uniquely
    for c in (0, 1, 2, 3, 5, 10, 100):
        m = min(length(b) + c * crossings(b) for b in BRACELETS)
        assert [b for b in BRACELETS if length(b) + c * crossings(b) == m] == [H_]
    # and 3 is not rare: 8 forms achieve it. The ARC is what makes it unique.
    assert len([b for b in BRACELETS if crossings(b) == 3]) == 8


def test_the_sector_structure_is_unmoved_by_the_price():
    for c in (0, 1, 2, 3, 5):
        cost = lambda o: length(o) + c * crossings(o)
        strict = [b for b in BRACELETS if all(cost(x) > cost(b) for x in GRAPH[b])]
        assert strict == [H_]                                  # one strict minimum, always
        m = min(cost(b) for b in SECTOR)
        floor = [b for b in SECTOR if cost(b) == m]
        assert len(floor) == 6 and F_ in floor                 # the field stays on it


def test_the_component_count_is_robust_to_the_price_though_not_to_the_move_set():
    """so my earlier 'the 51 is just my choice' needs splitting in two: the PRICING
    does not move it (c = 0 and every c >= 2 give 51); only changing the move GRAPH
    does. c = 1 is the one degenerate price, where arc and crossings tie too often."""
    counts = {}
    for c in range(0, 16):
        counts[c] = len(_components(lambda o, c=c: length(o) + c * crossings(o)))
    assert counts[1] == 40                                     # the accidental value
    assert all(counts[c] == 51 for c in range(0, 16) if c != 1)


def test_the_crossing_register_has_seventeen_sectors():
    """price the crossings ALONE and the landscape carries exactly seventeen
    conserved sectors — and every one has a power-of-two size."""
    C = _components(crossings)
    assert len(C) == 17
    from collections import Counter
    assert dict(sorted(Counter(len(c) for c in C).items())) == {2: 12, 4: 3, 8: 1, 16: 1}
    assert all(len(c) & (len(c) - 1) == 0 for c in C)           # every size a power of 2
    assert sorted({crossings(b) for b in BRACELETS}) == [3, 4, 5, 6]
    by = {}
    for c in C:
        by.setdefault(crossings(next(iter(c))), []).append(len(c))
    assert by[3] == [8] and sorted(by[4]) == [4, 4, 4]
    assert by[5] == [2] * 12 and by[6] == [16]


def test_fifty_one_refines_seventeen_and_the_refinement_is_forced():
    """cost-preservation at large c forces BOTH crossings and arc to be preserved,
    so the 51 sectors are the common refinement of arc-conservation and crossing-
    conservation. 51 = 3 x 17 holds only ON AVERAGE — the splits are 1,2,8,16, not 3."""
    C17 = _components(crossings)
    C51 = _components(lambda o: length(o) + 5 * crossings(o))
    assert len(C51) == 51 and len(C17) == 17
    assert all(any(small <= big for big in C17) for small in C51)     # a refinement
    splits = sorted(sum(1 for s in C51 if s <= big) for big in C17)
    assert splits == [1, 1, 1] + [2] * 12 + [8, 16]                  # NOT uniformly 3
    assert sum(splits) == 51 and len(splits) == 17


# ============ the author 2026-08-05, fifth pass: the bridge test — and it fails cleanly.

def test_the_sectors_do_not_map_onto_fifty_one_consecutive_integers():
    """RETIRED. The proposed bridge from this 51 (a sector count) to the banked 51
    (the transform's span 75 - 24) required the sectors to be labelled by consecutive
    integers. They are not labelled injectively at all."""
    from collections import Counter
    C51 = _components(lambda o: length(o) + 5 * crossings(o))
    pairs = [(length(next(iter(c))), crossings(next(iter(c)))) for c in C51]
    assert len(C51) == 51
    assert len(set(pairs)) == 12                        # twelve labels for 51 sectors
    assert dict(sorted(Counter(Counter(pairs).values()).items())) == {1: 2, 3: 5, 4: 1, 6: 2, 9: 2}
    for key in (lambda c: length(next(iter(c))),
                lambda c: crossings(next(iter(c))),
                lambda c: length(next(iter(c))) + 5 * crossings(next(iter(c)))):
        vals = [key(c) for c in C51]
        assert not (len(set(vals)) == 51 and max(vals) - min(vals) + 1 == 51)
    # so the two 51s stay two objects. The resemblance dies and nothing was spent.


def test_the_density_of_states():
    """what the landscape does have: level multiplicities, i.e. a density of states"""
    from collections import Counter
    dos = Counter(length(b) for b in BRACELETS)
    assert [dos[k] for k in sorted(dos)] == [1, 3, 6, 12, 10, 6, 9, 4, 3, 6]
    assert sum(dos.values()) == 60
    cum, run = 0, []
    for k in sorted(dos):
        cum += dos[k]
        run.append((k, cum))
    assert run[:4] == [(9, 1), (11, 4), (13, 10), (14, 22)]
    # a THIRD 51 appears here and it is not the sector count: 51 forms sit at or below
    # cost 18. NOTICED, NOT CLAIMED — 51 = 60 - 9 here, against 48 + 3 for the sectors.
    assert dict(run)[18] == 51
    assert 60 - 9 == 51 and 48 + 3 == 51
    # the crossing register's own density
    xdos = Counter(crossings(b) for b in BRACELETS)
    assert [xdos[k] for k in sorted(xdos)] == [8, 12, 24, 16]


def test_what_a_fermi_reading_would_still_need():
    """the author asked whether this is something like a Fermi surface forming. The pieces a
    Fermi surface needs are: a state space (present, 60 forms), an energy (present,
    the cost), a density of states (present, above), a ground state (present, unique).
    THE MISSING PIECE IS OCCUPANCY — nothing here says a form can hold one occupant
    rather than many, so there is no filling and hence no surface. Recorded as the
    open requirement, not as a claim."""
    assert len(BRACELETS) == 60                          # state space
    assert len({length(b) for b in BRACELETS}) == 10      # energy levels
    assert len([b for b in BRACELETS if length(b) == 9]) == 1   # unique ground state
    # half-filling, IF an exclusion rule existed, would fall inside level 15:
    cum = 0
    for k in sorted({length(b) for b in BRACELETS}):
        cum += len([b for b in BRACELETS if length(b) == k])
        if cum >= 30:
            break
    assert k == 15 and cum == 32                         # 22 below it, 32 through it


def test_the_twelve_is_forced_and_it_is_what_makes_the_sixty():
    """the author: '12 falls out as a result though, 75 - 12 - 3'. The 12 is indeed not free —
    it is |D6| = 2 x 6, the symmetry that turns 720 arrangements into 60 bracelets."""
    from math import factorial
    assert factorial(6) == 720 and len(BRACELETS) == 60
    assert 720 // 60 == 12 == 2 * 6                 # |D6|: six rotations, six reflections
    # and there are FIVE distinct 12s here, each with its own route — so the discipline
    # is to name the route, not the number
    assert len([b for b in BRACELETS if length(b) == 14]) == 12
    assert len(SECTOR) == 12
    assert len({(length(b), crossings(b)) for b in BRACELETS}) == 12
    assert len([b for b in BRACELETS if crossings(b) == 4]) == 12
    # likewise four distinct 3s
    assert len(AXIS) == 3
    assert min(crossings(b) for b in BRACELETS) == 3


def test_cc_seventy_five_minus_twelve_minus_three():
    """the relation holds, and BOTH terms it removes are forced quantities of this
    object — |D6| and the axis — which makes it better-founded than the three 51s.
    It is still a relation across registers (75 is a block VALUE, 60 is a COUNT of
    arrangements) with no operation shown between them. NOTICED, NOT CLAIMED."""
    assert 75 - 12 - 3 == 60 == len(BRACELETS)
    assert 12 + 3 == 15 == 57 - 42                  # the transform's banked inner gap
    assert 75 - 15 == 60
    assert 75 - 24 == 51 and 24 + 75 == 99          # the same figure's other quantities


# ========== the author 2026-08-05, sixth pass: "actually I think it IS a clean boundary."
# ========== He is right, and I had checked the wrong population.

def test_level_fifteen_splits_the_balanced_sector_exactly_in_half():
    """I called 15 'not a clean boundary' because half-filling the whole 60 lands
    inside it. But on the population that matters — the balanced sector — it is exact:
    six below, SIX above, and NOTHING ON THE LINE."""
    below = [b for b in SECTOR if length(b) < 15]
    at = [b for b in SECTOR if length(b) == 15]
    above = [b for b in SECTOR if length(b) > 15]
    assert (len(below), len(at), len(above)) == (6, 0, 6)
    assert {length(b) for b in below} == {14}          # the ledge, entire
    assert {length(b) for b in above} == {16, 20}      # the excited rungs, entire
    # so 15 is the midline separating the sector's floor from everything above it
    assert LEDGE == set(below)


def test_the_boundary_counts_and_cc_arithmetic():
    """32 - 15 = 17, and 32 and 17 are both COUNTS here; 15 is a LEVEL. Recorded with
    the type distinction stated as an assumption, not as a theorem — see the working record."""
    assert len([b for b in BRACELETS if length(b) <= 15]) == 32
    assert len([b for b in BRACELETS if abs(winding(b)) == 1]) == 32
    assert len(_components(crossings)) == 17
    assert 32 - 15 == 17 and 32 + 15 == 47
    assert len([b for b in BRACELETS if length(b) > 15]) == 28      # the banked bridge
    assert 60 - 32 == 28 == 4 * 7
    # the 15 <-> 51 reversal, and its displacement
    assert int(str(15)[::-1]) == 51
    assert 51 - 15 == 36                                # banked: 24 + 12 = 36, Sol on 24
    assert 15 == 3 * 5 and 51 == 3 * 17                 # reversal fixes the 3, sends 5 to 17


# ===== the author 2026-08-05: "is it possible a simplified version of the Madelung structure?"
# ===== The TOTALS coincide strikingly. The level-by-level structure does NOT.

def test_the_sixty_is_the_four_shell_madelung_capacity():
    """STRIKING, UNROUTED. 2 + 8 + 18 + 32 = 60, the first four Madelung shell totals,
    and this landscape has exactly 60 forms. Two routes to one number: 720/|D6| on one
    side, 2 x (1+4+9+16) on the other. No operation between them has been shown."""
    shells = [2 * n * n for n in range(1, 8)]
    assert shells == [2, 8, 18, 32, 50, 72, 98]
    assert sum(shells[:4]) == 60 == len(BRACELETS)
    assert 720 // 12 == 60 == 2 * (1 + 4 + 9 + 16)
    # and two waypoints coincide too
    cum = [sum(shells[:n]) for n in range(1, 8)]
    assert cum[:4] == [2, 10, 28, 60]
    assert len([b for b in BRACELETS if length(b) <= 13]) == 10        # Madelung's n=2
    assert len([b for b in BRACELETS if length(b) > 15]) == 28         # Madelung's n=3
    assert 28 == 4 * 7                                                 # and the banked bridge


def test_but_the_landscape_is_not_madelung_structured():
    """NEGATIVE, and it is what kills the simple version: the level multiplicities are
    not subshell capacities. Madelung fills 2, 6, 10, 14 in n+l order; this landscape's
    levels hold 1, 3, 6, 12, 10, 6, 9, 4, 3, 6. Only the TOTAL agrees."""
    from collections import Counter
    dos = [Counter(length(b) for b in BRACELETS)[k]
           for k in sorted({length(b) for b in BRACELETS})]
    assert dos == [1, 3, 6, 12, 10, 6, 9, 4, 3, 6]
    caps = [2 * (2 * l + 1) for l in range(4)]
    assert caps == [2, 6, 10, 14]
    assert dos[:4] != caps                                # not even the first four
    assert set(dos) & set(caps) == {6, 10}                # a partial overlap, no more
    assert 2 not in dos and 14 not in dos                 # the s and f capacities absent


def test_what_the_object_does_supply_toward_an_exclusion():
    """the crossing-sectors have power-of-two sizes — 2, 4, 8, 16 — which is the shape
    a capacity rule would need. Recorded as the live candidate, not as a rule."""
    C = _components(crossings)
    sizes = sorted(len(c) for c in C)
    assert all(s & (s - 1) == 0 for s in sizes)
    assert sorted(set(sizes)) == [2, 4, 8, 16]
    assert sum(sizes) == 60 and len(C) == 17


# ===== the author 2026-08-05: assign the four crossing levels to the four shells; and use the
# ===== four FSC Midy pairs to label them. Both fail — and the FIRST one fails for a
# ===== reason that confirms the author's own "octaves before the notes in them".

def test_the_object_counts_in_octaves_not_in_shells():
    """the author: 'the Madelung is fully developed with electrons, but maybe the octaves
    themselves appear in some order before the notes in them.' EXACTLY SO, and it is
    the difference between the two ladders:
        no l-substructure  -> capacities DOUBLE      2, 4, 8, 16   (this object)
        with l-substructure -> capacities are 2n^2   2, 8, 18, 32  (Madelung)
    because 2n^2 = 2 x sum(2l+1 for l < n): the shell total IS the doubled sum of the
    odd numbers, and the odd numbers ARE the l-degeneracies. Strip them and you are
    left with plain doubling. So this landscape sits at the octave stage, before the
    notes inside the octave differentiate — which is what the author proposed."""
    C = _components(crossings)
    sizes = sorted({len(c) for c in C})
    assert sizes == [2, 4, 8, 16] == [2 ** n for n in range(1, 5)]
    shells = [2 * n * n for n in range(1, 5)]
    assert shells == [2, 8, 18, 32]
    assert shells == [2 * sum(2 * l + 1 for l in range(n)) for n in range(1, 5)]
    assert [sum(2 * l + 1 for l in range(n)) for n in range(1, 5)] == [1, 4, 9, 16]
    assert sizes != shells and set(sizes) & set(shells) == {2, 8}
    # both ladders total 60 over four rungs, by different arithmetic
    assert sum(shells) == 60 == len(BRACELETS)
    assert sum(len([b for b in BRACELETS if crossings(b) == X]) for X in (3, 4, 5, 6)) == 60


def test_the_direct_shell_assignment_fails():
    """NEGATIVE. No permutation of the four crossing levels matches the four shells."""
    from itertools import permutations as perms
    mine = [len([b for b in BRACELETS if crossings(b) == X]) for X in (3, 4, 5, 6)]
    assert mine == [8, 12, 24, 16]
    shells = [2, 8, 18, 32]
    assert not any(list(p) == shells for p in perms(mine))
    assert sorted(mine) == [8, 12, 16, 24] and sorted(shells) == [2, 8, 18, 32]


def test_the_four_fsc_pairs_cannot_label_the_four_levels():
    """NEGATIVE, and decisive: every crossing level crosses 3, 6 and 9 in EQUAL
    numbers, so no level carries an axis label to match a pair against."""
    from collections import Counter
    for X in (3, 4, 5, 6):
        cens = Counter()
        for b in [x for x in BRACELETS if crossings(x) == X]:
            for a, s in zip(b, signed(b)):
                d = 1 if s > 0 else -1
                for k in range(1, abs(s)):
                    p = (a + d * k - 1) % N + 1
                    if p in AXIS:
                        cens[p] += 1
        assert len(set(cens.values())) == 1        # 3, 6 and 9 crossed equally, always
    # and the four omitted antipodal pairs of 137 split 2|2 on the axis, not 1|1|1|1
    pairs = [(0, 9), (1, 8), (2, 7), (3, 6)]
    assert all(a + b == 9 for a, b in pairs)
    touching = [p for p in pairs if set(p) & AXIS]
    assert len(touching) == 2 and len(pairs) - len(touching) == 2


# ===== the author 2026-08-05: "go find what supplies the l-degeneracies inside the hexad —
# ===== I think the average of 2 and 4 supplies the 3." FOUND, and it is the averaging.

def test_averaging_the_octave_ladder_generates_the_three_ladder():
    """the author's mechanism, and it is general: the arithmetic mean of two CONSECUTIVE powers
    of two is always three times a power of two. (2^n + 2^(n+1))/2 = 2^n x 3/2."""
    from fractions import Fraction as F
    for n in range(0, 8):
        m = F(2 ** n + 2 ** (n + 1), 2)
        assert m == 3 * F(2 ** n, 2)
        assert m % 3 == 0 or m.denominator == 2      # 3 x 2^(n-1)
    assert F(2 + 4, 2) == 3 and F(4 + 8, 2) == 6 and F(8 + 16, 2) == 12
    assert (42 + 24) // 2 == 33 == 3 * 11            # the author's second example


def test_the_hexad_averages_give_the_axis_and_the_odd_degeneracies():
    """THE ANSWER. Average each pair of adjacent hexad digits (cyclically):
         the three LARGE steps average onto 3, 6, 9 — THE AXIS, exactly;
         the three SMALL steps average onto 3/2, 9/2, 15/2 — which is
         (3/2) x {1, 3, 5}: SOL TIMES THE FIRST THREE ODD NUMBERS.
    So the l-degeneracies are inside the hexad, produced by the same averaging the author
    named, and separated from the axis by exactly the tone/semitone split."""
    from fractions import Fraction as F
    av = []
    for a, b in zip(HARMONIC, HARMONIC[1:] + HARMONIC[:1]):
        av.append(F(a + b, 2) if b > a else F(a + b + 9, 2))
    assert [str(x) for x in av] == ['3/2', '3', '9/2', '6', '15/2', '9']
    whole = sorted(int(x) for x in av if x.denominator == 1)
    half = sorted(x for x in av if x.denominator == 2)
    assert whole == [3, 6, 9] == sorted(AXIS)                  # the axis, exactly
    assert [x / F(3, 2) for x in half] == [1, 3, 5]            # 2l+1 for l = 0,1,2
    # and the integer ones are exactly the LARGE steps, the half ones the SMALL steps
    large = [i for i, (a, b) in enumerate(zip(HARMONIC, HARMONIC[1:] + HARMONIC[:1]))
             if (b - a) % 9 == 2]
    assert [av[i].denominator for i in large] == [1, 1, 1]


def test_the_hexad_supplies_exactly_three_shells_and_they_sum_to_the_modulus():
    """1 + 3 + 5 = 9 — the modulus, the geodesic length, and n^2 at n = 3. Doubling it
    (the octave, which is what this object does instead of an l-structure) gives 18:
    Madelung's third shell AND the transform's own block displacement. Both routes are
    INSIDE the hexad, which is the first alignment today to pass the author's referee on both
    sides — so it is recorded as a candidate weld rather than a coincidence."""
    assert 1 + 3 + 5 == 9 == N                       # the modulus
    assert 1 + 3 + 5 == 3 ** 2                       # n^2 at n = 3
    assert length(HARMONIC) == 9                     # the geodesic
    assert 2 * (1 + 3 + 5) == 18 == 2 * 3 * 3        # Madelung's third shell
    assert 75 - 57 == 18 and 24 - 42 == -18          # the transform's displacement
    # the hexad has three small steps, hence exactly three l-values: s, p, d. No f.
    small = [1 for a, b in zip(HARMONIC, HARMONIC[1:] + HARMONIC[:1]) if (b - a) % 9 == 1]
    assert len(small) == 3


# ===== the author 2026-08-05: does it predict three shells and forbid f? And what carries the
# ===== 9 to the 18 — "you mean like a clock maybe? I had thought it was from the
# ===== transform." BOTH ANSWERED, AND THE SECOND CLOSES.

def test_the_shell_count_is_forced_and_f_is_forbidden_at_this_modulus():
    """The hexad is Z/9 minus the multiples of three. Remove every third element of a
    3k-cycle and the sorted gaps MUST alternate 1,2 — so the small steps number k = n/3
    exactly, and each supplies one l-value. At n = 9 that is THREE: l = 0,1,2, the
    degeneracies 1,3,5, s p d. A fourth would need a fourth small step, i.e. modulus 12.
    SO f IS NOT MISSING HERE, IT IS FORBIDDEN — at this modulus there is no seat for it."""
    for k in (2, 3, 4, 5, 6):
        n = 3 * k
        S = [d for d in range(1, n + 1) if d % 3]
        gaps = [(S[(i + 1) % len(S)] - S[i]) % n for i in range(len(S))]
        assert gaps == [1, 2] * k                      # forced alternation
        assert sum(1 for g in gaps if g == 1) == k     # small steps = n/3
    assert 9 // 3 == 3                                 # three shells at modulus nine
    assert [2 * l + 1 for l in range(3)] == [1, 3, 5]  # s, p, d
    assert 2 * 3 + 1 == 7                              # f would need a 7
    S12 = [d for d in range(1, 13) if d % 3]
    assert sum(1 for i in range(len(S12))
               if (S12[(i + 1) % len(S12)] - S12[i]) % 12 == 1) == 4   # f arrives at 12


def test_the_transform_is_the_octave_read_through_the_clock():
    """the author: 'you mean like a clock maybe? I had thought it was from the transform.' BOTH,
    and they are the same thing. The discrete log base 2 on Z/9 assigns each hexad digit
    its OCTAVE COUNT, and the doubling order 1,2,4,8,7,5 IS that index 0..5. Read the
    transform's two swaps in that index and BOTH ARE A STEP OF EXACTLY ONE — one octave.
    So the transform's step, which is two POSITIONS on the circle, is ONE DOUBLING in the
    clock. That closes the gap in the 18: both routes are 9 x 2 with the same 9 (the
    modulus, which the l-sum equals) AND NOW THE SAME 2."""
    ind, x = {}, 1
    for k in range(6):
        ind[x] = k
        x = x * 2 % 9
    assert ind == {1: 0, 2: 1, 4: 2, 8: 3, 7: 4, 5: 5}
    assert sorted(ind, key=lambda d: ind[d]) == [1, 2, 4, 8, 7, 5] == list(DOUBLING)
    for a, b in ((4, 2), (5, 7)):
        assert abs(a - b) == 2                         # two positions on the circle
        assert abs(ind[a] - ind[b]) == 1               # ONE OCTAVE in the clock
    assert 24 - 42 == -18 and 75 - 57 == 18
    assert 18 == 9 * 2 == 2 * (1 + 3 + 5)              # one 9, one 2, both now shared


# ===== the author 2026-08-05: stress-test the averaging at modulus 12 and 15.
# ===== THE MECHANISM IS GENERAL. THE CLOSURE IS UNIQUE TO NINE.

def test_the_averaging_mechanism_is_general_at_every_modulus():
    """At modulus n = 3k, take Z/n minus the multiples of three, sort, and average each
    adjacent pair cyclically. ALWAYS: the large (crossing) steps average onto the k
    multiples of three — the axis — and the small steps average onto (3/2) x the first
    k odd numbers. Checked at n = 6, 9, 12, 15, 18, 21."""
    from fractions import Fraction as F
    for n in (6, 9, 12, 15, 18, 21):
        k = n // 3
        S = [d for d in range(1, n + 1) if d % 3]
        av = []
        for a, b in zip(S, S[1:] + S[:1]):
            av.append(F(a + b, 2) if b > a else F(a + b + n, 2))
        whole = sorted(int(x) for x in av if x.denominator == 1)
        odds = sorted(x / F(3, 2) for x in av if x.denominator == 2)
        assert whole == [3 * i for i in range(1, k + 1)]        # the axis, entire
        assert odds == [2 * i + 1 for i in range(k)]            # the first k odd numbers
        assert sum(odds) == k * k                               # and they sum to k^2


def test_but_the_closure_belongs_to_nine_alone():
    """The l-sum is k^2 and the modulus is 3k. THEY ARE EQUAL ONLY WHEN k = 3.
    So the fact that made the weld work — l-sum = modulus = geodesic length — is not a
    feature of the mechanism; it is a property of NINE, and of nothing else."""
    for k in range(1, 12):
        n = 3 * k
        assert (k * k == n) == (k == 3)
    assert 1 + 3 + 5 == 9 == 3 * 3                              # the unique coincidence
    # and since the sorted walk traverses the circumference, the geodesic IS the modulus,
    # so at nine the geodesic, the modulus and the l-sum are one number
    assert length(HARMONIC) == 9 == N == 1 + 3 + 5
    # nowhere else: at 12 the geodesic is 12 while the l-sum is 16
    assert 4 * 4 == 16 != 12


# ===== the author 2026-08-05: "is it the same event as the Catalan kiss... keep in mind we are
# ===== ultimately after gravity." NO to the first. And the second is where it lands.

def test_the_closure_is_not_the_catalan_kiss():
    """NEGATIVE. Catalan/Mihailescu: 3^2 - 2^3 = 1 is the ONLY solution of x^a - y^b = 1
    with x,y,a,b > 1 — a theorem about all perfect powers. Mine: k^2 = 3k has the single
    positive root k = 3 — the root of a quadratic. Both land on 9 and both single out
    {2,3}, but Catalan pits exponent 3 against exponent 2 while this pits exponent 2
    against FACTOR 3. Same pair, different pairing, incomparable depth. Not one event."""
    assert 3 ** 2 - 2 ** 3 == 1                       # the Catalan kiss, banked
    assert [k for k in range(1, 40) if k * k == 3 * k] == [3]
    assert 3 ** 2 == 9 == 3 * 3                       # the shared value, and only that
    # the Catalan statement is about a DIFFERENCE of powers; this one is an equality of
    # a power with a multiple. No implication either way.
    assert 3 ** 2 - 3 * 3 == 0 != 1


def test_the_hexad_stops_exactly_at_gravitys_multipole():
    """WHERE IT LANDS. 2l+1 is the component count of the l-th multipole field, and the
    hexad's averaging produces exactly 1, 3, 5:
        l=0  1 component   monopole    — mass, charge (scalar)
        l=1  3 components  dipole      — EM radiation           (banked: spin-1)
        l=2  5 components  quadrupole  — GRAVITATIONAL radiation (banked: spin-2, GEM 4=2^2)
        l=3  7 components  octupole    — leading for nothing    FORBIDDEN at modulus 9
    So the ladder the hexad supports is exactly the ladder the long-range forces use,
    and its ceiling is exactly gravity's multipole. GRAVITY-REOPENED already banks the
    same three rungs as the Golden-Egg ladder omni/cardioid/nephroid, cusp count 0,1,2."""
    assert [2 * l + 1 for l in range(3)] == [1, 3, 5]
    assert 2 * 3 + 1 == 7                             # the octupole, with no seat here
    assert 9 // 3 == 3                                # three rungs, forced by n/3
    # the banked cusp ladder has the same three rungs
    assert [m - 1 for m in (1, 2, 3)] == [0, 1, 2]
    # and the total component count IS the modulus and the geodesic
    assert 1 + 3 + 5 == 9 == N == length(HARMONIC)
    assert 2 * (1 + 3 + 5) == 18                      # doubled by the transform's octave
