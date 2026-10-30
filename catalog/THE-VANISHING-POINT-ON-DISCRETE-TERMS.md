---
title: The Vanishing Point on Discrete Terms
subtitle: What 0.999… = 1 is actually about.
byline: Christian Horstmann · thefirsthorstmann@gmail.com · July 5th, 2026 · version 2, October 2026 · manuscript for the public record
date: 2026-07-05
titlenote: Within the real numbers the equality is a theorem, settled and definitional, and nothing here alters it there. The subject is what its proof assumes: a completed infinite tail and a least upper bound that no finite sequence of operations reaches. The facts about the partial sums that bear on it are pinned by a mechanical test suite accompanying the manuscript and rerun on every revision. Changes of substance from version 1 are marked † and noted where they occur.
abstract: Within the real numbers 0.999… = 1 is a theorem: the decimal denotes the limit of its partial sums 0.9, 0.99, …, and that limit is 1. The proof rests on two assumptions no finite procedure carries out: a completed infinite tail of nines, and the completeness of the real numbers, under which every bounded increasing sequence converges to its least upper bound. This paper examines the equality operationally, under the program's hypothesis that physical reality is discrete and harmonic, with no completed infinity. The suite verifies four exact results about the partial sums. Every partial sum, read as the integer of its digits, has digital root 9, and no operation performed on it reaches root 1; reaching 1 requires supplying the missing unit, which is the rounding itself. The ratio of 1 to the n-th partial sum is exactly 10ⁿ/(10ⁿ − 1), superparticular for every n, the first being 10/9, the just minor whole tone. At every finite n the identity behind the one-line proof is 10·xₙ = 9 + xₙ₋₁, and the equation 10x = 9 + x misses by exactly 9·10⁻ⁿ; it holds only of the limit. Deep partial sums agree with 1 to every finite precision, yet each differs from it by exactly 10⁻ⁿ. What physical process could supply the missing unit remains open. The paper is refuted by a partial sum whose digital root is not 9, a non-superparticular ratio, a partial sum satisfying 10x = 9 + x, or a finite test separating the limit from every deep partial sum. Every exact claim re-derives in a public suite at github.com/thefirsthorstmann/g-theory-verify.
---

## 1 · Introduction: the most asserted equation

