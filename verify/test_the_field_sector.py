"""test_the_field_sector.py — THE FIELD SECTOR'S STATE SPACE AS THE
COMPOSITION OF RINGS (2026-08-22). the author: "go get the
field-sector state space." It was the one "open, named" item in §21.12 that
was apparatus rather than measurement.

THE OBJECTS, ALL BANKED IN §22 AND USED HERE AS THEY STAND.
  ring R_n      state = 2n integers: n amplitudes and n phase exponents
  Weyl pair     shift X and clock Z on R_n, Z X = ω X Z with ω = e^{2πi/n}
  character map F_n, the transform, normalized 1/√n because it must
                preserve the count; it conjugates shift into clock
  Born read     the squared amplitudes and nothing that depends on phase
  composition   two rings compose as a product (§22's identification)
  union         a union makes both records carry the same count, so the
                joint state of a unioned pair is supported on the diagonal
  faces         the horizon record's macrostate fixes the count face and
                the mirror-odd difference face (the log-coefficient census)

THE CONSTRUCTION. A field sector is a finite family of rings together with
an account partition — which rings have unioned. Its state space is the
product over accounts of the account's diagonal. Everything else is a
theorem about that object, and every theorem below is checked numerically:

  T1  COMPOSITION OF THE WEYL STRUCTURE. Weyl operators of distinct rings
      commute; within a ring they fail by ω_n; a composite pair X_a, Z_b
      fails by exp(2πi Σ a_i b_i / n_i), and the group of all such phases
      is the lcm-th roots of unity. One root of unity per ring becomes one
      root of unity per sector, its order the least common multiple.
  T2  COUNT PRESERVATION COMPOSES. The composite character map is the
      product of the ring maps, it is unitary, and its entries have modulus
      (Π n_i)^{-1/2}: the normalization is forced by composition, there is
      no freedom to tune it per ring.
  T3  THE HALF IS COMPOSITION-INVARIANT. On any sector the Born read
      returns exactly half of the state's integers — the amplitudes over
      the product basis — and every phase exponent is discarded, whether
      the state is a product or an entangled diagonal.
  T4  UNION COLLAPSES DIMENSION. m rings of size n that share one account
      have a diagonal of dimension n, not n^m: the union is many-to-one
      by exactly (m−1) ln n nats. Unioned records cannot disagree: the
      joint Born read in the clock basis has no off-diagonal weight.
  T5  THE HORIZON CENSUS IS A CASE OF THE COMPOSITION. N binary rings that
      have NOT unioned with one another, under the two faces, number
      C(N/2, N/4)²; the two faces are both diagonal in the clock basis,
      so they commute and the census is well defined.
  T6  THE CORRELATION BOUND SURVIVES EMBEDDING AND OBEYS MONOGAMY. A
      unioned pair reads 2√2 with the register's own settings, unchanged
      when embedded in a larger sector with a third ring it never unioned
      with; a pair that unioned as part of a TRIPLE account reads at most 2
      under every setting, register-native or not, while the triple itself
      carries the correlation (Mermin value 4). Never-unioned pairs stay
      at 2.

WHAT IT FORBIDS (the Maxwell bar): no super-quantum correlation anywhere in
a sector; no pairwise violation inside a triple account; no count
disagreement between unioned records; no census coefficient outside −m/2
for the constraint piece. And it closes the named item: the apparatus is
built from banked objects and one identification already on record. As
§22 says of the two-ring case, this forbids nothing standard quantum
mechanics permits; it is a reconstruction from register objects, offered
as one. The discriminator remains the logarithmic coefficient.
"""

import itertools
import math
import pathlib
from fractions import Fraction
from math import comb, gcd

import numpy as np

CATALOG = pathlib.Path(__file__).resolve().parent.parent / "catalog"
GRAVITY = (CATALOG / "GRAVITY-AS-TONAL-CENTER.md").read_text()
FLAT = " ".join(GRAVITY.split())
RNG = np.random.default_rng(7)


# --- the ring, as banked --------------------------------------------------------

