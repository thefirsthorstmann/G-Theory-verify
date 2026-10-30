%%TITLE: Tonal Function on Discrete Terms
%%SUBTITLE: Why the scale pulls: the diatonic functions derived from the arithmetic of the positions — the unique root theorem, the two joints, the mirror that exchanges dominant and subdominant, the cadence that uses one three and one two, and the physical offices the functions already hold in the companion records.
%%META: Christian Horstmann · thefirsthorstmann@gmail.com · August 25th, 2026 · version 2, October 2026 · manuscript for the public record
%%ABSTRACT: Tonal function is the observation that the degrees of a scale are not interchangeable: each carries a characteristic office, stable across repertoires and listeners. The standard accounts, the fundamental bass of Rameau, the three functions of Riemann and the probe-tone hierarchies of Krumhansl, describe the offices with precision but take function as primitive. This paper derives the offices from arithmetic, using only the exact ratios of the tones in the companion records. Four theorems carry the derivation. First, a pitch-class set supports a unique tonic only if no transposition maps it onto itself. The diatonic and pentatonic sets pass; the whole-tone, octatonic and chromatic sets, Messiaen's modes of limited transposition, cannot name a root on their own arithmetic. Second, the diatonic step word has exactly two semitone steps, from the mediant to the subdominant and from the leading tone to the tonic, where functional harmony moves; the whole-tone word has none. Third, the reflection that exchanges tonic and dominant carries the major set onto its parallel minor and the dominant seventh onto the minor subdominant with added sixth: dominant and subdominant are one object in two orientations. Fourth, the tritone of the dominant seventh spans the one unoccupied position of the ring and resolves by two just semitones in contrary motion, three units up and two down. A table states the physical office each function holds in the companion records, and each section carries its conditions of refutation. Every arithmetic claim re-derives in a public suite at github.com/thefirsthorstmann/g-theory-verify. These claims are also formalized there in Lean 4.
%%
 
## 1 · Introduction

Tonal function has three standard accounts. Rameau derived harmony from
the fundamental bass [1]; Riemann organized it into three functions [2];
the perception laboratory, after Krumhansl, measures the stability
hierarchies directly [3]. Each describes the offices of the degrees, and
none derives why exactly these degrees carry exactly these offices; §12
states the relation of this paper to each.

The companion records derived the form of gravitation, its coupling and
the vacuum's structure from the arithmetic of the reptend 1/7 =
0.142857…, on the nine-position figure of the series, with the tones at
exact ratios.† They used tonal function throughout, the station of the
subdominant, the rest at the submediant and the axis of the leading
tone, and derived it nowhere. This paper derives it in six parts. A
unique tonic is decided by a symmetry count: a theorem. Function is
located at the two semitone joints: a theorem. Dominant and subdominant
are related by a reflection: a theorem. The authentic cadence applies
one unit of each generator: a theorem on the lattice the series fixed
before this paper. Each function holds a named physical office in the
companion records: a table, with its grammar stated. The measured
perceptual hierarchy is consonant with the arithmetic: an observation.
The dimensional boundary of the Units record holds throughout: none of
this yields a magnitude.

<div class="vnote">† Version 1 said seats for positions, and ledger in
Theorem 4's name.</div>

## 2 · The positions, inherited

The figure's tones stand where the companion records put them: each
descending ratio times the full turn is the position in degrees, and the
octave on 24 carries the ascending numbers.

| tone | ascending, on 24 | interval from Do | descending ratio | position |
|---|---|---|---|---|
| Do | 24 | 1 | 0 | 0° |
| Re | 27 | 9/8 | 1/8 | 45° |
| Mi | 30 | 5/4 | 1/4 | 90° |
| Fa | 32 | 4/3 | 1/3 | 120° |
| Sol | 36 | 3/2 | 1/2 | 180° |
| La | 40 | 5/3 | 2/3 | 240° |
| Si | 45 | 15/8 | 7/8 | 315° |
| Do | 48 | 2 | 1 | 360° |

Nothing here is new; the table is the companion records' object,
restated so that this paper is self-contained. Two entries do this
paper's work. The submediant's descending ratio is 2/3, the fifth 3/2
read in reversal, which is why the submediant and no other degree is the
relative rest. And no tone stands between the subdominant and the
dominant: the tritone, 45/32, has no position, and §6 is about what
music does with an address the figure leaves unoccupied.

## 3 · The functions, defined

