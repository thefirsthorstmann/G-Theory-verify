---
title: The Fine-Structure Constant on Discrete Terms
titlestyle: font-size:21.5pt; letter-spacing:0.6px;
subtitle: The coupling's integer as a decimal-ring fact with the rest value above the measured approach.
byline: Christian Horstmann · thefirsthorstmann@gmail.com · July 5th, 2026 · version 2, October 2026
date: 2026-07-05
titlenote: This paper separates the reciprocal of the fine-structure constant into three strata and makes a different statement about each. The structure of the integer 137 is established as arithmetic. The first block of the decimal, 036, is read as a rest value and weighed against chance. Digits beyond it are left to measurement, in a window registered in a companion record. Each statement carries its condition of refutation, and all arithmetic is pinned in a public test suite, github.com/thefirsthorstmann/g-theory-verify. Changes of substance from version 1 are marked † and noted where they occur.
abstract: The reciprocal of the fine-structure constant is dimensionless and measured near 137.036, and attempts to derive it have a long record of failure. The failures share a form: a formula matched to the measured decimal, proposed after the measurement, and adjusted when the measurement moved. This paper separates the constant into three strata and makes a different statement about each. The integer 137 is the unique prime whose reciprocal has base-ten period eight and seventeen cyclic families, by an exhaustive check over the five prime divisors of 10⁸ − 1. Its repeating block 00729927 obeys Midy's theorem, and the four-nines complement extends across the seventeen families. In the first decimal block the numerator 36 is over-determined by three constructions that share no steps; its placement at the third decimal place follows through the nucleon masses and remains open from the arithmetic alone. The rest value 137.036 stands 6.0 parts per billion above the CODATA 2022 value, and every modern determination lies below it. Digits beyond the block are left to measurement: named values are dense there, and the best determinations disagree. Twenty-eight times the rest block is 1.008 exactly, and twenty-eight times the settled block 0.035999 is 1.007972, within 1.3 parts per million of the mean of the proton and neutron masses. A measured α⁻¹ at or above 137.036 refutes the reading of the block; an arithmetic error in any exhibit, or a census showing the three registers to be common, removes the result it concerns. Every exhibit re-derives in a public suite at github.com/thefirsthorstmann/g-theory-verify, where the exact arithmetic of Sections 2 to 7 is also formalized in Lean 4.
---

## 1 · Introduction

The reciprocal of the fine-structure constant is measured near 137.036.
It is dimensionless, and the same for every observer and every system of
units. Attempts to derive it span a century, and this paper begins with
what they have in common. Eddington counted the degrees of freedom of
his E-number algebra, 16 · 17/2 = 136, and added a unit when measurement
gave 137 [1]. Wyler obtained 137.0360824 from the volumes of symmetric
spaces [10]. That value lay inside the uncertainty of the measurement of
his day, 1.5 parts per million, and stands 0.6 parts per million above
the present value, which excludes it. Later constructions have followed
the same course with more developed mathematics. Their common form is a
continuous formula, matched to the measured decimal, proposed after the
measurement, and adjustable when the measurement moved. Feynman called
the number "one of the greatest damn mysteries of physics" [2], and no
formula of this kind has stood.

This paper makes statements of a different form, one for each of three
strata. **The structure of the integer is established as arithmetic**,
with base ten declared, and each step can be checked in minutes. **The
first decimal block has two parts.** Its numerator is over-determined by
three constructions that share no steps. Its placement at the third
decimal place follows through the nucleon masses and remains open from
the arithmetic alone. **The deeper digits are left to measurement.** The
best determinations disagree with one another exactly there, and a
companion record registers the window they occupy [11]. Nothing in this
paper is matched to a measurement, and no statement moves if a
measurement moves. Section 9 states in advance what each outcome would
do to each statement.

## 2 · A theory cannot derive its own alphabet

