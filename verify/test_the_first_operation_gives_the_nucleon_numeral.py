"""The first operation gives the nucleon numeral: the base, both stations, and their depth
(28 October 2026; CC: "I'll take a swing 1 42 8 57, the 42 and the 57 essentially become vacant so
1 00 8 00"; "I think the step is that because its a process of decay in octaves alternating sides
24- 12- 6- 3"; "33 is the average of 42 and 24 and 66 is the average of 57 and 75"; "64 as the frame
makes perfect sense since it is one round of the binary sequence"; "I think its the average of Fa and
La is Sol is what does it").

Builds on: THE-ORIGIN-ON-DISCRETE-TERMS.md (the first operation 1|42|8|57 -> 1|24|8|75, equations
6-9; the three orders), THE-PROTON-AND-NEUTRON-MASSES-ON-DISCRETE-TERMS.md sections 6, 8 and 10 (the
base 100800 in parts per 10^5, the six-ladder stations 66 and 72 over 64, the partition 23/32, the
syntonic increment), GRAVITY-AS-TONAL-CENTER.md sections 4 and 6 (the shortfall theorem; the register
rule through seven; the ports 2a + b = 0 mod 6), THE-SEVENTH.md sections 3 and 4 (the two reads),
TONAL-FUNCTION-ON-DISCRETE-TERMS.md Theorem 3, test_the_two_integers_against_the_grammar_null.py
(the orbits {1}, {2,3}, {4}, {5,6} of the first operation), and the Build F note of the same day on
branch claude/compassionate-pasteur-f1306c (the Catalan pair forces the digit 8 and not the depth).

Pinned, all exact:
- The first operation fixes positions 1 and 4 of the reptend, the digits 1 and 8, and moves the two
  interior pairs. Vacating the moved pairs gives 100800, the proton record's base numeral, equal to
  1.008 = 126/125 with the unit at the first position; the depth, three, is the distance between the
  two fixed points, Midy's half-period (1 + 8 = 9).
- Of the fifteen non-empty projections onto subsets of the four orbits, exactly one lands in Build
  F's window [1.0075, 1.0085), and it is the fixed-point set. The orbit-mean projection gives 133866
  and misses; the unmoved numeral misses; of the four unit placements only 1.00800 lands.
- The neutron numeral 100866 is the skeleton with the generation pair at its own centre (the mean of
  57 and 75); the proton numeral 100728 is the skeleton less the stepped pole, 75 - 3. The reading
  pair stays vacant in both.
- Of the six blocks 1, 42, 8, 57, 24, 75, only 24 carries the full octave descent on whole numbers;
  its halving chain 24, 12, 6, 3 alternates digit roots 6, 3, 6, 3; the quantum 3 is Re's offset on
  the root (27 - 24) and the Re station of the descent (24/8). On 57 +- q, 75 +- q the octave depth
  picks 72 uniquely for q = 3 and for no other q from 1 to 9.
- 66 is the mean of 57 and 75, twice the mean of 42 and 24, and 15 + 51; 33 + 66 = 99; 66 is the
  unique fixed point of the pole exchange x -> 132 - x, under which 72 -> 60 = 57 + 3.
- The frame 64 = 7 * 9 + 1 is the first return of doubling to 1 in both moduli (the order of 2 mod 63
  is 6). The stations 64 + 2^k, k odd, on the six-ladder are {66, 72, 96}, the published six-ladder
  set, with digit roots 3, 9, 6; no 64 + 2^k is divisible by seven, since -1 is not a power of two
  mod 7.
- (64, 66, 72) * 3/2 = (96, 99, 108): the pair sum and the block total of the first operation are
  the stations at the dominant. 108/64 = 27/16, and the just sixth misses it by exactly 81/80. 96 is
  the only octave of the root 24 among the three stations.
- The fifth is the least-cost 3-smooth interval in (1, 2); the Seventh's ascending read (Do Do Sol Do
  Mi Sol) and descending read (Fa Fa Do Fa La Do) differ by exactly 6, octave-reduced 3/2.
- Sol is the arithmetic mean of Fa and La, and Sol^2/(Fa * La) = 81/80; 36^2 - 32*40 = 16;
  66^2 - 57*75 = 33^2 - 42*24 = 81, so 33^2 = 1008 + 81.
- Through seven, the frame is short by one comma and the stations by 3, 2 and 5 commas; 64 is the
  only port (2a + b = 0 mod 6) among the chain's numbers; 64/24 = 8/3, the subdominant an octave up.
- 1 - 18/64 = 23/32: the inherited first-operation displacement over the frame gives the registered
  partition, and the neutron, inheriting 0, keeps all. Of the five distinct values d/g for d in
  {9, 18, 36}, g in {32, 64, 128}, one is 23/32; the chain's pool of 25 numbers yields 592 distinct
  one-operation values in (0, 1), of which exactly one lies within three sigma of the measured
  0.7187506(585) -- about one in five by density, so the weight rests on the record's registration.
- The mirror x -> 99 - x returns 66 to its own octave class (33) and sends 72 out of it (27); the
  stations below 99 closed under the mirror up to octaves are {3, 11, 33, 66, 88, 96}.

Withdrawn the same day, kept on the record: the digit-root rule for the quantum (q = the poles'
shared root) gives 48 on the second pair, 42/24, and was replaced by the octave floor of 24; the
wording "the polar flip is -3" (the corpus defines the flip as x -> 9 - x and the flip of 75 is 24,
whose floor is 3); a first draft that read "0.000001 = 1/64" as a decimal error, when CC meant binary,
where it is exact; and the grade "the fifth is a selection", since both sides of the identity are
forced on their own.

READING, open (may or may not be physics in terms of our current understanding): the rest value of
the reptend under the first operation is its fixed-point part, and the two nucleons are the two
excitations of its generation pair -- the centre for the neutral station, the stepped pole for the
charged one. The identification of the skeleton with the archetypal nucleon in daltons is the
hypothesis of Units, section 13, stated there under two conventions: the rest value of a numeral is
its fixed-point part with the displaced positions at zero, and the first reptend digit is the unit.
"""
from fractions import Fraction as F
from itertools import combinations, product

