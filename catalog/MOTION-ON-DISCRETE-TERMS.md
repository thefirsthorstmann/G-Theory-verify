%%TITLE: Motion on Discrete Terms
%%SUBTITLE: Deriving inertia, the speed limit, the quadratic form of kinetic energy, and the conservation of angular momentum from a discrete arithmetic
%%META: Christian Horstmann · thefirsthorstmann@gmail.com · August 25th, 2026 · manuscript for the public record
%%ABSTRACT: Classical mechanics assumes its kinematics rather than deriving it: inertia is posited as a law, the quadratic dependence of kinetic energy on velocity is taken from experiment, angular momentum is conserved by appeal to a symmetry, and orbital motion is fixed by a variational principle adopted from outside. This paper derives four of these from a single discrete structure and states the conditions under which each derivation fails. Inertia is obtained as a theorem of parity: the two generators of the structure admit no common closure, so the substrate has no fixed point and no rest state for a body to occupy. The speed limit is obtained as a counting bound of one place per tick, with admissible velocities forming a bounded ladder of rationals. The quadratic form of kinetic energy is obtained from the register's energy form applied to per-tick increments, uniform advance costing nothing. Conservation of angular momentum is obtained from the append-only property of the winding counter, integer values making quantization automatic. The orbit equation follows from these four together with a stationarity principle, which is named where it is used and is not derived; results depending on it are marked as such. Every arithmetic statement is verified in a public suite, and the measurements that would refute each result separately are given. Every exact claim re-derives in a public suite at github.com/thefirsthorstmann/g-theory-verify.
%%

## 1 · Introduction

Classical mechanics takes its kinematics as given. This section states five
propositions about motion, four of them derived below from a single discrete
structure and the fifth conditional on a stated principle. Each is labelled
by its type at the point it is made.

**Proposition 1 (inertia).** A body persists in uniform motion because the
substrate admits no rest state. This is a theorem of parity, not a law of
nature adopted from observation.

**Proposition 2 (the speed limit).** A maximum signal rate exists and equals
one place per tick. It is a counting bound: the count cannot outrun the
count.

**Proposition 3 (kinetic energy).** Energy is quadratic in rate because the
register's energy form is a sum of squared increments. Uniform advance costs
nothing, which is the invariance of the laws under a change of frame.

**Proposition 4 (angular momentum).** The conserved quantity is the winding
counter, which is append-only. Its values are integers, so quantization is
automatic rather than imposed.

**Proposition 5 (orbits), conditional.** Given Propositions 1 to 4 and a stationarity principle, stated in §7 and not
derived here, the orbit relation follows. Its observable consequences follow
with it: the climb of the orbital exponent, the exact period deviation, and
the apsidal ladder.

Every arithmetic statement below is machine-checked. Where a result depends
on the stationarity principle rather than on arithmetic alone, that
dependence is marked at the point of use, and §9 gives the measurement that
would refute each proposition separately.

## 2 · The substrate

The construction rests on the following objects, established in the companion
volumes and used here without re-derivation. A wheel is the orbit of a base's
powers among the residues, together with its digit realization. One place is
one rotation is one tick. The master wheel has period six. Extension stands at
rungs d = 10ⁿ − 1; one tick multiplies the rung count by ten and divides the
deficit by one hundred. A rider carries an integer k, and its shortfall is
exactly k parts. The two generators can never close on each other, and their
mutual rotation reads alternatingly, back and forth, by the convergent theorem
— the endless pulse the update-rule campaign pinned. Nothing below is new
substrate; the paper is the recomposition.

## 3 · Time, and the absence of rest

**Theorem 1. The substrate has no rest state.** A common closure of the two
generators would require 2^p = 3^q with p, q positive: an even number equal to
an odd one. There is none. The mutual rotation of two and three is therefore
perpetual — the fractional parts of q·log₂3 are never zero, and their record
minima fall exactly at the convergent denominators 1, 2, 5, 12, 41, 53, 306.

**Inertia is the corollary.** A body persists in its state of motion because
stopping is not among the states of the system. Where classical mechanics
postulates persistence, the discrete account has nothing for a body to stop
into: rest would be a settled ratio of the generators, and parity forbids the
settlement. Newton's first law, on these terms, follows from the parity of
integers.

