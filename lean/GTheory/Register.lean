/-
# The register theorem

Source: "The Origin on Discrete Terms" (Christian Horstmann, concept DOI
10.5281/zenodo.21212112), version 3, Volume I, "Theorem (the register)". The record's
statements:

* The first mechanism is residue bookkeeping. The classes modulo 9 are preserved under
  digit summation, so that the arithmetic of classes can be read off representations, if
  and only if the base b satisfies b ≡ 1 (mod 9).
* The second mechanism is the complete period. The first prime whose reciprocal has the
  maximal period, exhibiting the full 2×3 cycle, is 7, and its period is complete if and
  only if b is a primitive root modulo 7.
* Theorem (the register). Base ten is the least base carrying both mechanisms, and the
  carriers are rare: 10, 19 and 73 are the only ones below eighty. 28 fails because 7
  divides it, while 3, 5, 12 and 17 give the full period but fail the residue condition.
  The proof is a finite scan, machine-verified.
* The seed. 2ᵃ = 3ᵇ has no solution in positive integers, so no number of doublings ever
  equals a number of triplings.

The record states the theorem as conditional on the two mechanisms, and so does this file:
given the two predicates below, the register is uniquely determined. Nothing here argues
for the mechanisms themselves.
-/
import Mathlib.Tactic

namespace GTheory.Register

/-- Residue bookkeeping: the base is congruent to one modulo nine. -/
def ResidueBookkeeping (b : ℕ) : Prop := b % 9 = 1

/-- Complete unrolling: b is a primitive root modulo 7, stated concretely as the
multiplicative order of b modulo 7 being exactly six — b⁶ ≡ 1 and no smaller positive
power is. A base divisible by 7 fails at once, since no power of it is ≡ 1. -/
def Unrolls (b : ℕ) : Prop :=
  b ^ 6 % 7 = 1 ∧ ∀ j, 1 ≤ j → j < 6 → b ^ j % 7 ≠ 1

instance : DecidablePred ResidueBookkeeping := fun b =>
  inferInstanceAs (Decidable (b % 9 = 1))

instance : DecidablePred Unrolls := fun b =>
  inferInstanceAs (Decidable (b ^ 6 % 7 = 1 ∧ ∀ j, 1 ≤ j → j < 6 → b ^ j % 7 ≠ 1))

/-- A base carries the register when it has both mechanisms. -/
def Carries (b : ℕ) : Prop := ResidueBookkeeping b ∧ Unrolls b

instance : DecidablePred Carries := fun b =>
  inferInstanceAs (Decidable (ResidueBookkeeping b ∧ Unrolls b))

/-- **The register theorem, the finite scan.** Below eighty, the bases carrying both
mechanisms are exactly 10, 19 and 73. -/
theorem carriers_below_eighty :
    ∀ b, 2 ≤ b → b < 80 → (Carries b ↔ b = 10 ∨ b = 19 ∨ b = 73) := by
  decide

/-- **Base ten is the least base carrying both mechanisms.** -/
theorem ten_is_the_least :
    Carries 10 ∧ ∀ b, 2 ≤ b → b < 10 → ¬ Carries b := by
  decide

/-- **28 fails because 7 divides it**: it has the residue bookkeeping (28 ≡ 1 mod 9) and
no unrolling at all. -/
theorem twenty_eight_fails : 7 ∣ 28 ∧ ResidueBookkeeping 28 ∧ ¬ Unrolls 28 := by
  decide

/-- **3, 5, 12 and 17 unroll the period fully but falsify the residue bookkeeping.** -/
theorem four_unroll_without_bookkeeping :
    (Unrolls 3 ∧ Unrolls 5 ∧ Unrolls 12 ∧ Unrolls 17) ∧
    (¬ ResidueBookkeeping 3 ∧ ¬ ResidueBookkeeping 5 ∧
     ¬ ResidueBookkeeping 12 ∧ ¬ ResidueBookkeeping 17) := by
  decide

/-- Unrolling is a condition on the residue of the base modulo 7 alone: the primitive
roots modulo 7 are the residues 3 and 5. Stated for bases below eighty, as a scan. -/
theorem unrolling_is_a_residue_condition :
    ∀ b, b < 80 → (Unrolls b ↔ b % 7 = 3 ∨ b % 7 = 5) := by
  decide

/-- **The seed's contest never closes.** No positive power of two is a power of three,
because the left side is even and the right side is odd. -/
theorem no_power_of_two_is_a_power_of_three (a b : ℕ) (ha : 1 ≤ a) :
    2 ^ a ≠ 3 ^ b := by
  intro h
  have h2 : 2 ∣ 2 ^ a := dvd_pow_self 2 (by omega)
  have h3 : ¬ 2 ∣ 3 ^ b := by
    intro hd
    have := Nat.Prime.dvd_of_dvd_pow Nat.prime_two hd
    omega
  exact h3 (h ▸ h2)

end GTheory.Register
