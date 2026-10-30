/-
# The reptend of seven: the cycle, the label set, the anchors, the transform, the fold

Source: "The Seventh — A Constant Hidden in Plain Sight" (Christian Horstmann, DOI
10.5281/zenodo.21206863). Its four exhibits, in the record's words:

* The cycle (§2). The six fractions k/7 have one decimal expansion: each period is a
  rotation of the single string 142857, and the six rotations are distinct. Seven is the
  least prime for which base ten does this; the full-period primes below twenty are 7, 17
  and 19, and nothing smaller qualifies.
* The label set (§3). The six sevenths index the first six harmonics, and they are the
  smallest complete such label set: every denominator below seven terminates, repeats
  short, or collapses to fewer than six distinct labels.
* The anchors (§4). Normalized by their largest member, (k/7) ÷ (6/7) = k/6, the six
  sevenths become 1/6, 1/3, 1/2, 2/3, 5/6, 1, and reduced into one octave exactly three
  pitch classes remain: 2/3 (Fa), 1 (Do), 5/6 (La). Re, Mi, Sol and Si are visited by
  no seventh.
* The transform (§5). The reptend cycle has three orders: positional 142857, multiplicative
  124875 (the doubling orbit of 1 modulo nine), harmonic 124578 (the first digit of
  k/7). Split 142857 = 1 | 42 | 8 | 57 and reverse each interior pair: 1 | 24 | 8 | 75 =
  124875, the multiplicative order exactly; 42 falls by 18 and 57 rises by 18, net zero,
  42 + 57 = 99 = 24 + 75, and the pair-differences 57 − 42 = 15 and 75 − 24 = 51 are the
  same two digits transposed. Equivalently, substitute 2 ↔ 4 and 5 ↔ 7 with the axis
  {1, 8} fixed — the Midy pair, summing to nine.
* The fold (§6). Separate the family at Midy's axis: the upper sum to the lower sum is
  (4/7 + 5/7 + 6/7) / (1/7 + 2/7 + 3/7) = 5/2; the whole is 3; the centroids are 5/7 and
  2/7, a Midy pair. Truncate all six sevenths at six digits and the family falls short
  of its whole by exactly 3 × 10⁻⁶; exactly the upper three round up, and their three
  unit corrections restore it: 0.857142 + 2.142858 = 3.000000. For every odd prime at its
  period depth the number of rounders equals the truncation deficit in last-digit units,
  so the committed total is (p − 1)/2 exactly. The ratio generalizes as (3p − 1)/(p + 1):
  2 at p = 3, 5/2 at p = 7, 3 in the limit and never arriving; it equals 5/2 at p = 7
  alone, and the whole (p − 1)/2 coincides with the limit 3 at p = 7 alone.

Every statement below is arithmetic and is proved as arithmetic. The naming of the cycle
as a constant, and the reading of the anchors as tonal functions, are the record's, stated
there and not here.
-/
import Mathlib.Tactic
import GTheory.Coupling

namespace GTheory.Reptend

open GTheory.Coupling (Period)

/-! ## The cycle -/

/-- One-seventh has period six in base ten: 10⁶ ≡ 1 (mod 7) and no smaller power is. -/
theorem period_six : Period 10 7 6 := by decide

/-- 7 · 142857 = 999999: the period is the reptend of one-seventh. -/
theorem reptend : 7 * 142857 = 999999 := by norm_num

/-- Rotating the string 142857 by d digits, as arithmetic on the number. -/
def rotate (d : ℕ) : ℕ := (142857 % 10 ^ (6 - d)) * 10 ^ d + 142857 / 10 ^ (6 - d)

/-- **One expansion, six rotations.** The multiples 2 through 6 of 142857 are its own
rotations, by 2, 1, 4, 5 and 3 digits respectively, and the six rotations are distinct. -/
theorem six_rotations :
    rotate 0 = 1 * 142857 ∧ rotate 2 = 2 * 142857 ∧ rotate 1 = 3 * 142857 ∧
    rotate 4 = 4 * 142857 ∧ rotate 5 = 5 * 142857 ∧ rotate 3 = 6 * 142857 ∧
    ((List.range 6).map rotate).Nodup := by
  decide

