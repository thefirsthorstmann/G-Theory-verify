"""sm_wiring.py — Stage-3 gauntlet: the SM interaction graph from the engine.

TARGET: the wiring of the standard interactions diagram (SM incl. the
hypothetical graviton; plate: incoming/inspiration/"SM Interactions
Enneagrams?.png") — 9 nodes, 45 binary cells (36 pairs + 9 selfs).

HONESTY HEADER (read before scoring):
  * This is a RETRODICTION — the target is public knowledge. The audit
    is therefore about RULE PROVENANCE, not surprise:
      [banked]    the object predates today (citation given);
      [assembled] the mediator->domain mapping was assembled TODAY from
                  banked objects — it carries an obligation, and is flagged.
  * The colored-set {Q, g} is an INPUT (the framework's color machinery
    is thin/owed — named in THE-INVENTORY). Rule R3 is the weak joint.

THE RULES:
  R1 [banked] mass-is-rounding; never-round set = {photon, gluon,
      graviton}  (OBJECTIVE-AND-POSITION.md:197). Framework neutrinos
      held unrounded (angles forced, masses Scale-blocked) -> N does
      not couple to the rounding mediator.
  R2 [banked] the charge triad 3=+/6=-/9=n (THE-POSITION-REBUILD.md:184);
      photon = the 9-operator (journal:209) -> photon's domain = the
      EM-charged = {W, Q, L}; carries no charge itself.
  R3 [input]  colored set = {Q, g}; gluon mediates color and carries it.
  R4 [banked object / assembled domain] W and Z = the two faces of the
      transform (engine: transform() — the +-18 pair with net 0):
      W = the +-18 face — carries the flip-charge it mediates (self);
      Z = the net-0 face — carries nothing (no self). Domain of both =
      the weak (flip) sector: fermions + {W, Z, H} doublet/triplet
      partners (Z's own domain excludes Z itself: the net-0 face).
  R5 [banked] H = the rounding mediator (Higgs=7 operator, journal:209;
      mass-is-rounding R1): domain = whatever rounds = {Q, L, W, Z, H}.
  R6 [banked] graviton spin-2 = couples to everything that exists,
      including itself (journal:209 sketch; existence = Theorem 0 face).
  R7 [assembled] SELF-LOOP iff the mediator carries its own mediated
      charge: W(+-) yes, g(color) yes, H(rounds) yes, G(exists) yes;
      photon(9, no charge) no, Z(net-0) no.

Edge rule: for A != B, edge(A,B) iff B in domain(A) or A in domain(B).
Self rule: edge(A,A) iff A in domain(A).
"""

NODES = ("W", "Z", "A", "g", "H", "G", "Q", "L", "N")
#  W=W-boson  Z=Z0  A=photon  g=gluon  H=Higgs  G=graviton
#  Q=quarks(u,c,t,d,s,b)  L=charged leptons(e,mu,tau)  N=neutrinos

# --- the TARGET (the plate, as data) ---------------------------------------
TARGET_EDGES = {
    frozenset(p) for p in [
        # fermion--boson
        ("W", "Q"), ("W", "L"), ("W", "N"),
        ("Z", "Q"), ("Z", "L"), ("Z", "N"),
        ("A", "Q"), ("A", "L"),
        ("g", "Q"),
        ("H", "Q"), ("H", "L"),
        ("G", "Q"), ("G", "L"), ("G", "N"),
        # boson--boson
        ("W", "Z"), ("W", "A"), ("W", "H"),
        ("Z", "H"),
        ("G", "W"), ("G", "Z"), ("G", "A"), ("G", "g"), ("G", "H"),
    ]
} | {
    frozenset([x]) for x in ("W", "g", "H", "G")        # self-loops
}

# --- the FRAMEWORK domains (provenance in the docstring) --------------------
DOMAINS = {
    "A": {"W", "Q", "L"},                        # R2 [banked]
    "g": {"Q", "g"},                             # R3 [input]
    "W": {"Q", "L", "N", "W", "Z", "H"},         # R4 [assembled from banked]
    "Z": {"Q", "L", "N", "W", "H"},              # R4 (net-0: no Z itself)
    "H": {"Q", "L", "W", "Z", "H"},              # R5 [banked] (N unrounded)
    "G": set(NODES),                             # R6 [banked]
    "Q": set(), "L": set(), "N": set(),          # fermions mediate nothing
}

# which cells the [assembled]/[input] rules are responsible for
ASSEMBLED_CELLS = (
    {frozenset(p) for p in [("W", "Z"), ("W", "H"), ("Z", "H")]}  # EW pairs (R4)
    | {frozenset(["W"]), frozenset(["H"])}                        # W, H selfs (R7)
)
INPUT_CELLS = {frozenset(("g", "Q")), frozenset(["g"])}           # color (R3)


def predicted_edges(domains=None) -> set:
    dom = domains or DOMAINS
    out = set()
    for i, a in enumerate(NODES):
        for b in NODES[i:]:
            if a == b:
                if a in dom[a]:
                    out.add(frozenset([a]))
            elif b in dom[a] or a in dom[b]:
                out.add(frozenset((a, b)))
    return out


def score() -> dict:
    pred = predicted_edges()
    cells = [frozenset((a, b)) for i, a in enumerate(NODES)
             for b in NODES[i:]]                     # 45 cells
    right = [c for c in cells if (c in pred) == (c in TARGET_EDGES)]
    wrong = [c for c in cells if (c in pred) != (c in TARGET_EDGES)]
    banked_only_right = [c for c in right
                         if c not in ASSEMBLED_CELLS | INPUT_CELLS]
    return {
        "cells": len(cells),
        "right": len(right),
        "wrong": sorted(tuple(sorted(c)) for c in wrong),
        "assembled_cells": sorted(tuple(sorted(c)) for c in ASSEMBLED_CELLS),
        "input_cells": sorted(tuple(sorted(c)) for c in INPUT_CELLS),
        "banked_only_right": len(banked_only_right),
    }


if __name__ == "__main__":
    s = score()
    print(f"cells {s['cells']}  right {s['right']}  wrong {s['wrong']}")
    print(f"  of which [assembled-today] {s['assembled_cells']}")
    print(f"  and [input/owed: color]    {s['input_cells']}")
    print(f"  banked-machinery-only correct cells: {s['banked_only_right']}")
