---
title: Units on Discrete Terms
subtitle: What a physical unit is, which quantities a change of unit can move, and the status of the numerical value assigned to the speed of light
byline: Christian Horstmann · thefirsthorstmann@gmail.com · August 25th, 2026 · manuscript for the public record
date: 2026-08-05
titlenote: Every arithmetic statement here is exact, reproducible in a few lines and verifiable by machine, and the checks are named at the point at which each is made. Nothing in the development introduces a free parameter, and the whole of it rests on a single measured quantity, shown in §3 to be irreducible. Physical constants are quoted from the 2019 SI and the standard determinations. The running of the electromagnetic coupling in §8 and the nucleosynthesis pathway in §12 are standard results and are cited as such.
abstract: A physical magnitude is a dimensionless structure multiplied by one measured reference, and the reference is chosen rather than derived. This paper sets out the consequences of that division for the present system of units. Three results are established. First, a rescaling theorem: under any change of unit every dimensionless ratio is invariant, so no experimental agreement or disagreement can be created or removed by redefinition, and any claim that a rescaling improves a comparison is therefore false. Second, a register theorem: the length of the repeating block of 1/q in base b is the multiplicative order of b modulo q, from which the divisibility properties of the all-nines integers follow. Third, an account of the four historical redefinitions of the metre, each of which selected a numerical value for continuity with the preceding artefact rather than for any property of the number itself. A proposal is then made and labelled as metrological rather than physical: a rescaling of the metre by 0.0692 percent would give the speed of light the value 3 × 10⁸, whose factorisation contains only the base primes. The case for it is informational rather than economical: a numeral carries an extent as well as a value, only the value is invariant under a change of unit, and the SI numeral fixes an extent at which the register's structure cannot be read. No atomic or nuclear construction independently selects the same metre, so the proposal establishes a preference among conventions rather than a derivation. This paper continues to express every quantity in SI units; the rescaling is recorded for the metrological community, not applied here. Every exact claim re-derives in a public suite at github.com/thefirsthorstmann/g-theory-verify.
---

<!-- CONTENTS -->
<div style="page-break-before:always"></div>

<style>table:first-of-type { width: 96%; }
table:first-of-type td:last-child { text-align: right; }</style>

| | |
|---|---|
| **1 · Introduction** | 3 |
| **2 · The dimensional boundary** | 3 |
| **3 · The number of required references** | 4 |
| **4 · Conservation of the reference under relocation** | 4 |
| **5 · The present placement: the International System** | 5 |
| **6 · Invariance under rescaling** | 6 |
| &nbsp;&nbsp;&nbsp;6.1 · The dual cancellation: what a reading carries about a constant | 6 |
| **7 · The speed of light and the choice of metre** | 8 |
| **8 · Rest values and observed values** | 13 |
| **9 · The information carried by a positional expansion** | 14 |
| &nbsp;&nbsp;&nbsp;9.1 · Writing a reading so that it carries its own extent | 17 |
| **10 · The base, and what base-dependence does and does not show** | 18 |
| &nbsp;&nbsp;&nbsp;10.1 · The base as a position: the register theorem | 19 |
| &nbsp;&nbsp;&nbsp;10.2 · The arithmetic of the carriers | 20 |
| &nbsp;&nbsp;&nbsp;10.3 · The base as a register, and what a lossy reading actually loses | 20 |
| **11 · A worked case: the coupling, the spine, and the nucleon** | 21 |
| **12 · The placement criterion** | 24 |
| **12b · Addendum: the gravitational constant, revisited** | 26 |
| **13 · Prohibitions** | 27 |
| **14 · Conclusion** | 28 |

<div style="page-break-before:always"></div>
<!-- /CONTENTS -->

## 1 · Introduction

Every physical quantity consists of a number and a reference. The first is subject to derivation, proof, and refutation. The second is not: no argument yields the metre. Its value is established by stipulation, successively as a prototype bar, a wavelength of krypton-86, and since 1983 a fixed decimal value for the speed of light. Each such stipulation is a convention and not a result.

The traditional statement of the asymmetry is that a number carries no ruler, and the reason is exact: the relations of arithmetic are symmetric under rescaling. An equality between pure numbers holds independently of any unit in which its terms might be expressed, and no operation of algebra distinguishes one scale from another. Nothing in the structure selects a magnitude, because the structure is invariant under every change of magnitude.

That statement concerns the *value* a numeral denotes. A numeral is not exhausted by its value. A positional expansion carries, in addition, an extent and a traversal — how many places are read, and what path the digits describe — and these are counts rather than values. Counts are dimensioned by their own quantum. §9 develops this and demonstrates it on a worked case.

The asymmetry between the constituents is therefore structural rather than historical, and it is not removed by improving the stipulation. It admits exact statement, and the statement has consequences: it determines how much external input a theory requires, which of its constants may be derived, and where the required input must be placed. §§2 through 11 establish each in turn.

## 2 · The dimensional boundary

A dimensionless quantity determines no scale.

The relation between two and three is fixed and complete without reference to any magnitude. It remains unchanged when a scale is supplied and is indifferent to the supply. A magnitude is therefore not a number: it is a number multiplied by a reference, and the reference is not contained in the number.

**Theorem 1. No construction from dimensionless structure alone determines a dimensionful magnitude.**

This constrains every physical theory identically. Each meets the boundary at some point, through a fixed coupling, a stipulated unit, or a dimensional transmutation scale. A theory purporting to derive a length from dimensionless structure contains an error at a step identifiable by dimensional analysis alone.

The boundary is expressible in the language it constrains: the distinction between dimensionless and dimensionful quantities is itself a statement about number. The position reduces to

**magnitude = (dimensionless structure) × (one measured reference)**

in which the left factor admits derivation and the right does not.

## 3 · The number of required references

The boundary establishes that at least one measured quantity must be supplied externally. It does not establish the number required. That is a separate proposition with an exact answer.

Suppose every dimensionless quantity in a system is fixed. Let λ be any positive real, and scale every mass by λ and every length by λ⁻¹. Every mass ratio is invariant, both terms having scaled identically; every length ratio is invariant; every dimensionless combination is invariant by construction. No observable quantity has changed, and the units differ.

This family of rescalings constitutes a one-parameter group.

**Theorem 2. The number of measured quantities a physical theory must supply externally is exactly one.**

A smaller number is excluded because the group is nontrivial: dimensionless structure leaves λ undetermined and cannot yield a metre. A larger number is excluded because the group has a single parameter, so a second supplied quantity is determined by the first through dimensionless structure and constitutes a restatement rather than an addition.

The proposition stands one level beneath the boundary. The boundary states that a reference must be supplied; this states how much.

## 4 · Conservation of the reference under relocation

Given §3, the several constants that appear to fix scales independently cannot be independent.

The candidates are five. The atomic mass unit, defined as one twelfth of the
mass of carbon-twelve. The proton charge radius. The scale at which the strong
coupling reaches unity. The Planck mass, constructed from the gravitational
constant. And the caesium-133 hyperfine frequency. These constitute five presentations of one input. Each reduces to any other through dimensionless structure, and at the present definitional floor all reduce to the caesium frequency. No dimensionless structure yields the numeral 9192631770.

**Corollary 1. The presentation of the reference is free; its quantity is fixed at one, and no reformulation reduces it.**

A consequence for the reading of constants follows, and the distinction is exact. The decimal expansion of a *dimensionless* quantity — a coupling, a mass ratio — is structural, and is a legitimate object of investigation independently of whether structure is found in it. The decimal expansion of a *dimensioned* constant expressed in metres and seconds is relocatable reference, and structure identified there is structure in a definitional system rather than in the physics. The two are typographically indistinguishable and are not the same class of object.

## 5 · The present placement: the International System

The abstract character of the present standards is not a criticism of them. It is a design decision, taken deliberately, and the 2019 revision carried it to completion. Every base unit of the SI is now defined by assigning an exact value to a constant of nature. No base unit is any longer a measurement, and no artefact remains.

| base unit | quantity | fixed by | stipulated value | role |
|---|---|---|---|---|
| second | time | Δν(¹³³Cs) | 9192631770 Hz | **sets the scale** |
| metre | length | *c* | 299792458 m·s⁻¹ | converts time to length |
| kilogram | mass | *h* | 6.62607015 × 10⁻³⁴ J·s | converts to mass |
| ampere | electric current | *e* | 1.602176634 × 10⁻¹⁹ C | converts to charge |
| kelvin | temperature | *k* | 1.380649 × 10⁻²³ J·K⁻¹ | converts to temperature |
| mole | amount of substance | *N*_A | 6.02214076 × 10²³ mol⁻¹ | a cardinality |
| candela | luminous intensity | *K*_cd | 683 lm·W⁻¹ | photometric weighting |

