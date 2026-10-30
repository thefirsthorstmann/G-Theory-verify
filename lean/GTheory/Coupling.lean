/-
# The coupling's integer: the ring, the censuses, the block and the nucleon relation

Source: "The Fine-Structure Constant on Discrete Terms" (Christian Horstmann), version 2,
Sections 2 to 7. The record's statements, as it words them:

* Section 2. The integer is written in the alphabet of two, three and seven: 137 = 2⁷ + 3².
* Section 3. The second spelling is 137 = 8 · 17 + 1, with 17 = 3⁴ − 2⁶. The multiplicative
  order of ten modulo 137 is eight, so the one hundred thirty-six non-zero fractions over the
  prime fall into exactly seventeen cyclic families of period eight. A prime of decimal period
  eight must divide 10⁸ − 1 = 3² · 11 · 73 · 101 · 137, so the primes whose ring closes at the
  octave are exactly two, 73 and 137, and their product is the palindrome 10001. The census
  of the short periods is equally closed: period one {3}, two {11}, three {37}, four {101},
  five {41, 271}, six {7, 13}, seven {239, 4649}, eight {73, 137}.
* Section 4. The period block of 1/137 is 00729927; its halves sum to 9999, each of the four
  digit-pairs across the split sums to nine, 72 + 27 = 99, and every fraction over the prime
  carries the four-nines complement.
* Section 5. The censuses: the integers in [100, 200] of the form 2ᵃ + 3ᵇ are 113, 131, 137,
  145, 155; of the thirty-five primes below 150, two close at the octave.
* Section 6. The numerator 36 = lcm(9, 12) = 1008 ÷ 28 = 24 × 3/2; 137.036 stands 6.0 parts
  per billion above the CODATA 2022 value; the run of nines is the borrow of the offset; and
  twenty-eight times the tail against the mean of the proton and neutron masses.
* Section 7. 28 × 0.036 = 1.008; the stations −72 and +66 about that base; the two integers
  3 × 10⁸ and 3 × (10⁸ − 1), their factorizations, and their gap of three.

What is proved here is arithmetic. That 137 is the integer at the head of the fine-structure
constant is the record's identification, stated there, and not a theorem of this file. Where
a statement compares with measurement it is exact rational arithmetic on the central values
the record quotes: the CODATA 2022 and 2018 values of the inverse constant, the three
determinations of 2018, 2020 and 2023, and the CODATA 2022 proton and neutron masses in
atomic mass units. A count in standard deviations uses the published uncertainty it names.
-/
import Mathlib.Tactic

namespace GTheory.Coupling

/-- `Period b p k`: the multiplicative order of b modulo p is exactly k — bᵏ ≡ 1 and no
smaller positive power is. For a prime p not dividing b this is the length of the
repeating block of 1/p written in base b. -/
def Period (b p k : ℕ) : Prop :=
  b ^ k % p = 1 ∧ ∀ j, 1 ≤ j → j < k → b ^ j % p ≠ 1

instance (b p k : ℕ) : Decidable (Period b p k) :=
  inferInstanceAs (Decidable (b ^ k % p = 1 ∧ ∀ j, 1 ≤ j → j < k → b ^ j % p ≠ 1))

/-! ## Section 2 · The alphabet -/

/-- **The three spellings.** 137 = 2⁷ + 3², 17 = 3⁴ − 2⁶ and 137 = 8 · 17 + 1. -/
theorem three_spellings : 137 = 2 ^ 7 + 3 ^ 2 ∧ 17 = 3 ^ 4 - 2 ^ 6 ∧ 137 = 8 * 17 + 1 := by
  decide

/-! ## Section 3 · The ring theorem and its scarcity -/

/-- 137 is prime. -/
theorem prime_137 : Nat.Prime 137 := by norm_num

/-- **Eight seventeens plus one.** -/
theorem closure_equation : 137 = 8 * 17 + 1 ∧ 136 = 8 * 17 := by norm_num

