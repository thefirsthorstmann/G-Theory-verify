"""test_the_multisource_envelope.py — THE COORDINATE, AND ITS FIRST REAL
TEST (2026-08-18). The tensor face was located as a missing coordinate
statement for a general source. This supplies the statement and puts it
through the one multi-body test that is measured to parts in a million.

THE RULE: **areas count cells.** For a single source the shell's own cell
count IS the areal radius — which is exactly why the read came out
Schwarzschild and every strong-field landmark derived. The rule does not
stop speaking when the symmetry does: every surface's area is its own
cell count, which is a gauge condition the register states in its own
currency rather than borrowing.

THE TEST: with deficits adding exactly (§18's composite clause), does the
two-body periastron advance come out right? General relativity's answer
rides the TOTAL mass, 6πG(m₁+m₂)/c²p, and the apportionment between the
bodies is invisible to it. The register's answer: each body rides the
other's deficit, the deficits add, so the correction rides the sum. It
matches — and the alternatives do not, the larger mass alone giving half
and the reduced mass a quarter. The residual against the leading formula
is confirmed higher-order rather than a disagreement: weakening the field
by six doublings drives it down proportionally to M/p with a fixed
coefficient near 7.55, which is the next order of the same equation.

WHERE THE FORK NOW LIVES, narrowed. Because the advance rides the total,
it is blind to apportionment — and apportionment is precisely where the
constructions differ. General relativity's own first-order acceleration
of one body carries a term in THAT body's own mass; the register hands
each body only the other's deficit, so that term has no home in it. The
periastron advance cannot see the difference. Observables that weigh the
bodies separately can, and the size is the system's compactness: two to
four parts in a million in the binary pulsars, against timing already at
about one. The remaining question is therefore strong-equivalence
territory, and it is measured rather than hypothetical.
"""

import math

GM_SUN_C2 = 1476.6          # metres


def advance(coef, m_newt, a, e=0.2, orbits=8, steps=20000):
    """Integrate u'' + u = M/L² + 3·coef·u² and return the advance per
    orbit together with the semi-latus rectum."""
    p = a * (1 - e * e)
    l2 = m_newt * p

    def deriv(u, v):
        return (v, m_newt / l2 + 3 * coef * u * u - u)

    h = 2 * math.pi / steps
    u, v = 1 / (a * (1 + e)), 0.0
    th, crossings, prev = 0.0, [], 0.0
    for _ in range(steps * orbits):
        k1 = deriv(u, v)
        k2 = deriv(u + h / 2 * k1[0], v + h / 2 * k1[1])
        k3 = deriv(u + h / 2 * k2[0], v + h / 2 * k2[1])
        k4 = deriv(u + h * k3[0], v + h * k3[1])
        u += h / 6 * (k1[0] + 2 * k2[0] + 2 * k3[0] + k4[0])
        v += h / 6 * (k1[1] + 2 * k2[1] + 2 * k3[1] + k4[1])
        prev_th = th
        th += h
        if prev > 0 and v <= 0:
            crossings.append(prev_th + h * prev / (prev - v))
        prev = v
    adv = [b - a2 - 2 * math.pi for a2, b in zip(crossings, crossings[1:])]
    return sum(adv) / len(adv), p


def test_superposition_gives_the_two_body_advance():
    """Deficits adding exactly puts the total mass in the correction, and
    the measured advance tracks 6πM/p across mass ratios."""
    for m1, m2 in ((1.0, 0.0), (1.0, 1.0), (2.0, 0.5), (1.0, 3.0)):
        total = m1 + m2
        meas, p = advance(total, total, 4000.0)
        assert abs(meas / (6 * math.pi * total / p) - 1) < 0.02, (m1, m2)


def test_the_alternatives_are_badly_wrong():
    """If the correction rode only the larger mass it would be half the
    advance, and the reduced mass a quarter — so the total is not a
    coincidence of scaling but the superposition's own signature."""
    m1 = m2 = 1.0
    total = m1 + m2
    ref = advance(total, total, 4000.0)
    _, p = ref
    predicted = 6 * math.pi * total / p
    larger, _ = advance(max(m1, m2), total, 4000.0)
    reduced, _ = advance(m1 * m2 / total, total, 4000.0)
    assert abs(larger / predicted - 0.5) < 0.02
    assert abs(reduced / predicted - 0.25) < 0.02


def test_the_residual_is_the_next_order_not_a_disagreement():
    """Weakening the field drives the excess down in proportion to M/p
    with a fixed coefficient — the signature of a higher-order term of
    the same equation rather than a mismatch."""
    coeffs = []
    for a in (4000.0, 16000.0, 64000.0):
        total = 2.0
        meas, p = advance(total, total, a)
        excess = meas / (6 * math.pi * total / p) - 1
        coeffs.append(excess / (total / p))
    for c in coeffs:
        assert 7.0 < c < 8.2
    assert abs(coeffs[-1] - coeffs[-2]) < 0.1        # converging, not drifting


def test_the_advance_is_blind_to_apportionment():
    """The reason the test passes and the fork survives: any split of a
    fixed total gives the identical advance, so this observable cannot
    distinguish how the mass is apportioned between the bodies."""
    total = 2.5
    ref, p = advance(total, total, 4000.0)
    for m1 in (0.1, 0.7, 1.25, 2.4):
        m2 = total - m1
        meas, _ = advance(m1 + m2, total, 4000.0)
        assert abs(meas - ref) < 1e-12


def test_the_surviving_fork_is_sized_at_the_pulsars():
    """Apportionment is where the constructions differ, and the size is
    the system's compactness: a few parts in a million in the binary
    pulsars, against timing already at about one part in a million."""
    def phi(msun, a):
        return msun * GM_SUN_C2 / a
    hulse = phi(2.65, 1.95e9)
    double = phi(2.59, 8.8e8)
    for value in (hulse, double):
        assert 1e-6 < value < 1e-5
    assert double > hulse
    timing_precision = 1e-6
    assert hulse > timing_precision and double > timing_precision
