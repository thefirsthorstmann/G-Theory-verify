"""test_decimal_wheel.py — PART TWO OPENS: what a decimal place means, 2026-08-09.

the author's first swing: "a 9 means three rotations of the reptend." Verified cold, in
sharpened form, and it opens the dictionary of the place. Everything below is a
ratio, a count, or an exact congruence — no ruler, no magnitude claim. The fence
of THE-FORM-OF-GRAVITY §12 is untouched.

The dictionary so far (each entry pinned below):
    1 place   =  1 rotation of the reptend wheel   (x10 = the left-shift)
    each place multiplies by 3 mod 7               (the wheel turns BY the triad prime)
    3 places  =  negation                          (10^3 = -1 mod 7; the involution
                                                    of part one, as a MOTION)
    the 9     =  negation's seal                   (digit + digit-3-later = 9, every place)
    6 places  =  the cycle, returning SHORT by 1   (the remainder that reseeds the loop)
"""

import math
from fractions import Fraction as F

R = 142857
NINES = 10 ** 6 - 1


def _full_reptend(p):
    if p in (2, 5):
        return False
    o, x = 1, 10 % p
    while x != 1:
        x, o = (x * 10) % p, o + 1
    return o == p - 1


def test_one_decimal_place_is_one_rotation_of_the_wheel():
    """Multiplying by ten — moving the decimal point one place — IS the left
    rotation of the reptend string (the cyclic-number shift property). So the
    ladder of decimal places is the wheel's own odometer: places COUNT rotations."""
    cur = R
    seen = []
    for _ in range(6):
        seen.append(cur)
        cur = (cur * 10) % NINES                      # x10 = rotate left one place
    assert cur == R                                    # six places close the wheel
    s = str(R)
    assert seen == [int(s[i:] + s[:i]) for i in range(6)]   # each step IS a rotation

    # as residues mod 7 the walk is x3 each step: 1 -> 3 -> 2 -> 6 -> 4 -> 5
    assert 10 % 7 == 3                                 # the wheel turns BY the three
    ks = [v // R if v % R == 0 else None for v in seen]
    assert ks == [1, 3, 2, 6, 4, 5]
    assert all(ks[(i + 1) % 6] == (ks[i] * 3) % 7 for i in range(6))

    # seven's third specialness: among all full-reptend primes below 200, ONLY
    # seven lies below ten, so only seven's rotation residue reduces — and it
    # reduces to 3, the shared prime of the two rings (gcd(9,12) = 3).
    frs = [p for p in range(7, 200)
           if all(p % q for q in range(2, int(p ** .5) + 1)) and _full_reptend(p)]
    assert [p for p in frs if p < 10] == [7]
    assert 10 % 7 == 3 == math.gcd(9, 12)


def test_three_rotations_are_negation_and_the_nine_is_its_seal():
    """the author's swing, exact: three rotations = x10^3, and 1000 = -1 mod 7, so THREE
    PLACES ARE ONE NEGATION — the involution of part one (§8b: the one map,
    negation) is a MOTION on the wheel, costing exactly half the orbit. Its seal
    is the nine: every digit plus the digit three rotations later is 9, which is
    Midy's pairing read as motion. And 1001 = 7 x 11 x 13: three places is
    negation for seven, eleven and thirteen at once."""
    assert 1000 % 7 == 6 == (-1) % 7                   # three rotations = negation
    assert 7 * 11 * 13 == 1001                         # and for 11 and 13 too

    s = str(R)
    for i in range(6):
        assert int(s[i]) + int(s[(i + 3) % 6]) == 9    # the seal, at every place
    assert R + 857142 == NINES                         # value + 3-rotation image = nines
    assert (R * 1000) % NINES == 857142                # and that image IS x10^3

    # the general law: negation costs half the orbit, and its seal is the nine —
    # this is exactly the Midy condition 10^((p-1)/2) = -1 mod p
    for p in (7, 17, 19, 23, 29):
        e = p - 1
        rep = str((10 ** e - 1) // p).zfill(e)
        assert pow(10, e // 2, p) == p - 1             # half-orbit = negation
        assert all(int(rep[i]) + int(rep[(i + e // 2) % e]) == 9 for i in range(e))


def test_the_cycle_returns_short_and_the_shortfall_reseeds_the_loop():
    """Six places = two negations = the identity — but the RETURN IS SHORT:
    10^6 = 1 mod 7, and that remainder 1 is exactly what long division brings
    the next zero down onto. The deficit at cycle-completion is what restarts
    the wheel: the loop runs forever BECAUSE the return is one short. This is
    the mechanism's answer to 'where would it get energy to loop' — from its
    own shortfall, every turn."""
    assert pow(10, 6, 7) == 1                          # the cycle closes as residue 1
    assert 10 ** 6 - 7 * R == 1                        # ...which IS the shortfall of one
    assert pow(1000, 2, 7) == 1                        # two negations = identity

    # general: the remainder at full period is 1 for every full-reptend prime —
    # the same 1 that seeds the next period. One object: closure-residue = reseed.
    for p in (7, 17, 19, 23, 29):
        assert pow(10, p - 1, p) == 1
        assert 10 ** (p - 1) - p * ((10 ** (p - 1) - 1) // p) == 1

    # and in the extension reading (§10b): n places = n rotations, and the energy
    # falls a hundredfold per rotation — the inverse square, in wheel language
    for n in (1, 2, 3):
        d1, d2 = 10 ** n - 1, 10 ** (n + 1) - 1
        assert F(1, (d2 + 1) ** 2) / F(1, (d1 + 1) ** 2) == F(1, 100)


# ---------------------------------------------------------------------------
# THE 149 LEAD, THREE PROBES (2026-08-09) — provenance, type-flag, prediction
# ---------------------------------------------------------------------------

def test_a_decimal_rotation_is_three_octaves_and_one_just_third():
    """10 = 2^3 x 5/4 EXACTLY. One decimal rotation = three octaves + one just
    major third. So the 5/4 in the alpha_G lead is not imported from music --
    it is the RESIDUE OF THE DECIMAL OVER THE OCTAVE LADDER, the per-place
    remainder after the octaves are taken out. The dress has internal
    provenance. And the full cycle gives the deficit octave-third coordinates
    (-18, -6): the rotation-ledger number and the hexad count, one third per
    place (flagged as a reading, not built on)."""
    assert F(10) == F(2) ** 3 * F(5, 4)                    # the identity
    assert F(10) ** 6 == F(2) ** 18 * F(5, 4) ** 6         # the full cycle
    assert F(1, 10) == F(1, 2 ** 3) * F(4, 5)              # per place: 3 oct + 1 third
    # deficit coordinates: 10^-6 = 2^-18 (5/4)^-6
    assert F(1, 10 ** 6) == F(1, 2 ** 18) * F(4, 5) ** 6


def test_the_lead_in_minimal_form_its_type_flag_and_the_G_prediction():
    """(5/4) x 2^-149 = 5 x 2^-151 EXACTLY -- the lead's prime-minimal form is
    ONE five and 151 halvings. TYPE-FLAG, our own standard applied to ourselves:
    the banked gloss '149 = 137 + 12' adds a numeral (alpha^-1, linear) to an
    octave count (a logarithm) -- the same cross-type move that retired
    205 - 149 = 56. The gloss is retired-grade; the lead's legal content is the
    bare fit. PREDICTION: if the count is ever forced, the framework outputs
    G = 5 x 2^-151 x hbar c / m_e^2, ~35x sharper than CODATA-18 and sitting
    -106 ppm from its centre -- inside the unresolved G discordance, so the
    lead is neither killable nor confirmable on today's G."""
    assert F(5, 4) * F(1, 2 ** 149) == F(5, 2 ** 151)      # minimal form, exact

    hbar, c = 1.054571817e-34, 299792458.0                 # exact (SI 2019)
    me = 9.1093837015e-31                                  # CODATA-18, 0.31 ppm
    G_codata, G_rel = 6.67430e-11, 2.2e-5                  # CODATA-18, 22 ppm

    G_pred = float(F(5, 2 ** 151)) * hbar * c / me ** 2
    assert 6.67358e-11 < G_pred < 6.67360e-11              # 6.673590e-11
    offset_ppm = 1e6 * (G_pred - G_codata) / G_codata
    assert -107 < offset_ppm < -105                        # -106.4 ppm
    assert abs(offset_ppm) / (1e6 * G_rel) > 4             # >4 sigma of CODATA...
    assert abs(offset_ppm) < 250                           # ...but inside the G discordance


def test_the_four_dresses_are_one_point_and_the_old_number_reconciles():
    """(-151, +1) is a coordinate pair (exp of 2, exp of 5) -- the numbers never
    add. The five can arrive in four dresses, the octave count trading
    one-for-one: {149: 5/4, 150: 5/2, 151: 5, 152: 10} -- one lattice point,
    four costumes. And the octave PROJECTION of the point, -151 + log2(5)
    = -148.678, IS the banked '~148.7 octaves down': the old number and the
    lead were the same object all along."""
    lead = F(5, 2 ** 151)
    assert F(5, 4) * F(1, 2 ** 149) == lead            # the third dress
    assert F(5, 2) * F(1, 2 ** 150) == lead            # the tenth dress
    assert F(5, 1) * F(1, 2 ** 151) == lead            # the bare five
    assert F(10, 1) * F(1, 2 ** 152) == lead           # the rotation dress

    proj = -151 + math.log2(5)
    assert abs(proj - (-148.678072)) < 1e-6            # the octave projection
    assert abs((149 - math.log2(5 / 4)) - 148.678072) < 1e-6   # same reconciliation


def test_the_lattice_prunes_the_walks_to_one_lift_against_the_fall():
    """Two forced unreachability results, then the surviving shape.
    NEGATIVE 1: places + thirds alone cannot reach (-151, +1) -- the system
    forces 3x = 149, and 149 is not divisible by 3.
    NEGATIVE 2: deficit-cycles + octaves cannot reach it -- their five-exponent
    is always a multiple of six, never +1. The naive cascade family is dead.
    SURVIVES: every downward move (place, negation, deficit) carries NEGATIVE
    five-exponent and octaves carry none, so every walk to the lead contains
    exactly one net UPWARD five-carrier against a pure octave descent:
    ONE LIFT AGAINST A LONG FALL -- the mechanism's own shape.
    AND: the lead is three-free -- gravity's coupling lands on the {2,5}
    (decimal) lattice, not the harmonic {2,3} lattice; the banked 'off-lattice'
    negative was an off-the-2-3 verdict, now understood rather than bare."""
    assert 149 % 3 != 0                                # negative 1: no integer walk
    assert all((-6 * c) % 6 == 0 and -6 * c != 1
               for c in range(-30, 31))                # negative 2: five-exp stuck

    # downward moves all carry five-exponent <= -1; the lift candidates carry +1
    moves_down = {"place": (-1, -1), "negation": (-3, -3), "deficit": (-6, -6)}
    lifts = {"third": (-2, 1), "tenth": (-1, 1), "five": (0, 1), "rotation": (1, 1)}
    assert all(b < 0 for _, b in moves_down.values())
    assert all(b == 1 for _, b in lifts.values())

    # three-free: the lead's numerator and denominator carry no factor of three
    lead = F(5, 2 ** 151)
    assert lead.numerator % 3 != 0 and lead.denominator % 3 != 0
    assert lead.denominator == 2 ** 151 and lead.numerator == 5


# ---------------------------------------------------------------------------
# the author'S SWAP FIGURE (2026-08-09): the {4,5} transposition, drawn and dissected
# ---------------------------------------------------------------------------

def test_the_midy_swaps_and_their_costs():
    """Transposing the members of one Midy pair preserves the digit-pairing and
    costs a multiple of 999. In 999-units: reptend = 143 = 11 x 13 = 1001/7;
    the three swaps cost {1,8} -> +700, {2,7} -> +5, {4,5} -> +10. THE TWO
    INTEGER LIFT-DRESSES OF THE LATTICE WALK -- the bare five and the bare ten
    -- ARE THE SWAP-COSTS OF THE TWO INNER PAIRS. the author's bet (rotation, 10) is
    the {4,5} swap; the rival (five) is the {2,7} swap. And the {4,5} swap
    lands on 153 x 999 with 153 = 9 x 17 = T_17, the banked forced 153."""
    R_, S_ = 142857, 152847
    assert S_ not in {int(str(R_)[i:] + str(R_)[:i]) for i in range(6)}   # off the wheel
    assert S_ % 7 != 0
    s = str(S_)
    assert all(int(s[i]) + int(s[(i + 3) % 6]) == 9 for i in range(3))    # Midy kept
    assert 152 + 847 == 999

    assert R_ == 143 * 999 and 143 == 11 * 13 and F(1001, 7) == 143
    assert 842157 == 843 * 999 and 843 - 143 == 700       # {1,8} swap
    assert 147852 == 148 * 999 and 148 - 143 == 5         # {2,7} swap -> the FIVE
    assert S_ == 153 * 999 and 153 - 143 == 10            # {4,5} swap -> the TEN
    assert 153 == 9 * 17 == 17 * 18 // 2                  # T_17, the banked 153
    assert R_ == 3 ** 3 * 11 * 13 * 37 and S_ == 3 ** 5 * 17 * 37


def test_the_swap_threads_the_arena():
    """On the tempered seats, the standard path 1-4-2-8-5-7 crosses the mirror
    axis with only TWO of its six chords; the swapped path 1-5-2-8-4-7 crosses
    with ALL SIX. Transposing the stayers converts the wheel from axis-avoiding
    to axis-threading -- the swap routes the whole path through the arena."""
    ang = {1: 40, 2: 80, 4: 160, 5: 200, 7: 280, 8: 320}
    x = lambda d: math.sin(math.radians(ang[d]))
    std = [(1, 4), (4, 2), (2, 8), (8, 5), (5, 7), (7, 1)]
    swp = [(1, 5), (5, 2), (2, 8), (8, 4), (4, 7), (7, 1)]
    assert sum(1 for a, b in std if x(a) * x(b) < 0) == 2
    assert sum(1 for a, b in swp if x(a) * x(b) < 0) == 6


def _kite_ratio(angles):
    P = lambda d: (math.sin(math.radians(angles[d])), math.cos(math.radians(angles[d])))
    def inter(c1, c2):
        (x1, y1), (x2, y2) = P(c1[0]), P(c1[1])
        (x3, y3), (x4, y4) = P(c2[0]), P(c2[1])
        den = (x1 - x2) * (y3 - y4) - (y1 - y2) * (x3 - x4)
        t = ((x1 - x3) * (y3 - y4) - (y1 - y3) * (x3 - x4)) / den
        return (x1 + t * (x2 - x1), y1 + t * (y2 - y1))
    Pa, Pb, L = inter((1, 5), (8, 4)), inter((2, 5), (7, 4)), inter((1, 5), (7, 4))
    return (Pa[1] - L[1]) / (L[1] - Pb[1])


def test_the_kite_ratio_and_the_rectification_negatives():
    """The A/B question from the author's diagram, settled honestly. Tempered kite:
    A/B = 2.064178 -- near two, NOT two. Rectifying to the intonated seats
    makes it MORE unequal (2.241743, and NOT 9/4 -- off by 0.37%), and the
    seat-displacement family reaches A/B = 1 only near u ~ 6-7 x the intonated
    displacement: NO equal-area view exists in the family. And the one-param
    circle-preserving downward slide is REJECTED: the {2,7} pair forces
    s = tan(5 deg) exactly (2 atan s = 10 deg -- the half-degree appears),
    while the {1,8} pair forces s = tan(~3.69 deg). Inconsistent. What is
    forced is the RATIO; the fold reading (one lamina, two tilts) stays
    admissible but unforced."""
    TEMP = {1: 40, 2: 80, 4: 160, 5: 200, 7: 280, 8: 320}
    INTO = {1: 45, 2: 90, 4: 160, 5: 200, 7: 270, 8: 315}
    rt, ri = _kite_ratio(TEMP), _kite_ratio(INTO)
    assert abs(rt - 2.064177772) < 1e-8
    assert abs(rt - 2) > 0.06                              # near two, not two
    assert abs(ri - 2.241743328) < 1e-8
    assert abs(ri - 2.25) / 2.25 > 0.003                   # NOT 9/4
    assert ri > rt                                         # rectifying worsens it
    u7 = {1: 45 - 35, 2: 90 - 70, 4: 160, 5: 200, 7: 270 + 70, 8: 315 + 35}
    assert _kite_ratio(u7) > 1.3                           # equal-area not in family

    # the slide model: s = tan 5 deg maps 90 -> 80 exactly, but sends 45 -> 38.3
    s = math.tan(math.radians(5))
    assert abs(2 * math.degrees(math.atan(s)) - 10) < 1e-12
    th = math.radians(90 - 45)
    z = complex(math.cos(th), math.sin(th))
    w = (z + 1j * s) / (1 - 1j * s * z)
    a45 = 90 - math.degrees(math.atan2(w.imag, w.real))
    assert abs(a45 - 38.32) < 0.05 and abs(a45 - 40) > 1.5   # misses 40: inconsistent


def test_the_halves_collapse_to_the_other_pairs():
    """Digit-sums of the halves: reptend (142, 857) -> (7, 20) -- the banked
    20|7 pair -- and the swap moves exactly one unit: (152, 847) -> (8, 19).
    the author's step 19 -> 10 gives 10/8 = 5/4, the third -- re-deriving the
    dress-trade identity 10 = 8 x 5/4 from inside the figure (stop-at-10 is
    one named convention). Fully collapsed, no convention: the reptend's
    halves land on {7, 2} = the {2,7} PAIR and the swapped figure's on
    {8, 1} = the {1,8} PAIR -- transposing the stayers carries the figure's
    half-signature from the middle pair to the outer pair."""
    dsum = lambda n: sum(int(c) for c in str(n))
    dr = lambda n: 1 + (n - 1) % 9
    assert (dsum(142), dsum(857)) == (7, 20)
    assert (dsum(152), dsum(847)) == (8, 19)
    assert dsum(142) + dsum(857) == 27 == dsum(152) + dsum(847)   # hexad sum, both
    assert dsum(19) == 10 and F(10, 8) == F(5, 4)                 # the author's third
    assert F(10, 1) == F(8, 1) * F(5, 4)                          # the dress-trade
    assert (dr(142), dr(857)) == (7, 2)                           # the {2,7} pair
    assert (dr(152), dr(847)) == (8, 1)                           # the {1,8} pair
    assert dr(142) + dr(857) == 9 == dr(152) + dr(847)            # forced by Midy


def test_the_five_is_a_one_way_door_on_the_two_three_lattice():
    """the author's 24-move, manual path: 24 x 10/8 = 30 (Mi -- seats); 24 x 8/10 = 19.2
    (does not seat; the residue is exactly 1/5, the undissolved five). General
    theorem: on 2-3 numbers the up-third n x 5/4 seats whenever 4 | n, but the
    down-third n x 4/5 NEVER seats -- 5 never divides 2^a 3^b. THE FIVE ENTERS
    FREELY AND CAN NEVER LEAVE: the manual-path twin of the lattice result
    'every walk to the lead needs exactly one upward five-carrier'. And the
    additive manual-path residue of the dress-trade move 10/8 is 10 - 8 = +/-2
    -- a forced two riding the third; its link to spin-2 stays a signpost."""
    assert 24 * 10 // 8 == 30                              # Mi seats
    assert F(24 * 8, 10) == F(96, 5)                       # the down-third does not
    assert F(96, 5) - 19 == F(1, 5)                        # the residue IS 1/5
    for a in range(8):
        for b in range(5):
            n = 2 ** a * 3 ** b
            assert F(n * 4, 5).denominator == 5            # down-five never dissolves
            if n % 4 == 0:
                assert F(n * 5, 4).denominator == 1        # up-five seats on 4 | n
    assert 10 - 8 == 2 and 8 - 10 == -2                    # the additive residue


def test_the_collapse_trails_and_the_conserved_three():
    """the author: 'the root collapses in 2 steps, 1+9=10, 1+0=1 -- 1 unit, two
    rotations, total 3.' The collapse TRAIL is the object (§9), and it is
    forced: 847 -> 19 -> 10 -> 1. So the 10 is not a stopping convention --
    it is a STATION the high half necessarily passes through on its way to
    unity, and reading 10/8 = 5/4 there is reading a forced station.
    Depths: reptend halves (1, 2); swapped halves (1, 3) -- the swap adds one
    fold. And under the author's accounting (first sum, then value + remaining folds):
        857: 20 -> 2, value 2 + 1 fold = 3
        847: 19 -> 10 -> 1, value 1 + 2 folds = 3
    THE SWAP TRADES ONE UNIT OF VALUE FOR ONE FOLD OF DEPTH, CONSERVING
    THREE on the high half -- the triad number, conserved through the
    transposition of the stayers."""
    def trail(n):
        t = []
        while n > 9:
            n = sum(int(c) for c in str(n))
            t.append(n)
        return t

    assert trail(142) == [7] or sum(int(c) for c in "142") == 7   # one fold to 7
    assert trail(857) == [20, 2]                                  # two folds
    assert trail(152) == [8]                                      # one fold
    assert trail(847) == [19, 10, 1]                              # three folds
    assert 10 in trail(847)                                       # the forced station

    # the author's accounting: first sum, then (final value) + (remaining folds)
    assert 2 + 1 == 3                                             # 857: value 2, 1 fold
    assert 1 + 2 == 3                                             # 847: value 1, 2 folds
    # the swap moves one unit of value into one fold of depth; three conserved


def test_value_plus_address_is_the_just_semitone_raise():
    """the author's composite (value on the 24-root PLUS address in degrees) closes to
    a forced identity:  24r + 360(r-1) = 360(16r/15 - 1)  -- THE SUM OF VALUE
    AND ADDRESS IS THE ADDRESS OF THE TONE ONE JUST SEMITONE HIGHER. The 'two
    domains' are one statement. It lands on a scale tone exactly at the
    scale's own two half-step joints (Mi->Fa, Si->Do'), and its two most
    loaded landings are C(Fa) = 152 = the address of THE TRITONE 64/45 (the
    V7 engine, the self-inverse interval -- the deficit tone and the pull's
    engine are ONE HALF-STEP apart) and C(Re) = 72 = the address of the just
    minor third 6/5. TYPE-FLAG kept: 152 DEGREES is not 152 OCTAVES -- the
    numeral echo with the rotation-dress count is sandboxed, same standard
    as 137+12. And the author's fyi: La's address-fraction 240/360 = 2/3 is the
    REVERSED FIFTH -- the address-reciprocals 360/addr run {8,4,3,2,3/2,8/7},
    with La (the fifth) and Si (the septimal) the two non-integers."""
    SC = {'Do': F(1), 'Re': F(9, 8), 'Mi': F(5, 4), 'Fa': F(4, 3),
          'Sol': F(3, 2), 'La': F(5, 3), 'Si': F(15, 8)}
    addr = lambda r: 360 * (r - 1)

    for r in list(SC.values()) + [F(7, 5), F(22, 7)]:
        assert 24 * r + addr(r) == addr(F(16, 15) * r)      # the identity, exact

    joints = [n for n, r in SC.items()
              if F(16, 15) * r in SC.values() or F(16, 15) * r == 2]
    assert joints == ['Mi', 'Si']                            # the half-step joints

    assert 24 * F(4, 3) + addr(F(4, 3)) == 152 == addr(F(64, 45))   # Fa -> tritone
    assert F(16, 15) * F(4, 3) == F(64, 45)                  # one semitone above Fa
    assert 24 * F(9, 8) + addr(F(9, 8)) == 72 == addr(F(6, 5))      # Re -> minor third

    # the author's fyi: the reversed fifth 2/3, as a fraction of the turn, seats La
    assert F(addr(SC['La']), 360) == F(2, 3)
    recips = {n: F(360, addr(r)) for n, r in SC.items() if r != 1}
    assert recips == {'Re': F(8), 'Mi': F(4), 'Fa': F(3), 'Sol': F(2),
                      'La': F(3, 2), 'Si': F(8, 7)}


def test_the_harmonic_order_is_the_triad_with_its_up_coset():
    """the author's figure: 1+3+4+6+7+9 = 30, the harmonic order. The theorem under it:
    the nine seats split into the THREE COSETS OF THE TRIAD under one seat-step:
    t = {3,6,9} (sum 18, the rotation ledger), t+1 = {4,7,1} (sum 12, the
    up-roundings = the operator class, +40 deg), t-1 = {2,5,8} (sum 15, the
    banked carrier at -40 deg). THE HARMONIC ORDER IS t UNION t+1 -- the triad
    with its up-roundings; 'the rounding in the harmonic order' is round-UP,
    seat by seat. Sum 30 = 18 + 12."""
    t = {3, 6, 9}
    tp = {x % 9 + 1 for x in t}
    tm = {(x - 2) % 9 + 1 for x in t}
    assert tp == {4, 7, 1} and tm == {2, 5, 8}
    assert t | tp | tm == set(range(1, 10))            # the three cosets partition
    assert t | tp == {1, 3, 4, 6, 7, 9}                # the harmonic order
    assert set(range(1, 10)) - (t | tp) == tm          # complement = the carrier
    assert (sum(t), sum(tp), sum(tm)) == (18, 12, 15)
    assert sum(t | tp) == 30 == 18 + 12


def test_the_comma_ledger_selects_the_up_branch():
    """the author's ledger: the rest frame 2.999997 under ONE COMMA, both ways.
    Digit-sum collapse trails (forced):
        NEG  2.999996 -> 53 -> [8]
        REST 2.999997 -> 54 -> [9]
        POS  2.999998 -> 55 -> [10, 1]    (ten is a forced station)
    One comma acting +/- about the rest produces the (8, 9, 10) ladder, and
    BOTH dresses fall out of the one object: the up branch alone carries 10
    (the rotation dress); the branch ratio 10/8 = 5/4 (the third dress).
    SELECTION (graded ◇): the shortfall theorem forces the lift one-signed UP,
    so the mechanism only ever takes the up branch, whose station is TEN. If
    the coupling's dress is the station of the taken branch, the dress is 10,
    the count is 152. The premise is the reading; the ledger is forced.
    the author's 8x8: 64 -> [10, 1] shares the up-branch station (octave SQUARED up,
    bare 8 down -- the double-copy shape, signpost only)."""
    def trail(n):
        t = []
        while n > 9:
            n = sum(int(c) for c in str(n))
            t.append(n)
        return t

    assert sum(int(c) for c in "2999996") == 53 and trail(53) == [8]
    assert sum(int(c) for c in "2999997") == 54 and trail(54) == [9]
    assert sum(int(c) for c in "2999998") == 55 and trail(55) == [10, 1]
    assert F(10, 8) == F(5, 4)                          # the branch ratio
    assert trail(64) == [10, 1]                         # 8x8 shares the station
    # and the rest frame itself is the sevenths' rest-3: 3 x (1 - 10^-6)
    assert F(2999997, 10 ** 6) == 3 * (1 - F(1, 10 ** 6))


def test_the_exact_slide_and_the_369_digit_read_killed():
    """The {1,8} slide now has a closed form: s = (sec 50 - sqrt 2)/(1 + tan 50),
    angle 3.6942 degrees. The '3.69' was a two-decimal display of mine; the
    digit-read (three-six-nine) dies at the third decimal. Pinned so the
    pattern cannot regrow from the rounding."""
    s = (1 / math.cos(math.radians(50)) - math.sqrt(2)) / (1 + math.tan(math.radians(50)))
    # it satisfies the defining condition: the slide sends the 45-point to 40
    th = math.radians(90 - 45)
    z = complex(math.cos(th), math.sin(th))
    w = (z + 1j * s) / (1 - 1j * s * z)
    assert abs((90 - math.degrees(math.atan2(w.imag, w.real))) - 40) < 1e-9
    ang = math.degrees(math.atan(s))
    assert abs(ang - 3.694166) < 1e-5                   # the exact angle
    assert abs(ang - 3.69) > 0.004                      # the digit-read is dead


# ---------------------------------------------------------------------------
# THE SELECTION (2026-08-09) — which transposition, by elimination
# ---------------------------------------------------------------------------

def test_the_selection_eliminators():
    """Three Midy transpositions, three eliminators, all forced.
    (1) LATTICE CONTENT: the lead 5 x 2^-151 has one five, no three, no seven.
        {1,8}'s cost 700 = 2^2 x 5^2 x 7 is excluded TWICE (5-squared; a seven)
        with no premise needed. {2,7}'s 5 and {4,5}'s 10 are both legal.
    (2) FLANKING: {1,8} flanks the root, {4,5} flanks the empty seat, {2,7}
        flanks neither fixed point (60 deg from each).
    (3) THREADING, all three swaps now checked: standard 2/6, {1,8}-swap 2/6,
        {2,7}-swap 2/6, {4,5}-swap 6/6. ONLY the stayer transposition threads
        the arena; the other swaps leave the wheel arena-avoiding.
    Plus a numeral-level uniqueness (echo to the octave count sandboxed):
    only the {4,5} object has front-half = product of its halves' digit sums
    (8 x 19 = 152; reptend gives 140 != 142, the others 182/180)."""
    assert 700 == 2 ** 2 * 5 ** 2 * 7                     # excluded twice
    assert 5 == 5 and 10 == 2 * 5                         # both legal, one five

    T = {9: 0, 1: 40, 2: 80, 3: 120, 4: 160, 5: 200, 6: 240, 7: 280, 8: 320}
    x = lambda d: math.sin(math.radians(T[d]))
    assert sorted(d for d in T if min(T[d], 360 - T[d]) == 40) == [1, 8]
    assert sorted(d for d in T if abs(T[d] - 180) == 20) == [4, 5]
    assert min(abs(T[2] - 0), abs(T[2] - 180)) == 80 and abs(T[7] - 180) == 100

    paths = {
        "std": [(1, 4), (4, 2), (2, 8), (8, 5), (5, 7), (7, 1)],
        "s18": [(8, 4), (4, 2), (2, 1), (1, 5), (5, 7), (7, 8)],
        "s27": [(1, 4), (4, 7), (7, 8), (8, 5), (5, 2), (2, 1)],
        "s45": [(1, 5), (5, 2), (2, 8), (8, 4), (4, 7), (7, 1)],
    }
    crossings = {k: sum(1 for a, b in v if x(a) * x(b) < 0) for k, v in paths.items()}
    assert crossings == {"std": 2, "s18": 2, "s27": 2, "s45": 6}   # unique threading

    dsum = lambda n: sum(int(c) for c in str(n))
    assert dsum(152) * dsum(847) == 152                   # only the {4,5} object
    assert dsum(142) * dsum(857) == 140 != 142
    assert dsum(842) * dsum(157) == 182 != 842
    assert dsum(147) * dsum(852) == 180 != 147


def test_the_selection_conditional_and_what_remains():
    """The chain, with its one premise named and the remaining gap stated:
    PREMISE (◇, two banked feet: gravity is READ at the stratum; no source may
    SIT there -- so coupling is by CROSSING): the coupling's lift is the cost
    of the transposition that carries the wheel through the arena. Under it
    the {4,5} swap is unique, the dress is 10, and the lead reads
    10 x 2^-152. WHAT THIS DOES NOT DO: derive the 152. The descent count is
    the one remaining fitted number; the four dresses are one lattice point,
    so G_pred's VALUE never depended on the selection -- only the mechanism
    story did. G_pred goes fully live when the count is forced, not before."""
    assert F(10, 1) * F(1, 2 ** 152) == F(5, 2 ** 151)    # same point, dress derived

    hbar, c, me = 1.054571817e-34, 299792458.0, 9.1093837015e-31
    G_pred = float(F(5, 2 ** 151)) * hbar * c / me ** 2
    assert 6.67358e-11 < G_pred < 6.67360e-11             # 6.6735902e-11, unchanged
    offset_ppm = 1e6 * (G_pred - 6.67430e-11) / 6.67430e-11
    assert -107 < offset_ppm < -105                       # the standing -106.4 ppm


# ---------------------------------------------------------------------------
# THE COUNT (2026-08-09 night) — not forced; halved, and given a birth record
# ---------------------------------------------------------------------------

def test_the_square_split_and_the_wheels_own_tritone():
    """The banked double-copy (gravity = square) splits the lead exactly:
    10 x 2^-152 = (sqrt(10) x 2^-76)^2. The amplitude's dress sqrt(10) is THE
    WHEEL'S OWN PARTNERLESS INTERVAL -- the unique fixed point of decade
    inversion s <-> 10/s -- the same theorem that put the 12-ring's engine at
    the self-inverse 6. And sqrt(10) = sqrt(2) x sqrt(5): the octave's tritone
    times the five's. Under the double-copy reading the count question HALVES:
    force 76 and 152 = 2 x 76 follows. (The split is exact; the double-copy
    assignment is the banked ◇.)"""
    assert F(10, 2 ** 152) == F(10, 1) * F(1, 2) ** 152    # the lead, exact
    assert 2 * 76 == 152                                    # the square doubles
    s = math.sqrt(10)
    assert abs(s * s - 10) < 1e-12                          # s <-> 10/s fixed point
    assert abs(s - math.sqrt(2) * math.sqrt(5)) < 1e-12     # both tritones at once
    assert abs((s * 2 ** -76) ** 2 - 10 * 2 ** -152) < 1e-60


def test_the_cyclotomic_birth_of_151():
    """Where the count's prime is BORN on the halving ladder. The tether prime
    is the binary triple-nine: 7 = 2^3 - 1 = 111_2, period ord_2(7) = 3. The
    five's binary all-ones is 31 = 2^5 - 1, period 5. The two cycles first
    mesh at lcm(3,5) = 15, and the primitive prime born there is

        151 = (2^15 - 1)/((2^3 - 1)(2^5 - 1)) = Phi_15(2),  ord_2(151) = 15.

    THE MOTOR (3) AND THE LIFT (5), MESHED ON THE BINARY WHEEL, BEGET 151.
    Discriminator: among the four costume-counts {149,150,151,152}, ONLY 151
    is a Phi_n(2) value for any n <= 48 -- and its n is three-times-five.
    TYPE-FLAG, held: using the VALUE 151 as an EXPONENT (2^-151) is a
    value-as-exponent crossing; this is a birth record ◇◇, not a forcing.
    A forcing needs a mechanism that exponentiates."""
    def ord2(m):
        o, x = 1, 2 % m
        while x != 1:
            x, o = (x * 2) % m, o + 1
        return o

    assert 7 == 2 ** 3 - 1 and bin(7) == "0b111"            # binary triple-nine
    assert 31 == 2 ** 5 - 1
    assert (ord2(7), ord2(31), ord2(151)) == (3, 5, 15)
    assert math.lcm(3, 5) == 15
    assert 2 ** 15 - 1 == 32767 == 7 * 31 * 151
    assert (2 ** 15 - 1) // ((2 ** 3 - 1) * (2 ** 5 - 1)) == 151
    phi15 = lambda x: x ** 8 - x ** 7 + x ** 5 - x ** 4 + x ** 3 - x + 1
    assert phi15(2) == 151                                  # the 15th cyclotomic at 2

    def mobius(m):
        res, d = 1, 2
        while d * d <= m:
            if m % d == 0:
                m //= d
                if m % d == 0:
                    return 0
                res = -res
            d += 1
        return -res if m > 1 else res

    def phi_n_at_2(n):
        num = den = 1
        for d in range(1, n + 1):
            if n % d == 0:
                mu = mobius(n // d)
                if mu == 1:
                    num *= 2 ** d - 1
                elif mu == -1:
                    den *= 2 ** d - 1
        return num // den

    hits = {n: phi_n_at_2(n) for n in range(2, 49)
            if phi_n_at_2(n) in {149, 150, 151, 152}}
    assert hits == {15: 151}                                # unique among the four


def test_the_exponent_is_a_period_and_irreducibility_forces_the_block():
    """THE EXPONENTIATING MECHANISM: the figure's own way of putting a number in
    an exponent is the PERIOD OF A WHEEL -- the reptend form x/(b^k - 1), the
    form 1/7 itself lives in. Applied to the lead:

        alpha_G(e) = 5/(2^151 - 1)   -- block 5 = 101_2, period 151 --

    differing from 5 x 2^-151 by a relative 2^-151 ~ 3.5e-46: forty orders
    below G's softness; empirically identical forever. AND THE WHEEL FORM
    BREAKS THE COSTUME DEGENERACY: ord_2(5) = 4, and 4 does not divide 151,
    so gcd(5, 2^151-1) = 1 -- IRREDUCIBLE; but 4 | 152, so 5 divides
    2^152 - 1 and the ten-block form REDUCES, destroying its block; the 5/4
    and 5/2 costumes have non-integer blocks and no wheel form at all. The
    lead has EXACTLY ONE irreducible binary-wheel representation: the lift
    (101_2) circulating on the 151-cycle -- and 151 = Phi_15(2), the
    mesh-child. ONE JOINT REMAINS: why the coupling rides the mesh-child's
    Mersenne wheel. Block: forced. Period-of-that-wheel: forced. Parentage
    of 151: forced. The joint is the last open sentence."""
    M = 2 ** 151 - 1
    rel = (F(5, M) - F(5, 2 ** 151)) / F(5, 2 ** 151)
    assert rel == F(1, M)                                  # 2^-151-ish: ~3.5e-46
    assert float(rel) < 1e-45 < 2.2e-5                     # forty orders under G

    assert pow(2, 151, 5) != 1 and 151 % 4 != 0            # 5 coprime to 2^151-1
    assert (2 ** 151 - 1) % 5 != 0                         # irreducible block 5
    assert pow(2, 152, 5) == 1 and (2 ** 152 - 1) % 5 == 0  # ten-block reduces
    assert bin(5) == "0b101"                               # the lift, in binary

    # the Mersenne wheel's period is its own exponent: ord_2(2^151-1) = 151
    assert pow(2, 151, M) == 1
    assert all(pow(2, k, M) != 1 for k in (1, 76, 150))    # and nothing smaller

    # 76 dissolves: half the successor of the period; the amplitude's dress is
    # irrational (10 is not a square) -- the amplitude never seats, its square does
    assert 76 == (151 + 1) // 2
    assert math.isqrt(10) ** 2 != 10
    assert (4 ** 19 + 1) // 5 == 54975581389               # Phi_76(2): not framework


def test_the_tower_law_and_the_assembled_sentence():
    """THE CLOSING SENTENCE, with its negative and its grade.
    NEGATIVE first: the literal 'smallest wheel where motor and lift complete
    together' is depth 15, and 5/(2^15 - 1) ~ 1.5e-4 -- off by 41 orders. Dead.
    THE MISSING STEP IS THE FIGURE'S OWN GAIT: the tower law. For prime depth p,
    the promotion is Phi_p(2) = 2^p - 1, and the figure's prime chain IS the
    tower: promote(2) = 3 (the motor), promote(3) = 7 (the tether),
    promote(7) = 127. Value-becomes-depth is not a type crime -- it is how the
    octave begets the motor begets the tether, one promotion per generation.
    THE SENTENCE: alpha_G(e) = 5/(2^Phi_15(2) - 1) -- THE LIFT RIDING THE
    SINGLE PROMOTION OF THE MESH. Gravity's wheel is to the mesh (3 x 5) what
    the tether is to the motor (3): one promotion up.
    GRADE, held: every leg forced; the assembly Sound-conditional. And the author's
    caution folded in: THE 3 AND 5 ARE CHEAP -- any construction finds them --
    so the assembly's whole burden sits on three joints: (1) the mesh
    combination 15, (2) the promotion law's applicability (anchored by
    2->3->7->127 being the figure's own chain), (3) the single gait. Those
    three are where the adversarial pass must aim."""
    assert float(F(5, 2 ** 15 - 1)) > 1e-4                 # the literal sentence dies

    assert 2 ** 2 - 1 == 3 and 2 ** 3 - 1 == 7 and 2 ** 7 - 1 == 127
    # promote(2)=3, promote(3)=7, promote(7)=127 -- the figure's chain, one
    # promotion per generation (Catalan-Mersenne, cyclotomic form)

    assert 10 % 7 == 3 == math.gcd(9, 12)                  # the motor, forced twice
    assert 3 * 5 == 15 == math.lcm(3, 5)                   # the mesh
    phi15 = 2 ** 8 - 2 ** 7 + 2 ** 5 - 2 ** 4 + 2 ** 3 - 2 + 1
    assert phi15 == 151
    assert F(5, 2 ** phi15 - 1) == F(5, 2 ** 151 - 1)      # the sentence's object


def test_the_coverage_theorem_that_killed_catch_three():
    """Regime methodology, pinned so it is reusable: near m ~ 1.005 the grid
    {1 + 1/n} has spacing ~1/n^2 ~ 24 ppm, so EVERY value in the band sits
    within ~12 ppm of some banked-looking n. Total coverage = zero information.
    This is what killed the (205/204) x 2^-127 scan -- and it kills the whole
    class: a match to 1 + 1/n at n ~ 200 can never be evidence by itself."""
    for probe in (1.004879, 1.00463, 1.00512, 1.00548):    # arbitrary values
        best = min(abs(probe - (1 + 1 / n)) for n in range(150, 261))
        assert best < 15e-6                                # everything matches


def test_the_assault_null_only_the_deficit_force_rides_a_wheel():
    """Gained BY skeptic 2b of the assault on the sentence: if gravity alone is
    the deficit-force (part one), then gravity's coupling ALONE should admit a
    small-block wheel form x/(2^k - 1). Scan x <= 16, k <= 200 over the four
    couplings: alpha's best is 0.4% off, the proton's 0.5%, the muon's 0.4% --
    all dead; alpha_G(e) alone lands at ~106 ppm, with block FIVE at period
    151. The forbid PASSES. (Uses CODATA-18 inputs; alpha_G errors inherit
    G's 22 ppm, irrelevant at these scales.)"""
    G, hbar, c = 6.67430e-11, 1.054571817e-34, 299792458.0
    me, mp, mmu = 9.1093837015e-31, 1.67262192369e-27, 1.883531627e-28
    consts = {
        "alpha": 7.2973525693e-3,
        "aGe": G * me ** 2 / (hbar * c),
        "aGp": G * mp ** 2 / (hbar * c),
        "aGmu": G * mmu ** 2 / (hbar * c),
    }

    def best_wheel(Cv, bmax=16, kmax=200):
        best = None
        for k in range(2, kmax + 1):
            denom = 2 ** k - 1
            b = round(Cv * denom)
            if 1 <= b <= bmax:
                err = abs(b / denom / Cv - 1)
                if best is None or err < best[0]:
                    best = (err, b, k)
        return best

    err, b, k = best_wheel(consts["aGe"])
    assert (b, k) == (5, 151) and err < 2e-4              # gravity's: 106 ppm, PASS
    for name in ("alpha", "aGp", "aGmu"):
        err, b, k = best_wheel(consts[name])
        assert err > 2e-3                                  # everyone else: dead


def test_the_composite_gait_derived():
    """THE LAST WALL. The gait on composite depths is DERIVED, not chosen:
    LEG 1 (forced): every closure's all-ones factors into its divisor-depths'
    content -- 2^15-1 = Phi_3(2) x Phi_5(2) x Phi_15(2) = 7 x 31 x 151. The
    ancestors are already on the ledger (7 minted at depth 3, 31 at depth 5).
    LEG 2 (the corpus's own discipline): NO-RESEAT -- a closure cannot re-mint
    ancestral content (derive-once-then-append; one value, one address).
    LEG 3 (inductive from the chain's all-prime record 2, 3, 7, 127, 2^127-1):
    promotion mints ATOMIC (prime-period) wheels, so the promotable content is
    the closure's prime factors. ASSEMBLY: {7, 31, 151} minus the seated
    {7, 31} leaves the unique unseated prime 151 = Phi_15(2). On prime depths
    there are no proper ancestors, so residue = total: the two rules coincide
    on the chain's rungs BY DERIVATION. The residue is the physics -- the
    composite gait is section 9's manual path applied to the closure event.
    HONESTY: the mesh is GRACEFUL (Phi_15(2) prime, unintimate); depth 11
    would be ambiguous (Phi_11(2) = 23 x 89) and depth 18 intimate
    (Phi_18(2) = 57 = 3 x 19, a reseated three). Stated, pinned, not hidden."""
    def phi_at_2(n):
        def mob(m):
            r, d = 1, 2
            while d * d <= m:
                if m % d == 0:
                    m //= d
                    if m % d == 0:
                        return 0
                    r = -r
                d += 1
            return -r if m > 1 else r
        num = den = 1
        for d in range(1, n + 1):
            if n % d == 0:
                mu = mob(n // d)
                if mu == 1:
                    num *= 2 ** d - 1
                elif mu == -1:
                    den *= 2 ** d - 1
        return num // den

    # leg 1: the ledger at the mesh and the support depths
    assert 2 ** 15 - 1 == phi_at_2(3) * phi_at_2(5) * phi_at_2(15) == 7 * 31 * 151
    assert 2 ** 9 - 1 == phi_at_2(3) * phi_at_2(9) == 7 * 73
    assert 2 ** 10 - 1 == phi_at_2(2) * phi_at_2(5) * phi_at_2(10) == 3 * 31 * 11
    assert 2 ** 12 - 1 == (phi_at_2(2) * phi_at_2(3) * phi_at_2(4)
                           * phi_at_2(6) * phi_at_2(12)) == 3 * 7 * 5 * 3 * 13

    # the assembly: unique unseated prime at the mesh
    def is_prime(n):
        return n > 1 and all(n % d for d in range(2, int(n ** .5) + 1))
    promotable = {7, 31, 151}
    seated = {7, 31}                                       # depths 3 and 5
    residue = promotable - seated
    assert residue == {151} and is_prime(151)
    assert math.gcd(151, 7 * 31) == 1                      # unintimate: clean subtraction

    # prime depths reduce to the chain's own rule (no proper ancestors)
    for p in (3, 5, 7):
        assert phi_at_2(p) == 2 ** p - 1                   # residue = total on primes

    # the honesty checks, pinned
    assert phi_at_2(11) == 2047 == 23 * 89                 # ambiguous elsewhere
    assert phi_at_2(18) == 57 == 3 * 19 and 57 % 3 == 0    # intimate elsewhere


def test_atomicity_is_a_corollary_at_the_mesh():
    """The paper's strongest assumption, discharged where it is load-bearing.
    d | P exactly when (2^d - 1) | (2^P - 1): a wheel of period P RUNS every
    divisor wheel inside it, so no-reseat extends to components by arithmetic.
    The mesh's candidate periods are the divisors of 32767 beyond one; four
    contain the period-seven wheel (the master object), four the period-31
    wheel (the lift's own prescribed promotion); every candidate but 151
    contains a minted component. THE MESH PROMOTES 151 WITH NO ATOMICITY
    AXIOM — the prime period of the minted wheel is a corollary there. The
    general law matters only at depths with composite novel content (11 is
    the first) and carries no weight in the paper."""
    C = 2 ** 15 - 1
    divs = [d for d in range(2, C + 1) if C % d == 0]
    assert divs == [7, 31, 151, 217, 1057, 4681, 32767]

    for P in divs:                                   # containment is arithmetic
        for q in (d for d in range(2, P + 1) if P % d == 0):
            assert (2 ** P - 1) % (2 ** q - 1) == 0

    survivors = [P for P in divs if P % 7 != 0 and P % 31 != 0]
    assert survivors == [151]                        # unique unminted candidate
    assert C % (151 * 151) != 0                      # and no all-novel composite


def test_the_promotion_map_audit_retires_the_family():
    """Section 14 item 6, closed by its own audit. Small cyclotomic values at 2
    are DENSE in the program's characteristic numbers: fifteen of the
    twenty-three outputs through n = 24 land in a generously drawn favourites
    pool — a ~65% base rate against which six-for-six from a post-hoc input
    set is unremarkable. A fair pre-registered core set scores immediate
    misses at 21 (2359 = 7 x 337) and 24 (241), and the prettiest hit fails
    by the program's own doctrine: 73 lives in the SI numeral of c, whose
    native form 3 x 10^8 = 2^8 x 3 x 5^8 contains no 73. THE FAMILY IS
    RETIRED; the individual identities keep only the standing their own
    derivations give them."""
    def phi_at_2(n):
        def mob(m):
            r, d = 1, 2
            while d * d <= m:
                if m % d == 0:
                    m //= d
                    if m % d == 0:
                        return 0
                    r = -r
                d += 1
            return -r if m > 1 else r
        num = den = 1
        for d in range(1, n + 1):
            if n % d == 0:
                mu = mob(n // d)
                if mu == 1:
                    num *= 2 ** d - 1
                elif mu == -1:
                    den *= 2 ** d - 1
        return num // den

    vals = {n: phi_at_2(n) for n in range(2, 25)}
    faves = {3, 5, 7, 11, 13, 17, 19, 31, 43, 57, 73, 127, 151, 205, 241}
    assert sum(1 for v in vals.values() if v in faves) == 15   # 15 of 23: dense
    assert vals[21] == 2359 == 7 * 337                         # fair-set miss
    assert vals[24] == 241                                     # fair-set miss
    assert 300000000 == 2 ** 8 * 3 * 5 ** 8                    # native c: no 73
    assert 299792458 == 2 * 7 * 73 * 293339                    # the 73 is SI-historical


def test_the_fsc_wheel_carries_its_own_dress():
    """the author's rotation-count question, corrected and then confirmed richer than
    asked. The seal-separation is HALF THE PERIOD, wheel by wheel: three places
    on seven's wheel (period 6), four on 137's (period 8, banked in Units:
    137 divides 10^8 - 1). His totals stand by the digit-sum route, exact
    under Midy: seven's completion 999999 = block + negation-image = 27 + 27
    = 54; and THE FSC'S OWN WHEEL has block 00729927 with Midy halves
    0072 + 9927 = 9999, BLOCK DIGIT-SUM 36 -- the dress numeral of 137.036 --
    and completion digit-sum 72, the proton seat numeral. The banked anatomy
    alpha^-1 = 137 + 36/1000 carries as its dress the digit-sum of 137's own
    reptend block. Readings beyond the arithmetic are flagged, not built."""
    def ord10(p):
        o, x = 1, 10 % p
        while x != 1:
            x, o = (x * 10) % p, o + 1
        return o

    assert ord10(137) == 8
    block = str((10 ** 8 - 1) // 137).zfill(8)
    assert block == "00729927"
    assert int(block[:4]) + int(block[4:]) == 9999          # Midy halves
    assert all(int(block[i]) + int(block[(i + 4) % 8]) == 9 for i in range(8))
    assert sum(int(c) for c in block) == 36                 # the dress numeral
    assert 2 * 36 == 72                                     # the completion; the seat
    assert sum(int(c) for c in "142857") == 27              # seven's parallel
    assert 27 + 27 == 54                                    # the author's 54, by Midy
    assert 137 + 36 / 1000 == 137.036                       # the banked anatomy


def test_the_two_wheels_stand_a_fourth_apart():
    """the author's chain 24 x 54 = 1296, /72 = 18, 72/54 = 4/3 -- verified and reduced
    to a general law: for an even-period wheel the block digit-sum is 9e/2 and
    the completion sum is 9e (Midy, exact). So 54 = 9x6 and 72 = 9x8, and the
    ratio of the FSC wheel to the master wheel is their PERIOD ratio 8:6 = 4:3
    -- Fa, the lift interval, standing between the two wheels; descending,
    3/4 of the turn is 270 degrees, the intonated seat of the harmonic seventh
    (LIN(270) = 7/4, pinned elsewhere). 24 x 54 = 6^4 = 36^2 and 1296/72 = 18.
    DEFLATION KEPT VISIBLE: seventeen's wheel (e = 16) also block-sums to 72,
    so the 72-as-proton echo is numeral-level; the forced content is the law
    and the period ratio. The dress identity sharpens: 36 = 9 x 8/2 -- the FSC
    dress is half the nines of its own wheel's period."""
    def ord10(p):
        o, x = 1, 10 % p
        while x != 1:
            x, o = (x * 10) % p, o + 1
        return o

    for p in (7, 17, 19, 23, 137):
        e = ord10(p)
        s = sum(int(c) for c in str((10 ** e - 1) // p).zfill(e))
        assert e % 2 == 0 and s == 9 * e // 2              # the Midy sum law
    assert 9 * 6 == 54 and 9 * 8 == 72                     # the two completions
    assert 24 * 54 == 1296 == 6 ** 4 == 36 ** 2            # the author's product
    assert 1296 // 72 == 18                                # the triad sum
    from fractions import Fraction as F
    assert F(72, 54) == F(4, 3)                            # Fa between the wheels
    assert F(360 * 3, 4) == 270                            # 3/4 turn = 270 deg
    assert sum(int(c) for c in str((10 ** 16 - 1) // 17).zfill(16)) == 72  # the deflation


def test_the_99_101_companionship():
    """the author's years-old intuition -- 'the Midy 99 must have a companion at 101;
    I went looking but never came up with much empirical' -- RESOLVED 2026-08-09:
    the companion was always there, and it is structural.
    (1) THE LAW: 10^2h - 1 = (10^h - 1)(10^h + 1): every even wheel factors as
    closure x negation. 99 x 101 = 9999; 999 x 1001 = 999999 -- the MASTER
    WHEEL is the Midy 999 times its 1001 companion, and 1001 = 7 x 11 x 13
    carries the tether prime itself.
    (2) MIDY IS 101-FAMILY MEMBERSHIP: the digit-pair theorem for p IS the
    statement p | 10^(e/2) + 1 -- the prime lives in the negation modulus at
    half period. Residents: 1001 = 7x11x13; 10001 = 73 x 137 (the FSC prime,
    paired with 73); 10^8 + 1 = 17 x 5882353 (the spine prime's rung).
    (3) RECIPROCAL AND LITERAL: 1/99 = .010101... (99's body writes 101
    forever) and 1/101 = .00990099... (101's body writes 99 forever) -- each
    is the other's repeating block, because 99 x 101 = 9999.
    (4) THE CAST IN ONE LINE: 99999999 = 99 x 101 x 73 x 137 -- the FSC
    wheel's modulus is (the companion pair) x (137's own Midy pair).
    Corollary: EVERY face of the FSC wheel carries 101 as a prime factor,
    since block(k) = k x 729927 and 729927 = 9 x 11 x 73 x 101. (Master-wheel
    analogue: 142857 = 27 x 11 x 13 x 37 -- every face carries 1001's primes.)
    (5) HIS COLLAPSE LADDER 101 -> 11 -> 2 is the negation family descending
    its rungs 10^2+1, 10^1+1, 10^0+1. The negation family floors at TWO (the
    octave); the closure family floors at 10^0 - 1 = ZERO. And his aside
    checks: 70! has exactly 101 digits."""
    import math

    for h in (1, 2, 3, 4, 5):
        assert (10 ** h - 1) * (10 ** h + 1) == 10 ** (2 * h) - 1
    assert 99 * 101 == 9999
    assert 999 * 1001 == 999999                       # the master wheel splits
    assert 1001 == 7 * 11 * 13                        # the tether prime inside

    def ord10(p):
        o, x = 1, 10 % p
        while x != 1:
            x, o = (x * 10) % p, o + 1
        return o

    for p in (7, 17, 19, 23, 137):                    # Midy = membership
        e = ord10(p)
        assert e % 2 == 0 and (10 ** (e // 2) + 1) % p == 0
    assert 10 ** 4 + 1 == 73 * 137                    # the FSC resident
    assert 10 ** 8 + 1 == 17 * 5882353                # the spine resident

    assert 9999 // 101 == 99                          # 1/101's block is 0099
    assert 99 // 99 == 1                              # 1/99's block is 01
    assert 99999999 == 99 * 101 * 73 * 137            # the cast in one line
    assert (10 ** 8 - 1) // 137 == 729927 == 9 * 11 * 73 * 101
    assert (10 ** 6 - 1) // 7 == 142857 == 27 * 11 * 13 * 37

    assert [10 ** k + 1 for k in (2, 1, 0)] == [101, 11, 2]   # his collapse
    assert 10 ** 0 - 1 == 0                           # the two floors: 0 and 2
    assert len(str(math.factorial(70))) == 101        # his aside, exact


def test_the_mexican_hat_is_the_minus_ten_face_of_the_fsc_wheel():
    """the author's old page reads 127/137 = .92700729... as 'the most symmetrical
    form ... between two neutrals.' Verified and made exact: 92700729 is a
    PALINDROME, and the FSC wheel has exactly TWO palindromic faces, at
    residues +10 and -10 (rotations 1 and 5, half a period apart), carried
    onto each other by the Midy half-turn x10^4 = -1. The master wheel has
    NONE. And -10 mod 137 = 127 = 2^7 - 1, THE CATALAN-MERSENNE TOWER RUNG:
    his hat is the minus-ten face of the FSC wheel, and its numerator is the
    tower's fourth member, because 137 - 127 = 10 (FSC prime minus tower rung
    = the base). Midy runs straight through the symmetry he saw: 9270 + 0729
    = 9999, so the halves are reverse-complements -- reverse(x) = 9999 - x,
    the two central zeros seated between the two seals ('the two neutrals').
    His rounding transform {27->37, 72->73} lands on the wheel's own factor
    cast: 27 x 37 = 999 (the closure) and 73 x 137 = 10001 (the negation).
    And the number itself factors 92700729 = 127 x 9 x 11 x 73 x 101: the
    101 he conjectured is a PRIME FACTOR of the number on his own page."""
    block = str((10 ** 8 - 1) // 137).zfill(8)
    assert block == "00729927"
    rots = [block[i:] + block[:i] for i in range(8)]
    pals = [i for i, r in enumerate(rots) if r == r[::-1]]
    assert pals == [1, 5]                             # exactly two faces
    assert pow(10, 1, 137) == 10 and pow(10, 5, 137) == 127
    assert (10 + 127) % 137 == 0                      # they are +10 and -10
    assert pow(10, 4, 137) == 136                     # the Midy half-turn
    assert 127 == 2 ** 7 - 1 and 137 - 127 == 10      # the tower rung, -10
    assert rots[5] == "92700729" == str(127 * 729927) # his number exactly

    m = str((10 ** 6 - 1) // 7)
    assert not any((m[i:] + m[:i]) == (m[i:] + m[:i])[::-1] for i in range(6))

    assert 9270 + 729 == 9999                         # Midy through the hat
    assert int("9270"[::-1]) == 9999 - 9270           # reverse-complement
    assert 27 * 37 == 999 and 73 * 137 == 10001       # his rounded halves
    assert 92700729 == 127 * 9 * 11 * 73 * 101        # the 101 inside


def test_seven_and_thirteen_are_the_hexad_primes():
    """the author's thirteen-thread, grounded — and the grounding is exhaustive, not
    a search. A prime has decimal period exactly six iff it divides
    10^6 - 1 = 999999 = 3^3 x 7 x 11 x 13 x 37 without dividing any smaller
    10^k - 1; of those five primes, three fall away (3 has period one, 11
    two, 37 three), leaving EXACTLY SEVEN AND THIRTEEN. The hexad carries
    two primes and no others. They close for opposite reasons: seven closes
    because six is all it has — ten is a primitive root and the reptend is
    full — while thirteen closes at HALF its capacity, its group having
    order twelve. The full hexad and the half-turned one. Both are Midy:
    142 + 857 and 076 + 923 each make nines."""
    def ord10(n):
        k, v = 1, 10 % n
        while v != 1:
            v = (v * 10) % n
            k += 1
        return k
    assert 10 ** 6 - 1 == 999999 == 3 ** 3 * 7 * 11 * 13 * 37
    periods = {p: ord10(p) for p in (3, 7, 11, 13, 37)}
    assert periods == {3: 1, 7: 6, 11: 2, 13: 6, 37: 3}
    assert [p for p, k in periods.items() if k == 6] == [7, 13]
    assert ord10(7) == 7 - 1                              # full reptend
    assert ord10(13) == (13 - 1) // 2                     # half turn
    assert 142 + 857 == 999 and 76 + 923 == 999           # both Midy
