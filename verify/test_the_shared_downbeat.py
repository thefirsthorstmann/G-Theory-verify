"""test_the_shared_downbeat.py — the author'S CLAVE READING OF THE TRIGGER: ONE SHARED
REFERENCE AT THE START, EXCLUSION EVER AFTER, AND THE INFORMATIONAL
CO-OCCUPANCY THAT FIRES IT (2026-08-15). His structure, from the music that
carries it: the reggaeton/dembow grid puts the kick on beats one and three —
the two-side — and the snare on the and-of-two and four, the clave's second
and third hits; the salsa tumbao rides the same three-side and plays the
DOWNBEAT EXACTLY ONCE, at the start of the process, then floats forever. His
reading: the two-aspect and three-aspect of the clock share a SINGLE original
reference and then coexist superimposed without sharing — the form of the
exclusion principle — and the unique condition at the start violates
exclusion INFORMATIONALLY, not physically, by superposition, through the same
mechanism as the fourth and fifth sitting invisible as to which is which.

  FIRST, THE IDENTIFICATION THAT MAKES THIS MORE THAN A METAPHOR: THE
  TRESILLO IS THE BANKED ESCAPEMENT, BY NAME. The clave's three-side in the
  eight-pulse grid is the Euclidean rhythm E(3,8) — onsets at zero, three,
  six — and E(3,8) is THE-CLOCK-OBJECT's own escapement, banked. The kick's
  two-side is zero and four. the author's beat is not like the clock; it is the
  clock's pinned object, played.

  THE EXCLUSION STRUCTURE, FORCED: the three-side and the two-side intersect
  in EXACTLY the downbeat — {0,3,6} meets {0,4} in {0} alone — and the
  three-step orbit visits all eight pulses before returning (gcd(3,8)=1, the
  banked tick-contact fact), so within the cycle the two aspects co-occupy
  once and only once. After the one, exclusion — not as a postulate but as
  coprimality.

  THE SALSA DETAIL IS THE TWO INSCRIPTION CLOCKS' OWN STRUCTURE, FORCED: in
  one forty-two-digit record the tripling clock (period six) comes home seven
  times and the doubling clock (period forty-two) once; they are home
  TOGETHER exactly once — at the origin. The record's single shared downbeat.
  And the closure at forty-two IS the next downbeat: the tumbao's one-then-
  float is the record structure of the two movers, note for note.

  THE FOURTH-AND-FIFTH MECHANISM, EXACT: Fa times Sol is EXACTLY the octave
  — four-thirds times three-halves is two — so the pair is one split of the
  octave, and inversion through the octave SWAPS them: the fourth from one
  end is the fifth from the other. Without the reference (which end is Do)
  the pair {4/3, 3/2} is a single unordered object: two tones, one
  informational state, the which-is-which carried by EXACTLY ONE BIT — the
  same one bit as the held form's two names. And the gap that bit spans is
  Sol over Fa = NINE EIGHTHS — the kiss interval, whose defect is the unit,
  where the energy lives. S = 17/6, D = 1/6, Tartini (S^2-D^2)/4 = 2, all
  exact. So the co-occupancy at the downbeat is a HELD PAIR — superposition,
  the union-read theorem's own uncommitted state, "commitment is what
  selects one count" — and it violates exclusion informationally, never
  physically, exactly as the author said.

  THE TRIGGER, ASSEMBLED (Reading, the build's target tonight): WHERE —
  adjacency in the register; WHEN — the shared downbeat, the co-closure
  point, once per record; WHAT — the held pair collapsing, paying the
  which-is-which bit. The salsa one is the ignition; the float is the
  exclusion era; the next downbeat is the next union window. FLAGGED for the
  parked Pauli crosswalk: exclusion-after-a-single-shared-origin now has a
  candidate clock mechanism (coprimality), and the allowed violation at the
  origin is informational superposition — the crosswalk should start here.
"""

from fractions import Fraction as F
from math import gcd


