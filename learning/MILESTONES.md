# Thirty milestones for understanding causal threshold backaction

This map follows the scientific dependencies of the project. It contains
exactly **30 milestones**. M01–M14 build the background
from individual states and measurements to the complete causal task. M15–M30
assemble the mechanism, matching construction, robust bounds, and scientific
interpretation. The larger second phase reflects the several arguments needed
to connect the universal converse to a physically distributed instrument.

The map is an understanding route, not an inventory of every technical lemma.
Detailed derivations live in the [research documents](../science/proof_map.md).
The selected Watrous anchor, notation bridge, and overview of the two phases
are in [WATROUS_BRIDGE](WATROUS_BRIDGE.md). Each milestone connects a conceptual
question to its mathematical target, its role in the argument, and direct
scientific sources.

## Phase I — Background and preliminaries

### M01 — A state, an observable, and an outcome

**Question.** What distinguishes the quantum state of one spin from the classical
value obtained by measuring it?

**Target.** Relate a density operator, the occupation observable, and the Born
probabilities; distinguish a pure superposition from an incoherent mixture.

**Connection.** The theorem starts from a pure coherent input whose threshold answer is certain; its charge-diagonal mixture is a different initial state.

**Dependencies and role.** Starting point: identify the local objects from which
the many-spin task is built. **Sources.** Watrous Chapter 2, §§2.1 and 2.3;
[worked examples](WORKED_EXAMPLES.md).

### M02 — Total charge and its degenerate sectors

**Question.** What information does total occupation retain about a spin string?

**Target.** Explain why many basis strings share a charge and why preserving a
whole charge sector includes its internal superpositions.

**Connection.** The apparatus may learn total charge while retaining the relative amplitudes of basis strings within a sector.

**Dependencies and role.** M01; assemble local occupations into the model's
collective observable. **Sources.** [Model](../science/model.md);
[learning bridge](WATROUS_BRIDGE.md).

### M03 — A measurement specifies probabilities and state changes

**Question.** Why is a binary POVM insufficient to specify backaction?

**Target.** Distinguish an effect, an instrument branch, its normalized conditional
state, and the sum channel when the outcome is ignored.

**Connection.** Two detectors can have identical low/high probabilities and different retained-system channels, so calibration alone does not determine entropy.

**Dependencies and role.** M01–M02; identify the mathematical object to which the
theorem applies. **Sources.** Watrous §§2.2–2.3; [model](../science/model.md).

### M04 — Preservation within a sector

**Question.** How does preserving every state in a sector constrain its Kraus
operators?

**Target.** Explain the collinearity argument for a pure preserved state and why
linearity makes each Kraus operator scalar on an entire sector.

**Connection.** Scalar action in each sector reduces the exact disturbance problem to overlaps between charge-labelled environment states.

**Dependencies and role.** M02–M03; connect a physical nondisturbance assumption
to an algebraic constraint. **Sources.** Watrous §2.2;
[causal converse](../science/causal_converse.md).

### M05 — Retained subsystems and one-way causality

**Question.** What would let a change in the background signal to the active block?

**Target.** Use a partial trace to define the active output and explain the
full-channel condition that it depend only on the active input.

**Connection.** The same active coherence can be compared with different background charges because the active output must remain independent of that choice.

**Dependencies and role.** M03; move from one detector to spatially separated
laboratories. **Sources.** Watrous §§2.1–2.2; [model](../science/model.md).

### M06 — The environment remembers charge

**Question.** Where can a measurement place information while leaving a definite
charge state intact?

**Target.** Interpret a Stinespring dilation and charge-dependent pointer states;
relate pointer overlaps to loss of coherence in the retained system.

**Connection.** Pointers connect the apparatus's hidden charge information to attenuation of coherences between global sectors.

**Dependencies and role.** M03–M05; connect channel descriptions to the physical
mechanism. **Sources.** Watrous §2.2;
[worked examples](WORKED_EXAMPLES.md).

### M07 — Entropy from a pure joint state

**Question.** Why can a meter calculation determine the retained spins' entropy?

**Target.** Use equality of the nonzero spectra of two reductions of a pure state
and recognize the weighted Gram matrix as a smaller spectral calculation.

**Connection.** The supported charges supply the matrix needed for the exact entropy calculation, even when the full spin Hilbert space is much larger.

**Dependencies and role.** M06; identify the quantity that the proofs will bound.
**Sources.** Watrous §§2.1 and 5.2;
[pointer representation](../science/causal_converse.md).

### M08 — Fine charge, coarse bins, and residues