/-- The primes below twenty. -/
theorem primes_below_twenty (p : ℕ) (hp : p < 20) :
    Nat.Prime p ↔ p = 2 ∨ p = 3 ∨ p = 5 ∨ p = 7 ∨ p = 11 ∨ p = 13 ∨ p = 17 ∨ p = 19 := by
  interval_cases p <;> norm_num

/-- **The least prime.** Among the primes below twenty, the full period p − 1 occurs for
7, 17 and 19 and nothing smaller. -/
theorem full_period_primes_below_twenty (p : ℕ) (hp : p < 20) (hprime : Nat.Prime p) :
    Period 10 p (p - 1) ↔ p = 7 ∨ p = 17 ∨ p = 19 := by
  interval_cases p <;> first | decide | (exfalso; norm_num at hprime)

/-! ## The label set -/

/-- **Smallest complete label set.** No denominator below seven has the full period:
2 and 5 divide ten and 4 does after two digits, 3 repeats with period one, and 6 never
returns to one at all. -/
theorem no_smaller_denominator_has_the_full_period :
    ∀ d, 2 ≤ d → d < 7 → ¬ Period 10 d (d - 1) := by
  decide

/-- And below seven a denominator offers at most five labels, fewer than the six the
harmonics need. -/
theorem fewer_than_six_labels_below_seven : ∀ d, 2 ≤ d → d < 7 → d - 1 < 6 := by
  decide

/-! ## The anchors -/

/-- **The normalization.** (k/7) ÷ (6/7) = k/6 for the six sevenths. -/
theorem normalization :
    (1 / 7 : ℚ) / (6 / 7) = 1 / 6 ∧ (2 / 7 : ℚ) / (6 / 7) = 1 / 3 ∧
    (3 / 7 : ℚ) / (6 / 7) = 1 / 2 ∧ (4 / 7 : ℚ) / (6 / 7) = 2 / 3 ∧
    (5 / 7 : ℚ) / (6 / 7) = 5 / 6 ∧ (6 / 7 : ℚ) / (6 / 7) = 1 := by
  norm_num

/-- **The reduction into one octave.** Each normalized value, doubled until it lies in
(1/2, 1], lands on one of exactly three values: 2/3, 1, 5/6. -/
theorem three_anchors :
    (1 / 6 : ℚ) * 4 = 2 / 3 ∧ (1 / 3 : ℚ) * 2 = 2 / 3 ∧ (1 / 2 : ℚ) * 2 = 1 ∧
    (2 / 3 : ℚ) * 1 = 2 / 3 ∧ (5 / 6 : ℚ) * 1 = 5 / 6 ∧ (1 : ℚ) * 1 = 1 ∧
    ((1 / 2 : ℚ) < 2 / 3 ∧ (2 / 3 : ℚ) ≤ 1) ∧ ((1 / 2 : ℚ) < 5 / 6 ∧ (5 / 6 : ℚ) ≤ 1) := by
  norm_num

/-- **The silence.** The four remaining diatonic positions of the just lattice, reduced
into the same octave — Re 9/16, Mi 5/8, Sol 3/4, Si 15/16 — are visited by no seventh. -/
theorem four_silences :
    ((2 / 3 : ℚ) ≠ 9 / 16 ∧ (2 / 3 : ℚ) ≠ 5 / 8 ∧ (2 / 3 : ℚ) ≠ 3 / 4 ∧ (2 / 3 : ℚ) ≠ 15 / 16) ∧
    ((5 / 6 : ℚ) ≠ 9 / 16 ∧ (5 / 6 : ℚ) ≠ 5 / 8 ∧ (5 / 6 : ℚ) ≠ 3 / 4 ∧ (5 / 6 : ℚ) ≠ 15 / 16) ∧
    ((1 : ℚ) ≠ 9 / 16 ∧ (1 : ℚ) ≠ 5 / 8 ∧ (1 : ℚ) ≠ 3 / 4 ∧ (1 : ℚ) ≠ 15 / 16) := by
  norm_num

/-! ## The transform -/

/-- The three orders of the reptend cycle, as digit lists. -/
def positional : List ℕ := [1, 4, 2, 8, 5, 7]
def multiplicative : List ℕ := [1, 2, 4, 8, 7, 5]
def harmonic : List ℕ := [1, 2, 4, 5, 7, 8]

