"""polar_wave.py — the quantized polar wavefunction (exact arithmetic).

THE OBJECT: a state on the ring Z/n is a list of n pairs (A_k, m_k):
  A_k — integer amplitude of mode k;
  m_k — integer phase EXPONENT (the phase is the root of unity w^{m_k}).
Nothing continuous anywhere: the state is 2n integers. Engine law holds
(no floats, no seated limits) — phases live as exponents mod n, so all
Weyl/evolution algebra is exact integer arithmetic.

THE OPERATORS (the banked Weyl pair, Part Vb):
  shift S : psi'(k) = psi(k-1)          (rotate the modes)
  clock C : psi'(k) = w^k psi(k)        (m_k -> m_k + k)
  Weyl relation: C S = w * S C          (a global +1 on every exponent)

THE EVOLUTION (the clock object): one tick advances mode k by 3k —
  the 3/8 phase rate on the octave ring (n = 8): the discrete e^{-iE_k t}
  with the harmonic ladder E_k ∝ k and the escapement rate 3.

THE LOSSY MAP (the shield, CHAPTER-rest-value-lossy-observer): Born
  reads |psi|^2 = the A_k^2 list and DISCARDS every m_k — exactly half
  the object's integers. The kept half is magnitude (the E-face);
  the discarded half is phase/circulation (the M-face).
"""

def shift(state):
    return [state[-1]] + state[:-1]


def clock(state, n=None):
    n = n or len(state)
    return [(A, (m + k) % n) for k, (A, m) in enumerate(state)]


def global_phase(state, p, n=None):
    n = n or len(state)
    return [(A, (m + p) % n) for (A, m) in state]


def tick(state, rate=3, n=None):
    """One clock-tick: mode k advances by rate*k (the 3/8 evolution)."""
    n = n or len(state)
    return [(A, (m + rate * k) % n) for k, (A, m) in enumerate(state)]


def born(state):
    """The lossy readout: squared magnitudes, phases discarded."""
    return [A * A for (A, _) in state]


def info_content(state):
    """(total integers in the state, integers surviving Born)."""
    return 2 * len(state), len(state)
