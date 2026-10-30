/-
# The Origin on Discrete Terms: the finite arithmetic of its volumes

Source: "G-Theory — The Origin on Discrete Terms" (Christian Horstmann, concept DOI
10.5281/zenodo.21212112), version 3. Three files of this project already hold theorems of the
book: `Register.lean` (Volume I, the register theorem), `Aufbau.lean` (Volume V, the filling
order) and `Reptend.lean` (the period, its three orders, the involution and the fold). This
file holds the rest of the book's finite arithmetic, volume by volume, each statement in the
book's own words:

* Volume I: the near-miss ladder; Midy's complement; the depth-three commitment and the
  commitment ladder; the two multipliers of the width-three register; the clock;
* Volume II: the square identity;
* Volume III: the charge table as the unique solution of its four constraints, with its
  corollaries; the multiplicity scan; the chain of states; the proton's spin content; the
  helium fraction;
* Volume IV: the electroweak expression and its registered alternative; the held chord;
* Volume VII: the budget, the baryon share, the deceleration and the turning points;
* Volume VIII: the node rule; Bell's bound for outcomes written in advance; the factorial
  count; Euclid's identity; the ladder of ceilings;
* Volume IX: the rows of Pascal's triangle and the diffusion identity;
* Volume X: the triple lattice;
* the Mathematical Companion: the reptend classes of four primes and the complete figure;
* In Pure Mathematics: exact rounding (Theorem 6) and the geometric demand (Theorem 13).

The identifications of the book — which of these structures nature realizes — are the book's
readings and hypotheses, and no statement of this file. Measured values do not enter.
-/
import Mathlib.Tactic
import Mathlib.Analysis.SpecialFunctions.Trigonometric.Basic
import GTheory.Coupling

namespace GTheory.Origin

open GTheory.Coupling

/-! ## Volume I · Initial Conditions -/

/-- **The near-miss ladder.** The near-misses |2ᵃ − 3ᵇ| at the successive convergents
(a, b) = (3, 2), (5, 3), (6, 4), (8, 5), (11, 7) are 1, 5, 17, 13, 139. -/
theorem near_miss_ladder :
    3 ^ 2 - 2 ^ 3 = 1 ∧ 2 ^ 5 - 3 ^ 3 = 5 ∧ 3 ^ 4 - 2 ^ 6 = 17 ∧ 2 ^ 8 - 3 ^ 5 = 13 ∧
    3 ^ 7 - 2 ^ 11 = 139 := by
  decide

/-- **Midy's complement.** 142 + 857 = 999, because 7 divides 10³ + 1. -/
theorem midy_complement : 142 + 857 = 999 ∧ 7 ∣ 10 ^ 3 + 1 ∧ 10 ^ 3 + 1 = 7 * 143 := by
  decide

/-- **The depth-three commitment is exact.** 0.143 × 7 = 1.001, so rounding 1/7 at depth
three is precisely a multiplication by 1001/1000. -/
theorem depth_three_commitment :
    (143 : ℚ) / 1000 * 7 = 1001 / 1000 ∧ (143 : ℚ) / 1000 = 1 / 7 * (1001 / 1000) := by
  norm_num

/-- **The commitment ladder.** Rounding the first period at depths three, four and five
lifts the last digit kept: 142 to 143, 1428 to 1429, 14285 to 14286, that is 2 → 3, 8 → 9
and 5 → 6. (Rounding half up of 10ᵏ/7 is ⌊(2·10ᵏ + 7)/14⌋.) -/
theorem commitment_ladder :
    (10 ^ 3 / 7 = 142 ∧ (2 * 10 ^ 3 + 7) / 14 = 143) ∧
    (10 ^ 4 / 7 = 1428 ∧ (2 * 10 ^ 4 + 7) / 14 = 1429) ∧
    (10 ^ 5 / 7 = 14285 ∧ (2 * 10 ^ 5 + 7) / 14 = 14286) := by
  decide

/-- **The two multipliers of the width-three register.** For any three-digit a,
a · 1001 is the block a written twice, and a · 999 is the pair (a − 1) | (1000 − a), whose
halves sum to 999. -/
theorem two_multipliers (a : ℕ) (h₁ : 100 ≤ a) (h₂ : a < 1000) :
    a * 1001 = a * 1000 + a ∧ a * 999 = (a - 1) * 1000 + (1000 - a) ∧
    (a - 1) + (1000 - a) = 999 := by
  omega

/-- **One number connects the two multipliers.** 1/7 = 143/1001 exactly, and
143 × 999 = 142857, the period itself; 10⁶ − 1 = 999 · 1001, 1001 = 7 · 11 · 13 and
999 = 27 · 37. -/
theorem period_from_the_multipliers :
    (1 : ℚ) / 7 = 143 / 1001 ∧ 143 * 999 = 142857 ∧ 10 ^ 6 - 1 = 999 * 1001 ∧
    1001 = 7 * 11 * 13 ∧ 999 = 27 * 37 := by
  refine ⟨by norm_num, by decide, by decide, by decide, by decide⟩

