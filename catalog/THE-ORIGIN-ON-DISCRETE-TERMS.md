---
title: G-Theory — The Origin on Discrete Terms
subtitle: A fully quantized history of the universe — no continuum objects, no free parameters — in twelve volumes, with proofs.
titlestyle: font-size:23pt; letter-spacing:1px;
titleblock: none
byline: Christian Horstmann · thefirsthorstmann@gmail.com · July 2026 · version 3, October 2026 · manuscript for the public record
date: 2026-07-05
titlenote: This monograph is the model statement of a research program whose companion records are public; they are listed with their DOIs at the end of the Mathematical Companion. Version 3 follows the series glossary; changes of substance from version 2 are marked † and noted where they occur.
abstract: Twelve volumes carry the universe from initial conditions to the present on discrete terms, with no continuum objects and no free parameters. Volume I fixes the initial conditions without an initial instant and shows that the first operation is free. Volume II derives the dipole as the first structure and the absence of the monopole. Volume III derives the fermion charge table as a uniqueness theorem and the primordial helium fraction. Volume IV follows the plasma era through fifty octaves to recombination. An interlude places the four interactions in order of appearance and states gravitation as the register's reference level, the tonal center. Volume V derives the filling order of the periodic table from one closed form that ends at element 118. Volume VI reads the orbital resonances as small-integer ratios and bounds gravitational collapse. Volume VII states the cosmic budget in fifteenths and locates its two turning points. Volume VIII reads quantum measurement as filtering and tests Bell's inequality on a register machine. Volume IX derives position as an address and diffusion as a counting identity. Volume X confronts relativity and names three open problems. The Mathematical Companion states the construction as theorems, centred on the Line Theorem, and gives the reproduction manual. In Pure Mathematics closes with fourteen theorems that use no physical terms. A confirmed magnetic monopole or a fourth light fermion generation refutes the account. Every exact claim re-derives in a public suite at github.com/thefirsthorstmann/g-theory-verify, where the register theorem, the charge table, the filling order and Bell’s bound are also formalized in Lean 4.
---

<div class="cover"><div class="covertitle">G-THEORY</div><div class="covertitle2">The Origin on Discrete Terms</div><div class="coversub">A fully quantized history of the universe — no continuum objects, no free parameters — in twelve volumes, with proofs.</div><div class="coverby">Christian Horstmann · 2026</div></div>

<div class="epigraph">“In ancient times the holy sages made the Book of Changes thus: They invented the yarrow-stalk oracle in order to lend aid in a mysterious way to the light of the gods. To Heaven they assigned the number three and to Earth the number two; from these they computed the other numbers.”<div class="epigraphsrc">— the I Ching, Shuo Kua I (Wilhelm–Baynes)</div></div>

<div class="volhead">CONTENTS</div>

<div class="tocline"><span class="toct">OVERTURE</span><span class="tocd"></span><span class="tocp">4</span></div>
<div class="tocline"><span class="toct">VOLUME I · INITIAL CONDITIONS</span><span class="tocd"></span><span class="tocp">5</span></div>
<div class="tocline"><span class="toct">VOLUME II · THE DIPOLE</span><span class="tocd"></span><span class="tocp">15</span></div>
<div class="tocline"><span class="toct">VOLUME III · FIRST PARTICLES</span><span class="tocd"></span><span class="tocp">22</span></div>
<div class="tocline"><span class="toct">VOLUME IV · PLASMAS</span><span class="tocd"></span><span class="tocp">30</span></div>
<div class="tocline"><span class="toct">INTERLUDE · THE FORCES, IN ORDER OF APPEARANCE</span><span class="tocd"></span><span class="tocp">35</span></div>
<div class="tocline"><span class="toct">VOLUME V · THE BIRTH OF CHEMISTRY</span><span class="tocd"></span><span class="tocp">38</span></div>
<div class="tocline"><span class="toct">VOLUME VI · EARLY GALAXIES</span><span class="tocd"></span><span class="tocp">43</span></div>
<div class="tocline"><span class="toct">VOLUME VII · THE PATH TO THE PRESENT</span><span class="tocd"></span><span class="tocp">48</span></div>
<div class="tocline"><span class="toct">VOLUME VIII · MODERN PHYSICS</span><span class="tocd"></span><span class="tocp">53</span></div>
<div class="tocline"><span class="toct">VOLUME IX · POSITION AND DIFFUSION</span><span class="tocd"></span><span class="tocp">61</span></div>
<div class="tocline"><span class="toct">VOLUME X · RELATIVITY AND THE STANDARD MODEL</span><span class="tocd"></span><span class="tocp">65</span></div>
<div class="tocline"><span class="toct">THE MATHEMATICAL COMPANION</span><span class="tocd"></span><span class="tocp">72</span></div>
<div class="tocline"><span class="toct">IN PURE MATHEMATICS</span><span class="tocd"></span><span class="tocp">79</span></div>
<div class="tocline"><span class="toct">DEFINITIONS</span><span class="tocd"></span><span class="tocp">86</span></div>
<div class="tocline"><span class="toct">INDEX</span><span class="tocd"></span><span class="tocp">88</span></div>

<div style="page-break-before:always"></div>

<div class="title" style="font-size:23pt; letter-spacing:1px;">G-Theory — The Origin on Discrete Terms</div><div class="subtitle">A fully quantized history of the universe — no continuum objects, no free parameters — in twelve volumes, with proofs.</div><div class="byline">Christian Horstmann · thefirsthorstmann@gmail.com · July 2026 · version 3, October 2026 · manuscript for the public record</div><div class="titlenote">This monograph is the model statement of a research program whose companion records are public; they are listed with their DOIs at the end of the Mathematical Companion. Version 3 follows the series glossary; changes of substance from version 2 are marked † and noted where they occur.</div><hr class="rule">

<div class="abstract"><span class="lead">Abstract.</span> Twelve volumes carry the universe from initial conditions to the present on discrete terms, with no continuum objects and no free parameters. Volume I fixes the initial conditions without an initial instant and shows that the first operation is free. Volume II derives the dipole as the first structure and the absence of the monopole. Volume III derives the fermion charge table as a uniqueness theorem and the primordial helium fraction. Volume IV follows the plasma era through fifty octaves to recombination. An interlude places the four interactions in order of appearance and states gravitation as the register's reference level, the tonal center. Volume V derives the filling order of the periodic table from one closed form that ends at element 118. Volume VI reads the orbital resonances as small-integer ratios and bounds gravitational collapse. Volume VII states the cosmic budget in fifteenths and locates its two turning points. Volume VIII reads quantum measurement as filtering and tests Bell's inequality on a register machine. Volume IX derives position as an address and diffusion as a counting identity. Volume X confronts relativity and names three open problems. The Mathematical Companion states the construction as theorems, centred on the Line Theorem, and gives the reproduction manual. In Pure Mathematics closes with fourteen theorems that use no physical terms. A confirmed magnetic monopole or a fourth light fermion generation refutes the account. Every exact claim re-derives in a public suite at github.com/thefirsthorstmann/g-theory-verify, where the register theorem, the charge table, the filling order and Bell’s bound are also formalized in Lean 4.</div>

<div class="volhead">VOLUME I · INITIAL CONDITIONS</div>

*Time, matter, and asymmetry from three operations — a cosmogony with no free parameters, no continuum objects, and no initial singularity.*

This volume constructs the initial conditions of a universe from one postulate, that the substrate of physical process is counting, and proves that the first three operations available to such a substrate, ordered by cost, are uniquely determined. The first operation is an involution. The six digits of the first complete period of decimal division — 1/7 = 0.142857…, period 6 = 2×3 — admit exactly two canonical orders. These are the positional order in which division writes them, 142857, and the multiplicative order of the doubling orbit, 124875. The map between them holds the unit and the octave digit fixed, reverses the interior pairs, and is its own inverse. By Landauer's principle an invertible operation has no minimum thermodynamic cost: the first operation is free, and "least action at the origin" is thereby an observation, not an assumption. It creates displacement and conservation together: one interior pair falls by eighteen, the other rises by eighteen, the sum is invariant. The two orders it exchanges are structurally inequivalent, a sequence and its pair-reversal. This inequivalence is identified, as the first entry of the construction's physical dictionary, with the electric and magnetic faces of the field: the read face and the circulation face. Because the circulation face is a closed orbit with no endpoints, it has no sources: the solenoidal character of magnetism (∇·B = 0) holds from the first operation and is not an empirical regularity. The magnetic monopole is predicted absent — a standing falsification condition for this volume. The second operation is the carry, the unique non-local operation of positional counting, and time is defined as the count of carries: succession, not container. Asking what preceded the first carry is asking for a count below one. The question does not refer, so the construction contains no initial instant and no initial singularity. Independently, the zero of this arithmetic is a limit-place that no operation ever attains, so there is no object at the origin at which a singularity could occur. The third operation is the rounding — the first many-to-one, hence Landauer-costly, operation — and matter is identified with commitment: what persists is what has been rounded. The commitment ladder of the seed is exact. Rounding the first period at depths three, four and five lifts the carrier digits 2, 8, 5 to 3, 9, 6 respectively. The depth-three commitment is exactly a multiplication by 1001/1000, because 7 divides 10³+1 — the divisibility on which Midy's theorem rests. Three declared identifications — the two faces, time-as-carries, matter-as-commitment — yield the volume's results. The universe is born hot: the complete period, hence the full mode spectrum, is present in the first division, and heat death is descent rather than the approach to a beginning. Born chiral: the two faces are inequivalent by construction, and a handed cosmos follows. Dipole-first in its magnetism; three-tiered in its committed matter, by the three clean rounding depths; and singularity-free at both ends. Falsification conditions are enumerated, including two that can be tested today: a confirmed magnetic monopole, and a confirmed fourth light fermion generation. The framework's register is itself fixed by a least-action theorem and not by convention. Base ten is the least base in which residue bookkeeping modulo nine is preserved under digit summation and the first complete period appears in full. Below eighty the bases that carry both mechanisms are 10, 19 and 73, and the theorem is conditional on the two mechanisms. No parameter in this volume is free; no object in it is continuous; every equality in it is verified by machine.

## 1 · Introduction

**Every cosmology must answer three questions before its first equation
of motion.** They are what exists initially, why that and not something
else, and what the first events were.

**The standard account leaves all three open.** It posits a singular
initial state of infinite density and an inflaton field whose potential
is chosen to fit, evolving under equations whose twenty-six
dimensionless constants are measured and not derived. The first question
is deferred, since the singularity is where the theory's own description
ends. The second is outside its scope, since initial conditions are
inputs. The third lies beyond direct observation: models before
recombination, conjecture before inflation, and no description before
the Planck time.

**On discrete terms the three questions have exact answers.** The terms
are those of the companion paper on the Navier–Stokes problem [10]: the
substrate of physical process is discrete, events are counted, and the
continuum is a representation of them. What the account adopts from the
established record is named where it is used.

**What exists initially is the unit and the first incommensurable pair,
2 and 3.** No power of two equals a power of three: 2ᵃ = 3ᵇ has no
solution, since the left side is even and the right side odd.

**Nothing simpler exists to be chosen.** Counting begins at one and its
first two steps are 2 and 3, so the initial content involves no choice.

**The first events are three operations, ordered by cost: the first is
free, the second creates time, and the third creates matter.** They are
the subject of this volume.

**The volume proceeds in four steps: proofs, identifications,
consequences and refutation conditions.** It proves the arithmetic of
the three operations: the involution, the conservation, the exactness of
the first commitment, and the register theorem. It declares the three
identifications that constitute the physical dictionary. It derives what
the dictionary yields: a hot and chiral beginning, a dipole as the first
structure, three tiers of matter, and no singularity at either end. It
lists what would refute it: a magnetic monopole, a fourth light
generation, and the general conditions of the companion paper.

## 2 · The postulate, the register, and the seed

**Postulate C.** Physical process is the succession of distinguishable states of a finite counting system.

**The postulate's physical warrant is the Margolus–Levitin theorem,
which bounds the distinguishable state changes available at finite
energy [4].** It is the companion paper's substrate premise, adopted
whole, and everything in this volume depends on it.

**Rejecting the postulate commits an account to actual infinities.** The
alternative is a substrate executing uncountably many updates per
instant, a commitment shown in the companion paper to be unfalsifiable
in principle.

**A counting substrate that represents its states positionally must do
so in some base.** The mechanisms available depend on the base, and two
of them carry everything that follows.

**The first mechanism is residue bookkeeping.** The classes modulo 9 are
preserved under digit summation — so that the arithmetic of classes can
be read off representations — if and only if the base b satisfies

<div style="text-align:center; margin:12pt 0;">b ≡ 1 (mod 9)<span style="float:right;">(1)</span></div>

**The second mechanism is the complete period.** The first prime whose
reciprocal has the maximal period, exhibiting the full 2×3 cycle, is 7,
and its period is complete if and only if b is a primitive root modulo
7.

**Theorem (the register).** *Base ten is the least base carrying both
mechanisms, and the carriers are rare: 10, 19 and 73 are the only ones
below eighty. 28 fails because 7 divides it, while 3, 5, 12 and 17 give
the full period but fail the residue condition.* The proof is a finite
scan, machine-verified.

**The theorem is conditional on the two mechanisms.** They are the
construction's own commitments to 2 and 3: given the mechanisms, the
register is uniquely determined, and the mechanisms are the postulate's
own content.

**The seed is the pair 2 and 3, the first two counts beyond unity.**
Their powers never coincide:

<div style="text-align:center; margin:12pt 0;">2ᵃ = 3ᵇ &nbsp;has no solution in positive integers<span style="float:right;">(2)</span></div>

so no number of doublings ever equals a number of triplings — succession cannot terminate by coincidence.

**The near-misses of the pair, |2ᵃ − 3ᵇ|, are taken at the successive
convergents:**

<div style="text-align:center; margin:12pt 0;">|2ᵃ − 3ᵇ| : &nbsp;1, 5, 17, 13, 139<span style="float:right;">(3)</span></div>

— a ladder that will reappear throughout the series.

**The seed's first complete period is that of the division**

<div style="text-align:center; margin:12pt 0;">1/7 = 0.142857…<span style="float:right;">(4)</span></div>

period six — the first place the 2×3 cycle appears whole — with the complementary property of Midy

<div style="text-align:center; margin:12pt 0;">142 + 857 = 999<span style="float:right;">(5)</span></div>

on which the exactness of the third operation rests below.

## 3 · The first operation: the involution, and why the origin is free

**The six digits of the first complete period admit three natural
orders.**

| order | digits | how it arises |
|---|---|---|
| positional | 1, 4, 2, 8, 5, 7 | division writes them positionally |
| multiplicative | 1, 2, 4, 8, 7, 5 | the doubling orbit of the residues modulo 9 |
| harmonic | 1, 2, 4, 5, 7, 8 | the six sevenths themselves — 1/7 through 6/7 — carry them: the first digit of each, ⌊10k/7⌋ — the hexad in ascending order, skipping exactly the triad {3, 6} |

Three orders of one and the same six-element set: the order of *reading*, the order of *generation*, and the *harmonic* order in which the sevenths sound as nodes along a string.

**The first two orders are canonical, and the third is an order of the
family of fractions.** The first two are the figure's two Hamiltonian
readings, exchanged by the conserved involution. The third is not a path
on the figure: its leading digits are uniquely determined, and its
identification with the nodes of a string is a reading.

**Definition (the transform).** Hold the first digit (the unit) and the fourth (the octave digit, 8) fixed; reverse the two interior pairs:

<div style="text-align:center; margin:12pt 0;">1 | 42 | 8 | 57 &nbsp;→&nbsp; 1 | 24 | 8 | 75<span style="float:right;">(6)</span></div>

**Theorem (the first operation).** *The transform maps the positional order onto the multiplicative order —*

<div style="text-align:center; margin:12pt 0;">142857 → 124875<span style="float:right;">(7)</span></div>

*and 124875 is the doubling orbit read as digits — and it is an involution: applied twice, it is the identity.* Machine-verified.

Three consequences carry the volume.

**First: the operation is free.** An involution is invertible, and by Landauer's principle [1, 2] only irreversible — many-to-one — operations carry a minimum thermodynamic cost; reversible ones carry none. The universe's first operation therefore costs nothing. The principle of least action, at the origin, is not an axiom adopted: it is an inventory taken. Among all operations available to the structure, the minimum conceivable cost is zero, and the first operation attains it.

**Second: displacement and conservation are born together.** The transform's arithmetic is exact:

<div style="text-align:center; margin:12pt 0;">42 → 24 &nbsp;(−18), &nbsp;&nbsp; 57 → 75 &nbsp;(+18)<span style="float:right;">(8)</span></div>

<div style="text-align:center; margin:12pt 0;">42 + 57 = 24 + 75 = 99<span style="float:right;">(9)</span></div>

The pair 42 falls, the pair 57 rises, the sum is invariant. One
operation creates a displacement, its equal and opposite, and the
invariant they respect. Nothing moved "first"; the symmetry and the
conservation are the same fact.

**Third: the two faces are inequivalent — the origin is chiral.** The positional order and the multiplicative order are *not* related by any symmetry of the underlying set that preserves structure: one is a sequence, the other its interior pair-reversal.

**Identification.** The read face and the circulation face, the two
orders of the one structure, are identified with the electric and
magnetic faces of the field. This is the first entry of the
construction's physical dictionary. It is declared and not proved, and
its first consequence follows at once.

**A closed circulation has no sources.** The circulation face is a
*closed orbit*: the doubling sequence cycles with no endpoints. The
solenoidal character of magnetism therefore enters this construction
with the first operation, as the geometry of its second face, and not as
an empirical regularity awaiting explanation:

<div style="text-align:center; margin:12pt 0;">∇·B = 0<span style="float:right;">(10)</span></div>

**Prediction: there are no magnetic monopoles at any energy.** Dirac
showed that a single monopole would quantize charge [5]. On these terms
the implication runs the other way: charge is quantized because counting
is, and the monopole whose existence would explain the quantization is
structurally absent.

**Falsification.** One confirmed monopole falsifies this volume. Every
monopole search to date has returned a null result [6], as the
prediction requires.

**A universe built from two inequivalent faces is handed.** Chirality is
not introduced by an accident of dynamics; it is present in the initial
operation.

**The observed dipole excess is consistent with a handed cosmos, and its
amplitude remains open.** The large-scale dipole anisotropies in
radio-source and quasar counts exceed the kinematic expectation [7]. An
amplitude derived from the construction is what would make that
agreement a test.

## 4 · The second operation: the carry, and the origin of time

**Positional counting has exactly one non-local operation, the carry.**
It is the event in which a register, filled past its capacity, commits a
unit to its neighbor. Everything else in arithmetic happens *in place*;
only the carry *propagates*.

**Definition (time).** Time is the count of carries. Succession is not a container in which the construction sits; it is the tally of the construction's own propagating events.

The definition is literal, and three statements follow from it with no
free choice.

**There is no initial instant.** The first carry is event number one. To
ask what happened before it is to ask for a count below one; the
question does not refer. The construction does not *begin at* t = 0 — it
has no t = 0 to begin at, because time is a count and counts start at
one. The initial singularity of the standard picture is not resolved
here: it does not arise.

**The zero is not a term at which a singularity could occur.**
Independently of time's definition, the zero of this arithmetic is a
limit-place — the place toward which halving descends, (2ᴺ−1)/2ᴺ
approaching but never attaining unity's complement — and never a term of
the construction. There is no object at the origin at which a
singularity could occur.

**The singularity theorems stand as mathematics about the continuum
manifold [8].** The present construction contests the manifold and not
the theorems, as the companion paper does for the Navier–Stokes
singularity.

**The clock has an escapement.** The natural cycle of the construction's phases is the ring of eight (the octave digit's ring), and the natural step is three (the vector count). The 3-step on the 8-ring visits all eight positions and closes only at the least common multiple, 24, accumulating a deficit each cycle. The carry is the tick; the deficit is why the ticking never stops. A clock, on these terms, is a cycle plus a carry — and the universe has one from the second operation onward, not before.

**The construction begins with its complete spectral content.** The
first division does not produce its period gradually: all six digits of
142857, all six phases of the cycle, are present in the *first* complete
act of division. Every mode of the fundamental structure is excited at
once, and everything thereafter is *descent*: octave-by-octave cooling,
commitment, condensation.

**The heat of the hot big bang is the completeness of the initial
spectrum, not the temperature of an initial point.** The universe begins
hot because it begins *whole*, and it cools because descent is the only
direction succession offers. The statement belongs to the dictionary and
is tested by the thermal history.

**The identification requires that the cooling ladder reproduce the
thermal history, epoch by epoch.** The series takes this up beginning
with the plasma epoch of Volume IV.

## 5 · The third operation: the rounding, and the origin of matter

**A finite register cannot carry an infinite expansion.** At some depth
it must commit: truncate or round.

**The rounding is the first operation of the construction that is not
free.** Rounding is many-to-one: distinct states map to one committed
state, information is erased, and by Landauer's principle [1] the
erasure has a minimum cost. Work, heat, and irreversibility enter here,
and only here.

**Definition (matter).** Matter is commitment: what persists is what has been rounded. The third declared identification.

**The commitment ladder of the seed is exact and machine-verified.**
Rounding the first period at successive depths:

| depth | rounding | carrier lifted |
|---|---|---|
| three | 0.142857… → 0.143 | 2 → 3 |
| four | | 8 → 9 |
| five | | 5 → 6 |

**The depth-three commitment is exact in a sense the others are not:**

<div style="text-align:center; margin:12pt 0;">0.143 × 7 = 1.001<span style="float:right;">(11)</span></div>

so the depth-three rounding is precisely a multiplication by
**1001/1000**, because 7 divides 10³ + 1 — the divisibility on which
Midy's complement theorem rests (142 + 857 = 999). The construction's
first commitment is exact to the last digit.

**Identification.** The three depths, lifting the three carrier digits
2, 8, 5 to 3, 9, 6, are identified with the three generations of
committed matter:

<div style="text-align:center; margin:12pt 0;">2 → 3, &nbsp; 8 → 9, &nbsp; 5 → 6 &nbsp; (depths 3, 4, 5)<span style="float:right;">(12)</span></div>

This is the most direct test of the third identification: the structure
has exactly three clean commitment depths.

**Falsification.** A confirmed fourth light fermion generation falsifies
this volume.

**The invisible width of the Z boson counts three light neutrino species
[9].** On these terms the count is not an unexplained feature of the
particle spectrum: it is the number of rounding depths.

**In the width-three register the two natural multipliers act
oppositely.** Multiplication by 1001 *duplicates* a three-digit block,
the echo, and multiplication by 999 *splits* it into complements summing
to 999. Volume III builds on both:

<div style="text-align:center; margin:12pt 0;">×1001: &nbsp;a → a | a, &nbsp;&nbsp; ×999: &nbsp;a → a−1 | 1000−a<span style="float:right;">(13)</span></div>

**The first period connects the two multipliers through a single
number:**

<div style="text-align:center; margin:12pt 0;">1/7 = 143/1001 &nbsp;exactly, &nbsp;&nbsp; 143 × 999 = 142857<span style="float:right;">(14)</span></div>

— the period itself. The committed state and the flowing state are the two faces of one number under the register's two multipliers.

What this algebra becomes when the construction populates it — the
neutral pair, the split pair, the particle — is the subject of Volume
III.

## 6 · What the volume predicts, and what would falsify it

The three operations and three identifications yield, with no further input:

**1 · No magnetic monopoles.** It holds from the first operation, as a
property of the closed face.

**Falsification.** One confirmed monopole. It can be tested today, and
every search so far has returned a null result [6].

**2 · Exactly three generations of committed matter.** The three clean rounding depths.

**Falsification.** A confirmed fourth light generation. It can be tested
today, and the Z-width count [9] agrees with it.

**3 · A structurally chiral cosmos.** The two faces are inequivalent by
construction. The dipole-excess observations are consistent, and the
amplitude remains open.

**Falsification.** The general claim is falsified by demonstration that all large-scale handedness reduces to kinematics.

**4 · No initial singularity and no final one.** The question does not
arise at one end (there is no count below one), and the object is absent
at the other (the zero is not a term).

**The singularity theorems stand as mathematics.** They are contested as
physics at the level of their initial objects, as in the companion
paper.

**5 · Born hot, cooling by descent.** The thermal history is an octave
descent, developed volume by volume across the series.

**Summary.** Sections 2 through 5 proved the register theorem, the
two-orders theorem, the involution and its freedom, the conserved count
(±18, net zero), the incommensurability, the exactness of the
depth-three commitment, and the escapement arithmetic. The three
identifications — the two faces, time as carries, matter as commitment —
are declared and weighed, and predictions 1 through 5 follow from them.
The account adopts Landauer's principle and the Margolus–Levitin bound
from the established record. No free parameter is introduced, no
continuum object is employed, and the amplitude of the large-scale
dipole excess remains open, taken up in Volume II. A confirmed magnetic
monopole, or a confirmed fourth light fermion generation, falsifies the
volume.

**Volume II takes up the dipole in full.** It treats the cardioid as the
first radiating form, the multipole ladder of the two faces, and the
comparison with the measured large-scale anomalies.

## 7 · Objections

**"This is numerology."** The word names a practice — matching numbers
without structure, obligation, or risk. Every equality in this volume is
machine-verified; the register is fixed by a least-action theorem whose
conditionality is stated; the identifications are declared as such and
made to answer in falsifiable predictions; and two falsification
conditions can be tested today. The comparison is one of free
parameters. The standard account has a singular initial object outside
the theory's own description, an inflaton potential chosen from a
landscape, and twenty-six dimensionless constants without derivation;
this account has none.

**"The identifications are unproven."** Correct, and stated in the text
at every occurrence. They constitute a dictionary, and dictionaries are
judged by what they translate: this one translates three arithmetic
operations into the origin of conservation, time, and matter, and
returns five predictions, two of them falsifiable now. A dictionary that
returns results is retained; one that fails a falsification condition is
recorded as refuted. That is the whole standard, and the companion paper
is held to it as well.

