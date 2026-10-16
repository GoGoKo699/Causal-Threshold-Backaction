# Thirty milestones for understanding causal threshold backaction

This map describes the scientific project, independently of any reader's prior
knowledge. It contains exactly **30 milestones**. M01–M14 build the background
from individual states and measurements to the complete causal task. M15–M30
assemble the mechanism, matching construction, robust bounds, and scientific
interpretation. The larger second phase reflects the several arguments needed
to connect the universal converse to a physically distributed instrument.

The map is an understanding route, not an inventory of every technical lemma.
Detailed derivations live in the [research documents](../research/PROOF_MAP.md).
The single educational anchor and notation bridge are in [LEARNING](LEARNING.md).
Teaching intensity below means a suggested 1–3-round learning block after a
failed challenge; it does not change the target or imply a learner diagnosis.
Attempts and passes belong to a separate learning session, not to this map.

## Phase I — Background and preliminaries

### M01 — A state, an observable, and an outcome

**Question.** What distinguishes the quantum state of one spin from the classical
value obtained by measuring it?

**Target.** Relate a density operator, the occupation observable, and the Born
probabilities; distinguish a pure superposition from an incoherent mixture.

**Dependencies and role.** Starting point: identify the local objects from which
the many-spin task is built. **Sources.** Watrous Chapter 2, §§2.1 and 2.3;
[worked examples](WORKED_EXAMPLES.md). **Intensity.** 1 round.

### M02 — Total charge and its degenerate sectors

**Question.** What information does total occupation retain about a spin string?

**Target.** Explain why many basis strings share a charge and why preserving a
whole charge sector includes its internal superpositions.

**Dependencies and role.** M01; assemble local occupations into the model's
collective observable. **Sources.** [Model](../research/MODEL.md);
[learning bridge](LEARNING.md). **Intensity.** 1–2 rounds.

### M03 — A measurement specifies probabilities and state changes

**Question.** Why is a binary POVM insufficient to specify backaction?

**Target.** Distinguish an effect, an instrument branch, its normalized conditional
state, and the sum channel when the outcome is ignored.

**Dependencies and role.** M01–M02; identify the mathematical object to which the
theorem applies. **Sources.** Watrous §§2.2–2.3; [model](../research/MODEL.md).
**Intensity.** 2 rounds.

### M04 — Preservation within a sector

**Question.** How does preserving every state in a sector constrain its Kraus
operators?

**Target.** Explain the collinearity argument for a pure preserved state and why
linearity makes each Kraus operator scalar on an entire sector.

**Dependencies and role.** M02–M03; connect a physical nondisturbance assumption
to an algebraic constraint. **Sources.** Watrous §2.2;
[exact proofs](../research/EXACT_PROOFS.md). **Intensity.** 2 rounds.

### M05 — Retained subsystems and one-way causality

**Question.** What would let a change in the background signal to the active block?

**Target.** Use a partial trace to define the active output and explain the
full-channel condition that it depend only on the active input.

**Dependencies and role.** M03; move from one detector to spatially separated
laboratories. **Sources.** Watrous §§2.1–2.2; [model](../research/MODEL.md).
**Intensity.** 2 rounds.

### M06 — The environment remembers charge

**Question.** Where can a measurement place information while leaving a definite
charge state intact?

**Target.** Interpret a Stinespring dilation and charge-dependent pointer states;
relate pointer overlaps to loss of coherence in the retained system.

**Dependencies and role.** M03–M05; connect channel descriptions to the physical
mechanism. **Sources.** Watrous §2.2;
[worked examples](WORKED_EXAMPLES.md). **Intensity.** 2 rounds.

### M07 — Entropy from a pure joint state

**Question.** Why can a meter calculation determine the retained spins' entropy?

**Target.** Use equality of the nonzero spectra of two reductions of a pure state
and recognize the weighted Gram matrix as a smaller spectral calculation.

