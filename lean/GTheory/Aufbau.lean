/-
# The aufbau as a theorem

Source: "The Origin on Discrete Terms", Volume V, The Birth of Chemistry (Christian
Horstmann, concept DOI 10.5281/zenodo.21212112), version 3, Section 2, Theorem 1 and its
corollary. The pytest
pins are verify/test_genesis_v.py. This file proves the same statements in Lean, so that
they hold by the kernel's check rather than by a computation repeated on one machine.

The record's statements, in its own words:

* Definition. For an orbital with principal number n and angular number ℓ, let
  k = n − ℓ − 1 and define the exact rational
      V(n, ℓ) = 1296 · (2/3)^⌊k/2⌋ · (5/6)^(2ℓ + (k mod 2)).
  The root is 1296 = 6⁴ and the two multipliers are the exact ratios 2/3 and 5/6.
* Theorem 1 (the aufbau). The nineteen orbitals 1s through 7p, ranked by descending V,
  reproduce the empirical filling order term for term, with both anomalies automatic as
  strict inequalities of exact fractions: 4s = 720 > 625 = 3d, and
  4f = 15625/36 > 1250/3 = 5d.
* Moreover the odd s-orbitals stand at the perfect-square ranks, the square spine:
  1s, 3s, 5s, 7s at ranks 1, 4, 9, 16.
* Madelung's (n + ℓ, n) rule holds across the entire ranking as a consequence.
* Corollary (the noble gases). Filling each ranked orbital to its capacity 2(2ℓ + 1),
  the cumulative counts at the p-shell closures are exactly 10, 18, 36, 54, 86, 118,
  with helium's 2 closing the first s-shell.

What is proved here is the arithmetic: that this explicit function of the quantum numbers
orders the nineteen orbitals as chemistry fills them. That the pair (2/3, 5/6) is the
right pair is, as the record itself says, a declared selection, and no theorem below
claims otherwise.
-/
import Mathlib.Tactic

namespace GTheory.Aufbau

/-- The radial count k = n − ℓ − 1 (natural-number subtraction; every orbital used
below has ℓ < n, so no truncation occurs). -/
def k (n l : ℕ) : ℕ := n - l - 1

/-- The record's closed form V(n, ℓ), an exact rational. -/
def V (n l : ℕ) : ℚ :=
  1296 * (2 / 3 : ℚ) ^ (k n l / 2) * (5 / 6 : ℚ) ^ (2 * l + k n l % 2)

/-- The nineteen orbitals 1s … 7p, written in the empirical filling order
1s 2s 2p 3s 3p 4s 3d 4p 5s 4d 5p 6s 4f 5d 6p 7s 5f 6d 7p, as (n, ℓ) pairs. -/
def filling : List (ℕ × ℕ) :=
  [(1, 0), (2, 0), (2, 1), (3, 0), (3, 1), (4, 0), (3, 2), (4, 1), (5, 0), (4, 2),
   (5, 1), (6, 0), (4, 3), (5, 2), (6, 1), (7, 0), (5, 3), (6, 2), (7, 1)]

/-- The root and the two ratios are all that enter: the values at the first rungs. -/
theorem root_is_six_to_the_fourth : V 1 0 = 1296 ∧ (1296 : ℚ) = 6 ^ 4 := by
  norm_num [V, k]

/-- `Descending l` says V strictly decreases from each orbital in `l` to the next.
Stated by direct recursion on the list so that the theorem below depends on no
library naming, only on the definition of V. -/
def Descending : List (ℕ × ℕ) → Prop
  | [] => True
  | [_] => True
  | a :: b :: rest => V b.1 b.2 < V a.1 a.2 ∧ Descending (b :: rest)

/-- **Theorem 1 (the aufbau).** Along the empirical filling order, V strictly
decreases at every step; ranking the nineteen orbitals by descending V therefore
reproduces the filling order term for term. The proof unfolds to eighteen strict
inequalities between exact rationals and checks each one. -/
theorem ranking_is_the_filling_order : Descending filling := by
  simp only [filling, Descending, and_true]
  norm_num [V, k]

/-- **The first swerve, in integers.** 4s = 720 > 625 = 3d. -/
theorem first_anomaly : V 4 0 = 720 ∧ V 3 2 = 625 ∧ V 4 0 > V 3 2 := by
  norm_num [V, k]

/-- **The second swerve, in exact fractions.** 4f = 15625/36 > 1250/3 = 5d. -/
theorem second_anomaly : V 4 3 = 15625 / 36 ∧ V 5 2 = 1250 / 3 ∧ V 4 3 > V 5 2 := by
  norm_num [V, k]

/-- The rank of an orbital in the filling order, counted from 1. -/
def rank (o : ℕ × ℕ) : ℕ := filling.findIdx (fun p => decide (p = o)) + 1

/-- **The square spine.** 1s, 3s, 5s, 7s sit at ranks 1, 4, 9, 16. -/
theorem square_spine :
    rank (1, 0) = 1 ∧ rank (3, 0) = 4 ∧ rank (5, 0) = 9 ∧ rank (7, 0) = 16 := by
  decide

/-- **Madelung's rule as a consequence.** For every pair of orbitals in the ranking,
the earlier one has smaller n + ℓ, or equal n + ℓ and smaller n. -/
theorem madelung_rule_holds :
    filling.Pairwise (fun a b => a.1 + a.2 < b.1 + b.2 ∨
      (a.1 + a.2 = b.1 + b.2 ∧ a.1 < b.1)) := by
  decide

/-- The standard capacity of an orbital, 2(2ℓ + 1): two spins times the angular
degeneracy. Adopted from quantum mechanics, as the record states. -/
def capacity (o : ℕ × ℕ) : ℕ := 2 * (2 * o.2 + 1)

/-- Electrons accommodated by the first m orbitals of the ranking. -/
def filled (m : ℕ) : ℕ := ((filling.map capacity).take m).sum

/-- **Corollary (the noble gases).** Helium closes the first s-shell at 2, and the
p-shell closures fall at exactly 10, 18, 36, 54, 86, 118: neon, argon, krypton,
xenon, radon, oganesson. The nineteenth rung completes at 118. -/
theorem noble_gases :
    filled 1 = 2 ∧ filled 3 = 10 ∧ filled 5 = 18 ∧ filled 8 = 36 ∧
    filled 11 = 54 ∧ filled 15 = 86 ∧ filled 19 = 118 := by
  decide

/-- The nineteen orbitals hold 118 electrons in all: the table ends where the
ranking ends. -/
theorem terminus : filled filling.length = 118 := by
  decide

end GTheory.Aufbau
