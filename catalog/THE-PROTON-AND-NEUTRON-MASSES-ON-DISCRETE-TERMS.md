%%TITLE: The Proton and Neutron Masses on Discrete Terms
%%SUBTITLE: The six-digit seats derived, the residuals beyond them read as the elapsed epoch, and the ratio of the two excesses at 23/32.
%%META: Christian Horstmann · thefirsthorstmann@gmail.com · September 1st, 2026 · manuscript for the public record
%%ABSTRACT: The proton and neutron masses, in unified atomic mass units, are measured to eleven digits, and no accepted framework derives their values. The fine-structure constant's best determinations agree through 137.035999 and disagree at the next digit. The program derives six-digit statements for all three quantities — 1.00728, 1.00866, and 137.036 — and, through the bridge, the six-decimal value 137.035999, on which every determination agrees. That agreement is the license: only because the seats are derived are the residuals beyond them defined objects — this paper's subject. Three arithmetic identities organize the system. The multiplier 28 connecting 0.036 to 1.008 is the triangular number T(7), and the base 1008 is the product of T(7) and T(8). The unit's carbon fraction 1/126 is the difference of the adjacent unit fractions 1/28 and 1/36. The measured residuals satisfy a proton-to-neutron ratio of 23/32 to two parts in ten thousand — the only fraction with denominator at most 64 within three standard deviations. A seating temperature of one sixth of the proton mass is proposed, 156.38 MeV against the lattice crossover 156.5(15). The count from seating to the microwave background is 39.28 octaves. A deposition mechanism carrying this count is stated as a hypothesis, and under it the masses are epoch-dependent. Deposition continues today: the nucleon masses grow near one part in ten to the seventeenth per year, just beneath current bounds on the proton-to-electron drift. Excluded variants are listed, and the implied fine-structure values are registered against the current experimental discrepancy.
%%

---

<div style="page-break-before:always"></div>

## 1 · Introduction

The 2022 CODATA adjustment gives the proton mass as 1.0072764665789 unified atomic mass units, with a relative uncertainty near eight parts in a trillion [1]. The neutron mass is 1.00866491595 u, known to about five parts in ten billion. No accepted framework derives either value. Lattice quantum chromodynamics computes the nucleon masses from measured couplings at the percent level, which is an achievement of a different kind: it verifies the theory's consistency without explaining why the numbers are these numbers.

The fine-structure constant presents a sharper situation. Its two leading atom-interferometry determinations disagree: rubidium recoil at Paris gives an inverse constant of 137.035999206(11) [2], caesium recoil at Berkeley gives 137.035999046(27) [3], a separation of more than five standard deviations that has stood since 2020. The electron magnetic-moment route gives 137.035999166(15) [4]. All determinations, including every CODATA recommendation of the past fifteen years, agree through 137.035999 and part company at the next digit.

A third measured quantity enters below. Lattice computations place the crossover temperature of quantum chromodynamics, at which quarks bind into hadrons, at 156.5 MeV with an uncertainty of 1.5 MeV [5]. The temperature of the cosmic microwave background is 2.72548 K with uncertainty 0.00057 K [6].

The history of formulae for constants is largely a history of failure, and the anatomy of the failures is known: a formula tuned to the measured decimal, announced after the measurement, and adjusted when the measurement moved. The discipline of this paper is the opposite and is stated up front. Every arithmetic identity below is exact and displayed. Every numerical scan is reported in full, including its misses. Every proposed mechanism is labeled a hypothesis, every excluded variant is listed with the size of its failure, and every implied value is registered before the experiments that will judge it have resolved. The registry of record for this program's predictions is its published falsification schedule and prediction registry [7]; the values registered here enter that registry at its next version.

This paper is part of a series that works on discrete terms. The fine-structure seat 137.036 is derived in the published companion [9]; the mass seats are derived by the construction stated in Section 4 and pinned in the accompanying batteries. The residual is a defined object only because its seat is derived, and that is what permits any statement about the region beyond the sixth decimal. The present paper can nevertheless be read alone. Its claims divide into three kinds, and each is labeled where it is made. Exact arithmetic can be verified by hand. Measured concurrences are stated with uncertainties and with the scans that produced them. The one mechanism is stated as a hypothesis with its refutation conditions.

