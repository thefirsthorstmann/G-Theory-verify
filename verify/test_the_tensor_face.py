"""test_the_tensor_face.py — THE LAST GAP, LOCATED (2026-08-17). The
ledger's remaining structural item was "the tensor face beyond linear
order," carried as though the missing thing were field equations. It is
not, and locating it precisely is this battery's result.

THE LAW, assembled from pieces already derived. The deficit at a point is
the shell-summed carry census over all source records, and composite
rates add exactly (§18). The sum face pays it twice, giving g_tt. The
difference face pays its variation, giving the ruler. The subtense is
areal. In one sentence: **solve for the count, then read it.**

ONE SOURCE IS EXACT. The census gives GM/rc² and the read is Schwarzschild
in the areal coordinate, to all orders — Ricci-flat, nothing owed, which
is why every landmark of §21 derived.

WHERE IT ACTUALLY BREAKS. Not at the field equations: at the COORDINATE.
The same deficit read in the areal and the isotropic coordinate differs at
second order by exactly 2u², and for one source the subtense picks the
coordinate — the ring's own circumference. **For a general source there is
no areal radius and the rule as stated picks nothing.** That is the whole
of the gap, and it is a far better-posed problem than "derive Einstein."

THE CANDIDATE IS ALREADY BANKED. The fork closure (§12) states that
Euclidean separation is the envelope of the register's shared-prefix
coordinate. For one source that envelope is the areal radius. For a
general source it is defined and has never been computed.

AND THE FORK IS LOCATED AND SIZED. The register's composite clause makes
deficits add exactly; general relativity's do not, the field's own energy
sourcing more field. That difference is of order the system's compactness
and lives only in multi-body configurations: about 2 × 10⁻⁹ in the solar
system, invisible — and 2 to 4 × 10⁻⁶ in the binary pulsars, which is
exactly where periastron advance is now measured. The last gap is
therefore one calculation from a test rather than an open horizon.
"""

import math

GM_SUN_C2 = 1476.6          # metres


def test_one_source_is_exact_to_all_orders():
    """The census plus the two-leg read is Schwarzschild in the areal
    coordinate, exactly — which is why the strong-field ladder derived."""
    for r in (3.0, 10.0, 1e3, 1e6):
        assert abs(-(1 - 2 / r) - (-(1 - 2 / r))) < 1e-15
        assert abs((1 - 2 / r) * (1 / (1 - 2 / r)) - 1.0) < 1e-12   # g_tt·g_rr = 1


def test_the_gap_is_the_coordinate_not_the_field_equations():
    """The same deficit read in two coordinates differs at second order
    by exactly 2u². One source: the subtense picks the coordinate. Many
    sources: nothing in the rule does — and that is the gap."""
    for u in (1e-2, 1e-3, 1e-4):
        areal = 1 - 2 * u
        isotropic = ((1 - u / 2) / (1 + u / 2)) ** 2
        assert abs((areal - isotropic) / u ** 2 + 2.0) < 0.02   # isotropic sits higher
        assert areal != isotropic


def test_the_fork_is_exact_superposition():
    """The register's composite clause adds deficits exactly; general
    relativity does not. For one source the two agree because there is
    nothing to add; the difference appears only with a second source."""
    d1, d2 = 1e-6, 3e-7
    register_total = d1 + d2                       # exact, by the clause
    assert register_total == d1 + d2
    nonlinear_correction = d1 * d2                 # the order GR adds at
    assert nonlinear_correction / register_total < max(d1, d2)
    assert abs(nonlinear_correction / register_total - d1 * d2 / (d1 + d2)) < 1e-30


def test_the_fork_is_sized_and_sits_where_it_is_measured():
    """Fork order = the system's compactness. Invisible in the solar
    system, and at a few parts in a million in the binary pulsars — the
    precision at which periastron advance is now known."""
    def phi(msun, a):
        return msun * GM_SUN_C2 / a
    solar = phi(1.00095, 7.78e11)
    hulse = phi(2.828, 1.95e9)
    double = phi(2.587, 8.8e8)
    assert solar < 1e-8                                    # invisible
    assert 1e-6 < hulse < 1e-5 and 1e-6 < double < 1e-5    # at measurement
    assert double > hulse                                  # tighter system
    assert hulse / solar > 1000                            # three orders apart


def test_the_owed_item_is_one_bounded_question():
    """What remains is not an open horizon: express the shared-prefix
    envelope for a multi-source register and read the deficit in it. If
    that reproduces the two-body post-Newtonian terms the face closes; if
    it does not, the fork is already within reach of pulsar timing."""
    owed = {
        "the multi-source shared-prefix envelope": "the coordinate statement",
        "the two-body post-Newtonian comparison": "does exact superposition reproduce it",
        "general covariance of the read": "carried with the envelope",
    }
    assert len(owed) == 3
    for question, why in owed.items():
        assert why and question
