"""
THE SELECTION-BEARING HITS.   GRADE: STRIKING (not Forced).

These are the famous numerical results. They are real and often parameter-free, but
each carries a CHOICE in its construction, so they are STRIKING, never Forced. They live
in their own file so the discipline is visible: the Forced spine is everything else;
this is the at-risk, selection-bearing column. (The rigor-ledger flagged calling these
"Forced" as a defect to repair -- this file is that repair.)
"""
import math
from fractions import Fraction


def test_koide_predicts_tau_from_Q_two_thirds():
    """
    KOIDE.  STRIKING.  Q = (Sum m)/(Sum sqrt m)^2.  The framework fixes Q = 2/3 exactly
    (selection: 2/3 chosen as the value). With CODATA m_e, m_mu, solving for m_tau gives
    ~1776.96 MeV against the measured 1776.86 -- about 60 ppm, no further parameter.
    """
    m_e, m_mu = 0.51099895000, 105.6583755          # MeV (CODATA)
    a, b = math.sqrt(m_e), math.sqrt(m_mu)
    S1, S2 = a + b, m_e + m_mu
    # Q = 2/3  ->  c^2 - 4 S1 c + (3 S2 - 2 S1^2) = 0, with c = sqrt(m_tau); take larger root
    disc = (4 * S1)**2 - 4 * (3 * S2 - 2 * S1**2)
    c = (4 * S1 + math.sqrt(disc)) / 2
    m_tau = c**2
    assert abs(m_tau - 1776.96) < 0.5               # construction lands ~1776.96 MeV
    ppm = abs(m_tau - 1776.86) / 1776.86 * 1e6
    assert ppm < 100                                 # ~60 ppm from measured


def test_proton_radius_as_459_alpha():
    """
    PROTON RADIUS.  STRIKING & STAKED.  The dimensionless ratio 459*alpha = 3^3*17*alpha
    times the classical electron radius (one borrowed length -> legal under the Scale
    Theorem) gives the proton charge radius. Lands in the muonic-hydrogen band; staked --
    if the radius settles firmly outside it, the construction is wrong.
    """
    r_e = 2.8179403262e-15        # classical electron radius, m (the one borrowed ruler)
    alpha = 7.2973525693e-3
    assert 459 == 3**3 * 17
    r_p = r_e / (459 * alpha)     # = r_e / (459 alpha)
    r_p_fm = r_p * 1e15
    assert 0.8409 <= r_p_fm <= 0.8414    # muonic-hydrogen band (~0.8413 fm)


# --- THE MUON ------------------------------------------------------------------
# Encoded from the source: catalog/THE-FULL-POSITION-INTERNAL-2026-06-28.md  §14
# "The muon" (L156-164), the canonical 2026-06-28 monolith. Its header is exactly
# "## 14. The muon  forced engine / placement" -- so the muon is encoded as that
# split: an exact, could-have-failed engine (the two functions' assertions that use
# ==), and a selection-bearing headline (the 1.37 ppm match). The WHOLE result is
# graded STRIKING, because the number everyone quotes -- 206.768 -> 1.37 ppm -- is the
# selection-bearing half. (Built from the document, not reconstructed from memory;
# cross-checked against 06-VERIFICATION-LOG, 11-METHODS, the rigor-ledger and the
# prediction-registry, all of which agree on the climb and the 1.37 ppm figure.)

def test_muon_forced_engine_climb_and_closure():
    """
    MUON -- the forced engine.  This is the  half of monolith §14's split: exact
    integer identities that could have failed to close and do not, with NO measured
    value consulted to obtain them.

    The octave climb: from the forced root 24 = 2^3*3, pure doubling five times lands
    on 768 = 2^8*3 -- climb in the twos, the 3 stands invariant. The decimal descent
    206 . 768 2827 55... is then read as three routes to unity (the first multiple on
    each prime's ladder whose digital root returns to 1: twos 64, sevens 28, elevens
    55), each closing by stepping down one. The closure is the part that earns the
    word "forced": it is exact, and it could have come out otherwise.
    """
    # the octave climb  24 -> 48 -> 96 -> 192 -> 384 -> 768
    assert 24 == 2**3 * 3                          # the forced root
    rung = 24
    for _ in range(5):
        rung *= 2                                  # climb in the twos
    assert rung == 768 == 2**8 * 3 == 24 * 2**5    # the 3 is invariant; 2-powers lift

    # three routes to unity; each steps down one, every step-down at digital root 9
    assert (64, 28, 55) == (2**6, 2**2 * 7, 5 * 11)

    def digital_root(n):
        return n if n < 10 else digital_root(sum(int(d) for d in str(n)))
    assert digital_root(63) == digital_root(27) == digital_root(54) == 9

    # the closure is EXACT -- "it could have failed to close, and does not"
    assert 64 + 28 + 55 == 147 == 3 * 7**2
    assert 63 + 27 + 54 == 144 == 12**2
    # and 144 = F(12), the twelfth Fibonacci number
    fib = [1, 1]
    while len(fib) < 12:
        fib.append(fib[-1] + fib[-2])
    assert fib[11] == 144
    # their difference is exactly 3 -- the three units, one per route
    assert 147 - 144 == 3


def test_muon_headline_206768_is_striking():
    """
    MUON -- the headline.  GRADE: STRIKING / selection-bearing (the  half).

    206.768 matches CODATA m_mu/m_e = 206.7682827(46) to ~1.37 ppm with zero fitted
    parameters -- BUT the construction makes a choice: it reads the forced integer 768
    as the decimal tail .768 = 768/1000 (a base-10 /1000 placement), places each route
    into its decimal slots ("a scheme, not a forced map"), and selects the order
    28-before-27 to match an already-known value. That the muon's leading decimals
    *are* 768 is a ~4% coincidence (the ratio falling on so 3-smooth a value). So this
    is STRIKING, never Forced. Source: monolith §14 L158, L164.

    Deliberately NOT asserted: (1) the deep tail digits 2827/55 -- CODATA deep digits
    drift across releases (older ...2838 vs now ...2826), so matching them is fitting,
    not forcing (11-METHODS L198); (2) the "cleanest parameter-free form ~4.6 ppm"
    claimed only in Base-Camp L101 and GRADES.md -- no construction for it exists
    anywhere in the corpus, so it stays a note here, not a test assertion.
    """
    framework = 206 + Fraction(768, 1000)          # .768 = 768/1000, exactly
    assert framework == Fraction(206768, 1000)
    measured = 206.7682827                          # CODATA, monolith L158 (authoritative)
    ppm = abs(float(framework) - measured) / measured * 1e6
    assert ppm < 1.5                                # the cold value is 1.367 ppm

    # inoculation against the flagged CERN conflation .768 = 768/1024 = 3/4:
    # .768 is 768/1000, NOT 3/4. Using 3/4 (= 0.75) gives 206.75 -- ~88 ppm off, far
    # worse -- so the hit lives specifically at the literal decimal, not a "clean" 3/4.
    assert Fraction(768, 1000) != Fraction(3, 4)
    ppm_three_quarter = abs((206 + 0.75) - measured) / measured * 1e6
    assert ppm_three_quarter > 80                   # the 88 ppm the docs warn about