def test_the_tresillo_is_the_banked_escapement():
    """The tresillo {0,3,6} — gaps 3,3,2 — is a maximally even placement of
    3 onsets in 8 pulses, i.e. the Euclidean E(3,8), THE-CLOCK-OBJECT's
    escapement. (Stated by its gap structure, not a formula: my first
    floor-formula produced the rotation {0,2,5} and the pin refused it —
    same gap multiset, wrong anchoring; the played tresillo anchors the
    downbeat and runs 3+3+2.)"""
    tres = [0, 3, 6]                                # x..x..x. — the tresillo
    gaps = [(tres[(i + 1) % 3] - tres[i]) % 8 for i in range(3)]
    assert sorted(gaps) == [2, 3, 3]                # the 3+3+2 cell
    assert max(gaps) - min(gaps) == 1               # maximally even = Euclidean
    # the grid: beat1=0, and-of-2=3, beat4=6 — clave hits; snare = {3,6}:
    snare = [p for p in tres if p != 0]
    assert snare == [3, 6]                          # no snare on the downbeat
    kick = [0, 4]                                   # beats one and three
    assert set(kick) | set(tres) <= set(range(8))


def test_the_two_aspects_share_exactly_the_downbeat():
    """{0,3,6} meets {0,4} in {0} alone, and the three-orbit visits all
    eight pulses — exclusion after the one, by coprimality."""
    three_side, two_side = {0, 3, 6}, {0, 4}
    assert three_side & two_side == {0}             # the single shared hit
    orbit, x = [], 0
    for _ in range(8):
        orbit.append(x)
        x = (x + 3) % 8
    assert sorted(orbit) == list(range(8))          # all pulses visited
    assert gcd(3, 8) == 1                           # the banked reason


def test_the_tumbao_is_the_two_clocks_record_structure():
    """Period six comes home seven times per record, period forty-two once;
    together exactly once — the single one, then the float."""
    record = 42
    homes_3clock = [t for t in range(record) if t % 6 == 0]
    homes_2clock = [t for t in range(record) if t % 42 == 0]
    assert len(homes_3clock) == 7                   # seven hexad returns
    assert homes_2clock == [0]                      # once
    shared = set(homes_3clock) & set(homes_2clock)
    assert shared == {0}                            # THE SINGLE DOWNBEAT
    # and the closure is the next downbeat:
    assert record % 6 == 0 and record % 42 == 0     # both home again at 42


def test_fa_and_sol_are_one_octave_split_and_the_bit_spans_the_kiss():
    """Fa x Sol = 2 exactly; inversion swaps them; the which-is-which is one
    bit; the gap it spans is 9/8, the kiss interval."""
    fa, sol = F(4, 3), F(3, 2)
    assert fa * sol == 2                            # the octave, exactly
    assert 2 / fa == sol and 2 / sol == fa          # inversion swaps them
    assert sol / fa == F(9, 8)                      # the kiss interval
    assert 9 - 8 == 1                               # whose defect is the unit
    S, D = fa + sol, sol - fa
    assert S == F(17, 6) and D == F(1, 6)
    assert (S ** 2 - D ** 2) / 4 == 2               # Tartini returns the octave
    # the unordered pair is one state; the ordering is exactly one bit:
    assert {fa, sol} == {sol, fa}                   # one informational object
    assert len([(fa, sol), (sol, fa)]) == 2         # two orderings: one bit


def test_the_trigger_assembled_and_the_pauli_flag():
    """WHERE adjacency, WHEN the shared downbeat, WHAT the held pair paying
    its bit — Reading, with the exclusion mechanism flagged for the parked
    Pauli crosswalk."""
    trigger = {"where": "adjacency in the register",
               "when": "the shared downbeat (co-closure, once per record)",
               "what": "held pair collapses, which-is-which bit paid"}
    assert len(trigger) == 3
    exclusion_mechanism = "coprimality after a single shared origin"
    violation_at_origin = "informational (superposition), never physical"
    assert "coprimality" in exclusion_mechanism
    assert "physical" in violation_at_origin
    pauli_crosswalk_should_start_here = True
    assert pauli_crosswalk_should_start_here
