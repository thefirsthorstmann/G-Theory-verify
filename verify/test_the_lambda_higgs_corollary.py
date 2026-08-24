"""test_the_lambda_higgs_corollary.py — THE SEATED HIGGS SELF-COUPLING MAKES
v AN EXACT RATIONAL MULTIPLE OF THE HIGGS MASS, AND THE POSITION GETS A
LIVE KILL NUMBER; THE DIRECT DERIVATION GETS A CALIBRATED NEGATIVE
(2026-08-24). the author: "what's to stop us from seeing if we can get this
derivation?" Nothing did; here is what the attempt produced.

THE COROLLARY (of a seat banked BEFORE comparison — the parameter record's
λ = 2⁹/(3⁴·7²) = 512/3969, prediction-first, 2026-07-03; no look-elsewhere
attaches). With m_H² = 2λv²:

    √(2λ) = √(1024/3969) = 32/63  EXACTLY
    v = (63/32) · m_H             on the seats
    m_H(pred) = (32/63) · v = 125.06395 ± 0.00003 GeV   (bar from G_F)

Against measurement: PDG 125.20 ± 0.11 (−1.24σ), ATLAS 125.11 ± 0.11
(−0.42σ), CMS 125.38 ± 0.14 (−2.26σ). The coming generation of Higgs-mass
measurements (tens of MeV) decides the seat at many sigma either way. The
position v/m_e is thereby EQUIVALENT to the Higgs-to-electron ratio:
v/m_e = (63/32)(m_H/m_e), and 63/32 = 3²·7/2⁵ is itself a register word.

THE EXCLUSION. If λ is exact, m_H/m_e = (32/63)(v/m_e) = 244,744.05 ± 0.06
(the 0.26-ppm bar inherited from G_F). The nearest pure 2-3-7 word,
2⁴·3⁷·7 = 244,944, sits −0.31σ of the SOFT direct bar (m_H ± 0.11 GeV) but
+3,142σ of the tight chain: THE λ SEAT AND ANY 2-3-7 WORD FOR m_H/m_e ARE
MUTUALLY EXCLUSIVE at the v bar. The word's own null: 2-3-7 words have
density ≈ 52 per e-fold here, so ≈ 0.09 expected within the ±1σ direct
window — a one-in-eleven accident, recorded as such, not as a seat. The
near-integrality of the chain (244,744.046 ± 0.063, 0.73σ from the
integer) has probability ≈ 9 per cent under a uniform fractional part and
is recorded as non-evidence, per the banked 481840 lesson.

THE CALIBRATED NEGATIVE (the declared trail search; the generator set is
stated below and generosity in it only strengthens a negative). Generators:
the theory's own named constants — 2, 3, 7, 10, 24, 137, 151, the seven
just ratios, 8/7, 7/4, 63/32, 9/40, the four commas, and the shortfall
999999/10⁶ — with inverses, products of up to depth six:

    depth ≤ 4:    230,299 trails   0 in bar   0 within 5 ppm
    depth 5:    2,118,760 trails   0 in bar   0 within 5 ppm
    depth 6:   18,009,460 trails   0 in bar   0 within 5 ppm; closest 172 ppm

with the empirical null expecting only 0.02 accidental in-bar hits through
depth six — the search had discovery power and returned empty. The
position is beyond the theory's own vocabulary at low depth; what remains
is the operation the paper names, not a hidden product of the constants.
"""

import itertools
import math
from fractions import Fraction as F

import pathlib

CATALOG = pathlib.Path(__file__).resolve().parent.parent / "catalog"
GRAVITY = (CATALOG / "GRAVITY-AS-TONAL-CENTER.md").read_text()
FLAT = " ".join(GRAVITY.split())

LAM = F(2 ** 9, 3 ** 4 * 7 ** 2)
V, DV_REL = 246.219651, 0.26e-6                    # GeV, from G_F
ME = 0.51099895069e-3
N = V / ME


# --- the corollary -----------------------------------------------------------------

