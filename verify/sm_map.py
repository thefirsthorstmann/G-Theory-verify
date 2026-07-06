"""sm_map.py — Stage 3b: the full Standard Model mapped from the engine.

Three layers, every cell provenance-tagged:
  CONTENT   — the 36-fermion roster (12 manifest neutrals + 24 charged
              vectors) and the carrier (boson) roster;
  WIRING    — the interaction graph (sm_wiring.py, 45/45);
  PARAMETERS— the banked dimensionless values (SM-BLOCK-REFERENCE.md).

Provenance tags:
  [banked]    predates today, citation given
  [assembled] built today from banked objects — carries an obligation, flagged
  [input]     taken from outside (owed machinery)
  [owed]      named gap, nothing supplied

Banked spine used here:
  * 36 fermions = 12 neutral + 24 charged = 3x12, from the +-18
    (OBJECTIVE-AND-POSITION.md:190; THE-INVENTORY.md:104 "Forced
    structural"; journal:209 "12 manifest neutrals #1-12 by gen x type,
    +- -> 24 charged = 36 total").
  * Ontology (this session, THE-BASIC-SCHEME.md): the OBSERVED particle
    is the manifest NEUTRAL resultant (a 9, on the Do-Sol axis); its
    matter/antimatter +- vector pair (the Fa/La 120/240 contacts)
    supplies the energy locally. The SM's 24 is the vector layer;
    the neutral 12 is what is seen.
  * Quark charge 2/3 = La (positional 240 = 2/3), 1/3 = Fa (120 = 1/3)
    (THE-FULL-POSITION:144 — "forced arithmetic with the role read").
  * Neutrinos = the upper sevenths {4/7, 5/7, 6/7}, sum 15/7
    (THE-FULL-POSITION:260).
  * Generations = the three round-up depths 3/4/5 with polarity +/n/-
    (11-METHODS-TECHNIQUES.md:68, T3; engine generation()).
  * Carriers: photon = 9, Higgs = 7, W/Z, gluons x8, graviton spin-2
    (journal:209, sketch); W/Z = the transform's two faces
    (sm_wiring.py R4, [assembled]).
  * Boson-2 / fermion-3 split (THE-INVENTORY.md:104, Forced structural).
"""

from fractions import Fraction as F

from gtheory import CHARGE_SIGN, generation

# ---------------------------------------------------------------------------
# CONTENT — the fermion roster
# ---------------------------------------------------------------------------
# per-generation manifest types: the SM flavor slots read by the framework
TYPES = {
    #  type        |q|          q-reading            colored  rounds provenance
    "up":     dict(q=F(2, 3),  reading="La 240 = 2/3", color=True,  rounds=True,
                   prov="banked (FULL-POSITION:144)"),
    "down":   dict(q=F(1, 3),  reading="Fa 120 = 1/3", color=True,  rounds=True,
                   prov="banked reading (Fa=1/3 positional); sign [assembled]"),
    "lepton": dict(q=F(1, 1),  reading="the unit (Do)", color=False, rounds=True,
                   prov="[assembled] unit-charge; forcing owed"),
    "nu":     dict(q=F(0, 1),  reading="the 9-axis (neutral)", color=False,
                   rounds=False,
                   prov="banked: upper sevenths {4/7,5/7,6/7} (FULL-POS:260); "
                        "unrounded [dia-flag: nu-mass reality open]"),
}

GEN_NAMES = {
    1: dict(up="u", down="d", lepton="e", nu="nu_e"),
    2: dict(up="c", down="s", lepton="mu", nu="nu_mu"),
    3: dict(up="t", down="b", lepton="tau", nu="nu_tau"),
}


def generation_polarity(g: int) -> str:
    """Generation = round-up depth 3/4/5 -> charge polarity +/n/-  [banked T3]."""
    return generation(g + 2)["charge"]          # depths 3,4,5


def manifest_roster() -> list:
    """The 12 manifest neutrals: 3 generations x 4 types  [banked count]."""
    out = []
    for g in (1, 2, 3):
        for t, spec in TYPES.items():
            out.append(dict(
                name=GEN_NAMES[g][t], gen=g, type=t,
                gen_polarity=generation_polarity(g),
                q=spec["q"], q_reading=spec["reading"],
                colored=spec["color"], rounds=spec["rounds"],
                prov=spec["prov"],
            ))
    return out