Discussion of 0.999… = 1 divides into two positions. One holds that the
two differ, because a difference is visible at every length written. The
other holds that they are equal: in the real numbers the decimal denotes
the limit of its partial sums, that limit is 1, and the familiar
one-line proofs presuppose this. Within the real numbers the equality is
a theorem, and there the matter is settled. Its proof rests on two
assumptions that no finite procedure instantiates. It treats the
unending tail of nines as a completed object, and it takes as the
defining property of the real numbers that every bounded increasing
sequence converges to its least upper bound. Judged operationally, by
what a finite supply of operations can actually perform [4], neither can
be carried out: no process completes the tail, and no step reaches the
bound. This paper takes neither position's reading as given.
**Hypothesis (the program's): physical reality is discrete and harmonic
and admits no completed infinity, so a statement about quantity has
physical content only so far as a finite supply of operations can carry
it out.** Four exact results about the partial sums, each pinned by the
accompanying suite, show what that content is.

## 2 · Definitions

The **n-th partial sum** xₙ = 1 − 10⁻ⁿ is the decimal with n nines: x₁ =
0.9, x₂ = 0.99, and so on. Each is an exact rational, and each is a
value a finite procedure can write. The partial sums form a staircase
toward 1, one nine to each step. In the real numbers every bounded
increasing sequence converges to its least upper bound, and the decimal
0.999… is defined as the **limit** of its partial sums, which is 1;
analysis treats that limit as a completed object. The **digital root**
of a positive integer is its remainder on division by nine, with 9 in
place of 0, and the digital root of a partial sum is that of the integer
its digits form, 10ⁿ − 1. A ratio in lowest terms is **epimoric**
(superparticular) when its numerator exceeds its denominator by exactly
one. It is the form of the octave, the fifth and the fourth (2/1, 3/2,
4/3), of the two thirds of just intonation (5/4, 6/5), and of its two
whole tones (9/8, 10/9).†

<div class="vnote">† Version 1 called it the form of every named
consonance. The sixths 5/3 and 8/5 are consonances of just intonation
and are not superparticular.</div>

## 3 · The form never varies

The integer 10ⁿ − 1 formed by the digits of the n-th partial sum has
digital root 9, not approximately and not eventually but for every n
without exception. Ten leaves remainder one on division by nine, so 10ⁿ
− 1 is divisible by nine. The numeral 1 has digital root 1. Between the
two forms there is no passage: no operation performed on any partial sum
— no multiplication, no addition, no deepening of the string — carries a
root-9 numeral onto the root-1 numeral. Reaching 1 requires supplying
the missing unit 10⁻ⁿ from outside the staircase, and that is the
rounding itself: an assumption imposed on the partial sum, not an
operation any partial sum performs. The identity asserted by the theorem
therefore occurs at **no finite n**. Whatever the equality means, it is
not an event on the staircase; every step of the staircase says
otherwise, and the suite checks two hundred of them by exact arithmetic.

## 4 · The staircase of tones

What separates a partial sum from the limit is not a formless remainder.
The ratio of 1 to the n-th partial sum is exactly

**1/xₙ = 10ⁿ/(10ⁿ − 1)** — and this is epimoric for every n.

The first stair, 10/9, is not an anonymous number: it is the **minor
whole tone** of just intonation, an interval any string player can sound
and any ear can name [2]. The second, 100/99, is an interval of about
seventeen cents, the size of a comma; the third, 1000/999, is under two
cents. The staircase continues through ever-finer intervals, every one
superparticular and strictly greater than unity, descending toward
unison and never sounding it. The suite pins the exact form, the
epimoric property and the strict descent for sixty steps. Heard rather
than written, the dispute between the two positions resolves into a
statement neither would contest: **the staircase approaches unison;
unison is the limit, not a stair.** A musician states the theorem
correctly by instinct.

## 5 · The shifted tail

The most repeated proof runs: let x = 0.999…; then 10x = 9.999…;
subtract, 9x = 9, so x = 1. Its brevity rests on an assumption. For
every finite n the exact identity, pinned for every n tested, is

**10 · xₙ = 9 + xₙ₋₁,**

the *previous* partial sum, not the same one. The equation 10x = 9 + x
misses every partial sum by exactly the last digit, 9·10⁻ⁿ. It holds
only of the limit, where the tail is taken as completed and has no last
digit to miss. The proof therefore works exactly when the completed
infinite object is *already assumed to be in hand*, and at no finite n.
It is not a derivation of the equality from the partial sums; it is a
demonstration of what the limit means, given to a reader who has not
been told that the limit is in play. As teaching, it withholds the step
that carries the content; Section 7 states the theorem with that step in
view.

## 6 · The vanishing point

From the limit, the two objects are indistinguishable: for every finite
precision, every partial sum beyond some depth agrees with 1 to that
precision. The companion paper on π proved the corresponding fact for π
[3], and the suite pins it here directly. At every finite n the two
differ by exactly 10⁻ⁿ. Both facts are exact; the fallacy is in
conflating them, and it has a familiar name from drawing class. Parallel
rails appear to meet at the horizon. The popular reading of the theorem
concludes two things. The first is that the rails are *one rail*, which
is absurd at every point of the ground, where the gauge is constant. The
second is that they are *indistinguishable*, which is true only from the
horizon, **a point the notation added to the picture and no train ever
reaches.** Projective geometry adds the vanishing point deliberately, to
good effect, and analysis adds the limit deliberately, to good effect.
The error is not the addition but the forgetting: losing sight of the
fact that the meeting point belongs to the drawing, and then asserting
that the rails touch. In a world with a least count the two facts meet
physically. Once 10⁻ⁿ falls below that count no measurement
distinguishes the partial sum from 1, and the world supplies, to its own
resolution, the conditions under which the equality holds. The companion
paper on the ends of the number line develops the general position [4];
here it is enough that both of its exhibits stand pinned:
indistinguishable from the limit, distinct at every finite n.

## 7 · What the theorem is actually about

Now the equality can be read precisely, and both positions corrected
together. The real numbers are *built* — deliberately, and with
excellent reason — so that every bounded increasing sequence converges
to its least upper bound. Within that construction 0.999… and 1 name the
same number: the theorem is true and definitional, and inside the real
numbers its denial is false. But it is a statement **about the limit,
and empty of content about any partial sum**. It asserts neither that
any partial sum equals 1, nor that the staircase arrives, nor that the
forms converge digit by digit into each other; each of those claims is
false for every n, pinned. Those who assert the equality, pressed on
what they are asserting, often describe one of those false claims. The
correct claim, that the two notations name one limit in the real
numbers, is rarely stated, and the one-line proof does not teach it. The
lesson takes four sentences: here is a sequence; here is what analysis
chose to mean by its limit; under that choice the two names coincide;
the choice, with the completed object it assumes, is the theorem's
entire content. Taught that way, the equation stops being a shibboleth
and becomes what it always was — the signature of the construction, the
horizon drawn into the map. Nothing on the ground moved. What remains
open is the deeper question the rounding poses. For a partial sum to
become 1, the missing unit must appear where no operation of the
staircase supplies it. Physically that would be the appearance of a
quantity the process does not contain, comparable to an excitation of
the vacuum; whether any physical process supplies it remains open.

## 8 · What is established, and what would refute it

Established, and pinned for every n tested: the digital root 9 of every
partial sum (Section 3) and the epimoric staircase with its strict
descent (Section 4). Likewise pinned are the shifted identity 10xₙ = 9 +
xₙ₋₁ and the exact failure of 10x = 9 + x at every partial sum (Section
5). So is the agreement of deep partial sums with 1 to every finite
precision, alongside their exact distance 10⁻ⁿ from it (Section 6).
Stated as the program's hypothesis: a physical reality that is discrete
and harmonic, with no completed infinity (Section 1). Offered as
readings: the vanishing-point diagnosis of the popular understanding,
and the teaching of Section 7. Open: what physical process, if any,
supplies the missing unit (Section 7). The theorem inside the real
numbers is unaltered; what is examined is the standing of its
assumptions outside them. Four findings would each refute this paper.
They are a partial sum whose digital root is not 9, a ratio 1/xₙ that is
not superparticular, a partial sum satisfying 10x = 9 + x, and a finite
test separating the limit from every deep partial sum. Each is checkable
in seconds against the suite.

A condition that is met is recorded as a refutation and is not
reinterpreted. The program then uses the miss to find why the
construction failed, and a revised statement enters as a new one under
its own date.†

<div class="vnote">† Added in version 2.</div>

## 9 · Coda

The rails never touch, and the horizon is real as a feature of the
drawing. The equation asks only that both facts be held together.

## References

[1] G. H. Hardy, E. M. Wright, *An Introduction to the Theory of Numbers*, 6th ed., Oxford (2008) — congruences modulo nine.

[2] H. von Helmholtz, *On the Sensations of Tone*, 2nd English ed., tr. A. J. Ellis, Longmans (1885) — the just intervals; the minor tone 10/9.

[3] C. Horstmann, *π on Discrete Terms*, Zenodo preprint (2026), DOI
10.5281/zenodo.21205368 — finite precision never certifies the completed
limit.

[4] C. Horstmann, *Zero and Infinity on Discrete Terms*, Zenodo preprint
(2026), DOI 10.5281/zenodo.21209363, companion to this paper.

*All exact claims are verified in verify/test_vanishing_point.py and
rerun on every revision. It checks the digital root of two hundred
partial sums, the epimoric staircase across sixty, the
indistinguishability pins, and the shifted identity with the exact
failure of 10x = 9 + x at every partial sum.*

<div class="copyright" style="margin-top:24pt">Copyright<br>Christian Horstmann · July 5th, 2026 · version 2, October 2026<br>thefirsthorstmann@gmail.com<br>All rights reserved</div>
