%%TITLE: Visible Light on Discrete Terms
%%SUBTITLE: The band without octave equivalence, the circle that closes by mixing, and the wheel of hues read from the arithmetic of one seventh: complementary pairs from the half turn, the two triads as residues and non-residues, the white ray at 0.999999, and black as the unit shortfall.
%%META: Christian Horstmann · thefirsthorstmann@gmail.com · August 25th, 2026 · version 2, October 2026 · manuscript for the public record
%%ABSTRACT: The band of visible light spans about one octave, and vision has no octave equivalence: where a frequency and its double are both visible they are different hues, so the spectrum is a segment and not a circle. Perception closes it into a wheel through the purples, which have no wavelength and arise only by mixing the two ends. The mixing wheel has a fixed structure that no standard account derives from anything smaller than the receptor triad. It has six hues in a circle, three additive and three subtractive primaries alternating, three complementary pairs facing each other and each summing to white, and two poles, white and black. This paper exhibits the same structure in the decimal expansion of one seventh. Multiplication by ten arranges the six fractions k/7 in a circle on which the opposite fraction is the complement to one, since 10³ ≡ −1 (mod 7), and each opposite pair of blocks sums to 999999. Alternate positions split the six into the quadratic residues {1, 2, 4}, which sum to one whole, and the non-residues {3, 5, 6}, which sum to two. Taking mixing as addition and a pigment as the complement of its light, the calculus computes the standard wheel from one anchor: the hue order, the triads, the complementary pairs and every pairwise mixing law, with six namings left free. The identification of the rotations with the hues is an interpretation, and the structural findings that would refute it are named. Every exact claim re-derives in a public suite at github.com/thefirsthorstmann/g-theory-verify, where the same statements are also formalized in Lean 4.
%%
 
## 1 · Introduction

Visible light occupies a narrow band — about one octave, and under the common conventions just less than one. The edges of the band are conventional, and nothing is read in them here. What is read is a structural fact no convention moves: vision has no octave equivalence. In pitch, a frequency and its double are the same note again; in color, where a frequency and its double are both visible, they are simply different hues. The spectrum therefore offers perception a segment with two ends and no recurrence. Yet the perceived hues close into a circle. The closure runs through the purples — magenta and its neighbors — which correspond to no wavelength and arise only by mixing the segment's two ends. The circle of hues is therefore not a fact about the spectrum; it is a fact about mixing, and the object of this paper is the mixing wheel.

Color mixing has carried the same diagram for three centuries. Newton
passed the white ray through a prism, recovered it by recombination, and
divided the continuous spectrum into seven named colors — by explicit
analogy, as he records in the Opticks [1], with the seven notes of the
diatonic octave. The spectrum itself draws no lines; the count was a
reading, and it was a musical one. It was an artificial count, since a
continuum accepts any segmentation, but the direction of the borrowing
pointed somewhere real. This paper relocates it: the shared structure of
color and music is the mixing wheel's six, not the spectrum's seven, and
there it is exact. Goethe organized the mixing colors instead as a
closed wheel of six with two poles [2]. The modern accounts keep exactly
that object: three additive primaries whose lights sum to white, three
subtractive primaries that are their complements, the six alternating
around a circle, and complementary pairs facing each other across it.
The perception laboratory studies a different object, the opponent
structure of unique hues [3]; the object here is the mixing wheel.

The mixing wheel's structure is stated in every textbook, and the standard
account grounds it in the receptor triad it measures; from anything smaller
than that triad it is derived nowhere. Why six, why alternating triads, why
complements opposite, why the pair sums are white: this paper exhibits the
identical structure inside the decimal expansion of one seventh, where each
of its features is a short theorem. The
identification of arithmetic positions with hues is then stated for exactly
what it is — an interpretation, with its freedom declared — and the
conditions that would promote or refute it are given.

## 2 · The six rotations and their circle

The reciprocal 1/7 repeats with period six, and the six fractions k/7 are the
six cyclic rotations of the one block:

| k | k/7, first period | starts at |
|---|---|---|
| 1 | 0.142857… | 1 |
| 2 | 0.285714… | 2 |
| 3 | 0.428571… | 4 |
| 4 | 0.571428… | 5 |
| 5 | 0.714285… | 7 |
| 6 | 0.857142… | 8 |

Multiplication by ten advances the expansion one digit, and on the residues
it runs the cycle 1 → 3 → 2 → 6 → 4 → 5 → 1. That cycle is the wheel: the six
sevenths in the order the register itself visits them. Nothing is arranged by
hand; the circle is the orbit of ten acting on the residues of seven.

## 3 · The half turn is negation: the complementary pairs

