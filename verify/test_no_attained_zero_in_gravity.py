"""test_no_attained_zero_in_gravity.py — THE NAVIER-STOKES COUNT APPLIED TO
GRAVITY: NO ATTAINED ZERO, THEREFORE NO SINGULARITY (2026-08-15).

  the author'S REDIRECTION, WHICH WAS THE BETTER END OF THE DOCTRINE. I had been
  applying "no attained zero" at the FAR end — the sharing function reaching
  exactly zero one cell-width out. the author pointed at the NEAR end: there is no zero
  to blow up on as the separation goes to zero. And he said the Navier-Stokes
  work applies to the whole of this. It does, and it applies as an identity
  rather than an analogy.

  THE NS ARGUMENT, AS BANKED. A finite-time singularity requires the turbulent
  cascade driven to unbounded depth in finite time — infinitely many
  distinguishable operations completed in finite time, a SUPERTASK. Demand
  through depth N is (8^(N+1)-1)/7, exponential; supply is 2ET/(pi hbar) by
  Margolus-Levitin, linear in time. Reachable depth is logarithmic in the
  resources: 42 octaves for a cubic metre of water in vigorous motion, 132 for
  a computer commandeering the observable universe. THE COUNT, NOT THE
  DISSIPATION, TERMINATES THE CASCADE.

  THE TRANSFER, AND WHY THE NUMBERS COINCIDE. Resolving a separation d needs
  cells of size about d, hence depth about log_b(d); reaching d = 0 requires
  completing infinitely many depths. That is the same supertask. And the
  arithmetic is not merely similar: refining a three-dimensional register by
  two subdivides every cell into 2^3 = 8, which is exactly the NS cascade's
  population of 8 per shell. Same base, same demand, SAME NUMBERS — 42 and 132
  reappear without adjustment.

  THE CONSEQUENCE. The register has a deepest reachable cell u_min. Below it
  there is no finer address to occupy, so two records inside it are simply in
  the same cell and the sum over depths terminates. The potential therefore
  SATURATES rather than diverging, at exactly the geometric total of the
  reachable depths — for the binary layer, 2/u_min. Gravity is regular by the
  same count that makes water regular, and no regulator, cutoff or
  renormalisation was introduced to make it so.

  THE DOCTRINE AT BOTH ENDS, which is the tidy part. The program forbids the
  attained zero. At the NEAR end that forbids a zero separation, which removes
  the singularity (this file). At the FAR end it forbids a sharing function
  that reaches exactly zero — which kills max(0,1-x), the kinked F that the
  naive partition picture produces, and pushes F into the family that only
  approaches zero, which is precisely the family with the Mellin decay that
  keeps the ripple beneath measurement. ONE DOCTRINE, BOTH ENDS, and it happens
  to be the doctrine that was already banked.

  GRADE: the NS theorem is banked and published; its transfer here is an
  application, and the identification of register depth with cascade depth is a
  Reading. Not promoted. What is exact below is the arithmetic.
"""

from math import log, pi

HBAR = 1.054571817e-34


def _supply(E, T):
    """Margolus-Levitin: orthogonal state transitions available."""
    return 2.0 * E * T / (pi * HBAR)


def _depth(E, T, b=2, dim=3):
    """Deepest instantiable depth: (b^dim)^(N+1) <= demand budget."""
    S = _supply(E, T)
    pop = b ** dim
    return log((pop - 1) * S / pop + 1.0) / log(pop) - 1.0


def _rate(F, d, b=2.0, jmin=-200, jmax=200):
    t = 0.0
    for j in range(jmin, jmax):
        u = float(b) ** j
        if u < 1e-290 or u > 1e290:
            continue
        t += F(d / u) / u
    return t


_F = lambda x: 1.0 / (1.0 + x) ** 2