## 2 · The masses and their unit: a short history

The statement this paper makes is unusual, and the reader should be able to weigh it without leaving the page. This section supplies the chain of custody: where the two mass values come from, where their unit comes from, and why that unit is native to the present construction rather than borrowed from convention.

The proton's mass entered physics through the charge-to-mass ratio of hydrogen ions; the neutron's followed Chadwick's identification of the particle in 1932. Aston's mass spectrograph turned atomic masses into a precision subject, and his whole-number rule — the masses are nearly integers — is the crude ancestor of the seat structure studied here. The modern values are Penning-trap results: a single ion's cyclotron frequency is compared with that of a reference ion, so what is measured, at parts per trillion, is a mass ratio. The neutron, carrying no charge, is reached through the deuteron: its mass follows from the deuteron's mass and binding energy. The precision objects of this subject have therefore always been ratios, never masses in kilograms.

The unit has its own history, and it is a history of choosing a reference. Dalton set hydrogen at one; the nineteenth century moved to oxygen at sixteen; the discovery of the oxygen isotopes in 1929 split the scale in two, chemistry holding to natural oxygen while physics took the lightest isotope. The 1961 unification resolved the divergence by placing carbon-12 at twelve exactly — chosen in part because carbon serves mass spectrometry so well, supplying reference doublets across the table. Since the 2019 revision of the SI the kilogram is fixed through the Planck constant and the unified unit remains a measured quantity; but nothing in this paper touches the kilogram. Every mass here is a ratio to carbon-12, and those ratios are the eleven-digit objects.

Within this construction the unit is more than a well-chosen convention. Identity 3 of Section 5 places the free nucleon's excess over the unit at one part in 126 at seat. And 1/126 is the difference of the unit fractions 1/28 and 1/36 — the same pair that builds the base and the bridge. The unit's defining substance sits inside the arithmetic that the seats themselves come from. Expressing the masses in unified atomic mass units is therefore not an imported choice; it is the register in which the construction's statements become visible. The honest converse is also stated: the seats are statements in this unit and in base ten, and in other units they do not appear. What is claimed is claimed about measured ratios to carbon-12 — convention-free physical quantities — organized in the unit the construction derives.

The chain of the paper is then closed on its own pages: measured ratios with their history above, seats derived in Section 4, residuals defined by the license of Section 1, and a mechanism proposed for them in Section 8.

## 3 · Terminology

**The seat.** A short exact rational or six-digit decimal statement against which a measured value is compared. The seats used here are 1.00728, 1.00866, 1.00800, and 137.036. The word marks a comparison point, not a claim of mechanism.

**The residual.** The signed difference between a measured value and its seat, quoted in the natural place of the seat's last digits.

**The turn.** Six decimal digits. The reciprocal of seven has period six, and the six-digit statements above each occupy one turn. The companion papers develop this structure [9, 10].

**Triangular numbers and unit fractions.** T(n) = n(n+1)/2, and c(n) = 2/(n(n+1)) is its reciprocal, so that T(n)·c(n) = 1. The pair (T(7), T(8)) = (28, 36) appears throughout.

**The syntonic comma.** The ratio 81/80, the standard comma of just intonation, with excess 1/80 = 0.0125.

**The reflection.** The published tonal-function paper proves that reflecting the diatonic ring through the axis between the tonic and the dominant exchanges dominant and subdominant: the two are one object in two orientations [8]. That theorem is used here as proved there.

**The borrow in flight.** The published fine-structure paper reads the run of nines in 137.035999 as the borrow of a displacement in flight — an operation in progress rather than a stored quantity [9]. That reading is used here as published there.

## 4 · The seat system

The three measured quantities, against their seats:

| quantity | seat | measured (CODATA-22) | residual |
|---|---|---|---|
| proton mass (u) | 1.00728 = 1.00800 − 0.00072 | 1.0072764665789(83) | −3.53 ppm of the mass |
| neutron mass (u) | 1.00866 = 1.00800 + 0.00066 | 1.00866491595(49) | +4.87 ppm |
| inverse fine-structure constant | 137.036 | 137.035999177(21) | −6.0 parts per billion |

