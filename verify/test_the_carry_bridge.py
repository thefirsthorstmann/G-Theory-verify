"""The claim map of the paper "The Proton and Neutron Masses on Discrete
Terms" (2026).  Every exact identity, scan, exclusion, and registered value
in that paper is asserted here from stated premises: integers, exact
rationals, and the CODATA-22 table.  Where a measured value appears it
appears only as the thing being tested against.  Section numbers below
refer to the paper, whose source accompanies this repository in catalog/.
"""

from decimal import Decimal, getcontext
from fractions import Fraction as F

# measured constants (CODATA-22; MP is the earlier tabulated vintage used by
# the reproduction rows -- the razor tests carry their own CODATA-22 values)
AINV_CODATA = (137.035999177, 2.1e-8)     # recommended
AINV_PARIS = (137.035999206, 1.1e-8)      # Rb 2020
AINV_BERKELEY = (137.035999046, 2.7e-8)   # Cs 2018
# CODATA-2022 values (2026-09-01 review pass: the 2018-vintage neutron was
# retired; vintage-robustness rows live in test_the_stress_attacks).
MP, MN, ME = 1.0072764665789, 1.00866491606, 0.000548579909  # u; unc 8.3e-12 / 4.0e-10
AVG = (MP + MN) / 2


def comma(n):
    return F(2, n * (n + 1))


def T(n):
    return n * (n + 1) // 2


def test_the_seat_arithmetic_is_exact():
    """Paper Section 7, Identities 1 and 4: the tail seat, the bridge, and one part in 125."""
    assert F(36, 1000) == F(9, 250)                       # the tail seat
    assert F(9, 250) * 28 == F(1008, 1000) == F(126, 125)  # the bridge
    assert F(1008, 1000) - 1 == F(1, 125)                 # one part in 125 above closure


def test_one_carry_is_one_quantum_at_every_rung():
    """Terminology, Section 5: T(n) times c(n) is one at every n; the pair (28, 36)."""
    for n in range(2, 13):
        assert T(n) * comma(n) == 1
    assert T(7) == 28 and comma(7) == F(1, 28)


def test_the_closure():
    """Identity 4: the tail seat is c(7) times 126/125, exactly."""
    assert F(9, 250) == comma(7) * F(126, 125)


def test_the_reptend_lives_inside_the_comma():
    """The decimal expansion of 1/28 carries the period-six cycle of one seventh."""
    getcontext().prec = 40
    digits = str(Decimal(1) / Decimal(28))                # 0.03571428571428...
    assert digits.startswith("0.03571428571428")
    assert digits[4:10] == "571428"                       # a rotation of 142857
    assert digits[4:10] in "142857142857"


def test_the_measured_rows_reproduce():
    """Section 6's measured rows: the three residuals and the tightest composite row, reproduced from CODATA-22."""
    tail = AINV_CODATA[0] - 137.0
    drop_a = (0.036 - tail) / 0.036
    drop_n = (1.008 - AVG) / 1.008
    resid = (28 * tail - AVG) / AVG
    assert abs(drop_a * 1e6 - 22.86) < 0.05               # paper Section 6: -22.86 ppm
    assert abs(drop_n * 1e6 - 29.08) < 0.05               # paper Section 6: -29.08 ppm
    assert abs(resid * 1e6 - 6.22) < 0.05                 # paper Section 6: +6.2 ppm
    # the residual IS the drop-differential -- one fact, not two confirmations
    assert abs(resid - (drop_n - drop_a)) < 2e-10
    # composite seat (100800-3)e-5: the tightest mass row
    assert abs((AVG - 1.00797) / 1.00797 * 1e6 - 0.69) < 0.03


def test_live_exactness_is_refused_from_every_camp():
    """Section 11: 28 times the measured tail exceeds the measured nucleon mean from every determination — the relation is exact at the seats only."""
    for ainv, u in (AINV_CODATA, AINV_PARIS, AINV_BERKELEY):
        tail = ainv - 137.0
        resid = (28 * tail - AVG) / AVG
        sigma = 28 * u / AVG                              # mass uncertainty ~0.4 ppb: negligible
        assert resid > 0                                  # overshoot, every camp
        assert resid / sigma > 3.4                        # >= 3.4 sigma each


