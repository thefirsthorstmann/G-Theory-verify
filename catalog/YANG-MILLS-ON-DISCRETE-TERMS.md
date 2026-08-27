---
title: Yang–Mills&#58; Existence on Discrete Terms
subtitle: The physical instantiation of the continuum object is a supertask: existence by inspection, and the mass gap where the count can ask it.
byline: Christian Horstmann · thefirsthorstmann@gmail.com · July 12th, 2026 · posted August 26th, 2026 · manuscript for the public record
date: 2026-07-12
titlenote: This paper examines the Yang–Mills existence and mass-gap problem on discrete terms, comparing the structure the axioms require of a bounded region with the structure physical bounds allow a region to hold. No theorem of continuum mathematics is disputed anywhere in this manuscript, and asymptotic freedom is accepted at full strength. The argument is presented in full and stated so that it can be refuted; all exact claims are pinned by a mechanical test suite accompanying the manuscript and rerun on every revision, public with this paper's source at github.com/thefirsthorstmann/g-theory-verify. This is the second version. The first was submitted to an adversarial multi-agent review of fifty findings, of which forty-nine were sustained in whole or in part; every sustained repair is incorporated, and the review ledger is preserved alongside the suite.
abstract: The Yang–Mills existence and mass-gap problem asks for a quantum gauge theory on continuum ℝ⁴ satisfying the Wightman or Osterwalder–Schrader axioms. This paper compares what those axioms require of a bounded region with what physical bounds allow it to hold. The mode structure of a region is an octree: level n holds 8ⁿ cells, and the census through depth N is (8^(N+1) − 1)/7. The axioms make every level available without bound. Three standard results limit what a physical system occupies of it. One quantum at level n carries energy of order 2ⁿ·πℏc/L, so a system of energy E reaches no deeper than log₂(EL/πℏc). The Bekenstein bound, derived within quantum field theory by Casini, allots a region 2πER/ℏc nats of distinguishable state, about thirty-six bits for the proton. The Margolus–Levitin theorem allots 2ET/πℏ operations, confining any simulation to depth nineteen for a proton-second. The ladder from the confinement scale to the Planck scale spans sixty-six octaves; verified quantum chromodynamics occupies sixteen; the axioms make available infinitely many. The mass gap is addressed in three registers: a theorem of the lattice formulation at strong coupling, due to Osterwalder and Seiler; a measurement of the scalar glueball near 1.7 GeV; and a magnitude fixed by dimensional transmutation. Balaban's program obtained ultraviolet-stability bounds uniform in the lattice spacing but stops short of the completed object; the one classified four-dimensional interacting family is Gaussian in every scaling limit. Asymptotic freedom is accepted at full strength, and no theorem of continuum mathematics is disputed. What remains open is a property of the notation rather than of the gauge field. Every exact claim re-derives in a public suite at github.com/thefirsthorstmann/g-theory-verify.
---

## 1 · Introduction

The Yang–Mills existence and mass-gap problem asks for a proof that a non-trivial quantum Yang–Mills theory exists on ℝ⁴ for every compact simple gauge group, with axiomatic properties at least as strong as the Wightman or Osterwalder–Schrader framework, and that its spectrum has a gap Δ > 0 above the vacuum [1, 2]. It has stood open since the theory was written down [3], and was named a millennium problem in 2000. This paper examines the problem on discrete terms, by the same instrument and in the same manner as this program's treatment of the Navier–Stokes regularity problem [4]. The present argument is the second application of a single observation: **the continuum, taken as a physical object, demands actual infinities of finite things, and the demand is inconsistent with the physics that supplies its motivation.**

One boundary is drawn before anything else, because the entire argument lives on the correct side of it. No theorem of continuum mathematics is disputed in this paper — not the axioms, not the reconstruction theorems, not the existence of free fields on ℝ⁴, which is rigorous and accepted. Mathematics defines its objects by quantifiers, and nothing is due to physics for the privilege. The claims of this paper attach to two other things. The first is the **physical instantiation** of the demanded object: what it would take for any bounded region of this universe to hold, exhibit, build, or certify the structure the axioms make available. The second is the **stated motivation** of the problem, which is not mathematical. The prize rests, in its own public description, on the experimental success of the gauge theory [1], and the identification of that success with the demanded construction is a physical claim, examinable by physical accounting.

Three claims are proved.

**First.** The physical instantiation of the demanded object is a supertask, on three independent meters. The mode ledger of a bounded region is an octree whose census through depth N is (8^(N+1) − 1)/7, and the axioms make every level available without bound (Lemma 2). Occupying structure at level n costs energy of order 2ⁿ·πℏc/L per quantum — the occupancy meter, which is nothing but E = ℏω; holding distinguishable state is metered by the Bekenstein bound, derived within quantum field theory itself [7, 8]; and any staged physical construction or simulation of the ledger is metered by the Margolus–Levitin theorem [5, 6]. All three supplies are finite and the reachable depths logarithmic (Theorem 1); the availability demanded is infinite. No appeal is made to a fundamental lattice or to any discreteness of spacetime: the meters are theorems about energy, entropy, and distinguishable change as such, and they bind any substrate whatsoever of finite energy — the criterion for their authority, against the axioms' lack of it, is given in Section 2.

