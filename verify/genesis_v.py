"""genesis_v.py — Chapter V (The Birth of Chemistry): the exact claims.

THE MADELUNG THEOREM (the program's co-flagship, now in closed form).
Assign to each orbital (n, l) the exact value

    V(n, l) = 1296 * (2/3)^floor((n-l-1)/2) * (5/6)^(2l + (n-l-1 mod 2))

with root 1296 = 6^4 (the seed's fourth power) and the two multiplier
ratios 2/3 and 5/6. THEOREM: ranking the nineteen orbitals 1s..7p by
V in DESCENDING order reproduces the entire empirical filling order
of the periodic table TERM FOR TERM — including both celebrated
anomalies (4s before 3d: 720 > 625; 4f before 5d: 15625/36 > 1250/3)
— with the odd s-orbitals 1s, 3s, 5s, 7s landing at the perfect-
square ranks 1, 4, 9, 16, and the Madelung (n+l, n) rule holding
across the whole ranking. Zero chemistry input.

COROLLARY (the noble gases): filling each ranked orbital to its
standard capacity 2(2l+1), the cumulative counts at the p-shell
closures are exactly 2, 10, 18, 36, 54, 86 — helium through radon.
"""

from fractions import Fraction as F

FILLING = ["1s", "2s", "2p", "3s", "3p", "4s", "3d", "4p", "5s", "4d",
           "5p", "6s", "4f", "5d", "6p", "7s", "5f", "6d", "7p"]
L_OF = {"s": 0, "p": 1, "d": 2, "f": 3}


def madelung_value(n: int, l: int) -> F:
    """The closed-form value of orbital (n, l)."""
    k = n - l - 1
    return 1296 * F(2, 3) ** (k // 2) * F(5, 6) ** (2 * l + k % 2)


def ranked_orbitals() -> list:
    """All 19 orbitals 1s..7p, ranked by descending value."""
    orbs = [(label, int(label[0]), L_OF[label[1]]) for label in FILLING]
    return sorted(orbs, key=lambda o: madelung_value(o[1], o[2]),
                  reverse=True)


def noble_gas_closures() -> list:
    """Cumulative electron counts at each p-shell completion."""
    total, out = 0, []
    for label, n, l in ranked_orbitals():
        total += 2 * (2 * l + 1)
        if l == 1:
            out.append(total)
    return out
