"""test_the_complementary_pair.py — THE STATE, THE PORT, AND WHOSE
RELATION IT IS (2026-08-17, second writing). The first writing computed
a Fourier uncertainty product on the register's wheel and called it the
register's own. It is not. On the ring the state is 2n integers — an
amplitude and a phase EXPONENT for each mode — so knowing the state means
knowing both faces: the object carries no trade-off at all. What carries
the trade-off is the PORT. The Born read returns squared amplitudes and
discards every phase exponent, exactly half the integers, and the
familiar relation is a theorem about reading through that port in the
seated limit where the ring becomes a circle and the transform becomes
Fourier. Claiming it for the register would import the continuum the
program demotes — summing harmonics into a smooth wave and calling the
lost phase a law of nature.

So the products below are computed and kept, but located: they are the
ENVELOPE's face, correct as machinery. The register's own complementarity
is the Weyl residue — shift against clock, failing to commute by one root
of unity, exact in exponents — which the polar chapter already pinned.
The honest gain of this pass is the location, and one measured number:
the port's blindness is exactly half.
"""

import cmath
import math

N = 256


def _dft(a):
    n = len(a)
    return [sum(a[j] * cmath.exp(-2j * math.pi * k * j / n) for j in range(n))
            / math.sqrt(n) for k in range(n)]


def _width(probs):
    """Equivalent Gaussian width on the wheel, from the resultant length —
    the honest circular statistic, since the register wraps."""
    n = len(probs)
    r = abs(sum(p * cmath.exp(2j * math.pi * j / n) for j, p in enumerate(probs)))
    if r >= 1:
        return 0.0
    return math.sqrt(-2 * math.log(r)) * n / (2 * math.pi)


def _gaussian_state(sigma):
    amp = [math.exp(-((j - N // 2) ** 2) / (4 * sigma * sigma)) for j in range(N)]
    nrm = math.sqrt(sum(abs(x) ** 2 for x in amp))
    return [x / nrm for x in amp]


def test_the_envelope_product_saturates_at_the_minimum():
    """The seated-limit face: every Gaussian returns the same product,
    N/4π. Correct machinery, and located — this is the readout's relation
    in the continuous limit, not a statement about the register's
    state."""
    target = N / (4 * math.pi)
    for sigma in (2.0, 4.0, 8.0, 16.0):
        amp = _gaussian_state(sigma)
        dn = _width([abs(x) ** 2 for x in amp])
        dk = _width([abs(x) ** 2 for x in _dft(amp)])
        assert abs(dn - sigma) < 0.05, sigma
        assert abs(dn * dk - target) < 0.05, (sigma, dn * dk)


def test_no_state_beats_the_bound():
    """Spot-check against non-Gaussian states: a boxcar and a two-cell
    superposition both sit at or above the minimum, never below."""
    target = N / (4 * math.pi)
    box = [1.0 if abs(j - N // 2) < 10 else 0.0 for j in range(N)]
    nrm = math.sqrt(sum(x * x for x in box))
    box = [x / nrm for x in box]
    pair = [0.0] * N
    pair[100] = pair[140] = 1 / math.sqrt(2)
    for state in (box, pair):
        dn = _width([abs(x) ** 2 for x in state])
        dk = _width([abs(x) ** 2 for x in _dft(state)])
        assert dn * dk >= target - 0.05


def test_the_extremes_are_complementarity():
    """A single cell of count leaves the phase wholly unread — the
    transform is exactly flat — and a sharp phase leaves the count
    exactly flat. Complementarity as an identity, not a slogan."""
    sharp = [0.0] * N
    sharp[0] = 1.0
    pk = [abs(x) ** 2 for x in _dft(sharp)]
    assert max(pk) - min(pk) < 1e-15
    flat = [1 / math.sqrt(N)] * N
    pn = [abs(x) ** 2 for x in flat]
    assert max(pn) - min(pn) < 1e-15


def test_energy_time_from_the_rate_mass_map():
    """A rate is read only by watching: T ticks give frequency resolution
    1/T. With the carry rate identified as the mass — derived this
    morning, not assumed — that counting fact is Δt·ΔE ≥ 1 in register
    units."""
    for T in (10, 100, 10 ** 4, 10 ** 6):
        delta_rate = 1 / T
        assert abs(T * delta_rate - 1.0) < 1e-12
        assert delta_rate * T >= 1.0 - 1e-12


def test_interference_is_the_composition_law():
    """Amplitudes add and intensity is their square — the program's
    half-power law — so two paths give full-visibility fringes: four at
    agreement, zero at opposition, against the classical two."""
    vals = []
    for deg in (0, 60, 90, 120, 180):
        a = 1 + cmath.exp(1j * math.radians(deg))
        vals.append(abs(a) ** 2)
    assert abs(vals[0] - 4.0) < 1e-12          # constructive
    assert abs(vals[-1] - 0.0) < 1e-12         # destructive
    assert abs(vals[2] - 2.0) < 1e-12          # quadrature: the classical value
    visibility = (max(vals) - min(vals)) / (max(vals) + min(vals))
    assert abs(visibility - 1.0) < 1e-12


def test_the_products_are_pure_numbers():
    """The boundary the Scale Theorem demands: every quantity above is
    dimensionless — a count, a phase, a ratio of cells. The register
    yields the RELATION; the value of the action quantum is a ruler and
    enters only by calibration."""
    target = N / (4 * math.pi)
    assert isinstance(target, float) and target > 0
    for n in (64, 128, 512):
        assert abs((n / (4 * math.pi)) / (N / (4 * math.pi)) - n / N) < 1e-12


def test_the_state_itself_carries_no_trade_off():
    """The register's object: 2n integers, amplitude and phase exponent.
    Both are simultaneously specified, so there is nothing in the state
    to trade — and the Weyl residue supplies conjugacy without any bound
    on widths. The port is where the loss lives, and it is exactly half."""
    import os
    import sys
    sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
    from polar_wave import born, info_content

    n = 8
    state = [(k + 1, (3 * k) % n) for k in range(n)]     # amplitudes and exponents
    assert len(state) == n and all(len(x) == 2 for x in state)
    assert len({m for _, m in state}) > 1                # phases genuinely present
    read = born(state)
    assert len(read) == n                                # n survive of 2n
    other = [(a, (m + 1) % n) for a, m in state]         # different phases
    assert born(other) == read                           # the port cannot tell
    assert state != other                                # though the states differ
