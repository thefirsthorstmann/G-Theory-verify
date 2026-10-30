%%TITLE: The Vacuum on Discrete Terms
%%SUBTITLE: The cosmological term as a boundary count: its sign, its equation of state, and the redshift at which the measured fraction crossed two thirds
%%META: Christian Horstmann · thefirsthorstmann@gmail.com · August 25th, 2026 · version 2, October 2026 · manuscript for the public record
%%ABSTRACT: Computed as a field-theoretic zero-point sum, the vacuum energy density exceeds the value inferred from observation by about a hundred and twenty orders of magnitude. This paper argues that the sum is the wrong calculation: on a discrete register the cosmological term is a boundary count, and no sum exists to diverge. Five results are given. The vacuum is the unsourced tier of the shortfall theorem, which fixes its sign as positive and its equation of state at w = −1 at every redshift, since the term arises as a constant of integration. One Planck density distributed over the horizon's count of Planck cells is exactly the statement that the dark-energy fraction has the rest value 2/3. The measured fraction exceeds it by 2.7 percent on the Planck 2018 fit and by 5.4 percent on the fit to DESI's second data release. The excess equals the sweep rate −3 Ω_Λ Ω_m times the elapsed sweep, on both datasets to better than one percent, so it is a clock reading. The present epoch is proved to be the single external reference of the time sector. A holographic model with its parameter fixed at 2/3 is stated as a discriminator, in which the phantom crossing, the crossing of 2/3 and the coincidence of the two horizons are one event. The account is refuted by a measured equation of state departing from −1, which DESI's preference tests, and by Ω_Λ converging away from 2/3. Every exact claim re-derives in a public suite at github.com/thefirsthorstmann/g-theory-verify. Theorem 1 is also formalized there in Lean 4.

---

## 1 · Introduction

The cosmological constant problem is a discrepancy of some hundred and
twenty orders of magnitude. Summing the zero-point energies of the
quantum fields over modes up to the Planck scale gives a vacuum energy
density that far above the value inferred from cosmological observation
[1]. The discrepancy is not a small correction to be absorbed: the
calculation produces nothing near the measured quantity.

Several programmes treat this as a symptom rather than a computational
difficulty. Holographic approaches, from Cohen, Kaplan and Nelson to
Li's model of dark energy, bound the vacuum energy by the area of a
cosmological horizon rather than by a volume mode sum, removing the
divergence by removing the sum [2]. Unimodular formulations, after Unruh
and after Henneaux and Teitelboim, obtain the cosmological term as a
constant of integration rather than as a coupling in the field
equations, which changes what kind of quantity it is [3]. Entropic and
information-theoretic treatments, from Jacobson to Verlinde, derive the
field equations from horizon degrees of freedom, so the vacuum term
inherits a boundary origin rather than a bulk one [4]. What these
approaches share is the position that the vacuum energy is fixed by a
boundary count and not by a mode sum.

This paper develops an account in that class, on a discrete register. The
proposal is that no mode sum exists to diverge. The register holds a finite
number of cells within any horizon, the vacuum term is the count of those
cells, and the hundred and twenty orders never arise because the quantity
that would produce them is not defined. The construction requires one
external quantity, an epoch, and §5 shows that it can require no fewer.

Five results are advanced, each labelled by its type. The vacuum's tier
in the mechanism is a theorem. The vacuum law and its fraction are an
exact identity, resting on one labelled identification and one
established rest value.† The measured excess is interpreted as a clock
reading rather than a constant. The classification of the remaining
question is a second theorem. A candidate dynamics is then proposed,
carrying an exact crossing identity, and is stated together with its
standing against present data and the measurements that would refute it.
No parameter is adjusted at any point.

<div class="vnote">† Version 1 called the rest value the seat.</div>

## 2 · The tier theorem: numerators source, the modulus idles

**Theorem 1.** On the reptend cycle of the tethered prime, the k-th
rider's closure falls short by exactly k: k × 142857 × 7 = k·10⁶ − k,
for every k from one to six, and likewise for every full reptend prime.
The modulus's own gap is one: 10⁶ − 999999 = 1 — for every rider, and
with no rider at all.

