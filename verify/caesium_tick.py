"""caesium_tick.py — THE TICK ITSELF (the SI second's manifest).

Taking the ruler-ratio ladder (bridge.py) all the way to the tick that
defines the second. Two results:

(1) THE HYDROGEN RUNG ◆(float): the 21-cm line — the cleanest
    phenomenon-ruler after the Rydberg — pinned in closed form:
      nu_H = (8/3) alpha^2 (g_e/2) g_p (m_e/m_p) R_inf c (1+m_e/m_p)^-3
    lands +56 ppm from measurement; the residue is NAMED (proton
    structure / Zemach ~ -40 ppm + higher QED). Every factor displayed:
    8/3 the closure coefficient, alpha^2 the block, 1836 the seat,
    g_p the pair-seat's partner, and g_e/2 whose excess over 1 IS
    alpha/2pi — the Coefficient Atlas's "one closure" signing the dress.

(2) THE SECOND'S MANIFEST: nu_Cs factors as
      4 x (8/3) alpha^2 (g_e/2) g_Cs (m_e/m_p) R_inf c x A_Cs
    with the atomic-structure factor A_Cs EXTRACTED = 12.23 and its
    Fermi-Segre ballpark (Z/n*^3 x F_rel ~ 11) shown. Closed form for
    A_Cs is REFUSED honestly (55-electron many-body + Bohr-Weisskopf).
    The tick = seated skeleton x two named composites (g_Cs, A_Cs)
    x one convention (the integer 9,192,631,770).

FLOAT LAYER (memory-sourced CODATA/measured values; ratios pinned
with bands sized to survive late-digit drift).
"""

import math

ALPHA = 7.2973525693e-3
RYD_C = 10973731.568160 * 299792458.0     # R_inf c, Hz
ME_MP = 1.0 / 1836.15267343
G_P = 5.5856946893                        # proton g-factor
G_E = 2.00231930436256                    # electron g-factor
NU_H = 1420405751.768                     # 21-cm line, Hz (measured)
NU_CS = 9192631770.0                      # the second (exact by convention)
G_CS = 2.582025 / 3.5                     # Cs-133: mu/I in nuclear magnetons
Z_CS, NSTAR_CS = 55.0, 6 - 4.131          # charge, 6s effective n (memory)


def hydrogen_21cm() -> float:
    """The closed-form skeleton of the 21-cm line."""
    return ((8 / 3) * ALPHA ** 2 * (G_E / 2) * G_P * ME_MP * RYD_C
            * (1 + ME_MP) ** -3)


def schwinger_dress() -> tuple:
    """g_e/2 - 1 vs alpha/2pi: the dress on the 21-cm rung is the
    one-closure coefficient in the act."""
    return G_E / 2 - 1, ALPHA / (2 * math.pi)


def caesium_skeleton() -> float:
    """The seated part of the tick: 4 (=I+1/2) times the hydrogen-form
    skeleton with caesium's nuclear g."""
    return 4 * (8 / 3) * ALPHA ** 2 * (G_E / 2) * G_CS * ME_MP * RYD_C


def atomic_factor() -> float:
    """A_Cs = nu_Cs / skeleton: everything the 55-electron atom adds.
    EXTRACTED, not derived — the honest composite."""
    return NU_CS / caesium_skeleton()


def fermi_segre_estimate() -> float:
    """Ballpark for A_Cs: Z/n*^3 times the relativistic (Casimir)
    s-state factor 1/(gamma(2 gamma - 1)), gamma = sqrt(1-(Z alpha)^2)."""
    gam = math.sqrt(1 - (Z_CS * ALPHA) ** 2)
    return Z_CS / NSTAR_CS ** 3 / (gam * (2 * gam - 1))


def manifest() -> dict:
    """The second, itemized: what is seated, what is composite, what
    is convention."""
    return {
        "seated": ("8/3 closure", "alpha^2 (the block)",
                   "m_e/m_p (the 1836 seat)", "g_e/2 (alpha/2pi dress)",
                   "R_inf c (the web's reference rung)"),
        "composite": ("g_Cs = 0.7377 (nuclear, measured)",
                      "A_Cs = 12.23 (many-body, extracted)",
                      "4 = I + 1/2 (nuclear spin 7/2)"),
        "convention": "the integer 9,192,631,770",
    }