**Dependencies and role.** M06; identify the quantity that the proofs will bound.
**Sources.** Watrous §§2.1 and 5.2;
[exact proofs](../research/EXACT_PROOFS.md). **Intensity.** 2 rounds.

### M08 — Fine charge, coarse bins, and residues

**Question.** How do binning and conditioning divide charge uncertainty?

**Target.** Distinguish the random variables Q, floor(Q/g), bin parity, and Q mod g;
use entropy chain rules without confusing a bin with a residue class.

**Dependencies and role.** M02, M07; supply the classical variables used in the
two converse arguments. **Sources.** Watrous §5.1;
[worked examples](WORKED_EXAMPLES.md). **Intensity.** 2 rounds.

### M09 — Mixing and distinguishability

**Question.** When does a quantum mixture retain the entropy of its label?

**Target.** Explain entropy concavity, the entropy upper bound for mixing, and
the exact entropy decomposition when the mixture components have orthogonal
supports.

**Dependencies and role.** M07–M08; connect distinguishable pointer groups to an
entropy cost. **Sources.** Watrous §5.2;
[exact proofs](../research/EXACT_PROOFS.md). **Intensity.** 2 rounds.

### M10 — Shared random local phases

**Question.** How can a collective channel act nontrivially while remaining causal?

**Target.** Recognize exp(iθQ) as a product of local phase rotations and explain
why their shared random mixture cannot signal between laboratories.

**Dependencies and role.** M02, M05–M06; supply an attainable causal channel
family. **Sources.** [Apparatus](../research/APPARATUS.md);
[worked examples](WORKED_EXAMPLES.md). **Intensity.** 1–2 rounds.

### M11 — What a threshold calibration promises

**Question.** What does a gap of g charge units require, and what does it leave
unconstrained?

**Target.** Identify the low and high charge ranges, the intermediate sectors,
the active code, and the background capacity required to move a comparison
across the threshold.

**Dependencies and role.** M02–M05; turn the measurement task into precise
integer conditions. **Sources.** [Model](../research/MODEL.md);
[theorem](../research/THEOREM.md). **Intensity.** 2 rounds.

### M12 — Two different errors

**Question.** Why must wrong readout probability and retained-state disturbance
be controlled separately?

**Target.** Interpret calibration error η, survival loss ε, trace distance, and
pure-state overlap, and explain what each can and cannot certify.

**Dependencies and role.** M03, M06, M11; prepare the extension beyond exact
preservation. **Sources.** Watrous §§3.1–3.2;
[robustness](../research/ROBUSTNESS.md). **Intensity.** 2 rounds.

### M13 — Information in complementary descriptions

**Question.** How does retaining a charge label restrict information about its
conjugate phase?

**Target.** Interpret a Fourier family of coherent inputs, quantum side
information, and the role of the split-memory uncertainty inequality.

**Dependencies and role.** M06–M09, M12; connect imperfect preservation to an
entropy witness without an ambient Hilbert-space penalty. **Sources.** Watrous
§5.2 for entropy; [robustness](../research/ROBUSTNESS.md) supplies the bridge and
identifies the research-level uncertainty theorem. **Intensity.** 3 rounds.

### M14 — The complete physical task

**Question.** Which systems, records, assumptions, and entropy enter the claim?

**Target.** Reconstruct the model from preparation through local interactions to
classical collection; distinguish a causal retained-system channel from the
later availability of a global answer.

**Dependencies and role.** M01–M13; synthesize the background into one operational
description. **Sources.** [Model](../research/MODEL.md),
[worked examples](WORKED_EXAMPLES.md), [apparatus](../research/APPARATUS.md).
**Intensity.** 2–3 rounds.

## Phase II — Narrative and innovation

### M15 — Move a comparison to the threshold

**Question.** Why can a distant background expose differences inside a code whose
displayed answer is always low?

**Target.** Explain the shift b=a−q, its feasibility, and how the same active
coherence is compared before and after changing the background.

**Dependencies and role.** M04–M06, M11, M14; isolate the converse's physical
mechanism. **Sources.** [Exact proofs](../research/EXACT_PROOFS.md).
**Intensity.** 2 rounds.

