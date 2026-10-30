"""The one-loop moment engine of 15 October (verify/test_the_moment_on_the_pair.py), ported to a count object so that the
present count and a count of another kind run through the same code; the per-tick erasure of 17 October built in
(18 October 2026; the count whose chiralities share a momentum, from BRIEF-THE-COUNT-WHOSE-CHIRALITIES-SHARE-A-MOMENTUM).

A count object supplies: W0(k, th) the free 4 x 4 step at count momentum k (m, 3); eps(k, th) its quasienergy; and
X(kout, kin, modes), the per-tick vertex W0(kout)^-1 <kout| W_A |kin> for the distinct light modes [(K, A)], each inserted
once. Two counts are defined here.
  * PresentCount: the pair's count, the block (k, k + KV) with the copy-staggered turn tau_x s_z (R3's Ublk, turn, X).
  * DiracCount: the Dirac doublet, two species at the SAME momentum, the first stepping with the word U_A and the second
    with its inverse U_A^-1, the mass the on-site turn cos th - i sin th tau_x. The second species' coupling to light is the
    inverse rule, U_A^-1 = U^-1 - U^-1 V U^-1 + U^-1 V U^-1 V U^-1 - ..., enumerated over ordered set partitions of the
    inserted modes (word_inv).
The rules, the diagrams, the time sums, the Coulomb sector, the external states and the assembly are R3's, unchanged; the
erasure (erase=True) damps every internal count line by |cos(eps/2)| per tick in both time orderings, as in the 17 October
scratch step2.py, which this module reproduces to 1e-9 on the present count (checked in the rung-1 battery).

The gauge-invariant erasure (18 October 2026, the rounding as a Kraus operator with its vertices; kraus='WR'): per tick the
count steps by W_A and is rounded by R_A = (1 + W_A)/2 (the branch (1 - W_A)/2 dissipated), the survivor map
S_A = W_A R_A = (W_A + W_A^2)/2, the record's W^N R at N = 1. Its free eigenvalue f(lam) = lam (1 + lam)/2 carries the 17 October
modulus cos(eps/2) and the half-quasienergy turn. The vertex is that of S_A, X_S = X + (1 + W0)^{-1}(X W0 + X W0 X) by coefficient
of the inserted modes; every count line carries f (particles) or conj f (holes: the band vacuum held stationary, a deviation of
the one-body correlation evolving as S_A dC S_A^dag); the external count is on shell at the damped eigenvalue, e^{i omega} = 1/f.
kraus='R' is the reading S_A = R_A alone (the rounded time replacing the tick), kept for the Ward comparison.
Found in rung 1 (18 October, the Ward identity as the arbiter): the covariant erasure over the band vacuum is the kept branch
Gamma(S_A) of the whole many-body step, so EVERY line carries f forward and 1/f backward (holes amplified by 1/cos(eps/2), finite
in the resolvent form), the rules being R3's with lam -> f(lam) throughout; damping the holes by conj f (the quasiparticle
channel, the 17 October prescription) is not covariant (residual 0.23) and is kept as hole='conj' for the record.
"""

import itertools

import numpy as np

from test_the_general_vertex_of_the_pair import PI, KV, SX, word, turn, block, d_vec, c_of
from test_the_exchange_on_the_pair import LIFTS, f_pair

I2, I4 = np.eye(2), np.eye(4)
YHAT = np.array([0.0, 1.0, 0.0])


def H(M):
    return np.conj(np.swapaxes(M, -1, -2))


# ======================= the counts =======================

class PresentCount:
    """The pair's count: the block (k, k + KV) with the copy-staggered turn."""
    name = 'present'

    def W0(self, k, th):
        k = np.atleast_2d(k)
        return turn(th) @ block(word(k, []), word(k + KV, []))

    def eps(self, k, th):
        return np.arccos(np.clip(np.cos(th) * np.cos(np.atleast_2d(k)).prod(-1), -1, 1))

    def X(self, kout, kin, modes):
        kin, kout = np.atleast_2d(kin), np.atleast_2d(kout)
        a = H(word(kout, [])) @ word(kin, modes)
        b = H(word(kout + KV, [])) @ word(kin + KV, modes)
        return block(a, b)


def _ordered_partitions(items):
    """All ordered set partitions (B_1, ..., B_m) of a list."""
    items = list(items)
    if not items:
        yield ()
        return
    first, rest = items[0], items[1:]
    for part in _ordered_partitions(rest):
        # put first into an existing block, or as a new block at any position
        for i in range(len(part)):
            yield part[:i] + (part[i] + [first],) + part[i + 1:]
        for i in range(len(part) + 1):
            yield part[:i] + ([first],) + part[i:]


