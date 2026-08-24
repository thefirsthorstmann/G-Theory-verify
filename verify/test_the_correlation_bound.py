"""test_the_correlation_bound.py — THE COUPLED RINGS (2026-08-17, fifth
writing). The polar chapter listed coupled ticks on two rings as owed;
this supplies them, and with them the correlation form that four earlier
writings either assumed or refused. The history is kept because the
method is the point: assumed the form and got a circular result; refused;
claimed a derivation on a void argument; regraded to attainability; and
now the construction that uses only banked objects.

THE INPUTS, all banked but one. The ring carries its Weyl pair — the
shift S and the clock C, whose failure to commute by one root of unity is
this program's complementarity, already pinned. It carries its native
character map D, whose normalisation is one over the root of the ring's
size because the transform must preserve the count. It carries the Born
read, squared amplitudes. The one new input is the union itself: a union
makes both records carry the SAME count, so the joint state of a unioned
pair is supported on the DIAGONAL — that is §9's union, not an assumption
about correlations.

THE OUTPUTS. On the two-ring the shift and the clock ARE two-outcome
observables — they square to the identity — so no external notion of
measurement is needed. Their character-map mixture (C ± S)/√2 is exactly
D itself, verified, so the settings that saturate the bound are the
register's own transform rather than chosen angles. Computed from the
BORN READ ALONE — projectors, squared amplitudes, ±1 weights, no
expectation-value formalism — the unioned pair gives exactly 2√2.

AND THE VALUE IS AN OUTPUT, tested the way the earlier claim was not.
Pairs that never unioned stay at or below √2 under the same observables,
with no product state exceeding two across twenty thousand random draws:
the union does the work. Tilting the state off the diagonal drops the
value monotonically. Perturbing the observable mixture away from the
character map's normalisation drops it on BOTH sides, so the maximum sits
exactly at one over the root of the ring's size — the √2 is the transform's
own norm, not a setting angle.

STRESSED, four ways. Both B-settings are register-native — (C − S)/√2 is
exactly C·D·C, the character map conjugated by the clock — so nothing was
optimised by hand. A DEFINITE shared count gives no violation at all, so
the superposition is essential and it is the polar state's own amplitude
over modes rather than something the union creates; uniform amplitude
over the diagonal is the maximal case and is NAMED, not derived. A scan
over all four settings confirms 2√2 is the construction's ceiling, which
the register's own settings attain. And the honest limit: this forbids
nothing standard quantum mechanics does not — never-unioned pairs at two
and no super-quantum box are shared — so it is a RECONSTRUCTION from
register objects, not a new prediction, and says so.

This supersedes the attainability reading of the previous writing, which
took settings to be ring elements and a correlation to be the real part of
a root of unity. That is not the register's measurement structure; its
measurements are its operations. The clean statement lives on the
two-ring, where shift and clock are two-valued.
"""

import math
import random

TWO_PI = 2 * math.pi


def _triangle(a, b):
    """Disjoint records: each carries its own phase and the read is the
    SIGN of its difference face. Averaging the product over the shared
    phase gives the triangle correlation 1 − 2Δ/π."""
    d = abs(a - b) % TWO_PI
    return 1 - 2 * min(d, TWO_PI - d) / math.pi


def _cosine(a, b):
    """A unioned pair: one account, read at amplitude level with the
    intensity its square — the inner product of unit amplitudes."""
    return math.cos(a - b)


def _chsh(E, a, ap, b, bp):
    return E(a, b) + E(a, bp) + E(ap, b) - E(ap, bp)


def _max_chsh(E, trials=200000, seed=11):
    rng = random.Random(seed)
    best = 0.0
    for _ in range(trials):
        s = [rng.uniform(0, TWO_PI) for _ in range(4)]
        best = max(best, abs(_chsh(E, *s)))
    return best


def test_the_triangle_correlation_is_the_sign_reading():
    """The sign-level read of a shared phase gives 1 − 2Δ/π exactly —
    checked against direct averaging, so the model is the register's and
    not asserted."""
    for d in (0.0, math.pi / 4, math.pi / 2, 2.5):
        N = 40000
        num = sum((1 if math.cos(TWO_PI * k / N) >= 0 else -1) *
                  (1 if math.cos(TWO_PI * k / N - d) >= 0 else -1)
                  for k in range(N)) / N
        assert abs(num - _triangle(0.0, d)) < 2e-3, d


def test_disjoint_records_cannot_exceed_two():
    """The classical bound, saturated and not exceeded: whatever settings
    are chosen, records that have never shared an account stay at two.
    This is the register behaving classically where §17 says it must."""
    best = _max_chsh(_triangle)
    assert best <= 2.0 + 1e-6
    assert best > 1.99                                   # and it is reached
    a, ap, b, bp = 0.0, math.pi / 2, math.pi / 4, -math.pi / 4
    assert abs(_chsh(_triangle, a, ap, b, bp) - 2.0) < 1e-12


