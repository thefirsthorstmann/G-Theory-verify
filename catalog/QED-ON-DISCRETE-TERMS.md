%%TITLE: QED on Discrete Terms
%%SUBTITLE: What renormalization is when there is a shortest length, what the running of the coupling measures, and what this account leaves open on the anomalous moment
%%META: Christian Horstmann · thefirsthorstmann@gmail.com · August 26th, 2026 · version 2, October 2026 · manuscript for the public record
%%ABSTRACT: Quantum electrodynamics is verified to twelve significant figures, on a procedure disputed since its introduction: integrals over unbounded momenta diverge, a regulator is imposed, and the divergent parts are absorbed into redefined constants. This paper sets out what the procedure is on a discrete register. The register has a deepest reachable cell, established by an operation-supply argument and not imposed as a cutoff, so no integral runs to infinity and no divergence arises to be absorbed. Renormalization is then a statement about resolution: a measured quantity is read at a depth, and reading at a depth is what the register does. The running of the coupling is a change of count with depth, its direction fixed and its magnitude open. The bare and dressed values are the rest and measured values of the series' two-tier reading, and the regulator describes the reading, not a device. The coupling's integer is the unique prime whose reciprocal has base-ten period eight and seventeen cyclic families, checked over five candidates. The tail's numerator is over-determined by three constructions and its placement arrives through the nucleon masses; a derivation from the register alone, and the assignment to the electromagnetic coupling, remain open. Measurement stands 6.0 parts in 10⁹ below the rest value on the CODATA 2022 value. The anomalous moment is dimensionless and in scope, and its computation remains open. Each result is stated with the finding that would refute it. Every exact claim re-derives in a public suite at github.com/thefirsthorstmann/g-theory-verify.
%%

---

## 1 · Introduction

Quantum electrodynamics predicts the electron's magnetic moment to
twelve significant figures and agrees with measurement at every one of
them. It is also built on a step that its own founders described as
unsatisfactory. The integrals that produce those figures diverge, and
the divergence is removed by imposing a regulator and absorbing the
infinite parts into redefined values of the mass and the charge.

The step is called renormalization, and its interpretation has been
disputed for seventy years while its results have never failed. Dirac
rejected it as a formal trick. Feynman, who built much of the apparatus,
called the procedure a shell game [1] and doubted that it was
mathematically legitimate. The modern reading, due to Wilson and
Kadanoff [2], is more comfortable. A field theory is an effective
description valid below some scale. The divergences record ignorance of
what lies above it, and the running of the couplings is a real flow with
resolution. That reading is now standard, and it does not answer the
question it reframes. It says the theory does not know what happens at
short distance. It does not say what happens there.

Several programmes propose that something happens there which is not a
continuum. Causal set theory replaces the manifold with a countable
order [3]. Loop quantum gravity quantizes areas and volumes [4]. Lattice
gauge theory computes on a discrete grid and then takes the spacing to
zero, treating discreteness as a calculational device [5]. What these
share with the present account is the position that the continuum at
short distance is an assumption and not an observation.

This paper takes the position and states its consequences for
electrodynamics. The register developed in the companion records has a
deepest reachable cell. That floor is derived from an operation-supply
argument and is not imposed. A theory built on it has no integral
running to unbounded momentum, and therefore has no divergence to
absorb.

**Hypothesis.** Renormalization describes the resolution at which a quantity
is read. On a register with a shortest length there is nothing to repair,
and the procedure's success is explained by what it is doing rather than by
what it removes.

The argument runs through Sections 3 to 8. Section 3 states what the
register supplies and what follows immediately. Section 4 gives the
reading of the running coupling and its direction. Section 5 identifies
the bare and dressed values with the rest value and the measured value
of the companion records' two-tier reading. Section 6 separates what is
derived in the coupling's value from what is not. Section 7 states what
is held on the anomalous moment and what is missing. Section 8 gives the
conditions under which each claim fails.

---

## 2 · Terminology

Every term below is used technically and denotes an arithmetic object.