/-- **The ring theorem.** The multiplicative order of ten modulo 137 is eight. -/
theorem ring_theorem : Period 10 137 8 := by decide

/-- **Seventeen cyclic families of period eight.** Every non-zero residue r modulo 137
returns to itself after eight multiplications by ten and to nothing else before: its
orbit has exactly eight distinct members. The 136 residues therefore partition into
136 / 8 = 17 orbits. -/
theorem seventeen_families :
    (∀ r, 1 ≤ r → r < 137 →
      r * 10 ^ 8 % 137 = r ∧
      ((List.range 8).map (fun i => r * 10 ^ i % 137)).Nodup) ∧
    136 / 8 = 17 := by
  decide

/-- The factorization the scarcity rests on. -/
theorem ten_to_the_eight_minus_one : 10 ^ 8 - 1 = 3 ^ 2 * 11 * 73 * 101 * 137 := by
  norm_num

/-- A number of decimal period k divides 10ᵏ − 1. -/
theorem period_divides (p k : ℕ) (h : Period 10 p k) : p ∣ 10 ^ k - 1 := by
  have hd : p ∣ 10 ^ k - 10 ^ k % p := Nat.dvd_sub_mod (10 ^ k)
  rwa [h.1] at hd

/-- A prime of decimal period eight divides 10⁸ − 1. -/
theorem period_eight_divides (p : ℕ) (h : Period 10 p 8) : p ∣ 10 ^ 8 - 1 :=
  period_divides p 8 h

/-- **The five candidates.** A prime dividing 10⁸ − 1 is one of 3, 11, 73, 101, 137. -/
theorem the_five_candidates (p : ℕ) (hp : p.Prime) (h : p ∣ 10 ^ 8 - 1) :
    p = 3 ∨ p = 11 ∨ p = 73 ∨ p = 101 ∨ p = 137 := by
  rw [ten_to_the_eight_minus_one] at h
  rcases (Nat.Prime.dvd_mul hp).mp h with h | h
  · rcases (Nat.Prime.dvd_mul hp).mp h with h | h
    · rcases (Nat.Prime.dvd_mul hp).mp h with h | h
      · rcases (Nat.Prime.dvd_mul hp).mp h with h | h
        · exact Or.inl ((Nat.prime_dvd_prime_iff_eq hp Nat.prime_three).mp
            (hp.dvd_of_dvd_pow h))
        · exact Or.inr (Or.inl ((Nat.prime_dvd_prime_iff_eq hp (by norm_num)).mp h))
      · exact Or.inr (Or.inr (Or.inl ((Nat.prime_dvd_prime_iff_eq hp (by norm_num)).mp h)))
    · exact Or.inr (Or.inr (Or.inr (Or.inl
        ((Nat.prime_dvd_prime_iff_eq hp (by norm_num)).mp h))))
  · exact Or.inr (Or.inr (Or.inr (Or.inr
      ((Nat.prime_dvd_prime_iff_eq hp (by norm_num)).mp h))))

/-- The periods of the five candidates: 1, 2, 8, 4, 8. -/
theorem periods_of_the_five :
    Period 10 3 1 ∧ Period 10 11 2 ∧ Period 10 73 8 ∧ Period 10 101 4 ∧ Period 10 137 8 := by
  decide

/-- **The scarcity is closed.** Among all primes, the ring closes at the octave for
exactly two: 73 and 137. -/
theorem exactly_two_primes_close_at_the_octave (p : ℕ) (hp : p.Prime) :
    Period 10 p 8 ↔ p = 73 ∨ p = 137 := by
  constructor
  · intro h
    rcases the_five_candidates p hp (period_eight_divides p h) with rfl | rfl | rfl | rfl | rfl
    · exact absurd h (by decide)
    · exact absurd h (by decide)
    · exact Or.inl rfl
    · exact absurd h (by decide)
    · exact Or.inr rfl
  · rintro (rfl | rfl) <;> decide

