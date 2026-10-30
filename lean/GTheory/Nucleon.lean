/-
# The proton and neutron masses on discrete terms: the arithmetic the record stands on

Source: "The Proton and Neutron Masses on Discrete Terms" (Christian Horstmann,
DOI 10.5281/zenodo.22217669), version 4, Sections 6, 7, 8, 10 and 11. The record's mechanism is
a hypothesis and its comparisons are with measurement; neither is a theorem of this file. What
is proved here is the exact arithmetic the record displays, each statement in the record's own
words:

* §6: the stations above 64 with a superparticular step are exactly 66, 72 and 96; the steps
  33/32, 9/8 and 3/2; four of the eight arrangements leave the proton lighter; the base
  1008 = T(7)·T(8); the two reference values 100728 and 100866 and their average; 10⁴ + 1 = 73·137
  with nine and seventeen classes of eight; the depth of the fine-structure residual;
* §7: the four identities of the pair (28, 36), and the carbon restatement;
* §8: the two displacements as exact rationals from the 2022 central values, their ratio against
  23/32, the uniqueness of that fraction among denominators to 64 inside three standard
  deviations, and the two composite residuals;
* §10: six whole tones against the octave, the syntonic comma, the two candidate steps and the
  temperatures they set, and the digits of the two stations;
* §11: the image identity, and the reference image as a finite head followed by the cycle of
  the sevenths.

Measured values enter only as the rationals the record prints (CODATA 2022 central values and
the standard deviation it quotes for the ratio). That nature realizes any of this is the
record's hypothesis and no statement of this file.
-/
import Mathlib.Tactic

namespace GTheory.Nucleon

/-! ## Section 6: the stations, the base, the reference values -/

/-- **§6.** A station above the sixth octave 64 has a superparticular step exactly when its
distance from 64 divides 64, and this has three solutions: 66, 72 and 96. -/
theorem stations_with_a_superparticular_step (s : ℕ) (h64 : 64 < s) (h6 : 6 ∣ s) :
    (s - 64) ∣ 64 ↔ s = 66 ∨ s = 72 ∨ s = 96 := by
  constructor
  · intro h
    have hle : s - 64 ≤ 64 := Nat.le_of_dvd (by norm_num) h
    have hs : s ≤ 128 := by omega
    interval_cases s <;> omega
  · rintro (rfl | rfl | rfl) <;> decide

/-- **§6.** The steps are 33/32, 9/8 and 3/2; 66 and 72 are consecutive stations, their
difference the ladder's unit and their ratio 12/11. -/
theorem the_steps :
    (66 : ℚ) / 64 = 33 / 32 ∧ (72 : ℚ) / 64 = 9 / 8 ∧ (96 : ℚ) / 64 = 3 / 2 ∧
      (72 : ℕ) - 66 = 6 ∧ (72 : ℚ) / 66 = 12 / 11 := by
  refine ⟨?_, ?_, ?_, ?_, ?_⟩ <;> norm_num

/-- **§6.** Of the eight arrangements of the pair, by assignment and by sign, four leave the
proton lighter than the neutron. Each entry is (proton's station, neutron's station) with
(proton's sign, neutron's sign). -/
theorem four_arrangements_leave_the_proton_lighter :
    ((([(66, 72), (72, 66)] : List (ℤ × ℤ)).product
          ([(1, 1), (1, -1), (-1, 1), (-1, -1)] : List (ℤ × ℤ))).filter
        (fun x => 100800 + x.2.1 * x.1.1 < 100800 + x.2.2 * x.1.2)).length = 4 := by
  decide

/-- **§6, Identity 2.** The base is the product of the adjacent triangular numbers at the seed
pair: 1008 = T(7)·T(8) = 28·36. -/
theorem the_base : 7 * 8 / 2 = 28 ∧ 8 * 9 / 2 = 36 ∧ 1008 = 28 * 36 := by decide

/-- **§6.** The two mass reference values are one base with two stations, 100800 − 72 and
100800 + 66; their average is 100797; and the subtraction's borrow crosses the digit boundary,
100728 beginning 1007. -/
theorem the_reference_values :
    100800 - 72 = 100728 ∧ 100800 + 66 = 100866 ∧ (100728 + 100866) / 2 = 100797 ∧
      100728 / 100 = 1007 := by
  decide