### M16 — Causality forces separated pointers apart

**Question.** How do opposite calibrated outcomes constrain pointer overlap in
the original background?

**Target.** Derive the zero-overlap condition for charge separation at least g
from calibration and one-way causality, without assuming exact fine-charge
readout.

**Dependencies and role.** M06, M09, M15; convert the physical mechanism into the
converse's algebraic input. **Sources.** [Exact proofs](../research/EXACT_PROOFS.md).
**Intensity.** 2 rounds.

### M17 — The bin-parity entropy converse

**Question.** How can partial orthogonality force almost all coarse-charge entropy
into the environment?

**Target.** Group bins by parity, identify their mutually orthogonal supports,
and explain the at-most-one-bit cost of forgetting parity.

**Dependencies and role.** M08–M09, M16; obtain the arbitrary-prior lower bound.
**Sources.** [Theorem](../research/THEOREM.md),
[exact proofs](../research/EXACT_PROOFS.md). **Intensity.** 2–3 rounds.

### M18 — Translate a coherent window

**Question.** What pointer family preserves nearby coherences and separates
charges beyond the resolution gap?

**Target.** Construct a uniform length-g window, compute the triangular overlap
from intersecting supports, and interpret its effect on system coherences.

**Dependencies and role.** M06, M10, M16; supply the candidate attaining the
converse's scale. **Sources.** [Apparatus](../research/APPARATUS.md),
[worked examples](WORKED_EXAMPLES.md). **Intensity.** 2 rounds.

### M19 — Realize the window at separated sites

**Question.** How do shared entangled probes and local phase interactions realize
the collective window instrument?

**Target.** Follow the Fourier amplitudes, local probe readings, and finite
dimension condition; account for what must be prepared before the measurement.

**Dependencies and role.** M10, M14, M18; turn a channel construction into a
distributed apparatus. **Sources.** [Apparatus](../research/APPARATUS.md).
**Intensity.** 3 rounds.

### M20 — Fine records and the binary answer

**Question.** Why does grouping the meter's records into two outcomes leave more
than one bit of possible backaction?

**Target.** Distinguish the complete local transcript, its sum s, the binary
answer, and the unconditioned channel; explain why discarding s does not reverse
the physical interaction.

**Dependencies and role.** M03, M07, M19; connect attainability to the central
physical interpretation. **Sources.** [Apparatus](../research/APPARATUS.md),
[worked examples](WORKED_EXAMPLES.md). **Intensity.** 2 rounds.

### M21 — A uniform entropy upper bound

**Question.** What prevents the window apparatus from paying for every fine
position as an independent classical label?

**Target.** Explain position and Fourier dephasing, relative-entropy data
processing, and the role of the Fejér integral's finite constant.

**Dependencies and role.** M07–M09, M18; control the full von Neumann entropy,
including small eigenvalues. **Sources.** [Exact proofs](../research/EXACT_PROOFS.md).
**Intensity.** 3 rounds.

### M22 — Match necessity and attainability

**Question.** In what precise sense is coarse-charge entropy the optimal cost?

**Target.** Combine the converse and apparatus bound for each prescribed pure
input, identify the additive constants, and explain why one apparatus works for
all charge priors.

**Dependencies and role.** M17–M21; integrate the central theorem.
**Sources.** [Theorem](../research/THEOREM.md),
[proof map](../research/PROOF_MAP.md). **Intensity.** 2–3 rounds.

### M23 — The product-state consequence

**Question.** Why does an unentangled input already force a growing entropy cost?

**Target.** Relate the binomial charge spread to √m, use the residue-class lower
bound, and interpret log(1+√m/g) with its additive error.

**Dependencies and role.** M08, M22; expose the theorem's simplest many-spin
consequence. **Sources.** [Theorem](../research/THEOREM.md),
[worked examples](WORKED_EXAMPLES.md). **Intensity.** 2 rounds.

### M24 — Resolution wider than the fluctuations

