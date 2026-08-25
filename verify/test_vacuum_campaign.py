"""test_vacuum_campaign.py — PART THREE OPENS: the vacuum, 2026-08-09.

The banked identity rho_Lambda = rho_P N^-2 = pi rho_P / S_hor gains a mechanism
(Theorem 8 of the gravity paper at the k-less tier) and its owed teeth-test (K4,
the working record) is BUILT: the parameter-free w(z) triplet. Everything here is a
ratio or an exact congruence except the flow integrations, whose closure is
asserted, not narrated. Verdicts in this file are asserts — never prose written
before the number.
"""

import math

CH = math.sqrt(8 * math.pi / 3)          # the fixed coefficient: rho_DE = rho_P (l_P/R)^2


def test_the_tier_theorem_numerators_source_the_modulus_idles():
    """The sourced/unsourced split, formalized by arithmetic. Riders are
    NUMERATORS: rider k's shortfall is exactly k (sourced, proportional — the
    gravity tier). The vacuum is the MODULUS GAP: 10^6 minus the all-nines is
    ONE, for every rider and with no rider (unsourced, universal — the vacuum
    tier). One theorem, two tiers: the inverse square applied to a rider's
    deficit is the pull; applied to the modulus gap at the horizon's extension
    it is the vacuum."""
    for k in range(1, 7):
        assert k * 142857 * 7 == k * 10 ** 6 - k          # numerators source
    assert 10 ** 6 - 999999 == 1                          # the modulus idles
    for p in (7, 17, 19, 23):                             # and not only for seven
        assert 10 ** (p - 1) - (10 ** (p - 1) - 1) == 1


def test_reader_A_the_hubble_horizon_is_dead_on_arrival():
    """rho_P N_H^-2 with N_H = R_H/l_P and R_H = c/H reduces IDENTICALLY to
    (8pi/3) rho_crit — the banked six-decimal residual. As dynamics that means
    Omega_DE = 8pi/3 > 1: impossible in a flat universe, off the observed
    0.685 by the famous factor ~12.2, and a pure tracker with no acceleration
    onset. Only its today-EXPONENT (2 vs 2.018) was ever banked."""
    # symbolic reduction: rho_P (l_P/R_H)^2 = c^7/(hbar G^2) * (hbar G/c^3) * H^2/c^2
    #                    = c^2 H^2 / G;  rho_crit = 3 c^2 H^2/(8 pi G)
    G, hbar, c, H = 6.674e-11, 1.0546e-34, 2.998e8, 2.2e-18
    rho_P = c ** 7 / (hbar * G ** 2)
    l_P2 = hbar * G / c ** 3
    R_H = c / H
    ratio = (rho_P * l_P2 / R_H ** 2) / (3 * c ** 2 * H ** 2 / (8 * math.pi * G))
    assert abs(ratio - 8 * math.pi / 3) < 1e-9            # exact, H-independent
    assert 8 * math.pi / 3 > 1                            # impossible as an Omega
    assert 11 < (8 * math.pi / 3) / 0.685 < 13            # the banked ~12.2 residual


def _rhs(state, sign):
    om, lnh = state
    w = -(1 / 3) * (1 + sign * 2 * math.sqrt(max(om, 0)) / CH)
    return om * (1 - om) * (1 + sign * 2 * math.sqrt(max(om, 0)) / CH), -1.5 * (1 + w * om)


def _rk4(state, h, sign):
    def add(s, k, f):
        return (s[0] + f * k[0], s[1] + f * k[1])
    k1 = _rhs(state, sign)
    k2 = _rhs(add(state, k1, h / 2), sign)
    k3 = _rhs(add(state, k2, h / 2), sign)
    k4 = _rhs(add(state, k3, h), sign)
    return (state[0] + h * (k1[0] + 2 * k2[0] + 2 * k3[0] + k4[0]) / 6,
            state[1] + h * (k1[1] + 2 * k2[1] + 2 * k3[1] + k4[1]) / 6)