## 4 · The speed limit is the tick

**Theorem 2. No rate exceeds one rung per tick.** An address advances at most one place per tick. This follows from the wheel
definition, since one place is one rotation is one tick. The elementary step
is a single place, and a step of two places in one tick would be two rotations
within one rotation. Composite steps are sequences of elementary ones — the ledger records no other kind. In q ticks a rider
therefore advances at most q rungs, and velocities are the ladder of fractions
p/q with p ≤ q: rational rates bounded by the null rate one, at which advance
and count coincide.

The bound is not dynamical but combinatorial: the count cannot outrun the
count. The limiting rate is the rate of the clock itself. The gravity volume's
special-relativity identification, the octave as a dilation on a null axis, names the
same limit from the other side: the null axis is where one rung per tick is
exact. The ladder of admissible rates is the ladder of fractions, and
ten rungs in ten ticks is one rung in one tick: rates are ratios, carrying no
scale, exactly as the dimensional boundary requires.

## 5 · The energy of motion

**Theorem 3. Kinetic energy is the established form applied to rates.** The gravity
volume fixed the figure's deformation energy as the Dirichlet form: the sum of
squared gap deviations, exact and not an approximation. Apply the same form to
the per-tick increments of a moving configuration — the one identification
this section makes, stated as such. Two results follow at once,
both exact. Uniform advance — every seat stepping together — costs nothing:
the zero mode, which is the freedom of boosts; motion as such carries no charge, and only relative rate is registered. A rate gradient registers as the square of the rate: scaling the increments by k scales the form by k², so doubling a rate quadruples the quantity and tripling it multiplies it ninefold.

The generators' rates therefore cost as their squared intervals. The motor's
rate against the octave's costs nine against four — the fifth squared — and
the ladder of energy ratios is the ladder of interval squares. The square is
the point. The same composition law turns amplitude into observable in the Born rule,
turns a gauge object into gravity in the double copy, and here turns velocity
into energy. One square serves three offices, and in every office the squared
object is the one measurement reads.

## 6 · Conservation is the append-only ledger

**Theorem 4. The winding count is conserved and quantized.** After m ticks the pair of coarse windings and phase, m div 6 and m mod 6,
recovers m exactly, for every m. The counter is therefore append-only: nothing is lost and nothing is created twice. Within a cycle no rotation state repeats
until the sixth closes. The no-reseat rule that selected the coupling's period in the gravity volume states that a closure does not produce again what its ancestors produced. Read
in time rather than in depth, that discipline is conservation: a completed
winding is a completed count, and the ledger admits no free operations. Angular momentum,
as winding rate, is conserved by counting, and its quantization is automatic
because windings are integers. Where the standard account derives conservation
from symmetry, the discrete account derives it from bookkeeping — the theorem
of the count is that the books balance.

## 7 · The orbit equation

One principle now enters, and it is named as the principle it is: **the
stationarity rule**. Among the admissible states at fixed winding, the state
realized is the one that makes the energy stationary. This is a principle of
least action. It does in this framework the work that Newton's second law does
in his, and it is the only principle the paper assumes rather than derives.

Compose the postulates. Quadratic energy in the rate, the conserved winding L, and
the derived potential give the radial energy E(r) = L²/2r² − K/(r+λ₁), and
stationarity in r gives

```
      L²  =  K r³ / (r + λ₁)²        ⟺        v²  =  K r / (r + λ₁)²
```

This is the relation that classical kinematics supplies as a postulate. Here it
is derived, and the results standing on it follow from §§3–6 without further
assumption:

- **the orbital exponent climbs the seats** — one half at contact, one at the
  first rung, three halves in the far field, so Kepler's third law is the
  reversal pair of three halves and two thirds;
- **the exact deviation** T/T_Kepler = 1 + λ₁/r at every radius — the period
  fork against the exponential correction, four orders apart at ten rungs;
- **the apsidal ladder** π/√3 to π/√2 to π, closure exact only in the far
  limit, the far precession retrograde and power-law small.

## 8 · The three laws, located