**Second.** Nothing empirical is lost, and the scope of this claim is exact. Every **nonperturbative** ab-initio number the strong interaction has supplied to experiment — the hadron spectrum, the glueball masses, the string tension, the flavor matrix elements — was computed on the lattice formulation [9], a counting dynamics whose existence at every finite depth is inspection. The perturbative record — the R-ratio, the scaling violations, the jet cross sections, the running of the coupling itself — is the physics of the asymptotic octaves, where the one-loop inverse coupling is a linear meter of octave count (Lemma 1) and the higher corrections are themselves functions of the octave count alone. Both records live at finite depth; neither ever used the completed object.

**Third.** The surplus commitment of the continuum — actually infinite available structure in every bounded region — entails no finite-precision observable consequence directly: every finite dataset consistent with it is consistent with its denial (Proposition 3). Twice it has acquired indirect consequences through auxiliary couplings, and both consequences were severe: the equipartition divergence of the classical cavity, resolved when Planck quantized mode occupancy [14], and the vacuum-energy divergence, infinite as written and 10¹²³ against observation under the most charitable truncation [15] — the second still unresolved. We read the persistence of that discrepancy as the mark of the commitment's standing, and the reading is stated as a reading.

The mass gap is addressed on the field's terms in Section 7 and graded exactly: theorem at strong coupling, measurement in the scaling window, magnitude by dimensional transmutation — the supplied ruler this program's Scale Theorem requires of every dimensionful quantity [17]. What remains open — whether the gap survives in the completed limit object — is a question about the notation, and Section 8 records what the one rigorous classification of such limits in four dimensions delivered.

The reader is invited to attack every step; the falsification conditions are stated in Section 12.

## 2 · The meters and their grounds

**Axiom M: The process meter**

A physical process of average energy E performs at most 2ET/πℏ distinguishable state transitions in elapsed time T; and each transition alters a bounded number of degrees of freedom.

The first clause is the Margolus–Levitin theorem [5]; Lloyd applied it to bound the computational capacity of physical systems and of the observable universe, the latter near 10¹²⁰ operations over cosmic history [6]. When parts of a system evolve in parallel, each operation is floored by πℏ/2Eᵢ for the energy Eᵢ allocated to it, and the allocations sum to at most E, so the total in time T cannot exceed 2ET/πℏ however the work is divided [6]. The second clause is the locality of gauge dynamics itself — plaquette by plaquette, vertex by vertex; no known physical interaction has unbounded arity.

**Axiom S: The state meter**

A physical system confined to a region of radius R with energy E holds at most 2πER/ℏc nats — 2πER/(ℏc ln 2) bits — of distinguishable state.

This is the Bekenstein bound [7], derived by Casini inside quantum field theory as a statement about relative entropy, without gravitational input [8]. It meters what a region's **state** distinguishes; it says nothing against the richness of an observable **algebra**, and the distinction is load-bearing throughout this paper.

**The occupancy relation.** One quantum of field structure at refinement level n of a region of size L carries energy of order ℏω ≈ 2ⁿ·πℏc/L. This is not an axiom but the Planck relation itself, and it meters **depth**: a system of energy E obtains no quantum below level log₂(EL/πℏc). It is the simplest meter of the three and the hardest to dispute.

**Which theorems bind, and why the axioms do not.** A referee will note that Axioms M and S are themselves theorems of continuum quantum theory — Margolus–Levitin from Schrödinger evolution on Hilbert space, Casini from the algebras of continuum field theory — and ask why they carry physical authority while the Wightman axioms carry only mathematical standing. The criterion is Carnot's. A theorem that **bounds** what any physical system can do — Carnot's efficiency, Margolus–Levitin's rate, Bekenstein's ledger, Planck's quantization of occupancy — is a floor statement: it survives every substrate, because it states what no substrate can evade, and each such bound has held in every physical test. An axiom system that **demands** structure — infinitely many available levels in every bounded region — is a commitment: it holds exactly where it is instituted, and its distinctive content, Proposition 3 will show, is untestable. Bounds are physics; demands are notation until the demanded structure is exhibited. The three meters bound; the axioms demand; that is the whole asymmetry, and the paper rests on no other.

The finitude the meters require is supplied by the objects the problem's own motivation invokes: the proton and every laboratory system is a bounded region of finite energy. The axioms themselves are scale-free and energy-unbounded — which is precisely the gap between the notation and its stated motivation that this paper measures.

## 3 · The model

Let a bounded region — a cube of side L, and for concrete corollaries the diameter transit 2R/c of a proton-sized sphere — carry a gauge field. The **mode ledger** of the region is dyadic: refinement level n resolves field structure on cells of side L/2ⁿ, and level n holds **8ⁿ cells**. The census through depth N is the telescoping sum

**D(N) = Σₙ 8ⁿ = (8^(N+1) − 1)/7,**

the same octree census, cell for cell, as the cascade ledger of the fluid paper [4]. The **update telescope** is this paper's addition: one refresh of every cell at its own natural frequency — level n at 2ⁿ·c/L — costs U(N) = Σₙ 8ⁿ·2ⁿ = (16^(N+1) − 1)/15 operations per crossing time L/c. The census D(N) is the demand Lemma 2 will read off the axioms; the update demand U(N) is what **running** the ledger requires — of any process that instantiates its levels dynamically. The axioms demand a census; they fix no schedule, and the distinction governs which meter governs what in Theorem 1.

The lattice formulation of Wilson [9] is the ledger instantiated at finite depth: group elements on links, a local action on plaquettes, finite-dimensional integrals whose existence is inspection. The object of the problem statement is the ledger with every level available, in every bounded region, without bound.