The companion record on gravitation builds its account on the first
half: shortfall proportional to the count carried is sourcing, and the
equivalence principle and F ∝ M arrive from that one congruence. The
second half is this paper's object. **The modulus gap is unsourced**: it
does not scale with any rider, it belongs to the denominator rather than
the numerator, and it is present in the arithmetic whether or not
anything rides. It is the cycle's constant gap, the unit with which
every cycle restarts. The unit rider's shortfall is also one, but the
two differ structurally: the rider's one grows to k when k rides, while
the modulus's one never grows at all. The distinction is scaling and
locus, not magnitude.

**Interpretation 1.** The vacuum is the k-less tier: empty space is the
reptend cycle with no numerator, a cycle with no rider, empty of riders
and not of structure. The energy of empty space is the modulus gap read
at the horizon.

**Interpretation 2 (the ladder join, labeled).** The companion's inverse
square theorem holds in the cycle's own extension count. Reading that
count as the horizon's count of Planck cells identifies two ladders —
the arithmetic extension and the physical boundary — and everything
after this point stands on that join. It is the identification that
carries the paper, made once, here.

## 3 · The fraction: one unit per horizon

The rest value of the dark-energy fraction is established independently
of this paper, in the Origin's seventh volume, at **two thirds**. It is
the position of La on the figure, and the same two thirds as in Koide's
relation among the charged lepton masses. On the identification of
Interpretation 2, the vacuum law then takes a closed form with no
adjustable element:

```
      ρ_Λ  ×  A / l_P²   =   ρ_P  ×  1

                    ⟺

                   Ω_Λ  =  2/3
```

because A/l_P² is 4πN², the horizon's full area in raw Planck cells.

**Theorem 2.** One Planck density in total, distributed over the
horizon's raw cell count, is exactly the statement Ω_Λ = 2/3: verified
as an identity, for arbitrary expansion rate and arbitrary gravitational
constant, to twelve digits. The Bekenstein–Hawking quarter-cell
convention [5] would give 8/3 and is excluded by the rest value: the raw
cell is the convention the rest value selects, and the selection is
recorded as such, not as a derivation made in advance.

**The numerator of the identity is the modulus gap.** The one on the
right side is the tier theorem's object: the unsourced unit, the reseed.
**The vacuum is one reseed per horizon**: the cycle's single unsourced
unit, distributed over the entire boundary count. The mode sum of §1
assigns the vacuum an energy per cell and comes out a hundred and twenty
orders of magnitude too large. On discrete terms the vacuum carries one
unit per horizon of cells: the correction comes from the counting rather
than from any cutoff.

**A flat universe with Ω_Λ = 2/3 has a total matter fraction of one
third, exactly.** On the figure's table of positions one third is Fa's
descending address, as two thirds is La's, so the cosmic fractions split
on the pair of thirds. The unsourced sector rests at La. The sourced
sector, everything that carries a k, stands at the position of the
subdominant, the degree heard as a move away from rest, which is the
station of sourcing in the companion record. The reading of the split is
the figure's; the arithmetic of the complement is not.

## 4 · The excess is a clock reading

The measured fraction exceeds the rest value: 0.6847 against 2/3 on the
Planck 2018 fit [6], an excess of 2.7 percent, and 0.7025 on the ΛCDM
fit to DESI's second data release [7], an excess of 5.4. The excess is
not a constant awaiting derivation. In the standard expansion history
the fraction sweeps, and on the Planck fit it crossed the rest value at
redshift z\* = 0.028 , four hundred million years ago, within three
percent of the age of the universe. The excess grows from zero at the
crossing. Its rate is derived rather than quoted. Differentiating the
sweep and using Ω_Λ + Ω_m = 1 gives the rate at the present epoch:

```
   dΩ_Λ/dz  =  −3 Ω_Λ Ω_m
```

The crossing redshift follows from the exact expansion history, by solving
Ω_Λ(z) = 2/3, and the measured excess is then compared against the rate
times that elapsed sweep:

