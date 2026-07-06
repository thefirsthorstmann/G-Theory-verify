"""bridge.py — THE RULER-RATIO LADDER (the bridge to magnitudes).

THE POSITION: the Scale Theorem stands — no dimensionless construction
yields a magnitude. The NEW move is not to breach it but to notice what
is left: RATIOS OF PHENOMENA are dimensionless, hence in-scope. Nature's
candidate rulers (the Rydberg, the Compton frequency, the Bohr length,
the Hartree, the Cs tick) are not independent magnitudes — they form a
WEB whose links are pure powers of alpha and closure coefficients (2pi,
4pi). Every forced link is a rung; the ladder IS the bridge. A magnitude
question then decomposes as (forced phenomenon ratio) x (one convention
naming the reference phenomenon) — and the 2019 SI is the world's own
stated plainly: every unit is now DEFINED by counting a phenomenon and
fixing exchange-rate constants.

FLOAT LAYER 🟡: CODATA-2018 values below are memory-sourced; the
identities are pinned as RATIOS with 1e-6 bands so late-digit drift is
harmless. The identities themselves are definition-level in QED.
"""

import math

# CODATA 2018 (memory-sourced float layer — see module docstring)
ALPHA = 7.2973525693e-3          # fine-structure constant
RYDBERG = 10973731.568160        # R_inf, m^-1
C = 299792458.0                  # m/s (exact, SI)
H = 6.62607015e-34               # J s (exact, SI)
M_E = 9.1093837015e-31           # kg
BOHR = 5.29177210903e-11         # a_0, m
HARTREE = 4.3597447222071e-18    # E_h, J

# The 2019 SI: every unit = a counted phenomenon + fixed exchange rates.
SI_FIXED = ("delta_nu_Cs", "c", "h", "e", "k_B", "N_A", "K_cd")


def rydberg_over_compton() -> float:
    """R_inf / (m_e c / h) = alpha^2 / 2: the spectroscopic ruler and
    the mechanical (Compton) ruler interconvert through alpha alone."""
    return RYDBERG / (M_E * C / H)


def bohr_times_rydberg() -> float:
    """a_0 * R_inf = alpha / (4 pi): the atomic length and the
    spectroscopic ruler — an alpha link carrying the flux closure."""
    return BOHR * RYDBERG


def hartree_over_rest_energy() -> float:
    """E_h / (m_e c^2) = alpha^2: the chemical energy ruler is the
    rest-energy ruler scaled by two powers of alpha."""
    return HARTREE / (M_E * C * C)


def ruler_web() -> dict:
    """The assembled ladder: each link = (measured ratio, forced form).
    All three rungs are pure alpha-powers times closure coefficients —
    no link needs a unit; the web is dimensionless throughout."""
    return {
        "rydberg/compton": (rydberg_over_compton(), ALPHA ** 2 / 2),
        "bohr*rydberg": (bohr_times_rydberg(), ALPHA / (4 * math.pi)),
        "hartree/rest": (hartree_over_rest_energy(), ALPHA ** 2),
    }


def si_ledger() -> dict:
    """The 2019 SI structure as data: unit -> (counted phenomenon,
    fixed exchange rates). Dimension-kinds = ledger-kinds; one fixed
    rate per ledger suffices, which is WHY seven constants close all
    seven units."""
    return {
        "second": ("count 9_192_631_770 Cs hyperfine ticks", ("delta_nu_Cs",)),
        "metre": ("addresses light crosses per tick", ("c", "delta_nu_Cs")),
        "kilogram": ("commitments per tick via h", ("h", "c", "delta_nu_Cs")),
        "ampere": ("elementary charges counted per second", ("e", "delta_nu_Cs")),
        "kelvin": ("mode-average bookkeeping via k_B", ("k_B", "h", "delta_nu_Cs")),
        "mole": ("entities counted", ("N_A",)),
        "candela": ("weighted photon count", ("K_cd", "h", "delta_nu_Cs")),
    }