**"Where does the energy come from?"** The first operation is free
(Landauer); structure precedes dynamics, and "energy" enters the
construction with the first costly operation — the rounding — whose cost
is balanced by the conservation established in the first operation. The
question presupposes that energy must be expended before anything exists
to expend it, and the construction has no such stage.

**"What happened before the first carry?"** Counts begin at one. The
question does not refer. The reader already accepts the same answer to
"what is north of the north pole"; here the reason is arithmetic and not
geometric, and the pole is event number one.

## 8 · Conclusion, and the series

**The initial conditions of the universe, on discrete terms, are unity
at rest, the incommensurable pair, and three operations.** The
operations are the free involution that creates the two faces,
displacement, conservation and chirality; the carry that creates
succession; and the rounding that creates matter and cost.

There is no initial singularity, because there is no initial instant and
no zero at which one could occur.

The universe begins hot because it begins whole, and chiral because the
two faces were never equivalent.

Magnetism is solenoidal from the first operation, and matter has three
tiers by the commitment ladder. Every claim is proved, declared as an
identification, or stated with its refutation condition.

**The remaining volumes carry the same history forward.** **II — The
Dipole** takes the cardioid as the first radiating form, the multipole
ladder of the two faces, and the measured anomalies. **III — First
Particles** populates the pair-maker algebra, derives the charge table
as a uniqueness theorem, and gives the roster. **IV — Plasmas** covers
the cooling ladder and the electroweak epoch. **V — The Birth of
Chemistry** determines the filling order and hydrogen's exact
neutrality. Then come **VI — Early Galaxies**, **VII — The Path to the
Present**, **VIII — Modern Physics** and **IX — Position and
Diffusion**. **X — Relativity and the Standard Model** confronts the
serial substrate with the relativity of simultaneity and records the
outcome.


## References

[1] R. Landauer, *Irreversibility and heat generation in the computing
process*, IBM J. Res. Dev. **5** (1961) 183–191.

[2] C. H. Bennett, *Logical reversibility of computation*, IBM J. Res.
Dev. **17** (1973) 525–532.

[3] E. Midy, *De quelques propriétés des nombres et des fractions
décimales périodiques*, Nantes (1836).

[4] N. Margolus, L. B. Levitin, *The maximum speed of dynamical
evolution*, Physica D **120** (1998) 188–195.

[5] P. A. M. Dirac, *Quantised singularities in the electromagnetic
field*, Proc. R. Soc. Lond. A **133** (1931) 60–72.

[6] MoEDAL Collaboration, *Search results for magnetic monopoles*, Phys.
Rev. Lett. (2019–2022); Particle Data Group, monopole searches review.

[7] N. J. Secrest et al., *A test of the cosmological principle with
quasars*, Astrophys. J. Lett. **908** (2021) L51.

[8] R. Penrose, *Gravitational collapse and space-time singularities*,
Phys. Rev. Lett. **14** (1965) 57; S. W. Hawking, R. Penrose, Proc. R.
Soc. Lond. A **314** (1970) 529.

[9] P. Janot, S. Jadach, *Improved Bhabha cross section at LEP and the
number of light neutrino species*, Phys. Lett. B **803** (2020) 135319 —
N_ν = 2.9963 ± 0.0074, superseding the 2006 LEP value 2.984 ± 0.008 of
Phys. Rep. **427** (2006) 257.

[10] C. Horstmann, *Navier–Stokes: A Solution on Discrete Terms*, Zenodo
(2026), DOI 10.5281/zenodo.21197044.

*All exact claims are pinned by the mechanical test suite accompanying this manuscript and re-verified on every revision. They are the register scan, the two-orders theorem, the involution, the conservation, the incommensurability, the commitment ladder and its depth-three exactness, and the escapement arithmetic.*

<div class="volhead">VOLUME II · THE DIPOLE</div>

*The first form that points — why the dipole is the most widely realized
structure, why the quadrupole is its square, and why the magnetic
monopole will never be found.*

The dipole is the most reproduced structure in the physical universe —
every magnet, every antenna's elementary radiator, every planetary and
stellar field's leading term, the leading anisotropy of the microwave
sky. This volume derives its primacy from the construction of Volume I
and proves the exact statements available. The pointing theorem: the
general first-order directivity pattern is the one-parameter family a +
b·cosθ, the omni-to-dipole mixtures of classical acoustics. Its null
structure is exact: no null when the isotropic part dominates, two nulls
when the directed part dominates, and exactly one null at equal mixture,
which is the cardioid r = 1 + cosθ. Pointing requires a null, and
distinguishing one direction requires exactly one. The cardioid is the
least structure that points, and direction first appears at the equal
mixture of the first two multipoles. The theorem is elementary and
machine-pinned. It explains an engineering fact a century old — that the
cardioid is the universal directional pattern of microphone and antenna
practice — as an instance of a least-action principle rather than a
designer's preference. The ladder and the square: at order m the equal
mixture 1 + cos(mθ) has exactly m nulls. The one-cusp cardioid begins a
ladder whose m-th member is the m-cusp form. At m = 2 the pattern is
identically the square of the dipole term: 1 + cos2θ = 2cos²θ. The
quadrupole face is the dipole face squared. The modern
scattering-amplitudes program arrived at the same structure from the
opposite direction — gravitational amplitudes as the square of gauge
amplitudes, the double copy — and the gravito-electromagnetic factor 4 =
2² is the same square again. The radiation ladder: charge conservation —
the net-zero count written by the first operation of Volume I — forbids
monopole radiation of the charge face. Momentum conservation together
with the equivalence of inertial and gravitational mass forbids dipole
radiation of the mass face. Hence the first lawful radiating multipole
is ℓ = 1 for charge and ℓ = 2 for mass, one rung apart, by the same
first-lawful-move logic that sets the mass gap in the program's
Yang–Mills record. Gravitational waves arriving quadrupole-led are, on
these terms, the mass face radiating at its first lawful multipole: a
count of the conservation laws. The solenoidal face: Volume I derived
∇·B = 0 from the first operation, the circulation face being a closed
orbit with no endpoints. This volume states the consequence as an
asymmetry of falsifiability. Maxwell's theory accommodates a magnetic
monopole, and Dirac showed its consistency and its charge-quantizing
power. The present construction cannot: one confirmed monopole refutes
this series, whereas the standard framework accommodates it. On this
axis the construction is strictly more falsifiable than the received
picture, and every search to date has returned a null result. The
comparison with the sky: the CMB dipole is kinematic, exactly as the
standard treatment gives it. The persistent excess in the number-count
dipole of quasars and radio sources is consistent with a structurally
handed cosmos, and its amplitude remains open. The low-multipole
alignments remain open until the construction uniquely determines a
multipole. Falsification conditions are enumerated; the volume
introduces no free parameter and no continuum object.

## 1 · Introduction

**The form the physical universe repeats most widely across its scales
is the dipole.** It is the elementary radiator of every antenna, the
directional element of every microphone, the leading field of every
magnetized planet and star, and the leading anisotropy of the microwave
background: one form, from the centimeter to the gigaparsec.

**The standard account gives each of these dipoles its own reason.** The
antenna dipole is engineering, the stellar dipole is dynamo dynamics,
and the microwave dipole is kinematics. The absence of the magnetic
monopole, which makes the dipole the *first* magnetic multipole and not
the second, enters Maxwell's equations as an empirical law.

**Volume I derived that the circulation face of the field is a closed
orbit.** It constructed the origin from three operations, and the face
that results is sourceless, endpointless and solenoidal.

**This volume proves three exact theorems about the forms the two faces
can take.** They are the pointing theorem, the cusp ladder, and the
square identity. There is also one structural account: why radiation
begins at ℓ = 1 for the charge face and ℓ = 2 for the mass face.

**The theorems are then compared with observation.** Each observation is
given one of four standings: adopted from the established record,
consistent with the construction, open under a stated condition, or a
refutation condition of the series.

## 2 · The two faces, recalled

**The first operation of Volume I split the period's one structure into
its two Hamiltonian orders.** They are the read order and the
circulation order, the declared electric and magnetic faces. The same
operation produced the displacement pair and its conserved sum:

<div style="text-align:center; margin:12pt 0;">(−18, +18)<span style="float:right;">(1)</span></div>

Two structural facts carry into this volume.

**The circulation face is closed.** It is a cycle with no endpoints and
hence no sources: the solenoidal condition is inherited from the first
operation and is not imposed as a law.

**The count is conserved.** The net zero of the first operation is the
origin of the conservation laws, which belong, by the operation
classification of the Mathematical Companion, to the invertible,
workless side of the construction.

Conservation is what reversible structure cannot change, and radiation
is the first lawful move above it, as Section 5 shows.

## 3 · The pointing theorem

**The general first-order directivity pattern is a one-parameter
family.** It contains every first-order sensor, radiator, and mixture of
an isotropic part with a directed part, and has been standard in
acoustics for a century [1]:

<div style="text-align:center; margin:12pt 0;">D(θ) = a + b·cos θ, &nbsp; a, b ≥ 0<span style="float:right;">(2)</span></div>

**Theorem 1 (pointing).** *The null structure of the family is exact: for a > b there is no null; for a < b there are exactly two; and for a = b there is exactly one, at θ = π. The equal mixture is the cardioid:*

<div style="text-align:center; margin:12pt 0;">r = 1 + cos θ<span style="float:right;">(3)</span></div>

*The cardioid is the unique single-null member of the first-order family.*

**Proof.** Nulls require cos θ = −a/b, soluble only for a ≤ b; strict
inequality gives two solutions per period; equality gives one, at the
antipode. ∎ Machine-pinned across the mixture scan.

**The null count decides what a pattern can distinguish.** A pattern
with no null distinguishes no direction: it receives from everywhere and
points at nothing. A pattern with two nulls distinguishes an *axis* but
not an orientation along it.

| mixture | nulls | what is distinguished |
|---|---|---|
| a > b (isotropic part dominates) | none | no direction — hears everything, points at nothing |
| a < b (directed part dominates) | two | an axis, but not an orientation along it |
| a = b (equal mixture — the cardioid) | exactly one, at θ = π | exactly one direction |

**Exactly one null distinguishes exactly one direction.** The least
structure achieving it is the equal mixture of the first two multipoles,
so direction, as a physical capability, first appears at the cardioid.

**The cardioid's place in engineering is an instance of least action.**
It has been the universal directional pattern of audio and antenna
practice for a century [1]. Engineers, minimizing structure under a
pointing requirement, arrived at the form the construction produces
first.

**The cardioid is the sum of the zeroth multipole and the first in equal
measure.** The zeroth is presence and the first is displacement.
Magnitude and direction are combined in the minimal *vector-like* form,
with its null at the antipode: the direction *not* pointed at is the one
place where the form vanishes.

The first operation of Volume I produced displacement and conservation
together; the first radiating form produces presence and direction in
one curve.

## 4 · The ladder and the square

**Theorem 2 (the cusp ladder).** *At order m the equal mixture*

<div style="text-align:center; margin:12pt 0;">1 + cos(mθ)<span style="float:right;">(4)</span></div>

*has exactly m nulls.* The ladder of least pointing forms runs: one cusp (the cardioid), two cusps, three, m — machine-pinned through m = 5.

**Theorem 3 (the square identity).** *At m = 2 the equal mixture is identically the square of the dipole term:*

<div style="text-align:center; margin:12pt 0;">1 + cos 2θ = 2 cos²θ<span style="float:right;">(5)</span></div>

*The quadrupole face is the dipole face squared.* ∎

**Theorem 3 is a double-angle identity, and physics has reached the same
structure from the opposite direction twice.**

**The first is gravito-electromagnetism.** In the weak-field,
slow-motion limit of general relativity the gravito-electromagnetic
equations reproduce Maxwell's with a factor of 4 = 2² in the
magnetic-type coupling [3].

**The second is the double copy.** The scattering-amplitudes program
found that gravitational amplitudes are, in a precise and generative
sense, the square of gauge amplitudes: the double copy of Bern, Carrasco
and Johansson [4], now a large research program.

**The present construction supplies the statement at the level of the
radiating patterns themselves.** The second face's least pointing form
*is the square* of the first face's directed term.

**The double copy itself remains to be derived from the construction.**
What is established is that a construction with two faces one multipole
apart produces "the next force is the square of the last" as an identity
of first forms. That is the relation the amplitudes program has found
between gauge and gravitational theories.

## 5 · The radiation ladder: why ℓ = 1, why ℓ = 2

**Classical theory states the onset of radiation as two separate
theorems [2, 3].** Electromagnetic radiation begins at the dipole: there
is no monopole radiation, since charge conservation forbids a
time-varying total charge. Gravitational radiation begins at the
quadrupole: no monopole radiation, by mass-energy conservation; no
dipole radiation, by momentum conservation, since the mass dipole's rate
is the total momentum and the equivalence principle leaves nothing to
oscillate against.

**On the present terms the two theorems are one law applied twice.**

**The conserved quantities of each face are its lowest multipole
moments.** Conservation laws belong to the workless face, the invertible
operations of the Companion's classification. The charge face conserves
total charge. The mass face conserves total mass-energy *and* total
momentum, one more conservation, because of equivalence.

**Radiation is the first lawful move above the conserved quantities.**
The same first-rung logic sets the mass gap of the Yang–Mills sector in
this program. The charge face's first lawful radiating multipole is
therefore ℓ = 1; the mass face, with one more conservation, begins at ℓ
= 2 — one rung higher, and the square of Theorem 3 stands at exactly
that rung.

| face | conserved lowest moments | radiation forbidden at | first lawful rung |
|---|---|---|---|
| charge | total charge | monopole | ℓ = 1 |
| mass | total mass-energy *and* total momentum (one more, by equivalence) | monopole and dipole | ℓ = 2 |

**The first gravitational-wave detection was quadrupole-led [5].** That
character was received as a confirmation of geometry. On these terms it
is also a count of the conservation laws: the mass face radiates at
precisely its first lawful rung and no lower.

## 6 · The solenoidal face: strictly more falsifiable

**Volume I derived the solenoidal condition from the first operation:**

<div style="text-align:center; margin:12pt 0;">∇·B = 0<span style="float:right;">(6)</span></div>

This volume states the consequence as an asymmetry of exposure to
refutation.

**In the received picture the solenoidal law is an input.** Dirac proved
[6] that the framework admits its violation: a single monopole is
consistent with quantum electrodynamics and would explain charge
quantization. The received picture is therefore refuted neither by a
monopole nor by its absence.

**Falsification.** The present construction is refuted by one: the
circulation face has no endpoints, so **a single confirmed monopole
refutes this series**. Charge quantization, the fact Dirac's monopole
was introduced to explain, already follows here with no free choice,
because counting is quantized from the first operation.

**On this axis the construction is strictly more falsifiable than the
standard framework.** It forbids something the standard theory permits
and has not observed. Fifty years of searches have returned null results
[7], as the construction requires, and every future search tests this
volume.

**The same property organizes the observed magnetic fields of planets,
stars and galaxies.** That every such field is dipole-led at large
distance is, in the received account, a consequence of dynamo dynamics
together with the absence of monopoles, taken as an input. Here the
absence is a theorem of the origin. The dynamo, a circulation-face
process sustained by the workless transport of conducting flow, is the
mechanism by which the closed face takes the only leading form open to
it.

## 7 · The cosmic confrontation

Each observation has one of four standings: adopted from the established
record, consistent with the construction, open under a stated condition,
or registered as a prediction.

**From the established record.** The dominant dipole of the microwave
sky is kinematic, the observer's motion against the background, and the
construction adds nothing to it.

**Consistent with the construction.** The number-count dipole of distant
quasars and radio sources persistently exceeds the kinematic expectation
in amplitude [8]. A structurally handed cosmos, Volume I's two
inequivalent faces, *expects* a non-kinematic anisotropy component. The
observation agrees with that expectation and does not yet test it,
because no amplitude has been derived. Deriving the amplitude is an open
problem of the series.

**Open, under a stated condition.** The low-multipole anomalies of the
microwave sky, the quadrupole–octopole alignment among them, are held
open. The registered condition is that they bear on the construction
only when it *uniquely determines a specific multipole*. Until then they
are not evidence for it.

**Falsification.** The volume's falsifiable content is §6's: the
monopole. It stands on the series' record alongside Volume I's second
falsification condition (a fourth light generation) and the companion
paper's falsification conditions.

## 8 · Summary

Sections 3 through 5 established the pointing theorem, the cardioid as
the unique single-null form. They established the cusp ladder with its m
nulls at order m, the square identity making the quadrupole face the
dipole face squared, and the net-zero count beneath the radiation floor,
machine-pinned from the first operation. The solenoidal condition is
inherited from Volume I, where it follows from the first operation. The
account adopts from the established record the kinematic CMB dipole and
dynamo dynamics as mechanism. The identification of the radiation floor
with first-lawful-move logic is a reading, as is the connection to the
double copy. The quasar dipole excess is consistent with the
construction, its amplitude open, and the low-multipole alignments
remain open, pending a multipole uniquely determined by the
construction. One confirmed magnetic monopole falsifies the volume — an
asymmetric exposure, since the standard framework accommodates what
refutes this construction — and the volume introduces no free parameter
and no continuum object.

## 9 · Conclusion, and Volume III

**The dipole is everywhere because it is the origin's second step.** The
first step made two faces and a conserved count. The second, the first
form that points, is the equal mixture whose single null distinguishes
one direction in a universe that until then had none.

Above it the ladder rises by squares, the conservation laws set the
first radiating multipoles one rung apart, and the closed face, having
no sources, gives every astronomical magnetic field its dipole lead.

**Volume III, *First Particles*, populates the algebra set out at the
end of Volume I.** That algebra is the width-three register's two
multipliers, the echo pair and the split pair. From it come the exact
charge table, uniquely determined by closure, and the roster of
committed matter: the pre-particle, the neutral twin, and the particle
in three dimensions, each with its open problems named and its
falsification conditions attached.


## References

[1] H. F. Olson, *Acoustical Engineering*, Van Nostrand (1957) —
first-order directional patterns.

[2] J. D. Jackson, *Classical Electrodynamics*, 3rd ed., Wiley (1999).

[3] C. W. Misner, K. S. Thorne, J. A. Wheeler, *Gravitation*, Freeman
(1973); gravito-electromagnetism reviews.

[4] Z. Bern, J. J. M. Carrasco, H. Johansson, *Perturbative quantum
gravity as a double copy of gauge theory*, Phys. Rev. Lett. **105**
(2010) 061602.

[5] B. P. Abbott et al. (LIGO/Virgo), *Observation of gravitational
waves from a binary black hole merger*, Phys. Rev. Lett. **116** (2016)
061102.

[6] P. A. M. Dirac, *Quantised singularities in the electromagnetic
field*, Proc. R. Soc. Lond. A **133** (1931) 60–72.

[7] Particle Data Group, magnetic monopole searches review; MoEDAL
Collaboration results (2019–2022).

[8] N. J. Secrest et al., *A test of the cosmological principle with
quasars*, Astrophys. J. Lett. **908** (2021) L51.

[9] A. Einstein, *Über Gravitationswellen*, Sitzungsber. Preuss. Akad.
Wiss. (1918) 154 — the quadrupole formula.

[10] C. Horstmann, *Navier–Stokes: A Solution on Discrete Terms*, Zenodo
(2026), DOI 10.5281/zenodo.21197044.

*All exact claims — the null-structure scan, the cusp ladder, the square identity, and the conserved count — are pinned by the mechanical test suite accompanying this manuscript and re-verified on every revision.*

<div class="volhead">VOLUME III · FIRST PARTICLES</div>

*The charge table as a theorem, the particle as committed structure, antimatter as the standing complement, and the first quantitative output — three parts hydrogen to one part helium.*

This volume derives the electric charge table of a fermion generation as
the unique solution of a four-constraint linear system, each constraint
a structure of the preceding volumes. Closure: the generation's charges
sum to zero, the requirement known in the standard account as anomaly
cancellation, here inherited from the conserved count of the first
operation. The unit step: weak partners differ by exactly one unit, the
displacement quantum of the first operation. The neutral axis: the
neutrino carries zero. And the triad multiplicity: quarks count three,
leptons one, the construction's single remaining input, fixed by a scan:
of all multiplicities, only three puts the solution on the lattice of
thirds. The unique solution is the observed table: up 2/3, down −1/3,
lepton −1, neutrino 0. Its corollaries are exact — the proton's charge
is +1, the neutron's 0, and hydrogen is exactly neutral. One of the most
precisely verified nulls in physics, |q_p + q_e| < 10⁻²¹ elementary
charges, is therefore a measurement of how well a generation closes. The
particle itself is then constructed, not postulated. In the width-three
register of the committed arithmetic the two natural multipliers act
oppositely. Multiplication by 1001 duplicates a block into an identical
neutral twin, the *echo*. Multiplication by 999 splits it into
complements summing to 999, the *split*. The seed ties the two faces
through one number: 1/7 = 143/1001 exactly, while 143 × 999 = 142857,
the period itself. The chain of states is exact. The *rest* value is
1008 × 1/7 = 144 exactly, calculable and unobservable. The committed
*echo* is 1008 × 0.143 = 144.144, the neutral twin produced by the first
clean rounding, the pre-particle. The *split* is 144 × 999 = 143|856,
complements summing to 999, the charged pair. Antimatter is thereby an
entry in the algebra rather than a missing inventory. The anti-half of
every committed pair is its standing complement, present in the
arithmetic of every particle and not removed by a primordial
annihilation. The baryon-asymmetry problem is re-posed as the question
of which half is manifest, and it remains open. The three generations
are inherited from Volume I as the three clean commitment depths, with
the invisible width of the Z boson (N_ν = 2.9963 ± 0.0074) as their
measurement and a confirmed fourth light generation as their
falsification test. The proton's internal anatomy is computed exactly in
the classic spin-flavour bookkeeping: the up-quarks carry 4/3 of the
spin and the down −1/3, net one and gross five-thirds. The axial charge,
the quantity beta decay measures, is the gross. What the weak
interaction reads is the total third-count of the proton, not its net.
The volume closes with the construction's first quantitative
cosmological output. The seed ratio n/p = 1/7 gives a neutron fraction
of 1/8 and a primordial helium mass fraction of exactly 1/4 — three
parts hydrogen to one part helium — against the measured 0.245 ± 0.003.
The exact quarter is the rest value, and the two-percent deficit is the
perturbation offset: the incompleteness of the burn, since the ratio 1/7
already includes the neutron decay. The standard account derives its own
≈1/7 from freeze-out temperature and weak rates. The construction
carries 1/7 natively as its seed divisor. A dynamical estimate and a
structural constant agree, and Section 6 states both readings of the
agreement. Interaction wiring — all forty-five cells of the
boson-fermion graph from one reading criterion and one attribute table,
including the absent ZZZ vertex — is presented as a compression result,
a retrodiction. Free parameters introduced: none. Continuum objects:
none. Falsification conditions: a fourth light generation; any measured
deviation of quark charges from exact thirds; erosion of the
hydrogen-neutrality bound; the monopole, standing from Volumes I and II.

## 1 · Introduction

**The standard account defines a particle operationally.** It is an
irreducible representation of the Poincaré group, a field quantum, whose
charges and masses enter the theory as measured parameters.

**This volume constructs the particle from the origin of Volumes I and
II and derives its two most basic properties.** The first is the charge
table, as a theorem. The second is the particle's state structure —
rest, echo, split — as exact arithmetic of the committed register. The
volume then reaches the construction's first quantitative cosmological
result: the primordial helium fraction, as one exact fraction and one
correction from the established record.

**The method is that of the series.** What can be proved is proved and
machine-pinned. What must be identified is declared as an entry of the
dictionary. What the dictionary yields is enumerated, and what would
falsify it is stated as a definite condition.

## 2 · The charge table is a theorem

**A generation comprises an up-type quark and a down-type quark, each of
multiplicity m, a charged lepton, and a neutrino.** Four constraints
apply, each a structure of the preceding volumes.

**(C1) Closure.** The generation's total charge vanishes:

<div style="text-align:center; margin:12pt 0;">m·q<sub>u</sub> + m·q<sub>d</sub> + q<sub>e</sub> + q<sub>ν</sub> = 0<span style="float:right;">(1)</span></div>

In the standard account this is the anomaly-cancellation condition
required for quantum consistency [1]. In the present construction it is
inherited — the conserved net-zero count of the first operation (Volume
I), applied to the generation as a unit of commitment.

**(C2) The unit step.** Weak partners differ by exactly one unit:

<div style="text-align:center; margin:12pt 0;">q<sub>u</sub> − q<sub>d</sub> = 1 = q<sub>ν</sub> − q<sub>e</sub><span style="float:right;">(2)</span></div>

The displacement quantum of the first operation: one flip, one unit.

**(C3) The neutral axis.** q<sub>ν</sub> = 0: the neutrino sits on the
axis that never rounds — Volume I's uncommitted residue class.

**(C4) The triad.** m = 3. This is the construction's single remaining
input, and a scan fixes it. Solving the system at every multiplicity m =
1…12, only m = 3 puts the charges on proper thirds: m = 1 gives integer
charges, m = 2 quarters, m = 9 ninths. Machine-pinned.

<div style="page-break-before:always"></div>

**Theorem 1.** *Under C1–C4 the charge assignment is unique:*

<div style="text-align:center; margin:12pt 0;">q<sub>u</sub> = 2/3, &nbsp; q<sub>d</sub> = −1/3, &nbsp; q<sub>e</sub> = −1, &nbsp; q<sub>ν</sub> = 0<span style="float:right;">(3)</span></div>

*Proof:* C3 gives q<sub>ν</sub> = 0; C2 gives q<sub>e</sub> = −1; substituting C2 in C1: 3(2q<sub>d</sub> + 1) − 1 = 0, hence q<sub>d</sub> = −1/3, q<sub>u</sub> = 2/3. ∎

