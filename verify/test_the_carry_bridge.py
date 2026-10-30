"""THE CARRY BRIDGE — the x28 map read as the seed rung's carry ledger.

The banked pieces (each at its own grade, none new here):
  * tail seat 36/1000 = 9/250            (FSC paper, published; 137 is Striking)
  * the x28 bridge  .036 x 28 = 1.008    (dress ledger row, exact seat arithmetic)
  * one carry = T(n) commas at rung n;
    comma(n) = 2/(n(n+1)); T(n)*comma(n) = 1   (forced, banked 2026-08-03)
  * T(7) = 28 survived the trail-of-28 audit (2026-08-04); the PERFECT-NUMBER
    reading of 28 DIED the same day (failed its own 8128 prediction) and this
    battery does not rest on it.

THE CLOSURE (2026-08-31, this battery's reason to exist), exact:

    9/250  =  comma(7) x 126/125  =  (1/28) x (1008/1000)

so at the seats the alpha tail is ONE RUNG-7 COMMA dressed by the septimal
semicomma, the bare nucleon 1.008 = 126/125 is ONE CLOSED CARRY plus that same
semicomma, and the bridge multiplier 28 is T(7), the banked carry price -- a
named forced object rather than a fitted integer.  The AMU then reads as the
free nucleon with exactly one semicomma retired (carbon's per-nucleon dress),
which is the sense of "the AMU is a reading but a forced one" (CC, 2026-08-31).

GRADE, held apart deliberately: the seat arithmetic is exact (asserted below in
rationals).  The IDENTIFICATION -- the nucleon is one carry at the seed rung,
the tail its comma grading -- is a Reading.  Its promotion condition is the
dress ledger's own crown: force the two drops (-22.86 ppm alpha, -29.08 ppm
nucleon) individually.  What the data already rules (asserted below): the
relation is NOT live-exact -- 28 x tail overshoots the measured nucleon from
every alpha camp (>= 3.4 sigma each), so the weld exists at the seats only,
which is the banked seats/dresses split showing up on its own.  The residual
swings +2.6 -> +7.0 ppm across the alpha divergence: a derived differential
would pick a side in the alpha war (the ledger's wake condition, sharpened).
"""

from decimal import Decimal, getcontext
from fractions import Fraction as F

# ── measured constants, CODATA-22 / ledger vintage ─────────────────────────
AINV_CODATA = (137.035999177, 2.1e-8)     # recommended
AINV_PARIS = (137.035999206, 1.1e-8)      # Rb 2020
AINV_BERKELEY = (137.035999046, 2.7e-8)   # Cs 2018
# CODATA-22 throughout (board pass 2026-09-01): the ledger-vintage proton
# (1.00727646627, 37 sigma stale) and the mislabeled 2018 neutron
# (1.00866491595) are retired; the vintage-robustness rows live in
# test_the_stress_attacks.  Uncertainties: 8.3e-12 / 4.0e-10 u.
MP, MN, ME = 1.0072764665789, 1.00866491606, 0.000548579909  # u
AVG = (MP + MN) / 2


def comma(n):
    return F(2, n * (n + 1))


def T(n):
    return n * (n + 1) // 2


def test_the_seat_arithmetic_is_exact():
    assert F(36, 1000) == F(9, 250)                       # the tail seat
    assert F(9, 250) * 28 == F(1008, 1000) == F(126, 125)  # the bridge
    assert F(1008, 1000) - 1 == F(1, 125)                 # one part in 125 above closure


def test_one_carry_is_one_quantum_at_every_rung():
    for n in range(2, 13):
        assert T(n) * comma(n) == 1
    assert T(7) == 28 and comma(7) == F(1, 28)


def test_the_closure():
    """The alpha tail seat is one rung-7 comma dressed by the septimal semicomma."""
    assert F(9, 250) == comma(7) * F(126, 125)


def test_the_reptend_lives_inside_the_comma():
    getcontext().prec = 40
    digits = str(Decimal(1) / Decimal(28))                # 0.03571428571428...
    assert digits.startswith("0.03571428571428")
    assert digits[4:10] == "571428"                       # a rotation of 142857
    assert digits[4:10] in "142857142857"


def test_the_ledger_rows_reproduce():
    tail = AINV_CODATA[0] - 137.0
    drop_a = (0.036 - tail) / 0.036
    drop_n = (1.008 - AVG) / 1.008
    resid = (28 * tail - AVG) / AVG
    assert abs(drop_a * 1e6 - 22.86) < 0.05               # ledger: -22.86 ppm
    assert abs(drop_n * 1e6 - 29.08) < 0.05               # ledger: -29.08 ppm
    assert abs(resid * 1e6 - 6.22) < 0.05                 # ledger: +6.2 ppm
    # the residual IS the drop-differential -- one fact, not two confirmations
    assert abs(resid - (drop_n - drop_a)) < 2e-10
    # composite seat (100800-3)e-5: the tightest mass row
    assert abs((AVG - 1.00797) / 1.00797 * 1e6 - 0.69) < 0.03


def test_live_exactness_is_refused_from_every_camp():
    """28 x tail != measured nucleon: the weld lives at the seats only."""
    for ainv, u in (AINV_CODATA, AINV_PARIS, AINV_BERKELEY):
        tail = ainv - 137.0
        resid = (28 * tail - AVG) / AVG
        sigma = 28 * u / AVG                              # mass uncertainty ~0.4 ppb: negligible
        assert resid > 0                                  # overshoot, every camp
        assert resid / sigma > 3.4                        # >= 3.4 sigma each


def test_the_residual_is_an_alpha_war_weathervane():
    r = {}
    for name, (ainv, _) in (("b", AINV_BERKELEY), ("c", AINV_CODATA), ("p", AINV_PARIS)):
        r[name] = (28 * (ainv - 137.0) - AVG) / AVG * 1e6
    assert r["b"] < r["c"] < r["p"]
    assert abs(r["b"] - 2.58) < 0.05 and abs(r["p"] - 7.02) < 0.05


