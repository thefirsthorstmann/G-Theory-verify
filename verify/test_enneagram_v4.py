"""The Enneagram Is a Theorem, version 4, Part I (October 2026): the cross-references, the physical reading, the terms.

Brought to the definitive edition's numbering on 20 October 2026 (catalog/BRIEF-THE-DEFINITIVE-EDITION-2026-10.md): Part I
is §1–§21 and ends before "## 22 ·", §12 is expanded, §13 and §19 are new, the old §13–§17 are §14–§18 (the grading §18, the
line theorem §17), verification is §20 with the old §20's priority statement folded in, and the references §21. The old Part
Two is in catalog/SOURCE-THE-HARMONY-OF-THE-KINGS-FROM-THE-ENNEAGRAM-2026-10.md. The eighteen notes and every repaired
sentence are checked as before; only the section numbers below changed.

Three versions on Zenodo (5 July, 9 July, 27 August). Part I (§1–§20) applied on 7 October; Part II is being
restructured at CC's word (7 October): a brief part on ninefold cosmologies, the resurrection of the symbol, "Can
the Enneagram do it?", and the living inquiry in the Sierra Nevada, with the rest becoming a separate record, The
Harmony of the Kings. Found in Part I: §17 was a standalone chapter and kept its own section numbers in five
cross-references; §1 and §19 said no physical reading is made in the volume while §17 makes one; §1 pointed to §17
for the suite, which is §18; §16 named the pairings at a point two ways; §18 printed August's suite count. Round two
(7 October, the board): the cusps stand between the fixed points, not at them; Midy needs a prime modulus; the line
theorem's distinct points are the remainders; Z/9's quotient orders are {1, 3, 9}; the rounding lifts {2, 5, 8} only.
Part b: the abstract's "threefold multiplicity or none" (the board flagged it beside §17's; round two repaired only
§17), and §20's priority sentence, since the count of cyclic classes is the classical theory of decimal periods.
"""

import math
import pathlib
import re
from abstract_note import ADDRESS, note_of, statement_of

CATALOG = pathlib.Path(__file__).resolve().parent.parent / "catalog"
RAW = (CATALOG / "THE-ENNEAGRAM-IS-A-THEOREM.md").read_text()
LINES = RAW.split("\n")
CUT = next((i for i, line in enumerate(LINES) if line.startswith("## 22 · ")), len(LINES))
PART1 = " ".join(" ".join(LINES[:CUT]).split())
NOTES = re.findall(r'<div class="vnote">(.+?)</div>', PART1)
PROSE1 = re.sub(r'<div class="vnote">.+?</div>', " ", PART1)
ABSTRACT = re.search(r"(?m)^%%ABSTRACT: (.+)$", RAW).group(1)


def _section(number):
    start = next(i for i, line in enumerate(LINES) if line.startswith(f"## {number} · "))
    end = next(i for i in range(start + 1, len(LINES)) if LINES[i].startswith("## "))
    return " ".join(" ".join(LINES[start:end]).split())


def test_section_17_names_its_own_parts_instead_of_numbering_them():
    seventeen = _section(18)
    for stale in ("(Section 4)", "(Section 5)", "Sections 2 through 6", "the landing of Section 6",
                  "Sections 4, 6 and 8"):
        assert stale not in seventeen, stale
    for named in ("(the alternation theorem)", "(the theorem on minimal neutrals)",
                  "The abelian part of that structure",
                  "contradicts the identification's clause that the observable sector is the triangle",
                  "The readings attached to the alternation theorem, to the rounding and to the identification pin "
                  "nothing"):
        assert named in seventeen, named


def test_the_volume_says_where_its_physical_identifications_are():
    # 22 October 2026 (the consistency pass): section 9 states a second identification, the pair layer with the
    # primordial fluctuations, so section 1 and the companion paragraph name both; this test pinned the one of section 18.
    assert ("Two physical identifications are made, the pair layer with the primordial fluctuations in §9 and the "
            "grading with color charge in §18, each labeled there as an identification.†") in PART1
    assert "no physical reading is offered" not in PROSE1 and "nowhere in this volume" not in PROSE1
    assert PART1.count("The physical readings of these objects, beyond the identifications of §9 and §18") == 1
    assert "Identification: the figure's pair layer carries the primordial fluctuations" in PART1
    assert "*Here the figure is mathematics, and the mathematics is enough.*" in PART1


