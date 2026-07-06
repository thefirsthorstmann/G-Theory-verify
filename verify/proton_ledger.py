"""proton_ledger.py — CC's catch (2026-07-03): the proton's five-thirds.

CC's sentence: 'even though the third doubles back to 1 at 360, it
consists of five total units of 1/3.' That IS the anatomy of the
nucleon axial charge in the SU(6) quark model — computed here exactly
from the wavefunction, no shortcut:

    |p up> = (1/sqrt18) [ 2(u+ u+ d-) - (u+ u- d+) - (u- u+ d+) + perms ]

    Delta u = 4/3,  Delta d = -1/3
    NET   = Delta u + Delta d = 1      (the spin: doubles back to 1)
    GROSS = |Delta u| + |Delta d| = 5/3  (five units of third)
    g_A   = Delta u - Delta d = 5/3    (signs oppose: the measurable
                                        axial charge IS the gross)

The proton wears the same (net 1 | gross 5/3) anatomy in BOTH conserved
ledgers: charge 2/3 + 2/3 - 1/3 (CC's 2005 genesis triangle, pp38-41)
and spin (4/3 - 1/3). The same (4|-1)/3 weights run the magnetic
moment: mu_p = (4 mu_u - mu_d)/3 -> mu_p/mu_n = -3/2, with mu_p = 1
and mu_n = -2/3 (positional La, negative) in quark-moment units.

The La-duality identity underneath: 5/3 = 1 + 2/3 — interval La = the
unit plus positional La; the doubling-back drops exactly one turn (the
carry). Honest note: net = 1 is the NAIVE-model statement; measured
quark-spin content is ~0.3 (the 'spin crisis' — the rest in gluon spin
and ORBITAL circulation), and measured g_A = 1.2754(13), whose seat is
UNDERDETERMINED on the lattice (33 rivals within 1 sigma at q <= 200).
"""

from fractions import Fraction as F
from itertools import permutations

UP, DOWN = 1, -1


def proton_terms():
    """The 9 terms of the mixed-symmetry spin-up proton: coefficient 2
    on the three orderings of {u+,u+,d-}, -1 on the six of {u+,u-,d+}."""
    t = {}
    for perm in set(permutations([("u", UP), ("u", UP), ("d", DOWN)])):
        t[perm] = 2
    for perm in set(permutations([("u", UP), ("u", DOWN), ("d", UP)])):
        t[perm] = -1
    return t


def delta_q(flavor: str) -> F:
    """Spin carried by a flavor: expectation of (#up - #down)."""
    t = proton_terms()
    norm = sum(c * c for c in t.values())
    return sum(F(c * c, norm) * sum(s for (fl, s) in st if fl == flavor)
               for st, c in t.items())


def ledger() -> dict:
    """The full five-thirds ledger, exact."""
    du, dd = delta_q("u"), delta_q("d")
    return {"du": du, "dd": dd, "net": du + dd,
            "gross": abs(du) + abs(dd), "g_A": du - dd}


def moments() -> dict:
    """mu_p, mu_n in quark-moment units (e_u = 2/3, e_d = -1/3 pattern),
    from the same wavefunction — the same (4|-1)/3 weights."""
    t = proton_terms()
    norm = sum(c * c for c in t.values())
    e = {"u": F(2, 3), "d": F(-1, 3)}
    mu_p = sum(F(c * c, norm) * sum(e[fl] * s for (fl, s) in st)
               for st, c in t.items())
    mu_n = sum(F(c * c, norm) * sum(e["d" if fl == "u" else "u"] * s
                                    for (fl, s) in st)
               for st, c in t.items())
    return {"mu_p": mu_p, "mu_n": mu_n, "ratio": mu_p / mu_n}


def charge_ledger() -> dict:
    """CC's 2005 triangle: the charge wears the same anatomy."""
    charges = (F(2, 3), F(2, 3), F(-1, 3))
    return {"net": sum(charges), "gross": sum(abs(q) for q in charges)}


def straight_twenty() -> dict:
    """La on the 12->24 octave: the integer just scale and the splits."""
    just = {"Do": F(1), "Re": F(9, 8), "Mi": F(5, 4), "Fa": F(4, 3),
            "Sol": F(3, 2), "La": F(5, 3), "Ti": F(15, 8), "Do2": F(2)}
    vals = {n: 12 * r for n, r in just.items()}
    ints = {n: v for n, v in vals.items() if v.denominator == 1}
    la = vals["La"]
    return {"la": la, "integers": ints,
            "non_integers": {n: v for n, v in vals.items()
                             if v.denominator != 1},
            "split": (la - 12, 24 - la),
            "position": (la - 12) / (24 - 12)}
