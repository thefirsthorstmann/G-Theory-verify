%%TITLE: Gravity on Discrete Terms
%%SUBTITLE: Gravitation as the tonal center of a discrete harmonic system: its anomalies, its coupling, and a dimensionless cosmological ratio derived from the arithmetic of a positional register
%%META: Christian Horstmann · thefirsthorstmann@gmail.com · August 23rd, 2026 · manuscript for the public record
%%ABSTRACT: Gravitation differs from the other interactions in five respects that no accepted framework derives: it carries a single sign, it couples in proportion to mass while accelerating all bodies equally, it cannot be screened, it radiates first at quadrupole order, and its coupling is some forty-five orders of magnitude weaker than the others. This paper derives all five from the arithmetic of a positional register, together with the inverse-square law and the absence of a central singularity. The construction uses one repeating reciprocal, 1/7, and a theorem that its multiples fall short of closure by exactly one unit at the register's depth; that shortfall is identified with the gravitational deficit. The multiplier of the shortfall is identified with the tick rate of matter's rest-frame clock, so gravity's relation with mass begins at the acquisition of a rest frequency — through the Higgs mechanism for the elementary masses and through confinement for the hadrons. The coupling follows as αG(e) = 5/(2¹⁵¹ − 1), a repeating binary fraction of forced period 151 that adjusts no parameter. It gives G = 6.6735902(41) × 10⁻¹¹ m³ kg⁻¹ s⁻², 106 parts per million below the CODATA-2018 central value and inside the unresolved spread of the experiments, so convergent metrology decides it either way. A separate dimensionless chain fixes the ratio of the cosmological horizon to the nucleon at 10⁴²; with one declared length this yields the nuclear saturation density and the Hubble constant, and both are also obtained from measurement alone with nothing declared. Seventeen conditions under which the account fails are stated, and every arithmetic claim is verified in a public suite at github.com/thefirsthorstmann/g-theory-verify.

---

<div style="page-break-before:always"></div>

| | |
|---|---|
| **Summary of the position** | 3 |
| **1 · Introduction** | 5 |
| **2 · Terminology** | 9 |
| **PART I · THE FORM** | 11 |
| 3 · The mathematical basis: the reptend of 1/7 on the residue circle | 11 |
| 4 · The closure defect is a theorem: the force is attractive and unipolar | 12 |
| 5 · Source proportionality and the equivalence principle from one congruence | 13 |
| 6 · The station of unit residue: the subdominant carries the reptend comma | 13 |
| 7 · The mechanism: the closure defect is the gravitational potential | 15 |
| 7.1 · The rest clock: where gravity enters its relation with mass | 16 |
| 7.2 · Two experimental tests: the mass side and the clock side | 17 |
| 8 · The inverse-square law, first route: the all-nines integer as a projective coordinate | 18 |
| **PART II · THE INTERACTION** | 19 |
| 9 · The interaction event: unions occur only at carry boundaries | 19 |
| 10 · The interaction rate: bilinear in the two masses | 20 |
| 11 · The inverse-square law, second route: the carry rate against the cell size | 21 |
| 12 · No central singularity: the refinement census terminates | 22 |
| **PART III · THE COUPLING** | 24 |
| 13 · The coupling: αG(e) = 5/(2¹⁵¹ − 1), and the value of G | 24 |
| 13.1 · The hierarchy problem, read as the register's reference level | 27 |
| 14 · The cosmological chain: horizon over nucleon at 10⁴², the saturation density, and the expansion rate | 28 |
| **PART IV · THE CORRESPONDENCE** | 34 |
| 15 · The nine correspondences, each on an arithmetic pathway | 34 |
| **PART V · STANDING AND RELATION TO EXISTING THEORY** | 36 |
| 16 · The kinematics: the octave as a Lorentz boost | 36 |
| 17 · Relation to general relativity | 40 |
| 18 · The present state of the field, and what this account offers it | 41 |
| **PART VI · THE REMAINING REGIMES** | 44 |
| 19 · The dimension of space: the contact-count window at two, three and four | 44 |
| 20 · Orbits: Kepler's third law exact, and the precessing conic family | 46 |
| 21 · The strong field, the post-Newtonian order, and the structural accounts | 47 |
| 21.1 The horizon — 21.2 The circular-orbit landmarks — 21.3 What replaces the singularity — 21.4 The wave sector — 21.5 The rotating sector — 21.6 The second-order construction — 21.7 The quadrupole coefficient — 21.8 The dimension of space — 21.9 Relation to curvature-squared gravity — 21.10 The dimensional crossing — 21.11 Repulsion — 21.12 The quantization apparatus | 48 |
| 22 · Quantization reversed: integer sources, a finite spectrum, and the phase-blind readout | 71 |
| **23 · What would refute this paper** | 74 |
| **24 · Verification** | 77 |

<div style="page-break-before:always"></div>

## Summary of the position

Of gravitation's many perplexities the oldest is that it is unlike the
other forces: too weak, too universal, too one-sided, unquantizable,
unscreenable. There is even debate whether it is a force in the strictest
sense of the word. The claim of this paper is that the
complaint has the situation inverted. Gravitation is not a force that
fails to behave like the forces. It is the centre the forces are
referenced against: the unsounded reference of a discrete harmonic system,
carrying exactly the properties a centre must carry and no others. For
centuries musicians have used this exact phenomenon, because its literal
expression lives in their medium as what music defines as the tonal
centre — more commonly, the key. Stated as intuition it sounds like an
informal metaphor; stated rigorously in mathematics it proves to be
another thing altogether. This paper is the full exposition of how and why
harmonic structure has the capacity not only to describe gravitation but
to state what, phenomenally speaking, it is.

**The case in numbers.** The claim is technical and is checked at every
joint. The tonal claim is arithmetic before it is analogy. The subdominant's
register value on the root 24 is 7.999999; its shortfall of 10⁻⁶ is the
reptend comma of §4 by theorem, and §6 proves the subdominant is the only
station that can carry it. Fourier's theorem then makes a harmonic
reflection of gravitation the expectation rather than a surprise (§15).
From that arithmetic the paper derives the single sign, the equivalence
principle, the impossibility of screening, quadrupole-first radiation, and
the inverse square by two routes. The coupling follows as αG(e) = 5/(2¹⁵¹ − 1), giving G = 6.6735902(41) × 10⁻¹¹ m³ kg⁻¹ s⁻², 106 parts per million below the CODATA centre and inside the experiments' unresolved spread. Convergent metrology is the stated condition that refutes it. The
quadrupole coefficient is counted rather than fitted, a dimension over a
rank times the octave, and reproduces the double pulsar's orbital decay to
four parts in ten thousand. Every first-post-Newtonian parameter takes the
received value, the Nordtvedt parameter is exactly zero, and the rest
clocks obey the first law of binary mechanics, reproducing the
gravitational self-force series through third order with its π² term. The
horizon count carries the logarithmic coefficient −1, distinct from the
loop-quantum-gravity countings and stated as the discriminator. A
dimensionless chain fixes the horizon-to-nucleon ratio at 10⁴² and, with
one declared length, the saturation density 0.15993 fm⁻³ and the expansion
rate 70.05 km s⁻¹ Mpc⁻¹, both under declared watch conditions. The
electron's Planck hierarchy is the exact square √10 · 2⁻⁷⁶. The empirical structure is stated plainly. Where measurement has decided,
the account agrees with the received theory exactly. Where the account
differs — the value of G, the two chain numbers, the logarithmic
coefficient — measurement has not yet decided, and each difference carries
its stated condition of refutation. Every arithmetic statement re-derives in a public suite
of 2,671 tests, and seventeen stated conditions say what would refute the
account.

The account of gravitation given below covers the full scope set out in §1. Six accounts bear closures or first results, and the seventh is this assembly.
The outstanding items are named in their places rather than collected out of
sight. The vacuum term's magnitude stays unaccounted, since the coordinate
rule places it outside the equations as a constant of integration; its equation of state is settled at −1 exactly. The sharing profile's amplitude is a matter for experiment. The dimensional selection condition is an interval needing no optimum, with only the reason contact costs exactly
one three still outstanding. Only the dissipative two-body field carries no symmetry direction, and
there the flux is derived while the metric is numerical. The conservative binary keeps a helical count direction, where the rest clocks obey the first law of binary mechanics, and its dynamics are the received theory's through third post-Newtonian order. The position of the lepton ladder is reduced to one number, v/m_e = 481839.84 ± 0.12, which also fixes v/M_Planck and m_p/v. It matches no station of the register at fifteen standard deviations or better. The exact square carries the hierarchy ratio at a quarter of a
part per million, and the step a derivation still requires, an operation
placing the electroweak tick rate against the electron's, is stated in
§21.12. It remains open as the account's one unreduced number. One live constraint stands on it: the seated Higgs self-coupling makes the position equivalently the Higgs-to-electron ratio, and coming Higgs-mass precision decides that seat. Every class with one symmetry
or more — static, rotating, radiative and null alike — is exact. Completeness is claimed here in a defined sense: every open item is
recorded where it arises, with its bound and its route; every exact claim
re-derives mechanically in the public suite; and every identification
carries its stated condition of refutation. By that criterion the account
stands complete: open in five places, hidden in none.

<div style="page-break-before:always"></div>

## 1 · Introduction

Gravitation remains the only fundamental interaction without an accepted
microscopic account. General relativity describes it as spacetime curvature
and has passed every precision test applied to it, but it is not a quantum
theory, and attempts to quantize it encounter non-renormalizable
divergences. Several of its features are also described rather than
derived. The interaction carries a single sign. It couples in proportion to mass while
accelerating all bodies equally. It admits no screening, and it radiates first
at quadrupole order. Its coupling to the electron is some forty-five orders of
magnitude weaker than the electromagnetic coupling. Each of these is accommodated within the standard framework.
None follows from it.

Several research programmes have proposed that such features are
consequences of a more basic structure. Jacobson derived the Einstein field
equations from horizon thermodynamics together with the Clausius relation,
treating them as an equation of state rather than a dynamical law. Verlinde
recovered Newton's law from entropy gradients on holographic screens.
Information-theoretic treatments interpret gravitational attraction as a
process that reduces the informational complexity of matter distributions,
producing an entropic force. Discrete programmes — causal set theory among
them — replace the continuum manifold with a countable structure and
recover the manifold as an approximation. What these approaches share is
the position that the continuum description is emergent rather than
fundamental, and that the quantities appearing in the field equations are
statistical rather than microscopic.

This paper develops an account in that class. The structure proposed is
arithmetical rather than thermodynamic: a positional register in base ten,
carrying the reciprocal 1/7, whose repeating expansion is the unique cycle
in that base that loses no information. The relevant property of that expansion is a closure defect. Seven of its cycles do not sum to unity but fall short of it, and the defect is exactly one unit at the register's depth:

```
7 × 0.142857  =  0.999999  =  1 − 10⁻⁶
```

The shortfall is a theorem rather than an observation, and its sign is
fixed before any physical quantity is introduced. Laying the diatonic
octave on the smallest root that places every degree on a whole number,
which is 24, and evaluating the register's own division at each degree,
exactly one degree is short by one unit. It is the fourth, the subdominant:

```
   subdominant  =  24 / 3  =  8

   value in the register  =  7.999999

               shortfall  =  10⁻⁶
```

**Hypothesis.** The gravitational deficit is that shortfall, carried at that
degree, restoring toward a value it does not reach.

The paper argues for this hypothesis in three stages. Part I derives the
five features listed above, together with the inverse-square law and the
absence of a central singularity, from the shortfall and the geometry of
the register. Part III derives a value for the gravitational coupling and
compares it with measurement. Part VI treats the strong field, the post-Newtonian order, the two-body sector compared with general relativity, and the remaining regimes. Section 23 states seventeen
conditions under which the account fails, and every arithmetic statement is
verified in a public suite described in §24.

**A note on the vocabulary.** Musical terms appear throughout — degree,
octave, comma, interval, subdominant, dominant. They are used in their
exact sense in music theory and denote ratios of small integers. The fourth
degree of a diatonic scale is the ratio 4/3; a comma is a specific small
rational by which a cycle of intervals fails to close. Where a musical
statement is offered as interpretation rather than as arithmetic, it is
marked at the point it is made. Section 2 gives the complete correspondence
between the function names, the solfège syllables and the arithmetic
objects they denote.

**Defining the tonal center.** In a tonal system the centre is the degree against which every other degree is
heard as displaced. It is the reference that need not be sounded in order to
organize what is sounded. It is the point of repose toward which unstable
degrees resolve. And it is the one degree that cannot itself be the object of
that resolution.

**Why a tonal center.** The question is better put the other way: what
would prevent the tonal center from reflecting gravitation? Pitch falls
with mass and size. A string of greater mass per unit length vibrates lower at the same tension and length, and a longer string or a larger resonator lower still. An instrument reaches its low register with its heaviest and largest vibrating bodies, and the ordinary description of pitch as high and low is the report of that dependence. Every periodic motion
decomposes into integer multiples of one fundamental, and the tonal
functions name those ratios. Gravitation couples to everything that
carries energy and enters at the acquisition of a rest frequency (§7.1).
A system organized from below by mass and read in integer ratios is what a vibrating body and a gravitating one both are. Part IV states nine correspondences between them on explicit arithmetic pathways, each with what would refute it.

**What is classical here, and what is not.** An existing body of exact solutions must be reproduced by any proposed account of gravitation. This paper reproduces these: the Weyl class of 1917, the Ernst equation of 1968, the Einstein–Rosen cylindrical waves of 1937, Brinkmann's plane waves of 1925, and the unimodular formulation Einstein set down in 1919. Every one
is a solution class a relativist meets as a student, and every one is
reproduced here **exactly** rather than approximately — sixteen of sixteen
curvature components, in each of four sectors.

That reproduction is not the result. It is the test the account had to
pass, and an explanation that failed it would simply be wrong. The distinction: a paper offering new *results*
is judged by what it predicts that was not known, while a paper offering
an *explanation* is judged by whether the known follows from it. On the second axis, exact reproduction is the validation rather than a
shortfall, and the precedent is standard. Jacobson's 1995 recovery of the
Einstein equations from thermodynamics carried no new prediction whatever, and
is among the most-cited foundational papers in the subject. This paper is of
that kind, and is offered as such. What is put forward as new is three things
and no more.

**1. The objects are reached by counting rather than by geometry.** The
potential is a carry census, the time word a composition law about round
trips, and the spatial word a quadrature. They arrive at the classical
equations without being aimed at them.

**2. The dimension is selected by arithmetic.** Three is the only dimension
meeting all three of §19's conditions together: contact spellable in the
register's own two generators, refinement returning the sevenths wheel, and the
contact count doubling on both sides. The first two conditions alone admit
six as well, since 72 = 2³·3² is spellable and 2⁶ ≡ 1 (mod 7). The third
closes it, six's contact ratio being 9/5 rather than two.

**3. The coordinate rule is the unimodular condition.** It converts a stated
policy into a slot in the field equations, and makes the cosmological term a
constant of integration with an equation of state of exactly −1. It also
identifies this account's own clock, a count of carries defined in its first
chapter, with the physical clock canonical gravity is missing.

**Relation to earlier work on dimensionless constants.** Numerical
coincidence has a history in physics, and Eddington's derivation of the
fine-structure constant is its best-known instance. Mirowski's survey of
dimensionless constants treats that episode as one case in a recurring
pattern: an attempt to remove convention from measurement that terminates
in stipulation. The difference between that work and this one is
methodological, and it is worth stating precisely rather than claiming
greater care.

Eddington's construction proceeded without a governing principle. It
counted permutations of a matrix algebra, obtained 136, and was revised to
137 when measurement required it. The revision was available because
nothing in the construction forbade it: the target was the number, and the
route to it was chosen after the target was known.

The construction here is governed by a variational principle applied to a
structure fixed in advance. The figure's energy is the Dirichlet form introduced in §3, defined before any
physical quantity enters. The derived results follow from requiring that form
to be stationary: the inverse-square exponent in §8 and §11, the orbital
landmarks in §21.2, and the quadratic dependence of energy on rate. The structure those results
live on is the mode arithmetic of two and three, whose content is fixed by
the incommensurability of the two generators and admits no adjustment.
**A result that came out otherwise could not be repaired by changing an
integer, because none of the integers is free to change.** That is the
property Eddington's construction lacked, and it is the property that makes
the failure conditions in §23 meaningful rather than decorative.

**On the contingency of the base.** The wider charge in Mirowski's survey
is that any numeral base is culturally contingent. Here the answer is a
theorem rather than a preference. Nine seats requires 9 | b − 1; the
seven-cycle requires ord₇(b) = 6. Neither condition mentions a base. Their joint solutions are b ≡ 10 or 19 (mod 63), and ten is the least. A third condition, developed in the units companion, cuts the set further: every read must decide, with no self-complementary digit and no possible tie, and that requires an even base. Of the four admissible bases below one hundred it leaves ten and eighty-two, and ten remains the least. The base is not asserted to be natural; it is the smallest one that satisfies the conditions.

**On stipulation.** The 2019 revision of the SI stipulates all seven base
units and measures none of them, which is Mirowski's endpoint and is
correct. Where the verdict differs is that stipulation is not itself the
failure; unacknowledged stipulation is. One declared quantity, with every
other quantity a ratio, is what the boundary in §14 and the opening Summary permits, and
the declaration is carried openly through every result that follows.

A reader looking for new predictions in the exact sector will not find
them there and is not meant to. This is an account of what gravitation *is*, tested by whether it delivers
what gravitation *does*. The predictions it carries are enumerated in §23.
They live in the count, the vacuum term and the residual, rather than in the
classical solutions.

Physics has known for a century that gravity is the anomaly among the forces.
The table below states the anomalies as the literature states them, the
derivation this paper gives for each, and the name each has carried in music
for four centuries. Each row is a section of this paper; nothing in the right
column is doing any work the middle column does not do — the right column is
what the middle column *sounds like*.

| the anomaly, as physics states it | derived here from | the same fact, in the older vocabulary |
|---|---|---|
| couples to everything, in proportion to its source | the k-rotation identity: ride the figure k units and the shortfall is exactly k (§5) | no tone is outside the key |
| accelerates everything identically — the equivalence principle | the same identity: the relative shortfall is 10⁻⁶ for every k (§5) | transposition moves the whole key at once |
| one sign only: attracts, never repels | the shortfall theorem: short by exactly one, never over (§4); every generation decider rounds up (§6) | resolution pulls toward the tonic, never away |
| cannot be screened | the mirror's fixed point has no partner to oppose it (§3) | there is no counter-tonic |
| stands ~45 orders below the other couplings | the count: αG(e) = 5/(2¹⁵¹−1) — the lift alone on the 151-bit wheel, 149 octaves below the unit (§13) | the tonic is not a voice; a reference cannot be loud |
| radiates first at the quadrupole | the event ledger conserves the count and the translation fact conserves its flow — monopole and dipole channels shut by conservation — with the antipodal pair as the geometric setting (§3, condition stated) | the axis is a pair of poles |
| resists quantization | reversed: integer sourcing, finite spectrum, rational coupling on a wheel — nothing continuous left to quantize (§22) | just intonation is already the quantization; temperament is the continuum convention |
| orbits precess; exact closure is the exception | the comma: twelve fifths overshoot seven octaves by 531441/524288 (§15) | the circle of fifths never closes |

A reader who wants the shortest path: §4 (the shortfall theorem), §5 (source
and equivalence from one congruence), §9 (the interaction event derived), §13
(the number), §23 (what would refute all of it). Everything exact in this paper
re-derives itself in the public test suite in minutes, on any machine, and
section 19 maps every claim to its test.

**What derived means here.** Three kinds of statement appear
below, and each is named where it occurs. A *theorem* is proved and its proof
is checkable by hand or machine. An identification joins a proved structure to a physical office — the closure defect to the potential, the rounding excess to mass. Identifications are the load-bearing
joints of any physical theory, since force, here as everywhere, is identified
rather than deduced. Each is stated together with what would sever it. A *conjecture* is named as one and load-bearing for nothing.
There are no fitted parameters anywhere in the paper, and no constant is
adjusted to data at any point. Every numerical agreement below is therefore
either exact, accidental, or evidence. The construction is designed to reduce
the scope for accident as far as it can be reduced: with nothing adjustable,
an agreement cannot be arranged, and its significance is computed rather than
asserted.

## 2 · Terminology

Every term below is used technically. Nothing musical in this paper is
ornament: each name denotes an arithmetic object, and this table is the
complete dictionary a reader arriving from gravitational physics needs.

| term | what it denotes here |
|---|---|
| **reptend** | the repeating block of a decimal expansion — 142857 for 1/7 |
| **full-reptend prime** | a prime p whose reptend has the maximal length p − 1 (ten is a primitive root modulo p) |
| **the figure / the nine seats** | the nine nonzero residues on a circle, carrying the reptend's six-point line and the untouched triangle 3–6–9; used here purely as arithmetic |
| **Midy's theorem** | for a full reptend of even period, the two halves sum to all nines: 142 + 857 = 999 |
| **closure defect / the shortfall** | the amount by which a cycle falls short of closure — for the reptend, one unit in the register's last place; identified in §7 with the gravitational potential |
| **seat** | the integer address a value occupies — or misses; "the seat of Fa is 8" |
| **the register** | a positional numeral system treated as a physical record; **carry** — its overflow step, one digit turning the next; **held pair** — an integer register with a fractional register on the closed unit interval, the theory's notation for a record before commitment |
| **wheel** | a repeating fraction x/(2^k − 1): a block of k binary digits circulating forever — the theory's native way of placing a number in an exponent; the sevenths' own 1/7 is the master instance, and §13's coupling wheel is its binary counterpart |
| **scale degree** | the position of a tone in the diatonic scale, named by its harmonic function (see the table below); this paper uses function names throughout, since its claims concern function rather than pitch |
| **tonal center / tonic** | the reference tone defined in §1 — heard against, never required to sound |
| **dominant / leading tone** | Sol, the fifth degree, the strongest non-root station; Si, the seventh degree, the tone one semitone under the root that pulls hardest toward it |
| **diatonic** | the seven-degree scale structure the whole-number ratios seat |
| **just intonation** | tuning by exact small-integer ratios (3/2, 4/3, 5/4 …) — the exact column |
| **equal temperament** | the convention dividing the octave into twelve equal irrational steps so the circle of fifths closes by construction — the seating convention, not the arithmetic |
| **comma** | the small exact ratio by which cycles of just intervals fail to close — 531441/524288 for twelve fifths against seven octaves; 10⁻⁶ for the reptend at depth six |
| **descent** | an octave read downward through its ratios on a root: on 24, the values 24, 21, 16, 12, 8, 6, 3, 0 |
| **cadence / dominant seventh** | the resolving progression of tonal harmony; the chord Sol–Si–Re–Fa, whose resolution to the tonic is the strongest event in the practice |
| **pitch spiral** | the cycle of fifths drawn in log-frequency: twelve fifths overshoot seven octaves by the comma, so the circle never closes and the curve is a spiral |

**The organization and structure of the scale's degrees.** Music theory names a scale
degree by its harmonic function; the solfège syllables name the same
positions as pitches. Because every claim in this paper concerns function —
what a degree *does* in a resolution — the function names are used
throughout, and the syllables appear only where a table labels the descent.

| degree | function name | solfège | ratio *r* | 24*r* | 24(*r* − 1) |
|---|---|---|---|---|---|
| 1 | tonic | Do | 1/1 | 24 | 0 |
| 2 | supertonic | Re | 9/8 | 27 | 3 |
| 3 | mediant | Mi | 5/4 | 30 | 6 |
| 4 | **subdominant** | Fa | 4/3 | 32 | 8 |
| 5 | dominant | Sol | 3/2 | 36 | 12 |
| 6 | submediant | La | 5/3 | 40 | 16 |
| 7 | leading tone | Si | 15/8 | 45 | 21 |
| 8 | tonic (octave) | Do | 2/1 | 48 | 24 |

The final column, read upward, is the descent 24, 21, 16, 12, 8, 6, 3, 0.
It is the octave measured from the root rather than to it, and it is where
the subdominant's value of 8 comes from: r − 1 = 1/3 at the fourth degree,
so 24(r − 1) = 24/3 = 8. The four degrees whose r − 1 is a unit fraction are
the supertonic (1/8), the mediant (1/4), the subdominant (1/3) and the
dominant (1/2).

The fourth degree — the **subdominant** — is the carrier this paper
identifies with the gravitational deficit. Within the dominant seventh
chord it functions as the chordal seventh, and the interval it forms with
the leading tone is the tritone whose resolution defines the authentic
cadence.

Every musical name can be replaced by its arithmetic referent with nothing lost:
the subdominant is the ÷3 station of the descent, the comma its exact ratio, the
cadence the ledger of §9. The derivations have been checked under that
replacement.

# PART I · THE FORM

## 3 · The mathematical basis: the reptend of 1/7 on the residue circle

The structure underlying every derivation in this paper is stated here as
definitions and elementary facts, each with its reason attached.

**Defining the sevenths' reptend.** The decimal expansion of 1/7 repeats with
period six: 1/7 = 0.142857 142857…, reptend 142857.

**The reptend as geometry on the mod-9 circle.** Place the nine nonzero residues modulo nine at
equal angles on a circle and join the reptend's six digits in their order
of appearance, closing the last to the first. The result is a six-edge
closed path on the vertex set {1, 4, 2, 8, 5, 7}, together with the
untouched triangle {3, 6, 9}.

The facts the construction uses, each elementary:

1. The period is six because the multiplicative order of ten modulo seven
   is six: ord₇(10) = 6.
2. The digit set of the reptend is exactly the nonzero residues coprime to
   three. The multiples of three never appear, which is why the triangle
   3–6–9 stands untouched by the path.
3. Successive digits are successive states of one computation: with
   r₀ = 1, the k-th digit is ⌊10 rₖ / 7⌋ and rₖ₊₁ = 10 rₖ mod 7. The path
   is the orbit of the map x ↦ 10x (mod 7), read through its digits.
4. The reflection d ↦ 9 − d maps the path to itself. This is Midy's
   theorem of 1836 drawn as geometry: antipodal digits sum to nine because
   the two half-periods sum to 999.
5. Whether the six chords close into one path is governed by a
   divisibility criterion — the base must be a primitive root modulo the
   prime — treated in full in a companion volume. For seven in base ten
   it holds, and nothing beyond that fact is used here.

Everything in this paper is arithmetic performed on this object — the
reptend, its stations, its reflection, and its carry.





**The reflection's fixed points.** On the circle the reflection d ↦ 9 − d is the point reflection θ ↦ −θ (fact 4). On a rooted ring of nine seats it fixes exactly two places,
and the parity of nine forces their characters to differ:

- **the root**, 0°, occupied — seat 9;
- **the antipode**, 180°, *empty* — nine is odd, so no seat exists there; the
  point falls at the exact midpoint of the 4–5 gap.

**The fixed-point pair and its theorem.** Consider the figure's pair sector: the modes odd under the reflection, which is the sector this section's identification selects, with the condition stated. In every one of them the nine-cycle's Dirichlet energy has four
distinct frequencies, each doubly degenerate. The property that isolates the pair is **mirror-invariance, and
it must be stated as that rather than as immobility**: no seat has zero
amplitude in every mode, and a sentence claiming otherwise would be false.
What is true is that the reflection sends every seat to a different seat
except one, the root. Its only other fixed place is the antipode at 180°. The
oddness of nine leaves that place empty, so it is not a seat at all. Two fixed places, one occupied and one not, and no third.

