/-
# Predictions on discrete terms: the arithmetic the registry prints

Source: "Predictions on Discrete Terms" (Christian Horstmann, DOI 10.5281/zenodo.21206818),
version 3, Sections 2 and 3. The registry records commitments and argues nothing: the
constructions belong to the companion records. Its page nevertheless carries exact
arithmetic, and that arithmetic is what is proved here:

* the decimals of the registered rationals 4/7, 1/45, 5/17 and 23/32;
* the two members of the electroweak pair as single fractions, and their separation;
* the difference between 17/10 and the She–Lévêque value the registry quotes;
* the Higgs self-coupling 2⁹/(3⁴·7²) and its exact root 32/63;
* the bracket of the ideal saturation density 3·7³/(2¹¹π);
* the factorization 1836 = 36·51;
* the nearest alternatives of Section 3: among fractions of bounded denominator, how close
  any other fraction comes to 4/7 and to 1/45, and the precision that follows.

That an experiment will return a registered value is the registry's commitment and no theorem
of this file; nothing here bears on it.
-/
import Mathlib.Tactic
import Mathlib.Analysis.Real.Pi.Bounds

namespace GTheory.Registry

open Real

/-! ## The registered rationals and their decimals -/

/-- **Commitment 1.** 4/7 = 0.571429 to six places. -/
theorem theta23_decimal :
    (571428 : ℚ) / 10 ^ 6 < 4 / 7 ∧ (4 : ℚ) / 7 < 571429 / 10 ^ 6 := by
  constructor <;> norm_num

/-- **Commitment 2.** 1/45 = 0.022222 to six places. -/
theorem theta13_decimal :
    (22222 : ℚ) / 10 ^ 6 < 1 / 45 ∧ (1 : ℚ) / 45 < 22223 / 10 ^ 6 := by
  constructor <;> norm_num

/-- **The watched value.** 5/17 = 0.294118 to six places. -/
theorem theta12_decimal :
    (294117 : ℚ) / 10 ^ 6 < 5 / 17 ∧ (5 : ℚ) / 17 < 294118 / 10 ^ 6 := by
  constructor <;> norm_num

/-- **Commitment 11.** 23/32 = 0.71875 exactly. -/
theorem residual_ratio : (23 : ℚ) / 32 = 71875 / 100000 := by norm_num

/-! ## The electroweak pair -/

/-- **Commitment 6.** The primary 1 − 17/81 − 13/1000 is 62947/81000, the alternative
1 − 17/81 − 1/75 is 1573/2025, and the two differ by 1/3000. -/
theorem electroweak_pair :
    (1 : ℚ) - 17 / 81 - 13 / 1000 = 62947 / 81000 ∧
      (1 : ℚ) - 17 / 81 - 1 / 75 = 1573 / 2025 ∧
      (62947 : ℚ) / 81000 - 1573 / 2025 = 1 / 3000 := by
  refine ⟨?_, ?_, ?_⟩ <;> norm_num

/-! ## The slope, the Higgs root, the saturation density -/

/-- **Commitment 7.** 17/10 exceeds the She–Lévêque value 1.69594 by 0.00406. -/
theorem slope_against_she_leveque : (17 : ℚ) / 10 - 169594 / 100000 = 406 / 100000 := by
  norm_num

/-- **Commitment 8.** The self-coupling 2⁹/(3⁴·7²) is 512/3969, and 32/63 is the exact
root of its double, so that m_H = (32/63)·v follows from m_H² = 2λv² with no further choice. -/
theorem higgs_root :
    (2 : ℚ) ^ 9 / (3 ^ 4 * 7 ^ 2) = 512 / 3969 ∧
      ((32 : ℚ) / 63) ^ 2 = 2 * (2 ^ 9 / (3 ^ 4 * 7 ^ 2)) := by
  constructor <;> norm_num

/-- **Commitment 10's companion.** The ideal saturation density 3·7³/(2¹¹π) lies between
0.15993 and 0.15994. -/
theorem saturation_density :
    (15993 : ℝ) / 10 ^ 5 < 3 * 7 ^ 3 / (2 ^ 11 * π) ∧
      3 * 7 ^ 3 / (2 ^ 11 * π) < 15994 / 10 ^ 5 := by
  have h1 := pi_gt_d6
  have h2 := pi_lt_d6
  have hpos : (0 : ℝ) < 2 ^ 11 * π := mul_pos (by norm_num) pi_pos
  constructor
  · rw [lt_div_iff₀ hpos]
    norm_num at *
    linarith
  · rw [div_lt_iff₀ hpos]
    norm_num at *
    linarith

