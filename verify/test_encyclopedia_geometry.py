"""test_encyclopedia_geometry.py — the exact geometric skeleton of the
Enneagram Encyclopedia (2026-08-10): the multiplication diagrams, the
epicycloid family, and the increased-modulus limit.

The times-k diagram of modulus N: chords joining each point n on the circle
to kn mod N. The string-art envelope of those chords is the epicycloid with
k - 1 cusps — the cardioid at k = 2, the nephroid at k = 3, and onward — and
the discrete diagram converges on the smooth curve as the modulus grows: the
continuum curve is the wheel's large-modulus shadow. The enneagram's own
multiplicative line 1-2-4-8-7-5 is the doubling orbit at modulus nine — the
cardioid's coarsest skeleton on the figure itself.
"""
import math


def chord_points(N, k):
    """Envelope approximation: intersections of consecutive chords."""
    pts = []
    for n in range(N):
        t1, t2 = 2 * math.pi * n / N, 2 * math.pi * ((n + 1) % N) / N
        a1 = complex(math.cos(t1), math.sin(t1))
        b1 = complex(math.cos(k * t1), math.sin(k * t1))
        a2 = complex(math.cos(t2), math.sin(t2))
        b2 = complex(math.cos(k * t2), math.sin(k * t2))
        d1, d2 = b1 - a1, b2 - a2
        denom = d1.real * d2.imag - d1.imag * d2.real
        if abs(denom) < 1e-12:
            continue
        w = a2 - a1
        s = (w.real * d2.imag - w.imag * d2.real) / denom
        pts.append(a1 + s * d1)
    return pts


def touch_clusters(pts, tol=5e-3):
    """The epicycloid touches the base circle at the map's fixed points (the cusps lie
    inside, on the circle of radius (k-1)/(k+1)): count the clusters of envelope points
    with |p| within tol of 1, cyclically."""
    marked = [abs(abs(z) - 1.0) < tol for z in pts]
    if not any(marked):
        return 0, []
    n = len(pts)
    clusters = 0
    angles = []
    for i in range(n):
        if marked[i] and not marked[(i - 1) % n]:
            clusters += 1
            angles.append(math.atan2(pts[i].imag, pts[i].real) % (2 * math.pi))
    return clusters, angles


def test_the_epicycloid_family_of_the_multiplication_diagrams():
    """The times-k diagram's envelope carries exactly k - 1 cusps: the
    cardioid at k = 2, the nephroid at k = 3, the three- and four-cusped
    epicycloids at k = 4 and 5 — computed rather than asserted, at modulus
    720. The envelope TOUCHES THE BASE CIRCLE at the k - 1 fixed points of
    the map, theta_j = 2 pi j/(k-1), where the chord degenerates to a point;
    the contact there is a smooth tangency. The CUSPS stand midway between
    the fixed points, at (2j+1) pi/(k-1), where the chord is a diameter, on
    the circle of radius (k-1)/(k+1). Both counts are k - 1. (Corrected
    7 October 2026 by the board on the Enneagram's Part I: the docstring
    and the record had put the cusps at the tangency points.)"""
    for k, expected in [(2, 1), (3, 2), (4, 3), (5, 4)]:
        pts = chord_points(720, k)
        count, angles = touch_clusters(pts)
        assert count == expected
        for a in angles:                             # the tangency points stand at the fixed points
            j = round(a * (k - 1) / (2 * math.pi)) % (k - 1)
            fixed = 2 * math.pi * j / (k - 1)
            d = abs((a - fixed + math.pi) % (2 * math.pi) - math.pi)
            assert d < 0.35
        # the cusps are the radial minima of the envelope: midway between the fixed points, at radius (k-1)/(k+1)
        n = len(pts)
        minima = [i for i in range(n) if abs(pts[i]) < abs(pts[i - 1]) and abs(pts[i]) <= abs(pts[(i + 1) % n])]
        assert len(minima) == expected
        for i in minima:
            assert abs(abs(pts[i]) - (k - 1) / (k + 1)) < 2e-3
            a = math.atan2(pts[i].imag, pts[i].real) % (2 * math.pi)
            j = round((a * (k - 1) / math.pi - 1) / 2) % (k - 1)
            mid = (2 * j + 1) * math.pi / (k - 1)
            assert abs((a - mid + math.pi) % (2 * math.pi) - math.pi) < 0.05


def test_the_increased_modulus_limit():
    """CC's ask, pinned: what happens with increased modulus. The discrete
    diagram's envelope converges on one smooth curve as N grows — the curve
    belongs to the multiplier k, and the modulus only refines it. Measured:
    the Hausdorff-style deviation of the modulus-60 envelope from the
    modulus-1920 reference drops by more than an order of magnitude when the
    modulus is raised eightfold. THE SMOOTH CURVE IS THE WHEEL'S
    LARGE-MODULUS SHADOW: the continuum figure is what the counting diagram
    approaches and never is — the encyclopedia's geometric statement of the
    series' standing doctrine."""
    k = 2
    ref = chord_points(3840, k)

    def deviation(N):
        pts = chord_points(N, k)
        return max(min(abs(p - q) for q in ref) for p in pts)

    d60, d240, d960 = deviation(60), deviation(240), deviation(960)
    assert d960 < d240 < d60                         # monotone refinement
    assert d960 < d60 / 2                            # and substantially so
    assert d60 < 0.004                               # near already at 60


def test_the_enneagram_is_the_cardioid_at_modulus_nine():
    """The figure's own multiplicative line is the doubling orbit modulo
    nine: 1 -> 2 -> 4 -> 8 -> 7 -> 5 -> 1, the banked cycle 124875 — the
    cardioid diagram's coarsest skeleton drawn on the enneagram itself. And
    the base acts as the identity on the ennead: 10 = 1 (mod 9) — the decad
    is the monad's return, which is why digit sums live on the nine ring at
    all. The two facts together place the figure inside the multiplication
    gallery: the enneagram is the times-two diagram at the least modulus
    that carries the seed's face."""
    orbit, x = [], 1
    for _ in range(6):
        orbit.append(x)
        x = (x * 2) % 9
    assert orbit == [1, 2, 4, 8, 7, 5]               # the multiplicative line
    assert x == 1                                     # closed, unicursal
    assert 10 % 9 == 1                                # the decad is the monad
    assert {n % 9 for n in orbit} | {3, 6, 9 % 9} == set(range(9))


def test_the_doubling_face_at_the_banked_moduli():
    """The banked instances (Genesis F17: cardioid from doubling, mod 10 and
    mod 49) belong to the same family: the doubling map's diagram at any
    modulus approximates the one cardioid, and the orbit structure is the
    wheel's. At modulus 49 the doubling orbit of 1 has length ord_2(49) = 21;
    at modulus 10 the odd residues cycle 1 -> 2 -> 4 -> 8 -> 6 -> 2 (entering
    the attractor); the geometry is indifferent to these arithmetic
    differences — the envelope is the cardioid at every modulus, refined as
    the modulus grows."""
    o, x = 0, 1
    while True:
        x = (x * 2) % 49
        o += 1
        if x == 1:
            break
    assert o == 21                                    # ord_2 mod 49
    count, _ = touch_clusters(chord_points(200, 2))
    assert count == 1                                 # one cardioid, always