def ring(n):
    w = np.exp(2j * np.pi / n)
    X = np.roll(np.eye(n), 1, axis=0)                      # shift
    Z = np.diag(w ** np.arange(n))                          # clock
    F = np.array([[w ** (j * k) for k in range(n)] for j in range(n)]) / math.sqrt(n)
    return X, Z, F, w


def kron(*ms):
    out = np.array([[1.0 + 0j]])
    for m in ms:
        out = np.kron(out, m)
    return out


def lcm(*xs):
    out = 1
    for x in xs:
        out = out * x // gcd(out, x)
    return out


def test_the_single_ring_is_as_banked():
    for n in (2, 3, 5, 7):
        X, Z, F, w = ring(n)
        assert np.allclose(Z @ X, w * X @ Z)                 # one root of unity
        assert np.allclose(F @ F.conj().T, np.eye(n))        # count preserved
        assert np.allclose(abs(F) ** 2, 1 / n)               # 1/sqrt(n) forced
        assert np.allclose(F @ X @ F.conj().T, Z)            # shift -> clock


# --- T1 composition of the Weyl structure --------------------------------------

def test_weyl_operators_of_distinct_rings_commute_and_within_fail_by_omega():
    sizes = (2, 3, 4)
    rs = [ring(n) for n in sizes]
    eyes = [np.eye(n) for n in sizes]
    def embed(op, i):
        ms = list(eyes); ms[i] = op
        return kron(*ms)
    for i, j in itertools.combinations(range(3), 2):
        Xi, Zj = embed(rs[i][0], i), embed(rs[j][1], j)
        assert np.allclose(Xi @ Zj, Zj @ Xi)
    for i, n in enumerate(sizes):
        Xi, Zi = embed(rs[i][0], i), embed(rs[i][1], i)
        assert np.allclose(Zi @ Xi, rs[i][3] * Xi @ Zi)


def test_the_composite_phase_is_the_symplectic_form_and_its_order_the_lcm():
    sizes = (2, 3, 4)
    rs = [ring(n) for n in sizes]
    phases = set()
    for a in itertools.product(*[range(n) for n in sizes]):
        for b in itertools.product(*[range(n) for n in sizes]):
            Xa = kron(*[np.linalg.matrix_power(rs[i][0], a[i]) for i in range(3)])
            Zb = kron(*[np.linalg.matrix_power(rs[i][1], b[i]) for i in range(3)])
            expected = np.exp(2j * np.pi * sum(a[i] * b[i] / sizes[i] for i in range(3)))
            assert np.allclose(Zb @ Xa, expected * Xa @ Zb)
            phases.add(sum(Fraction(a[i] * b[i], sizes[i]) for i in range(3)) % 1)
    order = lcm(*sizes)
    assert phases == {Fraction(k, order) for k in range(order)}     # the lcm-th roots, all of them


# --- T2 count preservation composes ---------------------------------------------

def test_the_composite_character_map_is_unitary_with_the_forced_normalization():
    sizes = (2, 3, 5)
    F = kron(*[ring(n)[2] for n in sizes])
    d = math.prod(sizes)
    assert np.allclose(F @ F.conj().T, np.eye(d))
    assert np.allclose(abs(F) ** 2, 1 / d)
    # and it conjugates every composite shift into the composite clock
    X = kron(*[ring(n)[0] for n in sizes]); Z = kron(*[ring(n)[1] for n in sizes])
    assert np.allclose(F @ X @ F.conj().T, Z)


# --- T3 the half is composition-invariant -----------------------------------------

def _integer_state(d, L=12):
    """The register's state: amplitude integers and phase exponents."""
    a = RNG.integers(0, 5, size=d)
    e = RNG.integers(0, L, size=d)
    psi = a * np.exp(2j * np.pi * e / L)
    return a, e, psi


