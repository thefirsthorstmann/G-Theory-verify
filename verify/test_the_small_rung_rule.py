"""test_the_small_rung_rule.py — THE SMALL-RUNG TWO-RIDER RULE
(2026-08-17). The update-rule campaign took the two-rider exchange at the
far field and left one item inside it: "the exact small-rung lattice
version." It closes here, and closing it joins two objects that were
banked apart.

THE KERNEL. At the far field the exchange runs on the smooth extension
law. At small rungs the register's own kernel is the CARRY CENSUS: the
rate at depth j is the inverse of the cell it governs, and a separated
pair is registered by every depth down to the one whose cell matches the
separation. Summing that census gives two facts already banked, now from
one expression — its total over all depths is the saturation ceiling
2/u_min, and its ratio to the smooth law is a staircase.

AND THE STAIRCASE IS THE COMB. Because the depth index is an integer, the
census-to-smooth ratio is periodic in log₂ of the separation with a period
of exactly ONE OCTAVE — reproduced octave after octave to floating
precision. The log-periodic residual the operation movement predicts at
the envelope is the same object as the small-rung kernel's own
discreteness, seen from the other end. Two banked results, one mechanism.

THE LAWS SURVIVE. The question the debt really asked is whether the
two-rider theorems hold once the kernel is replaced, and they do, for a
reason that makes the answer general rather than lucky: the third law,
momentum conservation, the equivalence principle, the forced merge and
the path-independent binding ledger depend only on the kernel being ODD
and on the count product commuting — never on its form. Verified across
four kernels including an arbitrary one. So the far-field results are
inherited intact and only the orbit's shape changes with the rung, which
is exactly the comb.
"""

import math
from fractions import Fraction as F

UMIN = 2.0 ** -40


def census(d, umin=UMIN):
    """The exact small-rung kernel's potential: the carry census, summed
    over the depths that register a separation d."""
    J = min(math.floor(math.log2(1 / d)), math.floor(math.log2(1 / umin)))
    return 2 ** (J + 1) - 1


def _odd(kernel):
    """Wrap a magnitude law into an odd kernel on the line."""
    return lambda u: (F(1) if u > 0 else F(-1)) * kernel(abs(u)) if u else F(0)


KERNELS = {
    "sign (the 1D anchor)": _odd(lambda a: F(1)),
    "far field": _odd(lambda a: F(1, (a + 1) ** 2)),
    "small-rung census": _odd(lambda a: F(2 ** min(int(a).bit_length(), 8))),
    "arbitrary odd": _odd(lambda a: F(3, a + 2)),
}


def tick(riders, D, g=F(1)):
    acc = [g * sum(kj * D(xj - xi)
                   for j, (kj, xj, vj) in enumerate(riders) if j != i)
           for i, (ki, xi, vi) in enumerate(riders)]
    return [[k, x + v + a, v + a] for (k, x, v), a in zip(riders, acc)], acc


def test_the_census_total_is_the_saturation_ceiling():
    """Summed over every depth the census gives 2/u_min — the ceiling the
    operation movement derives — so the kernel and the ceiling are one
    expression rather than two claims."""
    for umin in (2.0 ** -10, 2.0 ** -20, 2.0 ** -40):
        total = census(umin / 2, umin)
        assert abs(total / (2 / umin) - 1) < 1e-3


def test_the_census_staircase_is_periodic_by_the_octave():
    """The ratio of the exact kernel to the smooth law repeats once per
    doubling of separation, to floating precision — the same period the
    envelope's residual carries."""
    ratios = []
    for k in range(32):
        d = 2.0 ** -20 * (2 ** (k / 16.0))
        ratios.append(census(d) / (2 / d - 1))
    first, second = ratios[:16], ratios[16:]
    assert max(abs(a - b) for a, b in zip(first, second)) < 1e-6
    assert max(first) - min(first) > 0.3            # a real modulation
    assert abs(first[0] - 1.0) < 1e-9               # exact at the octave marks


def test_the_third_law_holds_for_every_odd_kernel():
    """Momentum is conserved exactly under each kernel, including one
    chosen arbitrarily: the law rests on oddness and on the count
    product commuting, not on the kernel's shape."""
    for name, D in KERNELS.items():
        riders = [[F(2), F(0), F(0)], [F(3), F(7), F(0)], [F(5), F(19), F(0)]]
        state, _ = tick(riders, D)
        assert sum(k * v for k, x, v in state) == 0, name


def test_the_equivalence_principle_holds_for_every_odd_kernel():
    """Two riders of different count at the same address take the same
    acceleration under any kernel — the response is independent of the
    rider, which is the relative-shortfall uniformity."""
    for name, D in KERNELS.items():
        for k_test in (F(1), F(9), F(40)):
            riders = [[k_test, F(0), F(0)], [F(7), F(11), F(0)]]
            _, acc = tick(riders, D)
            assert acc[0] == F(7) * D(F(11)), (name, k_test)


def test_the_merge_and_the_binding_ledger_are_kernel_free():
    """The merge is an address holding a total, and its cost is the
    reduced-count relative term — neither statement mentions the kernel,
    so both are inherited from the far field unchanged."""
    for k1, v1, k2, v2 in ((F(2), F(3), F(5), F(-1)), (F(1), F(0), F(1), F(4))):
        K = k1 + k2
        V = (k1 * v1 + k2 * v2) / K
        before = k1 * v1 ** 2 / 2 + k2 * v2 ** 2 / 2
        after = K * V ** 2 / 2
        reduced = k1 * k2 / K
        assert before - after == reduced * (v1 - v2) ** 2 / 2   # exact
        assert before - after >= 0                              # one-signed
        assert k1 * v1 + k2 * v2 == K * V                       # momentum kept


def test_only_the_orbit_shape_depends_on_the_rung():
    """What the kernel does change: the trajectory. Same initial state,
    different kernels, different paths — so the small-rung rule is a
    dynamical refinement of the far field, not a revision of its laws."""
    paths = {}
    for name, D in KERNELS.items():
        state = [[F(1), F(0), F(0)], [F(1), F(9), F(0)]]
        for _ in range(6):
            state, _ = tick(state, D)
        paths[name] = tuple(x for k, x, v in state)
    assert len(set(paths.values())) == len(paths)      # all four differ
