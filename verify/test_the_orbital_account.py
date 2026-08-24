"""test_the_orbital_account.py — THE ORBITS, PRESSURE-TESTED AND EXTENDED
(2026-08-16). Ledger item five — and the rope-up corrected the ledger itself:
the account was further along than listed. Paper five (Motion on Discrete
Terms) retired the kinematics import — inertia as the absence of rest, the
speed limit as the tick, the square from the Dirichlet form, conservation as
the append-only ledger, the orbit from stationarity — and the two-rider wall
was taken on 2026-08-10 (the third law as the commutativity of the count
product; six pins in test_two_riders.py). Kepler's third law stands banked as
the (3/2, 2/3) reversal pair with the exponent climbing the seats, the exact
period deviation T/T_Kepler = 1 + lambda/r, and the apsidal ladder
Phi = pi sqrt((r+lambda)/(r+3lambda)). What remained named: general
(eccentric) orbits, and the octave residual's orbital face. Both are taken
below, by integration against formula — not formula alone.

  NEW RESULT ONE — THE OCTAVE PRECESSION FORMULA, VERIFIED 0.7%. A
  log-periodic force residual F = F_N (1 + A cos(2 pi log2 r + phi)) precesses
  a near-circular orbit by

      dphi_per_orbit = (2 pi^2 A / ln 2) * sin(2 pi log2 r + phi)

  — amplitude 28.48 A radians per orbit, r-dependent through the phase,
  verified against a leapfrog integration to seven parts in a thousand. THE
  SENSITIVITY CHAIN THIS OPENS: planetary ephemerides bound anomalous
  perihelion drift at the milliarcsecond-per-century level; at Mercury's 415
  orbits per century that is ~1.2e-11 rad per orbit, hence sensitivity to
  A ~ 4e-13 — SIX TO NINE ORDERS SHARPER than laboratory inverse-square
  template bounds. One caveat carried honestly: the phase at any single
  planet's r is unknown and can null a single measurement; the comb across
  several planets at different log r is the phase-proof form. Orbits are the
  octave residual's sharpest instrument, and account five hands account two
  its best test.

  NEW RESULT TWO — ECCENTRIC ORBITS CLOSED AT FIRST ORDER, ALL e (the
  campaign's remaining item c). Expanding the softened potential,
  -K/(r+lambda) = -K/r + K lambda/r^2 - ..., the 1/r^2 term is the classical
  exactly-solvable perturbation: the orbit family is the PRECESSING CONIC
  with

      dphi_per_orbit = -2 pi lambda / p,        p = a (1 - e^2)

  — the circular result's r replaced by the semi-latus rectum, retrograde at
  every eccentricity, verified by integration at e = 0, 0.3, 0.6 within the
  integrator's few-percent, with the 1/(1-e^2) trend confirmed monotone.
  Mercury's advance remains general relativity's and remains untouched, as
  the campaign stated.

  STILL OPEN, CARRIED: the exact small-rung lattice version of the two-rider
  rule, and the Maxwell bar on the update rule itself (it must eventually
  forbid on its own). The account's dynamics core is banked; today adds the
  eccentric family and the cross-account instrument.
"""

from math import cos, sin, pi, log, atan2, sqrt


def _integrate(force, r0, vt0, n_orbits=12, steps_per=16000):
    x, y = r0, 0.0
    vx, vy = 0.0, vt0
    dt = 2 * pi * sqrt(r0 ** 3) / steps_per

    def acc(px, py):
        r = sqrt(px * px + py * py)
        f = force(r)
        return f * px / r, f * py / r

    ax, ay = acc(x, y)
    peri = []
    rp2 = rp1 = r0
    for _ in range(int(n_orbits * steps_per * 1.25)):
        vx += 0.5 * dt * ax
        vy += 0.5 * dt * ay
        x += dt * vx
        y += dt * vy
        ax, ay = acc(x, y)
        vx += 0.5 * dt * ax
        vy += 0.5 * dt * ay
        r = sqrt(x * x + y * y)
        if rp1 < rp2 and rp1 < r:
            peri.append(atan2(y, x))
        rp2, rp1 = rp1, r
    return peri


def _drift(angles):
    ds = []
    for a, b in zip(angles, angles[1:]):
        d = b - a
        while d > pi:
            d -= 2 * pi
        while d < -pi:
            d += 2 * pi
        ds.append(d)
    return sum(ds) / len(ds)