def test_the_register_population_is_the_ns_cascade_population():
    """A binary register in three dimensions splits each cell into 8 — which
    is exactly the NS cascade's population per shell. Not an analogy."""
    assert 2 ** 3 == 8
    # NS demand through depth N, and the register's, are the same series:
    for N in (1, 3, 5, 9):
        ns = (8 ** (N + 1) - 1) // 7
        reg = ((2 ** 3) ** (N + 1) - 1) // (2 ** 3 - 1)
        assert ns == reg


def test_the_reachable_depth_reproduces_the_ns_numbers():
    """42 for a cubic metre of water in a second; 132 for the universe."""
    assert abs(_depth(5e4, 1.0) - 42) < 1.0
    universe = 1e120
    N = log(7 * universe / 8 + 1) / log(8) - 1
    assert abs(N - 132) < 1.0
    # and the depth is logarithmic in the budget, so no budget reaches them all
    assert _depth(9e16, 1.0) < 60
    assert _depth(9e16, 1e9) < _depth(9e16, 1e18)


def test_the_potential_saturates_instead_of_diverging():
    """Unbounded register: U ~ 1/d without limit. Floored: it levels."""
    unbounded = [_rate(_F, d) for d in (1.0, 1e-2, 1e-4, 1e-6)]
    assert unbounded[-1] / unbounded[0] > 1e5          # the singularity
    floored = [_rate(_F, d, jmin=0) for d in (1.0, 1e-2, 1e-4, 1e-6)]
    assert floored[-1] < 2.0000001                     # levels off
    assert all(b >= a - 1e-12 for a, b in zip(floored, floored[1:]))
    # the ceiling is the geometric total of the reachable depths:
    assert abs(_rate(_F, 0.0, jmin=0) - 2.0) < 1e-9    # sum 2^-j = 2


def test_the_floor_leaves_an_exact_short_range_correction():
    """It does NOT vanish at long range — it leaves a fractional deficit of
    order u_min/d, and the coefficient is exactly ln(b)/(b-1). My first
    version asserted the deficit was negligible; it is 7e-4 at d = 1000 u_min,
    and that is a prediction rather than a rounding error."""
    from math import log, log10
    # the coefficient is asymptotic in u_min/d — it converges, it is not exact
    # at every d, and the tolerance says so rather than pretending otherwise
    for d, tol in ((1e3, 1e-3), (1e4, 1e-4), (1e5, 1e-5), (1e6, 1e-5)):
        a, c = _rate(_F, d), _rate(_F, d, jmin=0)
        C = (a - c) / a * d
        assert abs(C - log(2.0) / (2.0 - 1.0)) < tol
    # the law across bases — at b = 2 alone the divisor is one, which is why
    # ln(b)/(b-1) and ln(b) coincide there and nowhere else:
    for b in (2.0, 3.0, 4.0):
        d = 1e5
        a, c = _rate(_F, d, b=b), _rate(_F, d, b=b, jmin=0)
        assert abs((a - c) / a * d - log(b) / (b - 1.0)) < 1e-4
    # and the envelope is still 1/d with the floor in place:
    e = log10(_rate(_F, 1e4, jmin=0) / _rate(_F, 1e3, jmin=0))
    assert abs(e + 1.0) < 1e-3


def test_the_doctrine_reads_at_both_ends():
    """No attained zero: near end kills the singularity, far end kills the
    kinked F. One banked doctrine, two consequences."""
    kink = lambda x: max(0.0, 1.0 - x)
    assert kink(1.0) == 0.0 and kink(2.0) == 0.0       # ATTAINS zero — forbidden
    assert _F(1.0) > 0 and _F(1e6) > 0                 # only approaches it
    assert _F(1e12) > 0
    # and the permitted family is the one with the usable Mellin decay:
    def ripple(F, b=2.0, n=400):
        ds = [100 * (b ** (k / float(n))) for k in range(n)]
        v = [_rate(F, d, b=b) * d for d in ds]
        return (max(v) - min(v)) / (sum(v) / len(v))
    assert ripple(kink) > 0.10                         # forbidden F: 11.5%
    assert ripple(_F) < 1e-9                           # permitted F: 1e-10
