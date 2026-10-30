%%TITLE: Motion on Discrete Terms
%%SUBTITLE: Deriving inertia, the speed limit, the quadratic form of kinetic energy, and the conservation of angular momentum from a discrete arithmetic
%%META: Christian Horstmann · thefirsthorstmann@gmail.com · August 25th, 2026 · version 2, October 2026 · manuscript for the public record
%%ABSTRACT: Classical mechanics assumes its kinematics rather than deriving it: inertia is posited as a law, the quadratic dependence of kinetic energy on velocity is taken from experiment, angular momentum is conserved by appeal to a symmetry, and orbital motion is fixed by a variational principle adopted from outside. This paper derives four of these from a single discrete structure and states the conditions under which each derivation fails. Inertia is obtained as a theorem of parity: the two generators of the structure admit no common closure, so the substrate has no fixed point and no rest state for a body to occupy. The speed limit is obtained as a counting bound of one place per tick, with admissible velocities forming a bounded ladder of rationals. The quadratic form of kinetic energy is obtained from the structure's energy form applied to per-tick increments, uniform advance carrying no energy. Conservation of angular momentum is obtained from the append-only property of the winding counter, integer values making quantization automatic. The orbit equation follows from these four together with one assumed principle of stationarity, named where it is used; results depending on it are marked as such. Every arithmetic statement is verified in a public suite at github.com/thefirsthorstmann/g-theory-verify, and the measurements that would refute each result separately are given.
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

**Proposition 3 (kinetic energy).** Energy is quadratic in rate because
the structure's energy form is a sum of squared increments. Uniform
advance carries no energy, which is the invariance of the laws under a
change of frame.

**Proposition 4 (angular momentum).** The conserved quantity is the winding
counter, which is append-only. Its values are integers, so quantization is
automatic rather than imposed.

**Proposition 5 (orbits), conditional.** Given Propositions 1 to 4 and a
stationarity principle, assumed and stated in §7, the orbit relation
follows. Its observable consequences follow with it: the climb of the
orbital exponent, the exact period deviation, and the apsidal ladder.

Every arithmetic statement below is machine-checked. Where a result
depends on the stationarity principle rather than on arithmetic alone,
that dependence is marked at the point of use, and §11 gives the
measurement that would refute each proposition separately.

## 2 · The substrate

The construction rests on the following objects, established in the
companion records and used here without re-derivation. A cycle is the
orbit of a base's powers among the residues, together with its digit
realization. One place is one rotation is one tick. The reptend cycle of
one seventh has period six. Extension stands at rungs d = 10ⁿ − 1; one
tick multiplies the rung count by ten and divides the deficit by one
hundred. A rider carries an integer k, and its shortfall is exactly k
parts. The two generators can never close on each other, and their
mutual rotation reads alternately back and forth, because the
convergents of log₂3 fall alternately above and below it. Nothing below
is new substrate; the paper is the recomposition.

## 3 · Time, and the absence of rest

**Theorem 1. The substrate has no rest state.** A common closure of the
two generators would require 2^p = 3^q with p, q positive: an even
number equal to an odd one. There is none. The mutual rotation of two
and three is therefore perpetual — the distance of q·log₂3 from the
nearest integer is never zero, and its record minima fall exactly at the
convergent denominators 1, 2, 5, 12, 41, 53, 306.†

<div class="vnote">† Version 1 gave these minima to the fractional
parts, whose record minima begin 1, 2, 7, 12, 53. The battery computes
the distance.</div>

**Inertia is the corollary.** A body persists in its state of motion because
stopping is not among the states of the system. Where classical mechanics
postulates persistence, the discrete account has nothing for a body to stop
into: rest would be a settled ratio of the generators, and parity forbids the
settlement. Newton's first law, on these terms, follows from the parity of
integers.

## 4 · The speed limit is the tick

**Theorem 2. No rate exceeds one rung per tick.** An address advances at
most one place per tick. This follows from the definition of the cycle,
since one place is one rotation is one tick. The elementary step is a
single place, and a step of two places in one tick would be two
rotations within one rotation. Composite steps are sequences of
elementary ones — the count records no other kind. In q ticks a rider
therefore advances at most q rungs, and velocities are the ladder of
fractions p/q with p ≤ q: rational rates bounded by the null rate one,
at which advance and count coincide.

The bound is not dynamical but combinatorial: the count cannot outrun
the count. The limiting rate is the rate of the clock itself. The
gravity record's special-relativity identification, the octave as a
dilation on a null axis, names the same limit from the other side: the
null axis is where one rung per tick is exact. The ladder of admissible
rates is the ladder of fractions, and ten rungs in ten ticks is one rung
in one tick: rates are ratios, carrying no scale, exactly as the
dimensional boundary requires.

## 5 · The energy of motion

**Theorem 3. Kinetic energy is the established form applied to rates.**
The gravity record fixed the figure's deformation energy as the
Dirichlet form: the sum of squared gap deviations, exact and not an
approximation. Apply the same form to the per-tick increments of a
moving configuration — the one identification this section makes, stated
as such. Two results follow at once, both exact. Uniform advance, every
position stepping together, carries no energy: it is the zero mode,
which is the freedom of boosts, and only relative rate is registered. A
rate gradient registers as the square of the rate: scaling the
increments by k scales the form by k², so doubling a rate quadruples the
quantity and tripling it multiplies it ninefold.

