"""test_tonal_function.py — the exact skeleton of Tonal Function on Discrete Terms.

The fourth paper's spine: the seat table (inherited), the unique-root theorem
(function requires a trivial transpositional stabilizer), the two joints, the
dominant/subdominant mirror, the over/undertone mirror triads, the dominant
seventh's resolution spending one 3 and one 2, and the fifth-below/fourth-above
identity. Every claim in the paper that is arithmetic lives here; the perceptual
and physical readings are labeled in the paper and carry no pin.
"""
from fractions import Fraction as F

DIATONIC = frozenset({0, 2, 4, 5, 7, 9, 11})      # the major set on root 0
PENTATONIC = frozenset({0, 2, 4, 7, 9})
WHOLE_TONE = frozenset({0, 2, 4, 6, 8, 10})
OCTATONIC = frozenset({0, 1, 3, 4, 6, 7, 9, 10})  # half–whole on 0
CHROMATIC = frozenset(range(12))


def stabilizer(s):
    """Transpositions t with s + t = s (mod 12)."""
    return {t for t in range(12) if {(x + t) % 12 for x in s} == set(s)}


def test_the_seat_table_inherited():
    """The intonated layout, banked: descending ratio × 360° = the seat's
    degree; the 24-octave carries the ascending frequencies. Do 24 @ 0°,
    Re 27 @ 45°, Mi 30 @ 90°, Fa 32 @ 120°, Sol 36 @ 180°, La 40 @ 240°,
    Si 45 @ 315°, Do 48 @ 360°."""
    seats = {  # name: (ascending frequency on 24, descending ratio)
        "Do": (24, F(0)), "Re": (27, F(1, 8)), "Mi": (30, F(1, 4)),
        "Fa": (32, F(1, 3)), "Sol": (36, F(1, 2)), "La": (40, F(2, 3)),
        "Si": (45, F(7, 8)), "Do'": (48, F(1)),
    }
    angles = {"Do": 0, "Re": 45, "Mi": 90, "Fa": 120, "Sol": 180,
              "La": 240, "Si": 315, "Do'": 360}
    for name, (freq, ratio) in seats.items():
        assert ratio * 360 == angles[name]
    assert seats["La"][1] == 1 / F(3, 2)          # La = the fifth reversed
    assert F(seats["Fa"][0], 24) == F(4, 3)       # the lift interval
    assert F(seats["Sol"][0], 24) == F(3, 2)


def test_the_unique_root_theorem():
    """FUNCTION REQUIRES A TRIVIAL TRANSPOSITIONAL STABILIZER. A set fixed by
    a nonzero transposition cannot name a unique tonic: every candidate root
    has stabilizer-many indistinguishable rivals. The diatonic and pentatonic
    stabilizers are trivial — a unique root is nameable. The whole-tone,
    octatonic and chromatic sets are scales of limited transposition — the
    root is 6-, 4- and 12-fold ambiguous respectively, and tonal function is
    forbidden ON THE SET'S OWN ARITHMETIC. The practice matches: whole-tone
    and octatonic are the canonical 'floating' scales, and the full chromatic
    is atonality's home — but the practice is corroboration, not the theorem."""
    assert stabilizer(DIATONIC) == {0}
    assert stabilizer(PENTATONIC) == {0}
    assert stabilizer(WHOLE_TONE) == {0, 2, 4, 6, 8, 10}
    assert stabilizer(OCTATONIC) == {0, 3, 6, 9}
    assert stabilizer(CHROMATIC) == set(range(12))
    # the ambiguity count is the stabilizer's order:
    assert len(stabilizer(WHOLE_TONE)) == 6
    assert len(stabilizer(OCTATONIC)) == 4


def test_the_two_joints_carry_the_function():
    """The diatonic step word is 2 2 1 2 2 2 1: exactly two semitone joints,
    and they sit at Mi–Fa and Si–Do — the lift's seat and the leading tone's.
    The whole-tone word 2 2 2 2 2 2 has none: nothing leads, nothing leans.
    Function lives at the joints, and only the asymmetric floor has any."""
    di = sorted(DIATONIC)
    steps = [(b - a) % 12 for a, b in zip(di, di[1:] + [di[0] + 12])]
    assert steps == [2, 2, 1, 2, 2, 2, 1]
    joints = [di[i] for i, s in enumerate(steps) if s == 1]
    assert joints == [4, 11]                       # Mi–Fa and Si–Do
    wt = sorted(WHOLE_TONE)
    assert [(b - a) % 12 for a, b in zip(wt, wt[1:] + [wt[0] + 12])] == [2] * 6