The seats are derived, not fitted, and the derivations are laid out here so that the paper is anchored on its own pages.

**The offsets.** Call 6k a station of the six-ladder. A station above the sixth octave 64 has a superparticular step exactly when 6k − 64 divides 64, and this has three solutions: 66, with step 33/32; 72, with step 9/8; and 96, with step 3/2. The third is the dominant's own degree, occupied by the frame itself, so the available pair is 66 and 72 — consecutive stations, their difference the ladder's unit, their ratio 12/11. The proton takes the larger offset below the base and the neutron the smaller above it. The signs are forced by the lightest atom: a proton heavier than the neutron would leave hydrogen unstable and no atom standing.

**The base.** The base is the product of the adjacent triangular numbers at the seed pair, 1008 = T(7) × T(8) = 28 × 36 (Identity 2 below). The selection of seven as the seed is the foundation of the series and is derived in the companions [9]; within this paper it is the one stated input.

**The fine-structure seat.** The primes whose reciprocals have base-ten period eight are exactly the prime divisors of 10⁴ + 1 = 73 × 137, and there are two. The prime 73 partitions its nonzero residues into nine cyclic classes; the prime 137 into seventeen. The companion paper assigns the seventeen-class prime to the electromagnetic office [9], and its integer is 137. The tail then follows from the bridge with no further choice: 1.008 divided by 28 is 0.036 exactly, which is T(8)/1000. Given the base, the bridge forces the tail; given the tail, it forces the base. One statement stands free, and two seats follow.

Every selection in this section is pinned in the batteries accompanying this record.

Three further structural facts about these seats are exact.

First, the two mass seats are one base with two offsets: 100800 − 72 and 100800 + 66, in units of one part in one hundred thousand. The offsets over the sixth power of two are the superparticular steps 72/64 = 9/8 and 66/64 = 33/32.

Second, the two kinds of seat split differently. The mass seats split arithmetically, base plus or minus offset, and the subtraction's borrow crosses the digit boundary: 100728 begins 1007, not 1008. The fine-structure seat splits positionally, at its midpoint: 137 | 036, three digits and three digits. An arithmetic split stores an address. A positional split at the half is the signature of a reciprocal in motion, which is the structure the borrow-in-flight reading describes [9]. The distinction between the two grammars carries the interpretation in Section 9.

Third, the weight of the table must be stated honestly, because it falls in different places for the two kinds of row. A five-decimal statement always sits within five parts per million of any mass, and both mass seats are the nearest five-decimal roundings. The agreement column therefore carries no evidence for the masses; the derivation above carries all of it. The fine-structure row is different in kind. Its residual is 0.0008 of the seat's own last digit — a depth of one part in twelve hundred, which no rounding provides. The residuals, not the seats, are the subject of this paper.

## 5 · Four exact identities

The following are arithmetic. Each can be checked by hand in one line.

**Identity 1 (the bridge).** The multiplier connecting the fine-structure tail to the mass base is the seventh triangular number:

```
0.036 × 28 = 1.008        28 = T(7)        36 = T(8)
```

**Identity 2 (the base).** The mass base is the product of the two adjacent triangular numbers:

```
1008 = 28 × 36 = T(7) × T(8)
```

**Identity 3 (the carbon fraction).** The seat form of the nucleon average, 1.008 = 126/125, places the free-nucleon excess over the unified mass unit at one part in 126, and

```
1/28 − 1/36 = c(7) − c(8) = 1/126
```

so the unit's carbon fraction is the gap between the adjacent unit fractions at the bridge. Because the unified unit is defined through carbon-12, this identity has a physical restatement: at seat level, the nuclear binding of carbon-12 less its electron masses is 12/125 = 0.096 u. The measured value, computable from the mass table alone, is 0.09565 u, which is 0.37 percent below the seat statement.

