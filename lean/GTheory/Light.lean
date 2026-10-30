/-
# The mixing wheel in the sevenths

Source: "Visible Light on Discrete Terms" (Christian Horstmann), version 2, §§2–6. The record's
statements:

* §2. Multiplication by ten runs the residues of seven in the cycle 1 → 3 → 2 → 6 → 4 → 5.
* §3, Theorem 1. 10³ ≡ −1 (mod 7): three steps carry k to 7 − k, and opposite six-digit blocks sum to
  999999.
* §4, Theorem 2. Alternate positions split the six into the quadratic residues {1, 2, 4} and the
  non-residues {3, 5, 6}, of sums 7 and 14; the even positions are the orbit of 100 ≡ 2; every
  complement of a residue is a non-residue.
* §5. 0.999999 + 0.000001 = 1; the residue triad of fractions sums to one whole, the other to two.
* §6, Theorems 3–5. Two lights make the opposite pigment: 1/7 + 2/7 = 1 − 4/7 and its two companions.
  On the orbit each non-residue stands between the two residues that sum to it. Of the twelve
  symmetries of the hexagon, six keep the residues on themselves: the namings left free.

What is proved here is arithmetic. That the six fractions are the six hues is the record's
interpretation, stated there.
-/
import Mathlib.Tactic

namespace GTheory.Light

/-- The residues of seven in the order multiplication by ten visits them. -/
def orbit : List ℕ := [1, 3, 2, 6, 4, 5]

/-- **§2, the circle.** The powers of ten modulo seven, from 10⁰, are the orbit. -/
theorem the_orbit : (List.range 6).map (fun i => 10 ^ i % 7) = orbit := by
  decide

/-- **Theorem 1, the half turn.** 10³ ≡ −1 (mod 7), so three steps carry k to 7 − k. -/
theorem the_half_turn : 10 ^ 3 % 7 = 6 ∧ ∀ k ∈ [1, 2, 3, 4, 5, 6], 10 ^ 3 * k % 7 = 7 - k := by
  decide

/-- **Theorem 1, the blocks.** Opposite six-digit blocks sum to 999999. -/
theorem opposite_blocks :
    142857 + 857142 = 999999 ∧ 285714 + 714285 = 999999 ∧ 428571 + 571428 = 999999 := by
  decide

/-- **Theorem 2, the triads.** The non-zero squares modulo seven are 1, 2, 4; they sum to 7 and the
others to 14; 100 ≡ 2; and the complement of every residue is a non-residue. -/
theorem the_triads :
    (List.range 7).filter (fun x => decide (x ≠ 0 ∧ ∃ y ∈ List.range 7, y * y % 7 = x)) = [1, 2, 4] ∧
    1 + 2 + 4 = 7 ∧ 3 + 5 + 6 = 14 ∧ 100 % 7 = 2 ∧ ∀ r ∈ [1, 2, 4], 7 - r ∈ [3, 5, 6] := by
  decide

/-- **§5, the poles.** 0.999999 + 0.000001 = 1; the residue triad of sevenths sums to one, the other
to two. -/
theorem the_poles :
    (999999 : ℚ) / 10 ^ 6 + 1 / 10 ^ 6 = 1 ∧ (1 : ℚ) / 7 + 2 / 7 + 4 / 7 = 1 ∧
    (3 : ℚ) / 7 + 5 / 7 + 6 / 7 = 2 := by
  norm_num

/-- **Theorems 3 and 4, mixing.** The sum of two additive lights is the complement of the third, and
removing two lights from white leaves the third. -/
theorem two_lights_make_the_opposite_pigment :
    (1 : ℚ) / 7 + 2 / 7 = 1 - 4 / 7 ∧ (2 : ℚ) / 7 + 4 / 7 = 1 - 1 / 7 ∧ (4 : ℚ) / 7 + 1 / 7 = 1 - 2 / 7 ∧
    1 - (1 : ℚ) / 7 - 2 / 7 = 4 / 7 := by
  norm_num

/-- **Theorem 5, the order is the mixing order.** On the orbit each non-residue stands between the
two residues that sum to it: 3 between 1 and 2, 6 between 2 and 4, 5 between 4 and 1. -/
theorem the_order_is_the_mixing_order :
    orbit.getD 0 0 + orbit.getD 2 0 = orbit.getD 1 0 ∧ orbit.getD 2 0 + orbit.getD 4 0 = orbit.getD 3 0 ∧
    orbit.getD 4 0 + orbit.getD 0 0 = orbit.getD 5 0 := by
  decide

/-- **§6, the free namings.** The residues stand at positions 0, 2, 4 of the orbit. Of the six
rotations of the hexagon three keep those positions on themselves, and of the six reflections three:
six of twelve symmetries, the namings left free. -/
theorem six_namings_are_free :
    [0, 2, 4].map (fun i => orbit.getD i 0) = [1, 2, 4] ∧
    (List.range 6).filter (fun r => [0, 2, 4].all (fun i => decide ((i + r) % 6 ∈ [0, 2, 4]))) = [0, 2, 4] ∧
    (List.range 6).filter (fun r => [0, 2, 4].all (fun i => decide ((r + 6 - i) % 6 ∈ [0, 2, 4]))) = [0, 2, 4] := by
  decide

end GTheory.Light