| term | what it denotes here |
|---|---|
| **the register** | a positional numeral system treated as a physical record; a **cell** is one resolvable address at a given depth |
| **depth** | the number of places read; resolving a separation d requires depth log_b(d) |
| **u_min** | the deepest reachable cell, derived in the gravity record from the operation-supply theorem |
| **the count** | the number of cells a quantity occupies; dimensionless, and the object the dimensional boundary permits this account to address |
| **rest value** | the value a quantity carries before a reading; **measured value**, what a reading returns; their difference is the **perturbation offset**† |
| **the two-tier map** | the fixed map from rest value to measured value, defined in the companion records |
| **the hexad** | the six nonzero residues modulo nine that the reptend of 1/7 visits, read in two orders |
| **running** | the dependence of a measured coupling on the momentum at which it is measured |

<div class="vnote">† Version 1 said observed value, and the seat and the
dress.</div>

Where a musical name appears it can be replaced by its arithmetic referent
with nothing lost, and the derivations have been checked under that
replacement.

---

## 3 · What the register supplies

Three results are taken from the companion records and used without
re-derivation. Each is machine-checked in the public suite.

**The register has a floor.** Resolving a separation d requires cells of
size d, hence register depth log_b(d). Reaching d = 0 requires
completing infinitely many depths, which is a supertask. The
operation-supply theorem forbids it: demand through depth N is
exponential in N, while the supply of any finite-energy system is linear
in elapsed time by the Margolus–Levitin bound [6]. The reachable depth
is therefore logarithmic in the resources, and the register has a
deepest reachable cell:

```
   u_min   the deepest reachable cell — derived, not imposed
```

**The count is dimensionless.** By the dimensional boundary (Units,
Theorem 1) no dimensionless construction yields a dimensionful
magnitude. A count of cells is a pure number. Any dimensionful statement
requires one external quantity, supplied once and named.

**Electromagnetism is one object read twice.** The companion account
identifies the electromagnetic sector with the hexad in its two orderings:
the positional order 142857 and the multiplicative order 124875, exchanged
by an involution. That identification is used here only where it is marked.

**The momentum integral becomes a finite sum.** A momentum integral in
quantum electrodynamics runs over all scales. On a register the scales
available are the depths, and the depths terminate at u_min. The
integral is therefore a finite sum:

```
   continuum:   ∫₀^∞ dk  (divergent, regulated by hand)

   register:    Σ over depths 1 … N(u_min)   (finite, no regulator)
```

No cutoff is introduced by this account at any point. The finiteness is a
consequence of the floor, and the floor is a consequence of the supply
theorem. The same census bars finite-time blow-up in the Navier–Stokes
account and excludes the central singularity in the gravity account. One
count regulates all three.

---

## 4 · The running of the coupling

The measured value of the fine-structure constant depends on the momentum at
which it is measured:

```
at q → 0 α⁻¹ = 137.035999177† at q = m_Z α⁻¹ = 127.952
```

In the received account this is vacuum polarization. Virtual pairs screen
the bare charge, so a probe at higher momentum penetrates further into the
screening cloud and sees more charge. The direction is fixed by the sign of
the beta function, and the magnitude is computed from the particle content.

<div class="vnote">† Above: version 1 quoted the 2018 value,
137.035999084.</div>

**On discrete terms the running is a change in the count with depth.** A
probe at higher momentum resolves to greater depth, and a reading at greater
depth traverses more cells. The coupling is a ratio of counts, so a reading
that traverses more cells returns a different ratio. Nothing is being
screened and nothing is being unveiled; the number reported is the number of
cells the reading crossed.

**The direction of the running is fixed, and its size is open.** The
direction is fixed. Greater depth means more cells, so the coupling
grows with momentum, which is the observed direction. The magnitude is
not fixed by the reading alone. It requires the count per depth for the
electromagnetic sector, an open computation. The direction is derived;
the size remains open, and nothing is fitted to it.

That leaves the running as a real physical dependence rather than an
artifact of a regulator. On the received reading the bare coupling is
infinite and unobservable, and the running removes an artifact of the
continuum. On this reading there is no bare infinity, the coupling at every
depth is finite, and the running is what a reading at that depth returns.

---

## 5 · Bare, dressed, and the two-tier map

The received procedure distinguishes a bare coupling, which appears in the
Lagrangian and is not measured, from a dressed coupling, which is measured
and depends on the scale. The bare value is formally infinite and the
difference is absorbed.

This account already carries that distinction under other names. The
companion records read every constant at two tiers, the rest value and
the measured value of the Origin's definitions, which differ by the
perturbation offset. The rest value is what a quantity carries; the
measured value is what a reading returns; and the map between the tiers
is fixed rather than free.

**Identification: the bare value is the rest value, and the dressed
value is the measured value.** The regulator is the specification of the
reading's depth.

