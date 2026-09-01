%%TITLE: The Proton and Neutron Masses on Discrete Terms
%%SUBTITLE: The masses derived to six significant figures, the parts-per-million residuals epoch-dependent, and their ratio at 23/32 to a part in a million.
%%META: Christian Horstmann · thefirsthorstmann@gmail.com · September 1st, 2026 · manuscript for the public record
%%ABSTRACT: The proton and neutron masses, in unified atomic mass units, are measured to eleven and nine digits, and no accepted framework derives either value. The fine-structure constant's best determinations agree through 137.035999 and disagree at the next digit. The program derives six-digit statements for all three quantities — 1.00728, 1.00866, and 137.036 — and, through the bridge, the six-decimal value 137.035999, on which every determination agrees. That agreement is the license: only derived seats make the residuals beyond them defined objects — this paper's subject. Four exact identities organize the system: the multiplier 28 connecting 0.036 to 1.008 is the triangular number T(7), the base 1008 is T(7) × T(8), and the unit's carbon fraction 1/126 is the difference of 1/28 and 1/36. The measured residuals satisfy a proton-to-neutron ratio of 23/32 to better than one part in a million — the only fraction with denominator at most 64 within three standard deviations. A seating temperature of one sixth of the proton mass is proposed and compared against the lattice crossover determinations. The count from seating to the microwave background is 39.28 octaves. A deposition mechanism carrying this count is stated as a hypothesis, and under it the masses are epoch-dependent: the neutron rises, the proton falls, and between receipts both stand still. The implied history is registered against clock comparisons, quasar absorption, and primordial helium. Excluded variants are listed with the sizes of their failures. Every identity, scan, exclusion, and registered value is pinned by machine-checked batteries at github.com/thefirsthorstmann/g-theory-verify.
%%

---

<div style="page-break-before:always"></div>

## 1 · Introduction

The 2022 CODATA adjustment gives the proton mass as 1.0072764665789 unified atomic mass units, with a relative uncertainty near eight parts in a trillion [1]. The neutron mass is 1.00866491606 u, known to about four parts in ten billion. No accepted framework derives either value in full. Lattice quantum chromodynamics computes the nucleon scale at the percent level and the neutron-proton splitting ab initio, as a near-cancellation of quark-mass and electromagnetic terms [12]. That verifies the theory's consistency without deriving the measured digits, which is the region this paper works in.

The fine-structure constant presents a sharper situation. Its two leading atom-interferometry determinations disagree: rubidium recoil at Paris gives an inverse constant of 137.035999206(11) [2], caesium recoil at Berkeley gives 137.035999046(27) [3], a separation of more than five standard deviations that has stood since 2020. The electron magnetic-moment route gives 137.035999166(15) [4]. All determinations, including every CODATA recommendation of the past fifteen years, agree through 137.035999 and part company at the next digit.

A third measured quantity enters below. Lattice computations locate the chiral crossover of quantum chromodynamics — an analytic crossover, not a phase transition, so its temperature is definition-dependent — at 156.5(15) MeV by one principal determination [5] and 158.0(6) MeV by the other [13]. The temperature of the cosmic microwave background is 2.72548 K with uncertainty 0.00057 K [6].

The history of formulae for constants is largely a history of failure, and the anatomy of the failures is known: a formula tuned to the measured decimal, announced after the measurement, and adjusted when the measurement moved. Eddington's arithmetic for the integer 137 is the canonical case, and any construction touching that constant inherits the burden of the precedent; Section 3 surveys the record. The discipline of this paper is the opposite and is stated up front. Every arithmetic identity below is exact and displayed. Every numerical scan is reported in full, including its misses. Every proposed mechanism is labeled a hypothesis, every excluded variant is listed with the size of its failure, and every implied value is registered before the experiments that will judge it have resolved. The registry of record for this program's predictions is its published falsification schedule and prediction registry [7]; the values registered here enter that registry at its next version.

This paper is part of a series that works on discrete terms. The fine-structure seat 137.036 is derived in the published companion [9]; the mass seats are derived by the construction stated in Section 6 and pinned in the accompanying batteries. The residual is a defined object only because its seat is derived, and that is what permits any statement about the region beyond the sixth decimal. The present paper can nevertheless be read alone. Its claims divide into three kinds, and each is labeled where it is made. Exact arithmetic can be verified by hand. Measured concurrences are stated with uncertainties and with the scans that produced them. The one mechanism is stated as a hypothesis with its refutation conditions.

## 2 · The masses and their unit: a short history

The statement this paper makes is unusual, and the reader should be able to weigh it without leaving the page. This section supplies the chain of custody: where the two mass values come from, where their unit comes from, and why that unit is native to the present construction rather than borrowed from convention.

The proton's mass entered physics through the charge-to-mass ratio of hydrogen ions; the neutron's followed Chadwick's identification of the particle in 1932. Aston's mass spectrograph turned atomic masses into a precision subject, and his whole-number rule — the masses are nearly integers — is the crude ancestor of the seat structure studied here. The modern values are Penning-trap results: a single ion's cyclotron frequency is compared with that of a reference ion, so what is measured, at parts per trillion, is a mass ratio. The neutron, carrying no charge, is reached through the deuteron: its mass follows from the deuteron's mass and binding energy. The precision objects of this subject have therefore always been ratios, never masses in kilograms.