The energies of the generators' rates therefore stand as their squared
intervals. The motor's rate against the octave's carries nine against
four, the fifth squared, and the ladder of energy ratios is the ladder
of interval squares. The same composition law turns amplitude into
observable in Born's rule, turns a gauge object into gravity in the
double copy of Bern, Carrasco and Johansson, and here turns velocity
into energy. In each of the three the squared object is the one that
measurement reads.

## 6 · Conservation is the append-only count

**Theorem 4. The winding count is conserved and quantized.** After m
ticks the pair of coarse windings and phase, m div 6 and m mod 6,
recovers m exactly, for every m. The counter is therefore append-only:
nothing is lost and nothing is created twice. Within a cycle no rotation
state repeats until the sixth closes. In the gravity record the
coupling's period is selected by the rule that a closure's novel content
is the factor no ancestor depth produces. Read in time rather than in
depth, that rule is conservation: a completed winding is a completed
count, and the count admits no free operations. Angular momentum, as
winding rate, is conserved by counting, and its quantization is
automatic because windings are integers. Where the standard account
derives conservation from symmetry, the discrete account derives it from
counting.

## 7 · The orbit equation

One principle now enters, and it is named as the principle it is: **the
stationarity rule**. Among the admissible states at fixed winding, the state
realized is the one that makes the energy stationary. This is a principle of
least action. It does in this framework the work that Newton's second law does
in his, and it is the only principle the paper assumes rather than derives.

Compose the results. Quadratic energy in the rate, the conserved winding
L, and the potential derived in the gravity record give the radial
energy E(r) = L²/2r² − K/(r+λ₁), and stationarity in r gives

```
      L²  =  K r³ / (r + λ₁)²        ⟺        v²  =  K r / (r + λ₁)²
```

This is the relation that classical kinematics supplies as a postulate.
Here it is derived from §§3–6 and the stationarity rule, and the results
standing on it follow without further assumption:†

- **the orbital exponent climbs the rest values** — one half at contact,
  one at the first rung, three halves in the far field, so Kepler's
  third law is the reversal pair of three halves and two thirds;
- **the exact deviation** T/T_Kepler = 1 + λ₁/r at every radius, whose
  power-law form no Yukawa correction can imitate;†
- **the apsidal ladder** π/√3 to π/√2 to π, closure exact only in the far
  limit, the far precession retrograde and power-law small.

<div class="vnote">† Version 1 said these follow from §§3–6 alone; they
rest also on the stationarity rule.</div>

<div class="vnote">† Version 1 put the deviation four orders from an
exponential correction at ten rungs, which depends on the Yukawa's
strength; the gravity record states the comparison as here.</div>

## 8 · The three laws, located

**The first law is derived.** Persistence is the absence of rest, by Theorem 1.

**The second law's shape is derived, and its coefficient is
established.** A quadratic energy makes momentum linear in rate, so
force — the energy gradient — changes momentum in proportion to the
change of rate. The coefficient is the rider count. The sourcing
congruence k·142857·7 = k·10⁶ − k makes the absolute shortfall
proportional to k and the relative shortfall independent of it. Force is
therefore proportional to source and response independent of the rider,
from one congruence, as the gravity record established.

**The third law is derived.** In the two-rider rule each rider is
accelerated by the sum of the other counts, weighted by the extension
law, with its own count absent. The force rider j exerts on rider i is
the count product k_i k_j in one direction. The force i exerts on j is
the same product in the other. Action and reaction are one
multiplication read twice, and the multiplication commutes. Momentum
conservation follows tick by tick, exactly. The merger of co-addressed
riders is determined rather than chosen, because an address on the cycle
holds a total and not a list. The energy of the merger is one-signed,
and equals the reduced-count relative term exactly. The total binding of
any assembly is path independent — a state function, verified in exact
arithmetic. The rule inherits the conditionality of §7's postulates and
nothing further. Its filters are machine checked in
`verify/test_two_riders.py`: exact reduction to the one-dimensional
count-force dynamics, the equivalence principle as an identity, and the
far-field orbit with the total count as source.

## 9 · What the continuum deletes

A trajectory is the quotient of a counted path. The tangent vector is
the limit that forgets how many ticks were used and in what order; the
smooth velocity is the trail with its count erased. The mechanics
recovered in this paper retains the full count: every rate a fraction,
every energy a square of counted increments, every conserved quantity an
exact count. The continuum approximation is exact in the far field for
the same reason it is exact for the metric: the steps average. It fails
within the first rungs, where the count is coarse and is itself the
physics.

## 10 · The correspondence: the tick rate as tempo

This section states the musical correspondence; nothing below depends on it.

Melody moves at notes per beat. However fast the passage, there is a
tempo, and the fastest playable music is one note per beat of the
smallest pulse: nothing can be played between the clicks of the
metronome's finest subdivision. That is Theorem 2, familiar to every
performer: the speed limit is the tick.

