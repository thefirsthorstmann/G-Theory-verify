"""chosen_three.py — F4: the three chosen numbers under trial by
least action (CC's directive), with the representational-optimality
position: each domain's language is the best structural analog for
the behavior it represents — and 'best' is now a computed claim.

THE BASE TRIAL: the framework's two load-bearing register mechanisms
are (i) the ennead — digit sums preserve mod 9, requiring b = 1 mod 9
— and (ii) the seed's full unrolling — ord_7(b) = 6. Scanning all
bases: 2-9 each fail at least one; BASE 10 IS THE UNIQUE LEAST BASE
CARRYING BOTH (the next is 19 = 10 + 9). The near-misses sharpen the
claim: bases 3, 5, 12, 17 unroll the seed fully but erase the ennead;
base 9 erases it maximally (digit sums go mod 8). Honesty: this is
CONDITIONAL least action — given the two mechanisms, 10 is forced-
least; the mechanisms themselves are the 2-perp-3 thesis (9 = 3^2,
7 = the seed). The circularity is named and weighed, not smuggled.

THE SEED TRIAL: 7 is the least full-reptend prime in base 10 (3 gives
period 1, 11 gives period 2, 13 gives half) — the first prime whose
division exhibits the COMPLETE period p-1 = 6 = 2x3: the first place
the incommensurability appears whole. And the full-reptend sequence
in base 10 opens {7, 17, 19, 23, ...}: THE SEED FIRST, THE SPINE
SECOND — the two structural primes are the register's own first two
full unrollings.

THE x3 TRIAL: cornered (only m = 3 lands the third-lattice — the
multiplicity scan, THE-FORCED-TABLE), braced (C_A = 3; gluons =
3^2 - 1 = 8 = the ring), NOT yet forced — the one remaining input,
and the trial states what would force it: an independent derivation
of color-as-the-triad-axis {3,6,9}.
"""


def ord_mod(b: int, p: int):
    """Multiplicative order of b mod p (None if p | b)."""
    if b % p == 0:
        return None
    x, k = b % p, 1
    while x != 1:
        x = x * b % p
        k += 1
    return k


def carries_ennead(b: int) -> bool:
    """Digit sums preserve mod 9 iff b = 1 (mod 9)."""
    return b % 9 == 1


def unrolls_seed(b: int) -> bool:
    """The seed divides fully iff ord_7(b) = 6."""
    return ord_mod(b, 7) == 6


def bases_with_both(lo: int = 2, hi: int = 30) -> list:
    return [b for b in range(lo, hi + 1)
            if carries_ennead(b) and unrolls_seed(b)]


def full_reptend_primes(base: int = 10, upto: int = 30) -> list:
    """Primes p with ord_p(base) = p - 1."""
    out = []
    for p in range(3, upto + 1):
        if all(p % d for d in range(2, int(p ** 0.5) + 1)):
            if ord_mod(base, p) == p - 1:
                out.append(p)
    return out
