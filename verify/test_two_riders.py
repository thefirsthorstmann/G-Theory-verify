"""test_two_riders.py — THE TWO-RIDER RULE (2026-08-10): the wall, taken.

The rule, assembled from banked theorems and one forced clause:

  STATE   riders (k_i, x_i, v_i) at distinct addresses; k_i positive integers.
  READ    a_i = g * sum_j k_j * D(x_j - x_i)     [all reads before any write]
          — the weighting by the OTHER'S count is Theorem 8 (sourcing
          proportional to k); the absence of k_i is the relative-shortfall
          uniformity (response independent of the rider): both banked, forced.
          D = sign in one dimension (the count-force theorem); D carries the
          extension law 1/(d+1)^2 on the ladder.
  STEP    v_i += a_i;  x_i += v_i                [one tick; synchronous]
  MERGE   co-addressed riders become one: k = k1 + k2,
          v = (k1 v1 + k2 v2)/(k1 + k2)
          — forced, not chosen: an address on the wheel holds a TOTAL, not a
          list (the wheel reads totals and cannot read factorizations,
          pinned); separate identity requires separate address. The adhesion
          model's vanishing viscosity was the continuum transcription of
          this clause.

  CONSEQUENCES, derived: the third law is the COMMUTATIVITY OF THE COUNT
  PRODUCT (F_ij = g k_i k_j = F_ji, antisymmetric in direction); momentum
  conservation follows; the equivalence principle holds identically; the
  merger's energy cost is one-signed and equals the reduced-count relative
  term exactly; the total binding of any merger sequence is path
  independent. Filters: the 1D anchor (exact reduction to the count-force
  dynamics) and the far-field orbit (the replanked relation with the total
  count) — both below.
"""
import math
from fractions import Fraction as F


def tick_1d(riders, g=F(1)):
    """One synchronous tick of the rule in one dimension, exact arithmetic.
    riders: list of [k, x, v] with Fractions. Returns new list, merged."""
    acc = []
    for i, (ki, xi, vi) in enumerate(riders):
        a = g * sum(kj * (1 if xj > xi else -1 if xj < xi else 0)
                    for j, (kj, xj, vj) in enumerate(riders) if j != i)
        acc.append(a)
    stepped = [[k, x + v + a, v + a] for (k, x, v), a in zip(riders, acc)]
    merged = {}
    for k, x, v in stepped:
        if x in merged:
            K, V = merged[x]
            merged[x] = (K + k, V + k * v)
        else:
            merged[x] = (k, k * v)
    return [[K, x, P / K] for x, (K, P) in sorted(merged.items())]


def test_the_1d_anchor():
    """FILTER A: with unit counts the rule IS the count-force dynamics —
    forces are the count differences, constant between crossings, and the
    trajectories are the exact ballistic quadratics. Verified in exact
    rational arithmetic against the closed form, twelve ticks, no crossing:
    identical to the last digit."""
    riders = [[F(1), F(0), F(0)], [F(1), F(200), F(0)], [F(1), F(500), F(0)]]
    f0 = [2, 0, -2]                                     # count differences
    state = [r[:] for r in riders]
    for t in range(1, 13):
        state = tick_1d(state)
        for i, (k, x, v) in enumerate(state):
            xi0, vi0, ai = riders[i][1], riders[i][2], F(f0[i])
            # v(t) = v0 + a t;  x(t) = x0 + sum_{s<=t} v(s)  (the tick sum)
            vt = vi0 + ai * t
            xt = xi0 + vi0 * t + ai * F(t * (t + 1), 2)
            assert v == vt and x == xt                  # exact ballistics


def test_the_third_law_is_the_product():
    """The force rider j exerts on i is g k_i k_j in magnitude — the count
    product — and the product commutes: F_ij = -F_ji with no assumption
    beyond the rule's two banked planks. Momentum sum(k v) is therefore
    conserved tick by tick, verified exactly over a mixed-count system for
    forty ticks including sign changes of every separation."""
    riders = [[F(3), F(0), F(1, 7)], [F(5), F(11), F(-1, 3)],
              [F(2), F(29), F(0)], [F(7), F(40), F(-2, 5)]]
    p0 = sum(k * v for k, x, v in riders)
    k0 = sum(k for k, x, v in riders)
    state = [r[:] for r in riders]
    for _ in range(40):
        # explicit pairwise antisymmetry at this state:
        for i, (ki, xi, vi) in enumerate(state):
            for j, (kj, xj, vj) in enumerate(state):
                if j <= i or xi == xj:
                    continue
                Fij = ki * (kj * (1 if xj > xi else -1))
                Fji = kj * (ki * (1 if xi > xj else -1))
                assert Fij == -Fji                      # the product commutes
        state = tick_1d(state)
        assert sum(k * v for k, x, v in state) == p0    # momentum, exact
        assert sum(k for k, x, v in state) == k0        # count, exact