The pair is therefore not dynamical content but reference structure: the place measured from and the place that cannot be occupied, half a turn apart. Every ordinary force in this theory sits on the orbit pairs — seats that come in couples, two-signed,
screenable. The fixed stratum is the one part of the figure that cannot carry a
relation, a sign, or an oscillation. Size is its only degree of freedom.

Two of gravity's signatures fall out of the fixed-point pair before any mechanism is named. **Nothing screens** what has no partner: screening is the cancellation
of a relation by its opposite, and a fixed point of the mirror has no opposite
to supply. And a source structure that is an *antipodal pair* rather than a
point has no dipole moment about its own center — the leading radiating
structure available to it is the quadrupole. (The second statement depends on identifying the radiating source structure with this pair. The condition is stated with its overshoot in the companion volume, and
nothing downstream leans on it.)

## 4 · The closure defect is a theorem: the force is attractive and unipolar

Multiply the reptend back by its prime:

```
142857 × 7 = 999999 = 10⁶ − 1
```

One short of the seat. Never over. And this is not a fact about seven:

**The shortfall and its theorem.** For every prime p whose reptend is full,

```
reptend × p  =  10^(p−1) − 1
```

so the product is short of closure by exactly one unit at the register's
depth: never more, never less, and never in excess. The minus sign is
constitutive, since the reptend is defined as

```
reptend  =  (10^(p−1) − 1) / p
```

and no case can therefore run in the other direction.

A value that sits below its seat restores upward. The restoring motion of
this arithmetic carries **one sign, with no free choice** — the first of
gravity's anomalies, obtained as a theorem about division.

The same one-signedness has a second aspect, and its strength must be stated
precisely, because a general law is available here and is not what obtains.
Midy's theorem pairs the halves of the reptend to nines:

```
142 + 857  =  999
```

**That pairing is general; the ordering is not.** For 1/13 = 076923 the
halves also sum to nines, but there the pairs run

```
0 + 9        7 + 2        6 + 3
```

with the second and third reversed, the high digit paired below the low. The
separation into a low half and a high half is a property of **seven**, not
a consequence of Midy, and it fails at 13, 17, 19, 23 and beyond.

What holds, and what the argument uses, is the fact about seven itself. Its
first half is all low and its second all high. The second half — 8, 5, 7 — is
precisely the set of deciders that determine rounding at the generation
depths. Every decider is high; every rounding goes up; every excess is
positive. By the route of direction (the shortfall) and by the route of tally
(the deciders), the arithmetic refuses to produce a negative pull. There is no
seat from which anything falls away.

## 5 · Source proportionality and the equivalence principle from one congruence

Ride the figure k units instead of one. The k-th multiple of the reptend is a
digit rotation of the reptend — the cyclic-number property — and its seat is
k·10⁶. The shortfall obeys a single identity:

```
k × 142857 × 7 = k·10⁶ − k          (k = 1 … 6)

absolute shortfall  =  k × 10⁻⁶     — proportional to the count carried
relative shortfall  =  10⁻⁶          — identical for every k
```

Those are two of gravity's signatures at once, from one line. The absolute
deficit is **proportional to the source**: twice the count, twice the force —
the linearity of weak-field gravitation in its source. The relative deficit is
**independent of the rider**: whatever k rides the figure, its fractional
displacement is the same — all things fall identically, which is the
equivalence principle. In this arithmetic the two are not separate facts to be
reconciled; they are the numerator and the denominator of the same congruence.

The musical analog of this is that transposition moves the whole key at once. No tone is displaced relative to the others by moving the key. The
displacement is of everything together, by the same interval. And no tone is
outside the key, because being a tone means standing in relation to the
centre.

## 6 · The station of unit residue: the subdominant carries the reptend comma

The nine-seat ring and the twelve-semitone ring share exactly one factor:

```
9 = 3²        12 = 2²·3        gcd(9, 12) = 3
```

The two systems touch at the number three, and one tone stands on it. The smallest root that lands a full octave descent entirely on integers is 24.
It is forced as the least common multiple of the just ratios' denominators (1,
8, 4, 3, 2, 3, 8, 1). On that root the descent runs 24, 21, 16, 12, 8, 6, 3,
0.

**Where the retardation is located.** Run the
register rule of the next paragraph at every station without amendment and
read the residues:

```
Do 24 → 3    Ti 21 → 0    La 16 → 2    Sol 12 → 5
Fa  8 → 1    Mi  6 → 6    Re  3 → 3    floor 0 → 0
```

**Exactly one station is short by residue one, and it is Fa.** That matters
because residue one is a retardation of exactly *one* unit at the register's
own depth — one comma, not an arbitrary shortfall. Every other retarded
station is short by two, three, five or six; Ti and the floor are multiples
of seven and are not retarded at all. The statement is a theorem rather than a table. The congruence n ≡ 1 (mod 7)
has one solution per seven consecutive integers. Of the four such values below
the root — 1, 8, 15, 22 — only 8 is a station of the descent. Its register value is 7.999999, and

```
8 − 7.999999 = 10⁻⁶ = 1 − 7·(0.142857)
```

— Fa's shortfall *is* the reptend comma of §4.

**The uniqueness of one rule at every station is a theorem.** A reader
may reasonably ask whether the route to that value was chosen to reach it:
divide a station by seven, truncate at the register's depth, multiply back
by seven, and some number always comes out. So state the route once and
run it, without amendment, at all eight stations of the descent. Because
the register's depth is the reptend's own period — 10⁶ ≡ 1 (mod 7) — the
answer is a theorem rather than a table of coincidences:

```
station n, through seven:   n − (n mod 7) × 10⁻⁶
```

The shortfall is the station's residue, counted in commas. Three outcomes
exhaust the descent. Where seven divides the station the route terminates
and there is no reptend at all: Si = 21 = 3·7 returns 21 exactly, dressless.
Where the residue is one the route returns the reptend and falls short by
**exactly one comma** — that is Fa, and in this descent Fa is the only
non-unit station there. Everywhere else the shortfall is a *multiple* of
the comma and therefore not the comma: Do 3, La 2, Sol 5, Mi 6, Re 3 —
so Sol's 11.999995, offered as an alternative, is five commas short and names
itself. The second reading — each tone by its own ratio rather than
through seven — yields no comma anywhere: Fa falls short by eight, La by
sixteen, the halvings by none.

**The license for the route: the two-ladder returns to its unit at eight.** Two has order three modulo seven, so 2³ = 8 is the first place the two-ladder
returns to the sevenths wheel's unit. The route through 8/7 = 1 + 1/7 is not a path
chosen for the subdominant. It is the sevenths wheel arriving home carrying its own
unit, and the subdominant's seat is where it lands. The
condition closes for every station of the form 2^a·3^b, since two is
three squared modulo seven: **2a + b ≡ 0 (mod 6)**. Within the descent it selects the unit and the subdominant and nothing else.
Beyond it the ports are 36, 64, 162, 288, 512 — one every three octaves on the
pure two-ladder. The three-ladder returns only at depth six, the reptend's own
period. What
this rule forbids is now checkable: a reptend comma claimed at any station
whose residue is not one is an arithmetic error, and the claim of Fa's
uniqueness stands or falls with the residue table above, pinned in
`verify/test_the_fa_license.py`. The tone that carries the
deficit is the tone standing on the one number the two rings share.

**The descent is unique, which the smallest numbers themselves prove.**
The roots whose descent stays whole are the multiples of 24, and the halving
chain 48 → 24 → 0 completes: the floor is reached, in whole numbers, with
nothing left over. The second family's chain, 144 → 72, holds whole numbers
for exactly one octave and can go no further — its half, 36, leaves the
integers at Si and Re. The working construction is a translation. The descent is the octave above
carried down seat by seat by the root: 48 → 24 landed on 24 → 0, the same gap
list, the whole numbers inherited. That is the self-similarity §16 identifies
with frame-indifference. The three
readings of the descent are set side by side, with the stations that leave
the integers marked:

| degree | r − 1 | by the spacing of 48 → 24 | by ratio, in the register | the 36-chain's half |
|---|---|---|---|---|
| tonic (Do) | 1 | 24 | 24 | 36 |
| leading tone (Si) | 7/8 | 21 | 21 | **31.5** |
| submediant (La) | 2/3 | 16 | 16 | 24 |
| dominant (Sol) | 1/2 | 12 | 12 | 18 |
| **subdominant (Fa)** | 1/3 | 8 | **7.999999** | 12 |
| mediant (Mi) | 1/4 | 6 | 6 | 9 |
| supertonic (Re) | 1/8 | 3 | 3 | **4.5** |
| tonic (Do) | 0 | 0 | 0 | 0 |

The first reading subtracts the spacings of the octave above: 3, 5, 4, 4, 2, 3, 3, the gaps of 48 → 24, whose sum is 24. It reaches the floor in whole numbers, with Fa at 8 exactly. The second computes the same stations through their ratios in the decimal register. Run the register rule at every station and the residues modulo seven are 3, 0, 2, 5, 1, 6, 3, 0. Fa alone is short by exactly one unit — 7 × 1.142857 = 7.999999, the reptend comma of §4. Every other retarded station is short by two, three, five or six of them. The third is the other family's half-chain: 144 → 72 holds
whole numbers for its own octave, but its half on 36 leaves the integers at
the leading tone and the supertonic. The whole-number descent to the floor
belongs to the 24-chain alone, and within it exactly one station resists
the register.

In tonal practice Fa is not a bystander. The subdominant is the seventh of the dominant chord, Sol–Si–Re–Fa. Its
tritone against the leading tone makes the V⁷ the strongest pull in tonal
music. The leading tone resolves upward to the tonic and the subdominant
downward to the mediant, as the root falls a fifth. The most gravitational event in harmony is carried
by the tone whose arithmetic is a permanent, one-signed shortfall.

## 7 · The mechanism: the closure defect is the gravitational potential

**Identification.** The gravitational potential is the closure defect of §4, carried at the station of §6, restoring toward the seat it never reaches.

This identification is stated in the form general relativity gave the
mechanism, not the form Newton did. In relativity nothing reaches out: mass
makes a deficit — of proper time, of closure — and what is called the force of
gravity is the deficit itself, read by whatever refuses to fall freely. A
free-falling accelerometer reads zero; the only measurable force in a
gravitational field points *up*, the ground refusing the fall. The arithmetic
above has exactly that structure and exactly that sign: a shortfall that exists
prior to any rider, a restoration that points upward toward the unreached seat,
a zero read by anything that simply rides.

What would sever the identification is stated in §23. What the identification does not do — by a theorem of this account rather than
a failure of it — is produce a dimensionful magnitude. Magnitudes enter in
Part III through one declared calibration. The shape of the mechanism is
complete without it.


### 7.1 · The rest clock: where gravity enters its relation with mass

The multiple k has so far been arithmetic. This subsection identifies it
physically, and the identification is marked as one: it joins the forced
arithmetic above to a physical office, and §23 states what severs it.

A mass is a clock. A body of mass m is a system whose internal dynamics
cycle at the Compton frequency ν = mc²/h, about 1.24 × 10²⁰ hertz for the
electron. This is not a picture but measured and institutional physics.
Atom interferometry has operated a clock referenced to a caesium atom's
Compton frequency; the interpretation of that experiment has been debated,
and nothing here rests on it. The institutional anchor is beyond debate:
since 2019 the kilogram itself is defined through the
Planck constant, so that a mass is determined by counting cycles. The
world's metrology already treats mass as a frequency; the register account
adds one clause to that treatment.

Physics owns two established mechanisms that give a system its rest
frequency. Confinement supplies roughly nine tenths of a nucleon's mass as
cycling energy, a share that survives in the chiral limit and needs no
Higgs. The Higgs condensate supplies the rest frequencies of the elementary
fermions and the weak bosons. Its full share of ordinary mass, measured by
the sigma terms, is near one part in ten. The bare quark masses alone are
one part in a hundred. The split between the sigma-term determinations is
an open metrological question, and nothing below depends on it. A massless
mode has no rest frame and no rest tick, but it still ticks in flight at
f = E/h, so it still gravitates in proportion to its energy; the rest tick
is the part that mass names.

The identification is then one sentence. **The multiple k is the tick
count.** The deficit per cycle is the same for every k (§5), so the deficit
current of a system is proportional to its tick rate, which is E/h. Gravity
enters at the acquisition of a rest frequency — through electroweak
symmetry breaking for the elementary masses, through confinement for the
hadrons — and the gravitational charge and the inertial mass are one count
read twice. Composition may shape the count, as the binding ledger measures
at the percent level. No composition can separate the two readings.

Each property derived earlier in this paper gains its physical narration at
once. Equivalence is an identity because both readings read one count. The
coupling follows energy and not only rest mass because everything with
energy ticks. The single sign holds because a shortfall has no negative,
and screening is impossible because no counter-tick exists. The weakness is the depth of the register the clock runs in: §13's coupling, five parts in 2¹⁵¹ − 1, is the last place of a 151-bit wheel. In the conservative two-body problem the same clock is the norm of the helical count direction and the mass's conjugate in the first law of binary mechanics, §21.9.

### 7.2 · Two experimental tests: the mass side and the clock side

The identification forbids two things, and both have been tested at high
precision by experiments built for exactly these questions.

**The mass side: free fall must be blind to what makes the ticks.** A tick
of Higgs provenance and a tick of chromodynamic provenance must carry the
same deficit. The MICROSCOPE test pair separates the provenances: titanium
and platinum differ in electron share by 3.3 × 10⁻⁵, in binding share by
8.5 × 10⁻⁴, and in nuclear Coulomb share by 2.0 × 10⁻³. The mission's final
result bounds the Eötvös ratio near 3 × 10⁻¹⁵, which holds any provenance
sensitivity of the deficit below parts in 10¹⁰ to 10¹² axis by axis. The
per-axis bounds assume no cancellation between axes; material pairs across
independent experiments close that loophole. A
coupling that counted constituents rather than energy is excluded by eleven
orders of magnitude. Antimatter obeys the same sign: the ALPHA-g experiment
observed antihydrogen to fall downward in 2023. The companion note *The
Eötvös Line* gives the full channel classification for any
composition-correlated signal.

**The clock side: the redshift must be blind to what makes the clock.** If
gravity attaches to ticks, a clock carried through a potential difference
must shift its rate exactly as its energy does, identically for every clock
species. This is the redshift leg of the equivalence principle, and its
record is long. Gravity Probe A confirmed the shift to seven parts in 10⁵
in 1976. The eccentric Galileo satellites confirmed it to a few parts in
10⁵ in 2018. Optical lattice clocks now resolve the shift across one
millimetre of height in a single sample. Co-located dissimilar clocks, tracked through the annual variation of the
solar potential, agree at the level of parts in 10⁵ and better. That is the
null form of the test. It states directly that the shift does not care what
kind of tick is being shifted. The ACES mission, launched in 2025, compares a laser-cooled
caesium clock on the International Space Station through a dedicated
microwave link with ground clocks that include cryogenic sapphire
oscillators, and targets the same comparison at two parts in 10⁶.

One honesty clause belongs beside the roster. None of these null results
distinguishes this account from general relativity, which predicts every
one of them; they distinguish both from any account in which provenance
matters. What distinguishes this account from general relativity is not a
null but a number: the derived coupling of §13 and the derived chain of
Part III, each of which measurement can refute.

The two tests are one statement seen from two sides. Free-fall tests
say the deficit ignores what makes the falling body's ticks. Redshift
tests say the rate shift ignores what makes the measuring clock's ticks.
Underneath both is the identity: the register counts cycles, and a cycle
is a cycle.

## 8 · The inverse-square law, first route: the all-nines integer as a projective coordinate

The shortfall at depth n is 10⁻ⁿ, and the seat's ratio to unity is

```
10ⁿ / (10ⁿ − 1)
```

which is superparticular at every stage — the form of every classical
consonance. Read the string of nines as what it is in one dimension of
description: a perspective coordinate. Standard perspective sends a true
distance d to an apparent coordinate d/(d+1), with the horizon at 1.
Solving for the depth-n shortfall,

```
   d / (d + 1)  =  1 − 10⁻ⁿ

              d  =  10ⁿ − 1
```

**The all-nines numeral is the extension.** The nines do not describe the
distance; they count it.

At depth n the deficit is 1/(d+1), an inverse *first* power, and the work of
a unit step against it is exactly quadratic in that amplitude — the
Dirichlet form of §3, with no approximation. The dictionary is fixed here
once, for every route in this paper:

```
   the deficit    is the amplitude,  the potential word,  inverse-first
   its square     is the intensity,  the force word,      inverse-second
```

An intensity that is the square of an inverse-first-power amplitude falls as
the inverse square:

```
deficit  ∝  1/(d+1)          intensity  ∝  deficit²  ∝  1/(d+1)²
```

Ten times the extension, one hundredth the intensity — a ratio statement, so
no unit enters. Part II reaches the same exponent by a second route, whose operation is
different — a gradient where this one squares. The scope of that agreement is
stated in §11: the two routes diverge
above one shared step and agree below it.

*A note on the word perspective, which is a picture and not a premise.* With
d = 10ⁿ − 1 the identity d/(d+1) = 1 − 10⁻ⁿ is algebra: the all-nines
numeral read as a fraction. No projective geometry does any work, and
deleting the word changes nothing in the argument. What the paragraph actually
imports is the identification **depth n ↔ extension 10ⁿ − 1**, and that is
where the argument leaves arithmetic for space.

