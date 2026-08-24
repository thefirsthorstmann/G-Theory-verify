"""test_the_fa_license.py — THE UNIFORM RULE AT EVERY STATION (2026-08-17).
The board's surviving attack on Movement I: Fa's 7.999999 was said to come
from a bespoke route (through 8/7) that would manufacture a comma for any
tone — Sol through 12/7 gives 11.999995 — so the uniqueness was called
bookkeeping. The answer is one rule applied identically to all eight
stations of the banked descent 24, 21, 16, 12, 8, 6, 3, 0, with a theorem
behind it: because 10⁶ ≡ 1 (mod 7), the through-seven route on station n
falls short by EXACTLY (n mod 7) commas. The trichotomy follows —
seven-divisible stations terminate with no reptend at all; stations at
residue 1 return the reptend and fall short by the comma itself;
everything else returns a multiple of the comma, which is not the comma.
In the descent exactly one non-unit station sits at residue 1: Fa = 8.
The license is the ladder's own — ord₇(2) = 3, so 2³ is where the
two-ladder returns to the wheel's unit — and for any 3-smooth station
2^a·3^b the condition closes to 2a + b ≡ 0 (mod 6). The rule FORBIDS: a
reptend comma claimed at Sol, La, Mi, Re, or Do is now a checkable error.
"""

from fractions import Fraction as F

DESCENT = [("Do", 24), ("Si", 21), ("La", 16), ("Sol", 12),
           ("Fa", 8), ("Mi", 6), ("Re", 3), ("Do", 0)]
PLACES = 6                      # the register's depth: ord₁₀(7) = 6


def through_seven(n, places=PLACES):
    """The route, defined once and applied to every station without
    amendment: divide by seven, truncate at the register's depth,
    multiply back by seven."""
    truncated = F(int(F(n, 7) * 10 ** places), 10 ** places)
    return truncated * 7


def test_the_shortfall_theorem():
    """Shortfall = (n mod 7) × 10⁻⁶ at every station, exactly — because
    10⁶ ≡ 1 (mod 7), so n·10⁶ ≡ n and the truncation remainder is
    (n mod 7)/7 of one unit in the last place."""
    assert pow(10, 6, 7) == 1
    for name, n in DESCENT:
        shortfall = (n - through_seven(n)) * 10 ** 6
        assert shortfall == n % 7, (name, n)


def test_the_descents_own_numbers_reproduce():
    """The three readings the record already carries, from the one rule:
    Fa 7.999999 (one comma), Sol 11.999995 (five), La 15.999998 (two)."""
    assert through_seven(8) == F(7999999, 10 ** 6)
    assert through_seven(12) == F(11999995, 10 ** 6)
    assert through_seven(16) == F(15999998, 10 ** 6)


def test_the_trichotomy_and_fas_uniqueness():
    """Three outcomes and no fourth: at residue 0 the seven divides and
    the route terminates — no reptend, no comma; at residue 1 the route
    returns the reptend short by exactly one comma; elsewhere it returns
    a multiple. Fa is the descent's only non-unit station at residue 1,
    so Fa alone carries the comma."""
    terminating = [n for _, n in DESCENT if n % 7 == 0]
    licensed = [n for _, n in DESCENT if n % 7 == 1]
    multiples = [n for _, n in DESCENT if n % 7 not in (0, 1)]
    assert terminating == [21, 0]                  # Si = 3·7, and the floor
    assert licensed == [8]                         # Fa, alone
    assert sorted(multiples) == [3, 6, 12, 16, 24]
    assert F(21, 7) == 3 and through_seven(21) == 21   # Si: exact, no dress
    for n in multiples:
        assert (n - through_seven(n)) * 10 ** 6 > 1    # a multiple, not the comma


def test_the_license_is_the_ladders_return():
    """ord₇(2) = 3: the two-ladder returns to the wheel's unit at 2³ = 8,
    which is Fa's seat — the route through 8/7 = 1 + 1/7 is the wheel
    arriving home carrying its own unit, not a chosen path. The ports
    recur every three octaves: 8, 64, 512."""
    assert min(k for k in range(1, 7) if pow(2, k, 7) == 1) == 3
    assert 2 ** 3 % 7 == 1
    for j in (3, 6, 9, 12):
        assert 2 ** j % 7 == 1                     # one port per three octaves
    assert min(k for k in range(1, 7) if pow(3, k, 7) == 1) == 6
    # the three-ladder returns only at depth six — the reptend's own period
    assert pow(10, 6, 7) == 1


def test_the_smooth_license_condition_closes():
    """The multiplicative group mod 7 is cyclic of order 6 with 2 ≡ 3²,
    so a 3-smooth station 2^a·3^b sits at residue 1 exactly when
    2a + b ≡ 0 (mod 6). Verified against residues for every 3-smooth
    station through the descent, and the condition names the next ports:
    36, 64, 162, 288, 512 — with 288 = 12·24 = 17² − 1, the bridge
    number, itself a port."""
    assert 2 % 7 == 3 ** 2 % 7
    smooth = sorted({2 ** a * 3 ** b for a in range(7) for b in range(5)
                     if 2 ** a * 3 ** b <= 24})
    for n in smooth:
        a = 0
        m = n
        while m % 2 == 0:
            m //= 2
            a += 1
        b = 0
        while m % 3 == 0:
            m //= 3
            b += 1
        assert ((2 * a + b) % 6 == 0) == (n % 7 == 1), n
    ports = [n for n in range(25, 600)
             if n % 7 == 1 and set(_factors(n)) <= {2, 3}]
    assert ports[:5] == [36, 64, 162, 288, 512]
    assert 288 == 12 * 24 == 17 ** 2 - 1


def _factors(n):
    out, m, d = [], n, 2
    while d * d <= m:
        while m % d == 0:
            out.append(d)
            m //= d
        d += 1
    if m > 1:
        out.append(m)
    return out


def test_the_own_ratio_route_never_yields_the_comma():
    """The second reading, applied uniformly: take each tone by its own
    ratio, truncate, multiply by the root. Fa falls short by eight
    commas, La by sixteen, and the halving stations by none — under this
    route no station yields the comma, at all. The comma belongs to the
    through-seven route and to Fa's residue, and to nothing else."""
    root = 24
    for ratio, n, expected in ((F(1, 3), 8, 8), (F(2, 3), 16, 16),
                               (F(1, 2), 12, 0), (F(1, 4), 6, 0)):
        truncated = F(int(ratio * 10 ** 6), 10 ** 6) * root
        assert (n - truncated) * 10 ** 6 == expected
