---
title: The Seventh — A Constant Hidden in Plain Sight
subtitle: The reptend of one-seventh as a dimensionless harmonic label set — one cycle, three anchors, a conserved transform between its two canonical orders, and a fold that makes the whole exact.
titlestyle: font-size:21.5pt; letter-spacing:0.6px;
byline: Christian Horstmann · thefirsthorstmann@gmail.com · July 2026 · version 6, October 2026 · manuscript for the public record
date: 2026-07-05
titlenote: Everything famous about the number 142857 is old, and the first section says so with citations. What this paper presents is what, to the author's knowledge, is not in that literature: a collapse theorem, a conserved transform, a fold theorem, and a naming. Every exact claim is pinned by a public test suite, and the four exhibits are formalized as theorems in Lean 4.
abstract: The decimal period of one-seventh, 142857, is the most famous curiosity in elementary arithmetic, and nearly everything known about it is very old — its cyclic property, its multiplication behavior, Midy's theorem of 1836, its standing as the signature of the smallest full-period prime in base ten. This paper credits all of that up front, because its claims lie elsewhere. Four exhibits, each exact and machine-pinned. First, the label set: the first six harmonics of a vibrating string, octave-reduced, sound the pitch-class sequence Do, Do, Sol, Do, Mi, Sol — and the six sevenths, in their natural arithmetic order, are the smallest complete dimensionless label set for that sequence: no denominator below seven yields six distinct non-terminating labels, a fact pinned by exhaustion. The distinction between labeling and touching is kept strictly — touching a string at one-seventh of its length excites the seventh harmonic, not the first; the sevenths name the series, they do not sound it. Second, the collapse: normalize the six sevenths by their largest member and they become the six sixths; octave-reduce those and exactly three pitch classes remain — Do, Fa, La, the root, the fourth, and the major sixth, the structural anchors of the descending just-intonation lattice — while Re, Mi, Sol, and Si are never visited by any seventh. Six values, three anchors, four silences: the collapse is exact rational arithmetic, verifiable in six lines, and to the author's knowledge it has not been stated in the literature. Third, the transform: split the period as 1 | 42 | 8 | 57 — a displayed definition, first digit, interior pair, fourth digit, interior pair — hold the outer digits and reverse the two interior pairs, and the result is 124875, which is exactly the multiplicative order of the same six digits: the doubling orbit 1, 2, 4, 8, 16 ≡ 7, 14 ≡ 5 modulo nine. The positional line and the multiplicative line of the reptend differ by one operation, and that operation is conserved: the first pair drops by exactly 18, the second rises by exactly 18, the net is zero, and both pairs sum to 99 before and after. A single exchange, balanced to the unit, connects the cycle's two canonical orders. Fourth, the fold: separate the family at Midy's own axis — the lower three sevenths against the upper three — and the division is exact in the family's own units: the ratio of the upper sum to the lower sum is (15/7)/(6/7) = 5/2, its reduced parts summing to seven; the whole is 3, divided 5/7 to 2/7 of itself; the group centroids are 5/7 and 2/7, themselves a Midy pair. The fold has an exact consequence: truncated at the period, the six labels fall short of their whole by exactly three units in the last place, and exactly the upper three round up, closing the deficit to the unit — the committed system totals 3.000000 exactly, an identity that holds as (p − 1)/2 for every odd prime at its period depth, while the ratio (3p − 1)/(p + 1) runs from 2 at p = 3 toward 3 in the limit and equals 5/2 at p = 7 alone. On these four exhibits the paper names the object — the harmonic constant: the reptend cycle of seven as the base-ten fingerprint of the smallest complete label set of the harmonic series, advanced as a true dimensionless constant of nature's harmonic structure, of the kind physics already honors, with the fine-structure constant its electromagnetic counterpart — a relation displayed in exact identities, 137 = 2⁷ + 3² = 8·17 + 1, eight the octave and seventeen the next full-period prime after seven; whether the counterpart admits a rest-value decomposition is taken up in a companion paper. The naming is a definition; the exhibits are theorems, formalized in Lean 4, and every exact claim re-derives in the public suite at github.com/thefirsthorstmann/g-theory-verify.
---

