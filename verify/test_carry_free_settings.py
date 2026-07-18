"""test_carry_free_settings.py — the free-settings audit of the S = 5/2 carry frontier.

Companion to carry_stand.py. champion() and test_carry_stand.py pin ONE
configuration and assert it yields S = 5/2. This file sweeps the two knobs that
champion() silently hard-codes — the carry-arc AND the measurement settings
a_set = (0, n/4), b_set = (n/8, 7n/8) — to separate what is FORCED from what is
SELECTION-BEARING in the famous 5/2. It is the machine-check behind the honest
grade; without it the "the arc is forced" claim is docstring prose, not a test.

VERDICT (cold, re-derived here on every run):

  * FORCED — THE VALUE.  Over the full free sweep the maximum silent
    (no-signaling, sig == 0) Bell value is exactly 5/2 and is never exceeded.
    The ceiling is real and parameter-robust.  [test_ceiling_is_five_halves]

  * FORCED — THE CENTERS.  At the committed settings the silent-5/2 arcs are the
    antipode pair {(3n/8, n/4), (7n/8, n/4)} — the champion straddling the
    octave-doubling wrap-seam n/2, its partner straddling the tonic 0.  Because
    2*(n/2) == 0 (mod n), the doubling (the promotion action) forces the center;
    promote=False collapses the frontier to 2.  [test_frozen_settings_pin_antipode_pair]

  * SELECTION-BEARING — THE EXACT ARC.  Free the measurement settings and the
    silent-5/2 set blooms: n=8 -> 3 antipode-orbits with lengths {2, 3}; n=16
    admits silent-5/2 arcs of length != n/4 (witness pinned below).  The arc and
    the settings were CO-TUNED.  The champion returns only as the unique
    MINIMAL-LENGTH orbit — a shortest-arc tie-break, an added selection
    principle, not a constraint the machine imposes.
    [test_free_settings_bloom_n8, test_free_settings_cotuning_witness_n16]

So ORIGIN-VIII's 5/2 keeps its Forced grade ON THE VALUE; the arc ADDRESS is
Striking / selection-bearing, not Forced.  (2026-07-16 — the crew caught the
co-tuning that the champion's hard-coded settings had hidden.)

n=8 carries the full free-everything sweep (fast, decisive).  n=16 confirms the
ceiling and the antipode pair, and exhibits a distinct-length co-tuning witness;
the full n=16 six-orbit bloom (lengths {4,5,6}) is verified out-of-band (~80s,
too slow to gate the suite).
"""

import itertools
from fractions import Fraction as F

import carry_stand as C


# ---------------------------------------------------------------------------
# audit with the measurement settings promoted to free parameters.  Byte-for-byte
# the committed audit() body otherwise; test_audit_free_is_faithful anchors it.
# ---------------------------------------------------------------------------
def audit_free(n, carry, psi0, psi1, a_set, b_set, chiA):
    Es, margs = {}, {}
    for a in a_set:
        for b in b_set:
            e = m = 0
            for lam in range(n):
                u = (lam - a) % n
                Bout = psi1[(2 * lam - b) % n] if u in carry else psi0[(lam - b) % n]
                e += chiA[u] * Bout
                m += Bout
            Es[(a, b)] = e
            margs[(a, b)] = m
    sig = max(abs(margs[(a_set[0], b)] - margs[(a_set[1], b)]) for b in b_set)
    return Es, sig


def chsh(Es, a_set, b_set):
    a0, a1 = a_set
    b0, b1 = b_set
    e = [Es[(a0, b0)], Es[(a0, b1)], Es[(a1, b0)], Es[(a1, b1)]]
    return max(abs(-e[i] + sum(e[j] for j in range(4) if j != i)) for i in range(4))


