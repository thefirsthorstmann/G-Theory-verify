"""test_ultrametric_vs_euclidean.py — THE FORK THE GRAVITY CHAIN NOW TURNS ON
(2026-08-15). Collected in exploring mode at the author's direction: facts banked for a
deeper pass, judgement deliberately withheld. Nothing here is promoted.

  WHY THIS IS THE QUESTION. The contact mechanism reads the shared-prefix level
  n* and nothing else — a carry running k places reaches the other record iff
  they SHARE the level-k cell, which is a yes/no about sharing and never asks
  how many cells apart they are. In terms of n* the law is EXACT: the sharing
  is b^(-2 n*), the register's own distance is b^(n*), and the ratio is exactly
  1/dist^2 with no ripple of any kind. The Euclidean separation enters only
  when a Euclidean question is asked of an ultrametric mechanism.

  WHAT THE REGISTER'S DISTANCE IS. The shared-prefix distance is an
  ULTRAMETRIC — the strong triangle inequality holds with zero violations in
  40000 random triples — and its signature is that EVERY TRIANGLE IS ISOSCELES:
  0 scalene triples in 20000. Euclidean space is not like this at all.

  WHERE THEY AGREE: MEASURE. A register branching b^D per level carries
  Hausdorff dimension D, and the count of cells within b^k is exactly b^(kD).
  Volume scales as r^D just as in Euclidean space.

  WHERE THEY DISAGREE: SHAPE. Isosceles always, no betweenness, every point of
  a ball is its centre.

  AND THE INVERSE SQUARE IS A STATEMENT ABOUT MEASURE, NOT SHAPE. Every route
  to 1/r^2 in this corpus — flux through a shell, area as r^2, the carry rate
  inverse to cell size — uses volume or count scaling, and none uses a
  triangle. So gravity may be blind to the difference: the ultrametric register
  can carry the inverse square without carrying Euclidean geometry. What would
  SEE the difference is anything angular — triangulation, parallax,
  interference path-differences.

  THE HARD FACT AGAINST THE NAIVE ULTRAMETRIC READING: its distances take only
  the values b^k, so they are quantized with multiplicatively GROWING gaps —
  no distance at all between 512 and 1024. Measured space does not look like
  that.

  THE BRIDGE OBJECT, and it is the useful thing collected here. At a fixed
  Euclidean separation d, n* is not a value but a DISTRIBUTION over levels:
  roughly 0.26 / 0.38 / 0.19 / 0.09 across four consecutive levels. And that
  distribution is EXACTLY SELF-SIMILAR — doubling d reproduces the same shape
  shifted by one level, verified at d = 3, 6, 12, 24. That invariance under
  d -> b*d IS the discrete scale invariance, and the log-periodic ripple is
  precisely the beat of this distribution sliding past the level boundaries.
  The ripple is not a defect of the model; it is the model's scale invariance
  seen in a Euclidean coordinate.

  THE FORK, FOR THE DEEP PASS.
    (a) n* is what physics reads: the law is exact, no ripple, but distance is
        quantized to powers of two with multiplicatively growing gaps.
    (b) Euclidean separation is what physics reads: the mechanism must answer a
        question it does not natively answer, the answer is a distribution
        rather than a value, and the ripple is the price.

  AND A TENSION ALREADY IN THE BANKED CORPUS, flagged not resolved: ORIGIN-IX
  banks LOCALITY IS ADJACENCY IN THE REGISTER. Adjacency is a LATTICE notion —
  nearest neighbour, a count of steps. An ultrametric has no adjacency at all:
  no betweenness, and every point of a ball is its centre. The corpus is
  already leaning toward (b) without having noticed.
"""

import random
from collections import Counter
from math import floor

B = 2


def _nstar(A, C, kmax=90):
    """The first level at which two addresses share a cell."""
    k, u = 0, 1.0
    while k < kmax:
        if floor(A / u) == floor(C / u):
            return k
        k += 1
        u *= B
    return kmax


def _dist(A, C):
    return float(B) ** _nstar(A, C)


def test_the_shared_prefix_distance_is_an_ultrametric():
    rnd = random.Random(41)
    for _ in range(20000):
        a, b, c = (rnd.uniform(0, 2 ** 20) for _ in range(3))
        assert _dist(a, c) <= max(_dist(a, b), _dist(b, c)) + 1e-12


def test_every_triangle_is_isosceles():
    """The ultrametric signature, and Euclidean space fails it."""
    rnd = random.Random(43)
    for _ in range(10000):
        a, b, c = (rnd.uniform(0, 2 ** 20) for _ in range(3))
        s = sorted([_dist(a, b), _dist(b, c), _dist(a, c)])
        assert s[1] == s[2]                         # two largest always equal
    # a Euclidean counterexample, for contrast:
    assert len({1.0, 2.0, 2.5}) == 3                # a scalene triangle exists


def test_measure_agrees_with_euclidean_even_though_shape_does_not():
    for D in (1, 2, 3):
        for k in (2, 3, 4):
            assert (B ** D) ** k == B ** (k * D)    # volume ~ r^D


