# From Watrous to causal threshold backaction

A measurement of many separated spins may report only whether their total
occupation lies above a threshold. Suppose a pure input is certain to produce
the low answer. The retained spins can nevertheless acquire entropy, because
the apparatus must also behave correctly on other inputs while obeying
causality and preserving every definite-charge sector. The work explains why
these requirements force information about charge into the environment and how
an explicit distributed apparatus nearly minimizes that cost.

Start with the [30-milestone map](MILESTONES.md), then the
[worked examples](WORKED_EXAMPLES.md). The map has 14 background milestones and
16 narrative milestones, ordered by the scientific dependencies of the project.
Specialists can go directly to the
[theorem](../science/entropy_law.md) and [proof map](../science/proof_map.md).

## Route through the project

| Stage | Milestones | Scientific connection | Direct reading |
|---|---|---|---|
| States, instruments, and information | M01–M07 | Local quantum objects lead to sector preservation, pointer records, and system entropy. | [Model](../science/model.md) and [causal converse](../science/causal_converse.md) |
| Conditions and the complete task | M08–M14 | Charge uncertainty, calibration, causality, and errors define the operational claim. | [Model](../science/model.md) and [robust assumptions](../science/robustness.md) |
| Universal necessity | M15–M17 | Background shifts force separated pointers and a coarse-charge entropy cost. | [Causal converse](../science/causal_converse.md) |
| Attaining apparatus | M18–M22 | Finite windows and distributed readout supply a uniform upper bound matching the converse. | [Window entropy](../science/window_entropy.md), [apparatus](../science/distributed_apparatus.md), and [entropy law](../science/entropy_law.md) |
| Product inputs and wide resolution | M23–M24 | Binomial fluctuations give the product law; concentration controls the vanishing limit. | [Fluctuation regimes](../science/fluctuation_regimes.md) |
| Robust instruments | M25–M27 | Survival, noisy decoders, and phase averages extend the argument beyond exact preservation. | [Robustness](../science/robustness.md) |
| Scope and synthesis | M28–M30 | Boundaries, prior work, and verification connect the theorem to its physical interpretation. | [Interpretation](../science/interpretation.md), [related work](../references/RELATED_WORK.md), and [verification](../verification/README.md) |

## One educational anchor