from sympy import n_order

A = "142857"
B = "124875"
PERM = {i + 1: B.index(A[i]) + 1 for i in range(6)}
ORBITS = [(1,), (2, 3), (4,), (5, 6)]
BLOCKS = [1, 42, 8, 57, 24, 75]
SCALE = [F(1), F(9, 8), F(5, 4), F(4, 3), F(3, 2), F(5, 3), F(15, 8), F(2)]
WINDOW = (F("1.0075"), F("1.0085"))
MEAS, SIG = F("0.7187506"), F("0.0000585")          # proton record, section 8, 2022 table


def v2(n):
    return (n & -n).bit_length() - 1


def dr(n):
    return 1 + (n - 1) % 9


def skeleton(keep):
    pos = {p for o in keep for p in o}
    return "".join(A[i - 1] if i in pos else "0" for i in range(1, 7))


def in_window(v):
    return WINDOW[0] <= v < WINDOW[1]


def test_the_first_operation_fixes_the_unit_and_the_octave_digit():
    assert PERM == {1: 1, 2: 3, 3: 2, 4: 4, 5: 6, 6: 5}
    fixed = [i for i in PERM if PERM[i] == i]
    assert fixed == [1, 4] and [A[i - 1] for i in fixed] == ["1", "8"]
    assert int(A[0]) + int(A[3]) == 9 and 4 - 1 == 3 == 6 // 2


def test_the_skeleton_is_the_base_numeral_and_the_depth_is_midys_half_period():
    s = skeleton([(1,), (4,)])
    assert s == "100800"
    assert F(int(s), 10**5) == F(1008, 1000) == F(126, 125)
    assert 1008 == 28 * 36 and 100800 - 72 == 100728 and 100800 + 66 == 100866


def test_one_of_fifteen_projections_lands_and_it_is_the_fixed_point_set():
    hits = []
    for r in range(1, 5):
        for keep in combinations(ORBITS, r):
            if in_window(F(int(skeleton(keep)), 10**5)):
                hits.append(keep)
    assert hits == [((1,), (4,))]