/-- Their product is the palindrome 10001. -/
theorem palindrome : 73 * 137 = 10001 := by norm_num

/-- **Uniqueness.** The only prime whose ring closes at the octave with seventeen
families is 137; the other octave prime, 73, has nine. -/
theorem seventeen_families_only_at_137 (p : ℕ) (hp : p.Prime) (h8 : Period 10 p 8)
    (h17 : (p - 1) / 8 = 17) : p = 137 := by
  rcases (exactly_two_primes_close_at_the_octave p hp).mp h8 with rfl | rfl
  · norm_num at h17
  · rfl

/-- The factorizations the census of the short periods rests on: 10ᵏ − 1 for k from one to
seven. -/
theorem short_period_factorizations :
    10 ^ 1 - 1 = 3 ^ 2 ∧ 10 ^ 2 - 1 = 3 ^ 2 * 11 ∧ 10 ^ 3 - 1 = 3 ^ 3 * 37 ∧
    10 ^ 4 - 1 = 3 ^ 2 * 11 * 101 ∧ 10 ^ 5 - 1 = 3 ^ 2 * 41 * 271 ∧
    10 ^ 6 - 1 = 3 ^ 3 * 7 * 11 * 13 * 37 ∧ 10 ^ 7 - 1 = 3 ^ 2 * 239 * 4649 := by
  decide

private theorem eq_of_prime_dvd {p q : ℕ} (hp : p.Prime) (hq : q.Prime) (h : p ∣ q) : p = q :=
  (Nat.prime_dvd_prime_iff_eq hp hq).mp h

private theorem eq_of_prime_dvd_pow {p q n : ℕ} (hp : p.Prime) (hq : q.Prime) (h : p ∣ q ^ n) :
    p = q :=
  (Nat.prime_dvd_prime_iff_eq hp hq).mp (hp.dvd_of_dvd_pow h)

