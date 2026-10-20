# Causal Threshold Backaction

**How much entropy must a causal threshold measurement create, even when its binary answer is certain?**

A detector measures whether the total occupation of N separated spins is below
or above a threshold. It must preserve every state within each definite-charge
sector, and its nonselective retained-system channel must not let a background
block signal to an active block. Even when a pure input is certain to produce
the low answer, these requirements force the apparatus to distinguish enough
charge information to create entropy in the retained spins.

The detector is designed to learn about collective charge while preserving
quantum information within each fixed-charge sector for later use. The
[physical motivation](science/interpretation.md#why-this-detector-model) explains
this preservation requirement, the finite calibration gap, and why the
classical answer can be collected after the separated interactions.

The central result identifies the **optimal entropy cost with coarse-charge
entropy, up to universal additive constants**. A finite distributed apparatus
attains this accuracy for every charge distribution. For a pure product input,
the resulting scale is $`\log_2(1+\sqrt m/g)`$, where m is the number of active
spins and g is the threshold's charge gap.

## Read the science

Start with the [model and scope](science/model.md) and the
[exact entropy law](science/entropy_law.md). The causal converse and window
construction establish the two sides of the optimum; the fluctuation and
robustness arguments explain its limiting regimes and error assumptions.
The [physical interpretation](science/interpretation.md) connects these results.

| To understand | Read |
|---|---|
| How causality constrains charge coherence | [Causal converse](science/causal_converse.md) |
| Why one translated window nearly minimizes entropy | [Window entropy bound](science/window_entropy.md) |
| How separated sites implement the full instrument | [Distributed apparatus](science/distributed_apparatus.md) |
| The product-state law and the separate vanishing limit | [Fluctuation regimes](science/fluctuation_regimes.md) |
| General instruments, preparation phases, and approximate causality | [Robustness](science/robustness.md) |
| Exact proof dependencies and the physical meaning of the results | [Proof map](science/proof_map.md) and [interpretation](science/interpretation.md) |
| Established ingredients and close antecedents | [Related work](references/RELATED_WORK.md) and [bibliography](references/references.bib) |
| Finite checks and self-directed study | [Verification](verification/README.md), [Watrous bridge](learning/WATROUS_BRIDGE.md), and [30 milestones](learning/MILESTONES.md) |

## The task and its domain

Let $`Q=\sum_{j=1}^N|1\rangle\langle1|_j`$. Choose integers

```math
g\ge1,\qquad 0\le a,\qquad a+g\le N,\qquad
0\le m\le\min(a,N-a).
```

The detector returns low for every definite charge $`q\le a`$ and high for
$`q\ge a+g`$. The intervening g−1 sectors are unconstrained. Exact preservation
means preserving **every state inside every global charge sector**, including
internal coherences. Causality of the retained-system channel is needed in
only one direction, from the N−m background spins to the m active spins.
The [model](science/model.md) gives the full channel condition.

Prepare a pure state

```math
|\Psi\rangle=
\left(\sum_{q=0}^{m}\sqrt{p_q}\,|a_q\rangle_A\right)
\otimes|0\rangle_B^{\otimes(N-m)},
```

where $`|a_q\rangle`$ is any normalized active state of charge q. This entire
input family lies in the low region. The entropy cost is the von Neumann
entropy of the retained spins after ignoring the measurement record, measured
in bits. Because the input is pure, it is also their entropy increase.

## Coarse-charge entropy determines the optimum

For the classical charge distribution p, let
$`J=\lfloor Q_{\rm in}/g\rfloor`$. Let $`\mathsf D(p)`$ denote the infimum of the
output entropy over all instruments satisfying the stated exact assumptions,
at the fixed ambient parameters. Then

```math
\boxed{\quad
\max\{0,H(J)-1\}
\ \le\ \mathsf D(p)
\ \le\ H(J)+2.220.
\quad}
```

The [theorem](science/entropy_law.md) gives the sharper upper correction
$`\log_2(2-1/g)+C_g<2.219898`$, with
$`C_g=2(1+\ln g-\sum_{j=1}^{g}1/j)/\ln2`$. One and the same window apparatus
satisfies the upper bound for every p and every choice of the internal sector
states. At g=1 the cost is exactly H(Q) for this active-input family with vacuum
background spins. The correction near a bin boundary is
necessary: coarse-bin entropy is not an exact equality in general.

The converse follows from a physical comparison. Changing the background can
move two active charges separated by at least g onto opposite sides of the
calibrated threshold. Their meter states must become distinguishable.
Nonsignalling forces the same loss of active coherence in the original
background. Grouping these constraints by bin parity gives the entropy lower
bound. [Complete causal converse](science/causal_converse.md).

## Product states already exhibit the cost

For $`|+\rangle^{\otimes m}|0\rangle^{\otimes(N-m)}`$, the charge distribution
is $`\mathrm{Bin}(m,1/2)`$. Writing $`\mathsf B(m,g)`$ for the optimum at
the same feasible ambient parameters,

```math
\max\left\{0,\log_2\!\left(1+\frac{\sqrt m}{g}\right)-1\right\}
\le\mathsf B(m,g)
\le\log_2\!\left(1+\frac{\sqrt m}{g}\right)+2.267.
```

| Resolution regime | Consequence |
|---|---|
| $`g\ll\sqrt m`$ | The necessary cost grows as $`\log_2(\sqrt m/g)+O(1)`$. |
| $`g`$ comparable to $`\sqrt m`$ | The cost stays bounded. |
| $`g\gg\sqrt m`$ | A separate common-core estimate proves that the window entropy, and hence the optimum, tends to zero. |

The large-gap statement uses the [common-core and concentration proof](science/fluctuation_regimes.md);
the additive constants alone do not imply a vanishing limit.

![Binary threshold calibration and product-state entropy](assets/threshold_entropy.svg)

The green curve evaluates the explicit apparatus; the shaded interval gives
analytic bounds on the optimum. Panel B has m=a=64, N=192, and 1≤g≤128, so
every point obeys the theorem's domain. The caption and physical explanation
are in [worked examples](learning/WORKED_EXAMPLES.md).

## An exact distributed apparatus

Prepare entangled D-level probes in advance, with $`D\ge N+g`$. Each site
applies a local controlled phase and reads its probe in a Fourier basis.
Classical addition of the local records in their common future gives the
fine outcome $`s=q+Z`$, with Z uniform on 0,…,g−1. Group these outcomes into
low and high.

The [apparatus proof](science/distributed_apparatus.md) derives the complete Kraus
instrument, its conditional states, and the coherence kernel

```math
C_{qr}=\left(1-\frac{|q-r|}{g}\right)_+.
```

Its nonselective channel is a mixture of product phase rotations and is
nonsignalling across every cut. Local interactions and readouts need no
communication or feedforward. The global answer becomes available when the
classical records are combined. Its eventual one-bit format does not erase
the finer information responsible for the retained-system entropy.

## Robustness and scope

The [robust theorem](science/robustness.md) permits general instruments with
calibration error η and survival loss ε. It proves entropy lower bounds
averaged over a specified family of coherent preparation phases, without an
ambient $`2^N`$ continuity penalty. With exact readout and exact nonsignalling,
the uniform Fourier family on M equally weighted charges
$`0,g,\ldots,g(M-1)`$, with $`g(M-1)\le m`$, obeys

```math
\overline S_{\rm out}\ge(1-2\varepsilon)\log_2M-b_\varepsilon,
\qquad
b_\varepsilon=h_2(\varepsilon)
 -(1-\varepsilon)\log_2(1-\varepsilon).
```

Approximate causality is controlled in full diamond norm. The proof retains
the distinction between phase averages and individual phases, and between
calibration error and state disturbance. The exact arbitrary-prior theorem
is not asserted unchanged under errors.

The result depends on ordered threshold calibration, sector preservation,
and pure input. A parity measurement can have at most one bit of pure-input
output entropy, and a charge-diagonal mixed input need not acquire any new
entropy. The [examples](learning/WORKED_EXAMPLES.md) explain these boundaries.

Causal measurement frameworks, translated noisy meters, GHZ-like distributed
probes, and the square-root fluctuation scale have close established
antecedents. The contribution here is the universal entropy converse together
with a quantitatively matching instrument under the stated assumptions.
[Attribution and primary-source comparisons](references/RELATED_WORK.md).

## Learn the project

The single educational anchor is **John Watrous, *The Theory of Quantum
Information* (2018)**. The [Watrous bridge](learning/WATROUS_BRIDGE.md) selects
the relevant chapters, translates the notation, and explains the steps from
states and channels to the causal entropy bound. The
[worked examples](learning/WORKED_EXAMPLES.md) follow a four-spin experiment,
its records, and the boundaries of the theorem.

The [30-milestone map](learning/MILESTONES.md) gives a common route through the
whole project. Its **14 background/preliminaries milestones** assemble the
measurement model and information tools; its **16 narrative/innovation
milestones** connect the causal mechanism, attaining apparatus, robust bounds,
and physical interpretation. Each milestone identifies a question, an
understanding target, dependencies, a conceptual connection, and source pointers.

Use the bridge alongside the milestones for self-directed study.
The [LLM reading guide](llms.txt) maps scientific questions and reader intentions
to the authoritative files. Specialists can follow the direct science route above.

## Reproduce the finite checks

```sh
python -m pip install -r requirements.txt
python -m unittest discover -s tests -v
OPENBLAS_NUM_THREADS=1 OMP_NUM_THREADS=1 python tools/verify.py --output build/verification
python tools/check_repository.py
```

The checks evaluate finite matrices and exact instrument identities. The
universal results rest on the analytical proofs. Figure regeneration and
reference values are documented in [verification](verification/README.md).

## Purpose and contact

This repository serves as a record of the work and a guide for the author’s self-directed learning. For discussion or potential collaboration, please contact Ruge Lin at [gogoko699@gmail.com](mailto:gogoko699@gmail.com).

See [CONTRIBUTING](CONTRIBUTING.md) for scientific and implementation changes.
The owner's original [MIT license](LICENSE) is preserved. Linked third-party
papers and the textbook are not redistributed or relicensed here.