The unit has its own history, and it is a history of choosing a reference. Dalton set hydrogen at one; the nineteenth century moved to oxygen at sixteen; the discovery of the oxygen isotopes in 1929 split the scale in two, chemistry holding to natural oxygen while physics took the lightest isotope. The 1961 unification resolved the divergence by placing carbon-12 at twelve exactly — chosen in part because carbon serves mass spectrometry so well, supplying reference doublets across the table. Since the 2019 revision of the SI the kilogram is fixed through the Planck constant and the unified unit remains a measured quantity. This paper makes no statement in kilograms, and the silence has a precise shape rather than a boundary of scope. The construction derives ratios, so the kilogram stands exactly one declared reference away: given any single mass in kilograms, every mass follows through the ratios derived here, the unified unit included. What is never derived is that single reference — a theorem the companion on units states and proves [16]. Every mass here is a ratio to carbon-12, and those ratios are the precision objects: eleven digits for the proton, nine for the neutron.

Within this construction the unit is more than a well-chosen convention. Identity 3 of Section 7 places the free nucleon's excess over the unit at one part in 126 at seat. And 1/126 is the difference of the unit fractions 1/28 and 1/36 — the same pair that builds the base and the bridge. The unit's defining substance sits inside the arithmetic that the seats themselves come from. Expressing the masses in unified atomic mass units is therefore not an imported choice; it is the register in which the construction's statements become visible. The honest converse is also stated: the seats are statements in this unit and in base ten, and in other units they do not appear. What is claimed is claimed about measured ratios to carbon-12 — convention-free physical quantities — organized in the unit the construction derives.

The chain of the paper is then closed on its own pages: measured ratios with their history above, seats derived in Section 6, residuals defined by the license of Section 1, and a mechanism proposed for them in Section 10.

## 3 · Formulae for the masses: a century of attempts

Attempts to derive the nucleon masses, or the ratios containing them, form a century-long record, and the record sorts into three families. Stating it plainly locates the present construction against each.

The first family proposes closed forms. Eddington derived the integer 137 from the algebra of a 136-dimensional structure and proposed a quadratic whose roots were to fix the proton-to-electron mass ratio; the values missed, and the adjustments that followed gave the genre its reputation [17]. Lenz observed in 1951 that 6π⁵ = 1836.118 matched the measured ratio of the day exactly [18]. The modern value, 1836.15267, excludes the expression by nineteen parts per million — several thousand standard deviations. Later entries fitted hadron masses to integer bins or lepton masses to power sums. Koide's relation among the lepton masses, holding today at parts per hundred thousand, remains the family's one surviving observation, and it remains unexplained [19]. The family's failure mode is uniform: the formula follows the measurement, no mechanism accompanies the number, and nothing is registered that could refute it.

The second family computes. Heisenberg's late program sought the masses as eigenvalues of a nonlinear spinor equation and produced no quantitative result. The bag and constituent-quark models of the 1970s reached the nucleon scale with fitted constants. Lattice quantum chromodynamics is this family in mature form: the ab initio light-hadron spectrum of 2008 reached the nucleon mass at the percent level [20], and the neutron-proton splitting followed in 2015 at twenty percent [12]. The inputs are the measured quark masses and one dimensionful anchor, so the computation verifies the theory without stating the digits, and its own account holds the absolute scale to be an input in principle.

The third family selects. Anthropic arguments constrain the light quark and electron masses to windows of roughly ten percent, outside which stable chemistry fails. The argument explains roughly where the values sit and, by construction, cannot say what they are.

One further precedent belongs to this paper specifically. Dirac's large-number hypothesis of 1937 was the first serious claim that a quantity containing the proton mass is epoch-dependent, and it carried a drift prediction that observation later excluded [21]. The hypothesis failed on the gravitational constant; the literature of varying constants that grew from it — the quasar absorption and clock comparisons of Section 12 — is the arena in which this paper's epoch claims are registered. The lineage is acknowledged: the claim-type is Dirac's; the mechanism, the register, and the exposure below are not.

Across the record, no attempt has combined four properties: digits stated in advance of adjustment, no adjustable parameter, a mechanism doing work beyond the number, and refutation conditions registered before the deciding measurements. The present paper asks to be weighed on that combination, together with a fifth property stated in the next section.

## 4 · The ground of the construction: the string's seventh and the forced base

The seed of the series is seven — the least full-reptend prime in base ten, the first prime whose reciprocal exhibits its complete period. That period is six, two times three: the first place the incommensurability of two and three appears whole. And the seed is not a symbol. The seventh partial stands on every vibrating string: touched at one seventh of its length, the string sounds the partial, with nodes at the sevenths and frequency at seven times the fundamental. The fraction is physically present — position, ratio, and node structure — before any notation exists for it. Western tuning admits the fifth and the third and has never seated the seventh: the one low partial every string carries is the one the keyboard omits. The companion papers develop this standing [23, 9]. The construction's starting object is therefore the string's own content, read in the six-digit turn its period defines.