**Theorem 1.** On the wheel of §2, the fraction diametrically opposite k/7 is
(7−k)/7, and the two six-digit blocks sum to 999999.

The proof is one congruence: 10³ ≡ −1 (mod 7). Three steps of the wheel —
the half turn — carry k to −k, so opposite positions are complements to one.
That opposite digits of the block sum to nine, and opposite blocks to
999999, is Midy's theorem for the period-six reptend. The three antipodal
pairs are (1, 6), (3, 4), (2, 5): every pair sums to 7 on the residues and
to 999999 on the blocks.

This is the complementary-pair law of the mixing wheel, as arithmetic.
Complementary hues stand opposite; complementary lights sum to white. On the
wheel of §2 the opposite position is the complement to one, and the sum of
every opposite pair is the same total, one unit short of unity at the sixth
place. The correspondence requires no geometry to be imposed on the
fractions: the half turn negates because the period is six and ten cubed
falls on minus one.

## 4 · The two triads: residues and non-residues

**Theorem 2.** Alternate positions of the wheel split the six into {1, 2, 4}
and {3, 5, 6}: the quadratic residues of seven and its non-residues. The
residue triad sums to 7, one whole; the non-residue triad sums to 14, two
wholes.

The wheel's positions at even steps are the powers of 100, and 100 ≡ 2
(mod 7), so the even positions are the orbit of 2 — which is the residue
subgroup {1, 2, 4}. The odd positions are its coset. Drawn on the circle the
two triads are two interleaved equilateral triangles, and each triangle's
members pair across the circle with the other triangle's: every complement
of a residue is a non-residue, since −1 is a non-residue of seven.

This is the two-triad law of the mixing wheel: three additive primaries and
three subtractive, alternating around the circle, with every hue's
complement belonging to the opposite triad. On the wheel it is the subgroup
and its coset, and the asymmetry of the two triads is not decorative — one
sums to a single whole and the other to two. The roles are therefore not
assignable: only the residue triad sums to unity, so which three positions
carry the additive office is decided by the arithmetic, and only the naming
within each office remains free.

## 5 · White and black

The poles of the wheel are not hues, and the arithmetic states them exactly.
Each complementary pair sums to 0.999999 — the register's closure value at
depth six, one unit short of unity. The full palette of six sums to three:
three whites, one per pair, short of 3 by exactly three units at the sixth
place. And the complement of white is the residue itself:

```
0.999999 + 0.000001 = 1
```

The mixing calculus closes on both poles, exactly. Each subtractive
fraction is one minus an additive light — 3/7 = 1 − 4/7, 5/7 = 1 − 2/7,
6/7 = 1 − 1/7 — so a pigment is precisely the removal of its complementary
light. The three additive lights sum to unity: white by addition. The three
pigments jointly remove the three lights, the removal of exactly one whole:
black by subtraction. At the register's depth the closed unit never
displays — the window shows 999999 — and the difference between the
displayed white and the closed one is the residue itself.

White is the sum every opposite pair reaches; black is the one address no
mixing reaches — the unit that closure lacks. The pair (white, black) is the
only pair on the page whose sum is exactly one, and neither member is a
rotation of the block. The poles stand off the wheel, as they do in the
diagram color practice has always drawn.

One cross-reference is recorded as an interpretation. The unit shortfall
at the register's depth, the 0.000001 by which the multiples of one
seventh fall short of closure, is the same residue the gravity record
identifies with the deficit that sources the pull. Read through the
present wheel, black and the gravitational deficit are the same residue.

## 6 · The wheel, computed

The identification of §9 can be put to work before it is judged, because
the calculus computes. Take the mixing law to be addition of the
fractions, a pigment to be the complement of its light, and white to be
unity. Three theorems follow, none with a free step.

**Theorem 3 (two lights make the opposite pigment).** For the additive
triad {1/7, 2/7, 4/7}, the sum of any two members is the complement of
the third, since the triad sums to unity: 1/7 + 2/7 = 3/7 = 1 − 4/7,
and likewise for the other pairs. Under the anchor that names 1/7
red, 2/7 green and 4/7 blue, the three instances read: red and green
make yellow; green and blue make cyan; blue and red make magenta. This
is the additive pairwise law of the standard wheel, exact.

**Theorem 4 (two pigments leave the third light).** Removing two lights
from white leaves the third: 1 − r_i − r_j = r_k. Read subtractively:
cyan and magenta leave blue; magenta and yellow leave red; yellow and
cyan leave green — the subtractive pairwise law, exact.

