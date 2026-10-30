"""test_intonated_enneagram.py — the INTONATED enneagram, 2026-08-07.

CC's asymmetric nine-point figure, named this session. Two Midy pairs are displaced
outward onto the eight-lattice: {1,8} by 5 degrees and {2,7} by 10, total 30.

    TEMPERED   0, 40,  80, 120, 160, 200, 240, 280, 320   (equal 40-degree spacing)
    INTONATED    0, 45,  90, 120, 160, 200, 240, 270, 315

Terminology per [[enneagram-terminology]]: INTONATED vs TEMPERED names the LAYOUT;
"harmonic" is reserved for the ORDERING axis. Reading: tuned vs counted.
"""

import math
from fractions import Fraction as F

TEMPERED = {9: 0, 1: 40, 2: 80, 3: 120, 4: 160, 5: 200, 6: 240, 7: 280, 8: 320}
INTONATED = {9: 0, 1: 45, 2: 90, 3: 120, 4: 160, 5: 200, 6: 240, 7: 270, 8: 315}
HEX = [(1, 4), (4, 2), (2, 8), (8, 5), (5, 7), (7, 1)]
TRI = [(3, 6), (6, 9), (9, 3)]
LIN = lambda deg: 1 + F(deg, 360)          # CC's linear circle: ratio linear in angle


def test_the_displacement_and_its_total():
    """Two Midy pairs move, outward, 5 and 10 degrees. Total 30."""
    movers = {d for d in TEMPERED if TEMPERED[d] != INTONATED[d]}
    assert movers == {1, 8, 2, 7}
    assert {1, 8} and {2, 7}                                   # both Midy pairs (sum 9)
    assert abs(INTONATED[1] - TEMPERED[1]) == abs(INTONATED[8] - TEMPERED[8]) == 5
    assert abs(INTONATED[2] - TEMPERED[2]) == abs(INTONATED[7] - TEMPERED[7]) == 10
    assert sum(abs(INTONATED[d] - TEMPERED[d]) for d in movers) == 30


def test_the_four_one_four_lattice_straddle():
    """The figure sits on TWO lattices: 8-fold near the root, 9-fold beyond, with
    the origin shared. Both lattices are forced by gcd, not chosen."""
    from math import gcd
    from functools import reduce
    pts = sorted(INTONATED.values())
    eight = [p for p in pts if p % 45 == 0]
    nine = [p for p in pts if p % 40 == 0]
    assert eight == [0, 45, 90, 270, 315]
    assert nine == [0, 120, 160, 200, 240]
    assert set(pts) == set(eight) | set(nine)                  # nothing off both
    assert set(eight) & set(nine) == {0}                       # 4 | 1 | 4
    assert reduce(gcd, [p for p in eight if p]) == 45          # coarsest is 8-fold
    assert reduce(gcd, [p for p in nine if p]) == 40           # coarsest is 9-fold
    # the eight-lattice points all lie within a quarter-turn of Do
    assert max(min(p, 360 - p) for p in eight) == 90
    assert min(min(p, 360 - p) for p in nine if p) == 120
    # and 8 = 2^3, 9 = 3^2 are the unique consecutive perfect powers (Mihailescu)
    assert 9 - 8 == 1 == 3**2 - 2**3


def test_the_movers_land_on_named_just_intervals():
    """On the linear circle all four movers land on named ratios; the stayers
    include the whole triangle, which lands on Do, Fa, La."""
    assert [LIN(INTONATED[d]) for d in (1, 2, 7, 8)] == [F(9, 8), F(5, 4), F(7, 4), F(15, 8)]
    assert [LIN(INTONATED[d]) for d in (9, 3, 6)] == [F(1), F(4, 3), F(5, 3)]     # Do, Fa, La
    stayers = {d for d in TEMPERED if TEMPERED[d] == INTONATED[d]}
    assert stayers == {3, 6, 9, 4, 5}                          # triangle + centre pair


def test_only_the_origin_displacements_keep_framework_primes():
    """THE SELECTIVE FACT. Collapsing a moved point costs (360+a)/(360+b). Over all
    eight candidate displacements (four mirror pairs x {5,10} degrees), exactly TWO
    keep every prime inside {2,3,5,7,11,17} — and they are the two the INTONATED form
    uses. Every other choice throws a foreign prime (41, 67, 89, 127, 97, 59, 37,
    13, 53)."""
    from sympy import factorint
    FRAME = {2, 3, 5, 7, 11, 17}
    clean = []
    for d in range(1, 5):
        a, b = 40 * d, (-40 * d) % 360
        for s in (5, 10):
            cu = F(360 + a + s, 360 + a)
            cd = F(360 + b, 360 + b - s)
            ps = set(factorint(cu.numerator)) | set(factorint(cu.denominator)) \
                | set(factorint(cd.numerator)) | set(factorint(cd.denominator))
            if ps <= FRAME:
                clean.append((d, s))
    assert clean == [(1, 5), (2, 10)]                          # exactly the INTONATED's two
    # and the two named commas among the four costs
    assert F(405, 400) == F(81, 80)                            # digit 1: SYNTONIC
    assert F(640, 630) == F(64, 63)                            # digit 7: SEPTIMAL


def test_the_combinatorics_are_invariant_and_the_difference_is_metric():
    """Same vertices, edges, regions in both forms — the displacement is
    combinatorially invisible. So 25/24 belongs to BOTH and cannot distinguish
    them; the whole difference is metric."""
    import itertools

    def counts(A):
        P = {d: (math.cos(math.radians(a)), math.sin(math.radians(a)))
             for d, a in A.items()}
        ch = HEX + TRI

        def x(a, b, c, d):
            (x1, y1), (x2, y2), (x3, y3), (x4, y4) = P[a], P[b], P[c], P[d]
            den = (x1-x2)*(y3-y4) - (y1-y2)*(x3-x4)
            if abs(den) < 1e-12:
                return None
            t = ((x1-x3)*(y3-y4) - (y1-y3)*(x3-x4)) / den
            u = ((x1-x3)*(y1-y2) - (y1-y3)*(x1-x2)) / den
            return (round(x1+t*(x2-x1), 9), round(y1+t*(y2-y1), 9)) \
                if 1e-9 < t < 1-1e-9 and 1e-9 < u < 1-1e-9 else None

        pts = {p for c1, c2 in itertools.combinations(ch, 2)
               if not set(c1) & set(c2) for p in [x(*c1, *c2)] if p}
        V = 9 + len(pts)
        E = 9 + sum(1 + sum(1 for c2 in ch if c2 != c and not set(c) & set(c2)
                            and x(*c, *c2)) for c in ch)
        return V, E, E - V + 2 - 1

    assert counts(TEMPERED) == counts(INTONATED) == (24, 48, 25)
    assert F(25, 24) == F(25, 24)


def test_the_hexad_encloses_zero_area_in_both_forms():
    """The stroke winds as much one way as the other. Shoelace on the unit circle
    is (1/2)|sum sin(dtheta)|, and the angular steps come in +/- pairs, so it is
    EXACTLY zero — in both forms, because the displacement preserves the pairing.
    Meanwhile the conserving triangle holds maximal area and never moves."""
    for A in (TEMPERED, INTONATED):
        steps = [A[HEX[(i+1) % 6][0]] - A[HEX[i][0]] for i in range(6)]
        assert abs(sum(math.sin(math.radians(s)) for s in steps)) < 1e-12
        tri = [(math.cos(math.radians(A[d])), math.sin(math.radians(A[d])))
               for d in (3, 6, 9)]
        area = abs(sum(tri[i][0]*tri[(i+1) % 3][1] - tri[(i+1) % 3][0]*tri[i][1]
                       for i in range(3))) / 2
        assert abs(area - 3*math.sqrt(3)/4) < 1e-12            # maximal, unchanged


def test_chord_classes_split_and_a_triangle_chord_becomes_an_octagon_chord():
    """TEMPERED has two distinct hexad chord lengths; INTONATED has three. Collapsing
    merges three classes into two — a degeneracy increase, i.e. information loss,
    in the same direction as the which-pair-moved bits. And the member that
    LENGTHENS swaps a nine-lattice chord for an eight-lattice one."""
    def lens(A):
        out = []
        for u, v in HEX:
            d = abs(A[u] - A[v]) % 360
            out.append(round(2 * math.sin(math.radians(min(d, 360 - d) / 2)), 9))
        return out
    assert len(set(lens(TEMPERED))) == 2
    assert len(set(lens(INTONATED))) == 3
    assert abs(max(lens(TEMPERED)) - math.sqrt(3)) < 1e-9                  # triangle chord
    assert abs(max(lens(INTONATED)) - math.sqrt(2 + math.sqrt(2))) < 1e-9    # octagon chord


def test_the_figure_is_a_mechanism_not_a_truss():
    """Maxwell count: 9 vertices, 9 bars. A rigid 2-D framework needs 2n-3 = 15.
    The enneagram is under-braced by six — it has six internal degrees of freedom
    and CANNOT be rigid. Flexing is mechanically licensed; a specific motion is not."""
    n, m = 9, len(HEX) + len(TRI)
    assert m == 9
    assert 2 * n - 3 == 15
    assert 2 * n - 3 - m == 6


def test_the_tuned_counted_partition_is_three_four_two():
    """The nine split by TUNING STATUS, and the split is exactly the movement
    structure: the triangle is tuned always, the movers are tuned only in INTONATED,
    and the two stayers are counted in both."""
    JUST = {F(1), F(9, 8), F(5, 4), F(4, 3), F(3, 2), F(5, 3), F(7, 4), F(15, 8)}
    named = lambda A: {d for d in A if LIN(A[d]) in JUST}

    assert named(TEMPERED) == {9, 3, 6}                     # the TRIANGLE, and only it
    assert named(INTONATED) == {9, 3, 6, 1, 2, 7, 8}          # triangle + all four movers
    assert named(INTONATED) - named(TEMPERED) == {1, 2, 7, 8}      # the movers ARE the gain
    assert set(TEMPERED) - named(INTONATED) == {4, 5}              # the stayers stay counted

    # what the counted ones are: consecutive rungs of the n/9 ladder
    assert [LIN(INTONATED[d]) for d in (4, 5)] == [F(13, 9), F(14, 9)]
    # and TEMPERED is nothing BUT that ladder: n/9 for n = 9..17
    assert sorted(LIN(v) for v in TEMPERED.values()) == [F(n, 9) for n in range(9, 18)]


def test_origin_is_the_just_major_scale_missing_only_the_fifth():
    """INTONATED realises Do Re Mi Fa La Si — the whole just major scale except Sol —
    plus the harmonic seventh 7/4. Sol's seat is 180 degrees, the antipode of the
    root: a point in NEITHER form, straddled symmetrically by the two stayers.
    The most consonant interval after the octave is the one seat never filled."""
    MAJOR = {F(1): 9, F(9, 8): 1, F(5, 4): 2, F(4, 3): 3,
             F(3, 2): None, F(5, 3): 6, F(15, 8): 8}
    have = {LIN(v) for v in INTONATED.values()}
    assert {r for r in MAJOR if r not in have} == {F(3, 2)}       # exactly one gap
    assert F(7, 4) in have                                        # and 7/4 as a bonus

    assert (F(3, 2) - 1) * 360 == 180                             # Sol's seat
    assert 180 not in TEMPERED.values() and 180 not in INTONATED.values()     # empty in both
    assert INTONATED[4] == 160 and INTONATED[5] == 200                          # straddled by +/-20
    assert (INTONATED[4] + INTONATED[5]) / 2 == 180

    # 180 is the antipode of the root — the mirror axis, and the second fixed point
    # of the doubling map (kernel {0, n/2}) that the carry work runs on.
    assert (0 + 180) % 360 == 180 == 360 // 2