**Question.** How do binning and conditioning divide charge uncertainty?

**Target.** Distinguish the random variables Q, floor(Q/g), bin parity, and Q mod g;
use entropy chain rules without confusing a bin with a residue class.

**Connection.** Bins organize the arbitrary-prior law; residues isolate separated charges and yield the product-state lower bound.

**Dependencies and role.** M02, M07; supply the classical variables used in the
two converse arguments. **Sources.** Watrous §5.1;
[worked examples](WORKED_EXAMPLES.md).

### M09 — Mixing and distinguishability

**Question.** When does a quantum mixture retain the entropy of its label?

**Target.** Explain entropy concavity, the entropy upper bound for mixing, and
the exact entropy decomposition when the mixture components have orthogonal
supports.

**Connection.** Orthogonal supports supply the converse, while entropy bounds for mixing assemble the window upper bound.

**Dependencies and role.** M07–M08; connect distinguishable pointer groups to an
entropy cost. **Sources.** Watrous §5.2;
[causal converse](../science/causal_converse.md) and
[window entropy](../science/window_entropy.md).

### M10 — Shared random local phases

**Question.** How can a collective channel act nontrivially while remaining causal?

**Target.** Recognize exp(iθQ) as a product of local phase rotations and explain
why their shared random mixture cannot signal between laboratories.

**Connection.** A shared phase correlates local actions without transferring a signal; its random mixture realizes the window channel's nonselective disturbance.

**Dependencies and role.** M02, M05–M06; supply an attainable causal channel
family. **Sources.** [Apparatus](../science/distributed_apparatus.md);
[worked examples](WORKED_EXAMPLES.md).

### M11 — What a threshold calibration promises

**Question.** What does a gap of g charge units require, and what does it leave
unconstrained?

**Target.** Identify the low and high charge ranges, the intermediate sectors,
the active code, and the background capacity required to move a comparison
across the threshold.

**Connection.** The integer placement conditions guarantee both a certain low input and enough spectator charge for every comparison used in the converse.

**Dependencies and role.** M02–M05; turn the measurement task into precise
integer conditions. **Sources.** [Model](../science/model.md);
[theorem](../science/entropy_law.md).

### M12 — Two different errors

**Question.** Why must wrong readout probability and retained-state disturbance
be controlled separately?

**Target.** Interpret calibration error η, survival loss ε, trace distance, and
pure-state overlap, and explain what each can and cannot certify.

**Connection.** A reliable answer and a well-preserved baseline are separate requirements; the robust theorem tracks readout error and survival loss independently.

**Dependencies and role.** M03, M06, M11; prepare the extension beyond exact
preservation. **Sources.** Watrous §§3.1–3.2;
[robustness](../science/robustness.md).

### M13 — Information in complementary descriptions

**Question.** How does retaining a charge label restrict information about its
conjugate phase?

**Target.** Interpret a Fourier family of coherent inputs, quantum side
information, and the role of the split-memory uncertainty inequality.

**Connection.** Complementary information turns decodable charge labels into an average entropy cost for coherent phase preparations.

**Dependencies and role.** M06–M09, M12; connect imperfect preservation to an
entropy witness without an ambient Hilbert-space penalty. **Sources.** Watrous
§5.2 for entropy; [robustness](../science/robustness.md) supplies the bridge and
identifies the research-level uncertainty theorem.

### M14 — The complete physical task

**Question.** Which systems, records, assumptions, and entropy enter the claim?

**Target.** Reconstruct the model from preparation through local interactions to
classical collection; distinguish a causal retained-system channel from the
later availability of a global answer.

**Connection.** The early retained-system channel and the later collected classical answer play distinct operational roles in the same experiment.

**Dependencies and role.** M01–M13; synthesize the background into one operational
description. **Sources.** [Model](../science/model.md),
[worked examples](WORKED_EXAMPLES.md), [apparatus](../science/distributed_apparatus.md).

## Phase II — Narrative and innovation

### M15 — Move a comparison to the threshold

**Question.** Why can a distant background expose differences inside a code whose
displayed answer is always low?

**Target.** Explain the shift b=a−q, its feasibility, and how the same active
coherence is compared before and after changing the background.

**Connection.** An input deep in the low region is constrained by the detector's required behavior on physically available background-shifted inputs.

**Dependencies and role.** M04–M06, M11, M14; isolate the converse's physical
mechanism. **Sources.** [Causal converse](../science/causal_converse.md).

### M16 — Causality forces separated pointers apart

