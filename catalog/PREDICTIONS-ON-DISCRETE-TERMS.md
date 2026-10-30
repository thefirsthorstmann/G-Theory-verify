---
title: Predictions on Discrete Terms
subtitle: A registered falsification schedule — sixteen live commitments and six exact nulls, their falsification conditions, and the experiments that will decide them.
byline: Christian Horstmann · thefirsthorstmann@gmail.com · July 5th, 2026 · version 3, October 2026 · registered before adjudication
date: 2026-07-05
titlenote: This document registers numerical predictions in advance of the measurements that will judge them. Where the construction of a value is published, its record is cited; where none is cited, the value stands as a bare registered number. What is presented is everything adjudication requires: exact values, falsification bands, adjudicating experiments and horizons. The registry is revised only additively, with every change documented in a visible log. All values are pinned by a mechanical test suite, public at github.com/thefirsthorstmann/g-theory-verify, and rerun on every revision. Version 3 re-reads the comparison column from its sources, dated October 2026, and adds the nucleon sector; the change log is §8, and no earlier commitment was altered or removed.
abstract: A prediction carries evidential weight only if it can fail and only if it is recorded before the data that test it. This registry records, in advance and under a timestamp, the numerical commitments of a research program whose discipline is stated at the outset: no adjustable parameters, every claim independently falsifiable, verdicts accepted as rendered. Sixteen live commitments and six exact nulls are registered. In the neutrino sector, sin²θ₂₃ = 4/7 = 0.5714 against a 2026 fit of 0.533 ± 0.018 with the octant unresolved, falsified if the measurements converge away from the value; sin²θ₁₃ = 1/45 = 0.02222 against 0.0217 ± 0.0007; and normal mass ordering, registered conditionally on an internal assignment and falling with it if the ordering proves inverted. At the proton, the magnetic radius is registered at 0.8487 fm, the arithmetic 11/3 fm minus the classical electron radius, with a value below 0.83 fm decisive against it; and the Zemach radius at 1.0922 fm, falsified below 1.04 fm, with the forthcoming muonic-hydrogen hyperfine measurements adjudicating and the band 1.08–1.10 separating the commitment from the standard dipole expectation of 1.0626 fm. In the electroweak sector a pair of values is registered for (m_W/m_Z)²: the primary 1 − 17/81 − 13/1000 and a named alternative 1 − 17/81 − 1/75, differing by 17 MeV in the W mass. Both fail together if the W mass resolves at the CDF value, and a ±5 MeV determination decides between them; the 2026 world average stands 3.1σ below the primary and 0.9σ below the alternative. In turbulence, the intermittency-corrected slope of the energy spectrum is registered at 17/10 exactly, against She–Lévêque's 1.69594, with a measurement at ±0.005 falsifying whichever the data leaves. Version 2 added three commitments from the gravitational record: the Higgs mass at 125.0640 ± 0.0001 GeV, from an exact self-coupling recorded on 2026-07-03, before comparison; Newton's constant at 6.673590137(4) × 10⁻¹¹ m³ kg⁻¹ s⁻², 106 parts per million below the CODATA centre, to be decided by convergent metrology; and the Hubble constant at 70.05 km s⁻¹ Mpc⁻¹, inside the present tension. It also added five exact nulls: the dark-energy equation of state at exactly −1, the Eötvös ratio at zero with no screening available, clock-species universality of the gravitational redshift, no gravitational radiation below quadrupole order, and a log-periodic residual whose period must be one octave if it is detected at all. Version 3 adds the nucleon sector: the ratio of the proton and neutron mass residuals at 23/32, the chiral crossover temperature at one sixth of the proton mass, a floor of 137.035999 under the inverse fine-structure constant, a null present-day drift of the proton-to-electron mass ratio with a step of +0.9 × 10⁻⁷ at redshift 0.886, and a two-sided value for the neutron residual. Eight items stand in tension with current data and are flagged in Section 4, among them the primary of the electroweak pair and the value of sin²θ₂₃. One value is registered as watched and is not committed: sin²θ₁₂ = 5/17 = 0.2941, 1.5σ below JUNO's 2026 measurement, whose sub-percent determination is expected to decide; the abstention is recorded so that neither a hit nor a miss can be narrated afterwards. The precedent is Balmer's formula, which preceded its mechanism by twenty-eight years, and Koide's relation, which has stood unexplained and respected since 1981. A registered number is legitimized by its conduct: exact statement, named adjudicator, accepted verdict. Every registered value and band re-derives in a public suite at github.com/thefirsthorstmann/g-theory-verify, with Sections 2 and 3 formalized in Lean 4.
---