**Exclusivity: no other interaction reads this structure.** The identification of §7 would be idle if another force did. None does.
Electromagnetism is two-signed on the orbit pairs by the ±18 ledger — excluded
by the one-signedness theorem. The strong interaction grows with separation —
excluded by the inverse-square fall above. The arrow of time is a rate
phenomenon, not a conservative quadratic form: the wrong type. The cosmological
constant is unsourced by definition, excluded at seat level by §5's
proportionality to k. Mass is not an alternative but the complement: the local rounding *excess*
(§4's deciders) is what a thing weighs; the global *deficit*, one short overall,
is what pulls it. Midy's pairing of the halves to nine makes them one structure:
**the local excess is the mass, the global deficit the gravitation.**

# PART II · THE INTERACTION

*Part I gives the standing structure: where the potential is located, its sign, its
source law, its fall with distance. It does not say when anything happens. This
part derives the interaction event itself — when two bodies' records meet,
what occurs at the meeting, and at what rate — from ledger facts already forced
elsewhere in the theory, with nothing new introduced. Its results were
established in the working record in August 2026 and are pinned test by test in
the suite of §24.*

## 9 · The interaction event: unions occur only at carry boundaries

A record in this theory is a held pair: an integer register and a fractional
register on the closed unit interval. Its ledger obeys two facts, both proved
where the notation is introduced. The collapse of the pair to its value is
many-to-one exactly at the integers, since every integer has two held names
and every non-integer has one. And holding is invertible while collapsing is
not: holding costs nothing, while collapsing dissipates exactly one bit, the
thermodynamic minimum for destroying the distinction between two names.

**Identification of the interaction as the union.** That a gravitational
interaction is a union — two records committing to one register with one phase
slot — is this part's load-bearing identification, the counterpart of
§7's; everything downstream of it in this part is theorem. A union is by
definition a *working*, many-to-one commitment. It therefore cannot occur
where the ledger is one-to-one, which is everywhere except the carry boundary:
given the identification, the *when* is not a further choice, because nowhere
else does the required arity exist.

**The meeting and its theorem.** Two clocks of periods p and q, run on one shared
tick, are simultaneously at their carry boundaries exactly at the common
multiples of p and q — at t ≡ 0 (mod lcm(p, q)), and only there.

**The trigger, defined without reference to a clock.** That statement speaks of two clocks on one shared tick, and simultaneity of
boundaries at separated places is frame-dependent. That is the failure which
has decided programmes of this kind before, since a regular lattice of ticks
generically names a rest frame. The shared tick, however, was never the content; it was the
description of the theorem in one convenient frame. What a union requires is that a carry boundary of one record and a carry
boundary of the other be connected by a null ray. Both halves of that are
invariant. A record's boundaries are events on its own worldline at its own
proper count, which is §17's invariant content, and null separation is frame-
free.
Written that way and then read in the pair's mutual rest frame, the
condition becomes

```
j·q − i·p = m ,     m = the separation, in ticks
```

whose solutions exist exactly when gcd(p, q) divides m and then recur
once per lcm(p, q). **The rate is gcd(p,q)/pq again — the same law, now from a statement that names
no clock at all**. One sharpening follows at once. Coprime periods divide every
separation, so the bilinear rate holds at every distance, while the
commensurate enhancement is confined to commensurate separations. The test that settles it is direct. Boost the same two worldlines, and the
null-connected set of unions is identical at every velocity. The coordinate-
simultaneous set — the reading the objection attacks — is populated at rest
and empty under any boost.

Two consequences result. The elementary trigger is selective per tick, and that selectivity does not
fall with ensemble size. What removes it is averaging over separation, which
every instrument does. A window of a few hundred ticks returns the bilinear
product to a part in a thousand, so no measurement that fails to resolve a
single register cell can see the structure. The aberration objection is that a force pointing at a retarded position
destabilizes orbits unless it propagates far faster than light. What answers
it is what the null connection carries: not merely that a record was there,
but its rate, which is its momentum. The receiver therefore extrapolates to the present position, and the first-
order lag cancels exactly. The residual is third order in v/c with coefficient
4/3 — two full orders of cancellation, the same order general relativity
achieves. The remainder sits at the radiative order where the quadrupole
already stands. Pinned in `verify/test_the_covariant_trigger.py`. At the meeting the committed count is the sum of the two counts. Addition is
the only composition consistent with the tick, and every alternative — maximum,
minimum, product and the rest — fails at a named witness. The count is
conserved to the digit, and exactly one bit is dissipated. The pair (k_a, k_b) and
its swap are two names for one committed record, so the union keeps the sum
while destroying the order. A symmetric pair cannot host the event at all: with nothing to distinguish, there is no distinction to dissipate.

Two consequences warrant their own exposition.

**The exclusion structure is coprimality.** Two clocks are informationally
co-occupant when their phases agree. The agreement recurs with period pq/gcd(q − p, pq), and this coincides with
the union window if and only if p and q are coprime. Coprime clocks share
exactly one downbeat and then exclude one another forever after. Commensurable
clocks re-align repeatedly between unions. The pair 2 and 3 — the theory's substrate — is the coprime case.

**The event is the cadence.** The companion volume on tonal function proves two things about the dominant
seventh. Its tension is an interval stretched across the empty fixed point of
§3, the address the figure never seats. And its resolution moves one voice up
by exactly a three and one voice down by exactly a two: one unit of each generator, moved in contrary motion, landing on the tonic frame. The union event above has the same grammar, item for item. Tension is a held
pair: two records, distinction intact. Resolution is the discharge of the generators: the commitment, one bit dissipated, count conserved. Arrival is the
occupied fixed point, the root. This can be understood intuitively: the strongest event in our perception of musical harmony and the interaction event of this part are one ledger event.

## 10 · The interaction rate: bilinear in the two masses

A clock of period p carries once every p ticks: its carry rate is 1/p. Two
clocks meet at their co-carries, so the meeting rate is

```
1 / lcm(p, q)  =  gcd(p, q) / pq  =  (1/p) · (1/q)   exactly when gcd(p, q) = 1
```

**The contact rate of two coprime clocks is the product of their individual
carry rates.** **A record's carry rate is its mass — and this is the rounding excess
under another name, not a second identification.** The account calls mass the local rounding excess in one part and the carry
rate in another. The two are one quantity, for a reason the carry itself
supplies. A record standing off its seat by a small excess accumulates that
much per tick, and a carry fires exactly when the accumulation crosses one
unit.
One carry is one unit of accumulated excess. The period is therefore the reciprocal of the excess, and the rate is the
excess: the carry rate *is* the rounding excess. The period-mass map is
accordingly p = 1/m, and the bilinear law below inherits nothing it has not
earned. Two consequences
follow and are stated. Elementary periods are whole, so this account claims that mass ratios are
rational, with denominators set by the constituent count. Best rational
approximation converges as the inverse square of the denominator, so a
denominator of a million already reproduces the proton-electron ratio to
eleven places. The claim is definite rather than vague, and far beyond present
reach. The equivalence worry that rode on the commensurability enhancement closes by
arithmetic. That enhancement is selective per register cell and averages away
as the inverse of the window. At laboratory separations of order ten to the
thirty-fifth cells, the composition-dependent residual therefore sits some
thirty orders below the parts in a thousand trillion the equivalence
experiments reach. Pinned in `verify/test_the_period_mass_map.py`. Under that identification the meeting rate of two bodies is proportional to
m₁m₂. That is the bilinear source structure of Newton's numerator, arrived at
rather than assumed. Its exception is stated rather than hidden: commensurable
periods meet more often, by exactly the factor gcd(p, q). The bilinear law is the coprime case, and the theory's
substrate pair is coprime.

## 11 · The inverse-square law, second route: the carry rate against the cell size

Part I read the inverse square out of the nines as perspective. The
operation supplies a second route, reaching the exponent by a different
operation — a gradient where the first squares — and sharing with it the
one step that carries either argument into space. The scope of that
agreement is set out exactly at the end of this section rather than claimed
here.

A register refines by cells. At depth j the cell has size u equal to b raised
to j, and the digit at that depth turns over once every u ticks. **The carry rate at a depth is therefore exactly the inverse of the cell it governs.** That inverse-first-power weight
is not a choice; it is what a carry is. Summing contact over depths, the meeting rate of two records at separation d
falls as 1/d in the envelope for every sharing profile tried. For the smooth
representative of the derived family this holds to twelve decimal places,
decade over decade. For the stepped profiles the same exponent of −1 holds in
the mean, with the ripple contributing a bounded phase wobble to any two-point
fit and never a drift. Both results hold in one dimension and in three.
**Identification of energy as the meeting rate.** Each meeting is a ledger event of
fixed cost, so the interaction energy at separation d is proportional to the meeting rate there. The potential then goes as m₁m₂/d and its gradient as

```
F  ∝  m₁ m₂ / d²
```

**The scope of the agreement.** The two routes reach the
exponent by *different operations*: Part I squares an inverse-first
amplitude; this section differentiates an inverse-first potential. Squaring and differentiating are not the same procedure, and their landing on one exponent is a real and valid way to verify the result.

This is not to say they are independent derivations, and it is not claimed here that they are.
Strip Part I's perspective language and its founding import is
**depth n ↔ extension 10ⁿ − 1**; this section opens with **depth j ↔ cell
b^j**. That is the same identification, and it is the step that carries the argument out of arithmetic and into physical space. Everything above it is register
algebra; everything below it is physics. **The routes diverge above that step and share the step itself.**

The statement is therefore one identification checked two ways downstream of this, rather than asserted as two pieces of evidence. On that narrower reading what holds is this: granted that depth is scale, the exponent is over-determined, the weight is
forced, and nothing else in the construction can move it. Sharing the depth-is-scale identification is sharing the theory; counting it twice would not be.

**The shared step introduces no unstated assumption.** Inside the register,
depth-is-scale is definitional: a digit at position n is a count at
resolution b⁻ⁿ, which is what a digit *is* rather than something assumed
about one. What bridges this to physics is the next step alone — that one
register resolution is one physical length — and that is the single borrow
this paper declares and the Scale Theorem requires. One declaration fixes
every other depth, because the ratios between depths are powers of the base
and therefore internal. Nor does the linearity of that map cost anything extra. The theorem's external
supply comes from the one-parameter group of rescalings, and a one-parameter
group of rescalings is exactly the multiplicative maps. A non-homomorphic
ladder would therefore need a slope as well as an offset, and would use two where one is allowed. **The chain uses one, at slope one — forty-two decades at forty-two positions.**

## 12 · No central singularity: the refinement census terminates

What happens as d → 0 is decided by counting, and the count reproduces the
conditions of the Navier–Stokes regularity problem exactly.

Resolving a separation d requires cells of size d, hence register depth
log_b(d): reaching d = 0 requires completing infinitely many depths. That is a
supertask, and the operation-supply theorem is unforgiving: demand through
depth N is exponential in N, while the supply of any finite-energy system is
linear in elapsed time by the Margolus–Levitin bound. The reachable depth is logarithmic in the resources. The census is identical,
term for term, to the one by which this theory's Navier–Stokes paper bars
finite-time blow-up in a fluid. A binary register in three dimensions refines
each cell into 2³ = 8, which is exactly the Kolmogorov cascade's population
per shell, and the demand series (8^(N+1) − 1)/7 is the same series. One count regulates both in a way that corresponds with observation: **water cannot blow up, and neither can gravitation.**

The register therefore has a deepest reachable cell u_min, the sum over depths
terminates, and the potential saturates at a derived ceiling — 2/u_min on the
binary layer — instead of diverging. The approach to the ceiling leaves a short-range signature. For the sharing
family the carry chain derives the inverse-square tail, with a fractional
weakening of the potential of size (ln 2)·u_min/d. The coefficient ln(b)/(b −
1) is derived rather than fitted, and equals ln 2 on the binary layer. It
falls as the first power of u_min/d. No regulator, cutoff, or renormalization was introduced at any step; the
finiteness is the count's.

**The short-range kernel is the comb, approached from the opposite direction.** The
two-rider exchange was taken at the far field, leaving its exact
small-rung form required; it closes with the same census. At small rungs the kernel is the census itself rather than the smooth
extension law: the rate at each depth against the cell it governs, summed over
the depths that register the separation. Two established facts fall out of
that one expression. Its total over all depths is the saturation ceiling
above, and its ratio to the smooth law is a staircase. Because the depth index
is a whole number, that staircase is periodic in the logarithm of
separation with a period of exactly **one octave**, repeating octave
after octave to the precision of the arithmetic. **The log-periodic
residual this part predicts at the envelope and the small-rung kernel's own discreteness are the same object, approached from opposite directions** — which is why the period was never adjustable.

What the replacement does *not* disturb is the exchange's laws. The third law, momentum conservation, the equivalence principle, the forced
merge and the path-independent binding ledger rest on two things only: the
kernel being odd, and the count product commuting. Nothing else about the
kernel's shape enters, as verified across four kernels including one chosen
arbitrarily. So the
far-field results are inherited whole, and only the orbit's shape depends
on the rung, which is the comb once more. Pinned in
`verify/test_the_small_rung_rule.py`.

**The register coordinate and the Euclidean read.** The derivations above are exact in the register's native coordinate, the
shared-prefix depth at which two records first occupy one cell. That
coordinate is an ultrametric: every triangle isosceles, every point of a cell
its centre, and no betweenness anywhere. Observation, meanwhile, reads a
Euclidean separation. The theory's one standing relation between substrate and continuum read applies here: **the Euclidean separation is the envelope of the register coordinate.**
The dictionary between them is the distribution of shared-prefix depths at a
fixed separation, which is exactly self-similar under doubling. The envelope read is exact in the mean: the octave-average reproduces
the inverse square as one scale-free constant, pinned to fifty binary digits.
Reading the substrate through the envelope leaves a fine structure periodic in log-separation with period
one octave, forced by the carry layer. Its amplitude is the sharing profile's
one free number. The register's stepped constructions put it near a tenth,
which existing inverse-square nulls already exclude; the derived family's
smooth members put it below one part in 10⁹. The amplitude is therefore an experimental parameter, with a fixed-period reanalysis template
published beside this paper. The substrate's *shape* — how three dimensions and their angles emerge from an
ultrametric register — belongs to the dimensional account, not to this part. Locality is not adjacency in the register but shared prefix. Inside one cell there is no inside for anything to cross — the mechanism this account's "correlation is
not transmission" always required.

# PART III · THE COUPLING

## 13 · The coupling: αG(e) = 5/(2¹⁵¹ − 1), and the value of G

The measured gravitational coupling of the electron is dimensionless:

```
αG(e)  =  G·m_e² / ħc  =  1.7518 × 10⁻⁴⁵
```

The construction's way of placing a number in an exponent is not a power but
a **wheel** — a repeating binary fraction with the form

```
x / (2ᵏ − 1)
```

which is the form the master object itself takes, since

```
1/7  =  142857 / (10⁶ − 1)
```

The measured coupling takes the wheel form

```
αG(e)  =  5 / (2¹⁵¹ − 1)        to 106 parts per million
```

A theorem then removes the representational freedom that affects bare
powers. The same number could be written in any of the forms

```
5 · 2⁻¹⁵¹        10 · 2⁻¹⁵²        (5/4) · 2⁻¹⁴⁹
```

but among all such forms exactly one is an irreducible wheel with integer
block: block 5, which is 101 in binary, at period 151. The argument is the
order of two:

```
ord₅(2)  =  4

4 ∤ 151     the five-block is irreducible
4 | 152     the ten-block dissolves
```

One representation is admissible, and no choice is exercised in selecting
it.

**The period is derived rather than observed.** The binary all-ones at
depth d factors cyclotomically over the divisors of d. Three names from the
construction's usage, introduced once:

| name | value | role |
|---|---|---|
| the motor | 3 | the driver of every cycle here |
| the lift | 5 | the raiser of the third |
| the tether | 7 | the prime of the reptend |

The motor's cycle first closes at depth 3, and the lift's at depth 5:

```
2³ − 1  =  7        the tether prime, itself the binary all-ones 111₂
2⁵ − 1  =  31
```

The two first close together at depth lcm(3, 5) = 15, where

```
2¹⁵ − 1  =  7 × 31 × Φ₁₅(2),      Φ₁₅(2) = 151
```

— the prime 151 is the *novel* content of the joint closure, the factor no ancestor depth produces. Advancement of a closure's novel content to the next depth is the construction's own law, derived within it rather than assumed. Iterating value-
becomes-depth from 2 gives 2 → 3 → 7 → 127, the Catalan–Mersenne chain, whose
consecutive rungs are this account's own primes. The coupling is the numerator 5 riding the single advancement of the mesh: **gravity is the generation the lift
joins.** Converting through exact constants and the electron mass — the one
supplied ruler, entering here and only here —

```
G_pred  =  5/(2¹⁵¹−1) · ħc/m_e²  =  6.67359015(4) × 10⁻¹¹ m³ kg⁻¹ s⁻²
```

with the uncertainty from the electron mass alone. This stands 106.4 ppm below the CODATA-2018 centre. That places it outside the
adjusted bar and inside the unresolved spread of the underlying experiments,
whose mutual discordance is the outstanding unresolved problem in G metrology.
It is refutable by convergence: if the laboratories converge on the CODATA
centre at their stated precisions, the coupling wheel is wrong. The pairing itself is an identification, and is labelled as one. The motor
joined to the tether would put the cycle at Φ₂₁(2), and the lift to the tether
at Φ₃₅(2), neither near any measured coupling. The lift joins the motor's
generation, and that choice is the section's named identification rather than
its theorem. An exclusivity test closes the section: among the
fine-structure constant and the gravitational couplings of electron, proton,
and muon, exactly one admits a small-block irreducible wheel, and it is the one the
mechanism singles out.

**The four targets scanned, and the criterion that selected them.** The
scan covered four couplings:

```
   the fine-structure constant

   the gravitational couplings of the electron, the proton and the muon
```

The criterion admitting these four and excluding others is stated
explicitly: the relevant mass is known to better than one part in 10⁹, and
the coupling is defined without a running-scheme convention. Both
conditions are properties of the measurement, fixed independently of the
result, and both are the criterion the opening of this section applies.

**The scan widened to sixteen targets.** The same criterion, applied with a wider tolerance, admits further couplings, so the scan was
repeated over sixteen. The additions were the gravitational couplings of the
neutron, tau, pion, up and down quarks, W, Z, Higgs and top, together with the
strong coupling at the Z mass, the weak coupling, and the weak mixing angle. The outcome:

```
   targets inside the achieved tolerance          1   (the electron)
   nearest competitor                             the proton,
                                                  46 × further out
```

The exclusivity is therefore unaffected by widening the set.

**The significance, computed.** Exclusivity within a scan is not
significance, so the null hypothesis of the scan is evaluated directly. The
candidate space is smaller than it appears. For a given numerator exactly one
exponent lands near a target. Every even numerator duplicates an odd one at
one lower depth, to within a part in the coupling wheel's own period,

```
2/(2¹⁵¹ − 1)      against      1/(2¹⁵⁰ − 1)
```

so the eight odd numerators through fifteen exhaust the distinct wheels.
Each lands within a relative tolerance *t* with probability 2*t*/ln 2:

```
   per target, at the achieved tolerance          0.25 percent

   family-wise over  4 targets     p ≈ 0.0098     2.6 standard deviations
   family-wise over 16 targets     p ≈ 0.039      2.1 standard deviations
```

Both figures were confirmed by Monte Carlo over randomly drawn targets.
**The figure this section stands on is the second: p ≈ 0.039, 2.1 standard
deviations**, computed over the wider set, since the criterion admits that
set. Widening reduces the significance by half a standard deviation and
leaves the exclusivity intact.

At that level the match is suggestive and not decisive, and the section
does not claim otherwise.

**The level of precision required, fixed in advance.** The tolerance is
fixed here before any future measurement, so that no tolerance can be
selected after the result is known. Family-wise p is linear in the
tolerance, with a coefficient that depends on the size of the target set —
so both sets are tabulated, and the widened one governs:

| | 4 targets | 16 targets |
|---|---|---|
| coefficient (*p* / *t*) | 92.4 | 369.3 |
| three standard deviations | 29.2 ppm | 7.31 ppm |
| five standard deviations | 0.0062 ppm | 0.0016 ppm |

**The distinction is material.** On
the four-target criterion, CODATA-2018's 22 ppm bar already sits inside the
three-sigma window, so present metrology would settle the question at that
level. On the sixteen-target set — the set this section's significance
figure is computed over — three sigma requires agreement within 7.31 ppm,
and **present metrology has not reached that precision.** The claim that
the test is already at three-sigma strength therefore holds on the narrower
criterion only, and is not asserted on the wider one.

What is true on both sets is the direction of the test. The prediction
stands 106.4 ppm below the CODATA-2018 central value — outside its adjusted
uncertainty, and inside the unresolved spread of the underlying
torsion-balance and atom-interferometry determinations, whose mutual
disagreement is the outstanding problem in G metrology.

```
   convergence on the CODATA central value
       at the stated precisions            →   this section is refuted

   convergence on the predicted value
       within 7.31 ppm                     →   three standard deviations
                                               on the widened set
```

Both outcomes are reachable by improvement in the existing experiments, and
neither requires a new apparatus. That is the whole of what §23's fourth
condition claims. Pinned in `verify/test_the_wheels_look_elsewhere.py`.

### 13.1 · The hierarchy problem, read as the register's reference level

The coupling's position in the hierarchy is then arithmetic. Since
5/(2¹⁵¹ − 1) = (5/4) · 2⁻¹⁴⁹ to one part in 10⁴⁵, the coupling stands 149
binary orders below unity, displaced from the pure power-of-two lattice by
the exact rational factor 5/4. The hierarchy problem asks why gravity sits
some forty-five decimal orders below the other couplings. The reading this account carries is structural: the gravitational coupling is not a small interaction strength among peers but the register's reference level. The reference is the numerator 5, alone, on the binary wheel of period 151 = Φ₁₅(2) — the deepest period the first joint closure of the generators' cycles produces. A
reference level has no magnitude of its own kind; the other couplings are
read against it. Section 15 carries the same structure as a correspondence.

**The experimental discordance.** The underlying experiments are not one measurement. Fifteen determinations
across four decades, quoted at collection time from the standing review and
the newest redetermination, give χ² = 189 about their own weighted mean for
fourteen degrees of freedom. The spread is 551 parts per million peak to peak,
against individual bars claiming tens. No constant fits the ensemble; something in the
laboratories, not in G, moves between experiments. Part II adds an entailment. The register's fine structure cannot be the cause,
because its amplitude is one number at every scale, and the ephemeris window
holds that number eight to nine orders below the discordance. The stance here
is therefore the one every position-invariant theory shares: the discordance
belongs to the laboratories and not to G. One rider is distinctive to this
paper. Measured G carries no genuine dependence on working separation at the
discordance scale, and an octave-periodic dependence found there would refute
Part II outright. The ensemble as it stands does not favour the coupling wheel. The tightest
determinations sit above it, and χ² about the coupling wheel's value is 538. Six of the
fifteen agree with it within two of their own standard uncertainties. The
CODATA centre itself scores seven on the same statistic, so the null outscores
the wheel. That figure is printed here rather than left for the reader to
compute. For the coupling wheel to be right, the five tightest determinations — four groups, three distinct methods — must share a positive systematic near one hundred parts per million for which no mechanism has been proposed. The claim rests on convergence, and the newest determination is set down for
what it is. In 2026 the BIPM torsion balance, rebuilt at NIST three decades
after its construction (Metrologia, 10.1088/1681-7575/ae570f), read
6.67387(38). That value is 0.7σ from the coupling wheel and 1.1σ from the CODATA
centre, so it discriminates between them not at all. It also sits 250 parts
per million below the same instrument's own Paris determinations, with no
specific systematic identified. Its real lesson is symmetric: an instrument of that class can carry a silent 250-ppm error, which weighs equally against every two-sigma agreement in this paragraph, the wheel's included. One experiment; the convergence criterion above stands unmoved.
Every number in this paragraph is pinned in `verify/test_the_g_file.py`, with
the planetary quadrature theorem beside it. Mercury and Jupiter sit a quarter-
period apart in the comb's cycle. Whatever phase nature picks, at least one
classical planet therefore keeps 92 percent of the full precession signal.

## 14 · The cosmological chain: horizon over nucleon at 10⁴², the saturation density, and the expansion rate

One more count belongs to this part because it is dimensionless from end
to end and carries a live failure condition. The theory's cosmological ledger
fixes, with no parameter and no unit anywhere,

```
frozen comoving horizon diameter / one nucleon's extent  =  10⁴²
```

**Where the exponent comes from, and what it rests on.** The forty-two is
not read off the sky. Each of the two generators has a canonical
inscription clock in the register's own base, and neither clock is chosen:

```
   the tripling clock    1/7          closes in  6

   the doubling clock    1/(100 − 2)  closes in  42
                         = 1/98
```

The doubling clock cannot live at the single-digit station, because two
divides ten and 1/(10 − 2) terminates; the minimal doubling wheel is
therefore 1/98. The two clocks strike together at their least common
multiple,

```
lcm(6, 42)  =  42
```

which is once per doubling revolution. To that forced arithmetic one
postulate is added, and it carries the whole weight:

> **A record is complete when the clock on its conserved face closes: one
> revolution, and no more.**

The depth is then the co-closure,

```
N  =  10⁴²
```

That postulate is the chain's single conjectural link, and it is stated
here rather than buried because everything dimensionful below inherits it.
Three things would break it. If the conserved span were kept on the energetic
face rather than the structural one, the clock assignment falls. If
completeness admitted more than one revolution, the count falls. And the
empirical landing below can fail on its own. The arithmetic of the
clocks is exact; that the clocks set the depth is the postulate.

The ratio is the whole of the parameter-free content. The dimensionful values below follow only once any single one of the three is
supplied, either declared from the construction or taken from measurement. One
anchor decides the other two, per the boundary held throughout this paper. The
chain stands or falls with all three at once. Stated in full:

```
DECLARED      cell   =  8/7 SI femtometres         the single borrow
                      ( = 2³/7, the three-dimensional refinement count
                        over the sevenths wheel it returns, since 8 ≡ 1 mod 7 )

SEATS         Ω_m    =  1/3        Ω_Λ  =  2/3      the account's own
              depth  =  10⁴²                        values, not measurements

DERIVED       n₀     =  1 / ( (4/3)π · cell³ )  =  3·7³ / (2¹¹π)
                     =  0.1599320668  fm⁻³

              I      =  B(1/6, 1/3) / ( √3 · 2^(1/6) )
                     =  4.3273634980       the frozen comoving horizon,
                                            in units of c/H₀

OUTPUT        H₀     =  2 c I / ( 10⁴² · cell )
                     =  70.0540  km s⁻¹ Mpc⁻¹
```

| the chain fixes | value | standing comparison |
|---|---|---|
| the nucleon cell | 8/7 fm, declared (Mode A) or from measured n₀ (Mode B) | — |
| nuclear saturation density | n₀ = 3·7³/(2¹¹π) = 0.15993 fm⁻³ | chiral EFT 0.164 ± 0.007 (0.6σ) · Skyrme survey 0.160 ± 0.010 (0.0σ) |
| the expansion rate | H₀ = 70.05 km s⁻¹ Mpc⁻¹ | between Planck's 67.36 ± 0.54 and SH0ES's 73.04 ± 1.04 — 5.0σ from Planck, 2.9σ from SH0ES |

**The precision of these figures, and where it is actually limited.** The
values above are exact consequences of the declaration. No measured
quantity enters the chain at any step: c and the megaparsec are
definitional, the seats are rational, and I is a closed form in gamma
functions. Evaluated at fifty digits the two routes to n₀ and the four
routes to I agree to the last place, so the chain propagates **no
experimental uncertainty of its own** and could be quoted to arbitrary
precision.

That is not a strength to lean on, because it means the chain's testable
precision is set entirely by the measurements it is compared against, and
those are one to two orders of magnitude coarser than the prediction:

```
   the chain's own arithmetic          exact  (25+ digits verified)

   best nuclear determination of n₀     4.3 percent
   best single-route determination of H₀  0.8 percent
   spread between the two H₀ routes       8   percent
```

**One structural feature does improve the situation, and it runs in the
useful direction.** Because H₀ depends on the inverse cell and the cell on
the cube root of the density, a fractional uncertainty in the nuclear
number reaches the cosmological one divided by three:

```
   H₀  ∝  1/cell  ∝  n₀^(1/3)

   4.3 percent in n₀    →   1.4 percent in H₀
   6.2 percent in n₀    →   2.1 percent in H₀
```

So the chain converts a nuclear measurement into a sharper cosmological
prediction than the nuclear measurement itself. That makes a second way of
running the chain available, and because the relevant measurement is not
settled, **both are given here rather than one.**

**The chain has two modes, and they answer different objections.** Any one
of the three quantities fixes the other two, so which one is taken as input
is a choice about what the account is willing to assume.

```
   MODE A — DECLARED.   cell = 8/7 fm, taken from the construction

        n₀  =  0.1599321 fm⁻³        H₀  =  70.0540 km s⁻¹ Mpc⁻¹

        exact, no measurement anywhere in it, and it exploits the Scale Theorem's one permitted declaration


   MODE B — MEASURED.   cell taken from the measured saturation density

        from  n₀ = 0.164 ± 0.007     H₀  =  70.64 ± 1.01
        from  n₀ = 0.160 ± 0.010     H₀  =  70.06 ± 1.46

        nothing declared, one measured input, a falsifiable output
```

Mode A is the framework speaking on its own terms. The value 8/7 = 2³/7 is
pure construction — the three-dimensional refinement count over the sevenths wheel it returns — and it yields an exact number with no experimental content
whatever. Mode B assumes nothing about the cell and asks what the chain
predicts given what nuclear physics currently measures.

**The two agree.** Mode A's exact 70.054 sits inside Mode B's bar in both
determinations, and the declared 8/7 sits at +0.59σ and +0.01σ against the
two measured cells. That agreement is the substantive claim of this
section: a length taken from the construction and a length taken from the
laboratory are the same length, to the precision the laboratory currently
offers.

**Mode B also carries no metre ambiguity.** The 0.0692 percent floor described below is a cost of
*declaring* a length in a named unit. When the cell is taken from a measured density instead, the unit cancels
between input and output. A change of metre moves n₀'s numerical value and the
cell's compensatingly, and H₀ in km s⁻¹ Mpc⁻¹ does not move at all. Verified to forty digits.
**So Mode B is exact where Mode A carries a floor, and Mode A is exact
where Mode B carries an experimental bar.** Neither dominates; each carries its uncertainty in a different place, which is why both are shown.

**Run backwards, the chain turns the Hubble tension into a nuclear
question.** Taking each published expansion rate as the input instead, and
asking what saturation density it requires:

| determination | H₀ | implies n₀ (fm⁻³) |
|---|---|---|
| Planck 2018 | 67.36 ± 0.54 | 0.1422 ± 0.0034 |
| DESI 2024 | 68.52 ± 0.62 | 0.1497 ± 0.0041 |
| TRGB / CCHP | 69.80 ± 1.90 | 0.1582 ± 0.0129 |
| SH0ES 2022 | 73.04 ± 1.04 | 0.1813 ± 0.0077 |
| **measured nuclear saturation** | — | **0.160 ± 0.010** |

Against the nuclear value the two principal determinations sit at **−1.69σ and
+1.68σ** — nearly symmetric, and in opposite directions. On this account
the two ladders are not merely disagreeing with each other; each is
disagreeing with nuclear physics, by about the same amount, on opposite
sides. The nuclear determination is currently too coarse to adjudicate between them.
Its 6 percent bar against an 8 percent separation between the determinations gives it under four
standard deviations of discriminating power in principle, and about 1.7 in
practice. It is nonetheless a third and wholly independent road to the
expansion rate, using no supernovae, no microwave background and no distance
ladder.

**Improving the measurement of nuclear saturation density is therefore three
times more valuable, per unit of fractional precision, than improving either
H₀ determination**. That is a statement about this chain, offered because no one
measuring saturation density has reason to know it.

**What limits precision that is not a measurement.** One ambiguity is a
choice rather than an error, and it must be named alongside any quoted
figure. The formula is invariant under rescaling the metre — c and the
cell rescale together, the kilometre and the megaparsec rescale together —
but *the declaration is not*, since "8/7 fm" names different physical
lengths on different metres. The units chapter proposes a native metre of
0.9993081933 SI metres, on which c reads exactly 3 × 10⁸:

| declared in | cell (SI fm) | n₀ | H₀ |
|---|---|---|---|
| SI femtometres | 1.142857 | 0.159932 | 70.0540 |
| native femtometres | 1.142067 | 0.160264 | 70.1025 |
| gap | 0.0692 % | 0.2078 % (the cube triples it) | 0.0692 % |

This paper declares SI, because that is the metre the comparison
quantities are quoted in. The native metre is a metrological proposal and
not a hypothesis about nature, so nothing forces it, and adopting it would
relocate the declaration rather than derive it. **Until that choice is
forced, 0.0692 percent is a floor on any claim made from this chain, and
no figure here should be read past it.** Neither choice changes the
standing against either Hubble determination: both sit inside the discordance and
outside both ends of it.

**The density in question.** The saturation figure is the **symmetric**
one — equal neutron and proton content — and the account is entitled to no
other. Two-species matter separates into two channels: a sum channel, the total
density, and a difference channel, the neutron-proton imbalance. The
construction above fixes the first and is silent on the second. That is
exactly as the drag word's difference face carries angular momentum and no
quadrupole. The
asymmetry is a continuous parameter, and this paper's own limit on
continuous parameters applies: the stations are the resting skeleton, and
the shift away from symmetry rides a measured ratio rather than a derived
one. The figure above may not be quoted for neutron matter, nor for any particular
nucleus, since everything past calcium is neutron-rich. A later derivation of
the symmetry energy or its slope from this arithmetic would contradict the
limit rather than extend it. Both reference values compared
against are themselves symmetric-matter numbers, so the comparison is made
at the same point on both sides.

**The vacuum term.** Part II's far boundary settles one more account here. Removing the depths beyond the horizon subtracts a constant
from every pair's binding (§18's exact theorem), and removed binding is
raised energy: a uniform, separation-independent, **positive**,
**pair-sourced** energy — the cosmological term's sign and character, derived
rather than chosen. Totaled over this chain's own horizon with banked inputs
only, it stands at 0.32 of the observed vacuum density at unit profile
constant. Three parts of that statement are derived and one is not, and the paper
separates them. The sign, the sourcing, and — the substantive part — the
absence of the catastrophe are derived. The term is infrared, set by the
ceiling alone and pinned independent of the register's floor across eight
orders. The 10¹²³ discrepancy therefore never arises, because this framework
contains no continuum mode sum to explode. The magnitude's landing at the observed order is entailed by criticality for
any horizon-set quantity. That is the coincidence problem surfacing through
this mechanism, rather than a derivation of Ω_Λ. The equation of state is
settled by the coordinate rule, below. The scaling objection is that a *bulk* reading falls wrong:
pair energy going as 1/a against pair density going as a⁻³ gives a⁻⁴,
never a⁰. What answers it is not a horizon but this account's own
capacity count — the depth ceiling, a constant of the model rather than a
length that tracks the expansion. Read there, the statement

```
ρ_Λ  =  (3/8π) · ρ_P / N_∞²
```

collapses identically to

```
ρ_Λ  =  3H² / 8πG
```

a consistency that derives no magnitude — which is exactly what the
dimensional boundary requires of it — and a density containing nothing that
could evolve.

**The coordinate rule settles the equation of state outright.** The rule that areas count cells says the metric's volume element equals the
flat one. That is a statement about the chart, as the same solution shows: it
satisfies the condition exactly in one set of coordinates and misses it by
order-unity factors in another. Its name elsewhere is the unimodular
condition, and it is always reachable: for any solution of the class used
above, u = ρ with v = ∫e^{2(γ−ψ)}dz has exactly the required Jacobian.
Fixing the volume element removes one metric component, and what follows
is algebra. The trace of the remaining field equations vanishes
identically — nine equations rather than ten — so the divergence, taken
with the Bianchi identity and a conserved source, leaves

```
∂_b ( R + κT )  =  0
```

That constant of integration is the cosmological term. **It is not a
coupling appearing in the equations; it is what the integration leaves
behind, and a constant of integration does not evolve.** Hence

```
w  =  −1        exactly, at every redshift
```

Its magnitude is boundary data, which is the dimensional boundary's own
verdict arriving by a second route.

This settles a question the section previously left open in favour of an
alternative that is now excluded. Sourcing the term on the *frozen*
horizon would give a term still growing before its limit, quintessence-like
and with an evolving equation of state. That requires the geometric term to
move, and a constant of integration cannot. The account therefore predicts
w = −1 at every redshift, with no second register available to retreat to.
The
standing refutation condition therefore bears on the coordinate rule itself:
sustained (w₀, wa) ≠ (−1, 0) at five standard deviations in two
independent supernova compilations, with the low-redshift calibration
dispute adjudicated. The DESI DR2 combination's present preference for
evolving dark energy, at 2.8 to 4.2 standard deviations depending on the
supernova set, is exactly the pressure that condition anticipates. What
remains outstanding is the other two thirds of the observed term and the chain's
own background; pinned in `verify/test_the_unimodular_chart.py`.

The H₀ row is stated with its tension shown, because the tension is the test:
the chain's value sits inside the corridor of the present Hubble discordance
and cannot survive a convergence of the two ladders onto either end. A
maintained watch tool in the public repository takes any newly published value
of n₀, H₀, or the cell and returns the two-sided verdict — closing support or
outright failure — with thresholds stated in advance.

# PART IV · THE CORRESPONDENCE

## 15 · The nine correspondences, each on an arithmetic pathway

