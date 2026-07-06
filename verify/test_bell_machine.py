"""Pins for the two-touch computation (bell_machine.py)."""

from fractions import Fraction as F

from bell_machine import (E_ledger, E_serial, B_marginal_serial, E_rand,
                          max_chsh, nonsignaling_max, touch_matrix,
                          comm_norm, strike_profile_overlap)

MENU = [2, 3, 4, 5, 6, 7]


def test_closed_forms_sane():
    # spot values, exact: the (2,7) pairing of the serial machine
    assert E_serial(2, 7) == F(1, 7)
    assert E_serial(7, 2) == F(6, 7)
    assert E_serial(7, 7) == 1 and E_serial(2, 2) == 1
    assert E_ledger(2, 2) == 1


def test_two_ledger_control_is_bell_classical():
    s, _ = max_chsh(E_ledger, MENU)
    assert s == 2      # exactly — the factorized machine obeys the theorem


def test_serial_machine_violates_only_by_telegraphing():
    s, t = max_chsh(E_serial, MENU)
    assert s == F(19, 7) and s == 2 + F(5, 7)     # the violation, exact
    assert t == (2, 7, 2, 7)                       # smallest vs largest prime on the menu
    qa, qa2, qb, qb2 = t
    sig = max(abs(B_marginal_serial(qa, q0) - B_marginal_serial(qa2, q0))
              for q0 in (qb, qb2))
    assert sig == F(6, 7)      # B's statistics betray A's choice — nature forbids this


def test_nonsignaling_slice_is_classical():
    assert nonsignaling_max(MENU) == 2     # silence the telegraph, lose the violation


def test_hidden_order_restores_classicality():
    s, _ = max_chsh(E_rand, MENU)
    assert s == 2      # the substrate's order, once unobservable, caps the machine


def test_filters_commute_strikes_do_not():
    # pure filters: diagonal in the mode basis -> parallel blocks, no 90 deg
    assert comm_norm(touch_matrix(1, 2, 0.0), touch_matrix(1, 3, 0.0)) < 1e-12
    # the strike law (probe injects) un-parallels them, linearly
    c1 = comm_norm(touch_matrix(1, 2, 0.25), touch_matrix(1, 3, 0.25))
    c2 = comm_norm(touch_matrix(1, 2, 0.5), touch_matrix(1, 3, 0.5))
    assert c1 > 1.0
    assert abs(c2 - 2 * c1) < 1e-9


def test_the_seed_supplies_the_right_angle():
    # sin(m*pi/2) exactly orthogonal to sin(m*pi/3) over full periods:
    # two-against-three IS the 90 degrees between the strike blocks
    assert abs(strike_profile_overlap()) < 1e-12


def test_observation_audit():
    import math
    from bell_machine import sharpness_threshold
    # rest ceiling 2 (pre-written), logical ceiling 4 (unpriced); the
    # physical ceiling is EXACTLY their geometric mean — half an octave
    # of dress above rest
    assert abs(2 * math.sqrt(2) - math.sqrt(2 * 4)) < 1e-12
    assert abs(1200 * math.log2(2 * math.sqrt(2) / 2) - 600.0) < 1e-9
    # the strike-strength audit: the violation is observation-powered,
    # with a pure binary-power threshold
    eta = sharpness_threshold()
    assert abs(eta ** 2 * 2 * math.sqrt(2) - 2) < 1e-12   # S(threshold) = rest
    assert abs(eta - 2 ** -0.25) < 1e-15


def test_the_ladder_of_wings():
    import math
    from bell_machine import mermin3_ceilings
    rest, phys = mermin3_ceilings()
    assert rest == 2                     # all 64 pre-written strategies
    assert abs(phys - 4.0) < 1e-6        # the Mermin operator norm
    # the ladder: each added orthogonal wing composes one more face
    # diagonal — ratio 2^((n-1)/2): sqrt2 at n=2, a FULL OCTAVE at n=3
    assert abs(phys / rest - 2 ** ((3 - 1) / 2)) < 1e-6
    assert abs(2 * math.sqrt(2) / 2 - 2 ** ((2 - 1) / 2)) < 1e-12


def test_nonsignaling_theorem_all_denominators():
    # not a menu census — a theorem: on the non-signaling set,
    # S = 2 - 4*(1/qa' - 1/lcm(qa',qb)) <= 2, every denominator
    import itertools as it
    from fractions import Fraction as Fr
    from bell_machine import E_serial, B_marginal_serial, chsh, _lcm
    for t in it.product(range(2, 11), repeat=4):
        qa, qa2, qb, qb2 = t
        if all(B_marginal_serial(qa, q0) == B_marginal_serial(qa2, q0)
               for q0 in (qb, qb2)):
            s = chsh(E_serial, *t)
            assert s <= 2
            assert s == abs(2 - 4 * (Fr(1, qa2) - Fr(1, _lcm(qa2, qb))))


def test_telegraph_supremum_is_three():
    # the signaling machine's true ceiling: the family (2, 2p, 2, p)
    # gives S = 3 - 1/p exactly — supremum 3, never attained
    from fractions import Fraction as Fr
    from bell_machine import E_serial, chsh
    for p in (3, 7, 13, 101):
        assert chsh(E_serial, 2, 2 * p, 2, p) == 3 - Fr(1, p)


def test_fourth_wing_third_rung():
    import math
    from bell_machine import mk4_ceilings
    rest, phys = mk4_ceilings()
    assert rest == 1                             # MK normalization: all 256 strategies
    assert abs(phys - 2 ** 1.5) < 1e-5           # 2^((4-1)/2): +1800 cents
    assert abs(1200 * math.log2(phys / rest) - 1800) < 0.1


def test_right_angle_closes_on_the_hexad():
    import math
    from bell_machine import strike_profile_overlap
    # exact zero on hexad registers; a broken register leaks sqrt(3)/2
    for n in (24, 30, 36, 6):
        assert abs(strike_profile_overlap(n)) < 1e-12
    assert abs(strike_profile_overlap(25) - math.sqrt(3) / 2) < 1e-12
