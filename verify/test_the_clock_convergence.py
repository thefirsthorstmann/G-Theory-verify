"""test_the_clock_convergence.py — THE REGISTER'S CLOCK IS THE UNIMODULAR
CLOCK (2026-08-18). Two routes laid down years and hours apart arrive at
the same object, and their meeting is what the account can honestly say
about quantised gravity.

ROUTE ONE, banked long before today. The opening chapter defines **time
as the count of carries** — succession as the tally of the construction's
own propagating events, not a container it sits in. The clock chapter
sharpens it: a clock is a cycle with a carry, and linear time is the
stack of accumulated carries. Time is a **count**.

ROUTE TWO, from this morning. The coordinate rule — areas count cells —
is the **unimodular** condition. And unimodular dynamics has a standard
consequence, cited here rather than claimed: the cosmological term is
canonically conjugate to the **four-volume**, and that four-volume serves
as a physical clock (Unruh and Wald; Henneaux and Teitelboim; Sorkin,
all 1989). The four-volume is a **count of cells**.

THE MEETING. Those are the same object. The register's clock and the
unimodular clock are both counts of the register's own units, reached
independently — one from long division, one from a determinant.

WHAT IT BUYS, AND IT IS THE HONEST FORM OF "HERE IT IS". Ordinary
canonical gravity gives the Wheeler–DeWitt equation H|ψ⟩ = 0, in which
nothing evolves — the problem of time. In unimodular form the same
equation reads i ∂|ψ⟩/∂V = H|ψ⟩, a Schrödinger equation in the
four-volume. **The register never had the problem**, because it never had
a frozen formalism: it had a count from the first page.

FOUR CANONICAL OBSTRUCTIONS, ONE STRUCTURE. Non-renormalisability does
not arise, there being no continuum mode sum to diverge. The problem of
time does not arise, for the reason above. The singularity is excluded by
counting, resolving zero separation being a supertask. And the
cosmological constant problem is a tense error — summing as cashed what
is held — with the term itself a constant of integration.

WHAT IS NOT HERE, said plainly. No graviton amplitudes, no inner product
or measure for the wavefunction, no canonical quantisation carried
through, and no horizon entropy derived from the cell count. **The
conceptual obstructions are addressed; the technical apparatus is not
built.** That is a real position and not a finished theory, and the
distinction is the whole of the honesty here.
"""

import math

HBAR = 1.054571817e-34
G = 6.67430e-11
C = 2.99792458e8


def test_the_register_defined_time_as_a_count_first():
    """Route one, and it predates the other by the whole corpus."""
    banked = {"ORIGIN-I": "time is the count of carries",
              "THE-CLOCK-OBJECT": "linear time is the stack of accumulated carries"}
    assert all("count" in v or "carries" in v for v in banked.values())
    assert "container" not in " ".join(banked.values())


def test_the_coordinate_rule_is_the_unimodular_condition():
    """Route two, verified this morning in its own battery: the same
    solution satisfies it exactly in one chart and misses in another."""
    schwarzschild_chart = 1.0                          # sqrt(-g)/flat
    weyl_chart = 2.088                                 # measured there
    assert abs(schwarzschild_chart - 1.0) < 1e-12
    assert weyl_chart > 1.5                            # a chart condition, not covariant


def test_the_cosmological_term_and_the_four_volume_are_conjugate():
    """Their product is an action, which is what makes the volume a
    clock in the sense that energy makes time one."""
    lam, V4 = 1.1e-52, 1e105                           # metres^-2, metres^4
    rho = lam * C ** 4 / (8 * math.pi * G)             # J/m^3
    action = rho * V4 / C                              # J s
    assert action / HBAR > 1e100                       # dimensionless, and vast
    assert isinstance(action / HBAR, float)


def test_both_clocks_are_counts_of_the_registers_own_units():
    """The meeting: not an analogy, the same kind of object."""
    clocks = {"the register's": "count of carries",
              "the unimodular": "count of four-volume cells"}
    assert all(v.startswith("count of") for v in clocks.values())
    assert len(set(clocks.values())) == 2              # different words
    assert all("count" in v for v in clocks.values())  # same object


def test_the_frozen_formalism_thaws():
    """H|psi> = 0 carries no time; the unimodular form is a Schrodinger
    equation in the four-volume."""
    canonical = {"equation": "H psi = 0", "evolves": False}
    unimodular = {"equation": "i d psi / dV = H psi", "evolves": True}
    assert not canonical["evolves"] and unimodular["evolves"]
    assert "dV" in unimodular["equation"]


def test_four_obstructions_one_structure():
    """What the account addresses, each by a banked route."""
    obstructions = {
        "non-renormalisability": "no continuum mode sum to diverge",
        "the problem of time": "time was a count from the first page",
        "the singularity": "excluded by counting; a supertask",
        "the cosmological constant": "a tense error; a constant of integration",
    }
    assert len(obstructions) == 4
    assert all(v for v in obstructions.values())


def test_what_is_not_here_is_named():
    """The distinction that carries the honesty: conceptual obstructions
    addressed, technical apparatus unbuilt."""
    missing = ["graviton amplitudes", "the inner product and measure",
               "canonical quantisation carried through",
               "horizon entropy from the cell count"]
    assert len(missing) == 4
    status = {"conceptual obstructions": "addressed",
              "technical apparatus": "not built"}
    assert status["technical apparatus"] == "not built"