The final column is the observation this section exists to make. **Of the seven stipulations, one sets a scale and six do not.** The caesium frequency establishes a magnitude of time. The speed of light converts time into length; the Planck constant converts into mass; the elementary charge into charge; the Boltzmann constant into temperature. The Avogadro constant is a cardinality, fixing how many entities constitute a mole, and the luminous efficacy is a weighting referred to human photopic response. Six of the seven are conversion factors between dimensions or countings within one, and none of the six sets a scale independently of the first.

This is §3 instantiated in the operative system. The theorem states that one reference is required and no more; the SI, arrived at by an entirely different route and for entirely practical reasons, supplies exactly one and expresses the remainder as conversions.

**The status of *c* follows and should be stated without ambiguity.** The 1983 stipulation of *c* = 299792458 m·s⁻¹ constituted no measurement of light and improved no determination of its speed. It transferred the reference out of the metre and into a definition, after which the metre is *defined* as the distance light travels in 1/299792458 of a second. The exactness is a property of the definition; what the definition constructs is the metre. The integer is not a fact about light and carries no structure: it is the numerical residue of an earlier metre, retained so that the new definition would not disturb existing measurements. Any attempt to read significance into its digits is reading the length of a French survey, and the same holds for the digits of *h*, *e*, *k* and *K*_cd.

The 2019 stipulation of *h* performed the corresponding transfer for the kilogram, with the consequence that the atomic mass unit, previously exact by definition, became a measured quantity with an uncertainty. Nothing was created or destroyed in either transfer. The reference moved — and the measurability moved with it: the same revision that fixed *h* returned μ₀, stipulated since 1948, to the class of measured quantities. §6.1 sets out what that stipulation had provided, and what it had silenced.

## 6 · Invariance under rescaling

The conservation statement has a directly verifiable corollary.

Let a prediction and a measurement of the same dimensionful quantity disagree. Replace the metre by *k* metres, for any positive *k* — a rescaled metre, in the sense of §3's group. The prediction is divided by *k*; the measurement is divided by *k*; their ratio is unchanged.

Verified on the proton charge radius, where a derived value and an experimental value are adjacent and unequal: rescaling by *k* = 1, 2.5, 10⁻³ and 10⁶ returns the ratio 1.000482 in every case, to all digits carried.

**No numerical disagreement is removable by a choice of unit, and none is producible by one.**

The statement constrains the present framework exactly as it constrains any other. A discrepancy of this kind is not a units problem and is not relieved by re-anchoring; it is either a statement about the physics or an arithmetic error, and no third possibility exists.

*Machine check: `verify/test_semitone_seam.py`.*

### 6.1 · The dual cancellation: what a reading carries about a constant

§6 concerns changes of unit: none moves a comparison. Its dual concerns the constants that enter a reported number twice — once through the defining expression and once through the unit the report is expressed in — and it is exact in the same way.

**Where a constant enters the defining expression and the reporting unit at the same exponent, it divides out of the report, and the reading is silent about that constant at every precision.** The proof is one line: the report contains the factor *X*^*m*/*X*^*m*, identically 1, before any apparatus is consulted. Precision does not help, because nothing is left for precision to resolve. Such a comparison is not a weak test of the constant; it is no test of it.

The operative system contains two standing instances, and neither is an accident.

**The angular instance.** The radian is arc against radius; the arcsecond is defined from it by 1 rad = (648 000/π)″. The relativistic perihelion advance is 6πGM/c²a(1−e²) radians per orbit; the ephemerides it is compared against are kept in arcseconds. In that comparison 6π × 648 000/π = 3 888 000 exactly. The celebrated
agreement — 42.98″ per century predicted, 42.98″ observed — is, at whatever
precision it is carried, silent about π. The constant cancels between the
formula and the unit before prediction meets measurement. The same holds for every angular comparison conducted in degrees or their subdivisions.

**The electromagnetic instance, which was a design decision.** From 1948 to 2019 the magnetic constant was stipulated: μ₀ = 4π × 10⁻⁷ H·m⁻¹, the numeral chosen in the rationalisation of the units precisely so that the 4π of the field equations would cancel against it. Within that system α = μ₀ce²/2h is proportional to π by stipulation, so α/π =
2 × 10⁻⁷ce²/h carries no π at all. The leading term of the electron's
anomalous moment, α/2π — the most precisely verified prediction in physics —
was therefore π-free by construction. Seven decades of electromagnetic readings were silent about the circle constant because the unit system had been designed, for a different and legitimate purpose, in exactly the way that silences them. §9.1 argues that a structured numeral keeps the ledger of a reading legible; this stipulation is the inverse operation, performed deliberately — a numeral chosen so that a constant vanishes from every ledger at once.

**For the derived constants the bookkeeping is mechanical.** Taking the stipulated constants as primitives — all seven numerals are π-free — together with the measured, π-free readings *m*_e and *G*, a derived constant carries π exactly as its defining expression does, and the expressions divide cleanly:

| derived constant | expression | net power of π |
|---|---|---|
| von Klitzing constant | *h*/*e*² | 0 |
| Josephson constant | 2*e*/*h* | 0 |
| magnetic flux quantum | *h*/2*e* | 0 |
| Compton wavelength | *h*/*m*_e*c* | 0 |
| second radiation constant | *hc*/*k* | 0 |
| **reduced Planck constant** | *h*/2π | **−1** |
| reduced Compton wavelength | ħ/*m*_e*c* | −1 |
| Bohr magneton | *e*ħ/2*m*_e | −1 |
| first radiation constant | 2π*hc*² | +1 |
| Stefan–Boltzmann constant | 2π⁵*k*⁴/15*h*³*c*² | +5 |
| Planck length | √(ħ*G*/*c*³) | −½ |

The parity in the table has one source. *h* is stipulated and π-free. ħ = h/2π is the single gate through which π enters
the system's own constants. A derived numeral carries π exactly as its route
passes through that gate, or through an explicit π of its formula. Which of the pair a formula is written in is a convention — and the convention is not innocent. The modern Planck units are defined on ħ; Planck's own units of 1899 were defined on *h*; the two differ by the factor √(2π) = 2.5066…, so that "the Planck length" names a convention rather than a length.

**The tables therefore hold three classes of object, and they are typeset as one.** A **stipulation** is exact by decision and reads nothing: the seven constants of §5, and formerly μ₀. A **reading** is a measurement: *G*, the electron mass, the mass ratios, and since 2019 the magnetic constant, whose uncertainty is now that of α. A **computation** is evaluated from the other two and adds nothing to them: it has exponents but no apparatus, and there is no second determination of it against which it could be checked. The Planck units are computations, and no experiment has returned one. Since ħ
and c are exact, their entire uncertainty is the 22 parts per million of G.
That is the least-determined constant in the tables, and its published
determinations disagree beyond their stated uncertainties. The 2019 revision, in these terms, was a rotation of constants between the
classes. Four moved from readings to stipulations: h, e, k and NA. One, μ₀,
moved from stipulation to reading. The von Klitzing and Stefan–Boltzmann
constants became exact computations, and the atomic mass unit became a reading. §5 stated that in each transfer the reference moves and nothing is destroyed. The same holds one level up: **measurability moves and is not destroyed** — every constant fixed by decision is balanced by a constant set free to be measured.

What the cancellation licenses is stated exactly, and it is negative. It does not show that π is a parameter of nature awaiting a better channel: π enters physics through the definitions of angular measure and of the harmonic cycle, and is not a quantity an apparatus constrains. What the bookkeeping identifies, before any apparatus is built, is which
comparisons are capable of carrying information about which constants. It also
identifies which are silent by construction, so that a null obtained through
them is a property of the channel and not of the world.

*Machine check: `verify/test_leverage.py`; the exponent derivations, by composition from the stipulated primitives, in `tools/codata_leverage.py`.*

## 7 · The speed of light and the choice of metre

§5 established that the numeral 299792458 is the residue of an earlier metre. This section states what follows if the metre is chosen differently, and it is the one place in this paper where a proposal is made rather than a result reported. The proposal is labelled as such, and the arithmetic beneath it is separated from it.

