"""Supporting structure for "The Proton and Neutron Masses on Discrete
Terms" (2026): the pair algebra of the period-six cycle.  On each rotation
of 142857, the digit pairs at positions (2,3) and (5,6) form a complement
pair summing to 99; their differences, straight and reversed, generate a
finite spectrum whose step is the triangular number 28.  The same algebra
runs in the period of 1/137 and at the depth of the six-digit seats, where
it separates the proton's station from the neutron's — the asymmetry the
paper's Section 10 uses.  Everything here is exact and closed: the catalog
is finite, so any use of it can be checked against the whole.
"""

from fractions import Fraction as F

W = "142857"
ROTS = [W[i:] + W[:i] for i in range(6)]


def straddle(rot):
    p1, p2 = int(rot[1:3]), int(rot[4:6])
    r1, r2 = int(rot[1:3][::-1]), int(rot[4:6][::-1])
    return p1, p2, r1, r2, abs(p1 - p2), abs(r1 - r2)


def test_the_pair_table_reproduces_exactly():
    """The three rows of the pair table, reproduced digit for digit."""
    assert straddle("142857") == (42, 57, 24, 75, 15, 51)
    assert straddle("285714") == (85, 14, 58, 41, 71, 17)
    assert straddle("428571") == (28, 71, 82, 17, 43, 65)


def test_every_straddle_is_a_midy_pair():
    """Each straddle's pairs sum to 99, straight and reversed."""
    for rot in ROTS:
        p1, p2, r1, r2, _, _ = straddle(rot)
        assert p1 + p2 == 99 and r1 + r2 == 99


def test_the_wheel_pairs_are_fourteen_times_one_two_three():
    """The cycle's six adjacent pairs are 14, 28, 42 and their 99-complements."""
    pairs = {int((r + r)[i:i + 2]) for r in ROTS for i in range(6)}
    assert pairs == {14, 28, 42, 57, 71, 85}
    assert {min(p, 99 - p) for p in pairs} == {14, 28, 42}


def test_the_straight_spectrum_steps_by_the_carry_price():
    """The displacement spectrum {15, 43, 71} is an arithmetic progression with step 28 = T(7)."""
    spec = sorted({99 - 2 * p for p in (14, 28, 42)})
    assert spec == [15, 43, 71]
    assert spec[1] - spec[0] == spec[2] - spec[1] == 28          # T(7)


def test_the_reversed_spectrum_and_the_couple_gaps():
    """The reversed spectrum is {17, 51, 65}; the couple gaps are {36, -54, 22}."""
    assert sorted({abs(2 * int(str(p)[::-1]) - 99) for p in (14, 28, 42)}) == [17, 51, 65]
    gaps = [51 - 15, 17 - 71, 65 - 43]
    assert gaps == [36, -54, 22]                                 # 36 = T(8) is the first, of three