## 4 · The door is open and the axioms demand the census

**Lemma 1: The flow converges — asymptotic freedom is granted in full**

*In the pure gauge theory the one-loop inverse coupling grows linearly with the octave count: passing from scale Q to 2Q advances 1/g² by exactly β₀ ln 2 / 8π², with β₀ = 11N/3 [12, 13]. At one loop the flow runs monotonically toward the free fixed point; the two-loop correction (coefficient 34N²/3) and its successors in mass-independent schemes are themselves functions of the octave count alone; no Landau obstruction interrupts the ascent at any finite octave.*

This is the point granted at full strength, the analogue of the converging turnover schedule in the fluid [4]: **the mathematics does not forbid the limit.** Each octave is closer to free, and the ultraviolet door stands open. That is why constructive field theory judged Yang–Mills the best four-dimensional candidate, why the prize chose it, and why the contrast case of Section 8, whose flow runs the other way, ended as it did. The count will not close the door mathematically. It meters every physical passage through it.

Note what the lemma also is: a dictionary entry. The running coupling — the theory's most celebrated equation [12, 13] — advances by equal increments per doubling of scale. **The physics of the gauge field depends on scale through the octave count.** The deciding structure of the theory is, in its own most famous discovery, a count.

**Lemma 2: The axioms demand the completed census — as availability**

*An object satisfying the Wightman or Osterwalder–Schrader axioms on ℝ⁴ makes every level of the ledger available in every bounded region: for every N there are test functions supported on single cells of level N, and the axioms assign the smeared field a nondegenerate operator — structure available at level N — for every N without bound. Exact Poincaré invariance enforces the same census from the symmetry side: a depth-N lattice theory is invariant under the hypercubic subgroup only, its artifacts vanishing as a power of the spacing, and the axioms demand the artifacts vanish exactly — no level is the last. Existence-as-posed therefore carries the completed census D(∞) as available structure.*

Three clarifications, each load-bearing, each stated at the outset.

**Availability is an algebra fact, not a state fact.** No clause of the axioms requires any state to hold, occupy, or exhibit the census; the vacuum is one state, stationary, and by the reconstruction theorem the whole object is equivalent to that one state's correlation functions. The axioms demand that the structure be *there to be had* at every depth; what any physical state can *have* is exactly what the meters of Section 2 measure, and the space between the two — infinite availability, logarithmic occupancy — is the subject of this paper, not a confusion in it.

**The census is blind to interaction and to dimension.** The free field on ℝ⁴ satisfies every Wightman axiom with the same infinite census — rigorously, and accepted without reservation — as do the interacting constructions of two and three dimensions [2]. That is the point, not an objection to it: the census is not what makes the four-dimensional interacting mathematics hard — uniformity of interacting estimates is, and this paper claims no theorem about that. The census is what the axioms make available in any dimension, free or interacting; the meters measure what physics can do with it; and the metering applies to the free field's surplus exactly as to Yang–Mills'.

**The disanalogy with the fluid is structural and stated.** The fluid's criterion — the Beale–Kato–Majda integral — defines an *event*: operations the fluid must execute in physical time, so the process meter carried that conclusion [4]. Existence defines an *object*: a census of availability, so the occupancy and state meters carry here, and the process meter covers only the running of it. The same observation, applied through the meter each problem's own definition selects.

## 5 · The counting theorem

**Lemma 3: Demand**

*The census through depth N is D(N) = (8^(N+1) − 1)/7 cells; the update demand is U(N) = (16^(N+1) − 1)/15 operations per crossing; occupancy at level n costs ≥ 2ⁿ·πℏc/L per quantum; and holding a census costs at least one bit per cell — the floor of the coarsest distinction. Both sums telescope; both are exponential in N.*

**Lemma 4: Exponential defeats linear** — *for every a > 0, 8ⁿ overtakes a·n within finitely many steps, and the ratio at least quadruples per step; identically for 16ⁿ.* Arithmetic, as in [4]. ∎

**Theorem 1: The completed census is physically unoccupiable, unholdable, and unrunnable**

*Let a region of size L (radius R) hold energy E and evolve for time T under the meters of Section 2. Then:*

*(occupancy)* *no quantum of structure below depth* **N\*ₒ = log₂(EL/πℏc)** *is ever excited;*

*(state)* *no state of the region holds a census beyond depth* **N\*ₛ ≤ log₈(14πER/(ℏc ln 2) + 1) − 1;*

*(process)* *no staged physical construction, simulation, or dynamical running of the ledger completes a depth beyond* **N\*ₚ ≤ log₁₆(30ET/πℏ + 1) − 1** *within T.*

*All three are logarithmic in the resources. The object of Lemma 2 makes infinitely many levels available; no physical system in a bounded region ever occupies, holds, or runs more than logarithmically few of them. The availability beyond every physical reach is the surplus, and it is carried entirely by structure no state exhibits.*

*Proof.* Occupancy: the Planck relation and Lemma 3. State: (8^(N+1) − 1)/7 bits ≤ 2πER/(ℏc ln 2) by Axiom S. Process: (16^(N+1) − 1)/15 ≤ 2ET/πℏ by Axiom M, with parallelism covered by the allocation accounting of Section 2. Finiteness by Lemma 4. ∎

**Corollary 1: The reach, concretely** (all values machine-verified; inputs stated)

