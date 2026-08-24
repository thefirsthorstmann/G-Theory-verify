"""test_serial_order.py — THE LEDGER'S GAUGE (2026-08-16). The deepest
debt discharged: the register commits one union at a time, which seems to
carry a universal sequence — the thing relativity forbids. The discharge
is a theorem set about ledgers. Unions with disjoint records COMMUTE, so
order between them is bookkeeping, not content (the serializability of
concurrent ledgers — distributed computing's oldest theorem). Order
carries content exactly where a record is SHARED; sharing requires
propagation; propagation is one depth per tick (the clock object's own
rule) — so the boundary of order-matters is the light cone, derived as
the parameter record's support boundary. A FRAME is a linear extension of the
causal partial order: every extension lands the identical ledger, and
the reshuffling boost rides the paper's own rungs (4ⁿ−1)/(4ⁿ+1),
reordering spacelike pairs and never timelike ones. The infaller and
the far observer keep TWO LEDGERS of one fall: the private record's
total is a finite geometric sum while the shared account books a fixed
charge per halving and never completes — the freeze and the finite
crossing are the same fall in two books, with no shared fact left to
disagree."""

from fractions import Fraction as F
from itertools import permutations


def union(state, x, y):
    """The banked union: both records jump to k_x + k_y."""
    k = state[x] + state[y]
    state[x] = state[y] = k
    return state


def test_disjoint_unions_commute():
    """Two unions touching disjoint records leave the identical ledger
    in either order: between them, sequence is bookkeeping, not
    content."""
    for seed in ((1, 2, 4, 8), (3, 5, 7, 11), (1, 1, 1, 1)):
        s1 = dict(zip("ABCD", seed))
        union(s1, "A", "B"); union(s1, "C", "D")
        s2 = dict(zip("ABCD", seed))
        union(s2, "C", "D"); union(s2, "A", "B")
        assert s1 == s2


def test_shared_record_orders_do_not_commute():
    """Order carries content exactly where a record is shared: with B
    common to both events, the two schedules land different ledgers —
    (3,7,7) against (7,7,6) from the seed (1,2,4)."""
    s1 = {"A": 1, "B": 2, "C": 4}
    union(s1, "A", "B"); union(s1, "B", "C")
    s2 = {"A": 1, "B": 2, "C": 4}
    union(s2, "B", "C"); union(s2, "A", "B")
    assert s1 == {"A": 3, "B": 7, "C": 7}
    assert s2 == {"A": 7, "B": 7, "C": 6}
    assert s1 != s2


def test_the_cone_is_the_support_boundary():
    """Propagation is one depth per tick — the clock object's rule: the
    carry commits one cell per tick, never a ripple in one. A
    perturbation at cell 0 first touches cell k at tick k, exactly — the
    discrete light cone as the parameter record's support boundary."""
    N, T = 40, 39

    def run(cells):
        history = [cells[:]]
        for _ in range(T):
            nxt = [cells[0]] + [cells[i] ^ cells[i - 1] for i in range(1, N)]
            cells = nxt
            history.append(cells[:])
        return history

    base = run([0] * N)
    pert = run([1] + [0] * (N - 1))
    for k in range(1, N):
        first = min(t for t in range(T + 1) if base[t][k] != pert[t][k])
        assert first == k                       # the cone edge, never earlier


def test_frames_are_linear_extensions():
    """Four events — a = union(R1,R2), b = union(R3,R4), c = union(R2,R3),
    d = union(R4,R5) — with the causal order a<c, b<c, b<d carried by the
    shared records. Exactly five total orders extend it; every one lands
    the identical final ledger; every order violating the cone lands a
    different one. A frame is a choice of extension, and the choice moves
    nothing."""
    events = {"a": ("R1", "R2"), "b": ("R3", "R4"),
              "c": ("R2", "R3"), "d": ("R4", "R5")}
    seed = {"R1": 1, "R2": 2, "R3": 4, "R4": 8, "R5": 16}

    def respects(order):
        return (order.index("a") < order.index("c")
                and order.index("b") < order.index("c")
                and order.index("b") < order.index("d"))

    def final(order):
        s = dict(seed)
        for e in order:
            union(s, *events[e])
        return tuple(sorted(s.items()))

    valid = [p for p in permutations("abcd") if respects(p)]
    invalid = [p for p in permutations("abcd") if not respects(p)]
    assert len(valid) == 5                      # five frames for this diagram
    finals = {final(p) for p in valid}
    assert len(finals) == 1                     # one physics
    the_final = finals.pop()
    assert all(final(p) != the_final for p in invalid)   # the cone is content


def test_the_boost_reshuffle_rides_the_ladder():
    """The reordering is quantitative on the paper's own rungs
    β = (4ⁿ−1)/(4ⁿ+1): the sign of Δt − βΔx flips for the spacelike pair
    (1, 2) already at the first rung 3/5, while no rung ever reorders the
    timelike pair (2, 1) — every rung sits below one, so the cone
    protects order with the ladder's own arithmetic. The null pair (1,1)
    is approached and never flipped."""
    rungs = [F(4 ** n - 1, 4 ** n + 1) for n in range(1, 8)]
    assert rungs[0] == F(3, 5)
    spacelike = [F(1) - b * 2 for b in rungs]
    assert spacelike[0] < 0                     # reordered at the first rung
    timelike = [F(2) - b * 1 for b in rungs]
    assert all(t > 1 for t in timelike)         # never reordered
    null = [F(1) - b * 1 for b in rungs]
    assert all(n > 0 for n in null)             # the edge, never crossed


def test_no_signal_rides_the_gauge():
    """The commutation theorem restricted to a marginal: the content of
    records C and D is identical whether the spacelike-separated union
    of A and B commits before or after theirs — no observable at (C,D)
    detects the remote order. Signaling would refute the register."""
    s1 = {"A": 1, "B": 2, "C": 4, "D": 8}
    union(s1, "A", "B"); union(s1, "C", "D")
    s2 = {"A": 1, "B": 2, "C": 4, "D": 8}
    union(s2, "C", "D"); union(s2, "A", "B")
    assert (s1["C"], s1["D"]) == (s2["C"], s2["D"])


def test_the_two_ledgers_of_the_fall():
    """The exact toy of halvings, matching the strong field's structure:
    at depth k the gap to the floor is 2⁻ᵏ, the budget is 1−2φ = 2¹⁻ᵏ,
    the private record spends Δτ = 2⁻ᵏ, and the shared account books
    Δt = Δτ/(1−2φ) = 1/2 — a fixed charge per halving. The private total
    converges to exactly 1; the shared total is N/2, unbounded — the log
    divergence of the freeze, linear in halvings. One fall, two books,
    no shared fact to disagree: the freeze is the ratio, and the ratio
    is the budget line."""
    private = F(0)
    shared = F(0)
    for k in range(1, 200):
        gap = F(1, 2 ** k)
        budget = 1 - 2 * (F(1, 2) - gap)
        assert budget == F(2, 2 ** k)
        dtau = gap
        dt = dtau / budget
        assert dt == F(1, 2)                    # fixed charge per halving
        private += dtau
        shared += dt
        assert private == 1 - F(1, 2 ** k)      # converges to exactly 1
        assert shared == F(k, 2)                # diverges linearly in depth
    assert private < 1 and shared > 99