def word_inv(k, modes):
    """The coefficient of prod_i A_i in U_A^-1 for the distinct modes [(K_i, A_i)], at input momentum k (m, 2, 2):
    sum over ordered set partitions (B_1..B_m) of (-1)^m U^-1(k_m) word(k_{m-1}, B_m) U^-1(k_{m-1}) ... word(k_0, B_1) U^-1(k_0),
    k_j = k_{j-1} + sum_{i in B_j} K_i."""
    k = np.atleast_2d(np.asarray(k, float))
    m = len(k)
    modes = [(np.broadcast_to(np.atleast_2d(K), (m, 3)).astype(float), A) for K, A in modes]
    out = np.zeros((m, 2, 2), complex)
    for part in _ordered_partitions(range(len(modes))):
        kk = k.copy()
        acc = H(word(kk, []))
        for Bj in part:
            acc = word(kk, [modes[i] for i in Bj]) @ acc
            kk = kk + sum(modes[i][0] for i in Bj)
            acc = H(word(kk, [])) @ acc
        out += (-1) ** len(part) * acc
    return out


class DiracCount:
    """The Dirac doublet: species 1 steps with U_A, species 2 with U_A^-1, both at momentum k; the mass tau_x."""
    name = 'dirac'

    def W0(self, k, th):
        k = np.atleast_2d(k)
        U = word(k, [])
        return self.turn(th) @ block(U, H(U))

    @staticmethod
    def turn(th):
        return np.cos(th) * I4 - 1j * np.sin(th) * np.kron(SX, I2)

    def eps(self, k, th):
        return np.arccos(np.clip(np.cos(th) * np.cos(np.atleast_2d(k)).prod(-1), -1, 1))

    def X(self, kout, kin, modes):
        kin, kout = np.atleast_2d(kin), np.atleast_2d(kout)
        a = H(word(kout, [])) @ word(kin, modes)
        b = word(kout, []) @ word_inv(kin, modes)
        return block(a, b)


# ======================= the engine =======================

def photon(K):
    """rho (pair factor folded in), two real transverse polarizations (m, 2, 3), mu = e^{-i sigma w}, sigma, w."""
    K = np.atleast_2d(K)
    c = c_of(K)
    sig = np.where(c >= 0, 1.0, -1.0)
    w = 2 * np.arccos(np.clip(np.abs(c), 0, 1))
    sw = np.sin(w)
    with np.errstate(divide='ignore', invalid='ignore'):
        rho = np.where(sw > 1e-14, np.abs(c) / (2 * sw), 0.25)
    rho = rho * f_pair(K) ** 2
    d = d_vec(K)
    dh = d / np.linalg.norm(d, axis=1)[:, None]
    a = np.where(np.abs(dh[:, [0]]) < 0.9, np.array([[1.0, 0, 0]]), np.array([[0, 1.0, 0]]))
    e1 = a - (a * dh).sum(1)[:, None] * dh
    e1 /= np.linalg.norm(e1, axis=1)[:, None]
    e2 = np.cross(dh, e1)
    return rho, np.stack([e1, e2], 1), np.exp(-1j * sig * w), sig, w


def sandwich(L, P, R, wgt):
    return (L @ P @ R) * wgt[:, None, None]


def chi(r, R1, R2):
    t = np.clip((r - R1) / (R2 - R1), 1e-12, 1 - 1e-12)
    a, b = np.exp(-1 / t), np.exp(-1 / (1 - t))
    out = 1 - a / (a + b)
    return np.where(r <= R1, 1.0, np.where(r >= R2, 0.0, out))