Tonal function is the observed fact that each degree of the scale
carries a characteristic office, stable across melodies, keys, centuries
and listeners. The traditional names, with what the ear hears at each,
are these. The tonic (Do) is heard as rest. The dominant (Sol), a fifth
above it, is heard as tension that seeks the tonic. The subdominant
(Fa), a fifth below, is heard as a move away from rest that prepares the
dominant. The submediant (La) is the root of the relative minor, and the
leading tone (Si), a semitone below the tonic, is heard as pulling up to
it. The standard accounts describe these offices. This paper locates the
offices in the arithmetic, as follows, with the derivations in §§4–6:

**Definition.** On the ring of twelve positions, negation — the
reflection through the root — fixes exactly two positions: 0 and 6.
**The Tonic is the occupied fixed point.** The scale sits on 0 and omits
6: **the tritone position is the empty fixed point**, the one address
negation preserves and the scale declines. **Dominant function is the
activation of the empty fixed point**: the chord of the fifth degree
with its seventh contains the interval that spans the ring's diameter
through position 6 without occupying it. **Subdominant function is the
Dominant's mirror image**, by §5. **The submediant is the position of
the reversal**: the one degree whose descending address is the fifth
read backwards. **The leading tone is the joint that leads**, by §4: the
upper of the two semitone joints, one step below closure.

These definitions have content: each names an arithmetic property a
degree has or lacks, and the theorems below show that the properties
select exactly the traditional offices.

## 4 · The unique root, and the two joints

**Theorem 1 (the unique root condition).** A pitch class set supports a unique
tonic only if its transpositional stabilizer is trivial — only if no nonzero
shift of the ring maps the set onto itself. If a shift t fixes the set, every
candidate root has an indistinguishable alternative at distance t, and no interior
evidence can decide between them.

The count, run on the standing scales: the diatonic set and the pentatonic set
are fixed by no shift — a unique root is nameable in both. The whole tone set is
fixed by six shifts, the octatonic by four, the full chromatic by all twelve.
These are the scales of limited transposition, and on their own arithmetic the
root is six-, four- and twelve-fold ambiguous: **tonal function in them is not
difficult but impossible**, forbidden at the level of the set before any note
sounds.

The corroboration, which is not part of the proof, is three centuries of
practice. Whole tone writing floats and is prized for floating; the
octatonic is the standard resource for suspended tonality; the
undifferentiated chromatic is atonality's home. And Messiaen, who
catalogued these sets [4], named them for exactly the property the
theorem counts — the limitation of their transpositions.

The condition is necessary and not sufficient; what directs a set that
passes it is the joint structure:

**Theorem 2 (the two joints).** The diatonic step word is 2 2 1 2 2 2 1:
exactly two semitone steps, the joints, and they fall at Mi–Fa and at
Si–Do. The whole tone word is 2 2 2 2 2 2: no joint at all.

**Function is located at the joints.** The joint at Si–Do belongs to the
leading tone: one step below closure, the strongest tendency in the
scale, and the upper voice of every authentic cadence. The joint at
Mi–Fa belongs to the subdominant: the place where the gravity record
locates the shortfall of one sign that sources the pull. A scale with no
joints has no step of tendency, which is Theorem 1's whole-tone floating
restated mechanically. Together the two theorems give the first
conclusion: **a scale has function when it can name its root and has
joints to move through, and the diatonic seven is the standing set that
does both.**

## 5 · The mirror: the relative behaviour of the functions

**Theorem 3 (the reflection).** The reflection of the ring through the axis at
the midpoint between Do and Sol — the axis that exchanges the two — carries the
major set onto its parallel natural minor. The same reflection carries the
dominant seventh — Sol, Si, Re, Fa — onto the set Do, Le, Fa, Re: the
subdominant minor chord with added sixth.

The consequences are the relative behaviours the musician already navigates.
**Dominant and subdominant are one object in two orientations**: the chord that
presses toward the tonic from the fifth above and the chord that settles onto it
from the fifth below are mirror images, exactly. This is why the authentic and
plagal cadences feel like two directions of one move. It is also why the
traditional account needed exactly three functions and no fourth: tonic, and
one function read twice.

The same reflection runs through the harmonic series itself. Take the
recipe "the first three prime partials of Do" and run it upward:
partials 2, 3 and 5, reduced by octaves, give Do–Sol–Mi — the major
triad, the overtone chord, the dominant side. Run the identical recipe
downward — divisors 2, 3 and 5, raised by octaves — and it gives
Do–Fa–Le: the minor triad on the subdominant side. One recipe, two
directions; the major and minor sonorities are the mirror pair of §5
heard as ratio, and each undertone address is exactly the octave over
its overtone partner: 4/3 = 2 ÷ 3/2, 8/5 = 2 ÷ 5/4. What is claimed here
is the arithmetic and only the arithmetic: whether any physical system
sounds an undertone series is a separate and contested question, and it
remains open here. The ratios mirror, and that is checked in a line.