**Question.** Why does a constant-error approximation alone fail to establish
vanishing backaction?

**Target.** Explain the common-core argument and charge-concentration binning;
distinguish a proven vanishing limit from an unproved sharp rate.

**Dependencies and role.** M18, M21, M23; resolve the broad-resolution endpoint
of the physical law. **Sources.** [Exact proofs](../research/EXACT_PROOFS.md).
**Intensity.** 2–3 rounds.

### M25 — Noisy threshold decoders

**Question.** How does causality remain useful when sector states are only
approximately preserved?

**Target.** Explain survival-conditioned pointers, Stinespring intertwiners, and
the readout-error bound for alternative threshold decoders.

**Dependencies and role.** M12, M15–M16, M22; replace exact scalar Kraus structure
with a robust information argument. **Sources.** [Robustness](../research/ROBUSTNESS.md).
**Intensity.** 3 rounds.

### M26 — From decoding to average output entropy

**Question.** Why do noisy comparisons and a Fourier preparation family give an
entropy lower bound?

**Target.** Describe serial information accounting and the complementary-memory
entropy transfer; keep the preparation phase label and the measured output
entropy distinct.

**Dependencies and role.** M08–M09, M13, M25; assemble the general robustness
proof without multiplying errors by the number of comparisons.
**Sources.** [Robustness](../research/ROBUSTNESS.md). **Intensity.** 3 rounds.

### M27 — Exact readout and approximate causality

**Question.** Which improvements follow from exact calibration, and which norm
supports an approximate-causality extension?

**Target.** Interpret the stronger exact-readout coefficient and explain why
diamond distance, including references, controls the dilation comparison.

**Dependencies and role.** M12–M13, M25–M26; understand the robust theorem's
assumption-sensitive boundaries. **Sources.** [Robustness](../research/ROBUSTNESS.md).
**Intensity.** 3 rounds.

### M28 — Sharp cases and counterexamples to overstatement

**Question.** What do sharp thresholds, sparse codes, neighboring bins, parity,
and mixed inputs teach about the theorem's scope?

**Target.** Identify exact equalities and explain why the result does not assert
a cost for every binary nonlocal measurement or every mixed charge prior.

**Dependencies and role.** M14, M22–M27; integrate the scientific limitations
through concrete examples. **Sources.** [Theorem](../research/THEOREM.md),
[worked examples](WORKED_EXAMPLES.md). **Intensity.** 2 rounds.

### M29 — Attribution and reproducible evidence

**Question.** Which ingredients are inherited, and what can the finite numerical
checks establish?

**Target.** Distinguish causal-measurement frameworks, known meter architectures
and fluctuation scales from the entropy converse and its matching bound; explain
why numerical agreement does not prove a universal theorem.

**Dependencies and role.** M19, M22–M28; connect the result to prior work and its
verification. **Sources.** [Attribution](../literature/ATTRIBUTION.md),
[verification](../VERIFICATION.md). **Intensity.** 2 rounds.

### M30 — Explain the whole result

**Question.** How would you explain the task, the unavoidable disturbance, the
attaining apparatus, and the strongest justified conclusion together?

**Target.** Give a coherent account from a pure product input and a certain
binary answer through causality, hidden pointer information, the entropy law,
and its robust and limiting regimes. State the assumptions without losing the
physical message.

**Dependencies and role.** M01–M29; final synthesis of the project, with no
additional unannounced assessment curriculum. **Sources.** [README](../README.md),
[theorem](../research/THEOREM.md), [proof map](../research/PROOF_MAP.md),
[attribution](../literature/ATTRIBUTION.md). **Intensity.** 2–3 rounds.

## Using the map

The [coaching protocol](COACHING.md) gives one challenge per milestone, starting
with two questions. All 30 passes complete this conceptual tutorial. The map
does not award passes, assess the author's current knowledge, or claim mastery
of every technical detail. A substantive change in the science can motivate a
documented map revision; a learner's incorrect answer cannot change its scope.