**Theorem 5 (the order is the mixing order).** On the orbit of ten —
1, 3, 2, 6, 4, 5 — each non-residue sits between exactly the two
residues that sum to it: 3 between 1 and 2, 6 between 2 and 4, 5
between 4 and 1. The register's own multiplicative order places every
secondary between its two parents. That is the adjacency law of the
standard wheel: yellow between red and green, cyan between green and
blue, magenta between blue and red.

**Corollary (the wheel entire).** Fix one anchor — which residue is
called red — and one orientation. Every remaining assignment is then
determined, and the computed wheel reproduces the standard wheel in
full. It gives the hue order red, yellow, green, cyan, blue, magenta
around the circle; the additive and subtractive triads; the
complementary pairs red–cyan, green–magenta, blue–yellow; and every
mixing identity above. The closure is included: magenta, the one
secondary that corresponds to no wavelength, is computed as the sum of
the segment's two ends, so the circle closes in the arithmetic exactly
where the spectrum cannot close it. The freedom declared in §9 is
thereby located exactly: which residue is named red, and the
orientation, six assignments,† and nothing else; all relations are
computed.

<div class="vnote">† Version 1 counted twelve assignments, the full
symmetry of the hexagon; the six that keep the additive triad on the
residues are the free ones.</div>

These identities reproduce established mixing behavior and show the
identification's coherence under calculation; the constraint that would
take the reading past coherence remains the one named in §9.

## 7 · In relation to electromagnetism

Visible light is electromagnetic radiation, and the companion records
derive the field's structure from the same six-digit constant this paper
reads. There, the block 142857 has two canonical orderings: the
positional order that division writes, and the multiplicative order that
doubling walks. The companion records identify the pair with the
electric and magnetic faces of the field (The Origin on Discrete Terms,
DOI 10.5281/zenodo.21212112; Gravity on Discrete Terms, DOI
10.5281/zenodo.22087599). The faces are the read face and the
circulation face, exchanged by an involution that is its own inverse,
and radiation begins at the dipole. Here, the same block is read by its
fractions: the six sevenths as the wheel of hues. One constant carries
both readings. The orderings give the field its two faces; the rotations
give its visible radiation the six hues; and neither reading borrows
from the other — each is derived where it is derived.

One structural echo is recorded as an observation. The faces are
exchanged by an involution, and the wheel's complementation is the half
turn, likewise its own inverse: two order-two moves on the one constant.
The parallel is noted and nothing rests on it. What is exhibited is one
arithmetic object underlying two accounts; a derivation of the field
equations from it is open.

## 8 · In relation to the quantum of light

A photon has a frequency and no hue. Color does not exist at the level
of the single quantum; it begins where counting begins — at the receptor
triad, whose three tallies are the tristimulus values of standard
colorimetry [4]. Color is a property of a three-channel count, not of
the light alone, and the standard account states as much: matching any
visible spectrum requires exactly three numbers.

The count is many-to-one, and its many-to-one has a name: metamerism.
Infinitely many spectra produce the same three tallies and are one
color, indistinguishable in principle to the instrument that counts
them. In the vocabulary of this series that is commitment — the eye is a
counting instrument, and a color is what remains after its count. The
reading is labeled as one; the colorimetry it reads is the standard
science.

This locates the calculus precisely, and answers the question of its use.
Wavelength arithmetic cannot carry the wheel, because the wheel does not
live in the spectrum: §1's segment has two ends and no circle. The wheel
lives in the quotient the count creates, and that is exactly where the
calculus of §6 computes — exact fractions for the classes, exact sums for
the mixtures, both poles closed. What can be calculated with the sevenths
is the complete mixing structure of visible color, from one fraction, with
no continuous apparatus: demonstrated in §6 rather than asserted.

The standard treatment reaches the same wheel through the continuum: color
as a vector in a real three-dimensional space, built on measured matching
functions, with the wheel's laws holding as observed regularities of that
apparatus. The calculus reaches them as exact identities of one fraction —
nothing measured, nothing rounded, no space larger than the six classes and
their sums. For the wheel's structural laws the two routes agree term for
term; the difference is economy and status. What the continuous route
carries as empirical regularity, the fraction carries as arithmetic
necessity, and what it computes, it computes exactly.

Why the count has three channels remains open: the calculus takes the
triad of channels as the standard science gives it. The subtractive
mechanism, finally, is the complement identity made physical. A pigment
absorbs its complementary band and transmits the rest, photon by photon,
and 1 − light is that removal stated exactly.

## 9 · What is established, and what is read

The arithmetic of §§2–6 is exact and machine checked. The wheel is the orbit
of ten; the half turn negates; opposite blocks sum to 999999; the triads are
the residue subgroup and its coset with sums 7 and 14; white plus black is
one. The mixing theorems of §6 compute the standard wheel entire from
one anchor. None of it is adjustable.