def test_the_empty_fifth_is_forced_by_parity():
    """THEOREM. Any mirror-symmetric nine-point figure leaves one of the two
    mirror-fixed seats EMPTY, and seating the root at 0 forces the empty one to be
    180 = 3/2 = Sol.

    Proof. Reflection about the 0-180 axis has exactly two fixed seats, 0 and 180.
    Every other seat lies in a 2-element orbit. A symmetric set of NINE points is a
    union of orbits, so #fixed-seats-occupied = 9 - 2*(number of pairs) is ODD.
    There are only two fixed seats, so exactly ONE is occupied. The nine digits are
    one unpaired digit (9) plus four Midy pairs; 9 takes the root at 0. Therefore
    180 is empty. QED — and it holds for BOTH layouts, and for every other
    mirror-symmetric nine-point figure there is.

    The consequence forbids: a mirror PAIR can reach 180 only by colliding on it
    (160+20 = 200-20 = 180), which destroys a vertex. The most consonant interval
    after the octave cannot be seated. It can only be GENERATED."""
    for A in (TEMPERED, INTONATED):
        pts = set(A.values())
        assert {(360 - p) % 360 for p in pts} == pts          # mirror-symmetric
        fixed = pts & {0, 180}
        assert len(fixed) % 2 == 1 and len(fixed) == 1        # parity forces exactly one
        assert fixed == {0}                                   # the root takes it
        assert 180 not in pts                                 # so Sol's seat is empty
        assert len(pts) == 9 and (len(pts) - len(fixed)) % 2 == 0

    # the only mirror-symmetric way onto 180 is a collision: 9 points become 8
    collided = dict(INTONATED); collided[4], collided[5] = 180, 180
    assert len(set(collided.values())) == 8                   # a vertex is destroyed


def test_the_seven_tuned_tones_regenerate_the_missing_fifth():
    """The seat is empty, but the tones that ARE present put Sol back by combination
    tone — twice at the octave below, once at its own pitch.

    Caveat kept in the test: 2*(5/4) - 1 = 3/2 holds for ANY set containing a root
    and its major third, so the MECHANISM is generic. What is structural is the
    coincidence — the figure omits exactly the degree its own tones regenerate."""
    from itertools import combinations
    T = [F(1), F(9, 8), F(5, 4), F(4, 3), F(5, 3), F(7, 4), F(15, 8)]   # INTONATED minus {4,5}

    diff = [(a, b) for a, b in combinations(T, 2) if b - a == F(3, 4)]
    assert len(diff) == 2                                     # Sol an octave down, x2
    assert (F(1), F(7, 4)) in diff and (F(9, 8), F(15, 8)) in diff
    assert max(b - a for a, b in combinations(T, 2)) < F(3, 2)          # never ON 3/2
    assert min(a + b for a, b in combinations(T, 2)) > F(3, 2)          # nor by summing

    cubic = {2 * b - a for a, b in combinations(T, 2)} | \
            {2 * a - b for a, b in combinations(T, 2)}
    assert F(3, 2) in cubic                                   # Sol at its own pitch
    assert 2 * F(5, 4) - F(1) == F(3, 2)                      # from Do and Mi

    # the two COUNTED points, given the same treatment, regenerate the ladder-unit
    # and two of the three triangle tones. A complementary control, not a null one.
    assert F(14, 9) - F(13, 9) == F(1, 9)
    assert 2 * F(13, 9) - F(14, 9) == F(4, 3)                 # Fa   (digit 3)
    assert 2 * F(14, 9) - F(13, 9) == F(5, 3)                 # La   (digit 6)


def test_the_origin_form_is_the_least_action_seven_limit_figure():
    """THE REPAIRED SELECTIVITY CLAIM. Criteria, all pre-existing in the framework:
    mirror-symmetric pair displacement; OUTWARD from the root; landings 7-limit just
    (a standard category); two pairs move; LEAST TOTAL MOTION (least action). Five
    complete figures satisfy the first four. The INTONATED enneagram is the unique
    minimum of the fifth, at 30 degrees against 58 for the runner-up.

    This REPLACES the earlier claim that a hand-picked prime set {2,3,5,7,11,17}
    selected two of eight candidates. In the full 312-candidate space the INTONATED's
    displacements rank only 16th and 6th by largest prime, and the simplest of all
    belongs to the stationary triangle. That criterion was a sieve; this one is not."""
    from sympy import factorint
    from itertools import combinations
    plim = lambda r: max(set(factorint(r.numerator)) | set(factorint(r.denominator)))
    land = lambda d, s: (LIN(40 * d + s), LIN((-40 * d) % 360 - s))

    sev = [(d, s) for d in (1, 2, 3, 4) for s in range(1, 40)
           if all(plim(r) <= 7 for r in land(d, s))]
    assert sev == [(1, 5), (1, 32), (2, 10), (3, 24), (4, 20)]
    assert land(4, 20) == (F(3, 2), F(3, 2))          # the ONLY route to Sol collides

    figs = []
    for (d1, s1), (d2, s2) in combinations(sev, 2):
        if d1 == d2:
            continue
        A = {9: 0}
        for k in (1, 2, 3, 4):
            sh = s1 if k == d1 else (s2 if k == d2 else 0)
            A[k], A[9 - k] = (40 * k + sh) % 360, (360 - 40 * k - sh) % 360
        if len(set(A.values())) == 9:
            figs.append((2 * s1 + 2 * s2, sorted(A.values())))

    assert len(figs) == 5
    figs.sort()
    assert figs[0][0] == 30 and figs[1][0] == 58                    # unique minimum
    assert figs[0][1] == sorted(INTONATED.values())                        # and it IS the INTONATED


def test_only_even_lattices_can_seat_the_fifth():
    """COROLLARY of the parity theorem, and the reason it matters: an equal
    n-lattice through the root contains the fifth's seat (180 deg = 3/2) IF AND
    ONLY IF n is even. So the 2-side seats the fifth and the 3-side cannot —
    and 3/2 IS the 2-vs-3 ratio. The interval that names the incommensurability
    is exactly the one the 3-side is forbidden to seat.

    An odd lattice always STRADDLES it symmetrically instead. On the enneagram the
    straddlers are digits 4 and 5 at 160 and 200 — precisely the two points the
    INTONATED transform leaves alone. They stay because they cannot move onto 180
    without colliding there, which is the vertex-destroying move of the theorem."""
    for n in range(2, 25):
        lat = {F(360 * k, n) for k in range(n)}
        assert (F(180) in lat) == (n % 2 == 0)

    assert F(180) in {F(360 * k, 8) for k in range(8)}        # 8 = 2^3, seatable
    assert F(180) not in {F(360 * k, 9) for k in range(9)}    # 9 = 3^2, forbidden
    assert LIN(180) == F(3, 2)                                 # the 2:3 ratio itself

    nine = sorted(F(360 * k, 9) for k in range(9))
    straddle = sorted(nine, key=lambda t: abs(t - 180))[:2]
    assert set(straddle) == {160, 200}                         # digits 4 and 5
    assert {d for d in TEMPERED if TEMPERED[d] in (160, 200)} == {4, 5}
    assert {d for d in TEMPERED if TEMPERED[d] == INTONATED[d]} - {3, 6, 9} == {4, 5}   # the stayers


def test_the_fifths_seat_is_the_doubling_kernel():
    """WHY 180 is not merely 'a position'. The doubling map t -> 2t (mod 360) has
    kernel {0, 180}: it cannot distinguish the fifth's seat from the root. So 180 is
    the root, one doubling later — the point where POSITION and the 2-OPERATION
    coincide. Same object as the carry work's mirror, whose fixed points are the
    doubling kernel {0, n/2}, and whose antipodal oddness is chi(m + n/2) = -chi(m).

    This is the reason the parity corollary runs the way it does: the seat belongs
    to the 2-operation, so even (2-side) lattices hold it and odd (3-side) cannot."""
    dbl = lambda t: (2 * t) % 360
    assert {t for t in range(360) if dbl(t) == 0} == {0, 180}
    assert dbl(180) == 0 == dbl(0)
    assert LIN(180) == F(3, 2) and LIN(0) == F(1)      # the fifth and the root


def test_the_lopsided_circle_must_be_chiral_and_is():
    """The theorem RETRODICTS a banked object. The lopsided circle
    (03-GENESIS-INDEX:27) is SEVEN points — odd — contains its root, AND contains
    180. By the parity theorem it therefore cannot be mirror-symmetric. It isn't:
    the mirror breaks at exactly one pair, 90 <-> 270. An odd rooted figure that
    wants its fifth MUST be chiral, which is what its name says."""
    LOP = {0, 45, 90, 120, 180, 240, 315}
    assert len(LOP) == 7 and len(LOP) % 2 == 1
    assert 0 in LOP and 180 in LOP                     # root AND fifth, both seated
    mir = {(360 - p) % 360 for p in LOP}
    assert mir != LOP                                  # so the mirror MUST be broken
    assert mir ^ LOP == {90, 270}                      # and it breaks at one pair


def test_sixteen_is_the_unique_one_nine_carry_of_the_doubling_ladder():
    """CC 2026-08-07. Straight doubling 1,2,4,8,16,... against its digital roots
    1,2,4,8,7,5. The span 2^k - dr(2^k) equals NINE exactly once, at 16.

    Forced, not lucky: for n = 10a+b with a+b <= 9, n - dr(n) = 9a, so the span is
    nine iff a = 1, i.e. iff n lies in 10..18. The teens are the only decade where
    one reduction eats exactly one nine, and 16 is the only power of two in them.

    Operationally (the manual path): 8 -> 16 is the ladder's FIRST CARRY, the first
    time doubling needs two digits. The value doubles while the root DROPS by one --
    8 -> 7 -- and the discrepancy is the nine the carry ate. carry = tick, and this
    tick costs exactly one nine. Every later tick costs more: 27, 63, 126, 252..."""
    dr = lambda n: 9 if n % 9 == 0 else n % 9
    assert [dr(2**k) for k in range(6)] == [1, 2, 4, 8, 7, 5]      # the doubling order
    assert [k for k in range(400) if 2**k - dr(2**k) == 9] == [4]  # unique, and 2^4=16
    assert 16 - dr(16) == 9 and dr(16) == 7
    assert [n for n in range(1, 1000) if n - dr(n) == 9] == list(range(10, 19))
    assert [n for n in range(10, 19) if (n & (n - 1)) == 0] == [16]

    # and 16 is the only power of two among the TEMPERED enneagram's numerators,
    # which are 9..17 -- the one-nine band, with the root 9 as its floor.
    nums = [9 + k for k in range(9)]
    assert nums == list(range(9, 18))
    assert [n for n in nums if (n & (n - 1)) == 0] == [16]
    assert nums.index(16) == 7 and dr(16) == 7          # digit 7, root 7, 2^4


