"""test_genesis_vii.py — Chapter VII pinned: the budget, the crest, the clash."""

from fractions import Fraction as F

from genesis_vii import (MEAS, OMEGA_B, OMEGA_DM, OMEGA_LAMBDA, OMEGA_M,
                         baryon_clash_pct, budget_closes, crest,
                         crest_redshifts, dm_from_sevenths,
                         hubble_ratio_vs_13_12, q0_seat)
from gtheory import transform


def test_the_budget_closes_exactly():
    """2/3 + 4/15 + 1/15 = 1: flatness is closure, not fine-tuning."""
    assert budget_closes()
    assert OMEGA_M == F(1, 3)


def test_the_budget_is_denominated_in_move_ones_interval():
    """The fifteenths: 57 - 42 = 15, the first operation's interval."""
    t = transform()
    assert t["internal_15"] == 15
    assert OMEGA_DM.denominator == OMEGA_B.denominator == 15


def test_the_dark_matter_seat_is_the_sevenths():
    assert dm_from_sevenths() == OMEGA_DM == F(4, 15)


def test_the_deceleration_seat():
    """q0 = 1/6 - 2/3 = -1/2 exactly."""
    assert q0_seat() == F(-1, 2)


def test_the_crest_is_exact_octave_thirds():
    """(1+z)^3 = 4 at acceleration onset, 2 at equality:
    z_accel = 4^(1/3) - 1, z_equal = 2^(1/3) - 1."""
    assert crest() == (4, 2)
    z_a, z_e = crest_redshifts()
    assert 0.585 < z_a < 0.590
    assert 0.259 < z_e < 0.261


def test_the_baryon_ledger_resolved():
    """The one displayed move: 1/15 splits 20|7 in 405ths; committed share
    (2/9)^2 = 4/81 vs measured 4.93% (+0.16%); Lambda_eff = 277/405 vs 68.5%
    (-0.11%); exact closure retained. Degeneracy honest (7/405 rides vacuum)."""
    committed = F(2, 9) ** 2
    moved = F(7, 405)
    assert F(1, 15) == committed + moved
    assert F(2, 3) + moved == F(277, 405)
    assert F(277, 405) + F(4, 15) + committed == 1
    assert abs(float(committed) - 0.0493) < 2e-4
    assert abs(float(F(277, 405)) - 0.6847) < 2e-3

def test_the_hubble_curiosity_parked():
    """73.04/67.4 sits within 4e-4 of 13/12 (loose grade) — noted, parked."""
    assert abs(hubble_ratio_vs_13_12()) < 5e-4


def test_the_wounds_first_anatomy_candidate():
    """Owed-ledger exploration (grade capped at signpost — 5 rivals in
    band): the baryon cell decomposes EXACTLY as 1/15 = (2/9)^2 + 7/405,
    with (2/9)^2 = 4/81 sitting +0.17% from the measured Omega_b.
    The problem STAYS OPEN; this pin records the candidate's arithmetic."""
    assert F(1, 15) == F(2, 9) ** 2 + F(7, 405)
    assert abs(float(F(4, 81)) - MEAS["b"]) / MEAS["b"] < 0.002


def test_ccs_catch_the_budget_is_the_tone_circle():
    """CC: '405 = 9/8 off 360.' Verified — and the seats on the plain
    circle are THE BANKED NUMBERS: Lambda = 240 (La's degree),
    dm = 96 (the wheel rung), b = 24 (the root). The budget IS the
    tone-circle partition; 405 is the circle overshot by Re, and the
    overshoot segment is 45."""
    assert 360 * F(9, 8) == 405
    assert 405 - 360 == 45
    assert (OMEGA_LAMBDA * 360, OMEGA_DM * 360, OMEGA_B * 360) == (240, 96, 24)
    assert (OMEGA_LAMBDA * 405, OMEGA_DM * 405, OMEGA_B * 405) == (270, 108, 27)


def test_the_wounds_full_anatomy_the_one_move():
    """On the overshot circle: seats (270|108|27); the measured budget
    sits at ~(277|107|20) — ONE MOVE: the seed 7 from the root cell to
    La's cell (dm's single unit ~ the neutrino share). After the move:
    b = (2/9)^2 (+0.16%), Lambda = 277/405 (-0.11%). The problem stays
    OPEN (the move's reading is degenerate with Lambda observationally)
    but its face is complete. Canonical Planck h = 0.6736 used; the
    stakes' dm value flagged for source re-check."""
    h2 = 0.6736 ** 2
    ob, oc, ol = 0.02237 / h2, 0.1200 / h2, 0.6847
    assert F(1, 15) - F(7, 405) == F(2, 9) ** 2
    assert F(2, 3) + F(7, 405) == F(277, 405)
    assert abs(float(F(4, 81)) - ob) / ob < 0.002        # +0.16%
    assert abs(float(F(277, 405)) - ol) / ol < 0.002     # -0.11%
    assert abs(float(F(4, 15)) - oc) / oc < 0.009        # +0.8% (dm unmoved)
    assert F(7, 405) / F(1, 15) == F(7, 27)              # seed over the cube