**Corollaries.** Proton (uud): +1. Neutron (udd): 0. Hydrogen (p + e):
0, exactly.

**The neutrality of bulk matter is among the most precisely verified
facts in physics:**

<div style="text-align:center; margin:12pt 0;">|q<sub>p</sub> + q<sub>e</sub>| < 10⁻²¹ elementary charges &nbsp; [2]<span style="float:right;">(4)</span></div>

In the standard account this is an exact equality between a hadron's
composite charge and a lepton's elementary one, which follows when the
anomaly conditions are taken as inputs. Here it is a corollary of
closure: the experiment measures how well a generation closes, and
twenty-one decimal places is its current answer.

**Falsification.** Every quark-charge determination — deep-inelastic structure functions, jet rates, the ratio R of hadronic to muonic cross-sections [3] — is a standing test of the exact thirds; any confirmed deviation falsifies Theorem 1.

## 3 · The particle as committed structure

**In the width-three register the two natural multipliers act
oppositely, and both facts are exact.** This is the algebra set out at
the end of Volume I, in the register of the first clean commitment; this
section populates it.

**Multiplication by 1001 duplicates a block:**

<div style="text-align:center; margin:12pt 0;">×1001: &nbsp; a → a|a<span style="float:right;">(5)</span></div>

The result is an identical twin across the point, with difference zero:
a neutral echo.

**Multiplication by 999 splits a block into complements:**

<div style="text-align:center; margin:12pt 0;">×999: &nbsp; a → (a−1)|(1000−a)<span style="float:right;">(6)</span></div>

The two parts sum to 999: a split pair.

**The seed connects the two multipliers through one number:**

<div style="text-align:center; margin:12pt 0;">1/7 = 143/1001 &nbsp; exactly<span style="float:right;">(7)</span></div>

<div style="text-align:center; margin:12pt 0;">143 × 999 = 142857<span style="float:right;">(8)</span></div>

— the period itself. The committed face and the flowing face of the same object, under the register's two multipliers.

**The chain of states follows from the base 1008.** The base is 42 × 24,
the displaced pair of the first operation as a product, and the atomic
weight of hydrogen in thousandths. Then, exactly:

| state | arithmetic | value | character |
|---|---|---|---|
| **REST** | 1008 × (1/7) | **144** | exact; the rest value — calculable, unobservable |
| **ECHO** | 1008 × 0.143 | **144.144** | the first clean rounding's product: an identical neutral twin — the pre-particle |
| **SPLIT** | 144 × 999 | **143 \| 856** | complements summing 999 — the committed pair |

**Identification.** A particle is a committed pair. The rest value is
structure without commitment — nothing to observe, since observation is
itself a committing operation. The echo is the neutral twin the first
commitment produces. The split is the pair — a member and its complement
— that commitment at the split face yields.

**Antimatter, in this algebra, is the standing complement of every
committed pair.** It is not a missing inventory: the anti-half is
present in the arithmetic of every particle as the 856 to its 143, the
two summing always to the register's ceiling.

**The baryon asymmetry problem is thereby re-posed.** The standard
account must explain why a symmetric creation left an asymmetric
residue. The present account requires something different: an
explanation of why the *manifest* half is the half that is observed,
which is a question about ports and commitment and not about a missing
annihilation.

**Open.** The re-posed question is not a solution. It is one of the
series' open problems.

## 4 · Three generations, counted

**Volume I derived the commitment ladder.** Rounding the seed's period
at the three clean depths — three, four, and five — lifts the carrier
digits to the axis:

<div style="text-align:center; margin:12pt 0;">2 → 3, &nbsp; 8 → 9, &nbsp; 5 → 6 &nbsp; (depths 3, 4, 5)<span style="float:right;">(9)</span></div>

**Identification.** These three commitments are the three fermion
generations. The identification was declared in Volume I, and it is
measurable.

**The invisible width of the Z boson counts the light neutrino
species:**

<div style="text-align:center; margin:12pt 0;">N<sub>ν</sub> = 2.9963 ± 0.0074 &nbsp; [4]<span style="float:right;">(10)</span></div>

On the present terms this number is the count of rounding depths.†

<div class="vnote">† The neutrino count 2.9963 ± 0.0074 is attributed to its source, Janot and Jadach (2020); version 2 cited it to the LEP paper of 2006, whose value is 2.984 ± 0.008.</div>

**Falsification.** A confirmed fourth light generation refutes the
identification, and the volume with it.

**Absolute masses lie outside a dimensionless construction.** By the
dimensional boundary of this program, no dimensionless construction
yields a dimensionful magnitude. Mass *ratios* are within reach and are
the subject of the program's registered predictions; absolute masses
require the one borrowed ruler. It follows that the only parameters the
construction must leave as inputs are the dimensionful ones, which
depend on the unit; the dimensionless parameters are, in principle,
uniquely determined.

## 5 · The proton's anatomy

**The proton's spin content is computed exactly in the standard SU(6)
spin-flavor scheme.** The computation uses the full eighteen-term
wavefunction and is machine-pinned:

<div style="text-align:center; margin:12pt 0;">Δu = 4/3, &nbsp; Δd = −1/3<span style="float:right;">(11)</span></div>

**The two contributions combine in two ways:**

<div style="text-align:center; margin:12pt 0;">net: &nbsp; Δu + Δd = 1<span style="float:right;">(12)</span></div>

<div style="text-align:center; margin:12pt 0;">gross: &nbsp; |Δu| + |Δd| = 5/3<span style="float:right;">(13)</span></div>

The net is the spin the proton shows; the gross is the total third-count in motion.

**The axial charge, the quantity beta decay measures, is the gross.** It
is g<sub>A</sub> = Δu − Δd, and because the signs oppose, g<sub>A</sub>
= 5/3 in this scheme. The same (4 | −1)/3 weights give the magnetic
moments, and the electric charge has the same structure.

| observable | reads | computed value | note |
|---|---|---|---|
| spin | net | 1 | the spin shown |
| axial charge g<sub>A</sub> | gross | 5/3 | measured 1.2753(13) [3], the renormalized value |
| magnetic moments | (4 \| −1)/3 | μ<sub>p</sub> = 1, μ<sub>n</sub> = −2/3 | quark-moment units; the classic ratio −3/2 [5] |
| electric charge | net / gross | 2/3 + 2/3 − 1/3 = 1 | gross 5/3 |

**The weak interaction reads the proton's gross third-count, not its
net.** The value 5/3 is a rest value and 1.2753 is the measured value.†
Throughout this series the rest value is the exact value the
construction fixes, the measured value is what an instrument returns,
and the perturbation offset is their difference. Here the offset is the
strong interaction's renormalization of the axial charge.

<div class="vnote">† The axial coupling is 1.2753(13) in the 2026 listings, one unit of the last place below the value version 2 printed.</div>

## 6 · The first quantitative output: three to one

**The construction's divisor 7, the first complete period of Volume I,
fixes the primordial neutron-to-proton ratio:**

<div style="text-align:center; margin:12pt 0;">n/p = 1/7<span style="float:right;">(14)</span></div>

**The neutron fraction follows, and with every available neutron bound
into helium-4, the helium mass fraction:**

<div style="text-align:center; margin:12pt 0;">(1/7) / (1 + 1/7) = 1/8, &nbsp;&nbsp; Y = 2 × 1/8 = 1/4<span style="float:right;">(15)</span></div>

Three parts hydrogen to one part helium, exactly.

**The measured primordial helium fraction is**

<div style="text-align:center; margin:12pt 0;">Y<sub>p</sub> = 0.245 ± 0.003 &nbsp; [6, 7]<span style="float:right;">(16)</span></div>

**The exact quarter is the rest value, and the two-percent deficit is
the perturbation offset.** The offset is not further neutron decay: the
ratio 1/7 is already the post-decay value at the onset of
nucleosynthesis, the freeze-out ratio standing nearer 1/6, so the decay
is complete before the fraction is formed. The deficit is the
incompleteness of the burn — a small residue of neutrons ends in
deuterium, helium-three and lithium-seven rather than in helium-four —
together with the detail of the reaction network.†

<div class="vnote">† The helium fraction is 0.245 ± 0.003, the recommended value revised in August 2025; version 2 printed an uncertainty of 0.004.</div>

**The standard account derives n/p ≈ 1/7 dynamically, from the
freeze-out temperature and the neutron–proton mass difference [8].**
Within that account the result has no reason to be a simple fraction.
The agreement of a dynamical estimate with a structural constant admits
two readings: either the dynamics arrives at 1/7 by coincidence, or the
dynamics is the perturbation about a rest value the construction carries
natively. Both readings are stated, and the accumulating record of the
series decides between them.

## 7 · The wiring, compressed

**The entire interaction graph of the standard roster is generated by
one criterion over one attribute table.** The graph has forty-five
cells: which of the nine field species couple to which, including every
absence. The attribute table's electric column is the output of Theorem
1.

**An edge exists where one leg *reads* a property the other *carries*.**
A self-loop exists where a carrier reads what it itself carries.

**The known absences are generated and not stipulated.** There is no
photon–photon coupling, no tree-level photon–Higgs coupling, no
Higgs–neutrino coupling (the never-committing class), and no ZZZ vertex:
the Z, carrying net zero of the property it reads, cannot read itself.

**The wiring requires the same single input as the charge table.**
Deleting the color attribute deletes exactly two cells, so the wiring
layer rests on C4's triad, as the content layer does.

**The result is a retrodiction: a compression of known structure.** Its
weight is its economy: one rule, one table, forty-five cells, no
exceptions.

## 8 · Summary

Sections 2 through 7 established the charge table as a uniqueness
theorem, with hydrogen's exact neutrality as its measured corollary.
They established the multiplicity scan that fixes the triad, the
pair-maker identities and the chain of states, and the proton's
spin-flavour anatomy — net 1, gross 5/3. They established the abundance
arithmetic 1/7 → 1/8 → 1/4, and the generation of the interaction
wiring, a retrodiction. The account adopts from the established record
the renormalization of g<sub>A</sub> and the reaction-network correction
to the helium fraction. It takes the particle as a committed pair and
the generations as commitment depths, both declared identifications,
with the two faces inherited from Volume I. The baryon asymmetry,
re-posed as an accounting question, remains open. A fourth light
generation, any measured deviation of the quark charges from exact
thirds, erosion of the hydrogen-neutrality bound, or a confirmed
magnetic monopole falsifies the volume. Free parameters introduced:
none; continuum objects: none; the single input is the triad, fixed by
the scan.

## 9 · Conclusion, and Volume IV

**A particle, on discrete terms, is a committed pair.** It has an exact
rest value that is never observed, first appears as a neutral echo at
the first clean rounding, and splits into a member and its standing
complement at the register's other face.

Its charge is a theorem, and its neutrality in atoms a corollary
measured to twenty-one decimal places. Its generations are counted by
the invisible width of the Z boson. Its first cosmological consequence,
three parts hydrogen to one part helium, is an exact fraction with a
perturbation offset of two percent.

**Volume IV, *Plasmas*, takes the inventory into the cooling ladder.**
It treats the octave descent as thermal history, the electroweak epoch
in which the masses of the two carriers stand one whole tone apart, and
the long opacity that ends at recombination.


## References

[1] C. Q. Geng, R. E. Marshak, *Uniqueness of quark and lepton
representations in the standard model from the anomalies viewpoint*,
Phys. Rev. D **39** (1989) 693; K. S. Babu, R. N. Mohapatra, Phys. Rev.
D **41** (1990) 271.

[2] G. Bressi et al., *Testing the neutrality of matter by acoustic
means in a spherical resonator*, Phys. Rev. A **83** (2011) 052101.

[3] F. Takahashi et al. (Particle Data Group), *Review of Particle
Physics*, Int. J. Mod. Phys. A **41** (2026) 2630011 — quark charges
from the R ratio, deep-inelastic scattering and jet observables; the
neutron's axial coupling, λ = −1.2753 ± 0.0013.

[4] P. Janot, S. Jadach, *Improved Bhabha cross section at LEP and the
number of light neutrino species*, Phys. Lett. B **803** (2020) 135319,
on the measurement of the ALEPH, DELPHI, L3, OPAL and SLD
Collaborations, Phys. Rep. **427** (2006) 257.

[5] F. Halzen, A. D. Martin, *Quarks and Leptons*, Wiley (1984) — SU(6)
spin-flavor bookkeeping, g_A and μ_p/μ_n.

[6] B. D. Fields, P. Molaro, S. Sarkar, *Big Bang nucleosynthesis*, in
[3], revised August 2025 — the recommended value Y_p = 0.245 ± 0.003.

[7] Planck Collaboration, *Planck 2018 results VI: cosmological
parameters*, Astron. Astrophys. **641** (2020) A6.

[8] E. W. Kolb, M. S. Turner, *The Early Universe*, Addison-Wesley
(1990) — the standard n/p ≈ 1/7 freeze-out computation.

[9] C. Horstmann, *Navier–Stokes: A Solution on Discrete Terms*, Zenodo
(2026), DOI 10.5281/zenodo.21197044.

*All exact claims are pinned by the mechanical test suite accompanying this manuscript and re-verified on every revision. They are the four-constraint solution and its corollaries, the multiplicity scan, the pair-maker identities, the chain of states, the abundance arithmetic, the proton anatomy, and the wiring generation.*

<div class="volhead">VOLUME IV · PLASMAS</div>

*Temperature without Kelvin, the electroweak epoch one whole tone wide, the held chord of the plasma age, and transparency as a theorem about charge.*

The universe passed its first four hundred thousand years as plasma —
charge unbound, light coupled to matter, structure impossible. This
volume states what that age is on discrete terms and proves what can be
proved. Temperature without kelvin: on a counting substrate, cooling is
octave descent. The scale-step is the halving, and the
renormalization-per-octave of the companion program is the thermal
history's own clock. Temperature enters as a ratio of scales, and
exactly one dimensioned anchor is borrowed, the measured microwave
background at 2.725 K. After that every epoch is an octave count, and
the span from the electroweak scale to the microwave background is fifty
octaves, machine-checked. The volume therefore needs no separate account
of reheating or of an initial temperature. The universe begins whole
(Volume I) with its full spectral content, and the plasma age is the
long descent of that content down the octave ladder. The electroweak
epoch: the two faces of the field acquire their heavy carriers with
masses one whole tone apart in the leading term. The registered
expression is (m_W/m_Z)² = (8/9)² − 13/1000, so that m_Z/m_W = 9/8
before the correction term. The full expression stands half a cent above
the 2026 world-average mass ratio: 24 MeV in the W mass, 3.1 standard
deviations, and the registry of predictions lists it as in tension. It
is refuted if the W mass resolves at the high value of the CDF
measurement. The held chord: the plasma age itself is the occupancy of
the near-closed seam 63/32 = 2 − 1/32, one part in sixty-four short of
the octave. Its gap to closure is exactly the septimal comma 64/63,
twenty-seven cents, the same comma the program's Higgs self-coupling
construction carries. Matter ionized, light coupled, the chord held one
comma short of resolution for four hundred thousand years. Recombination
as a corollary: the age ends, and the universe becomes transparent,
because hydrogen is exactly neutral — Volume III's closure corollary,
measured to twenty-one decimal places. Transparency is not an accident
of cross-sections. Light decouples because the committed form of matter
carries zero residual charge, and a universe whose generations closed
inexactly would scatter forever. The released chord is the microwave
background, a blackbody to fifty parts per million, because what is
released is the complete mode population of a single held structure,
present whole from the first division and released at once. The standard
dynamics of the epoch — Saha ionization balance, the acoustic
oscillations, the details of decoupling — are adopted whole from the
standard account as the dynamics that play out on this structure. The
structure itself is the volume's content: the octave clock, the
whole-tone split, the held seam, the exact neutrality. Free parameters
introduced: none. Continuum objects: none. Falsification conditions: the
electroweak prediction (registered, and in tension at 3.1 standard
deviations); a measured residual charge on hydrogen; and the volume's
identifications stand or fall with the series' dictionary.

## 1 · Introduction

**Between the first particles of Volume III and the first structures of
Volume VI lies the plasma age, the longest uneventful interval in cosmic
history.**

**The standard account describes the plasma age with high precision and
takes its three boundary facts as given.** It computes ionization
fractions, acoustic oscillations and the Thomson opacity. The boundary
facts are three. The epoch's *entry* is marked by two heavy carriers
with a particular mass ratio. The epoch *persists* as a long metastable
plateau. Its *exit*, recombination and transparency, is total, sudden on
cosmic timescales, and final.

This volume derives the form of all three from the construction, adopts
the intervening dynamics from the standard account, and attaches the
falsification conditions.

## 2 · Temperature without Kelvin

**On a counting substrate temperature is not primitive.** The volume
begins with what replaces it.

**Cooling is octave descent.** The natural scale-step of a
doubling-based register is the halving, and the renormalization per
octave of the companion records is the thermal history's own clock: a
coupling's change per octave is its change per step of cosmic cooling.

**Temperature enters only as a ratio of scales.** The construction
borrows exactly one dimensioned anchor, the measured temperature of the
microwave background:

<div style="text-align:center; margin:12pt 0;">T = 2.725 K &nbsp; [1]<span style="float:right;">(1)</span></div>

After the anchor, every epoch is an octave count.

**The count from the electroweak scale to the microwave background is
fifty octaves.** Taken from the vacuum expectation value, 246 GeV, to
the background's thermal energy, it is 49.9, machine-checked in the
comparison layer:

<div style="text-align:center; margin:12pt 0;">electroweak scale → microwave background &nbsp;=&nbsp; 50 octaves<span style="float:right;">(2)</span></div>

The entire history from the heavy carriers to the relic light is fifty halvings of scale.

**No reheating is required.** The universe begins whole (Volume I), with
its complete spectral content, and cools by descending its own ladder.

The kelvin, like every unit in this program, comes from outside the
arithmetic: one borrowed ruler, declared.

## 3 · The electroweak epoch: one whole tone

**The plasma age opens with the electroweak commitment.** The two faces
of the field acquire their heavy carriers.

**Prediction.** The construction's statement about that epoch is exact,
and it is the program's registered electroweak prediction [6]:

<div style="text-align:center; margin:12pt 0;">(m<sub>W</sub>/m<sub>Z</sub>)² = (8/9)² − 13/1000<span style="float:right;">(3)</span></div>

**The leading term alone gives**

<div style="text-align:center; margin:12pt 0;">m<sub>Z</sub>/m<sub>W</sub> = 9/8<span style="float:right;">(4)</span></div>

The two carriers stand one whole tone apart: the ratio 9/8 is the whole
tone of just intonation. The *cent*, used throughout, is the standard
logarithmic measure, 1200 per octave.

**The coefficient of the correction term is a gap of the seed's
near-miss ladder.** Volume I introduced the ladder: 1, 5, 17, 13, 139.
The gap is 13, placed at the third register:

<div style="text-align:center; margin:12pt 0;">13 = 2⁸ − 3⁵<span style="float:right;">(5)</span></div>

**The angle of the leading term is the ladder's gap 17 over its own
power:**

<div style="text-align:center; margin:12pt 0;">sin²θ = 17/81 = (3⁴ − 2⁶)/3⁴<span style="float:right;">(6)</span></div>

**Against the 2026 world-average masses [4] the full expression stands**

<div style="text-align:center; margin:12pt 0;">+0.5 cents — 24 MeV in the W mass, 3.1 standard deviations<span style="float:right;">(7)</span></div>

The registry of predictions lists the commitment as in tension [6]. Its
registered alternative, with 1/75 in place of 13/1000, stands 0.9
standard deviations above the same average.†

<div class="vnote">† The electroweak expression stands 3.1 standard deviations above the 2026 world-average W mass, where version 2 quoted 1.3 on the 2024 average.</div>

**Falsification.** The prediction stands in the registry with its
falsification condition. The 2026 world average is formed without the
CDF measurement, which lies well above it. A resolution of the W mass at
the CDF value refutes the expression and its alternative alike, and a
measurement to ±5 MeV decides between the two.

**The identification of the whole-tone structure with the electroweak
ratio is the program's.** The *arithmetic* — the leading term, the
ladder gaps, the correction term — is exact and machine-pinned, and the
prediction is registered with its date.

## 4 · The held chord: one comma short of closure

**The plasma age lasts because the epoch occupies a near-closed seam.**

**The construction's metastable interval is**

<div style="text-align:center; margin:12pt 0;">63/32 = 2 − 1/32<span style="float:right;">(8)</span></div>

— one part in sixty-four short of the octave.

**Its gap to closure is exactly the septimal comma.** The comma is about
27.3 cents, machine-pinned, and it is the same comma the program's Higgs
self-coupling construction carries:

<div style="text-align:center; margin:12pt 0;">64/63 ≈ 27.3 cents<span style="float:right;">(9)</span></div>

**The chord is held one comma short of resolution.** Matter is ionized,
light is coupled, and the structure is suspended. A system one small
exact interval from closure does not drift shut: it requires the closing
condition, which is the subject of the next section.

**Identification.** The plasma plateau is identified with the held seam,
as an entry of the dictionary; the seam itself, its gap, and the comma's
identity are exact.

## 5 · Recombination: transparency is the charge theorem

**The age ends when the temperature descends past the binding of
hydrogen and the plasma commits into atoms.**

**The standard account computes the kinetics in detail [2] and assumes
one fact.** The fact is that the resulting atom is *neutral enough to
matter*: that a universe of freshly formed hydrogen stops scattering
light.

**That fact is not kinetic.** It is **Volume III's closure corollary:
hydrogen is exactly neutral**, because a generation's charges sum to
zero as a theorem — and the experimental bound stands at

<div style="text-align:center; margin:12pt 0;">10⁻²¹ elementary charges<span style="float:right;">(10)</span></div>

**Identification.** Transparency is the charge theorem, observed at
cosmological scale.

**Recombination is final because closure is exact.** A universe whose
generations closed inexactly — residual charge at any level a few orders
above the current bound — would remain opaque to its own relic light,
and no astronomy would exist to read it. This is the construction's
explanation of the epoch's *totality*.

**What is released is the held chord entire.** It is the complete mode
population of a single suspended structure, present whole from the first
division of Volume I and released at once at commitment.

**The relic is therefore a nearly perfect blackbody:**

<div style="text-align:center; margin:12pt 0;">deviations below fifty parts per million &nbsp; [3]<span style="float:right;">(11)</span></div>

**Reading.** The standard account attributes the perfection to efficient
thermalization. This account adds that the spectrum is the release of
*one* structure and not the sum of many histories. The FIRAS measurement
is consistent with both.†

<div class="vnote">† The bound of fifty parts per million is Fixsen et al. (1996); version 2 cited it to the paper of 1994.</div>

## 6 · Summary

Sections 2 through 5 established the octave clock: fifty halvings from
the electroweak scale to the relic light, with the Kelvin as the one
borrowed ruler. They established the whole-tone split of the heavy
carriers, the near-closed seam 63/32 with its septimal-comma gap, and
transparency as the observed form of exact hydrogen neutrality. The
account adopts the standard treatment for the intervening dynamics — the
Saha ionization balance, the acoustic oscillations of the coupled fluid,
the visibility function and the details of decoupling. It takes from
Volume I the identification of the hot beginning with a complete
spectrum. Two predictions stand on record: the electroweak mass ratio,
registered, dated, and 3.1 standard deviations above the 2026 world
average; and the exact neutrality of hydrogen, whose bound continues to
be tested. One question remains open — whether the held chord's harmonic
anatomy determines any feature of the acoustic peak spectrum; the
derivation remains to be made. A W-mass resolution at the CDF value
falsifies the electroweak expression, a measured residual charge on
hydrogen falsifies the closure corollary, and the volume's readings
stand or fall with the series' dictionary at large.

**Free parameters introduced: none. Continuum objects: none.**

## 7 · Conclusion, and Volume V

**The plasma age, on discrete terms, has an entry, a duration and an
exit.** It is entered through a commitment whose carriers stand one
whole tone apart. It is sustained as a chord held one septimal comma
short of closure. It is ended by the one exactness the construction
guarantees, the neutral atom, and it leaves a blackbody whose perfection
marks a single released structure. The span is fifty octaves from the
carriers to the relic, with one borrowed kelvin and no adjustable
number.

**Volume V, *The Birth of Chemistry*, takes the newly transparent
universe into the periodic table.** It derives the entire
orbital-filling order, including both of its anomalies, from one root
and two exact multipliers: chemistry's ordering derived before chemistry
exists.


## References

[1] D. J. Fixsen, *The temperature of the cosmic microwave background*,
Astrophys. J. **707** (2009) 916 — T = 2.72548 ± 0.00057 K.

[2] P. J. E. Peebles, *Recombination of the primeval plasma*, Astrophys.
J. **153** (1968) 1; Ya. B. Zel'dovich, V. G. Kurt, R. A. Sunyaev, Sov.
Phys. JETP **28** (1969) 146.

[3] D. J. Fixsen et al., *The cosmic microwave background spectrum from
the full COBE FIRAS data set*, Astrophys. J. **473** (1996) 576 — rms
deviations below 50 parts per million of the peak; the first full
spectrum is J. C. Mather et al., Astrophys. J. **420** (1994) 439.

[4] F. Takahashi et al. (Particle Data Group), *Review of Particle
Physics*, Int. J. Mod. Phys. A **41** (2026) 2630011 — m<sub>W</sub> =
80.3625(77) GeV, m<sub>Z</sub> = 91.1879(20) GeV.

[5] G. Bressi et al., Phys. Rev. A **83** (2011) 052101 — the neutrality
of matter.

[6] C. Horstmann, *Predictions on Discrete Terms*, Zenodo (2026), DOI
10.5281/zenodo.21206818 — commitment 6, the electroweak pair.

[7] C. Horstmann, *Navier–Stokes: A Solution on Discrete Terms*, Zenodo
(2026), DOI 10.5281/zenodo.21197044.