**The arithmetic first.** Consider the two integers nearest to the rate of light at the octet:

```
   3 × 10⁸        =  300 000 000  =  2⁸ · 3 · 5⁸

   3 × (10⁸ − 1)  =  299 999 997  =  3³ · 11 · 73 · 101 · 137
```

The first factors into the base primes and nothing else: the base of the numeral system is 10 = 2 · 5, and 3 × 10⁸ contains 2, 3 and 5 alone. The second is three times the all-nines integer at eight places, and it carries the fine-structure prime.

**Theorem 3.** The fine-structure prime divides the all-nines integer at
eight places, and the cofactor is that prime's own repeating block:

```
   ord₁₃₇(10)  =  8          hence   137 | 10⁸ − 1

   (10⁸ − 1) / 137  =  729927  =  the repeating block of 1/137
```

That is Midy's structure, not a coincidence of size: the period of 1/*q* in base *B* is ord_*q*(*B*), the repeating block times *q* equals the all-nines integer of that length, and here the length is eight. The consequence is that the all-nines integer at eight places contains 137 by construction, and three times it contains 137 still, while 3 × 10⁸ does not contain it at all. The two integers differ by exactly 3.

**What every redefinition of the metre has done, and what none of them has done.** Each redefinition has followed the same rationale. The metre is re-expressed in terms of a more stable or more reproducible reference. The numerical value is then chosen so that the new definition agrees with the old to within the precision then available. The history is set out below because the proposal that follows rests on the same rationale, while differing from its predecessors in practice rather than in principle.

| year | the metre defined as | the definition's character | the numeral chosen |
|---|---|---|---|
| 1799 | 1/10 000 000 of the meridian quadrant | an artefact of the Earth | fixed by survey |
| 1889 | the length of a prototype bar | an artefact in a vault | to match 1799 |
| 1960 | 1 650 763.73 wavelengths of krypton-86 | a natural constant | to match 1889 |
| 1983 | the distance light travels in 1/299 792 458 s | a natural constant | to match 1960 |
| 2019 | (unchanged; all seven units recast on constants) | natural constants throughout | to match 1983 |

Every revision improved the **definition** and preserved the **numeral**. That was deliberate and correct: the purpose of each redefinition was to put the unit on a better foundation without invalidating existing measurements, and preserving numerical continuity is exactly how that is achieved. The consequence, however, is that the *definitions* are now structural while the *numbers* still descend, unbroken, from a survey of the meridian between Dunkirk and Barcelona. **The metrological reform is complete in its definitions and untouched in its numerals.**

**The fence.** 300 000 000 and 299 792 458 **are not two speeds**, and nothing in this section proposes that light moves at a rate other than the measured one. They are one rate read on two rulers 0.07 % apart. Nor does anything here derive a metre from arithmetic; Theorem 1 forbids that and is not circumvented. The 2019 revision established the principle that a unit should rest on a constant rather than on an artefact. **The observation of this section is that the numerical value assigned still rests on the artefact, and the proposal is to complete the reform in the direction it already travels.** Nothing about that is a departure from metrological practice. It would be the fifth redefinition of the metre, and it differs from the four preceding ones only in the criterion by which the numeral is selected.

**The proposal, which is metrological and not a hypothesis about nature.** Re-choose the metre alone, retaining the second, by the factor

<div style="margin:4pt 0 8pt 14pt;">0.999 308 193 3 × the SI metre &nbsp;=&nbsp; (299 792 458 / 300 000 000) × the SI metre,</div>

a change of 0.0692 %. On that metre the same rate of light reads exactly 3 × 10⁸. **This rescaled metre is referred to below as the native metre**. The name denotes
one specific unit and not a class: it is the particular member of the family
of rescaled metres at which the numeral for c becomes 3 × 10⁸. Any other member of that family — any positive multiple of the SI metre — remains equally admissible under §6, which is exactly why the choice among them must be made on grounds other than measurement. This requires no new physical claim and can be evaluated entirely on cost and benefit, in the way the four previous redefinitions were.

**What such a rescaling changes, and what it does not:**

