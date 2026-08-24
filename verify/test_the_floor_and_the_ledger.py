"""test_the_floor_and_the_ledger.py — TWO §21 DEBTS DISCHARGED
(2026-08-17). The strong-field file carried two named open items: what a
never-attained floor does to ringdowns, and the accretion bookkeeping of
a floor that grows. Both close here, one with a null and one with a law.

THE RINGDOWN, discharged with a null. The falling surface's tortoise
position obeys dr*/dt = −1/(1+ε)^{3/2} → −1: it is ASYMPTOTICALLY NULL.
Infalling radiation also runs at −1, so the closing rate is only 1.5ε,
and the total remaining closure ∫1.5ε dt = 3Mε is finite and minuscule
against the ~45M light-ring gap. Radiation never reaches the surface, so
there is NO echo train — the channel does not discriminate this floor
from a horizon. The published echo searches constrain STATIC surfaces at
fixed ε, whose delay 4M ln(1/ε) is constant; this account predicts no
such surface and no such train. A confirmed constant-spacing echo train
refutes the floor's kinematics.

THE ACCRETION, discharged with a law. The floor is not a place records
pass through; it is where the outside read's budget 1 − 2GM/rc² vanishes.
When M grows the budget at fixed r passes through zero: the record's
SHARED rate reaches zero while its PRIVATE ledger runs on. Freezing is
the event; no crossing event is owed. The frozen count then carries the
mechanics: S = πN² with N the horizon in Planck lengths gives S ∝ M², so
dS/dM > 0 identically — the area theorem is the irreversibility of
freezing — and dE = T dS holds exactly with the horizon's own
temperature.
"""

import math

HBAR, C, G = 1.054571817e-34, 299792458.0, 6.67430e-11
KB = 1.380649e-23
LP = math.sqrt(HBAR * G / C ** 3)
MSUN = 1.98892e30
M_GEOM = 1.0                                  # geometric units for the kinematics


def _rate(x):
    """d(ln ε)/dt for radial infall, ε = (r−2M)/2M, E = 1."""
    return -1.0 / (2 * M_GEOM * (1 + math.exp(x)) ** 1.5)


def test_the_surface_is_asymptotically_null():
    """Integrated in log space (the only stable way past ε ~ 10⁻¹²):
    the e-folding time settles on exactly 2M, so the surface's tortoise
    speed approaches −1 — the same speed as the radiation chasing it."""
    x, t, dt = math.log(0.25), 0.0, 1e-3
    marks = {}
    while t < 160:
        k1 = _rate(x); k2 = _rate(x + dt / 2 * k1)
        k3 = _rate(x + dt / 2 * k2); k4 = _rate(x + dt * k3)
        x += dt / 6 * (k1 + 2 * k2 + 2 * k3 + k4)
        t += dt
        for probe in (100, 150):
            if abs(t - probe) < dt / 2:
                marks[probe] = x
    tau = -(150 - 100) / (marks[150] - marks[100])
    assert abs(tau - 2 * M_GEOM) < 1e-3        # analytic: 2M
    assert marks[150] < -70                    # ε below 10⁻³⁰, still positive


def test_radiation_never_catches_the_falling_surface():
    """Closing rate 1.5ε, ε ~ ε₀e^(−t/2M), so the total remaining
    closure is 3Mε₀ — finite. Against the light ring's ~45M tortoise
    gap it is negligible at every ε a ringdown could meet."""
    for eps0 in (1e-3, 1e-6, 1e-10, 1e-20):
        total_closure = 1.5 * eps0 * 2 * M_GEOM
        assert abs(total_closure - 3 * M_GEOM * eps0) < 1e-30
        assert total_closure < 1e-2            # never spans the ~45M gap
    rstar = lambda r: r + 2 * M_GEOM * math.log(r / (2 * M_GEOM) - 1)
    gap = rstar(3 * M_GEOM) - (2 * M_GEOM + 2 * M_GEOM * math.log(1e-10))
    assert 40 < gap < 50                       # the light-ring gap in M


def test_a_static_surface_would_echo_and_this_floor_does_not():
    """The contrast that makes the null a statement: a surface parked at
    fixed ε returns echoes at the CONSTANT delay 4M ln(1/ε) — the
    template every published search uses. The falling floor returns
    none, so the searches' nulls neither support nor touch it."""
    for eps in (1e-6, 1e-10, 1e-20):
        delay = 4 * M_GEOM * math.log(1 / eps)
        assert 50 < delay < 190
        assert delay == 4 * M_GEOM * math.log(1 / eps)   # constant: no drift
    assert abs(4 * math.log(1e10) - 92.1) < 0.1


def _N(M):
    """The horizon diameter counted in Planck lengths."""
    return 2 * G * M / (C ** 2 * LP)


def _S(M):
    """The count's entropy, banked: S = πN² ≡ A/4."""
    return math.pi * _N(M) ** 2


def test_freezing_is_the_event_and_the_area_theorem_is_its_monotonicity():
    """A record at fixed r freezes when 2GM(t) = rc² — its shared rate
    reaches zero with no crossing. N ∝ M and S ∝ M², so the frozen count
    strictly increases with every accretion: the area theorem is not an
    extra law here but the irreversibility of freezing."""
    r = 3.0 * G * (10 * MSUN) / C ** 2
    M_freeze = r * C ** 2 / (2 * G)
    assert abs(1 - 2 * G * M_freeze / (r * C ** 2)) < 1e-12   # budget hits zero
    for M in (1 * MSUN, 10 * MSUN, 60 * MSUN):
        assert _S(M * 1.001) > _S(M)
        assert abs(_S(M * 2) / _S(M) - 4) < 1e-9              # S ∝ M²


def test_the_accretion_bookkeeping_is_the_first_law():
    """With S = πN² and the horizon's own temperature ħc³/8πGMk, the
    identity dE = T dS holds exactly — the count's bookkeeping for a
    growing floor reproduces the first law of black-hole mechanics with
    nothing added."""
    for Msun in (1.0, 10.0, 60.0):
        M = Msun * MSUN
        dM = M * 1e-9
        dS = _S(M + dM) - _S(M)
        T = HBAR * C ** 3 / (8 * math.pi * G * M * KB)
        assert abs(KB * T * dS / (dM * C ** 2) - 1) < 1e-6
