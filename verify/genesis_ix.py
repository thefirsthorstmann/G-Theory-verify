"""genesis_ix.py — Chapter IX (Position and Diffusion): the exact claims.

POSITION IS AN ADDRESS. On a counting substrate a position is not a
point on a continuum but an address at a resolution: an n-digit
address locates to one part in 10^n, and refinement is an OPERATION
(the meter applies). Locality is adjacency in the register.

DIFFUSION WITHOUT DICE. The random walk needs no randomness: Pascal's
triangle IS the diffusion kernel — C(n, k) COUNTS the paths, exactly,
and what the continuum calls probability is path-counting normalized.
The diffusion law is a combinatorial identity:

    MEAN-SQUARE DISPLACEMENT after n steps
        = sum_k C(n,k) (n - 2k)^2 / 2^n  =  n   EXACTLY.

Spread grows linearly in the count — sigma^2 = n — which is Fick's
law with the diffusion constant in lattice units, derived by counting
alone. The Gaussian is the ENVELOPE: the return weight C(2n,n)/4^n
approaches 1/sqrt(pi n) — PI EMERGES AS THE ENVELOPE OF COUNTING —
and de Moivre's limit is conceded as the instrument it is.

THE ARROW IN DIFFUSION: spreading is commitment accumulation — each
step is written; the walk's irreversibility is the ledger's, not
chance's. Entropy counts collisions (the program's classification),
and nothing anywhere appealed to chance.
"""

import math
from fractions import Fraction as F


def path_count(n: int, k: int) -> int:
    """C(n, k): the EXACT number of n-step walks with k left-steps."""
    return math.comb(n, k)


def total_paths(n: int) -> int:
    return sum(path_count(n, k) for k in range(n + 1))


def mean_square_displacement(n: int) -> F:
    """sum C(n,k) (n-2k)^2 / 2^n — exact."""
    return sum(F(path_count(n, k) * (n - 2 * k) ** 2, 2 ** n)
               for k in range(n + 1))


def return_weight_vs_envelope(n: int) -> float:
    """C(2n, n)/4^n against 1/sqrt(pi n): the ratio -> 1."""
    exact = path_count(2 * n, n) / 4 ** n
    envelope = 1 / math.sqrt(math.pi * n)
    return exact / envelope