def test_root_two_lambda_is_exactly_thirty_two_sixty_thirds():
    assert 2 * LAM == F(1024, 3969)
    assert F(32, 63) ** 2 == 2 * LAM
    assert F(63, 32) == F(3 ** 2 * 7, 2 ** 5)      # the multiplier is a register word


def test_the_seat_predicts_the_higgs_mass():
    mh = V * 32 / 63
    assert abs(mh - 125.06395) < 0.0001
    assert abs(mh * DV_REL) < 0.0001               # the prediction's own bar, GeV
    for name, m, dm in (("PDG", 125.20, 0.11), ("ATLAS", 125.11, 0.11), ("CMS", 125.38, 0.14)):
        pull = (mh - m) / dm
        assert abs(pull) < 3.0, name               # live, not excluded, not confirmed
    assert (mh - 125.20) / 0.11 < -1.0             # and honestly below the PDG centre


def test_the_position_is_equivalently_the_higgs_electron_ratio():
    chain = N * 32 / 63
    assert abs(chain - 244744.05) < 0.02
    direct = 125.20 / ME / 1  # m_H/m_e measured
    assert abs(direct - 245010.3) < 0.5
    assert abs((chain - direct) / (0.11 / ME)) < 1.5   # consistent at the soft bar


# --- the exclusion -----------------------------------------------------------------

def test_the_seat_and_the_nearest_word_are_mutually_exclusive():
    word = 2 ** 4 * 3 ** 7 * 7
    assert word == 244944
    soft_pull = (word - 125.20 / ME) / (0.11 / ME)
    tight_pull = (word - N * 32 / 63) / (N * 32 / 63 * DV_REL)
    assert abs(soft_pull) < 0.5                    # inside the direct bar
    assert tight_pull > 3000                       # far outside the chain's bar
    # the word's null: ~0.09 expected in the ±1σ window — a 1-in-11 accident
    lnX = math.log(2.45e5)
    density = lnX ** 2 / (2 * math.log(2) * math.log(3) * math.log(7))
    assert 0.05 < density * 2 * (0.11 / 125.20) < 0.15


def test_near_integrality_of_the_chain_is_not_evidence():
    chain = N * 32 / 63
    frac = abs(chain - round(chain))
    assert frac < 0.1
    assert 2 * frac > 0.05                         # ≈ 9% under a uniform fractional part


# --- the calibrated negative, re-run fast at depth ≤ 4 ------------------------------

def _gens():
    vals = [2, 3, 7, 10, 24, 137, 151,
            F(3, 2), F(4, 3), F(5, 4), F(9, 8), F(5, 3), F(15, 8), F(6, 5),
            F(8, 7), F(7, 4), F(63, 32), F(9, 40),
            F(81, 80), F(531441, 524288), F(64, 63), F(126, 125), F(999999, 1000000)]
    return [math.log(float(v)) for v in vals]


def test_no_trail_of_the_theorys_constants_reaches_the_position_at_depth_four():
    logs = _gens()
    signed = [l for l in logs] + [-l for l in logs]
    target = math.log(N)
    hits = near = inwin = 0
    for depth in range(1, 5):
        for combo in itertools.combinations_with_replacement(signed, depth):
            L = sum(combo)
            d = abs(L - target)
            if d < 1e-2:
                inwin += 1
                rel = abs(math.expm1(L - target))
                if rel < DV_REL:
                    hits += 1
                elif rel < 5e-6:
                    near += 1
    assert hits == 0 and near == 0
    assert inwin <= 10                              # the null: nothing even lands nearby
    # depths 5 and 6 (2.1M and 18M trails) were run in-session with the same
    # outcome — 0 in bar, 0 within 5 ppm, closest 1.7e-4 — and are recorded
    # in the docstring rather than re-run here for speed.


# --- the papers carry it ------------------------------------------------------------

def test_the_gravity_paper_carries_the_constraint_and_the_negative():
    assert "√(2λ) the exact rational 32/63" in FLAT
    assert "m_H = 125.0640 ± 0.0001 GeV" in FLAT
    assert "twenty million trails through depth six" in FLAT
    assert "verify/test_the_lambda_higgs_corollary.py" in FLAT