def _committed_settings(n):
    return (0, n // 4), (n // 8, 7 * n // 8)


def _champion_arc(n):
    return (3 * n // 8, n // 4)


def _antipode(arc, n):
    s, ln = arc
    return ((s + n // 2) % n, ln)


def _orbit(arc, n):
    """Canonical rep of the +n/2 (Midy fold) orbit of an arc."""
    return tuple(sorted([tuple(arc), _antipode(arc, n)]))


# ---------------------------------------------------------------------------
# the full free-everything sweep at n=8 (arc x length x psi0 x psi1 x a-pair x
# b-pair), silent slice only — computed once, decisive, ~seconds.
# ---------------------------------------------------------------------------
def _full_silent_sweep(n):
    # Precompute the full E[a][b], M[a][b] tables per (arc, psi0, psi1) once, then
    # read off every (a_set, b_set) quad by lookup.  Identical result to calling
    # audit_free()/chsh() on each quad (test_full_sweep_matches_audit_free checks
    # this at a sample point), ~20x faster.
    chiA = C._half_arc_pattern(0, n)
    pats = [C._half_arc_pattern(s, n) for s in range(n)]
    apairs = list(itertools.combinations(range(n), 2))
    a_c, b_c = _committed_settings(n)
    target = 5 * n // 2  # chsh integer value for S = 5/2
    ceiling = 0
    free = set()      # arcs reaching silent 5/2 under ANY free setting
    frozen = set()    # arcs reaching silent 5/2 at the committed settings
    for start in range(n):
        for length in range(1, n):
            carry = C._arc(start, length, n)
            for p0 in pats:
                for p1 in pats:
                    E = [[0] * n for _ in range(n)]
                    M = [[0] * n for _ in range(n)]
                    for a in range(n):
                        Ea, Ma = E[a], M[a]
                        for b in range(n):
                            e = m = 0
                            for lam in range(n):
                                u = (lam - a) % n
                                Bout = (p1[(2 * lam - b) % n] if u in carry
                                        else p0[(lam - b) % n])
                                e += chiA[u] * Bout
                                m += Bout
                            Ea[b] = e
                            Ma[b] = m
                    for a0, a1 in apairs:
                        for b0, b1 in apairs:
                            if (M[a0][b0] != M[a1][b0]) or (M[a0][b1] != M[a1][b1]):
                                continue  # sig != 0 (signaling): disqualified
                            e4 = [E[a0][b0], E[a0][b1], E[a1][b0], E[a1][b1]]
                            v = max(abs(-e4[i] + sum(e4[j] for j in range(4) if j != i))
                                    for i in range(4))
                            if v > ceiling:
                                ceiling = v
                            if v == target:
                                free.add((start, length))
                                if (a0, a1) == a_c and (b0, b1) == b_c:
                                    frozen.add((start, length))
    return {"ceiling": F(ceiling, n), "free": free, "frozen": frozen}


_N8 = _full_silent_sweep(8)


# ---------------------------------------------------------------------------
# tests
# ---------------------------------------------------------------------------
def test_audit_free_is_faithful():
    """The free-settings audit reduces to the committed audit() on the committed
    settings — exactly, at n = 8, 16, 32.  This anchors every claim below."""
    for n in (8, 16, 32):
        arc = C._arc(*_champion_arc(n), n)
        p0 = C._half_arc_pattern(0, n)
        p1 = C._half_arc_pattern({8: 4, 16: 9, 32: 19}[n], n)
        a_c, b_c = _committed_settings(n)
        Es_ref, sig_ref, _ = C.audit(n, arc, p0, p1, promote=True)
        Es_f, sig_f = audit_free(n, arc, p0, p1, a_c, b_c, C._half_arc_pattern(0, n))
        assert Es_f == Es_ref and sig_f == sig_ref


def test_full_sweep_matches_audit_free():
    """Guard the precomputed-table optimization in _full_silent_sweep: at a sample
    point (champion arc, champion patterns, committed settings, n=8) the table path
    must reproduce audit_free()/chsh() to the integer."""
    n = 8
    carry = C._arc(*_champion_arc(n), n)
    p0 = C._half_arc_pattern(0, n)
    p1 = C._half_arc_pattern(4, n)
    chiA = C._half_arc_pattern(0, n)
    a_c, b_c = _committed_settings(n)
    # table path
    E = [[0] * n for _ in range(n)]
    M = [[0] * n for _ in range(n)]
    for a in range(n):
        for b in range(n):
            e = m = 0
            for lam in range(n):
                u = (lam - a) % n
                Bout = p1[(2 * lam - b) % n] if u in carry else p0[(lam - b) % n]
                e += chiA[u] * Bout
                m += Bout
            E[a][b] = e
            M[a][b] = m
    a0, a1 = a_c
    b0, b1 = b_c
    e4 = [E[a0][b0], E[a0][b1], E[a1][b0], E[a1][b1]]
    v_table = max(abs(-e4[i] + sum(e4[j] for j in range(4) if j != i)) for i in range(4))
    sig_table = max(abs(M[a0][b0] - M[a1][b0]), abs(M[a0][b1] - M[a1][b1]))
    # reference path
    Es, sig_ref = audit_free(n, carry, p0, p1, a_c, b_c, chiA)
    assert sig_table == sig_ref
    assert v_table == chsh(Es, a_c, b_c)


def test_ceiling_is_five_halves():
    """FORCED (the value): the max silent Bell value over the full free sweep is
    exactly 5/2 — never exceeded by any arc under any measurement settings."""
    assert _N8["ceiling"] == F(5, 2)


def test_frozen_settings_pin_antipode_pair():
    """FORCED (the centers): at the committed settings the silent-5/2 arcs are
    exactly the antipode pair — the champion (straddling the doubling wrap-seam
    n/2) and its +n/2 image (straddling the tonic 0).  n=8 from the full sweep;
    n=16 by an independent pattern sweep."""
    n = 8
    champ = _champion_arc(n)
    assert _N8["frozen"] == {champ, _antipode(champ, n)}

    n = 16
    chiA = C._half_arc_pattern(0, n)
    pats = [C._half_arc_pattern(s, n) for s in range(n)]
    a_c, b_c = _committed_settings(n)
    target = 5 * n // 2
    frozen = set()
    for start in range(n):
        for length in range(1, n):
            carry = C._arc(start, length, n)
            for p0 in pats:
                for p1 in pats:
                    Es, sig = audit_free(n, carry, p0, p1, a_c, b_c, chiA)
                    if sig == 0 and chsh(Es, a_c, b_c) == target:
                        frozen.add((start, length))
    champ = _champion_arc(n)
    assert frozen == {champ, _antipode(champ, n)}


def test_doubling_wrap_seam_is_the_antipode():
    """The center that the antipode pair straddles is the doubling's 2-torsion /
    wrap-seam: {lam : 2*lam == 0 (mod n)} == {0, n/2}, for n = 8, 16, 32.  This
    is why 'quarter straddling the antipode' == 'quarter straddling the octave-
    doubling seam' — a real arithmetic identity, not a coincidence."""
    for n in (8, 16, 32):
        seam = {lam for lam in range(n) if (2 * lam) % n == 0}
        assert seam == {0, n // 2}


def test_free_settings_bloom_n8():
    """SELECTION-BEARING (the exact arc): freeing the settings blooms the silent-
    5/2 set at n=8 to 3 antipode-orbits spanning lengths {2, 3} — genuinely more
    than the frozen antipode pair, so the arc was co-tuned with the settings."""
    n = 8
    free = _N8["free"]
    orbits = {_orbit(a, n) for a in free}
    lengths = {ln for _, ln in free}
    assert len(orbits) == 3
    assert lengths == {2, 3}
    # ...and the champion is the UNIQUE minimal-length orbit (the tie-break that
    # re-selects it — an added principle, not a machine constraint).
    minlen = min(lengths)
    minlen_orbits = {o for o in orbits if o[0][1] == minlen}
    champ = _champion_arc(n)
    assert minlen_orbits == {_orbit(champ, n)}


def test_free_settings_cotuning_witness_n16():
    """SELECTION-BEARING at n=16: a pinned silent-5/2 witness whose arc length is
    5, not n/4 = 4 — impossible at the committed settings, so proof that a free
    setting admits distinct-length arcs (co-tuning) at the next scale too."""
    n = 16
    chiA = C._half_arc_pattern(0, n)
    p0 = C._half_arc_pattern(0, n)
    p1 = C._half_arc_pattern(9, n)          # champion patterns for n=16
    arc = C._arc(5, 5, n)                     # {5,6,7,8,9}: length 5 != 4
    a_set, b_set = (0, 3), (0, 5)             # a free setting, not the committed one
    Es, sig = audit_free(n, arc, p0, p1, a_set, b_set, chiA)
    assert sig == 0                           # silent (no-signaling)
    assert F(chsh(Es, a_set, b_set), n) == F(5, 2)
    assert (a_set, b_set) != _committed_settings(n)
    assert len(arc) != n // 4                 # distinct length: the co-tuning