/-- **The clock.** The 3-step on the 8-ring visits all eight positions and closes at
lcm(3, 8) = 24. -/
theorem escapement :
    Nat.lcm 3 8 = 24 ∧ (List.range 8).map (fun k => 3 * k % 8) = [0, 3, 6, 1, 4, 7, 2, 5] := by
  decide

/-! ## Volume II · The Dipole -/

/-- **Theorem 3 (the square identity).** At m = 2 the equal mixture is identically the
square of the dipole term: 1 + cos 2θ = 2 cos²θ. -/
theorem square_identity (θ : ℝ) : 1 + Real.cos (2 * θ) = 2 * Real.cos θ ^ 2 := by
  rw [Real.cos_two_mul]
  ring

/-! ## Volume III · First Particles -/

/-- **Theorem 1 (the charge table).** Under closure at multiplicity three, the unit step
between weak partners, and the neutral axis, the charge assignment is unique:
2/3, −1/3, −1, 0. -/
theorem charge_table_unique (qu qd qe qn : ℚ)
    (closure : 3 * qu + 3 * qd + qe + qn = 0) (step₁ : qu - qd = 1) (step₂ : qn - qe = 1)
    (axis : qn = 0) : qu = 2 / 3 ∧ qd = -1 / 3 ∧ qe = -1 ∧ qn = 0 := by
  refine ⟨by linarith, by linarith, by linarith, axis⟩

/-- **Corollaries.** The proton (uud) carries +1, the neutron (udd) 0, and hydrogen
(p + e) 0, exactly. -/
theorem charge_corollaries :
    (2 / 3 : ℚ) + 2 / 3 + (-1 / 3) = 1 ∧ (2 / 3 : ℚ) + (-1 / 3) + (-1 / 3) = 0 ∧
    (1 : ℚ) + (-1) = 0 := by
  norm_num

/-- **The multiplicity scan.** With multiplicity m the down-type charge is (1 − m)/2m,
whose denominator in lowest terms is 2m / gcd(m − 1, 2m). Among m = 1 … 12 that denominator
is three only at m = 3. -/
theorem only_three_gives_thirds (m : ℕ) (h₁ : 1 ≤ m) (h₂ : m ≤ 12) :
    2 * m / Nat.gcd (m - 1) (2 * m) = 3 ↔ m = 3 := by
  interval_cases m <;> decide

/-- **The chain of states.** From the base 1008 = 42 × 24: the rest value 1008 × 1/7 = 144;
the echo 1008 × 0.143 = 144.144; the split 144 × 999 = 143 | 856, complements summing to
999. -/
theorem chain_of_states :
    1008 = 42 * 24 ∧ (1008 : ℚ) * (1 / 7) = 144 ∧ (1008 : ℚ) * (143 / 1000) = 144144 / 1000 ∧
    144 * 999 = 143 * 1000 + 856 ∧ 143 + 856 = 999 := by
  refine ⟨by decide, by norm_num, by norm_num, by decide, by decide⟩

/-- **The proton's spin content.** With Δu = 4/3 and Δd = −1/3 the net is 1 and the
gross, which is the axial charge Δu − Δd, is 5/3. -/
theorem proton_spin_content :
    (4 / 3 : ℚ) + (-1 / 3) = 1 ∧ (4 / 3 : ℚ) - (-1 / 3) = 5 / 3 := by
  norm_num

/-- **Three to one.** The ratio n/p = 1/7 gives a neutron fraction of 1/8 and a helium
mass fraction of exactly 1/4. -/
theorem three_to_one : ((1 : ℚ) / 7) / (1 + 1 / 7) = 1 / 8 ∧ 2 * ((1 : ℚ) / 8) = 1 / 4 := by
  norm_num

/-! ## Volume IV · Plasmas -/

/-- **The electroweak expression.** (m_W/m_Z)² = (8/9)² − 13/1000 = 62947/81000; the
leading term is 1 − 17/81; the two coefficients are the ladder's gaps 13 = 2⁸ − 3⁵ and
17 = 3⁴ − 2⁶; the registered alternative, with 1/75 for 13/1000, is 1573/2025. -/
theorem electroweak_expression :
    ((8 : ℚ) / 9) ^ 2 - 13 / 1000 = 62947 / 81000 ∧ ((8 : ℚ) / 9) ^ 2 = 1 - 17 / 81 ∧
    2 ^ 8 - 3 ^ 5 = 13 ∧ 3 ^ 4 - 2 ^ 6 = 17 ∧ ((8 : ℚ) / 9) ^ 2 - 1 / 75 = 1573 / 2025 := by
  refine ⟨by norm_num, by norm_num, by decide, by decide, by norm_num⟩