*All exact claims — the held chord and its comma, the cooling span, the electroweak skeleton, and the neutrality corollary — are pinned by the mechanical test suite accompanying this manuscript (`test_genesis_iv.py`) and re-verified on every revision.*

<div class="volhead">INTERLUDE · THE FORCES, IN ORDER OF APPEARANCE</div>

*Where each interaction enters the unfolding — and why gravitation is not a fourth force among equals but the register's reference level: the tonal center, defined before anything sounds and confirmed when the first sustained tone begins.*

The received account lists four fundamental interactions side by side
and assigns them no order of appearance. The preceding volumes date
three of them, each in its own place, and the companion record on
gravitation derives the mechanism of the fourth. This interlude states
the order. Electromagnetism enters first, at Volume II's dipole: the two
faces exist from the first involution, radiation begins at ℓ = 1, and no
mass is required — first light precedes all weight. The strong sector
enters at commitment: Volume III's committed structure, whose
confinement completes the hadron's rest tick. The weak sector is the
operation between provenances — the transform's ±18 face, one flip
moving one unit — and its musical form, the authentic cadence, is
derived in the companion record on tonal function. Gravitation is
different in kind. The register's reference level — the fixed stratum,
the tonal center — is present from the first division, unsounded; a
tonal center is precisely the reference that need not be sounded in
order to organize what is sounded. What carries a date is gravitation's
relation with matter, which begins at the acquisition of a rest
frequency: at Volume IV's electroweak epoch — one whole tone — for
elementary matter, and at confinement for the hadrons. Before the first
rest clock, everything moves at the one rate and the key is unconfirmed;
after it, the deficit organizes everything that ticks. The order —
light, tone, operation, and only then weight — follows from the
construction with no free choice, and its exact claims are verified in
the public suite.

## 1 · Introduction

**These volumes use gravitation from the early galaxies onward without
stating where it enters.** Volume VI bounds collapse with it, Volume II
counts its radiation rung, and Volume X reads its time dilation as
budget consumption. In the received account the four interactions stand
side by side, none prior to another, and the question of which appears
first is not posed. On discrete terms it is well posed, and this
interlude answers it.

**The companion record on gravitation derives the mechanism in full
[1].** It gives the closure deficit as the potential, the inverse-square
law from the count of the nines, the coupling as an exact reciprocal,
and universality as one count read twice. Seventeen conditions of
refutation are stated there, and the claim map is public. The interlude
imports those results by citation. Its own content is the order of
appearance, which belongs to this book because the unfolding is this
book's subject.

## 2 · First light: the charge face at the dipole

**Volume II established that the charge face radiates from ℓ = 1.** The
involution's two faces, the read face and the circulation face, exist
from the first operation, and the first structure points.
Electromagnetic radiation begins at ℓ = 1, the dipole, because only the
total charge is conserved on the charge face; the monopole is forbidden
and predicted absent.

**Electromagnetism is present from the first carry: first light precedes
all weight.** Nothing in that construction requires mass. The charge
face and its radiation are available before any rest frequency exists
anywhere in the unfolding.

## 3 · The first sustained tones: the strong sector at commitment

**Volume III established that matter is commitment: what persists is
what has been rounded.** The hadrons are committed structure, of which
the proton's anatomy is that volume's example, and confinement is the
condition under which the committed parts hold one rest tick in common.

**The strong sector enters when the first structures commit and hold.**
A sustained tone is a rest frequency held: this is the sector of the
first sustained tones, and its scale is set where the hadron's tick
completes.

## 4 · The operations between tones: the weak sector

**The weak sector is the operation that changes provenance.** Weak
partners differ by exactly the unit — the transform's ±18 face, one flip
moving one unit — so the weak sector is not a tone but a move between
tones. Its musical form is the cadence, and the companion record on
tonal function [3] derives the authentic cadence's count exactly: one
unit of each generator, applied in contrary motion.

## 5 · The reference level: gravitation as the tonal center

**The register's fixed stratum holds the office of a tonal center.** A
tonal center is the degree against which every other degree is heard as
displaced — the reference that need not be sounded in order to organize
what is sounded. It is the point of repose toward which unstable degrees
resolve, and the one degree that cannot itself be the object of that
resolution. The companion record [1] derives the consequences: the
deficit at the reference is the gravitational potential, and the pull is
the arithmetic of falling short of it.

**The relation of gravitation with mass begins at the acquisition of a
rest frequency.** The reference level is present from the first
division, unsounded, and the field acts throughout. Radiation responds
to it — the companion record's classical tests include the bending of
light — and the radiation era's expansion is gravitational dynamics with
no rest clock anywhere in it. The relation with mass begins at Volume
IV's electroweak epoch, one whole tone, for the elementary masses, and
at Volume III's confinement for the hadrons. This is why the coupling is
to mass and the acceleration is universal: the gravitational charge and
the inertial mass are one count read twice [1], a statement the
MICROSCOPE mission bounds at parts in 10¹⁵ [2].

**The deficit has one sign, so the pull cannot be screened.** Volume
II's ladder already counted the radiation rung: the mass face begins at
ℓ = 2, one conservation higher than light. The coupling is the exact
reciprocal α_G(e) = 5/(2¹⁵¹ − 1), and the value of G it gives lies 106
parts per million below the CODATA centre, inside the unresolved spread
of the experiments; convergent metrology decides it [1]. Volume X's
reading — the equivalence principle as a bookkeeping identity, dilation
as consumption — stands as a reading, and its derivation is on the
public record with it.

## 6 · The order, and what it carries

**The order is light, tone, operation, and then weight.** Light comes
first, from the first carry, massless and pointing. Tone is second, at
commitment, when the first rest clocks start. The operations between
tones occur wherever provenance changes. Weight is last, and not because
gravitation arrives late: the tonal center was never absent, it was
unsounded, and the first sustained tone is what confirms the key.
Structure follows — Volume VI's galaxies are what the pull does once it
has matter to organize — and the volumes after this interlude use
gravitation with its entry stated.

**The order carries four conditions, inherited from the companion
record.** There is no monopole and no dipole gravitational radiation:
the rung count of Volume II, confirmed at the first detection. There is
no screening of the pull. There is no composition dependence of free
fall and no clock-species dependence of the redshift. Any confirmed
violation refutes the account outright, with no parameter available to
absorb it [1]. The unfolding of these volumes is a musical order: first
light, then tone, then cadence, then the key that had organized all of
it from the first.

## References

[1] C. Horstmann, *Gravity on Discrete Terms*, Zenodo (2026), DOI
10.5281/zenodo.22087599 — the mechanism, the coupling, the seventeen
conditions, and the public claim map.

[2] P. Touboul et al. (MICROSCOPE Collaboration), *MICROSCOPE mission:
final results of the test of the equivalence principle*, Phys. Rev.
Lett. **129** (2022) 121102.

[3] C. Horstmann, *Tonal Function on Discrete Terms*, Zenodo (2026), DOI
10.5281/zenodo.22119146 — the count of the authentic cadence.

*All exact claims of this interlude — the coupling's reciprocal, the placement of G, the radiation rungs, and the order's cross-references — are pinned by the mechanical test suite accompanying this manuscript (`test_the_forces_interlude.py`) and re-verified on every revision.*

<div class="volhead">VOLUME V · THE BIRTH OF CHEMISTRY</div>

*The entire orbital-filling order of the periodic table — both anomalies included, the noble gases as corollary, ending exactly at element 118 — from one root and two exact ratios, with zero chemistry input.*

Chemistry's deepest regularity is an ordering: the sequence in which the
orbitals of the atom fill — 1s, 2s, 2p, 3s, 3p, 4s, 3d, … — the aufbau
that generates the periodic table's entire architecture. The standard
account states this order as an empirical rule — Madelung's: increasing
n+ℓ, ties broken by n. It derives that rule only approximately from
many-electron numerics. It treats the two best-known irregularities — 4s
filling before 3d, and 4f before 5d — as effects of screening, computed
case by case. This volume states a theorem. Assign to each orbital (n,
ℓ) the exact rational value V(n, ℓ) = 1296 · (2/3)^⌊(n−ℓ−1)/2⌋ ·
(5/6)^(2ℓ + ((n−ℓ−1) mod 2)). The root 1296 = 6⁴ is the fourth power of
the seed's product, and the two multipliers are the exact ratios 2/3 and
5/6. Then the nineteen orbitals from 1s through 7p, ranked by descending
value, reproduce the empirical filling order term for term. Both
anomalies are automatic strict inequalities of exact fractions — 4s =
720 > 625 = 3d, and 4f = 15625/36 > 1250/3 = 5d — requiring no screening
argument, no numerics, and no chemistry input of any kind. The odd
s-orbitals 1s, 3s, 5s, 7s land at the perfect-square ranks 1, 4, 9, 16.
Madelung's own (n+ℓ, n) rule holds across the entire ranking as a
consequence rather than a postulate. Filling each ranked orbital to its
standard capacity 2(2ℓ+1) yields the noble-gas numbers as cumulative
sums at the p-closures: 10, 18, 36, 54, 86 and 118, neon through radon.
The ladder's final rung lands exactly on oganesson, the last noble gas
the laboratory has reached and the natural terminus of the periodic
table as known. Every value is an exact fraction; every comparison is
machine-pinned; the entire result is re-derived from the closed form in
the public suite. The volume then places the result in the series'
architecture. Chemistry exists at all because hydrogen is exactly
neutral, Volume III's closure corollary: bonding is the physics of
exactly-cancelled monopoles, which is why the residual forces are weak
enough for molecules to persist. The ordering exists before any atom
does, in the same sense the reptend exists before any division is
performed — the aufbau is a fact about the register, inherited by matter
at commitment. The orbital picture itself, the capacities 2(2ℓ+1), and
the quantitative energetics belong to standard quantum mechanics. The
known ground-state configuration exceptions (chromium, copper and their
homologues) belong to the inter-electron dynamics, perturbations about
the order and not violations of it. The multiplier pair (2/3, 5/6) is a
declared selection, stated with its least-action note, and its
justification is the economy of the result: nineteen terms, two
anomalies, six noble gases, one closed form. Free parameters: none.
Continuum objects: none.

## 1 · Introduction

**The periodic table rests on an ordering.** Electrons fill the atom's
orbitals in a sequence, the aufbau, that every element follows. It runs
1s, 2s, 2p, 3s, 3p, then the first anomaly (4s before 3d), the d-block,
and the second anomaly (4f before 5d), which places the lanthanides in
their separate row beneath the table.

**Madelung's rule summarizes the sequence [1].** Order by n + ℓ, and
break ties by n.

**The standard account attributes the rule to many-electron screening.**
Why the rule holds, and why it departs from the energy ordering of the
hydrogen atom, is computed numerically system by system, with the
anomalies as case studies [2].

**This volume replaces the rule with a theorem.** One exact closed form
on the quantum numbers has a magnitude ranking that *is* the sequence:
both anomalies, the lanthanide row, the noble gases and the end at
element 118.

## 2 · The theorem

**Definition.** For an orbital with principal number n and angular number ℓ, let k = n − ℓ − 1 (the radial count), and define the exact rational

<div style="text-align:center; margin:12pt 0;">V(n, ℓ) = 1296 · (2/3)^⌊k/2⌋ · (5/6)^(2ℓ + (k mod 2))<span style="float:right;">(1)</span></div>

**The root is 1296 = 6⁴, the fourth power of the seed pair's product.**
The two multipliers are the exact ratios 2/3 and 5/6. Nothing else
enters.

**Theorem 1 (the aufbau).** *The nineteen orbitals 1s through 7p, ranked by descending V, reproduce the empirical filling order term for term:*

<div style="text-align:center; margin:12pt 0;">1s · 2s · 2p · 3s · 3p · <strong>4s · 3d</strong> · 4p · 5s · 4d · 5p · 6s · <strong>4f · 5d</strong> · 6p · 7s · 5f · 6d · 7p<span style="float:right;">(2)</span></div>

*with both anomalies automatic as strict inequalities of exact fractions.*

**The first anomaly is an inequality of integers:**

<div style="text-align:center; margin:12pt 0;">4s = 720 > 625 = 3d<span style="float:right;">(3)</span></div>

**The second is an inequality of exact fractions:**

<div style="text-align:center; margin:12pt 0;">4f = 15625/36 > 1250/3 = 5d &nbsp; (434.03 > 416.67)<span style="float:right;">(4)</span></div>

*Moreover the odd s-orbitals stand at the perfect-square ranks, the
square spine:*

<div style="text-align:center; margin:12pt 0;">1s, 3s, 5s, 7s &nbsp; at ranks &nbsp; 1, 4, 9, 16<span style="float:right;">(5)</span></div>

 *Madelung's (n + ℓ, n) rule holds across the entire ranking as a
consequence.*

The ranking, the anomalies, the square spine and the rule are each
pinned by a named test.

**The theorem concerns an explicit function of the quantum numbers.**
Any decreasing list of nineteen numbers can be labeled in filling order,
and the theorem is not that. One root and two fixed ratios, with no case
analysis, generate the order, including the two places where it departs
from the hydrogenic ordering. In the standard account those two places
require a screening computation each; here each is a comparison of
fractions.

**Corollary (the noble gases).** Fill each ranked orbital to its standard capacity 2(2ℓ + 1). The cumulative counts at the p-shell closures are exactly

<div style="text-align:center; margin:12pt 0;">10 · 18 · 36 · 54 · 86 · 118<span style="float:right;">(6)</span></div>

— neon, argon, krypton, xenon, radon, **oganesson** — with helium's 2 closing the first s-shell.

**The ladder's nineteenth rung completes at 118.** That is oganesson,
the last noble gas the laboratory has reached [3] and the end of the
periodic table as known. The form does not stop there: extended, it
ranks 8s, 5g, 6f and onward, exactly as Madelung's rule does. So 118 is
where the laboratory has reached, not a boundary the construction
imposes.

## 3 · Why chemistry exists at all

**Chemistry requires neutral atoms, and neutrality is the closure
theorem of Volume III.** An ordering of orbitals would have no
consequence if atoms could not form stable, interacting, *neutral*
systems. Hydrogen is exactly neutral because a generation's charges
close as a theorem, verified to twenty-one decimal places.

**Chemistry is the physics of exactly cancelled monopoles.** Because the
atom's net charge is zero to closure, what remains between atoms are the
residual forces — dipoles, dispersion, exchange — weak enough that
molecules persist under thermal motion and strong enough to bind.

A universe with approximate closure, at any level orders of magnitude
above the current bound, has no chemistry: bare monopole forces disrupt
molecular structure.

**Three results secure three features of the periodic table:**

| of the periodic table | secured by |
|---|---|
| its *existence* | the closure theorem (Volume III) |
| its *architecture* | Theorem 1 |
| its *terminus* | the corollary |

**Reading.** The ordering is a fact about the register — exact
fractions, ranked — inherited by matter at commitment, in the same sense
that the reptend exists before any particular division is performed. The
order of the periodic table is fixed before the first atom forms.

## 4 · What is adopted, and the selection weighed

**From the established record.** Standard quantum mechanics supplies, in full: the orbital picture itself; the capacities 2(2ℓ+1) — angular momentum degeneracy times spin; and the quantitative energetics of many-electron atoms.

**The ground-state configuration exceptions belong to the inter-electron
dynamics.** In chromium, copper and their heavy homologues,
near-degenerate configurations exchange single electrons. These are
perturbations about the filling *order* and not violations of it, and
the standard references classify them so as well [2].

**The multiplier pair (2/3, 5/6) is a declared choice.**

**By least action, the pair is the two smallest descents available from
the seed's material.** 2/3 is the seed ratio itself, the construction's
most primitive step, and 5/6 is the unit-fraction step adjacent to it;
each multiplier is a superparticular descent.

**The pair is justified by the economy of the result, and it is not
uniquely determined.** That economy is nineteen terms, two anomalies,
the square spine, Madelung's rule as a consequence, six noble gases, and
the closure at 118, from one root and two ratios.

**Two fixed ratios yield more than twenty ordered facts.** The structure
is *ordinal*: its only degrees of freedom are the two ratios, used
identically at every rung.

**The exponent pair carries Madelung's rule.** For each of the nineteen
orbitals

<div style="text-align:center; margin:12pt 0;">2A + B = n + ℓ − 1<span style="float:right;">(7)</span></div>

exactly, and within each group of fixed n + ℓ the exponent A increases with n. The magnitude ranking is therefore ordered first by n + ℓ and then by n, which is Madelung's rule. That holds whenever the two ratios stand in the relation r₁ ≈ r₂², with a residual too small to overturn the primary key. The seed's pair stands in it exactly: (2/3) ÷ (5/6)² = 24/25.

**The seed's pair is the least member of a family of ratios that give
the ordering.** Write the pair as r₁ = m/(m+1) and r₂ = (2m+1)/(2m+2).
The residual is then 4m(m+1) over 4m(m+1) + 1, superparticular at every
m. The ordering holds from m = 2, checked through m = 9. It fails at m =
1, where the residual is 8/9 — a whole tone rather than a comma — and
the tie-break overturns the key, dropping 7s below 5f.

**Open.** Read in the descent of the companion record on gravitation
[6], 2/3 is the submediant and 7/8 the leading tone, while 3/4 belongs
to no position at all: its rising form 7/4 is the harmonic seventh.
Which position the first multiplier must occupy remains open.

## 5 · Summary

Sections 2 through 4 established Theorem 1 term for term, both anomalies
as exact inequalities, the square spine, Madelung's rule as a
consequence, and the noble-gas corollary through 118 — each
machine-pinned. The account adopts the orbital formalism, the capacities
2(2ℓ+1), the quantitative energetics, and the configuration exceptions
from standard quantum mechanics, and inherits exact neutrality from
Volume III as chemistry's existence condition. The multiplier pair (2/3,
5/6) is a declared selection, weighed in Section 4. The volume's content
is retrodictive: its weight is compression, not prediction. The series'
open falsification tests lie elsewhere: the monopole, the fourth
generation, the electroweak prediction. Free parameters: none. Continuum
objects: none.

## 6 · Conclusion, and Volume VI

**The periodic table, on discrete terms, is ordered by one closed form
on the quantum numbers.** It departs from the hydrogenic order where the
fractions do, closes its shells on the noble gases, and ends, on the
ladder's last rung, at oganesson. Its existence is secured by a closure
theorem, its architecture by a ranking of exact fractions, and each of
its two anomalies by a single comparison. Chemistry begins ordered
because the register was ordered before matter was.

**Volume VI, *Early Galaxies*, takes the newly transparent, newly
chemical universe into structure.** It treats the chiral spiral as
primordial form, the bounded depth of gravitational cascade, and the
observations of early galaxies more mature than hierarchical assembly
expects.


## References

[1] E. Madelung, *Die mathematischen Hilfsmittel des Physikers*,
Springer (1936); V. M. Klechkovskii, the (n+ℓ) rule literature.

[2] E. R. Scerri, *The Periodic Table: Its Story and Its Significance*,
Oxford (2007) — the aufbau, its anomalies, and the configuration
exceptions.

[3] Yu. Ts. Oganessian et al., *Synthesis of the isotopes of elements
118 and 116*, Phys. Rev. C **74** (2006) 044602.

[4] G. Bressi et al., Phys. Rev. A **83** (2011) 052101 — the neutrality
of matter.

[5] C. Horstmann, *Navier–Stokes: A Solution on Discrete Terms*, Zenodo
(2026), DOI 10.5281/zenodo.21197044.

[6] C. Horstmann, *Gravity on Discrete Terms*, Zenodo (2026), DOI
10.5281/zenodo.22087599.

*All exact claims — the closed form, the term-for-term ranking, both anomalies, the square spine, the Madelung rule, and the noble-gas corollary ending at 118 — are pinned by `test_genesis_v.py` and re-verified on every revision.*

<div class="volhead">VOLUME VI · EARLY GALAXIES</div>

*The resonance lattice measured in the orbits, the chiral spiral as
primordial form, and collapse budgeted: black holes without
singularities.*

Structure, in the standard account, is assembled: primordial
fluctuations grow by gravitational instability, halos merge
hierarchically, disks settle, spirals develop as density waves — a
bottom-up narrative in which coherent form is late and accumulated. This
volume argues the reverse ordering for the form itself: coherence is
primordial, and assembly is the dynamics that plays out on it. It
grounds that argument in the one place where gravity's preference for
structure can be read with arithmetic precision — the resonance lattice
of the solar system. Its resonances are just intervals, and this is
measured, textbook celestial mechanics and not analogy. The three inner
Galilean moons lock in the chain 1:2:4, the octave chain. The lock is an
exact integer relation among the mean motions, n₁ − 3n₂ + 2n₃ = 0,
satisfied by the measured motions to a few parts in ten million and
actively maintained by libration. The system holds the relation by
libration, correcting continuously about the exact value. Neptune and
Pluto lock on 3:2 — the fifth — a resonance that has protected Pluto
from close approach for the age of the system. The same lattice clears
positions as well as filling them. At the exact ratios 3:1, 5:2, 7:3 and
2:1 of Jupiter's motion the asteroid belt is emptied — the Kirkwood gaps
— each gap's radius mapped from its exact ratio by Kepler's law to
within a percent, machine-pinned. Gravitational dynamics, given time,
locks onto and organizes around small-integer ratios: the same
least-action lattice on which this entire series rests, here in the
oldest precision science. The framework's reading is then this. The
spiral — the chiral, pointed, circulation-borne form of Volume II — is
the archetype rotating matter expresses natively, and not a late product
of assembly. The observations of mature, massive, coherent galaxies at
redshifts where hierarchical assembly expects immature systems — the
James Webb Space Telescope's early-maturity tension — are consistent
with primordial coherence and do not yet test it. The construction has
not derived a formation redshift, and part of the tension may be
resolved by stellar-mass systematics. The collapse bound supplies the
volume's theorem. A curvature singularity requires the collapse cascade
to complete unboundedly many octaves of scale in finite proper time,
precisely the supertask of the companion Navier–Stokes paper. The
universal form proved there is that any process demanding infinitely
many sequential distinguishable changes in finite time with finite
energy contradicts the Margolus–Levitin bound. That bars the singularity
for gravitational collapse exactly as for turbulent cascade. Black holes
without singularities: the horizon is real and observed — the Event
Horizon Telescope images are part of the established record — while the
interior terminates at finite cascade depth. The Penrose theorem stands
as mathematics about the continuum manifold and is contested as physics
at the level of its objects, the same relocation executed twice before
in this program. The volume states its epistemic status: the interior
claim is a consistency statement, not a prediction, since the interior
is unobservable in principle. The falsifiable content of the volume
lives in the resonance arithmetic (pinned), and the primordial-coherence
reading awaits a derived formation epoch, a named open problem. Free
parameters: none. Continuum objects: none.

## 1 · Introduction

After transparency (Volume IV) and the first chemistry (Volume V),
matter is free to move, cool, and gather.

**The standard account of what follows is hierarchical.** Small
overdensities collapse first, merge, and build upward: structure is
accumulated, and coherence comes late. The account has real successes
and real strains, and its dynamics are adopted here.

**This volume asks a prior question: what form does gravitating,
rotating matter prefer, and how strongly?** It answers with the one
dataset where the preference is measured to many digits: the resonance
structure of the solar system.

It then applies the series' theorem to the standard account's deepest
difficulty, the center of collapse.

## 2 · The resonances of the solar system are just intervals

**The statement is celestial mechanics, two centuries old [1, 2].** It
is machine-pinned here.

**The Laplace chain is 1 : 2 : 4, the octave chain.** Io, Europa, and
Ganymede orbit with mean motions satisfying an exact integer relation,
not an approximate ratio:

<div style="text-align:center; margin:12pt 0;">n₁ − 3n₂ + 2n₃ = 0<span style="float:right;">(1)</span></div>

The measured motions,

<div style="text-align:center; margin:12pt 0;">n₁ = 203.4889, &nbsp; n₂ = 101.3747, &nbsp; n₃ = 50.3176 &nbsp; degrees per day,<span style="float:right;">(2)</span></div>

satisfy the relation to the precision quoted, a few parts in ten million
of the motions themselves.

**The system librates about the exact value.** Perturbed, it corrects:
the relation is actively *held*. The three inner Galilean moons have
sustained an exact arithmetic identity for four billion years.

**Neptune and Pluto lock on the fifth:**

<div style="text-align:center; margin:12pt 0;">3 : 2 &nbsp; — the fifth.<span style="float:right;">(3)</span></div>

**The measured period ratio lies within a third of a percent of exactly
3/2.** The resonance is why Pluto persists: the lock times every
approach to keep the bodies apart. The exact ratio is the rest value,
and the libration is the perturbation about it.

**The same lattice clears positions: the Kirkwood gaps.** At the exact
ratios of Jupiter's mean motion,

<div style="text-align:center; margin:12pt 0;">3:1, &nbsp; 5:2, &nbsp; 7:3, &nbsp; 2:1,<span style="float:right;">(4)</span></div>

the asteroid belt is *empty* [2]. Kepler's law maps each exact ratio to
a radius; the measured gaps lie on the mapped radii to within a percent
(pinned, all four). The lattice does not only fill positions; it clears
them: occupation and ejection are both organized by small integers.

| system | ratio | interval | the lattice's act |
|---|---|---|---|
| Io – Europa – Ganymede | 1 : 2 : 4 | the octave chain | position held, by libration |
| Neptune – Pluto | 3 : 2 | the fifth | position held; Pluto protected |
| asteroid belt vs. Jupiter | 3:1, 5:2, 7:3, 2:1 | the clearings | positions cleared — the Kirkwood gaps |

**Reading.** Gravitational dynamics, given time, locks onto the
small-integer lattice, the positions of least action. This is the same
lattice on which every volume of this series rests: the octave chain of
Volume I's register, the 3:2 of the seed pair, the ratios of Volume V's
filling order. The solar system is the one gravitational structure
measured for centuries, and what those centuries recorded is *just
intonation*: exact small-integer ratios. The integers are observed in
the orbits and are not put there by the framework; the framework
explains why the orbits settle on them.