def test_the_object_is_the_archetypal_nucleon_not_hydrogen():
    """The 2026-07-22 re-grade, reconfirmed cold: p+e misses by ~+150 ppm."""
    tail = AINV_CODATA[0] - 137.0
    assert abs((28 * tail - (MP + ME)) / (MP + ME)) * 1e6 > 100


def test_the_amu_read_is_self_contained():
    """12u = 6mp+6mn+6me - B  =>  B - 6me = 12(avg-1) u: no external binding input.
    Seat: 12/125 = 0.096 u.  Measured sits ~0.37% below -- the -29 ppm restated
    on the offset denominator (the ledger's own two-denominator discipline)."""
    excess = AVG - 1.0
    assert abs(12 * excess - F(12, 125)) / F(12, 125) < 0.004
    assert 12 * excess < F(12, 125)                       # below seat, one-signed


# ── 2026-08-31, the displacement campaign's scaffold ──────────────────────────

def test_the_base_is_the_consecutive_carry_pair():
    """1008 = T(7) x T(8): the base is the product of consecutive carry prices
    at the seed pair.  The alpha tail block 36 is T(8) itself, and the AMU's
    carbon fraction is the gap between the consecutive commas: c7 - c8 = 1/126.
    New readings on banked arithmetic (28x36=1008 was banked 2026-07-23 bare)."""
    T = lambda n: n * (n + 1) // 2
    c = lambda n: F(2, n * (n + 1))
    assert T(7) * T(8) == 1008 and T(8) == 36
    assert c(7) - c(8) == F(1, 126)
    assert F(126, 125) == 1 / (125 * (c(7) - c(8)))
    assert F(9, 250) == c(7) * F(126, 125)               # the closure, restated


def test_the_seats_are_rung_steps_over_the_sixth_octave():
    """72/64 = 9/8, the rung-8 superparticular step, whose comma is 1/T(8);
    66/64 = 33/32, the rung-32 step, whose comma is 1/T(32).  The proton sits
    on the very rung whose carry price is the alpha tail block."""
    assert F(72, 64) == F(9, 8) and F(66, 64) == F(33, 32)
    assert F(2, 8 * 9) == F(1, 36) and F(2, 32 * 33) == F(1, 528)


def test_the_displacement_family_frame():
    """The crown number is the ANTISYMMETRIC half of the two displacements:
    composite dress = (Dn - Dp)/2 x 10, split dress = (Dn + Dp) x 10 (units
    1e-6 u from offset units 1e-5).  Ordering fact: the higher floor displaces
    more (66's floor 33 vs 72's floor 9), sign-consistent with octaves-free/
    floor-paid.  Razor exclusions pinned: no licensed static closure."""
    Dp = (1.008 - MP) * 1e5 - 72
    Dn = (MN - 1.008) * 1e5 - 66
    assert abs((Dn - Dp) / 2 * 10 - ((MP - 1.00728) + (MN - 1.00866)) / 2 * 1e6) < 1e-9
    assert abs((Dn + Dp) * 10 - ((MN - 1.00866) - (MP - 1.00728)) * 1e6) < 1e-9
    assert Dn > Dp > 0                                   # one-signed, floor-ordered
    fp, fn = Dp / 72, Dn / 66
    assert abs(fp - 1 / 196) > 100 * 8.3e-12 * 1e5 / 72  # f_p is NOT c7^2
    assert abs(fn - 1 / 126) > 100 * 4.9e-10 * 1e5 / 66  # f_n is NOT c7 - c8
    assert abs(Dn / Dp - 1.5) > 0.05 and abs(Dn / Dp - 1.4) > 0.005


def test_the_timeline_kills_are_pinned():
    """The cycle-count campaign's first sitting (2026-08-31): razor kills, so
    they are not rediscovered.  The (28,39) common-slip pair dies at 13.8
    sigma; the discharge-as-eleven-commas at ~15 sigma; N = 50 (the banked
    EW->CMB count) yields no licensed comma.  The LIVE candidate is Watch-tier
    only: syntonic comma per octave x 39.328(4) octaves = the neutron load,
    equivalent to a seating temperature of 162 MeV against the banked CMB
    anchor — standing on three named selections (unbanked confinement rung,
    per-octave deposit, the naive unit assumption) and in ~4 sigma tension
    with the lattice crossover 156.5(15) MeV if that is the seating point."""
    Dp = (1.008 - MP) * 1e5 - 72
    Dn = (MN - 1.008) * 1e5 - 66
    sig = 4.9e-10 * 1e5
    ratio, sr = Dn / Dp, (Dn / Dp) * (sig / Dn)
    assert abs(ratio - 39 / 28) / sr > 11                  # the pair is dead
    assert abs((Dn - Dp) / (1 / 80) - 11) / (sig / (1 / 80)) > 10   # eleven commas: dead
    assert abs(Dn / 39.328 - 1 / 80) / (1 / 80) < 0.002    # the Watch candidate's arithmetic


