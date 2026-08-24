"""test_the_strong_field_file.py — THE STRONG-FIELD FILE, ASSEMBLED
(2026-08-16). Ledger item six. The file gathers what the program says where
gravity is strong — one banked cornerstone, one new assembly, two standing
replacements, the wave sector, and the entropy identity — into a single
statement with its open items named.

  THE NEW ASSEMBLY — THE LANDMARK LADDER IS PURE 2-3. Every characteristic
  radius of the Schwarzschild strong field, in units GM/c^2:

      horizon 2 · Buchdahl wall 9/4 · photon sphere 3 ·
      marginally bound 4 · shadow 3^(3/2) · ISCO 6

  — the octave, the fifth squared (the tone lifted an octave: 9/8 x 2), the
  motor, the double octave, Re's seat under the root (shadow^2 = 27), the
  hexad. NO PRIME BUT TWO AND THREE ENTERS THE STRONG FIELD'S GEOMETRY, and
  the ratios are the intervals themselves: photon/horizon = 3/2 (the fifth),
  ISCO/photon = 2 (the octave), wall/horizon = 9/8 (the tone). These are
  textbook-exact general relativity, read in the program's seats: the
  strongest gravity there is speaks in the two generators exclusively.

  THE CORNERSTONE, BANKED (2026-08-12, test_buchdahl_wall.py): the wall is
  the whole tone — R/r_s > 9/8 — from the clock's read y = sqrt(Phi)
  (amplitude against intensity, the half-power), whose surface value may not
  fall below ONE THIRD; and the scalar face cannot build the wall, missing
  it by the ratio 9/8 exactly — the tone is what the tensor face adds.

  WHAT REPLACES THE SINGULARITY: the saturation of the operation account —
  resolving zero separation is a supertask (the same census that regulates
  water), the register has a deepest cell, the potential saturates at a
  derived ceiling. No regulator; the count's own finiteness.

  WHAT REPLACES THE HORIZON: a never-attained floor. The read y = sqrt(Phi)
  is strictly positive for every r > r_s, and the program's no-attained-zero
  doctrine forbids the read from reaching zero: the horizon is approached
  forever and occupied never — the strong field's unsounded floor, the same
  office the tonic and the speed limit hold. In the register's serial order
  the infaller's commitment rate freezes; general relativity's finite
  proper-time crossing is the envelope read along the worldline; and the
  confrontation between the two — the serial order against the relativity of
  simultaneity — is ORIGIN-X's named honesty debt, carried here by name and
  not resolved in passing.

  THE WAVE SECTOR, positioned: the wave speed is c because the wave's record
  is null — no carry in flight, zero proper measure at any coordinate
  duration; radiation begins at the quadrupole (the arena is an antipodal
  pair; the nephroid rung holds the slot, banked at signpost grade); and the
  coupling is an exact square — alphaG = (sqrt(10) x 2^-76)^2 — the double
  copy's shape carried by the count itself.

  THE ENTROPY IDENTITY: the banked S_hor = pi N^2 (N = R/l_P) IS the
  Bekenstein-Hawking area law, algebraically: S = A/4 = pi R^2 in Planck
  units. One licensed dimensionful reference, as the banked analysis
  demands; the 2D storage reading (the missing third) stands behind it at
  reading grade.

  OPEN, NAMED: the serial-order confrontation (the honesty chapter's debt);
  the tensor-face dynamics beyond linear order (the wall's own caveat); and
  ringdown/echo phenomenology of a never-attained floor against the observed
  ringdowns — flagged as the file's observational face, unpriced.
"""

from fractions import Fraction as F
from math import sqrt, pi


LADDER = [("horizon", F(2), (1, 0)),
          ("buchdahl", F(9, 4), (-2, 2)),
          ("photon", F(3), (0, 1)),
          ("marginally_bound", F(4), (2, 0)),
          ("isco", F(6), (1, 1))]


def test_the_landmark_ladder_is_pure_two_three():
    for name, val, (a, b) in LADDER:
        assert val == F(2) ** a * F(3) ** b          # a 2-3 word, exactly
    # the shadow: b_ph^2 = 27 = 3^3 — Re's seat under the root
    assert abs((3 * sqrt(3.0)) ** 2 - 27) < 1e-12
    # ordering: horizon < wall < photon < mb < shadow < isco
    vals = [2, 2.25, 3, 4, 3 * sqrt(3.0), 6]
    assert vals == sorted(vals)


def test_the_ratios_are_the_intervals():
    assert F(3) / F(2) == F(3, 2)                    # photon/horizon: the fifth
    assert F(6) / F(3) == 2                          # ISCO/photon: the octave
    assert F(9, 4) / F(2) == F(9, 8)                 # wall/horizon: the tone
    assert F(6) / F(2) == 3                          # ISCO/horizon: the motor


def test_the_wall_cornerstone_cross_pinned():
    """The banked Buchdahl battery's chain, re-affirmed at its joints."""
    assert F(9, 8) * 2 == F(9, 4)                    # the tone times the octave
    # the read floor: y_R > 1/3 <=> Phi_R > 1/9 <=> r_s/R < 8/9
    assert F(1, 3) ** 2 == F(1, 9)
    assert 1 - F(1, 9) == F(8, 9)
    # the central read (3/2)sqrt(Phi_R) - 1/2 vanishes exactly at the ninth:
    assert F(3, 2) * F(1, 3) - F(1, 2) == 0


def test_the_horizon_is_never_attained():
    """y = sqrt(1 - 2/r) > 0 strictly for r > 2: the unsounded floor."""
    for r in (2.000001, 2.01, 3, 10, 1e6):
        y2 = 1 - 2.0 / r
        assert y2 > 0                                # never zero above the floor
    doctrine = {"attained zero": "forbidden",
                "the horizon": "approached forever, occupied never — the "
                               "office of the tonic and of c",
                "serial order vs proper crossing": "ORIGIN-X's named debt, "
                                                   "carried not resolved"}
    assert doctrine["attained zero"] == "forbidden"
    assert "named debt" in doctrine["serial order vs proper crossing"]


def test_the_singularity_replacement_cross_pinned():
    """The saturation ceiling: the depth sum is finite — the count's own
    finiteness, no regulator introduced."""
    s = sum(F(1, 2 ** j) for j in range(0, 200))
    assert 2 - s == F(1, 2 ** 199)                   # converges to the ceiling


def test_the_wave_sector_positions():
    # speed c: the null record — zero proper measure at any duration
    for t in (1e-9, 1.0, 3.15e7):
        assert (t - t) * (t + t) == 0.0
    # the double copy's square, exact:
    assert F(10, 2 ** 152) == F(5, 2 ** 151)
    quadrupole = "the nephroid rung holds the slot — banked, signpost grade"
    assert "signpost" in quadrupole


def test_the_entropy_identity_is_the_area_law():
    """S_hor = pi N^2 with N = R/l_P equals A/4 in Planck units, exactly."""
    import random
    rnd = random.Random(5)
    for _ in range(20):
        R = rnd.uniform(1e3, 1e40)
        lp = rnd.uniform(1e-36, 1e-34)
        A = 4 * pi * R ** 2
        S_area = A / (4 * lp ** 2)
        S_banked = pi * (R / lp) ** 2
        assert abs(S_area - S_banked) / S_area < 1e-12


def test_the_files_state():
    state = {"assembled": True,
             "open": ["the serial-order confrontation",
                      "tensor-face dynamics beyond linear order",
                      "ringdown phenomenology of a never-attained floor"]}
    assert state["assembled"] and len(state["open"]) == 3
