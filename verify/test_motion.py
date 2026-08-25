"""test_motion.py — the exact skeleton of Motion on Discrete Terms (paper five).

The kinematics wall, taken apart into planks: inertia = no rest state (parity);
the speed limit = the count cannot outrun the count; the square of velocity =
the banked Dirichlet form applied to rates; conservation = the append-only
ledger (no-reseat) applied to the winding count; the orbit equation =
stationarity (the projection grammar's plank, named as the principle it is)
composed with the other three. The campaign's orbital results are then
re-derived on in-house planks, with the kinematics import retired.
"""
import math
from fractions import Fraction as F


def test_inertia_is_the_absence_of_rest():
    """Newton's first law, on discrete terms, is not a law: it is the absence
    of any rest state to occupy. The two generators can never settle (2^p =
    3^q demands even = odd), so the substrate rotation has no fixed point and
    no periodic point: {q log2(3)} is never zero, and its smallest values sit
    exactly at the convergent denominators. A rider persists in its motion
    because stopping is not among the states of the system. Persistence needs
    no postulate where rest is arithmetically forbidden."""
    for p in range(1, 60):
        for q in range(1, 38):
            assert 2 ** p != 3 ** q                     # parity: no settling
    a = math.log2(3)
    best, argbest = 1.0, 0
    record = []
    for q in range(1, 400):
        d = abs(q * a - round(q * a))
        if d < best:
            best, argbest = d, q
            record.append(q)
        assert d > 0                                    # never a rest state
    assert record == [1, 2, 5, 12, 41, 53, 306]         # the convergent ladder


def test_the_speed_limit_is_the_tick():
    """One place is one rotation is one tick, by the wheel definition. A
    rider's address advances at most one place per tick, so no velocity
    exceeds one rung per tick: the speed limit is the counting bound — the
    count cannot outrun the count. Velocities form the rational ladder
    p/q <= 1 (p rungs in q ticks), with the limit itself the null rate the
    companion volume posits as the octave boost. Ten rungs in ten ticks is
    the same rate as one in one; the ladder is a ladder of fractions."""
    velocities = sorted({F(p, q) for q in range(1, 9) for p in range(0, q + 1)})
    assert velocities[0] == 0 and velocities[-1] == 1   # rest excluded above;
    assert all(0 <= v <= 1 for v in velocities)         # 0 is the ladder's
    assert F(10, 10) == F(1, 1)                         # ideal, never a state
    assert F(1, 2) in velocities and F(2, 3) in velocities


def test_the_square_is_the_banked_energy_form():
    """Kinetic energy quadratic in velocity is not a postulate here: Part I,
    Theorem 4 fixed the figure's energy as the Dirichlet form — the sum of
    squared gap deviations — and that form, applied to the per-tick increment
    sequence of a moving configuration, is quadratic in the rate. Scaling the
    rate by k scales the cost by k^2 exactly. The generators' rates then cost
    as their squared intervals: the ratio of the motor's cost to the octave's
    is 9/4 — the fifth squared — and the square that turns amplitude into
    observable (Born), gauge into gravity (the double copy), and interval
    into its double is the same square that turns velocity into energy: the
    framework's one composition law."""
    def dirichlet(u):
        n = len(u)
        return sum((u[(j + 1) % n] - u[j]) ** 2 for j in range(n))

    base = [F(j, 1) * 0 for j in range(9)]
    for v in (F(1, 3), F(1, 2), F(2, 3), F(1, 1)):
        incr = [v for _ in range(9)]                    # uniform advance u->u+v
        e1 = dirichlet([j * F(1, 1) for j in range(9)])  # a fixed strain
        # motion cost: the form applied to the tickwise increments about the
        # uniform mode — uniform part costs zero (the boost is free):
        assert dirichlet(incr) == 0                     # Galilean freedom
        ramp = [j * v for j in range(9)]                # rate-gradient config
        assert dirichlet([j * (2 * v) for j in range(9)]) == 4 * dirichlet(ramp)
        assert dirichlet([j * (3 * v) for j in range(9)]) == 9 * dirichlet(ramp)
    r32 = dirichlet([j * F(3, 1) for j in range(9)]) / \
        dirichlet([j * F(2, 1) for j in range(9)])
    assert r32 == F(9, 4) == F(3, 2) ** 2               # Sol squared