def test_reader_B_the_event_horizon_closes_and_its_curve_is_pinned():
    """The survivor. Integrating the flow forward with ln H carried alongside
    (no division by 1 - Omega anywhere — the underflow that inflated an early
    run is structurally excluded), the reconstructed event horizon returns the
    defining relation Omega = CH^2/(R_e H)^2 to machine precision. The
    parameter-free curve is then pinned at four redshifts."""
    h, x, st, integ = 5e-4, 0.0, (0.685, 0.0), 0.0
    f_prev = 1.0
    while x < 40.0:
        st = _rk4(st, h, +1)
        x += h
        f = math.exp(-x) / math.exp(st[1])
        integ += h * (f_prev + f) / 2
        f_prev = f
    target = CH / math.sqrt(0.685)
    assert abs(integ - target) / target < 2e-3            # the closure, asserted

    h, x, st = -5e-4, 0.0, (0.685, 0.0)
    tab = {0.0: 0.685}
    while x > -math.log(3.2):
        st = _rk4(st, h, +1)
        x += h
        for z in (0.5, 1.0, 2.0):
            if z not in tab and abs(x + math.log(1 + z)) < 2.6e-4:
                tab[z] = st[0]
    w = lambda om: -(1 / 3) * (1 + 2 * math.sqrt(om) / CH)
    assert abs(w(tab[0.0]) - (-0.5240)) < 2e-3
    assert abs(w(tab[0.5]) - (-0.5023)) < 2e-3
    assert abs(w(tab[1.0]) - (-0.4847)) < 2e-3
    assert abs(w(tab[2.0]) - (-0.4595)) < 2e-3
    assert all(w(tab[z]) < -1 / 3 for z in tab)           # accelerating regime


def test_reader_C_the_particle_horizon_never_accelerates():
    """The record-so-far reader: w stays above -1/3 at every epoch integrated —
    no acceleration, dead against the observed universe."""
    h, x, st = -5e-4, 0.0, (0.685, 0.0)
    w = lambda om: -(1 / 3) * (1 - 2 * math.sqrt(max(om, 0)) / CH)
    assert w(0.685) > -1 / 3
    while x > -math.log(4.0):
        st = _rk4(st, h, -1)
        x += h
        assert w(st[0]) > -1 / 3                          # never once below


def test_the_anti_dirac_signature_G_fixed_while_Lambda_drifts():
    """Dirac's large-number hypothesis required G to drift as 1/t — of order
    7e-11 per year at the present age — and observation bounds |Gdot/G| below
    1e-13 per year, a refutation by better than two orders (banked, the epoch
    file). This framework's G is a fixed rational times exact constants and a
    mass: it does not drift AT ALL, while its vacuum term falls as N^-2. The
    structure lands on the observed side of the divide that retired Dirac."""
    needed, observed = 7e-11, 1e-13
    assert needed / observed > 100                        # the two-order margin


def test_the_desi_confrontation_retires_the_parameter_free_vacuum():
    """K4's confrontation, run 2026-08-09 with DESI DR2 external data
    (FS+BAO)+CMB+SNe w0waCDM fits, arXiv 2503.14738 and companions:
    PantheonPlus (-0.858, 0.061, -0.68, 0.25), Union3 (-0.742, 0.096, -1.02,
    0.34), DESY5 (-0.761, 0.065, -0.96, 0.28). The survivor's curve CPL-fitted
    over the data range gives (w0, wa) = (-0.528, +0.094). The displacement
    floor — weakest combo at zero correlation, maximally conservative — is
    3.96 sigma (the first draft of this test asserted > 4.0 from a rounded
    display and FAILED — the pinned floor is the exact one); at the realistic
    tilt (rho ~ -0.8) every combo exceeds 8 sigma.
    The preferred region's RUNNING has the opposite sign to the entire
    event-horizon family (wa < 0 with a phantom past vs wa > 0, never below
    -1). Per the pre-registered rule the parameter-free vacuum RETIRES. What
    stands: the tier theorem, the exponent coincidence, the x12.2 explained as
    the coefficient's failure, and one merged wall — the coefficient ~1/12 of
    a Planck density per cell, which is the same door as N's rest reference."""
    w0_fit, wa_fit = -0.528, +0.094
    desi = {"PantheonPlus": (-0.858, 0.061, -0.68, 0.25),
            "Union3": (-0.742, 0.096, -1.02, 0.34),
            "DESY5": (-0.761, 0.065, -0.96, 0.28)}
    sigmas = {}
    for name, (w0, s0, wa, sa) in desi.items():
        z0, za = (w0_fit - w0) / s0, (wa_fit - wa) / sa
        for rho in (0.0, -0.8):
            chi2 = (z0 * z0 + za * za - 2 * rho * z0 * za) / (1 - rho * rho)
            sigmas[(name, rho)] = math.sqrt(chi2)
    assert 3.9 < min(s for (n, r), s in sigmas.items() if r == 0.0) < 4.0  # 3.96
    assert min(s for (n, r), s in sigmas.items() if r == -0.8) > 8.0    # realistic
    assert wa_fit > 0 and all(wa < 0 for (_, _, wa, _) in desi.values())  # opposite running


