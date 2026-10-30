"""test_structure_growth.py — the structure campaign's first two targets
(2026-08-10): the linear-growth inheritance pin, and the pair-layer skew
theorem behind the f_NL forbid.

Growth is an inheritance check in the Kepler manner: the standard linear
growth equation uses only ingredients the program has already located — the
far-field deficit law, conservation as the ledger, the standard background
(the declared inheritance of the vacuum paper) — so its exponents must come
out standard, and they do; the seat reading of those exponents is exact
arithmetic on a labeled reading. The skew theorem is exact on the wheel: a
mirror-even ensemble has identically vanishing odd moments, which is the
mechanism of the f_NL forbid; the identification of primordial fluctuations
with pair-layer statistics carries the same labeled-join status as the
vacuum paper's Interpretation 2, and the forbid is stated on that account.
"""
import math
from fractions import Fraction as F


def test_the_growth_exponents_are_seat_addresses():
    """The matter-era linear growth equation's indicial polynomial is
    3m^2 + m - 2 = (3m - 2)(m + 1): growing mode t^(2/3), decaying mode
    t^(-1), exactly. THE SEAT READING (labeled, arithmetic exact): the
    growing exponent 2/3 is La's descending address; in scale-factor terms
    the growing mode is a^1 — Do — so growth counts rungs one for one with
    the expansion (delta proportional to a), and the decaying mode is
    a^(-3/2) — the fifth downward. And the background itself walks the
    descending-ratio column: radiation era a ~ t^(1/2) (Sol's address, 180
    degrees), matter era a ~ t^(2/3) (La's address, 240 degrees) — THE ERA
    TRANSITION IS ONE TICK, sixty degrees, one place of the wheel."""
    # (3m - 2)(m + 1) = 3m^2 + m - 2: the exact roots
    roots = [F(2, 3), F(-1)]
    for m in roots:
        assert 3 * m ** 2 + m - 2 == 0
    grow_t, decay_t = roots
    assert grow_t == F(2, 3)                            # La's descending ratio
    # matter era t = a^(3/2): convert time exponents to a exponents
    grow_a = grow_t * F(3, 2)
    decay_a = decay_t * F(3, 2)
    assert grow_a == 1                                  # delta ~ a: Do
    assert decay_a == F(-3, 2)                          # the fifth downward
    # the background's own column
    assert F(1, 2) * 360 == 180 and F(2, 3) * 360 == 240
    assert (F(2, 3) - F(1, 2)) * 360 == 60              # one tick per era step


def test_the_growth_equation_integrates_to_the_exponent():
    """The equation itself, integrated cold: ddot(delta) + (4/3t) dot(delta)
    - (2/3 t^2) delta = 0 from generic initial data converges onto the
    growing mode t^(2/3). The ingredients are the program's: the far-field
    deficit law for the source, the ledger for conservation, the declared
    standard background — an inheritance in the Kepler manner, conditional
    on the same named planks."""
    t, dt = 1.0, 1e-5
    d, v = 1.0, 0.0                                     # generic start
    while t < 200.0:
        a_ = -(4.0 / (3.0 * t)) * v + (2.0 / (3.0 * t * t)) * d
        v += a_ * dt
        d += v * dt
        t += dt
    # local exponent d ln delta / d ln t at late time
    d2, v2 = d + v * (t * 1e-4), None
    expo = (t * v) / d
    assert abs(expo - 2.0 / 3.0) < 1e-3                 # the growing mode


def test_the_pair_layer_skew_vanishes():
    """THE MECHANISM OF THE f_NL FORBID, exact. The figure's energy is the
    Dirichlet form, and it is EVEN under a global sign flip: E(-u) = E(u)
    identically. Any ensemble weighted by an even function of the
    configuration is closed under u -> -u with equal weights, so every odd
    moment of every linear observable vanishes IDENTICALLY — not
    approximately: the third moment cancels pair by pair. Enumerated in full
    over all 3^9 configurations u in {-1,0,1}^9 with an even weight, in
    exact rational arithmetic: skew = 0 exactly. On the pair-layer account
    of primordial fluctuations (the labeled join), intrinsic local
    non-Gaussianity vanishes at leading order: LARGE |f_NL| IS FORBIDDEN.
    Data: Planck 2018 f_NL(local) = -0.9 +/- 5.1, consistent with zero;
    SPHEREx targets sigma of order one — a decisive |f_NL| of a few would
    refute the pair-layer account outright."""
    from itertools import product

    def dirichlet(u):
        return sum((u[(j + 1) % 9] - u[j]) ** 2 for j in range(9))

    # exactness of the evenness, spot-checked across the space
    for u in [(1, 0, -1, 1, 1, 0, -1, 0, 1), (1, 1, 1, 0, 0, 0, -1, -1, -1)]:
        assert dirichlet([-x for x in u]) == dirichlet(u)

    num = F(0)
    den = F(0)
    third_site = F(0)
    for u in product((-1, 0, 1), repeat=9):
        w = F(1, 1 + dirichlet(u))                      # any even weight
        s = sum(u)
        num += w * s ** 3                               # global third moment
        third_site += w * u[0] ** 3                     # site third moment
        den += w
    assert den > 0
    assert num == 0                                     # skew = 0 EXACTLY
    assert third_site == 0                              # sitewise too
    assert abs(-0.9) < 5.1                              # the data row, today


