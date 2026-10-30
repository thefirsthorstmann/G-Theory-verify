/-
# The vacuum on discrete terms: Theorem 1, the shortfall of the riders

Source: "The Vacuum on Discrete Terms" (Christian Horstmann), version 2, §2, Theorem 1, in the
record's own words: "On the reptend cycle of the tethered prime, the k-th rider's closure falls
short by exactly k: k × 142857 × 7 = k·10⁶ − k, for every k from one to six, and likewise for every
full reptend prime. The modulus's own gap is one: 10⁶ − 999999 = 1 — for every rider, and with no
rider at all."

The record identifies the shortfall with the vacuum tier; that identification is not a theorem of
this file. What is proved here is the arithmetic it is made on:

* the rider at seven, for every k (the record states k = 1 … 6), from the gravity record's file;
* the same for every prime p other than 2 and 5, with the period block (10^(p−1) − 1)/p in place
  of 142857; every full reptend prime is such a prime, so the record's clause is a case of it;
* the modulus's own gap, 10⁶ − 999999 = 1.

Written 28 October 2026, at CC's question whether any Lean was outstanding: the record has said
since October that its Theorem 1 is formalized, and only the case at seven was.
-/
import Mathlib.FieldTheory.Finite.Basic
import GTheory.Gravity

namespace GTheory.Vacuum

/-- **Theorem 1, at seven.** k × 142857 × 7 = k·10⁶ − k: the k-th rider's closure falls short
by exactly k. The record states it for k = 1 … 6; it holds for every k. -/
theorem riders_fall_short_at_seven (k : ℕ) : k * 142857 * 7 = k * 10 ^ 6 - k :=
  GTheory.Gravity.k_rotation k

/-- **Theorem 1, for every full reptend prime.** For a prime p other than 2 and 5, the period
block (10^(p−1) − 1)/p is a whole number, and k times it times p falls short of k·10^(p−1) by
exactly k. A full reptend prime is a prime other than 2 and 5, so the record's clause is a case. -/
theorem riders_fall_short_at_every_prime (p k : ℕ) (hp : p.Prime) (h2 : p ≠ 2) (h5 : p ≠ 5) :
    k * ((10 ^ (p - 1) - 1) / p) * p = k * 10 ^ (p - 1) - k := by
  have hnd : ¬ p ∣ 10 := by
    intro h
    rw [show (10 : ℕ) = 2 * 5 from rfl] at h
    rcases (Nat.Prime.dvd_mul hp).1 h with h' | h'
    · exact h2 ((Nat.prime_dvd_prime_iff_eq hp Nat.prime_two).1 h')
    · exact h5 ((Nat.prime_dvd_prime_iff_eq hp Nat.prime_five).1 h')
  have hcop : Nat.Coprime 10 p := ((Nat.Prime.coprime_iff_not_dvd hp).2 hnd).symm
  have hmod : 10 ^ (p - 1) ≡ 1 [MOD p] := by
    have h := Nat.ModEq.pow_totient hcop
    rwa [Nat.totient_prime hp] at h
  have hdvd : p ∣ 10 ^ (p - 1) - 1 :=
    (Nat.modEq_iff_dvd' (Nat.one_le_pow _ _ (by norm_num))).1 hmod.symm
  rw [mul_assoc, Nat.div_mul_cancel hdvd, Nat.mul_sub_one]

/-- **Theorem 1, the modulus's own gap.** 10⁶ − 999999 = 1, for every rider and with none. -/
theorem the_modulus_gap_is_one : 10 ^ 6 - 999999 = 1 := by norm_num

end GTheory.Vacuum
