---
title: π on Discrete Terms
subtitle: Construction routes, finite realizations, and the rest value — the intensional arithmetic of the circle's number.
byline: Christian Horstmann · thefirsthorstmann@gmail.com · July 5th, 2026 · version 2, October 2026 · manuscript for the public record
date: 2026-07-05
titlenote: A claim is asserted about mathematical practice — that equality by value has erased a distinction the sciences in fact depend on, and that the coefficients of physics, the realizations of measurement, and the classical brackets of geometry all carry it. π is taken as what it is established to be, a limit with the accepted digits. Every exact claim is pinned by a public test suite.
abstract: Analysis defines a real number by its value, and on the real line a value has no memory — two constructions that agree in the limit are one object. This paper argues that the sciences do not, in practice, live by that identification, and that π is the clearest case. Three exhibits are assembled, each machine-verified. First, the working coefficients of physics are construction routes presented as values: 2π is one closure of a cycle; 4π is a point's flux into three-space, the azimuth closure times a polar diameter that integrates to exactly 2; 8π in the Einstein field equations is doubled flux, not eight of anything; π²/6 is the integer lattice counted with no circle drawn; π⁴/15 — the coefficient of Planck's count, the count that preceded the full diagnosis of the ultraviolet catastrophe — carries the counting of thermal modes in its construction; and the ladder of sphere measures 2π, 4π, 2π² assigns each dimension its own closure signature. The route, not the value, is what the physics means, and a table of such signatures is presented as an object of study. Second, π needs no circle: the central binomial coefficient's envelope forces π from the counting of binary outcomes alone, and the convergence is exhibited to pinned precision — the number is a property of enumeration before it is a property of geometry. Third, no finite set of finite-precision measurements can distinguish π from a rational: for every precision a rational witness agreeing to that precision is constructed, so the completed limit — π as a finished infinite object — is a convention of notation, not an observable; this is the same demarcation argument the companion paper applied to the continuum fluid, and it points the same way. On these terms a further object is defined and one theorem about it proved. The classical method of Archimedes brackets π between inscribed and circumscribed polygon values; it is proved that the midpoint of every such bracket sits strictly above π, with the excess-to-deficit ratio tending to exactly 2 — the midpoint of every classical bracket overshoots, and by a fixed asymptotic proportion. Naming the two smallest natural registers — sevenths from above (22/7, the first continued-fraction convergent beyond 3) and six binary places from below (201/64) — the bounds are forced by floor and ceiling, and their midpoint is exactly 2815/896: rational, constructible, denominator 2⁷·7, sitting 47 parts per million above π — an overshoot established by direct calculation, in the same direction Theorem 3 forces on the classical stages. We call such an object a rest value — exactly calculable, never the realized measurement — and we display the register choice as a definition, not a discovery. The distinction between π and its rest value is categorical, not numerical: one is transcendental and unreachable by any finite process, the other rational and constructible, and they are objects of different kinds. A closing conjecture, on which nothing else depends, then proposes the rest value's physical status: realized circles lie strictly below the transcendental bound and bear an energy cost for their shape, as a played string sounds sharp of its rest pitch, so the exactly calculable center of the classical enclosure is advanced as the candidate for the circle's constant at zero excitation, and the expansion of 2815/896 — which settles after seven places into the pure repeating cycle of 1/7, where π's never settles — is offered as an illustration. What would refute this paper is stated: a physical realization of a completed infinite process, a finite measurement that excludes all rationals, or an Archimedean bracket whose midpoint undershoots. One measurement in which the circle constant does not cancel, the counting of atoms in a silicon sphere, is set against the conjecture: it reads π, and what it shows about the operations that return a circle constant is drawn out. Every exact claim re-derives in the public suite at github.com/thefirsthorstmann/g-theory-verify, where the arithmetic of the rest value is also formalized in Lean 4.
---

## 1 · Introduction

Two questions about a number are habitually treated as one: what is its
value, and how was it built. Analysis, for its own good reasons,
quotients by the first — a real number is an equivalence class of
constructions, and on the real line the class forgets its members. This
identification is called here the value-quotient. The habit is so
complete that the second question has almost no standard vocabulary
left. This paper's claim is that the sciences do not actually live
inside that quotient: the working coefficients of physics, the
realizations of measurement, and the classical geometry of the circle
all distinguish, in practice, between constructions the value-quotient
identifies. π is the clearest case, and the present paper assembles the
evidence for π alone.

