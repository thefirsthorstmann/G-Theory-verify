/-
# Tonal function: the unique root, the two joints, the reflection, the cadence

Source: "Tonal Function on Discrete Terms" (Christian Horstmann), version 2, §§2–7. The record's
statements, as it words them:

* §2. The tones stand at the positions the companion records give them: on 24 the octave carries
  24, 27, 30, 32, 36, 40, 45, 48; each descending ratio times the full turn is the position, 0°,
  45°, 90°, 120°, 180°, 240°, 315°, 360°. The tritone 45/32 has no position: it lies between the
  subdominant's 4/3 and the dominant's 3/2.
* §3. On the ring of twelve, negation fixes exactly two positions, 0 and 6.
* §4, Theorem 1. A pitch-class set supports a unique tonic only if no nonzero shift of the ring maps
  it onto itself: the diatonic and pentatonic sets are fixed by no shift, the whole-tone set by six,
  the octatonic by four, the chromatic by twelve.
* §4, Theorem 2. The diatonic step word is 2 2 1 2 2 2 1, with its two semitone steps at Mi–Fa and
  Si–Do; the whole-tone word is 2 2 2 2 2 2.
* §5, Theorem 3. The reflection through the axis between Do and Sol carries the major set onto its
  parallel natural minor, and the dominant seventh Sol, Si, Re, Fa onto Do, Le, Fa, Re. Partials
  2, 3, 5 give 3/2 and 5/4; divisors give 4/3 = 2 ÷ 3/2 and 8/5 = 2 ÷ 5/4. The fifth below is the
  fourth above, and the submediant is the reversal: 48 × 2/3 = 32 = 24 × 4/3, 48 × 5/6 = 40 = 24 × 5/3.
* §6, Theorem 4. The tritone resolves by contrary motion, both voices moving 16/15: 45 → 48 and
  32 → 30, three units up and two down, opening 45/32 × (16/15)² = 8/5.
* §7. The two cycles, of periods six and eight, close at all-nines integers of digit sums 54 and 72,
  in the ratio 4/3.

What is proved here is the arithmetic of pitch classes and ratios. That these properties are the
functions of tonal harmony is the record's reading, stated there.
-/
import Mathlib.Tactic

namespace GTheory.Tonal

/-- The diatonic set on the ring of twelve, from the tonic. -/
def diatonic : List ℕ := [0, 2, 4, 5, 7, 9, 11]
/-- The major pentatonic set. -/
def pentatonic : List ℕ := [0, 2, 4, 7, 9]
/-- The whole-tone set. -/
def wholeTone : List ℕ := [0, 2, 4, 6, 8, 10]
/-- The octatonic set. -/
def octatonic : List ℕ := [0, 1, 3, 4, 6, 7, 9, 10]
/-- The chromatic set. -/
def chromatic : List ℕ := List.range 12

/-- The shifts of the ring that carry the set into itself (for a finite set and an injective shift,
into is onto). -/
def stabilizer (S : List ℕ) : List ℕ :=
  (List.range 12).filter (fun t => S.all (fun x => decide ((x + t) % 12 ∈ S)))

/-- The steps between consecutive members, closing at the octave. -/
def steps (S : List ℕ) : List ℕ :=
  List.zipWith (fun a b => b - a) S (S.tail ++ [12])

/-- The reflection through the axis between Do (0) and Sol (7): x ↦ 7 − x on the ring. -/
def reflect (x : ℕ) : ℕ := (19 - x) % 12

/-- **§2, the table.** The ascending numbers on 24 and the positions of the descending ratios. -/
theorem the_positions :
    [24, 27, 30, 32, 36, 40, 45, 48].map (fun n : ℕ => (n : ℚ) / 24) =
      [1, 9 / 8, 5 / 4, 4 / 3, 3 / 2, 5 / 3, 15 / 8, 2] ∧
    [(0 : ℚ), 1 / 8, 1 / 4, 1 / 3, 1 / 2, 2 / 3, 7 / 8, 1].map (· * 360) =
      [0, 45, 90, 120, 180, 240, 315, 360] := by
  norm_num