| quantity | under a 0.0692 % rescaling of the metre |
|---|---|
| the second, and every frequency | **unchanged** — the second is retained |
| every dimensionless ratio | **unchanged** — α, *m*_p/*m*_e, every mass ratio, every angle |
| every experimental agreement or disagreement | **unchanged** — by §6 |
| every length, expressed numerically | rescaled by 0.999 308 |
| every derived unit containing a length | rescaled by the corresponding power |
| the numerical value of *c* | 299 792 458 → 3 × 10⁸ |

The first three rows are the whole of the cost. **No dimensionless quantity moves, no comparison between theory and experiment moves, and no measurement is invalidated.** The adjustment is 0.0692 %, which is smaller in consequence than the 1799, 1889, 1960 and 1983 changes, each of which was adopted without disturbing physics.

**The criterion by which the numeral would be selected.** The four previous revisions selected the numeral for continuity with the preceding artefact. The proposal is to select it for structure instead. On the SI metre the rate
of light is 299 792 458 = 2 · 7 · 73 · 293 339, an integer encoding the length
of a meridian survey. On the native metre it is 3 × 10⁸ = 2⁸ · 3 · 5⁸,
containing the base primes and the dimension count and nothing else, with an
all-nines neighbour carrying the coupling prime by Theorem 3. Neither number is more true. One is structured and one is historical, and §4 establishes that the choice between them is free.

**Observation. Within one per cent of the measured rate, exactly four integers factor entirely into the base primes {2, 3, 5}: 298 598 400, 300 000 000, 301 989 888 and 302 330 880. Of these, 3 × 10⁸ is the nearest — requiring a rescaling of 0.0692 per cent against 0.398 per cent for the next — and such targets occur at a density of roughly one in 1.5 million integers.**

That is the whole of what is claimed for the numeral, and it is a statement
about availability rather than about nature. If a structured target is wanted,
one is available at a cost smaller than any of the metre's previous revisions,
and it is the closest such target that exists.

**What the all-nines observation does and does not add.** Since ord₁₃₇(10) = 8, the integer 10^*k* − 1 carries 137 precisely when 8 divides *k*. The place-count *k* is fixed by the choice of unit, so the observation is a condition **on the choice** rather than a property of the rate. It is not, however, a free condition:

| *k* | metre required | change from the SI metre | 8 divides *k* |
|---|---|---|---|
| 7 | 9.993 × | ×9.99 | no |
| **8** | **0.999 308 ×** | **−0.0692 %** | **yes** |
| 9 | 0.099 93 × | ×0.0999 | no |
| 16 | 9.993 × 10⁻⁹ | ×10⁻⁸ | yes |

**The only place-count divisible by eight that is reachable without altering the metre by orders of magnitude is *k* = 8, and the scaling it requires is the same 0.0692 per cent already proposed.** The next is *k* = 16, which needs a further factor of 10⁸. So the proposed metre is the unique metre within any reasonable distance of the present one at which the all-nines neighbour of *c* carries the coupling prime.

The place-count is supplied by the unit, and a unit is chosen. What the
observation establishes is a second property satisfied by the same choice, at
no additional cost: the rescaling that reaches the nearest structured numeral
is also the rescaling that reaches a place-count the coupling divides. **Two conditions, one choice, and the choice was already the cheapest available.**

The genericity question this raises was decidable and has been decided: the count above is the decision. Clean targets at this precision are rare — four in a one-per-cent window — and the one at issue is the closest of them. **The remaining question was whether any construction not using the value of *c* independently fixes this same metre. It has been tested, and it does not.**

A length can certainly be built without *c*. Solving the dimensional system over ħ, *m*_e and *e*²/4πε₀ for a quantity of dimension L gives exponents (2, −1, −1):

<div style="margin:4pt 0 8pt 14pt;"><i>a</i>₀ = 4πε₀ħ² / (<i>m</i><sub>e</sub><i>e</i>²)</div>

the Bohr radius, in which *c* does not appear. Since α is dimensionless and its value is fixed without reference to any unit, every dimensionless multiple of *a*₀ inherits this — the classical electron radius α²*a*₀, both Compton wavelengths, the Rydberg length 4πα*a*₀. **The metre can therefore be fixed without the speed of light.**

Whether it is fixed *here* is a separate question, and applying the criterion already used above — a {2, 3, 5}-smooth mantissa, or one within a few parts in 10⁴ — to eight standard atomic lengths in both metres:

| length | SI, off by | native metre, off by |
|---|---|---|
| Bohr radius *a*₀ | +0.315 % | +0.245 % |
| classical electron radius | −0.193 % | −0.262 % |
| reduced Compton (electron) | −0.559 % | +0.614 % |
| Compton (electron) | +0.152 % | +0.083 % |
| proton charge radius | −0.130 % | −0.199 % |
| reduced Compton (proton) | −0.170 % | +0.230 % |
| Rydberg length 1/*R*_∞ | −0.002 % | −0.071 % |
| first Bohr circumference | −0.215 % | −0.284 % |

**Nothing is structured in the native metre.** The closest is the Rydberg length at 0.071 %, with the electron Compton wavelength next at 0.083 %. Against a criterion of a few parts in 10⁴ these miss by a factor of about two and a half — not a near miss, but not the order-of-magnitude gap an earlier revision of this section claimed either. The conclusion is unchanged: neither is inside the criterion, and the negative below stands on the whole table rather than on its best row.

One entry warrants notice rather than dismissal: the Rydberg length in SI is 9.112 670 5 × 10⁻⁸ m, and 9 112 500 = 2²·3⁶·5⁵ is smooth — 19 parts per million away. At that tolerance a random mantissa falls within reach 0.445 % of the time, and sixteen trials were made, giving an expected count of 0.071 and a chance probability near 7 per cent. It is not significant, and it is a hit in **SI**, which if taken at face value would argue for the metre already in use.

**Two questions have to be kept apart here, because they sound alike and have different answers.**

*Does the proposal fix a metre?* Yes, and trivially — stipulating *c* = 3 × 10⁸ fixes the metre exactly as stipulating *c* = 299 792 458 fixed it in 1983. That was never at issue.

*Does anything besides *c* independently select the same metre?* **No.** That is the question just tested, and it is the one that would have given the proposal a second, independent support. It does not have one.

**The conclusion is negative: no atomic construction fixes the metre proposed
here.** No independent derivation is available within the atomic domain, and
none is claimed.

**What the case does rest on is information, and this is where §9 applies.**
A positional expansion carries three registers: a value, an extent, and a
traversal. Only the value is invariant under a change of unit. The extent —
the number of places the reading occupies — and the traversal are fixed by
the choice of unit, so choosing a unit chooses what remains legible in the
numeral. That choice cannot be declined, since some unit must be adopted.

The two candidates differ in what they preserve:

```
   SI metre       c = 299792458   =  2 · 7 · 73 · 293339
                  extent 9 places
                  293339 is prime and enters from a meridian survey;
                  nothing of the register is legible in it

   native metre   c = 3 × 10⁸     =  2⁸ · 3 · 5⁸
                  extent 8 places
                  factors over the base primes alone, and by Theorem 4
                  the all-nines integer at that extent is
                  10⁸ − 1 = 3² · 11 · 73 · 101 · 137,
                  divisible by the coupling prime because ord₁₃₇(10) = 8
```

The SI numeral is not neutral between these. It is the residue of an
eighteenth-century survey, and adopting it fixes the extent at a place-count
where the register's own structure cannot be read. The rescaling does not
add information to the constant, whose value is unchanged; it selects the
extent at which the information already present becomes legible. **The
argument is therefore about what a convention discards, not about what it
costs.** The truncation ledger of §9 governs the same distinction. A
reading cut at a depth loses a determined quantity, one-signed and exactly
calculable. That loss is a property of where the cut falls, not of the value
being read.

That said, the argument establishes a preference among conventions and not a
derivation of one. Any positive multiple of the SI metre remains admissible
under §6, and §7's test shows that nothing outside the value of *c* selects
this particular multiple. Constructions from nuclear, condensed-matter or cosmological scales are untested and remain available to anyone who wants to try them.


## 8 · Rest values and observed values

§§2 through 6 concern the arithmetic of units. This section and the next concern what a number is, and together they determine the placement treated in §9.

**Every constant admits two values.** Its *rest value* is what the structure determines in the fully coherent limit, prior to scale-conditioning and prior to measurement. Its *observed value* is the output of an apparatus. These are distinct objects related by a map fixed by physics.

Three mechanisms separate them. The first two are standard; the third is the subject of §9 and is stated here because it is the one whose map is exactly known.

The first is the projective character of measurement. A coherent descriptor carries amplitudes and phases; a measurement returns squared magnitudes, and phase is not recoverable from a squared magnitude in a single determination. The map is many-to-one and phase-destroying. Content present in the coherent object beyond its magnitudes is absent from the reading.

The second is that a probe couples to the quantity it interrogates and contributes to the result. In quantum electrodynamics the electromagnetic coupling runs with momentum transfer, taking the value 1/137.036 at *Q*² = 0 and approximately 1/128 at *Q*² = *m*_Z². This is one constant returning two values under two interrogations, the difference arising because a higher-momentum probe penetrates further into the vacuum polarisation screening the bare charge. The direction of the running is theory-dependent — in quantum chromodynamics the coupling runs oppositely, by asymptotic freedom — while the structure is general: **the reading carries the scale of the probe that produced it.**

**The third is that a reading terminates at a depth.** A quantity whose expansion does not close — every rational with a repeating period, and every irrational — is never written down in full. What is written is a reading at some extent, and the extent is a choice made by the reader rather than a property of the quantity.

This is the same structure as the probe, one register over. The electromagnetic coupling reads differently according to the momentum at which it is interrogated, and its rest value is the limit as that momentum goes to zero. A repeating expansion reads differently according to the depth at which it is stopped, and its rest value is the exact fraction the reading approaches. **In both cases the reading carries the scale at which it was taken, and the rest value is the limit the readings approach.**

The difference between the two is that **the truncation map is exactly calculable at every depth, and the other two are not.** Phase discarded by a projective measurement is not recoverable at all. The running of a coupling is calculable but requires a theory of the interaction. The residue left by stopping a reading at a stated depth requires nothing
beyond arithmetic. It is the tail, and §9 computes it in closed form: one unit
of the final place per complementary pair, three units per rotation, with the
sign determined by the digit the reading stops before.

**So truncation is the mechanism by which a rest value and an observed value are separated in the one case where the separation can be written down exactly.** That is why the sevenths are the worked example of §9 rather than an illustration: they are the case in which the rest value, the observed value, and the exact distance between them are all available simultaneously.

A rest value therefore resides at the zero-probe limit, is obtained by extrapolation, and is not in principle the output of any single determination.

From this a classification follows. A dimensionful quantity is either **defined at the zero-probe limit** or **constituted as a reading under stated conditions**. Only the first admits use as a theory's reference without transmitting the characteristics of an apparatus into the theory's magnitudes.

Two properties of the map follow.

**The map is fixed in advance and independently calculable.** The running of a coupling is computed rather than fitted, and extrapolation to zero momentum transfer is standard procedure with quoted uncertainties. A rest value asserted for a constant therefore carries a determinate prediction for the observed value at any stated probe scale, and the two are checked against each other by the same computation everyone else performs.

**The distinction separates a derived value from a fitted one.** A framework that fits its parameters possesses no value prior to observation, its number being defined as the reading. A framework that determines a value from structure possesses one, and is refutable in a manner the first is not.

## 9 · The information carried by a positional expansion

§1 stated that a numeral is not exhausted by its value. This section establishes what else it carries, and the demonstration is arithmetic throughout.

A positional expansion of a rational number resolves into three registers, of which only the first is a value:

| register | what it is | dimensioned | invariant under reordering |
|---|---|---|---|
| **value** | the quantity denoted | no — the traditional statement of §1 holds | no |
| **extent** | the number of places read | yes: quantised by the period of the address | yes |
| **traversal** | the path the digits describe | yes: counted in positions | no |

**Theorem 4. The extent of a complete positional reading is quantised, and the quantum is the multiplicative order of the base modulo the denominator.**

In full: For a fraction *k*/*q* in base *B*, the expansion repeats with period ord_*q*(*B*), and a reading of that length constitutes one complete rotation of the address. A reading taken at a length that is not a multiple of the period is a reading taken mid-rotation, and the value it returns is a property of the cut rather than of the object. For the sevenths in base ten, ord₇(10) = 6: six places is one rotation, and no shorter complete reading exists.

This is not a re-description. It is a constraint on what a quoted decimal means, and it is testable. Quote a
value at a depth that is not a multiple of the period, and the discrepancy
from the completed value is calculable in advance rather than attributable to
rounding.