Two further relative facts complete the section, both exact on the
lattice on 24. **The fifth below is the fourth above**: 48 × 2/3 = 32 =
24 × 4/3. Descending Sol lands on Fa's own number, so the subdominant is
the dominant heard from the octave above, one position with two
approaches. **And the submediant is the position of the reversal**: 48 ×
5/6 = 40 = 24 × 5/3, the degree at 240° whose descending address is 2/3,
the fifth read backwards. This is why the relative minor rests there. It
is also why the gravity record and the Vacuum place the same 2/3 as the
vacuum's fraction of the cosmological budget (Gravity, §14; the Vacuum,
§3).

## 6 · The cadence uses one three and one two

**The authentic cadence resolves the dominant seventh to the tonic, and
its unrest has a single source.** The chord contains Si against Fa, the
tritone, the interval that spans the ring's diameter through the empty
fixed point. On the lattice the interval is 45 against 32, the ratio
45/32: **the one address the figure never occupies**, lying between the
subdominant's 4/3 and the dominant's 3/2. The chord does not stand on
the empty fixed point, since no tone does; it spans it, and the span is
the tension.

**Theorem 4 (the resolution's count).** The tritone resolves by contrary
motion, both voices moving the same just semitone 16/15: Si rises 45 →
48 and Fa falls 32 → 30. In lattice units the voices move +3 and −2 —
one unit of each generator, in opposite directions — and the opened
interval is 45/32 × (16/15)² = 8/5, the Mi–Do frame of the tonic chord.

**The cadence moves one voice by a three and one by a two.** The two
whole numbers out of which every ratio in this series is built are 2
and 3. The authentic cadence, the move common-practice harmony uses as
the sound of arrival, moves one voice up by exactly a 3 and one voice
down by exactly a 2. The pull heard at the dominant seventh is the
arithmetic's own pair, enacted in contrary motion through the one
address the figure leaves unoccupied. The gravity record derived a
force from a one-signed shortfall at the subdominant; this is the same
grammar at the scale of a phrase. **Tension is an unoccupied address,
resolution is the application of the generators, and arrival is the
occupied fixed point.**

**A structural parallel lies one layer deeper.** The reptend cycles of
the series carry two families of moduli: the all-nines integers, which
close a period, and their companions of the form 10ʰ + 1, which negate
one. Return and crossing are the two faces of every cycle of even
period, since 10²ʰ − 1 = (10ʰ − 1)(10ʰ + 1). The authentic cadence is a
crossing: it passes through the diameter, the half turn, the negation;
the plagal cadence, the mirror's cadence, arrives without crossing. That
the two cadences of common practice align with the two families of
moduli is recorded as a reading of the same arithmetic. The arithmetic
itself, the factorization of every even period into closure times
negation, is exact and machine-checked in the suite.

## 7 · The two cycles stand a fourth apart

The two working cycles of the program are the reptend cycle of the
sevenths, period six, and the cycle of 137, period eight. Each closes at
its all-nines integer, 999999 and 99999999, whose digit sums are 54 and
72, and the ratio of the two, like that of the periods, is 72/54 = 4/3:
**the interval of the subdominant. The two cycles of the series stand in
subdominant relation to one another**, a fourth apart, the interval
Theorem 2 places at the first joint. The observation forbids nothing; it
is recorded because the two central objects of the series stand in one
of the relations this paper derives.

## 8 · The physical offices, made explicit

The companion records did not use tonal vocabulary as ornament; the
functions hold offices in the physics, and this section states the
translation as a process that can be checked rather than a resemblance
that can be admired.

**The translation from a ratio to an office takes four steps.** Read the
ratio operationally: multiply and divide separately, count the
operations in the two generators, and find the residue, which is where
the work lies. Place it: the descending ratio times the full turn gives
its position on the figure. Name its function by the dictionary of §3,
now derived. Then, and only then, read its office: the function names
what the quantity does in the mechanism, and the claim is falsified
wherever the office and the mechanism disagree.

| position | function | physical office | where established |
|---|---|---|---|
| Fa, 4/3, the first joint | the subdominant | the shortfall of one sign that sources gravitation; F ∝ M and the equivalence principle from its congruence | Gravity, §§5–6 |
| the two fixed points, 0 and 6 | tonic and the empty position | the fixed stratum — the only two places no mode moves — where the deficit is read | Gravity, Part I |
| 45/32, the address never occupied | the dominant's tension | the excluded address, spanned in tension | the table of positions, §2; the Origin, the figure |
| La, 2/3, the reversal | the submediant, the relative rest | the vacuum's fraction: Ω_Λ = 2/3 exactly, one unsourced unit per horizon | Gravity, §14; the Vacuum, §3 |
| Si–Do, the second joint | the leading tone | the final semitone of closure; the shortfall of one at the period's close | Gravity, §4 |
| the step word's asymmetry | function's possibility | the floor's asymmetry; the shortfall of one sign that makes the vacuum's energy positive | Gravity, §§4, 14 |

The table is the point of the paper for the physicist reader, so its
logic is worth one paragraph of prose. In the standard account, that the
universe gravitates, that its vacuum energy is small and positive, and
that its scale structure is asymmetric are three unexplained facts. That
a scale pulls toward its tonic is a fourth fact, unrelated, filed under
psychology. On discrete terms the four are one grammar. The same
arithmetic that gives the subdominant its tendency makes mass gather.
The same reversal that places the relative minor places the vacuum's
fraction, and the same asymmetry that lets a melody end lets the floor
of the universe hold a sign. Music is not being used to describe physics
here, nor physics to dignify music: both are readings of the positions,
and the positions are arithmetic.

## 9 · The perceptual characteristics, noted

Two bodies of observation stand beside the derivation. They are
consonant with it, and whether they follow from it is open.

**The measured hierarchy of stability orders the degrees as the
arithmetic does.** The perception laboratory has quantified tonal
function for four decades with the probe-tone method of Krumhansl and
colleagues [3]: play a context that establishes a key, sound a probe
tone, and ask listeners to rate its stability. The obtained profiles are
the standard result of the field, replicated across training levels and
cultures with variations that are themselves studied. They order the
degrees: the tonic most stable, then the fifth, then the third, then the
remaining scale tones, then the chromatic residue. That ordering is the
arithmetic's: the occupied fixed point first, then the overtone triad,
then the occupied degrees, then the unoccupied addresses. The consonance
is noted at exactly that strength. What would make it more than
consonance — a perceptual experiment whose design is derived from the
table of positions and whose outcome the arithmetic constrains in
advance — is proposed in §11 as this paper's own test.

**The same forms reach the eye, and the pattern is held as a signpost.**
These series are mathematics felt in sound before they are mathematics
seen on paper — that is the fact of the psychology, however it is
finally explained. But the same structures are not confined to sound.
The companion records read the electromagnetic and gravitational forms
out of first order directivity — the monopole and dipole whose sum is
the cardioid — and the figure's own geometry is the spiral of positions
this paper's table walks. Where a material pattern in nature displays
spiral or cardioid structure, the series' characteristics are available
to the eye as they are to the ear. The definiteness of the perceptual
response in both channels is recorded here as a signpost. It suggests an
understanding of perception's relation to these forms deeper than this
paper derives, and it is left standing as exactly that.

## 10 · Interlude: for the musician

*The companion records carry interludes teaching tonality to the
physicist. This one runs the other way.*

A coupling constant is physics' name for how hard something pulls,
written as a pure number. The gravitational coupling of the electron —
how hard two electrons gravitate, compared with everything else they do
— is a number so small it takes forty-five digits to write. The standard
account can only measure it and file it. The gravity record shows that
it is not an arbitrary number: it is a five circulating on a cycle one
hundred and fifty-one places long — a single tone, held on a very long
string. You already have the skill this series runs on. When you hear a
dominant seventh and know, before it moves, where it must go, you are
reading unoccupied addresses and counting what closure requires — the
same reading this series does on the constants of nature. The claim of
these papers, said for the player: the universe's numbers behave like
voices, because voices and numbers are both built from two and three,
and nothing built from two and three gets to be arbitrary.

One theorist deserves naming in this interlude. George Russell's *Lydian
Chromatic Concept of Tonal Organization* (1953) [5] organized harmony
around what he called tonal gravity: the pull of every tone toward a
tonic. He located its source in the ladder of fifths, the same generator
this paper counts, and the gravity record — which reads the
gravitational field as a tonal center — meets his phrase from the other
side, seven decades on. The difference is structural and instructive.
Russell generates his parent scale one-sidedly, by consecutive fifths
upward from the tonic; this yields the Lydian set and omits the
subdominant. The present construction places the diatonic set
two-sidedly, one generator step below the tonic and five above. The
mirror of Theorem 3, dominant and subdominant as one object in two
orientations, lies exactly in the step his stack omits. On this account
his instinct was arithmetic fact, and the two-sided placement is what
makes it provable.

## 11 · What would refute this

1. **Theorem 1.** A repertoire establishing functional harmony — cadential
   arrival distinguishable by listeners at better than chance — inside a scale
   of limited transposition, without tones from outside it, refutes
   the unique root condition. None exists; the theorem forbids one.
2. **Theorem 2.** A functional idiom whose characteristic motions avoid the
   semitone joints — whose cadences move only by whole tone — refutes the
   joint location. The standing repertoires do the opposite.
3. **Theorem 3 and the triads.** The reflection identities are a line of
   arithmetic each; an error in any is decisive and checkable by hand.
4. **Theorem 4.** The count is exact on the lattice: if the just
  cadence's voices do not move 16/15 in contrary motion applying +3 and
  −2, the resolution reading fails. The check is four integers.
5. **The offices.** The table of §8 falls wherever a companion record's
  mechanism falls; it has no standing independent of those mechanisms.
6. **The proposed test.** Construct probe contexts in scales whose stabilizers
   differ — diatonic, pentatonic, whole tone, octatonic — and measure root
   inference. The arithmetic requires: unique root scales yield convergent
   root judgements; scales of limited transposition yield judgements split among
   the stabilizer's orbit, six ways and four ways respectively. A measured
   unique root, convergent across listeners, inside the whole tone set would
   refute Theorem 1 in the laboratory as surely as a repertoire would in the
   literature.

A condition that is met is recorded as a refutation and is not
reinterpreted. The program then uses the miss to find why the
construction failed, and a revised statement enters as a new one under
its own date.†

<div class="vnote">† Added in version 2.</div>

## 12 · Relation to the standard accounts

Rameau derived harmony from the fundamental bass and the corps sonore
[1]. Riemann gave the three functions [2] and proposed the undertone
dualism his critics took a century contesting. The negative-harmony
tradition after Levy [6] rediscovered the mirror as a compositional
resource, and the perception laboratory measured the hierarchies. To
each, this paper adds the same two things. A derivation: the offices
follow from a symmetry count, a step word, a reflection and a
four-integer count, on positions the companion records fixed for other
reasons entirely. And a prohibition: no scale of limited transposition
supports a unique tonic — a forbidding sentence none of the standard
accounts states, because none of them counts stabilizers. Where
Riemann's dualism claimed a sounding undertone series and was refutable
there, the mirror here is arithmetic and is refutable only as
arithmetic. Where the perceptual profiles are measurements in search of
a mechanism, the mechanism proposed is the table of positions, and §11.6
states the experiment that would test it.

## 13 · Verification

Every arithmetic statement in this paper is encoded as a re-runnable
test in `verify/test_tonal_function.py`. The battery covers the table of
positions, the stabilizer counts, the step words and joint locations,
the reflection images, the over- and undertone reductions, the cadential
count, the identity of the fifth below, and the cycles' fourth. The same
statements are formalized as ten theorems in Lean 4 with Mathlib. The
battery, the Lean file and this paper's source are public at
github.com/thefirsthorstmann/g-theory-verify. The two observations of §9
cite the standard results they rest on and pin nothing; the reading in
§6's final paragraph is labelled where it stands; and the derivations
use no quantity the companion records had not already fixed.

---

*Companions: Gravity on Discrete Terms, the form, the coupling and the
interlude on tonality for the physicist, DOI 10.5281/zenodo.22087599 ·
The Origin on Discrete Terms, the figure, DOI 10.5281/zenodo.21212112 ·
Units on Discrete Terms, the dimensional boundary, DOI
10.5281/zenodo.22119360 · The Vacuum on Discrete Terms, the drone, DOI
10.5281/zenodo.22119287.*

*References: [1] J.-Ph. Rameau, Traité de l'harmonie (1722) · [2] H.
Riemann, Vereinfachte Harmonielehre (1893) · [3] C. L. Krumhansl, E. J.
Kessler, Psychological Review 89 (1982) 334; C. L. Krumhansl, Cognitive
Foundations of Musical Pitch (1990) · [4] O. Messiaen, Technique de mon
langage musical (1944) · [5] G. Russell, The Lydian Chromatic Concept of
Tonal Organization (1953) · [6] E. Levy, A Theory of Harmony (1985).*

<div class="copyright" style="margin-top:24pt">Copyright<br>Christian Horstmann · August 25th, 2026 · version 2, October 2026<br>thefirsthorstmann@gmail.com<br>All rights reserved</div>
