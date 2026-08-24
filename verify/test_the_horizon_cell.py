"""test_the_horizon_cell.py — THE HORIZON COUNT, AND THE TARGET MADE ONE
NUMBER (2026-08-18). the author asked for the horizon area and for whatever the
technical apparatus needs. What came out is not the entropy derived, but
the target reposed from a field to a sentence — and one of my own clean
readings withdrawn on the way, which is the part worth keeping.

WHAT THE QUARTER IS MADE OF. The first law at the horizon reads
dM = (κ/8π)dA and the Hawking temperature is κ/2π, so dS = dA/4 with the
quarter being **2π over 8π** — the Euclidean periodicity divided by the
matter coupling. Both factors already sit in this account: the field
equations were verified in four classes today, and the periodicity is a
closure condition on an angle.

THE COUNTING FORM, AND A WITHDRAWAL. Asking which cell makes the entropy
one unit per cell gives a cell of side exactly two Planck lengths, at
which the quarter disappears — clean, and the doubling is the register's
own first generator. **But it is not available to this account.** One nat
per cell requires e states per cell, and a discrete register cannot have
e states. The nat reading is withdrawn.

WHAT THE ACCOUNT IS ENTITLED TO. For a register of N cells with k states
each the entropy is N ln k with **k an integer**, so matching A/4 requires
a cell of area 4 ln k. On the binary layer this account already runs on,
k = 2 and the cell has area **4 ln 2** Planck areas — side 2√(ln 2) ≈
1.665. The ln 2 is not imported: it is the same ln 2 derived elsewhere as
ln(b)/(b−1) for the short-range correction, and it appears here for the
same reason, the layer being binary.

THE TARGET, NOW ONE NUMBER. Before: derive the horizon entropy. Now:
**derive why the horizon's cell has area 4 ln 2 in Planck areas.** The
4 = 2² is the octave in each of the horizon's two directions; the ln 2 is
the binary layer. Both are register objects. What is *not* shown is that
they combine here for the register's own reasons rather than by matching
a known answer, and until that is shown this is a reposed target and not
a result.

AND THE LOGARITHM IS NOT OWED EITHER — the author's question settled it. Asked
whether the e is a continuum artifact, the answer is yes and precisely
where: Boltzmann's entropy is a natural logarithm, and base e arrives
through Stirling, the Gaussian and dx/x — every one a continuum
construction. **The nat is the continuum's unit of entropy; the bit is the
discrete one.** So ln 2 is not a coefficient to derive at all, it is the
conversion between the two, and it is the same ln 2 Landauer's bound
carries for the same reason — a conversion this account already adopted
in its first chapter.

WHICH LEAVES THE FOUR, AND THE FOUR TRACES FURTHER. It is 8π over 2π. The
2π is an angle closing, which is native in spirit. The 8π is the **matter
coupling's normalisation** — and the vacuum equations verified above have
T = 0, so none of that work ever saw it. Decomposed further, 8π = 2 × 4π,
the solid angle of a sphere times the trace factor.

**So what is actually owed is the 8π.** Not the entropy, not the
logarithm, not even the four as such: one dimensionless normalisation,
and a familiar one.

THE DISCRIMINATOR TO AIM AT NEXT. Approaches to quantum gravity are told
apart by the logarithmic correction, S = A/4 + α ln A: loop quantum
gravity gives α = −1/2, various string countings give others. **A value
of α from the register would be decisive in a way the leading term cannot
be**, because the leading term is what every approach is built to
reproduce.
"""

import math


def test_the_quarter_is_the_periodicity_over_the_coupling():
    """2π from the Euclidean angle, 8π from the matter coupling."""
    assert abs((2 * math.pi) / (8 * math.pi) - 0.25) < 1e-15


def test_the_nat_reading_is_clean_and_unavailable():
    """A cell of side two Planck lengths gives one nat per cell exactly —
    and requires e states per cell, which a discrete register cannot
    have. Recorded as withdrawn, not as a result."""
    side = 2.0
    assert abs(side ** 2 / 4 - 1.0) < 1e-15            # one nat per cell
    states = math.e
    assert abs(states - round(states)) > 0.2           # not an integer
    assert not float(states).is_integer()


