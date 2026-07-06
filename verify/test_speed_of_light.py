"""
THE SPEED OF LIGHT — two forms of a consonant unit.   GRADE: the factorizations and the
gap of 3 are FORCED ◆;  the identification with c is a UNITS READING ◇;  the MAGNITUDE
is NOT derived — held outside the forced column by the Scale Theorem (see GRADES.md, NOT CLAIMED).

This file is also the honesty check on the famous "137 surfaces inside c" claim. It is
true that the rest form carries 137 — but 137 divides the all-nines unit ITSELF
(because ord_137(10) = 8), so EVERY multiple of the all-nines carries it. The 137 in
the rest form is the period-8 fact about base 10, NOT a signal specific to light.

  observed / native :  3 x 10^8       = 300,000,000 = 2^8 . 3 . 5^8      (no 137)
  rest              :  3 x (10^8 - 1) = 299,999,997 = 3^3 . 11 . 73 . 101 . 137
  the two differ by exactly 3 (the dimension count)

Source: catalog/THE-FULL-POSITION-INTERNAL §18b; this session's c-bridge cold check.
"""
from sympy import factorint


def test_observed_form_factorization():
    assert 3 * 10**8 == 300_000_000
    assert dict(factorint(3 * 10**8)) == {2: 8, 3: 1, 5: 8}
    assert (3 * 10**8) % 137 != 0          # observed form does NOT carry 137


def test_rest_form_factorization_carries_137():
    rest = 3 * (10**8 - 1)
    assert rest == 299_999_997
    assert dict(factorint(rest)) == {3: 3, 11: 1, 73: 1, 101: 1, 137: 1}
    assert rest % 137 == 0


def test_two_forms_differ_by_three():
    assert (3 * 10**8) - (3 * (10**8 - 1)) == 3   # the dimension count


def test_137_in_rest_form_is_GENERIC_not_c_specific():
    """The honest deflation: 137 | (10^8 - 1), so n*(10^8 - 1) carries 137 for ALL n.
    The rest form (n=3) is one such multiple; the 137 is the period-8 fact, not c."""
    A = 10**8 - 1
    assert A % 137 == 0
    for n in range(1, 10):
        assert (n * A) % 137 == 0           # true for every multiple, not just 3
    # and it is NOT a property of the round power 10^8:
    assert (10**8) % 137 != 0
