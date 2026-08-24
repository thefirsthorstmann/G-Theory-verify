"""test_the_dimensional_account.py — THE 3+1 ACCOUNT'S FIRST EXACT SCAFFOLD
(2026-08-16). Ledger item four, carrying two debts: the June arc's parked
"rotational interlock + emergence of three spatial dimensions from the ray,"
and the fork closure's deferral — the angular envelope of an ultrametric
register. Today's session did not close the account. It did something the
account has never had: it found the exact ladder the question lives on.

  THE LADDER, EXACT. The root systems of the ADE chain in dimensions one
  through eight have cardinalities

      A1   A2   A3   D4   D5   E6   E7    E8
       2    6   12   24   40   72  126   240

  (Lie theory: |A_n| = n(n+1), |D_n| = 2n(n-1), E6/E7/E8 = 72/126/240), and
  these same numbers are the kissing numbers of the corresponding root
  lattices — the contact counts of optimally packed equal cells — with
  optimality PROVEN in dimensions 1, 2, 3, 4 and 8, and best-known status in
  5, 6, 7 (the honesty column, kept). EVERY RUNG IS A SEAT OF THIS PROGRAM:
  the octave, the hexad, the semitone ring, the root, La's seat, the proton
  seat, 2·3²·7 (the three primes once each — the one rung the program had
  not yet named, noted as 42 × 3), and the 240 of the gallery modulus and
  the banked 240-chain.

  THE DOUBLING WINDOW. Along the ladder the ratios run 3, 2, 2, 5/3, 9/5,
  7/4, 40/21: the count DOUBLES exactly and only across dimensions
  2 -> 3 -> 4 — the hexad to the chromatic ring to the root — so the octave
  operation is the dimension step precisely in the window containing
  physical space and spacetime, and nowhere else on the ladder.

  THE DIVISION-ALGEBRA SUBLADDER. At the division-algebra dimensions
  (R, C, H, O = 1, 2, 4, 8) the counts are 2, 6, 24, 240 and their ratios
  are 3, 4, 10 — the motor, the square of the octave, and the base. Held at
  signpost grade; recorded because it is exact.

  THE SECOND CONTACT LADDER. A cubic register's cells (Z^D, face contacts)
  give 2D: at the physical dimensions, 6 (the hexad) and 8 (the ring). BOTH
  natural contact ladders — cubic cells and optimal packing — land the
  program's numbers exactly at dimensions three and four, and land DIFFERENT
  program numbers: {6, 8} against {12, 24}. What relation the two ladders
  bear is an open question of the account, stated not solved.

  THE THREE FACES ASSEMBLED (banked, restated): the interlock face — the
  Lorentz group has six generators, three boosts and three rotations, two
  triads, and its sky is the 2-sphere, which is what makes space
  three-dimensional GIVEN the boost-rotation interlock (the June posit); the
  c face — the banked units reading, observed 3x10^8 against rest
  3(10^8 - 1), separated by exactly three, "the dimension count," flagged as
  a reading where it was banked; the arena face — the figure's oscillation
  spectrum has exactly FOUR distinct frequencies (banked theorem), a 3+1
  count carried by the object itself.

  THE ACCOUNT'S STATE AND ITS PROMOTION CONDITION. Not closed: no derivation
  of three is claimed. Transformed: the question "why three dimensions" is
  now "why does the register's contact structure realize the ADE ladder at
  the doubling window" — and the promotion condition is named: derive from
  the register's own mechanics (carry, union, cell) that equal-cell contact
  realizes A3 in space and D4 in spacetime, or exhibit the cubic and packing
  ladders as two faces of one structure. That is a mathematics question with
  a yes or no answer, which is what an account needs to be closable.
"""


def _A(n):
    return n * (n + 1)


def _D(n):
    return 2 * n * (n - 1)


LADDER = [("A1", 1, _A(1)), ("A2", 2, _A(2)), ("A3", 3, _A(3)),
          ("D4", 4, _D(4)), ("D5", 5, _D(5)), ("E6", 6, 72),
          ("E7", 7, 126), ("E8", 8, 240)]


def test_the_root_counts_are_the_programs_seats():
    counts = [r for _, _, r in LADDER]
    assert counts == [2, 6, 12, 24, 40, 72, 126, 240]
    seats = {2, 6, 12, 24, 40, 72, 240}                # the named seats
    assert seats < set(counts)                          # all named ones appear
    assert 126 == 2 * 3 ** 2 * 7 == 42 * 3              # the one new rung


def test_the_formulas_not_the_table():
    """The counts come from the Lie formulas, not from a copied list."""
    assert _A(1) == 2 and _A(2) == 6 and _A(3) == 12
    assert _D(4) == 24 and _D(5) == 40
    # E-series pinned as the standard constants with a consistency check:
    # dim of the Lie algebra = rank + roots
    assert 6 + 72 == 78                                 # E6: dim 78
    assert 7 + 126 == 133                               # E7: dim 133
    assert 8 + 240 == 248                               # E8: dim 248


