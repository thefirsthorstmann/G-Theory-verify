"""Pins for "pi on Discrete Terms" (pi_terms.py)."""

import math
from fractions import Fraction

from pi_terms import (PI_60, polygon_bracket, midpoint_overshoots,
                      excess_deficit_ratio, best_bounds, rest_pi,
                      rest_pi_overshoot_ppm, counting_envelope,
                      rational_witness)


def test_reference_pi():
    assert abs(float(PI_60) - math.pi) < 1e-15


def test_bracket_brackets():
    for _, i_n, c_n in polygon_bracket(20):
        assert i_n < math.pi < c_n


def test_archimedes_overshoot():
    # the midpoint of every classical bracket sits above pi
    # (depth 12: n = 24576, errors ~1e-9 — far above float noise)
    assert midpoint_overshoots(12)
    # and the excess/deficit ratio tends to 2
    assert abs(excess_deficit_ratio(12) - 2) < 1e-2
    # visibly converging toward 2 stage by stage
    r6, r9, r12 = (excess_deficit_ratio(d) for d in (6, 9, 12))
    assert abs(r9 - 2) < abs(r6 - 2) and abs(r12 - 2) < abs(r9 - 2)


def test_register_bounds_forced():
    lower, upper = best_bounds()
    assert upper == Fraction(22, 7)          # ceil(7 pi)/7
    assert lower == Fraction(201, 64)        # floor(64 pi)/64
    assert lower < PI_60 < upper


def test_rest_pi_exact_and_above():
    assert rest_pi() == Fraction(2815, 896)
    assert rest_pi() > PI_60                 # the inherited overshoot
    assert 46 < rest_pi_overshoot_ppm() < 49  # ~47 ppm


def test_pi_from_counting():
    # no circle drawn: the envelope converges to pi from below
    vals = [counting_envelope(n) for n in (10, 100, 1000, 10000)]
    errs = [abs(v - math.pi) for v in vals]
    assert errs == sorted(errs, reverse=True)     # monotone approach
    assert errs[-1] < 1e-4


def test_finite_precision_never_certifies():
    for k in (3, 6, 12, 24):
        r = rational_witness(k)
        assert abs(float(r) - math.pi) < 10.0 ** -k or k > 15
        assert r.denominator <= 10 ** k


def test_rest_pi_settles_into_the_reptend():
    from pi_terms import rest_pi_expansion
    e = rest_pi_expansion(31)
    assert e.startswith("3.1417410")
    tail = e[len("3.1417410"):]
    # pure period-6 cycle of 1/7 from there on, exactly
    assert tail == ("714285" * 6)[:len(tail)]


def test_universal_overshoot_all_orders():
    # the integral-inequality form: midpoint > pi for EVERY n >= 3
    for n in range(3, 2001):
        x = math.pi / n
        assert (n*math.sin(x) + n*math.tan(x)) / 2 > math.pi


def test_margin_witness_at_boundary_tight_test():
    # the referee's counterexample becomes the pin: reading 3.24 at
    # precision 0.1 accepts pi (margin ~0.0016); the deep truncation
    # passes where the shallow one fails
    reading, tol = 3.24, 0.1
    assert abs(reading - math.pi) < tol            # pi passes
    shallow = rational_witness(1)                  # 3.1 — fails the test
    assert abs(reading - float(shallow)) > tol
    deep = rational_witness(3)                     # 3.141 — passes
    assert abs(reading - float(deep)) < tol
