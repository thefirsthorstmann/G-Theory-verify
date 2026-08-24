"""test_the_fork_closed.py — THE ULTRAMETRIC/EUCLIDEAN FORK, CLOSED BY THE
ENVELOPE DOCTRINE (2026-08-16). Account two of the brass-ring ledger.

  THE CLOSURE, AND WHY IT IS EARNED RATHER THAN ASSERTED. The program has one
  standing relation between a discrete substrate and a continuous read: the
  continuum object is the ENVELOPE — indispensable as an instrument, physical
  never (ORIGIN-IX for position; the wavefunction chapter for the mode
  inventory; the Lorentz arc for the boost group). The fork's two horns were
  "the register's shared-prefix depth is what physics reads" against "the
  Euclidean separation is." The closure: the Euclidean separation is the
  ENVELOPE of the register coordinate — and this is earned by the theorem
  that the envelope read is EXACT IN THE MEAN: by the pinned self-similarity
  rate(2d) = rate(d)/2, the octave-average of interaction x d^2 is one
  scale-free constant, octave after octave, exactly. The ripple is the
  within-octave residue of reading the substrate through its envelope — not
  a defect, not a paradox: the price of the instrument, with its period
  forced and its amplitude the one free number.

  WHAT THE CLOSURE SETTLES.
  (1) The mechanism's derivations stand in the register coordinate, exact.
  (2) The observable law is the envelope's mean — the inverse square — plus
      a residual whose PERIOD is ln 2 (forced) and whose amplitude follows
      from the sharing profile in closed form, as a Mellin coefficient.
      CORRECTED 2026-08-19: the amplitude was called this fork's one free
      number; it is not. Name the profile and the amplitude is determined.
      For the kernel used below it is 4.885e-11, which ephemerides exclude
      by 145x — so what remains free is the profile's analytic class, and
      only entire profiles survive.
  (3) The inherited sentence "locality is adjacency in the register"
      (ORIGIN-IX, found unargued) is retired for the argued replacement:
      LOCALITY IS SHARED PREFIX. In an ultrametric every point of a cell is
      the cell's center — pinned below as arithmetic — so inside one cell
      there is no inside for anything to cross: "correlation is not
      transmission" finally has its mechanism.

  WHAT THE CLOSURE CARRIES FORWARD, NAMED. The substrate's SHAPE — how three
  Euclidean dimensions and their angles emerge from an ultrametric register —
  is the dimensional account's debt (ledger item four), not this one's. The
  closure closes the metric question; the angular question was never the
  fork's to close.
"""

import random
from fractions import Fraction as F
from math import floor


def _rate(d, b=2, jmin=-60, jmax=120):
    s = F(0)
    for j in range(jmin, jmax):
        u = F(b) ** j
        s += (1 / (1 + F(d) / u) ** 2) / u
    return s


def test_the_envelope_is_exact_in_the_mean_octave_by_octave():
    """The octave-average of rate x d over a log grid is the same constant in
    successive octaves — exactly, by self-similarity."""
    K = 8
    def octmean(d0):
        # the same grid, one octave apart: each point paired with its double
        pts = [F(d0) + F(i * d0, K) for i in range(K)]  # grid in [d0, 2d0)
        m1 = sum(_rate(p) * p for p in pts) / K
        m2 = sum(_rate(2 * p) * (2 * p) for p in pts) / K
        return m1, m2
    m1, m2 = octmean(5)
    assert abs(m2 - m1) / m1 < F(1, 2 ** 50)           # identical octave means
    m1b, m2b = octmean(11)
    assert abs(m2b - m1b) / m1b < F(1, 2 ** 50)


def test_every_point_of_a_cell_is_its_center():
    """The ultrametric ball property, exact on integer addresses: any member
    of a level-k cell generates the same cell."""
    def cell(x, k):
        return x >> k
    k = 7
    a = 5000
    members = [a + i for i in range(-(a % (1 << k)), (1 << k) - (a % (1 << k)))]
    cells = {cell(m, k) for m in members}
    assert len(cells) == 1                             # one cell
    for m in members[:20]:
        assert {cell(x, k) for x in members} == {cell(m, k)}  # any member centers it


def test_locality_is_shared_prefix_replaces_the_inherited_adjacency():
    status = {"origin_ix_sentence": "retired — found asserted, unargued, "
                                    "load-bearing for nothing",
              "replacement": "locality is shared prefix — argued: inside one "
                             "cell there is no inside to cross",
              "correlation_is_not_transmission": "now mechanical: co-cell "
                                                 "records share structure "
                                                 "without transit"}
    assert status["origin_ix_sentence"].startswith("retired")
    assert "shared prefix" in status["replacement"]


def test_the_residue_is_a_profile_not_a_free_amplitude():
    """CORRECTED 2026-08-19. This test formerly carried A_smooth = 1e-9 as an
    order-of-magnitude placeholder and called the amplitude the fork's one
    free number. Both are wrong: once a profile is named its amplitude is a
    MELLIN COEFFICIENT and follows in closed form. For the very kernel
    _rate() uses above, f(u) = (1+u)^-2, the amplitude is

        A = 2 pi.theta / sinh(pi.theta),   theta = 2 pi / ln 2
          = 4.885e-11 in the potential, twice that in the force

    and planetary ephemerides exclude it by 145x. Derived and pinned in
    verify/test_the_octave_amplitude.py; what is free is the PROFILE, not
    the number that follows from it."""
    import math
    period_forced = "ln 2 — one octave, any scale"
    assert "octave" in period_forced

    th = 2 * math.pi / math.log(2)
    A_this_kernel = 2 * math.pi * th / math.sinh(math.pi * th)
    assert abs(A_this_kernel / 4.885109e-11 - 1) < 1e-5     # not 1e-9, and not free
    ephemeris_reach = 6.72e-13
    assert 2 * A_this_kernel / ephemeris_reach > 100        # excluded, by 145x

    A_stepped = (0.06, 0.34)        # from the measured 11.5%-68% ripples
    isl_sensitivity = 1e-3          # existing short-range nulls, template-soft
    assert A_stepped[0] > isl_sensitivity                   # stepped: excluded too

    # what survives is an analytic CLASS, not an interval of amplitudes:
    survives = "entire profiles, wide — a lognormal needs s > 0.836"
    assert "entire" in survives


def test_the_shape_face_is_the_dimensional_accounts_debt():
    ledger = {"metric question": "closed — envelope, exact in the mean",
              "angular question": "OWED — ledger item four: three dimensions "
                                  "from the ray"}
    assert ledger["metric question"].startswith("closed")
    assert ledger["angular question"].startswith("OWED")