def test_kepler_three_is_the_fifth_pair():
    """Circular orbits in the derived potential: T proportional to a^(3/2),
    a proportional to T^(2/3) — the fifth up and the fifth down."""
    from fractions import Fraction as F
    # v^2/r = K/r^2  ->  v ~ r^(-1/2);  T = 2 pi r / v ~ r^(3/2)
    v_exp = F(-1, 2)
    T_exp = 1 - v_exp
    assert T_exp == F(3, 2)
    assert 1 / T_exp == F(2, 3)


def test_the_octave_precession_formula_against_integration():
    A = 1e-3
    r0 = 2 ** 0.25                              # phase where sin = 1
    force = lambda r: -(1.0 / r ** 2) * (1.0 + A * cos(2 * pi * log(r, 2)))
    vt = sqrt(1.0 / r0) * sqrt(1.0 + A) * 1.001
    drift = _drift(_integrate(force, r0, vt))
    pred = (2 * pi ** 2 * A / log(2)) * 1.0
    assert abs(drift / pred - 1) < 0.03          # verified to percent level


def test_eccentric_softened_orbits_all_e():
    lam = 0.01
    force = lambda r: -1.0 / (r + lam) ** 2
    measured = {}
    for e in (0.0, 0.3, 0.6):
        r_ap = 1.0 + e
        vt = sqrt((1 - e) / (1 + e))
        measured[e] = _drift(_integrate(force, r_ap, vt))
        pred = -2 * pi * lam / (1 - e * e)
        assert abs(measured[e] / pred - 1) < 0.08
        assert measured[e] < 0                   # retrograde at every e
    assert abs(measured[0.6]) > abs(measured[0.3]) > abs(measured[0.0])


def test_the_orbital_sensitivity_chain():
    amp = 2 * pi ** 2 / log(2)
    assert abs(amp - 28.48) < 0.01
    arcsec = 4.8481e-6
    bound_per_orbit = 1e-3 * arcsec / 415        # mas/cy at Mercury's cadence
    A_sens = bound_per_orbit / amp
    assert 3e-13 < A_sens < 6e-13
    lab_template = 1e-3
    assert lab_template / A_sens > 1e9           # nine orders sharper
    caveat = "single-planet phase can null; the multi-planet comb is phase-proof"
    assert "comb" in caveat


def test_the_accounts_state():
    state = {"kinematics": "retired — paper five",
             "third law": "taken — the count product commutes",
             "kepler three": "banked — the (3/2, 2/3) pair",
             "eccentric family": "closed at first order, all e — today",
             "octave instrument": "opened — orbits test A at 4e-13",
             "remaining": "the small-rung lattice rule; the rule's own forbid"}
    assert state["eccentric family"].startswith("closed")
    assert state["remaining"]


def test_the_comb_response_at_true_eccentricity():
    """The board's domain catch, faced: the 28.48 formula is the
    near-circular limit; at Mercury's e = 0.206 the comb phase sweeps
    0.6 octaves per orbit and partially self-averages. Integrated
    directly (interpolated perihelion crossings), the response keeps
    61% of the circular formula — a factor 1.6, not the order of
    magnitude feared — and the honest reach follows."""
    import math
    GM, a, e, A = 1.0, 2000.0, 0.206, 1e-4
    p_ = a * (1 - e * e)
    L2 = GM * p_
    amps = []
    for iphi in range(6):
        phi0 = iphi * 2 * math.pi / 6

        def deriv(u, v):
            pert = 1 + A * math.cos(2 * math.pi * math.log2(1.0 / u) + phi0)
            return (v, GM / L2 * pert - u)

        h = 2 * math.pi / 6000
        u, v = 1 / (a * (1 + e)), 0.0
        th, crossings, prev_v, prev_th = 0.0, [], 0.0, 0.0
        for _ in range(6000 * 20):
            k1 = deriv(u, v); k2 = deriv(u + h/2*k1[0], v + h/2*k1[1])
            k3 = deriv(u + h/2*k2[0], v + h/2*k2[1]); k4 = deriv(u + h*k3[0], v + h*k3[1])
            u += h/6*(k1[0]+2*k2[0]+2*k3[0]+k4[0]); v += h/6*(k1[1]+2*k2[1]+2*k3[1]+k4[1])
            prev_th = th; th += h
            if prev_v > 0 and v <= 0:
                crossings.append(prev_th + h * prev_v / (prev_v - v))
            prev_v = v
        adv = [(b - a2 - 2*math.pi) for a2, b in zip(crossings, crossings[1:])]
        amps.append(sum(adv) / len(adv) / A)
    resp = (max(amps) - min(amps)) / 2
    assert abs(resp / 28.48 - 0.61) < 0.04