One question comes before the arithmetic, because it decides what an
explanation of 137 could be. The companion series [3, 4] builds its
constructions from the arithmetic of two and three, the
incommensurability of doubling and tripling, realized through the
reptend of the sevenths [5]. Its alphabet is the numbers two, three, and
seven. To require that such a theory *derive* the integer 137
presupposes that 137 follows from something more basic. The finding of
this paper is the reverse: the integer stands at the basis and is
written in it —

**137 = 2⁷ + 3²,**

the coupling's integer written with the theory's three letters and
nothing else. Such an expression is called a spelling of the integer
below. A construction cannot be required to derive its own alphabet, any
more than geometry can be required to derive the point. What can be
required, and this paper accepts the requirement, is to show that the
spelling is not an accident. Three things are required. The integer must
be over-determined in the alphabet, spelled in several independent ways.
Each spelling must be weighed against chance in a stated census. The
whole must carry its conditions of refutation. Recognition,
over-determination, weight and exposure to refutation are the form of
statement appropriate to a constant that contains the basis of its
theory, and the rest of the paper carries it out.

## 3 · The ring theorem: the second spelling is a closure equation

The integer's second spelling is 137 = 8 · 17 + 1, with 17 = 3⁴ − 2⁶ = 81 −
64. Eight is the count of the octave, and seventeen is the anchor prime
  of the companion series, itself a power of three less a power of two
  [3]. The decisive fact is that this spelling is a **theorem about the
  integer's own decimal ring**. The multiplicative order of ten modulo
  137 is eight:

**ord₁₃₇(10) = 8,  therefore  136 = 8 · 17 —**

the one hundred thirty-six non-zero fractions over the prime fall into
exactly **seventeen cyclic families of period eight**. The count of
families is the anchor; the period is the octave; the plus-one is the
unit the ring closes on. The identity 8·17 + 1 is the closure equation p
− 1 = period × families. The same seventeen therefore appears twice, in
the spelling and as the family count: one fact stated two ways. The
contrast with Eddington's count is exact. Eddington's 136 = 16·17/2 also
carried a seventeen, and his added unit was applied after the
measurement moved. Here the unit belongs to the closure equation itself,
and it is in place before any measurement is consulted.

**The scarcity is settled by a factorization and not by statistics.** A
prime of decimal period eight must divide 10⁸ − 1 = 3² · 11 · 73 · 101
· 137. Therefore the primes whose ring closes at the octave are, among
all primes, exactly two: **73 and 137**, and their product is the
palindrome 10001. For comparison, the census of the short periods is
equally closed: period one {3}, two {11}, three {37}, four {101}, five
{41, 271}, **six {7, 13}**, seven {239, 4649}, **eight {73, 137}**. The
sevenths, the harmonic constant of the companion series [5], close at
period six, the hexad, with the full period: ord₇(10) = 6 = 7 − 1, a
single family. The coupling's prime closes at the octave, in seventeen
families. The two constants of the program close at the neighbouring
even periods, six and eight, under one ring law: one family there,
seventeen here.

## 4 · The backbone: 00729927

The leading fraction's reptend is the eight-figure block

**1/137 = 0.00729927 00729927 …**

and the block is organized about the all-nines 9999. Its halves are Midy
complements, 0072 + 9927 = 9999 [6]. Each of the four digit-pairs across
the split sums to nine: 0+9, 0+9, 7+2, 2+7. Read in twos the block is 00
· 72 · 99 · 27, with seventy-two and twenty-seven standing either side
of a central ninety-nine and summing to it, 72 + 27 = 99. The arithmetic
above is exact. A companion record constructs the same three values by a
different route [5]; that correspondence is a reading and is not used
further. The law extends over the whole ring, and every fraction over
the prime carries the four-nines complement. For example 2/137 =
.01459854 with 0145 + 9854 = 9999, and 3/137 = .02189781 with 0218 +
9781 = 9999. The pattern holds through all seventeen families. At period
six the same law gives the complement of the sevenths: **142 + 857 =
999**. The law also has a center. Complements reflect through half the
all-nines, which is the all-nines one octave down: the halves of the
sevenths about 499.5 and those of the backbone about 4999.5.† The
backbone and the harmonic constant obey one theorem at two depths. That,
and no resemblance of digits, is the documented relation between the
coupling's integer and the reptend of the sevenths: a shared law,
closure at neighbouring even periods, and one three-letter alphabet.