class Engine:
    def __init__(self, count, erase=False, lifts=None, kraus=None):
        self.C = count
        self.erase = erase
        self.kraus = kraus                      # None | 'WR' (the step then the rounding) | 'R' (the rounding alone)
        self.free_omega = False                 # the K3' variant: the external count at its free real quasienergy
        self.light_kraus = False                # light's own one-body rounding per tick: the photon line carries mu (1 + mu)/2
        self.light_clock = False                # 19 October: light's clock matched to the count's without the erasure's modulus:
                                                # the photon line carries e^{-3 i sigma w/2} (model C' of the one-clock brief)
        self.hole = 'inv' if kraus else 'conj'  # the backward factor: 'inv' (1/f, the kept branch Gamma(S_A), covariant) | 'conj' (conj f, holes damped: not covariant)
        self.lifts = LIFTS if lifts is None else lifts

    # ---------------- the rounding ----------------
    def f(self, lam):
        """The per-tick factor of a free mode of eigenvalue lam under the survivor map."""
        if self.kraus == 'WR':
            return lam * (1 + lam) / 2
        if self.kraus == 'R':
            return (1 + lam) / 2
        return lam

    def bar(self, lam):
        """The backward (hole) factor of a line of forward factor lam: conj(lam) or 1/lam, equal on the unit circle."""
        return np.conj(lam) if self.hole == 'conj' else 1 / lam

    def fl(self, mu, sig=None, w=None):
        """The photon's per-tick factor: mu; mu (1 + mu)/2 when light is rounded too (light_kraus); e^{-3 i sigma w/2}, the
        clock's turn without the modulus, when light's clock is matched (light_clock; sig and w are then required)."""
        if self.light_kraus:
            return mu * (1 + mu) / 2
        if self.light_clock:
            return np.exp(-1.5j * sig * w)
        return mu

    def onshell(self, eps):
        """The external count's quasienergy omega with e^{i omega} = 1/f(e^{-i eps}): complex when rounded."""
        if self.kraus and not self.free_omega:
            return 1j * np.log(self.f(np.exp(-1j * np.asarray(eps, dtype=complex))))
        return eps

    def kmass(self, th, h=1e-3):
        """The kinetic mass of the free dispersion at rest, 1/Re d^2 E'/dk^2 with e^{-iE'} = f(lam(k)); tan(th) unrounded."""
        if not self.kraus:
            return np.tan(th)
        E = [self.onshell(self.C.eps(np.array([kk, 0, 0.0]), th)[0]) for kk in (0.0, h, 2 * h)]
        d2 = (16 * (E[1] - E[0]) / h ** 2 - (E[2] - E[0]) / h ** 2) / 6
        return 1 / np.real(d2)

    # ---------------- spectral data ----------------
    def spectral(self, k, th, vac):
        """eps, (P_U, P_F), (lam_U, lam_F), (n_U, n_F) at count momenta k (m, 3)."""
        k = np.atleast_2d(k)
        W0 = self.C.W0(k, th)
        eps = self.C.eps(k, th)
        lU, lF = np.exp(-1j * eps), np.exp(1j * eps)
        PU = (W0 - lF[:, None, None] * I4) / (lU - lF)[:, None, None]
        PF = I4 - PU
        free = (lU, lF)                          # the free eigenvalues: the static sea's own response is undamped
        lU, lF = self.f(lU), self.f(lF)          # the line factors (lam itself when unrounded)
        nF = np.ones(len(k))
        if vac == 'rounded':
            nF = np.cos(eps / 2) ** 2 * np.cos(k[:, 0] / 2) ** 2
        elif vac == 'rounded-time':
            nF = np.cos(eps / 2) ** 2
        elif vac == 'empty':
            nF = np.zeros(len(k))                # no sea: the one-count theory (a diagnostic)
        return eps, (PU, PF), (lU, lF), (np.zeros(len(k)), nF), free

    @staticmethod
    def nmat(sp):
        _, (PU, PF), _, (nU, nF) = sp[:4]
        return nU[:, None, None] * PU + nF[:, None, None] * PF

    def X(self, kout, kin, modes):
        """The per-tick vertex: the count's X, or the rounding's X_S when kraus is set."""
        X = self.C.X
        if not self.kraus:
            return X(kout, kin, modes)
        kin, kout = np.atleast_2d(kin), np.atleast_2d(kout)
        m = max(len(kin), len(kout), max((len(np.atleast_2d(K)) for K, _ in modes), default=1))
        kin, kout = np.broadcast_to(kin, (m, 3)), np.broadcast_to(kout, (m, 3))
        th = self._th
        Wout = self.C.W0(kout, th)
        inv = np.linalg.inv(np.broadcast_to(I4, (m, 4, 4)) + Wout)
        Xf = X(kout, kin, modes)
        if self.kraus == 'R':                                   # S_A = (1 + W_A)/2: X_S = (1 + W0)^-1 W0 X
            return inv @ Wout @ Xf
        acc = Xf @ self.C.W0(kin, th)                           # X W0
        idx = list(range(len(modes)))
        for r in range(1, len(modes)):                          # X_{M1} W0 X_{M2}, every ordered split
            for M2 in itertools.combinations(idx, r):
                M1 = [i for i in idx if i not in M2]
                kmid = kin + sum(np.broadcast_to(np.atleast_2d(modes[i][0]), (m, 3)) for i in M2)
                acc = acc + X(kout, kmid, [modes[i] for i in M1]) @ self.C.W0(kmid, th) @ X(kmid, kin, [modes[i] for i in M2])
        return Xf + inv @ acc

    def _damp(self, lam):
        return np.abs(np.cos(np.angle(lam) / 2)) if self.erase else 1.0

    # ---------------- time sums ----------------
    def fw(self, om, sp, mu, sig):
        out = []
        for lam, n in zip(sp[2], sp[3]):
            r = self._damp(lam)
            Y = r * np.exp(1j * om) * lam * mu
            Z = r * np.exp(-1j * om) * self.bar(lam) * mu
            out.append((1 - n) * Y / (1 - Y) - n * Z / (1 - Z))
        return out

    def dfw(self, om, sp, mu, sig, h=1e-6):
        a, b = self.fw(om + h, sp, mu, sig), self.fw(om - h, sp, mu, sig)
        return [(x - y) / (2 * h) for x, y in zip(a, b)]

    def _S_C(self, sp2, sp1, om, mu, sig):
        out = {}
        for g in range(2):
            for gp in range(2):
                l1, n1 = sp2[2][g], sp2[3][g]
                l2, n2 = sp1[2][gp], sp1[3][gp]
                r1, r2 = self._damp(l1), self._damp(l2)
                x1, x2 = np.exp(1j * om) * l1, np.exp(1j * om) * l2
                Y1, Y2 = r1 * x1 * mu / (1 - r1 * x1 * mu), r2 * x2 * mu / (1 - r2 * x2 * mu)
                if not self.kraus:                               # the 15 and 17 October expressions, verbatim
                    Z1 = r1 * np.conj(x1) * mu / (1 - r1 * np.conj(x1) * mu)
                    Z2 = r2 * np.conj(x2) * mu / (1 - r2 * np.conj(x2) * mu)
                    R = r1 * r2 * x1 * np.conj(x2)
                    Rp = r1 * r2 * np.conj(x1) * x2
                else:
                    xb1, xb2 = np.exp(-1j * om) * self.bar(l1), np.exp(-1j * om) * self.bar(l2)
                    Z1 = r1 * xb1 * mu / (1 - r1 * xb1 * mu)
                    Z2 = r2 * xb2 * mu / (1 - r2 * xb2 * mu)
                    if self.hole == 'conj':
                        m1, m2 = sp2[4][g], sp1[4][gp]           # model B': the static pair the field creates from the sea, undamped
                        R = r1 * r2 * m1 * np.conj(m2)
                        Rp = r1 * r2 * np.conj(m1) * m2
                    else:
                        R = r1 * r2 * x1 * xb2                   # Gamma(S): f_g / f_g'
                        Rp = r1 * r2 * xb1 * x2
                with np.errstate(divide='ignore', invalid='ignore'):
                    rr = np.where(np.abs(1 - R) > 1e-13, R / (1 - R), 0)
                    rp = np.where(np.abs(1 - Rp) > 1e-13, Rp / (1 - Rp), 0)
                s = (1 - n1) * (1 - n2) * Y1 * Y2 + n1 * n2 * Z1 * Z2
                s = s - (1 - n1) * n2 * rr * (1 + Y1 + Z2) - n1 * (1 - n2) * rp * (1 + Y2 + Z1)
                out[(g, gp)] = s
        return out

    def gint(self, om, sp):
        """The leg's internal line: (1 - n) Y/(1 - Y) - n Z/(1 - Z), Y = e^{i om} lam, Z = e^{-i om} conj(lam); on the unit
        circle this is ((1 - n) x + n)/(1 - x), the 15 October form."""
        out = []
        for lam, n in zip(sp[2], sp[3]):
            x = np.exp(1j * om) * lam
            if not self.kraus:
                out.append(((1 - n) * x + n) / (1 - x))
            else:
                Z = np.exp(-1j * om) * self.bar(lam)
                out.append((1 - n) * x / (1 - x) - n * Z / (1 - Z))
        return out

    # ---------------- self-energy ----------------
    def sigma_K(self, k, om, th, vacs, K, want_d=False):
        self._th = th
        m = len(K)
        kk = np.broadcast_to(np.atleast_2d(k), (m, 3))
        kp = kk + K
        rho, E, mu, sig, w = photon(K)
        mu = self.fl(mu, sig, w)
        SP = {v: self.spectral(kp, th, v) for v in vacs}
        S = {v: np.zeros((m, 4, 4), complex) for v in vacs}
        dS = {v: np.zeros((m, 4, 4), complex) for v in vacs}
        F = {v: self.fw(om, SP[v], mu, sig) for v in vacs}
        dF = {v: self.dfw(om, SP[v], mu, sig) for v in vacs} if want_d else None
        for j in range(2):
            e = E[:, j]
            Xe = self.X(kp, kk, [(K, e)])
            Xa = self.X(kk, kp, [(-K, e)])
            sea = self.X(kk, kk, [(K, e), (-K, e)])
            for v in vacs:
                sp = SP[v]
                S[v] += (0.5 * sea - Xa @ self.nmat(sp) @ Xe) * rho[:, None, None]
                for g in range(2):
                    P = sp[1][g]
                    S[v] += sandwich(Xa, P, Xe, rho * F[v][g])
                    if want_d:
                        dS[v] += sandwich(Xa, P, Xe, rho * dF[v][g])
        return (S, dS) if want_d else S

    @staticmethod
    def Vcoul(p):
        dp = d_vec(p)
        return c_of(p) ** 2 / (8 * (dp * dp).sum(1))

    def sigma_C(self, k, th, vac, p):
        self._th = th
        m = len(p)
        kk = np.broadcast_to(np.atleast_2d(k), (m, 3))
        V = self.Vcoul(p)
        sp = self.spectral(kk + p, th, vac)
        return -1j * V[:, None, None] * (0.5 * I4 - self.nmat(sp))

    # ---------------- the vertex ----------------
    def vertex_K(self, kin, kout, om, th, vacs, K, ext):
        self._th = th
        m = len(K)
        kin = np.broadcast_to(np.atleast_2d(kin), (m, 3))
        kout = np.broadcast_to(np.atleast_2d(kout), (m, 3))
        Ke, Ae = ext
        Ke = np.broadcast_to(np.atleast_2d(Ke), (m, 3))
        k1, k2 = kin + K, kout + K
        km_in, km_out = kin - K, kout - K
        rho, E, mu, sig, w = photon(K)
        mu = self.fl(mu, sig, w)
        SPS = {v: [self.spectral(kk_, th, v) for kk_ in (kin, kout, k1, k2, km_in, km_out)] for v in vacs}
        ea = [(Ke, Ae)]
        Xa_oi = self.X(kout, kin, ea)
        Xa_21 = self.X(k2, k1, ea)
        Xa_mm = self.X(km_out, km_in, ea)
        pre = {}
        for v in vacs:
            sp_in, sp_out, sp1, sp2, spmi, spmo = SPS[v]
            pre[v] = (list(map(self.nmat, (sp_in, sp_out, sp1, sp2, spmi, spmo))), self._S_C(sp2, sp1, om, mu, sig),
                      self.fw(om, sp1, mu, sig), self.fw(om, sp2, mu, sig), sp1, sp2)
        outs = {v: np.zeros((m, 4, 4), complex) for v in vacs}
        for j in range(2):
            e = E[:, j]
            pK, pmK = (K, e), (-K, e)
            X1_1i = self.X(k1, kin, [pK])
            X1_o2 = self.X(kout, k2, [pmK])
            X1_i1 = self.X(kin, k1, [pmK])
            X1_2o = self.X(k2, kout, [pK])
            X1_mi = self.X(km_in, kin, [pmK])
            X1_imi = self.X(kin, km_in, [pK])
            X1_mo = self.X(km_out, kout, [pmK])
            X1_omo = self.X(kout, km_out, [pK])
            Xa1_2i = self.X(k2, kin, ea + [pK])
            Xa1_o1 = self.X(kout, k1, ea + [pmK])
            Xa1_omi = self.X(kout, km_in, ea + [pK])
            S_in = self.X(kin, kin, [pK, pmK])
            S_out = self.X(kout, kout, [pK, pmK])
            Xa11 = self.X(kout, kin, ea + [pK, pmK])
            for v in vacs:
                (n_in, n_out, n1, n2, nmi, nmo), SC, F1, F2, sp1, sp2 = pre[v]
                out = outs[v]
                A = (0.5 * Xa11 - 0.5 * Xa_oi @ n_in @ S_in - 0.5 * S_out @ n_out @ Xa_oi
                     - Xa1_omi @ nmi @ X1_mi - X1_o2 @ n2 @ Xa1_2i
                     + Xa_oi @ n_in @ X1_imi @ nmi @ X1_mi
                     + X1_omo @ nmo @ Xa_mm @ nmi @ X1_mi
                     + X1_omo @ nmo @ X1_mo @ n_out @ Xa_oi)
                out += A * rho[:, None, None]
                Ya1_o1 = Xa1_o1 - Xa_oi @ n_in @ X1_i1 - X1_o2 @ n2 @ Xa_21
                Ya1_2i = Xa1_2i - Xa_21 @ n1 @ X1_1i - X1_2o @ n_out @ Xa_oi
                for g in range(2):
                    out += sandwich(Ya1_o1, sp1[1][g], X1_1i, rho * F1[g])
                    out += sandwich(X1_o2, sp2[1][g], Ya1_2i, rho * F2[g])
                for g in range(2):
                    for gp in range(2):
                        out += (X1_o2 @ sp2[1][g] @ Xa_21 @ sp1[1][gp] @ X1_1i) * (rho * SC[(g, gp)])[:, None, None]
        return outs

    def vertex_C(self, kin, kout, th, vac, p, ext):
        self._th = th
        m = len(p)
        kin = np.broadcast_to(np.atleast_2d(kin), (m, 3))
        kout = np.broadcast_to(np.atleast_2d(kout), (m, 3))
        Ke, Ae = ext
        Ke = np.broadcast_to(np.atleast_2d(Ke), (m, 3))
        V = self.Vcoul(p)
        s2, s1 = self.spectral(kout + p, th, vac), self.spectral(kin + p, th, vac)
        Xa = self.X(kout + p, kin + p, [(Ke, Ae)])
        out = np.zeros((m, 4, 4), complex)
        for g in range(2):
            for gp in range(2):
                dn = s2[3][g] - s1[3][gp]
                if not self.kraus:
                    den = 1 - s1[2][gp] / s2[2][g]
                elif self.hole == 'conj':
                    den = 1 - s1[4][gp] * np.conj(s2[4][g])      # model B': the static pair, undamped
                else:
                    den = 1 - s1[2][gp] * self.bar(s2[2][g])    # Gamma(S): 1 - f_g'/f_g
                with np.errstate(divide='ignore', invalid='ignore'):
                    fac = np.where(np.abs(den) > 1e-13, dn / den, 0)
                out += (s2[1][g] @ Xa @ s1[1][gp]) * (1j * V * fac)[:, None, None]
        return out

    # ---------------- external states and the assembly ----------------
    def doublet(self, k, th):
        sp = self.spectral(np.atleast_2d(k), th, 'band')
        PU = sp[1][0][0]
        P0 = self.spectral(np.zeros((1, 3)), th, 'band')[1][0][0]
        w_, V_ = np.linalg.eigh((P0 + H(P0)) / 2)
        B0 = V_[:, w_ > 0.5]
        u = PU @ B0
        s, Vs = np.linalg.eigh(H(u) @ u)
        return u @ Vs @ np.diag(s ** -0.5) @ H(Vs)

    def point_integrand(self, p, th, Q, vacs, hk):
        m = len(p)
        self._th = th
        kin, kout = np.array([-Q / 2, 0, 0]), np.array([Q / 2, 0, 0])
        om = self.onshell(np.arccos(np.cos(th) * np.cos(Q / 2)))
        ext = (np.array([Q, 0, 0]), YHAT * (1 + np.cos(Q / 2)) / 2)
        ks = {'0': np.zeros(3), '1': np.array([hk, 0, 0]), '2': np.array([2 * hk, 0, 0])}
        names = ('Sin', 'dSin', 'Sout', 'dSout', 'Lam', 'S0', 'S1', 'S2')
        res = {v: {nm: np.zeros((m, 4, 4), complex) for nm in names} for v in vacs}
        for n in self.lifts:
            K = p + 2 * PI * n
            for nm, kk in (('in', kin), ('out', kout)):
                a, b = self.sigma_K(kk, om, th, vacs, K, want_d=True)
                for v in vacs:
                    res[v]['S' + nm] += a[v] / 8
                    res[v]['dS' + nm] += b[v] / 8
            L = self.vertex_K(kin, kout, om, th, vacs, K, ext)
            for v in vacs:
                res[v]['Lam'] += L[v] / 8
            for nm, kk in ks.items():
                e_k = self.onshell(self.C.eps(kk, th)[0])
                a = self.sigma_K(kk, e_k, th, vacs, K)
                for v in vacs:
                    res[v]['S' + nm] += a[v] / 8
        for v in vacs:
            r = res[v]
            r['SCin'], r['SCout'] = self.sigma_C(kin, th, v, p), self.sigma_C(kout, th, v, p)
            for nm, kk in ks.items():
                r['S' + nm] = r['S' + nm] + self.sigma_C(kk, th, v, p)
            r['CLam'] = self.vertex_C(kin, kout, th, v, p, ext)
        return res

    def assemble(self, I, th, Q, vac, hk):
        """F2 per q^2 and its parts from the integrated one-loop quantities I (dict of (4, 4))."""
        self._th = th
        kin, kout = np.array([[-Q / 2, 0, 0]]), np.array([[Q / 2, 0, 0]])
        om = self.onshell(np.arccos(np.cos(th) * np.cos(Q / 2)))
        ext = (np.array([[Q, 0, 0]]), YHAT * (1 + np.cos(Q / 2)) / 2)
        Ya = self.X(kout, kin, [ext])[0]
        ui, uo = self.doublet(kin[0], th), self.doublet(kout[0], th)
        spi, spo = self.spectral(kin, th, vac), self.spectral(kout, th, vac)
        Sin = I['Sin'] + I['SCin']
        Sout = I['Sout'] + I['SCout']
        gi_in, gi_out = self.gint(om, spi), self.gint(om, spo)
        leg = Sout @ spo[1][1][0] * gi_out[1][0] @ Ya + Ya @ spi[1][1][0] * gi_in[1][0] @ Sin
        cross = Ya @ (I4 - self.nmat(spi)[0]) @ I['SCin'] - I['SCout'] @ self.nmat(spo)[0] @ Ya
        G = I['Lam'] + I['CLam'] + leg + cross
        T0 = H(uo) @ Ya @ ui
        sin_P, sout_P = H(ui) @ Sin @ ui, H(uo) @ Sout @ uo
        dsin_P, dsout_P = H(ui) @ I['dSin'] @ ui, H(uo) @ I['dSout'] @ uo
        T1 = H(uo) @ G @ ui - 0.5 * (T0 @ sin_P + sout_P @ T0) + 0.5j * (dsout_P @ T0 + T0 @ dsin_P)
        TW = H(uo) @ self.C.X(kout, kin, [ext])[0] @ ui          # the unitary walk's tree amplitude: the Zeeman structure
        nrm = np.real(np.trace(H(TW) @ TW))
        z0 = np.real(np.trace(H(TW) @ T0)) / nrm                 # the rounded tree amplitude's Zeeman coefficient (1 unrounded)
        z1 = np.trace(H(TW) @ T1) / nrm                          # complex when rounded: Im is the decay's field dependence
        delta = z1 / z0
        perp = T1 - delta * T0
        dE = []
        for nm, kk in (('S0', 0.0), ('S1', hk), ('S2', 2 * hk)):
            PU = self.spectral(np.array([[kk, 0, 0]]), th, 'band')[1][0][0]
            dE.append(0.5j * np.trace(PU @ I[nm]))
        d2 = (16 * (dE[1] - dE[0]) / hk ** 2 - (dE[2] - dE[0]) / hk ** 2) / 6
        F2 = np.real(delta) - self.kmass(th) * np.real(d2)
        return dict(F2=F2, delta=delta, d2=d2, dE0=dE[0], perp=np.max(np.abs(perp)) / np.sqrt(nrm / 2),
                    sinP=sin_P, T0=T0)

    def integrate(self, pts, W, th, Q, vacs, hk, B=1024):
        tot = {v: None for v in vacs}
        for i in range(0, len(pts), B):
            r = self.point_integrand(pts[i:i + B], th, Q, vacs, hk)
            w = W[i:i + B]
            for v in vacs:
                part = {k: np.einsum('m,mab->ab', w, x) for k, x in r[v].items()}
                tot[v] = part if tot[v] is None else {k: tot[v][k] + part[k] for k in part}
        return tot

    # ---------------- tree level and the Ward identity ----------------
    def tree_g_half(self, th, Q):
        kin, kout = np.array([[-Q / 2, 0, 0]]), np.array([[Q / 2, 0, 0]])
        ext = (np.array([[Q, 0, 0]]), YHAT * (1 + np.cos(Q / 2)) / 2)
        self._th = th
        T0 = H(self.doublet(kout[0], th)) @ self.X(kout, kin, [ext])[0] @ self.doublet(kin[0], th)
        TW = H(self.doublet(kout[0], th)) @ self.C.X(kout, kin, [ext])[0] @ self.doublet(kin[0], th)
        z0 = np.real(np.trace(H(TW) @ T0)) / np.real(np.trace(H(TW) @ TW))      # the Zeeman coefficient (see assemble)
        return 2 * self.kmass(th) * z0 * np.sqrt(np.real(np.trace(H(TW) @ TW)) / 2) / Q, T0

    def ward_parts(self, p, th, kap, vac='band'):
        """At zero transfer: (the dressed on-shell y-vertex, the dressed quasienergy shift, the tree vertex) at k = (0, kap, 0),
        per photon momentum p (m, 3); the Ward identity says the first is minus the slope of the second once p and -p are
        paired."""
        self._th = th
        k = np.array([0, kap, 0.0])
        om = self.onshell(self.C.eps(k, th)[0])
        ext = (np.zeros(3), YHAT)
        m = len(p)
        Sig, dSig, Lam = (np.zeros((m, 4, 4), complex) for _ in range(3))
        for n in self.lifts:
            K = p + 2 * PI * n
            a, b = self.sigma_K(k, om, th, (vac,), K, want_d=True)
            Sig += a[vac] / 8
            dSig += b[vac] / 8
            Lam += self.vertex_K(k, k, om, th, (vac,), K, ext)[vac] / 8
        SC = self.sigma_C(k, th, vac, p)
        sp = self.spectral(np.atleast_2d(k), th, vac)
        Ya = self.X(np.atleast_2d(k), np.atleast_2d(k), [ext])[0]
        PU, PF = sp[1][0][0], sp[1][1][0]
        gi = self.gint(om, sp)
        S = Sig + SC
        G = (Lam + self.vertex_C(k, k, th, vac, p, ext) + S @ PF * gi[1][0] @ Ya + Ya @ PF * gi[1][0] @ S
             + Ya @ (I4 - self.nmat(sp)[0]) @ SC - SC @ self.nmat(sp)[0] @ Ya)
        t0 = 0.5 * np.trace(PU @ Ya)
        T1 = (0.5 * np.einsum('ab,mbc,ca->m', PU, G, PU) - t0 * 0.5 * np.einsum('ab,mba->m', PU, S)
              + 1j * t0 * 0.5 * np.einsum('ab,mba->m', PU, dSig))
        dE = 0.5j * np.einsum('ab,mba->m', PU, S)
        return 1j * T1, (dE if self.kraus else np.real(dE)), 1j * t0


