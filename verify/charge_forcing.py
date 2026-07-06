"""charge_forcing.py — Phase D1+D2: THE CHARGE TABLE IS FORCED.

The SM-MAP's owed cells 'lepton q = 1 forcing owed' and 'color x3
input' close together, because they are one linear system. Four
constraints, each a framework structure:

  (C1) CLOSURE — per generation the total charge vanishes:
           3 q_u + 3 q_d + q_e + q_nu = 0.
       Conservation lives on the workless face (A2, banked): a
       generation that did not close would leak charge per cascade
       cycle. In the SM literature this is anomaly cancellation —
       cited honestly; here it is the M-face closure corollary.
  (C2) THE UNIT STEP — weak partners differ by exactly the unit:
           q_u - q_d = 1  and  q_nu - q_e = 1.
       The W is the transform's +-18 face: one flip = one unit of
       charge moved (the two-faces identification, braced).
  (C3) THE AXIS — the neutrino sits on the neutral 9-axis (banked):
           q_nu = 0.
  (C4) THE TRIAD — quarks carry multiplicity 3, leptons 1.
       The single remaining INPUT — braced by C_A = 3 and the gluon
       count 3^2 - 1 = 8 = the ring (THE-FIRST-RUNG, same day).

THEOREM. Under (C1)-(C4) the charge assignment of a generation is
UNIQUE: q_u = 2/3, q_d = -1/3, q_e = -1, q_nu = 0. The forced values
land exactly on the banked tone readings (La = 2/3, Fa = 1/3 in
magnitude) and force the corollaries: proton uud = +1, neutron
udd = 0, HYDROGEN p + e = 0 exactly — atomic neutrality is not an
accident of nature but a consequence of closure. The proton's ledger
then wears the banked anatomy: net 1, gross 5/3 (proton_ledger.py).

The map's remaining owed input is ONE object: the x3 itself.
"""

from fractions import Fraction as F


def solve_charges(triad: int = 3):
    """Solve (C1)-(C4) exactly. Returns dict of the unique solution."""
    # C3: q_nu = 0; C2: q_e = q_nu - 1 = -1
    q_nu = F(0)
    q_e = q_nu - 1
    # C2: q_u = q_d + 1; C1: triad*(q_u + q_d) + q_e + q_nu = 0
    #  -> triad*(2 q_d + 1) - 1 = 0
    q_d = (1 - triad) / F(2 * triad)
    q_u = q_d + 1
    return {"u": q_u, "d": q_d, "e": q_e, "nu": q_nu}


def closure_residual(q: dict, triad: int = 3) -> F:
    """The generation sum — zero iff closed."""
    return triad * (q["u"] + q["d"]) + q["e"] + q["nu"]


def composites(q: dict) -> dict:
    """The forced corollaries."""
    proton = 2 * q["u"] + q["d"]
    neutron = q["u"] + 2 * q["d"]
    return {"proton": proton, "neutron": neutron,
            "hydrogen": proton + q["e"],
            "proton_gross": 2 * abs(q["u"]) + abs(q["d"])}


def uniqueness_scan(lo: int = 1, hi: int = 12) -> dict:
    """The triad input is the ONLY multiplicity giving third-integer
    charges landing on the banked tones; scan the alternatives."""
    out = {}
    for m in range(lo, hi + 1):
        q = solve_charges(m)
        out[m] = (q["u"], q["d"])
    return out