def test_the_one_dimensional_force_is_a_count():
    """THE FORMAL CORE OF THE ZELDOVICH RESULT. In one dimension the
    gravitational force on a particle from the others (infinite sheets) is
    F_i = g * sum_j sign(x_j - x_i): a constant times the difference of the
    counts on the two sides — A PURE COUNT, blind to every distance. Pinned
    two ways: the force equals (right count - left count) exactly, and it is
    INVARIANT under any order-preserving remapping of the positions —
    stretch the gaps arbitrarily and every force is unchanged. Gravity in
    one dimension is counting; geometry enters only with dimension."""
    xs = [0.0, 1.3, 2.0, 5.9, 11.0]
    def forces(xs):
        out = []
        for i, xi in enumerate(xs):
            s = sum((1 if xj > xi else -1) for j, xj in enumerate(xs) if j != i)
            out.append(s)
        return out
    f = forces(xs)
    for i in range(len(xs)):
        right = sum(1 for j, xj in enumerate(xs) if j != i and xj > xs[i])
        left = sum(1 for j, xj in enumerate(xs) if j != i and xj < xs[i])
        assert f[i] == right - left                     # the count difference
    stretched = [x ** 3 + 7 * x for x in xs]            # monotone remap
    assert forces(stretched) == f                       # distance-blind


def test_zeldovich_is_exact_in_one_dimension():
    """Between crossings every 1D particle feels a CONSTANT force (the count
    cannot change without a crossing), so trajectories are exactly quadratic
    — the ballistic map is not an approximation but the closed-form solution.
    Verified: a numerical integrator matches the closed form to 1e-9 up to
    the first crossing, whose time is computed in closed form; and AT the
    crossing the force ledger updates BY INTEGERS — the crossing pair's
    counts step by exactly two each, all other forces unchanged. One
    dimensional gravity is integer-stepped and event-driven: the count
    updating at counts' own events. This is the WHY of the approximation's
    success, formalized: the map is exact wherever gravity reduces to
    counting, and the three-dimensional error is the extension dressing of
    the count, not a failure of the kinematics."""
    g = 1.0
    xs = [0.0, 1.0, 2.5, 4.0, 6.0]
    vs = [0.0, 0.30, 0.0, -0.9, 0.0]

    def forces(xs):
        return [g * sum((1 if xj > xi else -1)
                        for j, xj in enumerate(xs) if j != i)
                for i, xi in enumerate(xs)]

    f0 = forces(xs)
    # closed-form first crossing between neighbors i, i+1:
    # gap(t) = dx + dv t + 0.5 df t^2 = 0, smallest positive root
    import math
    tcross, pair = None, None
    for i in range(4):
        dx = xs[i + 1] - xs[i]
        dv = vs[i + 1] - vs[i]
        df = f0[i + 1] - f0[i]
        roots = []
        if abs(df) > 1e-15:
            disc = dv * dv - 2 * df * dx
            if disc >= 0:
                for s in (+1, -1):
                    r = (-dv + s * math.sqrt(disc)) / df
                    if r > 1e-12:
                        roots.append(r)
        elif abs(dv) > 1e-15:
            r = -dx / dv
            if r > 1e-12:
                roots.append(r)
        for r in roots:
            if tcross is None or r < tcross:
                tcross, pair = r, (i, i + 1)
    assert tcross is not None and pair == (2, 3)

    # integrate to just before the crossing; compare to the quadratic map
    t_end = tcross * 0.999
    dt = t_end / 200000
    X, V = xs[:], vs[:]
    t = 0.0
    while t < t_end - dt / 2:
        F = forces(X)
        assert F == f0                                  # constant between
        X = [x + v * dt + 0.5 * fi * dt * dt            # crossings: the count
             for x, v, fi in zip(X, V, F)]              # cannot change; the
        V = [v + fi * dt for v, fi in zip(V, F)]        # Verlet step is exact
        t += dt
    for i in range(5):
        closed = xs[i] + vs[i] * t_end + 0.5 * f0[i] * t_end ** 2
        assert abs(X[i] - closed) < 1e-9                # ballistic = exact

    # step through the crossing: the ledger updates by integers
    Xc = X[:]
    Xc[2], Xc[3] = Xc[3], Xc[2]                         # order after crossing
    f1 = forces(Xc)
    assert f1[2] - f0[2] == -2 * g or f1[2] - f0[2] == 2 * g
    assert abs(f1[2] - f0[2]) == 2 * g and abs(f1[3] - f0[3]) == 2 * g
    for i in (0, 1, 4):
        assert f1[i] == f0[i]                           # spectators unchanged