**Identity 4 (the tail's composition).** The fine-structure tail seat is one bridge fraction multiplied by the carbon step:

```
9/250 = 0.036 = (1/28) × (126/125)
```

These four identities close on one another: the bridge, the base, the unit, and the tail are four presentations of the pair (28, 36). None of them involves a measured quantity.

## 6 · The two residuals and the ratio 23/32

Write the mass residuals as offset displacements, in units of one part in one hundred thousand: the measured proton offset is 72 + Δp and the measured neutron offset is 66 + Δn. The 2022 values give

```
Δp = 0.3533421(8)          Δn = 0.4915950(490)
```

Both displacements are positive: each offset exceeds its seat. Their ratio is the central measured fact of this paper:

```
Δp / Δn = 0.718767(72)          23/32 = 0.718750          difference: +0.2 σ
```

**Result (uniqueness of the fraction).** Among all reduced fractions with denominator at most 64, exactly one lies within three standard deviations of the measured ratio, and it is 23/32. The scan is exhaustive and the battery accompanying this paper re-runs it mechanically. The window admits about half a fraction on average, so uniqueness alone is close to a fair coin. The content is the proximity, at one fifth of a standard deviation, and the closure of the parts on the rung: 23 + 9 = 32. The fraction's parts close on the denominator: 23 + 9 = 32, with 32 the fifth power of two and 9 the square of three.

The composite consequence is immediate. The average nucleon's residual below 1.00797, the tightest row of the system at +0.69 ppm, equals half the difference of the two displacements; the neutron-minus-proton splitting's residual equals their sum. One pair of numbers carries the family.

The ratio is registered here as a constant: its refutation condition is a future neutron-mass determination that moves Δp/Δn away from 23/32 by more than three of its then-current standard deviations.

## 7 · The seating temperature

**Result (with its scan).** Dividing the proton mass by the integers two through twelve and comparing against the lattice crossover temperature of 156.5(15) MeV [5] gives one concurrence:

| divisor | m_p/d (MeV) | distance from the lattice value |
|---|---|---|
| 4 | 234.57 | +52 σ |
| 5 | 187.65 | +21 σ |
| **6** | **156.38** | **−0.1 σ** |
| 7 | 134.04 | −15 σ |
| 8 | 117.28 | −26 σ |

The divisors two, three, and nine through twelve miss by larger margins and are listed in the accompanying battery. The spacing of the candidates near the lattice value is about 22 MeV against an uncertainty of 1.5 MeV, so the probability of a chance concurrence this close is near one and a half percent for the stated scan. Widening the family to the neutron and the average roughly triples the trials and raises the chance toward four percent. The neutron's own sixth part lands at 156.59 MeV, inside the same window, so the statement concerns the nucleon scale rather than the proton specifically. The divisor six is not arbitrary within the program. Six is the period of the reciprocal of seven and the number of digits in one turn, and c(3) = 1/6 is the unit fraction at the third rung. In that language the statement reads: the hadrons seat when the ambient temperature falls to one c(3) of the proton's own mass.

**The count.** With the seating temperature m_p/6 and the microwave-background temperature 2.72548(57) K [6], the elapsed interval is

```
N = log₂( (m_p/6) / kT_CMB ) = 39.2764 octaves
```

The count is a ratio of two energies and is therefore a pure number; no unit survives into it. Its uncertainty from the background temperature is three parts in ten thousand of one octave. Its refutation condition is the lattice value: if the crossover temperature leaves the interval from 153 to 160 MeV, the seating statement fails.

## 8 · The deposition mechanism

**Hypothesis.** The following mechanism is proposed for the origin of the two displacements. It is stated in the program's own terms, its quantitative consequences are compared with measurement, and its excluded variants are listed in Section 9.

The seat structure has period six: six whole-tone steps of 9/8 span one octave, since (9/8)⁶ = 2 × 531441/524288, and the six degrees of the diatonic ring each reseat once per octave. Carrying a just major sixth through one reseating misses the three-limit target by exactly the syntonic comma 81/80. The hypothesis is that each seated object receives this miss once per octave of cooling, at its own degree's reseating. The displacements are then the accumulated receipts across the N = 39.28 octaves since seating.

Three structural clauses complete the mechanism, each resting on a published or exact foundation.

**The partition.** At each receipt, the deposit divides in the proportion 23 to 9 on the grid of 32. The retained part seats; the part 9/32 crosses the reflection. The proton, whose offset 72 is three times 24 and whose two-digit pair reverses to a different pair, sits on the dominant degree and possesses the reflection partner proved in the tonal-function paper: the subdominant, ratio 4/3 [8]. The transferred fraction crosses that exchange. This clause is the content of the measured ratio 23/32 of Section 6.

**The axis.** The neutron's offset 66 is a palindrome: it is invariant under digit reversal, and its seat is the doubled center of the system's scalar ladder. An object on the reflection axis is its own mirror image; it possesses no partner, and no fraction of its receipts can cross. The neutron therefore retains everything, which is why Δn carries the full count and Δp carries 23/32 of it. The same conclusion follows twice more: from the reversal-invariance of 66, and from the schedule below.

**The schedule.** The period-six structure carries two hands — the dominant-side and subdominant-side readings — and the convergents of the logarithm of three base two alternate sides strictly, which forces the alternating read. The two hands coincide twice per rotation: on the axis, and at the antipode. The antipode of a nine-point ring is empty, nine being odd, a fact the gravitational companion establishes independently [10]. Exactly one coincidence finds an occupant. The axis object is touched at that coincidence, once per octave, and at a coincidence both orientations are present, so nothing can cross: the neutron's full retention follows from the schedule as well as from the palindrome.

**The quantitative state of the hypothesis, plainly.** With the count of Section 7, the per-octave deposit required by the neutron's displacement is 0.0125163(12), which exceeds the syntonic excess 1/80 by 0.131(10) percent. Equivalently: an exactly syntonic deposit requires a seating temperature of 162.0 MeV, which the lattice value excludes at 3.7 standard deviations. The discrepancy factor lies within one standard deviation of both 28/27 and 29/28, the two superparticular steps adjacent to the bridge number 28, and the present measurements cannot separate the pair. Three resolutions are possible: the lattice value moves; the seating sits one such step above m_p/6 for a reason not yet derived; or the deposit itself carries a real excess of this size. The lattice program's own sharpening will adjudicate. The ratio 23/32 is unaffected by this open factor, because a uniform deposit excess cancels in the ratio.

## 9 · The fine-structure side

The two grammars of Section 4 now do their work. The mass seats split arithmetically and store; the fine-structure seat splits at the Midy half and flows. The published reading of the run of nines as a borrow in flight [9] identifies the fine-structure residual as a current rather than a ledger, and this section treats it as one.

**The window.** Every determination of the inverse constant in the modern record — Berkeley 2018, the CODATA recommendations of 2010 through 2022, the magnetic-moment route of 2023, Paris 2020 — lies strictly inside the one-unit interval

```
137.035999  <  α⁻¹  <  137.036000
```

The entire experimental discrepancy occupies the last unit of the seat's own turn. This window is registered: a future determination outside it refutes the reading.

**The three depths.** The construction states the fine-structure constant at three depths, each deeper than the last. The first is the seat, 137.036, one turn. The second follows from the bridge and the measured masses alone:

```
0.036 × ( m̄ / 1.008 )  =  m̄ / 28  =  0.0359989533(1)
```

where m̄ is the measured nucleon average in u. This is an identity, not a fit. Read at the register's own six-digit depth, the image rounds to 137.035999 — exactly the prefix on which every determination of the past fifteen years agrees, with the experimental disagreement confined to what lies beyond. The six-decimal statement is therefore derived, from the mass table, and confirmed by every instrument's own testimony. The third depth is the full image, 137.0359989533(1): the unison row of any transport between the mass and fine-structure residuals, registered here under the name the mechanism gives it — the fine-structure value with no transport applied. Every current determination sits above it.

**The transported values.** If the mass residual and the fine-structure residual are related by a just-intonation interval r, in the natural currency of parts per million of their own seats, then each licensed interval implies a value of the constant. The implied values are exact consequences of the measured masses:

| interval r | implied α⁻¹ | nearest determination |
|---|---|---|
| 10/9 | 137.0359990579 | Berkeley, at +0.4 σ |
| 5/4 | 137.0359991626 | CODATA-22, at −0.7 σ |
| 9/7 | 137.0359991859 | CODATA-22, at +0.4 σ |
| 4/3 | 137.0359992149 | Paris, at +0.8 σ |

Each determination lies within one standard deviation of one licensed interval, and no interval satisfies two determinations at once. The correspondence is registered before the discrepancy resolves; when it resolves, the surviving experiment selects the interval. Two structural facts lean toward the rubidium side without deciding it. The transferred fraction of Section 8 crosses to the subdominant, whose ratio 4/3 is the Paris row. And the ratio of the total transferred displacement to the Paris deficit is 1.7412(241), within half a percent of 7/4. Under the caesium value neither quantity lands on a licensed ratio.

**The flight form.** Read as a standing current fed by the transferred flow, the fine-structure residual equals the flow rate times a transit duration τ. The bookkeeping gives τ/N as the reciprocal of the interval r above: three fifths of the elapsed count under the recommended value, four sevenths under Paris. A steady-state variant sets the standing content by the transfer rate against the object's own crossing fraction 3/64. It predicts a deficit of 0.7510(1) parts per million of the tail and is excluded by every determination at 3.4 standard deviations or more.

## 10 · The present epoch, and the drift

The count of Section 7 locates the present inside the mechanism. The elapsed 39.2764 octaves place the present 27.6 percent of the way through the fortieth octave since seating. The thirty-ninth receipt completed at redshift 0.21, about 2.6 billion years ago; the fortieth arrives when the universe has expanded by a further factor of 1.65, roughly seven billion years from now. The receipts are uniform in octaves and strongly non-uniform in elapsed time: the first landed about twenty microseconds after the origin, and the current one has been underway for billions of years. The companion monograph's seventh volume locates the present at the crest of the energy budget by an independent construction; the octave coordinate above is the mechanism's own and is stated beside it, not derived from it.

A continuing clock has a present-day rate, and the rate is testable. Today one octave of cooling elapses per H/ln 2, about 1.03 × 10⁻¹⁰ octaves per year at the program's registered Hubble value. The deposition therefore implies that the nucleon masses, in unified atomic mass units, are growing now: the neutron at 1.3 × 10⁻¹⁷ per year relative, the proton at 9 × 10⁻¹⁸, with the electron not participating. The best current bounds on the drift of the proton-to-electron mass ratio, from methanol lines and quasar absorption, sit near 1.6 × 10⁻¹⁷ per year. The implied drift lies just beneath present sensitivity, and one further generation of molecular-clock measurements decides it.

One further coordinate is recorded with its residual unclaimed. Cooling ends at the de Sitter temperature floor of the registered Hubble value, and the full run from seating to that floor is 138.9 octaves. The program's published horizon count is forty-two decades, which is 139.5 octaves. The two agree to half an octave in 139, and the present sits at 28 percent of the run: past the first quarter. The half-octave residual is stated and not assigned.

## 11 · Excluded variants

Each of the following was tested against the same data and fails at the stated size. They are listed so that they are not rediscovered.

1. Static closures of the displacements. No fraction of the two-three-seven web, no comma of the standard ladder, and no banked station matches Δp, Δn, their difference, or their sum, at the measured precision. The nearest candidate across four objects and 2,198 licensed fractions fails the smallest-performer rule outright.
2. The exactly syntonic deposit. Requires a seating temperature of 162.0 MeV; excluded by the lattice at 3.7 σ.
3. The compound (continuous-decay) transfer. The fitted decay constant per octave is 0.01785; the nearest licensed constants fail at 7 σ and beyond. The transfer is event-coincident or the law is wrong.
4. The share model, in which a fraction of the transferred flow lands on the axis. It reproduces the neutron's deposit excess as 1/768 to +0.3 σ, and then fails its own second consequence, the proton's displacement, at 565 σ.
5. The six-deposit steady state for the fine-structure current: excluded at ≥3.4 σ by every determination.
6. Exact integer receipt counts (28 and 39): excluded at 11 σ.

## 12 · Registered values and refutation conditions

1. The seating temperature: m_p/6 = 156.379 MeV. Refuted if the lattice crossover leaves [153, 160] MeV.
2. The elapsed count: 39.2764 octaves, a pure number, moving only with the two anchors.
3. The ratio of displacements: Δp/Δn = 23/32. Refuted by a future neutron mass more than three standard deviations away.
4. The window: every future determination of α⁻¹ falls in (137.035999, 137.036000).
5. The root: 137.0359989533(1), the untransported value; registered as the unison row, not as a prediction of the measured constant.
6. The interval correspondence of Section 9: the resolution of the present discrepancy selects one licensed interval; the paper leans toward 4/3 and 7/4, the rubidium side, for the structural reasons stated, and records that lean before the fact.
7. No epoch dependence of the ratio: 23/32 is a constant, and any secular drift of the ratio refutes the partition.
8. The living clock: the nucleon masses in u grow today at 1.3 × 10⁻¹⁷ per year (neutron) and 9 × 10⁻¹⁸ (proton), the electron not participating. A proton-to-electron drift bound tightening past 5 × 10⁻¹⁸ per year with no signal refutes the continuing deposition.

## 13 · Verification

Every exact identity, every scan, every exclusion, and every registered value in this paper is pinned by mechanical batteries: forty-nine tests in three files, written alongside the work. The full program suite of 2,770 tests was re-run green before this manuscript was composed. The batteries are public, together with this paper's source, at github.com/thefirsthorstmann/g-theory-verify, where the reader can re-derive every number in this paper from the CODATA table and the two published anchors.

*Companion volumes: Tonal Function on Discrete Terms (the reflection theorem; doi.org/10.5281/zenodo.22119146) · The Fine-Structure Constant on Discrete Terms (the seat 137.036 and the borrow in flight; doi.org/10.5281/zenodo.21211050) · Units on Discrete Terms (the dimensional boundary; doi.org/10.5281/zenodo.22119360) · Gravity on Discrete Terms (the empty antipode; doi.org/10.5281/zenodo.22087599) · G-Theory — The Origin on Discrete Terms (doi.org/10.5281/zenodo.21212112) · Predictions on Discrete Terms (the registry of record; doi.org/10.5281/zenodo.21206818).*

## References

[1] E. Tiesinga, P. J. Mohr, D. B. Newell, B. N. Taylor, CODATA recommended values of the fundamental physical constants: 2022, Rev. Mod. Phys. 97 (2025).

[2] L. Morel, Z. Yao, P. Cladé, S. Guellati-Khélifa, Determination of the fine-structure constant with an accuracy of 81 parts per trillion, Nature 588, 61 (2020).

[3] R. H. Parker, C. Yu, W. Zhong, B. Estey, H. Müller, Measurement of the fine-structure constant as a test of the Standard Model, Science 360, 191 (2018).

[4] X. Fan, T. G. Myers, B. A. D. Sukra, G. Gabrielse, Measurement of the electron magnetic moment, Phys. Rev. Lett. 130, 071801 (2023).

[5] HotQCD Collaboration (A. Bazavov et al.), Chiral crossover in QCD at zero and non-zero chemical potentials, Phys. Lett. B 795, 15 (2019).

[6] D. J. Fixsen, The temperature of the cosmic microwave background, Astrophys. J. 707, 916 (2009).

[7] C. Horstmann, Predictions on Discrete Terms, Zenodo (2026), DOI 10.5281/zenodo.21206818; and G-Theory — The Falsification Schedule, DOI 10.5281/zenodo.22119549.

[8] C. Horstmann, Tonal Function on Discrete Terms, Zenodo (2026), DOI 10.5281/zenodo.22119146.

[9] C. Horstmann, The Fine-Structure Constant on Discrete Terms, Zenodo (2026), DOI 10.5281/zenodo.21211050.

[10] C. Horstmann, Gravity on Discrete Terms, Zenodo (2026), DOI 10.5281/zenodo.22087599.