One thing is said before anything else, because the territory near this
subject is crowded with claims of a different kind: **π is established
as a limit, the least upper bound of every realized value and the
greatest lower bound of every construction from above, reached by
neither.** Every digit is the accepted one. The object defined in
Section 6 is rational where π is transcendental, and Section 7
conjectures that it, and not the limit, is the circle's constant at zero
excitation. The subject throughout is routes and realizations.

Three exhibits and one theorem carry the argument. Section 3 presents
the coefficients of physics as construction routes presented as values,
and assembles the signature table. Section 4 shows π forced by pure
counting, with no circle drawn. Section 5 proves that finite-precision
measurement can never certify the completed limit — the demarcation
argument of the companion paper [5], applied now to a number rather than
a fluid. Section 6 proves the overshoot theorem for the classical
brackets and defines the rest value. Section 7 advances, under an
explicit label, the conjecture of the rest value's physical status.
Section 8 states what is established, what is conjectured, the
measurement the conjecture faces, and what would refute each.

## 2 · The three ways π has been computed

The history of π is a history of three methods, and they do not realize
the same kind of object. The bounding geometry of Archimedes [1]
produces *rational brackets*: pairs of constructible numbers provably
enclosing π, tightened by doubling, never touching. The infinite series,
from the Leibniz–Madhava alternation through Wallis's product [2] to the
modern algorithms, produce *completed limits*: the number treated as a
finished infinite object, of which any run of the machinery delivers
finitely many digits. And the statistical methods — Buffon's needle,
Monte Carlo — produce *realizations*: finite samples whose scatter
narrows toward the value without ever constituting it.

A bracket, a limit, and a sample are three different objects. The value-quotient identifies them; every working use of them keeps them apart. A bracket certifies; a limit defines; a sample estimates. The paper's whole argument is in that observation, unfolded.

## 3 · The coefficients of physics as construction routes

Physics checks its units with total discipline — a dimensional error
invalidates a result — and checks construction routes not at all: 8π may
be replaced by any expression of the same value without a referee's
comment. Yet the coefficients themselves are routes, and their routes
say what the physics means.

| coefficient | construction | what the route says | canonical site |
|---|---|---|---|
| 2π | one closure of a cycle | a single turn or period | ℏ = h/2π; Fourier analysis |
| 4π | (2π) × 2 — azimuth closure times the polar diameter, ∫₀^π sinθ dθ = 2 exactly | a point's flux into three-space | Gauss's law; 1/4πε₀ |
| 8π | 2 × (4π) — doubled flux | tensor sourcing of curvature | the Einstein field equations |
| π²/6 | the integer lattice's second sum, ζ(2) | double periodicity by counting — no circle drawn | the Basel problem; Casimir coefficients |
| 16π² | (4π)² — flux squared | one loop: a four-momentum closure | the loop factor of field theory |
| √π | one dimension's share of a two-dimensional closure | the enumeration envelope | diffusion; the Gaussian integral |
| 2π² | the measure of the three-sphere | closure in four dimensions | compactification volumes |
| π⁴/15 | Planck's integral ∫x³/(eˣ−1)dx — the fourth lattice sum | thermal modes counted | blackbody radiation [6] |

Read down the middle column and the table is a ladder of sphere measures
— S¹ = 2π, S² = 4π, S³ = 2π² — with each physical site inheriting its
coefficient from the dimension its process closes on. Planck's
coefficient π⁴/15 carries the counting of modes in its own construction
— and the count came first, before the ultraviolet catastrophe it
forestalls had been fully diagnosed [6]: the resolution of the first
great infinity crisis of physics was a *route*, and the route is still
legible in the number. Einstein's 8π is two sheets of flux, not eight of
anything: replace it by 25.13274 and the value remains while the physics
of the coefficient — what it is *made of* — is erased. The table is
presented as an object of study: the individual integrals are all
classical, and the claim attached to the table is the modest one that
the middle column exists — that routes carry content the value-quotient
deletes.

## 4 · π from pure counting

**Theorem 1: The counting envelope**

*Let W(n) = C(2n, n)/4ⁿ, the probability that 2n independent even-chance
binary trials balance exactly. Then n·W(n)² → 1/π: equivalently, π = lim
1/(n·W(n)²). π is forced by enumeration alone, with no circle drawn.*

*Proof.* W(n) = C(2n,n)/4ⁿ, and by the de Moivre–Stirling asymptotics [3] C(2n,n) ~ 4ⁿ/√(πn), whence n·W(n)² → 1/π. The classical bridge is Wallis's product [2], which delivers the same constant from the same combinatorial kernel without any appeal to geometry. ∎