def test_the_seating_rung_derives_as_the_hexad_part():
    """THE SEATING RUNG (2026-09-01): T_seat = m_p/6.  Derived by pre-registered
    divisor scan (2..12, smallest web integers) against the EXTERNAL chiral
    crossover, no peeking at the dress side: only the hexad divisor hits
    (-0.1 sigma vs HotQCD 156.5(15); -2.7 vs Budapest-Wuppertal 158.0(6);
    base rate ~13% at the 1-sigma declaration threshold on the wider bar,
    the board's honest figure -- the realized 0.1-sigma closeness is
    description, not the priced trial).  The runner-up m_p/7 = 134.0 is
    the neutral pion's neighbourhood (+0.7%), a different office, signpost
    only.  License: 6 = the turn's digits, the reptend period, the reseats per
    octave.  Grade: STRIKING (scan stated) + Reading (the why of six is open).
    FORBID: lattice T_c leaving [153, 160] MeV kills the exact form.

    THE CLOCK READING it completes (CC's decimal semantics): the value's turn
    is the IDENTITY (the seat), the wheel is CIRCULATION (free), and the dress
    is HISTORY — the neutron's sixth-decimal content reads the elapsed
    development, N = log2(m_p/(6 T_CMB)) = 39.276 octaves of cooling since
    the hadrons sat down.  The deposit per octave is thereby razor-boxed:
    s = load/N = 0.0125166(10) — and the derivation KILLS the naive syntonic
    branch (1/80 at ~13 sigma) and the per-decade 1/24 (~21 sigma): a real
    derivation may kill its campaign's favourite, and this one did.  CAUTION
    PINNED: at this precision every superparticular (1+1/k) family matches
    SOME k by construction (here k = 765 = 45x17; CC's notes carry 51x15 =
    765) — guaranteed-hit decoration, not evidence.  The nucleons' clock
    readings: the neutron holds all 39.28 deposits, the proton 28.23 — the
    exact-integer pair (28, 39) stays dead at 13.8 sigma."""
    import math
    mp, Tc, uTc = 938.27208816, 156.5, 1.5
    assert abs(mp / 6 - Tc) < uTc                          # the hexad hits the lattice
    for d in (2, 3, 4, 5, 7, 8, 9, 10, 11, 12):            # the full scan, every miss
        assert abs(mp / d - Tc) / uTc > 10
    assert abs(mp / 6 - 158.0) / 0.6 < 3                   # BW: taxed at 2.7, not excluded
    Tcmb = 2.72548 * 8.617333262e-5
    N = math.log2(mp / 6 * 1e6 / Tcmb)
    assert 39.27 < N < 39.29                               # the duration readout
    load, uload = 0.4916060, 0.0000400
    s = load / N
    assert 0.012514 < s < 0.012518                         # the boxed deposit
    assert abs(s - 1 / 80) / (uload / N) > 10              # syntonic: dead at razor
    assert abs(load / (N * math.log10(2)) - 1 / 24) / (uload / (N * math.log10(2))) > 10
    Dp = (1.008 - MP) * 1e5 - 72
    assert 28.22 < Dp / s < 28.24                          # the proton's clock reading


def test_the_why_of_six():
    """THE WHY OF SIX (2026-09-01, CC's triad-average addition closing it).
    The seating divisor wears only exact hats: the triad's average
    (3+6+9)/3 = 6 (its own fixed point), the triad's symmetry 3! = 6, the
    carry price at the tower's base rung T(3) = 6 with comma(3) = 1/6, the
    web's seed product 2x3, and the banked sixes (reptend period, turn
    digits, reseats per octave).  THE FENCE: the perfect-number reading of 6
    died 2026-08-04 (N3, at 8128); nothing here rests on it — the surviving
    frame is T(n)/comma(n).  THE MECHANISM (Reading, one confirmed instance):
    T_seat = m_p x comma(3) — the seat commits when the temperature falls to
    one rung-3 comma of the object's own mass, the minimum legal transfer at
    the tower's base rung; below it the register has no move small enough to
    renegotiate the object, and the rounding is permanent ('matter is
    commitment', Origin III).  The commitment is a carry event; the carry
    channel is the triad; the triad prices it at its root and names the
    divisor by its own average.  Honesty pinned: the triad's deeper comma
    rungs (m_p x c6 = 44.7 MeV, m_p x c9 = 20.9 MeV) hold NO office; the EW
    crossover sits above its masses, so the threshold form has one instance."""
    assert (3 + 6 + 9) // 3 == 6 and 3 * 2 * 1 == 6
    assert T(3) == 6 and comma(3) == F(1, 6) and T(3) * comma(3) == 1
    mp = 938.27208816
    assert abs(mp * float(comma(3)) - mp / 6) < 1e-12      # the mechanism identity
    assert abs(mp / 6 - 156.5) < 1.5                       # the lattice concurs
    assert mp * 2 / 42 < 100 and mp * 2 / 90 < 100         # deeper rungs: no office


def test_the_deposit_is_a_dressed_syntonic():
    """THE DEPOSIT CRACKED (2026-09-01).  The two exact anchors — rung = m_p/6
    and deposit = 1/80 — are incompatible at 13 sigma; one must be dressed.
    Branch 2 (exact syntonic) demands T_seat = 162.1 MeV: +3.8 sigma against
    HotQCD and +6.9 against BW, which both sit at m_p/6.  BRANCH 1 STANDS:
    the deposit is ONE SYNTONIC COMMA PER OCTAVE wearing a +0.133(8)% process
    dress — the program's first process dress, boxed and unclosed (no
    standard comma matches; the superparticular 1/765 is the guaranteed trap,
    refused).  The just-not-tempered rule applies: the residue is kept.

    THE DEPOSIT LAW, from the banked chain's own structure: the reseat chain
    runs six reseats per octave (the six degrees each reseat once, 'the
    previous La becomes the next Sol'), and each reseat costs one syntonic in
    the five-limit.  An object SEATED ON ONE DEGREE is touched once per
    octave — on its own degree's turn.  One object, one degree, one syntonic
    per octave: the per-octave law is occupancy, not choice.  (Which degree
    is the nucleon's, the process dress, and the proton's discharge law
    remain the open set.)  Killed and pinned: Pythagorean-per-octave (903
    sigma), six-syntonic-per-octave (5e4 sigma), ln(81/80) (75 sigma), the
    N-offset repairs (>= 19 sigma)."""
    import math
    mp, Tcmb = 938.27208816, 2.72548 * 8.617333262e-5
    load, uload = 0.4916060, 0.0000400
    N = math.log2(mp / 6 * 1e6 / Tcmb)
    s, us = load / N, uload / N
    assert abs(s * 80 - 1.00130) < 0.0002                  # the dressed syntonic
    assert (s - 1 / 80) / us > 10                          # not exact: the dress is real
    N2 = load / (1 / 80)
    T2 = 2 ** N2 * Tcmb / 1e6
    assert (T2 - 156.5) / 1.5 > 3                          # branch 2: lattice-disfavored
    assert abs(s - (531441 / 524288 - 1)) / us > 500       # Pythagorean: dead
    assert abs(s - 6 / 80) / us > 1000                     # six-per-octave: dead
    assert abs(s - math.log(81 / 80)) / us > 50            # the log form: dead