```
received here bare coupling rest value dressed coupling measured value
regulator the depth at which the reading is taken renormalization the
map between the two
```

Under this identification the procedure is not a device. It is the statement
that a measurement returns what a reading at a stated resolution returns,
which is what the register does at every depth whether or not a physicist is
watching. The infinity in the received version comes from letting the depth
run without bound, and the floor forbids that.

**This is an identification and is marked as one.** It joins an
established structure, the two-tier reading of the companion records, to
a physical office, the renormalization procedure. Every physical theory
rests on identifications, and each is stated here with the condition
that would refute it; this one's is in §8.

---

## 6 · The coupling's value: what is derived and what is not

A derivation is a chain from stated premises to a result in which no step
could have gone otherwise. Length is not the criterion. A short chain from
a small set of premises is stronger than a long one, because it offers
fewer places for a free choice to hide. What disqualifies a construction is
a fitted parameter, not brevity.

The premises used below are the two generators 2 and 3, the base ten,
and the two cycles of nine and twelve. Each is fixed by the companion
records before the coupling is considered.

### 6.1 The integer

The integer 137 is the unique prime whose reciprocal has base-ten period
eight and seventeen cyclic families. The demonstration is an exhaustive
check over a finite set rather than a numerical search.

A prime has base-ten period eight only if it divides 10⁸ − 1. That integer
factors completely as 3² × 11 × 73 × 101 × 137, so the candidates are five
primes and there are no others:

| prime | period of 1/p | cyclic families |
|---|---|---|
| 3 | 1 | 2 |
| 11 | 2 | 5 |
| 73 | 8 | 9 |
| 101 | 4 | 25 |
| 137 | 8 | 17 |

Two of the five have period eight, and one of those two has seventeen
families. Both conditions are fixed independently of the result.
Seventeen is 3⁴ − 2⁶, the gap between the nearest powers of the two
generators, which the programme uses throughout and did not introduce
here. The base is supplied by the register theorem of the Origin. That
theorem is stated there as conditional, and is repeated here in the same
form. Two mechanisms are given: the ennead lives in digit sums, and the
seed unrolls to full period. Under both, the admissible bases below one
hundred are ten, nineteen, seventy-three and eighty-two, and ten is the
least. The mechanisms are the construction's own content and are not
derived from anything more primitive.

The integer is therefore derived, in the ordinary sense that it follows from
stated premises with no step free to have gone otherwise. Conditionality on
declared premises is not a weakness in a derivation; it is what a derivation
is. What would be a weakness is a parameter fitted to the answer, and there
is none here. What remains open is narrower than it may
appear, and it is not a question about the standing of integers. This
account treats the register as physically discrete. A count is then a fact
about the register rather than an abstraction brought to it from outside,
and there are not two realms here to be placed in correspondence.

The open question is which office the count fills. The demonstration fixes
the integer. It does not by itself fix that the role this integer occupies
is the electromagnetic coupling rather than another dimensionless ratio the
register carries.

That is the same kind of gap as §6.2 below. Both assign a derived structure
to a physical office, and neither is closed by further arithmetic. Neither
is a fitted parameter, and this account contains none. Contact with
measurement is how a construction is tested and not a defect in how it was
built, since on the contrary standard no result in physics would qualify.

### 6.2 The tail

The tail's numerator is over-determined, by routes that share no
construction:

| route | construction | value |
|---|---|---|
| the two cycles | lcm(9, 12) | 36 |
| the nucleon average | 1008 ÷ 28 | 36 |
| the descent's dominant | 24 × 3/2 | 36 |

The second route is one the programme already carries in another place.
Twenty-eight times the tail is the mean of the proton and neutron masses
in atomic mass units, to within four parts in a million on the 2018
adjustment and six on the 2022 one. Read in the other direction, 1008
divided by 28 returns the numerator exactly, and 1008 is 42 × 24 in the
same vocabulary.

The placement question then divides in two. Through the nucleon route
the placement arrives with the numerator. Atomic weights are
dimensionless ratios to the carbon-12 twelfth; the archetypal average
reads 1.008 = 1008/1000 on the register; and dividing by twenty-eight
delivers 0.036 with its decimal position included. At the measured level
the route gives 0.035998953 against the measured tail — within four
parts per million on the 2018 adjustment, six on the 2022. What that
route makes precise is its two inputs: the twenty-eight, and the carbon
anchor of the atomic scale. From the register alone, with no anchor,
nothing above fixes the third decimal place rather than another; the
base is fixed and the register is three-dimensional, which is a reason
and not a proof. That narrower step is what remains open.

