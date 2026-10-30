"""THE WHEEL-PAIR MACHINE — CC's diagram (2026-08-31) formalized, and CLOSED.

The object: on each rotation of 142857, take the digit pairs at positions
(2,3) and (5,6) — a Midy-conjugate straddle, so the two pairs sum to 99 —
and record the straight difference |P1 - P2| and the reversed difference
|rev(P1) - rev(P2)|.  CC's table (rows 1/7, 2/7, 3/7) is reproduced below and
is the COMPLETE machine: the wheel has only six adjacent digit pairs, and
99-complements collapse them to three, so the spectrum is finite and this file
is its entire catalog.  That closure is the numerology firewall: any future
"hit" must cite a row of a closed table whose base rates are computable.

THE FORCED SKELETON (exact, asserted):
  * the wheel's adjacent pairs are 14 x {1,2,3} and their 99-complements;
  * the straight displacement spectrum {15, 43, 71} = |2P - 99| is an
    arithmetic progression with step 28 = T(7): THE CARRY PRICE AT THE SEED
    RUNG IS THE QUANTUM OF THE WHEEL'S OWN DISPLACEMENT ALGEBRA;
  * the reversed spectrum is {17, 51, 65}; couple gaps {+36, -54, +22}, so
    CC's 51 - 15 = 36 = T(8) is the first couple's gap (one gap of three:
    the selection is stated, not hidden);
  * the 1/137 period 00729927 runs the SAME pair algebra: halves sum 9999,
    and its single internal couple (27, 72) is a reversal couple — like the
    wheel's — with displacement |2x27 - 99| = 45 = T(9), forced-unique within
    that period.  Three consecutive carry prices hold three offices:
    T(7) = 28 the wheel's step (forced), T(8) = 36 the first gap (selection),
    T(9) = 45 the 137-period displacement (forced within its period).

THE RATIO READ (CC's, applied uniformly — the firewall's condition): each
two-digit member "ab" as a/b gives {1/5, 5, 1/7, 7, 4/3, 6/5}: the fifth
harmonic with its inversion, THE SEED ITSELF with its inversion (the wheel
names 1/7 in its own spectrum), and the interval couple (4/3 the subdominant,
6/5 the minor third) whose product is 8/5 and whose quotient is 10/9 — the
partner whole tone of the proton seat's 9/8, one syntonic comma apart.  Under
the same read the 137 couple is (2/7, 7/2): the doubled seed — the same 2/7
that is the seat image's exact sub-turn content (test_the_turn_and_the_wheel).
Grade: the read is uniform and total, and stays a Reading.

ROUTES, graded: 51 x 36 = 1836 reaches the integer part of m_p/m_e — a NEW
ROUTE to a number the standing honesty correction grades STRIKING, and the
route itself picks one product from the closed 18-member table, so it is
selection-bearing until an op-forcing argument exists.  The emirp couple
(17, 71) is exact.  The spectrum's digit set is {1,3,4,5,6,7}: both triad
members present, no 2, 8, 9, 0.
"""

from fractions import Fraction as F

W = "142857"
ROTS = [W[i:] + W[:i] for i in range(6)]


def straddle(rot):
    p1, p2 = int(rot[1:3]), int(rot[4:6])
    r1, r2 = int(rot[1:3][::-1]), int(rot[4:6][::-1])
    return p1, p2, r1, r2, abs(p1 - p2), abs(r1 - r2)


def test_ccs_table_reproduces_exactly():
    assert straddle("142857") == (42, 57, 24, 75, 15, 51)
    assert straddle("285714") == (85, 14, 58, 41, 71, 17)
    assert straddle("428571") == (28, 71, 82, 17, 43, 65)


def test_every_straddle_is_a_midy_pair():
    for rot in ROTS:
        p1, p2, r1, r2, _, _ = straddle(rot)
        assert p1 + p2 == 99 and r1 + r2 == 99


def test_the_wheel_pairs_are_fourteen_times_one_two_three():
    pairs = {int((r + r)[i:i + 2]) for r in ROTS for i in range(6)}
    assert pairs == {14, 28, 42, 57, 71, 85}
    assert {min(p, 99 - p) for p in pairs} == {14, 28, 42}


def test_the_straight_spectrum_steps_by_the_carry_price():
    spec = sorted({99 - 2 * p for p in (14, 28, 42)})
    assert spec == [15, 43, 71]
    assert spec[1] - spec[0] == spec[2] - spec[1] == 28          # T(7)


def test_the_reversed_spectrum_and_the_couple_gaps():
    assert sorted({abs(2 * int(str(p)[::-1]) - 99) for p in (14, 28, 42)}) == [17, 51, 65]
    gaps = [51 - 15, 17 - 71, 65 - 43]
    assert gaps == [36, -54, 22]                                 # T(8) is the first, of three


