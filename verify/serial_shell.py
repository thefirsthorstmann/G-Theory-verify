"""serial_shell.py — THE SERIAL SHELL MODEL: the depletion theorem.

THE MODEL. Shells n = 0, 1, 2, ... (octaves; the banked cascade). The
cascade at shell n comprises 8^n cells (2^3 children per rung in 3D;
DOF consistent with the banked Re^(9/4) = (Re^(3/4))^3). THE METER
(the one rule, CC): the substrate performs at most P operations per
tick of duration delta — supply is LINEAR in elapsed time. Creating a
phase-bearing cell is an operation (a fortiori, ALIGNING one is).

THE SCHEDULE. K41 turnovers shrink geometrically: tau_n = tau_0 *
2^(-2n/3) (from the banked octave cascade v_n ~ l_n^(1/3)). The total
Sum tau_n < 3 tau_0 — PROVED RATIONALLY: 2^2 = 32/8 > 27/8 = (3/2)^3,
so 2^(2/3) > 3/2, so the ratio r = 2^(-2/3) < 2/3, so the geometric
sum < 1/(1 - 2/3) = 3. Infinitely many turnovers FIT in finite time:
the continuum leaves finite-time blow-up kinematically open. THE
BLOW-UP IS A SUPERTASK.

THE DEMAND. Cells through depth N: D(N) = sum 8^n = (8^(N+1) - 1)/7
— exact, EXPONENTIAL (and counted in sevenths: the ring-sum is a
seventh). Tao's blow-up choreography requires the cascade executed
coherently at EVERY depth within the converging schedule.

THE THEOREM. Supply P*T/delta is linear in T; demand D(N) is
exponential in N; so the reachable depth in elapsed time T is
N*(T) <= log_8(7 P T / delta + 1) - 1 — LOGARITHMIC. Unbounded depth
in finite time requires infinitely many operations from a finite-rate
meter: impossible. No finite-time singularity on the substrate —
viscous or INVISCID — for any fixed degree of parallelism P. The
statistical cascade in unbounded time is untouched (real flows run
~10-20 octaves, comfortably inside any physical budget).

THE DIAGNOSIS. The continuum formulation grants unboundedly many
simultaneous updates axiomatically — it has no meter — so the bound
cannot even be STATED there. The singularity is not a physical
possibility but a supertask permitted by a language with the meter
erased.
"""

from fractions import Fraction as F


def demand(n_max: int) -> int:
    """Cells through depth N: sum of 8^n = (8^(N+1) - 1)/7, exact."""
    total = sum(8 ** n for n in range(n_max + 1))
    assert 7 * total == 8 ** (n_max + 1) - 1      # the sevenths identity
    return total


def supply(ticks: int, p: int = 1) -> int:
    """The meter: at most P operations per tick — linear."""
    return p * ticks


def supertask_ratio_bound() -> tuple:
    """The rational chain proving Sum tau_n < 3 tau_0:
    2^2 > (3/2)^3  =>  2^(2/3) > 3/2  =>  r < 2/3  =>  sum < 3."""
    lhs, rhs = F(2) ** 2, F(3, 2) ** 3            # 4 > 27/8
    bound = 1 / (1 - F(2, 3))                     # = 3
    return lhs, rhs, bound


def coherence_depth(ticks: int, p: int = 1) -> int:
    """Max depth N with D(N) <= supply: the LOGARITHMIC reach."""
    n = 0
    while demand(n + 1) <= supply(ticks, p):
        n += 1
    return n


def exponential_beats_linear(a: int, n_from: int, n_to: int) -> bool:
    """8^n > a*n for all n in range (with ratio strictly worsening)."""
    return all(8 ** n > a * n for n in range(n_from, n_to + 1))


def bkm_shell_terms(n_max: int, r=F(1, 2)) -> list:
    """THE BKM INTEGRAL COUNTS SHELLS. With omega_n = v_n/l_n and
    tau_n = l_n/v_n, the contribution of shell n to the Beale-Kato-
    Majda integral is tau_n * omega_n = 1 IDENTICALLY — each completed
    shell contributes exactly one unit. Divergence of the integral
    (the accepted blow-up criterion) <=> unboundedly many shells
    completed <=> the supertask. Exact for any scaling ratio r."""
    taus = [r ** n for n in range(n_max + 1)]
    omegas = [1 / t for t in taus]
    return [t * w for t, w in zip(taus, omegas)]


# Physical constants for the Margolus-Levitin instantiation (SI, CODATA)
HBAR = 1.054571817e-34          # J s
PI = 3.14159265358979


def ml_ops(energy_j: float, time_s: float) -> float:
    """Margolus-Levitin: max orthogonal state transitions in time T for
    average energy E is 2 E T / (pi hbar). The meter as a THEOREM of
    quantum mechanics — finite energy => finite operation rate."""
    return 2 * energy_j * time_s / (PI * HBAR)


def kolmogorov_depth(reynolds: float) -> int:
    """The physical cascade's own depth: (3/4) log2(Re) octaves
    (from l_0/eta = Re^(3/4)) — what nature actually runs."""
    import math
    return int(0.75 * math.log2(reynolds))


def universal_stage_cap(schedule, t_min: float, n_max: int = 10 ** 6) -> int:
    """THE UNIVERSAL FORM (referee pass, 2026-07-03). Any finite-time
    completion of infinitely many SEQUENTIAL stages is impossible
    under a minimum stage-time t_min, for ANY schedule whatsoever:
    sum(tau_n) < infinity with infinitely many stages forces
    tau_n -> 0, so eventually tau_n < t_min and the schedule is
    unexecutable. No geometry, no scaling exponent, no cascade
    structure assumed. Returns the first unexecutable stage."""
    for n in range(n_max):
        if schedule(n) < t_min:
            return n
    return n_max


def rate_depth_cap(energy_j: float, tau0_s: float) -> int:
    """THE RATE LEG (closes the concentrated-collapse loophole).
    A self-similar single-filament collapse activates only O(1) cells
    per shell — linear demand, evading the census count. But
    Margolus-Levitin also floors the TIME PER TRANSITION at
    pi hbar / 2E, while the schedule demands shell n complete within
    tau_n = tau_0 2^(-2n/3). Unexecutable beyond
        n = (3/2) log2(2 E tau_0 / pi hbar),
    so even the maximally concentrated collapse caps at finite depth
    while the BKM census requires infinite depth. No blow-up."""
    import math
    t_min = PI * HBAR / (2 * energy_j)
    return int(1.5 * math.log2(tau0_s / t_min))