/-- **The held chord.** 63/32 = 2 − 1/32, and its gap to the octave is exactly the
septimal comma 64/63. -/
theorem held_chord :
    (63 : ℚ) / 32 = 2 - 1 / 32 ∧ (2 : ℚ) / (63 / 32) = 64 / 63 ∧ 64 = 2 ^ 6 ∧ 63 = 3 ^ 2 * 7 := by
  refine ⟨by norm_num, by norm_num, by decide, by decide⟩

/-! ## Volume VII · The Path to the Present -/

/-- **The budget closes exactly.** 2/3 + 4/15 + 1/15 = 1; fifteen is the first operation's
internal interval, 57 − 42; the dark-matter share is (1/7 + 3/7)/(15/7) = 4/15. -/
theorem budget_closes :
    (2 / 3 : ℚ) + 4 / 15 + 1 / 15 = 1 ∧ 57 - 42 = 15 ∧
    ((1 : ℚ) / 7 + 3 / 7) / (15 / 7) = 4 / 15 := by
  refine ⟨by norm_num, by decide, by norm_num⟩

/-- **The baryon share.** 1/15 = 27/405 = 20/405 + 7/405, the 20 | 7 of the reptend's
half-blocks (8 + 5 + 7 and 1 + 4 + 2); the committed share is (2/9)² = 4/81; the effective
vacuum share is 2/3 + 7/405 = 277/405; and the budget still closes. -/
theorem baryon_share :
    (1 : ℚ) / 15 = 20 / 405 + 7 / 405 ∧ ((2 : ℚ) / 9) ^ 2 = 4 / 81 ∧ (4 : ℚ) / 81 = 20 / 405 ∧
    (2 : ℚ) / 3 + 7 / 405 = 277 / 405 ∧ (277 : ℚ) / 405 + 108 / 405 + 20 / 405 = 1 ∧
    8 + 5 + 7 = 20 ∧ 1 + 4 + 2 = 7 := by
  refine ⟨by norm_num, by norm_num, by norm_num, by norm_num, by norm_num, by decide, by decide⟩

/-- **The deceleration and the turning points.** At the rest values Ω_m = 1/3 and
Ω_Λ = 2/3: q₀ = Ω_m/2 − Ω_Λ = −1/2; acceleration begins where (1 + z)³ = 2Ω_Λ/Ω_m = 4, and
equality falls where (1 + z)³ = Ω_Λ/Ω_m = 2. -/
theorem deceleration_and_turning_points :
    ((1 : ℚ) / 3) / 2 - 2 / 3 = -1 / 2 ∧ 2 * ((2 : ℚ) / 3) / (1 / 3) = 4 ∧
    ((2 : ℚ) / 3) / (1 / 3) = 2 := by
  norm_num

/-! ## Volume VIII · Modern Physics -/

/-- **The node rule, in its arithmetic.** For a reduced position p/q, the mode m has a
node there exactly when m·p/q is a whole number, and that holds if and only if q divides m. -/
theorem node_rule (p q m : ℕ) (h : Nat.Coprime p q) : q ∣ m * p ↔ q ∣ m :=
  (Nat.Coprime.symm h).dvd_mul_right

/-- The sign ±1 of an outcome written in advance. -/
def sign (x : Bool) : ℤ := if x then 1 else -1

/-- **Bell's bound as a counting fact.** For outcomes written in advance, with two
settings on each wing and answers ±1, every one of the sixteen assignments gives |S| = 2,
and so satisfies |S| ≤ 2. -/
theorem rest_ceiling (a a' b b' : Bool) :
    (sign a * sign b + sign a * sign b' + sign a' * sign b - sign a' * sign b').natAbs = 2 := by
  cases a <;> cases a' <;> cases b <;> cases b' <;> decide

/-- **The factorial count.** Ten constituents stand at 3.6 million phase relations, and
twenty exceed 10¹⁸. -/
theorem factorial_count : Nat.factorial 10 = 3628800 ∧ 10 ^ 18 < Nat.factorial 20 := by
  decide

/-- **Duality is Euclid's identity.** (a² − b²)² + (2ab)² = (a² + b²)². -/
theorem euclid_identity (a b : ℚ) : (a ^ 2 - b ^ 2) ^ 2 + (2 * a * b) ^ 2 = (a ^ 2 + b ^ 2) ^ 2 := by
  ring