**The first law is derived.** Persistence is the absence of rest, by Theorem 1.

**The second law's shape is derived, and its coefficient is established.** A
quadratic energy makes momentum linear in rate, so force — the energy
gradient — changes momentum in proportion to the change of rate. The coefficient is the rider count. The sourcing congruence k·142857·7 = k·10⁶
− k makes the absolute shortfall proportional to k and the relative shortfall
independent of it. Force is therefore proportional to source and response
independent of the rider, from one congruence, as the gravity volume
established.

**The third law is derived.** In the two-rider rule each rider is accelerated by the sum of the other
counts, weighted by the extension law, with its own count absent. The force
rider j exerts on rider i is the count product k_i k_j in one direction. The
force i exerts on j is the same product in the other. Action and reaction are one multiplication read twice, and the multiplication
commutes. Momentum conservation follows tick by tick, exactly. The merger of co-
addressed riders is forced rather than chosen, because an address on the wheel
holds a total and not a list. The merger's energy cost is one-signed, and
equals the reduced-count relative term exactly. The total binding of any assembly is path independent — a state function, verified in exact
arithmetic. The rule inherits the conditionality of §7's postulates and nothing further.
Its filters are machine checked in `verify/test_two_riders.py`: exact
reduction to the one-dimensional count-force dynamics, the equivalence
principle as an identity, and the far-field orbit with the total count as
source.

## 9 · What the continuum deletes

A trajectory is the quotient of a counted path. The tangent vector is the limit that forgets how many ticks were used and in what order; the smooth
velocity is the trail with its ledger erased. The mechanics recovered in this
paper retains its full ledger: every rate a fraction, every energy
a square of counted increments, every conserved quantity a balanced book.
The continuum approximation is exact in the far field for the same reason it
is exact for the metric: the steps average. It fails within the first rungs,
where the count is coarse and the ledger is the physics.

## 10 · The correspondence: the tick rate as tempo

This section states the musical correspondence; nothing below depends on it.

Melody moves at notes per beat. However fast the passage, there is a tempo,
and the fastest playable music is one note per beat of the smallest pulse —
you cannot play between the clicks of the metronome's finest subdivision. That
is Theorem 2, and every musician's hands already know it: the speed limit is
the tick.

And the piece cannot stop. Not will not — cannot, and the reason has to be
stated with the right operation, because the obvious version of it is false.
Two voices *counting* in twos and threes land together every six beats;
there is no mystery in duple against triple, and a reader who checks that
sentence finds it false before the second bar. The incommensurability is
multiplicative, not additive. The voices that never meet are the ones that
**double** and **triple**: 2ᵃ never equals 3ᵇ above one, by unique
factorisation, and that is the whole of it. Stack fifths against octaves and
the same fact surfaces audibly — twelve fifths overshoot seven octaves by
the Pythagorean comma and the circle never closes, however long you go
round. Every apparent cadence is provisional; the counterpoint is perpetual
by arithmetic. What physics calls inertia, the player knows as the canon
that has no final bar. The universe coasts for the same reason the spiral of
fifths never becomes a circle: there is no place where both ladders meet.

## 11 · What would refute this

1. **Rest.** A common value 2^p = 3^q with positive exponents refutes
   Theorem 1 and restores a rest state. The parity of integers forbids it.
2. **The limit.** A rider advancing more than one rung in one tick refutes
   Theorem 2; the wheel definition makes the advance and the tick one event.
3. **The square.** A configuration whose motion cost, on the established form, scales other than
   quadratically — a rate doubled costing other than fourfold on the
   Dirichlet form — refutes Theorem 3 in a line of arithmetic.
4. **The ledger.** A tick count m not recovered from windings and phase, or a
   wheel state repeating before the sixth rotation, refutes Theorem 4.
5. **The orbit.** If stationarity of E(r) = L²/2r² − K/(r+λ₁) fails to give
   v² = Kr/(r+λ₁)², the recomposition fails; the algebra is four lines and
   machine checked.
6. **The named principle.** The stationarity rule is the paper's one
   principle. A realized configuration that is not stationary at fixed
   winding — in any system this series treats — refutes the postulate itself,
   and with it §7.

