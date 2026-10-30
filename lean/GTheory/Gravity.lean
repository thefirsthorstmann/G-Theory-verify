/-
# Gravity on discrete terms: the arithmetic the record stands on

Source: "Gravity on Discrete Terms" (Christian Horstmann, DOI 10.5281/zenodo.22087599),
version 4. The record's identifications join arithmetic to physics and are not theorems of
this file; what is proved here is the arithmetic those identifications are made on, each
statement in the record's own words:

* §4: 142857 × 7 = 10⁶ − 1, one short and never over;
* §5: k × 142857 × 7 = k·10⁶ − k, the absolute shortfall proportional to k;
* §6: the descent on the root 24 read through seven has residues 3, 0, 2, 5, 1, 6, 3, 0, and
  exactly one station, 8, has residue one; the root is the least common multiple of the just
  denominators; the two rings share the factor three;
* §13: 2¹⁵ − 1 = 7·31·151 with 151 = Φ₁₅(2) prime; the order of two modulo five is four, so
  the block 5 is irreducible at period 151 and reducible at 152; the three ways of writing
  the coupling are one number;
* §14: the two clocks, of periods 6 and 42, close together at 42;
* §16: one octave of boost is 3/5, two are 15/17, and two boosts of 3/5 stack to 15/17; the
  comma 3¹²/2¹⁹;
* §19: the contact counts are three times a power of two exactly in dimensions two, three
  and four; the products 6·8 and 12·24, 137 = 8·17 + 1, and the order of two modulo
  seventeen;
* §21: the circular-orbit landmarks at the deficits 1/3, 1/4 and 1/6, the energy 8/9, the
  Nordtvedt parameter, the frame constant 4/3, and refinement returning the sevenths' cycle
  exactly when three divides the dimension.
-/
import Mathlib.Tactic

namespace GTheory.Gravity

/-! ## Part I: the shortfall, the source law, the carrier -/

/-- **§4, the shortfall.** 142857 × 7 = 10⁶ − 1. -/
theorem shortfall_at_seven : 142857 * 7 = 10 ^ 6 - 1 := by norm_num

/-- **§5, the k-rotation identity.** k × 142857 × 7 = k·10⁶ − k. The record states it for
k = 1 … 6, where the multiple is a rotation of the reptend; the identity holds for every k. -/
theorem k_rotation (k : ℕ) : k * 142857 * 7 = k * 10 ^ 6 - k := by
  norm_num
  omega

/-- **§6.** The register's depth is the reptend's period, 10⁶ ≡ 1 (mod 7), and the
two-ladder returns to the unit at eight, 2³ ≡ 1 (mod 7). -/
theorem depth_is_the_period : 10 ^ 6 % 7 = 1 ∧ 2 ^ 3 % 7 = 1 := by norm_num

/-- **§6.** The residues of the eight stations of the descent, read through seven. -/
theorem residues_of_the_descent :
    [24, 21, 16, 12, 8, 6, 3, 0].map (· % 7) = [3, 0, 2, 5, 1, 6, 3, 0] := by decide

/-- **§6.** Exactly one station of the descent has residue one, and it is 8, the
subdominant. -/
theorem unit_residue_only_at_eight :
    [24, 21, 16, 12, 8, 6, 3, 0].filter (fun n => n % 7 = 1) = [8] := by decide

/-- **§6.** The nine-position ring and the twelve-semitone ring share exactly the factor
three, and 24 is the least common multiple of the just ratios' denominators. -/
theorem rings_and_root :
    Nat.gcd 9 12 = 3 ∧ [1, 8, 4, 3, 2, 3, 8, 1].foldl Nat.lcm 1 = 24 := by decide

/-! ## Part III: the coupling and the chain -/

/-- **§13.** The first joint closure of the motor's and the lift's cycles: 2¹⁵ − 1 = 7·31·151. -/
theorem joint_closure : 2 ^ 15 - 1 = 7 * 31 * 151 := by norm_num

/-- **§13.** 151 is the value at two of the fifteenth cyclotomic polynomial,
x⁸ − x⁷ + x⁵ − x⁴ + x³ − x + 1, and it is prime. -/
theorem period_151 :
    (2 : ℤ) ^ 8 - 2 ^ 7 + 2 ^ 5 - 2 ^ 4 + 2 ^ 3 - 2 + 1 = 151 ∧ Nat.Prime 151 := by
  constructor <;> norm_num

/-- **§13.** The three ways of writing the coupling are one number:
5·2⁻¹⁵¹ = 10·2⁻¹⁵² = (5/4)·2⁻¹⁴⁹. -/
theorem one_number :
    (5 : ℚ) / 2 ^ 151 = 10 / 2 ^ 152 ∧ (5 : ℚ) / 2 ^ 151 = 5 / 4 / 2 ^ 149 := by
  constructor <;> norm_num

/-- **§13.** The order of two modulo five is four; four does not divide 151 and does divide
152, so the block 5 is irreducible at period 151 and the block 10 reduces. -/
theorem block_five_is_irreducible :
    (2 ^ 4 % 5 = 1 ∧ 2 ^ 1 % 5 ≠ 1 ∧ 2 ^ 2 % 5 ≠ 1 ∧ 2 ^ 3 % 5 ≠ 1) ∧ ¬ 4 ∣ 151 ∧ 4 ∣ 152 := by
  decide