**Two operations are available at a cut, and they are not interchangeable.** A reading terminated at a stated depth may either *discard* the remaining tail or *commit* to the nearer available value. These are different operations with different signatures.

| operation | the tail | sign | office |
|---|---|---|---|
| **truncation** | discarded | **one-signed** — the reading always falls short | the lossy read: what an instrument does when it stops reading |
| **rounding** | settled to the nearer value | **two-signed** — three up and three down per rotation | the commitment: what a system does when it must occupy a state |

Truncation can only subtract. Rounding can also restore, and does: the six sevenths sum exactly to 3; truncated at one rotation the sum reads 2.999997; **rounded, it returns exactly 3.** The three units truncation removed are the three units rounding gives back.

**The two agree except where the deciding digit is high, and that exception is structural.** Rounding at depth *d* is decided by the digit at depth *d*+1: below five the operations coincide, at five or above they diverge. For 1/7 in base ten the digits are 1, 4, 2, 8, 5, 7, so the deciders for
successive depths are that sequence shifted one place. Since the reptend's
halves are nine's complements, a low first half compels a high second half.** The operations therefore agree at depths 1, 2, 6, 7, 8 and differ at exactly 3, 4 and 5**.

**Theorem 5. Under rounding, the deviation of a reading from its exact value is periodic in the depth, and the period of its sign is the order of the base modulo the denominator.**

For 1/7 in base ten the sign sequence is − − + + + −, of period 6 = ord₇(10), with three positive and three negative depths per rotation — the same three-and-three division as the ledger below. Verified to depth 36 in exact rational arithmetic. This is what it means for the extent to be a dimensioned register rather than a free parameter: **a reading does not improve smoothly with depth. It improves in a cycle whose period is fixed by the address, and its sign is decided by the digit it stops before.**

**Theorem 6. Under truncation at one complete rotation, the residue of each complementary pair is exactly one unit of the final place, and the two members round in opposite directions.**

The demonstration, on the sevenths in base ten: Take the six sevenths in base ten, each truncated at one full rotation. The residue beyond the cut for *k*/7 is exactly *k*/7 units of the final place. Summing over the six rows gives 21/7 = 3 units exactly. The rows pair under *k* ↔ 7−*k*, and each pair carries a residue of

<div style="margin:6pt 0 6pt 12pt;"><i>k</i>/7 + (7−<i>k</i>)/7 = 1 unit of the final place, exactly, for every pair.</div>

Three pairs, one unit each, three units in total. The deficit is not a sum that happens to equal three; it is three closures each costing one.

**The direction of the rounding is determined, not assigned.** A row rounds up when its residue exceeds half a unit and down otherwise. The residue of row *k* is *k*/7, so the division falls between *k* = 3 and *k* = 4: rows 1, 2 and 3 round down and rows 4, 5 and 6 round up. Since the complementary pairs are (1,6), (2,5) and (3,4), **each pair contains exactly one row of each direction.** Every complementary pair is therefore signed, with one member displaced downward and one upward by amounts summing to a single unit. The signing is obtained from the arithmetic; nothing is imposed.

**The polarity is carried by the extent, and is exact at every extent.** The preceding ledger was computed at one rotation. Recomputing it at two, three and four rotations — twelve, eighteen and twenty-
four places — returns the same result in every particular. The total residue
is exactly 3 units of the final place, and each complementary pair carries
exactly 1. The direction word is down, down, down, up, up, up without
alteration.

| rotations | places read | total residue | residue per pair | direction word |
|---|---|---|---|---|
| 1 | 6 | 3 units | 1 unit | D D D U U U |
| 2 | 12 | 3 units | 1 unit | D D D U U U |
| 3 | 18 | 3 units | 1 unit | D D D U U U |
| 4 | 24 | 3 units | 1 unit | D D D U U U |

This is the sense in which the polarity belongs to the dimensioned register rather than to the value. The value of each seventh is fixed and carries no sign. The **extent** is a count, quantised by Theorem 4, and at every value of that count the sign structure is present, identical, and exact. A signed quantity has therefore been obtained from an unsigned one by reading it to a determined depth — and the sign does not drift with depth, which is what distinguishes it from an artefact of truncation.

The moments of the three pairs, measured as displacement from the half, are 5/14, 3/14 and 1/14 — an arithmetic sequence in odd numerators, decreasing toward the centre, so that the innermost pair is the most nearly balanced. The endpoints 0/7 and 7/7 are exact, carry no residue, and are unsigned.

What this establishes: **a positional expansion carries a determined extent, a determined cost of truncation, and a determined sign, none of which is present in the value alone.** What it does not establish is equally exact: none of this yields a magnitude. The value remains dimensionless and §2 is untouched. The extent and the traversal are counts, and a count is dimensioned by its
quantum rather than by a ruler. That is why no continuum enters through the
reading: the extent of a reading changes from one integer to another, and no
intermediate value is available to it.

**Condition of falsification.** The account requires, for every prime denominator and every base: that the residues of a complementary pair sum to exactly one unit of the final place, and that the two members round in opposite directions. Either condition failing at any pair terminates it. Both are decidable in a line of arithmetic.

*Machine checks: `verify/test_rotation_quantum.py`, `verify/test_path_length.py`.*


### 9.1 · Writing a reading so that it carries its own extent

The sections above establish that a reading has three registers and that only the first is a value. Ordinary notation records the first and discards the others, and this subsection sets out what recording them would look like. It is a proposal about notation, offered because the arithmetic it rests on is established above.

**The difficulty with the usual convention, and its scope.** Significant figures already carry an extent: 1.000000 asserts unity known to six places, where 1.0 asserts two. But the trailing zeros make a further assertion — **that the residue is zero** — and that assertion is warranted only when the quantity terminates in the base. For 1/2 or for unity itself it is correct and nothing is lost. **For a quantity that does not terminate — 1/7, 1/3, and every rational whose
denominator carries a prime outside the base — it is not**. By Theorem 6 the
reading always falls short by a determinate amount, and the notation records
that amount as zero.

The correction is therefore narrower than a general reform of notation. Ordinary decimal notation already carries the extent, since the digits can be counted. What it does not carry is **the residue**, and only for the non-terminating case is there a residue to carry.

**The proposal.** Write a reading terminated at depth *n* as *n* nines:

<div style="margin:4pt 0 8pt 14pt;">.9 &nbsp; .99 &nbsp; .999 &nbsp; … &nbsp; .999999 &nbsp; = &nbsp; 1 − 10<sup>−n</sup>, with <i>n</i> the extent</div>

**What this is exactly.** The form is not "unity truncated" — unity truncated at any depth is unity. It is **the largest value representable at depth *n* that lies below one**, and its residue is exactly one unit of the final place. That residue is one unit only for this form; a general reading leaves a *fraction* of a unit, as §9 computes for the sevenths, where row *k* leaves *k*/7.

The form names a specific object rather than reforming notation generally. It
is the upper bound of a register of depth n. It carries its extent by digit
count, and its residue is fixed at one unit rather than asserted to be zero.

**Three ones are in play here and they should be kept apart.**

| | register | extent | residue |
|---|---|---|---|
| the multiplicative identity | value | none | none — 1 × *a* = *a* for every *a* |
| the counting unit | count | none | none — one tallies with it and nothing is left |
| unity read at depth *n* | both | *n* places | exactly one unit of the final place |

The first two carry no extent; they are one numeral doing two jobs in two registers. **The third is not a third meaning of "one". It is what one looks like from inside a register of depth *n*, and the count is what dimensions it.** The value it approaches never moves. At depths 1, 3, 6 and 8 the residue is
one unit of place 1, 3, 6 and 8 respectively. The extent alone therefore does
the dimensioning, which is the sense in which §9 calls a count dimensioned
without breaching Theorem 1.

The distinction from the counting unit is the sharpest of the three. **One tallies with the counting unit and nothing is left over; a reading of unity always leaves exactly one unit.** The counting unit is complete and the read unit never is.

**It composes, and the composition is the useful part.** Multiplying two readings at depth *n* gives a deficit of two units of the final place, three readings give three, and so on to first order — so **error propagation becomes a count of digits rather than a separate calculation.** At depth 6: (.999999)² = 0.999998000001, deficit 2 units; (.999999)³ = 0.999997000003, deficit 3.