**Why a harmonic correspondence is expected, and what would refute it.**
Every bounded periodic motion decomposes into integer multiples of one
fundamental. That is Fourier's theorem rather than a musical convention,
and the tonal names used below name those integer ratios by their
function. Gravitation couples to everything that carries energy, and §7.1
locates its entry at the acquisition of a rest frequency, which is a
periodicity. A harmonic reflection of gravitation is therefore the expectation. The burden rests with the claim that there is none, which would require a periodic physical structure that does not decompose harmonically. What this account adds is the station and its sign. The reflection sits at the unit residue of the reptend, the subdominant at 7.999999 on the root 24, the one place the cycle cannot close. The shortfall is exactly one and never over, which is why the station is a monopole with a single sign (§4, §6). What refutes the correspondence is
stated in §6: a reptend comma at any station other than the subdominant,
or a second station carrying a unit residue.

The identity claimed in §1 then runs in both directions. Nine
correspondences, each carried by an explicit pathway in the theory's
arithmetic — an equation and a machine-pinned fact, never a resemblance:

| the tonal center | the gravitational field | the pathway |
|---|---|---|
| the tonic need not be sounded; every tone is heard as displaced from it | the rest value: calculated, never observed | the bounds assemble the unit without either being it: .000001 + .999999 = 1; the center is off-lattice literally — no seat stands at 180° |
| tension is distance from rest | displacement; mass is the rounding remainder | the deviation formalism; the generation excesses +0.144, +0.0432, +0.00288, every one positive |
| resolution tends only toward the tonic | one-signed attraction | the shortfall theorem (§4) and the five-step Midy chain of deciders |
| no tone in the key is exempt | the equivalence principle | the k-rotation congruence (§5): relative shortfall identical for every k |
| the circle of fifths never closes | orbits precess; exact closure is the exception | (3/2)¹² / 2⁷ = 531441/524288 ≠ 1; Bertrand's theorem makes closed orbits the dynamical exception; equal temperament is the seating convention that closes the circle by construction — the continuum's move, made audible |
| the cadence: fall, contrary motion, arrival | the union event | §9: one three and one two, moved in contrary motion through the unseated address; one bit dissipated; count conserved |
| the leading tone and the dominant have addresses | the geography of the degrees | Si at 315°, the chiral axis; Sol at 180°, the empty seat's angle — the sounded tones stand on the dominant while the tonic stays unsounded |
| the reptend is a screw: one place, one residue step of 60°, the residue closing in six steps while the value falls short by 10⁻⁶ | the conservative binary's count direction is helical, ∂t + Ω∂φ, and the deficit along it is the clock rate | the screw invariance of 142857, whose rotation under multiplication is the discrete logarithm; the two orderings of the hexad as its two orientations; the helical Killing vector of §21.9 |
| the tension and release a listener reports | the audible instance | the reversal, below |

**The resolution toward the octave.** On the ladder of just steps the resolution toward the
upper octave is, at every rung, exactly one just step away and is never completed in finitely many steps; the total resolution is exactly one octave. The
seventh rung is real and is the dominant seventh: the partial product at n = 7
is 7/4, the harmonic seventh, with remainder 8/7 — the unresolved driver
standing one septimal step from home. The drive toward the tonal center is not a feeling about the arithmetic; it is the arithmetic's own residue column perceived by the human sensory apparatus, and its total is exact.

**The same non-closure, in time.** The theory's clock is a cycle with a carry:
on the eight-slot cycle the three-walk wants nine, the cycle supplies eight,
and the overshoot 9/8 — the whole tone — is handed forward, every cycle,
forever. The carry is the tick, linear time is the stack of carries, and the same never-seated drive acts in the time dimension. **The tonal center's tendency acts in frequency, the clock's in time** — reciprocal faces of one non-closure, which is the incommensurability of two and three itself.

**The reversal.** The organizing claim of this account is that the dimensionless
constants are the mode structure of a vibrating string. On the root 24 the just
ratios are not *like* the rest values — they **are** the rest integers
{24, 27, 30, 32, 36, 40, 45, 48}. The borrowing therefore reverses: tonal
gravity is not a metaphor lent by physics to music but the audible instance of
the law, delivered through the one sensory channel that parses 2⊥3 structure
natively. A suspension resolving is the equivalence principle in its audible instance. This is why the correspondences of this section are nine and not one:
a metaphor matches at a point; an instance matches everywhere the structure
goes.

**The audible instance.** The dominant seventh Sol–Si–Re–Fa sounded and released into Do–Mi–Sol carries the interval 45/32 across the one address the figure never seats. Its release moves one three and one two in contrary motion, which is §9's union event. The tension and the release are audible, and nothing in this paper's derivations requires them to be heard; everything it derives can be.

# PART V · STANDING AND RELATION TO EXISTING THEORY

## 16 · The kinematics: the octave as a Lorentz boost

The claim of this section: the diatonic series is not merely consistent with special relativity's kinematics — it carries them. The identification on which the section rests is: **the octave is a boost** — a doubling on one null axis, a halving on the other, rapidity ln 2. Everything after that identification is arithmetic, and every enumerated fact below is exact and pinned in the test suite.

**The reciprocal pair.** Walk up the series and two things happen at once:
the frequency rises and the wavelength falls, their product held fixed.
That pair — one coordinate dilating as the other contracts, the product
invariant — is not *like* a Lorentz boost; in light-cone coordinates it is
the definition of one. Set side by side:

```
   a boost, in light-cone coordinates       a change of pitch

        u = t + x   ↦   k·u                      f   ↦   k·f
        v = t − x   ↦   v/k                      λ   ↦   λ/k

        invariant:  u·v                     invariant:  f·λ
```

The octave is the case k = 2. Two consequences follow at the level of
structure rather than analogy. First, the signature. A transformation that preserves a product is hyperbolic,
and one that preserves a sum of squares is Euclidean. A geometry whose
founding move is the octave is therefore Lorentzian — not by choice, but
because doubling-while-halving is what its generator does. Second, the stability: the system as a whole is invariant — the product never moves —
while every station of it differs from every other, which is exactly what a
relativistic kinematics is: one invariant, many frames.

**The speed limit, and where it is located in the scale.** Stacking n octaves of
boost gives the velocity

```
β(n)  =  (4ⁿ − 1) / (4ⁿ + 1)
```

and the margin left below the limit is the complement:

| n | β(n) | margin = 2/(4ⁿ + 1) |
|---|---|---|
| 1 | 3/5 | 2/5 |
| 2 | 15/17 | 2/17 |
| 3 | 63/65 | 2/65 |
| 4 | 255/257 | 2/257 |

One octave is the 3–4–5 boost exactly. Two octaves land on the spine prime
17. The margin shrinks at every rung and reaches zero at none, so the limit c
is approached the way the tonic is
approached in §15's ladder — exactly one just step away at every rung, never
attained in finitely many. c is the unsounded center of the kinematics: every
massive thing is displaced from it, nothing occupies it, and it organizes the motion of everything relative to it. That an unpassable maximum exists is the metre read kinematically; the
companion volume derives it from the register's one-step-per-tick clause, and
the octave ladder gives the limit its scale structure. **The speed of light,
in full: the invariant, the numeral, and the dressed rates.** Three things called "c" must be held apart, and this theory's own units volume supplies the discipline. The *invariant* is the register's
one-step-per-tick clause — the thing the ladder above approaches; it is
structural and carries no digits. The numeral 299792458 carries digits and no structure. It is the residue of an
eighteenth-century survey, frozen into the 1983 definition of the metre. This
paper reads nothing in it, since reading its digits would be reading the
length of France. The one
structured statement available about a c-numeral is the units volume's
labelled proposal. On a metre differing by 0.0692 per cent — the same 0.0692
per cent that sets the floor under §14's chain — the same rate reads

```
   3 × 10⁸           =  2⁸ · 3 · 5⁸

   3 · (10⁸ − 1)     =  3³ · 11 · 73 · 101 · 137
```

so the all-nines neighbour carries the fine-structure prime. It does so
because the order of ten modulo 137 is eight:

```
ord₁₃₇(10) = 8       hence   137 | 10⁸ − 1
```

This is a fact about unit *choice*. It moves no dimensionless quantity, and
nothing in this paper is loaded on it. And the dressed rates. Light in a medium is a collective excitation of the
medium, and its group velocity is that of the dressed excitation rather than
the invariant. It is slowed in laboratory media by seven orders of magnitude,
and in the electromagnetically-induced-transparency experiments parked
entirely: the pulse is written into the medium's internal coherence, held, and
re-emitted.
On this paper's terms that is a held record parked in a material register and
released. Storage is possible precisely because the record has no internal
clock to lose, which is the cavity arithmetic at this section's close. Nothing
in it touches the invariant, which no medium-dependent rate reaches. Gravitational lensing sits on the same ledger from the other side. The bend of
light is the tickless record's response to the deficit: the photon exists, so
the existence-layer coupling of §17 reads it, and it falls without aging. The
factor-two agreement with the relativistic bend over the Newtonian belongs to
§17's weak-field record.

**Composition is the stacking of intervals.** The velocity-addition law
that replaces Galileo's is, in Doppler-factor form, a single line — factors
multiply:

```
k  =  k₁ · k₂
```

Velocities compose the way intervals stack, a fifth on a fifth landing a
ninth, never by adding frequencies. The identity

```
β(k₁k₂)  =  (β₁ + β₂) / (1 + β₁β₂)
```

is exact and rational, pinned over five hundred random rational factor
pairs. The Galilean transform is the *tempered* error — adding what
composes multiplicatively — and the two give different answers at one
octave each:

```
   added      3/5 + 3/5                    =  6/5     exceeds the limit

   stacked   (3/5 + 3/5) / (1 + 9/25)      =  15/17   cannot reach it
```

The old puzzle of two travellers approaching head-on near light speed
dissolves in the same line. Their relative motion is the stack k₁k₂, finite
for every finite pair. The limit itself has no rest frame to stand in: the tonic, again, has no voice. Practically: two ships approaching head-on at 0.9c each measure the other arriving at 0.9945c rather than 1.8c. Each carries k² = 19, the stacks multiply to k₁k₂ = 19, and the ratio (19² − 1)/(19² + 1) stays below one. The 1.8c is the closing rate a third observer assigns, which
no one measures locally; only the limit itself, which no finite stack
reaches, would read unity.

**Self-similarity is frame-indifference — two invariances, kept distinct.**
An additive lattice — points at a fixed spacing — is destroyed by any boost:
the spacing contracts, the lattice picks out the frame that built it, and
relativity is broken at the first step. The series carries two exact
symmetries instead, and they are not the same symmetry. The first is
*scaling congruence between octaves*. A boost by one octave maps the lattice onto itself. Every octave is the octave
above at half scale, gaps and all: 48 → 24 carries gaps 3, 5, 4, 4, 2, 3, 3,
and the octave above carries their doubles. No octave-boosted copy of the lattice is therefore
distinguishable from another. What the lattice does mark is the floor and the root — and those
are the cone and the center of §3, not a frame: the marked objects are
exactly the ones a boost cannot move. The second symmetry is the *terminal translation* of the descent table in §6: the last octave's gap list, carried
down unscaled, lands the floor in whole numbers — a translation, not a
dilation, and the one construction that reaches zero. Frame-indifference
among the boosted copies, whole-number arrival at the floor: the first is
the relativistic requirement met by construction, the second is the
register's own arrival mechanism, and conflating them would claim more than
either delivers. One stated residual keeps the edge falsifiable, and it is scale structure
rather than frame structure. Boosts finer than the ladder's rungs are not
register symmetries, which is a discreteness of the boost group visible as
structure in rapidity. The propagation rule itself is dispersionless at every
wavelength, one depth per tick exactly, so no photon-dispersion or
interferometer signal exists at any order. What remains falsifiable is the rung ladder and the comb; the frame sector is held empty by §17's gauge theorem.

**The comma is a residual boost, and the pitch spiral is the generic transformation.** Transport a system around the cycle the two generators
offer — twelve fifths up, seven octaves down — and it does not return. The non-closure is ancient knowledge: it is the Pythagorean comma, carried under that name since antiquity. The cycle misses closure by an exact rapidity:

```
   12 ln(3/2) − 7 ln 2   =   ln(531441 / 524288)

                         =   0.0135510334…

   where          3¹²    =   531441
                  2¹⁹    =   524288
```

corresponding to a residual velocity β = 0.013550. The circle of fifths is a spiral because ln 2 and ln 3 are incommensurable,
which is this account's founding fact expressed in rapidity units. A loop of
transports that returns displaced is the discrete face of what geometry calls
holonomy, the signature of curvature. Read as kinematics: one null coordinate expands
as the other contracts, the product held, and the cycle never quite closes;
the leftover is exact, derived, and small. This section states the identification of that non-closure with gravitational curvature as a reading, and it is the expected reading rather than a decoration. Harmonic systems express this non-closure universally, since the third harmonic's misfit with the powers of two is structural (§15). A curvature that is the same misfit read kinematically is therefore its logical appearance, not an incidental detail. What is loaded, and pinned,
is the arithmetic: the residual exists, its size is the comma, and it exists
because two and three share no power.

**Differentiation, or why a continuum cannot do this.** The question is mechanical: by what mechanism do the temporal and the spatial differentiate at all? A continuum offers no mechanism — every point of it is like every other, every scale like every other scale; nothing marks an address, so nothing
distinguishes. The series marks every address three ways at once. Each station carries a
unique frequency, its reciprocal wavelength, and an asymmetric local spacing.
The gap list 3, 5, 4, 4, 2, 3, 3 repeats but its stations do not, so value and
gap together name the seat. One face of the
address is temporal (the rate), one spatial (the length), one structural (the
interval to the neighbors) — and they cannot be traded without changing the
station. Time-like and space-like are distinguishable in this system because
the system is discrete and asymmetric enough to hold the distinction; motion
is re-addressing on it, and the addresses are real. That is the whole
mechanism, and it is unavailable to a homogeneous continuum by the
continuum's own homogeneity.

**The cavity question.** A source between two mirrors, lit for thirty
seconds: does a thirty-second train drain out when the switch opens? The
empirical answer first, because the premise deserves its correction: the
train picture is *right*, and the drain is real — but its clock is the
mirrors', not the source's.

```
   30 s of emission        =  8.99 × 10⁹ m of train

   folded into a 3 m cavity   →  3.0 × 10⁹ traversals
                              =  1.5 × 10⁹ round trips

   drain rate after switch-off:   τ  =  L / ( c (1 − R) )
```

Evaluated for that same three-metre cavity, the ring-down time depends
only on the mirrors:

| reflectivity | mirrors | ring-down τ |
|---|---|---|
| R = 0.95 | household silver | 200 ns |
| R = 0.99999 | research dielectric | 1.00 ms |
| R → 1 | perfect mirrors | unbounded |

**The formula contains no term for how long the source ran.** Cavity
ring-down spectroscopy is an industry built on measuring exactly
this afterglow. The persistence of the light measures the mirrors'
absorption rate — in this paper's vocabulary, their commitment rate — and
not the source's history. Then the informational point, which is the real question: is the stored light one photon stretched across the interval, or a
chain of dependent quanta? On discrete terms the two horns are one answer.
Each emission event opens one record. A photon in flight undergoes no carry,
by the never-rounds clause, which is the arithmetic u·v = 0 of the null
interval: zero proper measure at any coordinate duration. Each record is
therefore stretched whole across its flight, from emission to absorption, with
nothing ticking in between. The train is the ledger of such records, as many
of them as the source's emission count, each independent and none aging. The light does not carry its own history through the cavity. The history sits
in the emission ledger and the future in the commitment events. Between the
two the record simply holds — the held pair of §9, in flight.

## 17 · Relation to general relativity