/-- The positional order is the period as written. -/
theorem positional_is_the_period : Nat.ofDigits 10 positional.reverse = 142857 := by
  norm_num [positional, Nat.ofDigits]

/-- **The multiplicative order is the doubling orbit of 1 modulo nine**:
1, 2, 4, 8, 16 ≡ 7, 14 ≡ 5. -/
theorem multiplicative_is_the_doubling_orbit :
    (List.range 6).map (fun k => 2 ^ k % 9) = multiplicative := by
  decide

/-- **The harmonic order is the first digit of k/7**, ⌊10k/7⌋ for k = 1 … 6. -/
theorem harmonic_is_the_first_digit :
    (List.range 6).map (fun k => 10 * (k + 1) / 7) = harmonic := by
  decide

/-- The three orders are three arrangements of the same six digits, which skip 3, 6, 9. -/
theorem same_digits :
    positional.toFinset = multiplicative.toFinset ∧
    multiplicative.toFinset = harmonic.toFinset ∧
    ∀ x ∈ positional, x % 3 ≠ 0 := by
  decide

/-- **The split and the exchange.** 142857 = 1 | 42 | 8 | 57; reversing each interior
pair gives 1 | 24 | 8 | 75 = 124875, the multiplicative order exactly. -/
theorem split_and_exchange :
    142857 = 1 * 10 ^ 5 + 42 * 10 ^ 3 + 8 * 10 ^ 2 + 57 ∧
    124875 = 1 * 10 ^ 5 + 24 * 10 ^ 3 + 8 * 10 ^ 2 + 75 ∧
    Nat.ofDigits 10 multiplicative.reverse = 124875 := by
  norm_num [multiplicative, Nat.ofDigits]

/-- **The conservation.** 42 falls by 18 and 57 rises by 18; 42 + 57 = 99 = 24 + 75;
the pair-differences 15 and 51 are the same two digits transposed. -/
theorem conservation :
    42 - 24 = 18 ∧ 75 - 57 = 18 ∧ 42 + 57 = 99 ∧ 24 + 75 = 99 ∧
    57 - 42 = 15 ∧ 75 - 24 = 51 ∧ 15 = 1 * 10 + 5 ∧ 51 = 5 * 10 + 1 := by
  decide

/-- The substitution 2 ↔ 4, 5 ↔ 7 with 1 and 8 fixed. -/
def swap : ℕ → ℕ
  | 2 => 4 | 4 => 2 | 5 => 7 | 7 => 5 | n => n

/-- **The second realization.** The same substitution carries the positional order to
the multiplicative order; each moving pair is a doubling pair modulo nine, and the fixed
axis {1, 8} is the Midy pair, summing to nine. -/
theorem substitution_realization :
    positional.map swap = multiplicative ∧
    2 * 2 % 9 = 4 ∧ 2 * 7 % 9 = 5 ∧ 1 + 8 = 9 ∧ swap 1 = 1 ∧ swap 8 = 8 := by
  decide

/-! ## The fold -/

/-- **The separation at Midy's axis.** Upper sum to lower sum is 5/2, the whole is 3, and the
centroids 5/7 and 2/7 are a Midy pair whose ratio is again 5/2. -/
theorem the_cut :
    ((4 / 7 : ℚ) + 5 / 7 + 6 / 7) / (1 / 7 + 2 / 7 + 3 / 7) = 5 / 2 ∧
    (1 / 7 : ℚ) + 2 / 7 + 3 / 7 + 4 / 7 + 5 / 7 + 6 / 7 = 3 ∧
    ((4 / 7 : ℚ) + 5 / 7 + 6 / 7) / 3 = 5 / 7 ∧ ((1 / 7 : ℚ) + 2 / 7 + 3 / 7) / 3 = 2 / 7 ∧
    (5 / 7 : ℚ) + 2 / 7 = 1 ∧ (5 / 7 : ℚ) / (2 / 7) = 5 / 2 ∧ 5 + 2 = 7 := by
  norm_num