The convergence is exhibited in the accompanying suite: the estimate descends monotonically onto π and agrees to better than one part in 10⁴ by n = 10⁴. The philosophical weight of the theorem is not its difficulty — it is elementary — but its direction: the number that names the circle arrives before any circle does, as the envelope of counting. A discrete substrate that can only count has already, in that capacity, everything π requires.

## 5 · Finite precision never certifies the limit

**Theorem 2: Indistinguishability**

*Let O be any finite set of measurements or computations, each of finite precision, each consistent with the value π. Then there is a rational number consistent with every member of O.*

*Proof.* Every test in O that π passes, it passes with strict margin: a finite-precision test compares against a rational reading within a rational tolerance, and π, being irrational, never sits on the boundary — each test i leaves a positive slack δᵢ between π and the edge of its acceptance region. Let δ = min δᵢ > 0 over the finite set O, and take the truncation r = ⌊10ᴶπ⌋/10ᴶ for any J with 10⁻ᴶ < δ. Then |r − π| < δ, so r lies inside every acceptance region alongside π. The witness is constructed, not merely asserted; the suite exhibits it, including at boundary-tight tests where a shallow truncation fails. ∎

The consequence is the same demarcation the companion paper proved for
fluids [5]: the distinctive content of the completed limit — π as a
*finished* infinite object, as against an unbounded family of rational
brackets and realizations — entails no finite-precision observable
consequence whatsoever. Every dataset consistent with the limit is
consistent with its denial. What finite processes possess of π is
exactly the brackets, the algorithms, and the samples: the routes. The
completed object is a convention of notation — a useful one, adopted
here as everywhere, but a convention, and Section 6 uses what that
status permits: if the limit is a convention, the *structured rational
objects beneath it* are legitimate subjects of theorems.

## 6 · The rest value: the exact center of the classical enclosure

**Theorem 3: The Archimedes overshoot**

*Let I_n < π < C_n be the inscribed and circumscribed perimeter bounds of the regular n-gon, n = 6·2ᵏ, generated by the classical doubling. Then the midpoint (I_n + C_n)/2 exceeds π for every n, and the ratio of excess to deficit, (C_n − π)/(π − I_n), tends to 2.*

*Proof.* With x = π/n the bounds are I_n = n sin x and C_n = n tan x, so C_n − π = n(tan x − x) and π − I_n = n(x − sin x). For 0 < x < π/2, tan x − x = ∫₀ˣ tan²t dt while x − sin x = ∫₀ˣ 2 sin²(t/2) dt, and tan²t > t² > 2 sin²(t/2) on the interval; the excess therefore strictly exceeds the deficit and the midpoint exceeds π for every n ≥ 3 — universally, with no appeal to asymptotics. For the ratio: the expansions I_n = π − π³/6n² + O(n⁻⁴) and C_n = π + π³/3n² + O(n⁻⁴) give (C_n − π)/(π − I_n) → 2, the midpoint overshooting by π³/12n² + O(n⁻⁴). The suite verifies both: twelve doublings for the ratio, every polygon order to two thousand for the inequality. ∎

The midpoint of the classical bounds therefore always sits *above* π, by
a fixed asymptotic proportion of the bracket width. The overshoot is a
structural property of bounding the circle from inside and outside by
straight lines: in the limit the corners of the circumscribed polygon
add exactly twice what the chords of the inscribed one remove.

**Definition: The register bracket and the rest value**

A register is the set of fractions with one fixed denominator. Name the
two smallest natural registers — sevenths from above, six binary places
from below — and the bounds are forced, with no further choice: the
least seventh above π is ⌈7π⌉/7 = **22/7**, the first continued-fraction
convergent beyond 3 [4]; the greatest sixty-fourth below π is ⌊64π⌋/64 =
**201/64**. Their midpoint is exactly

**ρ = (201/64 + 22/7)/2 = 2815/896,**

rational, ruler-and-compass constructible, denominator 2⁷·7, sitting 47 parts per million above π — an overshoot the suite pins by direct calculation; the register bracket is not an Archimedean stage (its excess-to-deficit ratio is ≈ 1.31, not 2), so Theorem 3 does not apply, but the direction agrees. We call ρ the **rest value** of the bracket: the exactly calculable center of the tightest classical enclosure at the named registers. The choice of the two registers is a *definition, displayed as one* — sevenths because 22/7 is the canonical convergent every tradition reaches first; six binary places as its dyadic counterpart — and everything downstream of the choice is exact arithmetic with no further freedom.

