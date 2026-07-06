"""sevenths_harmonics.py — THE SEVENTH (satellite #4): the harmonic
scalar facts of Module 1, pinned exact.

Fact 1: the six k/7 are rotations of one six-digit string; 7 is the
        least full-period prime in base ten.
Fact 2: the first six harmonics octave-reduce to the pitch-class
        sequence Do Do Sol Do Mi Sol; the sevenths are their
        dimensionless LABEL SET (labels, not touch points — touching
        at 1/7 excites the seventh harmonic; the module's distinction
        is preserved strictly).
Fact 3: THE COLLAPSE — normalize the six sevenths by 6/7 (giving the
        six sixths) and octave-reduce into (1/2, 1]: exactly three
        pitch classes remain — Do {1, 1/2}, Fa {2/3}, La {5/6} — and
        Re, Mi, Sol, Si are never visited.
Fact 4: Midy (1836), credited not claimed.
"""

from fractions import Fraction as F

REPTEND = "142857"


def rotations():
    """The six sevenths' periods as rotations of one string."""
    out = []
    for k in range(1, 7):
        digits = ""
        r = k
        for _ in range(6):
            r *= 10
            digits += str(r // 7)
            r %= 7
        out.append(digits)
    return out


def full_period_primes_below(n):
    """Primes p < n with ord_p(10) = p - 1."""
    out = []
    for p in range(3, n):
        if p != 5 and all(p % d for d in range(2, p)):
            o, r = 1, 10 % p
            while r != 1:
                r = r * 10 % p
                o += 1
            if o == p - 1:
                out.append(p)
    return out


def octave_reduce(x: F) -> F:
    """Bring x into (1/2, 1] by powers of two."""
    while x > 1:
        x /= 2
    while x <= F(1, 2):
        x *= 2
    return x


HARMONIC_CLASSES = [octave_reduce(F(h)) for h in range(1, 7)]
# 1, 1, 3/2->3/4? no: frequency ratios reduce as 1,1,3/2... we reduce
# into (1/2,1] on STRING-length convention; pitch-class names below
PITCH = {F(1): "Do", F(1, 2): "Do", F(2, 3): "Fa", F(5, 6): "La",
         F(3, 4): "Sol", F(5, 8): "Mi"}


def collapse():
    """Fact 3: normalized, octave-reduced sevenths -> {Do, Fa, La}."""
    normalized = [F(k, 7) / F(6, 7) for k in range(1, 7)]   # k/6
    reduced = [octave_reduce(x) for x in normalized]
    return reduced, sorted({PITCH[x] for x in reduced})