<div class="vnote">† Version 1 added a reason, the halving ladder
meeting the all-nines, which is not shown and is withdrawn.</div>

## 5 · The razor: weighing every match against chance

A match carries exactly as much weight as chance fails to explain, and
the program applies that measure to its own matches, so a match that
chance explains too easily carries no weight [4]. The censuses follow,
each closed and checkable:

| register | census | odds |
|---|---|---|
| 137 = 2⁷ + 3² | integers in [100, 200] spelling as 2ᵃ + 3ᵇ: 113, 131, 137, 145, 155 | 5 in 101 |
| period eight | primes below 150 whose ring closes at the octave: 73, 137 | 2 in 35 |
| the rest block .036 | measured tail within a millesimal grid step, from below, at 0.8 millionths† | ~1 in 1000 |
| the conjunction | the same integer holding all three registers at once | the paper's case |

<div class="vnote">† 0.9 millionths in version 1, on the CODATA 2018
value.</div>

The registers are logically independent. The spelling does not imply the
period, and neither implies where the measured tail lies. The case
therefore rests on the conjunction, and each census can be audited
separately. One register is excluded from the case by design. At the
seventh decimal of any measured constant, named values are dense. At the
next digits of the neutron mass (Section 7), three of seven named
candidates fall within half a percent of the unit at that place, so this
paper reads no digits at that depth.

## 6 · The tail: the rest value above the measured approach

This is the stratum at which the earlier derivations failed, and the
paper is most explicit here. In this series a constant has two values
[3, 4]. The rest value is the exact value the arithmetic fixes, and it
is reached only by calculation. The measured value is what an instrument
returns under the conditions of its realization, and the perturbation
offset is the difference between the two.† For the coupling the
dependence on those conditions is itself measured: α runs from 1/137 at
zero momentum toward 1/128 at the Z pole, the mass of the Z boson near
91 GeV.

<div class="vnote">† Version 1 called these the rest form, the realized
value and the displacement.</div>

The paper reads the coupling's rest value as α⁻¹ (rest) = 137.036 = 137 +
36/1000. The numerator is 36 = 4 · 9 = LCM(9, 12), the smallest joint
period of the nine-circle and the twelve-tone octave. Its digit sum is
nine, and 36/1000 = 9/250. **The numerator is over-determined and the
placement is not, from the arithmetic alone.**† Thirty-six is the joint
period of the two cycles; it is 1008 ÷ 28 from the nucleon average; and
it is 24 × 3/2 at the descent's dominant. No parameter is fitted in any
of the three, and they share no steps. Through the second the placement
arrives with the numerator [13]. Atomic masses are dimensionless ratios
to a twelfth of carbon-12; the rest value of the nucleon average reads
1.008 on that scale; and 1.008 ÷ 28 = 0.036, with its decimal position
included. That route has two inputs, the twenty-eight and the carbon
anchor of the atomic scale. From the arithmetic alone nothing here fixes
why the numerator stands at the third decimal place, and Section 9 names
that narrower step as open.

<div class="vnote">† Version 1 read the whole block as one selection;
the constructions and the route to the placement are in [13].</div>

One figure states the position: 137.036 stands 6.0 parts per billion
above the CODATA 2022 value, 137.035999177(21) [9],† and every modern
determination lies below it. The figure in standard deviations is not
quoted, because the gap is fixed while the divisor differs by laboratory
and by year. The count runs from 35 to 72 across four sources and
carries no information. The rest value is not what an interferometer
returns. It is defined at zero excitation and obtained only by
calculation; what measurement approaches is the measured value, offset
below the rest value by the perturbation of its realization.

<div class="vnote">† Version 1 gave this distance as 72 standard
deviations, a count that depends on the determination chosen.</div>

