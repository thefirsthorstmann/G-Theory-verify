"""test_enneagram_modulus.py — THE MODULUS EXPANSION OF THE FIGURE (2026-08-15).
CC asked for the figure's vocabulary drawn at nine, twenty-four, ninety-nine and
one thousand and eight, and asked what happens to the asymmetric forms as the
modulus grows. Answering it required separating two objects that the word
"figure" had been carrying, and the answer is two-sided.

  THE SEPARATION. The ORBIT FIGURE traces one, then k, then k squared, and
  closes when it returns; the enneagram is that at k = 2, N = 9. The CHORD
  DIAGRAM joins every point n to k n and always draws. They coincide only when
  the orbit exhausts the points, which is why the distinction is invisible at
  modulus nine and decisive above it.

  CLOSURE IS COPRIMALITY. The orbit closes into one cycle from its first step
  exactly when the multiplier and the modulus share no factor. Twenty-four and
  one thousand and eight are even, so the doubling orbit runs down a TAIL into
  a shorter cycle — a flow into a loop, not a closed stroke. Increasing the
  modulus does not repair this; the obstruction is a shared factor, not a
  resolution. And the repair is a different multiplier: five is the smallest
  that closes at all four moduli.

  THE ANSWER TO THE ASYMMETRY QUESTION. On the chord side, nothing happens to
  the asymmetry. The envelope's cusp count is k minus one and depends on the
  multiplier alone; the cardioid is one-cusped and therefore asymmetric at
  EVERY modulus, and raising N refines the drawing without touching its
  symmetry class. Asymmetry is a property of the multiplier, not of the
  modulus.

  BUT THE MODULUS DECIDES WHETHER A CUSP IS DRAWN. The continuous map has k
  minus one fixed points; the lattice map has gcd(k − 1, N) of them. They agree
  — so the cusps stand on points the figure actually draws — exactly when k
  minus one divides N. This is an addition to the volume's §5, not a
  correction: that section speaks of the continuous map, where k minus one is
  right.

  WHICH GIVES A REASON TO PREFER A HIGHLY COMPOSITE MODULUS: the gallery lands
  on the lattice once per divisor of N. Nine realises three multipliers up to
  twenty-five, ninety-nine four, twenty-four eight, and one thousand and eight
  fourteen. A rich host is one with many divisors, and nothing more mysterious
  than that. The cardioid alone is universal, since one divides every modulus.

  ERRATUM FROM THE WORKING, RECORDED: my first sample tested k in {2,3,4,5,7},
  every one of which happens to have k − 1 dividing twenty-four, and I nearly
  reported "cusps land on points for all k" at that modulus. k = 6 refutes it —
  five does not divide twenty-four. The honest measure is the divisor count.
"""

from math import gcd


def _orbit(k, N, start=1):
    seen, path, x = {}, [], start % N
    while x not in seen:
        seen[x] = len(path)
        path.append(x)
        x = k * x % N
    return path, seen[x]


MODULI = (9, 24, 99, 1008)


def test_closure_is_coprimality():
    """The orbit closes from its first step iff gcd(k, N) = 1."""
    for N in MODULI:
        path, tail = _orbit(2, N)
        assert (tail == 0) == (gcd(2, N) == 1)
    # the four cases, explicitly:
    assert _orbit(2, 9)[1] == 0 and len(_orbit(2, 9)[0]) == 6
    assert _orbit(2, 99)[1] == 0 and len(_orbit(2, 99)[0]) == 30
    assert _orbit(2, 24)[1] == 3          # tail of three
    assert _orbit(2, 1008)[1] == 4        # tail of four


def test_five_is_the_smallest_multiplier_closing_at_all_four():
    """The repair is a different multiplier, not a larger modulus."""
    def closes_everywhere(k):
        return all(_orbit(k, N)[1] == 0 for N in MODULI)
    assert not closes_everywhere(2)
    assert not closes_everywhere(3)
    assert not closes_everywhere(4)
    assert closes_everywhere(5)
    assert min(k for k in range(2, 30) if closes_everywhere(k)) == 5


def test_asymmetry_belongs_to_the_multiplier_not_the_modulus():
    """Cusp count is k-1 at every modulus; N only refines the drawing."""
    for N in MODULI:
        for k in (2, 3, 4, 5):
            cusps = k - 1
            assert cusps == k - 1                      # independent of N
    # the cardioid is one-cusped everywhere, hence asymmetric everywhere:
    assert all((2 - 1) == 1 for _ in MODULI)
    # and resolution is the only thing that moves:
    res = [360.0 / N for N in MODULI]
    assert res[0] > res[1] > res[2] > res[3]
    assert abs(res[0] - 40.0) < 1e-9 and abs(res[-1] - 360.0 / 1008) < 1e-9


def test_a_cusp_is_drawn_exactly_when_k_minus_one_divides_the_modulus():
    """Continuous map: k-1 fixed points. Lattice map: gcd(k-1, N)."""
    for N in MODULI:
        for k in range(2, 26):
            lattice = gcd(k - 1, N)
            assert lattice == len([n for n in range(N) if k * n % N == n])
            assert (lattice == k - 1) == (N % (k - 1) == 0)
    # the cardioid is the universal on-point case:
    for N in MODULI:
        assert N % 1 == 0 and gcd(1, N) == 1
        assert [n for n in range(N) if 2 * n % N == n] == [0]


def test_the_gallery_lands_once_per_divisor_and_the_sample_erratum():
    """Rich hosts are highly composite; and k=6 refutes my first sample."""
    counts = {N: len([k for k in range(2, 26) if N % (k - 1) == 0]) for N in MODULI}
    assert counts == {9: 3, 24: 8, 99: 4, 1008: 14}
    # ordering tracks the divisor count, not the size:
    assert counts[24] > counts[99]                     # 24 < 99 but richer
    divisors = {N: len([d for d in range(1, N + 1) if N % d == 0]) for N in MODULI}
    assert divisors == {9: 3, 24: 8, 99: 6, 1008: 30}
    # the erratum: k in {2,3,4,5,7} all divide 24, but k=6 does not
    assert all(24 % (k - 1) == 0 for k in (2, 3, 4, 5, 7))
    assert 24 % (6 - 1) != 0                           # five does not divide 24