**Question.** How do opposite calibrated outcomes constrain pointer overlap in
the original background?

**Target.** Derive the zero-overlap condition for charge separation at least g
from calibration and one-way causality, without assuming exact fine-charge
readout.

**Connection.** Perfectly separated calibrated records force zero overlap for distant charges, even when their original binary answer agrees.

**Dependencies and role.** M06, M09, M15; convert the physical mechanism into the
converse's algebraic input. **Sources.** [Causal converse](../science/causal_converse.md).

### M17 — The bin-parity entropy converse

**Question.** How can partial orthogonality force almost all coarse-charge entropy
into the environment?

**Target.** Group bins by parity, identify their mutually orthogonal supports,
and explain the at-most-one-bit cost of forgetting parity.

**Connection.** Conditioning on bin parity reveals orthogonal supports, and removing that conditioning costs at most one bit in the lower bound.

**Dependencies and role.** M08–M09, M16; obtain the arbitrary-prior lower bound.
**Sources.** [Theorem](../science/entropy_law.md),
[causal converse](../science/causal_converse.md).

### M18 — Translate a coherent window

**Question.** What pointer family preserves nearby coherences and separates
charges beyond the resolution gap?

**Target.** Construct a uniform length-g window, compute the triangular overlap
from intersecting supports, and interpret its effect on system coherences.

**Connection.** Overlap of two finite windows controls nearby-charge coherence while enforcing the separation required by the converse.

**Dependencies and role.** M06, M10, M16; supply the candidate attaining the
converse's scale. **Sources.** [Apparatus](../science/distributed_apparatus.md),
[window entropy](../science/window_entropy.md),
[worked examples](WORKED_EXAMPLES.md).

### M19 — Realize the window at separated sites

**Question.** How do shared entangled probes and local phase interactions realize
the collective window instrument?

**Target.** Follow the Fourier amplitudes, local probe readings, and finite
dimension condition; account for what must be prepared before the measurement.

**Connection.** The shared probe realizes a global charge instrument using only local interactions before the classical records are combined.

**Dependencies and role.** M10, M14, M18; turn a channel construction into a
distributed apparatus. **Sources.** [Apparatus](../science/distributed_apparatus.md).

### M20 — Fine records and the binary answer

**Question.** Why does grouping the meter's records into two outcomes leave more
than one bit of possible backaction?

**Target.** Distinguish the complete local transcript, its sum s, the binary
answer, and the unconditioned channel; explain why discarding s does not reverse
the physical interaction.

**Connection.** Classical grouping changes which record is reported while retaining the same summed state-update channel.

**Dependencies and role.** M03, M07, M19; connect attainability to the central
physical interpretation. **Sources.** [Apparatus](../science/distributed_apparatus.md),
[worked examples](WORKED_EXAMPLES.md).

### M21 — A uniform entropy upper bound

**Question.** What prevents the window apparatus from paying for every fine
position as an independent classical label?

**Target.** Explain position and Fourier dephasing, relative-entropy data
processing, and the role of the Fejér integral's finite constant.

**Connection.** The Fourier entropy bound controls all eigenvalues of the pointer mixture and prevents an extra cost that grows with window length.

**Dependencies and role.** M07–M09, M18; control the full von Neumann entropy,
including small eigenvalues. **Sources.** [Window entropy](../science/window_entropy.md).

### M22 — Match necessity and attainability

**Question.** In what precise sense is coarse-charge entropy the optimal cost?

**Target.** Combine the converse and apparatus bound for each prescribed pure
input, identify the additive constants, and explain why one apparatus works for
all charge priors.

**Connection.** A lower bound for every admissible detector and an upper bound from one common detector locate each fixed input's optimum.

**Dependencies and role.** M17–M21; integrate the central theorem.
**Sources.** [Theorem](../science/entropy_law.md),
[proof map](../science/proof_map.md).

### M23 — The product-state consequence

**Question.** Why does an unentangled input already force a growing entropy cost?

**Target.** Relate the binomial charge spread to √m, use the residue-class lower
bound, and interpret log(1+√m/g) with its additive error.

**Connection.** Independent spins already provide a broad coherent charge prior; input entanglement is unnecessary for logarithmic growth when the gap is narrow.

**Dependencies and role.** M08, M22; expose the theorem's simplest many-spin
consequence. **Sources.** [Theorem](../science/entropy_law.md),
[fluctuation regimes](../science/fluctuation_regimes.md),
[worked examples](WORKED_EXAMPLES.md).

### M24 — Resolution wider than the fluctuations