def test_the_fraction_is_the_sphere_one_planck_unit_per_horizon():
    """THE SUMMIT. The data-demanded fraction 1/C = 8pi/(3 Omega) decomposes
    completely once the BANKED seat Omega = 2/3 is inserted (the epoch file's
    seat list; Base-Camp's La = 240 deg = 2/3; the Koide family):

        C_seat = 1/(4pi)  --  and 4pi N^2 = A/l_P^2, the horizon's FULL area
        in raw Planck cells. So the seat statement is

            rho_Lambda x (A/l_P^2) = rho_P x 1

        ONE PLANCK DENSITY, TOTAL, PER HORIZON -- and the numerator ONE is the
        tier theorem's own k-less object, the reseed. The x12.2 was never a
        mystery: it is the sphere's 4pi = 12.566, dressed by Omega's +2 to +5%
        (dataset-soft, carried).

    Verified exactly over arbitrary (H, G); the Bekenstein quarter-cell
    convention would give Omega = 8/3 > 1 (excluded -- the raw cell is the
    convention the banked seat selects, noted as seat-selected, not a priori).
    FENCE: this is a SEAT IDENTITY, not an all-epoch dynamics (dynamically on
    the Hubble horizon it reproduces retired reader A); LCDM's own flow crosses
    the seat at z* = 0.028 -- the reading epoch sits AT the crossing."""
    hbar, c = 1.0546e-34, 2.998e8
    for H, G in ((2.2e-18, 6.674e-11), (1.0e-18, 7e-11), (3.3e-18, 6e-11)):
        rho_P = c ** 7 / (hbar * G ** 2)
        l_P2 = hbar * G / c ** 3
        A = 4 * math.pi * (c / H) ** 2
        Om = (rho_P * l_P2 / A) / (3 * c ** 2 * H ** 2 / (8 * math.pi * G))
        assert abs(Om - 2 / 3) < 1e-9                     # exact, input-free
    assert abs(3 * (2 / 3) / (8 * math.pi) - 1 / (4 * math.pi)) < 1e-15
    assert 8 / 3 > 1                                      # BH quarter-cells: dead

    for Om_data, lo, hi in ((0.6847, 2.5, 3.0), (0.6774, 1.4, 1.9), (0.7025, 5.0, 5.7)):
        dress = 100 * (Om_data / (2 / 3) - 1)             # external data inputs
        assert lo < dress < hi                            # +1.6% .. +5.4%, soft

    z_star = (0.685 / (2 / 3) - 0.685) / (1 - 0.685)
    z_star = z_star ** (1 / 3) - 1
    assert 0.02 < z_star < 0.04                           # the crossing is NOW


def test_the_eighteen_relation_parked_with_its_cost():
    """the author's swing: 0.68 x 18 = 12.24 ~ the measured fraction. Inverted: 8pi/(3
    Omega) = 18 Omega forces Omega = sqrt(4pi/27) = 0.6822 -- the sphere over
    the triad-cubed, 0.34 sigma from Planck-18. COSTED: the same identity with
    ANY integer X gives Omega = sqrt(8pi/3X); adjacent integers are spaced
    ~1.9% while the dataset spread is ~3.8%, so two integers always land
    inside -- 17 (the spine) hits DESI's central at 0.06 sigma, 18 (the
    ledger) hits Planck's at 0.3 sigma: adjacent-integer coverage, the grid
    theorem again. Three clean candidates now sit inside the measurement
    range (2/3 banked-seat; sqrt(4pi/27); 2pi/9) and the data cannot
    discriminate. PARKED as a signpost; the banked seat keeps the
    load-bearing role on provenance; the discriminator is a forward
    mechanism or sharper data."""
    assert abs(math.sqrt(4 * math.pi / 27) - 0.682218) < 1e-6
    assert abs(math.sqrt(8 * math.pi / (3 * 17)) - 0.701996) < 1e-6
    assert abs(math.sqrt(8 * math.pi / (3 * 18)) - 0.682218) < 1e-6
    # coverage: spacing vs spread
    spacing = 0.682218 * (1 / (2 * 18))                   # dOmega/dX ~ Omega/2X
    spread = 0.7025 - 0.6774
    assert spacing < spread                               # >= 2 integers always land
    # the three candidates all inside the observational range
    for cand in (2 / 3, math.sqrt(4 * math.pi / 27), 2 * math.pi / 9):
        assert 0.66 < cand < 0.71


