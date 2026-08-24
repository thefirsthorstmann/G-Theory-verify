"""test_the_covariant_trigger.py — THE BOARD'S DEEPEST CUT, PAID
(2026-08-17). The objection: §9's meeting theorem speaks of two clocks
"run on one shared tick," and simultaneity of carry boundaries at
separated places is frame-dependent — the failure mode that has decided
discrete programs before, since a regular tick lattice generically names
a rest frame.

The discharge is that the shared tick was never the content. A union is a
pair of carry boundaries — one on each record's own worldline, at its own
proper count — that are NULL-SEPARATED. Both ingredients are invariant:
the proper count is each record's own (§17's invariant content) and null
separation is frame-independent. From that condition alone, in the pair's
mutual rest frame, the union condition reads jq − ip = m with m the
separation in ticks, whose solutions exist exactly when gcd(p,q) divides
m and then recur every lcm(p,q) — so **the rate is gcd(p,q)/pq, the
banked law, recovered from an invariant statement.** The sharpening is
free: coprime periods divide every separation, so the bilinear rate holds
everywhere and the commensurate enhancement is confined to commensurate
separations.

Two consequences are checked rather than asserted. The elementary trigger
is selective per tick and does NOT smooth with ensemble size; what smooths
it is averaging over separation, which every instrument does — a
256-tick window returns the bilinear product to a part in a thousand.
And aberration cancels: because the null connection carries the record's
RATE along with its count, the receiver extrapolates to the present
position, the first-order lag cancels exactly, and the residual is third
order with coefficient 4/3 — the same two orders of cancellation general
relativity achieves, with the remainder at the radiative order.
"""

import math
import random
from math import gcd


