"""rg_octave.py — Phase B1: the discrete RG as the clock's first application.

THE TICK APPLIED TO COUPLINGS: on-grid scale-step = the octave
(mu -> 2 mu), so a coupling's running is a change PER TICK:
    Delta(alpha^-1) per octave = b0 * ln2 / (2 pi)
The one-loop coefficient is FORCED (scheme-independent, banked):
    b0(QCD) = (11 N_c - 2 n_f) / 3
— the gauge part carries 11/3 per Casimir (the charge-thread eleven
over the vector three), the matter parts the triad-thirds 4/3, 2/3,
1/3; two-loop carries 34/3 = 2*17/3 (the spine). The exact fractions
live here; the comparison to measured runnings is the (clearly marked)
float layer, as with every measured-world comparison in this program.
"""

import math
from fractions import Fraction as F

GAUGE_PER_CASIMIR = F(11, 3)          # the forced 1-loop gauge coefficient
MATTER_THIRDS = (F(4, 3), F(2, 3), F(1, 3))
TWO_LOOP_SPINE = F(34, 3)             # = 2*17/3 (scheme-independent floor)


def b0(nc: int, nf: int) -> F:
    """(11 Nc - 2 nf)/3 — exact."""
    return F(11 * nc - 2 * nf, 3)


def octaves(mu_lo: float, mu_hi: float) -> float:
    return math.log2(mu_hi / mu_lo)


def run_alpha_inv(alpha_inv: float, n_octaves: float, b0_val: F) -> float:
    """alpha^-1 after running UP by n_octaves (down = negative)."""
    return alpha_inv + float(b0_val) * math.log(2) / (2 * math.pi) * n_octaves