## 3 · The spiral as primordial form

Volume II proved that direction first appears at the cardioid and that
circulation is the native motion of the closed face.

**Rotating, self-gravitating matter carrying both faces has a natural
form, the chiral spiral.** It is circulation wound onto a pointed axis.

**Reading.** The spiral is the *archetype*, expressed natively by
rotating matter at every scale where it is free to organize, and not a
late product of assembly. On this reading, coherent spiral structure
early in cosmic history is the default.

**The James Webb Space Telescope has reported galaxies at high redshift
more massive, settled and coherent than hierarchical assembly expects at
that epoch [3].** They include grand-design spirals and quiescent disks
where the standard account expected irregular, immature systems.

**Consistent with the construction.** The observation agrees with
primordial coherence and does not yet test it: the construction has not
derived a formation redshift, a growth rate, or a coherence scale, and
until it does, the observation is not *its* prediction.

Part of the early-maturity tension may be resolved by stellar-mass
systematics as calibrations improve.

**Open.** The derived formation epoch is a named open problem of the
series; the reading stands or falls with the series' dictionary, and not
with the present photometry.

## 4 · Collapse is budgeted: black holes without singularities

**The standard account's deepest difficulty lies inside its
best-confirmed prediction.** The horizon was predicted, and has now been
imaged [4]. The singularity behind it is where the theory reaches its
own limit: infinite curvature, geodesic incompleteness, the end of
predictability, guaranteed by the Penrose theorem [5] *given the
continuum manifold and its energy conditions*.

The present series has made this argument twice, for the initial
singularity and for the Navier–Stokes singularity, and makes it here a
third time.

**Theorem.** A curvature singularity requires the collapse cascade to
complete unboundedly many octaves of scale in finite proper time. That
is a supertask, the object barred in the companion Navier–Stokes paper.
The universal form proved there applies verbatim: *any process demanding
infinitely many sequential distinguishable changes in finite time with
finite energy contradicts the Margolus–Levitin bound.*

**The free-fall schedule is geometric.** Its stage durations shrink
below the quantum minimum time at a finite, computable depth (pinned).

**The horizon is real, the interior terminates at finite cascade depth,
and nothing attains r = 0.** The zero of this arithmetic is a
limit-place and never a term (Volume I).

**From the established record.** The Penrose theorem stands as mathematics about the manifold and is contested as physics at the level of its objects.

**The interior statement is one of consistency, not a prediction.** The
interior is unobservable in principle; the volume's falsifiable content
is the pinned arithmetic of Section 2.

**The construction is globally regular.** There are no attained
singularities at either end, Volume I having removed the initial one,
and the regularity is one theorem applied three times.

## 5 · Summary

Sections 2 through 4 established the resonance lattice as measured
celestial mechanics — the Laplace relation, the fifth, the four Kirkwood
clearings — and the collapse budget, all machine-verified. The account
adopts hierarchical dynamics from the established record as the dynamics
that play out on the archetype — mergers happen, instabilities grow,
density waves propagate — and leaves the dark sector and the
rotation-curve question to Volume VII. The JWST early-maturity tension
is consistent with primordial coherence and does not yet test it; three
questions remain open — the formation redshift, the coherence scale, and
the amplitude of primordial handedness, open since Volume II. The
volume's falsifiable content lives in the pinned resonance arithmetic of
Section 2 and in the collapse budget. Free parameters: none. Continuum
objects: none.

## 6 · Conclusion, and Volume VII

**Structure, on discrete terms, settles on the small-integer lattice.**
The orbits lock onto it and hold their ratios for billions of years:
measured, librating, exact. The spiral is the native form of rotating
matter and not a late product. Collapse, like every cascade in this
program, has a finite budget: horizons without singularities, and a
universe regular at both ends and between them.

**Volume VII, *The Path to the Present*, states the cosmic energy
budget.** It gives the deceleration parameter, the epoch at which the
expansion began to accelerate, and what the construction establishes
about the dark sector. Volumes VIII to X then treat modern physics, and
*In Pure Mathematics* gives the theorems of the whole series by
themselves.


## References

[1] P.-S. Laplace, *Mécanique Céleste* (1799–1805) — the Galilean
resonance; modern treatment in C. D. Murray, S. F. Dermott, *Solar
System Dynamics*, Cambridge (1999).

[2] D. Kirkwood, *Meteoric Astronomy* (1867); Murray & Dermott, op.
cit., ch. 8 — the gaps at 3:1, 5:2, 7:3, 2:1.

[3] I. Labbé et al., *A population of red candidate massive galaxies
~600 Myr after the Big Bang*, Nature **616** (2023) 266; JWST
early-spiral reports (2022–2024).

[4] Event Horizon Telescope Collaboration, *First M87 Event Horizon
Telescope results*, Astrophys. J. Lett. **875** (2019) L1.

[5] R. Penrose, *Gravitational collapse and space-time singularities*,
Phys. Rev. Lett. **14** (1965) 57.

[6] N. Margolus, L. B. Levitin, Physica D **120** (1998) 188.

[7] C. Horstmann, *Navier–Stokes: A Solution on Discrete Terms*, Zenodo
(2026), DOI 10.5281/zenodo.21197044.

*All exact claims — the Laplace relation, the 3:2 resonance, the four
Kirkwood mappings, and the collapse budget — are pinned by
`test_genesis_vi.py` and re-verified on every revision.*

<div class="volhead">VOLUME VII · THE PATH TO THE PRESENT</div>

*The cosmic budget in fifteenths, closing exactly to one: the
deceleration at minus one half, the turning points at the cube roots of
two and four, the baryon share resolved by one reassignment, and the
registered expansion rate.*

The energy budget of the universe — what fraction is vacuum, what
fraction is dark matter, what fraction is ordinary matter — is, in the
standard account, three measured numbers. The ΛCDM parameters are inputs,
and the flatness of their sum is a result inflation is invoked to
explain. The present epoch, just after vacuum overtook matter, is known
in the field as the coincidence problem. This volume states the
construction's budget and what follows from it. The rest values are Ω_Λ =
2/3, Ω_dm = 4/15 and Ω_b = 1/15, a budget written in fifteenths. Fifteen
is the first operation's own internal interval, 57 − 42 = 15, from Volume
I. The dark-matter share is built from the sevenths as (1/7 + 3/7)/(15/7)
= 4/15. The budget closes exactly: 2/3 + 4/15 + 1/15 = 1. Flatness is
closure, the same closure that made hydrogen neutral, and needs no
fine-tuning. The two large rest values stand within 3% of the measured
shares, the program's coarsest agreement. The third is resolved by one
reassignment. The raw baryon share 1/15 splits as the hexad's own halves
do, 27/405 = 20/405 + 7/405, the committed share being exactly (2/9)² =
4/81 = 4.94% against the measured 4.93%. The remaining 7/405 is counted
with the vacuum, giving an effective vacuum share of 277/405 = 68.4%
against the measured 68.5%, the budget still closing exactly. Within this
budget the reassigned part is indistinguishable from vacuum: a degeneracy
that is stated, with the surveys that could break it. From the rest
values, two exact consequences. The deceleration: q₀ = Ω_m/2 − Ω_Λ = 1/6
− 2/3 = −1/2 exactly; the measured shares imply −0.53, the offset being
the budget's own 3%. The turning points, in closed form: acceleration
began where (1+z)³ = 2Ω_Λ/Ω_m = 4, and vacuum-matter equality where
(1+z)³ = 2. The two turning points of cosmic history are therefore
z_accel = ∛4 − 1 ≈ 0.587 and z_equal = ∛2 − 1 ≈ 0.260. The expansion
turned when the count crossed the cube roots of two and four. The "why
now" coincidence — that the present epoch is the one at which vacuum
overtakes matter — is thereby re-posed: the equality epoch is an exact
rung of the octave lattice, not an anthropic accident. Observers arrive
when chemistry and structure permit, and the rung is where the rung is.
Finally, the Hubble tension: the two principal determinations of the
expansion rate disagree, 73.17 against 67.36. The companion record on
gravitation derives 70.05, a registered prediction, between them. The
ratio of the two measured values, 1.086 ± 0.015, contains the tridecimal
step 13/12 and its neighbours alike, and singles out no step until it is
known to a quarter of a percent. Free parameters: none. Continuum
objects: none. Falsification conditions: the budget's rest values are
falsified if the measured shares move decisively away from the
fifteenths. The turning points stand or fall with the budget. The baryon
resolution is falsified if the committed share moves from 4/81 beyond the
degeneracy it states.

## 1 · Introduction

**The present state of the cosmos is described by three numbers: the
fractions of critical density in vacuum energy, dark matter, and
ordinary matter.**

**The standard model of cosmology measures the three to percent
precision and takes them as inputs.** Their near-flat sum is attributed
to an inflationary epoch introduced in part to produce it. That the
present epoch falls just after vacuum overtook matter is the
"coincidence problem," which has become a research field of its own.

This volume states the construction's budget, derives the two turning
points of cosmic history in closed form, resolves the baryon share by
one reassignment with its degeneracy stated, and sets the program's
registered expansion rate beside the Hubble tension.

## 2 · The budget: fifteenths, closing to one

**The rest values of the budget are**

<div style="text-align:center; margin:12pt 0;">Ω<sub>Λ</sub> = 2/3, &nbsp; Ω<sub>dm</sub> = 4/15, &nbsp; Ω<sub>b</sub> = 1/15<span style="float:right;">(1)</span></div>

Three structural facts, machine-pinned.

**First, the budget closes exactly:**

<div style="text-align:center; margin:12pt 0;">2/3 + 4/15 + 1/15 = 1<span style="float:right;">(2)</span></div>

Flatness, the observed Ω<sub>total</sub> = 1 to sub-percent, is in the
standard account a fine-tuning that inflation was introduced to remove;
here it is closure, the same kind of fact as the vanishing of a
generation's charge. The budget sums to one because it is a partition of
the whole.

**Second, the budget is written in fifteenths, and fifteen is the first
operation's own internal interval:**

<div style="text-align:center; margin:12pt 0;">57 − 42 = 15<span style="float:right;">(3)</span></div>

— from Volume I, pinned there and cross-pinned here. The cosmic budget
and the origin's first displacement share a denominator.

**Third, the dark-matter share is built from the sevenths:**

<div style="text-align:center; margin:12pt 0;">(1/7 + 3/7)/(15/7) = 4/15<span style="float:right;">(4)</span></div>

— the construction's own fractions, and not a measured input.

**The two large shares against measurement [1]:**

| share | rest value | measured | offset |
|---|---|---|---|
| Ω<sub>Λ</sub> | 2/3 | 0.6847 | −2.6% |
| Ω<sub>dm</sub> | 4/15 | 0.2645 | +0.8% |

These are the program's coarsest rest values, two orders of magnitude
looser than its electroweak or magnetic-moment values. The third share,
as it stands, does not agree:

**The baryon share is resolved by one reassignment.** The raw share 1/15
= 6.67% stands thirty-five percent above the measured 4.93%, and the
resolution uses only parts the construction already holds.

**The share splits as the hexad's own halves do:**

<div style="text-align:center; margin:12pt 0;">27/405 = 20/405 + 7/405<span style="float:right;">(5)</span></div>

This is the 20|7 partition of the reptend cycle's half-blocks, whose
digits sum to 8 + 5 + 7 = 20 and 1 + 4 + 2 = 7. The 7/405 is counted
with the vacuum.

**The committed share is**

<div style="text-align:center; margin:12pt 0;">(2/9)² = 4/81 = 4.938%<span style="float:right;">(6)</span></div>

against the measured 4.93%: agreement at +0.16%.

**The effective vacuum share is**

<div style="text-align:center; margin:12pt 0;">2/3 + 7/405 = 277/405 = 68.40%<span style="float:right;">(7)</span></div>

against the measured 68.5% (−0.11%).

**The budget still closes exactly:**

<div style="text-align:center; margin:12pt 0;">277/405 + 108/405 + 20/405 = 1<span style="float:right;">(8)</span></div>

**The reassigned part is, within this budget, indistinguishable from
vacuum.** The direction of the split is the construction's own rounding
rule. The degeneracy is stated, and vacuum-sector surveys that separate
the two components would break it. The suite pins the split, the shares,
and the closure.

## 3 · The deceleration and the turning points: closed forms

From the rest values, with the standard Friedmann kinematics adopted:

**The deceleration parameter is**

<div style="text-align:center; margin:12pt 0;">q₀ = Ω<sub>m</sub>/2 − Ω<sub>Λ</sub> = 1/6 − 2/3 = −1/2 exactly<span style="float:right;">(9)</span></div>

The universe accelerates, and at the rest values the deceleration
parameter is exactly minus one half. The measured shares imply −0.53;
the offset of about 5% is the budget's own.

**Acceleration begins where the vacuum term balances the matter term:**

<div style="text-align:center; margin:12pt 0;">(1+z)³ = 2Ω<sub>Λ</sub>/Ω<sub>m</sub> = 4, &nbsp;&nbsp; z<sub>accel</sub> = ∛4 − 1 ≈ 0.587<span style="float:right;">(10)</span></div>

**Vacuum–matter equality, the "coincidence" epoch, falls at**

<div style="text-align:center; margin:12pt 0;">(1+z)³ = Ω<sub>Λ</sub>/Ω<sub>m</sub> = 2, &nbsp;&nbsp; z<sub>equal</sub> = ∛2 − 1 ≈ 0.260<span style="float:right;">(11)</span></div>

Both are machine-pinned as exact statements about the rest values.

**Reading.** The expansion turned when the count crossed the cube roots
of two and four. The turning points of cosmic history are octave thirds
— the same 2^(1/3)-family steps that pace the turnover schedule of the
companion paper's cascade.

**The coincidence problem is thereby re-posed.** In the standard
account, Ω<sub>Λ</sub> ≈ Ω<sub>m</sub> *today* is an unexplained feature
of the present epoch, and it has motivated anthropic reasoning. Here the
equality epoch is an exact rung: the count crosses ∛2 at a fixed step,
observers arrive when chemistry and structure permit (Volumes V, VI),
and the two schedules overlap because both follow the same ladder. The
coincidence is not removed; it becomes a statement of arithmetic.

## 4 · The Hubble tension

**The two principal determinations of the expansion rate disagree.** The
disagreement, the Hubble tension, is a decade old:

<div style="text-align:center; margin:12pt 0;">distance ladder: 73.17 ± 0.86 [2] &nbsp; · &nbsp; microwave background: 67.36 ± 0.54 [1]<span style="float:right;">(12)</span></div>

**The program's value is 70.05 km s⁻¹ Mpc⁻¹.** It is derived in the
companion record on gravitation [6] and registered as commitment 10 of
the registry of predictions [7]. It stands 5.0 standard deviations above
the microwave-background value and 3.6 below the distance ladder's, and
it is refuted if the tension resolves decisively away from it.

**The ratio of the two measured values is 1.086 ± 0.015.** Within that
interval lies

<div style="text-align:center; margin:12pt 0;">13/12<span style="float:right;">(13)</span></div>

— the tridecimal step, thirteen being a gap of the seed's near-miss
ladder (Volumes I, IV). It lies 0.2 standard deviations from the ratio,
and so do its neighbours: 12/11 and 14/13 lie within 0.6.

**The ratio singles out no step at present precision.** The neighbouring
steps lie 0.6 and 0.7 percent from 13/12, and the ratio is known to 1.4
percent.

**The ratio becomes evidence only when it is known to a quarter of a
percent, a sixfold tightening.** If the tension persists at that
precision with the ratio at 13/12, the question of why two
determinations differ by one lattice step is posed. If the tension is
resolved by systematics, the ratio has no significance.

The registered statement is the value 70.05. The ratio is recorded as an
observation, with the precision that would make it a test.

## 5 · Summary

Sections 2 and 3 established the budget's exact closure, the fifteenths
as the first operation's own interval, the sevenths construction of the
dark-matter share, and the deceleration at −1/2. They established the
closed forms of the turning points, 4 and 2, hence ∛4 − 1 and ∛2 − 1.
The degeneracy of the baryon resolution is stated, the reassigned 7/405
being indistinguishable from vacuum, and the two large rest values are
the program's coarsest, within 3% of the measured shares. The account
adopts the Friedmann kinematics from the established record. On the
Hubble tension the program's registered value is 70.05, and the ratio of
the two determinations singles out no step at present precision. The
coincidence problem is re-posed as an exact rung and remains open. A
decisive movement of the measured shares away from the fifteenths would
falsify the budget and the turning points with it. Free parameters:
none; continuum objects: none.

## 6 · Conclusion, and Volume VIII

The path to the present, on discrete terms, is a budget written in the
origin's own fifteenths and closing to one exactly. Its deceleration
parameter is minus one half, and its history turned at the cube roots of
two and four. The baryon share is resolved by one reassignment, with its
degeneracy stated, and the expansion rate carries a registered value
between the two determinations. The present epoch is a rung of the
ladder.

Volume VIII, *Modern Physics*, turns from the cosmos to the theories. It
states what the construction says quantum mechanics *is*, where the
paradoxes of the standard interpretation are resolved, and why the two
principal frameworks of twentieth-century physics have not been unified,
before Volume X makes the comparison with relativity.


## References

[1] Planck Collaboration, *Planck 2018 results VI: cosmological
parameters*, Astron. Astrophys. **641** (2020) A6.

[2] L. Breuval et al. (SH0ES), *Small Magellanic Cloud Cepheids observed
with the Hubble Space Telescope provide a new anchor for the SH0ES
distance ladder*, Astrophys. J. **973** (2024) 30 — H₀ = 73.17 ± 0.86 km
s⁻¹ Mpc⁻¹.

[3] A. G. Riess et al., Astron. J. **116** (1998) 1009; S. Perlmutter et
al., Astrophys. J. **517** (1999) 565 — the acceleration's discovery.

[4] S. Weinberg, *The cosmological constant problem*, Rev. Mod. Phys.
**61** (1989) 1 — addressed here at the level of shares; the magnitude
requires a unit.

[5] C. Horstmann, *Navier–Stokes: A Solution on Discrete Terms*, Zenodo
(2026), DOI 10.5281/zenodo.21197044.

[6] C. Horstmann, *Gravity on Discrete Terms*, Zenodo (2026), DOI
10.5281/zenodo.22087599 — the expansion rate, 70.05 km s⁻¹ Mpc⁻¹.

[7] C. Horstmann, *Predictions on Discrete Terms*, Zenodo (2026), DOI
10.5281/zenodo.21206818 — commitment 10.

*All exact claims — the closure, the fifteenths, the sevenths
construction, the deceleration, the turning points, the resolved baryon
share, and the Hubble ratio with its uncertainty — are pinned by
`test_genesis_vii.py` and re-verified on every revision.*

<div class="volhead">VOLUME VIII · MODERN PHYSICS</div>

*The quantum state as a sounding string, collapse as arithmetic
filtering, measurement as a lossy port, the paradoxes resolved by
counting — and the diagnosis of why the two principal theories of the
century have not been unified.*

<div style="font-size:9.2pt; line-height:1.5; text-align:justify;">Twentieth-century physics produced two highly successful calculational frameworks and one enduring open question: what either framework describes. Quantum mechanics has a measurement problem, many interpretations, and a state vector that is never observed directly. General relativity has singularities and resists quantization, and after ninety years no union of the two exists. This volume states the construction's account and shows several of these difficulties resolved under it by counting, with no new physics. The state: a quantum superposition is a sounding string, every harmonic present at once; it becomes a paradox only when the mathematics of the envelope is taken for a physical object. The collapse mechanism is exact and machine-pinned. Mode m of a string has a node at the reduced position p/q if and only if q divides m, so touching the string at p/q keeps exactly the multiples of q. Touching the midpoint keeps the octave family; touching the third keeps the triad family. Collapse is arithmetic filtering: a measurement selects a residue class, and which class depends on where the string is touched. No observer's mind is required: anything that commits, that rounds, filters. The port: the Born reading keeps the squared magnitudes and discards the phases, exactly half of the state's integers, a pinned theorem of this program. The discarded half is unread and not destroyed, and the irreversibility of measurement is a Landauer cost on the working face. The classical world: maintaining mutual phase across N constituents puts coherence at N factorial, and twenty constituents already exceed 10¹⁸. That is why dust is classical and the cat does not interfere; decoherence is the same count read from the environment's side. Duality: the two-slit trade-off P² + V² = 1 is, in this construction, Euclid's Pythagorean-triple identity, exact and pinned. The which-path and eraser phenomena are the bookkeeping of the legs in the marker triple P² + V² + C² = 1, which saturates Englert's bound. Entanglement: one harmonic read at two nodes is a chord, and correlations carried by a shared structure need no signal. The delayed-choice puzzles are resolved because the shared structure is non-temporal: there is no "before" on the harmonic. Bell's theorem constrains local hidden variables; the shared harmonic is global and structural and is not a variable, and Bell's theorem stands in full. The volume then tests the inequality on a register machine. The pre-written chord, run against the inequality, is classical, capped at exactly two. The register's unique non-local operation, the carry, firing at the antipode and acting by octave promotion, lifts an exactly silent machine to five-halves. The quantum ceiling is proved unreachable at any finite register: it is a rest value, approached and never attained. The one remaining rung, quadratic composition, is named and remains open. The diagnosis closes the volume. The infinities of field theory are artifacts of the continuum layer, where the companion paper finds the meter deleted. The naturalness and hierarchy problems are artifacts of frameworks with free parameters: where ratios are uniquely determined, nothing is unnatural. The interpretations multiply because the envelope was taken for the object. The failure of unification has a structural cause: quantum mechanics counted the working face, while relativity kept the flowing face as continuum geometry. One framework counts and the other flows, and as formulated they stand on opposite sides of the completed limit. That comparison belongs to Volume X; this volume states the diagnosis. Free parameters: none. Continuum objects: none, the envelope being acknowledged as an instrument.</div>

## 1 · Introduction

**The numbers of quantum mechanics are not in doubt, and what the theory
describes is not agreed.**

**The interpretations disagree about what exists.** Copenhagen,
many-worlds, Bohmian mechanics, QBism and others have stood side by side
for a century, which suggests that the question is not well posed.

**This volume poses the question on discrete terms.** It exhibits the
mechanisms (pinned), resolves what they resolve, and adopts from the
established record what stands. It diagnoses the absence of a quantum
theory of gravity, after ninety years, as a difference of bookkeeping
that the final volumes of the series take up directly.

## 2 · The state: a sounding string

**A piano string, once played, sounds every harmonic it supports at the
same time.** The fundamental, the octave, the twelfth and the rest are
all present, with amplitudes set by where the hammer fell.

**Identification.** On discrete terms this *is* superposition and not an
analogy to it: the state is the full list of (magnitude, phase) pairs
over the modes, all real, all present, evolving by the workless tick.

**The paradox arises when the envelope is taken for a physical object.**
A sounding string is not paradoxical. Its quantum counterpart became so
because the *envelope* — the continuum wavefunction, an instrument for
computing mode contents — was taken for a physical thing that must
"collapse."

## 3 · Collapse: arithmetic filtering, machine-pinned

What happens when a sounding string is *touched*?

**Mode m has a node at the reduced position p/q if and only if q divides
m:**

<div style="text-align:center; margin:12pt 0;">mode m has a node at p/q &nbsp; ⇔ &nbsp; q divides m<span style="float:right;">(1)</span></div>

**The node-touch selection rule (pinned).** *Touching the string at p/q keeps exactly the harmonics that are multiples of q.*

| touch at | what remains |
|---|---|
| the midpoint | the even family (the octave class) |
| the third | the multiples of three (the triad class) |
| a seventh | the seed's family — 7, 14, 21 |

**Collapse is arithmetic filtering.** A measurement is a touch: it
selects a residue class, the class is set by where contact is made, and
the modes with no node there deliver their content elsewhere.

**Anything that commits, that rounds, filters.** No observer or mind is
required. The von Neumann chain [1] terminates at the first irreversible
operation and not at consciousness; an irreversible operation is defined
arithmetically, as many-to-one, and carries its thermodynamic cost
(Landauer [7]).

On these terms the measurement problem does not arise.

## 4 · The port, and the exactly-half theorem

**What a measurement returns is the Born reading: squared magnitudes,
with the phases discarded.**

**Theorem (exactly half).** The state carries 2n integers, n magnitudes
and n phases, and the port returns n: the reading discards exactly half.
In the construction this is pinned:

<div style="text-align:center; margin:12pt 0;">state: 2n integers (n magnitudes, n phases) &nbsp; → &nbsp; port returns n<span style="float:right;">(2)</span></div>

**The discarded half is unread and not annihilated.** It is circulation
to which the port is blind, and every apparent loss of quantum
information is this unread half.

**The irreversibility of measurement is the Landauer cost of the
commitment.** It is incurred on the working face and released as heat.

**The classical world is a factorial fact (pinned).** Coherence across N constituents requires their mutual phases held, and the count of phase relations puts it at N!:

<div style="text-align:center; margin:12pt 0;">N! : &nbsp; ten constituents already stand at 3.6 million; &nbsp; twenty exceed 10¹⁸<span style="float:right;">(3)</span></div>

**Dust is classical because no available budget maintains a dust grain's
phase relations.** The cat does not interfere because the cat is an N of
order 10²⁵.

**From the established record.** Decoherence theory [4] computes the
same conclusion from the environment's side and is adopted whole; the
construction adds only the *arithmetic identity* of the result.

## 5 · Duality and entanglement, exactly

**Duality is Euclid's identity.** The two-slit trade-off between
which-path knowledge and fringe visibility,

<div style="text-align:center; margin:12pt 0;">P² + V² = 1<span style="float:right;">(4)</span></div>

is in this construction *the Pythagorean-triple identity itself*, exact
over the amplitude grid and machine-pinned:

