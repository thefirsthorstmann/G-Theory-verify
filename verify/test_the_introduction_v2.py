"""test_the_introduction_v2.py — THE FRONT DOOR AT VERSION 2 (2026-08-25).
The Introduction (ship 1, DOI 10.5281/zenodo.21212293) predated the gravity
paper; version 2 folds the result in with a light hand: one paragraph in §3
noting the fifth criterion's account now stands on the record, four shelf
rows (Gravity with its DOI; Tonal Function, Color, and Water with
placeholders filled at their posting), and the versioned front matter. The
manifesto's own voice is untouched.
"""

import pathlib
import re

CATALOG = pathlib.Path(__file__).resolve().parent.parent / "catalog"
DOC = (CATALOG / "G-THEORY-AN-INTRODUCTION.md").read_text()
FLAT = " ".join(DOC.split())


def test_the_front_matter_is_versioned():
    assert FLAT.count("version 2, August 25th, 2026") == 2   # byline + copyright


def test_the_fifth_criterion_paragraph_is_present():
    assert "the fifth criterion's connection stated and derived" in FLAT
    assert "seventeen conditions of refutation" in FLAT
    assert "github.com/thefirsthorstmann/g-theory-verify" in FLAT
    # the version-2 rigor pass on the criteria (CC, 2026-08-25):
    assert "**7. Harmonic structure.**" in DOC          # the technical name
    assert "**8. Common sense about tools.**" in DOC
    assert "worst mathematical tools" not in DOC        # the overreach, removed
    assert "an open empirical question" in FLAT         # perception left open
    assert "a working choice" in FLAT                   # the series' tool as hypothesis


def test_the_shelf_carries_the_gravity_row():
    assert "| 12 | *Gravity on Discrete Terms* | 10.5281/zenodo.22087600 |" in DOC


def test_the_three_new_rows_exist_with_doi_or_placeholder():
    for n, title in ((13, "Tonal Function on Discrete Terms"),
                     (14, "Visible Light on Discrete Terms"),
                     (15, "Water on Discrete Terms"),
                     (16, "The Vacuum on Discrete Terms"),
                     (17, "Motion on Discrete Terms"),
                     (18, "Units on Discrete Terms"),
                     (19, "Yang–Mills: Existence on Discrete Terms"),
                     (20, "QED on Discrete Terms"),
                     (21, "G-Theory — The Falsification Schedule")):
        pat = rf"\| {n} \| \*{re.escape(title)}\* \| (DOI-{n}|10\.5281/zenodo\.\d+) \|"
        assert re.search(pat, DOC), title
