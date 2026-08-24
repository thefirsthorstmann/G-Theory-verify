"""test_the_yukawa_leg.py — THE YUKAWA LEG: THE POSITION OF THE LEPTON
LADDER IS ONE NUMBER, IT IS OPEN, AND THE PAPER NOW CARRIES IT AS AN OPEN
ACCOUNT WITH THE ROUTE NAMED (2026-08-22).

the author: "lets do the four papers first then go get the Yukawa leg." The leg is
the electroweak-to-electron ratio named in §21.12's three-rulers passage,
which until today said "recorded as a target rather than as a wall" and
named no route.

ROPED UP FIRST, NOT RECONSTRUCTED. The position was worked on 2026-08-19
and the record is decisive: v/m_e = 481839.837 ± 0.124 (0.26 ppm, the bar
inherited from G_F) is no station of the register at fifteen sigma or
better, no pure 2-3-7 word, no wheel form with a small numerator, no
radiative form, no power of alpha, and no integer (working record; pinned in
test_the_yukawa_trail, test_ratio_not_absolute, test_shape_and_position).
The shape of the lepton ladder — the muon ratio and Koide — is complete.
Value-matching sweeps have no evidential power (an internal null-model tool), so no
new sweep is run here: running one would be the sin the record names.

WHAT THIS BATTERY ADDS, all cold:

  1. THE THREE OPEN POSITIONS ARE ONE NUMBER, as arithmetic rather than
     as a phrase. m_e/M_Planck is carried exactly (αG(e) = 5/(2^151 − 1),
     so m_e/M_Planck = √10 · 2^−76) and m_p/m_e is seated, so v/M_Planck
     and m_p/v are both functions of the single unknown v/m_e. One
     derivation closes all three. And because √αG is exact here, the
     account's v/M_Planck is a 0.26-ppm statement where the CODATA route
     through G is an 11-ppm one — forty times sharper, for free.

  2. THE REST-CLOCK READING of the count (§7.1): v/m_e is the number of
     electron ticks per electroweak tick, m_e c²/h against v/h. This is
     what the step the account would need must produce: an operation of
     the register placing one tick rate against the other. None is banked.

  3. THE STANDARD ROUTE NAMED AND MEASURED: Froggatt–Nielsen writes each
     Yukawa as an order-one coefficient times a power of the Cabibbo
     parameter. With the account's own Cabibbo value 9/40 the exponents
     are 3.07, 4.97 and 8.54 — the electron's coefficient is 0.45 at the
     eighth power and 1.99 at the ninth. The route parametrizes; it does
     not derive. Stated so the paper's sentence about it is a measurement.

  4. A FAMOUS COINCIDENCE PINNED AS A NEGATIVE so it is never re-found as
     a hit: the Koide mass scale Σm/6 = 313.84 ± 0.02 MeV sits 0.35 %
     from m_p/3 = 312.76 MeV. At the tau's bar that is fifty-four sigma.
     It is not a seat.

  5. THE PAPER CARRIES THE LEG as an open account: shape, position in bar
     units, the one-number reduction, the route, the rest-clock reading,
     and "open account rather than as a wall." §21.12 is retitled by its
     content. "Open, named" lists four items.
"""

import math
import pathlib
import sys

sys.path.insert(0, str(pathlib.Path(__file__).resolve().parent))
from test_the_yukawa_trail import N, REL, V, ME          # noqa: E402  the banked count

CATALOG = pathlib.Path(__file__).resolve().parent.parent / "catalog"
GRAVITY = (CATALOG / "GRAVITY-AS-TONAL-CENTER.md").read_text()
FLAT = " ".join(GRAVITY.split())

# measured inputs (CODATA 2018 / PDG), GeV unless stated
M_MU = 0.1056583755
M_TAU, D_TAU = 1.77686, 0.00012
M_P = 0.93827208816
MU_OVER_E = 206.7682830
P_OVER_E = 1836.15267343
M_PL_CODATA = 1.220890e19            # ±0.000014e19, 11 ppm, from G's 22 ppm
D_G_REL = 2.2e-5
ALPHA_G_ACCOUNT = 5 / (2 ** 151 - 1)


# --- 1. the three open positions are one number ------------------------------

def test_the_account_carries_the_electron_planck_ratio_exactly():
    """m_e/M_Planck = sqrt(alpha_G) = sqrt(10) * 2^-76 to the (2^151 - 1)
    truncation — the banked section-22 square."""
    assert abs(math.sqrt(ALPHA_G_ACCOUNT) / (math.sqrt(10) * 2.0 ** -76) - 1) < 1e-40


def test_v_over_planck_and_nucleon_over_v_are_functions_of_the_one_unknown():
    """Given the exact electron-Planck ratio and the seated proton ratio,
    both remaining positions are determined by v/m_e alone."""
    me_over_pl = math.sqrt(10) * 2.0 ** -76
    v_over_pl = N * me_over_pl
    p_over_v = P_OVER_E / N
    # shift the one unknown and both move with it, nothing else enters
    for scale in (1 - 1e-6, 1 + 1e-6):
        assert abs((scale * N) * me_over_pl / v_over_pl - scale) < 1e-12
        assert abs((P_OVER_E / (scale * N)) / p_over_v - 1 / scale) < 1e-12
    assert abs(v_over_pl - 2.0166e-17) < 0.0002e-17
    assert abs(1 / p_over_v - 262.42) < 0.01            # v/m_p