/-- **The census of the short periods is closed.** Among all primes: period one {3}, two
{11}, three {37}, four {101}, five {41, 271}, six {7, 13}, seven {239, 4649}. Period eight
is `exactly_two_primes_close_at_the_octave`. -/
theorem short_period_census_is_closed (p : ℕ) (hp : p.Prime) :
    (Period 10 p 1 ↔ p = 3) ∧ (Period 10 p 2 ↔ p = 11) ∧ (Period 10 p 3 ↔ p = 37) ∧
    (Period 10 p 4 ↔ p = 101) ∧ (Period 10 p 5 ↔ p = 41 ∨ p = 271) ∧
    (Period 10 p 6 ↔ p = 7 ∨ p = 13) ∧ (Period 10 p 7 ↔ p = 239 ∨ p = 4649) := by
  refine ⟨?_, ?_, ?_, ?_, ?_, ?_, ?_⟩
  · constructor
    · intro h
      have hd := period_divides p 1 h
      rw [show 10 ^ 1 - 1 = 3 ^ 2 by norm_num] at hd
      exact eq_of_prime_dvd_pow hp (by norm_num) hd
    · rintro rfl
      decide
  · constructor
    · intro h
      have hd := period_divides p 2 h
      rw [show 10 ^ 2 - 1 = 3 ^ 2 * 11 by norm_num] at hd
      rcases (Nat.Prime.dvd_mul hp).mp hd with hd | hd
      · obtain rfl := eq_of_prime_dvd_pow hp (by norm_num) hd
        exact absurd h (by decide)
      · exact eq_of_prime_dvd hp (by norm_num) hd
    · rintro rfl
      decide
  · constructor
    · intro h
      have hd := period_divides p 3 h
      rw [show 10 ^ 3 - 1 = 3 ^ 3 * 37 by norm_num] at hd
      rcases (Nat.Prime.dvd_mul hp).mp hd with hd | hd
      · obtain rfl := eq_of_prime_dvd_pow hp (by norm_num) hd
        exact absurd h (by decide)
      · exact eq_of_prime_dvd hp (by norm_num) hd
    · rintro rfl
      decide
  · constructor
    · intro h
      have hd := period_divides p 4 h
      rw [show 10 ^ 4 - 1 = 3 ^ 2 * 11 * 101 by norm_num] at hd
      rcases (Nat.Prime.dvd_mul hp).mp hd with hd | hd
      · rcases (Nat.Prime.dvd_mul hp).mp hd with hd | hd
        · obtain rfl := eq_of_prime_dvd_pow hp (by norm_num) hd
          exact absurd h (by decide)
        · obtain rfl := eq_of_prime_dvd hp (by norm_num) hd
          exact absurd h (by decide)
      · exact eq_of_prime_dvd hp (by norm_num) hd
    · rintro rfl
      decide
  · constructor
    · intro h
      have hd := period_divides p 5 h
      rw [show 10 ^ 5 - 1 = 3 ^ 2 * 41 * 271 by norm_num] at hd
      rcases (Nat.Prime.dvd_mul hp).mp hd with hd | hd
      · rcases (Nat.Prime.dvd_mul hp).mp hd with hd | hd
        · obtain rfl := eq_of_prime_dvd_pow hp (by norm_num) hd
          exact absurd h (by decide)
        · exact Or.inl (eq_of_prime_dvd hp (by norm_num) hd)
      · exact Or.inr (eq_of_prime_dvd hp (by norm_num) hd)
    · rintro (rfl | rfl) <;> decide
  · constructor
    · intro h
      have hd := period_divides p 6 h
      rw [show 10 ^ 6 - 1 = 3 ^ 3 * 7 * 11 * 13 * 37 by norm_num] at hd
      rcases (Nat.Prime.dvd_mul hp).mp hd with hd | hd
      · rcases (Nat.Prime.dvd_mul hp).mp hd with hd | hd
        · rcases (Nat.Prime.dvd_mul hp).mp hd with hd | hd
          · rcases (Nat.Prime.dvd_mul hp).mp hd with hd | hd
            · obtain rfl := eq_of_prime_dvd_pow hp (by norm_num) hd
              exact absurd h (by decide)
            · exact Or.inl (eq_of_prime_dvd hp (by norm_num) hd)
          · obtain rfl := eq_of_prime_dvd hp (by norm_num) hd
            exact absurd h (by decide)
        · exact Or.inr (eq_of_prime_dvd hp (by norm_num) hd)
      · obtain rfl := eq_of_prime_dvd hp (by norm_num) hd
        exact absurd h (by decide)
    · rintro (rfl | rfl) <;> decide
  · constructor
    · intro h
      have hd := period_divides p 7 h
      rw [show 10 ^ 7 - 1 = 3 ^ 2 * 239 * 4649 by norm_num] at hd
      rcases (Nat.Prime.dvd_mul hp).mp hd with hd | hd
      · rcases (Nat.Prime.dvd_mul hp).mp hd with hd | hd
        · obtain rfl := eq_of_prime_dvd_pow hp (by norm_num) hd
          exact absurd h (by decide)
        · exact Or.inl (eq_of_prime_dvd hp (by norm_num) hd)
      · exact Or.inr (eq_of_prime_dvd hp (by norm_num) hd)
    · rintro (rfl | rfl) <;> decide

/-! ## Section 4 · The backbone -/

/-- **The four-nines Midy complement.** The period block of 1/137 is 00729927, since
137 · 729927 = 10⁸ − 1, and its halves sum to 9999. -/
theorem midy_four_nines : 137 * 729927 = 10 ^ 8 - 1 ∧ 72 + 9927 = 9999 := by
  norm_num

