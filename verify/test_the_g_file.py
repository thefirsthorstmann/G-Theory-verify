"""test_the_g_file.py — BIG G, FACED (2026-08-16). the author: "there is some
things we can do with big G." The wheel states a value — αG(e) =
5/(2¹⁵¹−1), G = 6.67359015(4)e−11 — and this battery arms it against the
metrology rather than beside it. Data quoted exactly as printed at
collection time: the NSR precision-G review table (PMC8290936) and the
2026 Metrologia redetermination with the BIPM balance rebuilt at NIST
(10.1088/1681-7575/ae570f). Four theorems ride on top: the ensemble is
not one measurement about any center; the octave comb cannot be the
discordance's cause (eight to nine orders short); no phase hides the
comb from the classical planets (Mercury–Jupiter quadrature, floor
0.92); and a measurement spanning exactly one octave of separation
blinds itself (the suppression factor's zero).
"""

import math

HBAR, C, ME = 1.054571817e-34, 299792458.0, 9.1093837015e-31
G_WHEEL = 5 / (2 ** 151 - 1) * HBAR * C / ME ** 2
CODATA18 = 6.67430e-11

# (label, value, sigma) in units of 1e-11, as printed in the sources
EXPERIMENTS = [
    ("Luther-Towler-82", 6.67259, 0.00043),
    ("UWash-00", 6.674255, 0.000092),
    ("BIPM-01", 6.67559, 0.00027),
    ("UWup-02", 6.67422, 0.00098),
    ("MSL-03", 6.67387, 0.00027),
    ("HUST-05", 6.67222, 0.00087),
    ("UZur-06", 6.67425, 0.00012),
    ("HUST-09", 6.67349, 0.00018),
    ("JILA-10", 6.67260, 0.00025),
    ("BIPM-14", 6.67554, 0.00016),
    ("LENS-14", 6.67191, 0.00099),
    ("UCI-14", 6.67435, 0.00013),
    ("HUST-18-ToS", 6.674184, 0.000078),
    ("HUST-18-AAF", 6.674484, 0.000078),
    ("BIPM-NIST-26", 6.67387, 0.00038),
]

AU = {"Mercury": 0.387, "Venus": 0.723, "Earth": 1.0,
      "Mars": 1.524, "Jupiter": 5.203, "Saturn": 9.537}


def _chi2(center):
    return sum(((v - center) / s) ** 2 for _, v, s in EXPERIMENTS)


def test_the_wheel_value_recomputes_from_scratch():
    """5/(2^151−1) · ħc/m_e² gives the printed digits, 106.4 ppm below
    the CODATA-2018 center."""
    assert abs(G_WHEEL - 6.6735902e-11) < 5e-18
    ppm = (CODATA18 - G_WHEEL) / CODATA18 * 1e6
    assert abs(ppm - 106.4) < 0.1


def test_the_ensemble_is_not_one_measurement():
    """Fifteen determinations, chi2 = 189 about their own weighted mean
    for 14 dof — no constant fits the data at stated uncertainties. The
    discordance is nonstatistical whoever is right about the center."""
    wmean = (sum(v / s ** 2 for _, v, s in EXPERIMENTS)
             / sum(1 / s ** 2 for _, v, s in EXPERIMENTS))
    assert abs(_chi2(wmean) - 189) < 2
    assert _chi2(wmean) / (len(EXPERIMENTS) - 1) > 10   # Birge-squared >> 1
    span = (max(v for _, v, _ in EXPERIMENTS)
            - min(v for _, v, _ in EXPERIMENTS)) / 6.674 * 1e6
    assert abs(span - 551) < 2                          # ppm peak to peak


def test_the_wheel_sits_inside_the_spread_not_the_cluster():
    """The honesty pin, both directions at once: the wheel value lies
    inside the experimental spread, six of fifteen agree within two of
    their own sigma, the newest within one — AND the ensemble does not
    favor it: chi2 about the wheel (538) exceeds chi2 about the weighted
    mean (189); the precision cluster sits high. The claim rests on
    convergence, not on the present ensemble."""
    gw = G_WHEEL * 1e11
    vals = [v for _, v, _ in EXPERIMENTS]
    assert min(vals) < gw < max(vals)
    inside = [n for n, v, s in EXPERIMENTS if abs(v - gw) / s < 2]
    assert inside == ["UWup-02", "MSL-03", "HUST-05", "HUST-09",
                      "LENS-14", "BIPM-NIST-26"]
    newest = dict((n, (v, s)) for n, v, s in EXPERIMENTS)["BIPM-NIST-26"]
    assert abs(newest[0] - gw) / newest[1] < 1
    assert _chi2(gw) > _chi2(6.674294)                  # not favored — said plainly


def test_the_comb_cannot_cause_the_discordance():
    """The incompatibility theorem: one amplitude at every scale, the
    ephemeris window reaches A ~ 2.8e-12 marginalized over phase, and
    spanning the 551-ppm discordance needs A >= 2.8e-4 — eight orders. The
    template therefore PREDICTS the discordance resolves to systematics;
    an octave-periodic G(separation) at the discordance scale would
    refute the operation movement outright."""
    span = (6.67559 - 6.67191) / 6.674
    a_needed = span / 2
    a_marginalized = 2.8e-12                 # worst-phase, true-eccentricity
    orders = math.log10(a_needed / a_marginalized)
    assert 7.5 < orders < 8.5
    assert abs(orders - 8.0) < 0.1