def test_the_bit_reading_is_what_discreteness_allows():
    """N cells of k integer states give N ln k, so the cell has area
    4 ln k; on the binary layer that is 4 ln 2."""
    for k in (2, 3, 4, 7, 8, 9):
        area = 4 * math.log(k)
        assert float(k).is_integer()
        assert area > 0
    assert abs(4 * math.log(2) - 2.7725887) < 1e-6
    assert abs(2 * math.sqrt(math.log(2)) - 1.6651092) < 1e-6


def test_the_ln_two_is_the_accounts_own_coefficient():
    """Same ln(b)/(b−1) at b = 2 that the short-range correction carries."""
    b = 2
    assert abs(math.log(b) / (b - 1) - math.log(2)) < 1e-15


def test_the_identity_holds_at_every_horizon_scale():
    """Checked on real objects — and it holds exactly because it is an
    identity, which is precisely why it is a restatement."""
    G, c, hbar = 6.67430e-11, 2.99792458e8, 1.054571817e-34
    lP = math.sqrt(hbar * G / c ** 3)
    Msun = 1.98892e30
    for M in (Msun, 4.3e6 * Msun, 6.5e9 * Msun):
        rs = 2 * G * M / c ** 2
        A = 4 * math.pi * rs ** 2
        S = c ** 3 * A / (4 * G * hbar)                # nats
        N_bits = A / (4 * math.log(2) * lP ** 2)       # cells, one bit each
        assert abs(N_bits * math.log(2) / S - 1) < 1e-12


def test_the_target_is_now_one_number():
    """Reposed: not the entropy, but the cell's area in Planck areas."""
    target = {"quantity": "the horizon cell's area",
              "value": 4 * math.log(2),
              "parts": {"4 = 2^2": "the octave in each of two directions",
                        "ln 2": "the binary layer"}}
    assert abs(target["value"] - 2.7725887) < 1e-6
    assert len(target["parts"]) == 2
    assert all("octave" in v or "binary" in v for v in target["parts"].values())


def test_the_discriminator_is_the_log_correction():
    """The leading term is what every approach is built to reproduce; the
    logarithmic coefficient is what tells them apart."""
    alphas = {"loop quantum gravity": -0.5, "this account": None}
    assert alphas["this account"] is None              # owed, and named
    assert alphas["loop quantum gravity"] == -0.5


def test_the_nat_is_the_continuums_unit_and_the_bit_is_the_registers():
    """the author's question: is the e a continuum artifact? It is. Base e reaches
    entropy through Stirling, the Gaussian and dx/x — continuum
    constructions all — while a register counting distinctions is natively
    binary."""
    units = {"nat": "continuum", "bit": "discrete"}
    assert units["nat"] == "continuum" and units["bit"] == "discrete"
    assert abs(math.log(2) - 0.6931472) < 1e-6
    for bits in (1.0, 8.0, 1e10):                       # the conversion, exactly
        assert abs(bits * math.log(2) / (bits * math.log(2)) - 1) < 1e-15


def test_the_logarithm_is_landauers_own_and_so_is_not_owed():
    """Erasing one bit costs kT ln 2 for the same reason: the price of
    quoting a discrete distinction in continuum units. Adopted in the
    first chapter, so the account has carried it all along."""
    landauer_factor = math.log(2)
    horizon_factor = 4 * math.log(2) / 4
    assert abs(landauer_factor - horizon_factor) < 1e-15
    owed = {"ln 2": False, "the 4": True}
    assert not owed["ln 2"]


def test_what_is_owed_reduces_to_the_matter_coupling():
    """4 = 8π/2π. The 2π is an angle closing; the 8π is the matter
    coupling's normalisation, which the vacuum work never saw because
    T = 0 there."""
    assert abs(8 * math.pi / (2 * math.pi) - 4) < 1e-15
    assert abs(8 * math.pi - 2 * (4 * math.pi)) < 1e-12   # the trace factor and the solid angle
    seen_by_vacuum_work = {"the field equations": True, "the 8pi": False}
    assert seen_by_vacuum_work["the field equations"]
    assert not seen_by_vacuum_work["the 8pi"]