The base is not a convention either, within the series. The published Origin proves a register theorem: base ten is the least base in which residue bookkeeping modulo nine survives digit summation and the reciprocal of seven unrolls its complete period. The bases carrying both mechanisms are rare — ten, nineteen, and seventy-three below eighty [22]. The theorem is conditional on the mechanism pair, and the Origin states and weighs that conditionality. Within the series, then, the decimal statements in this paper are not artifacts of human counting; they are readings in the register the arithmetic itself selects.

These two facts close the construction over its own frame, and the closure can be checked by reading. No equation in this paper converts a unit. The seed enters from the string, and the base is the register theorem's. The reference mass is derived below as Identity 3, the unit's carbon fraction standing as the bridge pair's own gap, and the outputs stand beside the CODATA table with no step between. The selections that remain are priced in Section 13, and the exposure is registered in Section 14. In the series' reading, this is the point: the constants' values are not dynamical accidents awaiting computation from couplings, but arithmetic objects read in the register the arithmetic fixes. The reader need not adopt that reading to check any number in this paper.

## 5 · Terminology

**The seat.** A short exact rational or six-digit decimal statement against which a measured value is compared. The seats used here are 1.00728, 1.00866, 1.00800, and 137.036. The word marks a comparison point, not a claim of mechanism.

**The residual.** The signed difference between a measured value and its seat, quoted in the natural place of the seat's last digits.

**The turn.** Six decimal digits. The reciprocal of seven has period six, and the six-digit statements above each occupy one turn. The companion papers develop this structure [9, 10].

**Triangular numbers and unit fractions.** T(n) = n(n+1)/2, and c(n) = 2/(n(n+1)) is its reciprocal, so that T(n)·c(n) = 1. The pair (T(7), T(8)) = (28, 36) appears throughout.

**Licensed fractions.** The candidate constants admitted to the program's scans: ratios of the two-three-seven web with small parts, the standard commas, and the published stations. Each scan below runs over a pre-registered list, and the accompanying batteries carry every list in full.

**The syntonic comma.** The ratio 81/80, the standard comma of just intonation, with excess 1/80 = 0.0125.

**The reflection.** The published tonal-function paper proves that reflecting the diatonic ring through the axis between the tonic and the dominant exchanges dominant and subdominant: the two are one object in two orientations [8]. That theorem is used here as proved there.

**The borrow in flight.** The published fine-structure paper reads the run of nines in 137.035999 as the borrow of a displacement in flight — an operation in progress rather than a stored quantity [9]. That reading is used here as published there.

## 6 · The seated values and their derivation

The three measured quantities, against their seats:

| quantity | seat | measured (CODATA-22) | residual |
|---|---|---|---|
| proton mass (u) | 1.00728 = 1.00800 − 0.00072 | 1.0072764665789(83) | −3.51 ppm of the mass |
| neutron mass (u) | 1.00866 = 1.00800 + 0.00066 | 1.00866491606(40) | +4.87 ppm |
| nucleon average (u) | 1.00797 = 1.00800 − 0.00003 | 1.0079706913(2) | +0.69 ppm |
| inverse fine-structure constant | 137.036 | 137.035999177(21) | −6.0 parts per billion |

The seats are derived, not fitted, and the derivations are laid out here so that the paper is anchored on its own pages.

**The offsets.** Call 6k a station of the six-ladder. A station above the sixth octave 64 has a superparticular step exactly when 6k − 64 divides 64, and this has three solutions: 66, with step 33/32; 72, with step 9/8; and 96, with step 3/2. The third is the dominant's own degree, occupied by the frame itself, so the available pair is 66 and 72 — consecutive stations, their difference the ladder's unit, their ratio 12/11. The ladder yields the pair; it does not order it. Four sign-and-assignment arrangements leave the proton lighter than the neutron, as the stability of hydrogen requires, and the measured values select one: the proton at the larger offset below the base, the neutron at the smaller offset above it. The derivation fixes the pair and the base; the arrangement is read from measurement and is priced as a selection below.

**The base.** The base is the product of the adjacent triangular numbers at the seed pair, 1008 = T(7) × T(8) = 28 × 36 (Identity 2 below). The selection of seven as the seed is the foundation of the series and is derived in the companions [9]; within this paper it is the one stated input.

**The fine-structure seat.** The primes whose reciprocals have base-ten period eight are exactly the prime divisors of 10⁴ + 1 = 73 × 137, and there are two. The prime 73 partitions its nonzero residues into nine cyclic classes; the prime 137 into seventeen. The companion paper assigns the seventeen-class prime to the electromagnetic office [9], and its integer is 137. The tail then follows from the bridge with no further choice: 1.008 divided by 28 is 0.036 exactly, which is T(8)/1000. Given the base, the bridge forces the tail; given the tail, it forces the base. One statement stands free, and two seats follow.