**The best determinations agree through the block and disagree beyond
it.** The two best direct determinations of the constant differ from
each other by more than five standard deviations [7, 8]. Caesium
interferometry (Berkeley, 2018) gives 137.035999046 and rubidium
(Paris, 2020) gives 137.035999206. The electron g−2 route (2023) gives
137.035999166 [9]. All three agree on the integer, and all three agree
through the run of nines, .035999. All three lie strictly below
137.036, by 5.8 to 7.0 parts per billion. They part only from the
seventh decimal onward, which is the depth this paper leaves to
measurement. **No selection by this author produces that pattern.** It
is the present state of metrology. It separates the digits of the
constant into the three strata of this paper: an integer that holds, a
block that holds, and a depth on which the determinations have not
settled. The earlier derivations each claimed the third stratum. This
paper establishes the first and reads the second. For the third, a
companion record registers the window 137.035999 < α⁻¹ < 137.036000,
inside which every modern determination lies, and a conditional on the
digits past the sixth decimal [11].†

<div class="vnote">† Version 1 declined these digits permanently. The
window and the conditional were registered afterwards, in [11].</div>

**The run of nines is the arithmetic borrow of the offset.** Subtract a
small offset ε from 0.036 and decimal arithmetic propagates a borrow.
The 6 falls to 5 and a run of nines opens behind it, and the count of
nines gives the size of ε. So 0.036 − 7.94 × 10⁻⁷ = 0.035999206, digit
for digit the Paris value. The observed run of nines *is* the borrow of
the offset in flight. This is exact arithmetic: any value just below
.036 must carry this form. The measured tail is therefore not noise
about an unrelated number; it is the form an approach from below must
take.

**The settled block carries over to the nucleon mean under one factor.**
Twenty-eight times the rest block is the hydrogen base exactly, 28 ×
0.036 = 1.008 (Section 7). Twenty-eight times the settled block is 28 ×
0.035999 = 1.007972, also exact, and it stands against the measured
nucleon mean, (mp + mn)/2 = 1.0079707: a match of 1.3 parts per million.
Rest value maps to rest value, and the settled block to the measured
mean. The block's offset carried through the factor is 28 × 10⁻⁶ = 2.8 ×
10⁻⁵, and it tracks the mean's own offset from its base, −2.9 × 10⁻⁵.
That is the −3 of Section 7 seen from the coupling's side. Beyond the
block the determinations differ, and with their further digits the
product stands 2.6 to 7.0 parts per million above the mean [11].† The
reading has the standing of the rest of Section 7. It shows that the
offset between the two values is not private to the coupling: it carries
over.

<div class="vnote">† The sentence on the further digits is an addition
of version 2; the block's figures are those of version 1.</div>

## 7 · The family affair: the block and the nucleon masses

The rest block is related to the nucleon masses, and the relation is
shown here with the standing of each part. Twenty-eight, the seventh
triangular number T(7), times the rest block is exact:

**28 × 0.036 = 1.008,**

the hydrogen base of the companion series divided by a thousand, 1008 =
42 · 24 [3]. The multiplier and the numerator are the adjacent
triangular numbers T(7) = 28 and T(8) = 36, and the base is their
product [11]. About that base the measured nucleon pair stands at −72
for the proton and +66 for the neutron, the two stations of the
companion record on the nucleon masses [11]. In units of 10⁻⁵ on the
atomic-mass ratio, 1.008 − 0.00072 = 1.00728 and 1.008 + 0.00066 =
1.00866. The signs are fixed and not chosen: the base is bound hydrogen,
so the bare proton must lie below it and the free neutron above. Which
station goes with which nucleon is read from the measured masses [11].
The two stations average (−72 + 66)/2 = −3, so 1.00728 and 1.00866
average 1.00797. The measured mean, (mp + mn)/2 = 1.0079707, and
twenty-eight times the settled block, 1.007972, agree with that value to
five decimal places. The standing of each part is as follows. The
products and the average are exact arithmetic. The stations are read
here from measured masses at three digits, and the residuals of 3.5 and
4.9 parts per million are what the truncation leaves, pinned as such.
The seventy-two is the backbone's own second block, returning at the
proton. The atomic-mass ratios are dimensionless, so the dimensional
boundary permits the reading, and Section 5 weighs it.