## 1 · Conduct

Four rules govern this registry. **Stated status**: the values below are
registered predictions of a research program. Where a construction is
published, its record is cited; where none is cited, the value stands as
a bare registered number. **Maximal falsifiability**: every commitment
carries an exact value, a falsification band, a named adjudicating
experiment, and a horizon; a claim that cannot fail has no place on this
page. **Verdicts accepted, and learned from**: the registry is
timestamped in advance of the measurements, and verdicts are accepted as
rendered. A miss is recorded as a miss and is not reinterpreted. A miss
is also evidence: the program uses it to understand why the construction
failed, and revises its positions and techniques on that evidence. A
revised value enters as a new commitment under its own date, answerable
to later measurements, and the failed one stays in the log. **The whole
record, not any single row**: the commitments are independent, the items
in tension are flagged before they resolve, and the watched column shows
what the program has left uncommitted. The aggregate, and no single
agreement, is the evidence offered.

The precedent for registering numbers ahead of their mechanism is old.
Hooke recorded the spring law as an anagram in 1676; Balmer's formula
ran twenty-eight years ahead of its mechanism; Koide's relation [4] has
stood unexplained since 1981 and is tested to this day. The companion
records of this series [1, 2, 5, 6] argue the program's terms; this
document records its commitments.

## 2 · The live commitments

| # | quantity | commitment | measured, October 2026 | falsification condition | adjudicator · horizon |
|---|---|---|---|---|---|
| 1 | sin²θ₂₃ (PMNS) | **4/7 = 0.571429** | 0.533(18) PDG fit; NuFIT best fit 0.470, 3σ range to 0.584 | convergence away from the value: > 0.60 or < 0.55 | DUNE / JUNO / Hyper-K · ~2030 |
| 2 | sin²θ₁₃ (PMNS) | **1/45 = 0.022222** | 0.0217(7) PDG; 0.02249(57) NuFIT | precision excludes the value | reactor + accelerator · near threshold |
| 3 | ν mass ordering | **normal — conditional** | favored: 1.2–2.4σ NuFIT, ≥ 2.1σ JUNO | inverted ordering established | DUNE / JUNO · ~2030 |
| 4 | proton magnetic radius r_M | **11/3 fm − r_e = 0.848726 fm** | 0.851(26) PDG; determinations split: 0.846–0.847 vs 0.811 | r_M < 0.83 fm | muonic-H HFS, dispersive consolidation · running |
| 5 | proton Zemach radius r_Z | **1.0922 fm** | 1.082(37) μH · 1.086(12) scatt. | r_Z < 1.04 fm | muonic-H HFS campaigns · ~0.01 fm precision coming |
| 6 | (m_W/m_Z)² | **1 − 17/81 − 13/1000** (alternative registered: 1 − 17/81 − 1/75) | m_W = 80.3625(77) GeV: primary +3.1σ, alternative +0.9σ | resolution at the CDF value (m_W/m_Z > 0.8820) falsifies both | m_W at ±5 MeV: LHC combination, FCC-ee class |
| 7 | turbulence spectral slope, with intermittency | **17/10 = 1.700 exactly** | measured ≈ 1.70; She–Lévêque 1.69594 | slope at ±0.005 excludes it | high-Re DNS, atmospheric spectra · open |
| 8 | m_H (Higgs mass) | **(32/63) v = 125.0640(1) GeV** | 125.13(11) PDG; 125.04(12) CMS, 125.11(11) ATLAS | a combination at ±30 MeV excluding the value | HL-LHC combinations · 2030s |
| 9 | Newton's constant G | **6.673590137(4) × 10⁻¹¹ m³ kg⁻¹ s⁻²** | CODATA 2022 6.67430(15); input spread 551 ppm | convergent metrology excluding the value | BIPM-class determinations · open |
| 10 | H₀ | **70.05 km s⁻¹ Mpc⁻¹** | 67.36(54) CMB against 73.17(86) local ladder | the tension resolving decisively away from the value | CMB-independent ladders, standard sirens · ~2030 |
| 11 | Δp/Δn, ratio of the proton and neutron mass residuals | **23/32 = 0.71875, constant** | 0.7187506(585) | a neutron mass that moves the ratio by 3σ, or any drift of the ratio | Penning-trap spectrometry, CODATA · ~2030 |
| 12 | chiral crossover temperature of QCD | **m_p/6 = 156.379 MeV** | lattice: 156.5(15), 158.0(6) | a consolidated lattice value outside 153–160 MeV | lattice QCD · ongoing |
| 13 | α⁻¹ (window) | **137.035999 < α⁻¹ < 137.036000** | CODATA 2022 137.035999177(21) | any determination below 137.035999 | atom interferometry, electron g − 2 · ongoing |
| 14 | present-day drift of m_p/m_e | **zero** | −0.8(3.6) × 10⁻¹⁷ per year | a confirmed present-day drift | optical-clock comparisons · ongoing |
| 15 | Δμ/μ at redshift 0.886 | **+0.9 × 10⁻⁷** | −1.8(1.2) × 10⁻⁷; 3σ limit 3.6 × 10⁻⁷ | a determination that excludes the value | methanol absorption toward PKS 1830-211 · next campaign |
| 16 | Δn, the neutron mass residual | **0.4916103 or 0.4916906** (two-sided) | 0.4916060(400) | a consolidated value away from both | the next neutron-mass adjustment · ~2030 |