## 1 · Everything famous here is old

The cyclic behavior of 142857 — that its multiples by 1 through 6 are
its own rotations — has been a schoolroom marvel for centuries and
appears throughout the recreational literature. Midy proved the half-sum
theorem in 1836 [1]; Dickson's history catalogues the study of periodic
decimals back through Gauss [2, 3]; that seven is the least prime whose
base-ten period is full, the decimal of 1/p repeating only after p − 1
digits — the least *long prime* — is textbook number theory [3]. All of
this is adopted from the literature, cited once and used freely. The
paper's claims are four exhibits that, to the author's knowledge, are
*not* in that literature, and section 8 states the conditions under
which each fails.

## 2 · Sevenths express rotation

**The six fractions k/7 share a single decimal expansion:**

<div style="text-align:center; margin:12pt 0;">1/7 = 0.142857 142857 …<span style="float:right;">(1)</span></div>

Each period is a rotation of the single string 142857, and the six
rotations are distinct: one cycle, entered at six digits, pinned in the
suite by direct computation.

**Seven is the least prime for which base ten does this.** The
full-period primes below twenty are 7, 17, 19, and nothing smaller
qualifies. This reptend cycle is the smallest object of its kind that
exists in decimal arithmetic.

## 3 · How sevenths are organized as tones

**A string fixed at both ends sounds integer multiples of its
fundamental.** This is harmonic structure in its plainest instance.
Octave-reduced, each ratio halved until it lies between 1 and 2, the
first six harmonics land on the pitch classes

<div style="text-align:center; margin:12pt 0;">Do, Do, Sol, Do, Mi, Sol<span style="float:right;">(2)</span></div>

— the audible signature of the harmonic series in any string, pipe, or
resonant body [4] — and heard rising from the root, the series passes
through the anchoring intervals of tonality in order:

| harmonic | ratio | octave-reduced | interval, rising | pitch class | label |
|---|---|---|---|---|---|
| h₁ | 1:1 | 1 | root | Do | 1/7 |
| h₂ | 2:1 | 1 | octave | Do | 2/7 |
| h₃ | 3:1 | 3/2 | fifth | Sol | 3/7 |
| h₄ | 4:1 | 1 | octave | Do | 4/7 |
| h₅ | 5:1 | 5/4 | major third | Mi | 5/7 |
| h₆ | 6:1 | 3/2 | fifth | Sol | 6/7 |

**The six sevenths are the smallest complete label set for that
sequence.** In natural order, 1/7 through 6/7, they index its six
elements with six dimensionless values, and nothing smaller does: every
denominator below seven either terminates, repeats short, or collapses
under reduction to fewer than six distinct labels, a fact pinned by
exhaustion in the suite.

**The sevenths are labels, not touch points.** The distinction is kept
strictly, because confusing the two would undo the exhibit. Touching a
vibrating string at one-seventh of its length excites the seventh
harmonic, not the first — the sevenths name the series, they do not
sound it.

## 4 · Sevenths taken in descending order

**Normalized by their largest member, the six sevenths become the six
sixths.** The division is

<div style="text-align:center; margin:12pt 0;">(k/7) ÷ (6/7) = k/6<span style="float:right;">(3)</span></div>

and the six values are

<div style="text-align:center; margin:12pt 0;">1/6, &nbsp; 1/3, &nbsp; 1/2, &nbsp; 2/3, &nbsp; 5/6, &nbsp; 1<span style="float:right;">(4)</span></div>

**Reduced into a single octave, exactly three pitch classes remain.**
The octave here is the one below the root, from 1/2 to 1: 2/3 lies a
fifth below the root, the pitch class of the fourth above it, Fa; 5/6
lies a minor third below, the pitch class of the major sixth, La.