The gap of three recurs in the companion record's reading of the numeral
of the speed of light [12]. On a metre rescaled by 0.07 percent the rate
of light reads exactly 3 × 10⁸.† That integer and its all-nines
neighbour, 3 × (10⁸ − 1) = 299,999,997, differ by exactly 3 and factor
apart. The first is 2⁸ · 3 · 5⁸ and contains no 137. The second is 3³ ·
11 · 73 · 101 · 137, and it contains the coupling's prime necessarily:
the order of ten modulo 137 is eight, so the prime divides the all-nines
10⁸ − 1. The first is the second with its run of nines rounded up by
exactly three: a round form above and nines below, as with the
coupling's .036 over .035999. This is a reading of units under the
program's dimensional boundary. The magnitude of the speed of light
belongs to the unit: the SI numeral, 299,792,458, has been fixed by
definition since 1983, and nothing here derives or disputes it [12].
What is exact is the two factorizations and the gap; the identification
is the program's own.

<div class="vnote">† Version 1 called 3 × 10⁸ the observed form; the
measured and defined numeral is 299,792,458.</div>

## 8 · Watched: three adjacent items and the standing of each

Three items adjacent to this paper's subject are watched, each recorded
here with its present standing. **The coupling at the Z pole is near
1/128, and the comparison is scheme-dependent.** Here 128 = 2⁷ is the
power of two in the spelling 137 = 2⁷ + 3². The value is
scheme-dependent at the precision that would matter, so a
scheme-dependent match carries no weight. A scheme-invariant statement
of the endpoint remains open. **The two stations are constructed in the
companion record on the nucleon masses.** Section 7 uses the stations
only as read from the measured masses, and the companion record derives
72 and 66 as a pair [11]. **The digits beyond the stations' third place
are taken up in the same record.** They fall where named values are
dense, and this paper does not read them. That record treats them as the
two mass residuals and registers their ratio [11].

## 9 · Conduct: what is established, what is read, what is left to measurement

**Established as arithmetic, with base ten declared, and pinned:**

- the three spellings 2⁷ + 3², 8·17 + 1, and 17 = 3⁴ − 2⁶
- the ring theorem ord₁₃₇(10) = 8, whose seventeen families are the same fact as the spelling
- the scarcity {73, 137}, closed by the factorization of 10⁸ − 1
- the censuses of Section 5: five spellings in [100, 200], two octave primes below 150
- the backbone 00729927, with its Midy law and its family-wide four-nines complement
- the exact product 28 × 36/1000 = 1008/1000
- the factorizations of 3 × 10⁸ and 3 × (10⁸ − 1), and their gap of
  three
- the borrow that opens the run of nines, as arithmetic

**Read, and weighed against chance:**

- the assignment of the prime 137 to the electromagnetic coupling
- the placement of the rest block at the third decimal place, from the arithmetic alone
- the rest value 137.036 standing above the measured approach
- the backbone's 72 · 99 · 27 beside the companion construction of [5]
- the nucleon relation
- the two forms of the numeral of the speed of light as a round form
  over an all-nines form

**Left to measurement, or taken up in a companion record:**†

- every digit of the measured constant beyond the rest block (window
  registered in [11])
- every digit of the nucleon masses beyond the stations' third place,
  taken up in [11]
- the magnitude of the speed of light
- any formula for the measured decimal

<div class="vnote">† Headed “Declined, permanently” in version 1. The
censuses and the assignment are entries of version 2.</div>

