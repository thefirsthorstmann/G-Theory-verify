"""gtheory.py — the G-Theory engine, Stage 0: FORM.

The basic scheme as executable, exact arithmetic. This file is the model;
prose (MATH-MODULE.md, THE-BASIC-SCHEME.md) is commentary on it.

DESIGN LAWS (from CC's concerns, 2026-07-02):
  1. EXACT ONLY — integers, Fraction, digit-blocks. No float in the core.
     No seated limits: .999999 is a VALUE (a digit-block), never "= 1".
  2. Dimensionless by construction. Ruler-borrowing, when it ever happens,
     is one explicit function, never implicit.
  3. Rules are defined ONCE, here, and applied mechanically.
  4. Every free move is a named CHOICE in the CHOICES registry below.
     Forced content never references a CHOICE. An empty relevant-CHOICE
     list is the answer to "where does X come from."
"""

from fractions import Fraction as F

# ---------------------------------------------------------------------------
# THE CHOICES REGISTRY — every selection the model makes, in one place.
# Each entry: name -> (value, why it is a choice / what would force it)
# ---------------------------------------------------------------------------
CHOICES = {
    "BASE": (10, "the decimal base; framework reads base-10 as the manifest "
                 "domain {2,5}; TRIAL 2026-07-03 (chosen_three.py): 10 is the "
                 "UNIQUE LEAST base carrying both load-bearing mechanisms — "
                 "b=1 mod 9 (the ennead lives in digit sums) AND ord_7(b)=6 "
                 "(the seed unrolls full); carriers are rare (10, 19, 73); "
                 "CONDITIONAL least action — the mechanism pair is the 2perp3 "
                 "thesis itself, circularity named and weighed"),
    "SEED_DIVISOR": (7, "the origin move divide-by-7; TRIAL 2026-07-03: 7 = "
                        "the least full-reptend prime in base 10 (3: period "
                        "1; 11: period 2; 13: half) — the first prime whose "
                        "division exhibits the COMPLETE period 6 = 2x3; the "
                        "full-reptend sequence opens {7, 17, ...}: seed "
                        "first, spine second"),
    "ROUNDING_RULE": ("half-up-at-depth",
                      "round-half-up at the stated depth; T3: the depth "
                      "carries the physics; truncate-vs-round is fixed here"),
    "SIDE_ASSIGNMENT": ("24:left/minus",
                        "the cascade alternation is forced (halving parity); "
                        "which side is called LEFT/minus is the orientation "
                        "choice; CC: determined by how the roots fall — open"),
    "RULER_RUNG": ("3D", "the one borrowed ruler enters at the third "
                   "register (T3 depth-3 = the first clean commitment, "
                   "x1001/1000 exact); owed since the engine's founding, "
                   "entered 2026-07-03"),
    "DEGREE_MAP": ("frac(ratio)*360",
                   "the tone-circle convention; positional (frac x 360), "
                   "banked; alternatives (log/cents circle) are a different "
                   "object, kept distinct per 06-LOG:393"),
}

# ---------------------------------------------------------------------------
# 0 · The frame
# ---------------------------------------------------------------------------
HEXAD = (1, 2, 4, 8, 7, 5)          # doubling orbit, units mod 9
TRIAD = (3, 6, 9)                    # the vector axis; never visited by x2
OPERATORS = frozenset({1, 4, 7})     # ≡ 1 (mod 3)
CARRIERS = frozenset({2, 5, 8})      # ≡ 2 (mod 3): round UP, imparting charge
CHARGES = frozenset({3, 6, 9})       # ≡ 0 (mod 3)
CHARGE_SIGN = {3: "+", 6: "-", 9: "n"}

FLOOR = "000001"                     # the bounds as digit-blocks (VALUES,
CEILING = "999999"                   # not limits) — floor + ceiling = 10^6


def dr(n: int) -> int:
    """Digital root (endpoint only — physics uses cascade())."""
    n = abs(int(n))
    return 9 if n % 9 == 0 and n != 0 else n % 9


def cascade(n: int) -> list:
    """T7 — digital-root cascade KEEPING EVERY STEP (never shortcut).

    Returns the full fall, e.g. cascade(75) = [75, 12, 3];
    cascade(24) = [24, 6]. Step-count = len - 1. The step-count
    asymmetry the endpoint hides IS the physics (charge sign)."""
    steps = [int(n)]
    while steps[-1] >= 10:
        steps.append(sum(int(c) for c in str(steps[-1])))
    return steps