<div style="text-align:center; margin:12pt 0;">(a² − b²)² + (2ab)² = (a² + b²)²<span style="float:right;">(5)</span></div>

**A which-path marker adds a third leg, saturating Englert's bound [3]:**

<div style="text-align:center; margin:12pt 0;">P² + V² + C² = 1<span style="float:right;">(6)</span></div>

The quantum eraser is the bookkeeping of the legs: coherence is
relocated into the marker and can be retrieved from it.

**The finite object carries a signature the continuous theory does
not.** At a register of size n the fringe intensities are a finite set
of algebraic values and not a smooth continuum: at n = 8, the five
levels of ℤ[√2], with antipodal positions summing to twice the mean:

<div style="text-align:center; margin:12pt 0;">{4, &nbsp;2+√2, &nbsp;2, &nbsp;2−√2, &nbsp;0}<span style="float:right;">(7)</span></div>

And the principal maximum of an N-aperture pattern is exact:

<div style="text-align:center; margin:12pt 0;">principal maximum = N²<span style="float:right;">(8)</span></div>

These are ratios: they carry no unit and fix no length, so they stand as
falsification conditions within the dimensional boundary.

**Falsification.** A measured histogram of relative fringe intensities filling a continuum, or a principal maximum lying off an integer N², would refute the account at every register (machine-pinned).

**Entanglement is one harmonic with two nodes.** A single mode of a shared structure read at two places is a *chord*, and chords need no signals: the correlations were written when the structure was.

**The structure is non-temporal.** There is no "before" on a harmonic,
which is why delayed-choice arrangements produce no paradox.

**Bell's theorem [2] constrains local hidden variables.** The shared
harmonic is global and structural and is not a variable; no-signaling
holds.

**Bell's theorem stands, and the chord account is a reading.** The next
section tests the reading against the inequality and finds that, as
first stated, it does not reach the measured violation.

**From the established record.** The experimental record [5] stands in full.

What the register can and cannot do against the theorem is settled in
the next section, by machine.

## 6 · Giving Bell his well-deserved rest: the inequality as a rest ceiling

**Bell's theorem is itself a counting fact [2].** For outcomes written
in advance, with two settings on each wing and answers ±1, every one of
the sixteen possible assignments satisfies (enumerated, pinned)

<div style="text-align:center; margin:6pt 0;">|S| ≤ 2<span style="float:right;">(9)</span></div>

**Definition (rest ceiling).** Two is the correlation's *rest ceiling*:
the most that any account with outcomes written in advance can reach.

**Measurement exceeds it, in loophole-free tests [5]; the quantum
maximum, at the optimal settings, is**

<div style="text-align:center; margin:6pt 0;">S = 2√2<span style="float:right;">(10)</span></div>

This volume's own chord reading must therefore be tested against the
bound.

**The pre-written chord reaches exactly two.** Run as written, with the
pinned selection rule at two wings of one shared mode, it is capped
there (machine-checked, exact): the chord reading as first stated does
not produce the measured violations.

**The theorem excludes every pre-written account.** It does not address
the one-string account, a single structure read at two places, and that
account requires a mechanism.

**The mechanism the register offers is the carry.** Volume I established
that of the substrate's first operations exactly one is non-local.

**A carry conserves the count and moves only the writing.** Ten units at
one place become one unit at the next. It is therefore invisible to
every reading of the value, and its capacity is exactly one bit: there
is no half-carry.

**The machine has one shared register state and exact arithmetic
throughout (pinned).** The first wing's touch fires a carry precisely
when the state overflows the quarter straddling the antipode. The carry
acts by *octave promotion*, two at this mode becoming one at the next,
and the second wing reads the promoted or unpromoted register.

**The machine's value is**

<div style="text-align:center; margin:12pt 0;">S = 5/2 exactly<span style="float:right;">(11)</span></div>

scale-invariant across register sizes eight, sixteen and thirty-two,
with the second wing's statistics *exactly* independent of the first
wing's choice: the rest ceiling is exceeded in exact silence, that is,
with no signal between the wings.

**Two controls confirm that the carry is the cause.** Remove the carry
and the machine returns to two; let the carry act by anything other than
promotion and the machine returns to two. The entire excess above the
pre-written bound is produced by the register's one non-local operation,
acting as Volume I defines it.

**Four exact facts** state what the result establishes.

**First: the structure of the quantum ceiling** [9]. The operator
identity

<div style="text-align:center; margin:12pt 0;">S² = 4·I − [A,A′]⊗[B,B′]<span style="float:right;">(12)</span></div>

places the whole excess above two in the disturbance term, which is
nonzero only when the measurement frames fail to commute, so the
physical ceiling is the diagonal of two classical blocks:

<div style="text-align:center; margin:12pt 0;">√(2² + 2²) = 2√2<span style="float:right;">(13)</span></div>

The right angle of the frames is, on these terms, supplied by the seed
itself: the excitation profiles at one-half and one-third are exactly
orthogonal, closing on the hexad.

**Second: the denominator fact (pinned).** A register of size N yields
correlations that are multiples of 1/N, so the quantum value, which is
irrational, is unreachable at any finite register. Tsirelson's bound
stands to the carry machine's family as a rest value, approached at
every scale and attained at none: the two-tier structure applies to the
correlation ceiling itself.

**Third: the ladder of ceilings**, each exact:

| ceiling | value | note |
|---|---|---|
| the pre-written | 2 | — |
| the carry machine | 5/2 | the arithmetic mean of two and three |
| the measured world | 2√2 | the geometric mean of two and four |
| the open telegraph | 3 | supremum of S = 3 − 1/p, never attained |
| the logical maximum | 4 | — |

A counting machine composes arithmetically; the measured world composes
quadratically; and the gap between five-halves and 2√2 is the *quadratic
composition* the register has not yet been shown to perform. It remains
open.

**The value five-halves is also the fold ratio of the seed.** Split the
six sevenths at Midy's axis and the ratio of the sum of the upper three
to the sum of the lower three is (15/7)/(6/7) = 5/2 exactly. Generalized
to 1/p, the fold ratio is (3p − 1)/(p + 1). The family's endpoints are
this ladder's own ceilings, 2 at p = 3 and 3 in the limit, the telegraph
supremum. Its value is 5/2 at p = 7 alone, so the family takes its
midpoint at the seed prime and nowhere else. The arithmetic on both
sides of the correspondence is exact and machine-checked. The
identification of the two is a reading; a derivation connecting the
machine's correlation table to these sums would establish it.

**Open.** The rung between five-halves and 2√2 remains open. A
demonstration that the carry family exceeds five-halves in silence, or a
proof that it cannot, settles the question either way.

**Fourth: the boundary between what the machine determines and what it
selects (pinned).** The value five-halves is uniquely determined — swept
against the carry-arc and both measurement frames together, it is the
largest silent correlation the family reaches and is never once
exceeded. And the arc's centre follows with no free choice. The
promotion doubles the register state, and the fold of that doubling —
the two points that halve to zero — is exactly the antipode the carry
straddles. So "the quarter straddling the antipode" is the
octave-doubling seam rather than a chosen location.

**The arc's exact width and position are a selection.** With the
measurement frames held at the values this section fixes, the silent
five-halves arc is unique up to the register's own antipode symmetry.
Freeing those frames widens the silent family — at register eight, to
three antipode-orbits across two widths — with this section's arc
returning as the shortest. The ceiling and the seam admit no
alternative; the exact arc is a selection made together with the frames.

**Bell is given his well-deserved rest: his inequality is the rest
ceiling of every pre-written account, this volume's own first reading
included.** The register's unique non-local operation lifts a silent
machine above that ceiling by exactly half a unit. The remaining
distance to the measured value is a named and measured rung.

The theorem stands, the chord's bound of two stands, and the machine's
value stands; experiment decides between accounts.

## 7 · The diagnosis: why the two theories have not been unified

**The infinities of quantum field theory are artifacts of the continuum
layer.** Renormalization handles them case by case. On the companion
paper's argument they are quantities computed in a description whose
idealization deleted the meter. The construction's couplings run per
octave and its cascades have budgets; nothing in it diverges because
nothing in it completes a supertask.

**The naturalness and hierarchy problems arise in frameworks with free
parameters.** Why the Higgs is light and why gravity is weak are
questions about parameters that could take any value, so that a specific
value requires explanation. Where ratios are uniquely determined, as
throughout this series, nothing is unnatural: the hierarchy is a count
of octaves.

**The interpretations multiply because the envelope was taken for the
object.** The polar state has no interpretation problem: everything in
it is either readable (magnitudes), unread (phases), or declared (the
rest value). Nothing in it is at once unobservable in principle and
essential to the account.

**One framework counts and the other flows, which is why they have not
been unified as formulated.** Quantum mechanics quantized the working
face — action, charge, commitment — while general relativity kept the
flowing face as continuum geometry. They stand on opposite sides of the
completed limit. On this account they are two descriptions, one of the
world's own counting and one an instrument for it. What relativity's
confirmed phenomena look like when the flowing face is counted is the
subject of Volume X; this volume states only the diagnosis.

## 8 · Summary

Sections 2 through 6 established, machine-verified, the node-touch
selection rule, the exactly-half theorem, the duality identity, the
quantized fringe ladder with its N² principal maximum, the factorial
bound, and the Bell results. Those results are the pre-written chord
capped at exactly two, and the carry machine at five-halves in exact
silence with both controls returning it to two. The quantum ceiling is
unreachable at any finite register. The five-halves value and the
doubling-seam centre are uniquely determined, while the arc's exact
width is a selection made with the frames. The account adopts the
experimental record entire — interference, the Bell tests, delayed
choice, decoherence rates — together with the decoherence program's
computations; the piano identification and collapse-as-commitment are
readings, and Bell's theorem stands. Two questions remain open: the
quadratic-composition rung between five-halves and 2√2, and the
unification of the two frameworks, taken up in Volume X. A measured
histogram of relative fringe intensities filling a continuum, or a
principal maximum lying off an integer N², falsifies the volume. **Free
parameters: none. Continuum objects: none claimed as physical.**

## 9 · Conclusion, and Volume IX

**On discrete terms, the state is a sounding string.** Collapse is a
touch, and its selection rule is a divisibility fact. Measurement
returns exactly half and dissipates the Landauer heat of the reading.
Classicality is a factorial, duality is Euclid's identity, and
entanglement is a chord. Bell's inequality holds as the rest ceiling at
two, and the register's carry exceeds it in silence.

The difficulties of the century are, on this account, those of a
description that flows where the world counts. The two frameworks are a
count and a flow, on opposite sides of the completed limit.

**Volume IX, *Position and Diffusion*, takes the count into space
itself.** It states what position *is* when the substrate is resolution,
why diffusion needs no randomness, and what follows for locality. Volume
X then confronts relativity, and *In Pure Mathematics* gives the
theorems by themselves.


## References

[1] J. von Neumann, *Mathematische Grundlagen der Quantenmechanik*,
Springer (1932) — the measurement chain.

[2] J. S. Bell, *On the Einstein Podolsky Rosen paradox*, Physics **1**
(1964) 195.

[3] B.-G. Englert, *Fringe visibility and which-way information: an
inequality*, Phys. Rev. Lett. **77** (1996) 2154.

[4] W. H. Zurek, *Decoherence, einselection, and the quantum origins of
the classical*, Rev. Mod. Phys. **75** (2003) 715.

[5] A. Aspect et al., Phys. Rev. Lett. **49** (1982) 1804; the 2015
loophole-free tests (Delft, Vienna, NIST).

[6] H. von Helmholtz, *On the Sensations of Tone*, Longmans (1885) — the
harmonic content of a piano string.

[7] R. Landauer, IBM J. Res. Dev. **5** (1961) 183.

[8] C. Horstmann, *Navier–Stokes: A Solution on Discrete Terms*, Zenodo
(2026), DOI 10.5281/zenodo.21197044.

[9] B. S. Cirel'son, Lett. Math. Phys. **4** (1980) 93; N. D. Mermin,
Phys. Rev. Lett. **65** (1990) 1838; B. F. Toner, D. Bacon, Phys. Rev.
Lett. **91** (2003) 187904.

*All exact claims are pinned by `test_genesis_viii.py`, `test_bell_machine.py`, `test_carry_stand.py`, `test_carry_free_settings.py`, `test_five_halves_fold.py` and `test_two_slit.py`, re-verified on every revision.*

<div class="volhead">VOLUME IX · POSITION AND DIFFUSION</div>

*Position as address, locality as adjacency, and diffusion without
randomness — Fick's law as a counting identity, with π emerging as the
envelope of enumeration.*

Two concepts anchor every physical description: where a thing is, and
how ensembles of things spread. The standard account grounds both in
objects the preceding eight volumes have replaced — position in the
real-number continuum, diffusion in irreducible randomness. This volume
replaces both groundings and proves the replacements exact. Position is
an address. On a counting substrate a location is not a point on a
continuum but an address at a resolution, an n-digit address locating to
one part in 10ⁿ. Refinement is an operation, subject to the meter like
every operation in this program. The continuum of positions is the
familiar envelope, an instrument of description, while what exists
physically is the address actually committed. Locality is adjacency in
the register, and the analysis of Volume VIII (one harmonic, two nodes)
requires no action at a distance, because shared structure is not
transmission. Diffusion without randomness is the volume's theorem, and
it is a combinatorial identity. Pascal's triangle *is* the diffusion
kernel: the binomial coefficient C(n,k) counts, exactly, the n-step
walks with k steps leftward, and what the continuum account calls
probability is path-counting normalized. The diffusion law itself is the
exact identity Σₖ C(n,k)(n−2k)²/2ⁿ = n, machine-pinned for every n
tested and provable for all. That law is the linear growth of
mean-square displacement with time which Einstein derived for Brownian
motion and Perrin measured. Spread grows linearly in the count because
counting makes it so, with no random step anywhere. The Gaussian that
practitioners fit to diffusion clouds is the envelope of the counting.
The return weight C(2n,n)/4ⁿ approaches 1/√(πn), pinned to half a
percent by n = 100 and tightening. π itself emerges as the envelope of
pure enumeration: the circle's number appears in the asymptotics of
walks that never left the integer line. The companion record on π
develops that fact, and this volume exhibits it. The arrow of diffusive
spreading belongs to the record and not to chance: every step is a
committed entry, the walk cannot be undone because commitment is
many-to-one, and entropy — here as everywhere in this program — counts
collisions. Einstein's 1905 analysis and the stochastic calculus built
on it are adopted whole as envelope mathematics of the highest utility.
The volume's statement concerns the ground: beneath every successful
stochastic description is an exact enumeration, and the randomness was
never in the world — it was in the decision not to count. Free
parameters: none. Continuum objects: none claimed as physical. The
program's mathematics excludes three objects — the attained zero, the
completed continuum, irreducible randomness — and this volume
establishes the exclusion of the third.

## 1 · Introduction

**The standard account grounds position in the real numbers and
diffusion in chance.** The position of an electron is a real number,
with infinitely many digits, almost all of them unobservable. Cream
spreads through coffee because molecular motion is taken to be
irreducibly random and is described statistically.

**The world counts: it involves neither irreducible chance nor a
completed continuum.** The series has already contested the continuum,
in Volumes I and VIII and in the companion Navier–Stokes paper. This
volume contests irreducible randomness and completes the program's
position.

## 2 · Position is an address

**Definition (address).** On a counting substrate, a location is an
*address*: n digits specify a region one part in 10ⁿ of the reference
scale, and the region *is* the position at that resolution:

<div style="text-align:center; margin:12pt 0;">n digits &nbsp;→&nbsp; one part in 10ⁿ<span style="float:right;">(1)</span></div>

Three consequences follow, each doing work elsewhere in the series.

**Refinement is an operation.** Sharpening an address by one digit is a distinguishable state change, subject to the meter. Margolus–Levitin, in the companion paper, gives the consequence: infinitely precise position would require infinitely many operations. The continuum position is a supertask, and its unattainability here is the same theorem that barred the singularities.

**The continuum of positions is the envelope**: indispensable as an
instrument, and not physical. The real line does for location what the
wavefunction does for the mode inventory (Volume VIII): it summarizes
and is not itself a physical object.

**Locality is adjacency in the register**, and correlation is not
transmission. The results of Volume VIII for separated readings (one
harmonic, two nodes) follow at once: nothing needs to travel between the
nodes of a structure that was never in two pieces.

## 3 · Diffusion without randomness: the counting identity

**The walk that underlies diffusion theory has n steps, each left or
right.** The standard account makes the steps random and derives
statistics. The present account counts.

**The kernel is Pascal's triangle.** C(n, k) is the *exact number* of n-step walks with k left-steps — an enumeration, not a distribution. The 2ⁿ walks all exist in the count; "probability" is enumeration normalized.

The rows sum to 2ⁿ, and the kernel is symmetric, so there is no drift
without a cause (both pinned):

<div style="text-align:center; margin:12pt 0;">rows sum to 2ⁿ, &nbsp;&nbsp; C(n,k) = C(n,n−k)<span style="float:right;">(2)</span></div>

**Theorem (the diffusion law, by counting).** *The mean-square
displacement after n steps is*

<div style="text-align:center; margin:12pt 0;">Σₖ C(n,k) (n − 2k)² / 2ⁿ = n<span style="float:right;">(3)</span></div>

exactly, for every n. Machine-pinned across the range and elementary to prove in general.

**Identification.** This is Fick's law, spread linear in time with σ² =
n in lattice units, as a combinatorial identity.

**Einstein's 1905 result for Brownian motion [1], which Perrin's
measurements made evidence for the atom [2], is here a count of paths.**
No random step enters.

**π emerges as the envelope of enumeration.** The weight of return approaches the circle's number:

<div style="text-align:center; margin:12pt 0;">C(2n,n) / 4ⁿ &nbsp;→&nbsp; 1/√(πn)<span style="float:right;">(4)</span></div>

pinned to half a percent at n = 100 and tightening at n = 400.

**From the established record.** The Gaussian that practitioners fit to
every diffusion cloud is de Moivre's envelope [3] of the exact count,
and it is adopted as an instrument.

**The circle's number appears in the asymptotics of walks that never
left the integer line.** The instrument is continuous; what it
summarizes is a triangle of whole numbers. The companion record on π
develops this [6].

## 4 · The arrow in the spreading

**The standard answer to why mixing is never undone is overwhelming
improbability.** It is correct and incomplete.

**On discrete terms, every step is a committed entry.** The walk's
history is written as it happens, and spreading is the accumulation of
commitments. The process cannot be undone because commitment is
many-to-one: the same classification, invertible or irreversible, that
gave Volume I its third operation and Volume VIII its arrow of
measurement.

**Identification.** Entropy counts collisions. The diffusive arrow, the
thermodynamic arrow, and the arrow of measurement are one arrow: the
growth of the committed record, which only grows.

## 5 · What is adopted from the established record

**From the established record.** Everything operational is adopted
whole: Einstein's fluctuation analysis, the stochastic calculus, the
Fokker–Planck and Langevin equations, and the rest of the probabilistic
toolkit. They are the mathematics of the envelope: when 10²³ paths are
not counted, probability is the correct bookkeeping of that decision.

**Beneath every successful stochastic description is an exact
enumeration.** The volume's statement concerns the ground and not the
toolkit: the randomness is in the decision not to count, and not in the
world.

**The program's mathematics excludes three objects: the attained zero,
the completed continuum, and irreducible randomness.** The companion
paper and Volume I established the first exclusion, the series as a
whole argues the second, and this volume establishes the third.

## 6 · Summary

Sections 2 through 5 established the path count, with rows summing to 2ⁿ
and the kernel symmetric. They established the diffusion law as an exact
identity, σ² = n for every n tested, and the π-envelope convergence,
within half a percent at n = 100 and tightening. Each is
machine-verified. The stochastic toolkit entire is adopted from the
established record as envelope mathematics. Position as address,
refinement as operation, and the one arrow are identifications and not
derivations. A demonstrated physical process whose statistics *cannot*
arise from any enumeration — irreducible randomness exhibited and not
assumed — falsifies the volume. What observation would constitute such a
demonstration remains an open question.

**Free parameters: none. Continuum objects: none claimed as physical.**

## 7 · Conclusion, and Volume X

**Position, on discrete terms, is an address: precision is work, and
locality is adjacency.** Diffusion is the large-scale appearance of
counting: Fick's law is an identity, the Gaussian an envelope, π a
product of pure enumeration, and the arrow the one-way growth of the
record. The world counts, and the curves fitted to diffusion describe
that count.

**Volume X, *Relativity and the Standard Model*, sets the serial
substrate against the relativity of simultaneity.** The confirmed
phenomena of the two theories of relativity are taken one by one, and
what the construction derives, what it reads and what remains open are
stated for each. *In Pure Mathematics* then closes the series with the
mathematics alone.


## References

[1] A. Einstein, *Über die von der molekularkinetischen Theorie der
Wärme geforderte Bewegung von in ruhenden Flüssigkeiten suspendierten
Teilchen*, Ann. Phys. **17** (1905) 549.

[2] J. Perrin, *Les Atomes*, Alcan (1913).

[3] A. de Moivre, *The Doctrine of Chances* (1738); the de
Moivre–Laplace limit.

[4] N. Margolus, L. B. Levitin, Physica D **120** (1998) 188.

[5] C. Horstmann, *Navier–Stokes: A Solution on Discrete Terms*, Zenodo
(2026), DOI 10.5281/zenodo.21197044.

[6] C. Horstmann, *π on Discrete Terms*, Zenodo (2026), DOI
10.5281/zenodo.21205368.

*All exact claims — the path counts, the diffusion identity, the envelope convergence, and the kernel's symmetry — are pinned by `test_genesis_ix.py` and re-verified on every revision.*

<div class="volhead">VOLUME X · RELATIVITY AND THE STANDARD MODEL</div>

*The serial count set against the relativity of simultaneity: an account
of what is derived, what is read, what is adopted from the established
record, and what remains open.*

A series built on a substrate that does one thing at a time must meet
one of the best-confirmed principles of physics: that simultaneity is
relative and no preferred frame exists. A serial count *is* an ordering,
so the two conflict directly, and this volume addresses the conflict.
The position taken is the neo-Lorentzian one, and its provenance is
given. A preferred order may exist provided it is undetectable from
within, all internal instruments being made of the counted stuff and
deforming identically. That position is empirically equivalent to
special relativity, and John Bell endorsed it as legitimate pedagogy.
Modern cosmology uses the microwave background's rest frame as a de
facto preferred frame whenever it quotes a peculiar velocity. From the
construction itself comes the speed limit: motion is re-addressing, one
address-step per tick at most, so the existence of an unpassable c is
structural rather than postulated. Conditionally, with the premise
declared: suppose a moving system's operation budget partitions
quadratically between translation and internal evolution — the same
squaring as the Born port, the program's one squaring everywhere. Then
the internal rate is exactly √(1 − β²). That is the Lorentz factor from
budget accounting, with the light-clock geometry recovered and not
assumed. There is also an exactness result. The dilation is exact
rational arithmetic precisely on the Pythagorean triples: at
three-fifths of c clocks run at exactly four-fifths, at 5/13 exactly
12/13, at 8/17 exactly 15/17. This is the same Euclid identity that
carries the series' two-slit duality, now marking the frames where the
count closes exactly. Regarded as readings: the equivalence principle as
one conserved count. Inertial and gravitational mass are the same
commitment count, so their equality is a bookkeeping identity and needs
no further explanation. Then gravitational time dilation as budget
consumption by committed structure, and mass-energy equivalence as
commitment-budget convertibility. Inherited whole: the experimental
record — muon lifetimes, Ives–Stilwell, Hafele–Keating, GPS, light
bending, Shapiro delay, the binary pulsar, LIGO — whose quadrupole-led
signal Volume II read as a count of the conservation laws. And the
geometric machinery of general relativity as the envelope's finest
instrument. The numerical value of c belongs to the unit system. Since
1983 the metre is defined by fixing c, so the number is a fact about the
ruler and not about light. The dimensional boundary states the
principle: no dimensionless construction yields a dimensionful
magnitude. It gives a clean division of every quantity in the series
into counted structure and chosen ruler, developed with its own tables
in this volume's closing section. There are three open problems. The
Lorentz group — boosts as structure, the spinor representations,
Wigner's classification — is the series' deepest unbuilt object. Its
structural counterpart exists: the ring's full return at eight with the
Midy antipode at four, position restored at the half and identity only
at the whole, the form of the double cover, machine-pinned. A
counterpart is not a derivation. The second is the exact undetectability
of the count's order, why the Lorentzian concealment is exact and not
approximate. The third is the conversion E = mc² as a theorem and not a
reading. In sum: five results derived or verified, four readings
declared, the record inherited, and three open problems stated. Free
parameters: none. Continuum objects: none claimed as physical.

## 1 · The conflict, stated

**Postulate C says the substrate does one thing at a time.** An ordering
of all events is therefore central to the construction.

**Special relativity says that no experiment detects a preferred
frame.** Its observable content is confirmed beyond serious doubt, and
its standard interpretation extends the statement to: *no preferred
order exists.*

**There are two possible outcomes: a derived reconciliation, or an exact
statement of the gap.** The conflict is direct. This volume does some of
each and marks which is which.

## 2 · The position taken: Lorentz's, with Bell's endorsement and cosmology's practice

**The form of the reconciliation is Lorentz's, and it predates
Einstein.** A preferred order may exist provided it is *undetectable
from within*, because every rod, clock and observer is made of the
counted substrate and deforms identically under motion through the
count.

**Lorentzian relativity is empirically equivalent to Einstein's in all
confirmed content [1].** The difference is interpretive: for Einstein no
such frame exists, and for Lorentz it exists and is undetectable.

**John Bell endorsed the Lorentzian pedagogy explicitly [2].** Bell,
whose theorem bounds the account of Volume VIII, wrote: *"the facts of
physics do not oblige us to accept one philosophy rather than the
other."*

