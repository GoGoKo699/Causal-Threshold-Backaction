# A learning route into causal threshold backaction

A measurement of many separated spins may report only whether their total
occupation lies above a threshold. Suppose a pure input is certain to produce
the low answer. The retained spins can nevertheless acquire entropy, because
the apparatus must also behave correctly on other inputs while obeying
causality and preserving every definite-charge sector. The work explains why
these requirements force information about charge into the environment and how
an explicit distributed apparatus nearly minimizes that cost.

Start with the [30-milestone map](MILESTONES.md), then the
[worked examples](WORKED_EXAMPLES.md). The map has 14 background milestones and
16 narrative milestones. It is fixed by the project, not by an assessment of a
particular learner. Specialists can go directly to the
[theorem](../research/THEOREM.md) and [proof map](../research/PROOF_MAP.md).

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
| [Chapter 2](https://cs.uwaterloo.ca/~watrous/TQI/TQI.2.pdf), §§2.1–2.3 | States, registers, channels, representations, and measurements | M01–M07; sector preservation and charge-dependent pointers |
| [Chapter 3](https://cs.uwaterloo.ca/~watrous/TQI/TQI.3.pdf), §§3.1–3.3 | Distinguishability, fidelity, and channel distance with auxiliary systems | M12 and M25–M27; calibration and preservation errors |
| [Chapter 5](https://cs.uwaterloo.ca/~watrous/TQI/TQI.5.pdf), §§5.1–5.2 | Classical and quantum entropy and their inequalities | M08–M09 and M17–M27; mixture bounds and entropy transfer |

The locally supplied material explains threshold calibration, causal background
shifts, translated windows, and the final entropy law. Research-level imported
ingredients, including the split-memory uncertainty relation and Stinespring
continuity, are identified in the [robustness proof](../research/ROBUSTNESS.md)
and [attribution map](../literature/ATTRIBUTION.md). These citations support the
research; they do not add educational anchors or turn the route into a reading
list.

## Notation bridge

| Object | Notation in this repository | Role |
|---|---|---|
| Quantum state | $`\rho`$, or $`|\psi\rangle\langle\psi|`$ for a pure state | Input or retained output of the measurement |
| Quantum channel | $`\mathcal E`$ | The instrument with its outcome ignored |
| Instrument | $`\{\mathcal I_{\rm low},\mathcal I_{\rm high}\}`$ | Both the answer probabilities and conditional state changes |
| Kraus operators | $`K_\alpha`$; $`K_s`$ for window outcomes | A representation of the physical state change |
| Stinespring isometry | $`V`$ | A pure-system description including an environment |
| Additive charge | $`Q=\sum_j n_j`$ | The observable being thresholded; also its classical distribution label when stated explicitly |
| Active block and background | $`A`$ and $`B`$ | The two sides of the causal condition |
| Charge-sector projector | $`\Pi_q`$ | All states of total occupation q, including degeneracy |
| Pointer state | $`|e_q\rangle`$ | Environmental record associated with a preserved charge state |
| Classical and quantum entropy | $`H`$ and $`S`$ | Both measured in bits |
| Trace distance | $`\tfrac12\|\rho-\sigma\|_1`$ | Retained-state error; the factor one-half is explicit |
| Diamond norm | $`\|\Lambda-\Gamma\|_\diamond`$ | Full, unhalved channel difference including a reference |

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

The new causal step changes the background charge while holding the active
input fixed. A pair separated by at least g can be shifted onto opposite sides
of the calibrated threshold. Their records must then be distinguishable.
The nonsignalling condition transfers that constraint to the original
background. This remains true when the actual input occupies only the low
region and its displayed answer is certain.

Grouping the resulting pointer constraints by charge bins gives the entropy
converse. Translated windows provide a matching construction, and the phase
measurement argument bounds its entropy uniformly. These steps are developed
in M15–M22 and proved in [EXACT_PROOFS](../research/EXACT_PROOFS.md).

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

## Continuing in chat

For an interactive tutorial, ask to begin at M01 or name the next uncompleted
milestone. The [coaching protocol](COACHING.md) specifies Revise → Learn → Test,
four-option selection questions, and the bounded retry rules. A maintenance
request does not launch this course or award any passes.

For a specialist reading session, follow [MODEL](../research/MODEL.md) →
[THEOREM](../research/THEOREM.md) → [PROOF_MAP](../research/PROOF_MAP.md).
For numerical inspection, use [VERIFICATION](../VERIFICATION.md). All three
routes use the same assumptions and constants.