def test_no_phase_hides_the_comb_from_the_planets():
    """The quadrature theorem: |sin| has period one half in log2 r, and
    Mercury (0.130) and Jupiter (0.379) sit 0.249 apart there — a
    quarter-period, quadrature — so whatever phase nature picks, the
    best-placed classical planet keeps at least 92% of the full
    precession amplitude. 'Phase-proof' is a number, not a hope."""
    m = math.log2(AU["Mercury"]) % 0.5
    j = math.log2(AU["Jupiter"]) % 0.5
    assert abs(abs(j - m) - 0.25) < 0.002
    floor = min(
        max(abs(math.sin(2 * math.pi * math.log2(r) + phi)) for r in AU.values())
        for phi in [k * 2 * math.pi / 20000 for k in range(20000)])
    assert floor > 0.92


def test_the_suppression_factor_and_the_octave_blind_spot():
    """A measurement integrating uniformly over delta octaves of
    separation keeps sin(pi·delta)/(pi·delta) of the comb amplitude:
    closed form equals direct integration; a half-octave span keeps
    ~64%, a factor-1.5 span keeps ~52% — and a span of exactly one
    octave keeps zero. Design rule: an experiment averaging over one
    full octave cannot see the comb at all."""
    for delta in (0.25, 0.5, math.log2(1.5), 0.999):
        closed = math.sin(math.pi * delta) / (math.pi * delta)
        n = 200000
        num = sum(math.cos(2 * math.pi * (k / n * delta - delta / 2))
                  for k in range(n)) / n
        assert abs(closed - num) < 1e-4, delta
    assert abs(math.sin(math.pi * math.log2(1.5)) / (math.pi * math.log2(1.5))
               - 0.525) < 0.001
    assert abs(math.sin(math.pi * 1.0) / math.pi) < 1e-12


def _fit_comb(data):
    """Linear least squares for G_i = G0 + a·cos(2πx_i) + b·sin(2πx_i);
    returns (G0, A, phi). Exact normal equations, no iteration."""
    rows = [(1.0, math.cos(2 * math.pi * x), math.sin(2 * math.pi * x))
            for x, _, _ in data]
    y = [g for _, g, _ in data]
    w = [1 / s ** 2 for _, _, s in data]
    ata = [[sum(wk * r[i] * r[j] for wk, r in zip(w, rows)) for j in range(3)]
           for i in range(3)]
    atb = [sum(wk * r[i] * yk for wk, r, yk in zip(w, rows, y)) for i in range(3)]
    # 3x3 solve by elimination
    m = [row[:] + [b] for row, b in zip(ata, atb)]
    for c in range(3):
        p = max(range(c, 3), key=lambda r: abs(m[r][c]))
        m[c], m[p] = m[p], m[c]
        for r in range(3):
            if r != c:
                f = m[r][c] / m[c][c]
                m[r] = [a - f * b for a, b in zip(m[r], m[c])]
    g0, a, b = (m[i][3] / m[i][i] for i in range(3))
    return g0, math.hypot(a, b) / g0, math.atan2(-b, a)


def test_the_fit_engine_recovers_an_injected_comb():
    """The instrument for the day the working separations are collected:
    inject A = 8e-5 at phase 1.2 into twelve synthetic experiments with
    15-ppm noise; the linear engine recovers amplitude and phase. Under
    a null injection the fitted amplitude stays at the noise floor —
    the engine does not manufacture a comb."""
    import random
    rng = random.Random(142857)
    xs = [rng.uniform(-1, 1) for _ in range(12)]
    g_true, a_true, phi_true = 6.674e-11, 8e-5, 1.2
    data = [(x, g_true * (1 + a_true * math.cos(2 * math.pi * x + phi_true))
             + rng.gauss(0, 15e-6 * g_true), 15e-6 * g_true) for x in xs]
    g0, a, phi = _fit_comb(data)
    assert abs(a - a_true) / a_true < 0.25
    assert abs((phi - phi_true + math.pi) % (2 * math.pi) - math.pi) < 0.3
    null = [(x, g_true + rng.gauss(0, 15e-6 * g_true), 15e-6 * g_true)
            for x in xs]
    _, a0, _ = _fit_comb(null)
    assert a0 < 2.5e-5                                  # noise-floor bias only


def test_the_marginalized_bound_is_the_instruments_number():
    """The honest instrument number, sensitivity-weighted: per-planet
    reach = bound/(28.48 · suppression(e) · N_orbits · |sin phase|),
    suppression integrated at true eccentricity (Mercury 0.613). At the
    worst phase Mercury, Venus, and Earth jointly hold ~2.8e-12; the
    lucky-phase reach is ~6.7e-13. The 0.92 geometry floor stays true as
    geometry; this is the number an ephemeris fit would quote."""
    mas = math.pi / 180 / 3600 / 1000
    P = {"Mercury": (0.387, 415.2, 0.613, 1.0),
         "Venus":   (0.723, 162.6, 0.999, 1.0),
         "Earth":   (1.000, 100.0, 0.992, 1.0),
         "Mars":    (1.524,  53.2, 0.914, 1.0),
         "Jupiter": (5.203,  8.43, 0.97, 10.0),
         "Saturn":  (9.537,  3.39, 0.96, 10.0)}

    def bound_at(phi):
        best = 1e9
        for a, N, sup, B in P.values():
            sin = abs(math.sin(2 * math.pi * math.log2(a) + phi))
            if sin > 1e-9:
                best = min(best, B * mas / (28.48 * sup * N * sin))
        return best

    grid = [k * 2 * math.pi / 4000 for k in range(4000)]
    worst = max(bound_at(phi) for phi in grid)
    lucky = min(bound_at(phi) for phi in grid)
    assert abs(worst - 2.8e-12) < 0.2e-12
    assert abs(lucky - 6.7e-13) < 0.5e-13