A proton — energy 938 MeV, radius 0.84 fm, crossing time the diameter transit 2R/c — commands a Margolus–Levitin rate of 9.1 × 10²³ operations per second: **about five operations per crossing**. Its Bekenstein ledger is **thirty-six bits** — a census held through **depth one**. Its entire rest energy cannot obtain one quantum of structure below **level two** under any wave convention — the occupancy meter agreeing with the state meter that a proton's depth is one-ish, exactly the physics of its actual excitation spectrum. One full second of proton time allows an update-metered construction depth of **nineteen**. The operation budget of the observable universe, 10¹²⁰, runs the ledger to depth **ninety-nine**; its holographic ledger of ~10¹²³ bits holds no census beyond depth **one hundred thirty-six**. The conceivable ladder of the theory — confinement scale (taken at the conventional Λ = 200 MeV; other schemes shift the count by under an octave) to Planck — spans **65.7 octaves**; experimentally verified quantum chromodynamics occupies **16**. The axioms make available infinitely many. Between the deepest verified octave and the demanded infinity stand not fifty octaves but all of them.

**Corollary 2: Nature fits comfortably**

The physical gauge field never made the demand. Hadronic structure occupies the first octaves above the confinement scale; collider physics probes sixteen; deep-inelastic scattering resolves partonic structure at the octaves its beam energy reaches — the occupancy meter's own arithmetic, with the probe's energy, not the proton's, paying for the depth. Every physical interrogation of the strong interaction, ever, has been an exchange of finite-depth structure the region can support. The theorem bars nothing nature does; it meters the one thing nature is never asked to do — hold the completed census.

**Theorem 1′: The universal form**

*Any object whose definition demands infinitely many available levels in a bounded region of finite energy exceeds every meter — occupancy, state, and process — at a finite rank; any process whose completion demands infinitely many sequential distinguishable stages from finite energy violates the Margolus–Levitin floor at a finite stage. "Infinitely many distinguishable structures, in a finite thing" is a contradiction in quantum mechanics.* This is the same observation that closed the fluid argument [4], now in its state form beside its process form — and the reappearance is the point. Two millennium problems, posed against physical objects of finite resources, each define their central question as the completion of an infinite census. The inconsistency is internal to the formulations: the physics they invoke is finite by their own hypotheses, and the objects they demand are not.

## 6 · The spectrum is delivered in full

The scope of the empirical claim, stated exactly: every **nonperturbative** ab-initio number the strong interaction has supplied to experiment was computed on the counting formulation. The light-hadron spectrum, from three inputs, at few-percent precision [10]; the glueball spectrum of the pure gauge theory, the scalar near 1.7 GeV [11]; the static potential and string tension; the flavor matrix elements; the hadronic pieces of the muon's magnetic moment. The perturbative record — the R-ratio, deep-inelastic scaling violations, jet cross sections, the measured running of α_s — is genuine, confirmed, and belongs to the asymptotic octaves: computed where Lemma 1's meter runs, at depths experiment reaches, by expansions in a coupling that counts octaves. Between them the two records exhaust the theory's contact with experiment, and both live at finite depth. The completed object of the problem statement has contributed no number to either, because it has never been shown to exist — the problem statement's own acknowledgement [2].

On the continuum extrapolations of the lattice industry: the a → 0 extrapolation of [10] and its kin is Richardson extrapolation of a convergent sequence of dimensionless ratios of finite-depth theories — an estimate of a limit **value**, not a construction of a limit **object**. Numbers converge; the demanded object is a field on ℝ⁴ at census infinity. The industry's precision practice and this paper's accounting are the same arithmetic read in the same direction.

Two arithmetic remarks are displayed for the record, carrying no inferential weight, in the manner of their twins in [4]. The structural constants of the theory are the group's own small integers: three colours, N² − 1 = 8 = 2³ gluons, Casimirs C_F = 4/3 = 2²/3 and C_A = 3, one-loop coefficient β₀ = 11N/3, the celebrated 11 of the pure SU(3) flow. The octave meter of Lemma 1 makes the theory's ultraviolet law a statement of equal increment per doubling. The gauge theory's deepest equation counts; the display claims nothing further.

## 7 · The mass gap on the field's terms

The gap claim is Δ > 0 — in the prize's public voice, that *"the quantum particles have positive masses, even though the classical waves travel at the speed of light"* [1]. On discrete terms the claim decomposes into three graded parts, and the grading is the content.

**Theorem, at strong coupling — with its scope stated against it.** The convergent cluster expansion of Osterwalder and Seiler establishes exponential clustering — a mass gap — and the area law for the Wilson theory at sufficiently strong coupling, for **any** compact gauge group [16]. Any: including U(1), whose continuum physics is a massless photon and a Coulomb phase — and four-dimensional lattice U(1) provably **deconfines** at weak coupling [21, 22]. The strong-coupling gap is therefore a lattice-phase fact, and the physical question is persistence into the scaling window. That is the structure of the evidence: the abelian theory escapes through a phase transition on the way to weak coupling, and fifty years of instrument record show SU(3) exhibiting no such escape — the difference being exactly the non-abelian flow of Lemma 1, which runs the two theories in opposite directions. The strong-coupling theorem opens the case; the instrument closes the physical half of it.

**Measurement, in the window.** In the scaling window — where the numbers of Section 6 are computed — the lightest excitation of the pure SU(3) theory is the scalar glueball near 1.7 GeV [11], and no massless excitation of the strong sector has ever appeared: on the instrument, or in the hadronic spectrum nature exhibits. The gap stands wherever the gap can be physically asked.