/-- **A resolved result.** 1836 = 36·51 = 2²·3³·17. -/
theorem proton_electron_integer : (1836 : ℕ) = 36 * 51 ∧ (1836 : ℕ) = 2 ^ 2 * 3 ^ 3 * 17 := by
  constructor <;> norm_num

/-! ## The nearest alternatives of Section 3

A fraction p/q other than 4/7 stands at distance |7p − 4q|/(7q) from it. The statements below
are that distance bounded from below, cleared of denominators. -/

/-- **Denominators to 10.** No fraction p/q with 1 ≤ q ≤ 10, other than 4/7 itself, lies
closer to 4/7 than 1/63: in integers, q ≤ 9·|7p − 4q| on either side. -/
theorem nearest_to_four_sevenths_to_ten (p q : ℤ) (hq : 1 ≤ q) (hq' : q ≤ 10) :
    (1 ≤ 7 * p - 4 * q → q ≤ 9 * (7 * p - 4 * q)) ∧
      (1 ≤ 4 * q - 7 * p → q ≤ 9 * (4 * q - 7 * p)) := by
  constructor <;> intro h <;> interval_cases q <;> omega

/-- The bound is attained: 5/9 stands at exactly 1/63 from 4/7, so the precision at which
4/7 is alone in a ±2σ band, among denominators to 10, is 1/126 = 0.0079. -/
theorem five_ninths :
    (4 : ℚ) / 7 - 5 / 9 = 1 / 63 ∧ (79 : ℚ) / 10 ^ 4 < 1 / 63 / 2 ∧ (1 : ℚ) / 63 / 2 < 80 / 10 ^ 4 := by
  refine ⟨?_, ?_, ?_⟩ <;> norm_num

/-- **Denominators to 23.** No fraction p/q with 1 ≤ q ≤ 23, other than 4/7 itself, lies
closer to 4/7 than 1/161: in integers, q ≤ 23·|7p − 4q| on either side. -/
theorem nearest_to_four_sevenths_to_twenty_three (p q : ℤ) (hq : 1 ≤ q) (hq' : q ≤ 23) :
    (1 ≤ 7 * p - 4 * q → q ≤ 23 * (7 * p - 4 * q)) ∧
      (1 ≤ 4 * q - 7 * p → q ≤ 23 * (4 * q - 7 * p)) := by
  constructor <;> intro h <;> interval_cases q <;> omega

/-- The bound is attained: 13/23 stands at exactly 1/161 from 4/7, and half of it is 0.0031. -/
theorem thirteen_twenty_thirds :
    (4 : ℚ) / 7 - 13 / 23 = 1 / 161 ∧ (31 : ℚ) / 10 ^ 4 < 1 / 161 / 2 ∧ (1 : ℚ) / 161 / 2 < 32 / 10 ^ 4 := by
  refine ⟨?_, ?_, ?_⟩ <;> norm_num

/-- **Denominators to 50.** No fraction p/q with 1 ≤ q ≤ 50, other than 1/45 itself, lies
closer to 1/45 than 1/2070: in integers, q ≤ 46·|45p − q| on either side. -/
theorem nearest_to_one_forty_fifth (p q : ℤ) (hq : 1 ≤ q) (hq' : q ≤ 50) :
    (1 ≤ 45 * p - q → q ≤ 46 * (45 * p - q)) ∧ (1 ≤ q - 45 * p → q ≤ 46 * (q - 45 * p)) := by
  constructor <;> intro h <;> interval_cases q <;> omega

/-- The bound is attained: 1/46 stands at exactly 1/2070 from 1/45, and half of it is 0.00024. -/
theorem one_forty_sixth :
    (1 : ℚ) / 45 - 1 / 46 = 1 / 2070 ∧ (24 : ℚ) / 10 ^ 5 < 1 / 2070 / 2 ∧ (1 : ℚ) / 2070 / 2 < 25 / 10 ^ 5 := by
  refine ⟨?_, ?_, ?_⟩ <;> norm_num

end GTheory.Registry