# ======================= the grids of 17 October =======================

def ball_grid(th, R1, R2, n_log=24, n_lin=24, n_c=12, n_phi=16, rmin_frac=1e-5):
    rs, wr = [], []
    a, b = np.log(rmin_frac * th), np.log(3 * th)
    u, wu = np.polynomial.legendre.leggauss(n_log)
    lr = (b - a) / 2 * u + (b + a) / 2
    rs.append(np.exp(lr)); wr.append(wu * (b - a) / 2 * np.exp(lr))
    u, wu = np.polynomial.legendre.leggauss(n_lin)
    rs.append((R2 - 3 * th) / 2 * u + (R2 + 3 * th) / 2); wr.append(wu * (R2 - 3 * th) / 2)
    r, wr = np.concatenate(rs), np.concatenate(wr)
    c, wc = np.polynomial.legendre.leggauss(n_c)
    ph = 2 * PI * (np.arange(n_phi) + 0.5) / n_phi
    R_, C_, P_ = np.meshgrid(r, c, ph, indexing='ij')
    W = (wr[:, None, None] * r[:, None, None] ** 2 * chi(r, R1, R2)[:, None, None] * wc[None, :, None]
         * (2 * PI / n_phi)) * np.ones_like(R_)
    S_ = np.sqrt(1 - C_ ** 2)
    pts = np.stack([R_ * S_ * np.cos(P_), R_ * S_ * np.sin(P_), R_ * C_], -1).reshape(-1, 3)
    return pts, W.ravel() / (2 * PI) ** 3