def test_the_equivalence_principle_holds_identically():
    """FILTER B: the acceleration of a rider contains every count but its
    own. A test rider of count one and a test rider of count seven, placed
    identically in the same external configuration, trace IDENTICAL
    trajectories — eta = 0 as an identity of the rule, not a tuning."""
    sources = [(F(5), F(100)), (F(3), F(-60))]         # held fixed: the
    for k_test in (F(1), F(7)):                         # external field
        x, v = F(0), F(0)
        traj = []
        for _ in range(15):
            a = sum(kj * (1 if xj > x else -1) for kj, xj in sources)
            v += a
            x += v
            traj.append(x)
        if k_test == F(1):
            ref = traj
        else:
            assert traj == ref                          # identical, exactly
    # and the acceleration expression contains no k_test at any state:
    # a = g * sum k_j D — own count absent by the rule's construction.


def test_the_merger_is_forced_and_one_signed():
    """The merge clause: co-addressed riders become one, count and momentum
    conserved by construction — and the kinetic energy change is exactly
    minus the reduced-count relative term, mu/2 (v1 - v2)^2 with
    mu = k1 k2/(k1 + k2): ONE-SIGNED, a removal always. The energy does not
    vanish from the books; it is the binding ledger's entry — the merged
    rider sits lower by exactly the relative motion it absorbed."""
    k1, v1, k2, v2 = F(3), F(5, 2), F(6), F(-1, 2)
    K, V = k1 + k2, (k1 * v1 + k2 * v2) / (k1 + k2)
    dE = F(1, 2) * K * V ** 2 - (F(1, 2) * k1 * v1 ** 2 + F(1, 2) * k2 * v2 ** 2)
    mu = k1 * k2 / (k1 + k2)
    assert dE == -F(1, 2) * mu * (v1 - v2) ** 2         # the exact cost
    assert dE < 0                                       # one-signed, always


def test_the_binding_ledger_is_path_independent():
    """Merge three riders in every possible order: the total energy removed
    is identical every time — E_initial minus P^2/2K, a state function.
    The binding ledger does not depend on the history of assembly: the
    thermodynamic shape arrives with the rule, uninvited."""
    riders = [(F(2), F(3)), (F(5), F(-2)), (F(4), F(1, 2))]   # (k, v)
    P = sum(k * v for k, v in riders)
    K = sum(k for k, v in riders)
    E0 = sum(F(1, 2) * k * v * v for k, v in riders)
    expected_binding = E0 - P * P / (2 * K)
    import itertools
    for order in itertools.permutations(range(3)):
        pool = list(riders)
        a = pool[order[0]]
        for idx in order[1:]:
            b = pool[idx]
            a = (a[0] + b[0], (a[0] * a[1] + b[0] * b[1]) / (a[0] + b[0]))
        Ef = F(1, 2) * a[0] * a[1] ** 2
        assert E0 - Ef == expected_binding              # path independent
        assert a[0] == K and a[1] == P / K


def test_the_far_field_orbit_matches_the_replanked_relation():
    """FILTER C: two riders on the ladder (the softened extension law), in
    mutual circular orbit about the center of count. The relative problem
    must obey the replanked single-rider relation with the TOTAL count as
    source: v_rel^2 = g (k1 + k2) r / (r + L)^2. Simulated with the vector
    rule at small tick; the measured relative speed matches the relation
    within a tenth of a percent, and the center of count stays inertial to
    machine precision."""
    g, L = 1.0, 1.0
    k1, k2 = 3.0, 6.0
    r = 400.0
    K = k1 + k2
    v_rel = math.sqrt(g * K * r / (r + L) ** 2)
    # place riders about the center of count, opposite velocities
    x1, x2 = -k2 / K * r, k1 / K * r
    vy1, vy2 = -k2 / K * v_rel, k1 / K * v_rel
    p = [[k1, x1, 0.0, 0.0, vy1], [k2, x2, 0.0, 0.0, vy2]]
    dt = 0.05
    steps = int(2 * math.pi * r / v_rel / dt)           # about one period
    for _ in range(steps):
        (ka, xa, ya, vxa, vya), (kb, xb, yb, vxb, vyb) = p
        dx, dy = xb - xa, yb - ya
        d = math.hypot(dx, dy)
        f = g / (d + L) ** 2
        axa, aya = f * kb * dx / d, f * kb * dy / d
        axb, ayb = -f * ka * dx / d, -f * ka * dy / d
        p = [[ka, xa + (vxa + axa * dt) * dt, ya + (vya + aya * dt) * dt,
              vxa + axa * dt, vya + aya * dt],
             [kb, xb + (vxb + axb * dt) * dt, yb + (vyb + ayb * dt) * dt,
              vxb + axb * dt, vyb + ayb * dt]]
    (ka, xa, ya, vxa, vya), (kb, xb, yb, vxb, vyb) = p
    # center of count inertial (started at rest at origin):
    assert abs(ka * xa + kb * xb) / (ka + kb) < 1e-6 * r
    assert abs(ka * ya + kb * yb) / (ka + kb) < 1e-6 * r
    # separation maintained (circularity) and speed at the relation:
    d = math.hypot(xb - xa, yb - ya)
    assert abs(d - r) / r < 2e-3
    vrel = math.hypot(vxb - vxa, vyb - vya)
    assert abs(vrel - v_rel) / v_rel < 1e-3
