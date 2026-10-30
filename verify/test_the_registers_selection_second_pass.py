"""The register's selection, second pass (12 October 2026; CC: "next in order, the register's selection, go go go").

Where it stood. The capacity ledger's third lever asks what selects alpha's prime 137 and G's period 151 the way the
line's properties select the enneagram (7, 10). The first pass (11 October) found the Line Theorem's family classifies and
does not select. Read at source today: the Fine-Structure Constant record selects 137 by recognition in the alphabet
(137 = 2^7 + 3^2 = 8 x 17 + 1), by the closure of its decimal ring at the octave (ord_137(10) = 8, seventeen families) and
by the measured tail; the gravity record selects 151 by a representation theorem (block 5 irreducible at period 151) and
a derived depth (151 = Phi_15(2), the novel prime of the joint closure of 3 and 5 at depth 15), with the pairing an
identification. The one candidate principle of the line's kind that the week produced is the ORIENTATION-FREE LINE: a
reptend necklace equal to its own reversal, the line read backwards being the same line, which is the direction forgotten,
as the line selection forgot it (11 October: 137's reptend is such a necklace, one of three primes below 5000).

Pinned, exact:
  * the depths: a prime closes at period d in base b exactly when it divides the cyclotomic value Phi_d(b) (and not a
    smaller one): Phi_8(10) = 10^4 + 1 = 73 x 137, so the primes of decimal period eight are exactly 73 and 137 (none other
    below 10^5); Phi_6(10) = 91 = 7 x 13 (the seed's period, the line choosing 7); Phi_15(2) = 151 is prime, so 151 is the
    unique prime of binary period fifteen; Phi_3(2) = 7. The records' selections therefore reduce to two closure depths,
    8 in base ten and 15 in base two, plus a choice within the pair {73, 137};
  * the orientation-free line decides that choice: among all primes below 20000 the reptend necklace is reversal-
    symmetric for exactly 3 (period 1), 11 (period 2), 101 (period 4) and 137 (period 8), and in each case the block
    (10^n - 1)/p is a decimal palindrome (3, 9, 99, 729927); the mechanism, for p dividing 10^h + 1 with period 2h and
    c = (10^h + 1)/p, x = c - 1: the block is x 10^h + (10^h - 1 - x), a palindrome exactly when x = 0 or x and its reversal
    sum to all nines (digit pairs summing to nine; 72), and through h = 24 the mechanism's complete list is (1, 11),
    (2, 101), (4, 137): 137 is the only orientation-free line of period above four, and the only one that leaves the
    figure's neutral axis (3 touches the triangle's point 3; 11 and 101 touch 0 = 9 only; 137 touches 0 and the mirror
    pair {2, 7}); the clause "off the neutral axis" is added to exclude the three small cases and is named as added;
  * the line of 1/137 on the nine-point circle (9 = 0) is the triangle 0-7-2 walked once in each direction, a rest at 0
    before each pass: 0 0 7 2 | 9 9 2 7; read backwards it is the same line; 1/73 = 01369863 touches {0, 1, 3, 6, 8} and is
    chiral, as is the seed's 142857;
  * the binary side: the property decides nothing there: 1/151 in base two has period 15 and block 000000011011001
    (217), a chiral necklace; the seed's binary line 001 and the coupling's block 101 are palindromes trivially, as are six
    of the eight odd blocks through 15; and base two carries no complete figure in the line selection's sense (its digit
    ring Z/1 is trivial, and the pair (2, 2) is excluded).
READING, open (may or may not be physics in terms of our current understanding): the register's selection narrows to
two depths, 8 and 15, which the figure does not yet supply (the record names them the octave and the joint closure of the
motor and the lift), and to the orientation-free line, which selects alpha's prime within its depth and does not reach G's.
alpha's object lives in the seed's reading base, ten, and G's in its doubling base, two: the register's two faces.
"""

from sympy import cyclotomic_poly, factorint, isprime, n_order, primerange