The concept the definition carries: a rest value is *calculable and
never measurable*. No sample, no algorithm run, no physical process
delivers ρ — it is not the value being approached but the exact center
of the approach's classical enclosure. π and ρ differ categorically, not
numerically: one transcendental, unreachable and uncertifiable by any
finite means (Theorem 2); the other rational, constructible, known
exactly. They are objects of different kinds. What the pair exhibits is
the paper's whole thesis in one line: **beneath the completed limit, the
discrete structure is not featureless — it has centers, registers, and
theorems of its own.**

## 7 · Conjecture: the circle's constant at zero excitation is its rest value

Three facts stand proved above; what follows is a conjecture built on
them, and nothing else in this paper depends on it. First, a physically
realized circle is a finite-resolution object — operationally a polygon
— so every realized ratio of circumference to diameter lives strictly
below π, approaching the bound and never reaching it: the bound is the
limit of realizations, not a realization — Theorem 3's inscribed values
I_n < π are the same fact in classical form, and Theorem 2 adds that no
finite precision certifies the limit. Second, realization is never free.
A circle given physical shape is held in shape — a hoop under stress, a
standing wave under tension, an orbit under force — and a circle
measured is a circle excited: the probe supplies the energy that makes
the reading possible. A played string sounds sharp of its rest pitch and
settles toward it only as the excitation decays; a realized circle
constant is offset from its rest value the same way, and the rest value
is therefore reachable only by calculation — never by measurement, which
is always an excitation. Third, the calculable exact objects available
are the brackets and their centers, and Theorem 3 fixes their geometry:
the midpoint sits above π by a forced proportion.

The conjecture: **the physically operative exact constant of the circle
— the value the circle has at zero excitation — is the rest value of its
classical enclosure, not the transcendental limit.** π remains exactly
what it is: the boundary between the realizable-from-below and the
constructible-from-above, touched by neither. The proposal concerns the
value physics actually uses — whenever an exact, finitely expressible
stand-in for the circle constant is operationally required, the bracket
center is the principled candidate: calculable, constructible, and
displaced above the limit by precisely the geometry of enclosure. One
exact property illustrates the candidate: the expansion of ρ = 2815/896
settles, after seven places, into a pure six-place cycle — 3.1417410,
then 714285 repeating forever, the reptend of 1/7 — where the expansion
of π never settles at all. The realized world approaches from below and
bears an energy cost for every step it takes; the rest value sits
exactly still above the approach, already known. What would refute the
conjecture is stated in Section 8.

## 8 · What is established, and what would refute it

**Established.** That construction routes carry scientific content the
value-quotient deletes, with the table of Section 3 as the assembled
evidence; that π is forced by counting before geometry (Theorem 1); that
the completed limit is finitely uncertifiable (Theorem 2); that the
classical bracket midpoints overshoot with excess-to-deficit ratio 2
(Theorem 3); and that the register midpoint 2815/896 is a well-defined,
exactly computable structural object of the bracket, introduced under a
displayed definition.

**Adopted and conjectured.** π is the limit described in Section 1. The
individual classical results assembled belong to their authors [1–4];
the table of Section 3 is an *assembly*, and to the author's knowledge
it has not been systematically compiled elsewhere. The physical status
of ρ is the conjecture of Section 7, and nothing else in the paper
depends on it.

**What would refute this paper.** A physical realization of a completed
infinite process (which would also refute the companion paper [5], and
more besides); a finite-precision measurement that excludes all
rationals (Theorem 2 constructs a rational witness for every one, so
this would be an error in that construction); an Archimedean bracket
stage whose midpoint undershoots π (a single counterexample falsifies
Theorem 3); or a demonstration that any working use of a route-distinct
coefficient is invariant under route replacement — that 8π as doubled
flux and 8π as eight turns do the same explanatory work in the Einstein
equations. The last is the deepest test.

**One measurement in which the circle constant does not cancel has been
made, and it reads π.** In most precise measurements the constant
cancels between the formula and the unit of the result, as an angle
reported in arcseconds carries the same π as the expression that
predicts it. The counting of atoms in a one-kilogram sphere of
silicon-28 is different [7]: eight atoms to each cubic cell of edge
543.0996 pm, in a volume taken as that of a mathematical sphere of the
measured mean diameter, 93.72 mm. π enters that count once, and the
independent route through the Kibble balance does not contain it [8].
The two agree to between four and seven parts in 10⁸. With the rest
value in place of π the count would move by 47 parts per million, more
than six hundred times the larger difference. For a counted sphere the
operative constant is π.

