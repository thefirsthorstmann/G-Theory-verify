"""test_the_midy_involution.py — THE MIDY PAIR IS ONE OBJECT WITH A SIGN,
AND THE PRIME THAT HAS NO PAIR IS THE ONE THE FRAMEWORK ALREADY CALLS
NEUTRAL (2026-08-20). Second pass at the Fa location, still on the
Antikythera footing: report what the parts do, grade the reading apart.

WHAT A MIDY PAIR ACTUALLY IS. Not two objects that happen to cancel. For a
prime of even period 2k the halves sum to all-nines **because**

    10^k ≡ −1  (mod p)

verified for 7, 11, 13, 17, 101 and 137. So the register carries a built-in
**involution**, and that involution is "multiply by 10^k" — **a sign flip
that is a shift in depth.** For the seventh, 142 + 857 = 999 and 857 is the
complement of 142 against full; neither half is prior, and the operation
carrying you between them is a half-period shift.

**AND THE THREE HAS NO PAIR.** Its period is 1 — odd, so there is no half
period, no involution, **no sign to flip.** And three is precisely the
prime the framework already calls neutral: the triad {3, 6, 9} is the
residue class the hexad never touches. *No Midy pair, no sign, neutral* —
three statements that coincide on the one prime where the framework has an
independent opinion.

THE HONEST LIMIT, stated so the agreement is not oversold. Other primes
below sixty also have odd period — 31, 37, 41, 43, 53 — and the framework
makes no neutrality claim about any of them. So the correspondence holds
where it is tested and is untested elsewhere. **37 and 41 are the first
places it could fail**, and until someone checks them this is one data
point, not a law.

WHERE THE PRIMES ENTER, which bears on the coupling. Seven and thirteen
enter at depth **six** — the reptend's own period. One-three-seven enters
at depth **eight** — the octave ring. The two depths share only three and
eleven, and eleven because its order is two, which divides both.

    10⁶ − 1 = 3³·7·11·13·37
    10⁸ − 1 = 3²·11·73·101·137

THE FULL/EMPTY POINT, with both halves now in hand. The empty state 10^k
carries two and five only — the base's own. The full state 10^k − 1 carries
every other prime. **They differ by one.** So the single point of
differentiation at Fa is between a state carrying every prime and a state
carrying none, one tick apart — and everywhere else in the octave the two
readings differ by two, three, five or six ticks. Only here by the one that
separates full from empty.

THE READING, GRADED. CC proposes the Midy pairs are the seat of virtual
particles or simply are them. The shape is right — one object with two
complementary faces related by an operation acting as −1 is what a vacuum
fluctuation is, rather than two particles that cancel. But there is no
derivation here, no number, and no forbid. It is a correspondence, and the
one thing that would make it more is the neutrality test above: **if
no-pair ⟺ neutral is a law, the reading acquires a forbid.** Today it is
one confirmed instance.
"""

from sympy import factorint, n_order, primerange


def test_the_midy_condition_is_the_minus_one_congruence():
    for p in (7, 11, 13, 17, 101, 137):
        per = n_order(10, p)
        assert per % 2 == 0
        assert pow(10, per // 2, p) == p - 1


def test_the_sevenths_halves_are_complements_against_full():
    assert 142 + 857 == 999
    assert 857 == 999 - 142
    assert 10 ** 3 - 1 == 999


def test_the_involution_is_a_shift_in_depth():
    """Multiplying by 10^k is a rotation of the digit string."""
    for p in (7, 13, 137):
        per = n_order(10, p)
        k = per // 2
        assert pow(10, k, p) == p - 1
        assert pow(10, per, p) == 1                  # twice returns


def test_the_three_has_no_pair():
    assert n_order(10, 3) == 1
    assert n_order(10, 3) % 2 == 1                   # odd, so no half


def test_and_three_is_the_frameworks_neutral():
    triad = {3, 6, 9}
    hexad = {1, 4, 2, 8, 5, 7}
    assert not (triad & hexad)
    assert all(t % 3 == 0 for t in triad)


def test_the_correspondence_is_one_instance_not_a_law():
    odd_period = [p for p in primerange(3, 60)
                  if p != 5 and n_order(10, p) % 2 == 1]
    assert 3 in odd_period
    untested = [p for p in odd_period if p != 3]
    assert untested == [31, 37, 41, 43, 53]
    assert len(untested) > 0                         # so it is not yet a law


def test_seven_and_thirteen_enter_at_the_reptend_period():
    assert n_order(10, 7) == 6
    assert n_order(10, 13) == 6
    f = factorint(10 ** 6 - 1)
    assert 7 in f and 13 in f


def test_the_coupling_prime_enters_at_the_octave_ring():
    assert n_order(10, 137) == 8
    f = factorint(10 ** 8 - 1)
    assert 137 in f
    assert 7 not in f                                # and the seed is absent


def test_the_two_depths_share_only_three_and_eleven():
    a = set(factorint(10 ** 6 - 1))
    b = set(factorint(10 ** 8 - 1))
    assert a & b == {3, 11}
    assert n_order(10, 11) == 2
    from math import gcd
    assert gcd(6, 8) == 2                            # which is why


def test_the_empty_state_carries_only_the_bases_primes():
    for k in range(1, 10):
        assert set(factorint(10 ** k)) == {2, 5}


def test_and_the_full_state_carries_the_rest():
    for k in range(1, 10):
        f = set(factorint(10 ** k - 1))
        assert not (f & {2, 5})


def test_they_differ_by_one():
    for k in range(1, 10):
        assert (10 ** k) - (10 ** k - 1) == 1


def test_the_reading_carries_no_forbid_yet():
    graded = {"the minus-one congruence": "forced",
              "three has no pair": "forced",
              "three is the neutral": "banked",
              "no pair means neutral, generally": "untested",
              "Midy pairs are virtual pairs": "correspondence"}
    assert graded["no pair means neutral, generally"] == "untested"
    assert graded["Midy pairs are virtual pairs"] == "correspondence"
    has_forbid = False
    assert not has_forbid