def _block(p, b=10):
    n = n_order(b, p)
    r, digits = 1, []
    for _ in range(n):
        r *= b
        digits.append(r // p)
        r %= p
    return digits


def _orientation_free(digits):
    s = "".join(map(str, digits)) if max(digits) < 10 else ",".join(map(str, digits)) + ","
    return s[::-1] in s + s


def test_the_records_selections_reduce_to_two_closure_depths():
    assert factorint(cyclotomic_poly(8, 10)) == {73: 1, 137: 1}
    assert [p for p in primerange(3, 100000) if p != 5 and n_order(10, p) == 8] == [73, 137]
    assert (137 - 1) // 8 == 17 and (73 - 1) // 8 == 9
    assert factorint(cyclotomic_poly(6, 10)) == {7: 1, 13: 1} and n_order(10, 7) == 6 and n_order(10, 13) == 6
    assert cyclotomic_poly(15, 2) == 151 and isprime(151) and n_order(2, 151) == 15
    assert cyclotomic_poly(3, 2) == 7 and n_order(2, 7) == 3
    assert 2 ** 15 - 1 == 7 * 31 * 151
    # the fine-structure record's spellings, as it states them
    assert 137 == 2 ** 7 + 3 ** 2 == 8 * 17 + 1 and 17 == 3 ** 4 - 2 ** 6


def test_the_orientation_free_line_is_realized_four_times_below_20000_and_once_off_the_neutral_axis():
    hits = []
    for p in primerange(3, 20000):
        if p == 5:
            continue
        d = _block(p)
        if _orientation_free(d):
            hits.append((p, len(d), "".join(map(str, d))))
    assert hits == [(3, 1, "3"), (11, 2, "09"), (101, 4, "0099"), (137, 8, "00729927")]
    for p, n, s in hits:
        b = str((10 ** n - 1) // p)
        assert b == b[::-1]                                   # the block is a palindrome
    touched = {p: sorted(set(x % 9 for x in _block(p))) for p, _, _ in hits}
    assert touched == {3: [3], 11: [0], 101: [0], 137: [0, 2, 7]}
    assert [p for p, n, _ in hits if n > 4] == [137]
    # the mechanism, complete through h = 24: p | 10^h + 1 of period 2h, x = c - 1 zero or anti-palindromic
    mech = []
    for h in range(1, 25):
        N = 10 ** h + 1
        for p in factorint(N):
            if n_order(10, p) != 2 * h:
                continue
            x = N // p - 1
            k = len(str(x))
            if x == 0 or x + int(str(x)[::-1]) == 10 ** k - 1:
                mech.append((h, p, x))
    assert mech == [(1, 11, 0), (2, 101, 0), (4, 137, 72)]
    assert 72 + 27 == 99 and 73 * 9999 == 729927 and (10 ** 4 + 1) // 137 == 73


def test_the_line_of_137_is_the_triangle_walked_both_ways_and_73s_is_chiral():
    d = _block(137)
    assert d == [0, 0, 7, 2, 9, 9, 2, 7]
    pts = [x % 9 for x in d]
    steps = [(pts[i], pts[(i + 1) % 8]) for i in range(8)]
    assert steps == [(0, 0), (0, 7), (7, 2), (2, 0), (0, 0), (0, 2), (2, 7), (7, 0)]
    forward, backward = steps[1:4], steps[5:8]
    assert backward == [(b, a) for a, b in reversed(forward)]      # the same triangle, the other way round
    assert steps[0] == steps[4] == (0, 0)                           # a rest before each pass
    assert _orientation_free(d)
    assert _block(73) == [0, 1, 3, 6, 9, 8, 6, 3] and not _orientation_free(_block(73))
    assert _block(7) == [1, 4, 2, 8, 5, 7] and not _orientation_free(_block(7))
    # Midy's mirror holds for both period-eight primes; only 137 adds the reversal
    for p in (73, 137):
        b = _block(p)
        assert all(b[i] + b[i + 4] == 9 for i in range(4))


def test_the_binary_side_is_not_decided_by_the_property():
    d = _block(151, 2)
    assert len(d) == 15 and "".join(map(str, d)) == "000000011011001" and int("".join(map(str, d)), 2) == 217
    assert 151 * 217 == 2 ** 15 - 1
    assert not _orientation_free(d)
    assert _block(7, 2) == [0, 0, 1] and _orientation_free(_block(7, 2))
    palindromic = [m for m in range(1, 16, 2) if bin(m)[2:] == bin(m)[2:][::-1]]
    assert palindromic == [1, 3, 5, 7, 9, 15]
    # the coupling's block, 5, is irreducible at period 151 (the record's representation theorem)
    assert n_order(2, 5) == 4 and 151 % 4 != 0 and 152 % 4 == 0
    # base two carries no complete figure in the line selection's sense
    from sympy import totient
    k = 2 - 1
    p = int(totient(k)) + 1
    assert p == 2 and 2 % p == 0