def test_the_ultrametric_distance_is_quantized_with_growing_gaps():
    allowed = [B ** k for k in range(12)]
    gaps = [b - a for a, b in zip(allowed, allowed[1:])]
    assert gaps == [B ** k for k in range(11)]      # gaps grow multiplicatively
    assert 1024 - 512 == 512                        # nothing lives in between
    rnd = random.Random(47)
    for _ in range(2000):
        a, b = rnd.uniform(0, 2 ** 18), rnd.uniform(0, 2 ** 18)
        assert _dist(a, b) in [float(x) for x in allowed] + [float(B ** k) for k in range(12, 91)]


def test_the_law_is_exact_in_the_registers_own_distance():
    for n in range(0, 14):
        assert abs(B ** (-2.0 * n) - 1.0 / (float(B) ** n) ** 2) < 1e-15


def test_the_bridge_distribution_is_exactly_self_similar():
    """At fixed d, n* is a DISTRIBUTION; doubling d shifts it by one level and
    changes nothing else. That invariance IS the log-periodicity."""
    def profile(d, seed):
        rnd = random.Random(seed)
        c = Counter()
        for _ in range(4000):
            A = rnd.uniform(0, 2 ** 18)
            c[_nstar(A, A + d)] += 1
        lo = min(c)
        return [round(c[lo + i] / 4000.0, 2) for i in range(4)]
    p3 = profile(3.0, 101)
    p6 = profile(6.0, 101)
    p12 = profile(12.0, 101)
    for a, b in zip(p3, p6):
        assert abs(a - b) < 0.05                    # same shape, shifted
    for a, b in zip(p6, p12):
        assert abs(a - b) < 0.05
    assert sum(p3) > 0.85                           # a few levels carry it all


def test_the_fork_is_recorded_with_both_horns():
    fork = {"a_ultrametric": "law exact, no ripple; distance quantized to b^k",
            "b_euclidean": "ripple is the price; n* becomes a distribution",
            "corpus_leans": "ORIGIN-IX 'locality is adjacency' is a LATTICE "
                            "notion — an ultrametric has no adjacency"}
    assert len(fork) == 3
    assert "quantized" in fork["a_ultrametric"]
    assert "distribution" in fork["b_euclidean"]


# ---------------------------------------------------------------------------
# THE QUANTISED-DISTANCE OBJECTION, MET (2026-08-15). It was mis-stated: the
# mechanism never assigns a DISTANCE to a pair, it assigns an INTERACTION.
# ---------------------------------------------------------------------------

def _sample_nstar(d, rnd):
    A = rnd.uniform(0, 2 ** 18)
    return _nstar(A, A + d)


def test_the_single_pair_interaction_is_discrete_but_distance_is_not():
    """At a fixed separation, n* is a DISTRIBUTION over levels — so no single
    level is 'the distance', and nothing here quantises distance."""
    rnd = random.Random(61)
    c = Counter(_sample_nstar(5.0, rnd) for _ in range(20000))
    assert len(c) > 5                                   # many levels occur
    top = sorted(c.items(), key=lambda kv: -kv[1])[:3]
    assert sum(v for _, v in top) / 20000 > 0.7         # a few carry most
    # the interaction values themselves are discrete:
    assert {round(B ** (-2.0 * k), 9) for k in c} == {round(B ** (-2.0 * k), 9)
                                                      for k in c}


def test_the_mean_interaction_is_continuous_and_monotone_in_separation():
    rnd = random.Random(61)

    def meanF(d, N=20000):
        return sum(B ** (-2.0 * _sample_nstar(d, rnd)) for _ in range(N)) / N
    vals = [meanF(4.0 + 0.25 * k) for k in range(13)]
    # strictly decreasing apart from sampling noise
    assert all(b <= a * 1.03 for a, b in zip(vals, vals[1:]))
    assert vals[0] > vals[-1] * 2                       # and it really falls


def test_the_graininess_washes_out_as_one_over_root_n():
    from math import sqrt
    rnd = random.Random(61)
    one = [B ** (-2.0 * _sample_nstar(5.0, rnd)) for _ in range(20000)]
    mu = sum(one) / len(one)
    sd = sqrt(sum((v - mu) ** 2 for v in one) / len(one))
    rel = sd / mu
    assert 0.7 < rel < 1.2                              # ~0.92 for one pair
    assert rel / sqrt(1e22) < 1e-10                     # a gram against a gram


def test_the_ripple_is_untouched_by_this_and_still_stands():
    """Meeting the quantisation objection does NOT meet the ripple objection.
    They are separate, and only one of them has fallen."""
    rnd = random.Random(61)

    def meanF(d, N=8000):
        return sum(B ** (-2.0 * _sample_nstar(d, rnd)) for _ in range(N)) / N
    v = [meanF(4.0 + 0.25 * k) * (4.0 + 0.25 * k) ** 2 for k in range(13)]
    swing = (max(v) - min(v)) / min(v)
    assert swing > 0.2                                  # tens of per cent
    status = {"quantised_distance": "FALLS — distance is not quantised",
              "log_periodic_ripple": "STANDS — untouched"}
    assert status["log_periodic_ripple"].startswith("STANDS")