The piece also cannot stop, and the reason must be stated with the right
operation, because the obvious version of it is false. Two voices
*counting* in twos and threes coincide every six beats: duple against
triple meets regularly. The incommensurability is multiplicative, not
additive. The voices that never meet are the ones that **double** and
**triple**: 2ᵃ never equals 3ᵇ above one, by unique factorisation.
Stacked against octaves, fifths make the same fact audible: twelve
fifths overshoot seven octaves by the Pythagorean comma, and the circle
never closes however many times it is traversed. Every apparent cadence
is provisional, and the counterpoint is perpetual by arithmetic. What
physics calls inertia corresponds in music to a canon without a final
bar. Motion persists for the same reason that the spiral of fifths never
closes into a circle: there is no place where both ladders meet.

## 11 · What would refute this

1. A common value 2^p = 3^q with positive exponents refutes Theorem 1
  and restores a rest state. The parity of integers forbids it.
2. A rider advancing more than one rung in one tick refutes Theorem 2;
  the definition of the cycle makes the advance and the tick one event.
3. A configuration whose energy of motion, on the established form,
  scales other than quadratically — a doubled rate carrying other than
  four times the energy on the Dirichlet form — refutes Theorem 3 in a
  line of arithmetic.
4. A tick count m not recovered from windings and phase, or a cycle
  state repeating before the sixth rotation, refutes Theorem 4.
5. If stationarity of E(r) = L²/2r² − K/(r+λ₁) fails to give v² =
  Kr/(r+λ₁)², the recomposition fails; the algebra is four lines and
  machine checked.
6. The stationarity rule is the paper's one assumed principle. A
  realized configuration that is not stationary at fixed winding — in
  any system this series treats — refutes the postulate itself, and with
  it §7.

A condition that is met is recorded as a refutation and is not
reinterpreted. The program then uses the miss to find why the
construction failed, and a revised statement enters as a new one under
its own date.†

<div class="vnote">† Added in version 2.</div>

## 12 · Relation to the standard account

Galileo's inertia and the relativity of uniform motion appear here as
the zero mode: uniform advance carries no energy, so no experiment
inside the configuration detects it. Newton's laws are located in §8:
the first derived, the second derived in shape with an established
coefficient, and the third derived in the two-rider rule.† Lagrange and
Hamilton's stationarity is the one principle this paper takes, named as
a rule rather than derived; the series holds it where the classical
tradition holds it, at the foundation. Noether's account derives
conservation from symmetry. The discrete account derives it from
counting, by way of the append-only count. Noether's theorem requires a
continuous symmetry group; the count requires only integers, which is
why quantization arrives with conservation rather than after it.
Bertrand's theorem makes the closed orbit exceptional among force laws.
It appears here as the far-field limit of the apsidal ladder. Exact
closure is the idealization, and the near field opens the ellipse the
way the commas of the companion records open every cycle. The
special-relativistic speed limit is recovered as a counting bound,
agreeing with the octave-boost identification of the gravity record: the
limit is not a property of light but of counting, and light is the thing
that saturates it.

<div class="vnote">† Version 1 called the third law a labeled candidate
here, while §8 derives it in the two-rider rule.</div>

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
- the determined merger and its one-signed energy
- the path independence of the binding energy
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
9. Born, M. (1926). Zur Quantenmechanik der Stoßvorgänge. *Z. Phys.* 37, 863–867.
10. Bern, Z., Carrasco, J. J. M., and Johansson, H. (2010). Perturbative quantum gravity as a double copy of gauge theory. *Phys. Rev. Lett.* 105, 061602.

---

*Companions: Gravity on Discrete Terms, the form, the coupling and the
kinematics of §16, DOI 10.5281/zenodo.22087599 · Units on Discrete
Terms, the dimensional boundary, DOI 10.5281/zenodo.22119360 ·
Schrödinger's Piano, the thought experiment, DOI 10.5281/zenodo.21211076
· The Origin on Discrete Terms, the figure, DOI
10.5281/zenodo.21212112.*

<div class="copyright" style="margin-top:24pt">Copyright<br>Christian Horstmann · August 25th, 2026 · version 2, October 2026<br>thefirsthorstmann@gmail.com<br>All rights reserved</div>

## Addendum: the eccentric orbit family and the orbital instrument

The eccentric family is closed at first order for every eccentricity.
The softened potential's orbit family is the precessing conic, with an
apsidal drift of −2πλ/p per orbit. Here p is the semi-latus rectum a(1
− e²), the circular result's radius replaced by the conic's own —
verified by direct integration and pinned in
verify/test_the_orbital_account.py. The same battery pins the orbital
test. A log-periodic force residual of amplitude A precesses a
near-circular orbit by (2π²A/ln 2)·sin(2π log₂ r + φ) per orbit.
Planetary ephemerides therefore test the fixed-period template
published with the gravity record at four parts in ten trillion, eight
to nine orders of magnitude beyond laboratory sensitivity.†

<div class="vnote">† Version 1 said nine orders. The gravity record,
where the estimate is made, gives eight to nine.</div>