Every selection in this section is pinned in the batteries accompanying this record.

Three further structural facts about these seats are exact.

First, the two mass seats are one base with two offsets: 100800 − 72 and 100800 + 66, in units of one part in one hundred thousand. The offsets over the sixth power of two are the superparticular steps 72/64 = 9/8 and 66/64 = 33/32.

Second, the two kinds of seat split differently. The mass seats split arithmetically, base plus or minus offset, and the subtraction's borrow crosses the digit boundary: 100728 begins 1007, not 1008. The fine-structure seat splits positionally, at its midpoint: 137 | 036, three digits and three digits. An arithmetic split stores an address. A positional split at the half is the signature of a reciprocal in motion, which is the structure the borrow-in-flight reading describes [9]. The distinction between the two decompositions carries the interpretation in Section 11.

Third, the weight of the table must be stated honestly, because it falls in different places for the two kinds of row. A five-decimal statement always sits within five parts per million of any mass, and both mass seats are the nearest five-decimal roundings. The agreement column therefore carries no evidence for the masses; the derivation above carries all of it, and the arrangement of the pair adds a stated selection of one in four. The fine-structure row is different in kind. Its residual is 0.0008 of the seat's own last digit — a depth of one part in twelve hundred, which no rounding provides. The residuals, not the seats, are the subject of this paper.

## 7 · Four exact identities of the pair (28, 36)

The following four identities are arithmetic throughout and exact; each can be checked by hand in one line.

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

so the unit's carbon fraction is the gap between the adjacent unit fractions at the bridge. Because the unified unit is defined through carbon-12, this identity has a physical restatement: at seat level, the nuclear binding of carbon-12 less its electron masses is 12/125 = 0.096 u. The measured value, computable from the mass table alone, is 0.09565 u, which is 0.37 percent below the seat statement. This restatement is the average-nucleon seat statement scaled by twelve; it is displayed as the register's closure, not as an independent concurrence.