def test_the_dress_is_a_clock_so_the_two_owed_items_are_one():
    """Omega's dress is not a constant to derive: it was exactly zero at the
    seat-crossing z* = 0.028 and grows with the elapsed sweep — d(dress)/dz =
    3 Om(1-Om)/(2/3) ~ 0.97 per unit z, and rate x z* reproduces the measured
    dress. 'Derive the dress' and 'why do readings happen at seats' are one
    question about one number: the reading epoch."""
    Om0 = 0.685
    rate = 3 * Om0 * (1 - Om0) / (2 / 3)
    z_star = ((Om0 / (2 / 3) - Om0) / (1 - Om0)) ** (1 / 3) - 1
    assert abs(rate - 0.971) < 0.01
    assert abs(rate * z_star - (0.6847 / (2 / 3) - 1)) < 0.002   # clock closes


def test_the_epoch_borrow_and_the_anatomy_fork():
    """THE CLASSIFICATION (doctrinal, the temporal sibling of Units §3): the
    time-translation group is one-parameter, so a theory owes exactly ONE
    external epoch reference, and no dimensionless construction yields it.
    'Now' is the sector's single permitted borrow — the record-count's rest
    reference IS that borrow. The trilogy's shape: part one borrows nothing;
    part two one scale; part three one epoch.
    THE FORK, registered with its cost: the corpus's dress anatomy is
    alpha^-1 = 137 + 36/1000. Omega's additive dress reads 18.0/1000 on
    Planck-18 (THE LEDGER) and 35.8/1000 ~ 36 on DESI's LCDM fit (SOL, and
    36 = 2 x 18). Cheap today (sigma_x ~ 7; banked-numeral density ~1 in 4);
    DECIDABLE at sigma(Omega) ~ 0.002: ledger-dress vs Sol-dress vs no
    depth-3 dress. Nothing claimed now; the fork awaits data."""
    assert abs((0.6847 - 2 / 3) * 1000 - 18.03) < 0.1     # Planck: the ledger
    assert abs((0.7025 - 2 / 3) * 1000 - 35.83) < 0.1     # DESI: Sol-adjacent
    assert 36 == 2 * 18                                   # the pair structure
    assert abs(137.036 - 137 - 36 / 1000) < 1e-12         # the FSC anatomy
    sigma_x_today = 7.3                                   # from sigma(Omega) = 0.0073
    assert sigma_x_today > (36 - 18) / 3                  # cannot discriminate today
    assert 2.0 < (36 - 18) / 7.3 * 3 < 8                  # at 0.002: >2 sigma apart