def test_the_competitors_miss_and_the_orbit_mean_is_the_neutron():
    rey = "".join(str(F(sum(int(A[i - 1]) for i in o), len(o))) * len(o) for o in ORBITS)
    assert rey == "133866" and not in_window(F(133866, 10**5))
    assert not in_window(F(142857, 10**5))
    assert [c for c in ("0.100800", "1.00800", "10.0800", "100.800") if in_window(F(c))] == ["1.00800"]
    assert (57 + 75) // 2 == 66 and 100800 + 66 == 100866 and 100800 - (75 - 3) == 100728
    assert str(100866)[1:3] == "00" == str(100728)[1:3]
    assert str(100866)[4:6] == "66" and str(100728)[4:6] == "28" == str(100 - 72)


def test_the_quantum_is_the_octave_floor_of_the_only_integer_root():
    integer_roots = [b for b in BLOCKS if all((b * (r - 1)).denominator == 1 for r in SCALE)]
    assert integer_roots == [24]
    assert [n for n in range(1, 100) if all((n * (r - 1)).denominator == 1 for r in SCALE)] == [24, 48, 72, 96]
    chain = [24, 12, 6, 3]
    assert [dr(x) for x in chain] == [6, 3, 6, 3] and 24 * (F(9, 8) - 1) == 3 == 27 - 24
    for q in range(1, 10):
        c = [57 - q, 57 + q, 75 - q, 75 + q]
        top = max(map(v2, c))
        picked = [x for x in c if v2(x) == top]
        assert (picked == [72]) == (q == 3), q
    assert 72 == 75 - 3 == 3 * 24 and v2(72) == 3 and 72 >> 3 == 9


def test_the_neutron_is_the_mean_in_three_forms_and_the_fixed_point_of_the_pole_exchange():
    assert F(57 + 75, 2) == 66 == 2 * F(42 + 24, 2) == 15 + 51
    assert 57 - 42 == 15 and 75 - 24 == 51 and 33 + 66 == 99 == 42 + 57 == 24 + 75
    assert [x for x in range(133) if 132 - x == x] == [66] and 132 - 72 == 60 == 57 + 3


def test_the_frame_is_the_joint_closure_and_seven_never_divides_a_station():
    assert 64 == 7 * 9 + 1 and 64 % 7 == 1 == 64 % 9 and n_order(2, 63) == 6 == n_order(2, 9) == n_order(10, 7)
    ladder = [64 + 2**k for k in range(7) if (64 + 2**k) % 6 == 0]
    assert ladder == [66, 72, 96] == [s for s in range(66, 200, 6) if 64 % (s - 64) == 0]
    assert [dr(s) for s in ladder] == [3, 9, 6]
    assert {pow(2, k, 7) for k in range(300)} == {1, 2, 4} and all((64 + 2**k) % 7 for k in range(300))
    assert [F(s, 64) for s in ladder] == [F(33, 32), F(9, 8), F(3, 2)]