def cascade_polarity(n: int) -> str:
    """Charge sign from the cascade endpoint (3=+, 6=-, 9=n)."""
    end = cascade(n)[-1]
    if end not in CHARGE_SIGN:
        raise ValueError(f"{n} does not fall to the charge triad")
    return CHARGE_SIGN[end]


def doubling_orbit(start: int = 1) -> list:
    """The hexad as the x2 (mod 9) orbit: 1,2,4,8,7,5."""
    orbit, x = [], start
    while x not in orbit:
        orbit.append(x)
        x = dr(2 * x)
    return orbit


def halving_order(start: int = 1) -> list:
    """The reverse wheel order (the descent direction): 1,5,7,8,4,2."""
    orb = doubling_orbit(start)
    return [orb[0]] + list(reversed(orb[1:]))


# ---------------------------------------------------------------------------
# I · The reptend and the first neutral operation (the transform)
# ---------------------------------------------------------------------------
def expansion_digits(num: int, den: int, k: int) -> str:
    """First k decimal digits of num/den by long division. EXACT."""
    num, out = num % den, []
    for _ in range(k):
        num *= 10
        out.append(str(num // den))
        num %= den
    return "".join(out)


def reptend(p: int = 7) -> str:
    """The full reptend of 1/p (period = ord_p(10)). reptend(7)='142857'."""
    seen, num, digits = {}, 1 % p, []
    while num and num not in seen:
        seen[num] = len(digits)
        num *= 10
        digits.append(str(num // p))
        num %= p
    return "".join(digits)


# the composites under the decimal: 142857 = (1)(42)(8)(57)
def composites(seq: str = "142857"):
    """Split root|pair|octave|pair: '142857' -> 1, 42, 8, 57."""
    return int(seq[0]), int(seq[1:3]), int(seq[3]), int(seq[4:6])


def transform(seq: str = "142857") -> dict:
    """First neutral operation: hold root+octave, reverse interior pairs.
    142857 -> 124875. Returns the full forced ledger."""
    r, a, o, b = composites(seq)          # 1, 42, 8, 57
    a2 = int(str(a)[::-1])                # 42 -> 24   (down, -18)
    b2 = int(str(b)[::-1])                # 57 -> 75   (up,   +18)
    out = f"{r}{a2}{o}{b2}"               # 124875
    return {
        "in": seq, "out": out,
        "down": (a, a2, a2 - a),          # (42, 24, -18)
        "up": (b, b2, b2 - b),            # (57, 75, +18)
        "net": (a2 - a) + (b2 - b),       # 0  — neutral
        "internal_15": b - a,             # 15
        "internal_51": b2 - a2,           # 51
        "sum_pre": a + b, "sum_post": a2 + b2,   # 99, 99
    }


# ---------------------------------------------------------------------------
# II · The cascade spiral (alternation) — see CHOICES["SIDE_ASSIGNMENT"]
# ---------------------------------------------------------------------------
def octave_spiral(top: int = 24) -> list:
    """Halving spiral to the vector floor: 24 -> 12 -> 6 -> 3.
    Sides alternate per octave (forced by halving parity); the absolute
    left/right naming is CHOICES['SIDE_ASSIGNMENT']."""
    steps, x = [top], top
    while x % 2 == 0 and x > 3:
        x //= 2
        steps.append(x)
    sides = ["L" if i % 2 == 0 else "R" for i in range(len(steps))]
    return list(zip(steps, sides))


# ---------------------------------------------------------------------------
# III · The bounce (second neutral operation) -> 1/137
# ---------------------------------------------------------------------------
def bounce(t: dict = None) -> dict:
    """Out +-18, back -+3, net +-15 = the internal difference itself.
    75 -> 72, 24 -> 27; assembles 00|72|99|27 = the 1/137 block."""
    t = t or transform()
    lo = t["down"][1] + 3                 # 24 -> 27
    hi = t["up"][1] - 3                   # 75 -> 72
    block = f"00{hi}{99}{lo}"             # 00729927
    return {
        "lo": lo, "hi": hi,
        "net_off_original": (t["down"][0] - lo, hi - t["up"][0]),  # (15, 15)
        "neutrals": hi + lo,              # 99
        "block": block,
        "fsc_check": expansion_digits(1, 137, 8),   # must equal block
    }


# ---------------------------------------------------------------------------
# IV · Rest frame, generations, and the rounding ladder
# ---------------------------------------------------------------------------
def c_rest() -> int:
    """3 x (10^8 - 1) — the rest form of c. 299999997 = 3^3·11·73·101·137."""
    return 3 * (10 ** 8 - 1)


def factorize(n: int) -> dict:
    f, d, n = {}, 2, int(n)
    while d * d <= n:
        while n % d == 0:
            f[d] = f.get(d, 0) + 1
            n //= d
        d += 1
    if n > 1:
        f[n] = f.get(n, 0) + 1
    return f


def round_at(x: F, k: int) -> F:
    """The framework rounding rule — half-up at depth k (T3;
    CHOICES['ROUNDING_RULE']). Non-invertible: the working face."""
    scaled = F(x) * 10 ** k
    ip = int(scaled)
    if scaled - ip >= F(1, 2):
        ip += 1
    return F(ip, 10 ** k)


def rounded_seventh(depth: int) -> F:
    """1/7 rounded (half-up) at `depth` digits — CHOICES['ROUNDING_RULE'].
    The rounded-up digit at depth 3/4/5 is the carrier 2/8/5 -> 3/9/6."""
    digs = expansion_digits(1, 7, depth + 1)
    trunc = int(digs[:depth])
    if int(digs[depth]) >= 5:
        trunc += 1
    return F(trunc, 10 ** depth)


def generation(depth: int, base: int = 1008) -> dict:
    """One generation of the rounding ladder: base x rounded(1/7, depth)."""
    r = rounded_seventh(depth)
    val = base * r
    excess = val - 144
    carrier = int(expansion_digits(1, 7, depth)[-1])      # 2, 8, 5
    lifted = carrier + 1                                   # 3, 9, 6
    return {"depth": depth, "value": val, "excess": excess,
            "carrier": carrier, "lifted": lifted,
            "charge": CHARGE_SIGN[lifted]}


# ---------------------------------------------------------------------------
# V · The tone circle (degree map) — CHOICES["DEGREE_MAP"]
# ---------------------------------------------------------------------------
def degree(ratio: F) -> F:
    """frac(ratio) x 360, exact."""
    fr = ratio - int(ratio)
    return fr * 360


CARDINALS = {  # the harmonic tetrad 4:5:6:7 quarters the circle — forced
    "Do": F(1, 1), "Mi": F(5, 4), "Sol": F(3, 2), "H7": F(7, 4),
}

ENNEA_POS = {v: 40 * i for i, v in enumerate([9, 1, 2, 3, 4, 5, 6, 7, 8])}


def chord_arc(a: int, b: int) -> int:
    """Clockwise arc (degrees) from lattice value a to b."""
    return (ENNEA_POS[b] - ENNEA_POS[a]) % 360


def chord_axis(a: int, b: int) -> F:
    """Direction of the perpendicular axis (arc midpoint) of chord a->b."""
    return F(ENNEA_POS[a] + F(chord_arc(a, b), 2), 1) % 360


# ---------------------------------------------------------------------------
# VII · Multiple scales riding one wheel — the muon composite
# ---------------------------------------------------------------------------
def wheel_scales() -> dict:
    """Ascending octaves from 24 ride the doubling order; the descending
    207-block rides the halving order. At wheel value 5 they meet: 206.768."""
    up_vals = [24 * 2 ** k for k in range(6)]            # 24..768
    up = dict(zip(doubling_orbit(), up_vals))            # value -> rung
    down_vals = [207 - k for k in range(6)]              # 207..202
    down = dict(zip(halving_order(), down_vals))
    meet = {v: (down[v], up[v]) for v in up}
    return {"up": up, "down": down, "meet": meet,
            "muon": f"{down[5]}.{up[5]}"}                # "206.768"


# ---------------------------------------------------------------------------
# Derivations-on-demand (the audit objects)
# ---------------------------------------------------------------------------
def derive_137() -> dict:
    """137 from the scheme, with the relevant CHOICE names attached.
    Three independent arrivals; the block arrival is the basic scheme's."""
    t = transform()
    b = bounce(t)
    return {
        "block_arrival": {"digits": b["block"], "equals_1_over_137":
                          b["block"] == b["fsc_check"]},
        "additive_identity": {"2^7 + 3^2": 2 ** 7 + 3 ** 2},
        "spine_identity": {"8*17 + 1": 8 * 17 + 1,
                           "17": 3 ** 4 - 2 ** 6},
        "c_rest_carries_137": 137 in factorize(c_rest()),
        "choices_touched": ["BASE", "SEED_DIVISOR"],
    }