## 12 · Relation to the standard account

Galileo's inertia and the relativity of uniform motion appear here as the
zero mode: uniform advance costs nothing, so no experiment inside the
configuration detects it. Newton's laws are located in §8 — one derived, one
derived in shape with an established coefficient, one a labeled candidate. Lagrange
and Hamilton's stationarity is the one principle this paper takes, named as
the projection grammar's rule rather than derived; the series holds it where
the classical tradition holds it, at the foundation. Noether's account derives conservation from symmetry. The discrete account
derives it from counting, by way of the append-only ledger. Noether's theorem
requires a continuous symmetry group; the ledger requires only integers, which
is why quantization arrives with conservation rather than after it. Bertrand's theorem makes the closed orbit exceptional among force laws. It
appears here as the far-field limit of the apsidal ladder. Exact closure is
the idealization, and the near field opens the ellipse the way the companion
volumes' commas open every cycle. The special-relativistic speed limit is
recovered as a counting bound, agreeing with the octave-boost identification of the
gravity volume: the limit is not a property of light but of counting, and
light is the thing that saturates it.

## 13 · Verification

Every arithmetic statement in this paper is a re-runnable test:
`verify/test_motion.py` carries six pins:

- the absence of rest, with the convergent record
- the speed limit and the rational ladder
- the quadratic scaling and the zero mode of the established form
- the append-only winding count and the no-repeat cycle
- the orbit equation with its downstream results
- the arithmetic of the three laws

The two-rider rule of §8 is pinned separately in `verify/test_two_riders.py`,
with six further tests:

- the one-dimensional anchor
- the product third law, with exact momentum conservation
- the equivalence identity
- the forced merger and its one-signed cost
- the path independence of the binding ledger
- the far-field orbit

Both sit within the program's full suite, which passes. The stationarity
rule is the paper's single named principle; nothing else is assumed.

## References

1. Galilei, G. (1638). *Discorsi e dimostrazioni matematiche intorno a due
   nuove scienze.* Leiden.
2. Newton, I. (1687). *Philosophiæ Naturalis Principia Mathematica.* London.
3. Lagrange, J. L. (1788). *Méchanique analitique.* Paris.
4. Hamilton, W. R. (1834). On a general method in dynamics.
   *Phil. Trans. R. Soc.* 124, 247–308.
5. Bertrand, J. (1873). Théorème relatif au mouvement d'un point attiré vers
   un centre fixe. *C. R. Acad. Sci. Paris* 77, 849–853.
6. Mach, E. (1883). *Die Mechanik in ihrer Entwickelung.* Leipzig.
7. Einstein, A. (1905). Zur Elektrodynamik bewegter Körper.
   *Ann. Phys.* 17, 891–921.
8. Noether, E. (1918). Invariante Variationsprobleme.
   *Nachr. Ges. Wiss. Göttingen*, 235–257.

---

*Companions: Gravity on Discrete Terms (the form, the coupling, and the
kinematics of §16; doi.org/10.5281/zenodo.22087600) · Units on Discrete
Terms (the dimensional boundary; posted with this revision) · The Origin
on Discrete Terms (the figure; doi.org/10.5281/zenodo.21432752) ·
Schrödinger's Piano (the thought experiment;
doi.org/10.5281/zenodo.21270357).*

<div class="copyright" style="margin-top:80pt">Copyright<br>Christian Horstmann · August 25th, 2026<br>thefirsthorstmann@gmail.com<br>All rights reserved</div>

## Addendum: the eccentric orbit family and the orbital instrument

The eccentric family is closed at first order for every eccentricity. The
softened potential's orbit family is the precessing conic, with an apsidal
drift of −2πλ/p per orbit. Here p is the semi-latus rectum a(1 − e²), the
circular result's radius replaced by the conic's own — verified by direct integration and pinned in
verify/test_the_orbital_account.py. The same battery opens the orbital instrument. A log-periodic force residual
of amplitude A precesses a near-circular orbit by (2π²A/ln 2)·sin(2π log₂ r +
φ) per orbit. Planetary ephemerides therefore test the companion note's fixed-
period template at four parts in ten trillion, nine orders beyond laboratory sensitivity.
