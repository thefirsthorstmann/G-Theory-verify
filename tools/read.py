#!/usr/bin/env python3
"""read.py — the operational reader: interpret ANY decimal into its component
hexad/triad aspects, mod-9 angle, harmonic function, polarity, neighbour
behaviour, and CHANGING LINES (the carriers), I-Ching style.

Usage:
    python3 tools/read.py 0.142857
    python3 tools/read.py 3.14159265

This is the STATIC layer (fully grounded in banked structure) plus the
identification of the changing lines. The exact TRANSFORM of a changing line
(what the number becomes) is a pinnable rule — see DYNAMICS below and
THE-OPERATIONAL-READER doc; the candidate shown is flagged, not asserted.

Grounding: THE-CLOCK-OBJECT (traversal 1,4,7 | 2,5,8 | 3,6,9 = operators |
carriers | poles) · Base-Camp §2.3 (hexad {1,2,4,5,7,8}=scalar/2-side/material;
triad {3,6,9}=vector/3-side/energetic; 1/7 lives entirely in the hexad) ·
the mod-9 circle (enneagram = Z/9Z) · the doubling orbit 1,2,4,8,7,5.
"""
import sys

# --- banked digit structure ------------------------------------------------
TRIAD     = {3, 6, 9}            # vector / energetic / 3-side
HEXAD     = {1, 2, 4, 5, 7, 8}   # scalar / material / 2-side (units of Z/9)
OPERATORS = {1, 4, 7}            # clock traversal, class 1 (mod 3) -- the REST digits (do not round)
CARRIERS  = {2, 5, 8}            # clock traversal, class 2 (mod 3) -- changing lines that CARRY
POLES     = {3, 6, 9}            # clock traversal, class 0 (mod 3), the triad -- energetic, ROTATE
MOVERS    = {2, 3, 5, 6, 8, 9}   # the rounding/energetic digits (carriers + poles). CC's rule:
#                                  "only 1's, 4's and 7's do not round" -> REST iff string subset of {1,4,7}
ORBIT     = [1, 2, 4, 8, 7, 5]   # doubling orbit (the sounding wheel of 1/7)
HEX_PLUS  = {1, 2, 4}            # expanding half of the orbit
HEX_MINUS = {8, 7, 5}           # folding half (Midy partners of +, each pair sums to 9)


def digit_class(d):
    if d == 0: return "void"
    if d in OPERATORS: return "operator"
    if d in CARRIERS:  return "CARRIER"      # the changing line
    return "pole"


def family(d):
    if d == 0: return "void"
    return "triad" if d in TRIAD else "hexad"


def angle(d):
    """mod-9 circle: 9 at top (0 deg, neutral), 40 deg per step. 3->120, 6->240."""
    return (d % 9) * 40


def polarity(d):
    if d == 3: return "+"          # pole +
    if d == 6: return "-"          # pole -
    if d in (0, 9): return "0"     # void / neutral pole
    if d in HEX_PLUS: return "+"   # expanding half of the orbit
    return "-"                     # folding half


def harmonic(d):
    if d == 0: return "rest/vacuum"
    if d in TRIAD: return "silent axis"                 # the 3-6-9 the wheel never sounds
    return f"sounding (wheel {ORBIT.index(d)})"          # position in the doubling orbit


def neighbour(a, b):
    """behaviour of a digit adjacent to the next -- CC's rules, grounded."""
    if a == b:
        if a == 9: return "neutral (two poles at rest -- nothing)"
        if a == 8: return "vacuum (between two octave-limits -- quantized zero)"
        if a == 0: return "void"
        return "resonance (equal, no gradient)"
    if a + b == 9: return "closure (Midy pair, sums to 9)"
    if a in CARRIERS or b in CARRIERS: return "carry (a changing line -- movement)"
    return "step (gradient)"


def split(num_str):
    num_str = num_str.strip().lstrip("+")
    if "." in num_str:
        ip, fp = num_str.split(".", 1)
    else:
        ip, fp = num_str, ""
    ip = [int(c) for c in ip if c.isdigit()]
    fp = [int(c) for c in fp if c.isdigit()]
    return ip, fp


def read(num_str):
    ip, fp = split(num_str)
    digits = fp if fp else ip           # the "string" is the fractional tail if present
    label = "fractional string" if fp else "integer string"
    print(f"\nreading {num_str!r}  ({label}: {''.join(map(str, digits))})\n")
    hdr = f"  {'pos':>3} {'d':>2}  {'class':<9}{'family':<7}{'angle':>5}  {'pol':<4}{'harmonic':<16}{'motion'}"
    print(hdr); print("  " + "-" * (len(hdr) - 2))
    motion = {"operator": "rest", "CARRIER": "carry", "pole": "rotate", "void": "-"}
    for i, d in enumerate(digits):
        print(f"  {i:>3} {d:>2}  {digit_class(d):<9}{family(d):<7}{angle(d):>4}d  {polarity(d):<4}{harmonic(d):<16}{motion[digit_class(d)]}")
    # neighbour line
    print("\n  neighbours:")
    for i in range(len(digits) - 1):
        a, b = digits[i], digits[i + 1]
        print(f"    {a}->{b}: {neighbour(a, b)}")
    # summary
    n = len(digits)
    movers = [i for i, d in enumerate(digits) if d in MOVERS]
    carriers = [i for i, d in enumerate(digits) if d in CARRIERS]
    triad = [i for i, d in enumerate(digits) if d in TRIAD]
    pol = sum(1 if polarity(d) == "+" else -1 if polarity(d) == "-" else 0 for d in digits)
    at_rest = all((d in OPERATORS or d == 0) for d in digits)
    print("\n  SUMMARY")
    print(f"    hexad/triad balance : {n - len(triad)} hexad (scalar) / {len(triad)} triad (vector)")
    print(f"    net polarity        : {pol:+d}")
    print(f"    rounding digits     : {len(movers)}/{n} in {{2,3,5,6,8,9}} at {movers}"
          f"   -> {'AT REST (only operators 1,4,7)' if at_rest else 'MOVES'}")
    print(f"    changing lines      : carriers {carriers} carry; poles rotate; operators rest")
    print(f"    'temperature'       : {len(movers)/n:.2f}  (rounding-digit density -- 0.00 = fully at rest)")
    # DYNAMICS -- candidate transform, FLAGGED, not asserted
    if not at_rest:
        moved = [str(_candidate_flip(d)) for d in digits]
        print(f"\n  DYNAMICS (candidate rule, TO BE PINNED -- Midy-flip each carrier 2<->7,5<->4,8<->1):")
        print(f"    {''.join(map(str, digits))}  ->  {''.join(moved)}   (the 'moved' string / next hexagram)")
    print()


def _candidate_flip(d):
    """CANDIDATE only: a changing line flips to its Midy partner (sum 9). Pin with CC."""
    return {2: 7, 5: 4, 8: 1}.get(d, d)


if __name__ == "__main__":
    for arg in (sys.argv[1:] or ["0.142857"]):
        read(arg)