**Question.** Why does a constant-error approximation alone fail to establish
vanishing backaction?

**Target.** Explain the common-core argument and charge-concentration binning;
distinguish a proven vanishing limit from an unproved sharp rate.

**Connection.** A common part of nearby windows retains coherence, allowing concentration of charge to prove a limit that the additive bound cannot resolve.

**Dependencies and role.** M18, M21, M23; resolve the broad-resolution endpoint
of the physical law. **Sources.** [Broad-resolution proof](../science/fluctuation_regimes.md).

### M25 — Noisy threshold decoders

**Question.** How does causality remain useful when sector states are only
approximately preserved?

**Target.** Explain survival-conditioned pointers, Stinespring intertwiners, and
the readout-error bound for alternative threshold decoders.

**Connection.** Causality transfers shifted threshold comparisons to one complementary output even without exact scalar Kraus operators.

**Dependencies and role.** M12, M15–M16, M22; replace exact scalar Kraus structure
with a robust information argument. **Sources.** [Robustness](../science/robustness.md).

### M26 — From decoding to average output entropy

**Question.** Why do noisy comparisons and a Fourier preparation family give an
entropy lower bound?

**Target.** Describe serial information accounting and the complementary-memory
entropy transfer; keep the preparation phase label and the measured output
entropy distinct.

**Connection.** Serial decoding accounts for charge information without accumulating one error per possible comparison; uncertainty then bounds the prepared outputs' entropy.

**Dependencies and role.** M08–M09, M13, M25; assemble the general robustness
proof without multiplying errors by the number of comparisons.
**Sources.** [Robustness](../science/robustness.md).

### M27 — Exact readout and approximate causality

**Question.** Which improvements follow from exact calibration, and which norm
supports an approximate-causality extension?

**Target.** Interpret the stronger exact-readout coefficient and explain why
diamond distance, including references, controls the dilation comparison.

**Connection.** Exact readout strengthens the entropy coefficient, while full diamond distance controls how small signalling changes the decoder.

**Dependencies and role.** M12–M13, M25–M26; understand the robust theorem's
assumption-sensitive boundaries. **Sources.** [Robustness](../science/robustness.md).

### M28 — Sharp cases and counterexamples to overstatement

**Question.** What do sharp thresholds, sparse codes, neighboring bins, parity,
and mixed inputs teach about the theorem's scope?

**Target.** Identify exact equalities and explain why the result does not assert
a cost for every binary nonlocal measurement or every mixed charge prior.

**Connection.** Parity, mixed inputs, and neighboring-bin priors explain the theorem's task, preparation, and additive-error qualifications.

**Dependencies and role.** M14, M22–M27; integrate the scientific limitations
through concrete examples. **Sources.** [Theorem](../science/entropy_law.md),
[interpretation](../science/interpretation.md),
[worked examples](WORKED_EXAMPLES.md).

### M29 — Attribution and reproducible evidence

**Question.** Which ingredients are inherited, and what can the finite numerical
checks establish?

**Target.** Distinguish causal-measurement frameworks, known meter architectures
and fluctuation scales from the entropy converse and its matching bound; explain
why numerical agreement does not prove a universal theorem.

**Connection.** The finite calculations check the explicit apparatus and identities; the universal claim depends on the proofs and their stated quantifiers.

**Dependencies and role.** M19, M22–M28; connect the result to prior work and its
verification. **Sources.** [Attribution](../references/RELATED_WORK.md),
[verification](../verification/README.md).

### M30 — Explain the whole result

**Question.** How would you explain the task, the unavoidable disturbance, the
attaining apparatus, and the strongest justified conclusion together?

**Target.** Give a coherent account from a pure product input and a certain
binary answer through causality, hidden pointer information, the entropy law,
and its robust and limiting regimes. State the assumptions without losing the
physical message.

**Connection.** The physical account joins a certain answer, unavoidable hidden charge information, an attainable entropy cost, and the stated robust and limiting regimes.

**Dependencies and role.** M01–M29; final synthesis of the project. **Sources.** [README](../README.md),
[theorem](../science/entropy_law.md), [proof map](../science/proof_map.md),
[interpretation](../science/interpretation.md),
[attribution](../references/RELATED_WORK.md).

## Using the map

Use the questions to locate a concept, the targets to identify its mathematical
content, and the dependencies to connect it to earlier milestones. Follow the
linked proof for a step's full assumptions and derivation. The sequence ends
with the physical synthesis in M30; the [proof map](../science/proof_map.md)
provides the corresponding route through the complete arguments.