**Modern cosmology uses a preferred frame in practice.** The microwave
background defines a rest frame, the frame in which the relic light is
isotropic, and every peculiar-velocity measurement in the literature
quotes motion *with respect to it* [3]. The universe, as observed, *has*
a preferred frame; the principle says only that local dynamics cannot
find it from inside.

**The construction's position: the count is the order.** The order is
globally manifest, in the microwave background, and locally
undetectable, in the dynamics. The second half is an open problem, taken
up in Section 6.

## 3 · What is derived: the limit, and the conditional Lorentz factor

**A maximum speed exists as a matter of structure.** Motion, on discrete
terms, is re-addressing (Volume IX), and the register admits at most one
address-step per tick. Exceeding that would require completing more
operations than the meter admits, the same clause that barred the
supertasks. The existence of c is not a postulate here; it is the meter
read kinematically.

**Lemma (conditional).** Suppose a moving system's operation budget
partitions *quadratically* between translation and internal evolution.
Then with β the translational fraction, the internal rate is

<div style="text-align:center; margin:12pt 0;">√(1 − β²)<span style="float:right;">(1)</span></div>

— the Lorentz factor, from budget accounting, with the light-clock
geometry [4] recovered and not assumed.

**The premise is declared and not derived, and it has a basis.** The
quadratic composition of complementary readings is this program's proven
port law, the duality theorem of Volume VIII,

<div style="text-align:center; margin:12pt 0;">P² + V² = 1<span style="float:right;">(2)</span></div>

exact over the amplitude grid — and the budget identity

<div style="text-align:center; margin:12pt 0;">rate² + β² = 1<span style="float:right;">(3)</span></div>

is *formally the same identity*.

**What remains open is one identification.** It is not "why quadratic"
in general, since the port squares and that is a theorem. It is
narrower: the identification of the pair (translation, internal
evolution) as port-complementary. That one identification stands between
the construction and the whole of special relativity's kinematics.

**The lemma gives time dilation as budget arithmetic.** In quadrature, a
system moving at β uses the fraction β of its budget for translation and
has √(1−β²) for internal evolution.



**The triple lattice (pinned).** The dilation is *exact rational arithmetic* precisely on the Pythagorean triples:

| β | internal rate |
|---|---|
| 3/5 | 4/5 |
| 5/13 | 12/13 |
| 8/17 | 15/17 |
| 20/29 | 21/29 |

The same Euclid identity that carries the two-slit duality (Volume VIII)
marks the frames where the count closes exactly.

**From the established record.** The muon reaching the ground, the
airborne caesium clocks and the corrections of the GPS constellation [5]
are the confirmed record, adopted whole; the lemma gives it a structural
basis.

## 4 · What is read: one count, and gravity as consumption

**Reading: the equivalence principle as a bookkeeping identity.**
Inertial mass resists re-addressing; gravitational mass sources and
responds to the field. In the construction both are the same number
because both are the same conserved count: the commitment count of
Volume I's third operation.

**Their measured equality holds to parts in 10¹⁵ [6].** On this reading
it is an identity and not a coincidence: *there is only one count.* It
is declared as a reading here, and the companion record on gravitation
derives it [10].

**Reading: gravitational time dilation as budget consumption.**
Committed structure consumes operations to persist; near mass, more of
the local budget is in use and fewer ticks remain for clocks, so clocks
run slow near mass. The reading is qualitative here and consistent with
every confirmed test; the companion record on gravitation gives the
derivation [10].

**Reading: E = mc² as convertibility** between the commitment count and
the operation budget. The reading names the open problem, and Section 6
reports how far it is resolved.

## 5 · What is inherited, and what belongs to the unit system

**From the established record.** The experimental record of both
relativities is inherited whole: dilation in flight and orbit, the
bending, the delay, the pulsar's spin-down, and the gravitational waves
whose quadrupole-led form Volume II read as a count of the conservation
laws. So is the geometric machinery of general relativity, the most
developed instrument of the envelope, whose operational content is
unchanged.

**The numerical value of c belongs to the unit system.** Since 1983 the
metre is *defined* so that

<div style="text-align:center; margin:12pt 0;">c = 299,792,458 m/s &nbsp; exactly &nbsp; [7]<span style="float:right;">(4)</span></div>

— the number is a fact about the ruler, not about light.

The dimensional boundary, that no dimensionless construction yields a
dimensionful magnitude, places the number outside what can be derived.

The boundary yields a clean division of every quantity in the series
into counted structure and chosen ruler, developed with its own tables
in §8.

## 6 · The three open problems

**Open problem one: the Lorentz group.** Boosts as structure; the spinor representations; Wigner's classification [8].

**The construction holds a structural counterpart of the group.** It is
the ring's full return at eight ticks with the Midy antipode at four:
position is restored at the half and identity only at the whole, the
form of the double cover (machine-pinned). A counterpart is not a
derivation. The group itself, derived from the count, is the series'
deepest unbuilt object.

**Open problem two: exact undetectability, resolved in one space
dimension.** The identification is this: translation and internal
evolution are the two components of the phase field —

<div style="text-align:center; margin:12pt 0;">β = k/ω, &nbsp;&nbsp; rate = μ/ω<span style="float:right;">(5)</span></div>

— under the register's wave operator, which is *second-order*: the port's square.

**The quadratic law is that operator's own dispersion, exact in the sine
domain:**

<div style="text-align:center; margin:12pt 0;">4sin²(ω/2) = 4sin²(k/2) + μ²<span style="float:right;">(6)</span></div>

machine-pinned — reducing in the accessible domain to

<div style="text-align:center; margin:12pt 0;">ω² = k² + μ²<span style="float:right;">(7)</span></div>

— whence

<div style="text-align:center; margin:12pt 0;">rate² + β² = 1<span style="float:right;">(8)</span></div>

as the dispersion identity, not a premise.

**The massless mode of the unit-ratio lattice is dispersionless at every
wavenumber to the zone edge.** Light travels at exactly c on the
lattice, with zero deviation, in one space dimension (pinned to 10⁻¹²).
For light in one space dimension the concealment is therefore exact, as
a matter of structure.

**What remains open is the off-axis case in three space dimensions.**
That is the known place where propagation on a cubic lattice deviates,
and it is where the program's registered test of Lorentz invariance
applies. The open problem is now confined to that case.

**Open problem three: E = mc², resolved within the model.** From the
same dispersion:

<div style="text-align:center; margin:12pt 0;">ω = γμ<span style="float:right;">(9)</span></div>

in the accessible domain — pinned: ω/μ matches γ to a part in 10⁶. Energy *is* the phase rate; mass *is* the rest phase rate; their equivalence is the dispersion identity at k = 0.

What remains is to carry the statement from the model's phase field to
the full construction.

There are thus three open problems, each with a stated form. The results
obtained are the lemma of Section 3, the triple lattice, and the
structural limit.

## 7 · Summary, and the series' close

Sections 3 and 6 established the structural speed limit, the conditional
Lorentz factor with its premise displayed, the triple-lattice exactness,
and the double-cover counterpart; each is machine-pinned. Declared as
readings: the equivalence principle as one count, gravitational time
dilation as budget consumption, and mass-energy equivalence as
convertibility. The experimental record entire, and the envelope's
geometry, are adopted from the established record; the number that
defines the metre belongs to the unit system. Three problems remain open
— the group, the concealment, and the conversion — each in the form
Section 6 states.

**Free parameters: none. Continuum objects: none claimed as physical.**

**The series' claims end with this volume.** *In Pure Mathematics*
closes the set with the theorems alone, with no physical terms, for the
reader who will judge the structure first. In this volume the conflict
was addressed, part of it was resolved, and the remainder is stated as
three open problems.


## 8 · Units, rulers, and magnitudes

**The separation of dimensionful quantities is a classification, and it
can be shown as a table.** Since 2019, every unit of the SI is defined
by counting a phenomenon and fixing conversion constants [7]:

| unit | what is counted | fixed constants |
|---|---|---|
| second | 9 192 631 770 caesium hyperfine ticks | Δν |
| metre | the addresses light crosses per tick | c, Δν |
| kilogram | commitments per tick, through h | h, c, Δν |
| ampere | elementary charges per second | e, Δν |
| kelvin | mode-average bookkeeping | k, h, Δν |
| mole | entities counted | N_A |
| candela | a weighted photon count | K, h, Δν |

**When units change, only the ruler changes.** Nothing in that table is
this program's proposal: it is the International System's own
definition. The ruler is a counted phenomenon together with a
convention, and the content of every physical statement lies in
dimensionless ratios.

**Proposal: magnitudes are derived as ratios of phenomena, times one
stated convention.** The ratios are pure numbers, within the dimensional
boundary, and the convention names the reference.

**The atomic scales already form such a web, and its links are pure
numbers:**

| link between rulers | exact form |
|---|---|
| Rydberg against the Compton frequency, R∞/(m_e c/h) | α²/2 |
| Bohr length against the Rydberg, a₀ · R∞ | α/4π |
| Hartree against the rest energy, E_h/m_e c² | α² |

**Three domains of measurement — spectroscopic, mechanical, chemical —
interconvert through powers of the fine-structure constant.** The
conversion factors between the rulers are dimensionless, and they are
the kind of number this series derives.

**A question of magnitude factors into a uniquely determined ratio and a
stated convention.** Only the convention changed in 2019, and only the
convention ever changes.

The suite verifies these ratios and carries them to the hydrogen
hyperfine line. The leading-order expression lies fifty-six parts per
million above the measured frequency, the difference being the known
proton-structure and higher-order corrections.

## References

[1] H. A. Lorentz, *Electromagnetic phenomena in a system moving with
any velocity smaller than that of light*, Proc. R. Neth. Acad. **6**
(1904) 809; A. Einstein, Ann. Phys. **17** (1905) 891.

[2] J. S. Bell, *How to teach special relativity*, in *Speakable and
Unspeakable in Quantum Mechanics*, Cambridge (1987).

[3] Planck Collaboration, *Planck 2018 results I* — the CMB dipole and
the peculiar-velocity frame.

[4] R. P. Feynman, R. B. Leighton, M. Sands, *The Feynman Lectures on
Physics*, vol. I ch. 15 — the light clock.

[5] B. Rossi, D. B. Hall, Phys. Rev. **59** (1941) 223; J. C. Hafele, R.
E. Keating, Science **177** (1972) 166; N. Ashby, *Relativity in the
Global Positioning System*, Living Rev. Relativ. **6** (2003) 1.

[6] MICROSCOPE Collaboration, Phys. Rev. Lett. **129** (2022) 121102 —
the equivalence principle at 10⁻¹⁵.

[7] BIPM, *Le Système international d'unités*, 9th ed. (2019) — the
definitions of the units, and the metre of 1983.

[8] E. Wigner, *On unitary representations of the inhomogeneous Lorentz
group*, Ann. Math. **40** (1939) 149.

[9] C. Horstmann, *Navier–Stokes: A Solution on Discrete Terms*, Zenodo
(2026), DOI 10.5281/zenodo.21197044.

[10] C. Horstmann, *Gravity on Discrete Terms*, Zenodo (2026), DOI
10.5281/zenodo.22087599.



*All exact claims — the triple lattice, the conditional identity, the
rest form, and the double-cover counterpart — are pinned by
`test_genesis_x.py` and re-verified on every revision.*†

<div class="vnote">† Version 2 printed a reference entry as a paragraph of this volume’s text, with two entries numbered [5] in its list; the entry is removed and the list renumbered.</div>

<div class="volhead">THE MATHEMATICAL COMPANION</div>

*The axioms, the objects, the theorems, and the one-line figure that carries the whole construction — with complete instructions for mechanical reproduction of every exact claim in the series.*

This volume states the structure of the series explicitly. It carries
the postulate and its physical warrant, the register theorem, and the
objects — the seed, the period, the two orders. It carries the operation
classification that separates the workless from the working, the clock,
and the meter. Its centerpiece is the line theorem: the demonstration
that the entire construction is carried by a single closed line. The
enneagram figure — nine points on a circle, the six-point path
1→4→2→8→5→7→1 and the triangle 3-6-9 — is here a diagram that carries a
theorem. The theorem is this: the digit path of 1/p in base b is a
single closed stroke through distinct points if and only if the reptend
is full. That is, the number of reptend classes (p−1)/ord_p(b) equals
one, which is to say the base is a primitive root modulo p. Seven is the
least prime for which base ten draws one line; thirteen, by contrast,
requires two strokes (076923 and 153846), and eleven requires five. For
the pair (7, 10) the figure is complete in a sense made exact in five
machine-pinned parts. The line is unicursal: six distinct points, one
closed stroke. Its points are exactly the doubling orbit modulo nine, so
the line covers one face of the seed entirely. Its complement among the
nine residues is exactly the triangle {3, 6, 9}, the conservation axis
the line never touches. The figure's point reflection (d ↔ 9−d) is
Midy's theorem drawn: antipodal digits sum to nine because the
reflection is the half-period shift. And the first operation of Volume I
is the involution between the figure's two Hamiltonian cycles, the
positional line 142857 and the multiplicative line 124875. One closed
curve therefore carries five things simultaneously. They are the state
space (the nine residue classes), the dynamics (the line is the orbit of
the shift), and the symmetry (the reflection that is Midy). Then the
conservation structure (the untouched triangle) and the first operation
(the two-cycle involution). That is states, motion, symmetry,
conservation and genesis in one closed stroke. No other physical theory
is known to the author whose complete content is a single closed line.
For comparison, the standard model's content is a Lagrangian of dozens
of terms, a Feynman diagram carries one process, and a Dynkin diagram
carries a symmetry and no dynamics. Whether another such figure exists
is an open question. The volume closes with the reproduction manual. It
gives the test suite's architecture: exact rational arithmetic in the
core, floating-point only in clearly marked comparison layers. It gives
the registry of declared choices, in which every selection is entered,
and the projection grammar governing how every value claim in the series
must be stated. It gives the full theorem-to-test index for Volumes
I–III. A reader can then verify every exact claim in the series by
running the public suite, independently of the author.

## 1 · The postulate, the warrant, the register

**Postulate C.** Physical process is the succession of distinguishable states of a finite counting system.

**The postulate's finiteness is that of quantum mechanics.** By the
Margolus–Levitin theorem a system of average energy E completes at most
2ET/πℏ orthogonal transitions in time T [1].

**The register theorem** (Volume I; pinned). Positional representation
requires a base. The construction's two mechanisms are residue
bookkeeping modulo 9, preserved under digit summation (b ≡ 1 mod 9), and
the complete first full period (b a primitive root mod 7). Base ten is
the least base that carries both, and such bases are rare. The carriers
below eighty:

<div style="text-align:center; margin:12pt 0;">10, &nbsp; 19, &nbsp; 73<span style="float:right;">(1)</span></div>

The theorem is conditional on the mechanisms, and the mechanisms are the
postulate's own content, its commitments to 2 and 3.

## 2 · The objects

**The seed** is the pair (2, 3): the first two counts past unity,
incommensurable: 2ᵃ = 3ᵇ has no solution, by parity. Their near-misses
at the successive convergents:

<div style="text-align:center; margin:12pt 0;">|2ᵃ − 3ᵇ| = 1, 5, 17, 13, 139<span style="float:right;">(2)</span></div>

**The period** is the first complete period — six = 2×3 digits, the least prime whose reciprocal exhibits the whole cycle:

<div style="text-align:center; margin:12pt 0;">1/7 = 0.142857…<span style="float:right;">(3)</span></div>

with Midy's complement property [2]:

<div style="text-align:center; margin:12pt 0;">142 + 857 = 999<span style="float:right;">(4)</span></div>

**The three orders** of the period's six digits:

| order | the six digits | what it is |
|---|---|---|
| positional | 1, 4, 2, 8, 5, 7 | as division writes them |
| multiplicative | 1, 2, 4, 8, 7, 5 | the doubling orbit mod 9 |
| harmonic | 1, 2, 4, 5, 7, 8 | the leading digits ⌊10k/7⌋ of the six sevenths — the hexad in ascending order, skipping the triad |

The first two are the figure's Hamiltonian readings, joined by the conserved involution; the third is an order of the fractions, not a path on the figure.

**The harmonic order folds at Midy's axis.** The fold separates the six
sevenths into the lower three and the upper three, with leading digits
{1, 2, 4} below and {5, 7, 8} above, and every quantity of the
separation is exact:

| the fold | value | note |
|---|---|---|
| ratio of sums, upper to lower | (15/7) / (6/7) = 5/2 | the reduced parts sum to the seed: 5 + 2 = 7 |
| the whole | 3 | split 5/7 : 2/7 *of itself* — in quanta of 3/7, five above, two below |
| the centroids | 5/7 and 2/7 | themselves a Midy pair, summing to one; their ratio again 5/2 |
| the committed whole | 3.000000, exact | truncate all six at the period and round: exactly the upper three round, and their three round-ups close the truncation deficit of all six — 3 × 10⁻⁶ — to the unit |
| the general law | committed total = (p − 1)/2, every odd p | the rounders are the upper Midy half; their count equals the deficit in last-digit units, always |
| the family | upper/lower = (3p − 1)/(p + 1) | endpoints 2 (at p = 3) and 3 (in the limit); the value 5/2, the family's midpoint, is attained only at p = 7 |

The whole equals the family's limit — both are 3 — if and only if p = 7: only at the seed does the system's total coincide with its family's ceiling. All rows are machine-checked in the accompanying suite (`test_five_halves_fold.py`).

**The classes mod 9 are the hexad and the triad.** The hexad is the
doubling orbit and the triad is the axis; together they exhaust the
nonzero residues:

<div style="text-align:center; margin:12pt 0;">hexad {1, 2, 4, 5, 7, 8} &nbsp;·&nbsp; triad {3, 6, 9}<span style="float:right;">(5)</span></div>

## 3 · The Line Theorem — one stroke carries the whole

**Definition.** The *digit path* of 1/p in base b is the closed sequence of its period digits, drawn as a path on the circle of residues. The path is *one line* if it is a single closed stroke through distinct points. The *reptend class count* — the number of distinct cycles into which the p−1 nonzero numerators fall — is:

<div style="text-align:center; margin:12pt 0;">(p−1)/ord<sub>p</sub>(b)<span style="float:right;">(6)</span></div>

**Theorem M1 (the line).** *The figure of 1/p in base b is one line if and only if the reptend class count is one — that is, iff b is a primitive root modulo p.*

**Seven is the least prime drawing one line in base ten.** Thirteen
draws two (076923 and 153846); eleven draws five.

*In the seed's least-action selection, the first prime with a full
period, "full" is the one-stroke property.*

**Reptend classes of four primes in base ten (pinned):**

| prime p | reptend classes (strokes) |
|---|---|
| 7 | 1 |
| 13 | 2 |
| 17 | 1 |
| 11 | 5 |

**Theorem M2: the complete figure, five parts — all pinned.** For (p, b) = (7, 10):

1. **Unicursal:** the path 1→4→2→8→5→7→1 passes once through six distinct points and closes.
2. **Coverage:** its six points are exactly the doubling orbit modulo 9 — the line exhausts one face of the seed.
3. **Complement:** the residues it never touches are exactly {3, 6, 9} — the triangle; the conservation axis stands outside the motion.
4. **Symmetry = Midy:** the figure's point reflection d ↔ 9−d equals the half-period shift: antipodal digits sum to nine. *Midy's theorem is the figure's mirror symmetry, drawn.*
5. **Genesis:** the first operation of Volume I — the involution 142857
  ↔ 124875 — is precisely the map between the figure's two Hamiltonian
  cycles: the positional line and the multiplicative line.

**The figure therefore carries five things in one closed curve.** They
are the state space (nine residues), the dynamics (the line is the
shift's orbit), the symmetry (the reflection that is Midy's), the
conservation structure (the untouched triangle), and the origin
operation (the two-cycle involution). That is states, motion, symmetry,
conservation and genesis in one stroke.

**The dynamics along the line is invertible, the workless face.** The
figure is therefore unitary in both senses of the word: one, and
norm-preserving.

**No other physical theory is known to the author whose complete content
is a single closed line.** The standard model's content is a Lagrangian
of dozens of terms with nineteen or more measured inputs; a Feynman
diagram carries one process per drawing; a Dynkin diagram encodes a
symmetry group and no dynamics, states or conservation structure.

Whether another such figure exists is an open question. If one exists,
the comparison will be instructive.

## 4 · The operations, classified

**Definition (the two faces).** Every operation of the construction has
one of two faces, and the criterion is exact: **workless = invertible**;
**working = many-to-one**.

| face | criterion | the operations | the cost |
|---|---|---|---|
| workless | invertible | shift, clock, the tick, the transform-involution, the reflection | no information lost, no Landauer cost [3] |
| working | many-to-one | rounding, the digit-root cascade, the readout | information erased, its Landauer heat mandatory |

Conservation laws belong to the invertible operations, and the arrow of
time is the accumulation of irreversible ones.

The first operation of the universe is workless, and the first working
operation is the origin of matter (Volumes I, III).

## 5 · The clock and the meter

**The clock is the 3-step on the 8-ring.** It visits all eight positions
and closes at

<div style="text-align:center; margin:12pt 0;">lcm(3, 8) = 24<span style="float:right;">(7)</span></div>

accumulating a deficit per cycle: a cycle plus a carry is a clock, and the carry is the tick.

**The meter is the Margolus–Levitin bound: operations per unit time are
bounded by energy.**

**The companion paper's Theorem 1′, the universal form, turns the bound
into the impossibility of any infinite sequential schedule in finite
time.** In the companion paper it bars a physical Navier–Stokes
singularity; in this series it guarantees that every cascade is of
finite depth.

## 6 · The theorem-to-test index (Volumes I–III)

| claim | where | pinned by |
|---|---|---|
| register theorem (10, 19, 73) | I §2 | `test_chosen_three.py::test_base_ten_is_the_unique_least_register` |
| two orders; transform = doubling orbit | I §3 | `test_genesis_i.py::test_the_two_canonical_orders` |
| the involution (first op free) | I §3 | `test_genesis_i.py::test_the_first_operation_is_free` |
| the conserved count ±18, net 0 | I §3 | `test_genesis_i.py::test_the_first_ledger` |
| incommensurability 2ᵃ ≠ 3ᵇ | I §2 | `test_genesis_i.py::test_the_contest_never_closes` |
| commitment ladder; depth-3 = ×1001/1000 | I §5 | `test_genesis_i.py::test_the_commitment_ladder` |
| escapement lcm(3,8) = 24 | I §4 | `test_genesis_i.py::test_time_needs_the_carry_and_the_ring` |
| pointing theorem (cardioid unique single-null) | II §3 | `test_genesis_ii.py::test_the_cardioid_is_the_unique_single_null` |
| cusp ladder (m nulls at order m) | II §4 | `test_genesis_ii.py::test_the_cusp_ladder` |
| the square 1 + cos2θ = 2cos²θ | II §4 | `test_genesis_ii.py::test_the_quadrupole_is_the_dipole_squared` |
| charge table unique; hydrogen neutral | III §2 | `test_charge_forcing.py` (5 tests) |
| the chain rest/echo/split; seed tie | III §3 | `test_genesis_iii.py::test_the_particle_state_chain` |
| proton charge count net 1, gross 5/3 | III §5 | `test_proton_ledger.py` (6 tests) |
| abundance 1/7 → Y = 1/4 | III §6 | `test_genesis_iii.py::test_primordial_abundance` |
| wiring: 45 cells from one rule | III §7 | `test_vertex_rule.py` (5 tests) |
| Line Theorem M1, M2 (five parts) | Companion §3 | `test_enneagram_line.py` (6 tests) |

## 7 · The reproduction manual

**The suite accompanying the series is public and runs with one command,
`python3 -m pytest verify/`.** It is kept at
github.com/thefirsthorstmann/g-theory-verify, and its architecture
enforces the series' standards mechanically.

**The core is exact.** All structural claims are integer and rational
arithmetic (`fractions.Fraction`); no floating point exists in any exact
result.

**The comparison layer is marked.** Wherever a claim touches a measured
value, the test is explicitly a comparison-layer test, and the measured
inputs are flagged for verification at their sources.

**Every selection the construction makes is a named entry in one
registry.** The base, the seed divisor, the rounding rule and the rest
are entered there, each with its justification and its open questions.

**Every value claim in the series is stated in one form, the projection
grammar.** It gives the claim's structural address, its exact rest
value, and its unfolding operation by operation, each operation
classified by face. It gives the observed difference with its rationale,
the density of alternatives, and the least-action selection of every
choice it touches. A validator enforces the form, so a claim that cannot
complete it does not enter the corpus.

**The series' predictions are held in an executable registry.** Every
prediction carries a falsification band, an adjudicating experiment, and
a horizon, and the suite audits the registry itself. A prediction that
fails is recorded as refuted and is not reinterpreted. The program then
uses the miss to find why the construction failed, and a revised value
enters as a new registration under its own date.

The finite arithmetic of the series is also formalized in Lean 4 with
Mathlib, in the same repository. Forty-six theorems of this book are
proved there, among them the register theorem, the charge table, the
filling order and Bell's bound for outcomes written in advance.

**Every exact claim in this series can be verified by any reader,
independently of the author.** That is the series' whole standard of
authority.†

<div class="vnote">† Version 2 cited the suite as a count of tests that run in seconds; a count goes stale at every push. The suite is cited without a count.</div>

**The companion records of the series are public:** Navier–Stokes, DOI 10.5281/zenodo.21197044; π, DOI 10.5281/zenodo.21205368; the registry of predictions, DOI 10.5281/zenodo.21206818; Sevenths, DOI 10.5281/zenodo.21206863; the Enneagram, DOI 10.5281/zenodo.21206948; Zero and Infinity, DOI 10.5281/zenodo.21209363; the Vanishing Point, DOI 10.5281/zenodo.21209420; the Fine-Structure Constant, DOI 10.5281/zenodo.21211050; Schrödinger's Piano, DOI 10.5281/zenodo.21211076; Gravity, DOI 10.5281/zenodo.22087599; and the further records listed in the corpus guide, The Falsification Schedule, DOI 10.5281/zenodo.22119549.