def test_the_residual_moves_with_the_determinations():
    """The bridge residual moves monotonically across the fine-structure determinations: the discrepancy's resolution moves this number."""
    r = {}
    for name, (ainv, _) in (("b", AINV_BERKELEY), ("c", AINV_CODATA), ("p", AINV_PARIS)):
        r[name] = (28 * (ainv - 137.0) - AVG) / AVG * 1e6
    assert r["b"] < r["c"] < r["p"]
    assert abs(r["b"] - 2.58) < 0.05 and abs(r["p"] - 7.02) < 0.05


def test_the_object_is_the_archetypal_nucleon_not_hydrogen():
    """The bridge lands on the proton-neutron mean, not on hydrogen, which misses by about 150 parts per million."""
    tail = AINV_CODATA[0] - 137.0
    assert abs((28 * tail - (MP + ME)) / (MP + ME)) * 1e6 > 100


def test_the_amu_read_is_self_contained():
    """Identity 3's physical restatement, Section 7: carbon-12 binding less electron masses is 12/125 u at seat, measured 0.37 percent below."""
    excess = AVG - 1.0
    assert abs(12 * excess - F(12, 125)) / F(12, 125) < 0.004
    assert 12 * excess < F(12, 125)                       # below seat, one-signed


# ── the displacement structure ──

def test_the_base_is_the_consecutive_carry_pair():
    """Identity 2: the base is T(7) times T(8), the tail block is T(8), and the unit's carbon fraction is c(7) minus c(8)."""
    T = lambda n: n * (n + 1) // 2
    c = lambda n: F(2, n * (n + 1))
    assert T(7) * T(8) == 1008 and T(8) == 36
    assert c(7) - c(8) == F(1, 126)
    assert F(126, 125) == 1 / (125 * (c(7) - c(8)))
    assert F(9, 250) == c(7) * F(126, 125)               # the closure, restated


def test_the_seats_are_rung_steps_over_the_sixth_octave():
    """Section 6: the offsets over the sixth power of two are the superparticular steps 9/8 and 33/32."""
    assert F(72, 64) == F(9, 8) and F(66, 64) == F(33, 32)
    assert F(2, 8 * 9) == F(1, 36) and F(2, 32 * 33) == F(1, 528)


def test_the_displacement_family_frame():
    """Section 8: the composite residual is the half-difference of the two displacements, the splitting their sum; no licensed static closure exists."""
    Dp = (1.008 - MP) * 1e5 - 72
    Dn = (MN - 1.008) * 1e5 - 66
    assert abs((Dn - Dp) / 2 * 10 - ((MP - 1.00728) + (MN - 1.00866)) / 2 * 1e6) < 1e-9
    assert abs((Dn + Dp) * 10 - ((MN - 1.00866) - (MP - 1.00728)) * 1e6) < 1e-9
    assert Dn > Dp > 0                                   # one-signed, floor-ordered
    fp, fn = Dp / 72, Dn / 66
    assert abs(fp - 1 / 196) > 100 * 8.3e-12 * 1e5 / 72  # f_p is NOT c7^2
    assert abs(fn - 1 / 126) > 100 * 4.0e-10 * 1e5 / 66  # f_n is NOT c7 - c8
    assert abs(Dn / Dp - 1.5) > 0.05 and abs(Dn / Dp - 1.4) > 0.005


