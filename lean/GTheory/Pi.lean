/-
# π on discrete terms: the register bracket and the rest value

Source: "π on Discrete Terms" (Christian Horstmann, DOI 10.5281/zenodo.21205368), Section 6,
the Definition "The register bracket and the rest value", and Section 7. The record's
statements, in its words:

* The least seventh above π is ⌈7π⌉/7 = 22/7; the greatest sixty-fourth below π is
  ⌊64π⌋/64 = 201/64.
* Their midpoint is exactly ρ = (201/64 + 22/7)/2 = 2815/896, with denominator 2⁷·7.
* ρ sits 47 parts per million above π.
* The register bracket is not an Archimedean stage: its excess-to-deficit ratio is ≈ 1.31,
  not 2.
* The expansion of ρ settles, after seven places, into a pure six-place cycle: 3.1417410,
  then 714285 repeating, the reptend of the sevenths.

What is proved here is the arithmetic. That ρ is called the rest value is the record's
definition, and that it is the circle's constant at zero excitation is the record's
conjecture (Section 7); neither is a theorem of this file. Theorems 1 to 3 of the record are
analysis and are not formalized here.
-/
import Mathlib.Tactic
import Mathlib.Analysis.Real.Pi.Bounds

namespace GTheory.Pi

open Real

/-- **The register bracket encloses π.** 201/64 < π < 22/7. -/
theorem register_bracket : (201 : ℝ) / 64 < π ∧ π < 22 / 7 := by
  have h1 := pi_gt_d4
  have h2 := pi_lt_d4
  constructor <;> norm_num at * <;> linarith

/-- **The greatest sixty-fourth below π is 201/64.** -/
theorem floor_sixty_four_pi : ⌊64 * π⌋ = 201 := by
  have h1 := pi_gt_d4
  have h2 := pi_lt_d4
  rw [Int.floor_eq_iff]
  constructor <;> norm_num at * <;> linarith

/-- **The least seventh above π is 22/7.** -/
theorem ceil_seven_pi : ⌈7 * π⌉ = 22 := by
  have h1 := pi_gt_d4
  have h2 := pi_lt_d4
  rw [Int.ceil_eq_iff]
  constructor <;> norm_num at * <;> linarith

/-- **The midpoint of the bracket is 2815/896, and its denominator is 2⁷·7.** -/
theorem rest_value : ((201 : ℚ) / 64 + 22 / 7) / 2 = 2815 / 896 ∧ (896 : ℕ) = 2 ^ 7 * 7 := by
  constructor <;> norm_num

/-- **The midpoint lies above π by between 47 and 48 parts per million.** -/
theorem overshoot_is_47_ppm :
    47 / 10 ^ 6 < ((2815 : ℝ) / 896 - π) / π ∧ ((2815 : ℝ) / 896 - π) / π < 48 / 10 ^ 6 := by
  have h1 := pi_gt_d6
  have h2 := pi_lt_d6
  have hpos : (0 : ℝ) < π := pi_pos
  constructor
  · rw [lt_div_iff₀ hpos]
    norm_num at *
    linarith
  · rw [div_lt_iff₀ hpos]
    norm_num at *
    linarith

/-- **The bracket is not an Archimedean stage.** Its excess over its deficit lies between
1.30 and 1.32, where an Archimedean stage tends to 2. -/
theorem excess_to_deficit :
    (130 : ℝ) / 100 < (22 / 7 - π) / (π - 201 / 64) ∧
      (22 / 7 - π) / (π - 201 / 64) < 132 / 100 := by
  have h1 := pi_gt_d6
  have h2 := pi_lt_d6
  have hpos : (0 : ℝ) < π - 201 / 64 := by norm_num at *; linarith
  constructor
  · rw [lt_div_iff₀ hpos]
    norm_num at *
    linarith
  · rw [div_lt_iff₀ hpos]
    norm_num at *
    linarith

/-- **After seven places the expansion of ρ is the cycle of the sevenths.**
10⁷·ρ = 31417410 + 5/7, and 5/7 = 714285/999999, the period 714285. -/
theorem tail_is_the_reptend :
    (2815 : ℚ) / 896 * 10 ^ 7 = 31417410 + 5 / 7 ∧ (5 : ℚ) / 7 = 714285 / 999999 := by
  constructor <;> norm_num

end GTheory.Pi
