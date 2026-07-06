"""vertex_rule.py — Phase D3: THE WIRING GENERATED, not assembled.

sm_wiring.py reproduced the 45-cell interaction graph from mediator
DOMAIN LISTS, three of them hand-assembled (R4, R5, R7). This module
replaces every list with one criterion and one attribute table:

  THE READING RULE:  edge(A, B)  iff  some leg READS a property the
                     other CARRIES.
  THE SELF RULE:     edge(X, X)  iff  X reads what X itself carries —
                     the self-reading criterion of THE-FIRST-RUNG
                     (banked same day: gapped <=> the carrier reads
                     itself), now generating the SM self-vertex column:
                     W (flip-charged) yes, g (colored) yes, H (massive)
                     yes, G (existent) yes; photon (chargeless) NO,
                     Z (the net-0 face) NO — the absence of the ZZZ
                     vertex, a real SM fact, falls out of net-0.

  PORTS (who reads what — each banked):
    photon -> electric   [the 9-operator, banked]
    W, Z   -> flip       [the transform's two faces, banked objects]
    g      -> color      [the one input, same as the content layer]
    H      -> rounds     [mass-is-rounding, banked]
    G      -> exists     [spin-2 existence, banked]
    fermions read nothing [fermions mediate nothing, banked]

  ATTRIBUTES (who carries what — each banked/forced):
    electric: W, Q, L         [THE-FORCED-TABLE: the forced charges]
    flip:     W, Q, L, N      [the doublets + the +-18 face; Z net-0]
    color:    g, Q            [the x3 input]
    rounds:   W, Z, H, Q, L   [never-round set = photon, g, G, N]
    exists:   everything      [Theorem-0 face]

One criterion, one table, zero case-lists. The generator's output is
tested cell-for-cell against the banked TARGET_EDGES (the plate).
Removing the color attribute removes exactly the two [input] cells —
the wiring layer, like the content layer, owes exactly one object.
"""

NODES = ("W", "Z", "A", "g", "H", "G", "Q", "L", "N")

CARRIES = {
    "electric": {"W", "Q", "L"},
    "flip": {"W", "Q", "L", "N"},
    "color": {"g", "Q"},
    "rounds": {"W", "Z", "H", "Q", "L"},
    "exists": set(NODES),
}

READS = {
    "A": "electric",
    "W": "flip",
    "Z": "flip",
    "g": "color",
    "H": "rounds",
    "G": "exists",
    "Q": None, "L": None, "N": None,
}


def reads_other(a: str, b: str) -> bool:
    """Does a read a property b carries?"""
    prop = READS.get(a)
    return prop is not None and b in CARRIES[prop]


def generate_edges() -> set:
    """The whole 45-cell wiring from the reading rule + self rule."""
    edges = set()
    for i, a in enumerate(NODES):
        for b in NODES[i:]:
            if a == b:
                if reads_other(a, a):
                    edges.add(frozenset([a]))
            elif reads_other(a, b) or reads_other(b, a):
                edges.add(frozenset([a, b]))
    return edges


def generate_without(prop: str) -> set:
    """The wiring with one attribute deleted — for input isolation."""
    saved = CARRIES[prop]
    CARRIES[prop] = set()
    try:
        return generate_edges()
    finally:
        CARRIES[prop] = saved
