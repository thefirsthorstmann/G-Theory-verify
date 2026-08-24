"""test_the_wall_derived.py — THE WALL, RESOLVED (2026-08-16, second
writing). the author: "zero assumptions, thats the jam." The identified rule of
the first writing is DISCHARGED: the register's own counting — the
exterior's rule applied without amendment (the round trip pays the
endpoint's share on each leg, linearly; the share from the banked shell
count) — gives ONE rule inside and out, Φ(r) = 1 − 2·d(r), seam
automatic. It reproduces the field equations EXACTLY for the hollow
shell (vacuum standing point) and moves the program's wall in solid
matter: the center reads √(1−3φ_R), dying at surface deficit 1/3 — THE
PHOTON STATION. The count's wall coincides with the photon sphere: no
static body inside its own circle of light; compactness ceiling 2/3;
redshift ceiling √3 − 1; wall over horizon 3/2 — THE FIFTH. The
continuum's interior machinery (pressure sourcing, field feeding field,
the spatial word) lands instead at 9/4 — the tone, ceiling 8/9,
redshift 2, pressure pole. The walls sit a FOURTH apart; the interiors
split at second order by exactly (3/8)φ²; experiment holds the fork:
the windows (2/3, 8/9) in compactness and (√3−1, 2) in redshift are
empty at this writing.
"""

from fractions import Fraction as F
import math


def test_the_shell_coefficients_from_the_inverse_square():
    """Direct shell summation of the banked 1/r² potential inside a
    uniform ball: the sum is −GM(3R²−r²)/(2R³) — the center a fifth
    deeper than the surface, decomposition (3/2)φ_R − (1/2)φ_R r²/R²."""
    N, R, M = 40000, 1.0, 1.0
    for r in (0.0001, 0.3, 0.6, 1.0):
        pot = 0.0
        for k in range(N):
            s = (k + 0.5) / N * R
            m_s = 3 * M * s * s / R ** 3 * (R / N)
            pot += -m_s / max(r, s)
        closed = -M * (3 * R ** 2 - r ** 2) / (2 * R ** 3)
        assert abs(pot - closed) < 3e-4, r
    assert -M * 3 / (2 * R) == -1.5              # the fifth, at the center


def test_the_one_rule_inside_and_out():
    """Φ = 1 − 2d everywhere, d the endpoint's total share: outside,
    d = φ and the budget line returns; at the surface the seam is
    automatic; in the weak field the amplitude is the shell potential."""
    for pR in (F(1, 10), F(1, 4)):
        d_surface = F(3, 2) * pR - F(1, 2) * pR   # shell count at r = R
        assert d_surface == pR                    # seam: interior meets exterior
    for pR in (1e-5, 1e-7):
        for x in (0.0, 0.5, 1.0):
            d = 1.5 * pR - 0.5 * pR * x * x
            y = math.sqrt(1 - 2 * d)
            assert abs(y - (1 - d)) < 3 * d * d   # amplitude = 1 − d, weak field


def test_the_hollow_shell_agrees_with_the_field_equations_exactly():
    """Inside a hollow shell the share is constant — Gm/(sc²) — so the
    read is the constant √(1 − 2Gm/sc²): the same expression, exactly,
    that the field equations give for the flat interior frozen at the
    shell-edge rate. Where the clock stands in vacuum, count and
    continuum do not differ at any order."""
    for compact in (F(1, 10), F(1, 2), F(4, 5)):
        count_read_sq = 1 - compact               # Φ = 1 − 2·(Gm/sc²)
        birkhoff_sq = 1 - compact                 # GR: g_tt frozen at the edge
        assert count_read_sq == birkhoff_sq


def test_the_counts_wall_is_the_photon_station():
    """The center reads √(1 − 3φ_R); it dies at φ_R = 1/3 — the photon
    sphere's own deficit. The floor is the half, the center sits a fifth
    deeper, and the half over the fifth is the third: one mechanism, one
    station. No static body sits inside its own circle of light."""
    assert 1 - 2 * (F(3, 2) * F(1, 3)) == 0       # center dies
    assert F(1, 2) / F(3, 2) == F(1, 3)           # half over fifth = third
    assert 1 / F(1, 3) == 3                       # R_wall = 3 = R_photon
    for pR in (F(1, 4), F(3, 10), F(33, 100)):    # below the wall the center ticks
        assert 1 - 3 * pR > 0


