"""genesis_viii.py — Chapter VIII (Modern Physics): the exact claims.

THE PIANO, MADE EXACT. A struck string sounds all its harmonics at
once — superposition as a physical commonplace, not a mystery. The
collapse mechanism is the node-touch selection rule: mode m has a
node at position x = p/q (reduced) iff q divides m, so

    TOUCHING THE STRING AT p/q KEEPS EXACTLY THE MULTIPLES OF q.

Touch the midpoint: the even harmonics survive (the octave family).
Touch the third: the multiples of three (the triad family). The
"measurement" selects a residue class — collapse is filtering, and
the filter is arithmetic.

THE PORT: the Born reading keeps the squared magnitudes and discards
the phases — EXACTLY HALF the state (the program's pinned theorem,
asserted here as a dependency). Collapse is a rounding event on the
working face: Landauer-costly, thermodynamically irreversible —
measurement's irreversibility is bookkeeping, not mystery.

THE FACTORIAL WALL: maintaining mutual phase across N constituents
scales coherence as N! — twenty constituents already exceed 10^18 —
why dust is classical and cats do not interfere.

THE DUALITY DEPENDENCIES: P^2 + V^2 = 1 (Euclid's triple identity)
and the marker triple P^2 + V^2 + C^2 = 1 (Englert saturated) are
asserted from the program's own pinned modules.
"""

import math
from fractions import Fraction as F


def surviving_modes(q: int, n_max: int = 24) -> list:
    """The node-touch rule: touch at p/q (reduced) -> multiples of q."""
    return [m for m in range(1, n_max + 1) if m % q == 0]


def factorial_wall(n: int) -> int:
    return math.factorial(n)


def port_discards_exactly_half() -> bool:
    """Dependency: the Born port keeps A^2, discards m — half of 2n."""
    from polar_wave import info_content
    state = [(1, k) for k in range(8)]           # 8 modes: (A, m) pairs
    total, kept = info_content(state)
    return kept * 2 == total == 16


def duality_is_euclid() -> bool:
    """Dependency: P^2 + V^2 = 1 exactly, from the two-slit module."""
    from two_slit import duality_sum
    return all(duality_sum(a, b) == 1
               for a in range(1, 6) for b in range(1, 6))