def test_the_137_period_runs_the_same_algebra():
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
    read = {n: F(n // 10, n % 10) for n in (15, 51, 17, 71, 43, 65)}
    assert read[15] == 1 / read[51] and read[17] == 1 / read[71]  # two inversion couples
    assert read[43] == F(4, 3) and read[65] == F(6, 5)            # the interval couple
    assert read[43] * read[65] == F(8, 5)                         # the minor sixth
    assert read[43] / read[65] == F(10, 9)                        # the partner whole tone
    assert F(9, 8) / F(10, 9) == F(81, 80)                        # syntonic comma apart
    assert F(2, 7) == 1 / F(7, 2)                                 # 137's couple, same read


def test_the_routes_and_the_closed_product_table():
    assert 51 * 36 == 1836                                       # route to a Striking number
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
    assert _m(STATIONS["wheel"]) == (15, 51, 36)
    assert _m(STATIONS["proton"]) == (28, 82, 54)
    assert _m(STATIONS["neutron"]) == (66, 66, 0)          # bookkeeping: own digits
    assert _m(STATIONS["composite"]) == (97, 79, -18)
    assert _m(STATIONS["base"]) == (0, 0, 0)
    assert _m(STATIONS["alpha"]) == (1, 10, 9)
    assert _m(STATIONS["rest"]) == (36, 63, 27)            # 36 is bookkeeping; 63 is not
    assert _m(STATIONS["floor"]) == (64, 46, -18)
    assert _m(STATIONS["seatimg"]) == (63, 36, -27)


def test_the_seat_algebra_runs_on_hundred_complements():
    """The wheel's pairs sum to 99 (Midy, no carry); at seat depth the
    load-bearing pairs sum to 100 (with carry): the proton offset's
    carry-complement IS the carry price, and the tail block's IS the octave."""
    assert 72 + 28 == 100 and 28 == 7 * 8 // 2             # T(7)
    assert 36 + 64 == 100 and 64 == 2 ** 6                 # T(8) and the sixth octave
    assert _m(STATIONS["rest"])[0] + _m(STATIONS["floor"])[0] == 100


def test_the_alpha_seat_straddle_and_the_second_emirp():
    """137036's internal pairs are (37, 36): the reptend's hidden prime beside
    the carry price, one unit apart; the reversal channel carries 73 — the
    emirp partner of 37, as (17, 71) was the wheel's."""
    assert int("137036"[1:3]) == 37 and int("137036"[4:6]) == 36
    assert 37 - 36 == 1
    for n in (37, 73):
        assert all(n % k for k in range(2, int(n ** 0.5) + 1))
    assert 142857 == 3 ** 3 * 11 * 13 * 37


def test_rest_and_the_seat_image_are_machine_mirrors():
    """(36, 63, +27) against (63, 36, -27): the couple swaps and the gap flips
    sign, +-27 = 3^3.  Rest's couple is itself a Midy pair (sum 99) with ratio
    7/4 — the harmonic seventh, the banked rising form of the no-seat 3/4."""
    s, r = _m(STATIONS["rest"]), _m(STATIONS["seatimg"])
    assert (s[0], s[1], s[2]) == (r[1], r[0], -r[2])
    assert 36 + 63 == 99 and F(63, 36) == F(7, 4)
    assert abs(s[2]) == 27 == 3 ** 3


def test_every_seat_depth_gap_is_a_multiple_of_the_seal():
    """At seat depth the reversal channel is governed entirely by 9; the wheel
    itself carried one 9-breaker (the 22 of the (43,65) couple)."""
    for k in ("proton", "neutron", "composite", "base", "alpha",
              "rest", "floor", "seatimg"):
        assert _m(STATIONS[k])[2] % 9 == 0
    assert (65 - 43) % 9 != 0


def test_the_pn_reversal_asymmetry():
    """The machine's first proton/neutron distinction: the proton's couple has
    reversal-play (gap 54, six seals), the neutron's pair is a palindrome and
    has none.  Direction-consistent with the displacement family (the
    reversal-fixed seat displaces more).  MECHANISM LANGUAGE ONLY: no scale
    map from gap-play to offset-units exists, and no weld is claimed."""
    assert _m(STATIONS["proton"])[2] == 54 == 6 * 9
    assert _m(STATIONS["neutron"])[2] == 0
    assert str(66) == str(66)[::-1] and str(28) != str(28)[::-1]


# ── 2026-08-31, the scale-map fork ───────────────────────────────────────────

def test_the_interval_fork_table():
    """THE RELATIVE HALF OF THE SCALE MAP, registered as a fork.  The licensed
    commensuration is the ledger's own: drops as ppm of their own seats.  The
    razor nucleon drop (29.0761 ppm), transported by each pre-registered
    interval, yields a hard alpha^-1 prediction; the alpha war adjudicates the
    interval.  BASE-RATE HONESTY: ten candidates spaced ~0.5-1 ppm against
    targets with sigma ~0.5-0.8 ppm guarantees SOME interval fits any outcome
    -- the content is the registered correspondence, not any single fit.  As
    of CODATA-22: 5/4 and 9/7 are the blend's survivors; Paris's champion is
    4/3 (the machine's own 43, Fa, +0.8 sigma); Berkeley's is 10/9 (the
    machine's couple quotient, the minor tone, +0.4 sigma).  The machine's two
    native intervals each champion one war camp.  The absolute half of the map
    (integer seals -> offset units) remains open: its form is load x discharge
    with load = slip x cycle-count, and the missing number is the CYCLE COUNT
    since seating -- the development number.  No static closure exists (pinned
    null), and the two-point fit stays refused.

    PAPER STANCE (the 2026-09-01 board's density finding, pinned below): the
    licensed intervals blanket the war band at sub-bar spacing, so ANY
    outcome lands within a fraction of a sigma of some member — the fork
    stays an INTERNAL watch, presented in no paper as evidence, and the
    per-camp champions above are bookkeeping, not discrimination."""
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
    # the board's density finding, pinned as a negative: 9/8 is a SECOND
    # Berkeley server, and the licensed set blankets the band at sub-bar
    # spacing — which is WHY no interval table is evidence.
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