def test_the_pointers_the_notation_and_the_count():
    assert "Section 20 names the public suite" in PART1 and "Section 18 names" not in PART1
    sixteen = _section(17)
    assert "(**T**)" in sixteen and "(**X**)" in sixteen and "(**Y**)" in sixteen and "(**·**)" not in sixteen
    assert "two thousand seven hundred ten" not in PART1
    assert "an 80-digit number" in PART1 and "a 80-digit" not in PART1
    assert "about a third of a degree" in PART1 and abs(360 / 1008 - 0.357) < 1e-3
    assert "124875)." not in PART1


def test_the_front_and_the_notes():
    # 2026-10-28: the closing note on the public suite and Lean 4 is apparatus, counted apart (abstract_note.py).
    assert ADDRESS in note_of(ABSTRACT)
    words = [w for w in statement_of(ABSTRACT).split() if re.search(r"\w", w)]
    assert 150 <= len(words) <= 250
    assert "version 4, October 2026" in RAW
    assert len(NOTES) == 18 and PROSE1.count("†") == 18        # round one's three, round two's fourteen, §20's one


def test_part_one_carries_no_retired_word():
    """The volume's own wording, §1–§20; the reference list (§21) quotes titles as their authors wrote them (one is on
    antiferromagnetically coupled wheels), and a quoted title is not the volume's wording."""
    body = PROSE1.split("## 21 · References")[0]
    for gone in (r"\bseat\w*", r"\bwheel\w*", r"\bforced\b", "celebrated", r"bookkeep\w*", "spending",
                 r"\bbuys\b", "married", "photographed", "ALONG", "SAME", "pitch- class"):
        assert not re.search(gone, body), gone


def test_the_arithmetic_the_text_states():
    # the spectrum's quartic, the balanced forms as the multiples of 999, the pairing census
    for k in range(1, 5):
        x = 4 * math.sin(math.radians(20 * k)) ** 2
        assert abs(x ** 4 - 9 * x ** 3 + 27 * x ** 2 - 30 * x + 9) < 1e-9
    assert [f // 999 for f in (142857, 124875, 147852, 152847)] == [143, 125, 148, 153]
    assert all(f % 999 == 0 for f in (142857, 124875, 147852, 152847)) and 124578 % 999 != 0
    assert 8668 + 8264 + 2473 + 270 + 8 == 3 ** 9 and 8668 * 4 == 34672


def test_round_two_the_boards_repairs():
    import cmath
    for k in (2, 3, 4, 5):                                       # the cusps on the inner circle, the tangencies on the base
        z = lambda t: (k * cmath.exp(1j * t) + cmath.exp(1j * k * t)) / (k + 1)
        assert abs(abs(z(math.pi / (k - 1))) - (k - 1) / (k + 1)) < 1e-12 and abs(abs(z(0)) - 1) < 1e-12
    assert "The k − 1 cusps stand midway between the fixed points" in PART1
    assert "Red marks the cusps, on the circle of radius (k−1)/(k+1)" in PART1
    assert 'cx="0" cy="21" r="2.1" fill="#a81810"' in RAW                  # the cardioid's cusp, re-marked
    assert "If 1/q, with q prime, has even period 2h" in PART1               # Midy
    assert "The remainder path of 1/p in base b" in PART1                    # the line theorem
    assert "its quotients in all are of orders one, three and nine" in PART1 # Z/9
    assert "the rounding depths three, four and five" in PART1                # the lift of one class
    assert "from 207 to 202" in PART1 and "207 to 201" not in PART1
    assert "the number that divides every balanced form" in PART1
    assert "Four choices precede it and are named where they enter" in PART1
    # part b: the abstract, §1, §17 and §20
    assert "coarsens the figure's residues into more than one class has threefold multiplicity" in ABSTRACT
    assert "charges off the third-integer lattice" not in ABSTRACT           # the charge table's, not the grading's
    assert "without proving what fixes any of the three" in PART1
    assert "that the accounts known to the author notice and do not derive" in PART1
    assert "in the theory of decimal periods that Gauss's Disquisitiones Arithmeticae of 1801 completed" in PART1
    assert "Gauss, C. F. (1801). *Disquisitiones Arithmeticae.*" in PART1  # and he stands in the references
    for gone in ("three names for one property", "Three independent conditions", "no scan and no selection",
                 "threefold multiplicity or none", "Held twice over", "smallest noncommutative structure",
                 "outward in one member and inward in the other", "Martin polynomial data"):
        assert gone not in PROSE1, gone