**A registered null is refuted by one confirmed counter-instance at any
precision.** The nulls below were added in versions 2 and 3, and the
program has no screening mechanism or free parameter to absorb a
counter-instance. The gravitational constructions are argued in the
record [5]; the log-periodic entry is two-sided: non-detection does not
refute it, detection at any period other than one octave does.

| quantity | commitment | falsification condition | adjudicator |
|---|---|---|---|
| w, dark-energy equation of state | **−1 exactly, no fallback** | established evolution of w | DESI- and Euclid-era combinations |
| Eötvös ratio η | **0 exactly, no screening** | any confirmed nonzero η — any pair, any range | MICROSCOPE-class missions, torsion balances |
| gravitational redshift, by clock species | **universal exactly** | confirmed species dependence between co-located clocks | optical-clock comparisons, ACES |
| gravitational radiation below ℓ = 2 | **none** | a confirmed monopole or dipole component | pulsar timing, gravitational-wave catalogs |
| free fractional charge | **none** | one confirmed instance | colliders, bulk matter |
| log-periodic residual in the coupling | **period one octave, if detected** | detection at any other period | short-range gravity experiments |

**Where the arithmetic of a commitment is public, it is shown here.**
Commitment 4 is an explicit arithmetic of published constants: 11/3
femtometres minus the classical electron radius, 3.666667 − 2.817940 =
0.848726 fm. Commitment 6's two members differ by 17 MeV in the W mass,
and a measurement at ±5 MeV decides between them. Against the 2026 world
average the primary stands 24 MeV above and the alternative 7 MeV above;
the registry commits to the primary and names the alternative so that no
later re-selection is possible. Commitment 7 sets an exact rational
beside the standard intermittency model's 1.69594: a difference of
0.00406, decided by any measurement that fixes the slope to ±0.002.
Commitment 8's basis is the self-coupling of the resolved results — the
exact rational 2⁹/(3⁴·7²), recorded 2026-07-03 before any comparison.
The mass follows from it with no further freedom: m_H = (32/63) v, with
v taken from the Fermi constant. Commitment 9 is the coupling αG(e) =
5/(2¹⁵¹ − 1), carried into SI units by the electron mass at its CODATA
2022 value. Commitment 10 stands on one declared chain together with the
nuclear saturation density, whose ideal value on the same chain is
3·7³/(2¹¹π) fm⁻³ = 0.15993 fm⁻³; the two stand or fall together.
Commitments 11 to 16 are derived in the record on the proton and neutron
masses [6], which registers nine values; the six with a refutation
condition and a named measurement are entered here. The residuals are Δp
= (1.00728 − m_p) × 10⁵ and Δn = (m_n − 1.00866) × 10⁵, with the masses
in unified atomic mass units. Commitments 14 and 15 follow from one
hypothesis: the masses are constant between increments and step at each,
and one increment separates redshift 0.886 from the present.