def test_the_reduction_is_consistent_with_the_measured_hierarchy():
    """The account's v/M_Planck must agree with v/M_Planck(CODATA) to the
    known G offset: the account's G is 106 ppm below CODATA, so its
    v/M_Planck is about 53 ppm below, inside the experiments' spread."""
    acc = N * math.sqrt(10) * 2.0 ** -76
    codata = V / M_PL_CODATA
    r = acc / codata - 1
    assert -1.2e-4 < r < 0                             # below, and by under 120 ppm


def test_the_reduction_sharpens_the_hierarchy_number_forty_fold():
    """Through G the hierarchy ratio carries 11 ppm; through the exact
    square it carries v/m_e's own 0.26 ppm."""
    via_g = D_G_REL / 2
    via_account = REL
    assert via_g / via_account > 40


# --- 2. the rest-clock reading of the count --------------------------------

def test_the_count_is_electron_ticks_per_electroweak_tick():
    h = 6.62607015e-34
    e = 1.602176634e-19
    nu_e = ME * 1e9 * e / h                            # m_e c^2 / h
    nu_v = V * 1e9 * e / h                             # v / h
    assert abs(nu_e - 1.2356e20) < 0.001e20            # the paper's Compton rate
    assert abs(nu_v - 5.954e25) < 0.002e25
    assert abs(nu_v / nu_e - N) < 1e-6 * N


# --- 3. the standard route, measured -----------------------------------------

def _yukawas():
    return {f: math.sqrt(2) * m / V for f, m in (("e", ME), ("mu", M_MU), ("tau", M_TAU))}


def test_froggatt_nielsen_exponents_with_the_accounts_cabibbo_value():
    eps = 9 / 40
    y = _yukawas()
    n = {f: math.log(v) / math.log(eps) for f, v in y.items()}
    assert abs(n["tau"] - 3.07) < 0.01
    assert abs(n["mu"] - 4.97) < 0.01
    assert abs(n["e"] - 8.54) < 0.01


def test_the_electrons_order_one_coefficient_is_not_one_at_any_power():
    """0.45 at the eighth power, 1.99 at the ninth: the route needs an
    order-one coefficient and so parametrizes rather than derives."""
    eps = 9 / 40
    ye = _yukawas()["e"]
    c8, c9 = ye / eps ** 8, ye / eps ** 9
    assert 0.43 < c8 < 0.46
    assert 1.97 < c9 < 2.01
    assert min(abs(ye / eps ** k - 1) for k in range(1, 20)) > 0.4


# --- 4. the Koide scale is not the nucleon third ----------------------------

def test_koide_solves_the_tau_as_banked():
    s = math.sqrt(ME) + math.sqrt(M_MU)
    lo, hi = 1.0, 3.0
    for _ in range(200):
        mid = (lo + hi) / 2
        f = (ME + M_MU + mid) - (2 / 3) * (s + math.sqrt(mid)) ** 2
        if f > 0:
            hi = mid
        else:
            lo = mid
    mt = (lo + hi) / 2
    assert abs(mt * 1e3 - 1776.969) < 0.002
    assert 0.85 < (mt - M_TAU) / D_TAU < 0.95


def test_the_koide_mass_scale_misses_the_nucleon_third_by_fifty_sigma():
    mu = (ME + M_MU + M_TAU) / 6                        # GeV
    d_mu = D_TAU / 6
    third = M_P / 3
    assert abs(mu * 1e3 - 313.84) < 0.01
    assert abs(third * 1e3 - 312.76) < 0.01
    rel = mu / third - 1
    assert 0.0033 < rel < 0.0037                        # the famous 0.35 %
    pull = (mu - third) / d_mu
    assert 50 < pull < 60                               # and not a seat


# --- 5. the paper carries the leg as an open account ------------------------

def test_the_paper_states_shape_position_and_the_one_number_reduction():
    assert "holds the shape of the charged-lepton ladder without its position" in FLAT
    assert "v/m_e = 481839.84 ± 0.12" in FLAT
    assert abs(N - 481839.84) < 0.13                    # inside the bar it quotes
    assert "the nearest banked station lies fifteen standard deviations away" in FLAT
    assert "the three open positions are one number and one derivation would close all three" in FLAT


def test_the_paper_names_the_route_and_the_needed_step():
    assert "Froggatt–Nielsen" in FLAT
    assert "parametrizes the spectrum and does not derive it" in FLAT
    assert "the count of electron ticks per electroweak tick" in FLAT
    assert "places the electroweak tick rate against the electron's, and none is banked" in FLAT


def test_the_boundary_is_an_open_account_not_a_target():
    assert "recorded as an open account rather than as a wall" in FLAT
    assert "recorded as a target rather than as a wall" not in FLAT
    
    assert "The position of the lepton ladder, v/m_e, stated above." in FLAT


def test_section_21_12_is_titled_by_its_content():
    assert "### 21.12 · The quantization apparatus" in GRAVITY
    assert "What is not here" not in GRAVITY
    assert "21.12 The quantization apparatus |" in GRAVITY   # the Contents row