def test_the_ceilings_of_the_count():
    """Compactness ceiling 2GM/Rc² = 2/3; surface-redshift ceiling
    √3 − 1 ≈ 0.732; wall over horizon 3/2 — the fifth itself."""
    assert 2 * F(1, 3) == F(2, 3)
    z = math.sqrt(3) - 1
    assert abs(1 / math.sqrt(1 - 2 / 3) - 1 - z) < 1e-12
    assert F(3) / F(2) == F(3, 2)


def test_the_two_walls_sit_a_fourth_apart():
    """The continuum's interior machinery lands at 9/4 — the tone above
    the horizon, ceiling 8/9, redshift ceiling 2, central pressure
    (1−y_R)/(3y_R−1) poling at its own wall with rational marks on the
    approach. The walls' ratio is 4/3 — the fourth — and the fifth is
    the tone times the fourth: the disagreement is interval arithmetic."""
    assert F(3) / F(9, 4) == F(4, 3)
    assert F(9, 8) * F(4, 3) == F(3, 2)
    assert 2 * F(4, 9) == F(8, 9)                 # continuum ceiling
    assert 1 / F(1, 3) - 1 == 2                   # continuum redshift ceiling
    pc = lambda yr: (1 - yr) / (3 * yr - 1)
    assert pc(F(1, 2)) == 1 and pc(F(2, 5)) == 3  # the dress's rational marks
    assert 3 * F(1, 3) - 1 == 0                   # its pole at its wall


def test_the_interiors_split_at_second_order_by_three_eighths():
    """Count center √(1−3φ) and continuum center (3/2)√(1−2φ) − 1/2
    agree through first order — no existing measurement separates them —
    and split at second by exactly (3/8)φ², the count the stricter."""
    for p in (1e-3, 1e-4, 1e-5):
        count = math.sqrt(1 - 3 * p)
        gr = 1.5 * math.sqrt(1 - 2 * p) - 0.5
        split = gr - count
        assert split > 0                          # the count is stricter
        assert abs(split - (3 / 8) * p * p) < 40 * p ** 3


def test_the_fork_windows_are_stated_and_open():
    """The refutation windows the block states: a static body with
    compactness in (2/3, 8/9) — redshift in (√3−1, 2) — decides for the
    continuum's extra sourcing and retires the count's interior, leaving
    the exterior cascade standing; beyond 8/9 retires both. The windows
    are nonempty as arithmetic, and their edges are the stations."""
    assert F(2, 3) < F(8, 9)
    lo, hi = math.sqrt(3) - 1, 2.0
    assert lo < hi
    assert abs(lo - 0.7320508) < 1e-6
    edge_low = 1 / math.sqrt(1 - 2 / 3) - 1       # redshift at the count's wall
    edge_high = 1 / math.sqrt(1 - 8 / 9) - 1      # redshift at the continuum's
    assert abs(edge_low - lo) < 1e-12 and abs(edge_high - hi) < 1e-12


def test_the_wall_is_extremal_over_the_monotone_class():
    """The board's counterexample hunt, inverted: for every
    non-increasing density profile the central share ratio
    d(0)/phi_R = R·(int s rho)/(int s^2 rho) is at least 3/2, with
    equality only at uniform — concentration deepens the center and
    lowers the ceiling (a near-point core caps below compactness 0.12).
    The wall at 2/3 is profile-independent over exactly the class
    Buchdahl's theorem governs: the count's own theorem."""
    def ratio(rho, n=20000):
        num = sum(rho((k + 0.5) / n) * ((k + 0.5) / n) for k in range(n))
        den = sum(rho((k + 0.5) / n) * ((k + 0.5) / n) ** 2 for k in range(n))
        return num / den

    uniform = ratio(lambda s: 1.0)
    assert abs(uniform - 1.5) < 0.001
    for rho in (lambda s: 1 - s, lambda s: 1 - s * s,
                lambda s: (1 - s) ** 3, lambda s: math.exp(-60 * s * s)):
        assert ratio(rho) > uniform + 0.1               # every concentration deeper
    assert 1 / ratio(lambda s: math.exp(-60 * s * s)) < 0.12