**The magnitude is the supplied ruler.** Classical Yang–Mills has no scale; the quantum theory generates one by dimensional transmutation — the running of Lemma 1 converts a pure number into a scale Λ, and every mass is a dimensionless number times Λ, with Λ fixed by one calibration against experiment. This is a theorem of this research program arriving in standard dress: **no dimensionless construction yields a dimensionful magnitude; magnitude is number times a borrowed ruler** [17]. The counting theory owns the ratios and the gap's existence at every askable depth; the MeV is the honest calibration.

What remains — all that remains — is whether a gap survives in the completed limit object, at census infinity, where no instrument, probe, or state has ever operated or could. Section 8 records what the one rigorous classification of completed four-dimensional limits found there. The gap where physics lives is proved and measured; the gap in the surplus is a property of the notation, awaiting the notation's own answer.

## 8 · What the rigorous record actually says

Two bodies of rigorous work frame the continuum question, and this paper reads both without inversion.

The first is the constructive program. Balaban's renormalization-group analysis of four-dimensional lattice Yang–Mills established ultraviolet-stability bounds **uniform in the lattice spacing** — control of the effective actions across all renormalization steps, in finite volume, a monument of rigor [18]. What the program did not reach is the completed object: the correlation functions, the infinite-volume limit, the reconstruction of the axioms. The stall is at the assembly of the thing itself. The reading this paper takes, offered as a reading, is that the program's own structure says why. It is counting, octave by octave, executed by hand at the highest standard the subject possesses, and what stands between its uniform bounds and the demanded object is precisely the passage from every finite depth to the completed census. In two and three dimensions, where the census demand is light — superrenormalizable, finitely many divergences — the constructive program **succeeded**: P(φ)₂ with its nontrivial scattering, φ⁴₃, Yukawa₂ [2]. The dimension-dependence of the record is the count's own fingerprint: completion succeeds where the ledger is affordable and stalls where it is not.

The second is the result from the one classified case. In 2021 Aizenman and Duminil-Copin proved that every (subsequential) scaling limit of the critical four-dimensional nearest-neighbor Ising and φ⁴ lattice models is Gaussian [19]: in the one four-dimensional interacting family whose continuum limits have been rigorously classified, **no limit houses the interaction**. This paper claims no triviality for Yang–Mills — Lemma 1's open door is accepted at full strength, and the mechanisms differ. The theorem carries a different weight: it is the only rigorous datum in the dimension about what completed limits deliver, and the datum is a free field. Those who assert that the completed census houses the physics must supply a four-dimensional example in which it ever has; in two and three dimensions they have them; in four, the classified record reads Gaussian.

And the formalism's own relationship to counting deserves exact statement, because it is not what a casual reading of either side suggests. Axiomatic field theory **can** count: the nuclearity condition of Buchholz and Wichmann [20] bounds the local degrees of freedom below an energy cutoff, and Casini's theorem [8] — this paper's own state meter — meters a region's distinguishable state from inside the formalism. But both are finiteness criteria and theorems **about states and energy**, bolted onto axioms that do not require them: the bare Wightman demands are census demands, type-III local algebras with available structure at every scale and divergent raw entanglement. The formalism recovers physical finitude exactly the way this paper does — by installing an energy meter and measuring what states can hold against what the axioms make available. The count is not foreign to the continuum's mathematics. It is the part of the continuum's mathematics that does the physics.

## 9 · The epistemic status of the surplus