/-- **§14.** The tripling clock 1/7 closes in 6 and the doubling clock 1/98 in 42: ten has
order 6 modulo 7 and order 42 modulo 49. -/
theorem clock_periods :
    (10 ^ 6 % 7 = 1 ∧ ∀ k, 0 < k → k < 6 → 10 ^ k % 7 ≠ 1) ∧
      (10 ^ 42 % 49 = 1 ∧ ∀ k, 0 < k → k < 42 → 10 ^ k % 49 ≠ 1) := by
  refine ⟨⟨by norm_num, ?_⟩, ⟨by norm_num, ?_⟩⟩
  · intro k h0 h1
    interval_cases k <;> norm_num
  · intro k h0 h1
    interval_cases k <;> norm_num

/-- **§14.** The two clocks coincide at their least common multiple, lcm(6, 42) = 42. -/
theorem co_closure : Nat.lcm 6 42 = 42 := by decide

/-! ## Part V: the kinematics -/

/-- **§16.** One octave of boost is 3/5 and two are 15/17: β(n) = (4ⁿ − 1)/(4ⁿ + 1). -/
theorem octave_boosts :
    ((4 : ℚ) ^ 1 - 1) / (4 ^ 1 + 1) = 3 / 5 ∧ ((4 : ℚ) ^ 2 - 1) / (4 ^ 2 + 1) = 15 / 17 := by
  constructor <;> norm_num

/-- **§16.** Two boosts of 3/5 stack to 15/17 and never to 6/5. -/
theorem stacked_boosts : ((3 : ℚ) / 5 + 3 / 5) / (1 + 9 / 25) = 15 / 17 := by norm_num

/-- **§16.** The comma: twelve fifths against seven octaves, 3¹² = 531441 and 2¹⁹ = 524288. -/
theorem pythagorean_comma : (3 : ℕ) ^ 12 = 531441 ∧ (2 : ℕ) ^ 19 = 524288 := by
  constructor <;> norm_num

/-! ## Part VI: the dimension, the landmarks, the refinement -/

/-- **§19.** Among the contact counts of dimensions one to eight, the count is three times a
power of two, 3·2^(d−1), exactly at d = 2, 3 and 4. -/
theorem contact_window :
    ([1, 2, 3, 4, 5, 6, 7, 8].zip [2, 6, 12, 24, 40, 72, 126, 240]).filter
        (fun p => p.2 = 3 * 2 ^ (p.1 - 1)) = [(2, 6), (3, 12), (4, 24)] := by
  decide

/-- **§19.** The bridge between the two ladders: 6·8 = 48 = 7² − 1 and
12·24 = 288 = 17² − 1 = 16·18. -/
theorem ladder_bridge :
    6 * 8 = 48 ∧ 48 = 7 ^ 2 - 1 ∧ 12 * 24 = 288 ∧ 288 = 17 ^ 2 - 1 ∧ 288 = 16 * 18 := by
  decide

/-- **§19.** The two primes couple: 137 = 8·17 + 1, and the order of two modulo seventeen
is eight. -/
theorem primes_couple :
    137 = 8 * 17 + 1 ∧ 2 ^ 8 % 17 = 1 ∧ ∀ k, 0 < k → k < 8 → 2 ^ k % 17 ≠ 1 := by
  refine ⟨by norm_num, by norm_num, ?_⟩
  intro k h0 h1
  interval_cases k <;> norm_num

/-- **§21.2.** The circular-orbit landmarks. The orbital speed reaches light speed at the
deficit 1/3; the circular energy E² = (1 − 2φ)²/(1 − 3φ) equals rest energy at 1/4 and is 8/9
at 1/6. -/
theorem landmarks :
    (1 / 3 : ℚ) / (1 - 2 * (1 / 3)) = 1 ∧
      (1 - 2 * (1 / 4 : ℚ)) ^ 2 / (1 - 3 * (1 / 4)) = 1 ∧
      (1 - 2 * (1 / 6 : ℚ)) ^ 2 / (1 - 3 * (1 / 6)) = 8 / 9 := by
  refine ⟨?_, ?_, ?_⟩ <;> norm_num

/-- **§21.6.** The Nordtvedt parameter η = 4β − γ − 3 vanishes at β = γ = 1. -/
theorem nordtvedt : 4 * (1 : ℚ) - 1 - 3 = 0 := by norm_num

/-- **§21.8.** The frame constant (d + 1)/d runs 2/1, 3/2, 4/3, 5/4, 6/5 over d = 1 … 5;
at d = 3 it is 4/3, and 24 × 4/3 = 32. -/
theorem frame_constant :
    [1, 2, 3, 4, 5].map (fun d : ℚ => (d + 1) / d) = [2 / 1, 3 / 2, 4 / 3, 5 / 4, 6 / 5] ∧
      (24 : ℚ) * (4 / 3) = 32 := by
  constructor <;> norm_num

/-- **§21.8.** Refinement into 2^d children returns the sevenths' cycle, 2^d ≡ 1 (mod 7),
exactly when three divides d; checked for every dimension to twelve. -/
theorem refinement_returns (d : ℕ) (h : d ≤ 12) : 2 ^ d % 7 = 1 ↔ 3 ∣ d := by
  interval_cases d <;> decide

end GTheory.Gravity