### 6.3 The constructed value against measurement

The construction gives 137.036. Every modern measurement excludes it:

| source | α⁻¹ | gap from 137.036 | relative |
|---|---|---|---|
| Berkeley 2018 | 137.035999046 | 9.5 × 10⁻⁷ | 7.0 × 10⁻⁹ |
| CODATA 2018 | 137.035999084 | 9.2 × 10⁻⁷ | 6.7 × 10⁻⁹ |
| Paris 2020 | 137.035999206 | 7.9 × 10⁻⁷ | 5.8 × 10⁻⁹ |
| CODATA 2022 | 137.035999177 | 8.2 × 10⁻⁷ | 6.0 × 10⁻⁹ |

The relative gap lies between 5.8 and 7.0 parts in 10⁹ across the four
sources, and is 6.0 on the CODATA 2022 value.† The same gap expressed in
standard deviations is not stable, and runs from 35 to 72 across these
four, because it divides a fixed quantity by an uncertainty that differs
by laboratory and by year. The relative figure is the one that carries
information, and the figure in standard deviations should not be quoted
as though it did.

<div class="vnote">† Version 1 said stable near seven parts in 10⁹, and
put the zero-momentum reading nine parts in 10⁷ below the rest value, on
the 2018 adjustment.</div>

The constructed value is therefore an ideal one and not a prediction of
the measured value. In the companion records' terms it is the rest
value, and the measured figure differs from it by the perturbation
offset. The rest value fills exactly one six-digit turn, 137|036, the
two Midy halves, and the offset lies in the turn that follows. The
zero-momentum reading stands 8.2 parts in 10⁷ below the rest value, and
the running of §4 carries measurement away from the rest value with
rising momentum, not toward it. The rest value is reached only by
calculation: the two-tier reading of §5, applied to the coupling itself.
The departure is small and real, and two accounts of it stand in this
paper: the nucleon route of §6.2, which characterizes the offset to
parts per million, and §4's count per depth, which remains open.

**One fact about the tail that is not this account's.** The Units record
establishes that α as defined in the 1948–2019 system was proportional
to π by stipulation, so that α/π carried no π at all, and the leading
term of the anomalous moment was π-free by construction. That is a
statement about the system of units and not about nature, and it is
repeated here because it constrains what a structural reading of the
digits could mean.

---

## 7 · The anomalous moment

The electron's magnetic moment exceeds the Dirac value by a small amount:

| quantity | value |
|---|---|
| g_e | 2.002319304361 |
| a_e = (g − 2)/2 | 1.159652180590 × 10⁻³ |

The received calculation expands a_e as a series in α/π. With the
coefficients now computed [8] and the CODATA 2022 value of α, five terms
reproduce the measurement [7] to four parts in 10⁹:†

| order | coefficient | term |
|---|---|---|
| 1 | 0.500000000 | 1.161410 × 10⁻³ |
| 2 | −0.328478966 | −1.772305 × 10⁻⁶ |
| 3 | 1.181241456 | 1.480420 × 10⁻⁸ |
| 4 | −1.912245764 | −5.566799 × 10⁻¹¹ |
| 5 | 6.737 | 4.555582 × 10⁻¹³ |

<div class="vnote">† Version 1 printed the coefficients of 2012 at
fourth and fifth order, −1.9106 and 9.16, and three parts in 10⁹.</div>

**The Dirac value is held.** The value g = 2 is the doubling the spin
moment rides, and it is exact in this account. The correction is not.

**The correction is inside this account's boundary.** The quantity a_e
is dimensionless. The dimensional boundary permits this account to
address dimensionless ratios and forbids it only dimensionful
magnitudes. The anomalous moment is therefore in scope, and its
computation remains open.

**The missing quantity is a rate, the change of a quantity per unit of
depth.** The gap has the same shape as the one left open in §4. Section
4 gives the running's direction and not its size, and a correction to
the moment would need the same rate. Whether one supply closes both is
open, and §8 states what a supply would have to satisfy.

---

## 8 · What would refute this paper

1. **The floor.** If a measurement resolves structure below the register's
   deepest reachable cell, the supply argument fails and every finiteness
   claim above fails with it. The bound is the same one the Navier–Stokes
   and gravity accounts rest on, so a failure here is a failure in all
   three.

