"""test_the_color_wheel.py — THE MIXING WHEEL OF COLOR AS THE ARITHMETIC OF
ONE SEVENTH (2026-08-25). CC's recall, reconstructed and verified cold the
same morning: ".999999 being the white ray, the 7ths the six primary and
secondaries, .000001 being black."

THE STRUCTURE, all exact: the six sevenths are the six rotations of 142857,
and multiplication by ten arranges them in a circle (the orbit 1→3→2→6→4→5).
On that circle the antipode of k/7 is (7−k)/7 — because 10³ ≡ −1 (mod 7),
the half turn IS negation, which is Midy's theorem — and every antipodal
pair of blocks sums to 999999: complementary pairs summing to white.
Alternate positions split the six into the quadratic residues {1,2,4} (sum
7, one whole — the additive triad's seat) and the non-residues {3,5,6} (sum
14, two wholes — the subtractive triad's), two interleaved triangles with
every complement crossing between them (−1 is a non-residue of 7). White +
black = 0.999999 + 0.000001 = 1 exactly; the poles stand off the wheel; and
black is the same unit shortfall the gravitational volume reads as the
deficit. The hue IDENTIFICATION is an interpretation with declared freedom
(rotation/reflection) and pins nothing; this battery pins the arithmetic.
"""

import pathlib
from fractions import Fraction as F

CATALOG = pathlib.Path(__file__).resolve().parent.parent / "catalog"
DOC = (CATALOG / "VISIBLE-LIGHT-ON-DISCRETE-TERMS.md").read_text()
FLAT = " ".join(DOC.split())

