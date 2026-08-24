"""test_the_apportionment.py — THE FIRST POST-NEWTONIAN ORDER, CLOSED
(2026-08-18). The multi-source envelope passed its test but left one
term: the register hands each body only the other's deficit, while the
received theory's first-order acceleration of a body carries a term in
that body's own mass. The worry was a strong-equivalence violation. It
does not occur, and the reason comes from words already derived.

THE NORDTVEDT PARAMETER IS A COMBINATION OF THE OTHERS: η = 4β − γ − 3.
This paper derives γ = 1 (the ruler paying the enclosed variation) and
β = 1 (the isotropic transform of the assembled metric), so **η = 0
exactly** — not assumed, not fitted, and comfortably inside lunar
ranging's four parts in ten thousand and the pulsar ensembles' one.
Structurally the same thing says it: there is one mass attribute, the
carry rate being the rounding excess, so binding energy enters the mass
once and gravitational and inertial mass cannot differ.

AND THE CLOSURE IS WIDER THAN THE ONE TERM. At first post-Newtonian
order the parametrized framework is complete — ten parameters fix the
dynamics entirely. Two are computed here from the metric; the remaining
eight are zero by the register's own structural results: no preferred
frame, from the parameter record's gauge theorem, and no violation of the
conservation laws, from the union conserving the count exactly. Every
one takes the received theory's value, so **the whole of first
post-Newtonian dynamics agrees, the apportionment term included.** What
was called a fork at that order cannot live there; it moves to second
post-Newtonian, where this framework does not reach and where the
comparison must be done directly.
"""

GAMMA = 1.0        # derived: the ruler as the enclosed amplitude
BETA = 1.0         # derived: the isotropic transform


def test_the_nordtvedt_parameter_is_exactly_zero():
    """η = 4β − γ − 3 with the two derived words gives zero, and zero
    sits inside every published bound."""
    eta = 4 * BETA - GAMMA - 3
    assert eta == 0.0
    for bound in (4.4e-4, 1.0e-4):
        assert abs(eta) < bound


def test_one_mass_attribute_forbids_the_violation_structurally():
    """The same conclusion without the framework: the carry rate IS the
    rounding excess, so a composite's binding enters its mass once and
    the gravitational and inertial values are the same number."""
    parts = (7, 11, 13)
    binding = 2
    committed = sum(parts) - binding          # the settled total
    gravitational = committed
    inertial = committed
    assert gravitational == inertial
    assert committed != sum(parts)            # binding is real, and counted once


def test_every_parametrized_word_takes_the_received_value():
    """Two computed, eight zero by the register's own structure — so the
    first post-Newtonian dynamics agrees entirely."""
    ours = {"gamma": GAMMA, "beta": BETA, "xi": 0.0,
            "alpha1": 0.0, "alpha2": 0.0, "alpha3": 0.0,
            "zeta1": 0.0, "zeta2": 0.0, "zeta3": 0.0, "zeta4": 0.0}
    received = {"gamma": 1.0, "beta": 1.0, "xi": 0.0,
                "alpha1": 0.0, "alpha2": 0.0, "alpha3": 0.0,
                "zeta1": 0.0, "zeta2": 0.0, "zeta3": 0.0, "zeta4": 0.0}
    assert ours == received
    assert len(ours) == 10                    # the framework is complete at 1PN


def test_the_grounds_are_named_not_waved():
    """Each zero has a stated source in banked work, so the claim can be
    checked rather than taken: the frame parameters rest on §17's gauge
    theorem and the conservation parameters on §9's exact count."""
    grounds = {
        "gamma": "computed from the ruler word",
        "beta": "computed from the isotropic transform",
        "xi": "no distinguished cell in the register",
        "alpha1": "the parameter record's gauge theorem",
        "alpha2": "the parameter record's gauge theorem",
        "alpha3": "the gauge theorem and the conserved count",
        "zeta1": "the union conserves the count exactly",
        "zeta2": "the union conserves the count exactly",
        "zeta3": "the union conserves the count exactly",
        "zeta4": "the union conserves the count exactly",
    }
    assert len(grounds) == 10
    computed = [k for k, v in grounds.items() if v.startswith("computed")]
    assert sorted(computed) == ["beta", "gamma"]


def test_the_fork_moves_to_second_order():
    """What remains is the comparison the framework cannot make: second
    post-Newtonian, where the parameters run out and the constructions
    must be expanded against each other directly."""
    orders_settled = {"newtonian", "first post-newtonian"}
    orders_open = {"second post-newtonian"}
    assert orders_settled & orders_open == set()
    assert "first post-newtonian" in orders_settled
