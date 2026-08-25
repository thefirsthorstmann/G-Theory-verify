"""test_leverage.py — the dual cancellation and the exponent bookkeeping of
UNITS-ON-DISCRETE-TERMS section 6.1, pinned 2026-08-08.

The principle: where a constant enters an observable's defining expression and
its reporting unit at the same exponent, it divides out of the report, and the
reading is silent about that constant at every precision.

Primitives: the seven stipulated SI numerals (all pi-free) plus the measured,
pi-free readings m_e and G. hbar = h/(2 pi) is the single gate through which pi
enters the system's own constants.
"""
import math

C  = 299792458.0
H  = 6.62607015e-34
E  = 1.602176634e-19
K  = 1.380649e-23
ME = 9.1093837015e-31
G  = 6.67430e-11
DG = 0.00015e-11
ALPHA_INV = 137.035999177


def test_the_perihelion_comparison_cancels_pi_identically():
    """6 pi GM/(c^2 a(1-e^2)) radians per orbit, compared in arcseconds where
    1 rad = 648000/pi arcsec: the pi of the formula and the pi of the unit are
    the same pi, and the product 6 pi x 648000/pi = 3888000 is exact."""
    from sympy import pi, Rational, simplify
    assert simplify((6 * pi) * (Rational(648000) / pi)) == 3888000
    # and numerically, the full prediction is invariant under ANY pi re-valuation
    GM = 1.32712440018e20; a = 5.7909050e10; ecc = 0.205630
    def arcsec_per_orbit(P):
        return (6 * P * GM / (C**2 * a * (1 - ecc**2))) * (648000.0 / P)
    # the cancellation is algebraic (the sympy line above); in floats the two
    # evaluation orders agree to machine epsilon
    assert abs(arcsec_per_orbit(math.pi) / arcsec_per_orbit(3.0) - 1) < 1e-14


def test_the_1948_2019_electromagnetic_sector_was_pi_free():
    """With mu_0 stipulated as 4 pi x 10^-7 exactly, alpha = mu_0 c e^2/(2h) is
    proportional to pi by stipulation, so alpha/(2 pi) = 10^-7 c e^2 / h carries
    no pi at all. The leading term of the electron's anomalous moment was pi-free
    by construction for seven decades."""
    schwinger_from_stipulation = 1e-7 * C * E**2 / H          # no pi anywhere
    schwinger_from_alpha = 1 / (ALPHA_INV * 2 * math.pi)
    assert abs(schwinger_from_stipulation / schwinger_from_alpha - 1) < 1e-9


def test_the_exponent_table_of_section_6_1():
    """The derived constants divide cleanly: pi enters only through the hbar gate
    (h/2pi) or an explicit pi of the formula. Exponents derived by composition."""
    X = {"h": 0, "e": 0, "c": 0, "k": 0, "m_e": 0, "G": 0, "pi": 1}
    def expo(*parts):
        return sum(X[n] * p for n, p in parts)
    X["hbar"] = expo(("h", 1), ("pi", -1))

    table = {
        "R_K   h/e^2":            expo(("h", 1), ("e", -2)),
        "K_J   2e/h":             expo(("e", 1), ("h", -1)),
        "Phi_0 h/2e":             expo(("h", 1), ("e", -1)),
        "lam_C h/m_e c":          expo(("h", 1), ("m_e", -1), ("c", -1)),
        "c_2   hc/k":             expo(("h", 1), ("c", 1), ("k", -1)),
        "hbar  h/2pi":            X["hbar"],
        "red-C hbar/m_e c":       expo(("hbar", 1), ("m_e", -1), ("c", -1)),
        "mu_B  e hbar/2m_e":      expo(("e", 1), ("hbar", 1), ("m_e", -1)),
        "c_1   2 pi h c^2":       expo(("pi", 1), ("h", 1), ("c", 2)),
        "sigma 2pi^5k^4/15h^3c^2": expo(("pi", 5), ("k", 4), ("h", -3), ("c", -2)),
        "l_P   sqrt(hbar G/c^3)": expo(("hbar", 0.5), ("G", 0.5), ("c", -1.5)),
    }
    assert [table[k] for k in table] == [0, 0, 0, 0, 0, -1, -1, -1, 1, 5, -0.5]
    zero = [k for k, v in table.items() if v == 0]
    assert all("hbar" not in k for k in zero)                 # the h-built are silent
    assert table["hbar  h/2pi"] == -1                          # the gate itself


def test_the_planck_convention_factor():
    """Planck's 1899 units used h; the modern ones use hbar. The two differ by
    sqrt(2 pi) = 2.5066..., so 'the Planck length' names a convention."""
    hbar = H / (2 * math.pi)
    lP_hbar = math.sqrt(hbar * G / C**3)
    lP_h = math.sqrt(H * G / C**3)
    assert abs(lP_h / lP_hbar - math.sqrt(2 * math.pi)) < 1e-12
    assert abs(lP_hbar - 1.616255e-35) < 1e-40
    assert abs(lP_h - 4.051351e-35) < 1e-40
    assert abs(math.sqrt(2 * math.pi) - 2.5066283) < 1e-7


def test_the_planck_units_entire_uncertainty_is_G():
    """hbar and c are exact since 2019, so G is the sole uncertainty source of
    every Planck unit, entering at power 1/2: 22.47 ppm halves to 11.24 ppm."""
    relG = DG / G
    assert abs(relG - 2.247e-5) < 1e-8
    assert abs(relG / 2 - 1.124e-5) < 1e-8


def test_the_2019_rotation_of_the_classes():
    """The revision rotated constants between the classes: R_K and sigma became
    exact computations; mu_0 returned to the readings, its uncertainty now
    alpha's. Pinned numerically from the stipulated values alone."""
    R_K = H / E**2
    assert abs(R_K - 25812.80745) < 1e-4                       # exact von Klitzing
    sigma = 2 * math.pi**5 * K**4 / (15 * H**3 * C**2)
    assert abs(sigma / 5.670374419e-8 - 1) < 1e-9              # exact Stefan-Boltzmann
    mu_0 = 2 * (1 / ALPHA_INV) * H / (C * E**2)                # now a READING via alpha
    assert abs(mu_0 / (4e-7 * math.pi) - 1) < 1e-8             # still 4pi e-7 to ~1e-9