BLOCK = {k: (10 ** 6 * k) // 7 for k in range(1, 7)}
WHEEL = [pow(10, n, 7) for n in range(6)]              # 1, 3, 2, 6, 4, 5


def test_the_six_sevenths_are_the_six_rotations_of_one_block():
    digits = "142857142857"
    starts = {k: str(BLOCK[k]).zfill(6) for k in range(1, 7)}
    assert all(starts[k] in digits for k in range(1, 7))
    assert len(set(starts.values())) == 6              # all six rotations occur


def test_the_wheel_is_the_orbit_of_ten():
    assert WHEEL == [1, 3, 2, 6, 4, 5]
    assert sorted(WHEEL) == [1, 2, 3, 4, 5, 6]         # the full orbit, no repeats


def test_the_half_turn_is_negation_and_the_pairs_sum_to_white():
    assert pow(10, 3, 7) == 7 - 1                      # 10^3 = -1 (mod 7): Midy
    for i in range(3):
        a, b = WHEEL[i], WHEEL[i + 3]
        assert a + b == 7                              # antipode = complement to one
        assert BLOCK[a] + BLOCK[b] == 999999           # each pair sums to white


def test_the_triads_are_the_residue_subgroup_and_its_coset():
    even, odd = set(WHEEL[0::2]), set(WHEEL[1::2])
    qrs = {(x * x) % 7 for x in range(1, 7)}
    assert even == qrs == {1, 2, 4}
    assert odd == {3, 5, 6}
    assert sum(even) == 7 and sum(odd) == 14           # one whole against two
    assert pow(100, 1, 7) == 2                         # even steps: the orbit of 2


def test_every_complement_crosses_between_the_triads():
    qrs = {1, 2, 4}
    for k in qrs:
        assert (7 - k) not in qrs                      # -1 is a non-residue of 7


def test_white_plus_black_is_exactly_one():
    assert F(999999, 10 ** 6) + F(1, 10 ** 6) == 1
    assert sum(BLOCK.values()) == 3 * 999999           # the palette: three whites
    assert sum(F(k, 7) for k in range(1, 7)) == 3


def test_the_mixing_calculus_closes_on_both_poles():
    """White by addition, black by subtraction — both exact."""
    assert sum(F(k, 7) for k in (1, 2, 4)) == 1        # the additive triad: white
    assert BLOCK[1] + BLOCK[2] + BLOCK[4] == 999999    # and its displayed window
    for pig, light in ((3, 4), (5, 2), (6, 1)):
        assert F(pig, 7) == 1 - F(light, 7)            # each pigment = 1 - a light
    assert sum(F(k, 7) for k in (3, 5, 6)) == 2        # joint absorption removes 1:
    assert 3 - sum(F(k, 7) for k in (3, 5, 6)) == 1    # of three whites, one remains
                                                       # removed entire — black
    assert sum(F(k, 7) for k in (1, 2, 4)) != sum(F(k, 7) for k in (3, 5, 6))
    # only the residue triad sums to unity: the additive office is not assignable
    # §6, Theorems 3-4 (2026-08-25): the pairwise laws, exact
    from itertools import combinations
    triad = (1, 2, 4)
    for i, j in combinations(triad, 2):
        k = next(x for x in triad if x not in (i, j))
        assert F(i, 7) + F(j, 7) == 1 - F(k, 7)        # two lights -> opposite pigment
        assert 1 - F(i, 7) - F(j, 7) == F(k, 7)        # two pigments -> third light
    # §6, Theorem 5: the orbit places each secondary between its two parents
    wheel = [pow(10, n, 7) for n in range(6)]          # 1, 3, 2, 6, 4, 5
    for idx, v in enumerate(wheel):
        if v in (3, 6, 5):                             # the secondaries
            left, right = wheel[idx - 1], wheel[(idx + 1) % 6]
            assert left + right == v or left + right == v + 7
            assert {left, right} <= {1, 2, 4}          # both neighbors are primaries
    # the anchored wheel reads R, Y, G, C, B, M in orbit order
    names = {1: "R", 3: "Y", 2: "G", 6: "C", 4: "B", 5: "M"}
    assert "".join(names[v] for v in wheel) == "RYGCBM"


def test_the_paper_states_the_theorems_and_labels_the_reading():
    assert "10³ ≡ −1 (mod 7)" in FLAT
    assert "the half turn is negation" in FLAT.lower()
    assert "999999" in FLAT and "0.999999 + 0.000001 = 1" in FLAT
    assert "quadratic residues" in FLAT
    assert "an interpretation" in FLAT                 # the reading typed at the statement
    assert "rotation and reflection within each office" in FLAT   # the freedom, located
    assert "only the naming" in FLAT                   # relations exact, names conventional
    assert "None is claimed here" in FLAT              # no constraint overclaimed
    # CC's sharpening (2026-08-25): not diagram-resemblance — one factorization,
    # two realizations, with the polarity and triad offices matched
    assert "the two sixes factor identically, with matched offices" in FLAT
    assert "one factorization in two realizations" in FLAT
    # the two relation sections (2026-08-25): the field and the quantum
    assert "each is derived where it is derived" in FLAT      # no borrowed authority
    assert "photon has a frequency and no hue" in FLAT
    assert "metamerism" in FLAT
    assert "the quotient the count creates" in FLAT           # where the calculus computes
    assert "Why the count has three channels is not derived" in FLAT   # the freedom stated
    # CC's two notes (2026-08-25): the Newton stance made plain; the continuum comparison scoped
    assert "an artificial count" in FLAT               # Newton's seven, called plainly
    assert "the mixing wheel's six" in FLAT and "not the spectrum's seven" in FLAT
    assert "nothing measured, nothing rounded" in FLAT
    assert "the two routes agree term for term" in FLAT   # no rivalry claimed
    assert "empirical regularity" in FLAT and "arithmetic necessity" in FLAT
    # violet as the unseated seventh (CC, 2026-08-25) — a signpost with exact anchor
    seats = {24, 27, 30, 32, 36, 40, 45, 48}
    place = 7 * 48 // 4 // 2                            # 7/4 on the lattice of 24
    assert place == 42 and place not in seats and 40 < place < 45
    assert "its place is 42, between the submediant at 40 and the leading tone at 45" in FLAT
    assert "recorded as a signpost and nothing more" in FLAT
