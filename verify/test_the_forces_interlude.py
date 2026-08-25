"""test_the_forces_interlude.py — THE FLAGSHIP'S FORCES INTERLUDE: THE FOUR
INTERACTIONS DATED INSIDE THE UNFOLDING, GRAVITATION SEATED AS THE REFERENCE
LEVEL (2026-08-25). CC: "Origin should have a gravity/forces section that
gives the logical unfolding — where, when, how."

THE FINDING THAT MOTIVATED IT: the book used gravitation from the early
galaxies onward and never introduced it as mechanism; "tonal center"
appeared nowhere in its 2,173 lines. THE INTERLUDE (between Volumes IV and
V, where all ingredients exist and before structure needs the pull): light
first (the dipole, ℓ = 1, no mass required); tone second (commitment,
confinement completing the hadron's rest tick); the weak sector as the
operation between provenances; and gravitation NOT as a fourth peer but as
the register's reference level — present from the first division,
unsounded, its relation with matter DATED at the acquisition of a rest
frequency (the electroweak whole tone for elementary matter, confinement
for hadrons). Mechanism imported from the gravity paper by citation, never
re-derived. This battery pins the interlude's exact claims and its
consistency with both the book's own Volume II rung count and the published
gravity paper.
"""

import pathlib

CATALOG = pathlib.Path(__file__).resolve().parent.parent / "catalog"
BOOK = (CATALOG / "THE-ORIGIN-ON-DISCRETE-TERMS.md").read_text()
GRAVITY = (CATALOG / "GRAVITY-AS-TONAL-CENTER.md").read_text()
FLAT = " ".join(BOOK.split())
GFLAT = " ".join(GRAVITY.split())


def test_the_interlude_sits_between_volumes_four_and_five():
    i4 = BOOK.index('VOLUME IV · PLASMAS</div>')
    ii = BOOK.index('INTERLUDE · THE FORCES, IN ORDER OF APPEARANCE</div>', i4)
    i5 = BOOK.index('VOLUME V · THE BIRTH OF CHEMISTRY</div>', ii)
    assert i4 < ii < i5
    assert FLAT.count("INTERLUDE · THE FORCES, IN ORDER OF APPEARANCE") == 2
    # once in the Contents, once as the volhead


def test_the_coupling_is_the_exact_reciprocal_in_both_places():
    alpha = 5 / (2 ** 151 - 1)
    assert abs(alpha - 1.7517e-45) < 2e-49
    assert "5/(2¹⁵¹ − 1)" in FLAT
    assert "5/(2¹⁵¹ − 1)" in GFLAT                     # the same object, same form


def test_the_placement_of_g_matches_the_gravity_paper():
    ppm = (6.6735902 - 6.67430) / 6.67430 * 1e6
    assert abs(ppm + 106) < 1
    assert "106 parts per million below the CODATA centre" in FLAT
    assert "6.6735902" in GFLAT


def test_the_onset_identification_matches_the_paper_verbatim():
    assert "acquisition of a rest frequency" in FLAT
    assert "acquisition of a rest frequency" in GFLAT   # one identification, one wording
    assert "one count read twice" in FLAT
    assert "first light precedes all weight" in FLAT


def test_the_rung_count_agrees_with_volume_two():
    assert "first lawful rung" in FLAT                  # Volume II's own table
    assert "begins at ℓ = 2" in FLAT                    # the interlude's import
    assert "ℓ = 1, the dipole" in FLAT or "begins at ℓ = 1" in FLAT


def test_the_tonal_center_definition_matches_the_gravity_paper():
    phrase = "need not be sounded in order to organize what is sounded"
    assert phrase in FLAT                               # the interlude and definitions
    assert phrase in GFLAT                              # the paper's own definition
    assert "**tonal center (the key)**" in BOOK         # the definitions entry


def test_the_front_matter_carries_version_two():
    assert FLAT.count("10.5281/zenodo.22087600") >= 3   # titlenote x2 + reference
    assert FLAT.count("public at github.com/thefirsthorstmann/g-theory-verify") >= 2
    assert FLAT.count("version 2, August 25th, 2026") == 3   # byline x2 + copyright
    assert "121102" in FLAT                             # MICROSCOPE cited


def test_the_index_and_conditions_carry_the_interlude():
    assert "<p>tonal center — " in BOOK
    assert "<p>gravitation — " in BOOK
    assert "refutes the account outright" in FLAT       # the inherited conditions