**Version 3 (October 2026) follows the series glossary.** Rest value, measured value and perturbation offset replace the terms of version 2, the parts of the book are called volumes throughout, paragraph heads state what their paragraphs establish, and measured values are re-read at their sources. In Volume VII the distance of the Hubble ratio from 13/12, quoted in version 2 as four parts in ten thousand, came from a rounded input and is restated with its uncertainty, and the registered value 70.05 is stated. Changes of substance from version 2 are marked † and noted where they occur.

## References

[1] N. Margolus, L. B. Levitin, Physica D **120** (1998) 188.

[2] E. Midy, *De quelques propriétés des nombres et des fractions
décimales périodiques*, Nantes (1836); standard treatments in Hardy &
Wright, *An Introduction to the Theory of Numbers*.

[3] R. Landauer, IBM J. Res. Dev. **5** (1961) 183; C. H. Bennett, IBM
J. Res. Dev. **17** (1973) 525.

[4] C. Horstmann, *Navier–Stokes: A Solution on Discrete Terms*, Zenodo
(2026), DOI 10.5281/zenodo.21197044.

*This volume's own claims are pinned by `test_enneagram_line.py` and the index of §6.*

<div class="volhead">IN PURE MATHEMATICS</div>

*The series' theorems, with no physical terms — definitions, statements,
proofs, and the mechanical suite that re-verifies them.*

Fourteen theorems in elementary number theory, combinatorics, and
analysis, with proofs, each machine-verified by a named test in the
accompanying suite. The subjects: the multiplicative structure of
base-ten arithmetic modulo small primes. The unicursal figure of the
first full-period prime and the involution between its two Hamiltonian
cycles. The exact arithmetic of rounding a repeating decimal. A
two-ratio semigroup whose magnitude ranking reproduces a well-known
empirical ordering term for term. The null structure of first-order
trigonometric families. A variance identity that grounds diffusion in
enumeration. The impossibility of infinite sequential schedules under a
positive stage-time floor. And the rational points of the unit circle.
Nothing below requires or mentions any interpretation. The volume exists
so that the structure can be judged by itself, before the physical
reading.

## 0 · Conventions

**Notation.** ℤ, ℚ as usual; (ℤ/n)* the multiplicative group of units modulo n; ord_n(b) the multiplicative order of b in (ℤ/n)*; F(a,b) the fraction a/b in lowest terms; C(n,k) the binomial coefficient.

**Every claim marked ▸ is pinned by a named test in the accompanying
suite, `verify/`.** The suite uses exact rational arithmetic in its core
and floating point only in explicitly marked comparison assertions.

## 1 · The register

**Theorem 1.** *Among integer bases b ≥ 2, the least satisfying both* (i) *b ≡ 1 (mod 9)* *and* (ii) *ord₇(b) = 6* *is*

<div style="text-align:center; margin:12pt 0;">b = 10<span style="float:right;">(1)</span></div>

*the only such bases below 80 are 10, 19, 73.* ▸

*Proof.* (i) restricts to b ∈ {10, 19, 28, 37, 46, 55, 64, 73, …}. For (ii):

| b | b (mod 7) | ord₇ |
|---|---|---|
| 10 | 3 | 6 |
| 19 | 5 | 6 |
| 28 | 0 | undefined |
| 37 | 2 | 3 |
| 46 | 4 | 3 |
| 55 | 6 | 2 |
| 64 | 1 | 1 |
| 73 | 3 | 6 |

∎

*Remark.* Condition (i) is equivalent to: digit sums preserve residue classes mod 9. Condition (ii) is equivalent to: the decimal (base-b) period of 1/7 is maximal.

## 2 · Incommensurability and the near-miss ladder

**Theorem 2.** *The equation*

<div style="text-align:center; margin:12pt 0;">2ᵃ = 3ᵇ<span style="float:right;">(2)</span></div>

*has no solution in positive integers.* ▸

*Proof.* The left side is even, the right odd. ∎

**Definition.** The *near-miss ladder* is the sequence |2ᵃ − 3ᵇ| evaluated at the convergents of log₂3:

<div style="text-align:center; margin:12pt 0;">(a, b) = (3,2), (5,3), (6,4), (8,5), (11,7), &nbsp; giving &nbsp; 1, 5, 17, 13, 139<span style="float:right;">(3)</span></div>

▸

## 3 · The period, and Midy's complement

**Theorem 3.** *ord₇(10) = 6, and the period of 1/7 is 142857. Its digit set is the orbit of the doubling map x ↦ 2x on the units (ℤ/9)\*, namely {1, 2, 4, 5, 7, 8}. The half-period shift complements each digit to 9:*

<div style="text-align:center; margin:12pt 0;">142 + 857 = 999<span style="float:right;">(4)</span></div>

▸

*Proof.* The order divides 6 and direct computation excludes 1, 2, 3. The digit set is inspection. For the complement: 10³ ≡ −1 (mod 7) since 7 | 1001, so shifting the repeating expansion by three places sends the remainder r to −r (mod 7), whence the shifted expansion is the nines-complement of the original. ∎

**Remark (the leading-digit order).** The digit set {1, 2, 4, 5, 7, 8} is presented in ascending order by the six fractions themselves: the first digit of k/7 is ⌊10k/7⌋, which runs

<div style="text-align:center; margin:12pt 0;">⌊10k/7⌋ = 1, 2, 4, 5, 7, 8 &nbsp; (k = 1, …, 6)<span style="float:right;">(5)</span></div>

monotone in k and skipping exactly the multiples of three among 1–8. So the reptend's six digits carry three natural orderings:

| ordering | sequence | what it reads |
|---|---|---|
| positional | 142857 | one of the two Hamiltonian readings of the line theorem's figure |
| multiplicative doubling-orbit | 124875 | the other Hamiltonian reading |
| ascending *harmonic* | 124578 | the order in which the six sevenths sit as nodes along a string |

## 4 · The line theorem, and the complete figure

**Definition.** The *digit path* of 1/p in base b is the closed sequence of period digits drawn on the circle of residues; it is *one line* if it is a single closed stroke through distinct points. The *class count* is the number of cycles into which the map r ↦ br (mod p) partitions (ℤ/p)*:

<div style="text-align:center; margin:12pt 0;">class count = (p − 1)/ord<sub>p</sub>(b)<span style="float:right;">(6)</span></div>

**Theorem 4 (the line).** *The figure of 1/p in base b is one line iff the class count is 1, i.e., iff b generates (ℤ/p)*. In base ten:*

| p | lines | note |
|---|---|---|
| 7 | one | the least such prime |
| 13 | two | the cycles of 076923 and 153846 |
| 11 | five | — |

▸

**Theorem 5: the complete figure, p = 7, b = 10.**

*(i) The path*

<div style="text-align:center; margin:12pt 0;">1 → 4 → 2 → 8 → 5 → 7 → 1<span style="float:right;">(7)</span></div>

*is unicursal — six distinct points, one closed stroke.*

*(ii) Its point set equals the doubling orbit of Theorem 3.*

*(iii) Its complement in {1,…,9} is exactly {3, 6, 9}.*

*(iv) The point reflection d ↦ 9 − d equals the half-period shift (Theorem 3).*

*(v) The map holding positions 1 and 4 fixed and reversing the interior pairs —*

<div style="text-align:center; margin:12pt 0;">142857 ↦ 124875<span style="float:right;">(8)</span></div>

*— is an involution carrying the positional cycle onto the multiplicative cycle, with displacements*

<div style="text-align:center; margin:12pt 0;">(42 → 24, 57 → 75) = (−18, +18), &nbsp; net 0, &nbsp; invariant pair-sum 99<span style="float:right;">(9)</span></div>

▸ (five named tests)

*Proof.* (i)–(iii) inspection; (iv) is Theorem 3's complement read geometrically; (v) direct computation: the map applied twice is the identity, and 124875 is the doubling orbit written as digits. ∎

## 5 · Exact rounding, and the two multipliers

**Theorem 6.** *Rounding 1/7 to k decimal places multiplies it by exactly*

<div style="text-align:center; margin:12pt 0;">1 + 10⁻³ at k = 3 (since 7 | 10³ + 1), &nbsp; 1 − 10⁻⁶ at k = 6 (since 7 | 10⁶ − 1)<span style="float:right;">(10)</span></div>

*at k = 4, 5 the excesses are 3·10⁻⁴ and 2·10⁻⁵ respectively.* ▸

**Theorem 7: the two multipliers of the width-3 register.** *For any three-digit integer a: a · 1001 is the concatenation a‖a, and a · 999 = (a−1)‖(1000−a), whose halves sum to 999. Moreover*

<div style="text-align:center; margin:12pt 0;">1001 = 7·11·13, &nbsp; 999 = 27·37, &nbsp; 10⁶ − 1 = 999 · 1001<span style="float:right;">(11)</span></div>

*and*

<div style="text-align:center; margin:12pt 0;">1/7 = 143/1001, &nbsp; 143 · 999 = 142857<span style="float:right;">(12)</span></div>

▸

*Proofs.* a·1001 = 1000a + a; a·999 = 1000(a−1) + (1000−a); the factorizations and identities are computation. ∎

## 6 · The escapement

**Theorem 8.** *Since gcd(3, 8) = 1, the walk k ↦ k + 3 on ℤ/8 is transitive with period 8, and the joint cycle of step-3 against period-8 closes at*

<div style="text-align:center; margin:12pt 0;">lcm(3, 8) = 24<span style="float:right;">(13)</span></div>

▸

## 7 · A unique solution, and a multiplicity scan

**Theorem 9.** *The linear system*

<div style="text-align:center; margin:12pt 0;">m·q₁ + m·q₂ + q₃ + q₄ = 0, &nbsp; q₁ − q₂ = 1 = q₄ − q₃, &nbsp; q₄ = 0<span style="float:right;">(14)</span></div>

*has, for each m, the unique solution*

<div style="text-align:center; margin:12pt 0;">q₂ = (1−m)/2m, &nbsp; q₁ = q₂ + 1, &nbsp; q₃ = −1, &nbsp; q₄ = 0<span style="float:right;">(15)</span></div>

*at m = 3 this is*

<div style="text-align:center; margin:12pt 0;">(2/3, −1/3, −1, 0)<span style="float:right;">(16)</span></div>

*and m = 3 is the only positive integer for which q₁, q₂ have denominator 3.* ▸

*Proof.* Substitution gives the solution. Since gcd(m − 1, 2m) = gcd(m −
1, 2), the denominator of (1−m)/2m in lowest terms is m when m is odd
and 2m when m is even, so it equals 3 only at m = 3. ∎†

<div class="vnote">† The second step of this proof is restated in version 3; the step as printed in version 2 was garbled.</div>

## 8 · A two-ratio semigroup and an empirical ordering

**Theorem 10.** *Define, for integer pairs (n, ℓ) with 0 ≤ ℓ < n ≤ 7 drawn from the standard nineteen labels,*

<div style="text-align:center; margin:12pt 0;">k = n − ℓ − 1, &nbsp; V(n, ℓ) = 1296 · (2/3)^⌊k/2⌋ · (5/6)^(2ℓ + (k mod 2))<span style="float:right;">(17)</span></div>

*Then the nineteen values are distinct, and ranking them in descending order yields the sequence whose (n+ℓ, n)-lexicographic monotonicity holds throughout; in particular*

<div style="text-align:center; margin:12pt 0;">V(4,0) = 720 > 625 = V(3,2), &nbsp; V(4,3) = 15625/36 > 1250/3 = V(5,2)<span style="float:right;">(18)</span></div>

*the four values V(n, 0) with n odd occupy ranks 1, 4, 9, 16, and the cumulative totals 2Σ(2ℓ+1) at the ℓ = 1 completions are*

<div style="text-align:center; margin:12pt 0;">10, 18, 36, 54, 86, 118<span style="float:right;">(19)</span></div>

▸ (five named tests)

*Proof.* Finite and mechanical; the suite performs it. ∎

## 9 · Null structure of first-order families

**Theorem 11.** *For a, b ≥ 0, the function a + b·cos(mθ) on [0, 2π) has no zeros if a > b, exactly m zeros if a = b, and exactly 2m if a < b > 0. In particular the m = 1 equal-mix (the cardioid) is the unique single-null member of its family, and*

<div style="text-align:center; margin:6pt 0;">1 + cos 2θ = 2cos²θ<span style="float:right;">(20)</span></div>

*identically.* ▸

*Proof.* Zeros require cos(mθ) = −a/b ∈ [−1, 0); equality gives the m antipodal solutions; strict inequality two per period of cos(mθ). The identity is the double-angle formula. ∎

## 10 · Diffusion as enumeration

**Theorem 12.**

<div style="text-align:center; margin:6pt 0;">Σₖ C(n,k)(n − 2k)² = n·2ⁿ<span style="float:right;">(21)</span></div>

*for every n ≥ 1; equivalently the mean of (n−2k)² under the exact path count is n.* ▸

*Proof.* Write n − 2k = Σᵢ sᵢ over sign vectors s ∈ {±1}ⁿ with k negatives. Then Σₛ(Σᵢsᵢ)² = Σₛ[n + Σ_{i≠j} sᵢsⱼ] = n·2ⁿ, the cross terms vanishing because for i ≠ j each of the four sign combinations occurs equally often. ∎

**Remark ▸.** De Moivre's limit:

<div style="text-align:center; margin:12pt 0;">C(2n,n)/4ⁿ · √(πn) → 1<span style="float:right;">(22)</span></div>

the suite pins the convergence at n = 100 and its tightening at n = 400.

## 11 · No infinite schedule under a stage-time floor

**Theorem 13.** *Let (τₙ) be any sequence of positive stage durations with Σ τₙ < ∞ and infinitely many stages. Then τₙ → 0; hence for every t_min > 0 there is an N with τₙ < t_min for all n ≥ N, and a process whose stages each require duration ≥ t_min completes at most N of them.*

*Separately: since*

<div style="text-align:center; margin:12pt 0;">Σ₀ᴺ 8ⁿ = (8^{N+1} − 1)/7<span style="float:right;">(23)</span></div>

*while any linear budget grows as c·N, the demand exceeds every linear supply beyond an explicit rank.* ▸

*Proof.* The first is the necessary condition for convergence of a
series; the second is the geometric sum against Bernoulli's inequality.
The observations are elementary; their consequences lie outside this
volume. ∎

## 12 · The rational circle

**Theorem 14.** *The rational points of x² + y² = 1 with x, y > 0 are exactly*

<div style="text-align:center; margin:12pt 0;">((a²−b²)/(a²+b²), 2ab/(a²+b²)) &nbsp; over integers a > b ≥ 1<span style="float:right;">(24)</span></div>

*— Euclid's parametrization — and in particular*

<div style="text-align:center; margin:12pt 0;">(3/5, 4/5), &nbsp; (5/13, 12/13), &nbsp; (8/17, 15/17), &nbsp; (20/29, 21/29)<span style="float:right;">(25)</span></div>

*lie on the circle.* ▸

*Proof.* Classical; the listed points are computation. ∎

## 13 · Closing note

**The fourteen theorems are parts of one object.** Individually they are
elementary; the volume's single observation is structural.

**Each theorem connects to the others through the same pair of
integers.** The register of Theorem 1 holds the period of Theorem 3,
whose figure is Theorem 4's one line and whose symmetry is Theorem 3's
complement. Its two cycles are exchanged by Theorem 5's involution, its
rounding arithmetic is Theorem 6, and its register multipliers are
Theorem 7. So it continues through the ladder, the semigroup, the null
families, the walk, the schedule bound and the circle.

Removing any one theorem from the suite shows which of the others depend
on it: the dependency graph is the object.

What the object *is*, whether a structure of arithmetic only or of
something more, is the question the other eleven volumes address; this
volume leaves it aside.

*Every ▸ corresponds to a named test in the accompanying suite; the
index mapping theorems to tests is in the Mathematical Companion, §6.*

<div class="volhead">DEFINITIONS</div>
*The musical vocabulary of these volumes, and the construction's own
terms, for the reader without musical training. Every musical object
below is arithmetic first; the instrument merely makes the arithmetic
audible.*

**octave** — the doubling: the interval from a frequency to twice itself (ratio 2/1). On these pages the octave is also the register's carry step — two at one place is one at the next.

**whole tone** — the interval 9/8, the gap between the first two scale
steps; the electroweak carriers of Volume IV stand one whole tone apart.

**semitone (Limma)** — the Pythagorean half-step, 256/243 = 2⁸/3⁵ — pure powers of two against pure powers of three. The diatonic scale's two half-step gaps sit at Mi–Fa and Si–Do.

**comma** — any small remainder between two routes to nearly the same
pitch. The **Pythagorean comma** (3¹²/2¹⁹) is the residue of twelve
fifths against seven octaves. The **septimal comma** (64/63 = 2⁶/(3²·7))
is the gap between the two musical sevenths — the step from the ratios
of 2 and 3 to those of 7, carried by Volume IV's held chord and the
Higgs construction alike.

**cent** — the standard logarithmic measure of interval size: 1200 cents to the octave, 100 to the equal-tempered semitone.

**just intonation** — tuning by exact whole-number ratios (3/2, 5/4, 9/8) rather than by equal division; the tuning of these volumes throughout.

**equal temperament** — the modern keyboard's compromise: twelve equal semitones of 2^(1/12), in which no interval but the octave is an exact ratio.

**solfège** — the syllables Do, Re, Mi, Fa, Sol, La, Si for the seven scale degrees. Do is the **tonic** (the root), Mi the **mediant** (the third), Sol the **dominant** (the fifth), Si the **leading tone** — the seventh degree, a half-step below the upper Do.

**fifth · fourth · third** — the intervals 3/2, 4/3 and 5/4: the simplest ratios after the octave, and load-bearing structures throughout these volumes.

**the two sevenths** — the seventh of stacked fifths, 16/9, and the harmonic seventh of the overtone series, 7/4; their disagreement is the septimal comma.

**tritone** — the half-octave, √2 in equal temperament: the point diametrically opposite the tonic on the tone circle — the **antipode**. In Volume VIII's Bell section, the carry fires there.

**harmonic (partial, overtone)** — a mode of a vibrating string: a
frequency at a whole-number multiple of the fundamental. A played string
sounds all of them at once.

**node** — a point of a vibrating mode that does not move. Mode m has a node at position p/q exactly when q divides m — the arithmetic behind Volume VIII's collapse rule.

**chord** — several modes sounding as one body; in Volume VIII, an entangled pair is one harmonic read at two places.

**monochord** — the single stretched string of the ancient demonstrations, divided by ratio; the construction's root instrument.

**reptend** — the repeating block of a decimal expansion: 1/7 = 0.142857 142857…, whose six-figure block is the construction's harmonic constant.

**Midy complement** — the theorem that, for a prime denominator, the two halves of an even-length reptend sum to all nines: 142 + 857 = 999. The pivot of every such pair is half the all-nines — the register's own center, one octave down.

**hexad** — the six-member family {1, 2, 4, 5, 7, 8}: the reptend's digit set, the six carriers of the flow lattice, and the closure period of the seed's right angle.

**enneagram** — the nine-pointed figure whose internal line traces the
reptend of the sevenths and whose untouched triangle {3, 6, 9} is the
neutral axis. It is established as a theorem in the Mathematical
Companion and in the companion record *The Enneagram Is a Theorem*.

**register** — a positional counting system read as an instrument: places, digits, and the carry between them.

**tonal center (the key)** — the degree against which every other degree
is heard as displaced: the reference that need not be sounded in order
to organize what is sounded. In these volumes, the register's fixed
stratum holds the office, and gravitation is its physics — the Interlude
and the companion record on gravitation.

**carry** — the register's one operation that moves between places (ten units at one place becoming one unit at the next). It conserves the count, changes only the writing, and has capacity of exactly one bit. Volume VIII's Bell section rests on it.

**octave promotion** — the carry read musically: two units at one mode becoming one unit at the mode above.

**commitment (rounding)** — the many-to-one act by which a held structure becomes a definite value; the construction's word for what measurement, condensation and freezing have in common. Irreversible, and dissipating its Landauer heat.

**rest value, measured value, perturbation offset** — the two tiers of
every constant in this program, and their difference. The **rest value**
is the exact arithmetic object, reached only by calculation. The
**measured value** is what an instrument returns, displaced from rest by
the energy and context of its realization. The **perturbation offset**
is the difference between the two — as a played string sounds sharp of
its rest pitch and settles toward it while the excitation decays.

**octave descent** — cooling as halving: the thermal history of Volume IV, counted as fifty octaves from the electroweak scale to the microwave background.

**cymatics** — the standing patterns a driven medium draws (Chladni's sand figures): eigenmode node-lines made visible — the medium's counting, seen.

**pinned** — asserted by a named test in the public suite, which is
re-run on every revision.

<div class="volhead">INDEX</div>
<div class="idx">
<p>antipode — 17, 53, 55, 57, 58, 65, 68, 72, 75, 83, 86</p>
<p>baryon — 22, 25, 28, 48, 49, 50, 52</p>
<p>Bell — 4, 53, 56, 58, 59, 60, 65, 66, 71, 78, 86, 87</p>
<p>Born — 53, 55, 65</p>
<p>cardioid — 12, 13, 15, 17, 20, 45, 77, 83</p>
<p>carry — 5, 9, 10, 13, 36, 37, 53, 57, 58, 59, 76, 86, 87</p>
<p>charge table — 4, 13, 21, 22, 23, 27, 77, 78</p>
<p>chord — 30, 32, 33, 34, 53, 56, 58, 59, 60, 86</p>
<p>collapse — 4, 14, 35, 43, 44, 46, 47, 53, 54, 59, 60, 86</p>
<p>comma — 30, 32, 33, 34, 41, 86</p>
<p>commitment — 5, 6, 7, 10, 11, 12, 13, 14, 22, 23, 24, 25, 27, 31, …</p>
<p>decoherence — 53, 55, 59, 60</p>
<p>dipole — 4, 5, 6, 9, 12, 13, 15, 16, 18, 19, 20, 35, 37, 40, …</p>
<p>enneagram — 4, 72, 87</p>
<p>entanglement — 53, 55, 56, 60, 86</p>
<p>exactly half — 53, 55, 58, 59, 60</p>
<p>fine-structure — 4, 70</p>
<p>forces, order of appearance — 35</p>
<p>Gauss — 61, 63, 64</p>
<p>gravitation — 4, 14, 15, 18, 19, 21, 35, 36, 37, 41, 42, 43, 45, 47, …</p>
<p>helium — 4, 22, 23, 26, 27, 28, 40</p>
<p>hexad — 8, 48, 50, 57, 73, 74, 87</p>
<p>Higgs — 27, 30, 32, 59, 86</p>
<p>hydrogen — 13, 22, 23, 24, 25, 27, 28, 30, 33, 34, 38, 39, 40, 48, …</p>
<p>Landauer — 5, 8, 10, 12, 13, 14, 53, 54, 55, 60, 76, 78, 87</p>
<p>Limma — 86</p>
<p>Line Theorem — 4, 72, 74, 77, 81</p>
<p>Madelung — 38, 39, 40, 41, 42</p>
<p>measured value — 4, 26, 48, 51, 58, 77, 87</p>
<p>Midy — 5, 7, 11, 14, 58, 65, 68, 72, 73, 74, 75, 78, 87</p>
<p>monopole — 4, 5, 6, 9, 11, 12, 14, 15, 16, 18, 19, 20, 21, 23, …</p>
<p>muon — 24, 65, 67</p>
<p>neutrino — 4, 11, 14, 22, 23, 25, 27, 29</p>
<p>neutron — 22, 24, 26, 27, 29</p>
<p>node — 8, 53, 54, 56, 59, 61, 62, 81, 86, 87</p>
<p>octave descent — 12, 28, 30, 31, 87</p>
<p>octave promotion — 53, 57, 87</p>
<p>periodic table — 4, 34, 38, 40, 41, 42</p>
<p>perturbation offset — 4, 22, 26, 27, 28, 87</p>
<p>plasma — 4, 10, 13, 28, 30, 31, 32, 33, 34</p>
<p>proton — 22, 24, 26, 27, 29, 36, 70, 77</p>
<p>quadrupole — 15, 18, 19, 20, 21, 65, 68</p>
<p>recombination — 4, 6, 28, 30, 31, 33, 34</p>
<p>register — 4, 5, 6, 7, 9, 10, 11, 12, 14, 21, 22, 23, 24, 25, …</p>
<p>relativity — 4, 13, 18, 52, 53, 59, 60, 64, 65, 66, 67, 68, 71</p>
<p>reptend — 38, 40, 50, 72, 74, 75, 81, 87</p>
<p>rest value — 4, 22, 25, 26, 27, 28, 44, 48, 49, 50, 51, 52, 53, 57, …</p>
<p>seed — 5, 6, 7, 10, 22, 24, 25, 32, 38, 39, 41, 45, 51, 54, …</p>
<p>septimal — 30, 32, 33, 34, 86</p>
<p>sevenths — 4, 8, 48, 49, 51, 52, 58, 73, 74, 81, 86, 87</p>
<p>Standard Model — 13, 29, 49, 64, 65, 72, 75</p>
<p>tonal center — 4, 35, 36, 37, 87</p>
<p>tritone — 86</p>
<p>Tsirelson — 57</p>
<p>two-tier — 57</p>
<p>vacuum — 31, 48, 49, 50, 52</p>
<p>wavefunction — 26, 54, 62</p>
<p>whole tone — 28, 30, 31, 32, 34, 35, 36, 41, 86</p>
</div>


<div class="copyright" style="margin-top:80pt">Copyright<br>Christian Horstmann · July, 2026 · version 3, October 2026<br>thefirsthorstmann@gmail.com<br>All rights reserved</div>