**Proposition 3: Observational indistinguishability** *(on the instrument's own convergence record)*

*Let O be any finite set of observations of strong-interaction physics, each of finite precision. If the continuum theory is consistent with O, so is a lattice theory of sufficiently fine spacing.*

*Grounds.* Lattice observables approach their scaling-window values with corrections vanishing as powers of the spacing, the Symanzik systematics that constitute the lattice community's own validated error budget. The record of Section 6 demonstrates that at feasible spacings the lattice values sit inside experiment's intervals. Choose the depth accordingly. The claim is empirical-methodological, resting on the instrument's convergence record rather than on a convergence theorem — the available strength, stated as such. ∎

**Corollary 5: The surplus is directly unfalsifiable**

The distinctive content of the continuum commitment — actually infinite available structure in a bounded region, as against finite — entails no finite-precision observable consequence: every finite dataset consistent with it is consistent with its denial. The quantifier order bears stating, because it is the whole logic: each level is individually testable by a probe that meets that level's occupancy requirement, and each test to date is matched by a finite-depth theory; what no finite dataset ever touches is the infinite conjunction — that no level is the last. By the demarcation standard the sciences apply to every other object [23], the conjunction is not an empirical claim. It is a choice of notation.

Directly unfalsifiable — and twice engaged indirectly, through auxiliary couplings, with severe consequences. The first: classical equipartition over the actually-infinite mode family of a cavity predicts divergent radiated energy, and measurement contradicts it. Planck's resolution was reached from the infrared data before the divergence had been fully diagnosed, the count preceding the catastrophe's naming [14]. It was to quantize the **occupancy** of each mode, so that deep modes, whose quanta lie beyond the thermal budget's reach, stand empty. The mode family stayed infinite; the occupancy became counted; the divergence died at exactly the meter this paper's Section 2 carries forward. The second: couple the zero-point energy of the mode family to gravity, and the result is infinite as written; truncate the census, most charitably, at the last physically motivated octave — the Planck scale — and the discrepancy is still of order **10¹²³** against the measured vacuum energy density (machine-verified in the suite; the classic statement of the problem is [15]). The first was settled by counting occupancy. The second remains on the continuum's ledger. We read its century of non-payment as the standing mark of what the surplus is — and that reading is stated as a reading, since the account is not closed.

The identification of "a continuum Yang–Mills theory exists" with "the gauge field exists" therefore has the following status. The field's existence is a fact of nature at every reachable depth, computed on a formulation whose existence is inspection. The demanded object's existence is a fact about the surplus — about availability no state holds, no probe certifies, one rigorous classification has found empty of interaction, and both indirect examinations have found severe. The two claims are distinct; the literature has treated them as one; and the conflation, not the mathematics, is what this paper examines.

## 10 · The problem's terms

The Institute publishes the problem in two voices. The formal statement — Jaffe and Witten's — is sober mathematics [2], exact about its own condition: it states that no mathematically complete example of the demanded kind exists in four dimensions. Its demand is taken exactly: ℝ⁴, Wightman strength, every compact simple group. The public description states the motivation in one sentence [1]: *"Quantum Yang-Mills theory is now the foundation of most of elementary particle theory, and its predictions have been tested at many experimental laboratories."* Quoted exactly — and it asserts an identification: that the theory the laboratories confirmed is the object whose construction the prize demands.

This paper has measured the distance between the two. The laboratories' record is Section 6's: nonperturbative numbers from the counting formulation, perturbative numbers from the asymptotic octaves, all at depths reachable many times over (Corollary 2); every observation in that record or ever to join it is matched by a finite-depth theory (Proposition 3); and the demanded object carries its content precisely in the census no laboratory reaches (Theorem 1). The success and the demand are about different things, and the difference is exactly the question.

The difficulty lies in none of the usual places. Jaffe and Witten's formal statement is exact, and candid about its own condition. The constructive analysts' uniform bounds are treated here as the count executed by hand [18]. Least of all does it lie with the lattice formulation, whose fifty years of finite-depth arithmetic are the actual mathematical content of the laboratories' success. It lies in the identification, which draws on the empirical record for an object that record never used.

The problem's terms admit two readings, and the results above bear differently on each. **On the first, the empirical motivation is set aside and the question is understood as the internal consistency of an idealization** — one whose known four-dimensional classifications return free fields, and whose finiteness criteria arrive as separate conditions. **On the second, the motivation is the physical field, in which case answers on the field's terms are admissible**: existence by inspection at every physically reachable depth, for every compact group; the gap by theorem at strong coupling for every compact group, and by measurement, for the group nature realizes, in the window where every laboratory has ever operated. The two readings are not combinable, with the empirical record supplying the motivation and the idealization supplying the content.

## 11 · Objections

**Objection: mathematical existence needs no physical instantiation; the supertask objection lands on a claim nobody made.** Correct as far as it goes, and stated in Section 1 at the outset: no theorem of continuum mathematics is disputed, and mathematics defines by quantifiers freely. The observation concerns the stated motivation and the identification — the prize's own public description rests the construction on laboratory physics [1] — and to the physical-instantiation claims that identification implies. Section 10's two readings are the formal shape: keep the empirical motivation and accept the field's terms, or keep the notation and set the motivation aside. The objection, pressed to the end, simply takes the second reading, at which point this paper's §13 accepts the residue.

**Objection: the vacuum is stationary — the process meter reads zero on the axioms' central object.** Exactly so, and the architecture says so: the axioms fix no schedule, which is why existence is metered as occupancy and state, and only construction, simulation, and dynamics as process (Section 3; Theorem 1). The stationary vacuum holds what a state can hold; it runs nothing; and what the axioms make available beyond its holdings, Lemma 2 counts and the meters measure.

**Objection: the lattice is a scaffold; only the continuum limit is the theory.** The approximation arrow runs the other way, jointly in mathematics and history. The lattice theory is autonomous — finite integrals, existence by inspection — and it produced the nonperturbative record; the "fundamental" object has produced no number, having never been shown to exist [2]. The industry's own a → 0 extrapolations are estimates of limit values of the counting theory's ratios, not invocations of a limit object (Section 6). To insist the scaffold is provisional and the unbuilt edifice fundamental is the commitment under examination, restated.

**Objection: φ⁴ triviality says nothing about asymptotically free Yang–Mills.** Agreed, twice over (Sections 4 and 8): no triviality is claimed, and the door is accepted as open. The classification carries a different weight — the burden of exhibiting a four-dimensional completion that houses interaction, against a record of two- and three-dimensional successes, one four-dimensional classification returning Gaussian, and fifty years of stall at the assembly point.

**Objection: Poincaré invariance is exact in nature.** Exactness is a universally quantified claim over all precisions, and no finite-precision measurement certifies it — Proposition 3's quantifier logic verbatim. The symmetry's observed content is depth-graded and delivered at every tested depth by the count.

**Objection: renormalization already handles the infinities.** Renormalization is the count's own discipline practiced inside the notation — cutoffs installed, octave-to-octave flow computed, physics expressed in flow-invariants; the renormalization group is octave bookkeeping, and Lemma 1 is its most famous page read literally. The formalism's finiteness instruments — nuclearity [20], Casini's bound [8] — are the same move made rigorous (Section 8). That the continuum's rescue apparatus is a counting apparatus is not an objection to this paper; it is this paper.

**Objection: the Bekenstein bound is speculative.** Casini's derivation is a theorem of relative entropy inside quantum field theory, without gravitational input [8]. And the load is distributed: the occupancy relation — bare E = ℏω — carries the depth conclusion independently, and the process meter independently bars every staged construction and simulation. A reader who withholds assent from Axiom S keeps both.

**Objection: this is finitism.** No. Finitism disputes the mathematics; this paper accepts all of it. The claims are physical, their instruments are theorems of physics, and the burden runs the other way: to refute the meters one must exhibit a bounded physical system holding or executing unboundedly many distinguishable structures on finite energy — that is, refute quantum mechanics.

## 12 · What would refute this paper

Any of the following lands. A finite-precision observation inconsistent with every finite-depth theory — a measurement that requires the surplus, which by Proposition 3 no measurement can be. A violation of the Margolus–Levitin bound, of the Bekenstein bound in Casini's form, or of the Planck occupancy relation. A massless excitation of the strong sector, on the instrument or in the hadronic spectrum, refuting the gap where this paper asserts it. A demonstration that the nonperturbative record of Section 6 requires the completed object at any point of its pipeline. Conversely, a rigorous continuum construction of four-dimensional Yang–Mills with a mass gap would not contradict the physical claims made here. It would, however, be the first four-dimensional completion housing an interaction. It would carry with it the account of how the census is assembled, the step five decades of the constructive program have located as the stall, and would settle §7's residue in the notation's favour. On that outcome the second reading of Section 10 holds, with the mathematics enriched and the physical accounting of Sections 2–6 standing exactly as written. And should the construction complete the way the one classified family completed — trivially — the reading of Section 8 is confirmed in the strongest form. The alternative commitment, for its part, can name no observation that would refute its distinctive content; that is Corollary 5, and it is the whole point.

## 13 · Conclusion

The Yang–Mills existence and mass-gap problem, examined on discrete terms, resolves into two questions that fifty years of literature have treated as one. The physical question — does the gauge field exist, and is it gapped — is closed, and was closed by the field's own instruments. Existence follows by inspection at every depth any bounded region can reach. The gap follows by theorem where the coupling is strong and by measurement everywhere the window opens, and the magnitude by the one borrowed ruler that every dimensionful quantity requires. The notational question — whether the idealization those instruments never used can be completed at census infinity — remains open, and is a question about the notation. Its accounting is now stated: the availability it demands is infinite; the occupancy, state, and process any physical region affords are logarithmic; its one classified four-dimensional completion is empty of interaction; and its surplus, directly untestable, has twice been examined indirectly and stands at 10¹²³ against observation.

This is the second application of a single observation, which now has its general form. The regularity problem demanded infinitely many executed operations from a fluid of finite energy; the existence problem demands infinitely many available structures of regions of finite energy; the fluid's was an event and fell to the process meter, the field's is an object and falls to occupancy and state — the same structure, examined through the meter each problem's own definition selects. In both, the infinity issues not from the physics, whose hypotheses supply the finitude, but from the founding idealization of the notation — **a formalism whose empirical basis is finite in every observable respect, extended by definition to an actual infinity in every bounded region, and then examined for the behaviour of that infinity.** The fluid answered by counting. The field answers by counting. The pattern will hold wherever a notation's surplus has been mistaken for a property of the world.

Numbers were the instrument of every step: the octree sevenths (8^(N+1) − 1)/7 that count the availability, the ln 2 that makes the running coupling an octave meter, the πℏc/L that sets a level's occupancy, the thirty-six bits of the proton, the 10¹²³ of the standing account. The author's confidence rests there. Time and measurement will decide between the count and the continuum.

## 13b · Addendum: the mechanism of the gap, on the count's own terms

*Added 2026-08-09, on the completion of the program's five-volume derivation — Units, Gravity, The Vacuum, Tonal Function, and Motion on Discrete Terms. The body of this paper is unchanged.*

Section 7 graded the gap: theorem at strong coupling, measurement in the window, magnitude by the supplied ruler. What that grading lacked was a mechanism — a structural reason, on the count's own terms, why the sourced sector of a gauge theory should be gapped at all. The five volumes supply three, each machine checked, each exact where it is arithmetic and labeled where it is a reading.

**The integer gap.** In the program's mechanism, sourcing is counted: the k-th rider of the wheel falls short by exactly k parts, k an integer, and the riderless wheel is the vacuum tier. The spectrum of source strengths is therefore the non-negative integers, and there is nothing between zero and one: the lightest sourced excitation carries one full unit, and the gap exists by integrality, before any dynamics is computed. Only the magnitude awaits calibration, exactly as Section 7's transmutation paragraph states — existence of the gap is the integer step, and the MeV is the supplied ruler. The prize's own contrast sentence — massive quantum particles from massless classical waves — reads, on these terms, as the contrast between the counted and the averaged: the classical wave is the count's deleted average, gapless because averaging erased the integers, and a formulation that keeps the count is gapped by construction.

**The sector theorem.** The figure that carries the program's derivations has an exact spectrum: one uniform mode at zero and four doubled positive frequencies, 2 sin 20°, 2 sin 40°, 2 sin 60°, 2 sin 80°. The mirror splits the doubled frequencies into even and odd partners, and the zero mode is even: the odd sector — the pair sector, which carries every seat-to-seat relation and which the gravity volume identifies as the physical sector — contains no zero mode at all. Its spectrum begins at 2 sin 20°, strictly positive. A sector selected by a symmetry that excludes the uniform mode is gapped by construction, and the two faces of gauge physics sit here as the two mirror sectors of one object: the massless abelian face lives where the zero mode lives, and the confined face is the pair sector, which never had a massless mode to lose. The reading of this split as the abelian–non-abelian difference is labeled a reading; the spectral split itself is exact.

**The native non-abelian structure.** On the ring, rotation and mirror do not commute, and conjugating the rotation by the mirror yields the inverse rotation: the dihedral relation, the minimal non-commutative structure. This is the program's reversal — the fifth read backward, the alternating bidirectional rotation of the two generators — appearing as group arithmetic: non-commutativity is the existence of the reversal, and the abelian case is the case with no reversal to read. The gauge field whose flow Section 4 meters is non-abelian precisely where its structure carries the reversal; the program's substrate carries it natively.

One display joins the record of Section 6, in that section's register, exact and carrying no inferential weight. The celebrated eleven of the pure SU(3) flow, 11N/3 at N = 3, is the total of the directed four-vector of the generator pair — the difference, the pair, the sum: 1 + 2 + 3 + 5, four consecutive Fibonacci numbers, the first rung of the negation family 10 + 1. The identity is arithmetic; its weight is a question the program's base-rate audit owns.

The three legs are pinned in `verify/test_yang_mills_gap.py`. What they change in Section 13 is emphasis: the physical question was closed by the field's instruments; the count says why the answer had to be the gapped one.

## References

[1] Clay Mathematics Institute, *Yang–Mills and the Mass Gap*, public problem description, claymath.org (quoted sentences verbatim from the Institute's pages).

[2] A. Jaffe and E. Witten, *Quantum Yang–Mills Theory*, official Clay Millennium Prize problem description, Clay Mathematics Institute (2000).

[3] C. N. Yang and R. L. Mills, *Conservation of Isotopic Spin and Isotopic Gauge Invariance*, Phys. Rev. **96**, 191 (1954).

[4] C. Horstmann, *Navier–Stokes: A Solution on Discrete Terms*, Zenodo preprint (2026), DOI 10.5281/zenodo.21197045.

[5] N. Margolus and L. B. Levitin, *The maximum speed of dynamical evolution*, Physica D **120**, 188 (1998).

[6] S. Lloyd, *Ultimate physical limits to computation*, Nature **406**, 1047 (2000); *Computational capacity of the universe*, Phys. Rev. Lett. **88**, 237901 (2002).

[7] J. D. Bekenstein, *Universal upper bound on the entropy-to-energy ratio for bounded systems*, Phys. Rev. D **23**, 287 (1981).

[8] H. Casini, *Relative entropy and the Bekenstein bound*, Class. Quantum Grav. **25**, 205021 (2008).

[9] K. G. Wilson, *Confinement of quarks*, Phys. Rev. D **10**, 2445 (1974).

[10] S. Dürr et al. (Budapest–Marseille–Wuppertal Collaboration), *Ab initio determination of light hadron masses*, Science **322**, 1224 (2008).

[11] C. J. Morningstar and M. Peardon, *Glueball spectrum from an anisotropic lattice study*, Phys. Rev. D **60**, 034509 (1999).

[12] D. J. Gross and F. Wilczek, *Ultraviolet behavior of non-abelian gauge theories*, Phys. Rev. Lett. **30**, 1343 (1973).

[13] H. D. Politzer, *Reliable perturbative results for strong interactions?*, Phys. Rev. Lett. **30**, 1346 (1973).

[14] M. Planck, *Über das Gesetz der Energieverteilung im Normalspectrum*, Ann. Phys. **309**, 553 (1901).

[15] S. Weinberg, *The cosmological constant problem*, Rev. Mod. Phys. **61**, 1 (1989).

[16] K. Osterwalder and E. Seiler, *Gauge field theories on a lattice*, Ann. Phys. **110**, 440 (1978).

[17] C. Horstmann, *G-Theory: An Introduction*, Zenodo (2026), DOI 10.5281/zenodo.21212293 — the Scale Theorem.

[18] T. Balaban, *Renormalization group approach to lattice gauge field theories I–II*, Commun. Math. Phys. **109**, 249 (1987); **116**, 1 (1988), and the program cited therein.

[19] M. Aizenman and H. Duminil-Copin, *Marginal triviality of the scaling limits of critical 4D Ising and φ⁴ models*, Ann. Math. **194**, 163 (2021).

[20] D. Buchholz and E. H. Wichmann, *Causal independence and the energy-level density of states in local quantum field theory*, Commun. Math. Phys. **106**, 321 (1986).

[21] A. H. Guth, *Existence proof of a nonconfining phase in four-dimensional U(1) lattice gauge theory*, Phys. Rev. D **21**, 2291 (1980).

[22] J. Fröhlich and T. Spencer, *Massless phases and symmetry restoration in abelian gauge theories and spin systems*, Commun. Math. Phys. **83**, 411 (1982).

[23] K. Popper, *Logik der Forschung* (1934); English: *The Logic of Scientific Discovery* (1959).

<div class="copyright" style="margin-top:80pt">Copyright<br>Christian Horstmann · July, 2026 · posted August 26th, 2026<br>thefirsthorstmann@gmail.com<br>All rights reserved</div>
