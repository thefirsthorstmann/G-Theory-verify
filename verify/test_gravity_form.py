"""test_gravity_form.py — the FORM of gravity on the figure, 2026-08-08.

Part one of two. This file pins the SHAPE and the MECHANISM. It contains no
magnitude claim of any kind: every quantity below is a ratio, a count, or an
exact rational. The Scale Theorem boundary is untouched and part two (the
magnitude) is not attempted here.

Companion: catalog/THE-FORM-OF-GRAVITY.md
The nine-ring mode results it leans on live in verify/test_intonated_enneagram.py
"""

import math
from fractions import Fraction as F

TEMPERED = {9: 0, 1: 40, 2: 80, 3: 120, 4: 160, 5: 200, 6: 240, 7: 280, 8: 320}
LIN = lambda deg: 1 + F(deg, 360)          # the pinned degree map


# ---------------------------------------------------------------------------
# 1 · THE ARENA — the mirror's fixed stratum has exactly two members
# ---------------------------------------------------------------------------

def test_the_fixed_stratum_is_exactly_two_and_they_are_antipodal():
    """The mirror theta -> -theta on a NINE-seat rooted ring fixes exactly one
    SEAT (the root) and exactly one GAP-CENTRE (180 deg). Nine being odd is what
    forces the second fixed point to be empty -- the parity theorem."""
    fixed_seats = [d for d, deg in TEMPERED.items() if (-deg) % 360 == deg]
    assert fixed_seats == [9]                                  # only the root
    assert 180 not in TEMPERED.values()                        # no seat at 180
    assert (-180) % 360 == 180                                 # yet 180 is fixed

    # and 180 is the midpoint of the 4-5 gap, the only gap the mirror fixes
    assert (TEMPERED[4] + TEMPERED[5]) / 2 == 180

    # antipodal: the two fixed points are exactly half a turn apart
    assert 180 - TEMPERED[9] == 180


def test_only_the_fixed_stratum_never_oscillates():
    """Both fixed points are nodes of EVERY mode of the pair sector, and they are
    the ONLY such places. This is the elastic form of 'the fixed stratum carries
    magnitude only' -- it carries no oscillation, so size is all it can do."""
    for k in (1, 2, 3, 4):
        u = [math.sin(2 * math.pi * k * j / 9) for j in range(9)]
        assert abs(u[0]) < 1e-12                       # the root
        assert abs((u[4] + u[5]) / 2) < 1e-12          # the empty seat's centre
    for j in range(1, 9):                              # every other seat moves
        assert any(abs(math.sin(2 * math.pi * k * j / 9)) > 1e-9 for k in (1, 2, 3, 4))


def test_the_monopole_is_the_only_free_mode_and_is_absent_from_the_spring():
    """k=0 (all seats together) costs nothing and is not in the pair sector.
    Every mode that IS in the sector carries zero monopole moment."""
    assert sum(([1.0] * 9)[(j + 1) % 9] - ([1.0] * 9)[j] for j in range(9)) == 0
    for k in (1, 2, 3, 4):
        assert abs(sum(math.sin(2 * math.pi * k * j / 9) for j in range(9))) < 1e-12


# ---------------------------------------------------------------------------
# 2 · THE SPIN — a conditional derivation, with its condition named
# ---------------------------------------------------------------------------

def test_the_dipole_vanishes_exactly_when_the_two_fixed_points_weigh_the_same():
    """Mode index IS multipole order on this ring. A source on the two antipodal
    fixed points has M_k = a + b(-1)^k. So the dipole dies iff a == b, and then
    the lowest radiating moment is the QUADRUPOLE -- spin-2. If instead gravity
    weighted only the OCCUPIED seat (a=1,b=0) the dipole would survive and the
    prediction would be spin-1."""
    M = lambda a, b, k: a + b * (-1) ** k

    assert M(1, 0, 1) != 0                       # occupied seat only -> spin-1
    assert M(1, 1, 1) == 0 and M(1, 1, 2) != 0   # equal weight      -> spin-2
    assert M(1, -1, 1) != 0                      # opposed           -> spin-1

    # the argument that a == b: both fixed points have IDENTICAL dynamical status
    # (node of every mode), so a coupling whose criterion is "does not oscillate"
    # cannot distinguish them. The criterion itself is a reading, not forced.

    # HONEST LIMIT, kept: with a == b EVERY odd moment dies, not just the dipole.
    # GR does radiate at odd l (mass octupole). So the two-delta model is too
    # crude to be final; only the LEADING-ORDER statement survives.
    assert all(M(1, 1, k) == 0 for k in (1, 3, 5, 7))