def test_the_born_read_returns_exactly_half_of_the_integers():
    for sizes in ((2, 3), (2, 2, 2), (3, 4)):
        d = math.prod(sizes)
        a, e, psi = _integer_state(d)
        read = abs(psi) ** 2
        assert read.shape == (d,)                            # d numbers read
        assert np.allclose(read, a.astype(float) ** 2)       # they are the amplitudes
        e2 = (e + RNG.integers(1, 12, size=d)) % 12          # change every phase exponent
        psi2 = a * np.exp(2j * np.pi * e2 / 12)
        assert np.allclose(abs(psi2) ** 2, read)             # the read cannot tell
        assert 2 * d == len(a) + len(e)                      # half of 2d integers


# --- T4 union collapses dimension -------------------------------------------------

def _diagonal_projector(n, m):
    d = n ** m
    P = np.zeros((d, d))
    for k in range(n):
        idx = sum(k * n ** (m - 1 - j) for j in range(m))
        P[idx, idx] = 1
    return P


def test_an_account_of_m_rings_has_the_dimension_of_one_ring():
    for n, m in ((2, 2), (2, 3), (3, 2), (3, 3), (2, 5)):
        P = _diagonal_projector(n, m)
        assert round(np.trace(P)) == n                       # not n**m
        lost = m * math.log(n) - math.log(n)
        assert abs(lost - (m - 1) * math.log(n)) < 1e-12


def test_unioned_records_cannot_disagree():
    n, m = 3, 2
    P = _diagonal_projector(n, m)
    psi = P @ (RNG.normal(size=n ** m) + 1j * RNG.normal(size=n ** m))
    psi /= np.linalg.norm(psi)
    read = abs(psi) ** 2
    for k1 in range(n):
        for k2 in range(n):
            if k1 != k2:
                assert read[k1 * n + k2] < 1e-14


# --- T5 the horizon census is a case of the composition ----------------------------

