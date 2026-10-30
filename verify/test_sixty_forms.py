"""test_sixty_forms.py — CC's "60 forms", 2026-08-05, and what selects the reptend.

CC proposed that the whole picture (temporal and non-temporal orders, the 60
forms, the FSC, the vacuum) has to be looked at together, at the scale of its
step-by-step logic. This is the first piece of that laid out as a test rather
than a picture.

  (1) THE 60 IS FORCED. The six digits {1,2,4,5,7,8} admit 6! = 720 arrangements;
      720/6 = 120 up to rotation (necklaces, C_6); 720/12 = 60 up to rotation AND
      reflection (bracelets, D_6). EXACTLY 60 DISTINCT FORMS.
  (2) THE 60-DEGREE COINCIDENCE IS NOT WELDED. 60 forms = 6!/|D_6| = 720/12, and
      60 degrees = 360/6; these agree only because 6! = 2 x 360 and |D_6| = 2 x 6.
      The form-count is group-forced; the angle needs the chosen 360-division. Same
      number, one of them convention-dependent — flagged, not joined.
  (3) TWO TESTS THAT ARE NOT FREE, applied to all 60:
        MIDY-CLOSED     — is the 9-complement a rotation of the form? 16 of 60.
        DOUBLING-CLOSED — is 2x the number a rotation of the form? 1 of 60.
  (4) THE RESULT: 142857 IS THE UNIQUE DOUBLING-CLOSED FORM among all sixty
      arrangements of its own digits. Midy-closure is common (27%); doubling-
      closure is unique. SO THE SELECTION IS THE DOUBLING, NOT THE MIDY — the
      complement structure is shared, and the dynamics is what picks the reptend
      out of its own alphabet.
  (5) And the whole banked family — 142857, 124875, 152847, 147852, and the
      linear 124578 — is Midy-closed, so the family lives inside the 16 while
      only its first member survives the doubling test.
"""

from itertools import permutations

DIGITS = (1, 2, 4, 5, 7, 8)


def _rots(s):
    return [s[i:] + s[:i] for i in range(6)]


def _canon(s):
    return min(min(_rots(s)), min(_rots(s[::-1])))


def _num(s):
    return int("".join(map(str, s)))


BRACELETS = sorted({_canon(p) for p in permutations(DIGITS)})


def test_the_sixty_is_forced():
    perms = list(permutations(DIGITS))
    assert len(perms) == 720
    assert len({min(_rots(p)) for p in perms}) == 120        # necklaces, C_6
    assert len(BRACELETS) == 60                              # bracelets, D_6
    assert 720 // 12 == 60 and 360 // 6 == 60                # equal only via 6! = 2*360


def test_midy_closure_is_common():
    midy = [b for b in BRACELETS if tuple(9 - d for d in b) in _rots(b) + _rots(b[::-1])]
    assert len(midy) == 16
    for s in [(1, 4, 2, 8, 5, 7), (1, 2, 4, 8, 7, 5), (1, 5, 2, 8, 4, 7),
              (1, 2, 5, 8, 7, 4), (1, 2, 4, 5, 7, 8)]:
        assert _canon(s) in midy                             # the whole family


def test_doubling_closure_is_unique():
    dbl = []
    for b in BRACELETS:
        d = str(_num(b) * 2)
        if len(d) == 6:
            t = tuple(int(c) for c in d)
            if t in _rots(b) + _rots(b[::-1]):
                dbl.append(b)
    assert dbl == [(1, 4, 2, 8, 5, 7)]                       # 142857 alone, of sixty
    assert _num(dbl[0]) * 2 == 285714 and _num(dbl[0]) * 7 == 999999