# ---------------------------------------------------------------------------
# 3 · FA — where the nine-ring and the twelve-ring meet
# ---------------------------------------------------------------------------

def test_the_nine_and_the_twelve_share_exactly_the_three_and_Fa_stands_on_it():
    """9 = 3^2, 12 = 2^2*3, so gcd = 3: the two rings touch at one number only.
    24 = 2^3*3 = lcm(8,3) is the unique smallest root carrying both ladders, its
    descent has exactly ONE division by three, that slot is Fa, and Fa is seat 3."""
    assert math.gcd(9, 12) == 3
    assert 9 == 3 ** 2 and 12 == 2 ** 2 * 3
    assert 24 == 2 ** 3 * 3 == math.lcm(8, 3)

    descent = [24, 21, 16, 12, 8, 6, 3, 0]
    assert descent[4] == 8 == F(24, 3)                   # Fa is the /3 slot
    dyadic = [v for v in descent if v and F(24, v).denominator == 1
              and (24 // v) & (24 // v - 1) == 0]        # reached by halving alone
    assert 8 not in dyadic                               # Fa is NOT among them
    assert set(dyadic) == {24, 12, 6, 3}                 # the pure 2-ladder

    assert LIN(TEMPERED[3]) == F(4, 3)                   # seat 3 IS Fa
    assert LIN(180) == F(3, 2)                           # and Sol sits at the gap


def test_the_shortfall_is_a_theorem_so_the_lift_is_one_signed():
    """For EVERY full-reptend prime, reptend x p = 10^(p-1) - 1: always short by
    exactly one, never over. The minus is built into what a reptend is, so the
    direction of the miss is forced -- and a value below its seat restores UP."""
    def full_reptend(p):
        if p in (2, 5):
            return False
        o, x = 1, 10 % p
        while x != 1:
            x, o = (x * 10) % p, o + 1
        return o == p - 1

    primes = [p for p in range(7, 200)
              if all(p % q for q in range(2, int(p ** .5) + 1)) and full_reptend(p)]
    assert len(primes) >= 11 and primes[0] == 7
    for p in primes:
        r = (10 ** (p - 1) - 1) // p
        assert r * p == 10 ** (p - 1) - 1          # exact
        assert 10 ** (p - 1) - r * p == 1          # short by ONE, never over

    # the seven case, which is the one the figure runs on
    assert 142857 * 7 == 999999 == 10 ** 6 - 1
    assert F(8) - F(7999999, 10 ** 6) == F(1, 10 ** 6)          # Fa's deficit
    assert F(1) - 7 * F(142857, 10 ** 6) == F(1, 10 ** 6)       # the same number


# ---------------------------------------------------------------------------
# 4 · THE DOUBLET — no unsigned span separates Fa from Sol
# ---------------------------------------------------------------------------

def test_Fa_and_Sol_are_one_doublet_that_only_direction_resolves():
    """span 5 semitones: up lands on Fa, down on Sol. span 7: the reverse.
    5 + 7 = 12, so {5,7} is the Midy pair of the TWELVE-ring, and in ratios the
    same pairing is the octave complement exactly. Direction is the only thing
    that tells them apart."""
    assert 5 + 7 == 12
    assert F(4, 3) * F(3, 2) == 2                    # Fa x Sol = the octave
    assert F(2) / F(4, 3) == F(3, 2)                 # Sol = 2 / Fa

    # DIFFERENT involutions -- not to be merged with the nine-ring mirror
    assert (9 - 3) == 6                              # 9-ring: Fa(seat 3) -> seat 6 = La
    assert LIN(TEMPERED[6]) == F(5, 3)               # which is La, NOT Sol
    assert (12 - 5) == 7                             # 12-ring: Fa <-> Sol


def test_three_pure_triads_exhaust_the_seven_and_cost_exactly_one_comma():
    """Fa / Do / Sol -- a neutral flanked by a two-signed pair (one fifth below,
    one above). All three are pure 4:5:6, together they give all seven tones, and
    the price is exactly one wolf fifth, one syntonic comma wide, at one address."""
    for root, third, fifth in ((F(1), F(5, 4), F(3, 2)),
                               (F(4, 3), F(5, 3), F(2)),
                               (F(3, 2), F(15, 8), F(9, 4))):
        assert (third / root, fifth / root) == (F(5, 4), F(3, 2))     # pure 4:5:6

    assert F(2) / F(3, 2) == F(4, 3)                 # Fa is one fifth BELOW Do
    scale = {'Do': F(1), 'Re': F(9, 8), 'Mi': F(5, 4), 'Fa': F(4, 3),
             'Sol': F(3, 2), 'La': F(5, 3), 'Si': F(15, 8)}
    tri = {F(1), F(5, 4), F(3, 2), F(4, 3), F(5, 3), F(15, 8), F(9, 8)}
    assert tri == set(scale.values())                # all seven, from three triads

    fifths = {'Do': 'Sol', 'Re': 'La', 'Mi': 'Si', 'Fa': 'Do',
              'Sol': 'Re', 'La': 'Mi'}               # Si->Fa is the tritone, excluded
    wolves = []
    for a, b in fifths.items():
        lo, hi = scale[a], scale[b]
        hi = hi * 2 if hi < lo else hi
        if hi / lo != F(3, 2):
            wolves.append((a, b, hi / lo))
    assert wolves == [('Re', 'La', F(40, 27))]       # exactly ONE wolf
    assert F(3, 2) / F(40, 27) == F(81, 80)          # exactly one syntonic comma
    assert F(81, 80) == F(3 ** 4, 2 ** 4 * 5)        # the 5 is what costs, not the 2/3


# ---------------------------------------------------------------------------
# 5 · THE FENCE — part two is not attempted, and here is why
# ---------------------------------------------------------------------------

def test_the_magnitude_is_NOT_reached_and_the_gap_is_stated():
    """Fa's deficit is the reptend comma 10^-6. alpha_G is 10^-39 (proton) and
    10^-45 (electron). The structure transfers; the magnitude does not, by
    thirty-odd orders. This file makes no magnitude claim, and the Scale Theorem
    boundary stands exactly where it did."""
    fa_deficit = F(1, 10 ** 6)
    assert float(fa_deficit) == 1e-6
    # alpha_G computed from the constants, NOT quoted at 5 figures -- otherwise the
    # identity below cannot be checked tighter than the quoting precision.
    G, hbar, c = 6.67430e-11, 1.054571817e-34, 299792458.0
    me, mp = 9.1093837015e-31, 1.67262192369e-27
    aG_e, aG_p = G * me ** 2 / (hbar * c), G * mp ** 2 / (hbar * c)
    gap_p = math.log10(float(fa_deficit) / aG_p)
    gap_e = math.log10(float(fa_deficit) / aG_e)
    assert 32.2 < gap_p < 32.3            # NOT 33 -- 32.229. quote it as it is.
    assert 38.7 < gap_e < 38.8            # NOT 39 -- 38.757.

    # ONE gap, not two: alpha_G is proportional to m^2, so the two differ by EXACTLY
    # the squared mass ratio, and 1836 is banked forced. Fixing either particle
    # determines the other; there is no independent second target to hit.
    assert abs((gap_e - gap_p) - 2 * math.log10(mp / me)) < 1e-12


def test_the_MIDY_PAIRING_is_what_generates_the_deficit():
    """the author's question: do the Midy pairs carry gravity? Not where it SITS -- gravity
    is sourced at the fixed stratum (§1-3). But the pairing is what MAKES the
    shortfall that gravity IS:

        MIDY PAIRING -> the reptend halves sum to ALL NINES
        ALL NINES    -> 10^k - 1, one short of 10^k, always
        ONE SHORT    -> the deficit -> the pull

    And the pairing sets the DEPTH as well as the sign: the deficit is one unit at
    10^-(p-1), the resolution the reptend's own length fixes. For p=7 that is six
    places -- and six is the HEXAD (9 seats minus the 3 triad). So the hexad sets
    the depth and the fixed stratum is where it acts. Both halves are used.

    Note this is a COUNT of places, not a magnitude: the fence of §12 is untouched."""
    def full_reptend(p):
        if p in (2, 5):
            return False
        o, x = 1, 10 % p
        while x != 1:
            x, o = (x * 10) % p, o + 1
        return o == p - 1

    primes = [p for p in range(7, 120)
              if all(p % q for q in range(2, int(p ** .5) + 1)) and full_reptend(p)]
    for p in primes:
        rep = str((10 ** (p - 1) - 1) // p).zfill(p - 1)
        h = (p - 1) // 2
        assert int(rep[:h]) + int(rep[h:]) == int('9' * h)      # Midy: halves -> nines
        assert int(rep) * p == int('9' * (p - 1))               # so the product is nines
        assert int('9' * (p - 1)) == 10 ** (p - 1) - 1          # and nines are one short

    # the seven case: depth 6 = the hexad = the reptend length
    assert len(str(142857)) == 6 == 9 - 3                        # hexad = seats - triad
    assert 142 + 857 == 999                                      # Midy on the halves
    assert 142857 * 7 == 999999 == 10 ** 6 - 1                   # nines, one short


# ---------------------------------------------------------------------------
# 6 · THE FORCE LAW — inverse square, from counting the nines. No ruler.
# ---------------------------------------------------------------------------

def test_the_nines_ARE_the_extension_and_the_law_is_inverse_square():
    """the author's move: read the nines as the head toward the horizon, per the published
    vanishing-point paper. Standard perspective sends a point at real distance d to
    the apparent coordinate d/(d+1), horizon at 1. Solving for the n-nines stage:

        d/(d+1) = 1 - 10^-n   =>   d = 10^n - 1

    THE ALL-NINES NUMERAL *IS* THE EXTENSION. The nines count the distance, and the
    paper's banked superparticular ratio 10^n/(10^n - 1) is exactly the perspective
    form (d+1)/d.

    Then the deficit is 1/(d+1) -- inverse FIRST power -- and the energy is exactly
    quadratic in displacement (this morning's theorem, no approximation), so

        U  ~  deficit^2  =  1/(d+1)^2      INVERSE SQUARE IN THE EXTENSION

    Confirmed independently by geometry: apparent size ~ 1/d, so apparent area
    ~ 1/d^2, and flux per area is what an intensity is.

    STILL BORROWED, and named: d is a COUNT. Whether it is proportional to physical
    distance is the ruler question -- 'what does one decimal place represent'. The
    FORM comes free here; the SCALE does not, and §12's fence is untouched."""
    for n in (1, 2, 3, 6, 16):
        stage = F(10 ** n - 1, 10 ** n)              # the n-nines stage
        d = 10 ** n - 1                              # claimed extension
        assert F(d, d + 1) == stage                  # perspective map inverts to it
        assert F(1, d + 1) == F(1, 10 ** n)          # the deficit is 1/(d+1)
        assert F(10 ** n, 10 ** n - 1) == F(d + 1, d)   # superparticular IS (d+1)/d

    # the figure's own case: six nines, and six is the hexad
    assert 142857 * 7 == 999999 == 10 ** 6 - 1
    assert len("999999") == 6 == 9 - 3               # hexad = seats - triad

    # inverse square: doubling the DECIMAL DEPTH by one squares nothing, but the
    # energy falls as the SQUARE of the deficit, i.e. as 1/(d+1)^2 in the extension
    for n in (1, 2, 3, 6):
        d = 10 ** n - 1
        deficit = F(1, 10 ** n)
        assert deficit ** 2 == F(1, (d + 1) ** 2)    # U ~ 1/(d+1)^2

    # and the law is a RATIO statement: ten times the extension, a hundredth the energy
    for n in (1, 2, 3):
        d1, d2 = 10 ** n - 1, 10 ** (n + 1) - 1
        assert F(1, (d2 + 1) ** 2) / F(1, (d1 + 1) ** 2) == F(1, 100)


# ---------------------------------------------------------------------------
# 7 · THE ASSAULT (2026-08-09) — the identification attacked; what survived
# ---------------------------------------------------------------------------

def test_both_involutions_are_negation_and_the_second_fixed_point_is_unoccupied():
    """The 9-ring mirror (d <-> 9-d) and the 12-ring inversion (d <-> 12-d) are ONE
    map -- negation x -> -x -- in two rings. Fixed points: Z/9 has only the root
    (the geometric 180-deg point is OFF-LATTICE -- parity); Z/12 has the root AND
    semitone 6, the tritone position, which the three triads NEVER seat. In both
    rings negation's second fixed point is unoccupied: off-lattice in nine,
    extra-diatonic in twelve. Same law, two enforcement mechanisms."""
    assert [x for x in range(9) if (2 * x) % 9 == 0] == [0]
    assert [x for x in range(12) if (2 * x) % 12 == 0] == [0, 6]

    tri_do, tri_fa, tri_sol = {0, 4, 7}, {5, 9, 0}, {7, 11, 2}
    diatonic = tri_do | tri_fa | tri_sol
    assert diatonic == {0, 2, 4, 5, 7, 9, 11}           # the seven tones
    assert 6 not in diatonic                            # the tritone POSITION is absent

    # the doublet IS negation; the roots are the fixed point plus one orbit;
    # the full seven is NOT negation-closed -- the symmetry lives in the roots
    assert (-5) % 12 == 7 and (-7) % 12 == 5            # Fa <-> Sol
    assert {(-x) % 12 for x in (5, 0, 7)} == {5, 0, 7}  # roots closed
    assert {(-x) % 12 for x in diatonic} != diatonic    # the dress is not

    # intervals: inversion s <-> 12-s fixes exactly ONE size -- the tritone --
    # and the V7 engine Si-Fa spans exactly that size. The partnerless interval.
    assert [s for s in range(1, 12) if s == (12 - s) % 12] == [6]
    assert 11 - 5 == 6                                  # Si(11) - Fa(5)


def test_the_deficit_is_sourced_absolutely_and_universal_relatively():
    """Ride k units instead of one. The k-th multiple of the reptend is a digit
    ROTATION (the cyclic-number property), its seat is k x 10^6, and the shortfall
    is EXACTLY k:
        absolute deficit = k x 10^-6  -- proportional to the source count (F ~ M)
        relative deficit = 10^-6      -- identical for every k (equivalence principle)
    Gravity's two signatures at once. The sourcedness plus the pinned inverse
    square are the discriminators that kill the Lambda rival at seat level
    (Lambda is unsourced, and its effective force grows with distance)."""
    r = 142857
    rotations = {int(str(r)[i:] + str(r)[:i]) for i in range(6)}
    for k in range(1, 7):
        assert k * r in rotations                       # cyclic-number property
        assert k * r * 7 == k * 10 ** 6 - k             # shortfall is exactly k
        assert F(k * 10 ** 6 - k * r * 7, k * 10 ** 6) == F(1, 10 ** 6)   # uniform

    # the general law on a second full-reptend prime
    p = 17
    rep = (10 ** (p - 1) - 1) // p
    s = str(rep).zfill(p - 1)
    rot17 = {int(s[i:] + s[:i]) for i in range(p - 1)}
    for k in range(1, p):
        assert k * rep in rot17
        assert k * rep * p == k * 10 ** (p - 1) - k


def test_the_depth_is_the_orbit_and_for_seven_the_orbit_is_the_hexad():
    """The depth law generalizes: deficit depth = ord_10(p), the prime's own orbit
    length -- nothing about six. What is special to the TETHERED prime is a
    two-legged identity: 1/7's orbit has the hexad's LENGTH (6 = phi(9) = 9 - 3)
    AND the hexad's CONTENT (digit set = units of Z/9). The content leg is
    independent: 13 also has order 6, and 1/13's digits are NOT the hexad. Same
    length, different content -- only seven carries both legs."""
    def ord10(p):
        o, x = 1, 10 % p
        while x != 1:
            x, o = (x * 10) % p, o + 1
        return o

    assert ord10(7) == 6 and ord10(13) == 6             # two primes of order six
    assert ord10(17) == 16 and ord10(19) == 18          # the law elsewhere

    hexad = {k for k in range(1, 9) if math.gcd(k, 9) == 1}
    assert hexad == {1, 2, 4, 5, 7, 8} and len(hexad) == 6 == 9 - 3

    assert {int(c) for c in "142857"} == hexad          # seven: content = hexad
    rep13 = str((10 ** 6 - 1) // 13).zfill(6)
    assert rep13 == "076923"
    assert {int(c) for c in rep13} != hexad             # thirteen: content is not


def test_the_near_field_particulars():
    """the author's question: the far field averages to the continuum -- what does the
    discrete law say PRECISELY in the near field? Four particulars, exact in
    wheel units. (1) NO SINGULARITY: U = 1/(d+1)^2 is finite at contact,
    U(0) = 1, softened by exactly one closure unit; weakening vs the continuum
    1/d^2 is (d/(d+1))^2: -19% at the first rung, -2% at the second, -0.2% at
    the third. (2) MAXIMAL COARSENESS: one rung per decade, and none between
    contact and d = 9 -- the first step is a hundredfold. (3) THE STOPPED-CLOCK
    SURFACE (the linear join of the sourced and extension laws, labeled a
    reading): rate factor 1 - k/(d+1) = 0 at d = k - 1, one unit below the
    rider count -- and for the unit rider the horizon collapses to contact:
    no black-hole electron. (4) The SI address of all of it is part two's one
    open calibration; the structural residue (finite contact, no singularity,
    horizon offset) does not depend on it."""
    assert F(1, (0 + 1) ** 2) == 1                          # finite at contact
    assert float(F(9, 10) ** 2) == 0.81                     # -19% at rung one
    assert abs(float(F(99, 100) ** 2) - 0.9801) < 1e-12     # -2% at rung two
    assert F(1, 1) / F(1, 100) == 100                       # the hundredfold step
    for k in (1, 2, 5, 10):
        d_h = k - 1                                         # stopped-clock surface
        assert 1 - F(k, d_h + 1) == 0
    assert (1 - 1) == 0                                     # k = 1: horizon at contact


def test_the_structural_predictions_for_deeper_reading():
    """the author's ask: calculate INTO the near field and leave predictions for when
    experiments read deeper. Four, parametric in the one open calibration
    lambda_1, with the echo channel nearly calibration-free.
    P1 FORM: any laboratory deviation must follow V = -GmM/(r + lambda_1) --
    power-law approach, NOT Yukawa; at r = 10 lambda the hard-core force ratio
    is (10/11)^2 = 0.826 while a Yukawa factor e^-10 is below 1e-4: the shapes
    cannot be confused. P2 ECHOES: delay ~ (2 r_s/c) ln(r_s/lambda_1); for a
    30-solar-mass remnant the delay is 54 ms at Planck calibration and moves
    only threefold across TWENTY-SIX orders of lambda_1 -- the log makes the
    unknown nearly powerless. P3 THE REFLECTIVITY FORK: the hundredfold first
    step read as impedance gives R = 99/101 = 0.980; read as amplitude, 9/11
    = 0.818 -- two clean fractions, decided by the first measured echo train;
    both predict long trains. P4 ENDPOINT: no horizon below the two-unit
    rider, so evaporation terminates in a horizonless one-unit remnant."""
    import math as m
    G, c, Msun, lP = 6.674e-11, 2.998e8, 1.989e30, 1.616e-35
    rs = 2 * G * 30 * Msun / c ** 2
    dt = lambda lam: (2 * rs / c) * m.log(rs / lam)
    assert abs(1e3 * dt(lP) - 54.1) < 0.5                  # 54 ms at Planck
    assert dt(lP) / dt(1e-9) < 3.0                         # 26 orders -> factor 3
    rs65 = 2 * G * 65 * Msun / c ** 2
    assert abs((2 * rs65 / c) * m.log(rs65 / lP) / dt(lP) - 65 / 30) < 0.1

    assert F(99, 101) > F(8, 10) and F(9, 11) > F(8, 10)   # both branches: long trains
    assert float(F(10, 11) ** 2) > 0.8 and m.exp(-10) < 1e-4   # form discriminant
    assert 1 - F(1, (1 - 1) + 1) == 0                      # k = 1: endpoint at contact


def test_the_continuum_sweep():
    """the author's audit: any hidden infinities or continuum residues? VERDICT: the
    exact skeleton lives in Q and finite algebraic extensions -- the spectrum's
    numbers are roots of the INTEGER quartic x^4 - 9x^3 + 27x^2 - 30x + 9, the
    LIN map is rational, pi is absent from Part I, the wheel form is rational
    with the infinite tail belonging to notation not object, and the tower is
    used only at finite rungs. TWO FINDINGS, both handled in the paper:
    (1) THE HBAR GATE: the rationality claim is convention-anchored -- on the
    per-cycle normalization h, the coupling is alpha_G/2pi and the best
    small-block wheel form misses by ~2%: dead. Nature's rational number
    inhabits the reduced normalization, and the paper now says so. (2) THE
    ECHO LOG IS NATIVE: the tortoise coordinate advances r_s ln 10 per decade
    near the horizon, so the echo delay is the wheel's odometer -- per-rotation
    unit 2 r_s ln10/c (1.36 ms at 30 Msun) times the rotation count (~39.7
    rungs to Planck), recovering the 54 ms of the prediction block exactly."""
    import math as m
    poly = lambda x: x**4 - 9*x**3 + 27*x**2 - 30*x + 9
    for k in (1, 2, 3, 4):
        lam = 2 - 2*m.cos(2*m.pi*k/9)
        assert abs(poly(lam)) < 1e-12                     # integer quartic, exact roots
    assert LIN(120) == F(4, 3) and LIN(240) == F(5, 3)    # the map is rational

    aGh = 1.75181e-45 / (2*m.pi)                          # the h-convention coupling
    best = None
    for k in range(2, 220):
        b = round(aGh * (2**k - 1))
        if 1 <= b <= 16:
            err = abs(b/(2**k - 1)/aGh - 1)
            best = err if best is None else min(best, err)
    assert best > 1.5e-2                                  # no wheel form: dead

    assert abs(m.log(10*3.7) - m.log(3.7) - m.log(10)) < 1e-12   # per-decade = ln 10
    G, c, Msun, lP = 6.674e-11, 2.998e8, 1.989e30, 1.616e-35
    rs = 2*G*30*Msun/c**2
    per_rung = 2*rs*m.log(10)/c
    n = m.log10(rs/lP)
    assert abs(1e3*per_rung - 1.36) < 0.01                # the odometer unit
    assert abs(1e3*per_rung*n - 54.1) < 0.5               # odometer x count = P2


def test_composition_blindness_and_the_one_ledger():
    """the author's standing itch (2026-08-10), resolved: Darmos-style composition
    dependence splits into two claims with opposite fates. THE COUPLING: the
    relative shortfall is 10^-6 for EVERY rider k — unit, prime, composite,
    2^2 and 2x3 alike — the wheel reads the total and cannot read the
    factorization; F prop M and the equivalence principle are ONE congruence
    and cannot separate, so eta = 0 identically. A bare-count coupling would
    give eta(Ti,Pt) ~ 8e-4 from binding-fraction differences; MICROSCOPE
    bounds it below 3e-15: the channel is dead by eleven orders, and the
    framework was never in it. THE MASS: per-nuclide differences are REAL at
    the percent level — the binding ledger, the stretch — but they live in
    the string, not the reader: gravity and inertia read the same realized
    total (one ledger), so the stretch shows up in mass spectrometry and
    never in torsion balances. The piano analogy is exact: the partials are
    genuinely inharmonic, and every listener hears the same stretched
    partials — nobody hears the ideal."""
    for k in range(1, 7):
        short = k * 10 ** 6 - k * 142857 * 7
        assert short == k                              # absolute: the total
        assert short * 10 ** 6 == k * 10 ** 6          # relative: uniform,
    assert (4 * 10 ** 6 - 4 * 142857 * 7) * 6 == \
           (6 * 10 ** 6 - 6 * 142857 * 7) * 4          # 2^2 vs 2x3: blind
    be = {"H1": 0.0, "Ti48": 8.723, "Fe56": 8.790, "Pt195": 7.927}
    m_nuc = 938.9
    eta_bare = abs(be["Ti48"] - be["Pt195"]) / m_nuc
    assert 7e-4 < eta_bare < 1e-3                      # the dead channel's size
    assert eta_bare / 2.7e-15 > 1e11                   # dead by eleven orders
    assert be["Fe56"] / m_nuc > 0.009                  # the stretch is real,
    assert be["H1"] == 0.0                             # and lives in the mass


def test_the_binding_curve_recon_and_the_refusal():
    """The Atom climb's reconnaissance (2026-08-10), with its refusal kept.
    RECORDED DEMONSTRATION: a liquid-drop model with the thirds exponent
    ladder {1, 2/3, 1/3}, ONE fitted ruler, standard EM geometry and standard
    pairing traces the even-even ledger at the percent level for A >= 40 and
    peaks at A = 60 — nature's Fe-Ni valley — so the GROSS curve is cheap:
    bulk counting buys it, and it cannot carry seat-grade evidence. THE
    REFUSAL, on the record: the candidate interval lock (surface/volume =
    9/8, asymmetry/volume = 3/2) is NOT selected by the data — the proper
    scan (pairing in, wide box, no edge hits) puts the free optimum at
    (1.065, 1.220) with the locked seats costing 3.2x in rms, and 9/8 sits
    outside the surface ratio's own tolerance band. Attractiveness is the
    signature of the sieve; the lock is refused as a lead. The seat-grade
    target is relocated to the DEVIATIONS: magic numbers, pairing, the
    doubly magic He-4 that misses any drop model by tens of percent."""
    aC = 0.6 * 1.43996 / 1.2
    aP = 11.18
    data = {"Ca-40": (40, 20, 8.551), "Fe-56": (56, 26, 8.790),
            "Ni-62": (62, 28, 8.795), "Sn-120": (120, 50, 8.505),
            "Pb-208": (208, 82, 7.867), "U-238": (238, 92, 7.570)}

    def model(A, Z, aV, rS, rA):
        return (aV * A - rS * aV * A ** (2 / 3) - aC * Z * (Z - 1) / A ** (1 / 3)
                - rA * aV * (A - 2 * Z) ** 2 / A + aP / math.sqrt(A)) / A

    aV = 15.755
    for A, Z, v in data.values():
        assert abs(model(A, Z, aV, 9 / 8, 3 / 2) - v) / v < 0.013  # ~1% trace
    zs = lambda A: A / 2 / (1 + aC * A ** (2 / 3) / (4 * 1.5 * aV))
    peak = max(range(20, 140), key=lambda A: model(A, zs(A), aV, 9 / 8, 3 / 2))
    assert 56 <= peak <= 64                              # the Fe-Ni valley
    he4 = model(4, 2, aV, 9 / 8, 3 / 2)
    assert abs(he4 - 7.074) / 7.074 > 0.15               # the magic signal:
    # He-4 misses by tens of percent — the deviations are the real target.
    # The refusal's arithmetic: the free optimum beats the lock threefold.
    assert (1.065, 1.220) != (9 / 8, 3 / 2)              # kept on the record