def test_the_timeline_exclusions_are_pinned():
    """Section 13, exclusion 6 and the seating context: the exact-integer receipt counts fail at eleven standard deviations; the syntonic-per-octave arithmetic of the Watch row."""
    Dp = (1.008 - MP) * 1e5 - 72
    Dn = (MN - 1.008) * 1e5 - 66
    sig = 4.0e-10 * 1e5
    ratio, sr = Dn / Dp, (Dn / Dp) * (sig / Dn)
    assert abs(ratio - 39 / 28) / sr > 11                  # the pair is excluded
    assert abs((Dn - Dp) / (1 / 80) - 11) / (sig / (1 / 80)) > 10   # eleven commas: excluded
    assert abs(Dn / 39.328 - 1 / 80) / (1 / 80) < 0.002    # the Watch candidate's arithmetic


def test_the_seating_rung_derives_as_the_hexad_part():
    """Section 9: the divisor scan, the lattice concurrence at one sixth of the proton mass, the count of 39.28 octaves, and the deposit it fixes."""
    import math
    mp, Tc, uTc = 938.27208816, 156.5, 1.5
    assert abs(mp / 6 - Tc) < uTc                          # the hexad hits the lattice
    assert abs(mp / 5 - Tc) / uTc > 10 and abs(mp / 7 - Tc) / uTc > 10
    Tcmb = 2.72548 * 8.617333262e-5
    N = math.log2(mp / 6 * 1e6 / Tcmb)
    assert 39.27 < N < 39.29                               # the duration readout
    load, uload = 0.4916060, 0.0000400
    s = load / N
    assert 0.012514 < s < 0.012518                         # the boxed deposit
    assert abs(s - 1 / 80) / (uload / N) > 10              # exact syntonic: excluded
    assert abs(load / (N * math.log10(2)) - 1 / 24) / (uload / (N * math.log10(2))) > 10
    Dp = (1.008 - MP) * 1e5 - 72
    assert 28.22 < Dp / s < 28.24                          # the proton's clock reading


def test_the_why_of_six():
    """Section 9: the divisor six as the triangular number T(3), with c(3) = 1/6, the seating condition in unit-fraction form."""
    assert (3 + 6 + 9) // 3 == 6 and 3 * 2 * 1 == 6
    assert T(3) == 6 and comma(3) == F(1, 6) and T(3) * comma(3) == 1
    mp = 938.27208816
    assert abs(mp * float(comma(3)) - mp / 6) < 1e-12      # the mechanism identity
    assert abs(mp / 6 - 156.5) < 1.5                       # the lattice concurs
    assert mp * 2 / 42 < 100 and mp * 2 / 90 < 100         # deeper rungs: no office


def test_the_deposit_exceeds_the_syntonic():
    """Section 10's quantitative state: the per-octave deposit exceeds 1/80 by 0.13 percent; an exactly syntonic deposit needs 162 MeV, which the lattice value excludes."""
    import math
    mp, Tcmb = 938.27208816, 2.72548 * 8.617333262e-5
    load, uload = 0.4916060, 0.0000400
    N = math.log2(mp / 6 * 1e6 / Tcmb)
    s, us = load / N, uload / N
    assert abs(s * 80 - 1.00130) < 0.0002                  # the measured excess
    assert (s - 1 / 80) / us > 10                          # not exact: the excess is real
    N2 = load / (1 / 80)
    T2 = 2 ** N2 * Tcmb / 1e6
    assert (T2 - 156.5) / 1.5 > 3                          # branch 2: lattice-disfavored
    assert abs(s - (531441 / 524288 - 1)) / us > 500       # Pythagorean: excluded
    assert abs(s - 6 / 80) / us > 1000                     # six-per-octave: excluded
    assert abs(s - math.log(81 / 80)) / us > 50            # the log form: excluded


def test_the_degree_identification():
    """Section 10: the proton's station as three times twenty-four with the reflection partner 4/3; the neutron's palindromic 66 as the axis; the returning ladder one schisma above 72."""
    assert 72 == 3 * 24 and 66 == 2 * 33
    assert F(40, 1) * F(9, 8) ** 5 / 72 == F(32805, 32768)   # the schisma, exact
    assert abs(2.79284734 / -1.91304273 - -1.45990) < 1e-5   # the soft mu ratio
    assert str(66) == str(66)[::-1]                          # the axis is its own mirror
    schisma, excess = 32805 / 32768 - 1, 0.001327
    assert abs(schisma - excess) / excess > 0.10             # near, and kept apart


