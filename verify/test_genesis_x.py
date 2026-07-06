"""test_genesis_x.py — Chapter X pinned: the lemma, the triples, the seat."""

from fractions import Fraction as F

from genesis_x import (c_rest_form, double_cover_shape, internal_rate,
                       triple_frames)


def test_the_triple_lattice_is_exact():
    """Dilation is exact rational arithmetic on the Pythagorean
    triples: 3/5 -> 4/5, 5/13 -> 12/13, 8/17 -> 15/17, 20/29 -> 21/29."""
    assert triple_frames() == [
        (F(3, 5), F(4, 5)),
        (F(5, 13), F(12, 13)),
        (F(8, 17), F(15, 17)),
        (F(20, 29), F(21, 29)),
    ]


def test_the_conditional_lemma_arithmetic():
    """rate^2 + beta^2 = 1 — the quadratic budget split, exact where
    exact and consistent everywhere."""
    for beta, rate in triple_frames():
        assert rate ** 2 + beta ** 2 == 1
    assert abs(internal_rate(F(1, 2)) ** 2 + 0.25 - 1) < 1e-12


def test_the_rest_form_and_the_refusal():
    """3(10^8 - 1) = 299999997 = 3^3 x 11 x 73 x 101 x 137 (internal);
    the SI value of c is definitional and refused on the boundary."""
    c = c_rest_form()
    assert c["value"] == 299_999_997
    assert c["factors"] == {3: 3, 11: 1, 73: 1, 101: 1, 137: 1}


def test_the_double_cover_shape():
    """Full return at 8 ticks; the half (the Midy antipode) differs:
    position at the half, identity only at the whole — the spinor's
    structural seat."""
    assert double_cover_shape()


def test_the_payment_light_is_exactly_c_on_the_lattice():
    """X open problem #2's first datum + the LIV watch's first benign entry:
    the massless mode has ZERO dispersion at all k (1+1D, unit ratio)
    — the concealment is exact for light, structurally."""
    from genesis_x import massless_dispersion_error
    for k in (0.1, 0.5, 1.0, 2.0, 3.0):
        assert abs(massless_dispersion_error(k)) < 1e-12


def test_the_identification_is_the_dispersion():
    """THE ONE IDENTIFICATION, made: (translation, internal) =
    (k/w, mu/w) — the phase field's two components under the SQUARED
    wave operator; the quadratic law is the operator's dispersion;
    and E = gamma m emerges (w/mu = gamma to 1e-6 in the domain)."""
    import math
    from genesis_x import massive_dispersion
    mu = 0.001
    for k in (0.0005, 0.001, 0.002):
        w, resid, beta, rate, gamma_lattice = massive_dispersion(k, mu)
        assert abs(resid) < 1e-14                  # exact sine-Pythagoras
        assert abs(rate ** 2 + beta ** 2 - 1) < 1e-6
        gamma = 1 / math.sqrt(1 - beta ** 2)
        assert abs(gamma_lattice - gamma) / gamma < 1e-6   # E = gamma m