| seventh | normalized | octave-reduced | position |
|---|---|---|---|
| 1/7 | 1/6 | 2/3 | **Fa** |
| 2/7 | 1/3 | 2/3 | **Fa** |
| 3/7 | 1/2 | 1/2 ≡ 1 | **Do** |
| 4/7 | 2/3 | 2/3 | **Fa** |
| 5/7 | 5/6 | 5/6 | **La** |
| 6/7 | 1 | 1 | **Do** |

**The three are the structural anchors of the descending just-intonation
lattice:**

<div style="text-align:center; margin:12pt 0;">Do · Fa · La — the root, the perfect fourth, the major sixth<span style="float:right;">(5)</span></div>

The other four diatonic positions — Re, Mi, Sol, Si — are visited by no
seventh at all.

**Six values fall on three anchors and leave four positions silent.**
The silences are part of the result: the collapse is exact rational
arithmetic from end to end, pinned in the suite, verifiable by hand in
six lines. To the author's knowledge this fact is not stated in the
mathematical or music-theoretic literature.

## 5 · The transform: one exchange between the two canonical orders

**The reptend cycle has three orders:**

| order | the six digits | what it is |
|---|---|---|
| positional | 142857 | the period as written |
| multiplicative | 124875 | the doubling orbit of 1 modulo nine: 1, 2, 4, 8, 16 ≡ 7, 14 ≡ 5 |
| harmonic | 124578 | the first digit of k/7, ⌊10k/7⌋ — the six digits ascending, skipping the 3 and the 6, the order in which they lie along the string |

The first two are the canonical orders: both order the single reptend,
and they differ by exactly one operation. The third is an order of the
family of six fractions.

**The period is split as first digit, interior pair, fourth digit,
interior pair.** The split is a displayed definition:

<div style="text-align:center; margin:12pt 0;">142857 = 1 | 42 | 8 | 57<span style="float:right;">(6)</span></div>

**With the outer digits held, reversing each interior pair gives the
multiplicative order exactly.** 42 becomes 24 and 57 becomes 75:

<div style="text-align:center; margin:12pt 0;">1 | 24 | 8 | 75 = 124875<span style="float:right;">(7)</span></div>



**The exchange is exactly conservative:**

<div style="text-align:center; margin:12pt 0;">42 → 24 falls by 18 &nbsp;·&nbsp; 57 → 75 rises by 18 &nbsp;·&nbsp; net 0 &nbsp;·&nbsp; 42 + 57 = 99 = 24 + 75<span style="float:right;">(8)</span></div>

and the pair-differences move from 57 − 42 = 15 to 75 − 24 = 51 — the
same two digits, transposed. One balanced exchange, nothing created and
nothing destroyed, connects the cycle's positional order to its
multiplicative order.

**The same operation is a substitution of octave partners.** This second
realization is equivalent and pinned: substitute each digit by its
octave partner — each pair related by doubling modulo nine — while 1 and
8 stand unmoved:

<div style="text-align:center; margin:12pt 0;">2 ↔ 4, &nbsp; 5 ↔ 7, &nbsp; with the axis {1, 8} fixed — the Midy pair, summing to nine<span style="float:right;">(9)</span></div>

The result is the same string. The block form displays the conservation;
the substitution form displays the mechanism — octave pairs rotating
about a neutral axis. The suite pins every figure of both. To the
author's knowledge the observation is unpublished.

## 6 · The fold: separation across Midy's axis

**The family is separated at Midy's axis, the lower three sevenths
against the upper three.** Midy's theorem [1] pairs the sevenths across
that axis — k/7 + (7−k)/7 = 1, three pairs, each summing to one.
Separated there instead, every quantity of the division is exact, and
every one is stated in the family's own units:

| the division | value | note |
|---|---|---|
| upper sum to lower sum | (4/7 + 5/7 + 6/7) / (1/7 + 2/7 + 3/7) = (15/7) / (6/7) = **5/2** | the reduced parts sum to the seed: 5 + 2 = 7 |
| the whole | **3** | divided 5/7 : 2/7 *of itself* — in quanta of 3/7, five above, two below |
| the centroids | **5/7 and 2/7** | themselves a Midy pair, summing to one; their ratio again 5/2 |