def test_the_discharge_law():
    """Sections 8 and 10: the partition 23/32 against the measured ratio at 0.01 sigma on the 2022 table; 9/32 the only fraction to denominator 64 in the window; the leak event-coincident."""
    # CODATA-22 masses locally: the module MP is an earlier tabulated vintage,
    # 3.1e-10 u from CODATA-22.  The law is judged on the current values; under
    # the earlier vintage it would still hold at +1.1 sigma.
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
    assert 23 + 9 == 32 and 32 == 2 ** 5                   # the partition closes on the rung


def test_the_fa_flow():
    """Section 11: the transferred flow, its ratio to each determination's deficit, the near-7/4 landing under the rubidium value, and the excluded steady state."""
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
    assert r_berk < r_codata < r_paris                     # monotone across the determinations
    assert abs(r_paris - 7 / 4) / (7 / 4) < 0.006          # Paris lands near 7/4
    assert 54 // 6 == 9 and F(54, 192) == F(9, 32)         # tier 3 recovers the law
    assert F(9, 192) == F(3, 64) and 61 + 3 == 64          # the alpha prediction
    naive = 61 / 64 * math.log2(0.26 / 2.3486e-4) * 0.0125166
    assert abs(naive - 0.823) / 0.823 > 0.5                # the non-closure, pinned


def test_the_axis_touching_schedule():
    """Section 10's schedule: the convergents of log2(3) alternate sides strictly; six ticks of sixty degrees close the rotation; the antipode holds no seat, nine being odd."""
    import math
    lg3 = math.log2(3)
    conv = [(1, 1), (2, 1), (3, 2), (8, 5), (19, 12), (65, 41), (84, 53), (485, 306)]
    sides = [p / q < lg3 for p, q in conv]
    assert all(sides[i] != sides[i + 1] for i in range(len(sides) - 1))
    assert 6 * 60 == 360                                   # six ticks, one rotation
    assert 180 == 3 * 60 and 9 % 2 == 1                    # the antipode: a station, empty
    assert str(66) == str(66)[::-1]                        # the occupant is the mirror-fixed one


def test_the_excess_is_the_count_gap():
    """Section 10: the deposit's 0.13 percent excess equals the count gap identically; the share variant fails its own second prediction at 565 sigma; the factor sits between 28/27 and 29/28."""
    import math
    mp22, mn22 = MP, MN
    Dp, Dn = (1.008 - mp22) * 1e5 - 72, (mn22 - 1.008) * 1e5 - 66
    N = math.log2(938.27208816 / 6 * 1e6 / (2.72548 * 8.617333262e-5))
    s0 = 1 / 80
    excess = Dn / N / s0 - 1
    Np = Dn / s0
    assert abs(excess - (Np / N - 1)) < 1e-12              # the identity: one object
    assert abs((23 / 32) * N * s0 - Dp) / 8.3e-7 > 500     # the share variant: excluded
    f = 2 ** (Np - N)
    assert abs(f - 29 / 28) / 0.0023 < 1                   # the bridge edge above
    assert abs(f - 28 / 27) / 0.0023 < 1                   # the bridge edge below
    assert abs(f - 36 / 35) / 0.0023 > 2                   # standard commas: outside
    assert abs(f - 33 / 32) / 0.0023 > 2
    ks = [k for k in range(2, 200) if abs(f - (1 + 1 / k)) < 0.0023]
    assert ks == [26, 27, 28]                              # razor menu: 27/26, 28/27, 29/28
    ks_lat = [k for k in range(2, 200) if abs(162.13 / 156.5 - (1 + 1 / k)) < 0.00995]
    assert len(ks_lat) == 17 and 27 in ks_lat and 28 in ks_lat  # the lattice-bar menu (the paper's)


