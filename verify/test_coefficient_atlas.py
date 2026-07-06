"""test_coefficient_atlas.py — the atlas pinned: routes, not furniture."""

import math

from coefficient_atlas import (basel, blackbody, einstein_route,
                               gauss_integral, loop_factor, polar_diameter,
                               solid_angle, sphere_measure)


def test_the_solid_angle_route():
    """4 pi = (2 pi) x 2: azimuth closure times the polar diameter —
    the polar integral is EXACTLY 2 (cos 0 - cos pi)."""
    assert abs(polar_diameter() - 2.0) < 1e-15
    assert abs(solid_angle() - 4 * math.pi) < 1e-12


def test_the_einstein_route_is_doubled_flux():
    """8 pi = 2 x (4 pi): the tensor's two sheets, not eight turns."""
    assert abs(einstein_route() - 8 * math.pi) < 1e-12


def test_the_basel_route_is_the_lattice():
    """zeta(2) -> pi^2/6: the circle's square arriving by COUNTING
    the integer lattice — no circle drawn."""
    assert abs(basel() - math.pi ** 2 / 6) < 1e-4


def test_the_gaussian_route_is_the_half_closure():
    """int e^{-x^2} = sqrt(pi): one dimension's share of a 2D closure
    — the diffusion envelope's root (Chapter IX's pi-from-counting)."""
    assert abs(gauss_integral() - math.sqrt(math.pi)) < 1e-9


def test_the_loop_factor_is_flux_squared():
    """16 pi^2 = (4 pi)^2: one loop = one 4D momentum closure."""
    assert abs(loop_factor() - 16 * math.pi ** 2) < 1e-10


def test_the_sphere_ladder():
    """S^1 = 2pi, S^2 = 4pi, S^3 = 2pi^2: the closure ladder by
    dimension — each rung a different process signature."""
    assert abs(sphere_measure(1) - 2 * math.pi) < 1e-12
    assert abs(sphere_measure(2) - 4 * math.pi) < 1e-12
    assert abs(sphere_measure(3) - 2 * math.pi ** 2) < 1e-12


def test_the_blackbody_route_is_thermal_counting():
    """int x^3/(e^x - 1) = pi^4/15: Planck's integral — the fourth
    lattice sum; the coefficient that ended the ultraviolet
    catastrophe carries the mode count in its route."""
    assert abs(blackbody() - math.pi ** 4 / 15) < 1e-4
