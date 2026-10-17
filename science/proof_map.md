# Proof map

Read the [model](model.md) for the operational class and notation, then the
[entropy law](entropy_law.md) for the exact finite statements. The diagram organizes
logical dependencies; the table locates the complete arguments.

```mermaid
flowchart TD
  P["Sector preservation"] --> K["Scalar Kraus operators"]
  N["Calibration and causality"] --> O["Separated pointers"]
  K --> O
  O --> L["Entropy converse"]
  W["Translated windows"] --> A["Distributed instrument"]
  W --> U["Uniform entropy bound"]
  L --> T["Optimal coarse-charge law"]
  U --> T
  A --> T
  T --> C["Product-state consequence"]
```

## Exact theorem

| Argument | What it establishes | Full derivation |
|---|---|---|
| Pure-state preservation and linearity | Every Kraus operator is scalar on each global charge sector | [Causal converse §1](causal_converse.md#1-exact-sector-preservation-forces-scalar-kraus-operators) |
| Background charge shift | Active-input pointers at q,r in 0,…,m separated by at least g are orthogonal | [Causal converse §2](causal_converse.md#2-nonsignalling-and-calibration-force-pointer-orthogonality) |
| Bins grouped by parity | Output entropy is at least H(J)−H(J mod 2) | [Causal converse §3](causal_converse.md#3-lower-bounds-from-coarse-bins-and-residues) |
| Translated window overlap | An admissible kernel with exact gap-dependent coherence loss | [Window construction](window_entropy.md#1-a-causal-instrument-with-translated-window-pointers) |
| All-record Fourier calculation | The full fine and binary instruments follow from local probe readouts | [Distributed apparatus §3](distributed_apparatus.md#3-derivation-of-the-full-instrument) |
| Fourier dephasing and data processing | S(window mixture) ≤ H(Q+Z)−log₂g+Cg | [Window entropy §2.1](window_entropy.md#21-a-finite-dimensional-entropy-inequality) |
| Fejér integral | A dimension-independent, explicitly evaluated constant | [Window entropy §2.2](window_entropy.md#22-evaluation-of-the-fejér-entropy-integral) |
| Entropy of bin mixtures | The upper bound H(J)+log₂(2−1/g)+Cg | [Universal upper bound](window_entropy.md#3-completion-of-the-universal-upper-bound) |
| Residue classes and binomial entropy | The product-state lower bound H(Bin(m,1/2))−log₂g | [Fluctuation regimes §1.1](fluctuation_regimes.md#11-an-elementary-entropy-lower-bound) |
| Discrete variance entropy bound | The explicit product-state upper bound and uniform logarithmic envelope | [Fluctuation regimes §1.2](fluctuation_regimes.md#12-a-uniform-upper-bound-from-the-variance) |
| Common-core pinching and concentration | Vanishing window entropy when the gap dominates the charge fluctuations | [Common core](fluctuation_regimes.md#2-a-common-core-bound-for-nearby-windows) and [centered bins](fluctuation_regimes.md#3-centered-bins-and-a-uniform-vanishing-bound) |
| Parity as a mixture of two product unitaries | A different binary calibration can have at most one bit of pure-input entropy | [Parity comparison](interpretation.md#the-parity-comparison) |

The exact lower bound needs one direction of nonsignalling on one specified
cut. The construction obeys the stronger condition on every cut. Its existence
proves that the admissible class is nonempty and supplies the upper bound for
all priors with one apparatus.

## Robust theorem

All robust steps are in [Robustness](robustness.md). They start from selected
baseline-state survival, not from an approximate scalar-Kraus assertion.

| Argument | Role | Full derivation |
|---|---|---|
| Common Stinespring dilation of the active marginal | Moves a change of background into the complementary output | [Robustness §3](robustness.md#3-semicausality-gives-common-stinespring-intertwiners) |
| Survival-conditioned pointers and calibration | Provides alternative noisy threshold decoders on one encoded ensemble | [Robustness §4](robustness.md#4-a-threshold-decoder-for-the-normalized-pointers) |
| Serial information accounting | Converts decoder performance into pointer entropy | [Ordered encodings](robustness.md#5-ordered-quantum-encodings-with-an-arbitrary-prior) and [residue classes](robustness.md#6-pointer-entropy-from-residue-classes) |
| Fourier-family entropy transfer | Converts pointer entropy into average retained-system entropy without an ambient-dimension penalty | [Robustness §7](robustness.md#7-transferring-pointer-entropy-to-actual-output-entropy) |
| Exact-readout compression bound | Improves the coefficient when readout and nonsignalling are exact | [Robustness §9](robustness.md#9-stronger-theorem-for-exact-readout) |
| Continuity of Stinespring dilation | Extends decoder control to a full-diamond causality defect | [Robustness §10](robustness.md#10-approximate-causality-in-full-diamond-norm) |

The comparison decoders are alternative measurements used in an information
argument. The proof does not repeatedly interrogate one physical copy. The
Fourier family is a preparation ensemble whose index is retained; the lower
bound concerns the average of the individual output entropies.

## Evidence and attribution

[Verification](../verification/README.md) documents independent finite-matrix checks
and reproducible examples. They test the implementation and analytic formulas;
they are not a substitute for the quantifiers in the proofs.
[Related work](../references/RELATED_WORK.md) identifies the imported mathematical
tools and close physical precedents. The [learning route](../learning/WATROUS_BRIDGE.md)
provides a separate conceptual path into these same statements.