def test_the_degree_identification():
    """WHICH DEGREE (2026-09-01).  PROTON = SOL, on three banked routes: 72 =
    3 x 24, the third harmonic in the chain's own root-24 frame; the moment
    ratio mu_p/mu_n = -3/2 = Sol (in-model exact, measured -1.4599 soft); and
    the chain's landing — every reseat lands La -> Sol, and the syntonic miss
    is the cost of carrying the lift THROUGH the reseat, materializing where
    the proton sits.  NEUTRON = THE AXIS, the doubled center (banked ladder
    33 -> 66 -> 132: center -> neutron seat -> universe count) — and the
    machine's palindrome fact now DERIVES from geometry: an axis object is
    its own mirror image, so it has no partner, no reversal-play, no
    discharge channel.  Full retention is the axis, not a property.  THE
    DISCHARGE DOOR, by the tonal paper's published Theorem 3 (the reflection
    exchanges Sol and Fa — dominant and subdominant one object in two
    orientations): the proton's mirror-partner is Fa = 4/3 — the machine's
    43 and the interval fork's Paris row.  Whether the discharged deposits
    flow through that channel into the alpha tail is UNBUILT: signpost only.
    NEW EXACT, pinned: the frame-ladder's returning La sits one schisma
    above the proton's seat, 40 x (9/8)^5 / 72 = 32805/32768.  The schisma
    (+0.1129%) is NEAR the process dress (+0.1327%) but 15% low: kept apart.
    The axis object's touching schedule stays open (the cycle-close slip is
    Pythagorean-sized: killed)."""
    assert 72 == 3 * 24 and 66 == 2 * 33
    assert F(40, 1) * F(9, 8) ** 5 / 72 == F(32805, 32768)   # the schisma, exact
    assert abs(2.79284734 / -1.91304273 - -1.45990) < 1e-5   # the soft mu ratio
    assert str(66) == str(66)[::-1]                          # the axis is its own mirror
    schisma, dress = 32805 / 32768 - 1, 0.001327
    assert abs(schisma - dress) / dress > 0.10               # near, and kept apart


def test_the_discharge_law():
    """THE DISCHARGE LAW (2026-09-01), written: at each octave-touch the
    deposit divides on the axis rung's grid — 32, the neutron's own rung —
    with 23/32 SEATING and 9/32 (the seal squared over the axis rung)
    passing the open Sol->Fa mirror.  Between touches the ledger is closed.

    EVIDENCE: Dp/Dn = 0.7187506(585) vs 23/32 = 0.7187500 -> +0.01 sigma
    (the 2022 neutron adjustment, board-corrected 2026-09-01; the mislabeled
    2018 value gave +0.2 -- the correction SHARPENED the law twenty-fold).  THE
    SWEEP: 9/32 is the ONLY reduced fraction with q <= 64 inside 3 sigma of
    the discharge fraction, and it is 3-smooth — unique overall AND unique
    licensed.  THE SHAPE: the linear law (leak once, at deposit time) is
    alive at 0.01 sigma; the compound law (continuous decay) has no licensed
    constant (1/56 at 63 sigma, 1/55 at +7, 1/64 at 4.6%) — the leak is
    EVENT-COINCIDENT: the door is open only during the touch.

    WHAT IT REWRITES: the whole dress family from one clock and one
    partition — neutron = N s, proton = (23/32) N s, crown = (9/64) N s,
    split = (55/32) N s.  FORBIDS: Dp/Dn = 23/32 as a constant of nature
    (the next neutron-mass precision decides; window 6e-5 relative now); no
    epoch dependence; no continuous-decay signature; the discharged flow
    2 d_c = 1.3825e-6 u conserved somewhere (the Fa-destination — if it
    feeds the alpha tail, the program leans Paris — stays unbuilt).
    Decoration echo, unclaimed: 23 = 32 - 9 also factors the seat-depth
    half-sums 828 = 36x23 and 966 = 42x23."""
    import math
    mp22, mn22 = MP, MN
    Dp = (1.008 - mp22) * 1e5 - 72
    Dn = (mn22 - 1.008) * 1e5 - 66
    rho = Dp / Dn
    srho = rho * (4.0e-10 * 1e5 / Dn)
    assert abs(rho - 23 / 32) / srho < 0.05                # the law, at 0.01 sigma
    delta = 1 - rho
    others = [(p, q) for q in range(2, 65) for p in range(1, q)
              if math.gcd(p, q) == 1 and abs(p / q - delta) < 3 * srho]
    assert others == [(9, 32)]                             # unique to q = 64
    assert abs(9 / 32 - 54 / 192) < 1e-15                  # the play over Sol' of 64
    assert 32 == 2 ** 5 and 9 == 3 ** 2                    # the rung, and the seal squared


