"""The two faces of the first operation, each a closed orbit in its own modulus (8 October 2026, at CC's word: "yes chase
the handedness, what does it forbid").

Roped up: the corpus's handedness, the exchange (2 4)(5 7) of the two orderings of the hexad, is the Origin's FIRST
OPERATION (THE-ORIGIN-ON-DISCRETE-TERMS, Volume I, section 3): the free involution 142857 -> 124875 between the read face
(the order in which division writes the digits) and the circulation face (the doubling orbit), declared as the electric
and magnetic faces of the field. Its published prohibition is the magnetic monopole: "The circulation face is a closed
orbit: the doubling sequence cycles with no endpoints", hence no sources. The first rope-up on the handedness (gravity
record, Basic Scheme) missed the owning record; recorded in the journal.

Pinned here, all exact:
  * each face is the orbit of one multiplier in its own modulus: the circulation face is doubling modulo 9 on the
    digits; the read face is multiplication by ten modulo 7 on the remainders, carried to the digits by the monotone
    bijection r -> floor(10r/7);
  * stepped in the OTHER modulus, each face moves +2, -1, +2, +2, -1, +2 in logarithms, and the bijection itself, read in
    logarithms, is the first operation: the structure is symmetric under exchanging the moduli;
  * colour {1,4,7}|{2,5,8} is the alternation of the circulation face (the squares modulo 9); the octonion orientation
    {1,2,5}|{4,7,8} is the alternation of the read face (the quadratic residues modulo 7); rounding polarity and the
    fourth labelling are contiguous halves of both faces; so the first operation exchanges colour with orientation;
  * on the four interior digits the mirror (charge conjugation, board of 8 October), the perspective reversal x -> 1/x
    (CC's lead for a physical handedness) and the first operation are the three involutions of one Klein four-group;
    on the whole hexad the mirror is the swap of 1 and 8 times the other two. Only the perspective reversal leaves
    colour alone, as a parity must.

What this does not settle: "closed, no endpoints" holds of both faces in their own moduli, so the published asymmetry
that gives the read face its sources is that it is written (it has a first digit); that step, and the identification
of the faces with the electric and magnetic fields ("declared and not proved", Origin I, section 3), carry the
monopole prohibition.
"""

HEXAD = [1, 2, 4, 5, 7, 8]
BETA = {r: (10 * r) // 7 for r in range(1, 7)}                      # remainder -> the digit division writes
READ = [BETA[pow(10, k, 7)] for k in range(6)]                       # 1, 4, 2, 8, 5, 7
CIRC = [pow(2, k, 9) for k in range(6)]                              # 1, 2, 4, 8, 7, 5
FIRST = dict(zip(READ, CIRC))                                        # the first operation
LOG2 = {pow(2, k, 9): k for k in range(6)}
LOG3 = {pow(3, k, 7): k for k in range(6)}
UNBETA = {d: r for r, d in BETA.items()}

COLOUR, ORIENT, ROUNDING, FOURTH = {1, 4, 7}, {1, 2, 5}, {1, 2, 4}, {1, 5, 7}
split = lambda s: frozenset(s) if 1 in s else frozenset(set(HEXAD) - set(s))   # a labelling up to its sign


def test_each_face_is_the_orbit_of_one_multiplier_in_its_own_modulus():
    assert list(BETA.values()) == HEXAD                              # monotone: the hexad in ascending order
    assert READ == [1, 4, 2, 8, 5, 7] and CIRC == [1, 2, 4, 8, 7, 5]
    assert all((10 * UNBETA[READ[i]]) % 7 == UNBETA[READ[(i + 1) % 6]] for i in range(6))
    assert all((2 * CIRC[i]) % 9 == CIRC[(i + 1) % 6] for i in range(6))
    assert FIRST == {1: 1, 4: 2, 2: 4, 8: 8, 5: 7, 7: 5}


def test_each_face_steps_the_same_pattern_in_the_other_modulus():
    step = lambda a, b, m: next(x for x in range(1, m) if (a * x) % m == b)
    assert [step(READ[i], READ[(i + 1) % 6], 9) for i in range(6)] == [4, 5, 4, 4, 5, 4]
    circ_r = [UNBETA[d] for d in CIRC]
    assert [step(circ_r[i], circ_r[(i + 1) % 6], 7) for i in range(6)] == [2, 5, 2, 2, 5, 2]
    in_logs_9 = [(LOG2[READ[(i + 1) % 6]] - LOG2[READ[i]]) % 6 for i in range(6)]
    in_logs_7 = [(LOG3[circ_r[(i + 1) % 6]] - LOG3[circ_r[i]]) % 6 for i in range(6)]
    assert in_logs_9 == in_logs_7 == [2, 5, 2, 2, 5, 2]               # +2, -1, +2, +2, -1, +2


def test_the_bijection_read_in_logarithms_is_the_first_operation():
    swap = {0: 0, 1: 2, 2: 1, 3: 3, 4: 5, 5: 4}
    assert {LOG3[r]: LOG2[BETA[r]] for r in range(1, 7)} == swap
    assert {LOG2[d]: LOG2[FIRST[d]] for d in HEXAD} == swap


def test_colour_alternates_on_the_circulation_face_and_orientation_on_the_read_face():
    assert {(x * x) % 9 for x in HEXAD} == COLOUR == set(CIRC[0::2])
    assert {BETA[(x * x) % 7] for x in range(1, 7)} == ORIENT == set(READ[0::2])
    halves = lambda cyc: {split(set(cyc[i:i + 3] + cyc[:max(0, i + 3 - 6)])) for i in range(3)}
    assert halves(READ) == {split(ROUNDING), split(FOURTH), split(COLOUR)}
    assert halves(CIRC) == {split(ROUNDING), split(FOURTH), split(ORIENT)}
    assert [str(k * 142857) for k in (1, 2, 3)] == ["142857", "285714", "428571"]   # the Midy halves of 1/7, 2/7, 3/7
    image = lambda f, s: split({f[d] for d in s})
    assert image(FIRST, COLOUR) == split(ORIENT) and image(FIRST, ORIENT) == split(COLOUR)
    assert image(FIRST, ROUNDING) == split(ROUNDING) and image(FIRST, FOURTH) == split(FOURTH)


def test_mirror_perspective_reversal_and_first_operation_form_a_klein_group():
    mirror = {d: 9 - d for d in HEXAD}
    reverse = {d: pow(d, -1, 9) for d in HEXAD}                      # x -> 1/x: doubling read as halving
    after = lambda f, g: {d: f[g[d]] for d in HEXAD}
    assert after(reverse, FIRST) == after(FIRST, reverse) == {1: 1, 2: 7, 4: 5, 5: 4, 7: 2, 8: 8}
    assert all(after(reverse, FIRST)[d] == mirror[d] for d in (2, 4, 5, 7))
    swap_root_pair = {**{d: d for d in HEXAD}, 1: 8, 8: 1}
    assert after(swap_root_pair, after(reverse, FIRST)) == mirror
    assert {BETA[pow(r, -1, 7)] for r in range(1, 7)} == set(HEXAD)
    assert all(BETA[pow(r, -1, 7)] == reverse[BETA[r]] for r in range(1, 7))   # the same inversion in both moduli
    image = lambda f, s: split({f[d] for d in s})
    assert image(reverse, COLOUR) == split(COLOUR) and image(reverse, ORIENT) == split(ORIENT)
    assert image(reverse, ROUNDING) == split(FOURTH)
    assert all({mirror[d] for d in s} == set(HEXAD) - s for s in (COLOUR, ORIENT, ROUNDING, FOURTH))
