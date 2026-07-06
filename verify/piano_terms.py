"""piano_terms.py — SCHRODINGER'S PIANO (the thought experiment, pinned).

Three mechanical exhibits behind the paper:

(1) THE STRUCK TONE IS SHARP: a stiff string is a hardening oscillator
    (Duffing, beta > 0). Its sounded frequency EXCEEDS the rest pitch,
    rises with striking amplitude, and settles to the rest pitch only
    in the vanishing-amplitude limit — the rest tone is the limit of
    ever-gentler strikes, never a sounding. Integrated cold (RK4),
    period read off zero crossings.

(2) THE HARDER THE PROBE, THE LARGER THE READING: the measured running
    of the electromagnetic coupling, alpha^-1 = 137.036 at zero
    momentum down to ~128 at the Z pole — the field-theory instance
    of the sharp tone (float layer, memory-sourced, generous band).

(3) THE RADIUS THAT CANNOT BE READ: the proton charge radius is
    DEFINED at zero momentum transfer, the slope of the form factor
    at Q^2 = 0. Every finite-Q^2 reading of a dipole form factor
    UNDERSHOOTS the true slope and rises toward it monotonically as
    the probe softens: the rest value sits above every reading and
    is reached only by extrapolation — by calculation.
"""


def duffing_frequency(amplitude, beta=0.5, omega0=1.0, dt=1e-4):
    """Sounded frequency of x'' + omega0^2 x + beta x^3 = 0 released
    from rest at x = amplitude: read the full period off the zero
    crossings, integrated by RK4."""
    def acc(x):
        return -(omega0 ** 2) * x - beta * x ** 3

    x, v, t = amplitude, 0.0, 0.0
    crossings = []
    while len(crossings) < 3 and t < 1000.0:
        # RK4 step
        k1x, k1v = v, acc(x)
        k2x, k2v = v + 0.5 * dt * k1v, acc(x + 0.5 * dt * k1x)
        k3x, k3v = v + 0.5 * dt * k2v, acc(x + 0.5 * dt * k2x)
        k4x, k4v = v + dt * k3v, acc(x + dt * k3x)
        nx = x + dt * (k1x + 2 * k2x + 2 * k3x + k4x) / 6
        nv = v + dt * (k1v + 2 * k2v + 2 * k3v + k4v) / 6
        if x > 0 >= nx or x < 0 <= nx:
            # linear interpolation of the crossing time
            crossings.append(t + dt * x / (x - nx))
        x, v, t = nx, nv, t + dt
    period = 2 * (crossings[2] - crossings[0]) / 2  # two half-periods
    return 1.0 / period


def rest_pitch(omega0=1.0):
    """The silent frequency — the vanishing-amplitude limit."""
    import math
    return omega0 / (2 * math.pi)


# float layer: the coupling's measured running (memory-sourced)
ALPHA_INV_ZERO_Q = 137.036       # zero-momentum neighborhood
ALPHA_INV_AT_Z = 128.0           # ~127.9-129 depending on scheme; band in test


def dipole_radius_reading(q2_over_lambda2):
    """Finite-Q^2 secant reading of the dipole form factor's slope,
    in units where the true value (the Q^2 -> 0 limit) is 12:
    r2_eff = 6 (1 - G) / Q^2 with G = (1 + x)^-2."""
    x = q2_over_lambda2
    if x == 0:
        return 12.0
    g = (1 + x) ** -2
    return 6 * (1 - g) / x


TRUE_DIPOLE_SLOPE = 12.0