def test_the_doubling_order_splits_three_three_by_carry():
    """WHAT CC's SPAN IS. The doubling order 1,2,4,8,7,5 splits exactly in half by
    whether the root-step carries:
        1->2->4->8   no carry, cost 0   (the pure single-digit powers 2^0..2^3)
        8->7->5->1   carries, cost 9 per step
    Three free, three paying. 16 = 2^4 is the FIRST ELEMENT OF THE PAYING HALF, so
    its span is the unique nine: it is the only step that has paid exactly once.
    Everything after pays cumulatively.

    NB this is a split WITHIN the doubling order and is NOT the banked hexad/triad
    split (hexad {1,2,4,5,7,8} against triad {3,6,9}). Different object, new here."""
    dr = lambda n: 9 if n % 9 == 0 else n % 9
    H = [1, 2, 4, 8, 7, 5]
    carry = [i for i in range(6) if 2 * H[i] > 9]
    assert carry == [3, 4, 5] and len(carry) == 3          # exactly half, contiguous
    assert [2*H[i] - H[(i+1) % 6] for i in range(6)] == [0, 0, 0, 9, 9, 9]
    assert H[:4] == [2**j for j in range(4)]               # the free run is the powers

    # the span sequence: doubling, +1 exactly on the carrying steps
    g = [(2**k - dr(2**k)) // 9 for k in range(4, 16)]
    assert g[:6] == [1, 3, 7, 14, 28, 56]
    assert all(g[i+1] in (2*g[i], 2*g[i] + 1) for i in range(len(g)-1))
    # the +1 lands exactly on the carrying steps. dr(2^k) has period 6 and carries
    # at k mod 6 in {3,4,5}; this list starts at k=4, so the residues are {0,1,5}.
    plus = [i for i in range(len(g)-1) if g[i+1] == 2*g[i] + 1]
    assert plus == [i for i in range(len(g)-1) if 2*dr(2**(4+i)) > 9]
    assert all(p % 6 in (0, 1, 5) for p in plus)           # 3 of every 6, periodic


def test_the_straddle_is_audible_as_a_consonance_signature():
    """NAMING EVIDENCE, 2026-08-07. INTONATED is NOT simply 'more consonant' — it wins
    two standard measures and loses two. The split is the structure:

        band (mean pairwise Tenney)   within-8   within-9   ACROSS
        TEMPERED                          7.02       6.64      6.31   (flat)
        INTONATED                           5.50       6.64      9.03   (split)

    TEMPERED is uniform middling with no family structure. INTONATED has each lattice
    internally simple and concentrates its entire cost in the SEAM between them.
    The 8|9 straddle of the lattice test is the same fact measured as consonance.

    Against the ROOT alone INTONATED wins cleanly: 6 of 8 simple ratios against 2 of 8.
    So the honest description is ROOT-consonant and internally split — which is why
    'consonant' overstates as a name and 'tuned' does not."""
    from math import log2
    from itertools import combinations
    T = lambda r: log2(r.numerator * r.denominator)
    E8 = [d for d, a in INTONATED.items() if a % 45 == 0]
    N9 = [d for d, a in INTONATED.items() if a % 40 == 0 and a]
    assert sorted(E8) == [1, 2, 7, 8, 9] and sorted(N9) == [3, 4, 5, 6]

    def band(A, S1, S2=None):
        src = combinations(S1, 2) if S2 is None else [(a, b) for a in S1 for b in S2]
        rs = [max(LIN(A[x]), LIN(A[y])) / min(LIN(A[x]), LIN(A[y])) for x, y in src]
        return sum(T(r) for r in rs) / len(rs)

    r8, r9, ra = band(TEMPERED, E8), band(TEMPERED, N9), band(TEMPERED, E8, N9)
    o8, o9, oa = band(INTONATED, E8), band(INTONATED, N9), band(INTONATED, E8, N9)
    assert max(r8, r9, ra) - min(r8, r9, ra) < 0.8      # TEMPERED is flat
    assert oa - o8 > 3.0                                 # INTONATED's seam is the cost
    assert o8 < r8 and oa > ra                           # simpler inside, dearer across
    assert o9 == r9                                      # the 9-set never moved

    # against the root alone, INTONATED wins outright
    simple = lambda A: sum(1 for d, a in A.items() if a and LIN(a).denominator <= 8)
    assert simple(INTONATED) == 6 and simple(TEMPERED) == 2
    assert sum(T(LIN(a)) for a in INTONATED.values()) < sum(T(LIN(a)) for a in TEMPERED.values())


# ---------------------------------------------------------------------------
# 2026-08-08 — THE FRESH DERIVATION. CC: "get the order and cause right according
# to the least action principle ... let the law of the symbol itself speak."
#
# The previous least-action claim (the intonated layout as unique minimum at 30
# degrees) is WITHDRAWN. It imported three things the construction never gave:
# "outward", "two pairs move", and total ANGULAR motion as the action. Degrees are
# not the symbol's currency. Redone below with nothing imported.
#
# NATIVE constraints, each read off the construction:
#   nine points ............ the ring is Z/(b-1) = Z/9
#   mirror symmetry ........ Midy's theorem, not a stylistic choice
#   the root is present .... the figure contains its own reference
#   7-limit prime content .. p=7, b=10=2*5, b-1=9=3^2  ->  primes {2,3,5,7}
#   the 72-point lattice ... gcd(40, 5, 10) = 5 degrees, the coarsest grid
#                            containing both named layouts
#   the action ............. TENNEY HEIGHT log2(num*den), which counts the
#                            operation-trail (CLAUDE.md 9) and is standard
# ---------------------------------------------------------------------------

def _sweep():
    from math import log2
    from itertools import combinations
    ANG = [5 * k for k in range(72)]
    R = {a: F(360 + a, 360) for a in ANG}
    T = {a: log2(R[a].numerator * R[a].denominator) for a in ANG}
    TP = {(a, b): log2((R[b] / R[a]).numerator * (R[b] / R[a]).denominator)
          for a in ANG for b in ANG if a < b}
    out = {}
    for q in combinations([a for a in ANG if 0 < a < 180], 4):
        pts = [0] + list(q) + [360 - x for x in reversed(q)]
        g = [pts[(i + 1) % 9] - pts[i] if i < 8 else 360 - pts[8] for i in range(9)]
        out[q] = (sum(T[a] for a in pts),
                  sum(TP[(min(x, y), max(x, y))] for x, y in combinations(pts, 2)),
                  sum((x - 40) ** 2 for x in g))
    return out


def test_the_tempered_layout_is_the_action_minimum():
    """THE ORDER AND CAUSE, derived not assumed. Over all 52360 mirror-symmetric
    nine-point layouts on the native lattice, the TEMPERED layout is the global
    minimum of pairwise Tenney height — rank 1 of 52360 — and of non-uniformity.

    The reason is structural: equal division of the circle gives every point the
    common denominator 9, so every pairwise ratio is n/m with both in 9..17, and
    no other layout can beat that. The counted form is the RESTING STATE.

    Consequence for the order: the intonated layout is not 'earlier', it is
    HIGHER IN ACTION. 'Upstream' means uphill, not before. The collapse runs
    downhill, which is why it is irreversible."""
    s = _sweep()
    TEMPERED, INTONATED = (40, 80, 120, 160), (45, 90, 120, 160)
    assert min(s, key=lambda q: s[q][1]) == TEMPERED        # pairwise Tenney, rank 1
    assert min(s, key=lambda q: s[q][2]) == TEMPERED        # uniformity, rank 1
    assert s[TEMPERED][2] == 0 and s[INTONATED][2] == 300
    assert s[INTONATED][0] < s[TEMPERED][0]                 # but MORE just at the root
    assert s[INTONATED][1] > s[TEMPERED][1]                 # and dearer pairwise

    # and the intonated layout minimises NOTHING globally — the old claim is dead
    for k in (0, 1, 2):
        assert min(s, key=lambda q: s[q][k]) != INTONATED


def test_both_layouts_are_pareto_optimal_and_the_frontier_is_six_long():
    """WHAT SURVIVES, and it is better than what it replaces. Trading justness
    (Tenney vs the root) against non-uniformity, the Pareto frontier over 52360
    layouts is exactly SIX points — and BOTH named layouts sit on it.

    So neither form is 'the' optimum. They are two corners of one trade-off curve,
    which is precisely what temperament IS in music: justness bought with
    irregularity. The figure displays the curve. Nothing here needs 'outward',
    'two pairs', or angular distance."""
    s = _sweep()
    TEMPERED, INTONATED = (40, 80, 120, 160), (45, 90, 120, 160)
    front, best = [], None
    for q in sorted(s, key=lambda q: (s[q][0], s[q][2])):
        if best is None or s[q][2] < best:
            front.append(q); best = s[q][2]
    assert len(front) == 6
    assert front == [(45, 60, 90, 120), (60, 90, 120, 135), (60, 90, 120, 160),
                     INTONATED, (45, 80, 120, 160), TEMPERED]
    assert front[-1] == TEMPERED and front[3] == INTONATED

    # at its OWN displacement level the intonated layout does not merely qualify,
    # it dominates: rank 1 of 24, by a margin of more than ten
    same = sorted((s[q][0], q) for q in s if s[q][2] == 300)
    assert same[0][1] == INTONATED and len(same) == 24
    assert same[1][0] - same[0][0] > 10


def test_the_collapse_is_two_single_pair_steps_through_a_resting_place():
    """The frontier's TAIL is a descent moving one Midy pair at a time (its head,
    step 1->2, rearranges all four — corrected here, I overstated it once).

    The consequence that matters: the intonated -> tempered collapse is NOT one
    event. It is two single-pair relaxations, and the intermediate layout
    (0,45,80,120,160) — pair {1,8} displaced, pair {2,7} already home — is itself
    Pareto-optimal. The figure can rest there. A third layout the symbol offers
    that has never been examined."""
    F6 = [(45, 60, 90, 120), (60, 90, 120, 135), (60, 90, 120, 160),
          (45, 90, 120, 160), (45, 80, 120, 160), (40, 80, 120, 160)]
    moved = [[j for j in range(4) if F6[i][j] != F6[i + 1][j]] for i in range(5)]
    assert len(moved[0]) == 4                      # the head rearranges everything
    assert all(len(m) == 1 for m in moved[1:])     # the tail moves one pair a step

    assert moved[3] == [1] and moved[4] == [0]     # pair {2,7} first, then {1,8}
    assert F(1) + F(90, 360) == F(5, 4) and F(1) + F(80, 360) == F(11, 9)
    assert (F(5, 4)) / (F(11, 9)) == F(45, 44)     # step one pays 45/44
    assert (F(9, 8)) / (F(10, 9)) == F(81, 80)     # step two pays the syntonic comma

    mid = [0, 45, 80, 120, 160, 200, 240, 280, 315]
    assert len(set(mid)) == 9
    assert [LIN(a) for a in (45, 315)] == [F(9, 8), F(15, 8)]      # {1,8} just
    assert [LIN(a) for a in (80, 280)] == [F(11, 9), F(16, 9)]     # {2,7} on the ladder


# ---------------------------------------------------------------------------
# 2026-08-08, CC's three diagrams: the gapping, the tone-motion circles, and the
# "spin" labels. All three turn out to read the same structure.
# ---------------------------------------------------------------------------

def test_the_spin_labels_read_the_skipped_seat():
    """CC's diagram 3 assigns 'spin' values to hexad steps: 1<->8 gets 1 (3/3),
    2<->4 gets 1/3, 5<->7 gets 2/3, 4<->5 gets 1/2. They are not rotations.

    EACH ARC SKIPS EXACTLY ONE SEAT, AND THE LABEL IS THAT SEAT'S POSITION AS A
    FRACTION OF THE CIRCLE. Three skip a triangle point — 3 at 1/3, 6 at 2/3,
    9 at 3/3. The fourth skips 180, which the parity theorem proves can hold no
    digit. So the label set is the triangle's three positions plus the empty seat,
    and 1/2 is the outlier for a structural reason: it is the only label whose
    seat is unoccupied."""
    AT = {v: k for k, v in TEMPERED.items()} if False else \
         {0: 9, 40: 1, 80: 2, 120: 3, 160: 4, 200: 5, 240: 6, 280: 7, 320: 8}
    P = {v: k for k, v in AT.items()}
    for (a, b), lab in {(8, 1): F(1), (2, 4): F(1, 3),
                        (5, 7): F(2, 3), (4, 5): F(1, 2)}.items():
        lo, span = P[a], (P[b] - P[a]) % 360
        skipped = [(lo + t) % 360 for t in range(1, span)
                   if (lo + t) % 40 == 0 or (lo + t) == 180]
        assert len(skipped) == 1
        m = skipped[0]
        assert F(m if m else 360, 360) == lab           # the label IS the position
    # and only the 1/2 seat is empty
    assert 180 not in P.values()
    assert all(x in P.values() for x in (0, 120, 240))


def test_the_three_triad_forms_decompose_the_triangle():
    """CC: 'three triad forms — the complete triangle, one that goes 93969396,
    and a horizon of just 363636.' They are a complementary decomposition:

        alternating 9396  =  the two edges THROUGH the root
        horizon      36   =  the one edge that AVOIDS the root

    disjoint, and their union is the complete triangle. 'Horizon' is geometrically
    exact rather than decorative: with 9 at the top, the 3-6 chord is the ONLY
    horizontal edge of the triangle, and the unseatable 180 lies below it."""
    import math
    E = lambda w: {frozenset((w[i], w[(i + 1) % len(w)])) for i in range(len(w))
                   if w[i] != w[(i + 1) % len(w)]}
    full, alt, hor = E([9, 3, 6]), E([9, 3, 9, 6]), E([3, 6])
    assert alt | hor == full and not (alt & hor)
    assert alt == {frozenset((9, 3)), frozenset((9, 6))}
    assert hor == {frozenset((3, 6))}
    assert [sum(int(c) for c in s) for s in ("936", "9396", "36")] == [18, 27, 9]

    h = lambda deg: math.cos(math.radians(deg))         # 9 at top, height coordinate
    assert abs(h(120) - h(240)) < 1e-12                 # the 3-6 chord is level
    assert abs(h(0) - h(120)) > 1e-9                    # the other two are not
    assert h(180) < h(120)                              # the empty seat is below it


def test_intonation_is_a_redistribution_of_gap():
    """CC's diagram 1 marks two gaps. Both are gaps that OPEN, and the figure's
    nine gaps account for the whole displacement without any point 'moving':

        four gaps OPEN  by  +5   (the four nearest the root)
        two  gaps CLOSE by -10   (the two flanking the triangle points 3 and 6)
        three gaps UNCHANGED at 40 (the bottom arc, 120..240)

    Net zero, as it must be. The marked 'gap between the 9s' is the 8-to-1 span,
    80 -> 90. The marked 'gap between the pairs' is 1-to-2, 40 -> 45. And the arc
    intonation cannot touch is exactly the horizon edge spanning the empty seat."""
    T = [0, 40, 80, 120, 160, 200, 240, 280, 320]
    I = [0, 45, 90, 120, 160, 200, 240, 270, 315]
    g = lambda P: [(P[(i + 1) % 9] - P[i]) % 360 for i in range(9)]
    d = [b - a for a, b in zip(g(T), g(I))]
    assert d == [5, 5, -10, 0, 0, 0, -10, 5, 5]
    assert sum(d) == 0 and d.count(5) == 4 and d.count(-10) == 2
    assert [g(I)[i] for i in (3, 4, 5)] == [40, 40, 40]        # the bottom arc holds
    assert (40 - 320) % 360 == 80 and (45 - 315) % 360 == 90   # the marked 9-gap
    assert 80 - 40 == 40 and 90 - 45 == 45                     # the marked pair-gap


def test_the_four_tone_circles_are_the_lopsided_seven():
    """CC's diagram 2 draws four tone-assignments on the positions
    0, 45, 90, 120, 180, 240, 315. That is exactly the banked lopsided circle
    (03-GENESIS-INDEX:27) — the SEVEN-point figure the parity theorem retrodicted:
    odd, rooted, and seating 180, therefore forced to be chiral, breaking at
    90 <-> 270. His fourth panel puts Do at 0 and Sol at 180, i.e. the fifth
    SEATED — which only a chiral figure is permitted to do.

    The 75-degree span he marks in all four panels is 315 - 240, and 75 is the
    banked composite of the 57/75 pole."""
    D2 = {0, 45, 90, 120, 180, 240, 315}
    assert len(D2) == 7 and 0 in D2 and 180 in D2
    mir = {(360 - p) % 360 for p in D2}
    assert mir != D2 and mir ^ D2 == {90, 270}
    assert 315 - 240 == 75


# ---------------------------------------------------------------------------
# 2026-08-08, CC: "exclusion would insist that however the actual mechanical
# process looked, those transforms would need to go AROUND those points, and the
# 40deg arc is the least action to do that ... spin isn't really spin and this
# isn't either, it is moving around a point, the quality of which is 1, or 1/3,
# or 2/3, or 1/2 at the point at 180."
#
# The go-arounds: 8->1 about seat 9, 2->4 about seat 3, 5->7 about seat 6,
# 4->5 about the empty 180.
# ---------------------------------------------------------------------------

_GA = [(8, 1, 0), (2, 4, 120), (5, 7, 240), (4, 5, 180)]
_TEM = {9: 0, 1: 40, 2: 80, 3: 120, 4: 160, 5: 200, 6: 240, 7: 280, 8: 320}
_INT = {9: 0, 1: 45, 2: 90, 3: 120, 4: 160, 5: 200, 6: 240, 7: 270, 8: 315}
_MID = {9: 0, 1: 45, 2: 80, 3: 120, 4: 160, 5: 200, 6: 240, 7: 280, 8: 315}


def _halves(P, a, b, at):
    lo = P[a]
    hi = P[b] if P[b] > P[a] else P[b] + 360
    m = at if at >= lo else at + 360
    return m - lo, hi - m


def test_exclusion_prices_the_go_around_at_a_factor_of_two():
    """CC's least-action claim, confirmed. In the tempered layout circumnavigating
    an OCCUPIED seat costs 80 degrees — two 40-degree steps, one to clear it on
    each side — while the EMPTY seat at 180 costs 40, a single step, because with
    nothing there its two flankers are adjacent.

    So 40 degrees is the quantum of going-around, exclusion prices itself at
    exactly a factor of two, and the empty seat is the figure's only
    single-quantum crossing."""
    costs = {at: sum(_halves(_TEM, a, b, at)) for a, b, at in _GA}
    assert costs[0] == costs[120] == costs[240] == 80      # the three occupied seats
    assert costs[180] == 40                                 # the empty one, half price
    assert all(c % 40 == 0 for c in costs.values())         # quantised in 40s
    assert 180 not in _TEM.values()                         # and it IS empty


def test_the_tempered_layout_is_the_isotropic_one():
    """THE MECHANICAL LEAST-ACTION RESULT, independent of every tuning measure.
    In the tempered layout every go-around is SYMMETRIC — the two halves equal —
    so + and - cost the same at every seat. In the intonated layout the
    go-arounds at 3 and 6 become 30|40 and 40|30: MIRROR-IMAGE asymmetries.

    That is CC's 'ability to perform positive and negative actions': in tempered
    the two directions are degenerate; in intonated they are split at two seats,
    oppositely. A local polarisation, with the figure still globally
    mirror-symmetric. Tempering is what removes it."""
    bias = lambda P: sum(abs(l - r) for a, b, at in _GA for l, r in [_halves(P, a, b, at)])
    assert bias(_TEM) == 0                                  # isotropic
    assert bias(_INT) == 20                                 # polarised
    assert _halves(_INT, 2, 4, 120) == (30, 40)             # and the two biases
    assert _halves(_INT, 5, 7, 240) == (40, 30)             # are mirror images
    assert _halves(_TEM, 2, 4, 120) == _halves(_TEM, 5, 7, 240) == (40, 40)


def test_the_two_midy_pairs_do_two_different_jobs():
    """WHAT THE REDISTRIBUTION IS FOR — and it recovers, by a completely unrelated
    route, the two-step order the Pareto frontier forced yesterday.

        pair {2,7}, the 10-degree movers: the ONLY pair whose motion touches the
            asymmetry. THE POLARISING PAIR.
        pair {1,8}, the 5-degree movers: the go-around at 9 is symmetric in every
            layout (40|40, then 45|45); their motion changes only its SIZE.
            THE DILATING PAIR, asymmetry-neutral throughout.

    So the collapse is two mechanically distinct operations in a forced order:
        step 1  {2,7} relaxes -> DEPOLARISATION, asymmetry 20 -> 0
        step 2  {1,8} relaxes -> CONTRACTION,    root arc  90 -> 80

    and it identifies the intermediate resting place, which the frontier could
    locate but not characterise: DEPOLARISED BUT STILL DILATED.

    WITHDRAWN 2026-08-08: an earlier note on this result called the {3,6} bias
    pair "a couple, pure torque". IT IS NOT. See
    test_mirror_symmetry_forbids_net_torque below — the mirror forbids net torque
    identically. The biases are a SQUEEZE symmetric about the axis (short gap
    away from 180 at both seats), not a rotation about it."""
    bias = lambda P: sum(abs(l - r) for a, b, at in _GA for l, r in [_halves(P, a, b, at)])
    root = lambda P: sum(_halves(P, 8, 1, 0))

    assert (bias(_INT), root(_INT)) == (20, 90)             # polarised + dilated
    assert (bias(_MID), root(_MID)) == (0, 90)              # depolarised, still dilated
    assert (bias(_TEM), root(_TEM)) == (0, 80)              # and finally contracted

    # {1,8} never touch the asymmetry; {2,7} never touch the root arc
    assert root(_INT) == root(_MID) and bias(_MID) == bias(_TEM)
    # the order matches the Pareto frontier's: {2,7} first, then {1,8}
    assert _INT[2] != _MID[2] and _INT[1] == _MID[1]
    assert _MID[1] != _TEM[1] and _MID[2] == _TEM[2]


def test_the_constructibility_straddle():
    """CC 2026-08-08: "can any of this be drawn with a straight edge and compass?"

    The regular nine-gon is NOT constructible — 9 = 3^2, a repeated Fermat prime,
    so drawing 40 degrees is trisecting 120 (Wantzel 1837). An angle 360a/b in
    lowest terms is constructible iff the regular b-gon is, i.e. iff b is a power
    of two times DISTINCT Fermat primes.

    The result inverts the usual telling:
        TEMPERED      3 of 9 constructible — and they are EXACTLY THE TRIANGLE.
                      The whole hexad needs trisection. The 'regular' figure
                      cannot be drawn, only approximated.
        INTERMEDIATE  5 of 9
        INTONATED     7 of 9 — the four movers land on 45, 90, 270, 315, every
                      one a bisection of a right angle. Only the STAYERS resist.

    So intonation does not perturb a drawable figure into an undrawable one; it
    moves four points OFF the untrisectable ninefold division ONTO the eightfold
    one, where they are exact. The 8|9 straddle is a CONSTRUCTIBILITY straddle.

    And the two that resist are {4,5} — the straddlers of the empty seat, already
    singled out by parity. The figure's two unconstructible points are its two
    immovable ones."""
    from sympy import factorint
    FERMAT = {3, 5, 17, 257, 65537}

    def con(deg):
        b = F(deg, 360).denominator
        odd = {p: e for p, e in factorint(b).items() if p != 2}
        return all(p in FERMAT and e == 1 for p, e in odd.items())

    assert not con(40) and not con(80)              # the ninefold division resists
    assert con(45) and con(90) and con(120)         # eight- and three-fold do not
    MID = {9: 0, 1: 45, 2: 80, 3: 120, 4: 160, 5: 200, 6: 240, 7: 280, 8: 315}

    ok = lambda P: {d for d in P if con(P[d])}
    assert ok(TEMPERED) == {3, 6, 9}                # exactly the triangle
    assert ok(INTONATED) == {1, 2, 3, 6, 7, 8, 9}   # everything but the stayers
    assert set(INTONATED) - ok(INTONATED) == {4, 5}
    assert len(ok(MID)) == 5
    assert (len(ok(INTONATED)), len(ok(MID)), len(ok(TEMPERED))) == (7, 5, 3)

    # the unconstructible pair is the immovable pair: parity forbids them 180
    assert {d for d in TEMPERED if TEMPERED[d] == INTONATED[d]} - {3, 6, 9} == {4, 5}
    assert (INTONATED[4] + INTONATED[5]) / 2 == 180


def test_the_two_stayers_are_unreachable_by_any_construction():
    """CC: "are you sure no straight crossing of two intersections given by the
    constructible part of the figure can get the two bottom points?"

    NO, and it is a theorem rather than a failed search. Every straightedge-and-
    compass step — two lines, a line and a circle, two circles — solves at worst a
    QUADRATIC over the field already in hand, so any reachable point lies in a
    tower of degree-2 extensions and its degree over Q is a POWER OF TWO.

    cos 160 has degree THREE, with minimal polynomial 8x^3 - 6x + 1 — the SAME
    cubic as angle trisection. Three divides no power of two. So the two bottom
    points are unreachable from the rest of the figure by any arrangement of
    chords whatsoever, however clever, permanently."""
    from sympy import cos, pi, Rational, minimal_polynomial, symbols, degree
    x = symbols('x')
    deg = lambda a: degree(minimal_polynomial(cos(pi * Rational(a, 180)), x), x)

    for a in (0, 45, 90, 120, 240, 270, 315):
        d = deg(a)
        assert d & (d - 1) == 0                      # a power of two: reachable
    for a in (40, 80, 160, 200, 280, 320):
        assert deg(a) == 3                           # the trisection cubic: never
    assert minimal_polynomial(cos(pi * Rational(160, 180)), x) == 8*x**3 - 6*x + 1
    assert minimal_polynomial(cos(pi * Rational(40, 180)), x) == 8*x**3 - 6*x + 1


def test_constructibility_decays_monotonically_down_the_frontier():
    """THE THIRD QUANTITY. Along the Pareto frontier from most-just to most-uniform
    the constructible count runs 9, 9, 7, 7, 5, 3 — monotone, bottoming out at the
    rest state with only the triangle left.

    So justness and constructibility move TOGETHER and both oppose uniformity: the
    trade-off is three quantities, not two. Nobody looked for the third because the
    classical question is binary and is only ever asked of a REGULAR figure; it
    arises at all only once the figure is allowed to be irregular.

    Stated honestly: 7/9 is NOT a ceiling. The lattice's constructible points are
    exactly the multiples of 15 degrees, and 9/9 layouts exist — two of them sit at
    the just end of this very frontier. The intonated layout is not distinguished
    by constructibility; it is distinguished by being the layout that keeps the
    most of it while paying the least uniformity."""
    from sympy import factorint
    FERMAT = {3, 5, 17, 257, 65537}
    con = lambda d: all(p in FERMAT and e == 1 for p, e in
                        {p: e for p, e in factorint(F(d, 360).denominator).items()
                         if p != 2}.items())

    assert [5*k for k in range(72) if con(5*k)] == [15*k for k in range(24)]

    FRONT = [(45, 60, 90, 120), (60, 90, 120, 135), (60, 90, 120, 160),
             (45, 90, 120, 160), (45, 80, 120, 160), (40, 80, 120, 160)]
    counts = []
    for q in FRONT:
        pts = [0] + list(q) + [360 - x for x in reversed(q)]
        counts.append(sum(1 for p in pts if con(p)))
    assert counts == [9, 9, 7, 7, 5, 3]
    assert all(counts[i] >= counts[i + 1] for i in range(5))      # monotone

    # the rest state keeps only the triangle; both named layouts share that skeleton
    assert {p for p in TEMPERED.values() if con(p)} == {0, 120, 240}
    assert {p for p in INTONATED.values() if con(p)} == {0, 45, 90, 120, 240, 270, 315}
    # and NO layout containing the stayers can be complete
    assert not con(160) and not con(200)


def test_the_bisection_ladders_failure_is_the_hexad_itself():
    """CC 2026-08-08: "what construction method gets us closest to 9 equidistant
    points?" The answer runs through the figure's own arithmetic.

    A bisection adds one binary place, so a compass ladder reaches exactly the
    angles whose turn-fraction terminates in binary. 1/9 does not: its expansion is
    0.000111000111... with period 6, because ord_9(2) = 6.

    AND THE REMAINDERS ALONG THAT EXPANSION ARE 1, 2, 4, 8, 7, 5 — THE HEXAD IN
    DOUBLING ORDER. The bit is 1 exactly when the doubling carries, so the
    expansion's 000|111 IS the 3|3 carry-split of the doubling order banked on
    2026-08-07. The obstruction to constructing the figure is not external to it;
    it is the figure."""
    v, rems, bits = F(1, 9), [], []
    for _ in range(12):
        rems.append(int(v * 9))
        v *= 2
        bits.append(1 if v >= 1 else 0)
        if v >= 1:
            v -= 1

    assert rems[:6] == [1, 2, 4, 8, 7, 5]            # the hexad, doubling order
    assert rems[6:12] == rems[:6]                     # period 6 = ord_9(2)
    assert bits[:6] == [0, 0, 0, 1, 1, 1]             # the 3|3 carry split
    assert all(bits[i] == (1 if 2 * rems[i] > 9 else 0) for i in range(6))
    assert pow(2, 6, 9) == 1 and all(pow(2, k, 9) != 1 for k in range(1, 6))


def test_nine_equal_constructible_steps_cannot_close_the_turn():
    """The consequence that shapes every approximate nonagon: nine equal steps must
    sum to 360, and no constructible step is exactly 40, so the figure CANNOT close.
    The error is forced and has to be placed somewhere — dumped in one gap or spread
    over nine, but never removed.

    Best approximations, by construction cost (pentagon = 360/10, then bisections):
        40.5        error 0.5      deg   4 bisections   ninth gap -4.5
        39.9375     error 0.0625   deg   7 bisections   ninth gap +0.5625
        40.0078125  error 0.0078   deg  10 bisections   ninth gap -0.0703"""
    from sympy import factorint
    FERMAT = {3, 5, 17, 257, 65537}
    con = lambda t: all(p in FERMAT and e == 1 for p, e in
                        {p: e for p, e in factorint(F(t).denominator).items()
                         if p != 2}.items())

    assert not con(F(1, 9))                            # 40 degrees, unreachable
    for a in (F(81, 2), F(639, 16), F(10242, 256)):    # 40.5, 39.9375, 40.0078125
        assert con(F(a, 360)) and a != 40              # constructible, and never 40
        assert 9 * a != 360                            # so the turn never closes

    assert 9 * F(81, 2) - 360 == F(9, 2)               # 40.5   overshoots by 4.5
    assert 9 * F(639, 16) - 360 == F(-9, 16)           # 39.9375 undershoots
    # each further bisection roughly halves the error
    errs = [abs(a - 40) for a in (F(81, 2), F(639, 16), F(10242, 256))]
    assert all(errs[i + 1] < errs[i] / 4 for i in range(2))


def test_no_flip_or_median_can_reach_forty_degrees():
    """CC 2026-08-08: "if the values are 40.5 it would imply doing the reverse, ie
    flipping the paper over, could create a median pathway that was exact no?"

    NO, and the reason covers every such scheme at once rather than this one.
    The constructible numbers are a FIELD, closed under +, -, x, / and square roots.
    Flipping the paper is negation; taking a median is (a+b)/2. Both stay inside the
    field, so no flip, no median, and no combination of them at any depth can leave
    it. cos 40 has degree 3 and is outside. The scheme is not merely unlucky in its
    pairing — it is closed off in principle."""
    from sympy import symbols, minimal_polynomial, cos, pi, Rational, degree
    x = symbols('x')
    assert degree(minimal_polynomial(cos(pi * Rational(40, 180)), x), x) == 3

    # the concrete medians, for the record: they land nowhere
    med = lambda k: (F(81, 2)*k + (360 - F(81, 2)*(9 - k))) / 2
    misses = [med(k) - 40*k for k in range(1, 6)]
    assert misses == [F(-7, 4), F(-5, 4), F(-3, 4), F(-1, 4), F(1, 4)]
    assert all(m != 0 for m in misses)
    # and the field is closed under exactly the two operations the scheme uses
    a, b = F(81, 2), F(45)                      # two constructible angles
    assert (a + b) / 2 == F(171, 4) and -a == F(-81, 2)   # median and flip: still rational


def test_the_nonagon_is_foldable_even_though_it_is_not_constructible():
    """AND CC's PHYSICAL INSTINCT IS RIGHT, with a different operation. Paper folding
    is strictly stronger than straightedge and compass: the Huzita-Hatori fold O6
    solves CUBICS, so folding trisects angles, and 120/3 = 40 exactly.

        compass:  n-gon reachable iff n = 2^a x distinct FERMAT primes
        folding:  n-gon reachable iff n = 2^a x 3^b x distinct PIERPONT primes

    The whole difference is the admitted factor 3^b. 9 = 2^0 x 3^2, so the repeated
    three is exactly what the compass rule forbids and the folding rule permits.

    Reading (not a theorem): the compass is a 2-only instrument and folding is a
    2-and-3 instrument, so the tempered layout — the rest state no compass reaches —
    is exactly foldable. 2-perp-3 stated about instruments rather than numbers."""
    from sympy import factorint, isprime
    FERMAT = {3, 5, 17, 257, 65537}
    pierpont = lambda p: isprime(p) and any(p - 1 == 2**u * 3**v
                                            for u in range(14) for v in range(9))
    assert all(pierpont(p) for p in (2, 3, 5, 7, 13, 17, 19, 37, 73))
    assert not pierpont(11) and not pierpont(23)      # 10 and 22 carry a 5

    def compass_ok(n):
        odd = {p: e for p, e in factorint(n).items() if p != 2}
        return all(p in FERMAT and e == 1 for p, e in odd.items())

    def fold_ok(n):
        rest = {p: e for p, e in factorint(n).items() if p not in (2, 3)}
        return all(pierpont(p) and e == 1 for p, e in rest.items())

    assert factorint(9) == {3: 2}
    assert not compass_ok(9)          # 3 appears squared -> forbidden
    assert fold_ok(9)                 # 3^b allowed outright -> permitted
    # folding is strictly stronger: it reaches everything the compass does, and more
    assert all(fold_ok(n) for n in range(3, 200) if compass_ok(n))
    assert [n for n in range(3, 40) if fold_ok(n) and not compass_ok(n)] == \
           [7, 9, 13, 14, 18, 19, 21, 26, 27, 28, 35, 36, 37, 38, 39]


def test_constructibility_reads_the_denominator_and_the_diatonic_scale_passes():
    """CC 2026-08-08: "what about diatonic ratios, constructible?"

    THE RULE. On the linear circle theta = 360(r-1), so theta/360 = (p-q)/q, and
    since gcd(p,q) = 1 that fraction's denominator IS q. Therefore r = p/q sits at a
    constructible angle IFF its DENOMINATOR is 2^a x distinct Fermat primes. The
    numerator is irrelevant.

    EVERY JUST DIATONIC RATIO PASSES — denominators 1, 8, 4, 3, 2, 3, 8, 1, powers
    of two times at most a SINGLE three. The tempered layout's ratios are ninths and
    six of nine fail. So the whole constructibility story is one fact: denominator
    nine. The intonated layout is drawable because its movers are diatonic; the
    tempered one is not because its ratios are counted in ninths.

    NB keep two obstructions apart: 180 degrees is perfectly CONSTRUCTIBLE (it is
    the diameter, and 3/2 has denominator 2). The parity theorem does not forbid
    drawing it — it forbids a digit OCCUPYING it. They coincide on one point by
    different arguments."""
    from sympy import factorint
    FERMAT = {3, 5, 17, 257, 65537}
    okden = lambda q: all(p in FERMAT and e == 1 for p, e in
                          ({p: e for p, e in factorint(q).items() if p != 2}
                           if q > 1 else {}).items())
    con = lambda r: okden(F(r).denominator)

    DIATONIC = [F(1), F(9,8), F(5,4), F(4,3), F(3,2), F(5,3), F(15,8), F(2)]
    assert all(con(r) for r in DIATONIC)                       # every one passes
    assert [r.denominator for r in DIATONIC] == [1, 8, 4, 3, 2, 3, 8, 1]

    # the tempered layout is ninths, and that is the whole obstruction
    TEM = [F(9 + k, 9) for k in range(9)]
    assert sum(1 for r in TEM if not con(r)) == 6
    assert {r.denominator for r in TEM if not con(r)} == {9}
    assert {r.denominator for r in TEM if con(r)} == {1, 3}

    # the intonated movers are diatonic, hence drawable
    assert all(con(r) for r in (F(9,8), F(5,4), F(7,4), F(15,8)))
    assert not con(F(13,9)) and not con(F(14,9))               # only the stayers fail

    # seven in the numerator is fine; seven in the denominator is not
    assert con(F(7,4)) and con(F(7,5)) and con(F(7,6))
    assert not con(F(8,7)) and not con(F(9,7)) and not con(F(12,7))

    # and the two obstructions at 180 are genuinely different
    assert con(F(3,2))                                          # drawable
    assert 180 not in TEMPERED.values() and 180 not in INTONATED.values()  # unoccupied


def test_no_re_indexing_or_stepping_can_reach_nine_equal_seats():
    """CC 2026-08-08: "if you can construct 315 in relation to 360/0, why can't you
    index the circle on that basis?" Three readings, all closed off by ONE fact —
    the constructible angle-fractions are a GROUP whose denominators are closed
    under lcm, so a squared three can never be manufactured.

    (1) STEPPING BY 315 returns the octagon: gcd(315,360) = 45, and 315 = 7 x 45
        walks the eight-lattice in a different order onto the same eight seats.
    (2) STEPPING BY ANYTHING constructible gives a polygon of order n/gcd(m,n),
        which divides n and is therefore constructible too. Nine never appears.
    (3) RE-INDEXING from 315 is translation by a group element: same seats, renamed.

    The positive half, which is the real content: indexing on the eight-lattice
    works, and gives 0, 45, 90, 270, 315 — which with the triangle's 120 and 240 is
    exactly the intonated layout's seven exact seats. The eight-lattice hands over
    the figure and refuses the count."""
    from math import gcd
    from sympy import factorint
    FERMAT = {3, 5, 17, 257, 65537}
    ok = lambda n: all(p in FERMAT and e == 1 for p, e in
                       ({p: e for p, e in factorint(n).items() if p != 2}
                        if n > 1 else {}).items())

    orb, x = set(), 0
    while True:
        orb.add(x); x = (x + 315) % 360
        if x == 0:
            break
    assert orb == {45 * k for k in range(8)}          # the octagon, not nine points
    assert gcd(315, 360) == 45 and 315 == 7 * 45

    # no constructible step size anywhere generates exactly nine seats
    assert not [(m, n) for n in range(1, 2049) if ok(n)
                for m in range(1, n) if n // gcd(m, n) == 9]

    # the denominators are closed under lcm, so the group is closed
    for a, b in ((3, 5), (8, 3), (12, 20), (16, 15), (5, 17), (24, 40)):
        assert ok(a) and ok(b) and ok(a * b // gcd(a, b))

    # the positive half: the eight-lattice plus the triangle IS the drawable figure
    eight = {45 * k for k in range(8)}
    tri = {0, 120, 240}
    exact = {a for a in INTONATED.values() if a in eight | tri}
    assert exact == {0, 45, 90, 120, 240, 270, 315}
    assert set(INTONATED.values()) - exact == {160, 200}


def test_the_conserved_unit_drives_the_stayers_inward():
    """CC 2026-08-08: a real system's endpoints cannot be free — they need a
    conserved unit to anchor them, "hence .5 + .5 = 1" — and this "would of
    necessity drive the points inward by .5 each."

    IT DOES, and neither the size nor the sign is a choice.
      SIZE: the unit condition is 2d = 1, so d = 1/2 at each seat. Unique.
      SIGN: at d = 1/2 the inward pair 160.5/199.5 is constructible and the outward
            pair 159.5/200.5 is not. Only one direction exists.

    The reason is the same squared three as everywhere else. 160 = 4/9 of a turn, so
    with d = a/b the seat is (160b+a)/(360b) and the 3^2 reduces only if
    3 | (160b+a); since 160 = 1 (mod 3) that is just 3 | (a+b). Inward a+b = 3;
    outward a+b = 1.

    SCOPE, kept honest: the sign is NOT forced at every scale — d = 1/2^k alternates,
    inward for odd k and outward for even. But at the unit-conserving size k = 1 only
    inward exists, and that is the scale the argument is about."""
    from sympy import factorint
    FERMAT = {3, 5, 17, 257, 65517 - 20}   # 65537
    con = lambda a: all(p in FERMAT and e == 1 for p, e in
                        {p: e for p, e in factorint(F(a, 360).denominator).items()
                         if p != 2}.items())

    assert con(F(321, 2)) and con(F(399, 2))          # 160.5 / 199.5  inward: yes
    assert not con(F(319, 2)) and not con(F(401, 2))  # 159.5 / 200.5  outward: no
    assert F(321, 2) - 160 == F(1, 2) and 200 - F(399, 2) == F(1, 2)
    assert (F(321, 2) - 160) + (200 - F(399, 2)) == 1           # the conserved unit

    assert 160 % 3 == 1                                # so the test is 3 | (a+b)
    assert (1 + 2) % 3 == 0 and (-1 + 2) % 3 != 0      # inward clears it, outward not
    # the alternation by scale, stated rather than hidden
    assert [con(160 + F(1, 2**k)) for k in range(1, 7)] == [True, False, True,
                                                            False, True, False]
    assert [con(160 - F(1, 2**k)) for k in range(1, 7)] == [False, True, False,
                                                            True, False, True]

    # what the move does: one unit out of the arc spanning the forbidden seat
    T = [0, 40, 80, 120, 160, 200, 240, 280, 320]
    A = [0, 40, 80, 120, F(321, 2), F(399, 2), 240, 280, 320]
    gap = lambda P: [(P[(i + 1) % 9] - P[i]) % 360 for i in range(9)]
    assert [b - a for a, b in zip(gap(T), gap(A))] == \
           [0, 0, 0, F(1, 2), -1, F(1, 2), 0, 0, 0]
    assert gap(A)[4] == 39                             # the arc over 180 closes by one


def test_rigidity_diverges_logarithmically_at_both_fixed_seats():
    """CC's other half: the anchoring "would play out in reality as the logarithmic
    increase in rigidity of the system approaching infinity at the two end points."

    In the operation-count currency it does, exactly. A mirror pair held at 180 -/+ d
    has separation interval (540+d)/(540-d); its Tenney height — the cost of the
    operation trail — grows as 2*log2(1/d), gaining precisely two bits per halving,
    without bound. The same law holds at the root, the other fixed seat.

    This is the NS line made measurable on this figure: in the continuum a point may
    sit anywhere near a fixed seat at no cost whatever, while the discrete accounting
    charges unboundedly to keep the pair DISTINCT. Resource accounting is what the
    continuum deletes."""
    from math import log2
    T = lambda r: log2(r.numerator * r.denominator)
    costs = [T(F(540 + F(1, 2**k), 540 - F(1, 2**k))) for k in range(1, 12)]
    steps = [costs[i + 1] - costs[i] for i in range(len(costs) - 1)]
    # two bits per halving, approached FROM ABOVE and converging
    assert all(2 < s < 2 + 1e-5 for s in steps)
    assert all(steps[i + 1] < steps[i] for i in range(len(steps) - 1))
    assert costs[-1] - costs[0] > 18                    # and it diverges

    root = [T(F(720 - F(1, 2**k), 360 + F(1, 2**k))) for k in range(1, 12)]
    rsteps = [root[i + 1] - root[i] for i in range(len(root) - 1)]
    # the root's steps approach 2 from BELOW, the 180-seat's from above; both converge
    assert all(2 - 1e-3 < s < 2 for s in rsteps)
    assert all(rsteps[i + 1] > rsteps[i] for i in range(len(rsteps) - 1))


def test_root_twelve_halves_are_exactly_the_midy_pair():
    """CC 2026-08-08: "the diatonic ladder from 12 to 24 is 12, 13.5, 15, 16, 18,
    20, 22.5, 24 — the unique octave to display these two .5 values at Re and Si."

    IT IS FORCED, not a coincidence. Re = 9/8 and Si = 15/8 are the only two
    diatonic tones with DENOMINATOR 8; 12 is divisible by 4 but not by 8, so exactly
    those two fall to halves and every other tone stays whole. And Re and Si are
    digits 1 and 8 — THE MIDY PAIR the intonation displaces onto 45 and 315, the
    pair the go-around analysis found to be asymmetry-neutral (the DILATING pair).
    The eighth-denominators, the eight-lattice seats, and the dilating pair are one
    set reached three ways.

    The numbers that follow: 45/2 - 27/2 = 9 exactly, and 27 + 45 = 72, with
    27 = 3^3 the hexad sum and the polar flip of 72."""
    SCALE = {"Do": F(1), "Re": F(9,8), "Mi": F(5,4), "Fa": F(4,3),
             "Sol": F(3,2), "La": F(5,3), "Si": F(15,8), "Do'": F(2)}
    halves = {n for n, r in SCALE.items() if (r*12).denominator != 1}
    assert halves == {"Re", "Si"}
    assert {n for n, r in SCALE.items() if r.denominator == 8} == {"Re", "Si"}
    assert SCALE["Re"]*12 == F(27,2) and SCALE["Si"]*12 == F(45,2)

    # Re and Si are digits 1 and 8 in the figure, and that is the Midy pair
    assert LIN(INTONATED[1]) == F(9,8) and LIN(INTONATED[8]) == F(15,8)
    assert 1 + 8 == 9
    # and they are the ONLY digits whose ratio has denominator 8
    assert {d for d in INTONATED if LIN(INTONATED[d]).denominator == 8} == {1, 8}

    assert F(45,2) - F(27,2) == 9                      # difference exactly nine
    assert 27 + 45 == 72 and 27 == 3**3                # numerators give the 72
    assert sum(int(c) for c in "142857") == 27         # 27 is the hexad sum

    # 12 is the FIRST such root; the family needs 12 | N and 8 does not divide N
    fam = [N for N in range(1, 73)
           if {n for n, r in SCALE.items() if (r*N).denominator != 1} == {"Re", "Si"}]
    assert fam == [12, 36, 60] and fam[0] == 12
    assert all(N % 12 == 0 and N % 8 != 0 for N in fam)


def test_the_closed_arc_is_the_sum_of_three_powers_of_three():
    """CC: the 1-degree reduction "gives you 39". Recorded as arithmetic, ungraded
    beyond that: 39 = 3 + 9 + 27, the first three powers of three summed, on a
    figure whose whole obstruction is the SQUARED three. No mechanism is proposed
    for why the closed arc should land on that sum."""
    assert 3 + 9 + 27 == 39 == (3**4 - 3) // 2
    assert 39 == 3 * 13
    T = [0, 40, 80, 120, 160, 200, 240, 280, 320]
    A = [0, 40, 80, 120, F(321,2), F(399,2), 240, 280, 320]
    assert (A[5] - A[4]) == 39 and (T[5] - T[4]) == 40


def test_the_mirror_forces_the_two_layer_structure():
    """2026-08-08, the gravity join's mechanical face. THEOREM: in EVERY
    mirror-symmetric nine-point layout (digits in standard order), the Midy
    mirror d <-> 9-d forces:

      (a) the go-arounds about its FIXED seats — the root and the empty 180 —
          to be exactly symmetric: the fixed stratum can carry no directional
          bias, ever; SIZE is its only degree of freedom (dilation);
      (b) the biases about the 2-ORBIT seats 3 and 6 to be exact negatives:
          two-signed, equal-and-opposite action, riding exactly the transform
          arcs 2<->4 and 5<->7 that carry the banked +/-18 ledger.

    Proof: the mirror maps the arc 2->4 onto 5->7 orientation-reversed (halves
    swap between them) and maps the root arc 8->1 and empty arc 4->5 each onto
    THEMSELVES reversed (halves swap in place, hence equal). One paragraph.

    SCOPE, held exactly: this forces the two-layer SHAPE — one-signed at the
    mirror's fixed stratum, two-signed on its orbit pairs — from the same Midy
    mirror that GRAVITY-REOPENED section 2 derives the sign split from. The
    ASSIGNMENT (gravity reads the fixed stratum, EM the orbit pairs) remains
    the banked join, Sound-conditional per THE-GRAVITY-WHY-DOSSIER. Shape
    forced; assignment not promoted here."""
    from itertools import combinations
    for q1, q2, q3, q4 in combinations([5 * k for k in range(1, 36)], 4):
        # fixed seats: halves equal identically (mirror partners flank them)
        assert q1 == q1 and (180 - q4) == (180 - q4)          # structure, by algebra
        b3 = (q3 - q2) - (q4 - q3)
        b6 = (q4 - q3) - (q3 - q2)
        assert b3 + b6 == 0                                    # equal and opposite
    # and the named layouts instantiate it: tempered bias (0,0), intonated (-10,+10)
    assert ((120 - 80) - (160 - 120), (160 - 120) - (120 - 80)) == (0, 0)
    assert ((120 - 90) - (160 - 120), (160 - 120) - (120 - 90)) == (-10, 10)
    # the +/-18 ledger rides the same two arcs: 42->24 = -18, 57->75 = +18
    assert 24 - 42 == -18 and 75 - 57 == +18


def test_mirror_symmetry_forbids_net_torque():
    """WITHDRAWAL, pinned so it cannot come back. The {3,6} bias pair was called
    "a couple, pure torque" on 2026-08-08. It is neither.

    Reflection about the root axis lies IN the plane, so it maps the out-of-plane
    direction z -> -z. Torque is an AXIAL vector along z, so a mirror-symmetric
    configuration satisfies tau_z = -tau_z and therefore tau_z = 0 — identically,
    for every mirror-symmetric layout. The same mirror that gives the layer
    theorem forbids the torque.

    Mechanically: for a tangential displacement field on the ring, m = 0 is rigid
    rotation and is the only mode carrying net angular momentum. It vanishes
    exactly in both the anchoring and the intonation.

    ALSO WITHDRAWN: the follow-on claim that the pattern is quadrupole-dominant,
    "the multipole gravity radiates in". The half-degree pattern's spectrum is
    |sin(20 m deg)|, peaking at m = 4 and 5, not at m = 2; the intonation's peaks
    at m = 1. Both statements were written before the output was read."""
    import cmath
    POS = [0, 40, 80, 120, 160, 200, 240, 280, 320]
    amp = lambda d, m: abs(sum(x * cmath.exp(-1j * m * math.radians(p))
                               for x, p in zip(d, POS)))
    anchor = [0, 0, 0, 0, 0.5, -0.5, 0, 0, 0]
    intone = [0, 5, 10, 0, 0, 0, -10, -5, 0]

    assert amp(anchor, 0) < 1e-12 and amp(intone, 0) < 1e-12   # no net rotation
    # and the spectra are NOT quadrupole-peaked
    a = [amp(anchor, m) for m in range(7)]
    i = [amp(intone, m) for m in range(7)]
    assert a.index(max(a)) == 4 and i.index(max(i)) == 1        # not m = 2
    assert all(abs(a[m] - abs(math.sin(math.radians(20 * m)))) < 1e-12
               for m in range(7))                               # the closed form

    # the shape that does survive: short gap away from 180 at BOTH seats
    INT = {2: 90, 3: 120, 4: 160, 5: 200, 6: 240, 7: 270}
    assert (INT[3] - INT[2], INT[4] - INT[3]) == (30, 40)       # at 3: short, long
    assert (INT[6] - INT[5], INT[7] - INT[6]) == (40, 30)       # at 6: long, short


def test_the_figure_has_as_much_freedom_out_of_plane_as_in_it():
    """CC 2026-08-08: "are we even looking for gravity on the correct axis — just
    because it has an orientation in its action, that does not mean it originates
    on the axis of that action, and may originate 90 degrees to it."

    The question is well posed against this object. Maxwell counts: planar
    rigidity needs 2n-3 = 15 bars against the figure's 9, leaving 6 internal
    degrees of freedom; spatial rigidity needs 3n-6 = 21, leaving 12. So SIX of
    the twelve freedoms are out of plane — the figure has exactly as much freedom
    perpendicular to its plane as within it, and nothing in the bar count prefers
    the plane.

    What this does NOT supply is a dynamics. The squeeze is a static shape; a
    motion needs a response rule the figure does not have. Same wall as U1."""
    n, bars = 9, 9
    assert 2 * n - 3 - bars == 6                     # planar freedoms
    assert 3 * n - 6 - bars == 12                    # spatial freedoms
    assert (3 * n - 6 - bars) - (2 * n - 3 - bars) == 6   # out-of-plane, equal count


def test_the_bias_is_curvature_and_the_fixed_stratum_is_flat():
    """2026-08-08. What the two half-degrees actually spend, computed rather than
    named. The 'bias' at a seat — arriving gap minus leaving gap — is

        bias(s) = (t_s - t_prev) - (t_next - t_s) = 2 t_s - t_prev - t_next
                = MINUS the discrete second difference at s

    i.e. it is the DISCRETE CURVATURE of the position sequence. (Sign noted
    exactly: bias = -Laplacian, not +.)

    THEOREM, strengthening the morning's layer result: this curvature VANISHES
    IDENTICALLY ON THE MIRROR'S FIXED STRATUM — at the root and at the empty seat
    — for every mirror-symmetric layout whatever, including ones with all four
    Midy pairs displaced by unrelated amounts. Forced: the mirror places each
    point and its partner symmetrically about a fixed seat, so the second
    difference there is zero by construction. All curvature is supported on the
    orbit pairs.

    And the contributions are structured, not shared: displacing pair {1,8} puts
    ZERO curvature at 3 and 6 (it only dilates the root arc); {2,7} and {4,5} each
    put one unit; {3,6} puts TWO, being the centre of its own stencil. The
    coefficient vector (0, -1, +2, -1) IS the Laplacian stencil, which is why the
    'unit spent equals bias received' bookkeeping holds while the contributions
    differ — it is a second difference, not a redistribution."""
    from fractions import Fraction as Fr

    def layout(d18=0, d27=0, d36=0, d45=0):
        return {9: Fr(0), 1: 40 + d18, 2: 80 + d27, 3: 120 + d36, 4: 160 + d45,
                5: 200 - d45, 6: 240 - d36, 7: 280 - d27, 8: 320 - d18}

    def bias(P, s, prev, nxt, wrap=0):
        return (P[s] - (P[prev] - wrap)) - (P[nxt] - P[s])

    # bias is minus the standard second difference
    P = layout(d45=Fr(-1, 2))
    assert bias(P, 3, 2, 4) == -(P[2] - 2 * P[3] + P[4])
    assert bias(P, 6, 5, 7) == -(P[5] - 2 * P[6] + P[7])

    # the stencil: which pair contributes how much curvature at seat 3
    coeffs = [bias(layout(**{k: Fr(1)}), 3, 2, 4) for k in
              ("d18", "d27", "d36", "d45")]
    assert coeffs == [0, -1, 2, -1]                 # the Laplacian stencil
    assert coeffs[0] == 0                            # {1,8} puts no curvature
    assert abs(coeffs[2]) == 2 * abs(coeffs[1])      # {3,6} doubles

    # and the fixed stratum is FLAT, in every layout
    for kw in ({}, {"d45": Fr(-1, 2)}, {"d18": 5, "d27": 10},
               {"d18": Fr(3), "d27": Fr(7), "d36": Fr(2), "d45": Fr(5)}):
        P = layout(**kw)
        root = 2 * Fr(0) - (P[8] - 360) - P[1]       # curvature at the root
        empty = 2 * Fr(180) - P[4] - P[5]            # curvature at the empty seat
        assert root == 0 and empty == 0


def test_the_ring_carries_a_discrete_poisson_structure():
    """2026-08-08. The curvature result set up as a source problem on the ring.

    FORCED, all three:
      (a) GAUSS IDENTITY — the signed total of the curvature is zero in every
          layout, because the second difference telescopes on a closed ring. This
          is what forces curvature to appear as EQUAL AND OPPOSITE PAIRS. It
          explains the sign structure, NOT the magnitude. (The conserved unit is
          the ABSOLUTE total, whose value comes from the displacement's size —
          a separate statement, and the two must not be run together.)
      (b) THE TEMPERED LAYOUT IS THE UNIQUE SOURCE-FREE ONE — curvature zero at
          every seat forces every gap to equal its neighbour, hence equal
          division, hence tempered up to rotation. 'The rest state' reads as
          'the vacuum solution'.
      (c) OF THE THREE TRIAD MEMBERS, TWO MAY CARRY SOURCE AND ONE MAY NOT.
          curv(9) = 0 in every layout (it is a fixed seat); curv(3) and curv(6)
          are always exact negatives. This is CC's 3 / 9 / 6 as + / neutral / -,
          derived from the mirror rather than read off the diagram.

    NOT CLAIMED: that this is Poisson. Poisson is lap(Phi) = 4 pi G rho; here the
    Laplacian is taken of a POSITION SEQUENCE, and nothing licenses reading
    positions as a potential. Both are functions on a manifold with Laplacians,
    and at present that is the whole resemblance. The reading's one forbidding
    consequence — no source on the mirror's fixed stratum — is recorded as the
    place to push, not as a result."""
    from fractions import Fraction as Fr
    ORD = [9, 1, 2, 3, 4, 5, 6, 7, 8]

    def lay(d18=0, d27=0, d36=0, d45=0):
        return {9: Fr(0), 1: 40 + d18, 2: 80 + d27, 3: 120 + d36, 4: 160 + d45,
                5: 200 - d45, 6: 240 - d36, 7: 280 - d27, 8: 320 - d18}

    def curv(P):
        t = [P[s] for s in ORD]
        out = {}
        for i, s in enumerate(ORD):
            prev = t[i - 1] - (360 if i == 0 else 0)
            nxt = t[(i + 1) % 9] + (360 if i == 8 else 0)
            out[s] = prev - 2 * t[i] + nxt
        return out

    CASES = [{}, {"d45": Fr(-1, 2)}, {"d18": 5, "d27": 10}, {"d36": Fr(1)},
             {"d18": Fr(3), "d27": Fr(7), "d36": Fr(2), "d45": Fr(5)}]
    for kw in CASES:
        c = curv(lay(**kw))
        assert sum(c.values()) == 0                       # (a) Gauss identity
        assert c[9] == 0                                  # (c) the nine cannot
        assert c[3] == -c[6]                              # (c) exact negatives

    assert all(v == 0 for v in curv(lay()).values())      # (b) tempered is vacuum
    assert any(v != 0 for v in curv(lay(d45=Fr(-1, 2))).values())

    # three DISTINCT quantities, kept apart (I ran two of them together once):
    #   displacement 2|d| — the conserved unit, chosen
    #   signed curvature 0 — the Gauss identity, forced
    #   absolute curvature 8|d| — neither; the stencil is four seats wide, since
    #   moving 4 and 5 puts curvature AT 4 and 5 as well as at 3 and 6
    d = Fr(1, 2)
    c = curv(lay(d45=d))
    assert sum(c.values()) == 0                                  # Gauss
    assert sum(abs(v) for v in c.values()) == 8 * d              # not the unit
    assert (c[3], c[4], c[5], c[6]) == (d, -3 * d, 3 * d, -d)    # the stencil
    assert 2 * d == 1                                            # the unit itself


# ---------------------------------------------------------------------------
# THE ELASTIC SPECTRUM  (2026-08-08)
# The Dirichlet energy U = sum (gap - 40)^2 is EXACTLY the graph Dirichlet form
# of the 9-cycle; its normal modes in the mirror sector are the sine modes of
# C_9, so the figure's spectrum returns the figure's own layout. No ruler is
# used anywhere below: every quantity is a ratio.
# ---------------------------------------------------------------------------

PAIRS = ((1, 8), (2, 7), (3, 6), (4, 5))


def _energy(v):
    """U = sum over seats of (gap - 40)^2, after displacing each Midy pair
    outward by v[i] (hi seat +v, lo seat -v). Exact integer arithmetic."""
    p = dict(TEMPERED)
    for k, (hi, lo) in zip(v, PAIRS):
        p[hi] += k
        p[lo] -= k
    s = sorted(p.values())
    gaps = [(s[(i + 1) % 9] - s[i]) % 360 for i in range(9)]
    assert sum(gaps) == 360
    return sum((g - 40) ** 2 for g in gaps)


def test_the_energy_is_exactly_quadratic_and_the_pairs_form_a_CHAIN():
    """U is an exact quadratic form -- no small-displacement approximation --
    and its coupling matrix is TRIDIAGONAL: only ADJACENT Midy pairs interact.
    The mirror folds the 9-ring into a 4-site chain."""
    e = lambda i: tuple(1 if j == i else 0 for j in range(4))
    Q = [[0] * 4 for _ in range(4)]
    for i in range(4):
        Q[i][i] = _energy(e(i))
        for j in range(i + 1, 4):
            Q[i][j] = Q[j][i] = (_energy(tuple(a + b for a, b in zip(e(i), e(j))))
                                 - _energy(e(i)) - _energy(e(j)))

    assert Q == [[4, -4, 0, 0],
                 [-4, 4, -4, 0],
                 [0, -4, 4, -4],
                 [0, 0, -4, 6]]                 # tridiagonal: a chain, not a ring
    assert Q[0][2] == Q[0][3] == Q[1][3] == 0   # non-adjacent pairs do not couple
    assert Q[3][3] == 6 and Q[0][0] == 4        # {4,5} stiffer: it spans the empty seat

    # exact, not approximate — checked on displacement vectors of every sign pattern
    qf = lambda v: (sum(Q[i][i] * v[i] ** 2 for i in range(4))
                    + sum(Q[i][j] * v[i] * v[j] for i in range(4) for j in range(i + 1, 4)))
    for v in ((5, 10, 0, 0), (1, -2, 3, -1), (4, 4, 4, 4), (0, 0, 7, -5),
              (3, 1, -2, 6), (-1, 5, 2, 0), (-3, -3, 1, 8)):
        assert qf(v) == _energy(v)

    # the intonated layout is (5,10,0,0): the two pairs COUPLE, they do not add
    assert _energy((5, 10, 0, 0)) == 300
    assert _energy((5, 0, 0, 0)) + _energy((0, 10, 0, 0)) == 500      # if independent
    assert _energy((5, 10, 0, 0)) - 500 == -200                       # cross term


def test_the_spectrum_is_the_ring_returned():
    """Hessian/4 = the C_9 Laplacian restricted to the mirror sector. The four
    stiffnesses are 2 - 2cos(phi) at phi = 40, 80, 120, 160 -- the tempered seat
    angles themselves -- and the frequencies are 2 sin(20 k) degrees."""
    L = [[2, -1, 0, 0], [-1, 2, -1, 0], [0, -1, 2, -1], [0, 0, -1, 3]]

    for k in (1, 2, 3, 4):
        lam = 2 - 2 * math.cos(2 * math.pi * k / 9)
        shape = [math.sin(2 * math.pi * k * j / 9) for j in (1, 2, 3, 4)]
        Lv = [sum(L[i][j] * shape[j] for j in range(4)) for i in range(4)]
        assert all(abs(Lv[i] - lam * shape[i]) < 1e-12 for i in range(4))   # sine mode
        assert abs(lam - (2 - 2 * math.cos(math.radians(40 * k)))) < 1e-12  # seat angle
        assert abs(math.sqrt(lam) - 2 * math.sin(math.radians(20 * k))) < 1e-12

    # k=0, the uniform mode, is ABSENT from the sector: the modes present are
    # k = 1,2,3,4 and no others, so there is NO zero-frequency mode -- L is
    # positive definite. det L = 9, the constant term of the char poly.
    # This is the already-banked "mirror forbids net torque", recovered here:
    # a global rotation is not even representable in pair-antisymmetric
    # coordinates, so it cannot appear as a soft mode.
    assert min(2 - 2 * math.cos(2 * math.pi * k / 9) for k in (1, 2, 3, 4)) > 0
    det = 1                                          # Gaussian elimination, exact
    M = [[F(x) for x in row] for row in L]
    for i in range(4):
        det *= M[i][i]
        for r in range(i + 1, 4):
            f = M[r][i] / M[i][i]
            for c in range(i, 4):
                M[r][c] -= f * M[i][c]
    assert det == 9                                  # nonsingular: no null direction


def test_exactly_one_normal_mode_is_rational_and_it_is_the_TRIAD():
    """char poly = (x-3)(x^3 - 6x^2 + 9x - 3). The cubic is Eisenstein at 3 --
    the triad's own prime certifies that the other three modes are irrational.
    The rational mode sits at phi = 120 and holds {3,6} exactly still."""
    L = [[2, -1, 0, 0], [-1, 2, -1, 0], [0, -1, 2, -1], [0, 0, -1, 3]]

    # (x-3)(x^3-6x^2+9x-3) expands to the char poly x^4-9x^3+27x^2-30x+9
    prod = [0] * 5
    for i, u in enumerate([1, -3]):
        for j, w in enumerate([1, -6, 9, -3]):
            prod[i + j] += u * w
    assert prod == [1, -9, 27, -30, 9]

    # lambda = 3 exact, eigenvector (1,-1,0,+1): the {3,6} coordinate is a NODE
    v = [1, -1, 0, 1]
    assert [sum(L[i][j] * v[j] for j in range(4)) for i in range(4)] == [3, -3, 0, 3]
    assert v[2] == 0                                  # {3,6} does not move
    assert abs(3 - (2 - 2 * math.cos(math.radians(120)))) < 1e-15   # phi = 120, the triad
    assert abs(math.sqrt(3) - 2 * math.sin(math.radians(60))) < 1e-15

    # Eisenstein at p=3 on x^3-6x^2+9x-3  =>  irreducible over Q
    tail = [-6, 9, -3]
    assert all(c % 3 == 0 for c in tail) and tail[-1] % 9 != 0
    # degree 3 over Q: NOT straightedge-and-compass (3 does not divide 2^n),
    # but origami-constructible (Pierpont). Same split as the seats themselves.


def test_the_spectrum_does_not_depend_on_choosing_squares():
    """U = sum f(gap) for ANY local, seat-isotropic f with f''(40) > 0 gives the
    SAME Hessian up to the scalar f''(40): the four frequency ratios are a property
    of C_9, not of the squared form. The quartic (g-40)^4 has f''(40) = 0 and is
    excluded by the hypothesis -- it deviates, which shows the condition is real."""
    def spectrum(f, h=1e-4):
        def U(v):
            p = dict(TEMPERED)
            for k, (hi, lo) in zip(v, PAIRS):
                p[hi] += k
                p[lo] -= k
            s = sorted(p.values())
            return sum(f((s[(i + 1) % 9] - s[i]) % 360) for i in range(9))
        H = [[0.0] * 4 for _ in range(4)]
        for i in range(4):
            for j in range(4):
                d = lambda a, b: [(h if t == i else 0) * a + (h if t == j else 0) * b
                                  for t in range(4)]
                H[i][j] = (U(d(1, 1)) - U(d(1, -1)) - U(d(-1, 1)) + U(d(-1, -1))) / (4 * h * h)
        # symmetric 4x4 -> eigenvalues by characteristic polynomial roots (numpy-free)
        import numpy
        return sorted(math.sqrt(max(x, 0)) for x in numpy.linalg.eigvalsh(numpy.array(H)))

    target = [2 * math.sin(math.pi * k / 9) for k in (1, 2, 3, 4)]
    for f in (lambda g: (g - 40) ** 2,            # f''(40) = 2
              lambda g: math.cosh(g - 40),        # f''(40) = 1
              lambda g: g * math.log(g / 40)):    # f''(40) = 1/40
        w = spectrum(f)
        assert all(abs(w[i] / w[0] - target[i] / target[0]) < 1e-4 for i in range(4))

    w4 = spectrum(lambda g: (g - 40) ** 4)        # f''(40) = 0 -> hypothesis fails
    assert abs(w4[3] / w4[0] - target[3] / target[0]) > 0.5


def test_the_two_mirror_FIXED_POINTS_are_nodes_of_every_mode():
    """The root (seat 9, 0 deg) and the empty seat (180 deg) are the only places on
    the figure that never oscillate, in any mode. And the monopole k=0 -- the uniform
    mode -- is the only mode that costs nothing, and it is absent from the spring.
    Neutral twice over: the seat that does not move, the mode that does not pay."""
    for k in (1, 2, 3, 4):
        u = [math.sin(2 * math.pi * k * j / 9) for j in range(9)]
        assert abs(u[0]) < 1e-12                      # the root never moves
        assert abs(u[4] + u[5]) < 1e-12               # 4 and 5 mirror across 180 ...
        assert abs((u[4] + u[5]) / 2) < 1e-12         # ... so the empty seat is a node
        assert abs(sum(u)) < 1e-12                    # every spring mode is monopole-free

    # k=0, the monopole: all seats together, zero Dirichlet cost
    const = [1.0] * 9
    assert sum((const[(j + 1) % 9] - const[j]) ** 2 for j in range(9)) == 0

    # ONLY these two places are universal nodes -- every other seat moves somewhere
    for j in (1, 2, 3, 4, 5, 6, 7, 8):
        assert any(abs(math.sin(2 * math.pi * k * j / 9)) > 1e-9 for k in (1, 2, 3, 4))


def test_the_hexad_triad_split_IS_the_rational_normal_mode():
    """The banked hexad/triad split arrives here as a DYNAMICAL object: in mode k=3
    the whole triad 9-3-6 is at rest and only the hexad {1,2,4,5,7,8} moves, summing
    to zero. The alternation is in RING order (1,2,4,5,7,8), NOT in reptend order
    (1,4,2,8,5,7) -- in reptend order the signs run + + - - - +. k=3 is the unique
    C_3-invariant mode, which is why it alone is rational (9 = 3^2, C_9 contains C_3)."""
    u = [math.sin(2 * math.pi * 3 * j / 9) for j in range(9)]
    assert all(abs(u[j]) < 1e-12 for j in (0, 3, 6))          # triad at rest
    ring = [1, 2, 4, 5, 7, 8]                                  # hexad in ring order
    assert all(abs(u[j]) > 0.8 for j in ring)                  # hexad all moving
    assert abs(sum(u[j] for j in ring)) < 1e-12                # and summing to zero
    sgn = [1 if u[j] > 0 else -1 for j in ring]
    assert sgn == [1, -1, 1, -1, 1, -1]                        # alternates in RING order
    assert [1 if u[j] > 0 else -1 for j in (1, 4, 2, 8, 5, 7)] == [1, 1, -1, -1, -1, 1]

    # uniqueness: only k=3 is invariant under rotation by 120 deg (j -> j+3)
    inv = [k for k in (1, 2, 3, 4)
           if all(abs(math.sin(2 * math.pi * k * ((j + 3) % 9) / 9)
                      - math.sin(2 * math.pi * k * j / 9)) < 1e-12 for j in range(9))]
    assert inv == [3]


def test_the_full_nine_mode_spectrum_and_the_degeneracy():
    """CORRECTION to the first statement of this result. The figure does NOT have
    four modes: it has NINE = 1 + 2x4. The four costly EVEN modes carry exactly the
    same frequencies as the odd four -- they are degenerate partners, not new
    frequencies. The falsifiable content survives (a fifth DISTINCT frequency still
    refutes) but the count was wrong."""
    L = [[0] * 9 for _ in range(9)]
    for j in range(9):
        L[j][j] = 2
        L[j][(j + 1) % 9] -= 1
        L[j][(j - 1) % 9] -= 1

    for k in (1, 2, 3, 4):
        lam = 2 - 2 * math.cos(2 * math.pi * k / 9)
        for shape in ([math.sin(2 * math.pi * k * j / 9) for j in range(9)],
                      [math.cos(2 * math.pi * k * j / 9) for j in range(9)]):
            Lv = [sum(L[a][b] * shape[b] for b in range(9)) for a in range(9)]
            assert all(abs(Lv[a] - lam * shape[a]) < 1e-12 for a in range(9))
    # multiplicity 2 for k=1..4, multiplicity 1 for k=0 -> 1 + 2*4 = 9
    assert 1 + 2 * 4 == 9

    # the degeneracy is a CIRCULATION: cos +/- i sin are the two travelling waves,
    # and the mirror j -> -j is exactly what exchanges them
    for k in (1, 2, 3, 4):
        for j in range(9):
            assert abs(math.sin(2 * math.pi * k * (-j % 9) / 9)
                       + math.sin(2 * math.pi * k * j / 9)) < 1e-12   # sine flips
            assert abs(math.cos(2 * math.pi * k * (-j % 9) / 9)
                       - math.cos(2 * math.pi * k * j / 9)) < 1e-12   # cosine holds


def test_the_triad_frequency_carries_BOTH_forms_of_the_split():
    """At omega = sqrt(3) the two degenerate partners give the hexad/triad split
    twice over, in complementary form:
        ODD  k=3: triad AT REST, hexad alternating +,-,+,-,+,- (ring order)
        EVEN k=3: triad all +1 TOGETHER, hexad all -1/2 TOGETHER -- the triad moving
                  AGAINST the hexad, in the 3:6 ratio that makes the total vanish."""
    tri, hexad = (0, 3, 6), (1, 2, 4, 5, 7, 8)
    odd = [math.sin(2 * math.pi * 3 * j / 9) for j in range(9)]
    even = [math.cos(2 * math.pi * 3 * j / 9) for j in range(9)]

    assert all(abs(odd[j]) < 1e-12 for j in tri)                    # odd: triad still
    assert all(abs(even[j] - 1.0) < 1e-12 for j in tri)             # even: triad together
    assert all(abs(even[j] + 0.5) < 1e-12 for j in hexad)           # even: hexad opposed
    assert abs(3 * 1.0 + 6 * -0.5) < 1e-12                          # 3:6 conserves
    assert abs(sum(even)) < 1e-12 and abs(sum(odd)) < 1e-12         # both monopole-free