The mechanism of §7 was stated in relativity's form deliberately, and the
agreement is structural at every point where relativity differs from Newton.
The pull is a deficit, not an agency: nothing reaches out, and the one
measurable force points up — the account a free-fall accelerometer gives. The weak field splits into the two faces this account derives for every long-
range sector. One is a sourced, one-signed, gravitoelectric face on the
existence layer. The other is a workless, circulating, gravitomagnetic face
with no monopole — the frame-dragging face, carried here by the ledger's net-
zero transform. Orbits do
not close, and their failure to close is the founding test: the perihelion
advances because closure is the exception (§15's comma row), which is
relativity's correction to Kepler read as arithmetic. Radiation begins at the quadrupole because the source's reference structure is an antipodal pair (§3). The boundary is kept as a theorem. This paper derives the dimensionless
structure of the interaction — sign, source law, exponent, event, rate and
coupling. The dimensionful apparatus of the metric enters through exactly one
declared calibration, the electron mass in §13. That follows the Scale
Theorem: no dimensionless construction yields a dimensionful magnitude, so a theory built from pure number must of necessity borrow at least one ruler. Here that ruler is the electron mass, the reference on which §13's coupling is read, in this paper's view the least compromised choice, the electron being elementary, stable and measured to parts in 10¹⁰. The cosmological chain of §14 makes its own single declared borrow, the cell of §21.10.

**The gauge of the account: serial order and simultaneity.** This
series has carried one open item by name since its relativity account
was first written: the register commits one union at a time, which seems to
carry a universal sequence — exactly the thing relativity forbids. The item
is discharged here by a theorem set about ledgers, each part pinned. First, unions whose records are disjoint commute. Either order leaves the
identical ledger, so sequence between them is bookkeeping rather than content.
That is the serializability of concurrent ledgers, distributed computing's
oldest theorem, holding here because the union writes only its own records.
Second, order carries content exactly where a record is shared. A record is
shared only by propagation, and propagation is one depth per tick — the clock
object's own rule, the carry that commits one cell per tick and never ripples.
The boundary of order-matters is therefore the light cone, derived as the
support boundary of the ledger. Third, a *frame* is a linear extension
of the causal partial order: a four-event diagram admits exactly five total
orders consistent with its cone, every one lands the identical final
ledger, and every cone-violating order lands a different one. The relativity of simultaneity is therefore not a threat the register must
survive. It is the register's own gauge freedom, read from outside. The
reshuffle is also quantitative on the paper's own rungs: β = 3/5, the ladder's
first boost, already reorders the spacelike pair (Δt, Δx) = (1, 2). No rung
ever reorders a timelike pair, because every rung sits below one. The cone protects order with the ladder's own arithmetic. Fourth, what
the register adds rather than concedes: the invariant content is the causal
partial order *and each record's own count* — proper time as committed
length. The infalling record and the far observer keep two ledgers of one
fall. In the exact toy of halvings the private record's total approaches the bounded
sum 1/2 + 1/4 + … → 1. That sum is bounded and completed at no finite depth,
which is the same censused approach as §12's. The shared account meanwhile
books a fixed charge of one half per halving and never completes. The freeze
is the ratio, and the ratio is the rate line. The freeze and the bounded
crossing are the same fall entered in two books, one bounded and one
unbounded, neither complete, with no shared fact left for them to disagree
about. What this forbids is stated with it. Order-dependence of any observable at
spacelike separation — signalling — refutes the commutation theorem and the
register with it. The register's structure must also appear as scale and never
as frame: the octave comb's phase may depend on separation only, so a sidereal
or velocity modulation of the comb would refute this section outright. That is also why a century of interferometer
nulls at parts in 10¹⁸ never touched the register: they probe frame
structure, and the register has none to offer them. Every claim of this
block is pinned in `verify/test_serial_order.py`.

## 18 · The present state of the field, and what this account offers it



**Loop quantum gravity** shares this paper's central conviction — that the
continuum is not fundamental — and holds, as its definite prediction, a
discrete spectrum for measured areas. Where it stands: its discreteness is installed at the Planck scale, where no
experiment reaches. Its classical limit — recovering the smooth spacetime we
measure — remains the named open problem of the programme. And quantization
ambiguities have kept it from a crisp numerical prediction in the laboratory
regime. The discreteness here is the register's rather than a postulated
geometry's, so the continuum limit is the envelope by construction, read
against §19's still-open container account, rather than an unsolved dynamical
recovery problem. The account also produces numbers with failure conditions
attached: a value of G inside the live experimental discordance, a saturation
density, and an expansion rate. Each is falsifiable now, at bench and survey
precision, rather than at the Planck frontier.

**String theory** is the most developed quantum theory of gravity. A
graviton appears in its spectrum by necessity, the Einstein equations arise
as its leading consistency condition, and its dualities have produced exact
results no other programme possesses, including a statistical count of
black-hole microstates for special charge configurations. Where it stands: its solutions form a landscape with no accepted selection principle, so it derives no measured coupling. Its constructions live at the Planck scale and in higher dimensions whose reduction to four is not fixed. It states no falsification condition of the kind §23 lists. What this paper
offers that it cannot is a coupling with a number and a null attached, at
bench precision. What it possesses that this paper does not is a complete
perturbative quantum theory of the graviton.

**Asymptotic safety** conjectures a nontrivial ultraviolet fixed point that
would render quantum general relativity predictive with no new structure.
Functional renormalization calculations support the fixed point's
existence, and its low-energy predictions remain scheme-sensitive. Its
premise is the inverse of this paper's: the continuum retained and rendered
finite by the flow, rather than replaced by the register.

**Modified Newtonian dynamics**, Milgrom's programme, shares a different conviction — that
gravity's own phenomenology, taken seriously, is speaking — and its
acceleration scale a₀ ≈ 1.2 × 10⁻¹⁰ m s⁻² organizes galactic rotation with
considerable economy. Where it stands: a₀ is fitted rather than derived, in every version of the
theory. The current decisive test is the internal dynamics of wide binary
stars, where no dark halo can hide. From the same Gaia data it has produced
published claims of Newtonian behaviour at nineteen sigma and of MONDian
behaviour at ten, a contradiction still standing in the literature. No relativistic completion is settled. Its external field effect also violates the strong equivalence principle, which is the line this account draws on the other side. The Nordtvedt parameter is exactly zero here (§21.6) and the composition dependence of free fall is excluded (§7.2), so the two are separable by the composition experiments as well as by the rotation curves. The galactic regime is carried here as
an **open account, with the route named and the first exact results on the
record.** The route is the register's far structure, and three results
already stand. First, a refusal. A bare far ceiling on the register — the horizon — subtracts
a constant from every pair's potential, within an exact derived bound
proportional to d over the horizon squared. It leaves the force law untouched
at any separation far below that ceiling, so no flat rotation curve comes from
a cutoff alone. The constant left behind is a vacuum-shaped term, one part per
pair in the horizon, which is the standing cosmological-constant signpost
arriving from a second direction. Second, a scale. If the mechanism produces an infrared acceleration at all it
is horizon-set, and the horizon this account's own chain fixes puts cH₀ = 6.81
× 10⁻¹⁰ m s⁻². That is within a soft geometric divisor of the fitted a₀ ≈ 1.2
× 10⁻¹⁰. The order is reached with zero parameters, and the divisor is not
derived. Third, a fingerprint that is distinctive either way. The contact sum is
exactly self-similar under the doubling of separation. Any residual this
mechanism imprints on a rotation curve is therefore periodic in log r with
period ln 2, which is one octave. Neither the halo nor the modified law
predicts that signature, and it is a reanalysis target for the same survey
data both of them fit. The first route, the ensemble statistics of chained union events, has produced a result
that was not ordered in advance. Committed composites carry at exactly the sum
of their parts' rates, and coincide with any test clock at the product law, so
bound matter superposes exactly. Every laboratory and solar-system test of
superposition therefore passes untuned. Uncommitted ensembles, by contrast,
exceed superposition by the commensurability excess, a factor growing as
(6/π²) times the log of their period diversity. The prediction is anomalous
pull exactly where matter is diffuse and none where it is bound and tested.
That gives the dark sector's direction as a derivation rather than a fit; the
magnitude awaits the period-mass map. The remaining routes —
the geometry of orbits on the ultrametric horn, the enhancement over
realistic spectra — stay open on the record. Beyond the account, this paper offers what a fitted constant cannot: a coupling that is derived, the wheel of §13 carrying no dial to turn, and an interaction event with a ledger. Neither the halo picture nor the modified force law has either.

**The experimental record this paper's conditions actually touch** is
precise and mostly recent. The inverse square law is tested clean to gaps of roughly fifty micrometres,
with micro-resonator platforms pushing below that. Those nulls already exclude
this paper's stepped sharing profiles under the Euclidean reading of §12. The
surviving fingerprint is a log-periodic residual repeating once per octave of
separation. It is a reanalysis target for exactly those datasets, since
existing analyses fit Yukawa forms and would not have flagged it. The G determinations remain
mutually discordant at the hundred-ppm level, which is the corridor §13's prediction occupies and the convergence that would end it. Laboratory light
has been slowed by seven orders and parked outright in atomic coherence —
the dressed-rate physics §16 places on the record's side of the ledger. And
the equivalence principle stands confirmed at parts in 10¹⁵, which is this
paper's own §5 passing continuously. **The programs that reached these targets first, and what separates
them.** Three lines of work arrived at parts of this paper's territory before it.
*Thermodynamic and entropic derivations came first.* Jacobson recovered the
field equations as an equation of state across local causal horizons, and
Verlinde recovered Newton's law from entropy gradients on holographic screens.
Together they established that gravitation can be read as bookkeeping before
it is read as geometry, which is this paper's premise and was theirs first.
The separation is in what each takes and what each gives. Both accept an area-
entropy relation as input, where here πN² is an algebraic identity of the
count. Both are silent on the coupling's magnitude, where here the coupling is
a number with a null attached. And neither forbids a fine structure in the
force law, where Part II does. *Causal set theory is the nearest relative, and the one whose language §17 approaches.* Order and number giving geometry is the formulation of Bombelli,
Lee, Meyer and Sorkin. Discrete general covariance — the requirement that a
growth dynamics not depend on the order of its steps — was posed for causal
sets by Rideout and Sorkin before it was posed here. That literature also established the hard part this paper has not supplied. Only a random
sprinkling is known to avoid a preferred frame, and a regular substrate
generically defines one. What this account brings that the kinematics
does not is a mechanism — an event with a rate, a coupling with a value,
a residual with a period. *Discrete scale invariance*: the octave comb's
mathematical form is not new, log-periodic corrections to power laws
being the standard signature of a discrete scaling symmetry in Sornette's
sense. Saying so strengthens the proposal, because the difference is the
parameter that decides everything — in that literature the preferred
ratio is fitted per system, while here it is forced to two by the
register's base and admits no adjustment. The template is theirs; the
fixed period is this paper's, and it is what makes the reanalysis a test
rather than a fit. Causal dynamical triangulations obtains a
spectral dimension flowing to four from a sum over discrete geometries. That
is a dynamical answer to the question §19 leaves open, and a place where another programme has what this one does not.

The programmes above install discreteness by hand where no instrument reaches, or a constant by hand where every instrument does. This paper derives its discreteness, constant and event from one object, and places every claim within reach of existing instruments.

# PART VI · THE REMAINING REGIMES

A claim of identity cannot be regional: there are not several solutions to gravity, and a proposal that cedes a regime is an opinion about the others. This part carries the three remaining regimes — the dimensions, the orbits, the strong field — each with its first exact results and its open items named in place. Every numbered fact below is pinned in the suite of §24.

## 19 · The dimension of space: the contact-count window at two, three and four

Every part above works in three space dimensions and one time, and assumes
the number three. That is not derived here — no derivation of three is
claimed — but the question now has the exact structure it stands on, which it
never had before.

**The ladder.** The root systems of the ADE chain in dimensions one through eight have
cardinalities equal to the kissing numbers of their lattices. Those are the
contact counts of optimally packed equal cells, with optimality proven in
dimensions 1, 2, 3, 4 and 8 and best-known standing in 5, 6 and 7. Every rung
is a seat of this theory. The ratios along the ladder run 3, 2, 2, 5/3, 9/5,
7/4, 40/21. The count doubles exactly and only across dimensions two to three to four —
the hexad to the chromatic ring to the root. The octave operation is therefore
the dimension step precisely in the window holding physical space and
spacetime, and nowhere else. At the division-algebra dimensions (1, 2, 4, 8) the counts are
2, 6, 24, 240, with ratios **3, 4, 10**. And a second ladder stands honestly
beside the first: cubic register cells make face contacts 2D — landing **6
and 8** at the physical dimensions, where the packing ladder lands 12 and 24.

**The bridge between the ladders.** The cubic pair at the physical
dimensions is not arbitrary. **Six is the decimal period of the prime seven,
and eight is the decimal period of the prime 137** — the gravitational and
electromagnetic primes supply the two contact counts. The pair flanks the
seed, and its product is twice the root:

```
6 · 8   =   48   =   7² − 1
```

The packing pair's product resolves the same way, one prime up:

```
12 · 24  =  288  =  17² − 1  =  16 · 18
```

where 16 and 18 are Fa and Sol on the root 12, flanking the spine. The two
primes couple exactly as the two forces do:

```
137  =  8 · 17 + 1           ord₁₇(2)  =  8
```

The cubic ladder speaks the *periods*, the packing ladder speaks the
*seats*, and the bridge is the pair (7, 17).

**Three independent faces assemble here**. The Lorentz group's six generators are
two triads, three boosts and three rotations, and its sky is the two-sphere,
which makes space three-dimensional given the octave-boost identification. The
observed 3 × 10⁸ and the rest 3(10⁸ − 1) differ by exactly three, the
dimension count, in a units reading flagged where it was established. And the
figure's own oscillation spectrum carries exactly four distinct frequencies, a
3 + 1 count in the object itself.

**The account's state, iron:** not closed. The question is transformed rather than answered. "Why three dimensions" has
become "why does the register's contact structure realize the ADE ladder at
the doubling window". The selection condition is then named: derive from
carry, union and cell mechanics that equal-cell contact realizes A₃ in space
and D₄ in spacetime, or exhibit the two ladders as faces of one structure. A
mathematics question with a yes-or-no answer.

**Characterising the window.** That question is not answered here; rather, it is relocated. Across dimensions one to eight the contact counts run 2, 6, 12, 24, 40, 72,
126, 240. In exactly dimensions two, three and four — and nowhere else — the
count is 3·2^(d−1): three times a power of two, the two generators and nothing
besides. Beyond the window a foreign prime enters at once: a five at five, a seven at
seven, a five again at eight. The test is stricter than smoothness, since
seventy-two at dimension six is itself a two-three word and yet does not take
the form. The register refines a cell into 2^d children, the same eight that regulates
the cascade of §12. Within the window the contact count is therefore exactly
three halves of the child count. That holds at each of the three dimensions
and at none of the others. The window is where contact and refinement stand a
fifth apart. Both physical slots are interior to it, twelve in space and
twenty-four in spacetime, with its edges at two and four. **The window is an extremum, not a coincidence.** Divide the two
counts by one another and read what comes out. Contact per child is one
at a single dimension, exactly three halves at two, three and four, and
then falls away — 1.25, 1.125, 0.98, 0.94, downward. So the window is
where **contact per child attains its maximum, and that maximum is
exactly the fifth.** Contact is what a cell can union with, and refinement is what a subdivision
costs. Their ratio is union opportunity per unit of refinement. The register
sitting at that maximum is therefore a least-action statement in this
account's own currency rather than an imported one.

The result is secure rather than provisional. The saturation is proven,
since the contact number is settled exactly at the window's three
dimensions. The failure outside is tested against the best upper bounds, so no future
packing can disturb it. Five dimensions is the closest call anywhere, forty-
four against a ceiling of forty-eight. Every larger dimension is far below,
with contact numbers growing like 2^0.401d against a ceiling growing like 2^d,
a gap that widens without bound. One exception is recorded: the fall is not monotone,
rising once at twenty-four where the Leech lattice is exceptionally
dense — far beneath the maximum, and not touching where it is attained.

**A second characterization requires no extremum.** Read the
contact counts in the register's own two generators. At one dimension the
count is two — pure doubling, no three. At two, three and four it is
2^a·3, carrying **exactly one three**. At five a **five** appears, which
the register does not have. So the window is the half-open interval
between the second generator's first appearance and a foreign prime's,

```
[ first three , first foreign prime )  =  [2, 5)  =  {2, 3, 4}
```

which is the doubling window exactly, stated with no optimization anywhere in it. The register does not choose the window: it can only
spell contact counts in the generators it has, and this is the stretch
over which contact is spellable. The maximum is a consequence, since one
three over a power of two forces the ratio to three halves. Six
dimensions would also fail, seventy-two carrying two threes — but the
five arrives first, so a prime foreign to the register is what shuts the
door. Six candidate principles were tested and four rejected: being a
two-three word admits six as well, contact merely keeping up with
refinement admits one through six, exact knowledge of the contact number
admits eight, and a half-integer ratio admits one. What remains to be shown is
narrower and nearer the mechanics — why contact should cost exactly one
three rather than none or two. Pinned in `verify/test_the_contact_window_interval.py`, `verify/test_the_promotion_window.py` and `verify/test_the_contact_maximum.py`.

## 20 · Orbits: Kepler's third law exact, and the precessing conic family

The kinematics this section stands on is derived rather than imported. A
companion volume locates each classical postulate in the theory's own
structure. Inertia is the absence of any rest state, since a power of two can
never equal a power of three, so the substrate rotation has no fixed point to
stop at. The speed limit is the tick. The square of velocity is the Dirichlet
form applied to per-tick increments. Conservation is the append-only winding
ledger, and the orbit follows from stationarity. The third law is derived in the two-rider rule:
the force between riders is the count product read in two directions, and
the product commutes — action and reaction are one multiplication read twice.

**Kepler's third law is the fifth, both ways.** In the derived potential the period runs as the three-halves power of the
distance, and the distance as the two-thirds power of the period — the (3/2,
2/3) pair. The orbital exponent climbs the seats: one half at contact, one at
the first rung, three halves in the far field. An exact period deviation
accompanies it, T/T_Kepler = 1 + λ/r, whose power-law form no Yukawa
correction can imitate.

**The eccentric family, closed at first order in the deficit.** The softened potential's
expansion carries a 1/r² term, the classically exactly-solvable perturbation:
the orbit family is the precessing conic with

```
Δφ per orbit  =  −2πλ/p,        p = a(1 − e²)
```

— the circular result's radius replaced by the semi-latus rectum, retrograde
at every eccentricity, verified by integration across e = 0 to 0.6. Mercury's
perihelion advance is general relativity's and is untouched.

**Orbits are the octave residual's most sensitive instrument.** A
log-periodic force residual of amplitude A (§12) precesses a near-circular
orbit by

```
Δφ per orbit  =  (2π²A / ln 2) · sin(2π log₂ r + φ)
```

— amplitude 28.48·A, verified against direct integration to seven parts in a
thousand. Planetary ephemerides bound anomalous perihelion drift at the
milliarcsecond-per-century level; at Mercury's four hundred fifteen orbits a
century that reaches **A ~ 4 × 10⁻¹³ — eight to nine orders of magnitude past the laboratory's template sensitivity**. A single planet's unknown phase can null
a single measurement; the comb across several planets at different log r is
phase-proof. The solar system, with no new experiment required, is the operation
part's precision instrument.

## 21 · The strong field, the post-Newtonian order, and the structural accounts

This is the longest section of the paper and covers three distinct kinds of
material, so its scope is set out before it begins. **21.1 to 21.5** derive
the strong-field landmarks and the rotating sector. **21.6 and 21.7** carry
the construction to second order and settle the quadrupole coefficient.
**21.8 to 21.12** address the structural questions the account must
answer to be complete. They are the dimension of space, the relation to
curvature-squared gravity, the crossing from dimensionless to dimensioned,
what the account permits by way of repulsion, and what is not here.

**Every landmark radius of the strong field is a word in two and three
alone.** In units of GM/c²:

| landmark | value | the word | the seat |
|---|---|---|---|
| the horizon | 2 | 2 | the octave |
| the Buchdahl wall | 9/4 | 3²/2² | the fifth squared |
| the photon sphere | 3 | 3 | the motor |
| the marginally bound orbit | 4 | 2² | the double octave |
| the shadow radius | 3^(3/2) | shadow² = 27 | Re's seat |
| the innermost stable orbit | 6 | 2·3 | the hexad |

No other prime enters, and the ratios between landmarks are the intervals
themselves:

| ratio | value | interval |
|---|---|---|
| photon sphere / horizon | 3/2 | the fifth |
| innermost stable orbit / photon sphere | 2 | the octave |
| Buchdahl wall / horizon | 9/8 | the tone |

At this file's first writing these stood as exact statements of general
relativity, read in the paper's seats. Every rung of the table stands on the paper's own materials, five of them from
the rate line's cascade in 21.2. The wall's row resolves separately, into
the count's wall at the photon station and the continuum's at the tone. The derivation begins
at the coefficient everything else hangs on: why two.

### 21.1 · The horizon

**The horizon's two is the mirror's two.** The deficit φ = GM/rc² is the one-way rate a record at r carries on its shared account with M — the
weak-field redshift, measured at coefficient one. A one-way rate, though,
is an amplitude, not an observable: §3 fixed the reference structure as an antipodal pair, and what is observed is the round trip across it. The round trip includes both legs, and counting is linear, so the observed rate is exactly

```
Φ(r)  =  1 − 2φ ,        φ = GM/rc²
```

with y = √Φ as its amplitude — the half-power read, the theory's one
composition law, whose origin is now on the table. The rate is exhausted
where the two legs of an observation consume the whole unit:

```
2φ = 1            r = 2GM/c²
```

**The coefficient of the horizon is the number of legs in an observation.**
That two is the octave's two and the tower's two: the doubling equals the
sum of all the halvings,

```
1 + 1/2 + 1/4 + 1/8 + …  =  2
```

which is the ceiling the saturation count already carries — one number in
three settings, the derivation proceeding through the first.

### 21.2 · The circular-orbit landmarks

**The cascade of circular orbits.** Hold a record on a circle. It never
moves radially, so the radial term of the metric never enters; the inputs
are the rate line, the deficit φ = GM/rc², the areal subtense r², and
stationarity. Balancing the gradient of the rate against the gradient of
the subtense gives

```
Ω²  =  GM / r³
```

which is Kepler's third law, surviving exact into the strong field. The
local orbital speed follows, and with it four landmarks. Each is derived,
not fitted; each falls at a rational value of φ. Radii are quoted in units
of GM/c².

```
     local orbital speed²   =   φ / (1 − 2φ)

     reaches light speed at        φ = 1/3        r = 3
       the photon sphere;  capture parameter  b² = 27,
       so the shadow radius is 3√3
```

```
     circular energy        =   E²  =  (1 − 2φ)² / (1 − 3φ)

     equals rest energy at         φ = 1/4        r = 4
       the marginally bound circle

     stability edge factors as   (1 − 2φ)(6φ − 1)

     so the innermost stable orbit is at

                                   φ = 1/6        r = 6

       with       L²  =  12 (GM/c)²        E²  =  8/9
```

The energy 8/9 at the innermost stable orbit is the whole tone, inverted:
the deepest stable seat lies one tone of intensity below rest. The fraction
released on the way down,

```
1 − √(8/9)  =  0.0572…   =  5.72 percent
```

is the accretion efficiency of every non-rotating engine in the sky.

Collected, the derived rungs in deficit units are

```
φ  =  1/2,   1/3,   1/4,   1/6
```

These are the partials of two and three. The fifth partial is absent, as a
two-three algebra requires: **no landmark sits at φ = 1/5, and a landmark
found there would refute the exclusivity.** The wall's row is resolved in
its own block below.

**What is not attained.** Approaching the horizon halves the remaining rate one register depth at a time; resolving 2φ = 1 exactly is the same
unfinishable census that excludes the singularity in §12, one level up. The
floor is approached forever and occupied never, in every outside read — the
collapse continues; it does not conclude.

**What this derivation covers, and what it does not.** It is the time-time word and the angular geometry only — circular records never move radially, which is why these rungs were derivable without the radial word. The word itself is derived after the wall's block below, where it completes the exterior metric. Landmarks are
hereby forbidden off their stations: a measured photon ring, innermost
stable orbit, or bound circle away from the deficits 1/3, 1/6, 1/4 — away
from the two-three words — refutes this account at the rung in question.
Every claim of this block is pinned in
`verify/test_ceiling_two_horizon_two.py`.

**The wall resolved: the count gives the fifth, the continuum gives the
tone, and experiment distinguishes them.** The derivation uses the register's own counting, with no identified rule in
it, and it rests on three established results and nothing else. Pairwise rates are bilinear and composite rates add, so a
clock's share inside matter is the shell count itself. In a uniform body,

```
d(r)  =  (3/2) φ_R  −  (1/2) φ_R · r²/R²

   at the surface   r = R :   d = φ_R
   at the centre    r = 0 :   d = (3/2) φ_R
```

so the centre sits a fifth deeper than the surface. And the observed rate
is the exterior's own rule
applied without amendment — the round trip includes the endpoint's share on
each leg, linearly — the same two legs and the same linear counting that
produced the rate line exactly. One rule, inside and out:

```
Φ(r)  =  1 − 2·d(r)
```

with the surface seam automatic. Two checks before the consequence. Inside a hollow shell the share is constant, so the read is the constant √(1 −
2Gm/sc²). That is identical — exactly, not approximately — with what the field
equations give there. Where the clock stands in vacuum, count and continuum do
not differ at all. In the weak field the amplitude is 1 − d,
the shell potential again. The consequence is the wall, and it is
arithmetic with no joint: the center reads √(1 − 3φ_R), which vanishes when the surface deficit reaches **one third — the photon station**. The floor is
the half, the center sits a fifth deeper, and the half over the fifth is
the third: **the count's wall coincides with the photon sphere. No static body sits inside its own circle of light.** The uniform body is the extremal case rather than a special one. Under the
count's rule, any concentration of the profile deepens the centre's share and
lowers the ceiling; a near-point core caps below compactness 0.12. The wall at
2/3 is therefore profile-independent over exactly the monotone class
Buchdahl's theorem governs, which makes it the count's own theorem. Collected:

| | the count | the continuum |
|---|---|---|
| wall radius | 3 (the photon sphere) | 9/4 (a tone above the horizon) |
| compactness ceiling | 2GM/Rc² = 2/3 | 8/9 |
| surface-redshift ceiling | √3 − 1 = 0.732 | 2 |
| wall over horizon | 3/2, the fifth | 9/8, the tone |

 The continuum answers the same
question
through its interior machinery — pressure entering the source, field
feeding field, the spatial word — and its central pressure
(1 − y_R)/(3y_R − 1) poles exactly at its own wall. The scalar face builds neither wall. The tone is what the continuum's second
face adds, and the fifth is what the count keeps. The two walls sit a fourth
apart: 3 over 9/4 is 4/3, and the fifth is the tone times the fourth. Even the
disagreement is interval arithmetic. The fork belongs to experiment, and it is stated as a window. A static body
observed with compactness between 2/3 and 8/9 — surface redshift between 0.732
and 2 — decides for the continuum's extra sourcing. So would any confirmed
surface hiding inside its own photon sphere, the signature now hunted as
light-ring echoes in ringdown data. Either outcome retires the count's
interior while leaving the exterior cascade untouched. A surface beyond 8/9
retires both. The window is empty at this writing — weighed honestly, both accounts predict emptiness through the realistic equation-of-state range, so the emptiness alone scores lightly. The exposure is what carries weight. Causal equations of state let the
continuum populate the window to compactness near 0.85. One sufficiently
massive compact star would then meet the count's wall while leaving the
continuum untroubled — the class that GW190814's 2.6-solar-mass secondary
would join, were it a star with radius under twelve kilometres. The light-ring-echo channel is not a second exposure, since the block below
shows this floor returns no echo train at all. The record there is stated for
what it is: claimed detections have not survived independent reanalysis, and
they constrain parked surfaces, which this account does not predict. In the weak field
the two interiors agree through first order and split at second by exactly
(3/8)φ_R² — below any current measurement, which is why no existing test
has ever chosen between them. Every number of this block is pinned in
`verify/test_the_wall_derived.py`.

**The spatial word: the ruler supplies the variation, and the metric
completes.** The last named word of the weak field follows from an established result of the programme: a quantity is a directed object with a sum face and a difference
face, and the two reads of the register divide between them. A clock is a
sum-face read, compared remotely — it registers the account's *value*, both
legs, and that is the rate line already derived. A ruler is a
difference-face read, compared locally, address against adjacent address —
it registers the account's *variation*. The shell theorem then does the rest. Outer shells carry value without
variation, so their account is constant where the clock stands, which is
exactly why they exert no pull. They slow the clock and leave the ruler alone.
The ruler's whole charge is therefore the enclosed account's edge amplitude:

```
dℓ  =  dr / y_enc ,        g_rr = 1 / (1 − 2 φ_enc(r))
```

Three regimes land at once, none adjusted. Outside a body the account and the enclosure coincide, so the two faces
discount equally: γ = 1, exactly rather than approximately. The exterior
metric then assembles to Schwarzschild's, exactly: (1 − 2φ) dt² − dr²/(1 − 2φ)
− r² dΩ². Inside a
uniform body the ruler word is the interior solution's own. Inside a
hollow shell the enclosure is empty: **space is exactly flat while the
clock still registers the account** — the split general relativity itself
carries, reproduced here by the two faces of one count. The classical file follows in a single motion. Light bends by the full
4GM/c²b, the temporal half from the rate line and the spatial half from the
ruler word, so the factor of two that began this account is derived rather
than assumed. The Shapiro delay carries its (1 + γ) = 2. The parametrized β is
one as well, since the metric is Schwarzschild in areal form. The perihelion
base is the metric's own 6πGM/pc², with the comma reading of §17 standing on a
derived floor. One localization sharpens the wall's fork rather than
touching it: inside matter the spatial words of count and continuum are
the same function, so the fork sits in exactly one place — the interior
clock — and nowhere else. What this forbids: a confirmed γ − 1 ≠ 0 at any
precision — the Cassini bound stands at parts in 10⁵ and every future
tightening must land on one — and any measured spatial curvature inside a
hollow shell. Every claim of this block is pinned in
`verify/test_the_spatial_word.py`.

### 21.3 · What replaces the singularity

**What replaces the singularity** is the saturation of Part II: reaching
zero separation is a supertask, the register has a deepest cell, the
potential saturates at a derived ceiling. No regulator — the count's own
finiteness. **What replaces the horizon** is a never-attained floor: the read
y is strictly positive above the trapped radius, and the no-attained-zero principle gives the horizon the same office the tonic and the speed limit
hold — *approached forever, occupied never*. In the register's serial order the infalling record's commitment rate freezes.
Relativity's finite proper-time crossing is the envelope read along the
worldline. Section 17 discharges the confrontation between the two: order is
the ledger's gauge, and the invariant content is the causal partial order
together with each record's own count. The freeze and the finite crossing are
the same fall booked in two ledgers, the shared account and the private
record, with no shared fact left for them to disagree about.

### 21.4 · The wave sector: ringdown and accretion

**The wave sector.** The wave's speed is c because its record is null, with no
carry in flight. The binary-neutron-star record is the passing measurement of
exactly that statement: wave and light arrived together across a hundred
million light-years, their speeds equal to parts in 10¹⁵. Radiation begins at
the quadrupole, with the nephroid rung holding the slot at signpost grade. The
coupling's structure as an exact square, which is the double copy's shape,
stands in Part III. One null term is outstanding and is named here rather than omitted: the weak-
field deflection coefficient, the doubling of Newtonian light-bending that
general relativity states and measurement confirms. Both halves are now
supplied, the temporal by the rate line and the spatial by the ruler word
above. The null sector's entry is therefore closed, and the full deflection
and the Shapiro delay are the metric's own. **The entropy identity.** The horizon's entropy πN², with N the horizon
measured in Planck lengths, *is* the area law S = A/4 algebraically. It uses
one licensed dimensionful reference, as the units principle requires. The
paper's three visible anchors then reduce to one. The Planck length is
√(ħG/c³) with G the coupling wheel's own output, so it returns to the electron mass.
The cell's femtometre is a calibration and is labelled as one. The ruler count
net of derivations is therefore one —

**and that count is not a discipline kept but a consequence of what the
register counts.** The natural question, once a coupling has been read
off a wheel, is whether the action quantum can be read off one too. It cannot, and the answer arrives before any scan. A wheel is a ratio of
integers and the action quantum carries units, so the Scale Theorem forbids
the construction outright. That is a proof that looking is the wrong move,
rather than a search that failed. What stands in its place is
better. Follow the register's own units with the map of §10 in hand:
energy is a carry rate, time is a count of ticks, and their product —
action — is a count of **carries**. Action in the register is a pure
count, and **the quantum of action is one carry**. It is not a number to
derive; it is the unit the counting is done in, which is exactly why no
wheel can carry it and why none is needed. The same holds one step over:
the speed limit is one cell per tick, the cone rule of §17, likewise a
register fact rather than a convention. So the register's natural units
are its own accounting, not a convenience, and exactly one ruler is left
to borrow — a mass. That is what the magnitude above used, and nothing
else. Recorded beside it, the banked negative it belongs with: the
quantum sector's own dimensionless coupling misses every small-block
wheel by thousands of parts per million where the electron's
gravitational coupling lands inside a hundred. Pinned in `verify/test_the_action_unit.py`, with the two-dimensional storage reading standing behind it at reading grade.

**The ringdown, and what the floor does to it.** A floor approached
forever invites the obvious question — does it ring? The answer is a null,
and the null is a statement. A surface parked at a fixed depth ε above the
floor returns echoes at the constant delay 4M ln(1/ε), and that constant
spacing is the template every published echo search uses. This floor is
not parked. Its tortoise speed is −1/(1 + ε)^{3/2}, which approaches −1, so the falling
surface is asymptotically null — the same speed as the radiation chasing it.
The closing rate is therefore only 1.5ε. The total remaining closure ∫1.5ε dt
= 3Mε is finite and minuscule against the light ring's own ~45M gap. Infalling radiation never reaches the surface.
There is no echo train. In this channel the never-attained floor and a horizon
are indistinguishable, so the echo searches' nulls neither support this
account nor touch it. A confirmed constant-spacing echo train would refute the
floor's kinematics.

**The accretion accounting, and the law it satisfies.** A growing floor
appears to swallow layers the outside book never saw crossed. It does not,
because the floor is not a place records pass through: it is where the
outside read's rate factor 1 − 2GM/rc² vanishes. When the mass grows, the rate factor at a fixed radius passes through zero, and at that moment the
record's *shared* rate reaches zero while its *private* ledger runs on
untouched. **Freezing is the event; no crossing event is required.** The
frozen count then carries the mechanics without further assumption. With the horizon counted in Planck lengths the entropy is πN². The count
therefore grows as the square of the mass and strictly increases with every
accretion. The area theorem is not an extra law here but the irreversibility
of freezing. And the identity dE = T dS holds exactly,
with the horizon's own temperature — **the bookkeeping for a growing
floor is the first law of black-hole mechanics, in the count's own
words.** Both results are pinned in
`verify/test_the_floor_and_the_ledger.py`.

### 21.5 · The rotating sector

**The rotating sector: the drag is the round trip's other face.** Every
observed engine spins, and the ladder above is the resting slice — so the sector is opened here with the principle already in use rather than left as an entry. The rate line was the round trip's **sum**: two legs, each carrying the deficit. A rotating source makes those two legs unequal. What the round trip's
difference returns is precisely a Sagnac reading: the same two legs, the same
inverse distance and the same coefficient two, on the difference face instead
of the sum face.
Identifying the difference-face charge with the source's angular momentum
— this block's one named identification, as the interior rule was the
wall's — the words read

```
g_tt = −(1 − 2M/r)     the sum face, the rate factor
g_tφ = −2J/r           the difference face, the drag
g_φφ = r²              the areal subtense
```

and everything else follows without addition. The dragging rate is
−g_tφ/g_φφ = **2J/r³, the Lense-Thirring rate exactly** — the frame
dragging that Gravity Probe B and the laser-ranged satellites measure,
and the first test this account named for itself when the entry was still
empty. The landmark stations then track the rotating solution's to first
order in spin: the innermost stable orbit moves with slope −4√(2/3) and
the photon orbit with −2/√3, both reproduced by the derived words rather
than imported.

Two limits are printed rather than stretched. Taken alone these are the first-order-in-spin words, and the residual against the exact rotating solution grows as the square of the spin — the geometry's own quadrupole, which the block below now supplies. And spin moves the stations **off** the two-and-three
rationals: the shift coefficients are irrational, so the ladder is the
resting skeleton and no arithmetic claim survives a continuous spin
parameter. The landmark condition of §23 binds accordingly — at rest on
the stations themselves, and in rotation on these first-order shifts.
Pinned in `verify/test_the_rotating_sector.py`.

**The second order, and the slot it lands in.** The first-order words
left the rotating geometry's own quadrupole unaddressed. Locating it settles most of the question. In the equatorial plane the two
words this account derived are exact to all orders in spin, since the sum face
and the difference face take no correction whatever. Everything at second
order therefore sits in the two spatial words, which is where the register
would put it: the temporal pair came from the round trip, and the spatial pair
from the ruler's own charge. Nor are those two independent: the
combination g_tφ² − g_tt·g_φφ is the deficit polynomial exactly, so once
the deficit is fixed the subtense follows. Two spatial words, one unknown.

The clause that fixes it is one the theory already carries. **The
deficit gains the difference-face charge squared:** 2M/r becomes
2M/r − (a/r)², with a the ratio of the difference charge to the sum
charge, and the coefficient of the new term is one. The coefficient is
fixed by the stationary field equations of §21.6 rather than by
comparison. Write the two faces as one potential on the prolate chart, px − iqy: the
sum face linear in the radial coordinate, the difference face linear in
the angular one. Here Mp is the horizon's offset from the mass and
q = a/M. The equations are satisfied if and only if
p² + q² = 1, the residual off that circle being exactly
2(px + iqy)(p² + q² − 1), and on the circle the deficit polynomial's
constant term is M²q² = a². The coefficient is therefore the unit norm of
the two faces' potential: the horizon offset and the difference charge
are the legs of a right triangle whose hypotenuse is the sum charge, since
(M² − a²) + a² = M². The Kerr bound is the same circle read as p² ≥ 0. The
*charged* non-rotating solution carries the deficit polynomial
r² − 2Mr + Q², so the difference-face charge occupies the electric
charge's slot with the same coefficient. That is the double copy written
as arithmetic, the shape this paper already claims at signpost grade, and
here a consequence rather than the source. Pinned in
`verify/test_the_clause_coefficient.py`.

Granting the clause, the rotating solution is the output, and it can be
checked as one.
The innermost stable orbit reproduces the exact values at every spin tested,
while neighbouring coefficients miss by wide margins. A half or a three-halves
is off by tenths of a mass at moderate spin, and by more than a mass near
extremal. Three things arrive that were never imposed: the horizons as the deficit
polynomial's roots, M ± √(M² − a²); the extremal limit, where they merge at M;
and the Kerr bound itself. Beyond a = M the polynomial has no real root, so
the account forbids naked spin as its own discriminant rather than by decree. With the spin
off, the clause vanishes and the resting ladder returns intact. Pinned in
`verify/test_the_quadrupole.py`.

**Locating the remaining gap.** This section has carried "the tensor face
beyond linear order" as though what were missing were field equations.
That is not what is missing, and saying where the gap actually sits is
worth more than restating that it exists. The law is already assembled from derived pieces. The deficit at a point is
the shell-summed census over all source records, with composite counts adding
exactly. The sum face registers it twice, the difference face registers its
variation, and the subtense is areal. In one sentence — **solve for the count, then read it.** With one
source that rule is exact to all orders: the census gives GM/rc² and the
read is the vacuum solution in the areal coordinate, which is why every
landmark above derived rather than being fitted.

Where it breaks is **the coordinate**. The same deficit read in the areal
and the isotropic coordinate differs at second order — by exactly twice
the square — and for a single source the subtense settles the matter, the
ring's own circumference fixing the radius. For a general source there is
no areal radius, and the rule as stated selects nothing. That is the whole of the gap, and it is a far better-posed problem than
deriving a field equation, because the register already carries the candidate.
The fork closure of §12 states that Euclidean separation is the envelope of
the register's shared-prefix coordinate. For one source that envelope *is* the
areal radius. For a general source it is defined and has never been
computed.

The divergence from the received theory is located along with it, and
§21.6 resolves it. The composite clause makes deficits add **exactly**, and
the question was whether the received theory's do, the field's own energy
sourcing more field. The resolution has two parts. The deficit does superpose, being the harmonic potential, while the metric does not, the quadrature supplying the cross term. Where the field circulates the clause gives way to the equations themselves, so that the two-body comparison at second order finds no divergence. What remains is the
multi-source envelope for a general source, owed as apparatus. Pinned in
`verify/test_the_tensor_face.py`.

### 21.6 · The second-order construction

**The coordinate supplied, and its first test.** The rule the
register states in its own currency is **areas count cells**. For a single source the shell's own cell count is the areal radius. That is
why the read came out as the vacuum solution, with every landmark above
derived rather than fitted. The rule does not fall silent when the symmetry
does, since every surface's area is its own cell count whatever the source. That is a gauge condition written in counting rather
than borrowed from geometry.

Put it through the one multi-body measurement known to parts in a
million. General relativity's two-body periastron advance rides the
**total** mass, and the register's answer arrives by a different road:
each body rides the other's deficit, deficits add exactly, so the
correction rides the sum. **It matches.** The alternatives do not — a
correction riding only the larger mass gives half the advance, the
reduced mass a quarter — so the total is the superposition's own
signature rather than an accident of scaling. The residual against the leading formula is the next order of the same
equation rather than a disagreement. Weakening the field through six doublings
drives it down in proportion to the compactness, with a fixed coefficient near
seven and a half.

**That narrows the divergence rather than closing it, and locates it.** The advance rides the total, and is therefore blind to how that total is
apportioned between the bodies. Apportionment is precisely where the two
constructions differ. General relativity's first-order acceleration of one
body carries a term in that body's own mass, while the register hands each
body only the other's deficit. No periastron measurement can see this. Observables that weigh
the bodies separately can, and the size is the system's compactness:
**two to four parts in a million in the binary pulsars, against timing
already at about one part in a million.** The last question of the
gravity account is therefore strong-equivalence territory, sized, and
already within reach of the instruments — not an open horizon. Pinned in
`verify/test_the_multisource_envelope.py`.

**The apportionment term closes, from words already derived.** The
worry was that handing each body only the other's deficit would violate
the strong equivalence principle. It does not, and the parametrized
framework settles it without new machinery. The Nordtvedt parameter is a
fixed combination of two post-Newtonian parameters, both of which this
paper derives:

```
   η  =  4β − γ − 3

   γ  =  1     from the ruler word
   β  =  1     from the isotropic transform

   η  =  4(1) − 1 − 3  =  0        exactly
```

— inside lunar ranging's four parts in ten thousand
and the pulsar ensembles' one. The register says the same thing
structurally: there is one mass attribute, the carry rate being the
rounding excess, so a body's binding enters its mass once and its
gravitational and inertial values cannot differ.

The closure is wider than the single term. At first post-Newtonian order
that framework is complete — ten parameters fix the dynamics entirely.
Two are computed here from the assembled metric; the remaining eight
vanish on the register's own structural results, the frame parameters by
§17's gauge theorem and the conservation parameters by §9's exactly
conserved count. Every one takes the received theory's value, so **the
whole of first post-Newtonian dynamics agrees, apportionment included** —
which is why the periastron advance came out right and why no
strong-equivalence test can separate the two accounts. The divergence
therefore cannot live at that order. It moves to second post-Newtonian,
where the parameters run out and the two constructions must be expanded
against one another directly. Pinned in
`verify/test_the_apportionment.py`.

**Second order: compared, and there is no divergence.** The comparison at second order is made here, and it closes the question rather than bounding it. Two facts decide it. The account's field equations
are Einstein's, with the derived coupling, wherever it has built a
construction. Its one shortcut, the exact superposition of deficits, is a
theorem in every class with a Killing reduction and fails the vacuum
equations at second order in the circulation. Where the binary circulates
the account therefore supplies no alternative rule, and the conservative
two-body dynamics are the received theory's own at second post-Newtonian
order and beyond. The account's structural statement there, that the rest
clocks are the masses' conjugates, is then checked against those dynamics.
Fed the received conservative invariants E(x) and J(x) through third
post-Newtonian order, the first law of binary mechanics returns the clock
rate of each body. The test-mass clock is √(1 − 3M/r) term by term, and the
heavy body's clock is its exact law −(m₂/M)x/√(1 − 3x) through x⁴. For the
small body the inverse clock reproduces the gravitational self-force series
of black-hole perturbation theory, u^T = (1 − 3y)^(−1/2) + q[−y − 2y² − 5y³
− (121/3 − 41π²/32)y⁴], including the π² term. That agreement between the post-Newtonian invariants and perturbation theory is the one Blanchet, Detweiler, Le Tiec and Whiting established, and the clock law carries it. The earlier bound from the double pulsar, a fifth of the second-order coefficient, is thereby
superseded: the coefficient is the received one. What the account adds at this order is not a different number but the reading — the helical count direction, the clock as its norm, and the law that makes the clocks the masses' conjugates. That is the kind of addition the paper makes throughout. The received theory describes how gravitation acts; this account states what the action is, the shortfall of a count, and where it is composition-related and where it is not (§7.2). Inspiral phasing and pulsar timing now test the same
coefficients, which this account shares with the received theory. Pinned
in `verify/test_the_2pn_comparison.py` beside
`verify/test_the_second_order.py`.

**The coordinate: a first attempt and its correction.** "Areas count cells" has a sharper reading: if every register cell is the same
size, the volume element must equal the flat one. That condition holds exactly
on both solutions this account derives — the non-rotating one, and,
equatorially, the rotating one. What it does **not** do is single out the
multi-source metric, and the attempt made here to complete it failed a
direct test. Reading the ruler as stretched along the deficit's gradient and areal
transverse reproduces the vacuum solution for a single source exactly. For two
sources its Einstein tensor does not vanish. Scanning the masses down three
decades shows the residual falling as the first power rather than the second. A rule that fails at linear order
fails before any post-Newtonian comparison begins, so that reading is
withdrawn rather than carried.

What the equations want instead is the ruler read as the same stretch in
every direction. There the residual falls as the **second** power
exactly, so that form is right at first post-Newtonian order — agreeing,
by a wholly independent route, with what the parametrized argument
concluded. But it is not exact even for a single source, where its
residual is also second order while the areal form's vanishes
identically.

**So the honest state is sharper than before, and it rests on a
computation rather than an intuition.** Two readings exist, each correct
in a different regime: areal exact for one source, the same-stretch form
correct to first order for many, and neither exact for many beyond that.
The rule the account requires is the one that reduces to the first with a
single source and to the second at first order with several — which is
the register's own account of the second-order potential. The instrument
that will decide it now exists and is validated: exact symbolic
derivatives, a vanishing Ricci tensor on the case whose answer is known,
and a clean power law on the cases whose answer is not. Pinned in
`verify/test_the_einstein_tensor.py`.

**The second-order word, half found.** The instrument settles the time
half at once. Adding a coefficient times the squared deficit to the rate line and scanning it, the value **one** drives the time-time
residual from second order to **third, exactly** — and no other value
does. So the second-order time word is settled: the rate line gains
twice the squared deficit, and that piece is pure monopole, carrying no
direction at all.

What survives is then wholly spatial, and it carries a shape worth
naming: decomposed, its traceless part exceeds its trace, so the
remainder is a **quadrupole**. That is the angular language of the
theory's own notation doing real work — the split into a directionless
part and a two-lobed one isolates the scalar fix and confirms it exactly.
But the same language shows where it stops. Three local candidates were scanned against the spatial remainder: a traceless
quadrupole built from the deficit's gradients, a scalar square, and the cross
product of the two deficits, which is the register's own bilinear union
object. None of them moves the spatial order. **The reason is structural rather than a failure of search**: the second-order potential solves an equation whose
source is the squared gradient, so it is an *integral* of the deficits
and not any algebraic function of them. The one place it does close
algebraically is the cross term, whose Laplacian is exactly the cross
source — verified — which is why the two-source piece has the right form
while the whole does not reduce to a formula.

So the account requires a solved equation rather than a chosen harmonic, and
it now knows which one and what it must reproduce. Pinned in
`verify/test_the_second_order_potential.py`.

**The rate line multiplies.** Chasing the second-order word turned
up something this account had wrong at the root, and the correction comes
from the theory's own kinematics rather than from any fit. §16 states
that factors *multiply* — that adding what composes multiplicatively is
the tempered error — and §21 then wrote the round trip's rate factor additively. Tested against the vacuum equations, the three forms separate. The additive
form leaves a residual falling only as the second power. Adding the squared
deficit lifts it to the third. The exponential, which is what multiplying two
legs actually gives, reaches the third power with a residual three times smaller still. **The squared term was never a correction to be discovered — it is the second term of that exponential, and the whole series is what the composition law required from the start.** The rate line is therefore written as the product of the two legs' discounts, with
one minus twice the deficit as its first-order truncation, which is the
form every result above used and remains exact where they were checked.

**The remaining word has its equation.** With the time word
multiplicative, the surviving residual is wholly spatial, and the equation it
obeys can be written down rather than searched for. For a static field the
vacuum condition sets the spatial curvature equal to the second derivative of
the time potential plus its squared gradient. Carrying the spatial metric one
order past the conformal form turns that into a **Poisson problem for the
trace-reversed second-order piece**. Its self
terms are solved by the one-body solution exactly. Its cross term's trace
is algebraic — the product of the two deficits has precisely the required
Laplacian, verified — while the traceless part needs the integral, which
is exactly why no local formula closed it. And the route that finishes it
is classical: two static sources are axisymmetric, so the configuration
lies in the Weyl class, where the second potential is obtained by
**quadrature** rather than guesswork. Pinned in
`verify/test_the_multiplicative_budget.py`.

**The quadrature, and the static sector closing exactly.** A static
axisymmetric field is a Weyl field, and the Weyl equations say two things
that this account has been saying independently. First, the time
potential is flat-harmonic, which is precisely the composite clause:
deficits summing with nothing added. Second, the remaining spatial word
is not free but is obtained from that potential by quadrature. Setting
the Weyl potential equal to the register's deficit and the time word to
the multiplicative rate line above completes the dictionary with nothing
left to choose.

**Theorem.** *Take the Weyl metric with both functions arbitrary. If the
deficit is flat-harmonic and the spatial word satisfies the two
quadrature equations, every component of the Ricci tensor vanishes
identically.* Computed symbolically, all sixteen do. So the construction
is exactly vacuum for every static axisymmetric configuration whatever —
any number of sources, of any shape — and not to any finite order. The
quadrature's integrability is general in the same way: its cross
condition reduces to zero by the harmonicity of the deficits alone, so
the spatial word always exists, and only its closed form depends on which
bodies are present. For two point deficits that form is

```
γ_cross  =  m₁m₂/(2a²) · [ (ρ² + z² − a²)/(r₁r₂) − 1 ]
```

**In the Weyl chart the single source is a rod of length 2m.** Which member of the class the register builds is fixed by the shape of its
source read in these coordinates. The register's own single-source answer
settles it: that answer is Schwarzschild's exterior, whose Weyl potential is
the potential of a uniform rod of coordinate length 2m. It is reproduced to
the last digit, where the point potential is not. The register's point mass is not a
point in this chart; it is the segment onto which the circle of light
maps, which is the same statement the strong-field section reaches from
the other side. The two potentials part only at third order in the mass
ratio, so the weak field and the post-Newtonian faces are indifferent to
the distinction; what it fixes is which exact solution is being named.

**The quadrature resolves the divergence rather than measuring it.** The standing
worry was that exact superposition must disagree with a theory whose
field sources itself, and the second-order comparison was to be scored
against the double pulsar. The subtlety was what superposes: the
**deficit** does, being the harmonic potential, while the **metric** does
not — the quadrature supplying a cross term that is nothing like a sum.
The composite clause was right, and the apparent conflict was a confusion
between the two objects. The agreement is quantitative rather than merely
structural. The register's static two-body force is the strut tension of the
next subsection, m₁m₂/(d² − (m₁ + m₂)²), which is Bach and Weyl's own
general-relativistic value. In the static sector the two theories therefore
share one exact solution to every post-Newtonian order. The divergence is
therefore confined to the genuinely dynamical two-body field, where no Killing vector survives, and there the comparison of §21.6 finds none. What lies outside this result is the sector it
never claimed: motion and radiation, where the field is not static.
Pinned in `verify/test_the_quadrature.py`.

**Two static counts cannot rest unsupported, and the register fixes the
support.** The cross term above does not vanish on the axis between the
two sources. On the axis outside both it is zero, and a small circle round the axis has circumference 2π times its radius. On the segment between them γ_cross = −4m₁m₂/d², with d the separation, and the ratio is e^{−γ₀} rather than one. A conical defect on the segment joining two bodies is a
stress holding them apart, Weyl's strut, read as a line source by Israel.
Its magnitude is fixed by the quadrature, F = (e^{−γ₀} − 1)/4 with γ₀ the
value on the strut. For point deficits that is m₁m₂/d² at leading order.
For the register's own source, the rod of coordinate length 2m, the quadrature gives γ₀ = ln[(d² − (m₁ + m₂)²)/(d² − (m₁ − m₂)²)]. The force is then exactly m₁m₂/(d² − (m₁ + m₂)²): the inverse square with the rods' total length subtracted from the squared separation, diverging where the rods touch. That is the Bach–Weyl force, obtained here by performing
the quadrature. So the static two-body sector forbids something: no two
counts rest in an elementarily flat axis, and the stress that holds a
static pair is not free. Pinned in `verify/test_the_strut.py`.

**Rotation comes inside, by the same route.** The stationary axisymmetric field has its own reduction, and the construction
lands on that one too. With the time word, the dragging word and the spatial
word all arbitrary, imposing the two field equations and the quadrature
annihilates every Ricci component identically. That is sixteen of sixteen
again, with Kerr among the solutions covered. So every time-independent field is exact, rotating or
not, and what stands outside narrows to the genuinely non-stationary:
motion and radiation.

**The static equation turns out to be this account's two statements
at once.** Written for the time word alone it says that f times its
Laplacian equals its gradient squared — which is identically the
statement that **the logarithm of f is harmonic**, that is, f = e^{2ψ}
with ψ flat-harmonic. The multiplicative rate line came from the round
trip's composition law and the composite clause came from the census
adding; they were derived by separate routes and they are the same
equation. Nothing was arranged to make them meet.

**Rotation exposes a statement the static sector could not show.** With
rotation the time word's equation gains a term and gains it negated,

```
f · lap(f)  =  (grad f)²  −  (grad χ)²

so that     lap(ln f)  =  −(grad χ)² / f²
```

which is **never positive**. The deficit becomes subharmonic: it can only
be shallower than the harmonic function with the same boundary values,
never deeper. **Circulation and depth divide one fixed rate, and what goes
into circulation comes out of depth, with no free sign in it.**
One-signedness with no choice available is this account's signature
elsewhere — the shortfall that is always exactly one and never over — and
here it arrives from the field equations instead. Checked on Kerr itself,
both sides agreeing to machine precision and both negative at every point.

**It locates where the composite clause ends.** Two static deficits
superpose with residual identically zero. Two rotating potentials do not. Each solves its own equation to one part in
10¹⁸, and their sum misses by two parts in a hundred. That is a different
order of thing rather than a small correction, and the logarithm that works in
the static sector does not rescue it. The clause is exact where the register counts and fails where
it circulates, which is precisely the boundary the sum and difference
faces were claimed to have. Pinned in `verify/test_the_twist.py`.

**Radiation closes the same way, which settles what rotation had put
in doubt.** Cylindrical gravitational waves have their own reduction, again with two Killing vectors, one of them now a translation rather than a time. Killing vector is the standard term, after Wilhelm Killing, for an exact symmetry direction of the geometry. The construction lands on it unchanged. With both functions arbitrary, the
cylindrical wave equation in place of Laplace, together with the same
quadrature, annihilates all sixteen components identically. That is
real radiation, carrying energy, not a static field relabelled. So one
construction covers three sectors, with only the deficit's own equation
changing beneath it:

| sector | the deficit's equation | the composite clause |
|---|---|---|
| static | Laplace | exact |
| stationary | twist-sourced, nonlinear | fails |
| radiative | cylindrical wave | exact |

The question the rotating sector raised was whether the clause fails
whenever the field stops being static. It does not. The wave operator is
linear, so radiative deficits superpose exactly — two independent modes
and their sum all solving to zero. **The clause holds wherever the
register counts and fails only where it circulates.** Motion does not
break it; rotation does. That is the sum face and the difference face
read off the field equations rather than asserted, and it is the sharper
statement, because "dynamic" is the easy guess and is wrong.

What remains outside is therefore narrower than motion and radiation.
Every class reducing to two Killing vectors is exact. What is not covered
has fewer — the binary with no symmetry at all, which is precisely where the quadrupole coefficient is located. The outstanding sector's name is **the
asymmetric one**. Pinned in `verify/test_the_radiative_class.py`.

### 21.7 · The quadrupole coefficient

**The quadrupole coefficient is derived rather than fixed by comparison.**
No factor in it is read off a measurement; every factor is a count.

The **five** is a dimension — symmetric three-by-three tensors number
six, and removing the trace leaves five, which is the quadrupole's own
component count. The **two** is a rank — the transverse-traceless
projector is idempotent with trace exactly two, the two polarizations a
wave can carry and no more. The two join without an integral. The angular average of that projector,
restricted to the five-dimensional space, must be a multiple of the identity
there, because the space is irreducible. The multiple is forced to be **rank
over dimension, two fifths**. The integral is not computed; it is counted. The flux formula's
own half turns it into the familiar fifth.

The **thirty-two** is the octave. The quadrupole is even under
reflection, so its lowest harmonic is the second — **a binary radiates
exactly one octave above its orbit**, with nothing to choose. Three time derivatives of a second-harmonic motion, squared and summed, give
2⁵ = 32 exactly, and constant in time. Two independent checks confirm it: the
closed form, and a transformed Keplerian orbit, where the fundamental comes
out at machine zero while the octave lands on 32.0000.

That last is a prohibition rather than a description. For a circular
orbit there is **no gravitational radiation at the orbital frequency
itself** — the octave is the floor, and eccentricity opens the
fundamental only at order e², measured at a ratio of 0.151 e² across
three eccentricities. Assembled, the coefficient reproduces the double
pulsar's orbital decay to four parts in ten thousand, that residue being
the rounding of the masses rather than the formula's. So the coefficient
is a dimension divided by a rank, times the octave — and the octave is
the interval this whole account is built on, arriving unbidden in the
luminosity of a merging binary. Pinned in
`verify/test_the_quadrupole_coefficient.py`.

**That ratio has a family.** If an average over a group acts on an
irreducible space it must be a multiple of the identity there, so the
multiple is forced to be rank over dimension — two counts divided, no
integral performed. Symmetric traceless rank-L tensors in three
dimensions have dimension 2L+1, verified by explicit rank through L = 6,
and a wave carries two polarizations whatever L. So every multipole's
radiation carries **2/(2L+1)**: two thirds, two fifths, **two sevenths**,
two ninths. The quadrupole's is one member, and the octupole's
denominator is the reptend's own.

Two more sit in this account already. The isotropic average of a
rank-one projector is one third — the plainest member. The tetrahedral tight frame sums to four thirds of the identity: four vectors
over three dimensions, which is the perfect fourth. Its companion fact, the
pairwise product of exactly −1/3, is the tetrahedral bond angle carried
elsewhere in this account. Two candidates were tested and rejected. Contact-per-child's three halves is a
maximum of a ratio rather than an average on an irreducible space. Koide's two
thirds is a constraint rather than an average, since an isotropic vector gives
one third and a ratio of one. Neither is recorded as a Schur
ratio.

**The thirty-two identified.** On the root-24 scale, 32 = 2⁵ is the only pure power of two in the octave, as
27 = 3³ is the only pure power of three. A coefficient that is a pure two-
power can therefore seat nowhere but the subdominant. The quadrupole's
numerator lands there because of what it is, rather than by resemblance. The prediction that
followed — that the octupole should then carry three-powers and seat at
Re — is **false**: its contracted fourth derivative is 8202/5, whose
numerator carries the prime 1367, foreign to this account.

The reason is better than the prediction, and it is a double uniqueness.
The quadrupole is **the only monochromatic multipole among those
conservation permits to radiate**: its moment is
quadratic, so the motion is a constant plus the octave and the constant
vanishes under differentiation, leaving one line. The restriction is not
decoration — the dipole is monochromatic too, carrying a single line at
the orbital frequency, and it is excluded not by its spectrum but by the
momentum conservation that shuts its channel. Above the quadrupole the
octupole carries
the first and third harmonics together and the sixteen-pole the second
and fourth. And the quadrupole is **the only multipole whose luminosity
coefficient is exactly its own Schur ratio**, with factorial remainder
one, where the octupole's remainder is 27 and the next 1008. The
coefficient is clean at both ends for reasons that hold at no other
multipole: a pure octave above, pure Schur below. Those factorial
remainders factor over small primes because small factorials do, and are
not counted here as anything else. Pinned in
`verify/test_the_schur_sweep.py`.

### 21.8 · The dimension of space

**Pressing on the tetrahedral fourth.** It is not a resemblance. The
regular simplex in d dimensions has d+1 unit vectors, and they are the
**minimal frame that is both isotropic and balanced** — the fewest
directions that spread evenly *and* sum to zero, so that no net direction
survives. An orthonormal basis is isotropic with d vectors but does not
balance; the one further direction that balances it changes the frame
constant from one to **(d+1)/d**.

That constant is an interval. Tabulated against dimension:

```
       d  =   1      2      3      4      5
 (d+1)/d  =  2/1    3/2    4/3    5/4    6/5
```

These are the consecutive-partial ratios of the harmonic series, in order,
so **dimension indexes the series**. In our own dimension the constant is
4/3, the fourth, **Fa**, and two further quantities follow at d = 3:

```
 pairwise cosine  =  −1/d  =  −1/3     the tetrahedral bond angle

        24 × 4/3  =  32               the seat named in §6
```

**This identifies the carrier's denominator.** Section 6 establishes Fa as
the carrier by the residue table: of the eight stations, Fa alone is short
by exactly one unit. Its ratio to the root is 4/3, and the three in that
denominator is the dimension of space, since as a frame constant the ratio
reads (d+1)/d at d = 3. The carrier's identity therefore witnesses the
dimension and cannot be relocated without changing it: in two dimensions
the carrier would be the fifth, in four the major third.

**Three is also the only dimension where that frame meets the quadrupole.**
The angle at which second-order anisotropy vanishes is the magic angle,
where the squared cosine is one third; the simplex angle is arccos(−1/d).
Requiring the second to be exactly twice the first gives

```
2cos²θ − 1  =  −1/d        with     cos²θ = 1/3

        2(1/3) − 1  =  −1/3        so      d = 3
```

**and no other dimension satisfies it.** So here, and nowhere else, the
minimal balanced frame's own angle
is precisely double the angle where the quadrupole's anisotropy vanishes:
Fa's frame and the quadrupole's zero are one object in three dimensions
and separate in every other. That is the second time the quadrupole and
Fa have arrived together — the first being the coefficient's numerator —
and this time a dimension comes attached.

Read through the same family the doubling window carries the three primary consonances at d = 2, 3 and 4, with the dimension we occupy
carrying the fourth. Two things are declined. At d = 7 the constant is 8/7, which is also the packing cell's ratio. There is
no route from a seven-dimensional simplex to a length in three. It is recorded
as a coincidence of the number, so that it is not counted as more. And the musical naming of (d+1)/d is this account's
own convention on root 24: the theorem is the frame constant, and the names
are the reading. Pinned in
`verify/test_the_simplex_interval.py`.

**The decline above was half wrong, in the informative half.** The
seven-dimensional constant's resemblance to the packing cell is indeed a
coincidence — no route runs from a seven-dimensional simplex to a length
in three. But the **8** in that ratio is not a coincidence anywhere, and
following it closes a question this account had left standing: why three
dimensions.

Every seventh is a rotation of one six-digit block, whatever the
numerator — the closure the carrier section rests on. Doubling has order
three modulo seven, so those six rotations fall into two triads and one
cycle of the reptend is three doublings. Now put that beside refinement.
The register divides a cell into 2^d children, and

```
2^d ≡ 1  (mod 7)    exactly when    3 divides d
```

so the smallest dimension whose refinement returns the sevenths wheel to its own rotation is **three**. It holds at every depth and not merely the first. In three dimensions 2^(3k) ≡
1 for every k, so refining is invisible to the sevenths wheel however deep it goes.
One, two and four dimensions return only at every third level. Since a length in this register is a
count of cells, that is the same sentence twice — counting deeper costs the sevenths wheel nothing, and only here.

**Crossed with the doubling window, this selects the dimension.**
Contact per child is maximal exactly at d = 2, 3, 4, and that window came
from contact numbers and child counts with no seven anywhere in it, so
the two conditions are independent. Of the window's three dimensions only three closes the sevenths wheel. Two independent criteria, one survivor.

The cell's own ratio follows: 8/7 was carried as a declared number, and
its parts now have names — the three-dimensional refinement count over the sevenths wheel it returns. What that does **not** touch is the femtometre. A
ratio is explained; a unit is not, and the dimensional boundary stands
exactly where it stood. Nor is the selection unconditional: the
arithmetic is forced, but the requirement that refinement leave the wheel
invariant is this register's principle rather than a theorem, and the
selection of three dimensions is forced only given it. Pinned in
`verify/test_the_wheel_under_refinement.py`.

### 21.9 · Relation to curvature-squared gravity

**What this is not: curvature-squared gravity.** The shape of the
construction invites the question, so it is answered here. Quadratic
gravity adds curvature-squared terms to the action and thereby acquires
three things at once: **fourth-order** field equations, a massive
spin-two **ghost** of negative norm, and **Yukawa** corrections to the
Newtonian potential carrying a free mass scale. This account has the
Ricci tensor vanishing identically instead — sixteen components of
sixteen, in three classes — which is the second-order Einstein vacuum
equation. No fourth derivatives, no ghost, no new mass.

The solution sets nest, which is why the question is natural and why it is not
decisive. Ricci-flatness annihilates the scalar curvature, hence every
curvature-squared term and its variation, and Einstein metrics are Bach-flat.
Every vacuum solution of general relativity therefore also solves quadratic
gravity, Schwarzschild included. The converse fails. Einstein
sits inside the enclosing theory, and this account sits at Einstein.

The quadratics that *are* present are Einstein's own. The Ricci tensor is already quadratic in first derivatives of the metric, and
this account's quadrature is exactly that structure: quadratic in the
deficit's gradients, entering as an integral rather than as a term added to a
Lagrangian. That is what makes exactness available in place of corrections. The quadratic structure also enters from the register's own side. Energy
quadratic in rate is the Dirichlet form derived from per-tick increments
(§16, §20). The square the quadrature carries is therefore derived twice —
once by the register's counting and once as the Ricci tensor's own
structure — and the two agree. The harmonic half of the description is
simply accurate:
the deficit is flat-harmonic, and the radiative sector replaces Laplace
by the wave operator with nothing else changing.

The two are separable by measurement rather than by preference. Both
predict a short-range departure from the inverse square, and they predict
different ones — an exponential with a free mass against **a first power
whose coefficient is derived**, ln(b)/(b−1) and so ln 2 on the binary
layer. At ten cells of separation the power law already stands four
orders above the Yukawa, and at a hundred, forty orders; any short-range
excess observed at large separation is the power law and cannot be the
other. Pinned in `verify/test_not_quadratic_gravity.py`.

**The outstanding sector's boundary was drawn in the wrong place.** It had
been recorded as every case with fewer than two Killing vectors. Tested
directly, one exact class remains with a single Killing vector:
plane-fronted waves with parallel rays, whose one symmetry direction is a
covariantly constant null direction. The construction covers this class
with less machinery than any other.

They are also born in this account's own chart: the determinant is
**exactly −1** with no transformation performed, so areas count cells
natively here, alone among the four classes. Computing the curvature with
the profile arbitrary, **exactly one component is ever nonzero**, and it
is the profile's transverse Laplacian. Imposing only that the profile is
harmonic across the wavefront — the composite clause, and nothing else —
annihilates all sixteen. No rate word, no quadrature, no second
potential. **Strip the construction to the clause alone and what remains
is still a complete exact vacuum solution: the clause by itself is a
theory of gravitational radiation.** And being linear it is exact at
every order, which is why parallel plane waves pass through one another
unchanged.

**The real boundary shows when it breaks.** Two waves that do *not* share
the null direction do not superpose: the naive sum carries a curvature of
order unity and leaves this chart as well, its determinant no longer
minus one. That is the collision problem, and it makes a singularity. So
the composite clause holds under **two** conditions rather than one — the
sources must share a symmetry direction, *and* the deficit's own equation
must be linear. Rotation breaks the second; collision breaks the first.

That closes the sector as a statement about domain rather than as a gap.
Each exact class has a symmetry direction, and the deficit is the metric
function that symmetry makes available — a count taken along a direction
in which nothing changes. Where no direction is free of carry there is no count to take, and the deficit is not defined as a field; it survives only on the sources themselves, whose rest clocks of §7.1 carry it. The fully asymmetric case
is therefore the edge of what this construction has an object for, not a
computation left undone; what remains available there is the expansion, where this account already sits at every first post-Newtonian parameter exactly. Pinned in `verify/test_the_null_class.py`.

**One refinement narrows the edge: the conservative binary has a count
direction.** The circular two-body system, radiation set aside, is
stationary in the co-rotating sense: it admits the helical Killing vector
ξ = ∂t + Ω ∂φ, and the bodies' worldlines are integral curves of ξ. The
register's rule therefore applies there. The deficit at each body is the
norm of ξ at its position — the body's clock rate, which is §7.1's
rest-clock deficit and is the redshift invariant of the two-body
literature. The identification carries a law. If the clock rates are the
deficits, they must be the masses' conjugates in the conservative
dynamics: δM − Ω δJ = z₁δm₁ + z₂δm₂, the first law of binary mechanics.
Verified exactly at Newtonian and first post-Newtonian order, for general
masses, with each body riding only the other's deficit. At first order
the law holds with the point-mass metric sourced by the conserved masses
and selects it, the centre-of-mass correction dropping out. In the
test-mass limit it is exact to all orders: on a circular geodesic the particle's energy and angular
momentum per unit mass obey E − ΩL = √(1 − 3M/r), and the right side is
the clock rate itself. The law fails if the kinetic dilation is
dropped, if the companion's deficit is halved, or if each body is charged
the total: the first law selects it. The apportionment of §21.6 is thereby
confirmed at the two-body level by an independent identity. What still
lacks a Killing direction is the dissipative sector alone, since exact helical symmetry is incompatible with asymptotic flatness and outgoing radiation, as Gibbons and Stewart showed; and the dissipative sector is the flux §21.7 derives. The reduction of the field along ξ is not one of the linear classes and remains the open computation; its result, by §21.6, is the received dynamics. Pinned in `verify/test_the_helical_sector.py`
and `verify/test_the_first_law_1pn.py`.

### 21.10 · The dimensional crossing

**The dimensional crossing.** With the cell's number now carrying names,
the boundary can be crossed in one stated move. **Declared: the cell is
8/7 fm**, its numerator the three-dimensional refinement count and its denominator the sevenths wheel that count returns. The **femtometre** is the
borrow, and the only one. From it a nucleon occupying a sphere of that radius fixes the saturation
density at 3·7³/(2¹¹π) = 0.1599321 per cubic femtometre, six tenths of a
standard deviation below chiral effective theory's 0.164 ± 0.007. With the
dimensionless depth of 10⁴² and the frozen comoving horizon's closed form, the
expansion rate comes out at 70.0540 kilometres per second per megaparsec. That
value sits five standard deviations above the Planck determination and nearly
three below the local ladder, inside the present discordance and decided by
its resolution. One borrowed unit,
two dimensionless structures, two measurable magnitudes: the boundary is
not bent anywhere, it is crossed at exactly one declared place. Pinned in
`verify/test_the_crossing_statement.py`.

### 21.11 · What the account permits by way of repulsion

**What the account permits by way of repulsion, in four parts.**
*First, a prohibition.* For every full-reptend prime the reptend times
the prime is one short of the power of ten — never zero, never over — so
the force is one-signed with no free choice, and a count does not go negative. There is nothing in the arithmetic to build a repulsive
counterpart from. *Second, a term that already is repulsive.* The cosmological term is positive, with an equation of state of exactly −1,
and it accelerates the expansion. Being a constant of integration, it can be
neither sourced, shielded, screened nor switched. That is what makes it
useless as a device. *Third, a reduction that cannot reverse.*
Circulation makes the well shallower and never deeper, one-signed and
bounded. *Fourth, the one place the sign genuinely inverts:* inside the
ergosurface the time word goes negative, the direction that was free of
carry having stopped being a direction of time. No static observer exists
there and energy can be extracted, at the cost of angular momentum and
bounded by the irreducible mass — some twenty-nine per cent at the
extremal limit. So the account's answer is not shielding and not negative
mass but **rotation carried far enough to change the symmetry direction's
character**, and what it yields is a battery rather than a drive. Pinned
in `verify/test_repulsion.py`.

**The coordinate rule has one further consequence, which is what this
account can honestly say about quantizing gravity.** Two routes laid down
years and hours apart arrive at the same object.

The first was banked at the beginning: **time is the count of carries** —
succession as the tally of the construction's own propagating events, not
a container it sits in. A clock is a cycle with a carry, and linear time
is the stack of accumulated carries. Time is a **count**.

The second is this section's. The coordinate rule is the unimodular
condition, and unimodular dynamics carries a standard consequence, cited
rather than claimed: the cosmological term is canonically conjugate to
the **four-volume**, and that four-volume serves as a physical clock. The
four-volume is a **count of cells**.

Those are the same object, reached independently — one from long
division, one from a determinant. And the consequence is the one that
matters. Ordinary canonical gravity gives H|ψ⟩ = 0, in which nothing
evolves; in unimodular form the same equation becomes a Schrödinger
equation in the four-volume. **This account never had the problem of
time, because it never had a frozen formalism** — it had a count from the
first page, and that count turns out to be the clock the formalism was
missing.

Four canonical obstructions therefore meet one structure.
Non-renormalisability does not arise, there being no continuum mode sum
to diverge. The problem of time does not arise, for the reason above. The
singularity is excluded by counting, resolving zero separation being a
supertask. And the cosmological constant problem is a tense error — summing as realized what is only held — with the term itself a constant of integration.

### 21.12 · The quantization apparatus: what is carried, the horizon count, and what is open

**The apparatus, item by item.** The items a continuum programme
would list — graviton amplitudes, an inner product for the state, canonical
quantization carried through — divide on this account rather than standing
as one debt. Two are already present in register form. The ring's character
map is the inner product, its normalization fixed by count preservation,
and the Weyl pair's failure to commute by one root of unity is the
commutation structure, exact rather than imposed (§22). One is excluded
with its falsifier stated: a single-shot graviton amplitude is a port
reading of the phase half, and §23's twelfth condition says what ends that
position. The remaining two, the composition of many rings into the field sector's state space and the horizon count's logarithmic coefficient, are built in §22 and below: the first as a product of accounts, the second as the discriminator. Pinned in `verify/test_the_clock_convergence.py`.

**The horizon's own count, and what building the apparatus actually
requires.** The entropy is the number every approach to quantizing
gravity is judged on, so it is worth being exact about where this account
stands on it.

The familiar quarter is 2π over 8π: the Euclidean periodicity divided by the
matter coupling. Both factors are already present here. The field equations
have been verified in four classes above, and the periodicity is a closure
condition on an angle.

Ask which cell makes the entropy one unit per cell and the answer is a
cell of side exactly two Planck lengths, at which the quarter disappears
and the doubling is this account's own first generator. **That reading is
clean and it is not available.** One nat per cell requires e states per
cell, and a discrete register cannot have e states. It is withdrawn here
rather than kept.

What discreteness does allow is the count with an integer alphabet. N cells of
k states give N ln k, so matching the received entropy requires a cell of area
4 ln k. On the binary layer this account already runs on, that is 4 ln 2
Planck areas, a side of 2√(ln 2). The logarithm is
not imported; it is the same ln(b)/(b−1) derived elsewhere for the
short-range correction, appearing here for the same reason.

**The logarithm turns out not to be required at all.** Boltzmann's
entropy carries a natural logarithm, and base e reaches it through
Stirling, the Gaussian and dx/x — every one of them a continuum
construction. The nat is the continuum's unit of entropy; the bit is the
discrete one. So ln 2 is not a coefficient to derive but the conversion
between them, and it is the same ln 2 that Landauer's bound carries for
the same reason — a conversion established in the companion volume on units.

That leaves the four, and the four traces further: it is 8π over 2π,
where the 2π is an angle closing and the 8π is the **matter coupling's
normalization**. The vacuum equations verified above have no matter in
them, so none of that work ever saw it. **What is actually required, then, is
the 8π** — not the entropy, not the logarithm, not even the four as such,
but one dimensionless normalization.

**That one is not free either.** Take a weak static field: the
time-time Ricci component to first order is exactly the potential's
Laplacian. Write the field equation in the form the Bianchi identity
forces, R_ab = κ(T_ab − ½g_ab T), and apply it to dust at rest, whose
source is half its density since T_00 − ½g_00T = ρ − ρ/2. Matching the
Newtonian limit gives **κ = 8πG**, symbolically and with nothing chosen.
Its two factors are the **solid angle of a sphere in three dimensions** and a
factor of two. The solid angle arrives with Gauss's law, and Gauss's law is
the inverse square this account derives by two routes, in the dimension it
selects. The two is the trace reversal's own half inverted. The trace-reversed
form is forced, because the Einstein tensor is the unique divergence-free
symmetric two-tensor in second derivatives of the metric.

**The normalization is not a separate thing to derive.** A scaling law
fixes no constant when it is a bare power law; this one is not. A
conserved count spreads over the sphere it has reached, so in d
dimensions the intensity is P/(Ω_d r^(d−1)) and the amplitude falls as
r^(−(d−1)/2). Inverse-square intensity therefore occurs at **three
dimensions and nowhere else** — and the very statement that fixes the
exponent fixes the constant, since Ω₃ = 4π *is the measure of the sphere
whose growth produced the exponent*. They are one fact read twice. This
account's own first route already is that statement: reading the deficit
as an inverse-first amplitude is the three-dimensional flux law, and it
carries the 4π with it.

So the horizon chain contains **no unaccounted dimensionless factor
anywhere along it** — a conserved count, three dimensions, the sphere's
measure, a Bianchi-forced trace reversal, and the nat-to-bit conversion,
each supplied.

**What that does not close, and it widens rather than settles.** The
conversion from a count-density to an acceleration is dimensionful and is
therefore a declared borrow. But a dimensionful anchor is now named in
three places — the electroweak vev, the packing cell, and the Planck
length this chain rides on — and the ratios among them are not derived.
The borrow-accounting entry gains a third line.

**Those missing ratios have names.** Electroweak over Planck is
v/M_Planck, about two parts in ten million million million — **the
hierarchy problem**. Nuclear over electroweak is about 1426 — the strong
scale against the weak one, which is **dimensional transmutation**.
One of the three ratios is already carried in register form. Section 22
records the coupling as an exact square, so m_e/M_Planck = √10 · 2⁻⁷⁶: the
electron's Planck hierarchy is §13's wheel read at amplitude, and the
measured ratio matches that expression to the coupling's own precision.
What remains is sharper than a general absence. The electroweak-to-electron
ratio is the Yukawa spectrum, and this account holds the shape of the
charged-lepton ladder without its position. The shape is two ratios, both
parameter-free contacts: the muon-to-electron ratio 206.768283, and the
Koide relation, which given the electron and muon masses places the tau at
1776.97 MeV against a measured 1776.86 ± 0.12 MeV. The position is one
number, v/m_e = 481839.84 ± 0.12, and it is no station of the register:
the nearest banked station lies fifteen standard deviations away, and no
wheel form, radiative form or power of α reaches it. Since m_e/M_Planck is
carried exactly and m_p/m_e is seated, both v/M_Planck and the
nucleon-to-electroweak ratio m_p/v reduce to this same unknown, so the
three open positions are one number and one derivation would close all
three. The standard route to the Yukawa spectrum, the Froggatt–Nielsen
expansion in powers of the Cabibbo parameter with order-one coefficients,
parametrizes the spectrum and does not derive it. One live constraint and
one calibrated negative stand with the position. The theory's Higgs self-coupling seat, λ = 2⁹/(3⁴·7²) with the coupling
read at tree level from m_H² = 2λv², was recorded on 2026-07-03, before
comparison. It makes √(2λ) the exact rational 32/63, so on the seats
v = (63/32)·m_H and the position is equivalently the Higgs-to-electron
ratio. The seat therefore predicts m_H = 125.0640 ± 0.0001 GeV against the measured 125.20 ± 0.11 GeV, the individual experiments spanning 125.11 to 125.38. The coming generation of Higgs-mass measurements decides it. The negative: a declared search over products of the theory's named constants, twenty million trails through depth six, finds nothing within five parts per million of the position. The calibrated expectation of accidental hits inside its bar was two in a hundred, so the search had discovery power and returned empty. The position is not a
hidden product of the constants. Pinned in
`verify/test_the_lambda_higgs_corollary.py`. In the rest-clock reading
of §7.1 the number v/m_e is the count of electron ticks per electroweak
tick. The step this account would need is an operation of the register
that places the electroweak tick rate against the electron's, and none is
banked. The boundary sits at the Yukawa spectrum, and it is recorded as an
open account rather than as a wall. Pinned in
`verify/test_the_yukawa_leg.py`.

One candidate was tested here and rejected on two counts. The
nuclear-to-Planck ratio is 7.0710 × 10¹⁹ and 5√2 is 7.07107, a miss of
seven parts per million — inside the eleven-ppm floor that G's own
uncertainty imposes. But sweeping ten thousand words and counting only
those in the same decade, the chance of *some* word landing inside the
window is about one in a hundred, and that makes no allowance for the free
power of ten. Worse, the reading contradicts this account's own value of
G: on the coupling wheel's figure the same comparison misses by forty-six ppm
rather than seven. Both cannot stand, and the coupling wheel is the older claim.

The horizon chain is internally complete; the cross-chain accounting is not.
Pinned in `verify/test_the_eight_pi.py`,
`verify/test_the_normalisation.py` and `verify/test_the_three_rulers.py`.

**The logarithmic coefficient, derived given the census.** The correction
below the leading term follows from one counting theorem and one named
identification. The theorem: N binary cells subject to m independent
additive constraints number 2^N · N^(−m/2) up to a constant, so each
conserved quantity the microstates must realize contributes −(1/2) ln N.
The identification, of the same class as §13's pairing: the horizon
record's macrostate fixes exactly the record's two faces — the count, and
the mirror-odd difference, zero for the static hole. Two faces, m = 2.

For this census the count is exact rather than asymptotic. The figure's reflection splits the cells into two antipodal hemispheres, and a fixed
sum with zero difference is precisely the balance of each hemisphere
separately:

```
   #states  =  C(N/2, N/4)²

   S  =  N ln 2 − ln N + ln(4/π)

      =  A/4  −  ln A  +  ln(16 ln 2 / π)         N  =  A / (4 ln 2)
```

**The coefficient is −1: one half from each face.** A nonzero
difference-face value — a rotating hole — shifts the two binomials apart.
The entropy falls quadratically in the spin while the coefficient stays at
−1: rotation costs entropy at fixed area, and the coefficient does not
move. The scope is exact: this is the constraint piece of the microstate
count, the analogue of the quantum-geometry computations, and infrared
one-loop matter contributions are additive and separate.

**The discriminator is now a number.** Loop quantum gravity's U(1)
counting gives −1/2 and its SU(2) counting −3/2; Cardy-based countings
typically give −3/2. The register gives −1, half a unit from each — the
census's own unit, since each conserved face added or removed moves the
coefficient by one half. The comparison is to these microstate-counting
results specifically. The coefficient of the Euclidean effective action
depends on the field content near the horizon and is therefore not a single
number. The claim is not that −1 separates the register from every
computation, but that it is the value the two-face census forces. §23's seventeenth
condition states what removes it. Pinned in
`verify/test_the_log_coefficient.py` beside `verify/test_the_horizon_cell.py`.

**Open, named.** Two items. A register-native derivation of the two-body field beyond first post-Newtonian order. The dynamics there are the received theory's own, confirmed through third order by the first law and the self-force series, so nothing physical is at stake and the derivation from counting is owed as apparatus. The dissipative sector alone lacks a Killing direction, with §21.7 carrying its flux. The position of the lepton ladder, v/m_e, stated above.

## 22 · Quantization reversed: integer sources, a finite spectrum, and the phase-blind readout

The impasse of quantum gravity assumes there is a continuum to quantize. On discrete terms the situation reverses. The sourcing is integer, the k of
§5. The oscillation spectrum is finite, four frequencies by §3. The
interaction is an event with a one-bit ledger, by §9. And the coupling is a
rational number on a wheel of prime period, by §13. There is nothing continuous left to quantize;
what is left is the opposite question — why measurement reads a continuum — and
the theory answers it elsewhere as the envelope. One structural note carries
across: αG is an exact square, (√10 · 2⁻⁷⁶)², the observable rational with an
amplitude that is never seated — the Born rule's shape, and the double copy's, proposed as one fact seen
three ways.

**Why the field has no quantum signature, and what that forbids.** The companion account of the single-particle wave proves a fact about reading
rather than about apparatus. A state is 2n integers: n amplitudes and n phase-
exponents. The Born port returns the n squared amplitudes and nothing that
depends on the phases. Exactly half the state survives the
reading, and the half that does not is not lost by the state but simply not
carried by the reading.

Set the potential of §7 in that discarded half. The closure defect is one-signed and
prior to any rider; it is the unseated station, the one place the register
cannot close; and it is therefore the first content a truncation drops. The
consequence is not a shrug about weakness but a pair of statements with
opposite signs:

- gravity **cannot** appear in a single Born reading, at any precision,
  because that reading is a function of the amplitudes alone;
- gravity **must** appear wherever relative phase survives, which is
  interference.

The second half is what makes this a claim rather than an excuse, and it has
been confirmed for fifty years. The gravitationally induced phase shift is
measured in neutron interferometry from Colella, Overhauser and Werner onward,
and in atom interferometry since. Gravity shows up
exactly where phase survives. Had it failed to appear there, this
paragraph would be dead. The first half is consistent with the other side
of the record — no single graviton has been detected, and Dyson's argument
that none can be is, on this reading, a statement about the port rather
than about the coupling. What would end it is a graviton registered by a
phase-blind single-shot detector.

One quantity is worth stating because it inverts the usual picture. The
discarded fraction is exactly one half, not some small remainder — so on
this reading gravity's information content **equals** what is read rather
than falling short of it. The field is not faint. It is on the other side
of the port, and whatever the hierarchy is about it is not about how much
there is.

This is also where the account meets Penrose, and meets him with something
he does not have. He argues from the geometry that superposed mass
distributions superpose spacetimes unstably, so that gravitation and
reduction are intimate. Here the connection is located. The union of two records can occur only where
the register's collapse is many-to-one, which is the carry boundary and
nowhere else, by §9. The carry is also the tick, and the place the deficit is discharged. Collapse, gravitation and time are not
three neighbours. **They are one boundary described three ways**, and the
counting says *where* — which the geometry does not.

**The register's own state carries no uncertainty at all.** The
temptation here is to reach for the familiar relation and claim it, so
the theory's earlier work is what governs. On the ring the state is
**2n integers** — for each mode an amplitude and a phase *exponent* —
and nothing in it is continuous. Know the state and you know both faces:
there is no trade-off in the object. Complementarity is nevertheless already present and already exact — not as a
bound on widths, but as the Weyl residue, the shift and the clock failing to
commute by precisely one root of unity. Conjugate structure is a property of
the ring rather than of continuity. What is lossy is the *port*: the Born read returns
squared amplitudes and discards every phase exponent, exactly half the
state's integers. **The state never loses its phase; the readout does.**

That places the famous uncertainty product where it belongs. Send the ring to the circle and the ring's transform to the Fourier transform,
and the minimum product appears in its usual form. That is the seated-limit
face: a theorem about a phase-blind readout inside a continuous formalism,
rather than a theorem about the register. Claiming it as
the register's own would import precisely the continuum this theory
demotes, by summing harmonics into a smooth wave and then calling the
lost phase a law of nature. The register's account is the stronger one:
the relation is an artifact of the port, and the port's blindness is
measured — exactly half the integers.

**The same discipline governs the correlations, and the coupled rings
supply what four earlier attempts could not.** Two statements are the
register's before any construction. Records with disjoint support commute, by §17. Records that never shared an
account are therefore locally describable, and a sign-level read of their
common phase has a Clauser–Horne–Shimony–Holt maximum of exactly two. The
register is classical precisely where the gauge theorem requires, and a
violation there would refute it. And a unioned pair is not two separable systems: it
shares one account, so factorizability fails, while the marginals stay
untouched and nothing signals.

The correlation itself then follows from banked objects and one new
input. The ring carries three things. Its **Weyl pair** — shift and clock — fails to
commute by one root of unity, which is this account's complementarity already
established. Its native character map has a normalization of one over the root
of the ring's size, because the transform must preserve the count. And its
Born read is the squared amplitudes. The new input is the
union itself: a union makes both records carry the *same* count, so a
unioned pair's joint state is supported on the **diagonal**. That is §9's
union, not an assumption about correlations.

On the two-ring the consequences are exact. The shift and the clock
square to the identity, so they are two-outcome readings with no external
measurement postulate. Their character-map mixture is **the transform
itself**, so the settings that saturate the bound are the register's own map
rather than chosen angles. Computing from the Born read alone — projectors,
squared amplitudes and signed weights, with no expectation-value formalism —
the unioned pair returns exactly **2√2**.

**The value is an output, tested the way the earlier claim was not.**
Pairs that never unioned stay at or below the root of two under the same
observables, with no product state exceeding two across twenty thousand
random draws — the union does the work. Tilting the state off the
diagonal drops the value monotonically. Perturbing the observable mixture away from the character map's normalization
drops it on both sides, so the maximum sits exactly at one over the root of
the ring's size. The root of two here is the transform's own norm rather than
a setting angle. What
this forbids: records that never unioned cannot exceed two, and the
construction admits no super-quantum correlation, the unit norm of the
character map capping it. Three things are named rather than hidden, and a
stress pass fixed the wording of each. Both settings on the second ring
are register-native — the second is the character map conjugated by the
clock — so no angle was chosen by hand. A union leaving both records at one definite count violates nothing at all.
The superposition is the polar state's own amplitude over modes. Uniform amplitude over the diagonal is the maximal case, a named condition rather than a derived one. And two identifications stand: that two rings compose as a
product, and that a setting is a choice of which operation to read in,
which the Weyl relation already pairs. A scan over all four settings
confirms 2√2 is this construction's ceiling, attained by the register's
own map and never exceeded. **What it does not do is forbid anything standard quantum mechanics permits.** Never-unioned pairs sit at two, and there is no super-quantum box; both are
shared. This is therefore a reconstruction from register objects rather than a
new prediction, and is offered as one. Pinned in
`verify/test_the_correlation_bound.py` and
`verify/test_the_complementary_pair.py`.

**The field sector: many rings compose as a product of accounts.** The
single ring and the unioned pair are the two cases above; the field sector
is the general case, and it is built here from the same three objects and
the one identification already on record. Call an account the set of rings
that have unioned, so that they carry one count. A field sector is a finite
family of rings together with its partition into accounts, and its state
space is the product over accounts of each account's diagonal. Six
statements follow, each checked numerically in
`verify/test_the_field_sector.py`.

The Weyl structure composes. Shift and clock operators of distinct rings
commute, and within a ring they fail to commute by that ring's root of
unity. A composite shift against a composite clock fails by the product of
the rings' roots, each raised to the powers taken. The set of all such
phases is exactly the roots of unity of one order: one root of unity per
sector, of order the least common multiple of the ring sizes. The character
map composes as the product of the ring maps; it is unitary, and every
entry has modulus one over the root of the sector's dimension. Count
preservation therefore fixes the normalization of the composite with no
freedom left per ring. The Born read of the composite returns the squared
amplitudes over the product basis. That is exactly half of the state's
integers, for every composition and every partition into accounts, and
every phase exponent is discarded, as on one ring.

Union collapses dimension. An account of m rings of size n has the
dimension of one ring, not of m: the diagonal of the m-fold product has n
states where the product has n to the m. The union is many-to-one by
exactly m minus one times the logarithm of n, and unioned records cannot
disagree, since the joint Born read in the clock basis carries no weight
off the diagonal. The horizon census of §21.12 is a case of the
composition: N binary rings that have not unioned with one another, under
the count face and the mirror-odd difference face, number C(N/2, N/4)².
Both faces are diagonal in the clock basis, so they commute and the census
is well defined.

The correlation bound composes, and it obeys monogamy. A unioned pair reads
2√2 with the register's own settings, and the value is unchanged when the
pair is embedded in a larger sector beside a ring it never unioned with. A
pair that unioned as part of a triple account reads at most two under every
setting, register-native or not, while the triple itself carries the
correlation: Mermin's combination on the triple's diagonal returns four,
its maximum. Never-unioned pairs stay at two.

What the composition forbids: a super-quantum correlation anywhere in a
sector, a pairwise violation inside a triple account, and a count
disagreement between unioned records. For the constraint piece of any
horizon census it also forbids a logarithmic coefficient other than minus
one half per conserved face. As with the two-ring case, none of this
forbids anything standard quantum mechanics permits, and it is offered as a
reconstruction from register objects rather than as a prediction. What it
closes is the apparatus item of §21.12: the field sector's state space is
built, from banked objects and one identification, and the discriminator
remains the logarithmic coefficient.

In the musical analog the whole section is one sentence: just intonation is already the quantization, and temperament is the continuum convention laid over it.
 

## 23 · What would refute this paper

Stated so the paper can be wrong, with numbers where numbers exist.

1. **The sign.** One observed repulsion between positive masses ends §4, and
   the paper with it.
2. **The source law.** Any pull nonlinear in its source, or any response
   depending on the rider's composition, ends §5. The present record is the passing measurement of exactly this prediction: the
space accelerometer at parts in 10¹⁵, and ground balances at parts in 10¹³.
The congruence requires equivalence to hold exactly, at every precision. Any
confirmed violation, at any precision, would end it.
3. **The exponent.** The inverse square must hold as a ratio statement in the
   extension — ten times the extension, one hundredth the energy — by two
   independent routes (§8, §11). A different exponent ends both routes at
   once.
4. **The coupling wheel.** If the G experiments converge on the CODATA-2018 centre at their stated
precisions, 5/(2¹⁵¹ − 1) is excluded. So is it if any two independent
determinations at twenty-five parts per million or better, by distinct
methods, agree on a value off the coupling wheel's. The prediction sits 106.4 ppm below
centre, and the discordance corridor is its only shelter. Equally:
   a small-block irreducible wheel for α, αG(proton), or αG(muon) would
   destroy the exclusivity that makes the electron's wheel selective.
5. **The chain.** n₀ = 0.15993 fm⁻³ and H₀ = 70.05 km s⁻¹ Mpc⁻¹ are standing
   targets. Convergent metrology that leaves either — n₀ beyond its stated
   bars, or the Hubble ladders agreeing on either end of the present corridor —
   ends §14.
6. **The fine structure of the fall.** The envelope read (§12) carries one
   profile-independent signature: any log-periodic residual in the force law
   must repeat **once per octave of separation**. Observation of a
   log-periodic residual at any *other* period ends Part II
   outright; a residual at one octave, at any amplitude, is its fingerprint
   and measures the register's base in the field. Deepening nulls bound the
   sharing profile's amplitude — the part's one free number — toward the
   smooth family; they do not touch the substrate, whose geometry is not the
   envelope's. The published template states the analysis: one fixed-frequency
   cosine in log r, two fitted parameters, five archived datasets.
7. **The event ledger.** The union's ledger (§9) forbids count creation
   or deletion at commitment. One verified interaction whose committed count differs from the sum of its
parts', less the radiated settlement's, ends Part II. That is conservation
with the settlement on the books, which is what the measured mass of a bound
state already is.
8. **The comb at the planets.** If the octave amplitude is nonzero, the anomalous perihelion residuals of
several planets must fit one fixed-period comb in log r, by §20. A log-
periodic planetary residual at any other period ends Part II. The multi-planet
fit is phase-proof where any single planet is not.
9. **Assembly history.** The ensemble theorem (§18) predicts that two
   systems of identical mass and different binding history gravitate
   differently — the anomaly correlates with commitment state, never with a
   conserved substance. A demonstrated identical-mass pair with identical
   dynamics across distinct assembly histories, at sensitivity to the
   log-of-spectrum excess, refutes the ensemble route; the correlation, if
   found, is one no halo model can carry.
10. **The landmark stations.** For the non-rotating case the derived rungs of §21 stand at deficits 1/3, 1/4
and 1/6, with the continuum's wall at 4/9 and the count's at 1/3. The
horizon's coefficient stands at the mirror's two. Each station carries the
comb's own tolerance, below parts in 10¹¹ at the marginalized amplitude bound.
A strong-field measurement placing a photon ring, marginally bound circle or
innermost stable orbit off these stations refutes the rate-line derivation
at the rung in question, as does a non-rotating accretion efficiency away from
1 − √(8/9) = 5.72 percent. Form and count would then have to answer for
themselves. A static body with surface deficit beyond one third refutes the count's
interior specifically. The relevant markers are compactness past 2/3, surface
redshift past √3 − 1, and a surface inside its own photon sphere. Found
between the count's wall and the continuum's, at compactness 2/3 to 8/9, it
decides the stated fork for the continuum's extra sourcing while leaving the
exterior cascade standing. Found beyond 8/9, it retires both walls. In rotation the condition binds the first-order shifts derived in §21: the
innermost stable orbit and photon orbit move with the slopes stated there, and
the dragging rate stands at 2J/r³. The second order in spin remains
outstanding, and no landmark claim is made at extremal spin. And the spatial word binds: a confirmed γ − 1 ≠ 0 at any precision, or measured spatial curvature inside a hollow shell, refutes the ruler word and the metric's completion with it.

11. **The gauge.** Order at spacelike separation is bookkeeping. Any observable found to depend
on it — signalling — refutes the commutation theorem and the register with it.
Any sidereal or velocity modulation of the octave comb's phase is a preferred-
frame signature that refutes the ledger's gauge outright. The register's
structure must appear as scale, never as frame.

12. **The port.** §22 places the potential in the half of the state the Born
   reading does not carry, and that cuts both ways. **A single-shot
   amplitude detection of a quantum gravitational effect — a graviton
   registered by a phase-blind detector — ends it.** So, equally, would the absence of gravitational phase shifts from
interferometry. That half is already decided in the claim's favour: the shift
is measured. Had it not been, this entry would have refuted the section rather
than supported it.

13. **The selections.** Every claim of uniqueness in this paper states the
   predicate and the class over which it holds. A uniqueness claim that
   turns out to require an unnamed further condition is refuted as stated,
   though not, by itself, are its neighbours. Each such claim is pinned in
   the suite by a test naming its predicate and its class, so the condition
   is checkable rather than asserted.

14. **The arithmetic.** Every exact claim re-derives in the public suite
   (§24). An arithmetic error anywhere is an error everywhere it propagates,
   and finding one is the most direct refutation available.

15. **The composition line.** The gravitational charge and the inertial
   mass are one count read twice (§§5, 7), so no composition may separate
   the two readings. A confirmed nonzero Eötvös ratio η — any material
   pair, any precision, any range — refutes the mechanism outright.
   Accounts with light scalar partners can screen or tune such a result
   away; nothing here can. Composition may shape the mass itself, and
   measurably does at the percent level in the binding ledger, without
   touching this condition. The companion note *The Eötvös Line* states
   the discriminating tests.

16. **The clock leg.** If the deficit attaches to ticks, every clock
   species must shift identically with potential. A confirmed clock-species
   dependence of the gravitational redshift — two dissimilar co-located
   clocks disagreeing as the potential varies — refutes the identification
   of §7 as directly as a composition-dependent free fall. Null redshift
      comparisons bound such dependence at parts in 10⁵ and better, and the
   space comparisons now running sharpen the bound.

17. **The logarithmic coefficient.** Given the two-face census, the horizon
   count carries S = A/4 − ln A + ln(16 ln 2/π), coefficient −1 exactly
   (§21.12). A demonstration that the horizon record's macrostate fixes
   more or fewer conserved faces than two moves the coefficient in steps
   of one half and refutes the census as stated. An agreed derivation or
   measurement of the correction at any value other than −1 refutes it
   outright, while leaving the leading term standing.

What no experiment can refute is the identity of Part IV as a matter of
taste; what it can refute is every load-bearing joint the identity stands on,
and the list above is those joints.

## 24 · Verification

Every exact statement in this paper is a re-runnable test in the theory's
suite — 2,671 tests passing at this writing. The paper's own claim map,
1,009 assertions together with this paper's source, is public at
github.com/thefirsthorstmann/g-theory-verify and re-derives the paper's
exact skeleton in under four minutes on an ordinary machine. The map from
claim to test:

| claim | section | test |
|---|---|---|
| the fixed-point pair: one place occupied, one empty, no third | §3 | `verify/test_gravity_form.py` |
| the shortfall theorem; the Midy decider chain | §4 | `verify/test_gravity_sign.py` |
| the k-rotation congruence (source + equivalence) | §5 | `verify/test_gravity_form.py` |
| the inverse square from the nines | §8 | `verify/test_gravity_form.py` |
| the held form's two names and one bit | §9 | `verify/test_the_held_form.py` |
| the union only at co-carry; addition forced; the ledger | §9 | `verify/test_the_trigger.py`, `verify/test_tick_contact.py` |
| the covariant trigger: null connection, the rate recovered, frame invariance, aberration to third order | §9 | `verify/test_the_covariant_trigger.py` |
| the period-mass map: the rate as the excess, rational mass ratios, the equivalence residual | §10 | `verify/test_the_period_mass_map.py` |
| the small-rung kernel: the census as the ceiling, its staircase as the octave comb, the laws kernel-free | §12 | `verify/test_the_small_rung_rule.py` |
| the coupled rings: shift and clock as two-outcome reads, the character map as the setting, the bound from the Born read | §22 | `verify/test_the_correlation_bound.py` |
| the field sector: rings compose as a product of accounts — one root of unity per sector of lcm order, the character map's normalization forced, the half composition-invariant, union collapsing m rings to one, the census and the bound as cases, and monogamy inside a triple account | §22 | `verify/test_the_field_sector.py` |
| the state's 2n integers carry no trade-off; the Weyl residue; the port's measured blindness | §22 | `verify/test_the_complementary_pair.py` |
| the coprimality exclusion; the shared downbeat | §9 | `verify/test_the_shared_downbeat.py`, `verify/test_the_trigger.py` |
| the cadence moves one three and one two | §9, §15 | `verify/test_tonal_function.py` |
| the contact rate gcd(p,q)/pq; bilinearity iff coprime | §10 | `verify/test_the_contact_where.py` |
| the exponent −1 from the carry weight; both routes agree | §11 | `verify/test_the_joint_derivation.py` |
| the sharing profile's derived tail; the fork's terms | §11–11 | `verify/test_what_fixes_F.py`, `verify/test_ultrametric_vs_euclidean.py` |
| no singularity; saturation; the ln 2 coefficient | §12 | `verify/test_no_attained_zero_in_gravity.py` |
| the coupling wheel, its irreducibility, the period Φ₁₅(2), the advancement chain, the exclusivity scan | §13 | `verify/test_the_wheel_count.py`, `verify/test_decimal_wheel.py` |
| the chain's three values and their comparisons | §14 | `verify/test_watch_condition.py`, `tools/watch.py` |
| the resolution to the octave; the seventh rung 7/4 with remainder 8/7 | §15 | `verify/test_curvature_ladder.py` |
| the just seats on root 24; the degree map | §15 | `verify/test_musical_arithmetic.py` |
| the translation fact; the boost ladder; composition as stacking; the comma's rapidity; the cavity arithmetic | §6, §16 | `verify/test_diatonic_relativity.py` |
| the carrier's license: the shortfall theorem, the trichotomy, Fa's uniqueness, the smooth condition | §6 | `verify/test_the_fa_license.py` |
| the c_rest factorization and the order of ten modulo 137 | §16 | `verify/test_diatonic_relativity.py` |
| the wheel's look-elsewhere null: the duplication, the family-wise p, the pre-registered thresholds | §13 | `verify/test_the_wheels_look_elsewhere.py` |
| the action quantum: not wheel-able by the Scale Theorem; action as a count of carries; the ruler count of one | §14 | `verify/test_the_action_unit.py` |
| the ledger's gauge: commutation at disjoint support, the cone as support boundary, frames as linear extensions, the two-ledgers fall | §17 | `verify/test_serial_order.py` |
| the coordinate rule as a chart, the cosmological term as a constant of integration, w = −1 exactly, and the frozen-horizon evolution withdrawn | §14 | `verify/test_the_unimodular_chart.py` |
| the ceiling theorem, the horizon acceleration, the octave fingerprint | §18 | `verify/test_the_galactic_regime.py` |
| rate additivity of composites; the log-of-spectrum excess; superposition recovered for bound matter | §18 | `verify/test_the_ensemble_route.py` |
| the vacuum term: sign, sourcing, infrared pin, the ratio, the open equation of state | §14 | `verify/test_the_vacuum_offset.py` |
| the fork's closure: envelope exact in the mean; every point of a cell its center; the residue as one parameter | §12 | `verify/test_the_fork_closed.py` |
| the ADE ladder, the doubling window, the two contact ladders, the (7,17) bridge | §19 | `verify/test_the_dimensional_account.py` |
| the doubling window characterized: contact as three times a power of two, the fifth against refinement | §19 | `verify/test_the_promotion_window.py` |
| the window as an extremum: contact per child maximal exactly there, at exactly the fifth, secure against upper bounds | §19 | `verify/test_the_contact_maximum.py` |
| the window without a maximum: the half-open interval between the second generator and the first foreign prime | §19 | `verify/test_the_contact_window_interval.py` |
| the Kepler pair, the eccentric family, the octave precession instrument | §20 | `verify/test_the_orbital_account.py` |
| the landmark ladder, the wall as the tone, the replacements, the entropy identity | §21 | `verify/test_the_strong_field_file.py` |
| ceiling-2 → horizon-2: the rate line, the derived rungs, the harmonic deficits, the supertask clause | §21 | `verify/test_ceiling_two_horizon_two.py` |
| the wall resolved: one rule inside and out, the count's wall at the photon station, the fork with the continuum | §21 | `verify/test_the_wall_derived.py` |
| the floor's two ledgers: the asymptotically null surface, the echo null, freezing as the event, the first law | §21 | `verify/test_the_floor_and_the_ledger.py` |
| the drag word: the difference face, the Lense-Thirring rate, the first-order station shifts, the truncation's scope | §21 | `verify/test_the_rotating_sector.py` |
| the quadrupole: the derived words exact in spin, the subtense from the identity, the charge slot, the Kerr bound as discriminant | §21 | `verify/test_the_quadrupole.py` |
| the clause's coefficient derived: the two faces' potential px − iqy solves the stationary equations if and only if p² + q² = 1, the unit circle that is the coefficient one; the charged solution's slot a consequence | §21 | `verify/test_the_clause_coefficient.py` |
| the tensor face located: one source exact, the gap as the coordinate, the fork sized at the pulsars | §21 | `verify/test_the_tensor_face.py` |
| the coordinate rule and its test: areas count cells, the two-body advance from superposition, the fork narrowed to apportionment | §21 | `verify/test_the_multisource_envelope.py` |
| the apportionment closed: the Nordtvedt parameter exactly zero, and every parametrized word at the received value | §21 | `verify/test_the_apportionment.py` |
| second order, the earlier bound: exact in the test-particle limit, and the double pulsar limiting any disagreement to a fifth, superseded by the comparison below | §21 | `verify/test_the_second_order.py` |
| the coordinate rule: cells keep their volume, verified on both solutions, and the cross-term identity | §21 | `verify/test_the_coordinate_rule.py` |
| the Einstein tensor computed: machinery validated, the gradient reading refuted at linear order, the same-stretch reading second order | §21 | `verify/test_the_einstein_tensor.py` |
| the second-order word: the time half settled at power three, the spatial remainder a quadrupole, and shown non-local | §21 | `verify/test_the_second_order_potential.py` |
| the rate line multiplies: the additive form second order, the exponential third, and the spatial equation named | §21 | `verify/test_the_multiplicative_budget.py` |
| the quadrature: Laplace plus the two quadrature equations annihilate the whole Weyl class, and the register's source is a rod of length 2m | §21 | `verify/test_the_quadrature.py` |
| the strut: the cross term on the axis between two counts is −4m₁m₂/d², a conical defect that is a supporting stress; its force fixed by the quadrature, Bach–Weyl's m₁m₂/(d² − (m₁ + m₂)²) for the register's rods | §21 | `verify/test_the_strut.py` |
| the helical sector: the conservative binary's count direction, the clock as the vector's norm, the first law with the apportioned clocks at Newtonian and first post-Newtonian order, three failing controls, and the conserved-mass metric selected | §21 | `verify/test_the_helical_sector.py` |
| the second-order comparison made: no divergence, the received invariants through third order satisfying the first law, the clocks meeting both exact limits, and the small body's inverse clock reproducing the self-force series with its π² term | §21 | `verify/test_the_2pn_comparison.py` |
| rotation inside: the stationary class annihilated the same way, the static equation as rate-and-clause together, and twist drawn one-signedly out of depth | §21 | `verify/test_the_twist.py` |
| radiation inside: the wave class annihilated by the same construction, and the composite clause found to track circulation rather than motion | §21 | `verify/test_the_radiative_class.py` |
| the quadrupole coefficient counted: a dimension over a rank by Schur, times the octave, with no radiation at the orbital frequency itself | §21 | `verify/test_the_quadrupole_coefficient.py` |
| the Schur family 2/(2L+1), the tetrahedral fourth, two rejected candidates, and the quadrupole's double uniqueness | §21 | `verify/test_the_schur_sweep.py` |
| the simplex constant as interval: (d+1)/d indexes the harmonic series, Fa is three-dimensional isotropy, and d = 3 uniquely meets the quadrupole's zero | §21 | `verify/test_the_simplex_interval.py` |
| the wheel under refinement: 2^d returns it only when three divides d, invariant at every depth in three, and the window's unique survivor | §21 | `verify/test_the_wheel_under_refinement.py` |
| what this is not: second order against fourth, no ghost, no free mass, and a power law where curvature-squared gravity gives a Yukawa | §21 | `verify/test_not_quadratic_gravity.py` |
| a fourth exact class on one Killing vector, native to the chart, the clause alone sufficing; and the clause's two conditions | §21 | `verify/test_the_null_class.py` |
| the crossing declared: one borrowed unit, two dimensionless structures, a density and an expansion rate | §21 | `verify/test_the_crossing_statement.py` |
| repulsion in four parts: the prohibition, the term already repulsive, the bounded reduction, and the ergoregion | §21 | `verify/test_repulsion.py` |
| the clock convergence: the register's count and the unimodular four-volume are one, and the frozen formalism thaws | §21 | `verify/test_the_clock_convergence.py` |
| the horizon cell: the quarter decomposed, the nat reading withdrawn on discreteness, and the target reposed as 4 ln 2 | §21 | `verify/test_the_horizon_cell.py` |
| the coupling derived: 8pi as the sphere's solid angle times a Bianchi-forced trace reversal, with no free factor | §21 | `verify/test_the_eight_pi.py` |
| the normalization: exponent and constant are one fact, closing the chain's dimensionless content and widening the borrow to three anchors | §21 | `verify/test_the_normalisation.py` |
| the three rulers named: the two outstanding ratios are the hierarchy problem and dimensional transmutation, and one candidate rejected | §21 | `verify/test_the_three_rulers.py` |
| the spatial word: the ruler as the enclosed amplitude, γ = 1 and β = 1, bending's factor two, Shapiro, the flat hollow, the perihelion base | §21 | `verify/test_the_spatial_word.py` |
| the assembly: the seven accounts, the cross-constants, the inventory of outstanding items | the Summary | `verify/test_gravity_complete.py` |
| big G: the ensemble's internal inconsistency, the comb–discordance incompatibility, the planetary quadrature floor, the fit engine | §13 | `verify/test_the_g_file.py` |

The identifications and the one conjecture presented in this paper are indicated
as such; every other statement in the paper is exact, and the table above maps
each one to the test that establishes it. The account is complete in the sense
set out in the Summary: open in five places, each recorded where it occurs. From
a single closure defect in a positional register the account derives the
one-signed pull, source proportionality, the equivalence principle and the
impossibility of screening. It derives quadrupole-first radiation, the
inverse-square law by two routes, the coupling, and the absence of a central
singularity. The tonal center as experienced in music is therefore a microcosmic
expression, in the domain of harmonic structure, of the general principle of
gravitation. It offers a tool with which to build a deeper understanding of the
phenomenon, one closer to an explanation than to a description. Section 23 states
the seventeen conditions under which the account fails, and the test suite
verifying every mathematical claim is public at
github.com/thefirsthorstmann/g-theory-verify.

## References

*Identifiers are given where they were verified against the source at the
time of writing; the remaining entries are complete by journal, volume and
page.*

**Companion volumes.** The companion volumes stand on the public record with digital object
identifiers, and the machine-verified suite named throughout §24 accompanies
them. They are: Gravity on Discrete Terms, the first statement, which this paper
supersedes; Tonal Function on Discrete Terms; The Clock Object; and
Position and Diffusion on Discrete Terms. With them stand the Navier–Stokes
resolution, Units on Discrete Terms, and The Octave Residual, the reanalysis
note whose template §12 states. The suite itself is a directory of re-runnable tests
distributed with those deposits.

**Measurement.**
Tiesinga, E., Mohr, P. J., Newell, D. B., and Taylor, B. N. (2021).
CODATA recommended values of the fundamental physical constants: 2018.
*Rev. Mod. Phys.* **93**, 025010. —
Xue, C., *et al.* (2020). Precision measurement of the Newtonian
gravitational constant. *National Science Review* **7**, 1803. —
Quinn, T., *et al.* (2026). Redetermination of the gravitational constant
with the BIPM torsion balance at NIST. *Metrologia* **63**, 025001,
doi:10.1088/1681-7575/ae570f. —
Bertotti, B., Iess, L., and Tortora, P. (2003). A test of general
relativity using radio links with the Cassini spacecraft. *Nature*
**425**, 374. —
Touboul, P., *et al.* (MICROSCOPE Collaboration) (2022). MICROSCOPE
mission: final results of the test of the equivalence principle. *Phys.
Rev. Lett.* **129**, 121102. —
Anderson, E. K., *et al.* (ALPHA Collaboration) (2023). Observation of
the effect of gravity on the motion of antimatter. *Nature* **621**,
716. —
Vessot, R. F. C., *et al.* (1980). Test of relativistic gravitation with
a space-borne hydrogen maser. *Phys. Rev. Lett.* **45**, 2081. —
Delva, P., *et al.* (2018). Gravitational redshift test using eccentric
Galileo satellites. *Phys. Rev. Lett.* **121**, 231101; and Herrmann,
S., *et al.* (2018). *Phys. Rev. Lett.* **121**, 231102. —
Bothwell, T., *et al.* (2022). Resolving the gravitational redshift
across a millimetre-scale atomic sample. *Nature* **602**, 420. —
Lan, S.-Y., *et al.* (2013). A clock directly linking time to a
particle's mass. *Science* **339**, 554. —
Cacciapuoti, L., and Salomon, C. (2009). Space clocks and fundamental
tests: the ACES experiment. *Eur. Phys. J. Special Topics* **172**,
57. —
Kapner, D. J., *et al.* (2007). Tests of the gravitational inverse-square
law below the dark-energy length scale. *Phys. Rev. Lett.* **98**,
021101. —
Abbott, B. P., *et al.* (LIGO, Virgo, Fermi-GBM, INTEGRAL) (2017).
Gravitational waves and gamma-rays from a binary neutron star merger:
GW170817 and GRB 170817A. *Astrophys. J. Lett.* **848**, L13. —
Abbott, R., *et al.* (2020). GW190814: gravitational waves from the
coalescence of a 23 solar mass black hole with a 2.6 solar mass compact
object. *Astrophys. J. Lett.* **896**, L44. —
Riley, T. E., *et al.* (2021). A NICER view of the massive pulsar PSR
J0740+6620. *Astrophys. J. Lett.* **918**, L27. —
Abedi, J., Dykaar, H., and Afshordi, N. (2017). Echoes from the abyss.
*Phys. Rev. D* **96**, 082004; and the reanalysis, Westerweck, J., *et
al.* (2018). *Phys. Rev. D* **97**, 124037. —
Abdo, A. A., *et al.* (Fermi-LAT) (2009). A limit on the variation of the
speed of light arising from quantum gravity effects. *Nature* **462**,
331. —
Planck Collaboration (2020). Planck 2018 results VI: cosmological
parameters. *Astron. Astrophys.* **641**, A6. —
Riess, A. G., *et al.* (2022). A comprehensive measurement of the local
value of the Hubble constant. *Astrophys. J. Lett.* **934**, L7. —
DESI Collaboration (2025). DESI DR2 results II: measurements of baryon
acoustic oscillations and cosmological constraints. arXiv:2503.14738.

**Theory this paper builds on or against.**
Jacobson, T. (1995). Thermodynamics of spacetime: the Einstein equation
of state. *Phys. Rev. Lett.* **75**, 1260. — Verlinde, E. (2011). On the origin of gravity and the laws of Newton. *J. High Energy Phys.* **2011**(4), 029. — Milgrom, M. (1983). A modification of the Newtonian dynamics as a possible alternative to the hidden mass hypothesis. *Astrophys. J.* **270**, 365. —
Bombelli, L., Lee, J., Meyer, D., and Sorkin, R. D. (1987). Space-time as
a causal set. *Phys. Rev. Lett.* **59**, 521. —
Rideout, D. P., and Sorkin, R. D. (2000). Classical sequential growth
dynamics for causal sets. *Phys. Rev. D* **61**, 024002. —
Sornette, D. (1998). Discrete-scale invariance and complex dimensions.
*Physics Reports* **297**, 239. —
Ambjørn, J., Jurkiewicz, J., and Loll, R. (2005). Spectral dimension of
the universe. *Phys. Rev. Lett.* **95**, 171301. —
Buchdahl, H. A. (1959). General relativistic fluid spheres. *Phys. Rev.*
**116**, 1027. —
Bekenstein, J. D. (1973). Black holes and entropy. *Phys. Rev. D* **7**,
2333; Hawking, S. W. (1975). Particle creation by black holes. *Commun.
Math. Phys.* **43**, 199. —
Carlip, S. (2000). Aberration and the speed of gravity. *Phys. Lett. A*
**267**, 81. —
Li, M. (2004). A model of holographic dark energy. *Phys. Lett. B*
**603**, 1. —
Lamport, L. (1978). Time, clocks, and the ordering of events in a
distributed system. *Commun. ACM* **21**, 558. —
Landauer, R. (1961). Irreversibility and heat generation in the computing
process. *IBM J. Res. Dev.* **5**, 183; Margolus, N., and Levitin, L. B.
(1998). The maximum speed of dynamical evolution. *Physica D* **120**,
188. —
Bertrand, J. (1873). Théorème relatif au mouvement d'un point attiré vers
un centre fixe. *C. R. Acad. Sci. Paris* **77**, 849. —
Midy, E. (1836). *De quelques propriétés des nombres et des fractions
décimales périodiques*. Nantes. —
Conway, J. H., and Sloane, N. J. A. (1999). *Sphere Packings, Lattices
and Groups*, 3rd ed. Springer. —
Chandrasekhar, S. (1983). *The Mathematical Theory of Black Holes*.
Oxford. —
Bach, R., and Weyl, H. (1922). Neue Lösungen der Einsteinschen
Gravitationsgleichungen. *Mathematische Zeitschrift* 13, 134–145. —
Israel, W. (1977). Line sources in general relativity. *Physical Review D*
15, 935–941. —
Detweiler, S. (2008). Consequence of the gravitational self-force for
circular orbits of the Schwarzschild geometry. *Physical Review D* **77**,
124026. —
Le Tiec, A., Blanchet, L., and Whiting, B. F. (2012). First law of binary
black hole mechanics in general relativity and post-Newtonian theory.
*Physical Review D* **85**, 064039. —
Friedman, J. L., Uryū, K., and Shibata, M. (2002). Thermodynamics of
binary black holes and neutron stars. *Physical Review D* **65**, 064035. —
Gibbons, G. W., and Stewart, J. M. (1983). Absence of asymptotically flat
solutions of Einstein's equations which are periodic and empty near
infinity. In *Classical General Relativity*, Cambridge, 77. —
Blanchet, L., Detweiler, S., Le Tiec, A., and Whiting, B. F. (2010).
High-order post-Newtonian fit of the gravitational self-force for circular
orbits in the Schwarzschild geometry. *Physical Review D* **81**, 064004.