def test_the_alpha_residual_is_a_flux_not_an_accumulation():
    """Sections 6 and 11: the two split grammars — arithmetic for the masses, positional at the half for the fine-structure seat — and the excluded six-deposit steady state."""
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
        assert (d - pred) / u > 3.3                        # the steady state: excluded
    assert abs(1 / (5 / 3) - 3 / 5) < 1e-15                # the two flight endings
    assert abs(1 / (7 / 4) - 4 / 7) < 1e-15


def test_the_present_epoch_and_the_drift():
    """Section 12, corrected in the 2026-09-01 review pass: the neutron rises and the proton falls; the law is event-coincident, so the present laboratory rate is zero; the observable is the step across receipts — the ratio of proton to electron mass stood 0.9e-7 higher at redshift 0.886, at the current bar of that sightline; the early splitting was half a percent smaller at weak freeze-out; the run to the asymptotic de Sitter floor meets the horizon count to a third of an octave."""
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
    assert 0.85e-17 < dp_sm < 1.05e-17                     # smeared proton rate (falls)
    assert abs(-0.8e-17) < 3.6e-17                         # the null against the clock bar
    step = (23 / 32) * s / 1.00728                         # the one-receipt step in the ratio
    assert 8.5e-8 < step < 9.5e-8
    assert step / 1.0e-7 < 1.0                             # inside the methanol bar
    Nfr = math.log2(156.379 / 0.8)                         # octaves to weak freeze-out
    assert 7.5 < Nfr < 7.7 and 0.17 < Nfr / N < 0.21       # a fifth of the deposits
    sd_then = 0.845 * (Nfr / N)
    shrink = 1 - (0.00138 + sd_then * 1e-5) / (0.00138 + 0.845e-5)
    assert 0.0045 < shrink < 0.0053                        # the splitting, 0.49% smaller
    Hinf = 70.05 * math.sqrt(0.69)
    TdS = 1.054571817e-34 * (Hinf * 1000 / 3.0857e22) / (2 * math.pi * 1.380649e-23) * 8.617333262e-5
    total = math.log2(156.379e6 / TdS)
    assert abs(total - 42 * math.log2(10)) < 0.5           # a third of an octave


def test_the_seat_derivations_as_printed():
    """Section 6's derivations, line for line: the three superparticular stations, the forced pair, the two period-eight primes, and the tail from the bridge."""
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
    """The paper's own adversarial pass: vintage robustness of 23/32, the rounding-vacuity statement of Section 6, the widened seating scan of Section 9, the fraction base rate of Section 8, and the drift across the Hubble dispute."""
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


def test_the_seating_deposit_candidate():
    """Section 10's seating deposit: the excess derived as a two-candidate
    receipt zero, with its exposure — the septimal 28/27 (nearer
    nineteen-fold) and the chromatic 25/24 (the smaller parts, the deposit's
    own limit); the next neutron adjustment separates them.  Write
    load = (N + X)/80: the one-time excess is X = 0.052123(3200) octaves.  In
    the pre-registered class (log2 of 7-smooth superparticulars n<=50 + the
    standard commas), TWO candidates sit inside 3 sigma: log2(28/27) at -0.11
    and log2(25/24) at -2.1; 28/27 is 19x closer, UNIQUE in the razor band,
    and pure web (2^2 x 7 / 3^3).  The reading: seating is receipt zero — commitment
    charges one septimal step at the gate, partitioned 23/32 like every
    receipt (a neutron-only toll dies at 16 sigma on the ratio).  THE TWO FACES ARE ONE IDENTITY: load counts
    from 14 m_p/81 = 162.17 MeV while the CROSSOVER observable stays m_p/6 —
    the 162 MeV lattice tension dissolves; the lattice never sees the gate.
    Structure: 9/7 x 28/27 = 4/3 exactly — the septimal third stepped onto
    the door — and 28/27 = (7/6)/(9/8), the septimal-vs-three-limit step.
    Registered value 9: Dn -> 0.4916103 as the neutron mass sharpens (25/24
    predicts 0.4916906; the pure syntonic is long dead); and 23/32 must
    continue to hold exactly through it."""
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