def test_the_fa_flow():
    """THE FA-DESTINATION BUILT (2026-09-01), three tiers, grades held apart.

    PAPER STANCE (2026-09-01 board): the interval/flow correspondences stay
    INTERNAL -- licensed candidates blanket the war band at sub-bar spacing
    (density pinned in the wheel-pair battery), so the paper presents no
    interval table as evidence and registers no lean.

    TIER 1 (exact): the discharged growth = Dn - Dp = 2 d_c = 1.382639e-6 u
    over the history, (9/32)s per octave.  The SIGN crosses the door
    inverted: Theorem 3's two orientations (press-from-above vs
    settle-from-below) turn Sol-side spillage into Fa-side DEFICIT — which
    is what the alpha tail is.

    TIER 2 (Watch, war-soft): flow/deficit = 1.6800(429) at CODATA.  The
    crowd, performers stated: 5/3 = La (+0.31 sigma, performer 5, the
    least-performer LEAN), 27/16 (-0.17, 27), 42/25 (+0.00, 42).  Relative
    form through the bridge: 0.06000 ~ 3/50.  Per-camp: Paris -> 1.7412 ~
    7/4, the rest couple's own 63/36; Berkeley -> 1.449, no licensed
    station.  A NEW WEATHERVANE — and the SECOND structural Paris-lean:
    under Paris both flow objects go clean (the door 4/3, the ratio 7/4).

    TIER 3 (registered by FORM, not fit): the law generalizes as
    discharge = machine-play/192 (one selection: 192 = 3 x 64, Sol' of the
    sixth octave).  Recovers the proton (54/192 = 9/32), builds in the axis
    (0), and PREDICTS the alpha object discharges 3/64 and retains 61/64 of
    its own deposits.  The alpha clock (seating candidate: recombination,
    ~10.1 octaves) does NOT close naively — 61/64 x 10.1 x s_syntonic =
    0.121e-6 against the measured 0.823e-6 deficit — so the alpha deposit
    currency is its own open object and NO fit is claimed."""
    import math
    mp22, mn22 = MP, MN
    Dp, Dn = (1.008 - mp22) * 1e5 - 72, (mn22 - 1.008) * 1e5 - 66
    flow = (Dn - Dp) * 1e-5
    assert abs(flow * 1e6 - 1.382639) < 1e-4               # tier 1: exact algebra
    r_codata = flow / (0.036 - 0.035999177)
    assert abs(r_codata - 1.6799) < 0.001
    assert abs(r_codata - 5 / 3) / 0.0429 < 1              # La: inside one sigma
    assert abs(r_codata - 42 / 25) / 0.0429 < 0.1          # the crowd is real
    r_paris = flow / (0.036 - 0.035999206)
    r_berk = flow / (0.036 - 0.035999046)
    assert r_berk < r_codata < r_paris                     # the weathervane swings
    assert abs(r_paris - 7 / 4) / (7 / 4) < 0.006          # Paris lands near 7/4
    assert 54 // 6 == 9 and F(54, 192) == F(9, 32)         # tier 3 recovers the law
    assert F(9, 192) == F(3, 64) and 61 + 3 == 64          # the alpha prediction
    naive = 61 / 64 * math.log2(0.26 / 2.3486e-4) * 0.0125166
    assert abs(naive - 0.823) / 0.823 > 0.5                # the non-closure, pinned


def test_the_axis_touching_schedule():
    """THE TOUCHING SCHEDULE (2026-09-01), assembled almost entirely from
    banked parts.  The clock: two hands, one tick = 60 degrees of seat angle,
    six ticks = the rotation = the octave (UPDATE-RULE Sec.1 ◆).  The two
    hands ARE the dominant side and the subdominant side — the banked text
    names them — and the read ALTERNATES BY THEOREM: the convergents of
    log2(3) alternate sides strictly (asserted below on the banked ladder).
    The hands' two meetings per rotation fall on the AXIS (the midpoint
    between Do and Sol that exchanges the two — tonal Theorem 3, published)
    and on the ANTIPODE at 180 degrees, where NO SEAT EXISTS because nine is
    odd (the gravity paper, published).  So exactly one meeting finds an
    occupant: the center's — the neutron — once per octave.  THE SCHEDULE:
    six landings touch the six degree-seats (the proton at Sol's landing,
    the mirror door open, 9/32 leaking); the one occupied meeting touches
    the axis.  And at a meeting BOTH orientations are present — there is no
    elsewhere — so zero discharge derives a SECOND time, independently of
    the palindrome geometry.  Grade: Reading; the two joints that are ours
    (the meeting as the touch-event; the deposit at a meeting = the same s)
    are labeled; everything else cites banked or published lines."""
    import math
    lg3 = math.log2(3)
    conv = [(1, 1), (2, 1), (3, 2), (8, 5), (19, 12), (65, 41), (84, 53), (485, 306)]
    sides = [p / q < lg3 for p, q in conv]
    assert all(sides[i] != sides[i + 1] for i in range(len(sides) - 1))
    assert 6 * 60 == 360                                   # six ticks, one rotation
    assert 180 == 3 * 60 and 9 % 2 == 1                    # the antipode: a station, empty
    assert str(66) == str(66)[::-1]                        # the occupant is the mirror-fixed one