**The notation is the paper's own, and its objects have been in use throughout.** Six nines is the white ray of §11, and six is ord₇(10), one rotation of the
seed. The product 999999 = 7 × 142857 is the seed times its own repetend. And
.999999 + .000001 = 1 exactly, the two bounds of a six-place register closing
on unity.

**What this has to do with §7.** A structured numeral for *c* is worth having for the same reason. On the SI metre c = 299 792 458 = 2 · 7 · 73 · 293 339. Every computation
containing it drags a five-digit prime along. A truncated result therefore
carries a tail which is an artifact of the unit rather than a residue of
anything. On the proposed metre *c* = 2⁸ · 3 · 5⁸ terminates, and a truncated result carries only what the truncation actually cost. **A structured unit is one in which the ledger of §9 stays legible; an unstructured one buries it.** That, rather than the appearance of the numeral, is what the choice in §7 secures.


## 10 · The base, and what base-dependence does and does not show

The preceding section read a quantity in base ten and drew structural conclusions from what it found there. The standing objection to that procedure is worth stating at its strongest before it is answered, because it is the objection this paper will meet first and it is not a foolish one.

**The objection.** Base ten is a biological accident. Had we ten fingers on one hand the digits of 1/7 would differ, the period would differ, the ledger would read differently, and any structure found in the expansion is therefore structure in a notation rather than in the world. A result that moves when the base moves is an artifact of bookkeeping.

**The sorting, which settles most of it without argument.** The objection is decidable case by case, and the results divide sharply. Below, each is tested in every base under 101 satisfying the two conditions of the register theorem (§11.1) — bases 10, 19, 73 and 82:

| result | base 10 | base 19 | base 73 | base 82 | status |
|---|---|---|---|---|---|
| period of 1/7 is 6 | ✓ | ✓ | ✓ | ✓ | **base-free** |
| Midy halves complement to *B*−1 | ✓ | ✓ | ✓ | ✓ | **base-free** |
| residue of row *k* is *k*/7 of a unit | ✓ | ✓ | ✓ | ✓ | **base-free** |
| each complementary pair costs exactly 1 unit | ✓ | ✓ | ✓ | ✓ | **base-free** |
| three rows round up, three down | ✓ | ✓ | ✓ | ✓ | **base-free** |
| the digit string | 142857 | 2·13·10·16·5·8 | … | … | base-specific |
| *which* depths carry the positive sign | 3,4,5 | 1,2,3 | 3,4,5 | 1,2,3 | base-specific |
| ord₁₃₇(*B*) | 8 | 68 | 17 | 136 | base-specific |

**Every quantity the argument leans on is in the base-free half.** The period is 6 in any base where seven has full period, because full period *means* the period is *q*−1. The complementation is Midy's theorem, which holds in every base. The residue *k*/7 and the one-unit pair cost are statements about sevenths and carry no base at all. Even the three-and-three division of the rounding survives, because it follows from the complementation rather than from the digits.

What moves is the labelling: which particular numerals appear, and which particular depths carry the sign. **The counts are base-free and the labels are not** — and no claim in this paper rests on a label.

### 10.1 · The base as a position: the register theorem

That sorting is sufficient for the technical argument, and a reader who wants only the technical argument may stop here. The remainder of this section states the interpretive position the work is done under, because it is better stated than inferred.

**The demand for base-independence is itself a commitment, not a neutral standard.** It presupposes that a number is a *notation* — a way of writing down an object that exists prior to and independently of any way of writing it. On that view every base is equally arbitrary, none is distinguished, and structure appearing in one is an artifact by definition. This is a coherent position and it is the majority one. It is also a metaphysical claim about the existence of mathematical objects, and it is assumed rather than shown.

The position taken here is the other one: that counting is not a description
applied to a substrate but the substrate's own operation. On that view a base
is not a choice of notation but a property of the register in which the
counting happens. On that view the question is not *which base is arbitrary* but *which base a register would have*, and that question has an answer.