The labels divide in their own units: the whole they sum to is divided
into sevenths of itself, the two group means are members of the family,
and the ratio's parts count back to seven. In the harmonic order's terms
the division is visible at a glance — the lower labels lead with 1, 2,
4, digits summing to seven; the upper with 5, 7, 8.

**Rounded at the period, the six labels sum to exactly three: the
committed whole.** This is the fold's exact consequence. Truncate all
six sevenths at the period — six digits — and the system falls short of
its whole by exactly 3 × 10⁻⁶: each k/7 loses k/(7 · 10⁶), and the six
losses sum to 21/(7 · 10⁶). Now round. Exactly the upper three round up
— they are the sevenths past one-half — and their three unit corrections
restore exactly 3 × 10⁻⁶:

<div style="text-align:center; margin:12pt 0;">0.857142 + 2.142858 = 3.000000, exactly<span style="float:right;">(10)</span></div>

The rounding half closes the truncation deficit of the whole family, to
the unit; the whole is exact because, and only because, the upper group
commits. Nor is this an accident of seven: for every odd prime at its
period depth, the number of rounders equals the truncation deficit in
last-digit units, so the committed total is (p − 1)/2 exactly — pinned
in the suite from p = 3 through p = 23.

**The ratio generalizes to every odd prime, and 5/2 occurs at seven
alone.** For the fractions of any odd prime p, the ratio of the upper
sum to the lower sum is

<div style="text-align:center; margin:12pt 0;">(3p − 1)/(p + 1): &nbsp; 2 at p = 3 &nbsp; → &nbsp; 5/2 at p = 7 &nbsp; → &nbsp; 3 in the limit, never arriving<span style="float:right;">(11)</span></div>

It equals **5/2 at p = 7 alone** — the arithmetic mean of the family's
own two endpoints is attained at exactly one prime, the least
full-period prime, this paper's object. And the whole, (p − 1)/2,
coincides with the family's limit — both are 3 — again only at p = 7.
Two uniqueness marks on the same division. To the author's knowledge
neither the committed-whole identity nor the fold family is stated in
the literature.

## 7 · Why sevenths should be called a constant

**Definition: the reptend cycle of seven is the harmonic constant.** On
the four exhibits the paper names its object — the base-ten fingerprint
of the smallest complete dimensionless label set of the harmonic series,
carrying a three-anchor collapse, a conserved transform between its two
canonical orders, and a fold that makes the whole exact — and advances
it as a true dimensionless constant of nature's harmonic structure, of
the *kind* physics already honors: dimensionless, scale-invariant,
structure-organizing. Its selection is least action as this series uses
it, the smallest object that performs being taken first, and its
referent is harmonic structure, which every bounded system displays.

**Its electromagnetic counterpart in those tables is the fine-structure
constant.** The relation is arithmetic: the celebrated integer part of
its inverse satisfies

<div style="text-align:center; margin:12pt 0;">137 = 2⁷ + 3² = 8·17 + 1<span style="float:right;">(12)</span></div>

— the octave register to the seventh power by one route; by another,
eight — the octave — times seventeen, *the next full-period prime after
seven*, plus one. These are displayed as exact identities.

**The counterpart's rest-value decomposition is the subject of a
separate paper.** Whether it admits a decomposition of the kind the
companion paper defines [6] is taken up there [7]. The naming itself is
a definition, in the sense the companion papers of this series give such
acts [5, 6]: a definition is justified by the theorems it organizes, and
the theorems here are pinned.

## 8 · What is established, and what would refute it

**Established.** The smallest-complete-label-set fact (section 3, pinned
by exhaustion); the collapse to Do–Fa–La with four positions unvisited
(section 4, exact); the transform identity and its exact conservation
(section 5); the fold — the five-to-two division of the sum, the
committed-whole identity, and the family (3p − 1)/(p + 1) with the value
5/2 attained only at seven (section 6, exact); and the naming as a
definition.