def test_the_fixed_points_and_the_empty_seat():
    """Negation on the 12-ring fixes exactly {0, 6}: the root and the tritone.
    The diatonic set OCCUPIES 0 and omits 6 — the occupied and the empty fixed
    point, the banked pair (the never-seated tritone; the fixed stratum the
    gravity companion reads). The dominant seventh {Sol, Si, Re, Fa} contains
    the interval 6 — Si to Fa spans the ring's diameter through the empty
    seat — without any note sitting on it: dominant function is the chord that
    activates the empty fixed point."""
    fixed = {x for x in range(12) if (-x) % 12 == x}
    assert fixed == {0, 6}
    assert 0 in DIATONIC and 6 not in DIATONIC
    dominant7 = {7, 11, 2, 5}                      # Sol Si Re Fa
    assert dominant7 <= DIATONIC
    assert (11 - 5) % 12 == 6                      # the tritone inside it
    assert 6 not in dominant7                      # spanned, never seated
    assert F(45, 32).numerator == 45               # the JI tritone address,
    assert F(4, 3) < F(45, 32) < F(3, 2)           # between Fa and Sol


def test_the_resolution_spends_a_three_and_a_two():
    """THE CADENTIAL ARITHMETIC, exact on the 24-lattice: the dominant
    seventh's tritone is Si 45 against Fa 32 (the ratio 45/32, the
    never-seated address). It resolves by contrary motion, both voices moving
    the just semitone 16/15: Si 45 → Do 48 and Fa 32 → Mi 30. The lattice
    units spent are +3 and −2 — THE TWO GENERATORS, one of each, in opposite
    directions. The strongest progression in tonal music is the arithmetic's
    own pair enacted."""
    assert F(48, 45) == F(16, 15)                  # Si rises a just semitone
    assert F(32, 30) == F(16, 15)                  # Fa falls a just semitone
    assert 48 - 45 == 3                            # the 3, spent upward
    assert 32 - 30 == 2                            # the 2, spent downward
    assert F(45, 32) * F(16, 15) ** 2 == F(8, 5)   # the tritone opened by the
    assert F(48, 30) == F(8, 5)                    # two semitones = Mi–Do, 8/5


def test_the_mirror_exchanges_dominant_and_subdominant():
    """The reflection x ↦ 7 − x (the axis through the Do–Sol diameter's
    midpoint) maps the major set onto the parallel natural-minor set and
    carries the dominant seventh {Sol,Si,Re,Fa} to {Do,Le,Fa,Re} — the
    subdominant minor sixth chord. Dominant and subdominant are one object
    seen in the mirror; authentic and plagal are the two directions of one
    move. The relative behaviour of the functions is reflection arithmetic,
    not convention."""
    minor = {(7 - x) % 12 for x in DIATONIC}
    assert minor == {0, 2, 3, 5, 7, 8, 10}         # C natural minor
    image = {(7 - x) % 12 for x in {7, 11, 2, 5}}
    assert image == {0, 8, 5, 2}                   # Fa–Le–Do–Re: Fm6 on the
    assert {5, 8, 0} <= image                      # subdominant-minor triad


def test_the_over_and_under_triads_are_the_mirror_pair():
    """The overtone triad of Do 24 — partials 2, 3, 5, octave-reduced — is
    Do–Sol–Mi, the major chord: the dominant side. The undertone triad —
    divisors 2, 3, 5, octave-raised — is Do–Fa–Le, the minor subdominant: the
    plagal side. One recipe, run up and run down: the mirror of the previous
    test heard as physics. Major/minor duality is the over/under mirror."""
    def octave_into(x, lo=F(24)):
        while x < lo:
            x *= 2
        while x >= 2 * lo:
            x /= 2
        return x / lo

    over = sorted(octave_into(F(24) * k) for k in (2, 3, 5))
    assert over == [F(1), F(5, 4), F(3, 2)]        # Do, Mi, Sol — major
    under = sorted(octave_into(F(24) / k) for k in (2, 3, 5))
    assert under == [F(1), F(4, 3), F(8, 5)]       # Do, Fa, Le — minor subd.
    assert F(4, 3) == 2 / F(3, 2) and F(8, 5) == 2 / F(5, 4)  # exact mirrors


def test_the_fifth_below_is_the_fourth_above():
    """the author's superposition, exact: the descending fifth from the upper Do lands
    on Fa's own number — 48 × 2/3 = 32 = 24 × 4/3. Descending Sol IS ascending
    Fa as a seat; the subdominant is the dominant heard from the octave above.
    And La the same way: 48 × 5/6 = 40 = 24 × 5/3 — the relative minor's root
    is the fifth's reversal 2/3 placed on the seat ladder at 240°."""
    assert F(48) * F(2, 3) == 32 == F(24) * F(4, 3)
    assert F(48) * F(5, 6) == 40 == F(24) * F(5, 3)
    assert F(2, 3) * 360 == 240                    # La's seat, the reversal


def test_the_two_wheels_stand_in_functional_relation():
    """Cross-pin (full statement in test_decimal_wheel): the master wheel's
    period is 6, the FSC wheel's is 8; the Midy completions are 54 and 72;
    their ratio is 4/3 — the two wheels of the program stand a FOURTH apart,
    the lift interval, the subdominant relation. The papers' two engines are
    themselves a functional pair."""
    def ord10(p):
        o, x = 1, 10 % p
        while x != 1:
            x, o = (x * 10) % p, o + 1
        return o
    assert ord10(7) == 6 and ord10(137) == 8
    assert F(9 * 8, 9 * 6) == F(4, 3)