The identification — six rotations as the six hues, pair sums as the
white ray, the residue as black — is an interpretation, and its freedom
is declared rather than hidden. It does not rest on a resemblance of
diagrams, and the reason deserves its own sentence: the two sixes factor
identically, with matched offices. The wheel of color is, on its own
terms, two times three — the additive–subtractive polarity times the
triad of primaries. The hexad is Z/2 × Z/3 with the same assignment: the
polarity component is the Midy pairing, the triad component is the
residue split. What is identified is one factorization in two
realizations, not one picture beside another. The arithmetic fixes the
structure and more: six positions on a circle, three antipodal
complementary pairs, two interleaved triads, which triad carries the
additive office, and the mixing sums that reach both poles. What it
leaves free is only the naming — which residue is called red — a freedom
of rotation and reflection within each office. That is the same division
every color system makes when it sets its zero of hue angle by
convention; relations and mixtures are defined exactly, names
conventionally. An interpretation with the naming freedom describes the
wheel and computes its mixtures; it does not yet forbid a measurement.
What would promote it is a constraint: a quantitative statement about
mixing or about hue spacing that the arithmetic requires and measurement
could refuse. No such constraint is yet known, and finding one is the
open problem. What would refute the reading as it stands is structural.
A mixing wheel of color with complements that do not sum to white, or
whose primary triads do not interleave, would leave the arithmetic with
nothing to name; no such wheel is in use.

A finding of either kind is recorded as a refutation and is not
reinterpreted. The program then uses the miss to find why the
construction failed, and a revised statement enters as a new one under
its own date.†

<div class="vnote">† Added in version 2.</div>

**Violet, the last spectral hue, is held as a signpost.** One spectral
hue asks for a seventh reading. Violet stands at the segment's short
end, and perception tinges it with the other end: violet is seen as
reddish blue, the standard hue circle bending the segment's short end
back toward the long. The last visible hue is already seen with a trace
of red. The observation is perceptual and standard, and its mechanism
remains open. The scale of the companion records carries a matching
absence. The harmonic seventh, 7/4, is the tone the diatonic figure
never occupies: on the lattice of 24 its place is 42, between the
submediant at 40 and the leading tone at 45. The gap between the two
musical sevenths is the septimal comma, the crossing from the world of
two and three into the world of seven. Whether violet is rightly read as
the wheel's unoccupied seventh, the hue of the address before closure,
as 7/4 is the tone before the octave that the figure's positions leave
out, is recorded as a signpost and nothing more.

Newton's precedent bounds the claim from the other side. His seven
spectral names were chosen to match the octave, and the choice was
fertile for three centuries while deriving nothing. A reading of color
from arithmetic must therefore expect to establish its standing the slow
way, by finding the constraint the wheel imposes; this paper contributes
the structure and the statement of what remains open.

## 10 · Verification

Every arithmetic statement in this paper is encoded as a re-runnable
test in `verify/test_the_color_wheel.py` within the program's suite. The
battery covers the six rotations, the orbit order, the half-turn
negation, the three pair sums, the residue split with its two totals,
and the closure values of white and black. The same statements, with the
count of the free namings, are formalized as eight theorems in Lean 4
with Mathlib. The battery, the Lean file and the source of this paper
are all public, at github.com/thefirsthorstmann/g-theory-verify. The
identification of §9 pins nothing; it is the part of the paper that is
read rather than proved, and it is labeled where it stands.

---

*Companions: Gravity on Discrete Terms, the unit shortfall as the
deficit, DOI 10.5281/zenodo.22087599 · Tonal Function on Discrete Terms,
the functions of the scale from the same positions, DOI
10.5281/zenodo.22119146 · The Seventh — A Constant Hidden in Plain Sight,
the reptend itself, DOI 10.5281/zenodo.21206863 · The Origin on Discrete
Terms, the figure, DOI 10.5281/zenodo.21212112.*

*References: [1] I. Newton, Opticks (1704) · [2] J. W. von Goethe, Zur
Farbenlehre (1810) · [3] E. Hering, Grundzüge der Lehre vom Lichtsinn
(1920); L. M. Hurvich, D. Jameson, Psychological Review 64 (1957) 384 ·
[4] G. Wyszecki, W. S. Stiles, Color Science, 2nd edition (1982).*

<div class="copyright" style="margin-top:24pt">Copyright<br>Christian Horstmann · August 25th, 2026 · version 2, October 2026<br>thefirsthorstmann@gmail.com<br>All rights reserved</div>