def test_the_invariants_are_the_stations_at_the_dominant():
    assert [x * F(3, 2) for x in (64, 66, 72)] == [96, 99, 108]
    assert 99 == 42 + 57 and 108 == 1 + 42 + 8 + 57
    assert F(108, 64) == F(27, 16) and F(27, 16) / F(5, 3) == F(81, 80) and F(99, 96) == F(33, 32) == F(66, 64)
    assert [s for s in (66, 72, 96) if F(s, 24).denominator == 1 and (s // 24) & (s // 24 - 1) == 0] == [96]
    assert F(108, 96) == F(9, 8) == F(27, 24) and F(64, 24) == 2 * F(4, 3) and F(4, 3) * F(3, 2) == 2


def test_the_fifth_is_the_least_cost_interval_and_the_sevenths_two_reads_differ_by_it():
    cands = sorted(
        ((abs(a) + abs(b), F(2)**a * F(3)**b) for a in range(-8, 9) for b in range(-5, 6)
         if b != 0 and 1 < F(2)**a * F(3)**b < 2),
        key=lambda t: (t[0], t[1]))
    assert [r for _, r in cands[:3]] == [F(3, 2), F(4, 3), F(9, 8)] and cands[0][0] == 2

    def up(x):
        while x >= 2:
            x /= 2
        return x

    def down(x):
        while x <= F(1, 2):
            x *= 2
        while x > 1:
            x /= 2
        return x

    names = {F(1): "Do", F(3, 2): "Sol", F(5, 4): "Mi", F(2, 3): "Fa", F(5, 6): "La"}
    assert [names[up(F(k))] for k in range(1, 7)] == ["Do", "Do", "Sol", "Do", "Mi", "Sol"]
    assert [names[down(F(k, 6))] for k in range(1, 7)] == ["Fa", "Fa", "Do", "Fa", "La", "Do"]
    assert F(1, F(1, 7)) / F(1, F(6, 7)) == 6 and up(F(6)) == F(3, 2)
    assert sorted(down(x * F(2, 3)) for x in (F(1), F(5, 4), F(3, 2))) == [F(2, 3), F(5, 6), F(1)]


def test_sol_is_the_mean_of_fa_and_la_and_the_comma_is_the_means_excess():
    assert (F(4, 3) + F(5, 3)) / 2 == F(3, 2) and F(3, 2)**2 / (F(4, 3) * F(5, 3)) == F(81, 80)
    assert (32 + 40) // 2 == 36 and 36**2 - 32 * 40 == 16 == 4**2 and F(36**2, 32 * 40) == F(81, 80)
    assert F(3, 2) / F(4, 3) == F(9, 8) and F(5, 3) / F(3, 2) == F(10, 9) and F(9, 8) / F(10, 9) == F(81, 80)
    assert 66**2 - 57 * 75 == 81 == 33**2 - 42 * 24 == 9**2 and 33**2 == 1008 + 81


def test_the_frame_alone_is_a_unit_residue_port_in_the_chain():
    short = {n: n % 7 for n in (64, 66, 72, 96, 99, 108, 24)}
    assert short == {64: 1, 66: 3, 72: 2, 96: 5, 99: 1, 108: 3, 24: 3}
    assert 64 - F(1, 10**6) == F("63.999999")

    def port(n):
        a = b = 0
        while n % 2 == 0:
            n //= 2
            a += 1
        while n % 3 == 0:
            n //= 3
            b += 1
        return n == 1 and (2 * a + b) % 6 == 0

    assert [n for n in (24, 64, 66, 72, 96, 99, 108) if port(n)] == [64]


def test_the_retention_rule_gives_the_partition_and_the_neutron_keeps_all():
    assert 1 - F(18, 64) == F(23, 32) and 1 - F(0, 64) == 1 and F(18, 64) == F(9, 32)
    family = {F(d, g) for d in (9, 18, 36) for g in (32, 64, 128)}
    assert len(family) == 5
    lo, hi = MEAS - 3 * SIG, MEAS + 3 * SIG
    assert [1 - r for r in family if lo <= 1 - r <= hi] == [F(23, 32)]
    pool = sorted({1, 42, 8, 57, 24, 75, 99, 108, 18, 9, 15, 51, 3, 64, 66, 72, 96, 33, 27, 32, 63, 36, 48, 12, 6})
    vals = set()
    for a, b in product(pool, pool):
        if b and 0 < F(a, b) < 1:
            vals.add(F(a, b))
    for a, b, c in product(pool, pool, pool):
        if c:
            for v in (F(a - b, c), F(a + b, c)):
                if 0 < v < 1:
                    vals.add(v)
    assert len(vals) == 592 and [v for v in vals if lo <= v <= hi] == [F(23, 32)]
    assert 0.2 < float(len(vals) * 6 * SIG) < 0.25


def test_the_mirror_criterion_and_the_withdrawn_digit_root_rule():
    def odd(n):
        while n % 2 == 0:
            n //= 2
        return n

    assert 99 - 66 == 33 and F(66, 33) == 2 and 99 - 72 == 27 and F(72, 27) == F(8, 3)
    assert [x for x in range(1, 99) if odd(x) == odd(99 - x)] == [3, 11, 33, 66, 88, 96]
    # the withdrawn rule, kept on the record: the shared digit root as the quantum
    assert dr(57) == dr(75) == 3 and dr(42) == dr(24) == 6
    c = [42 - 6, 42 + 6, 24 - 6, 24 + 6]
    assert [x for x in c if v2(x) == max(map(v2, c))] == [48]