def full_roster() -> dict:
    """36 = 12 manifest neutrals + 24 charged vectors (the +- pairs).

    The +- pair of each manifest slot = the matter/antimatter vectors
    (+-40-degree displacement mirror, ARCHETYPAL-MAP; the +-18 engine
    object is their arithmetic source). [banked count; pair mechanics
    sketch-grade]"""
    manifest = manifest_roster()
    vectors = []
    for m in manifest:
        for sign in ("+", "-"):
            vectors.append(dict(name=f"{m['name']}({sign})",
                                base=m["name"], sign=sign))
    return {"manifest": manifest, "vectors": vectors,
            "total": len(manifest) + len(vectors)}


# ---------------------------------------------------------------------------
# CONTENT — the carrier (boson) roster
# ---------------------------------------------------------------------------
CARRIERS = {
    "A": dict(sm="photon",   framework="the 9-operator (neutral axis)",
              spin=1, prov="banked (journal:209)"),
    "H": dict(sm="Higgs",    framework="the 7-operator (rounding/mass)",
              spin=0, prov="banked (journal:209)"),
    "W": dict(sm="W+-",      framework="the transform's +-18 face "
                             "(carries its own flip-charge -> self-couples)",
              spin=1, prov="[assembled] from banked transform (sm_wiring R4)"),
    "Z": dict(sm="Z0",       framework="the transform's net-0 face "
                             "(carries nothing -> no self-loop)",
              spin=1, prov="[assembled] from banked transform (sm_wiring R4)"),
    "g": dict(sm="gluons x8", framework="the color carrier (x8 sketch)",
              spin=1, prov="[input] colored-set; color machinery owed"),
    "G": dict(sm="graviton", framework="spin-2, couples to everything "
                             "(existence itself; Theorem 0 face)",
              spin=2, prov="banked sketch (journal:209)"),
}

BOSON_FERMION_SPLIT = "bosons ride the 2-side, fermions the 3-side " \
                      "[banked Forced-structural, THE-INVENTORY:104]"

# ---------------------------------------------------------------------------
# PARAMETERS — the banked dimensionless layer (pointer + the short list)
# ---------------------------------------------------------------------------
PARAMETERS = {
    "alpha^-1":      dict(value="137 = 2^7+3^2 = 8*17+1; block 00729927",
                          grade="Striking (integer) / block ◆ arithmetic"),
    "sin2_thetaW":   dict(value="3/13", grade="Reading (scheme-muddied)"),
    "m_W/m_Z":       dict(value="sqrt(1 - 17/81 - 13/1000) = 0.8815",
                          grade="Striking (Class-2 live)"),
    "Koide Q":       dict(value="2/3 = La", grade="Striking (tightest)"),
    "PMNS th23":     dict(value="4/7", grade="Striking (sharpest pending bet)"),
    "PMNS th13":     dict(value="1/45", grade="Striking (pending)"),
    "PMNS th12":     dict(value="5/17", grade="Reading (soft)"),
    "Higgs lambda":  dict(value="2^9/(3^4*7^2) = 512/3969 = 0.12900",
                          grade="Striking (7-limit, prediction-first)"),
    "nu sum":        dict(value="15/7 = 2.142857...", grade="Forced sum; "
                          "identification read"),
    "muon m/e":      dict(value="206.768 (climb 24->768 + block 207)",
                          grade="Striking; climb ◆"),
    "proton m/e":    dict(value="1836 = 2^2*3^3*17 = 36*51",
                          grade="Striking; factorization ◆"),
}
PARAMETERS_REF = "catalog/SM-BLOCK-REFERENCE.md (full table with " \
                 "measured values, S/N gate, deviations)"

# ---------------------------------------------------------------------------
# The consistency observation (not a claim): anomaly-style charge sum
# ---------------------------------------------------------------------------
def charge_sums() -> dict:
    """Per-generation manifest charge sums, with and without the color x3.

    WITHOUT color: 2/3 - 1/3 - 1 + 0 = -2/3  (does not vanish)
    WITH color x3 on quarks: 3(2/3) - 3(1/3) - 1 + 0 = 0  (vanishes)
    -> the x3 the owed color machinery must supply is EXACTLY the factor
       consistency (anomaly cancellation) requires. [observation ◇]"""
    q = dict(up=F(2, 3), down=F(-1, 3), lepton=F(-1, 1), nu=F(0, 1))
    return {
        "without_color": q["up"] + q["down"] + q["lepton"] + q["nu"],
        "with_color": 3 * q["up"] + 3 * q["down"] + q["lepton"] + q["nu"],
    }


if __name__ == "__main__":
    r = full_roster()
    print(f"fermions: {len(r['manifest'])} manifest + {len(r['vectors'])} "
          f"vectors = {r['total']}")
    print("generation polarities:",
          {g: generation_polarity(g) for g in (1, 2, 3)})
    print("charge sums:", charge_sums())
    print("carriers:", {k: v["sm"] for k, v in CARRIERS.items()})