/-- **§6.** The primes of base-ten period eight divide 10⁴ + 1 = 73·137; the nonzero residues
of 73 fall into nine classes of eight and those of 137 into seventeen. -/
theorem period_eight_primes :
    10 ^ 4 + 1 = 73 * 137 ∧ 73 - 1 = 8 * 9 ∧ 137 - 1 = 8 * 17 := by decide

/-- **§6.** The fine-structure residual on the 2022 central value, 137.036 − 137.035999177,
is 0.000823 of the reference value's last digit: a depth of one part in twelve hundred. -/
theorem depth_of_the_fine_structure_residual :
    ((137036 : ℚ) / 1000 - 137035999177 / 10 ^ 9) * 1000 = 823 / 10 ^ 6 ∧
      (1 : ℚ) / 1216 < 823 / 10 ^ 6 ∧ (823 : ℚ) / 10 ^ 6 < 1 / 1214 := by
  refine ⟨?_, ?_, ?_⟩ <;> norm_num

/-! ## Section 7: the four identities of the pair (28, 36) -/

/-- **Identity 1 (the bridge).** 0.036 × 28 = 1.008. -/
theorem identity_one : (36 : ℚ) / 1000 * 28 = 1008 / 1000 := by norm_num

/-- **Identity 3 (the carbon fraction).** 1.008 = 126/125 places the free-nucleon excess at one
part in 126, and 1/28 − 1/36 = 1/126. -/
theorem identity_three :
    (1008 : ℚ) / 1000 = 126 / 125 ∧ ((126 : ℚ) / 125 - 1) / (126 / 125) = 1 / 126 ∧
      (1 : ℚ) / 28 - 1 / 36 = 1 / 126 := by
  refine ⟨?_, ?_, ?_⟩ <;> norm_num

/-- **Identity 3, restated.** In the reference values the binding of carbon-12 less its electron
masses is 12/125 = 0.096 u; the 2022 central values give 0.0956483 u, which is 0.37 percent
below it. -/
theorem carbon_restatement :
    12 * ((126 : ℚ) / 125 - 1) = 12 / 125 ∧ (12 : ℚ) / 125 = 96 / 1000 ∧
      6 * ((10072764665789 : ℚ) / 10 ^ 13) + 6 * (100866491606 / 10 ^ 11) - 12
        = 956482958334 / 10 ^ 13 ∧
      (36 : ℚ) / 10 ^ 4 < (96 / 1000 - 956482958334 / 10 ^ 13) / (96 / 1000) ∧
      ((96 : ℚ) / 1000 - 956482958334 / 10 ^ 13) / (96 / 1000) < 37 / 10 ^ 4 := by
  refine ⟨?_, ?_, ?_, ?_, ?_⟩ <;> norm_num