/-- Each of the four digit-pairs across the split sums to nine, 0+9, 0+9, 7+2, 2+7, and read
in twos the block is 00 · 72 · 99 · 27 with 72 + 27 = 99. -/
theorem pairs_sum_to_nine :
    List.zipWith (· + ·) [0, 0, 7, 2] [9, 9, 2, 7] = [9, 9, 9, 9] ∧ 72 + 27 = 99 := by
  decide

/-- **Every fraction over the prime carries the four-nines complement.** For each of the 136
numerators r, the period block of r/137 is r · 729927, and its two halves sum to 9999. -/
theorem four_nines_across_the_ring :
    ∀ r < 137, 1 ≤ r → r * 729927 / 10 ^ 4 + r * 729927 % 10 ^ 4 = 9999 := by
  decide

/-- The two examples the record prints: 2/137 = .01459854 with 0145 + 9854 = 9999, and
3/137 = .02189781 with 0218 + 9781 = 9999. -/
theorem two_examples :
    2 * 729927 = 1459854 ∧ 145 + 9854 = 9999 ∧ 3 * 729927 = 2189781 ∧ 218 + 9781 = 9999 := by
  decide

/-! ## Section 5 · The censuses -/

/-- **The census of the spelling.** The integers in [100, 200] of the form 2ᵃ + 3ᵇ, with
both exponents at least one, are 113, 131, 137, 145 and 155: five in one hundred and one. -/
theorem spelling_census :
    (List.range 201).filter
        (fun n => 100 ≤ n ∧ ∃ a ∈ List.range 8, ∃ b ∈ List.range 5, 1 ≤ a ∧ 1 ≤ b ∧ n = 2 ^ a + 3 ^ b)
      = [113, 131, 137, 145, 155] := by
  decide

/-- The primes below one hundred and fifty. -/
def primesBelow150 : List ℕ :=
  [2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43, 47, 53, 59, 61, 67, 71, 73, 79, 83, 89, 97,
   101, 103, 107, 109, 113, 127, 131, 137, 139, 149]

/-- There are thirty-five of them, and the list is complete. -/
theorem thirty_five_primes_below_150 :
    primesBelow150.length = 35 ∧ ∀ p < 150, (Nat.Prime p ↔ p ∈ primesBelow150) := by
  refine ⟨by decide, ?_⟩
  intro p hp
  interval_cases p <;> simp [primesBelow150] <;> norm_num

/-- **The census of the period.** Of the thirty-five, the ring closes at the octave for two:
73 and 137. -/
theorem two_of_them_close_at_the_octave :
    primesBelow150.filter (fun p => decide (Period 10 p 8)) = [73, 137] := by
  decide

/-! ## Section 6 · The tail -/

/-- **The numerator is over-determined.** Thirty-six is the joint period of the nine-circle
and the twelve-tone octave, it is 1008 ÷ 28, and it is 24 × 3/2; 36 = 4 · 9 and
36/1000 = 9/250. -/
theorem numerator_thirty_six :
    Nat.lcm 9 12 = 36 ∧ 1008 / 28 = 36 ∧ 28 * 36 = 1008 ∧ 24 * 3 / 2 = 36 ∧ 36 = 4 * 9 ∧
    (36 : ℚ) / 1000 = 9 / 250 := by
  refine ⟨by decide, by decide, by decide, by decide, by decide, by norm_num⟩

/-- **6.0 parts per billion.** 137.036 stands above the CODATA 2022 value, 137.035999177, by
823 in the ninth decimal, which rounds to 6.0 parts per billion of that value. Above the 2018
value, 137.035999084, the gap rounds to 6.7. -/
theorem gap_from_the_2022_value :
    (137036 : ℚ) / 1000 - 137035999177 / 10 ^ 9 = 823 / 10 ^ 9 ∧
    (595 : ℚ) / 10 ^ 11 < 823 / 137035999177 ∧ (823 : ℚ) / 137035999177 < 605 / 10 ^ 11 ∧
    (137036 : ℚ) / 1000 - 137035999084 / 10 ^ 9 = 916 / 10 ^ 9 ∧
    (665 : ℚ) / 10 ^ 11 < 916 / 137035999084 ∧ (916 : ℚ) / 137035999084 < 675 / 10 ^ 11 := by
  norm_num