def test_the_process_dress_is_the_fork_gap():
    """THE PROCESS DRESS RESOLVED BY DISSOLUTION (2026-09-01): it is not a new
    object.  s/s0 - 1 = N'/N - 1 identically (N' = load/syntonic): the dress
    is THE FORK'S GAP worn three ways — +0.133(8)% on the deposit, 0.0521
    octaves on the count, the lattice's 3.7-sigma objection to 162 MeV.

    THE KILL THAT PROVED UNIFORMITY: the spill-share candidate (1/216 of the
    proton's spill lands on the axis; predicts the neutron dress as 1/768 at
    +0.3 sigma — beautiful) DIES at 565 sigma on its own second prediction,
    the proton's displacement.  Like 8128.  Since Dp/Dn holds 23/32 at 0.2
    sigma, the dress CANCELS in the ratio: it rides the deposit as delivered,
    identically for both recipients — source/clock-side, never landing-side.

    THE GAP'S LICENSED NAMES: the needed temperature factor 1.03679(230)
    carries THREE superparticulars in its razor 1-sigma band (27/26, 28/27,
    29/28) and
    SEVENTEEN on the lattice bar (k = 22..38, the paper's priced menu);
    straddled inside one sigma by BOTH Catalan-edge superparticulars at the
    bridge — 28/27 (the septimal third-tone, -0.12) and 29/28 (T(7)+1 over
    T(7), +0.46) — and by nothing in the STANDARD comma set (36/35, 33/32,
    26/25 all outside); the superparticular family is the priced menu.  The razor cannot split the pair; the lattice taxes either at
    ~3.6 sigma.  RESOLUTION TRIANGLE: the lattice moves; or the seating sits
    one bridge-edge above the hexad toll for an unwritten mechanism; or the
    dress is genuine process physics.  The lattice's sharpening adjudicates —
    the dress has MERGED INTO the fork's standing forbid."""
    import math
    mp22, mn22 = MP, MN
    Dp, Dn = (1.008 - mp22) * 1e5 - 72, (mn22 - 1.008) * 1e5 - 66
    N = math.log2(938.27208816 / 6 * 1e6 / (2.72548 * 8.617333262e-5))
    s0 = 1 / 80
    dress = Dn / N / s0 - 1
    Np = Dn / s0
    assert abs(dress - (Np / N - 1)) < 1e-12               # the identity: one object
    assert abs((23 / 32) * N * s0 - Dp) / 8.3e-7 > 500     # the spill-share: killed
    f = 2 ** (Np - N)
    assert abs(f - 29 / 28) / 0.0023 < 1                   # the bridge edge above
    assert abs(f - 28 / 27) / 0.0023 < 1                   # the bridge edge below
    assert abs(f - 36 / 35) / 0.0023 > 2                   # standard commas: outside
    assert abs(f - 33 / 32) / 0.0023 > 2
    ks = [k for k in range(2, 200) if abs(f - (1 + 1 / k)) < 0.0023]
    assert ks == [26, 27, 28]                              # razor menu: 27/26, 28/27, 29/28
    ks_lat = [k for k in range(2, 200) if abs(162.13 / 156.5 - (1 + 1 / k)) < 0.00995]
    assert len(ks_lat) == 17 and 27 in ks_lat and 28 in ks_lat  # the lattice-bar menu (the paper's)


def test_the_alpha_is_a_current_not_a_ledger():
    """THE LAST BOX CLOSED BY CATEGORY CORRECTION (2026-09-01).  The alpha
    object has no deposit currency because it is not a ledger: its turn
    splits at the MIDY HALF (137|036, 3|3 — an active reciprocal, the wheel
    mid-turn), where the nucleon's splits base|offset (1008|72, 4|2 — a
    storage address).  The published FSC paper already reads its sub-turn as
    'the borrow of the displacement IN FLIGHT'.  Storage and flight: two
    offices of the sixth decimal.  Tier-3's alpha-clock premise was the
    wrong office — which is why its closure failed, honestly, when tested.

    THE CURRENT MODEL, razor, no free parameter, KILLED and pinned: arrival
    (9/32)s per octave, leak 3/64 on the standing current, steady state =
    (9/32)(64/3)s = SIX DEPOSITS EXACTLY — one rotation's worth in flight,
    0.7510(1)e-6 — excluded by every war camp at >= 3.4 sigma.  The
    noticing (partition x leak-inverse = the tick count) stays beside its
    kill.  THE SURVIVING FORM: the finite flight, d_alpha = flow x tau with
    tau/N = 1/r identically — the borrow in flight for 3/5 of the age
    (La's inverse, the blend) or 4/7 (the seed's fourth, Paris).  The war
    chooses the fraction; both endings are licensed and named."""
    s6 = "137036"
    assert s6[:3] == "137" and s6[3:] == "036"             # the Midy split IS positional
    # the storage split is ARITHMETIC, not positional: the borrow crosses digits
    assert 100728 == 100800 - 72 and 100866 == 100800 + 66
    assert (9 / 32) * (64 / 3) == 6.0                      # the noticing, exact
    import math
    mp22, mn22 = MP, MN
    Dn = (mn22 - 1.008) * 1e5 - 66
    N = math.log2(938.27208816 / 6 * 1e6 / (2.72548 * 8.617333262e-5))
    pred = 6 * (Dn / N) * 10
    for d, u in ((0.954, 0.027), (0.823, 0.021), (0.794, 0.011)):
        assert (d - pred) / u > 3.3                        # the steady state: dead
    assert abs(1 / (5 / 3) - 3 / 5) < 1e-15                # the two flight endings
    assert abs(1 / (7 / 4) - 4 / 7) < 1e-15


