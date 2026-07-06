"""
THE REST-BELL BRACKET.   GRADE: the arithmetic identity is FORCED ◆;  the CHSH/Bell
reading (that this brackets the quantum ceiling) is a READING ◇.

Parallel to rest-pi: the framework brackets the Tsirelson bound 2*sqrt(2) with two just
tritones and never seats the irrational.

  45/32  (just augmented fourth, tritone up)
  64/45  (just diminished fifth, tritone down)
  product = 2  (the octave -- the 45's cancel; 3 up x 3 down -> the two threes annihilate)

  rest-Bell = 45/32 + 64/45 = 4073/1440 ~ 2.82847,   +0.0016% above 2*sqrt(2).

sqrt(2) is the tritone: the geometric mean of fifth and fourth, the residue left after
the three cancels. The ceiling is bracketed, never seated -- the magnitude stays the
irrational forbidden zero.

Source: catalog/THE-FULL-POSITION-INTERNAL §Vb ("the rail and the three-cancellation").
"""
import math
from fractions import Fraction


def test_two_just_tritones_multiply_to_the_octave():
    up, down = Fraction(45, 32), Fraction(64, 45)
    assert up * down == 2                       # the 45's cancel -> the octave


def test_rest_bell_value():
    up, down = Fraction(45, 32), Fraction(64, 45)
    rest_bell = up + down
    assert rest_bell == Fraction(4073, 1440)    # exact


def test_rest_bell_brackets_tsirelson_from_above():
    rest_bell = float(Fraction(4073, 1440))
    tsirelson = 2 * math.sqrt(2)
    assert rest_bell > tsirelson                          # bracketed from above
    pct = (rest_bell - tsirelson) / tsirelson * 100
    assert 0.0010 < pct < 0.0020                           # +0.0016%, never seated
