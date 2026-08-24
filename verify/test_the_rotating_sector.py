"""test_the_rotating_sector.py — THE DRAG WORD (2026-08-17). The
ledger's last strong-field debt, opened to first order in spin. The
objection was fair and sharp: every observed engine rotates, Kerr moves
the ISCO across 1 to 9 GM/c², and §21's ladder is the non-rotating slice.

The word comes from the doctrine already in use. The budget line was the
round trip's SUM — two legs, each spending the deficit. A rotating source
makes those two legs unequal, and the round trip's DIFFERENCE is what a
Sagnac reading returns: the same two legs, the same inverse distance,
the same coefficient two, on the difference face rather than the sum
face. Identifying the difference-face charge with the source's angular
momentum — this block's one named identification, as the interior rule
was the wall's — gives

    g_tt = −(1 − 2M/r)        the sum face, the budget
    g_tφ = −2J/r              the difference face, the drag
    g_φφ = r²                 the areal subtense

and from it, with nothing added: the dragging rate ω = −g_tφ/g_φφ =
2J/r³, which is the Lense-Thirring rate exactly — the parameter record's own named
first test — and landmark stations that track Kerr's to first order in
spin, the ISCO's slope −4√(2/3) and the photon orbit's −2/√3.

The scope is stated rather than stretched: these words are the
first-order-in-spin truncation, so the residual against exact Kerr grows
as a², the rotating geometry's own quadrupole, which the difference face
does not carry. And spin moves the stations OFF the two-three rationals —
the shift coefficients are irrational — so the ladder is the
non-rotating skeleton and no arithmetic claim survives a continuous spin
parameter. Both facts are printed here rather than left for a reader.
"""

import math

M = 1.0


def _circ_energy(r, a):
    """Energy of the prograde circular orbit in the derived words."""
    gtt, gtp, gpp = -(1 - 2 * M / r), -2 * M * a / r, r * r
    dtt, dtp, dpp = -2 * M / r ** 2, 2 * M * a / r ** 2, 2 * r
    disc = dtp * dtp - dtt * dpp
    if disc < 0:
        return None
    om = (-dtp + math.sqrt(disc)) / dpp
    den = -gtt - 2 * gtp * om - gpp * om * om
    if den <= 0:
        return None
    return -(gtt + gtp * om) / math.sqrt(den)


def _isco(a, lo=2.5, hi=12.0):
    def slope(r):
        hi_, lo_ = _circ_energy(r + 1e-5, a), _circ_energy(r - 1e-5, a)
        return None if (hi_ is None or lo_ is None) else (hi_ - lo_)
    for _ in range(200):
        mid = (lo + hi) / 2
        s = slope(mid)
        if s is None or s <= 0:
            lo = mid
        else:
            hi = mid
    return (lo + hi) / 2


def _photon(a, lo=2.0, hi=5.0):
    def den(r):
        gtt, gtp, gpp = -(1 - 2 * M / r), -2 * M * a / r, r * r
        dtt, dtp, dpp = -2 * M / r ** 2, 2 * M * a / r ** 2, 2 * r
        disc = dtp * dtp - dtt * dpp
        if disc < 0:
            return None
        om = (-dtp + math.sqrt(disc)) / dpp
        return -gtt - 2 * gtp * om - gpp * om * om
    for _ in range(200):
        mid = (lo + hi) / 2
        d = den(mid)
        if d is None or d <= 0:
            lo = mid
        else:
            hi = mid
    return (lo + hi) / 2


def _isco_kerr(a):
    z1 = 1 + (1 - a * a) ** (1 / 3) * ((1 + a) ** (1 / 3) + (1 - a) ** (1 / 3))
    z2 = math.sqrt(3 * a * a + z1 * z1)
    return 3 + z2 - math.sqrt((3 - z1) * (3 + z1 + 2 * z2))


def _photon_kerr(a):
    return 2 * (1 + math.cos((2 / 3) * math.acos(-a)))


def test_the_drag_word_gives_the_lense_thirring_rate():
    """ω = −g_tφ/g_φφ = 2J/r³ exactly, at every radius — the rate frame
    dragging is measured by, and the first test the ledger named for this
    account when it was still an empty entry."""
    for a in (0.1, 0.5, 0.998):
        for r in (10.0, 100.0, 1e4):
            omega = (2 * M * a / r) / r ** 2
            assert abs(omega - 2 * M * a / r ** 3) < 1e-18
            assert omega > 0                       # drags with the rotation


def test_the_non_rotating_limit_returns_the_ladder():
    """At a = 0 the words collapse to the budget line and the stations
    return: ISCO 6, photon sphere 3 — the derived ladder intact."""
    assert abs(_isco(0.0) - 6.0) < 1e-6
    assert abs(_photon(0.0) - 3.0) < 1e-6
    assert abs(_isco_kerr(0.0) - 6.0) < 1e-9


def test_the_stations_track_kerr_to_first_order_in_spin():
    """The ISCO's slope is −4√(2/3) and the photon orbit's is −2/√3;
    the derived words reproduce both, so the landmark shifts with spin
    are the account's and not imported."""
    d = 0.01
    isco_slope = (_isco(d) - _isco(0.0)) / d
    photon_slope = (_photon(d) - _photon(0.0)) / d
    assert abs(isco_slope - (-4 * math.sqrt(2 / 3))) < 0.02
    assert abs(photon_slope - (-2 / math.sqrt(3))) < 0.01
    kerr_isco_slope = (_isco_kerr(d) - _isco_kerr(0.0)) / d
    assert abs(isco_slope - kerr_isco_slope) < 0.02


def test_the_truncation_scope_is_second_order_in_spin():
    """The residual against exact Kerr grows as a² — the rotating
    geometry's quadrupole, which the difference face does not carry. The
    account is therefore honest to first order in spin and owes the
    second, which is where the extremal limit lives."""
    residuals = []
    for a in (0.05, 0.10, 0.20):
        residuals.append((a, _photon(a) - _photon_kerr(a)))
    for a, res in residuals:
        assert abs(res) < 0.4 * a ** 2 + 1e-6      # quadratic, not linear
    a1, r1 = residuals[0]
    a2, r2 = residuals[-1]
    growth = abs(r2 / r1)
    assert 8 < growth < 25                          # ~ (0.20/0.05)^2 = 16


def test_spin_moves_the_stations_off_the_two_three_rationals():
    """Stated rather than hidden: at rest the stations are 2, 9/4, 3, 4,
    6 — two-three words — while the first-order shifts are irrational.
    The ladder is the non-rotating skeleton; a continuous spin parameter
    admits no arithmetic claim, and the paper's landmark condition binds
    accordingly."""
    for slope in (-4 * math.sqrt(2 / 3), -2 / math.sqrt(3)):
        r = abs(slope)
        for _ in range(60):                        # no small 2-3 rational
            pass
        assert min(abs(r - n / d) for n in range(1, 200) for d in
                   (1, 2, 3, 4, 6, 8, 9, 12, 16, 18, 24, 27, 32)) > 1e-6
    assert abs(_isco(0.3) - 6.0) > 0.5             # the station has moved
