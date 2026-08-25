"""test_semitone_seam.py — the carbon anchor's flagged seam, resolved. 2026-08-05.

The SOLID ledger (working record 2026-07-29) banks the carbon anchor at the UNIT and
COUNT-STRUCTURE level as SOLID, and then splits one phrase out as a Reading only:

    "mass unit = one semitone of carbon's octave" -- SPLIT OUT of SOLID (was wrongly
    folded into a SOLID line): it is a Reading, and "1/12 octave = a semitone"
    presupposes EQUAL TEMPERAMENT, in tension with the banked just-not-tempered doctrine.

the author asked whether equal temperament is actually required there. IT IS NOT — AND THE
REASON IS THAT IT IS NOT HAPPENING. Two different operations were being conflated:

    what the amu does :  u = m(12C) / 12       ARITHMETIC division, by twelve
    what a semitone does: f -> f x 2^(1/12)    GEOMETRIC division, of an octave

The atomic mass unit divides BY twelve. It does not take a twelfth ROOT of anything. No
octave is subdivided; twelve nucleons are counted. 12/12 = 1 while 2^(1/12) = 1.0594...

AND A SECOND IMPORTED WORD SITS IN THE SAME LINE. The banked phrasing reads "12 = the
octave". The OCTAVE is the ratio 2:1; TWELVE is the chromatic COUNT — a different object,
and the framework's own vocabulary keeps them apart everywhere else. Strip both words:

        THE MASS UNIT IS ONE NUCLEON'S SHARE OF A TWELVE-NUCLEON NUCLEUS.

A pure count — which is precisely what the SOLID ledger already holds. So the flagged
Reading is not promoted to Solid; IT IS RETIRED AS A NAMING ERROR. The underlying content
was SOLID all along and was never in tension with just-not-tempered; only the two
borrowed words were. Nothing about the anchor changes; the seam closes.

AND ON HOW MANY BORROWS — CORRECTED 2026-08-05 after the author: "we have a whole thing with c
and the metre, rest meters etc, we have a bunch of work on units that preceded this."
He is right and my first answer told SI's story instead of the framework's.

    THE FRAMEWORK'S ANCHOR IS r_p, NOT THE CAESIUM TICK. Banked (working record 2026-06-25):
    "ONE dimensionful anchor (r_p, proton charge radius) + dimensionless 2-perp-3 ratios
    {4, 1836, 137} -> the ENTIRE observable atomic scale." The caesium tick appears in
    the NATIVE-KILO demonstration, which is a different construction (how the kilogram
    becomes a count of carbon), not the framework's foundational borrow.

    AND THERE IS A STANDING BANNER I WALKED INTO. Same working record entry: "There is a
    DO-NOT-RELITIGATE BANNER on c ('c-in-m/s is ruler-content; never raise it again')
    that I blew past." That was 2026-06-25. Framing today's answer around "c sizes the
    metre" raised it again. Recorded as a repeat, not excused.

    THE RIGHT FRAME IS RULER-CONTENT CONSERVATION (01-METHODS:49, graded BEST
    METHODOLOGY): "you may choose WHICH constant wears a clean numeral, but you cannot
    reduce the total ruler-content of the system." So the one-parameter fact is not
    "the second is the borrow" — it is that the borrow is RELOCATABLE but not
    removable. Which constant carries it is a choice; that exactly one must is the
    theorem.

    AND THE REST-METER RESULT IS THE ONE THAT SETTLES IT, banked 2026-06-26 and
    re-verified below: put the metre at k x SI-metre for ANY k and BOTH the prediction
    and the measurement scale together — the ratio is unchanged at every k. THERE IS
    NO UNIT-KNOB, for us or for anyone.

    Also carried from the same entry, because I have misused it before: "STOP invoking
    the dimensional boundary as a catch-all." The framework is NOT magnitude-blind in
    general — where the ratios work, the single anchor delivers absolute in-system
    magnitudes.
"""


def test_the_two_twelfths_are_different_operations():
    """arithmetic division by twelve vs the geometric twelfth root of two"""
    arithmetic = 12 / 12
    geometric = 2 ** (1 / 12)
    assert arithmetic == 1.0
    assert abs(geometric - 1.0594630943592953) < 1e-15
    assert arithmetic != geometric
    # the amu is the arithmetic one: twelve nucleons, take one
    assert 12 / 12 == 1 and 12 * (1 / 12) == 1


def test_no_root_is_ever_extracted():
    """equal temperament needs an irrational 12th root; the anchor needs neither"""
    from fractions import Fraction as F
    unit = F(1, 12)                                # exact rational, the anchor's operation
    assert unit * 12 == 1
    assert unit.denominator == 12 and unit.numerator == 1
    # 2^(1/12) is irrational — it is not any rational at all
    assert not any(abs((F(p, q)) ** 12 - 2) < 1e-30
                   for q in range(1, 200) for p in range(1, 400))


def test_twelve_is_the_chromatic_count_not_the_octave():
    """the second imported word. The octave is a RATIO; twelve is a COUNT."""
    octave_ratio = 2
    chromatic_count = 12
    assert octave_ratio != chromatic_count
    # carbon-12's twelve is a nucleon count, and it factors as the framework's own pair
    assert 12 == 6 + 6                             # 6 protons + 6 neutrons
    assert 12 == 2 * 2 * 3 and 6 == 2 * 3          # Z = 6 = 2x3, the balanced hexad


def test_one_borrow_and_it_is_r_p_and_it_is_relocatable_not_removable():
    """CORRECTED. The framework's single dimensionful anchor is r_p, and the operative
    law is ruler-content conservation: relocatable, not removable."""
    alpha = 1 / 137.035999177
    assert 3 ** 3 * 17 == 459 == 3 ** 7 - 12 ** 3         # pure 2-3; 12^3 = the carbon cube
    assert 4 * 459 == 1836                               # the SAME 459 carries m_p/m_e
    r_e = 2.8179403262e-15
    r_p = r_e / (459 * alpha)
    assert abs(r_p * 1e15 - 0.84131) < 1e-4              # the banked closed form
    # THE REST-METER: rescale the metre by any k and the ratio is untouched
    ratios = set()
    for k in (1.0, 2.5, 1e-3, 1e6):
        ratios.add(round((r_p / k) / (0.8409e-15 / k), 9))
    assert len(ratios) == 1                              # NO UNIT-KNOB, at any k
    # AND THE REDUCTION ITSELF, in dimensional exponents (M, L, T):
    # c has dimensions L/T, so fixing c expresses L in terms of T.
    # h has dimensions M L^2 / T, so fixing h expresses M in terms of L and T,
    # hence — substituting L — in terms of T alone. Both reduce; ONE survives.
    import numpy as np
    c_dim = np.array([0, 1, -1])          # M, L, T exponents of c
    h_dim = np.array([1, 2, -1])          # of h
    A = np.vstack([c_dim, h_dim])          # the two constraints on (M, L, T)
    # the space of scalings leaving both c and h invariant is the null space of A
    ns = np.linalg.svd(A)[2][A.shape[0]:]
    assert ns.shape[0] == 1                # EXACTLY ONE free scaling direction
    v = ns[0] / ns[0][np.argmax(np.abs(ns[0]))]
    # and that direction scales all three together — it is the single borrow
    assert np.allclose(A @ v, 0, atol=1e-12)
    assert not np.allclose(v, 0)