| | Planck 2018 | DESI |
|---|---|---|
| Ω_Λ now | 0.6847 | 0.7025 |
| sweep rate | 0.648 | 0.627 |
| crossing z\* | 0.02782 | 0.05692 |
| **rate × z\*** (predicted) | **0.01802** | **0.03569** |
| **Ω_Λ − 2/3** (measured) | **0.01803** | **0.03583** |
| agreement | 0.10 % | 0.40 % |

It closes on **both** datasets to better than one per cent. The rate is not free. It is fixed by the same two
fractions the sweep is made of, so the closure is a check rather than a fit.
What it checks is that the sweep is linear across the interval: z* comes
from the exact expansion history, while the prediction is the linear
extrapolation.

**The excess is the crossing clock's reading**: the excess equals the elapsed time since the
crossing multiplied by the computed rate. A derivation of the excess's value
would therefore be a derivation of the elapsed time — of the present epoch —
and §5 proves the present epoch is the one quantity the theory must be
supplied externally.

## 5 · The epoch theorem: the one external reference of the time sector

**Theorem 3 (the counterpart in time of the reference theorem of Units
on Discrete Terms).** The reference count of that companion — the number
of measured scales a theory must be supplied externally — was proved
there to be exactly one, from the one-parameter group of rescalings that
remains once all dimensionless content is fixed. The identical argument
runs in the time sector. The theory's dimensionless content is invariant
under time translation, which is a one-parameter group. The number of
external epoch references a theory must be supplied is therefore exactly
one, and no dimensionless construction can produce it.

**The present epoch is that reference.** It enters this paper exactly
once, as the clock reading of §4, just as the electron mass enters the
gravity record exactly once. Requiring a derivation of the present epoch
from pure structure is the same category error as requiring a magnitude
from a pure number, and the account declines both for the same proved
reason. That the cosmic record is read only against its own tick is not
solved here but classified: it is the time sector's single external
reference, and the sector requires no second.

## 6 · The candidate dynamics, and the coincidence of three crossings

The law of §3 admits accelerating solutions on one of the available
horizon geometries, the future event horizon. On that geometry the rest
value itself serves as the holographic constant [2]:

```
      ρ_Λ  =  ρ_P l_P² / A_event        ⟺        c_H²  =  2/3
```

in the notation of the holographic dark energy family — a parameter the
literature fits, here fixed by the same two thirds that fixes the fraction. The
flow closes on its defining relation at machine precision, and today it gives

```
w₀  =  −1.009
```

an offset from the cosmological constant several times smaller than today's
error bar on that number. An exact identity structures the whole history:

**Theorem 4: three crossings coincide.** In this model the equation of
state equals −1 precisely when the dark-energy fraction equals its rest
value, and the fraction equals its rest value precisely when the event
horizon equals the Hubble radius. **The phantom crossing, the crossing
of 2/3, and the horizon coincidence are one event**, at z\* = 0.028 on
the Planck fit, the same crossing the clock of §4 reads. In this reading
the universe crossed the phantom divide four hundred million years ago,
at the moment its two horizons touched, as the vacuum's fraction passed
its rest value.

**The account's own position is w = −1 exactly, and the model of this
section is a discriminator.** The position is committed outright: w = −1
at every redshift, with no fallback, because the term is a constant of
integration. The registry carries the null (Predictions on Discrete
Terms; Gravity on Discrete Terms, §14). The model of this section is
therefore not the account's position. Its office is discrimination. It
characterizes what evolving dark energy would look like if the evolution
followed the geometry of the rest value: the phantom crossing at the
crossing of 2/3 and nowhere else. A confirmed evolution, wherever it
lies, can then be located relative to the rest value. Over the survey
range the model's running is positive, its equation of state relaxing
toward −1/3 into the past, while the current DESI preference runs the
other way. In a Gaussian reading of the DR2 contours the model is
competitive with ΛCDM, within one to two standard deviations, and at
today's precision it is inseparable from ΛCDM. A confirmed evolution of
the equation of state refutes the registered position outright, and this
section does not stand in for it. Within such a refutation, two
signatures would distinguish evolution along the geometry of the rest
value from generic evolution: positive running, and a phantom crossing
located at the crossing of 2/3 rather than elsewhere or nowhere.