/-- **§2, the unoccupied address.** The tritone 45/32 lies strictly between 4/3 and 3/2. -/
theorem the_tritone_has_no_position : (4 : ℚ) / 3 < 45 / 32 ∧ (45 : ℚ) / 32 < 3 / 2 := by
  norm_num

/-- **§3, the two fixed points.** Negation on the ring of twelve fixes exactly 0 and 6. -/
theorem negation_fixes_two : (List.range 12).filter (fun x => (12 - x) % 12 == x) = [0, 6] := by
  decide

/-- **Theorem 1, the counts.** No nonzero shift fixes the diatonic or the pentatonic set; six fix the
whole-tone set, four the octatonic, twelve the chromatic. -/
theorem stabilizer_counts :
    stabilizer diatonic = [0] ∧ stabilizer pentatonic = [0] ∧
    (stabilizer wholeTone).length = 6 ∧ (stabilizer octatonic).length = 4 ∧
    (stabilizer chromatic).length = 12 := by
  decide

/-- **Theorem 2, the two joints.** The diatonic step word is 2 2 1 2 2 2 1, its semitones after Mi
(4) and after Si (11); the whole-tone word is 2 2 2 2 2 2. -/
theorem the_two_joints :
    steps diatonic = [2, 2, 1, 2, 2, 2, 1] ∧ steps wholeTone = [2, 2, 2, 2, 2, 2] ∧
    diatonic.getD 2 0 = 4 ∧ diatonic.getD 6 0 = 11 := by
  decide

/-- **Theorem 3, the reflection.** It exchanges Do and Sol, carries the major set onto the natural
minor {0, 2, 3, 5, 7, 8, 10}, and the dominant seventh {7, 11, 2, 5} onto {0, 8, 5, 2}. -/
theorem the_reflection :
    reflect 0 = 7 ∧ reflect 7 = 0 ∧
    diatonic.map reflect = [7, 5, 3, 2, 0, 10, 8] ∧ [7, 11, 2, 5].map reflect = [0, 8, 5, 2] := by
  decide

/-- **§5, the over- and undertones.** Partials 3 and 5 reduce to 3/2 and 5/4; the undertone
addresses are the octave over them, 4/3 and 8/5. -/
theorem over_and_under :
    (3 : ℚ) / 2 = 3 / 2 ∧ (5 : ℚ) / 4 = 5 / 4 ∧ (2 : ℚ) / (3 / 2) = 4 / 3 ∧ (2 : ℚ) / (5 / 4) = 8 / 5 := by
  norm_num

/-- **§5, the fifth below and the reversal.** 48 × 2/3 = 32 = 24 × 4/3 and 48 × 5/6 = 40 = 24 × 5/3. -/
theorem fifth_below_and_reversal :
    48 * 2 / 3 = 32 ∧ 24 * 4 / 3 = 32 ∧ 48 * 5 / 6 = 40 ∧ 24 * 5 / 3 = 40 := by
  decide

/-- **Theorem 4, the cadence's count.** Both voices move 16/15, Si up 45 → 48 by three units and Fa
down 32 → 30 by two, and the interval opens to 8/5. -/
theorem the_cadence :
    (48 : ℚ) / 45 = 16 / 15 ∧ (32 : ℚ) / 30 = 16 / 15 ∧ 48 - 45 = 3 ∧ 32 - 30 = 2 ∧
    (45 : ℚ) / 32 * (16 / 15) ^ 2 = 8 / 5 := by
  norm_num

/-- **§7, the two cycles a fourth apart.** The all-nines integers of periods six and eight have digit
sums 54 and 72, in the ratio 4/3; and 10²ʰ − 1 = (10ʰ − 1)(10ʰ + 1) at h = 3 and 4. -/
theorem two_cycles_a_fourth :
    (Nat.digits 10 999999).sum = 54 ∧ (Nat.digits 10 99999999).sum = 72 ∧ (72 : ℚ) / 54 = 4 / 3 ∧
    10 ^ 6 - 1 = (10 ^ 3 - 1) * (10 ^ 3 + 1) ∧ 10 ^ 8 - 1 = (10 ^ 4 - 1) * (10 ^ 4 + 1) := by
  refine ⟨by norm_num, by norm_num, by norm_num, by norm_num, by norm_num⟩

end GTheory.Tonal