**John Watrous, *The Theory of Quantum Information* (Cambridge University Press,
2018)** is the educational anchor for this repository.
[Author's book page](https://cs.uwaterloo.ca/~watrous/TQI/).

The relevant parts develop states, channels, measurements, state and channel
distances, and entropy in one consistent language. Use them as needed alongside
the milestones; reading the entire book is not a prerequisite. The author's
manuscript is linked rather than redistributed.

| Read selectively | What it supplies here | Project bridge |
|---|---|---|
| [Chapter 2](https://cs.uwaterloo.ca/~watrous/TQI/TQI.2.pdf), §§2.1–2.3 | States, registers, channels, representations, and measurements | M01–M07; [sector preservation and charge-dependent pointers](../science/causal_converse.md) |
| [Chapter 3](https://cs.uwaterloo.ca/~watrous/TQI/TQI.3.pdf), §§3.1–3.3 | Distinguishability, fidelity, and channel distance with auxiliary systems | M12 and M25–M27; [calibration, survival, and channel-error conventions](../science/robustness.md) |
| [Chapter 5](https://cs.uwaterloo.ca/~watrous/TQI/TQI.5.pdf), §§5.1–5.2 | Classical and quantum entropy and their inequalities | M08–M09 and M17–M27; [coarse-bin bounds](../science/causal_converse.md), [window entropy](../science/window_entropy.md), and [robust entropy transfer](../science/robustness.md) |

The locally supplied material explains threshold calibration, causal background
shifts, translated windows, and the final entropy law. Research-level imported
ingredients, including the split-memory uncertainty relation and Stinespring
continuity, are identified in the [robustness proof](../science/robustness.md)
and [attribution map](../references/RELATED_WORK.md). These citations support the
research ingredients; Watrous remains the single educational anchor.

## Notation bridge

| Object | Notation in this repository | Role |
|---|---|---|
| Quantum state | $`\rho`$, or $`\lvert\psi\rangle\langle\psi\rvert`$ for a pure state | Input or retained output of the measurement |
| Quantum channel | $`\mathcal E`$ | The instrument with its outcome ignored |
| Instrument | $`\{\mathcal I_{\rm low},\mathcal I_{\rm high}\}`$ | Both the answer probabilities and conditional state changes |
| Kraus operators | $`K_\alpha`$; $`K_s`$ for window outcomes | A representation of the physical state change |
| Stinespring isometry | $`V`$ | A pure-system description including an environment |
| Additive charge | $`Q=\sum_j n_j`$ | The observable being thresholded; also its classical distribution label when stated explicitly |
| Active block and background | $`A`$ and $`B`$ | The two sides of the causal condition |
| Charge-sector projector | $`\Pi_q`$ | All states of total occupation q, including degeneracy |
| Pointer state | $`\lvert e_q\rangle`$ | Environmental record associated with a preserved charge state |
| Classical and quantum entropy | $`H`$ and $`S`$ | Both measured in bits |
| Trace distance | $`\tfrac12\lVert\rho-\sigma\rVert_1`$ | Retained-state error; the factor one-half is explicit |
| Diamond norm | $`\lVert\Lambda-\Gamma\rVert_\diamond`$ | Full, unhalved channel difference including a reference |

Watrous writes the adjoint using a star in many places. This repository uses
a dagger. The density-operator, Kraus, and dilation descriptions are the same
objects under that change of notation.

## The bridge from textbook objects to the theorem

For a definite charge state, exact preservation makes each Kraus operator act
as a scalar. A dilation can therefore attach a pointer without changing that
state. On a pure superposition of charges it acts as

```math
\sum_q\sqrt{p_q}|a_q\rangle_A|0\rangle_B
\longmapsto
\sum_q\sqrt{p_q}|a_q\rangle_A|0\rangle_B|e_q\rangle_E.
```

Tracing out the meter multiplies a coherence between charges q and r by
their pointer overlap. Orthogonal pointers remove that coherence. Since the
joint output is pure, the retained spins and the meter have equal entropy:

```math
S_{\rm out}=S\!\left(\sum_qp_q|e_q\rangle\langle e_q|\right).
```

The causal comparison step changes the background charge while holding the active
input fixed. A pair separated by at least g can be shifted onto opposite sides
of the calibrated threshold. Their records must then be distinguishable.
The nonsignalling condition transfers that constraint to the original
background. This remains true when the actual input occupies only the low
region and its displayed answer is certain.

Grouping the resulting pointer constraints by charge bins gives the
[entropy converse](../science/causal_converse.md). The
[distributed apparatus](../science/distributed_apparatus.md) realizes translated
windows, and the [Fourier entropy argument](../science/window_entropy.md)
bounds their entropy uniformly. M15–M22 connect these steps to the
[matching entropy law](../science/entropy_law.md).

## A small example before the full proof

Take four spins, a two-spin active block, a=2, and g=2. The product input
$`|+\rangle^{\otimes2}|00\rangle`$ has charge probabilities
$`(1/4,1/2,1/4)`$ and always returns low. The window apparatus produces the
weighted Gram matrix

```math
G=\begin{pmatrix}
1/4&1/(4\sqrt2)&0\\
1/(4\sqrt2)&1/2&1/(4\sqrt2)\\
0&1/(4\sqrt2)&1/4
\end{pmatrix}.
```

Its nonzero eigenvalues are $`(3+\sqrt5)/8`$, $`1/4`$, and
$`(3-\sqrt5)/8`$. Their entropy exceeds one bit even though the displayed answer
has zero entropy. [WORKED_EXAMPLES](WORKED_EXAMPLES.md) follows the preparation,
coherences, and records in detail and connects them to the general bound.

## Proofs and calculations

For the complete assumptions and statements, follow the [model](../science/model.md),
[entropy law](../science/entropy_law.md), and [proof map](../science/proof_map.md).
The [worked examples](WORKED_EXAMPLES.md) connect these statements to explicit
states and records. [Verification](../verification/README.md) provides the
reproducible calculations and their limits. These routes use the same
assumptions and constants.