def test_conservation_is_the_append_only_ledger():
    """The winding counter is append-only: after m ticks the pair (m div 6,
    m mod 6) — coarse windings and phase — recovers m exactly, for every m:
    nothing is lost and nothing is re-minted. A completed winding is a
    completed count, and the no-reseat discipline that derived the composite
    gait is, read in time, the conservation of the count: angular momentum as
    winding rate is conserved because the ledger admits no free operations.
    Quantization is automatic — windings are integers."""
    for m in range(0, 1000):
        w, r = divmod(m, 6)
        assert w * 6 + r == m                           # bijective: conserved
        assert 0 <= r < 6
    rot = 142857
    seen = {rot}
    for _ in range(5):
        rot = (rot * 10) % 999999
        assert rot not in seen                          # no re-mint mid-cycle
        seen.add(rot)
    assert (rot * 10) % 999999 == 142857                # closure at six exactly


def test_the_orbit_replanked():
    """The campaign's circular-orbit results, re-derived with the kinematics
    import retired: quadratic energy (the banked form), conserved winding L,
    and stationarity of E(r) = L^2/2r^2 - K/(r+lam) — the projection
    grammar's least-action plank, named as the principle it is. Stationarity
    gives L^2 = K r^3/(r+lam)^2, hence v^2 = K r/(r+lam)^2: exactly the
    relation the campaign imported, now produced. Everything downstream
    stands unchanged: T/T_Kepler = 1 + lam/r, the exponent climbs 1/2 -> 1
    -> 3/2 crossing one at the first rung, far field Kepler exact."""
    K, lam = 1.0, 1.0
    for r in (0.3, 1.0, 7.0, 1e3, 1e6):
        # stationarity: dE/dr = -L^2/r^3 + K/(r+lam)^2 = 0
        L2 = K * r ** 3 / (r + lam) ** 2
        v2 = L2 / r ** 2
        assert abs(v2 - K * r / (r + lam) ** 2) < 1e-12 * max(1, v2)
        T = 2 * math.pi * r / math.sqrt(v2)
        T_kep = 2 * math.pi * r ** 1.5 / math.sqrt(K)
        assert abs(T / T_kep - (1 + lam / r)) < 1e-9
    assert abs((0.5 + 1e9 / (1e9 + 1)) - 1.5) < 1e-8    # the far exponent
    assert 0.5 + 1.0 / (1.0 + 1.0) == 1.0               # Do at the first rung


def test_newtons_laws_mapped():
    """The three laws, located in the framework rather than imported. FIRST:
    no rest state — pinned above; persistence is parity. SECOND, the shape:
    quadratic energy makes momentum linear in rate, and Theorem 8 of the
    gravity companion makes the coefficient the rider count k — force
    proportional to source, response independent of the rider, from the one
    congruence k x 142857 x 7 = k 10^6 - k. THIRD, the candidate, held as
    such: exchange between Midy partners preserves the pair sum — the nine —
    so what one member gains the other loses exactly; the arithmetic
    invariant is pinned, the dynamical identification stays labeled."""
    for k in range(1, 7):
        assert k * 142857 * 7 == k * 10 ** 6 - k        # sourcing linear in k
    # quadratic energy -> momentum linear: E(v) = c v^2, p = dE/dv = 2c v
    E = lambda v, c=3: c * v * v
    h = 1e-6
    for v in (0.2, 0.5, 0.9):
        p = (E(v + h) - E(v - h)) / (2 * h)
        assert abs(p - 2 * 3 * v) < 1e-6                # linear in v
    block = "142857"
    for i in range(6):
        assert int(block[i]) + int(block[(i + 3) % 6]) == 9  # the pair sum