## 3 · The precision that decides each commitment

For each commitment the table gives the precision at which the
registered value becomes the only simple rational inside the
measurement's ±2σ band, the point at which agreement becomes selection
among alternatives. For the rational commitments the alternatives are
the nearest fractions of bounded denominator, taken smallest first: the
order least action prescribes for candidates, fixed in advance.

| commitment | nearest alternatives | σ needed | σ, October 2026 | sharpening required |
|---|---|---|---|---|
| sin²θ₂₃ = 4/7 | 3/5 · 5/9 · 13/23 | 0.0079 (denominators to 10) · 0.0031 (to 23) | 0.018 | ×2.3 — inside DUNE-era projections |
| sin²θ₁₃ = 1/45 | 1/44 · 1/46 · 2/91 | 0.00024 | 0.00057 | ×2.4 — beyond existing and planned experiments |
| (m_W/m_Z)² pair | each other: 17 MeV | ±5 MeV on m_W | ±7.7 MeV | ×1.5 — final LHC combination |
| slope 17/10 | She–Lévêque: 0.00406 | ±0.002 | ~±0.01 | ×5 — high-Re DNS |
| r_M | the split between determinations first, then ±0.001 fm | staged | the split itself | resolution in progress |
| r_Z | dipole 1.0626 at distance 0.030 | ±0.015 (dipole separation) | ~±0.03 | ×2 — coming campaigns |
| m_H = (32/63) v | nearest register alternative 102 MeV above | ±25 MeV | ±110 MeV | ×4 — HL-LHC projections reach ±10–20 MeV |

The last column states the purpose of the registry: **every live
commitment names the precision that decides it.** All but one of the
figures lie within a funded program's published projections. The
exception is sin²θ₁₃: no existing or planned experiment is expected to
improve on Daya Bay's final precision, and the figure required here
awaits a new one.

## 4 · In tension now

Eight items stand in tension with current data, and the registry states
each before its verdict. **The primary of the electroweak pair stands
3.1σ above the 2026 world average of the W mass**, 80.3625(77) GeV,
formed without the CDF measurement; the named alternative stands 0.9σ
above it. The deciding precision of ±5 MeV has not been reached, and the
commitment stays with the primary as registered. **The octant of θ₂₃ is
unresolved, and the 2026 fits are centred below the registered value**:
0.533(18) in the PDG fit, 2.1σ below 4/7, and a best fit of 0.470 in
NuFIT 6.1, whose three-sigma range reaches 0.584. A resolution in the
lower octant falsifies commitment 1. **The crossover temperature of
commitment 12 stands 2.7σ below one of the two lattice determinations**,
158.0(6) MeV, and 0.1σ below the other. **The dark-energy null faces the
second DESI release** [8], which prefers an evolving equation of state
at 2.8 to 4.2σ depending on the supernova sample; established evolution
refutes the null. **Newton's constant, registered 106 ppm below the
CODATA centre**, lies outside CODATA's 22 ppm uncertainty and inside the
551 ppm spread of the determinations it adjusts. **The proton
charge-radius value, 0.84131 fm**, sits +0.9σ from CODATA 2022's
0.84075(64); it fails outside 0.8398–0.8428 fm. **Commitment 10, the
Hubble constant, stands 5.0σ above the CMB value and 3.6σ below the
local ladder's**; the two stand 5.7σ apart, and it fails if they resolve
decisively away from 70.05. **The step of commitment 15 stands 2.2σ
above the latest estimate on its sightline**, −1.8(1.2) × 10⁻⁷ [9], and
inside its three-sigma limit. The Higgs mass, 0.6σ below the 2026
average [3], leaves this section. If any of these fails, the next
version of this registry will state it, and the program will take up
why.

