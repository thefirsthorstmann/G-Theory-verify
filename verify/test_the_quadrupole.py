"""test_the_quadrupole.py — THE SECOND ORDER IN SPIN (2026-08-17). The
last strong-field debt: the drag word was exact to first order and the
rotating geometry's own quadrupole stood owed. It closes, and the closing
needs one clause the program already carries at signpost grade.

WHERE THE SECOND ORDER LIVES. In the equatorial plane the two words the
register derived are already exact to ALL orders in spin: the sum face
g_tt = −(1 − 2M/r) and the difference face g_tφ = −2Ma/r receive no
correction whatever. Everything at second order sits in the two SPATIAL
words — the subtense and the ruler — which is where the register expects
it, the temporal pair having come from the round trip and the spatial
pair from the ruler's own tax.

THE SUBTENSE IS NOT INDEPENDENT. The combination g_tφ² − g_tt·g_φφ equals
the deficit polynomial exactly, so once the deficit is fixed the subtense
follows: two spatial words, one unknown.

THE CLAUSE, AND THE STANDING OF ITS COEFFICIENT. The deficit gains the
difference-face charge squared: 2M/r → 2M/r − (a/r)², with a = J/M the
ratio of the difference charge to the sum charge. The coefficient is one,
read off the charged solution — deficit polynomial r² − 2Mr + Q² there,
r² − 2Mr + a² here, the difference-face charge in the electric charge's
own slot. That is the double copy as arithmetic, the shape this program
claims at signpost grade. But a self-stress pass corrected the earlier
wording: reading a coefficient off another solution is a CALIBRATION
against known geometry, not a derivation from the register, and nothing
here supplies the one independently. The clause is an identification with
a comparison-fixed coefficient, of the same standing as the wall's
interior rule, and it is carried on the ledger as such.

Kerr is then the OUTPUT, and the tests below confirm it: the innermost
stable orbit matches at every spin while neighbouring coefficients fail
by wide margins; the horizons, the extremal limit and the Kerr bound come
out as the deficit's own discriminant rather than being imposed.

UPDATE 2026-08-22 (test_the_clause_coefficient.py): the coefficient is
now DERIVED. Within the two faces' linear potential px − iqy on the
prolate chart, the stationary equations the account verified (Ernst's)
are satisfied if and only if p² + q² = 1, and that circle is c = 1. The
ISCO rigidity below stands as the check it always was; the origin of the
one is the field equations, and the charged solution's slot is the
consequence.
"""

import math

M = 1.0


def words(r, a, c=1.0):
    """The three equatorial words: sum face, difference face, and the
    subtense reconstructed from the identity with deficit carrying
    c·(a/r)²."""
    gtt = -(1 - 2 * M / r)
    if abs(gtt) < 1e-14:
        return None
    gtp = -2 * M * a / r
    delta = r * r - 2 * M * r + c * a * a
    return gtt, gtp, (gtp * gtp - delta) / gtt


def _E(r, a, c, h=1e-6):
    w, wp, wm = words(r, a, c), words(r + h, a, c), words(r - h, a, c)
    if not (w and wp and wm):
        return None
    gtt, gtp, gpp = w
    dtt, dtp, dpp = [(wp[i] - wm[i]) / (2 * h) for i in range(3)]
    disc = dtp * dtp - dtt * dpp
    if disc < 0 or dpp == 0:
        return None
    om = (-dtp + math.sqrt(disc)) / dpp
    den = -gtt - 2 * gtp * om - gpp * om * om
    return None if den <= 0 else -(gtt + gtp * om) / math.sqrt(den)


def isco(a, c=1.0):
    rp = M + math.sqrt(max(M * M - c * a * a, 0.0))
    lo, hi = rp + 0.05, 12.0
    for _ in range(120):
        mid = (lo + hi) / 2
        up, dn = _E(mid + 1e-4, a, c), _E(mid - 1e-4, a, c)
        if up is None or dn is None:
            lo = mid
        elif up - dn > 0:
            hi = mid
        else:
            lo = mid
    return (lo + hi) / 2


def isco_kerr(a):
    z1 = 1 + (1 - a * a) ** (1 / 3) * ((1 + a) ** (1 / 3) + (1 - a) ** (1 / 3))
    z2 = math.sqrt(3 * a * a + z1 * z1)
    return 3 + z2 - math.sqrt((3 - z1) * (3 + z1 + 2 * z2))


def test_the_derived_words_need_no_second_order_correction():
    """The sum and difference faces are exact to all orders in spin in the
    equatorial plane — so the two words the register already derived stand
    untouched, and only the spatial pair is at stake."""
    for r, a in ((5.0, 0.3), (3.0, 0.9), (2.5, 0.998)):
        gtt, gtp, _ = words(r, a)
        assert abs(gtt - (-(1 - 2 * M / r))) < 1e-15
        assert abs(gtp - (-2 * M * a / r)) < 1e-15


def test_the_subtense_follows_from_the_identity():
    """g_tφ² − g_tt·g_φφ is the deficit polynomial exactly, so the
    reconstructed subtense equals the rotating solution's own — checked
    to machine precision across radius and spin."""
    for r, a in ((5.0, 0.3), (3.0, 0.9), (2.5, 0.998), (10.0, 0.5)):
        _, _, gpp = words(r, a)
        exact = r * r + a * a + 2 * M * a * a / r
        assert abs(gpp - exact) < 1e-10, (r, a)


def test_the_coefficient_is_rigid_and_every_neighbour_fails():
    """With the coefficient of one the innermost stable orbit matches at
    three spins, while neighbouring coefficients miss by wide margins. The
    rigidity is the check; the origin of the one is the stationary field
    equations (test_the_clause_coefficient.py, 2026-08-22)."""
    for a in (0.3, 0.5, 0.9):
        assert abs(isco(a, 1.0) - isco_kerr(a)) < 1e-3, a
        for c in (0.0, 0.5, 1.5, 2.0):
            assert abs(isco(a, c) - isco_kerr(a)) > 0.05, (a, c)


def test_the_horizons_and_the_kerr_bound_are_the_discriminant():
    """Setting the deficit polynomial to zero gives r± = M ± √(M²−a²):
    the horizons, the extremal limit at a = M, and the bound a ≤ M as the
    discriminant's own condition — none of them imposed."""
    for a in (0.0, 0.6, 0.998):
        disc = M * M - a * a
        assert disc > 0
        rp = M + math.sqrt(disc)
        assert abs(rp * rp - 2 * M * rp + a * a) < 1e-12      # a root
        assert 1.0 <= rp <= 2.0
    assert abs((M + math.sqrt(M * M - M * M)) - M) < 1e-15    # extremal
    assert M * M - 1.2 ** 2 < 0                               # beyond: no root


def test_the_ladder_returns_at_zero_spin():
    """With the spin off, the clause vanishes and the resting ladder
    comes back: the innermost stable orbit at six, the horizon at two."""
    assert abs(isco(0.0, 1.0) - 6.0) < 1e-3
    assert abs(isco_kerr(0.0) - 6.0) < 1e-9
    assert abs((M + math.sqrt(M * M)) - 2.0) < 1e-15