def test_the_morphology_polarity_census():
    """CC: 1D pancake, 2D filament, 3D cluster — how do the rounding rules
    and polarities meet this? THE CORRESPONDENCE, pinned at its exact layer.
    Zeldovich morphology is classified by the SIGN PATTERN of three ordered
    deformation eigenvalues: void (+++), pancake (-++), filament (--+),
    cluster (---) — four classes, multiplicities 1-3-3-1, collapse
    proceeding largest-magnitude-first. The rounding ledger's anatomy
    matches piece for piece: THREE complementary pairs, strictly ordered by
    moment 5/14 > 3/14 > 1/14 (the most unbalanced first), each pair
    carrying exactly one down and one up member — three ordered dipoles,
    each two-valued. Three binary polarities give eight states in four
    classes by minus-count {0,1,2,3} with multiplicities {1,3,3,1}; the
    number of collapsed dimensions is the number of committed pairs, CC's
    own 1-2-3 ladder. The identification of pairs with axes is a labeled
    reading; every count above it is exact. The Doroshkevich fractions
    (widely quoted 8/42/42/8 percent for a Gaussian field) are a WATCH ITEM
    under the precision rule: the displayed numerals are rounded favourites
    and the exact analytic values must be computed before any numeral claim."""
    from itertools import product
    moments = [F(5, 14), F(3, 14), F(1, 14)]            # the ordered dipoles
    assert moments == sorted(moments, reverse=True)
    assert [m.denominator for m in moments] == [14, 14, 14]
    pairs = [(1, 6), (2, 5), (3, 4)]
    for k, kk in pairs:
        assert k + kk == 7                              # complement pairs
        assert k <= 3 < kk                              # one down, one up
    census = {}
    for signs in product((-1, +1), repeat=3):
        census.setdefault(signs.count(-1), 0)
        census[signs.count(-1)] += 1
    assert census == {0: 1, 1: 3, 2: 3, 3: 1}           # void sheet fil node
    assert sum(census.values()) == 8
    morphology = {0: "void", 1: "pancake", 2: "filament", 3: "cluster"}
    assert [morphology[k] for k in sorted(census)] == \
        ["void", "pancake", "filament", "cluster"]      # the 1-2-3 ladder


def test_the_natural_viscosity_of_the_count():
    """CC: 'so our non-zero is essentially naturally viscous?' YES, with the
    standard anchor made exact: any discrete conservative update PRESENTS,
    in its continuum shadow, as a viscosity proportional to the grid unit —
    the modified-equation fact. Pinned three ways on the transport equation.
    (1) The causal (upwind) update stays bounded and diffuses: a carried
    profile spreads at the effective rate nu = a dx (1-c)/2 — the count's
    shadow viscosity, proportional to the unit, vanishing only if the unit
    does. (2) The measured spreading matches that coefficient. (3) THE SIGN
    IS FORCED: the anti-causal (downwind) update carries NEGATIVE effective
    viscosity and destroys the ledger — amplitudes explode — so the shadow
    viscosity is one-signed by causality itself, the arrow in numerical
    dress. The substrate is not viscous (the ledger is exact and
    conservative); viscosity is the continuum's name for the unit's
    granularity plus the one-signed causal order — which is why the adhesion
    repair needed a positive vanishing viscosity: it was transcribing the
    count."""
    import math
    N, a, c = 400, 1.0, 0.5
    dx = 1.0
    dt = c * dx / a
    nu_eff = a * dx * (1 - c) / 2.0

    def gaussian(center, sig):
        return [math.exp(-0.5 * ((i - center) / sig) ** 2) for i in range(N)]

    def variance(u):
        m = sum(u)
        mean = sum(i * ui for i, ui in enumerate(u)) / m
        return sum((i - mean) ** 2 * ui for i, ui in enumerate(u)) / m

    # causal update: information from the direction motion comes from
    u = gaussian(100.0, 5.0)
    v0 = variance(u)
    steps = 100
    for _ in range(steps):
        u = [u[i] - c * (u[i] - u[i - 1]) for i in range(N)]
    assert max(u) <= 1.0 + 1e-12                        # bounded: ledger kept
    growth = variance(u) - v0
    expected = 2 * nu_eff * steps * dt
    assert abs(growth - expected) / expected < 0.15     # nu = a dx (1-c)/2
    # anti-causal update: negative shadow viscosity, the ledger destroyed
    w = gaussian(100.0, 5.0)
    for _ in range(60):
        w = [w[i] - c * (w[(i + 1) % N] - w[i]) for i in range(N)]
    assert max(w) > 10.0                                # one-signedness forced
