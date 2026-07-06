"""
THE PROTON-ELECTRON RATIO, integer part.   GRADE: the factorization is FORCED ◆;
the assembly of THIS lattice node as "the proton" is selection-bearing (noted).

The measured m_p/m_e = 1836.15267343. Its integer part factors on the 2-3 lattice and
carries the spine prime 17:

  1836 = 2^2 . 3^3 . 17 = 108 . 17,   with   17 = 3^4 - 2^6.

The factorization is a fact about the measured ratio however one reaches it. What is
NOT claimed as forced: that this particular node "is" the proton (still external
physics) — see catalog/06-VERIFICATION-LOG "HONEST CEILING."

Source: catalog/THE-FULL-POSITION-INTERNAL §15.
"""
from sympy import factorint


def test_1836_factorization():
    assert dict(factorint(1836)) == {2: 2, 3: 3, 17: 1}
    assert 1836 == 2**2 * 3**3 * 17 == 108 * 17


def test_carries_the_spine_17():
    assert 17 in factorint(1836)
    assert 17 == 3**4 - 2**6


def test_is_the_integer_part_of_the_measured_ratio():
    measured = 1836.15267343
    assert int(measured) == 1836