## 7 · Two registered forks

Both are decided by measurement, and neither touches the registered null
on the equation of state.

**The anatomy fork: the excess reads eighteen or thirty-six thousandths,
according to the dataset.** The fine-structure rest value is 137 +
36/1000. The vacuum fraction's additive excess over its rest value reads
18.0/1000 on the Planck fit and 35.8/1000 ≈ 36/1000 on DESI's. That is
the eighteen of the first operation's exchange (the Origin, Volume I),
or its double, which is the fine-structure excess itself. At today's
uncertainty, ±7 in those units, any value lands near some structured
numeral, and the observation is recorded at exactly that strength. At
σ(Ω_Λ) ≈ 0.002, which the next generation of surveys reaches, the fork
decides among three outcomes: an excess of eighteen, an excess of
thirty-six at the dominant degree, or neither, in which case the
parallel is withdrawn. The crossing redshift takes the same fork's
second form: the Planck branch crosses at 0.028, the DESI branch at
0.057.

**The same future data decide the candidate of §6.** Confirmation of
negative running removes the candidate together with ΛCDM. Resolution
toward ΛCDM leaves the two separated only by the crossing signature and
the sign of a small running, which is a discrimination for the surveys
after next.

## 8 · The correspondence: the vacuum term as a sustained tone

This section states the musical correspondence; nothing below depends on it.

Consider the structure of the vacuum from the point of view of a held
continuous tone — a drone. A drone is a tone that sounds under a melody
without belonging to it: the melody's phrases begin and end, and the drone
neither begins nor ends with them. Musical practice in many traditions
maintains such a tone deliberately, because melodic motion is heard as motion
relative to something that does not move.

Now read the tier theorem in those terms. The riders are the melody:
each phrase carries its own count k, each meets its own shortfall, and
those contributions are the sourced world — mass, pull. The modulus is
the drone: the cycle itself, sounding whether or not anything rides, its
single unsourced unit spread under the whole performance. Empty space is
not silence on these terms; it is the cycle turning with no numerator —
the held tone under a melody that happens to be absent. And the fraction
of §3 states the drone's level exactly: one unit — not one per cell, one
per horizon.

**The rest value completes the reading.** The vacuum's fraction rests at
two thirds, and two thirds is La's descending address, the fifth read
downward, placed at 240 degrees on the figure. In the figure's own terms
the vacuum rests at the drone's interval.

## 9 · What would refute this

1. **The tier and the fraction.** Theorem 2 is exact. What is refutable
  is its application. A measured Ω_Λ converging, at σ ≈ 0.002, away from
  both branches of the anatomy fork and inconsistent with rest value
  plus clock would leave the fraction's reading without its excess
  accounted for.
2. **The equation of state.** The registered position is w = −1 exactly,
  with no fallback: a confirmed evolution refutes the account outright,
  and the registry carries the null. Within that refutation, a measured
  phantom crossing located away from the Ω_Λ = 2/3 crossing removes §6's
  characterization specifically, since the model permits no other
  location; confirmation of negative running removes it jointly with
  ΛCDM.
3. **The epoch theorem.** A derivation of the present epoch from
  dimensionless structure — by anyone — would refute Theorem 3 as
  stated, exactly as a derivation of a magnitude from a pure number
  would refute its counterpart.
4. **The sign.** The shortfall theorem permits no overclosure, so the
  k-less term carries one sign: this framework's vacuum energy cannot be
  negative. A measured negative vacuum density would have refuted the
  mechanism outright. The observed density is positive.

A condition that is met is recorded as a refutation and is not
reinterpreted. The program then uses the miss to find why the
construction failed, and a revised statement enters as a new one under
its own date.†

<div class="vnote">† Added in version 2.</div>

## 10 · Relation to the standard account