def test_the_137_period_runs_the_same_algebra():
    """The period of 1/137 is 00729927; its halves sum to 9999 and its internal couple (27, 72) has displacement 45 = T(9)."""
    s, r = "", 1
    for _ in range(16):
        r *= 10
        s += str(r // 137)
        r %= 137
    assert s[:8] == s[8:16] == "00729927"                        # period eight
    assert int(s[:4]) + int(s[4:8]) == 9999                      # Midy halves
    assert 27 + 72 == 99 and int("27"[::-1]) == 72               # the reversal couple
    assert abs(2 * 27 - 99) == 45 == 9 * 10 // 2                 # displacement = T(9)


def test_the_ratio_read_is_uniform_and_total():
    """Read as first-digit over second, the six members give two inversion couples and the interval pair (4/3, 6/5), whose product is 8/5 and whose quotient 10/9 sits a syntonic comma from 9/8."""
    read = {n: F(n // 10, n % 10) for n in (15, 51, 17, 71, 43, 65)}
    assert read[15] == 1 / read[51] and read[17] == 1 / read[71]  # two inversion couples
    assert read[43] == F(4, 3) and read[65] == F(6, 5)            # the interval couple
    assert read[43] * read[65] == F(8, 5)                         # the minor sixth
    assert read[43] / read[65] == F(10, 9)                        # the partner whole tone
    assert F(9, 8) / F(10, 9) == F(81, 80)                        # syntonic comma apart
    assert F(2, 7) == 1 / F(7, 2)                                 # 137's couple, same read


def test_the_routes_and_the_closed_product_table():
    """51 x 36 = 1836; the closed eighteen-member product table from which that value is one pick; the reversal-prime couple (17, 71)."""
    assert 51 * 36 == 1836                                       # one product of the closed table
    table = sorted({d * g for d in (15, 43, 71, 17, 51, 65) for g in (36, 54, 22)})
    assert len(table) == 18 and 1836 in table                    # one pick from eighteen
    for n in (17, 71):                                           # the emirp couple
        assert all(n % k for k in range(2, int(n ** 0.5) + 1))
    digits = {d for n in (15, 51, 17, 71, 43, 65) for d in divmod(n, 10)}
    assert digits == {1, 3, 4, 5, 6, 7}


# ── 2026-08-31, the machine at seat depth ────────────────────────────────────
# The same operations, unchanged, on the nine pre-named six-digit turn
# statements.  Bookkeeping vs content, held apart in the assertions' comments:
# neutron->66 and rest->36 read out their own written digits; proton->28, the
# alpha gap 1, floor->64, the mirror law, and the gap-niner law are the
# non-trivial outputs.

STATIONS = {"wheel": "142857", "proton": "100728", "neutron": "100866",
            "composite": "100797", "base": "100800", "alpha": "137036",
            "rest": "036000", "floor": "035999", "seatimg": "035998"}


def _m(s):
    P1, P2 = int(s[1:3]), int(s[4:6])
    r1, r2 = int(s[1:3][::-1]), int(s[4:6][::-1])
    return abs(P1 - P2), abs(r1 - r2), abs(r1 - r2) - abs(P1 - P2)


def test_the_seat_depth_table_is_pinned_entire():
    """The same operations on the nine six-digit stations, the full table pinned."""
    assert _m(STATIONS["wheel"]) == (15, 51, 36)
    assert _m(STATIONS["proton"]) == (28, 82, 54)
    assert _m(STATIONS["neutron"]) == (66, 66, 0)          # reads out its own digits
    assert _m(STATIONS["composite"]) == (97, 79, -18)
    assert _m(STATIONS["base"]) == (0, 0, 0)
    assert _m(STATIONS["alpha"]) == (1, 10, 9)
    assert _m(STATIONS["rest"]) == (36, 63, 27)            # the 36 reads its own digits; the 63 does not
    assert _m(STATIONS["floor"]) == (64, 46, -18)
    assert _m(STATIONS["seatimg"]) == (63, 36, -27)


def test_the_seat_algebra_runs_on_hundred_complements():
    """At seat depth the load-bearing pairs sum to 100: 72 with 28, and 36 with 64."""
    assert 72 + 28 == 100 and 28 == 7 * 8 // 2             # T(7)
    assert 36 + 64 == 100 and 64 == 2 ** 6                 # T(8) and the sixth octave
    assert _m(STATIONS["rest"])[0] + _m(STATIONS["floor"])[0] == 100


def test_the_alpha_seat_straddle_and_the_second_emirp():
    """137036's internal pairs are (37, 36), one unit apart; the reversal channel carries 73, the prime partner of 37."""
    assert int("137036"[1:3]) == 37 and int("137036"[4:6]) == 36
    assert 37 - 36 == 1
    for n in (37, 73):
        assert all(n % k for k in range(2, int(n ** 0.5) + 1))
    assert 142857 == 3 ** 3 * 11 * 13 * 37


def test_rest_and_the_seat_image_are_machine_mirrors():
    """The rest and seat-image stations exchange their couples with the gap changing sign; rest's couple is a 99-pair with ratio 7/4."""
    s, r = _m(STATIONS["rest"]), _m(STATIONS["seatimg"])
    assert (s[0], s[1], s[2]) == (r[1], r[0], -r[2])
    assert 36 + 63 == 99 and F(63, 36) == F(7, 4)
    assert abs(s[2]) == 27 == 3 ** 3


def test_every_seat_depth_gap_is_a_multiple_of_nine():
    """Every seat-depth gap is a multiple of nine; the cycle itself carries one exception, the 22."""
    for k in ("proton", "neutron", "composite", "base", "alpha",
              "rest", "floor", "seatimg"):
        assert _m(STATIONS[k])[2] % 9 == 0
    assert (65 - 43) % 9 != 0


def test_the_pn_reversal_asymmetry():
    """Section 10's asymmetry: the proton's pair reverses to a different pair (gap 54); the neutron's 66 is a palindrome with no play."""
    assert _m(STATIONS["proton"])[2] == 54 == 6 * 9
    assert _m(STATIONS["neutron"])[2] == 0
    assert str(66) == str(66)[::-1] and str(28) != str(28)[::-1]


# ── 2026-08-31, the scale-map fork ───────────────────────────────────────────

def test_the_interval_fork_table():
    """The interval correspondence, kept as an internal watch after the 2026-09-01 review pass: the paper offers no interval table as evidence, because the licensed set blankets the contested band at sub-bar spacing — the density fact is pinned below. The per-interval implications and each determination's nearest member remain bookkeeping."""
    mp, mn = 1.0072764665789, 1.00866491606
    drop_n = (1.008 - (mp + mn) / 2) / 1.008 * 1e6
    assert abs(drop_n - 29.0761) < 0.002
    pred = lambda r: 137 + 0.036 * (1 - drop_n / r * 1e-6)
    # the blend's survivors, inside CODATA-22's one sigma:
    for r in (5 / 4, 9 / 7):
        assert abs(pred(r) - 137.035999177) < 2.1e-8
    # each camp's champion, inside its own one sigma:
    assert abs(pred(4 / 3) - 137.035999206) < 1.1e-8      # Paris  -> 4/3 (Fa)
    assert abs(pred(10 / 9) - 137.035999046) < 2.7e-8     # Berkeley -> 10/9
    # and the fork discriminates: no interval satisfies two camps at once
    for r in (5 / 4, 9 / 7, 4 / 3, 10 / 9):
        inside = sum(abs(pred(r) - a) < u for a, u in
                     ((137.035999177, 2.1e-8), (137.035999206, 1.1e-8),
                      (137.035999046, 2.7e-8)))
        assert inside == 1
    # the density fact, pinned as a negative: 9/8 is a second server of the
    # caesium value, and the licensed set blankets the band at sub-bar
    # spacing — which is why no interval table is presented as evidence.
    import math
    assert abs(pred(9 / 8) - 137.035999046) < 2.7e-8
    def _s7(n):
        for q in (2, 3, 5, 7):
            while n % q == 0:
                n //= q
        return n == 1
    band = sorted({p / q for q in range(1, 65) for p in range(q, 2 * q)
                   if math.gcd(p, q) == 1 and _s7(p) and _s7(q)
                   and 10 / 9 <= p / q <= 4 / 3})
    preds = sorted(pred(r) for r in band)
    gaps = [b - a for a, b in zip(preds, preds[1:])]
    assert len(band) >= 20                                # the set blankets the band
    assert sum(g < 2.7e-8 for g in gaps) > 0.8 * len(gaps)  # sub-bar spacing throughout