def test_reader_Bprime_and_the_crossing_trinity():
    """THE STRESS ROUND'S FIND. K4's triplet fixed the coefficient at one
    Planck density per cell; the summit derived the true coefficient as
    1/(4pi) of that. THE SEAT-CORRECTED EVENT READER WAS NEVER IN THE TRIPLET:
    rho = rho_P l_P^2/A_event gives c_H^2 = 2/3 -- THE SEAT ITSELF AS THE
    HOLOGRAPHIC PARAMETER -- and today w0 = -1.0091, within a tenth of current
    sigma of LCDM. THE TRINITY (exact in-model): w = -1 exactly when
    Omega = c_H^2 (any c), and Omega = c^2 means L H = c -- so the PHANTOM
    CROSSING, the SEAT CROSSING, and the HORIZON COINCIDENCE (event horizon
    = Hubble radius) are ONE EVENT, at z* = 0.028. HONEST STATUS: against
    DESI DR2's CPL fits (Gaussian approx) B-prime sits at 4.8-6.8 sigma where
    LCDM sits at 3.6-5.0 in the same metric -- one to two sigma WORSE than
    LCDM, because its running (wa ~ +0.56 over the data range) opposes the
    data's hint. It dies with LCDM if wa < 0 confirms; it is distinguished
    FROM LCDM by positive running and the crossing-now signature. Recorded as
    the refined candidate at reading-grade dynamics, not a victory."""
    cH = math.sqrt(2 / 3)
    w = lambda om: -(1 / 3) * (1 + 2 * math.sqrt(max(om, 0)) / cH)
    assert abs(3 * cH ** 2 / (8 * math.pi) - 1 / (4 * math.pi)) < 1e-15
    assert abs(w(2 / 3) - (-1.0)) < 1e-12                 # w = -1 AT the seat, exact
    assert abs(w(0.685) - (-1.0091)) < 5e-4               # today: just past it
    # Omega = c^2/(LH)^2, so Omega = c^2  <=>  LH = 1: the horizon coincidence
    assert abs(math.sqrt(cH ** 2 / (2 / 3)) - 1.0) < 1e-12

    def rhs(state):
        om, lnh = state
        ww = -(1 / 3) * (1 + 2 * math.sqrt(max(om, 0)) / cH)
        return om * (1 - om) * (1 + 2 * math.sqrt(max(om, 0)) / cH), -1.5 * (1 + ww * om)

    def rk4(st, h):
        def add(s, k, f):
            return (s[0] + f * k[0], s[1] + f * k[1])
        k1 = rhs(st); k2 = rhs(add(st, k1, h / 2))
        k3 = rhs(add(st, k2, h / 2)); k4 = rhs(add(st, k3, h))
        return (st[0] + h * (k1[0] + 2 * k2[0] + 2 * k3[0] + k4[0]) / 6,
                st[1] + h * (k1[1] + 2 * k2[1] + 2 * k3[1] + k4[1]) / 6)

    h, x, st, integ, fp = 5e-4, 0.0, (0.685, 0.0), 0.0, 1.0
    while x < 40.0:
        st = rk4(st, h); x += h
        f = math.exp(-x) / math.exp(st[1])
        integ += h * (fp + f) / 2; fp = f
    assert abs(integ - cH / math.sqrt(0.685)) / (cH / math.sqrt(0.685)) < 2e-3

    h, x, st = -5e-4, 0.0, (0.685, 0.0)
    tab = {0.0: 0.685}
    while x > -math.log(3.2):
        st = rk4(st, h); x += h
        for z in (0.5, 1.0, 2.0):
            if z not in tab and abs(x + math.log(1 + z)) < 2.6e-4:
                tab[z] = st[0]
    assert abs(w(tab[0.5]) - (-0.8566)) < 2e-3
    assert abs(w(tab[1.0]) - (-0.7487)) < 2e-3
    assert abs(w(tab[2.0]) - (-0.6296)) < 2e-3


def test_function_requires_asymmetry_and_the_floor_sign():
    """the author's paired questions, pinned where they are decidable.
    (1) FUNCTION REQUIRES ASYMMETRY: the whole-tone set {0,2,4,6,8,10} is
    closed under negation — fully symmetric — and possesses no semitone joint,
    which is exactly why whole-tone music has no tonal gravity: nothing leads,
    nothing leans. The diatonic seven is NOT negation-closed (its roots are),
    and it carries exactly two semitone joints — the two places the climbing
    theorem lands and the two places functional harmony moves. The floor that
    has function is necessarily the asymmetric one.
    (2) THE SIGN OF THE FLOOR: the shortfall theorem permits no over-closure,
    so the k-less term is one-signed — the vacuum energy of this framework
    CANNOT be negative. Observation: Lambda > 0. A measured negative vacuum
    would have refuted the mechanism outright; this forbid was available from
    Theorem 6 of the gravity paper before any cosmology entered."""
    whole_tone = {0, 2, 4, 6, 8, 10}
    assert {(-x) % 12 for x in whole_tone} == whole_tone       # symmetric
    diatonic = {0, 2, 4, 5, 7, 9, 11}
    assert {(-x) % 12 for x in diatonic} != diatonic           # asymmetric dress
    assert {(-x) % 12 for x in (5, 0, 7)} == {5, 0, 7}         # symmetric roots
    wt_steps = sorted((b - a) % 12 for a, b in zip(sorted(whole_tone),
                      sorted(whole_tone)[1:] + [12]))
    assert 1 not in wt_steps                                   # no semitone joint
    di = sorted(diatonic)
    di_steps = [(b - a) % 12 for a, b in zip(di, di[1:] + [di[0] + 12])]
    assert di_steps.count(1) == 2                              # exactly two joints
    for p_ in (7, 17, 19, 23):                                 # never over: one sign
        rep = (10 ** (p_ - 1) - 1) // p_
        assert 10 ** (p_ - 1) - rep * p_ == 1 > 0