def mid_grid(th, r_hi=0.6, n_r=40, n_c=12, n_phi=16):
    """The mid shell of 17 October: log-spaced radii from 2 th to r_hi, weight chi(r, 0.4, 0.6) - chi(r, 2 th, 4 th)."""
    r_lo = 2 * th
    u, wu = np.polynomial.legendre.leggauss(n_r)
    lr = (np.log(r_hi) - np.log(r_lo)) / 2 * u + (np.log(r_hi) + np.log(r_lo)) / 2
    r = np.exp(lr)
    wr = wu * (np.log(r_hi) - np.log(r_lo)) / 2 * r
    c, wc = np.polynomial.legendre.leggauss(n_c)
    ph = 2 * PI * (np.arange(n_phi) + 0.5) / n_phi
    Rr, C, P = np.meshgrid(r, c, ph, indexing='ij')
    Ss = np.sqrt(1 - C ** 2)
    pts = np.stack([Rr * Ss * np.cos(P), Rr * Ss * np.sin(P), Rr * C], -1).reshape(-1, 3)
    wm = chi(r, 0.4, 0.6) - chi(r, 2 * th, 4 * th)
    W = (wr[:, None, None] * r[:, None, None] ** 2 * wm[:, None, None] * wc[None, :, None] * (2 * PI / n_phi)
         * np.ones_like(Rr)).ravel() / (2 * PI) ** 3
    return pts, W