/-- **Identity 4 (the tail's composition).** 9/250 = 0.036 = (1/28) × (126/125). -/
theorem identity_four :
    (9 : ℚ) / 250 = 36 / 1000 ∧ (9 : ℚ) / 250 = 1 / 28 * (126 / 125) := by
  constructor <;> norm_num

/-! ## Section 8: the two displacements and their ratio -/

/-- **§8.** On the 2022 central values the displacements are Δp = 0.35334211 and Δn = 0.491606,
in units of one part in one hundred thousand. -/
theorem the_displacements :
    ((100728 : ℚ) / 10 ^ 5 - 10072764665789 / 10 ^ 13) * 10 ^ 5 = 35334211 / 10 ^ 8 ∧
      ((100866491606 : ℚ) / 10 ^ 11 - 100866 / 10 ^ 5) * 10 ^ 5 = 491606 / 10 ^ 6 := by
  constructor <;> norm_num

/-- **§8.** Their ratio is 0.7187506 to seven places, and it stands above 23/32 = 0.71875 by
less than one part in a million of that fraction. -/
theorem the_ratio :
    (7187506 : ℚ) / 10 ^ 7 < 35334211 / 10 ^ 8 / (491606 / 10 ^ 6) ∧
      (35334211 : ℚ) / 10 ^ 8 / (491606 / 10 ^ 6) < 7187507 / 10 ^ 7 ∧
      (23 : ℚ) / 32 = 71875 / 10 ^ 5 ∧
      (0 : ℚ) < 35334211 / 10 ^ 8 / (491606 / 10 ^ 6) - 23 / 32 ∧
      ((35334211 : ℚ) / 10 ^ 8 / (491606 / 10 ^ 6) - 23 / 32) / (23 / 32) < 1 / 10 ^ 6 := by
  refine ⟨?_, ?_, ?_, ?_, ?_⟩ <;> norm_num

/-- **§8, Result (uniqueness of the fraction).** Among fractions p/q with 1 ≤ q ≤ 64, the only
one within three standard deviations of the measured ratio, 0.7187506 ± 3 × 0.0000585, is
23/32. The window is [0.7185751, 0.7189261], cleared of denominators. -/
theorem uniqueness_of_the_fraction (p q : ℤ) (hq : 1 ≤ q) (hq' : q ≤ 64)
    (lo : 7185751 * q ≤ 10 ^ 7 * p) (hi : 10 ^ 7 * p ≤ 7189261 * q) : 32 * p = 23 * q := by
  interval_cases q <;> omega

/-- 23/32 itself lies in the window, so the fraction exists as well as being the only one. -/
theorem the_fraction_is_in_the_window :
    (7185751 : ℚ) / 10 ^ 7 ≤ 23 / 32 ∧ (23 : ℚ) / 32 ≤ 7189261 / 10 ^ 7 := by
  constructor <;> norm_num

/-- **§8.** One pair of numbers carries the family: the average's residual is half the
difference of the two displacements, and the splitting's residual is their sum. -/
theorem the_composites (dp dn : ℚ) :
    ((100866 + dn) + (100728 - dp)) / 2 - 100797 = (dn - dp) / 2 ∧
      ((100866 + dn) - (100728 - dp)) - (100866 - 100728) = dn + dp := by
  constructor <;> ring

/-! ## Section 10: the whole tones, the comma, the candidate steps -/

/-- **§10.** Six whole-tone steps of 9/8 span one octave and the comma 531441/524288. -/
theorem six_whole_tones : ((9 : ℚ) / 8) ^ 6 = 2 * (531441 / 524288) := by norm_num

/-- **§10 and §5.** The three-limit sixth 27/16 stands above the just sixth 5/3 by exactly the
syntonic comma 81/80, whose excess is 1/80 = 0.0125. -/
theorem syntonic_comma :
    ((27 : ℚ) / 16) / (5 / 3) = 81 / 80 ∧ (81 : ℚ) / 80 - 1 = 1 / 80 ∧ (1 : ℚ) / 80 = 125 / 10 ^ 4 := by
  refine ⟨?_, ?_, ?_⟩ <;> norm_num

/-- **§10.** The septimal step is 28/27 = (7/6)/(9/8), and it carries the septimal third onto
the subdominant, 9/7 × 28/27 = 4/3; the chromatic step is 25/24 = (5/4)/(6/5). One step above
m_p/6 they set 14 m_p/81 and 25 m_p/144. -/
theorem the_candidate_steps :
    (28 : ℚ) / 27 = (7 / 6) / (9 / 8) ∧ (9 : ℚ) / 7 * (28 / 27) = 4 / 3 ∧
      (25 : ℚ) / 24 = (5 / 4) / (6 / 5) ∧ (1 : ℚ) / 6 * (28 / 27) = 14 / 81 ∧
      (1 : ℚ) / 6 * (25 / 24) = 25 / 144 := by
  refine ⟨?_, ?_, ?_, ?_, ?_⟩ <;> norm_num

/-- **§10.** The station 72 is three times 24 and its two digits reverse to a different pair,
27; the station 66 is a palindrome and the doubled centre 33. -/
theorem the_digits_of_the_stations :
    72 = 3 * 24 ∧ 72 = 7 * 10 + 2 ∧ 2 * 10 + 7 = 27 ∧ 27 ≠ 72 ∧ 66 = 6 * 10 + 6 ∧ 66 = 2 * 33 := by
  decide

/-! ## Section 11: the images -/

/-- **§11.** The image identity: 0.036 × (m̄/1.008) = m̄/28 for every m̄. -/
theorem image_identity (m : ℚ) : (36 : ℚ) / 1000 * (m / (1008 / 1000)) = m / 28 := by
  ring

/-- **§11.** Dividing the reference values gives 100797/2800000, a finite head 0.0359989
followed by the cycle of the sevenths: the remainder is exactly 2/7 at the seventh place. -/
theorem reference_image :
    ((100728 : ℚ) + 100866) / 2 / 10 ^ 5 / 28 = 100797 / 2800000 ∧
      (100797 : ℚ) / 2800000 = 359989 / 10 ^ 7 + 2 / 7 / 10 ^ 7 := by
  constructor <;> norm_num

end GTheory.Nucleon