2. **The direction of the running.** The account fixes the sign: greater
   depth returns a larger coupling. A measured running of the
   electromagnetic coupling in the opposite direction, at any momentum,
   refutes §4. The observed direction is currently as the account requires.

3. **The magnitude of the running.** It remains open. A derivation of
  the count per depth that returned a magnitude disagreeing with the
  measured flow would refute the reading rather than complete it.

4. **The identification of §5.** If the bare-to-dressed map is shown to
  differ in structure from the rest-to-measured map of the companion
  records, the identification is refuted. One case would be a scheme
  choice shown to change a measurable rather than only a bookkeeping
  convention. The two must be the same map or the section fails.

5. **The integer.** The uniqueness of 137 under the stated condition is a
   finite check and can be repeated in a few lines. What is open is which
   office the count fills. A structural condition motivated as
   independently, reaching a different integer, removes the assignment to
   the electromagnetic coupling and removes nothing else here.

6. **The placement.** The numerator 36 is over-determined; its position
   arrives through the nucleon route, carried by the carbon anchor,
   and is not yet fixed by the register alone. A register-native
   derivation of the position closes §6.2 entirely. A demonstration that
   no such derivation exists leaves the integer and the anchored route
   standing and withdraws the register-native placement.

7. **The correction.** A computation of a_e from this account's own
  structure closes §7. A demonstration that a_e cannot be reached from a
  dimensionless construction would be more consequential, since it would
  contradict the dimensional boundary's own statement of what this
  account grips.

A condition that is met is recorded as a refutation and is not
reinterpreted. The program then uses the miss to find why the
construction failed, and a revised statement enters as a new one under
its own date.†

<div class="vnote">† Added in version 2.</div>

---

## 9 · Verification

Every exact statement in this paper is machine-checked in the public suite:

- the factorization 137 = 2⁷ + 3², and ord₁₃₇(10) = 8 with 137 dividing
  10⁸ − 1
- the measured values of α at zero momentum and at the Z mass, and the
  direction of the flow between them
- the five-term series for a_e and its agreement with measurement to four
  parts in 10⁹
- the operation-supply bound and the existence of u_min, in the gravity
  record's own battery
- the statement that a_e is dimensionless, by explicit dimensional analysis

The battery is `verify/test_qed_on_discrete_terms.py`. With this paper's
source it is public at github.com/thefirsthorstmann/g-theory-verify, and
a reader with Python can re-derive the paper's entire exact content from
it.

---

*Companion records.* Units on Discrete Terms carries the dimensional
boundary and the classes of constants, DOI 10.5281/zenodo.22119360.
Gravity on Discrete Terms carries the operation-supply theorem and
u_min, DOI 10.5281/zenodo.22087599. The Fine-Structure Constant on
Discrete Terms carries the integer 137, DOI 10.5281/zenodo.21211050. The
Origin on Discrete Terms carries the two-tier reading of §5, the rest
value and the measured value, in its definitions, and the hexad's two
orderings, in its first volume, DOI 10.5281/zenodo.21212112.

*References: [1] R. P. Feynman, QED: The Strange Theory of Light and
Matter (1985) · [2] L. P. Kadanoff, Physics 2 (1966) 263; K. G. Wilson,
J. Kogut, Phys. Rep. 12 (1974) 75 · [3] L. Bombelli, J. Lee, D. Meyer,
R. D. Sorkin, Phys. Rev. Lett. 59 (1987) 521 · [4] C. Rovelli, L.
Smolin, Nucl. Phys. B 442 (1995) 593 · [5] K. G. Wilson, Phys. Rev. D 10
(1974) 2445 · [6] N. Margolus, L. B. Levitin, Physica D 120 (1998) 188 ·
[7] X. Fan, T. G. Myers, B. A. D. Sukra, G. Gabrielse, Phys. Rev. Lett.
130 (2023) 071801; P. J. Mohr et al., CODATA 2022, Rev. Mod. Phys. 97
(2025) 025002 · [8] T. Aoyama, T. Kinoshita, M. Nio, Atoms 7 (2019) 28.*

<div class="copyright" style="margin-top:24pt">Copyright<br>Christian Horstmann · August 26th, 2026 · version 2, October 2026<br>thefirsthorstmann@gmail.com<br>All rights reserved</div>