/-- **The three determinations lie below 137.036, by 5.8 to 7.0 parts per billion.** Caesium
(…046) by 7.0, rubidium (…206) by 5.8, the electron moment (…166) by 6.1. The two
interferometry values differ by 160 in the ninth decimal against uncertainties of 27 and 11,
which is more than five standard deviations of the difference. -/
theorem three_determinations_below :
    (695 : ℚ) / 10 ^ 11 < 954 / 137035999046 ∧ (954 : ℚ) / 137035999046 < 705 / 10 ^ 11 ∧
    (575 : ℚ) / 10 ^ 11 < 794 / 137035999206 ∧ (794 : ℚ) / 137035999206 < 585 / 10 ^ 11 ∧
    (605 : ℚ) / 10 ^ 11 < 834 / 137035999166 ∧ (834 : ℚ) / 137035999166 < 615 / 10 ^ 11 ∧
    206 - 46 = 160 ∧ 5 ^ 2 * (27 ^ 2 + 11 ^ 2) < 160 ^ 2 := by
  norm_num

/-- **The count in standard deviations runs from 35 to 72.** The same gap divided by four
published uncertainties: 954/27, 823/21, 834/15 and 794/11. -/
theorem standard_deviation_counts :
    (35 : ℚ) < 954 / 27 ∧ (954 : ℚ) / 27 < 36 ∧ (39 : ℚ) < 823 / 21 ∧ (823 : ℚ) / 21 < 40 ∧
    (55 : ℚ) < 834 / 15 ∧ (834 : ℚ) / 15 < 56 ∧ (72 : ℚ) < 794 / 11 ∧ (794 : ℚ) / 11 < 73 := by
  norm_num

/-- **The borrow.** 0.036 − 7.94 × 10⁻⁷ = 0.035999206, digit for digit the Paris value. -/
theorem borrow_in_flight : (36 : ℚ) / 1000 - 794 / 10 ^ 9 = 35999206 / 10 ^ 9 := by
  norm_num

/-- **Twenty-eight times the block.** 28 × 0.036 = 1.008 with 28 = T(7) and 1008 = 42 · 24;
28 × 0.035999 = 1.007972; and 1.008 ÷ 28 = 0.036, the placement arriving with the numerator. -/
theorem twenty_eight_times_the_block :
    (28 : ℚ) * (36 / 1000) = 1008 / 1000 ∧ 28 = 7 * 8 / 2 ∧ 1008 = 42 * 24 ∧
    (28 : ℚ) * (35999 / 10 ^ 6) = 1007972 / 10 ^ 6 ∧ (1008 : ℚ) / 1000 / 28 = 36 / 1000 := by
  refine ⟨by norm_num, by decide, by decide, by norm_num, by norm_num⟩