**The register theorem**, proved by finite scan, states it. Base ten is the
least base carrying both of the construction's mechanisms at once. The ennead
lives in digit sums, which requires B ≡ 1 (mod 9). The seed unrolls to full
period, which requires the base to be a primitive root modulo seven — that is,
ord₇(B) = 6, the period of 1/7 in base B reaching its maximum. *(Wording corrected 2026-08-21: this formerly read "requires seven to be a primitive root", which inverts the condition — it puts the requirement on seven modulo the base rather than on the base modulo seven. The two are genuinely different: in base 19 the seed unrolls to full period and seven is not a primitive root, while in base 46 the reverse holds and the seed's period collapses to three. The result is untouched, since both conditions single out ten as the least admissible base, which is why the slip never surfaced.)* Below one hundred only 10, 19, 73 and 82 satisfy both, and ten is the least. **The theorem is conditional and the condition is stated rather than smuggled:** given those two mechanisms, the base is determined; the mechanisms are the postulate's own content and are not derived from anything more primitive.

The exact form of the position is not "base ten is true". It is this: given a
register that counts, and given the two commitments this construction makes
about how it counts, ten is the least base that carries both. Results obtained
in it are results about that register.** A reader who rejects the commitments will reject the conclusion, and should**; a reader who accepts them cannot dismiss the results as notational, because on those commitments notation is not what a base is.

**What neither position licenses.** Nothing above permits reading significance into a numeral that carries none — the digits of a dimensioned constant remain what §4 said they were, an artifact of a definitional system, in any base whatever. The sorting is the discipline: state which side of the line a result falls on, and do not use the base-free results to defend the base-specific ones.



### 10.2 · The arithmetic of the carriers

The two conditions of the register theorem are congruences, and their joint solution is a pair of arithmetic progressions rather than a scattered list.

Seven has full period in base *B* precisely when *B* is a primitive root modulo 7. There are φ(6) = 2 such residues, namely 3 and 5, so the condition is **B ≡ 3 or 5 (mod 7)**. The ennead condition is **B ≡ 1 (mod 9)**. Since 7 and 9 are coprime, the Chinese Remainder Theorem gives the joint
solution modulo 63: B ≡ 10 or 19 (mod 63). The carriers are therefore exactly
10, 19, 73, 82, 136, 145, 199, 208, … — two progressions of common difference
63, of density 2/63 among the integers, verified by direct test to 400. **Ten is the least, and the structure of the set is closed-form rather than empirical.**

Midy's theorem supplies the rest without reference to any base: if 1/*q* has even period 2*h* in base *B*, the two halves of the repetend sum digitwise to *B* − 1. Two consequences follow that carry no base at all. A digit below *B*/2 has its complement above *B*/2, so **exactly half the rows round up and half round down — the three-and-three division of §9 is a theorem rather than a tally.** And for *q* = 7 the period is 6, which is even, so Midy applies in every carrier base without exception.

### 10.3 · The base as a register, and what a lossy reading actually loses

The objection of §10 can be put in information terms, and in that form it answers itself.

A base is not a label but a **register**: it fixes how much a single symbol carries and therefore how finely a reading resolves. A digit in base *B* carries log₂*B* bits, so one rotation of the sevenths costs about 19.9 bits in base ten, 25.5 in base nineteen and 37.1 in base seventy-three. The registers are genuinely different channels, and a higher base resolves the same object more finely.

**The loss is nevertheless the same.** Truncating at one full rotation, the residue of row *k* is *k*/7 of a unit of the final place — **in every carrier base**, though the unit itself is *B*⁻⁶ and therefore differs by orders of magnitude between them. In absolute terms row 1 loses 1.43 × 10⁻⁷ in base ten and 9.44 × 10⁻¹³ in base seventy-three. As a fraction of the resolution available, it loses exactly one seventh in both.

| | base 10 | base 19 | base 73 | base 82 |
|---|---|---|---|---|
| bits per rotation | 19.9 | 25.5 | 37.1 | 38.2 |
| unit of the final place | 10⁻⁶ | 19⁻⁶ | 73⁻⁶ | 82⁻⁶ |
| residue of row *k* | *k*/7 unit | *k*/7 unit | *k*/7 unit | *k*/7 unit |
| total over six rows | 3 units | 3 units | 3 units | 3 units |

**So the encoding changes and the fraction lost does not.** The absolute loss scales with the resolution; the relative loss is an invariant of seven. This is the same division the paper has drawn throughout — a value that does not move, and an extent that does — appearing here as the difference between what a register costs and what it discards.

The consequence for the objection is direct. **An observer that stops reading loses a determinate fraction of a unit, and that fraction is a property of the quantity being read rather than of the register reading it.** A lossy reading is therefore not an artifact of notation even though its digits are: the digits are the encoding, the loss is the arithmetic, and only the first depends on the base.


## 11 · A worked case: the coupling, the spine, and the nucleon

The preceding sections are about method. This one exhibits the method operating, because a claim that a framing recovers information is worth only what it recovers.


**The first case is hydrogen, because its spectrum is the paper's thesis in the most precisely measured object physics has.** The Rydberg formula

<div style="margin:4pt 0 8pt 14pt;">1/λ = <i>R</i> ( 1/<i>n</i>₁² − 1/<i>n</i>₂² )</div>

makes **every wavelength ratio of hydrogen a rational number**. The Rydberg constant is the single supplied scale; everything else is dimensionless structure. Hydrogen therefore sits entirely on the derivable side of Theorem 1, and its ratios are legitimate objects of structural investigation by §4's own criterion — while its absolute wavelengths are not.

Taking the Balmer series against its own series limit, λ_*n*/λ_∞ = *n*²/(*n*²−4):

| *n* | ratio | line | wavelength | prime content |
|---|---|---|---|---|
| 3 | 9/5 | Hα | 656.3 nm | 5-limit |
| 4 | **4/3** | Hβ | 486.1 nm | **3-smooth — the fourth** |
| 5 | 25/21 | Hγ | 434.0 nm | carries a 7 |
| 6 | **9/8** | Hδ | 410.2 nm | **3-smooth — the whole tone, 3²/2³** |
| 7 | 49/45 | — | 397.0 nm | carries a 7 |

**Theorem 7. In the entire Balmer series, exactly two members have 3-smooth ratios to the series limit, and both fall in the visible band.** The ratio *n*²/(*n*²−4) is 3-smooth only when *n*, *n*−2 and *n*+2 are simultaneously 3-smooth — that is, only where two 3-smooth pairs differing by 2 overlap at *n*. Those pairs are exactly (1,3), (2,4), (4,6), (6,8) and (16,18), a finite set, and two of them overlap only at *n* = 4 and *n* = 6. The result is exhaustive rather than sampled.

The observation this supports is not about hydrogen but about method. The same
series contains ratios of three different prime characters. Which of them a
framework can address is decided by that character rather than by the quality
of the measurement.** All five wavelengths above are known to more digits than any argument here requires**. What distinguishes them is arithmetic.


**The second case is the fine-structure constant and the proton**, and the point of it is that a single prime appears in both and in the length that relates them. The arithmetic is exact and is stated first.

<div style="margin:4pt 0 8pt 14pt;">
137 = 8 · 17 + 1<br>
459 = 3³ · 17 = 3⁷ − 12³<br>
1836 = 2² · 3³ · 17 = 4 · 459
</div>

The integer 1836 is the proton-to-electron mass ratio to the nearest whole
number. The integer 137 is the reciprocal of the electromagnetic coupling to
the nearest whole number; 137 is the reciprocal of the electromagnetic coupling to the nearest whole number. **These are ordinarily unrelated quantities, measured independently and explained by nothing.** In the factorisations above they share the prime 17, and the number 459 that carries it appears in both a power identity in 3 and 12 and in the mass ratio as one quarter of it.

The length that uses both is the proton charge radius, expressed as a pure ratio to the classical electron radius:

```
   r_e / r_p  =  459 α        ⟹        r_p  =  0.84131 fm
```

The current experimental value is 0.8409 ± 0.0004 fm. The relation is dimensionless on both sides, so by §6 it is invariant under every choice of unit, and the comparison is the same in every system.

**What this exhibits.** The identities in 17 are arithmetic and are checked in a line. The radius relation is the framework's, it is parameter-free, and it stands about one standard deviation above the present determination. It is a use of the method rather than a proof of it. The method's content is
that dimensionless quantities are the objects in which structure may be
sought. Here two of them turn out to share a factor, while a third relates
them numerically.


**The third case is a convention rather than a constant, and it is included because it is the clearest instance in the paper of the failure mode §5 describes.**

Newton divided the visible spectrum into seven colours. He chose seven to match the seven notes of the diatonic scale, and said so. The division has been inherited for three centuries, and the boundaries between its bands have never been made sharp — not for want of instrumentation, but because there are no boundaries there to sharpen.

Trichromatic vision has three channels. Three channels, each present or absent, admit 2³ = 8 states. Removing the null state leaves seven, of which three are single channels, three are pairs, and one is the whole:

| state | channels | what it is |
|---|---|---|
| 001, 010, 100 | one each | the three primaries |
| 011, 101, 110 | two each | the three secondaries |
| 111 | all three | white |
| 000 | none | black |

**Hue is therefore not a partition of a frequency continuum into bands. It is the state space of a three-channel system** — six states with two bounds, not seven regions. Complementary pairs are bitwise complements: each primary pairs with the secondary formed from the other two, and each pair sums to the whole. That the count is seven is correct; that it is a division of the spectrum is not.

The parallel with §5 is exact. In both cases a quantity was fixed for a reason external to its structure — a
musical analogy in one, a meridian survey in the other. In both cases the
fixing was never revisited, because nothing depended on revisiting it. **The numeral survived the reason for it.** That is the condition this paper is written to identify, and colour is the case where it can be seen without any apparatus at all.


**The seventh, and why the framework's generator is dimensionless.** The framework's generating object is the set of sevenths in base ten, and its selection is not free: seven is the least prime whose reciprocal has a full period in base ten, ord₇(10) = 6 = 7 − 1. Every ratio built on it is dimensionless by construction and therefore lies on the derivable side of §2. The sevenths supply structure; they supply no magnitude, and §9's registers are where their extent and traversal are counted. A framework whose generator is dimensionless is one whose entire derivable content is on the left of the line in §2 — which is what makes the single supplied reference of §3 both necessary and sufficient.


## 12 · The placement criterion

§§3, 8 and 9 together determine the placement of the single reference:

**Definition. The reference is placed on a quantity defined at the zero-probe limit, whose dimensionless surroundings are structural rather than measured.**

Applied to the standing candidates, the criterion selects:

| candidate | what the number is | class | admissible |
|---|---|---|---|
| **proton charge radius** | slope of the form factor as *Q*² → 0 | defined at the zero-probe limit | **yes**, by definition |
| **carbon-12 mass unit** | one twelfth of a twelve-nucleon nuclide | a cardinality, not a reading | **yes**, by construction |
| caesium-133 hyperfine frequency | transition frequency in a dressed atom | reading under stated conditions | no |
| Planck mass | √(ħ*c*/*G*) | a computation, not a reading; conventional to √(2π) | no |
| strong-interaction scale | where the coupling reaches unity | reading, and scheme-dependent | no |
| iron-56 | terminus of stellar fusion | satisfies no criterion; corroborating | no |

The preceding sections enter this table as follows. §3 fixes that exactly one
row may be used. §4 establishes that the rows are one input in several
presentations rather than six inputs. §5 identifies which row the operative
system presently uses. §8 supplies the class column, which is the column that
decides, and §2 guarantees that no row can be dispensed with.

The individual determinations follow.

**The proton charge radius satisfies the criterion by definition.** The radius is the slope of the electric form factor as *Q*² → 0. No finite-*Q*² determination returns it; each returns the form factor at that *Q*². The radius is obtained by measurement across a range of momentum transfers followed by extrapolation to zero, that is, by calculation from readings rather than by a reading. Anchoring on it places the reference on the class of dimensionful magnitude that does not transmit the characteristics of the apparatus. Combined with a small set of dimensionless ratios, one such length determines absolute magnitudes across the atomic domain.

**The Planck mass fails the criterion three times over.** It is constructed from a dimensionful constant, which the table records. The construction is conventional to a factor of √(2π): the modern definition uses ħ where Planck's own units of 1899 used *h*, so the quantity named is one of a pair 2.5066 apart, and nothing in physics selects between them. It is a computation rather than a reading, since no determination of it exists
apart from the constants it is assembled from. Because ħ and c are exact, its
entire uncertainty is the 22 parts per million of G, the least-determined
constant in the tables. An object of the third class of §6.1 cannot carry the reference, whatever its exponents.

**The caesium-133 hyperfine frequency does not satisfy it.** It is the frequency of a transition in an atom subject to field, temperature and pressure conditions, and is exact at present only by stipulation. Its selection in 1967 followed from reproducibility under laboratory control, which is a metrological criterion and not a structural one. The numeral itself is not at issue. What is at issue is its class: it is a reading elevated to a definition, and a reading is the wrong class of object to carry a theory's reference when a zero-probe quantity is available.

**Carbon-12 satisfies the criterion in the second manner: it is not a reading.** Six protons, six neutrons and six electrons constitute a nuclide balanced in three registers, the most symmetric of the light nuclei, and correspondingly the natural object of a counting unit. Its twelve is a count of constituents; the mass unit is one constituent's share. The operation is division by twelve, not extraction of a twelfth root, and involves no subdivision of an interval and no temperament. Expressed in the unit of the object itself, **one kilogram is 5.0185 × 10²⁵ atoms of carbon-12** — the unit stated as a cardinality, which is the form §9 identifies as dimensioned by its own quantum.

**Iron-56 satisfies no criterion in this paper and is included because it is frequently proposed.** Iron-56 marks the terminus of stellar fusion. The process is exoergic up to
this region of the chart and endoergic beyond it. A stellar core therefore
accumulates material at the iron peak and proceeds no further by that
mechanism, every heavier nuclide arising by other processes. It is correspondingly the most abundant nuclide in the region, and in the arithmetic under discussion it factors as 8 × 7 = 2³ × 7. None of this makes it a zero-probe quantity, and it is therefore not admissible as the reference.

The required exactness on the accompanying claim: **the maximum of binding energy per nucleon belongs to nickel-62, not to iron-56**, which lies slightly below it. The two statements are independent and both hold. Nickel-62 is the most tightly bound nuclide; iron-56 is where material accumulates, silicon burning proceeding through nickel-56, which is doubly magic and alpha-conjugate and which decays to iron-56. Iron's position is a fact about the pathway of nucleosynthesis; nickel's is a fact about the binding curve. The description "iron is the binding peak" conflates them and is not used here.

None of these placements crosses the boundary of §2. Anchoring at the proton radius or at carbon-12 determines no magnitude; it places the single required reference on an object whose definition is structural rather than procedural.

## 12b · Addendum: the gravitational constant, revisited

This paper names *G* three times as the tables' least-determined constant: twenty-two
parts per million, with published determinations disagreeing beyond their stated
uncertainties, and the entire uncertainty of every Planck computation. The companion volume derives the dimensionless gravitational coupling of the
electron as the repeating binary fraction αG(e) = 5/(2¹⁵¹ − 1), the five
circulating on a wheel whose period is Φ₁₅(2) = 151. It converts that through
the exact stipulations ℏ and c, together with one reading — the electron mass
at 0.31 parts per million — to

```
G  =  6.6735902(41) × 10⁻¹¹  m³ kg⁻¹ s⁻²
```

one hundred and six parts per million below the CODATA-2018 central value and inside
the experimental discordance. Three consequences belong in this paper's terms. First,
the discipline is exactly the one legislated here: the pure number is derived, no
dimensionless construction yields any magnitude, and the single supplied reference
enters once, openly, as §3 requires. Second, the classes of §6.1 gain their missing case: a computation that can be
checked. G has until now been a reading with no second route. The companion
supplies one, which takes a side in the standing disagreement among the
readings. Third, if the value stands, the leverage of the tables inverts. The least-
determined constant becomes determinate to under a part per million, and the
Planck computations' uncertainty collapses from the twenty-two parts per
million of G to the 0.31 of the electron mass. Everything §12 concludes about
them is unchanged: the Planck mass remains a computation, conventional to
√(2π), and still cannot carry the reference. The verification of the
companion's exact claims is machine-checked in `verify/test_decimal_wheel.py`.

The same day closed the trilogy. Its third volume, The Vacuum on Discrete
Terms, runs §3's argument in the time sector. The theory's dimensionless
content is invariant under time translation, which is a one-parameter group.
The number of external epoch references a theory requires is therefore
likewise exactly one, and no dimensionless construction can supply it. The present epoch enters that volume once, as the
electron mass enters the gravity companion once. The reference theorem now has its
sibling, and the two sectors' external references are counted by the same proof.

## 13 · Prohibitions

Six consequences follow. Each is stated as a prohibition, with the condition under which it would not hold.

**No dimensionful constant is derivable from dimensionless structure alone.** The failure of any such derivation is locatable by dimensional analysis: a magnitude has entered without acknowledgement. The gravitational constant is the standing instance.

**No theory requires zero measured references**, by §3. A theory of pure ratio describes a system possessing no scale.

**No theory requires two independent measured references**, by the same argument. Where a framework appears to require two, one is determined by the other through structure not yet identified.

**No numerical disagreement is removable by a choice of unit**, by §6.

**No complete positional reading of a rational number is available at a length
that is not a multiple of the period of its address, by §9**. Within one such
reading, the residues of a complementary pair sum to exactly one unit of the
final place, with the two members oppositely signed. Any counterexample refutes §9 in a line.

**No comparison in which a constant's exponents cancel between the defining expression and the reporting unit constrains that constant**, by §6.1; and no computation constitutes a determination, there being no second value against which to check it. A null obtained through a cancelled channel is a property of the channel and not of the world. The condition under which the first statement would fail is an exponent
mismatch, decidable by inspection of the two expressions. The standing
cancelled channels — every angular comparison in arcseconds, and the
electromagnetic sector of 1948–2019 — are identified in §6.1.

One statement is not a consequence, and is set out because the boundary is frequently extended to cover it. Where the dimensionless ratios hold, a single reference determines absolute magnitudes throughout the system, and a framework supplying one reference is not thereby indifferent to magnitude. A failed prediction within such a system constitutes a failure of ratio on the framework's own ground, and the boundary has no bearing on it. Invoking the dimensional boundary to account for a failed prediction is a category error.

## 14 · Conclusion

The two constituents of a physical quantity are objects of different kinds. The numerical constituent is structure: derivable, checkable, refutable. The reference constituent is supplied: relocatable, placeable well or badly, and not reducible below one nor substitutable for structure.

The traditional account of the asymmetry is correct as far as it extends. A number carries no ruler, because arithmetic is symmetric under rescaling and nothing in it selects a magnitude. What the traditional account omits is that a numeral is not exhausted by its
value. The reading of one carries an extent and a traversal. Both are counts,
both are quantised by the address rather than by a ruler, and both carry
determinations — of cost, of sign, of completeness — that the value alone does
not. That is the precision the abstract framing forgoes, and it is recoverable without disturbing anything above it.

The placement of the required reference is likewise determined rather than preferential, because measured quantities are not interchangeable. Some are defined at the zero-probe limit; others are readings constituted under conditions; only the first class carries a reference without transmitting an apparatus. The distinction does three things. It identifies which constants are
legitimate objects of structural investigation and which are artifacts of a
definitional system. It establishes that no disagreement is a units problem.
And it locates the boundary of any dimensionless programme in terms that
programme is able to state.

A unit is not bookkeeping. It is the single point at which a physical theory admits a quantity that its structure does not determine — and the only such point, once the count is fixed at one.


*Machine-verified as follows. The one-parameter reduction and the rescaling
invariance are in `verify/test_semitone_seam.py`. The cancellation identities,
the exponent table, the Planck convention factor and the 2019 class rotation
of §6.1 are in `verify/test_leverage.py`. The rotation quantum and the
truncation ledger are in `verify/test_rotation_quantum.py`, and the register
decomposition in `verify/test_path_length.py`. The identities 459 = 3³·17 = 3⁷
− 12³ and 4·459 = 1836 are in the first of these. The boundary of §2 and the count of §3 are proved rather than computed. The 2019 SI values (§5), the running of the electromagnetic coupling (§8) and the nucleosynthesis pathway (§12) are standard results. The batteries and this paper's source are public at github.com/thefirsthorstmann/g-theory-verify.*

*Companions: Gravity on Discrete Terms (the coupling this paper's §12b
places; doi.org/10.5281/zenodo.22087600) · The Vacuum on Discrete Terms
(doi.org/10.5281/zenodo.22119288) and Motion on Discrete Terms
(doi.org/10.5281/zenodo.22119337) · The Origin on
Discrete Terms (the figure; doi.org/10.5281/zenodo.22119129).*

<div class="copyright" style="margin-top:80pt">Copyright<br>Christian Horstmann · August 25th, 2026<br>thefirsthorstmann@gmail.com<br>All rights reserved</div>