def unions(p, q, m, T):
    """Null connection from A's boundary i·p to B's boundary j·q across a
    separation of m ticks: the light lands at i·p + m, which must be a
    boundary of B."""
    return [(i, (i * p + m) // q) for i in range(T // p + 1)
            if (i * p + m) % q == 0 and i * p + m <= T]


def test_the_invariant_condition_returns_the_banked_rate():
    """Rate gcd(p,q)/pq, with unions existing exactly when gcd divides
    the separation — the banked law and one sharpening, from a condition
    that names no global clock."""
    for p, q, m in ((3, 5, 1), (3, 5, 7), (4, 6, 2), (6, 10, 4), (7, 7, 7)):
        g = gcd(p, q)
        assert m % g == 0
        T = 20 * p * q
        rate = len(unions(p, q, m, T)) / T
        assert abs(rate - g / (p * q)) < 2e-3, (p, q, m)
    for p, q, m in ((4, 6, 3), (7, 7, 3), (6, 10, 5)):
        assert m % gcd(p, q) != 0
        assert unions(p, q, m, 20 * p * q) == []      # no union at all


def test_the_recurrence_is_the_lcm():
    """Consecutive solutions of jq − ip = m sit one lcm(p,q) apart in
    either record's own count — which is why the rate inverts it."""
    for p, q, m in ((3, 5, 1), (4, 6, 2), (5, 7, 3)):
        u = unions(p, q, m, 40 * p * q)
        steps = {b[0] * p - a[0] * p for a, b in zip(u, u[1:])}
        assert steps == {p * q // gcd(p, q)}          # exactly the lcm


def _boost(t, x, beta):
    g = 1 / math.sqrt(1 - beta * beta)
    return g * (t - beta * x), g * (x - beta * t)


def test_the_union_set_is_frame_independent_and_the_naive_one_is_not():
    """The decisive test. Boost the same two worldlines and re-find the
    unions: the null-connected set is identical at every boost, while
    the coordinate-simultaneous set — the reading the objection attacks —
    is populated at rest and EMPTY under any boost. The shared tick was
    a description, not the mechanism."""
    p, q, d = 3, 5, 1
    A = [(i * p, 0.0) for i in range(12)]
    B = [(j * q, float(d)) for j in range(8)]
    invariant_sets, naive_sets = [], []
    for beta in (0.0, 0.5, 0.8, -0.6):
        Ab = [_boost(t, x, beta) for t, x in A]
        Bb = [_boost(t, x, beta) for t, x in B]
        invariant_sets.append({(i, j) for i, (ta, xa) in enumerate(Ab)
                               for j, (tb, xb) in enumerate(Bb)
                               if abs(abs(tb - ta) - abs(xb - xa)) < 1e-9 and tb > ta})
        naive_sets.append({(i, j) for i, (ta, _) in enumerate(Ab)
                           for j, (tb, _) in enumerate(Bb) if abs(tb - ta) < 1e-9})
    assert len(set(map(frozenset, invariant_sets))) == 1        # one set, all frames
    assert invariant_sets[0] == {(3, 2), (8, 5)}
    assert naive_sets[0] and not any(naive_sets[1:])            # the naive one dies


def test_selectivity_is_per_tick_and_averages_to_the_bilinear_law():
    """Honest about what does and does not smooth it: the per-tick
    selectivity survives any ensemble size, and what removes it is
    averaging over separation. A 256-tick window returns the bilinear
    product to a part in a thousand, so no instrument that fails to
    resolve a single register cell can see the structure."""
    rng = random.Random(7)
    PA = rng.sample(range(2, 2000), 48)
    PB = rng.sample(range(2, 2000), 48)
    rate = lambda m: sum(gcd(p, q) / (p * q)
                         for p in PA for q in PB if m % gcd(p, q) == 0)
    bilinear = sum(1 / p for p in PA) * sum(1 / q for q in PB)
    raw = [rate(m) for m in range(1, 400)]

    def windowed(w):
        av = [sum(raw[i:i + w]) / w for i in range(0, len(raw) - w + 1)]
        return (max(av) - min(av)) / (sum(av) / len(av)), (sum(av) / len(av)) / bilinear

    s1, _ = windowed(1)
    s256, ratio256 = windowed(256)
    assert s1 > 1.0                                   # raw: order-unity structure
    assert s256 < 0.02                                # windowed: flat
    assert abs(ratio256 - 1) < 0.01                   # and it rides the bilinear law


def _angles(beta, D=1.0):
    """Circular binary: the lag of the retarded direction and the residual
    of the rate-extrapolated one, both measured against the true one."""
    om, tau = 2 * beta / D, D
    th = math.pi - om * tau
    Br = (D / 2 * math.cos(th), D / 2 * math.sin(th))
    vr = (-om * D / 2 * math.sin(th), om * D / 2 * math.cos(th))
    Bn = (-D / 2, 0.0)
    Be = (Br[0] + vr[0] * tau, Br[1] + vr[1] * tau)
    A = (D / 2, 0.0)
    ang = lambda P, Q: (math.atan2(Q[1] - A[1], Q[0] - A[0])
                        - math.atan2(P[1] - A[1], P[0] - A[0]))
    return abs(ang(Bn, Br)), abs(ang(Bn, Be))


def test_aberration_cancels_to_third_order():
    """The null connection carries the record's rate, so the receiver
    extrapolates to the present position. The retarded lag is first order
    in v/c — the Laplace disaster if it stood — and the extrapolated
    residual is THIRD order with coefficient 4/3: two full orders of
    cancellation, the order general relativity achieves, leaving the
    remainder at the radiative order where the quadrupole already sits."""
    for beta in (1e-2, 1e-3, 1e-4):
        lag, res = _angles(beta)
        assert abs(lag / beta - 1.0) < 1e-3           # first order, coefficient 1
        assert abs(res / beta ** 3 - 4 / 3) < 0.01    # third order, coefficient 4/3
    lag2, res2 = _angles(1e-3)
    lag3, res3 = _angles(1e-4)
    assert abs((lag2 / lag3) - 10) < 0.1              # one decade per decade
    assert abs((res2 / res3) - 1000) < 30             # three decades per decade