def far_grid(L, part=0, nparts=1):
    """The far region of 17 October: the L^3 lattice with weight 1 - chi(|p|, 0.4, 0.6), sliced into parts."""
    g = -PI + 2 * PI * np.arange(L) / L
    pts = np.stack(np.meshgrid(g, g, g, indexing='ij'), -1).reshape(-1, 3)
    W = (1 - chi(np.linalg.norm(pts, axis=1), 0.4, 0.6)) / L ** 3
    keep = W > 0
    pts, W = pts[keep], W[keep]
    sl = slice(part * len(pts) // nparts, (part + 1) * len(pts) // nparts)
    return pts[sl], W[sl]


def shell_grid(r, n_c=12, n_phi=16):
    """A thin spherical shell at radius r: the contribution per unit |p| (the shells of 17 October)."""
    c, wc = np.polynomial.legendre.leggauss(n_c)
    ph = 2 * PI * (np.arange(n_phi) + 0.5) / n_phi
    C, P = np.meshgrid(c, ph, indexing='ij')
    Ss = np.sqrt(1 - C ** 2)
    pts = r * np.stack([Ss * np.cos(P), Ss * np.sin(P), C], -1).reshape(-1, 3)
    W = (r ** 2 * wc[:, None] * (2 * PI / n_phi) * np.ones_like(C)).ravel() / (2 * PI) ** 3
    return pts, W


def add_dicts(a, b):
    return {k: a[k] + b[k] for k in a}