/-- The six sevenths truncated at six digits, as integers in units of 10⁻⁶. -/
def truncated (k : ℕ) : ℕ := 10 ^ 6 * k / 7

/-- The remainder that truncation discards, in sevenths of the last unit. -/
def remainder (k : ℕ) : ℕ := 10 ^ 6 * k % 7

/-- **The committed whole.** The six truncations sum to 2999997, short of the whole
3000000 by exactly 3; the discarded remainders are 1, 2, 3, 4, 5, 6 sevenths; exactly the
upper three, whose remainders exceed half, round up; and their three unit corrections
restore the whole: 857142 + 2142858 = 3000000. -/
theorem committed_whole :
    ((List.range 6).map (fun i => truncated (i + 1))).sum = 2999997 ∧
    3000000 - 2999997 = 3 ∧
    (List.range 6).map (fun i => remainder (i + 1)) = [1, 2, 3, 4, 5, 6] ∧
    ((List.range 6).filter (fun i => 2 * remainder (i + 1) ≥ 7)).length = 3 ∧
    truncated 1 + truncated 2 + truncated 3 = 857142 ∧
    (truncated 4 + 1) + (truncated 5 + 1) + (truncated 6 + 1) = 2142858 ∧
    857142 + 2142858 = 3000000 := by
  decide

/-- The deficit in the record's units: 3 − 2999997/10⁶ = 3 × 10⁻⁶. -/
theorem deficit_is_three_millionths : (3 : ℚ) - 2999997 / 10 ^ 6 = 3 / 10 ^ 6 := by
  norm_num

/-- For a prime p with period L, the discarded remainders of k/p at depth L, in
p-ths of the last unit, and the rounders (those exceeding one half). -/
def deficitUnits (p L : ℕ) : ℕ := ((List.range (p - 1)).map (fun i => 10 ^ L * (i + 1) % p)).sum / p
def rounders (p L : ℕ) : ℕ :=
  ((List.range (p - 1)).filter (fun i => 2 * (10 ^ L * (i + 1) % p) ≥ p)).length

/-- **Rounders equal the deficit at every odd prime with a period, 3 through 23**, and
both equal (p − 1)/2: at 3 (period 1), 7 (6), 11 (2), 13 (6), 17 (16), 19 (18), 23 (22).
Five is excluded because 1/5 terminates and has no period. -/
theorem committed_total_is_half_the_family :
    ∀ pL ∈ [(3, 1), (7, 6), (11, 2), (13, 6), (17, 16), (19, 18), (23, 22)],
      Period 10 pL.1 pL.2 ∧
      deficitUnits pL.1 pL.2 = (pL.1 - 1) / 2 ∧ rounders pL.1 pL.2 = (pL.1 - 1) / 2 := by
  decide

/-- **The fold family.** The ratio of the upper sum to the lower sum for the fractions of an odd prime
is (3p − 1)/(p + 1): 2 at p = 3, 5/2 at p = 7, and below 3 for every p. -/
theorem fold_family :
    ((3 * 3 - 1 : ℚ) / (3 + 1)) = 2 ∧ ((3 * 7 - 1 : ℚ) / (7 + 1)) = 5 / 2 ∧
    ∀ p : ℕ, ((3 * p - 1 : ℚ) / (p + 1)) < 3 := by
  refine ⟨by norm_num, by norm_num, fun p => ?_⟩
  rw [div_lt_iff₀ (by positivity)]
  linarith

/-- **5/2 at p = 7 alone.** -/
theorem five_halves_only_at_seven (p : ℕ) :
    ((3 * p - 1 : ℚ) / (p + 1)) = 5 / 2 ↔ p = 7 := by
  have hp : (p : ℚ) + 1 ≠ 0 := by positivity
  rw [div_eq_iff hp]
  constructor
  · intro h
    have : (p : ℚ) = 7 := by linarith
    exact_mod_cast this
  · rintro rfl
    norm_num

/-- **The whole meets the limit at p = 7 alone**: for odd p, (p − 1)/2 = 3 exactly when
p = 7. -/
theorem whole_meets_limit_only_at_seven (p : ℕ) (hodd : p % 2 = 1) :
    (p - 1) / 2 = 3 ↔ p = 7 := by
  omega

end GTheory.Reptend
