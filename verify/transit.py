"""transit.py — the transit read (CC, 2026-07-03): a number in passage
between bases, decimal digits sitting on binary place-values.

    transit(.d1 d2 d3 ...) = d1/2 + d2/4 + d3/8 + ...

A digit above 1 is a REDUNDANT binary digit — a stack of un-executed
carries. The transit state is the loaded escapement: 1.008 holds one
whole suspended unit (8 at the 1/8 slot), 1.001 holds one carry
QUANTUM (1 at the 1/8 slot -> transit 9/8 = Re, the overshoot).

NULL HONESTY, built in: every finite transit read is dyadic (k/2^n by
construction), so 'landing on a clean fraction' is guaranteed and
carries no information — the content is only ever in WHICH k.

THE REPTEND IN TRANSIT: the repeating read of 142857 is
    (sum d_i 2^(6-i)) / (2^6 - 1) = 161/63 = (7x23)/(7x9) = 23/9
— the seed divisor cancels ITSELF out, and the residue pair (23, 9)
multiplies back to 207, the banked muon block. The four banked
orderings read 7/3, 23/9, 25/9 = (5/3)^2, 28/9 — all ninths; the
7-divisibility filter passes exactly 144 of the 720 orderings (= 1/5).

THE MIDY COMMA: rounding 1/7 at depth 3 is EXACTLY multiplication by
1001/1000 — because 7 | 10^3 + 1 (the very fact behind Midy's
142 + 857 = 999). 1001 = 7 x 11 x 13 (the full hidden-prime cast) over
10^3 = (2x5)^3 (the manifest pair cubed); 10^6 - 1 = 999 x 1001. Depth
6 rounds DOWN by exactly 10^-6 (7 | 10^6 - 1). Depths 4, 5 are dirty
(excess 3/10^4, 2/10^5). The register family b^k + 1: 11, 101 (in
c_rest), 1001 — Pascal rows in base-10^k registers until the carry.

THE LADDER IN TRANSIT: the four depth-tails (digit, place) =
(1,3), (3,4), (2,5), (-1,6) project on 24 to {3, 9/2, 3/2, -3/8} =
3 x {1, 3/2, 1/2, -1/8} — the vector, Sol over 3, Sol over 1, and
MINUS THE CLOCK RATIO at the full period. Up-projections d x 2^k:
{8, 48, 64, -64} — the ring, the octave of 24, the period weight.
"""

from fractions import Fraction as F
from itertools import permutations


def transit(digits: str) -> F:
    """Finite transit read of a digit string (the part after the point)."""
    return sum(F(int(d), 2 ** (i + 1)) for i, d in enumerate(digits))


def transit_rep(block: str) -> tuple:
    """Repeating transit read: (block-sum, value = S/(2^n - 1))."""
    n = len(block)
    s = sum(int(d) * 2 ** (n - 1 - i) for i, d in enumerate(block))
    return s, F(s, 2 ** n - 1)


def seven_filter_count() -> int:
    """How many orderings of {1,4,2,8,5,7} have 7 | block-sum
    (i.e. transit value a pure ninth after the seed cancels)."""
    return sum(1 for p in permutations("142857")
               if transit_rep("".join(p))[0] % 7 == 0)


# the generation-ladder tails: depth -> (digit, decimal place)
LADDER_TAILS = {3: (1, 3), 4: (3, 4), 5: (2, 5), 6: (-1, 6)}


def ladder_down(depth: int) -> F:
    """The tail's transit value projected on 24."""
    d, place = LADDER_TAILS[depth]
    return 24 * F(d, 2 ** place)


def ladder_up(depth: int) -> int:
    """The other direction: digit times the binary place-value."""
    d, place = LADDER_TAILS[depth]
    return d * 2 ** place