**Falsification conditions, in force now.** A confirmed measurement of
α⁻¹ at or above 137.036 refutes the approach-from-below reading
outright; the floor of the registered window, 137.035999, is the
companion record's condition [11]. Convergence of the interferometry
disagreement onto a settled value would move those digits from
*unsettled* to *measured*; the exhibit of Section 6 would weaken, and a
later version would say so. An arithmetic error in any pinned exhibit,
each checkable in minutes, refutes the corresponding statement of
structure directly. A larger census, constructed on the same rule, that
showed the registers of Section 5 to be more common than stated would
weaken the case and would be registered. A structural condition
motivated as independently as the one given here, and selecting a
different integer, would remove the assignment to the coupling and leave
the arithmetic standing [13].† The open result that would strengthen the
paper is named as well: a construction of the placement from the
arithmetic alone. A statement refuted under these conditions is recorded
as refuted and is not reinterpreted. The program then uses the miss to
find why the construction failed, and a revised statement enters as a
new one under its own date. The paper is revised additively, and every
change of substance is marked where it occurs.

<div class="vnote">† Added in version 2: the condition on the
assignment, and what follows a refutation. Version 1 named a
construction of 36/1000 as the open result; the numerator is now
constructed.</div>

## References

[1] A. S. Eddington, *Relativity Theory of Protons and Electrons*, Cambridge (1936); *Fundamental Theory*, Cambridge (1946).

[2] R. P. Feynman, *QED: The Strange Theory of Light and Matter*, Princeton (1985), 129.

[3] C. Horstmann, *Navier–Stokes: A Solution on Discrete Terms*, Zenodo
(2026), DOI 10.5281/zenodo.21197044; and the series it opens.

[4] C. Horstmann, *Predictions on Discrete Terms*, Zenodo (2026), DOI
10.5281/zenodo.21206818.

[5] C. Horstmann, *The Seventh — A Constant Hidden in Plain Sight*, Zenodo
(2026), DOI 10.5281/zenodo.21206863; *The Enneagram Is a Theorem*,
Zenodo (2026), DOI 10.5281/zenodo.21206948.

[6] E. Midy, *De quelques propriétés des nombres et des fractions décimales périodiques*, Nantes (1836); modern treatment in B. D. Ginsberg, *Midy's (nearly) secret theorem*, College Math. J. **35** (2004) 26.

[7] R. H. Parker, C. Yu, W. Zhong, B. Estey, H. Müller, *Measurement of the fine-structure constant as a test of the Standard Model*, Science **360** (2018) 191.

[8] L. Morel, Z. Yao, P. Cladé, S. Guellati-Khélifa, *Determination of the fine-structure constant with an accuracy of 81 parts per trillion*, Nature **588** (2020) 61.

[9] X. Fan, T. G. Myers, B. A. D. Sukra, G. Gabrielse, *Measurement of
the electron magnetic moment*, Phys. Rev. Lett. **130** (2023) 071801;
P. J. Mohr, D. B. Newell, B. N. Taylor, E. Tiesinga, *CODATA recommended
values of the fundamental physical constants: 2022*, Rev. Mod. Phys.
**97** (2025) 025002.

[10] A. Wyler, *L'espace symétrique du groupe des équations de Maxwell*,
C. R. Acad. Sci. Paris **269** (1969) A743; *Les groupes des potentiels
de Coulomb et de Yukawa*, C. R. Acad. Sci. Paris **271** (1971) 186.

[11] C. Horstmann, *The Proton and Neutron Masses on Discrete Terms*,
Zenodo (2026), DOI 10.5281/zenodo.22217669.

[12] C. Horstmann, *Units on Discrete Terms*, Zenodo (2026), DOI
10.5281/zenodo.22119360.

[13] C. Horstmann, *QED on Discrete Terms*, Zenodo (2026), DOI
10.5281/zenodo.22119528.

*The public suite at github.com/thefirsthorstmann/g-theory-verify pins
every exhibit above and is rerun on every revision. The exact arithmetic
of Sections 2 to 7 is also formalized as thirty-two theorems in Lean 4
with Mathlib, in the same repository.*

<div class="copyright" style="margin-top:14pt">Copyright<br>Christian Horstmann · July 5th, 2026 · version 2, October 2026<br>thefirsthorstmann@gmail.com<br>All rights reserved</div>