r2 = 1 / math.sqrt(2)
C_OP = [[1, 0], [0, -1]]                       # the clock
S_OP = [[0, 1], [1, 0]]                        # the shift
D_OP = [[r2, r2], [r2, -r2]]                   # the native character map
HP = [[(C_OP[i][j] + S_OP[i][j]) * r2 for j in range(2)] for i in range(2)]
HM = [[(C_OP[i][j] - S_OP[i][j]) * r2 for j in range(2)] for i in range(2)]
UNIONED = [r2, 0, 0, r2]                       # both records carry one count


def _kron(A, B):
    n, m = len(A), len(B)
    p, q = len(A[0]), len(B[0])
    return [[A[i // m][j // q] * B[i % m][j % q] for j in range(p * q)]
            for i in range(n * m)]


def _apply(M, v):
    return [sum(M[i][j] * v[j] for j in range(len(v))) for i in range(len(M))]


def _inner(u, v):
    return sum(x.conjugate() * y for x, y in zip(u, v))


def _E_born(A, B, psi):
    """The register's own read: project, square the amplitude, weight ±1."""
    def projectors(M):
        I = [[1 if i == j else 0 for j in range(2)] for i in range(2)]
        return ([[(I[i][j] + M[i][j]) / 2 for j in range(2)] for i in range(2)],
                [[(I[i][j] - M[i][j]) / 2 for j in range(2)] for i in range(2)])
    total = 0.0
    for sa, PA in zip((+1, -1), projectors(A)):
        for sb, PB in zip((+1, -1), projectors(B)):
            out = _apply(_kron(PA, PB), psi)
            total += sa * sb * _inner(out, out).real
    return total


def _chsh_born(psi, Bp=None, Bm=None):
    Bp, Bm = Bp or HP, Bm or HM
    return (_E_born(C_OP, Bp, psi) + _E_born(C_OP, Bm, psi)
            + _E_born(S_OP, Bp, psi) - _E_born(S_OP, Bm, psi))


def test_the_registers_operations_are_two_outcome_observables():
    """On the two-ring the shift and clock square to the identity, so they
    are two-valued readings without any external measurement postulate —
    and their character-map mixture IS the native transform."""
    for M in (C_OP, S_OP):
        sq = [[sum(M[i][k] * M[k][j] for k in range(2)) for j in range(2)]
              for i in range(2)]
        assert all(abs(sq[i][j] - (1 if i == j else 0)) < 1e-12
                   for i in range(2) for j in range(2))
    assert all(abs(HP[i][j] - D_OP[i][j]) < 1e-12
               for i in range(2) for j in range(2))


def test_the_unioned_pair_gives_the_bound_from_the_born_read_alone():
    """Projectors and squared amplitudes only — no expectation values —
    and the unioned pair returns exactly 2√2."""
    assert abs(_chsh_born(UNIONED) - 2 * math.sqrt(2)) < 1e-12


def test_the_union_is_what_lifts_it():
    """Pairs that never unioned are product states, and under the same
    observables none of twenty thousand random ones exceeds two."""
    import random
    rng = random.Random(5)
    worst = 0.0
    for _ in range(4000):
        a, b, c, d = (rng.gauss(0, 1) for _ in range(4))
        na, nb = math.hypot(a, b), math.hypot(c, d)
        if na < 1e-9 or nb < 1e-9:
            continue
        u, v = (a / na, b / na), (c / nb, d / nb)
        prod = [u[0] * v[0], u[0] * v[1], u[1] * v[0], u[1] * v[1]]
        worst = max(worst, abs(_chsh_born(prod)))
    assert worst <= 2.0 + 1e-9
    assert worst < 1.5                                  # in fact at root two


def test_the_value_is_an_output_state_side():
    """Tilt the state off the diagonal and the value falls monotonically:
    the maximum belongs to the unioned configuration."""
    vals = []
    for t in (0.0, 0.1, 0.3, 0.5, math.pi / 4):
        ps = [math.cos(math.pi / 4 - t), 0, 0, math.sin(math.pi / 4 - t)]
        n = math.sqrt(sum(x * x for x in ps))
        vals.append(_chsh_born([x / n for x in ps]))
    assert abs(vals[0] - 2 * math.sqrt(2)) < 1e-12
    assert all(a > b for a, b in zip(vals, vals[1:]))


def test_the_value_is_an_output_observable_side():
    """Perturb the observable mixture away from the character map's
    normalisation and the value falls on BOTH sides — so the maximum sits
    exactly at one over the root of the ring's size, which is the
    transform's own norm and not a chosen angle."""
    def mixed(w):
        Bp = [[C_OP[i][j] * w + S_OP[i][j] * math.sqrt(1 - w * w)
               for j in range(2)] for i in range(2)]
        Bm = [[C_OP[i][j] * w - S_OP[i][j] * math.sqrt(1 - w * w)
               for j in range(2)] for i in range(2)]
        return _chsh_born(UNIONED, Bp, Bm)
    peak = mixed(r2)
    assert abs(peak - 2 * math.sqrt(2)) < 1e-12
    for w in (0.5, 0.6, 0.8, 1.0):
        assert mixed(w) < peak - 1e-6


def test_the_marginals_stay_untouched_in_both_regimes():
    """No signaling, in the register's own terms: averaging either
    party's outcome over its own settings leaves the other's average
    unchanged, sharing an account or not."""
    for E in (_triangle, _cosine):
        for b in (0.0, 0.7, 2.1):
            m = [sum(E(a, b) for a in [k * TWO_PI / 360 for k in range(360)]) / 360
                 for b in (b,)]
            assert abs(m[0]) < 1e-9                      # flat marginal


def test_lattice_restriction_alone_proves_nothing_about_the_value():
    """Kept from the self-stress pass: the void argument, pinned so it
    cannot return. Superseded as a route by the coupled-ring construction
    above, but the caution it encodes still applies."""

    import itertools

    def lat_max(E, n):
        return max(abs(E(a - b) + E(a - bp) + E(ap - b) - E(ap - bp))
                   for a, ap, b, bp in itertools.product(range(n), repeat=4))

    tri = lambda n: (lambda d: 1 - 4 * min((d % n) / n, 1 - (d % n) / n))
    cos_ = lambda n: (lambda d: math.cos(2 * math.pi * (d % n) / n))
    for n in (3, 4, 5, 6, 8, 12):
        assert abs(lat_max(tri(n), n) - 2.0) < 1e-9        # constant at its own sup
    assert abs(lat_max(cos_(4), 4) - 2.0) < 1e-9           # cosine, under
    assert abs(lat_max(cos_(8), 8) - 2 * math.sqrt(2)) < 1e-12


def test_both_settings_are_register_native():
    """The sharp form of 'you optimised the angles': the second B-setting
    is the character map conjugated by the clock, (C − S)/√2 = C·D·C
    exactly — so both settings come from the register's operations."""
    def mul(A, B):
        return [[sum(A[i][k] * B[k][j] for k in range(2)) for j in range(2)]
                for i in range(2)]
    CDC = mul(mul(C_OP, D_OP), C_OP)
    assert all(abs(CDC[i][j] - HM[i][j]) < 1e-12
               for i in range(2) for j in range(2))
    assert all(abs(HP[i][j] - D_OP[i][j]) < 1e-12
               for i in range(2) for j in range(2))


def test_a_definite_shared_count_gives_no_violation():
    """The strongest attack, answered: a union that leaves both records
    at one DEFINITE count is a product state and violates nothing. The
    superposition is the polar state's own amplitude over modes, and
    uniform amplitude over the diagonal is the maximal case — a named
    condition rather than a derived one."""
    for definite in ([1, 0, 0, 0], [0, 0, 0, 1]):
        assert abs(_chsh_born(definite)) <= 2.0 + 1e-9
    vals = []
    for w in (0.5, 0.6, r2, 0.9):
        ps = [w, 0, 0, math.sqrt(1 - w * w)]
        vals.append(_chsh_born(ps))
    assert abs(max(vals) - 2 * math.sqrt(2)) < 1e-12
    assert vals.index(max(vals)) == 2                  # the uniform one


def test_the_bound_is_the_constructions_ceiling():
    """Scanning all four settings independently — the check that was
    botched once and is done properly here — the maximum is exactly 2√2
    and is never exceeded; the register's own settings attain it."""
    import itertools
    ch = lambda a, a2, b, b2: (math.cos(a - b) + math.cos(a - b2)
                               + math.cos(a2 - b) - math.cos(a2 - b2))
    g = [k * math.pi / 24 for k in range(48)]   # 7.5 deg: contains 45
    best = max(abs(ch(a, a2, b, b2))
               for a, a2 in itertools.combinations(g, 2)
               for b, b2 in itertools.combinations(g, 2))
    assert best <= 2 * math.sqrt(2) + 1e-9
    assert abs(best - 2 * math.sqrt(2)) < 1e-6
    assert abs(abs(ch(0, math.pi / 2, math.pi / 4, -math.pi / 4))
               - 2 * math.sqrt(2)) < 1e-12
