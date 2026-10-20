# Model and scope

The question is how much entropy an ordered charge measurement must create when its nonselective channel cannot transmit a signal from a spectator block to an observed block. The displayed answer is one bit. The measurement must also preserve every state within a fixed charge sector.

The exact result concerns the entropy of a pure input after the outcome is ignored. Its scale is the Shannon entropy of the input charge grouped into bins of the detector's transition width. The [entropy law](entropy_law.md) gives dimension-independent additive bounds.

## Scientific reading route

This page fixes the common model and conventions. Read the [exact claims](entropy_law.md),
then the [causal converse](causal_converse.md) and [window entropy bound](window_entropy.md)
for necessity and attainability. The [distributed apparatus](distributed_apparatus.md)
derives the full instrument at separated sites. [Fluctuation regimes](fluctuation_regimes.md)
specializes the law to product inputs and proves the broad-resolution limit.
[Robustness](robustness.md) treats general imperfect instruments under its stated
operational assumptions. The [physical interpretation](interpretation.md) joins
these conclusions and explains the parity comparison. Its
[detector motivation](interpretation.md#why-this-detector-model) connects the
preservation requirement and the timing of readout to the intended measurement.

Use the [proof map](proof_map.md) for individual argument dependencies and the
[Watrous bridge](../learning/WATROUS_BRIDGE.md) for the conceptual route into them.

## System and charge

There are $`N`$ qubits with Hilbert space $`(\mathbb C^2)^{\otimes N}`$. Define

```math
n_j=|1\rangle\langle1|_j,\qquad
Q=\sum_{j=1}^{N}n_j=\sum_{q=0}^{N}q\,\Pi_q.
```

The projector $`\Pi_q`$ selects the total-charge sector $`q`$. A sector can have many dimensions. Preserving all states in that sector therefore includes preserving superpositions and entanglement within it.

An instrument has two displayed outcomes $`y\in\{0,1\}`$:

```math
\mathcal I_y(\rho)
  =\sum_{\alpha}K_{y,\alpha}\rho K_{y,\alpha}^{\dagger},
\qquad
\mathcal E=\mathcal I_0+\mathcal I_1.
```

Each $`\mathcal I_y`$ is completely positive, and the nonselective channel $`\mathcal E`$ is trace preserving. The label $`\alpha`$ includes information that is not displayed.

## Exact calibration and transition width

Choose integers $`a`$ and $`g`$ satisfying

```math
g\ge1,\qquad 0\le a,\qquad a+g\le N.
```

The instrument is exactly calibrated if, for every density operator supported in the specified sector,

```math
\begin{aligned}
\mathrm{Tr}\,\mathcal I_0(\rho)&=1
&&\text{when }\rho=\Pi_q\rho\Pi_q,\quad q\le a,\\
\mathrm{Tr}\,\mathcal I_1(\rho)&=1
&&\text{when }\rho=\Pi_q\rho\Pi_q,\quad q\ge a+g.
\end{aligned}
```

The $`g-1`$ integer sectors $`a+1,\ldots,a+g-1`$ have unconstrained readout probabilities. Thus $`g=1`$ is a sharp threshold, with no unconstrained sector.

Calibration applies uniformly to all states in a calibrated sector. A particular distribution of input charges is not part of this requirement.

## Exact preservation within charge sectors

The preservation assumption is

```math
\mathcal E(\rho)=\rho
\quad\text{for every density operator }\rho=\Pi_q\rho\Pi_q,
\quad q=0,\ldots,N.
```

This condition specifies the postmeasurement state after the outcome is ignored. Merely preserving the charge probabilities or the expectation of $`Q`$ would be weaker.

Exact preservation has a useful consequence:

```math
K_{y,\alpha}=f_{y,\alpha}(Q)
  =\sum_{q=0}^{N}f_{y,\alpha}(q)\Pi_q.
```

This scalar form is derived from the preservation assumption; it is not an additional restriction on the instrument. A pure state that is fixed by a channel must be mapped to a collinear vector by each Kraus operator. Linearity then makes that scalar the same throughout a sector. See [the scalar-Kraus proof](causal_converse.md#1-exact-sector-preservation-forces-scalar-kraus-operators).

## The cut and the nonsignalling condition

Partition the qubits into a block $`A`$ of $`m`$ spins and a spectator block $`B`$ of $`N-m`$ spins. The exact theorem uses

```math
0\le m\le\min(a,N-a).
```

Nonsignalling from $`B`$ to $`A`$ means that there is a channel $`\mathcal E_A`$ such that

```math
\mathrm{Tr}_{B_{\mathrm{out}}}\,\mathcal E(\rho_{AB})
  =\mathcal E_A\!\left(\mathrm{Tr}_{B}\,\rho_{AB}\right)
\quad\text{for every density operator }\rho_{AB}.
```

This is a condition on the nonselective channel. The displayed outcome can subsequently be collected and compared. The theorem does not require the conditional channel associated with a particular outcome to be nonsignalling.

Only this fixed direction across this fixed cut is needed for the lower bound. Requiring nonsignalling across all bipartitions is a sufficient stronger assumption. The [translated-window construction](distributed_apparatus.md) satisfies the stronger condition.

The restriction on $`m`$ has two concrete purposes:

- $`m\le a`$ puts the entire input family below threshold.
- $`m\le N-a`$ leaves enough spectator spins to shift a charge comparison to the calibrated threshold.

In the proof, a charge pair $`q<r`$ in $`A`$ is shifted by preparing $`B`$ with charge $`a-q`$. This charge is nonnegative and at most $`N-m`$. The shifted upper charge is $`a+r-q\le N`$.

## Inputs and the entropy cost

The input is pure, with the spectators in the vacuum:

```math
|\Psi\rangle
  =|\psi\rangle_A|0\rangle_B^{\otimes(N-m)},
\qquad
|\psi\rangle_A
  =\sum_{q=0}^{m}\sqrt{p_q}\,|a_q\rangle_A.
```

For every $`q`$ with $`p_q>0`$, the vector $`|a_q\rangle_A`$ is normalized and has charge $`q`$. Relative phases may be included in these vectors. Different charge sectors are orthogonal, so $`p`$ is a probability distribution. The state within $`A`$ may be entangled.

The entropy cost is

```math
S_{\mathrm{out}}(\mathcal I,\Psi)
  =S\!\left(\mathcal E(|\Psi\rangle\langle\Psi|)\right).
```

The input entropy is zero, so this is also its entropy increase. All von Neumann and Shannon entropies are measured in bits:

```math
S(\rho)=-\mathrm{Tr}\,\rho\log_2\rho,\qquad
H(p)=-\sum_qp_q\log_2p_q.
```

We use $`0\log_2 0=0`$. The binary entropy is $`h_2(t)=-t\log_2t-(1-t)\log_2(1-t)`$.

Let $`Q_{\mathrm{in}}`$ denote the classical random charge with probabilities $`p_q`$. Its coarse bin label is

```math
J=\left\lfloor\frac{Q_{\mathrm{in}}}{g}\right\rfloor.
```

The bins are $`\{jg,\ldots,(j+1)g-1\}`$, intersected with the input support. Their alignment is fixed at charge zero.

## Optimal cost and the purified meter

Let $`\mathfrak C_{N,a,g,m}`$ be the class of instruments satisfying the calibration, preservation, and fixed-cut nonsignalling conditions above. Define

```math
\mathsf D_{N,a,g,m}(\psi)
  =\inf_{\mathcal I\in\mathfrak C_{N,a,g,m}}
    S_{\mathrm{out}}(\mathcal I,\Psi).
```

The class is nonempty: the translated-window instrument is an explicit member. This quantity minimizes over detectors for a fixed input; there is no additional maximization over inputs.

A purified dilation can use meter vectors

```math
|e_q\rangle
  =\sum_{y,\alpha}f_{y,\alpha}(q)|y,\alpha\rangle,
\qquad
\langle e_q|e_q\rangle=1.
```

On the specified input, the joint output is

```math
\sum_q\sqrt{p_q}\,
  |a_q\rangle_A|0\rangle_B^{\otimes(N-m)}|e_q\rangle.
```

The reduced meter state is therefore

```math
\sigma_E=\sum_qp_q|e_q\rangle\langle e_q|,
\qquad
S_{\mathrm{out}}=S(\sigma_E).
```

For a fixed detector, this entropy depends only on the charge distribution $`p`$. It is independent of the vectors within the charge sectors and of their relative phases.

The equality uses a purification of all unobserved degrees of freedom of the instrument. It does not assert that a single charge eigenstate produces meter entropy: that input has a pure pointer vector.

## Scope of the results

The exact optimal-cost theorem concerns pure inputs and exact assumptions. A mixed input already diagonal in charge can have substantial charge entropy without the instrument creating that entropy. The pure-input statement should not be applied to that situation.

The universal bounds are additive in bits. Their binomial specialization determines the logarithmic cost when the charge spread exceeds the transition width. A separate estimate proves that the translated-window cost vanishes in the opposite limit; its rate is an upper bound, not a claimed optimal asymptotic equivalent.

For approximate calibration, preservation, or causality assumptions, see [robustness](robustness.md). Standard mathematical ingredients and the relationship to existing measurement results are recorded in [attribution and literature](../references/RELATED_WORK.md).
