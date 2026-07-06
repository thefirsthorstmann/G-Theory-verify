"""genesis_i.py — Chapter I (Initial Conditions): the exact claims.

THE THREE MOVES, as arithmetic:

MOVE ONE — the first operation is FREE. The six digits of the first
complete period (1/7 = 0.142857...) admit exactly two canonical
orders: the POSITIONAL order 1,4,2,8,5,7 (the order in which division
writes them) and the MULTIPLICATIVE order 1,2,4,8,7,5 (the doubling
orbit mod 9). The transform (hold the 1 and the 8, reverse the
interior pairs) maps one onto the other: 142857 -> 124875 — and
124875 IS the doubling orbit read as digits. The transform is an
INVOLUTION (its own inverse): invertible, hence free of Landauer
erasure — the first operation asks nothing, and least action at the
origin is an observation, not an assumption. Its ledger: 42 -> 24
(-18), 57 -> 75 (+18), net 0 — displacement and its conservation
born in one move.

MOVE TWO — the carry: time. Positional counting has one non-local
operation, the carry; succession is the count of carries; the 3-walk
on the 8-ring closes only at lcm(3,8) = 24 with a deficit per cycle —
the escapement (pinned in the clock/polar modules).

MOVE THREE — the rounding: matter. Rounding at fixed depth is
many-to-one (Landauer: costly). The commitment ladder of the seed:
depths 3, 4, 5 round the carriers 2, 8, 5 up to 3, 9, 6 — and depth 3
commits EXACTLY by the factor 1001/1000 (because 7 | 10^3 + 1, the
Midy factor): the first clean commitment of the construction.

THE SEED'S INCOMMENSURABILITY: 2^a = 3^b has no solution in positive
integers (parity: the left side is even, the right odd) — the contest
never closes; the near-miss ladder |2^a - 3^b| runs 1, 5, 17, 13, 139.
"""

from fractions import Fraction as F

from gtheory import doubling_orbit, reptend, rounded_seventh, transform


def positional_order() -> str:
    """The order division writes: the reptend itself."""
    return reptend(7)                      # '142857'


def multiplicative_order() -> str:
    """The doubling orbit mod 9, read as digits."""
    return "".join(str(d) for d in doubling_orbit())   # '124875'


def first_operation():
    """The transform's full ledger (from the engine)."""
    return transform()


def is_involution() -> bool:
    """T(T(x)) = x: the first operation undoes itself — free."""
    once = transform()["out"]
    twice = transform(once)["out"]
    return twice == reptend(7)


def no_closure(max_power: int = 200) -> bool:
    """2^a = 3^b has no positive solution (parity); verified over a
    range far beyond any physical register."""
    return all(2 ** a != 3 ** b
               for a in range(1, max_power) for b in range(1, max_power // 2))


def commitment_ladder() -> list:
    """Depths 3, 4, 5: carrier digit -> lifted value; depth 3 exact."""
    out = []
    for depth in (3, 4, 5):
        digs = str(rounded_seventh(depth).numerator)
        carrier = int(reptend(7)[depth - 1])
        out.append((depth, carrier, carrier + 1))
    return out