/-- **The nucleon relation, with the tail as measured.** On the CODATA 2022 central values,
twenty-eight times the tail 0.035999177 is 1.007976956, and the mean of the proton and
neutron masses is 1.00797069131945 u. The product stands above the mean by a ratio that
rounds to 6.2 parts per million. The six settled digits give 1.007972, which rounds to 1.3.
The offset of the block carried through the factor is 2.3044 × 10⁻⁵, and the mean lies
2.930868055 × 10⁻⁵ below the base 1.008. -/
theorem measured_tail_times_twenty_eight :
    (28 : ℚ) * (35999177 / 10 ^ 9) = 1007976956 / 10 ^ 9 ∧
    ((10072764665789 : ℚ) / 10 ^ 13 + 100866491606 / 10 ^ 11) / 2 = 100797069131945 / 10 ^ 14 ∧
    (615 : ℚ) / 10 ^ 8 <
      (1007976956 / 10 ^ 9 - 100797069131945 / 10 ^ 14) / (100797069131945 / 10 ^ 14) ∧
    ((1007976956 : ℚ) / 10 ^ 9 - 100797069131945 / 10 ^ 14) / (100797069131945 / 10 ^ 14) <
      625 / 10 ^ 8 ∧
    (125 : ℚ) / 10 ^ 8 <
      (1007972 / 10 ^ 6 - 100797069131945 / 10 ^ 14) / (100797069131945 / 10 ^ 14) ∧
    ((1007972 : ℚ) / 10 ^ 6 - 100797069131945 / 10 ^ 14) / (100797069131945 / 10 ^ 14) <
      135 / 10 ^ 8 ∧
    (28 : ℚ) * (823 / 10 ^ 9) = 23044 / 10 ^ 9 ∧
    (1008 : ℚ) / 1000 - 100797069131945 / 10 ^ 14 = 2930868055 / 10 ^ 14 := by
  norm_num

/-- **Across the three determinations the product stands 2.6 to 7.0 parts per million above
the mean.** Caesium rounds to 2.6, the electron moment to 5.9, rubidium to 7.0. -/
theorem nucleon_relation_across_determinations :
    (255 : ℚ) / 10 ^ 8 <
      (28 * (35999046 / 10 ^ 9) - 100797069131945 / 10 ^ 14) / (100797069131945 / 10 ^ 14) ∧
    ((28 : ℚ) * (35999046 / 10 ^ 9) - 100797069131945 / 10 ^ 14) / (100797069131945 / 10 ^ 14) <
      265 / 10 ^ 8 ∧
    (585 : ℚ) / 10 ^ 8 <
      (28 * (35999166 / 10 ^ 9) - 100797069131945 / 10 ^ 14) / (100797069131945 / 10 ^ 14) ∧
    ((28 : ℚ) * (35999166 / 10 ^ 9) - 100797069131945 / 10 ^ 14) / (100797069131945 / 10 ^ 14) <
      595 / 10 ^ 8 ∧
    (695 : ℚ) / 10 ^ 8 <
      (28 * (35999206 / 10 ^ 9) - 100797069131945 / 10 ^ 14) / (100797069131945 / 10 ^ 14) ∧
    ((28 : ℚ) * (35999206 / 10 ^ 9) - 100797069131945 / 10 ^ 14) / (100797069131945 / 10 ^ 14) <
      705 / 10 ^ 8 := by
  norm_num

/-! ## Section 7 · The block and the nucleon masses -/

/-- **The stations about the base.** 1.008 − 0.00072 = 1.00728 and 1.008 + 0.00066 = 1.00866,
and the two stations average (−72 + 66)/2 = −3. -/
theorem stations_about_the_base :
    (1008 : ℚ) / 1000 - 72 / 10 ^ 5 = 100728 / 10 ^ 5 ∧
    (1008 : ℚ) / 1000 + 66 / 10 ^ 5 = 100866 / 10 ^ 5 ∧ ((-72 : ℤ) + 66) / 2 = -3 := by
  refine ⟨by norm_num, by norm_num, by decide⟩

/-- **The two integers and their gap of three.** 3 × 10⁸ = 2⁸ · 3 · 5⁸, and
3 × (10⁸ − 1) = 299999997 = 3³ · 11 · 73 · 101 · 137; they differ by exactly 3. -/
theorem two_forms_gap_three :
    3 * 10 ^ 8 = 2 ^ 8 * 3 * 5 ^ 8 ∧ 3 * (10 ^ 8 - 1) = 299999997 ∧
    299999997 = 3 ^ 3 * 11 * 73 * 101 * 137 ∧ 3 * 10 ^ 8 - 299999997 = 3 := by
  decide

end GTheory.Coupling
