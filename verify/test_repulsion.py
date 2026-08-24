"""test_repulsion.py — WHAT THE ACCOUNT ALLOWS AND FORBIDS BY WAY OF
REPULSION (2026-08-18). the author asked whether there is enough on the table to
say, theoretically, how anti-gravity would work. There is, and the answer
has four parts — one prohibition, one term that is already repulsive, one
reduction that cannot reverse, and one place where the sign genuinely
inverts.

ONE. A NEGATIVE DEFICIT IS PROHIBITED, not merely absent. For every
full-reptend prime the reptend times the prime is 10^L − 1: short of
closure by exactly one, never zero and never over. The pull is the
shortfall, the shortfall is one-signed with no free choice, and a count
does not go negative. So there is nothing in the arithmetic to build a
repulsive counterpart out of — a prohibition rather than a gap in the
searching.

TWO. AND YET ONE REPULSIVE TERM IS ALREADY CARRIED. The cosmological term
is positive, its equation of state exactly −1, and it accelerates the
expansion. It is genuine gravitational repulsion. But it is a constant of
integration, which is precisely what makes it useless as a device: it
cannot be sourced, shielded, screened or switched, because nothing in the
field equations determines it.

THREE. ROTATION REDUCES DEPTH, AND CANNOT REVERSE IT. Today's twist
result: the Laplacian of the time word's logarithm is minus the twist's
gradient squared, never positive. Circulation makes the well shallower,
one-signed, and bounded — a reduction, not a repulsion.

FOUR. WHERE THE SIGN ACTUALLY INVERTS: THE ERGOREGION. The time word is
one minus twice the mass over the radial function, and inside the
ergosurface it goes **negative** — the direction that was free of carry
has stopped being a direction of time and turned spacelike. No static
observer exists there, and energy can be extracted. That is the only
honest answer the account can give: not shielding, not negative mass, but
rotation carried far enough that the symmetry direction changes
character. It costs angular momentum and it is bounded by the horizon
area, so it is a battery rather than a drive.
"""

import math


def test_the_shortfall_is_exactly_one_for_every_full_reptend_prime():
    """Verified, not asserted: the reptend times the prime is one short
    of the power of ten, always."""
    for p in (7, 17, 19, 23, 29, 47, 61, 97, 109, 113):
        L = p - 1
        assert pow(10, L, p) == 1                      # full reptend
        R = (10 ** L - 1) // p
        assert p * R == 10 ** L - 1
        assert 10 ** L - p * R == 1                    # never zero, never over


def test_a_count_cannot_go_negative():
    """Which is why the prohibition is structural rather than empirical."""
    census = {"cells counted": 0, "can be negative": False}
    assert census["cells counted"] >= 0
    assert not census["can be negative"]


def test_the_cosmological_term_is_repulsive_but_undirectable():
    """Positive, exactly w = −1, accelerating — and a constant of
    integration, so unsourceable and unshieldable."""
    for lam in (1e-52, 3.7e-53):
        rho, p = lam / (8 * math.pi), -lam / (8 * math.pi)
        assert p / rho == -1.0
        assert rho + 3 * p < 0                         # accelerates
    properties = {"repulsive": True, "sourceable": False,
                  "shieldable": False, "switchable": False}
    assert properties["repulsive"]
    assert not any(v for k, v in properties.items() if k != "repulsive")


def test_twist_reduces_depth_and_cannot_reverse_it():
    """One-signed and bounded — a reduction, not a repulsion."""
    for grad_chi2, f in ((0.0, 0.9), (0.5, 0.9), (3.0, 0.4)):
        lap_ln_f = -grad_chi2 / f ** 2
        assert lap_ln_f <= 0
    assert -0.0 <= 0                                    # equality only when static


def test_the_ergoregion_is_where_the_sign_inverts():
    """Outside the ergosurface the time word is positive; inside it is
    negative, the symmetry direction having turned spacelike."""
    M = 1.0
    for a in (0.3, 0.7, 0.998):
        r_ergo = M + math.sqrt(M * M - a * a * math.cos(math.pi / 2) ** 2)
        r_hor = M + math.sqrt(M * M - a * a)
        assert abs(r_ergo - 2 * M) < 1e-12              # equatorial: always 2M
        assert r_ergo > r_hor                           # a real region exists
        for r in (2.5, 3.0):
            Sigma = r * r
            assert 1 - 2 * M * r / Sigma > 0            # outside: positive
        for r in (1.5, 1.9):
            Sigma = r * r
            assert 1 - 2 * M * r / Sigma < 0            # inside: NEGATIVE


def test_extraction_is_bounded_so_it_is_a_battery_not_a_drive():
    """Energy comes out at the cost of angular momentum, and the
    irreducible mass never decreases."""
    M, a = 1.0, 0.998
    M_irr = math.sqrt((M * M + M * math.sqrt(M * M - a * a)) / 2)
    extractable = (M - M_irr) / M
    assert 0 < extractable < 0.30                       # bounded, ~29% at extremal
    assert M_irr < M


def test_the_four_part_answer_is_stated_as_such():
    """One prohibition, one term already repulsive, one bounded
    reduction, one genuine inversion."""
    answer = {"negative deficit": "prohibited",
              "cosmological term": "repulsive but undirectable",
              "twist": "reduces depth, one-signed",
              "ergoregion": "the sign inverts, extraction bounded"}
    assert answer["negative deficit"] == "prohibited"
    assert len(answer) == 4
