"""vanishing_point.py — pins for THE VANISHING POINT ON DISCRETE TERMS.

The stage objects: x_n = 1 - 10^-n (n nines after the point).

(1) THE FORM NEVER VARIES: the digital root of the n-nines numeral is 9
    at every stage; the digital root of 1 is 1; no stage crosses.
(2) THE STAIRCASE OF TONES: the gap ratio 1/x_n = 10^n/(10^n - 1) is
    EPIMORIC (superparticular, numerator = denominator + 1) at every
    stage — the first stair is 10/9, the minor whole tone — strictly
    descending toward unison and never reaching it.
(3) THE SHIFTED TAIL: at every stage, 10*x_n = 9 + x_{n-1} EXACTLY —
    not 9 + x_n. The folk proof's equation 10x = 9 + x holds only in
    the quotient; at every stage it misses by the last digit, 9*10^-n.
(4) THE VANISHING POINT: for every finite precision k, all stages
    n > k pass every k-precision test that 1 passes — indistinguishable
    from the seat, distinct at every stage by exactly 10^-n.
"""

from fractions import Fraction


def stage(n: int) -> Fraction:
    return 1 - Fraction(1, 10 ** n)


def digital_root(m: int) -> int:
    return 1 + (m - 1) % 9 if m else 0


def gap_ratio(n: int) -> Fraction:
    return 1 / stage(n)          # = 10^n / (10^n - 1)


def is_epimoric(q: Fraction) -> bool:
    return q.numerator - q.denominator == 1