def test_the_two_faces_commute_and_count_the_banked_census():
    for N in (8, 12):
        Z = ring(2)[1]
        eye = np.eye(2)
        def embed(op, i):
            ms = [eye] * N; ms[i] = op
            return kron(*ms)
        number = [(np.eye(2 ** N) - embed(Z, i)) / 2 for i in range(N)]   # (1 - Z)/2 per cell
        count = sum(number)
        diff = sum(number[:N // 2]) - sum(number[N // 2:])
        assert np.allclose(count @ diff, diff @ count)            # both diagonal: commute
        cdiag, ddiag = np.real(np.diag(count)), np.real(np.diag(diff))
        dim = int(np.sum((abs(cdiag - N / 2) < 1e-9) & (abs(ddiag) < 1e-9)))
        assert dim == comb(N // 2, N // 4) ** 2                   # the banked count


# --- T6 the correlation bound under composition -------------------------------------

def _chsh_born(state, A0, A1, B0, B1):
    """CHSH from the Born read alone: projectors, probabilities, signed sums."""
    def corr(A, B):
        val = 0.0
        for sa, Pa in _projectors(A):
            for sb, Pb in _projectors(B):
                p = np.real(state.conj() @ np.kron(Pa, Pb) @ state)
                val += sa * sb * p
        return val
    return corr(A0, B0) + corr(A0, B1) + corr(A1, B0) - corr(A1, B1)


def _projectors(O):
    w, v = np.linalg.eigh(O)
    return [(float(np.sign(w[i])), np.outer(v[:, i], v[:, i].conj())) for i in range(len(w))]


def _register_settings():
    X, Z, F, _ = ring(2)
    return Z, X, F, Z @ F @ Z       # clock, shift, the map, the map conjugated by the clock


def test_a_unioned_pair_reads_two_root_two_with_register_settings():
    Z, X, F, ZFZ = _register_settings()
    phi = np.zeros(4, complex); phi[0] = phi[3] = 1 / math.sqrt(2)      # the diagonal
    assert abs(_chsh_born(phi, Z, X, F, ZFZ) - 2 * math.sqrt(2)) < 1e-12


def test_the_value_is_unchanged_by_embedding_in_a_larger_sector():
    Z, X, F, ZFZ = _register_settings()
    phi = np.zeros(4, complex); phi[0] = phi[3] = 1 / math.sqrt(2)
    third = RNG.normal(size=3) + 1j * RNG.normal(size=3); third /= np.linalg.norm(third)
    state = np.kron(phi, third)                                        # pair x a third ring of size 3
    # read the pair only: the third ring's identity
    def corr(A, B):
        val = 0.0
        for sa, Pa in _projectors(A):
            for sb, Pb in _projectors(B):
                P = np.kron(np.kron(Pa, Pb), np.eye(3))
                val += sa * sb * np.real(state.conj() @ P @ state)
        return val
    chsh = corr(Z, F) + corr(Z, ZFZ) + corr(X, F) - corr(X, ZFZ)
    assert abs(chsh - 2 * math.sqrt(2)) < 1e-12


def _reduced_pair_of_triple():
    ghz = np.zeros(8, complex); ghz[0] = ghz[7] = 1 / math.sqrt(2)     # a triple account's diagonal
    rho = np.outer(ghz, ghz.conj()).reshape(2, 2, 2, 2, 2, 2)
    return np.einsum("abcdec->abde", rho).reshape(4, 4)               # trace the third ring


def test_a_pair_inside_a_triple_account_cannot_exceed_two():
    rho = _reduced_pair_of_triple()
    # Horodecki: the maximum CHSH over ALL settings is 2 sqrt(sum of the two largest eigenvalues of T^T T)
    paulis = [ring(2)[0], 1j * ring(2)[0] @ ring(2)[1], ring(2)[1]]    # X, Y, Z
    T = np.array([[np.real(np.trace(rho @ np.kron(a, b))) for b in paulis] for a in paulis])
    ev = sorted(np.linalg.eigvalsh(T.T @ T), reverse=True)
    assert abs(2 * math.sqrt(ev[0] + ev[1]) - 2.0) < 1e-12           # exactly the classical bound
    # and with the register's own settings the same
    Z, X, F, ZFZ = _register_settings()
    def corr(A, B):
        return sum(sa * sb * np.real(np.trace(rho @ np.kron(Pa, Pb)))
                   for sa, Pa in _projectors(A) for sb, Pb in _projectors(B))
    assert abs(corr(Z, F) + corr(Z, ZFZ) + corr(X, F) - corr(X, ZFZ)) <= 2.0 + 1e-12


def test_the_triple_account_carries_the_correlation_itself():
    """Mermin's combination on the triple's diagonal: 4, the maximum, against
    the classical 2 — the correlation lives in the account, not in its pairs."""
    X = ring(2)[0]; Y = 1j * X @ ring(2)[1]
    ghz = np.zeros(8, complex); ghz[0] = ghz[7] = 1 / math.sqrt(2)
    M = kron(X, X, X) - kron(X, Y, Y) - kron(Y, X, Y) - kron(Y, Y, X)
    assert abs(np.real(ghz.conj() @ M @ ghz) - 4.0) < 1e-12


def test_never_unioned_pairs_stay_at_two():
    Z, X, F, ZFZ = _register_settings()
    worst = 0.0
    for _ in range(300):
        a = RNG.normal(size=2) + 1j * RNG.normal(size=2); a /= np.linalg.norm(a)
        b = RNG.normal(size=2) + 1j * RNG.normal(size=2); b /= np.linalg.norm(b)
        worst = max(worst, abs(_chsh_born(np.kron(a, b), Z, X, F, ZFZ)))
    assert worst <= 2.0 + 1e-9


# --- the paper carries it -----------------------------------------------------------

def test_the_paper_builds_the_field_sector_and_closes_the_named_item():
    assert "**The field sector: many rings compose as a product of accounts.**" in FLAT
    assert "one root of unity per sector, of order the least common multiple" in FLAT
    assert "exactly half of the state's integers, for every composition" in FLAT
    assert "dimension of one ring, not of m" in FLAT
    assert "unioned as part of a triple account reads at most two" in FLAT
    
    assert "The field sector's state space, as the composition of rings." not in FLAT