## 5 · Watched, not committed

**sin²θ₁₂ = 5/17 = 0.294118** is registered as watched and is not
committed. JUNO's measurement from 207 days of data, 0.3036 ± 0.0064
[7], sits 1.5σ above the value, and its sub-percent determination will
decide the question. The abstention was recorded in advance so that
neither outcome can be narrated afterwards: if the measurement lands on
5/17 the registry claims no credit, and if it lands elsewhere no
commitment fails. Also watched, with conditions for promotion in place
of commitments: glueball mass ratios, pending verification of their
sources, and a low-multipole CMB feature, which is committed only if a
specific multipole is derived. The gravitational-coupling expression
watched in version 1 is promoted to commitment 9, its construction
published in the gravitational record [5], as §8 records.

## 6 · Resolved results

**These values agree with settled measurement and are retrodictions.**
The program's constructions produced them before this registry existed,
and they are listed for context. The muon-to-electron mass ratio stands
at 206.768 (1.4 ppm), and the tau mass follows through an exact
one-third relation on lepton mass square roots (61 ppm, the Koide anchor
[4]). The proton-to-electron ratio has the integer factorization 1836 =
36·51, and the proton-to-neutron magnetic moment ratio is an exact power
ratio of 2 and 3 (3.6 ppm). A Higgs self-coupling was stated as an exact
rational, 0.12900, before comparison; since version 2 it is the basis of
commitment 8. They carry no weight in adjudication. The program's
evidence-bearing claims are the commitments above, which were recorded
before their verdicts and can still fail.

## 7 · Terms of adjudication

This registry is versioned additively: commitments may be added in later
versions, and none will be removed or altered silently. Every change of
status (confirmed, falsified, withdrawn, promoted from watched) will
appear in a change log on the face of the document. Current experimental
values are taken from the standard compilations [3] and from the single
measurements cited beside them [7, 8], as they stood in October 2026.
The registry's timestamp is its publication date; the program's terms
are argued in the companion records [1, 2, 5, 6]; the verdicts belong to
the experiments.

## 8 · Change log

**Version 3 — October 2026.** The comparison column is re-read from its
sources and dated October 2026: the 2026 Particle Data Group listings,
NuFIT 6.1 and the single measurements cited [3, 7, 8]. The column of
versions 1 and 2 was out of date when they were registered. It quoted
the 2024 listings and, for the neutrino angles θ₂₃ and θ₁₃, the global
fit of 2022 in its variant without the Super-Kamiokande atmospheric
data. The 2026 listings, the May 2026 combination of the W mass and the
global fits of 2024 and 2025 were already available. Against those
sources three standings were already the ones printed here. The primary
of commitment 6 stood 3.1σ above the world-average W mass, and 1.3σ
above the 2024 value. Commitment 1 stood 2.1σ above the fit of sin²θ₂₃,
where versions 1 and 2 quoted 0.572(19). Commitment 8 stood 0.6σ below
the Higgs average, where version 2 printed 1.2σ, and it leaves the
in-tension section. One measurement is new since version 2: JUNO's of
September 29th, 2026 [7], which puts the watched sin²θ₁₂ 1.5σ low and
favours normal ordering. The dark-energy null, Newton's constant and the
Hubble constant are entered in the in-tension section. The first two
stand as in version 2. Commitment 10 is compared with the 2024 local
determination, 73.17(86), which existed when version 2 quoted 73.0(1.0),
and stands 3.6σ below it. Six commitments of the nucleon sector are
added, 11 to 16, from the record on the proton and neutron masses [6],
published September 1st, 2026. Their measured values are read at the
sources; for commitment 15 the 2021 analysis of its sightline [9] stands
where that record printed a figure of 2013. The value of commitment 9 is
restated on the CODATA 2022 electron mass with the Planck constant
untruncated: 6.673590137(4) where version 2 printed 6.673590151(41). The
commitment is the coupling 5/(2¹⁵¹ − 1), which is unchanged; the
restated value lies inside the uncertainty version 2 printed. The note
on commitment 6 gives its distances in MeV; version 2's figure of 0.36
was in cents of the mass ratio and was labelled parts per thousand. A
sixth exact null is registered on October 8th, 2026, as the program's
hypothesis: every state has charge Q relative to the vacuum and color
triality t with Q + t/3 an integer. For matter with only Standard Model
charges, that is its Z₆ condition, undecided by experiment and shared
with SU(5), SO(10) and E₆ [11]. Pair-production searches exclude free
charge 2e/3 from 50 to 640 GeV and e/3 from 50 to 60 GeV [10]. No
earlier commitment was altered or removed. The wording follows the
series' glossary of October 2026: the number of a commitment is its
registered value.