**Identity 4 (the tail's composition).** The fine-structure tail seat is one bridge fraction multiplied by the carbon step:

```
9/250 = 0.036 = (1/28) × (126/125)
```

These four identities close on one another: the bridge, the base, the unit, and the tail are four presentations of the pair (28, 36). None of them involves a measured quantity.

## 8 · The two mass residuals and their ratio 23/32

Write the mass residuals as offset displacements, in units of one part in one hundred thousand: the measured offsets are 72 + Δp and 66 + Δn. The 2022 values give

```
Δp = 0.3533421(8)          Δn = 0.4916060(400)
```

Both displacements are positive: each offset exceeds its seat. The neutron value is the 2022 adjustment. Under the superseded 2018 value the ratio below reads 0.718767(72), two tenths of a standard deviation from the same fraction: the identification survives the adjustment, which sharpened it twenty-fold. Their ratio is the central measured fact of this paper:

```
Δp / Δn = 0.7187506(585)          23/32 = 0.7187500          difference: +0.01 σ
```

**Result (uniqueness of the fraction).** Among all reduced fractions with denominator at most 64, exactly one lies within three standard deviations of the measured ratio, and it is 23/32. The scan is exhaustive, and the accompanying battery re-runs it mechanically. The three-sigma window admits about four tenths of a fraction on average, so uniqueness alone is close to a fair coin; the content is the proximity. The measured ratio agrees with 23/32 to better than one part in a million — one hundredth of a standard deviation. The probability that a random ratio falls this close to some fraction of denominator at most 64 is about one and a half parts in a thousand. The denominator is not a free bound: 32 is the grid of the seat rung itself, on which the offsets stand as 72/64 and 66/64. The parts reappear in the mechanism of Section 10, where 23 parts in 32 seat and 9 cross.

The composite consequence is immediate. The average nucleon's residual against its seat 1.00797, the tightest row of the system at +0.69 ppm, equals half the difference of the two displacements; the neutron-minus-proton splitting's residual equals their sum. One pair of numbers carries the family.

The ratio is registered here as a constant: its refutation condition is a future neutron-mass determination that moves Δp/Δn away from 23/32 by more than three of its then-current standard deviations.

The sharpness of the statement deserves its own sentence. Both displacements are ratios to carbon-12, so the claim is jointly a statement about the nucleon masses and the binding of the reference nucleus. A shift of the unit by six parts in ten billion — seven electron-volts in the binding energy of carbon-12 — moves the ratio three standard deviations. The constraint is registered, and exposed, at that sharpness.

## 9 · The seating temperature: one sixth of the proton mass

**Result (with its scan).** Dividing the proton mass by the integers two through twelve and comparing against the chiral crossover gives one candidate:

| divisor | m_p/d (MeV) | distance from the lattice value |
|---|---|---|
| 4 | 234.57 | +52 σ |
| 5 | 187.65 | +21 σ |
| **6** | **156.38** | **−0.1 σ** |
| 7 | 134.04 | −15 σ |
| 8 | 117.28 | −26 σ |

The divisors two, three, and nine through twelve miss by larger margins, listed in the accompanying battery. The table's distances are quoted against [5]; the other principal determination, 158.0(6) MeV [13], places m_p/6 at −2.7 standard deviations, with the crossover's definition-dependence stated in Section 1. The base rate is priced at the declaration threshold, not at the achieved closeness. With candidates spaced about 22 MeV near the crossover, a random value lands within one standard deviation of some divisor about thirteen percent of the time on the wider bar. The neutron's sixth part and the average's lie within 0.2 MeV of the proton's, a seventh of the bar: the three numerators are one trial, not three. The hadron-resonance-gas picture already places the crossover near a sixth of the nucleon mass; the content proposed here is the exact form, its seed in the turn, and the count it opens below. The divisor six is not arbitrary within the program. Six is the period of the reciprocal of seven and the number of digits in one turn, and c(3) = 1/6 is the unit fraction at the third rung. In that language the statement reads: the hadrons seat when the ambient temperature falls to one c(3) of the proton's own mass.

**The count.** With the seating temperature m_p/6 and the microwave-background temperature 2.72548(57) K [6], the elapsed interval is

```
N = log₂( (m_p/6) / kT_CMB ) = 39.2764 octaves
```

The count is a ratio of two energies and is therefore a pure number; no unit survives into it. Computed from the exact form m_p/6, its uncertainty is the anchors': three parts in ten thousand of one octave, from the background temperature. Read from the measured crossover instead, the count is 39.28(1); the exact form is the registered statement, the lattice its test. Its refutation condition is the lattice value: if the consolidated crossover temperature leaves the interval from 153 to 160 MeV, the seating statement fails. The window is wide because the determinations disagree; their convergence will tighten it.

## 10 · The deposition mechanism: one syntonic comma per octave

**Hypothesis.** The following mechanism is proposed for the origin of the two displacements. It is stated in the program's own terms, its quantitative consequences are compared with measurement, and its excluded variants are listed in Section 13.

The seat structure has period six: six whole-tone steps of 9/8 span one octave, since (9/8)⁶ = 2 × 531441/524288, and the six degrees of the diatonic ring each reseat once per octave. Carrying a just major sixth through one reseating misses the three-limit target by exactly the syntonic comma 81/80. The hypothesis is that each seated object receives this miss once per octave of cooling, at its own degree's reseating. The displacements are then the accumulated receipts across the N = 39.28 octaves since seating.

Three structural clauses complete the mechanism, each resting on a published or exact foundation.

**The partition.** At each receipt, the deposit divides in the proportion 23 to 9 on the grid of 32. The retained part seats; the part 9/32 crosses the reflection. The proton, whose offset 72 is three times 24 and whose two-digit pair reverses to a different pair, sits on the dominant degree and possesses the reflection partner proved in the tonal-function paper: the subdominant, ratio 4/3 [8]. The transferred fraction crosses that exchange. This clause is the content of the measured ratio 23/32 of Section 8.

**The axis.** The neutron's offset 66 is a palindrome: it is invariant under digit reversal, and its seat is the doubled center of the system's scalar ladder. An object on the reflection axis is its own mirror image; it possesses no partner, and no fraction of its receipts can cross. The neutron therefore retains everything, which is why Δn carries the full count and Δp carries 23/32 of it. The same conclusion follows twice more: from the reversal-invariance of 66, and from the schedule below.

**The schedule.** The period-six structure carries two hands — the dominant-side and subdominant-side readings — and the convergents of the logarithm of three base two alternate sides strictly, which forces the alternating read. The two hands coincide twice per rotation: on the axis, and at the antipode. The antipode of a nine-point ring is empty, nine being odd, a fact the gravitational companion establishes independently [10]. Exactly one coincidence finds an occupant. The axis object is touched at that coincidence, once per octave, and at a coincidence both orientations are present, so nothing can cross: the neutron's full retention follows from the schedule as well as from the palindrome.

**The quantitative state of the hypothesis, plainly.** With the count of Section 9, the per-octave deposit required by the neutron's displacement is 0.0125166(10), which exceeds the syntonic excess 1/80 by 0.133(8) percent. Equivalently: an exactly syntonic deposit requires a seating temperature of 162.1 MeV, which the two crossover determinations exclude at 3.8 and 6.9 standard deviations. Against the wider lattice bar the discrepancy factor is 1.0360(99), and seventeen superparticular steps lie within one standard deviation of it. The two adjacent to the bridge number, 28/27 and 29/28, are noted as the construction's own — a stated selection, not an inference. Three resolutions are possible: the lattice value moves; the seating sits one such step above m_p/6 for a reason not yet derived; or the deposit itself carries a real excess of this size. The lattice program's own sharpening will adjudicate. The ratio 23/32 is unaffected by this open factor, because a uniform deposit excess cancels in the ratio.

## 11 · The fine-structure side: a current, not a store

Section 6 established two decompositions: the mass seats are sums, 100800 − 72 and 100800 + 66, whose borrows propagate across digit positions; the fine-structure seat is a concatenation, the six-digit string split at its midpoint into 137 | 036. A sum stores a stationary address; a midpoint split of a period-six string is the form of a reciprocal read mid-cycle, and it flows. The published reading of the run of nines as a borrow in flight [9] identifies the fine-structure residual as a current rather than a ledger, and this section treats it as one.

**The window.** Every determination of the inverse constant in the modern record — Berkeley 2018, the CODATA recommendations of 2010 through 2022, the magnetic-moment route of 2023, Paris 2020 — lies strictly inside the one-unit interval

```
137.035999  <  α⁻¹  <  137.036000
```

The entire experimental discrepancy occupies the last unit of the seat's own turn. This window is registered: a future determination outside it refutes the reading. The determinations occupy the window's lowest sixth, so the operative content is the floor: no determination in the modern record sits below 137.035999. The ceiling is not in contest.

**The three depths.** The construction states the constant at three depths, each deeper than the last. The first is the seat, 137.036, one turn. The second follows from the bridge and the measured masses alone:

```
0.036 × ( m̄ / 1.008 )  =  m̄ / 28  =  0.0359989533(1)
```

where m̄ is the measured nucleon average in u. This is an identity, not a fit. Read at the register's own six-digit depth, the image rounds to 137.035999 — exactly the prefix every determination of the past fifteen years shares, the disagreement confined to what lies beyond. The six-decimal statement is therefore derived from the mass table, and it is the deepest statement on which derivation and measurement agree. The third depth is the full image, 137.0359989533(1): the unison row of any transport between the mass and fine-structure residuals, registered here under the name the mechanism gives it — the fine-structure value with no transport applied. Every current determination sits above it, by 3.4 standard deviations at the nearest bar and 23 at the sharpest; as a fraction of the image's own deficit below the seat, the overshoot is 27 percent. Section 14 registers the image in exactly those terms — not a prediction of the measured constant — and the conditional below addresses the standing. Dividing the seats rather than the measured masses gives the exact rational 100797/2800000 = 0.035998928571..., whose expansion past the seventh digit is the period-six cycle of one seventh. The measured image sits 0.025 millionths above it — the composite residual carried through the bridge. This two-part form — a finite head, then the period-six cycle — is this series' published definition of a rest value, and the published rest value of π carries the same form [11]. The parallel is structural, with no numerical claim.

**The five stations.** The constant is therefore stated from five perspectives on one axis, ordered here as they sit:

| station | value | perspective |
|---|---|---|
| the seat | 137.036 | arithmetic: T(8)/1000, one turn |
| the determinations | 137.035999046 – 206 | measurement: the cluster inside the seat's last unit |
| the six-decimal statement | 137.035999 | the image at the register's depth; the agreed prefix |
| the measured image | 137.0359989533(1) | the measured masses over 28 |
| the seat image | 137.035998928571... | the seats over 28; the period-six tail |

The two ends are pure arithmetic, the middle row is pure measurement, and the two images are each built from both. The six-decimal statement is the images' rounding at the register's depth, and the seat, derived independently, coincides with their three-digit rounding: two image values, one cluster, and the arithmetic statements they meet. Every gap between adjacent stations is a named object of this paper. The first is the deficit below the seat, the current this section reads; the second, the standing addressed in the conditional below; the third, the rounding depth of the register; the fourth, the composite residual over 28.

**A registered conditional.** Every determination stands above the derived image, one-signed, by 0.09 to 0.25 millionths. Whether the digits past the sixth decimal are further precision, or diffuse content of the register's circulation rather than of the constant, is not decided here. The period-six structure grounds the second possibility: the turn is six digits because the reciprocal of seven has period six, and the seat image's expansion past its head is that cycle and nothing else. The conditional is registered: if the digits beyond six decimals are shown to be diffuse rather than more accurate, the constant's exact statement is 137.035999. At that depth derivation and measurement agree exactly.

## 12 · The present epoch, and the mass drift

The count of Section 9 locates the present inside the mechanism. The elapsed 39.2764 octaves place the present 27.6 percent of the way through the fortieth octave since seating. The thirty-ninth receipt completed at redshift 0.21, about 2.6 billion years ago; the fortieth arrives when the universe has expanded by a further factor of 1.65, roughly seven billion years from now. The receipts are uniform in octaves and strongly non-uniform in elapsed time: the first landed about twenty microseconds after the origin, and the current one has been underway for billions of years. The companion monograph's seventh volume locates the present at the crest of the energy budget by an independent construction; the octave coordinate above is the mechanism's own and is stated beside it, not derived from it.

A continuing clock has a testable history. Today one octave of cooling elapses per H/ln 2 — about 1.03 × 10⁻¹⁰ octaves per year at the program's registered Hubble value of 70.05 km/s/Mpc [7]. The direct determinations span four percent to either side of that value, and every rate below inherits the band. All drifts are stated in the unit's own register, masses as ratios to carbon-12, and the register closes on itself. Differentiating the unit's definition, the transfers require the carbon binding, less the electron term, to absorb about two parts in 10¹⁶ of the binding per year — far below any present measurement. Within the register the signs are fixed by the mechanism. The neutron's offset grows upward and the proton's grows downward: the neutron mass rises, the proton mass falls, and the splitting widens. Smeared over the octave, the rates are +1.3 × 10⁻¹⁷ per year for the neutron and −0.9 × 10⁻¹⁷ for the proton.

The law, however, is event-coincident (Section 13, variant 3): between receipts the masses stand still. The laboratory prediction is therefore null: no clock comparison at any precision detects a present rate. The best present limit on the proton-to-electron ratio from optical-clock comparisons, −0.8(3.6) × 10⁻¹⁷ per year [15], is consistent with the predicted zero. The observable content lies across receipts. One receipt separates redshift 0.886 from the present, so the proton-to-electron ratio stood higher then by 0.9 × 10⁻⁷, a sign-definite step; the methanol determination on that sightline reads 0.0(1.0) × 10⁻⁷ [14]. The prediction sits at the measurement's own bar, and a factor-of-a-few improvement decides it. Earlier epochs compound the steps. At weak freeze-out, 7.6 octaves after seating, the accumulated deposits were a fifth of today's, so the neutron-proton splitting was half a percent smaller than now. The primordial helium fraction shifts upward at the level of several tenths of a percent — the scale of current determinations. That confrontation is stated as an open account of the mechanism, with its direction fixed, and is not computed further here.

One further coordinate is recorded with its residual unclaimed. Cooling ends at the de Sitter temperature floor of the asymptotic expansion rate — the registered Hubble value carried to its dark-energy limit — and the full run from seating to that floor is 139.2 octaves. The program's published horizon count is forty-two decades, which is 139.5 octaves. The two stand a third of an octave apart in 139, and the present sits at 28 percent of the run. The residual is stated and not assigned.

## 13 · Excluded variants, and the priced selections

Each of the following was tested against the same data and fails at the stated size. They are listed so that they are not rediscovered. The selections the paper itself makes are also priced here, in one place. The arrangement of the seat pair is one in four; the seating divisor, thirteen percent at its declaration threshold; the superparticular naming at the deposit, two of seventeen. The ratio's denominator bound is fixed by the rung grid rather than chosen. The registered values of Section 14 carry the exposure forward either way.

One further negative is recorded in the same spirit, before the list. If the mass residual and the fine-structure residual were related by a just-intonation interval, each licensed interval would imply a value of the constant. The program maintains that correspondence internally, and this paper declines to present it as evidence, for a reason that is itself a result: licensed intervals blanket the contested band at a spacing finer than the experimental bars. Every conceivable value of the constant therefore lies within a fraction of a standard deviation of some licensed implication. A correspondence of that density discriminates nothing. The derivation of the fine-structure residual is an open account of the program, held to the same standard as the mass residuals' mechanism, and it is not settled here.

1. Static closures of the displacements. No licensed fraction — 2,198 candidates across the two-three-seven web, the standard commas, and the published stations — matches Δp, Δn, their difference, or their sum, at the measured precision. The sole three-sigma item, 59/12 against the neutron at +1.5 σ, is reported and carries no structure. The displacements are not static stations, and that finding is what motivates the mechanism of Section 10.
2. The exactly syntonic deposit. Requires a seating temperature of 162.1 MeV; excluded by the two crossover determinations at 3.8 σ and 6.9 σ.
3. The compound (continuous-decay) transfer. The fitted decay constant per octave is 0.01785; the nearest licensed constant, 1/56, fails at 63 σ, and every other candidate by more. The transfer is event-coincident or the law is wrong.
4. The share model, in which a fraction of the transferred flow lands on the axis. It reproduces the neutron's deposit excess as 1/768 to +0.3 σ, and then fails its own second consequence, the proton's displacement, at 565 σ.
5. The six-deposit steady state for the fine-structure current: excluded at ≥3.4 σ by every determination.
6. Exact integer receipt counts (28 and 39): excluded at 11 σ.

## 14 · Registered values and refutation conditions

1. The seating temperature: m_p/6 = 156.379 MeV. Refuted if the consolidated lattice crossover leaves [153, 160] MeV. The two present determinations, 156.5(15) and 158.0(6) MeV, stand at −0.1 σ and −2.7 σ.
2. The elapsed count: 39.2764 octaves from the exact form, a pure number moving only with the two anchors; 39.28(1) if read from the measured crossover instead.
3. The ratio of displacements: Δp/Δn = 23/32, holding at one hundredth of a standard deviation on the 2022 table. Refuted by a future neutron mass more than three standard deviations away — equivalently, the ratio pins the carbon-12 binding to seven electron-volts, and a departure at that sharpness refutes it.
4. The window and its floor: every future determination of α⁻¹ falls in (137.035999, 137.036000). The operative content is the floor: no determination below 137.035999.
5. The root: 137.0359989533(1), the value with no transport applied — registered as the mechanism's unison row, not as a prediction of the measured constant, which stands 3.4 to 23 standard deviations above it.
6. No epoch dependence of the ratio: 23/32 is a constant, and any secular drift of the ratio refutes the partition.
7. The living clock, in two clauses. Between receipts the masses stand still: a present-day proton-to-electron drift confirmed at current laboratory sensitivity refutes the event-coincident law. Across receipts the ratio steps: it stood 0.9 × 10⁻⁷ higher at redshift 0.886 than today, a sign-definite prediction at the current bar of that sightline. The smaller early splitting raises primordial helium at the several-tenths-of-a-percent level, an open account with its direction fixed.
8. The conditional of Section 11: if the digits beyond six decimals are shown to be diffuse content rather than added precision, the constant's exact statement is 137.035999, and derivation and measurement agree exactly at that depth.

## 15 · Verification: the public batteries

Every exact identity, every scan, every exclusion, and every registered value in this paper is pinned by mechanical batteries: fifty-one tests in three files, written alongside the work. The full program suite of 2,775 tests was re-run green before this manuscript was composed. The batteries are public, together with this paper's source, at github.com/thefirsthorstmann/g-theory-verify, where the reader can re-derive every number in this paper from the CODATA table and the two published anchors.

*Companion volumes: Tonal Function on Discrete Terms (the reflection theorem; doi.org/10.5281/zenodo.22119146) · The Fine-Structure Constant on Discrete Terms (the seat 137.036 and the borrow in flight; doi.org/10.5281/zenodo.21211050) · Units on Discrete Terms (the dimensional boundary; doi.org/10.5281/zenodo.22119360) · Gravity on Discrete Terms (the empty antipode; doi.org/10.5281/zenodo.22087599) · G-Theory — The Origin on Discrete Terms (doi.org/10.5281/zenodo.21212112) · Predictions on Discrete Terms (the registry of record; doi.org/10.5281/zenodo.21206818).*

## References

[1] E. Tiesinga, P. J. Mohr, D. B. Newell, B. N. Taylor, CODATA recommended values of the fundamental physical constants: 2022, Rev. Mod. Phys. 97, 025002 (2025).

[2] L. Morel, Z. Yao, P. Cladé, S. Guellati-Khélifa, Determination of the fine-structure constant with an accuracy of 81 parts per trillion, Nature 588, 61 (2020).

[3] R. H. Parker, C. Yu, W. Zhong, B. Estey, H. Müller, Measurement of the fine-structure constant as a test of the Standard Model, Science 360, 191 (2018).

[4] X. Fan, T. G. Myers, B. A. D. Sukra, G. Gabrielse, Measurement of the electron magnetic moment, Phys. Rev. Lett. 130, 071801 (2023).

[5] HotQCD Collaboration (A. Bazavov et al.), Chiral crossover in QCD at zero and non-zero chemical potentials, Phys. Lett. B 795, 15 (2019).

[6] D. J. Fixsen, The temperature of the cosmic microwave background, Astrophys. J. 707, 916 (2009).

[7] C. Horstmann, Predictions on Discrete Terms, Zenodo (2026), DOI 10.5281/zenodo.21206818; and G-Theory — The Falsification Schedule, DOI 10.5281/zenodo.22119549.

[8] C. Horstmann, Tonal Function on Discrete Terms, Zenodo (2026), DOI 10.5281/zenodo.22119146.

[9] C. Horstmann, The Fine-Structure Constant on Discrete Terms, Zenodo (2026), DOI 10.5281/zenodo.21211050.

[10] C. Horstmann, Gravity on Discrete Terms, Zenodo (2026), DOI 10.5281/zenodo.22087599.

[11] C. Horstmann, π on Discrete Terms, Zenodo (2026), DOI 10.5281/zenodo.21205368.

[12] S. Borsanyi et al., Ab initio calculation of the neutron-proton mass difference, Science 347, 1452 (2015).

[13] S. Borsanyi et al., QCD crossover at finite chemical potential from lattice simulations, Phys. Rev. Lett. 125, 052001 (2020).

[14] N. Kanekar, W. Ubachs, K. M. Menten, J. Bagdonaite et al., Constraints on changes in the proton-electron mass ratio using methanol lines, Mon. Not. R. Astron. Soc. 448, L104 (2015).

[15] R. Lange et al., Improved limits for violations of local position invariance from atomic clock comparisons, Phys. Rev. Lett. 126, 011102 (2021).

[16] C. Horstmann, Units on Discrete Terms, Zenodo (2026), DOI 10.5281/zenodo.22119360.

[17] A. S. Eddington, Fundamental Theory, Cambridge University Press (1946).

[18] F. Lenz, The ratio of proton and electron masses, Phys. Rev. 82, 554 (1951).

[19] Y. Koide, A new view of quark and lepton mass hierarchy, Lett. Nuovo Cimento 34, 201 (1982).

[20] S. Dürr et al., Ab initio determination of light hadron masses, Science 322, 1224 (2008).

[21] P. A. M. Dirac, The cosmological constants, Nature 139, 323 (1937).

[22] C. Horstmann, G-Theory — The Origin on Discrete Terms, Zenodo (2026), DOI 10.5281/zenodo.21212112.

[23] C. Horstmann, The Seventh — A Constant Hidden in Plain Sight, Zenodo (2026), DOI 10.5281/zenodo.21206863.