def test_the_present_epoch_and_the_drift():
    """The paper's Section 12, board-corrected 2026-09-01 (referee: the SIGN;
    metrologist: event-coincidence, H-infinity floor; statistician's electron
    catastrophe dissolved by the corrected sign — the u-identity asks carbon's
    binding to absorb only ~2e-16 relative/yr).  THE FRAME: drifts in the
    unit's own register.  THE SIGNS: the neutron offset grows up, the proton
    offset grows DOWN — the neutron mass rises, the proton mass FALLS, the
    splitting widens; mu = m_p/m_e steps DOWN.  THE LAW IS EVENT-COINCIDENT:
    between receipts the masses stand still — the laboratory prediction is
    NULL (Lange 2021, -0.8(3.6)e-17/yr, consistent); the smeared rates
    (+1.3e-17 n, -0.9e-17 p) are octave averages, not today's rates.  THE
    OBSERVABLE: one receipt separates z = 0.886 from now, so mu stood
    +0.9e-7 higher there, sign-definite.  THE SIGHTLINE, RE-READ AT THE SOURCES
    ON 2026-10-04 (PKS 1830-211 methanol; delta mu = mu_z - mu_lab): the bar
    this battery first quoted, (0.0+-1.0)e-7, is Bagdonaite et al. 2013; Kanekar
    et al. 2015 set a robust two-sigma limit of 4e-7 and held the earlier
    methanol figures limited by systematics; Muller et al. 2021 give
    (-1.8+-1.2)e-7 and a three-sigma limit of 3.6e-7.  The step lies inside both
    limits and 2.2 sigma above the latest estimate.  BBN: at weak
    freeze-out (7.6 octaves in) the deposits were a fifth of today's, the
    splitting 0.49% smaller, primordial helium shifted UP at tenths of a
    percent — an open account, direction fixed.  THE ALLOTMENT, corrected to
    the ASYMPTOTIC floor H0*sqrt(0.69): 139.2 octaves against 42 decades =
    139.5 — a third of an octave, stated and unclaimed."""
    import math
    N = math.log2(938.27208816 / 6 * 1e6 / (2.72548 * 8.617333262e-5))
    assert 0.27 < N - 39 < 0.29                            # 27.6% through the fortieth
    T39 = 156.379e6 / 2 ** 39
    assert 0.20 < T39 / 2.3486e-4 - 1 < 0.22               # receipt 39 at z = 0.21
    H_yr = 70.05 * 1000 / 3.0857e22 * 3.156e7
    rate = H_yr / math.log(2)
    s = 0.0125166e-5
    dn_sm = s * rate / 1.00866
    dp_sm = (23 / 32) * s * rate / 1.00728
    assert 1.2e-17 < dn_sm < 1.4e-17                       # smeared neutron rate (rises)
    assert 0.85e-17 < dp_sm < 1.05e-17                     # smeared proton rate (FALLS)
    assert abs(-0.8e-17) < 3.6e-17                         # the null vs the lab bar
    step = (23 / 32) * s / 1.00728                         # mu's one-receipt step
    assert 8.5e-8 < step < 9.5e-8
    assert 0.85 < step / 1.0e-7 < 0.95                     # 0.9 sigma on the 2013 figure, (0.0 +- 1.0)e-7
    assert step < 4e-7 and step < 3.6e-7                   # inside the robust limits of 2015 (2 sigma) and 2021 (3 sigma)
    assert 2.2 < (step - (-1.8e-7)) / 1.2e-7 < 2.3         # 2.2 sigma above the 2021 estimate, (-1.8 +- 1.2)e-7
    Nfr = math.log2(156.379 / 0.8)                         # octaves to weak freeze-out
    assert 7.5 < Nfr < 7.7 and 0.17 < Nfr / N < 0.21       # a fifth of the deposits
    sd_now, sd_then = 0.845, 0.845 * (math.log2(156.379 / 0.8) / N)
    shrink = 1 - (0.00138 + sd_then * 1e-5) / (0.00138 + sd_now * 1e-5)
    assert 0.0045 < shrink < 0.0053                        # the splitting, 0.49% smaller
    Hinf = 70.05 * math.sqrt(0.69)
    TdS = 1.054571817e-34 * (Hinf * 1000 / 3.0857e22) / (2 * math.pi * 1.380649e-23) * 8.617333262e-5
    total = math.log2(156.379e6 / TdS)
    assert abs(total - 42 * math.log2(10)) < 0.5           # a third of an octave


def test_the_seat_derivations_as_printed():
    """Section 6 of the paper, pinned line for line (2026-09-01).  THE
    OFFSETS: a six-ladder station above the sixth octave has a superparticular
    step exactly when 6k - 64 divides 64; the three solutions are 66 (33/32),
    72 (9/8), and 96 (3/2); the third is the dominant's own degree, so the
    available pair {66, 72} is forced — consecutive, difference 6, ratio
    12/11 — with the signs forced by the stability of hydrogen.  THE BASE:
    1008 = T(7) x T(8).  THE FINE-STRUCTURE SEAT: the period-eight primes are
    exactly the divisors of 10^4 + 1 = 73 x 137; 73 carries nine cyclic
    classes, 137 seventeen; the tail follows from the bridge with no further
    choice, 1.008/28 = 0.036 = T(8)/1000, so one statement stands free and
    two seats follow."""
    sols = [6 * k for k in range(11, 22) if (6 * k - 64) > 0 and 64 % (6 * k - 64) == 0]
    assert sols == [66, 72, 96]
    assert F(66, 64) == F(33, 32) and F(72, 64) == F(9, 8) and F(96, 64) == F(3, 2)
    assert 72 - 66 == 6 and F(72, 66) == F(12, 11)
    assert 73 * 137 == 10 ** 4 + 1
    for p, classes in ((73, 9), (137, 17)):
        k, x = 1, 10 % p
        while x != 1:
            x = x * 10 % p
            k += 1
        assert k == 8 and (p - 1) // 8 == classes
    assert F(1008, 1000) / 28 == F(9, 250)                 # the tail, forced


def test_the_stress_attacks():
    """The pre-post adversarial pass (2026-09-01), five attacks, pinned.
    (1) VINTAGE: the ratio 23/32 holds across the constants' own revisions —
    and the board's correction of the mislabeled neutron (2018 -> true 2022,
    1.00866491606(40)) SHARPENED it from +0.2 to +0.01 sigma.
    (2) VACUITY: both mass seats ARE the nearest five-decimal roundings, so
    their ppm agreement is automatic and the derivation carries all the
    weight; the alpha residual is 0.0008 of its seat's last digit — a depth
    no rounding provides.  Stated in the paper's Section 6.  (3) LOOK-
    ELSEWHERE: the three numerators span 0.14 sigma = ONE trial (the old x3
    was retracted by the board); the honest base rate is ~13% at the 1-sigma
    declaration threshold, stated in Section 9.  (4) BASE RATE: the q<=64
    window expects ~0.44 fractions, so uniqueness is a fair coin; the content
    is the 0.01-sigma proximity (honest single-trial p ~0.15%), Section 8.
    (5) DRIFT: the smeared scale is robust across the Hubble dispute — and
    the LAW's present-day laboratory rate is zero (event-coincident)."""
    import math
    for mp, mn, umn, lo, hi in ((1.007276466879, 1.00866491588, 4.9e-10, -1.0, 0.0),
                                (1.007276466621, 1.00866491595, 4.9e-10, -0.4, 0.6),
                                (1.0072764665789, 1.00866491595, 4.9e-10, -0.1, 0.4),
                                (1.0072764665789, 1.00866491606, 4.0e-10, -0.1, 0.1)):
        r = ((1.008 - mp) * 1e5 - 72) / ((mn - 1.008) * 1e5 - 66)
        sr = r * (umn * 1e5 / ((mn - 1.008) * 1e5 - 66))
        assert lo < (r - 23 / 32) / sr < hi
    assert round(MP, 5) == 1.00728 and round(MN, 5) == 1.00866
    assert abs(0.823e-6 / 1e-3 - 0.000823) < 1e-9          # the alpha depth: 1/1215
    assert abs(939.565 / 6 - 156.5) < 1.5                  # the neutron co-hit
    dens_win = 3 / math.pi ** 2 * 64 ** 2 * 6 * 5.85e-5
    assert 0.3 < dens_win < 0.6                            # the fair-coin base rate
    for H in (67.4, 73.0):
        rate = H * 1000 / 3.0857e22 * 3.156e7 / math.log(2)
        assert 1.1e-17 < 0.0125166e-5 * rate / 1.00866 < 1.5e-17


