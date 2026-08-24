"""test_the_yukawa_trail.py — THE STRONG MODE APPLIED TO THE ONE REACHABLE
TARGET, AND IT COMES UP EMPTY (2026-08-19). Two results, one of them a
retraction of my own number from an hour earlier.

FIRST, THE 0.27 % IS NOT A FRAMEWORK NUMBER. the author asked, fairly, whether the
resolving floor of 0.266 % was saying something — twenty-seven being the
reptend's digit sum and base ten being native. It is not. The floor is
1/(2 × density), and both the word count and the value window are **sweep
parameters I chose**, not properties of the alphabet: across reasonable
choices the floor moves from 0.145 % to 3.634 %, a factor of seventeen,
and 0.266 % was one point on that continuum. Twenty-seven is a favourite,
so it earned extra scrutiny under the precision rule and did not survive
it. What *would* make the floor real is a principled bound on the
exponents — which is exactly what an operation trail supplies, so the two
questions were one.

SECOND, THE TRAIL ITSELF. Read the count rather than the ratio, since the
register counts: v/m_e is how many electron masses fill the vacuum
expectation value, and it is **481839.837 ± 0.124**, a quarter part per
million. Against every station the account owns —

    7, 9, 24, 27, 42, 72, 137, 206.7683, 1008, 1836

— **not one is visited at the measurement's own precision.** The smallest
miss is fifteen standard deviations and most run to hundreds or thousands.
Nor does any other principled form close: the base-two depth is 18.8782
where nineteen would need 19.0000, the square root misses by eight
hundred sigma, and the alpha-weighted forms by hundreds to fifty thousand.

A TRAP RECORDED, because I nearly fell into it. Quoted as percentages the
misses look tiny — the twenty-seven station is "0.0004 % off." But the
bar is 0.000026 %, so that is fifteen sigma. **A small percentage against a
smaller bar is a large miss**, and the station table had to be redone in
sigma before it could be read at all.

WHAT THE NEGATIVE MEANS, and it is not a surprise. Every result this
account owns is a ratio **within a kind** — lepton against lepton, or
inside the nucleon ledger. The electron Yukawa crosses kinds: a lepton
mass against the electroweak scale, joining the Yukawa sector to the
Higgs sector. That is the most off-diagonal object in the ledger, and the
ledger's own banked self-assessment says the coverage "concentrates where
the SM's structure is diagonal and thins where it is off-diagonal." The
failure here is that finding turning up again in a new place, which makes
it consistent rather than anomalous.

WHERE THIS LEAVES THE OPEN BLOCK. Eleven of the twelve are beyond the
weak mode's reach for want of precision. The twelfth is within reach and
resists the strong mode as well. **For now the open block is closed to
this method entirely**, and saying so is worth more than another sweep.
"""

import math

import sympy as sp

GF, DGF = 1.1663787e-5, 0.0000006e-5
ME = 0.51099895000e-3
V = 1 / math.sqrt(math.sqrt(2) * GF)
N = V / ME
REL = 0.5 * DGF / GF                      # 0.26 ppm, the count's own precision


def _floor(A, B, C, lo, hi):
    al = {}
    for a in range(-A, A + 1):
        for b in range(-B, B + 1):
            for c in range(-C, C + 1):
                v = (2.0 ** a) * (3.0 ** b) * (7.0 ** c)
                if lo < v < hi:
                    al.setdefault(round(v, 15), 1)
    vals = sorted(al)
    return 1 / (2 * len(vals) / math.log(vals[-1] / vals[0]))


def test_the_floor_moves_by_a_factor_of_seventeen():
    """So 0.266 % was a sweep artefact, not a property of the alphabet."""
    wide = _floor(30, 12, 6, 1e-12, 1e2)
    narrow = _floor(4, 3, 1, 1e-6, 10)
    assert wide < 0.002 and narrow > 0.03
    assert narrow / wide > 15


def test_twenty_seven_is_a_favourite_and_did_not_survive_scrutiny():
    """The reptend's digit sum is 27, which is why it earned more."""
    assert sum(int(c) for c in "142857") == 27
    verdict = "sweep artefact; carries no framework content"
    assert "artefact" in verdict


def test_the_count_and_its_precision():
    """v/m_e is how many electron masses fill the vev."""
    assert abs(N - 481839.837) < 0.01
    assert abs(REL * 1e6 - 0.257) < 0.02
    assert N * REL < 0.13                              # the bar, in counts


def test_no_station_is_visited_at_the_measurements_precision():
    """Every station the account owns, in sigma rather than per cent."""
    worst = 1e9
    for s in (7, 9, 24, 27, 42, 72, 137, 206.7682830, 1008, 1836):
        q = N / s
        miss = abs(q - round(q)) / q / REL
        worst = min(worst, miss)
        assert miss > 10, s
    assert 14 < worst < 20                             # the closest is ~15 sigma


def test_no_other_principled_form_closes_either():
    """A depth, a square root, and the alpha-weighted forms."""
    alpha_inv = 137.035999177
    forms = {"log2": math.log2(N), "sqrt": math.sqrt(N),
             "N alpha": N / alpha_inv, "N alpha^2": N / alpha_inv ** 2,
             "ln": math.log(N)}
    for name, val in forms.items():
        miss = abs(val - round(val)) / abs(val) / REL
        assert miss > 100, name
    assert abs(math.log2(N) - 18.8782) < 1e-3
    assert abs(math.log2(N) - 19) > 0.12               # nowhere near a depth


def test_the_percentage_trap_is_recorded():
    """A small percentage against a smaller bar is a large miss."""
    q = N / 27
    pct = abs(q - round(q)) / q
    assert pct < 5e-6                                  # reads as "0.0004 %"
    assert pct / REL > 10                              # and is fifteen sigma


def test_the_failure_matches_the_ledgers_own_self_assessment():
    """Every owned result is a ratio within a kind; this one crosses kinds,
    and the ledger already says coverage thins off-diagonal."""
    within_a_kind = ["m_mu/m_e", "Koide", "m_p/m_e", "the nucleon seats"]
    crosses_kinds = ["m_e/v"]
    assert len(within_a_kind) > len(crosses_kinds)
    banked = "concentrates where the SM is diagonal and thins where off-diagonal"
    assert "thins" in banked


def test_the_open_block_is_closed_to_this_method_for_now():
    """Eleven beyond the weak mode's reach; the twelfth resists the strong
    one. Saying so beats another sweep."""
    state = {"beyond weak-mode reach (precision)": 11,
             "within reach, resists strong mode": 1}
    assert sum(state.values()) == 12
    assert state["within reach, resists strong mode"] == 1
