"""color.py — the color object: the triad circuit.

Source: CC's plate "Spin as 1? as 0deg? as 360deg?" (2026-07-02) + the
banked triad {3,6,9} and the La/Fa arc readings. Grade: [assembled] --
built today from banked objects; NOT yet forced. Promotion path: force
quarks-as-arc-riders from the 36-roster construction itself.

THE OBJECT. Color = position/motion on the triad circuit:
  * the three COLORS   = the triad vertices {3, 6, 9}
    (drawn as 3.33 / 6.66 / 9.99 — the never-seated thirds of 10);
  * a QUARK            = an arc-rider: up rides +2/3 (La, 240),
                         down rides -1/3 (Fa, 120, reversed);
  * an ANTIQUARK       = the counter-arc;
  * a GLUON            = a transition-rider between vertices:
                         3x3 pairings minus the 9->9 identity = 8;
  * an OBSERVABLE      = a CLOSED circuit (net turns integer).

THE TWO CLOSURE MODES (the plate's title question "0deg? 360deg?"):
  proton  uud: +2/3 +2/3 -1/3 = 1 -> closes at 360 (the octave face)
  neutron udd: +2/3 -1/3 -1/3 = 0 -> closes at 0   (the rest face)
Both closed, both observable. An open arc (a lone quark) is not a unit
and never stands alone -- confinement as the no-open-arc principle,
the same law as no-true-zero (a partial turn is not a place to stand).

WHAT THIS SUPPLIES (the three demands of THE-SM-MAP #6.1):
  (a) the x3 that closes the per-generation charge sum = the three legs;
  (b) the colored set {Q, g} = arc-riders + transition-riders (derived,
      no longer an input) -> the g-wiring cells;
  (c) the x8 of the gluons = 3^2 - 1.
"""

from fractions import Fraction as F

VERTICES = (3, 6, 9)                       # the colors (never-seated thirds)

ARC = {                                     # what each rider subtends
    "u": F(2, 3), "c": F(2, 3), "t": F(2, 3),        # La-arc riders
    "d": F(-1, 3), "s": F(-1, 3), "b": F(-1, 3),     # Fa-arc riders (reversed)
}


def anti(quark: str) -> F:
    return -ARC[quark]


def circuit(*legs) -> dict:
    """Compose arcs; closed iff net is an integer number of turns."""
    net = sum((ARC[q] if isinstance(q, str) else F(q)) for q in legs)
    return {"net": net, "degrees": net * 360,
            "closed": net.denominator == 1, "observable": net.denominator == 1}


def gluons() -> dict:
    """The transition-riders: ordered vertex pairs minus the identity
    singlet (the 9->9 / trace direction — the would-be colorless gluon)."""
    pairs = [(a, b) for a in VERTICES for b in VERTICES]
    return {"count": len(pairs) - 1, "excluded_singlet": "the identity/9-axis"}


def colored_set() -> set:
    """DERIVED (was [input] in sm_wiring): whatever rides the circuit."""
    return {"Q", "g"}                       # arc-riders + transition-riders


def charge_sum_with_legs() -> F:
    """The anomaly closure: sum the generation over the three legs."""
    return 3 * (F(2, 3) + F(-1, 3)) + F(-1) + 0    # = 0 exactly