def test_the_cell_splits_as_the_hexad_halves():
    """The anatomy's structural anchor: the baryon cell's committed |
    uncommitted split (20 | 7 in 405ths) IS the banked hexad-halves
    split {8,7,5} = 20 | {1,2,4} = 7 — the muon block's own 207. An
    anchor to a banked object, not a scan."""
    committed, uncommitted = 20, 7
    assert F(committed, 405) == F(4, 81) == F(2, 9) ** 2
    assert F(uncommitted, 405) == F(7, 405)
    assert committed == 8 + 7 + 5                 # the heavy half
    assert uncommitted == 1 + 2 + 4               # the light half
    assert committed * 10 + uncommitted == 207    # the muon block's split


def test_the_neutrino_note_is_not_a_stake():
    """THE TRAP, pinned so it stays sprung: if the dm cell carried the
    neutrinos, Sum m_nu = (4/15 h^2 - 0.1200) x 93.14 eV — which swings
    from NEGATIVE to 0.3 eV across the current h band. Pure h-leverage
    is not a prediction; logged as consistency-note with a double wake."""
    smn = lambda h: (4 / 15 * h ** 2 - 0.1200) * 93.14
    assert smn(0.67) < 0                          # fails at low h
    assert 0.05 < smn(0.6736) < 0.15              # plausible at canonical h
    assert smn(0.68) > 0.25                       # explodes at high h


def test_the_mechanism_is_located_at_the_midy_fold():
    """The open problem's mechanism, located: the cell's 20|7 halves ARE the
    reptend's own Midy half-blocks 142|857 — the heavy half is the
    complement-image of the light half (9-d), and the fold between
    them (10^3 = -1 mod 7) is THE SAME FOLD as the first clean
    commitment (7 | 10^3 + 1, the depth-3 rounding of Chapter I).
    The residue, narrowed: derive the DIRECTION (why the post-fold
    half is the manifest share)."""
    light, heavy = (1, 4, 2), (8, 5, 7)
    assert sum(light) == 7 and sum(heavy) == 20
    assert tuple(9 - d for d in light) == heavy   # complement-image
    assert int("".join(map(str, light))) == 142   # the half-blocks are
    assert int("".join(map(str, heavy))) == 857   # the reptend's own
    assert 142 + 857 == 999                       # Midy's fold
    assert (10 ** 3 + 1) % 7 == 0                 # = the commitment fold


def test_ccs_catch_the_fold_is_directional():
    """CC: 'don't the Midy pairs split high/low — that's directional?'
    YES, and it closes the residue: each pair (1,8),(4,2... each pair
    (d, 9-d) has a lesser and a greater member; THE HEAVY HALF IS
    EXACTLY THE THREE GREATER MEMBERS; the threshold is 9/2 — the
    half; and the parity structure mirrors (light: 1 odd 2 even;
    heavy: 2 odd 1 even)."""
    pairs = ((1, 8), (4, 5), (2, 7))
    light, heavy = {1, 4, 2}, {8, 5, 7}
    for a, b in pairs:
        assert a + b == 9
        assert min(a, b) in light and max(a, b) in heavy
    assert all(d < 4.5 for d in light) and all(d > 4.5 for d in heavy)
    assert sum(1 for d in light if d % 2) == 1    # parity mirror: 1 odd
    assert sum(1 for d in heavy if d % 2) == 2    #               2 odd


def test_the_direction_is_the_rounding_rule():
    """THE RESIDUE CLOSES INTO A REGISTERED CHOICE: commitment is
    rounding; the engine's ROUNDING_RULE is half-UP (recorded in the
    CHOICES registry since the founding); at the fold the manifest
    representative of each pair is therefore the UPPER member — the
    manifest share is 8+5+7 = 20 of 27, the residue 1+4+2 = 7. The
    direction is not a floating mystery: it is the rule's own
    direction, inherited."""
    from gtheory import CHOICES
    assert CHOICES["ROUNDING_RULE"][0] == "half-up-at-depth"
    manifest = sum(max(p) for p in ((1, 8), (4, 5), (2, 7)))
    residue = sum(min(p) for p in ((1, 8), (4, 5), (2, 7)))
    assert (manifest, residue) == (20, 7)


def test_the_81_80_wake_fires_once():
    """CC's original syntonic conjecture, first construction-level
    appearance after the zero-hit sweep: the committed baryon share is
    ONE TWENTIETH FLATTENED BY THE SYNTONIC COMMA — (1/20)(80/81) =
    4/81 = (2/9)^2. Honest caveat pinned in prose: 80|81 adjacency
    makes the identity unremarkable ALONE; the content is that 1/20 is itself
    the banked 20 (the heavy half; La on the wheel). Grade: signpost."""
    assert F(1, 20) * F(80, 81) == F(4, 81) == F(2, 9) ** 2
    assert 8 + 7 + 5 == 20                        # the banked twentieth