**At the scale of the atom a curve is no longer a physical object, and
the circle constant depends on the operation.** On a square-lattice disc
three operations return three constants. Counting the points inside
returns π. A taut line through the outermost points returns π from
below. A line that follows the steps of the boundary returns four times
the diameter at every size, and in silicon a path from atom to atom
along the bonds is longer than the straight line by 22 to 73 percent.
The smooth circle is the common limit of the first two and of no stepped
line. The sphere experiment ends where the grain begins: one atomic
layer of doubt in the place of the surface is one to two parts in 10⁸ of
the volume, the size of its stated uncertainty. On discrete terms a
curve is the exact summary of a large grouping; below the grain it has
no referent, and what a measurement returns there is fixed by what is
measured and how. This is the companion paper's point about the
continuum fluid [5], met in a solid: such a description serves the
grouping and does not explain the grain.

**What would refute the conjecture.** It fails separately, and more
easily: if realized circle constants show no offset scaling with the
energy of their realization, or if the operational role it names — the
exact finite stand-in — can be shown to need no principled occupant. The
sphere is the first such test. As a count at room temperature it shows
no offset at 47 parts per million, so the conjecture does not hold of
counts; it stands as a statement about an operation it has yet to name,
and naming that operation is the open problem of Section 7.

## 9 · Conclusion

π has been treated here as a family of constructions with one value:
brackets that certify, limits that define, samples that estimate, routes
that mean. Each exhibit is classical; the assembly is the contribution.
The practical moral is addressed to physics, whose unit discipline is
total and whose route discipline is nonexistent: the coefficients are
not incidental, and the table of their signatures is small enough to
check by hand. The structural moral is the rest value: beneath the limit
convention, the rational scaffolding of the circle has its own exact
centers and its own theorems — the overshoot is one, and it was sitting
in Archimedes' method for twenty-two centuries, unnamed because the
value-quotient gave no reason to name it. The routes were always there.
The quotient forgot them; the count did not.

## References

[1] Archimedes, *Measurement of a Circle*, in T. L. Heath (ed.), *The Works of Archimedes*, Cambridge University Press (1897).

[2] J. Wallis, *Arithmetica Infinitorum*, Oxford (1656).

[3] A. de Moivre, *Miscellanea Analytica*, London (1730); J. Stirling, *Methodus Differentialis*, London (1730).

[4] G. H. Hardy, E. M. Wright, *An Introduction to the Theory of Numbers*, Oxford University Press, 6th ed. (2008), ch. X–XI.

[5] C. Horstmann, *Navier–Stokes: A Solution on Discrete Terms*, Zenodo
preprint (2026), DOI 10.5281/zenodo.21197044.

[6] M. Planck, *Zur Theorie des Gesetzes der Energieverteilung im Normalspectrum*, Verhandl. Deut. Phys. Ges. **2** (1900) 237–245.

[7] B. Andreas *et al.*, *Determination of the Avogadro constant by
counting the atoms in a ²⁸Si crystal*, Phys. Rev. Lett. **106** (2011)
030801.

[8] P. J. Mohr, D. B. Newell, B. N. Taylor, E. Tiesinga, *Data and
analysis for the CODATA 2017 special fundamental constants adjustment*,
Metrologia **55** (2018) 125–146.

*All exact claims — the bracket and convergence facts of Theorems 1 and
3, the witnesses of Theorem 2, the forced bounds ⌈7π⌉/7 and ⌊64π⌋/64,
the identity ρ = 2815/896 and its 47 ppm overshoot, and the lattice
counts of Section 8 — re-derive in the public suite, where the register
bracket, the identity for ρ, its overshoot and its decimal tail are also
formalized as seven theorems in Lean 4 with Mathlib:
github.com/thefirsthorstmann/g-theory-verify.*

**Version 2 — October 2026.** Terminology is revised to the series
glossary: the completed limit, in place of the seated limit; excitation
and the rest value in Section 7. Section 8 states what is established,
what is adopted and conjectured, and the conditions that refute each; it
names the measurement the conjecture faces, the counting of atoms in a
silicon sphere, and what that measurement shows about curves at the
scale of the atom.

<div class="copyright" style="margin-top:115pt">Copyright<br>Christian Horstmann · July 5th, 2026<br>thefirsthorstmann@gmail.com<br>All rights reserved</div>