def test_the_gate_toll_candidate():
    """THE GATE TOLL (2026-09-02, CC: 'whole hog'): Section 10's deposit excess
    derived as a TWO-CANDIDATE gate, published in v2 with its exposure.
    CC'S LEAN, ON THE RECORD: 25/24 — the least performer, the deposit's own
    five-limit, the superparticular at the root 24, the chromatic semitone
    (6/5 x 25/24 = 5/4: commitment as the Picardy step).  The table's lean:
    28/27 at 19x the closeness.  The measurement decides; both are pinned.  Write
    load = (N + X)/80: the one-time excess is X = 0.052123(3200) octaves.  In
    the pre-registered class (log2 of 7-smooth superparticulars n<=50 + the
    standard commas), TWO candidates sit inside 3 sigma: log2(28/27) at -0.11
    and log2(25/24) at -2.1; 28/27 is 19x closer, UNIQUE in the razor band,
    and pure web (2^2 x 7 / 3^3).  READING: seating is receipt zero — the
    commitment (Origin III: rounding is costly) charges one septimal step at
    the gate, partitioned 23/32 like every receipt (a neutron-only toll dies
    at 16 sigma on the ratio).  THE TWO FACES ARE ONE IDENTITY: load counts
    from 14 m_p/81 = 162.17 MeV while the CROSSOVER observable stays m_p/6 —
    the 162 MeV lattice tension dissolves; the lattice never sees the gate.
    STRUCTURE: 9/7 x 28/27 = 4/3 exactly — the septimal third stepped onto
    the door — and 28/27 = (7/6)/(9/8), the septimal-vs-three-limit step.
    REGISTERED (value 9 of the paper): Dn -> 0.4916103 as m_n precision
    tightens (25/24 predicts 0.4916906; pure syntonic long dead); and 23/32
    must continue to hold exactly through it."""
    import math
    N = math.log2(938.27208816 / 6 * 1e6 / (2.72548 * 8.617333262e-5))
    load, uload = (MN - 1.008) * 1e5 - 66, 4.0e-5
    X, sX = 80 * load - N, 80 * uload
    assert abs(X - math.log2(28 / 27)) / sX < 0.5           # the toll, at -0.11 sigma
    assert 1.5 < abs(X - math.log2(25 / 24)) / sX < 3       # the rival, alive but far
    assert abs(X - math.log2(81 / 80)) / sX > 10            # the syntonic itself: dead
    assert (load - N / 80) / uload > 15                     # no toll: dead
    r_no = (23 / 32) * N / (N + math.log2(28 / 27))
    assert abs(0.7187506 - r_no) / 0.0000585 > 15           # neutron-only toll: dead
    from fractions import Fraction as F
    assert F(9, 7) * F(28, 27) == F(4, 3)                   # the door identity
    assert F(7, 6) / F(9, 8) == F(28, 27)                   # the step's own name
    assert abs(938.27208816 * 14 / 81 - 162.17) < 0.01      # the load origin, closed form


def test_the_crossing_watch():
    """SANDBOX WATCH (2026-09-02, CC's 'what note are we on').  THE CROSSING:
    24 x 2^frac(N) sweeps [24,48) once per octave and is passing the banked
    nucleon drop 29.0761 ppm NOW.  Read as an identity it PREDICTS the CMB
    temperature from the mass table: T = 4 m_p/(2^39 x drop) = 2.72464 K,
    against Fixsen 2.72548(57) — a standing of -1.5 sigma, equivalently a
    crossing 4.4 Myr ahead at today's cooling rate.  THE HONEST FRAME: the
    crossing is CERTAIN once per octave; the content is why-NOW, p ~ 5e-4
    over the ~17 Gyr octave — the dark-energy-coincidence species.  THE
    DECISIVE NEGATIVE (pinned below): the deposition mechanism CANNOT lock
    it — the drop drifts at ~2e-17/yr while the sweep runs at ~2e-9/yr, so
    the identity is a passage, not an equilibrium; any reading must be
    positional (crest-like), never dynamical.  Deciding instrument: a
    microkelvin-class absolute CMB temperature (PIXIE-class); T = 2.72464 K
    confirms the crossing at the razor, anything else retires the watch.
    NOT in any paper; the shelf, if ever, is the Predictions watch list."""
    import math
    N = math.log2(938.27208816 / 6 * 1e6 / (2.72548 * 8.617333262e-5))
    Tpred = 938.27208816e6 * 4 / (2 ** 39 * 29.0761) / 8.617333262e-5
    assert abs(Tpred - 2.72464) < 0.00001                  # the predicted temperature
    standing = (Tpred - 2.72548) / 0.00057
    assert -2.0 < standing < -1.0                          # the current standing
    assert abs(24 * 2 ** (N % 1) - 29.067) < 0.001         # the sweep, today
    sweep = 24 * math.log(2) * 2 ** (N % 1) * 1.03e-10     # per year
    drift = 2e-17                                          # the drop's own rate
    assert sweep / drift > 1e7                             # no dynamical lock: a passage
    assert 2 * 4.4e6 / 1.7e10 < 1e-3                       # the why-now prior
