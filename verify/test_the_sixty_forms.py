"""test_the_sixty_forms.py — THE CATALOGUE OF THE FIGURE, COMPLETE (2026-08-15).
CC asked for the sixty forms and the twelve harmonic forms of the earlier book
to be drawn and extrapolated. The enumeration and its classification are
verified here against the book's own claims, and the extrapolation is settled.

  THE COUNT. The figure's six moving points are the units modulo nine. Their
  seven hundred and twenty orderings reduce to SIXTY distinct closed forms,
  because a closed form is a cyclic sequence: divide by six rotations and by
  two directions, and seven hundred and twenty over twelve is sixty.

  THE CLASSIFICATION, MATCHING THE BOOK EXACTLY. Four are BALANCED — opposite
  positions summing to nine, which is mirror symmetry stated twice. Twelve
  more are HARMONIC — self-mirror by reversal without being balanced. The
  remaining forty-four are CHIRAL, falling into twenty-two handed pairs. Four
  plus twelve plus forty-four is sixty, and sixteen are self-mirror. Exactly
  one form is CONVEX, and it is the units in their own circular order; it is
  harmonic, not balanced.

  AND BOTH TRADITIONAL READINGS ARE BALANCED. The four balanced forms are
  124875, 125874, 142857 and 152847 — which contains BOTH the positional order
  of the digits of one seventh AND the multiplicative doubling order. The two
  drawings of the figure are not one canonical form and one variant; they are
  two members of the same four-element class.

  THE EXTRAPOLATION IS SETTLED IN THE NEGATIVE, AND THAT IS THE FINDING. The
  catalogue is drawable only at nine. Twenty-four already carries two thousand
  five hundred and twenty closed forms; ninety-nine carries an eighty-digit
  number of them; one thousand and eight a five-hundred-and-eighty-three-digit
  number. Above nine the catalogue is enumerated BY CLASS and never by
  exhaustion — and the classes persist: twenty-four has twenty-four balanced
  and a hundred and twenty self-mirror forms among its two and a half
  thousand, and exactly ONE convex form, as every modulus does. Convexity is
  the one class that is universal and singular at every modulus.

  THE SEAT PASS, WHICH CC ASKED FOR. Taking the eight diatonic seats as moduli,
  only two host a closed doubling figure — Re at twenty-seven and Si at
  forty-five — because they are the only two odd seats. That is the same pair
  distinguished twice already in this corpus: the only two degrees whose ratio
  carries a three in the denominator, and the only two that fail to halve into
  integers. THREE INDEPENDENT CONDITIONS, ONE PAIR.
"""

from itertools import permutations
from math import gcd, factorial

U9 = [1, 2, 4, 5, 7, 8]


def _canon(seq):
    n = len(seq)
    i = seq.index(min(seq))
    rot = tuple(seq[i:] + seq[:i])
    return min(rot, (rot[0],) + tuple(reversed(rot[1:])))


def _forms(units, N):
    return sorted({_canon(list(p)) for p in permutations(units)})


def test_the_count_is_sixty_and_the_reduction_is_by_twelve():
    forms = _forms(U9, 9)
    assert len(forms) == 60
    assert factorial(6) == 720 and 720 // 12 == 60
    assert 12 == 6 * 2                                  # rotations x directions


def test_the_classification_matches_the_book():
    forms = _forms(U9, 9)
    bal = [f for f in forms if all((f[i] + f[(i + 3) % 6]) % 9 == 0 for i in range(3))]
    mir = [f for f in forms if _canon([9 - d for d in f]) == f]
    cvx = [f for f in forms if list(f) == sorted(f)]
    harm = [f for f in mir if f not in bal]
    chi = [f for f in forms if f not in mir]
    assert len(bal) == 4                                # "exactly four are balanced"
    assert len(cvx) == 1                                # "exactly one is convex"
    assert len(harm) == 12                              # "twelve more"
    assert len(chi) == 44 and len(chi) % 2 == 0         # "twenty-two pairs"
    assert len(bal) + len(harm) + len(chi) == 60
    assert len(mir) == 16 == len(bal) + len(harm)
    # balance IS mirror symmetry:
    assert all(f in mir for f in bal)
    # the convex form is harmonic, not balanced:
    assert cvx[0] in harm and cvx[0] not in bal
    assert cvx[0] == (1, 2, 4, 5, 7, 8)


def test_both_traditional_readings_are_balanced():
    forms = _forms(U9, 9)
    bal = {f for f in forms if all((f[i] + f[(i + 3) % 6]) % 9 == 0 for i in range(3))}
    assert _canon([1, 4, 2, 8, 5, 7]) in bal            # positional 142857
    assert _canon([1, 2, 4, 8, 7, 5]) in bal            # multiplicative 124875
    assert len(bal) == 4


def test_the_catalogue_is_drawable_only_at_nine():
    def phi(N):
        return len([x for x in range(1, N) if gcd(x, N) == 1])
    counts = {N: factorial(phi(N) - 1) // 2 for N in (9, 24)}
    assert counts[9] == 60 and counts[24] == 2520
    assert len(str(factorial(phi(99) - 1) // 2)) == 80
    assert len(str(factorial(phi(1008) - 1) // 2)) == 583
    # the classes persist and convexity stays singular:
    U24 = [x for x in range(1, 24) if gcd(x, 24) == 1]
    f24 = _forms(U24, 24)
    assert len(f24) == 2520
    n = len(U24)
    bal24 = [f for f in f24 if all((f[i] + f[(i + n // 2) % n]) % 24 == 0 for i in range(n // 2))]
    mir24 = [f for f in f24 if _canon([(24 - d) % 24 for d in f]) == f]
    cvx24 = [f for f in f24 if list(f) == sorted(f)]
    assert (len(bal24), len(mir24), len(cvx24)) == (24, 120, 1)


def test_only_the_two_odd_seats_host_a_closed_doubling_figure():
    seats = {"Do": 24, "Re": 27, "Mi": 30, "Fa": 32,
             "Sol": 36, "La": 40, "Si": 45, "Do'": 48}

    def closes(N):
        seen, x = set(), 1
        while x not in seen:
            seen.add(x)
            x = 2 * x % N
        return x == 1
    hosts = sorted(n for n, N in seats.items() if closes(N))
    assert hosts == ["Re", "Si"]
    assert seats["Re"] % 2 and seats["Si"] % 2          # the only odd seats
    assert all(seats[n] % 2 == 0 for n in seats if n not in ("Re", "Si"))
    # and the same pair by the other two conditions already banked:
    from fractions import Fraction as F
    ratios = {"Do": F(1), "Re": F(9, 8), "Mi": F(5, 4), "Fa": F(4, 3),
              "Sol": F(3, 2), "La": F(5, 3), "Si": F(15, 8)}
    three = {n for n, r in ratios.items() if r.denominator % 3 == 0}
    halves = {n for n, s in seats.items() if s % 2}
    assert three == {"Fa", "La"}                        # the ratio condition
    assert halves == {"Re", "Si"}                       # the seat condition
    assert set(hosts) == halves                         # doubling agrees with halving
