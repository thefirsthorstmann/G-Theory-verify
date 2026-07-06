"""genesis_iii.py — Chapter III (First Particles): the exact claims.

THE PARTICLE-STATE CHAIN (the commitment algebra populated). In the
width-three register the two multipliers act oppositely: x1001
duplicates a block (a -> a|a: the ECHO, a neutral twin) and x999
splits it into complements summing 999 (a -> a-1 | 1000-a: the SPLIT
pair). The seed ties the two faces through one number:
1/7 = 143/1001 exactly, and 143 x 999 = 142857 — the period itself.
The chain of states, exact:

    REST     1008 x (1/7)   = 144          (exact; unobservable seat)
    ECHO     1008 x 0.143   = 144.144      (the committed neutral twin)
    SPLIT    144 x 999      = 143|856      (the complement pair, sum 999)

with 1008 = 42 x 24 (the first operation's own displaced pair as a
product) = hydrogen's atomic weight x 1000. The anti-half of every
committed pair is its standing complement — "where is the
antimatter" is answered by the algebra, not by a lost inventory.

PRIMORDIAL ABUNDANCE (the first quantitative cosmological output):
the seed ratio n/p = 1/7 gives the neutron fraction 1/8 and the
helium mass fraction Y = 2 x (1/8) = 1/4 exactly — the 75/25
hydrogen/helium split. Measured Y_p = 0.245(4): the exact 1/4 is the
SEAT; the ~2% deficit is the dress (neutron decay during freeze-out,
conceded to the standard dynamics).
"""

from fractions import Fraction as F

from charge_forcing import composites, solve_charges
from proton_ledger import ledger


def particle_chain() -> dict:
    """Rest -> echo -> split, exact."""
    rest = 1008 * F(1, 7)
    echo = 1008 * F(143, 1000)
    split_lo, split_hi = divmod(144 * 999, 1000)
    return {"rest": rest, "echo": echo,
            "split": (split_lo, split_hi),
            "split_sum": split_lo + split_hi,
            "seed_tie": (F(143, 1001), 143 * 999)}


def helium_fraction(n_over_p: F = F(1, 7)) -> F:
    """Y = 2 f where f = neutron fraction = (n/p)/(1 + n/p)."""
    f = n_over_p / (1 + n_over_p)
    return 2 * f


def chapter_dependencies() -> bool:
    """The chapter stands on the forced table and the proton ledger."""
    q = solve_charges()
    c = composites(q)
    L = ledger()
    return (q["u"] == F(2, 3) and c["hydrogen"] == 0
            and L["net"] == 1 and L["gross"] == F(5, 3))
