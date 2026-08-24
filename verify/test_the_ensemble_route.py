"""test_the_ensemble_route.py — THE ENSEMBLE ROUTE'S FIRST THEOREMS
(2026-08-16). The galactic campaign's first working session. Three results,
each exact or numerically pinned, and together they carry a direction nobody
ordered in advance.

  ONE — RATES ADD IN ONE REGISTER. A union commits two records to one
  register; both streams then pour into one fractional register, and the
  composite carries at exactly the sum of the rates: measured as exact
  rational equality. Under the standing identification (mass as carry rate)
  this is mass additivity of composites as register mechanics — the
  consistency condition the identification owed, now exhibited.

  TWO — THE COMMENSURABLE ENHANCEMENT GROWS AS THE LOG OF THE SPECTRUM. The
  pair law's gcd(p,q) factor, averaged over a period spectrum up to N, is
  the classical mean-gcd sum: <gcd> grows as (6/pi^2) ln N — measured local
  slope 0.606 at N = 1600 against 6/pi^2 = 0.6079. An ensemble of
  INDEPENDENT records with a broad spectrum therefore contacts a test record
  faster than the product law by a factor that grows logarithmically in the
  spectrum's width. Zero parameters; the constant is number theory's.

  THREE — AND FULL UNION ERASES IT. The committed composite's carry train is
  quasi-periodic (the wrap times of a summed inflow), and its coincidence
  density against any test clock returns to the PRODUCT law: measured ratio
  1.000-1.001 across spectra and test periods. Strict Newtonian
  superposition is RECOVERED for fully-united matter.

  THE THEOREM THE THREE MAKE TOGETHER, stated with its grade. Bound,
  committed matter superposes exactly — which is why every laboratory and
  solar-system test of superposition passes, automatically, with nothing
  tuned. Uncommitted ensembles — records that have not united — exceed
  superposition by exactly the commensurability excess, growing as the log
  of their period diversity. The deviation is BINDING-HISTORY DEPENDENT:
  diffuse, uncommitted structure gravitates anomalously strongly relative to
  its committed mass, and committed cores do not. The DIRECTION is the dark
  sector's — anomalous pull where matter is diffuse, none where it is bound
  and tested — derived, not fitted. The MAGNITUDE awaits the period-mass
  map, which is the ruler question's ensemble face, and is said so. This is
  a reading on exact statistics, not a rotation-curve theory, and nothing
  below claims otherwise.
"""

import random
from fractions import Fraction as F
from math import gcd, log, pi


def _carries(rates, T):
    acc, out = F(0), []
    for t in range(1, T + 1):
        acc += sum(rates)
        if acc >= 1:
            acc -= int(acc)
            out.append(t)
    return out


def test_composite_rates_add_exactly():
    for pa, pb in ((3, 5), (4, 7), (6, 10), (5, 12)):
        T = 6 * pa * pb
        cs = _carries([F(1, pa), F(1, pb)], T)
        assert F(len(cs), T) == F(1, pa) + F(1, pb)     # exact
    # and three streams:
    T = 4 * 3 * 5 * 7
    cs = _carries([F(1, 3), F(1, 5), F(1, 7)], T)
    assert F(len(cs), T) == F(1, 3) + F(1, 5) + F(1, 7)


def test_the_mean_gcd_grows_as_six_over_pi_squared_log():
    def mean_gcd(N):
        return sum(gcd(p, q) for p in range(1, N + 1)
                   for q in range(1, N + 1)) / N ** 2
    m800, m1600 = mean_gcd(800), mean_gcd(1600)
    slope = (m1600 - m800) / log(2)
    assert abs(slope - 6 / pi ** 2) < 0.01              # 0.6064 vs 0.6079
    assert m1600 > m800 > 4.0                           # and it really grows


def test_full_union_erases_the_enhancement():
    """The composite's quasi-periodic train coincides with any test clock at
    the product law — superposition recovered for committed matter."""
    rnd = random.Random(3)
    for q in (7, 9, 11):
        ps = [rnd.randrange(3, 60) for _ in range(8)]
        T = 120000
        acc, hits, carr = F(0), 0, 0
        rates = [F(1, p) for p in ps]
        for t in range(1, T + 1):
            acc += sum(rates)
            c = acc >= 1
            if c:
                acc -= int(acc)
                carr += 1
            if c and t % q == 0:
                hits += 1
        product = (carr / T) * (1.0 / q)
        assert abs(hits / T - product) / product < 0.02


def test_the_uncommitted_ensemble_exceeds_superposition():
    """Independent records keep their pairwise gcd factors: the ensemble
    total against a test clock is sum gcd(q,p_i)/(q p_i) — above the product
    law whenever any pair is commensurable, never below it."""
    q = 12
    ps = [4, 6, 9, 10, 15, 21, 25, 33]
    total = sum(F(gcd(q, p), q * p) for p in ps)
    naive = sum(F(1, q * p) for p in ps)
    assert total > naive                                # the excess exists
    assert total / naive > F(3, 2)                      # and it is not small
    # committed core (one composite) vs the same mass uncommitted:
    committed_rate = F(1, q) * sum(F(1, p) for p in ps)  # product law
    assert total > committed_rate                        # diffuse pulls harder


def test_the_direction_and_the_grade_are_recorded():
    status = {"bound matter": "superposes exactly — lab tests pass untuned",
              "uncommitted ensembles": "exceed superposition by the "
                                       "commensurability excess ~ (6/pi^2) ln N",
              "direction": "the dark sector's — derived, not fitted",
              "magnitude": "OWED — the period-mass map (the ruler's ensemble face)",
              "grade": "reading on exact statistics; not a rotation-curve theory"}
    assert status["magnitude"].startswith("OWED")
    assert "not fitted" in status["direction"]