/-- **The ladder of ceilings**, in squares: the pre-written bound 2, the carry machine's
5/2 (the arithmetic mean of two and three), the quantum maximum 2√2 (whose square is
2² + 2² = 8), the supremum 3 and the logical maximum 4 stand in that order. -/
theorem ladder_of_ceilings :
    (5 / 2 : ℚ) = (2 + 3) / 2 ∧ (2 : ℚ) ^ 2 < (5 / 2) ^ 2 ∧ ((5 : ℚ) / 2) ^ 2 < 2 ^ 2 + 2 ^ 2 ∧
    (2 : ℚ) ^ 2 + 2 ^ 2 < 3 ^ 2 ∧ (3 : ℚ) ^ 2 < 4 ^ 2 := by
  norm_num

/-! ## Volume IX · Position and Diffusion -/

/-- **The kernel is Pascal's triangle.** The rows sum to 2ⁿ. -/
theorem rows_sum (n : ℕ) : ∑ k ∈ Finset.range (n + 1), n.choose k = 2 ^ n :=
  Nat.sum_range_choose n

/-- The kernel is symmetric: C(n, k) = C(n, n − k). -/
theorem kernel_symmetric (n k : ℕ) (h : k ≤ n) : n.choose (n - k) = n.choose k :=
  Nat.choose_symm h

/-- **The diffusion law, by counting**, for walks of up to twelve steps: the sum of
C(n, k)·(n − 2k)² over k is n·2ⁿ, so the mean-square displacement after n steps is n. -/
theorem diffusion_identity (n : ℕ) (h : n ≤ 12) :
    ∑ k ∈ Finset.range (n + 1), (n.choose k : ℤ) * ((n : ℤ) - 2 * (k : ℤ)) ^ 2 = (n : ℤ) * 2 ^ n := by
  interval_cases n <;> decide

/-! ## Volume X · Relativity and the Standard Model -/

/-- **The triple lattice.** At β = 3/5, 5/13, 8/17 and 20/29 the internal rate is the
rational 4/5, 12/13, 15/17 and 21/29: rate² + β² = 1 exactly. -/
theorem triple_lattice :
    ((3 : ℚ) / 5) ^ 2 + (4 / 5) ^ 2 = 1 ∧ ((5 : ℚ) / 13) ^ 2 + (12 / 13) ^ 2 = 1 ∧
    ((8 : ℚ) / 17) ^ 2 + (15 / 17) ^ 2 = 1 ∧ ((20 : ℚ) / 29) ^ 2 + (21 / 29) ^ 2 = 1 := by
  norm_num

/-! ## The Mathematical Companion -/

/-- **Reptend classes of four primes in base ten.** The class count is (p − 1)/ord_p(10):
one for 7 (order 6), two for 13 (order 6), one for 17 (order 16), five for 11 (order 2). -/
theorem reptend_classes :
    (Period 10 7 6 ∧ (7 - 1) / 6 = 1) ∧ (Period 10 13 6 ∧ (13 - 1) / 6 = 2) ∧
    (Period 10 17 16 ∧ (17 - 1) / 16 = 1) ∧ (Period 10 11 2 ∧ (11 - 1) / 2 = 5) := by
  decide

/-- **Theorem M2, parts 3 and 4.** The residues the path 1 → 4 → 2 → 8 → 5 → 7 never
touches are exactly 3, 6, 9; and the reflection d ↦ 9 − d is the half-period shift, sending
1, 4, 2, 8, 5, 7 to 8, 5, 7, 1, 4, 2. -/
theorem complete_figure :
    (List.range 10).filter (fun d => 1 ≤ d ∧ d ∉ [1, 4, 2, 8, 5, 7]) = [3, 6, 9] ∧
    [1, 4, 2, 8, 5, 7].map (fun d => 9 - d) = [8, 5, 7, 1, 4, 2] := by
  decide

/-! ## In Pure Mathematics -/

/-- **Theorem 6 (exact rounding).** Rounding 1/7 to k places multiplies it by exactly
1 + 10⁻³ at k = 3 and 1 − 10⁻⁶ at k = 6; at k = 4 and 5 the excesses are 3·10⁻⁴ and
2·10⁻⁵. -/
theorem exact_rounding :
    (143 : ℚ) / 10 ^ 3 = 1 / 7 * (1 + 1 / 10 ^ 3) ∧
    (142857 : ℚ) / 10 ^ 6 = 1 / 7 * (1 - 1 / 10 ^ 6) ∧
    (1429 : ℚ) / 10 ^ 4 = 1 / 7 * (1 + 3 / 10 ^ 4) ∧
    (14286 : ℚ) / 10 ^ 5 = 1 / 7 * (1 + 2 / 10 ^ 5) := by
  norm_num

/-- **Theorem 13, second clause (the geometric demand).** The sum of 8ⁿ for n from 0 to N
is (8^(N+1) − 1)/7. -/
theorem geometric_demand (N : ℕ) :
    ∑ n ∈ Finset.range (N + 1), 8 ^ n = (8 ^ (N + 1) - 1) / 7 :=
  Nat.geomSum_eq (by norm_num) (N + 1)

end GTheory.Origin