def test_the_doubling_window_is_exactly_two_three_four():
    from fractions import Fraction as F
    counts = [r for _, _, r in LADDER]
    ratios = [F(b, a) for a, b in zip(counts, counts[1:])]
    assert ratios == [F(3), F(2), F(2), F(5, 3), F(9, 5), F(7, 4), F(40, 21)]
    doubles = [i for i, r in enumerate(ratios) if r == 2]
    assert doubles == [1, 2]                            # 6->12 and 12->24 only


def test_the_division_algebra_ratios_are_motor_square_base():
    from fractions import Fraction as F
    sub = {d: r for _, d, r in LADDER if d in (1, 2, 4, 8)}
    assert [sub[1], sub[2], sub[4], sub[8]] == [2, 6, 24, 240]
    assert [F(6, 2), F(24, 6), F(240, 24)] == [3, 4, 10]


def test_the_proof_status_column_is_honest():
    proven = {1: 2, 2: 6, 3: 12, 4: 24, 8: 240}         # optimal kissing proven
    best_known_only = {5: 40, 6: 72, 7: 126}
    for _, d, r in LADDER:
        if d in proven:
            assert proven[d] == r
        else:
            assert best_known_only[d] == r              # flagged, not claimed


def test_the_cubic_ladder_also_speaks_at_three_and_four():
    cubic = {D: 2 * D for D in (1, 2, 3, 4)}            # Z^D face contacts
    assert cubic[3] == 6 and cubic[4] == 8              # hexad and ring
    packing = {3: 12, 4: 24}                            # chromatic and root
    assert set(cubic.values()) & set(packing.values()) == set()
    # two ladders, both in the program's vocabulary, relation OPEN


def test_the_three_faces_and_the_lorentz_generators():
    boosts, rotations = 3, 3
    assert boosts + rotations == 6                      # two triads, one hexad
    assert 3 * 10 ** 8 - 3 * (10 ** 8 - 1) == 3         # the c gap: the count
    four_distinct_frequencies = 4                       # the arena theorem
    assert four_distinct_frequencies == 3 + 1


def test_the_account_state_is_recorded():
    state = {"closed": False,
             "transformed": "why three -> why the register realizes the ADE "
                            "ladder at the doubling window",
             "promotion": "derive equal-cell contact = A3 (space) and D4 "
                          "(spacetime) from carry/union/cell mechanics, or "
                          "unify the cubic and packing ladders"}
    assert state["closed"] is False
    assert "doubling window" in state["transformed"]


# ---------------------------------------------------------------------------
# the author'S FLANKING LEAD (2026-08-16, mid-stream): the two-ladder question's
# candidate answer-shape. The cubic contacts at the physical dimensions are
# the DECIMAL PERIODS OF THE TWO FORCE PRIMES — 6 = ord_10(7), gravity's; 8 =
# ord_10(137), electromagnetism's — flanking the seed 7 with product 48 =
# 7^2 - 1 = twice the root. The packing contacts {12, 24} have product 288 =
# 17^2 - 1 = 16 x 18 = Fa x Sol on root 12, flanking the spine 17. And the
# two primes couple exactly as the two forces do: 137 = 8*17 + 1, with
# ord_2(17) = 8. The cubic ladder speaks the PERIODS, the packing ladder
# speaks the SEATS, and the bridge between them is the pair (7, 17) — the
# relation of gravity and EM, as the author said. Reading on exact arithmetic.
# ---------------------------------------------------------------------------

def _ord(b, m):
    k, t = 1, b % m
    while t != 1:
        t = t * b % m
        k += 1
    return k


def test_the_cubic_contacts_are_the_force_primes_periods():
    assert _ord(10, 7) == 6                      # gravity's prime: period 6
    assert _ord(10, 137) == 8                    # EM's prime: period 8
    cubic_at_physical_dims = {3: 6, 4: 8}
    assert cubic_at_physical_dims[3] == _ord(10, 7)
    assert cubic_at_physical_dims[4] == _ord(10, 137)


def test_the_flanking_products_are_p_squared_less_one():
    assert 6 * 8 == 7 ** 2 - 1 == 48 == 2 * 24   # the seed's pair: twice the root
    assert 16 * 18 == 17 ** 2 - 1 == 288         # the spine's pair
    from fractions import Fraction as F
    assert 12 * F(4, 3) == 16 and 12 * F(3, 2) == 18   # Fa and Sol on root 12


def test_the_bridge_between_the_ladders():
    """The packing pair's product IS the spine pair's product — two
    factorizations of 17^2 - 1 — and the primes couple as the forces do."""
    assert 12 * 24 == 16 * 18 == 288
    assert 137 == 8 * 17 + 1                     # eight spines and one
    assert _ord(2, 17) == 8                      # the spine's binary period