**Version 2 — August 25th, 2026.** Three live commitments added: 8, the
Higgs mass, from the exact self-coupling recorded 2026-07-03 in the
resolved results; 9, Newton's constant, promoted from the watched
column; 10, the Hubble constant, on one declared chain with the
saturation density. The table of null commitments added: five exact
nulls from the gravitational record [5], published August 24th, 2026
with its own seventeen refutation conditions and public claim map. The
table of Section 3 gained the Higgs row. The in-tension section gained
the Higgs mass. No version-1 commitment was altered or removed; the
subtitle's count and the abstract were updated to match. This version
also sets the registry's vocabulary to commitment throughout, and
carries the withdrawn items in the program's internal record; no value
or band changed.

**Version 1 — July 5th, 2026.** The original seven commitments, the
table of Section 3, the flags now carried as in tension, and the watched
and resolved columns.

## References

[1] C. Horstmann, *Navier–Stokes: A Solution on Discrete Terms*, Zenodo
preprint (2026), DOI 10.5281/zenodo.21197044.

[2] C. Horstmann, *π on Discrete Terms*, Zenodo preprint (2026), DOI
10.5281/zenodo.21205368.

[3] F. Takahashi et al. (Particle Data Group), Int. J. Mod. Phys. A
**41** (2026) 2630011; NuFIT 6.1 (2025), nu-fit.org, with I. Esteban et
al., JHEP **12** (2024) 216; CODATA 2022 recommended values.

[4] Y. Koide, *A fermion-boson composite model of quarks and leptons*, Phys. Lett. B **120** (1983) 161; the mass relation first stated 1981.

[5] C. Horstmann, *Gravity on Discrete Terms*, Zenodo preprint (2026), DOI 10.5281/zenodo.22087599.

[6] C. Horstmann, *The Proton and Neutron Masses on Discrete Terms*,
Zenodo preprint (2026), DOI 10.5281/zenodo.22217669.

[7] JUNO Collaboration, *Measurement of neutrino oscillation parameters
at JUNO and indication of the neutrino mass ordering*, arXiv:2609.37895
(2026); CMS Collaboration, Phys. Rev. D **111** (2025) 092014.

[8] DESI Collaboration, *DESI DR2 results II: measurements of baryon
acoustic oscillations and cosmological constraints*, arXiv:2503.14738
(2025).

[9] S. Muller et al., *A study of submillimeter methanol absorption
toward PKS 1830−211*, Astron. Astrophys. **652** (2021) A5.

[10] CMS Collaboration, Phys. Rev. Lett. **134** (2025) 131802.

[11] D. Tong, JHEP **07** (2017) 104; S. Koren and A. Martin, SciPost
Phys. **18** (2025) 004.

*Every registered value, band and deciding precision above is recomputed
from its registered form by a mechanical test suite, rerun on every
revision. The exact arithmetic of Sections 2 and 3 is also formalized as
fifteen theorems in Lean 4 with Mathlib. The suite and the proofs are
public at github.com/thefirsthorstmann/g-theory-verify.*

<div class="copyright" style="margin-top:24pt">Copyright<br>Christian Horstmann · July 5th, 2026 · version 3, October 2026<br>thefirsthorstmann@gmail.com<br>All rights reserved</div>