**Adopted and open.** The classical material of section 1 is adopted
from the literature. The relations to the fine-structure constant in
section 7 are exact identities, and its rest-value decomposition is the
subject of the companion paper [7]. A physical mechanism for these
correspondences remains open.

**What would retire the statements of novelty.** A prior statement of
section 4's collapse, section 5's transform, or section 6's fold in the
literature; it would be cited in the next version.

**What would falsify the content.** An arithmetic error in the pinned exhibits — each is checkable in minutes.

## 9 · Coda

**The evidence is five exact results.** A six-element exact label set
proved minimal by exhaustion; a collapse onto the three tonal anchors
with four silences, exact in rational arithmetic end to end; a conserved
involution linking the object's two canonical orders; a fold across
Midy's own axis dividing the labels five to two in their own units,
whose committed roundings make the whole exact; and an arithmetic
relation, by displayed identity, with the integer part of the inverse
fine-structure constant. On this evidence, **the author proposes this
value for the tables physics keeps for its fundamental dimensionless
constants.**

**The criteria the field itself applies are met point by point:**

| criterion | how it is met |
|---|---|
| dimensionless | the object is pure rational structure, no unit anywhere in its construction |
| universal | the construction is base-general — a cycle arises wherever a base meets a full-period prime, seven being the least such prime in the base humans count in — and its referent, the harmonic series, sounds in every resonant body in nature |
| exact | where the fine-structure constant must be measured, the harmonic constant is computed, every digit determined |
| structure-organizing | the label set, the anchors, and the transform are its working output, exhibited and machine-pinned above |

**Proposal: the harmonic constant belongs in the tables, beside its
electromagnetic counterpart.** A case for excluding it carries the
burden of showing which criterion it fails. The number has been in plain
sight since decimal notation began: every schoolchild meets the cycle,
every physicist meets the harmonic series, and the two sat side by side
for centuries without the label set, the collapse, or the balanced
exchange being written down. On the evidence presented and pinned here,
the author proposes the reptend sevenths, within the corpus of physics,
as **the harmonic constant**.

<div style="page-break-before:always"></div>

## References

[1] E. Midy, *De quelques propriétés des nombres et des fractions décimales périodiques*, Nantes (1836).

[2] C. F. Gauss, *Disquisitiones Arithmeticae* (1801), art. 312–318.

[3] L. E. Dickson, *History of the Theory of Numbers*, vol. I, Carnegie Institution (1919), ch. VI; G. H. Hardy, E. M. Wright, *An Introduction to the Theory of Numbers*, 6th ed., Oxford (2008), §9.

[4] H. von Helmholtz, *On the Sensations of Tone*, 2nd English ed., tr. A. J. Ellis, Longmans (1885), part I.

[5] C. Horstmann, *Navier–Stokes: A Solution on Discrete Terms*, Zenodo
preprint (2026), DOI 10.5281/zenodo.21197044.

[6] C. Horstmann, *π on Discrete Terms*, Zenodo preprint (2026), DOI
10.5281/zenodo.21205368.

[7] C. Horstmann, *The Fine-Structure Constant on Discrete Terms*,
Zenodo preprint (2026), DOI 10.5281/zenodo.21211050.

*All exact claims — the six rotations, the least-full-period fact, the
label-set exhaustion, the collapse table, the transform conservation,
and the fold: the five-halves division, the committed whole, and its
family — re-derive in the public suite, where the four exhibits are also
formalized as twenty-four theorems in Lean 4 with Mathlib:
github.com/thefirsthorstmann/g-theory-verify.*

**Version 6 — October 2026.** Terminology is revised to the series
glossary: the reptend cycle and its positional, multiplicative and
harmonic orders. The decomposition of the fine-structure constant,
reserved in earlier versions, is the subject of a companion paper [7].

<div class="copyright" style="margin-top:205pt">Copyright<br>Christian Horstmann · July 5th, 2026<br>thefirsthorstmann@gmail.com<br>All rights reserved</div>