One convention is named before the comparisons, because every comparison in
this paper runs through it. The observational quantities engaged here are the dark energy fraction, the
equation of state, and its running. None is a direct observable. They are
parameters of the standard cosmological model and its extensions, fitted to
the surveys' distance and clustering data. This paper engages the data through that parametrization, as every model in
the field does. Its statements about those parameters inherit it. That is why
the fraction is quoted on two fits separately rather than as one number. The background expansion throughout is the standard one, consistent
with the position that the field equations stand; what the paper
contributes is the density law's structure, not an alternative cosmography.

The holographic family of dark energy models is established literature,
and the dynamics of the event-horizon variant is known [2]. This paper
adds no new mechanism to that family. It inherits the family's
equations, and with them its known conceptual tension: the present
density is defined through the future horizon, a circularity the
self-consistency of the flow exhibits but does not explain. What this
paper adds is one number. The family's free parameter is fixed here at
the rest value, c_H² = 2/3, by the same structure that fixes the
fraction, with nothing fitted. That fixing produces the coincidence of
the three crossings (Theorem 4), which fitted versions of the model do
not have. The cosmological constant problem's hundred and twenty orders
arise from assigning the vacuum an energy per cell; the counting
proposed here assigns it one unit per horizon, and §3 is the entire
correction. The coincidence problem is not solved here but relocated to
a proved boundary, the single epoch reference of Theorem 3. Two
observations attach to it. The present epoch lies within three percent
of the crossing of 2/3. In the candidate model that crossing is also the
phantom crossing and the horizon coincidence. The present observational
situation is a preference for evolving dark energy with negative
running: 3.1 standard deviations for DESI's second release with the
cosmic microwave background, and 2.8 to 4.2 with the supernova samples
added [7]. It presses on the registered null directly: confirmed, it
refutes the account, and it removes §6's characterization together with
ΛCDM. The account stands or falls with named measurements rather than
with argument.

## 11 · Verification

Every exact statement is encoded as a re-runnable test in
`verify/test_vacuum_campaign.py`:

- the tier theorem
- the fraction identity at arbitrary inputs
- the flow closures at machine precision
- the clock rate
- the coincidence of the three crossings
- the fork values

The two interpretations are labelled where they stand, in §2. The
provenance of the rest value is independent of this paper. Every
comparison sentence of the account is printed by a conditional on a
computed number. Theorem 1 is also formalized in Lean 4 with Mathlib, in
the same repository, with the gravity record's theorems. The battery and
this paper's source are public at
github.com/thefirsthorstmann/g-theory-verify.

---

*Companions: Gravity on Discrete Terms, the form, the coupling and the
rest values of §14, DOI 10.5281/zenodo.22087599 · Units on Discrete
Terms, the reference theorem and the classes of constants, DOI
10.5281/zenodo.22119360 · The Origin on Discrete Terms, the figure, DOI
10.5281/zenodo.21212112 · The Vanishing Point on Discrete Terms, the
nines and the horizon, DOI 10.5281/zenodo.21209420 · The registry,
Predictions on Discrete Terms, DOI 10.5281/zenodo.21206818 · The
Fine-Structure Constant on Discrete Terms, the rest value 137.036, DOI
10.5281/zenodo.21211050.*

*References: [1] S. Weinberg, Rev. Mod. Phys. 61 (1989) 1 · [2] A. G.
Cohen, D. B. Kaplan, A. E. Nelson, Phys. Rev. Lett. 82 (1999) 4971; M.
Li, Phys. Lett. B 603 (2004) 1 · [3] W. G. Unruh, Phys. Rev. D 40 (1989)
1048; M. Henneaux, C. Teitelboim, Phys. Lett. B 222 (1989) 195 · [4] T.
Jacobson, Phys. Rev. Lett. 75 (1995) 1260; E. Verlinde, JHEP 04 (2011)
029 · [5] J. D. Bekenstein, Phys. Rev. D 7 (1973) 2333 · [6] Planck
Collaboration, Astron. Astrophys. 641 (2020) A6 · [7] DESI
Collaboration, DESI DR2 Results II, arXiv:2503.14738 (2025).*

<div class="copyright" style="margin-top:24pt">Copyright<br>Christian Horstmann · August 25th, 2026 · version 2, October 2026<br>thefirsthorstmann@gmail.com<br>All rights reserved</div>
