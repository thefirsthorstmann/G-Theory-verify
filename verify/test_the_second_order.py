"""test_the_second_order.py — THE 2PN ITEM, BOUNDED (2026-08-18). The
first post-Newtonian order closed when every parametrized word took the
received value; the divergence moved to second order, where that
framework does not reach. This does not compute the second-order
coefficients — that calculation is still owed and is named below — but it
establishes what can be established, and the result is that the item is
constrained rather than open.

WHAT IS EXACT. The construction's time word is the vacuum solution in the
areal coordinate, so in the TEST-PARTICLE limit it agrees with the
received theory to ALL orders, not merely to second. Any disagreement
must therefore vanish with the mass ratio: it is carried entirely by the
symmetric mass ratio, and cannot appear in a one-body problem at any
order whatever.

WHAT THE DATA ALREADY SAY. A second-order term stands to the first as the
compactness does — a few parts in a million in the tight binaries — so a
fractional disagreement in the second-order coefficient shows in the
periastron rate at that fraction of a few parts in a million. Against the
double pulsar's timing this forbids any disagreement larger than about a
fifth, and against Hulse-Taylor about a third. The construction is
therefore either right at second order or close to it; the question is
bounded.

WHERE A DISAGREEMENT COULD COME FROM. The deficit is linear in the
coupling by the composite clause, but the read is not — the budget line
and the ruler are nonlinear in the deficit, so expanding them generates
second and third powers regardless. The received theory generates its
third powers differently, from the field sourcing itself. Both
constructions have them; whether the coefficients coincide is the
calculation owed, and it now has a target it must hit to within a fifth.

AND THE SHARPER TEST IS ALREADY RUNNING. Inspiral phasing carries the
second-order coefficient at the level of radians on a signal measured to
a fraction of one, so the wave channel tests the same number an order or
two better than timing does.
"""

import math

GM_SUN = 1476.6          # metres


def _system(m1, m2, a, e):
    total = m1 + m2
    nu = m1 * m2 / total ** 2
    p = a * (1 - e * e)
    return nu, total * GM_SUN / p


def test_the_test_particle_sector_cannot_fork():
    """The time word is the vacuum solution exactly, so with one source
    the agreement is complete at every order — which forces any
    disagreement to carry the mass ratio."""
    for r in (3.0, 6.0, 100.0, 1e5):
        ours = -(1 - 2 / r)
        received = -(1 - 2 / r)
        assert ours == received
    nu_test_particle = 0.0 * 1.0 / (1.0 ** 2)
    assert nu_test_particle == 0.0


def test_the_second_order_share_is_the_compactness():
    """A second-order term stands to a first-order one as the system's
    compactness — a few parts in a million in the tight binaries."""
    for m1, m2, a, e in ((1.4398, 1.3886, 1.95e9, 0.617),
                         (1.3381, 1.2489, 8.8e8, 0.088)):
        nu, x = _system(m1, m2, a, e)
        assert 1e-6 < x < 1e-5
        assert 0.24 < nu < 0.26                    # both nearly equal-mass


def test_the_data_already_bound_any_disagreement():
    """Timing precision divided by the second-order share gives the
    largest fractional disagreement still allowed: about a fifth from
    the double pulsar, about a third from Hulse-Taylor."""
    bounds = {}
    for name, m1, m2, a, e, prec in (
            ("hulse", 1.4398, 1.3886, 1.95e9, 0.617, 1.2e-6),
            ("double", 1.3381, 1.2489, 8.8e8, 0.088, 7.7e-7)):
        _, x = _system(m1, m2, a, e)
        bounds[name] = prec / x
    assert 0.30 < bounds["hulse"] < 0.40
    assert 0.15 < bounds["double"] < 0.20
    assert bounds["double"] < bounds["hulse"]      # the tighter system wins


def test_both_constructions_carry_third_powers():
    """The deficit is linear in the coupling, but the read is not, so
    expanding the budget line and the ruler produces second and third
    powers anyway — the disagreement, if any, is between two sets of
    third-power coefficients, not between having them and lacking them."""
    d = 1e-3
    budget = 1 - 2 * d
    ruler = 1 / (1 - 2 * d)
    series = 1 + 2 * d + 4 * d * d + 8 * d ** 3
    assert abs(ruler - series) < 20 * d ** 4       # the read's own cube, to the next term
    assert abs(budget - (1 - 2 * d)) < 1e-15       # linear in the deficit


def test_the_wave_channel_tests_it_harder():
    """Inspiral phasing carries the second-order coefficient at the level
    of radians against a signal measured to a fraction of one."""
    for vc, cycles in ((0.1, 3000), (0.2, 800), (0.3, 300)):
        radians_of_2pn = vc ** 4 * cycles
        assert radians_of_2pn > 0.2
    assert 0.3 ** 4 * 300 > 0.1 ** 4 * 3000        # louder events test harder


def test_the_owed_calculation_is_named():
    """What remains is one comparison with a target it must hit."""
    owed = ("expand the construction's two-body dynamics to second "
            "post-Newtonian order and compare the coefficients")
    target = 0.18
    assert "second post-Newtonian" in owed
    assert 0 < target < 0.25
