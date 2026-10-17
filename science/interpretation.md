# What the entropy cost means physically

A detector can display a certain answer while changing the quantum state that
produced it. The result here makes that distinction quantitative for an ordered
charge threshold. Calibration, preservation within charge sectors, and
nonsignalling together constrain information left outside the retained spins.
The [entropy law](entropy_law.md) identifies its necessary size, and the
[distributed apparatus](distributed_apparatus.md) realizes the bound within a
constant number of bits.

## A certain answer is compatible with growing backaction

The [model](model.md) fixes a detector on all $`N`$ spins. It must answer low on
every charge sector $`q\le a`$ and high on every sector $`q\ge a+g`$, where
$`g\ge1`$ and $`0\le a<a+g\le N`$. Its input family is

```math
|\Psi\rangle
=\left(\sum_{q=0}^{m}\sqrt{p_q}\,|a_q\rangle_A\right)|0\rangle_B,
\qquad
0\le m\le\min(a,N-a).
```

Here $`|a_q\rangle_A`$ has charge $`q`$, and $`|0\rangle_B`$ is the spectator
vacuum. Every component lies in the low region. Exact calibration makes the
displayed answer low with probability one, including on their coherent
superposition. An ideal global Lüders threshold update would leave this input
unchanged. The causal converse constrains which state updates can accompany
that same correct answer. [Definitions and input domain](model.md).

Knowing the input prior does not allow the detector to ignore calibration on
other inputs. The optimum is an infimum over admissible detectors for each
prescribed pure input; every detector in that optimization must still satisfy
the global promises. Nor does the theorem require entanglement among the active
spins: the product state $`|+\rangle^{\otimes m}`$ already has coherent charge
fluctuations and exhibits the growing cost. [Exact statements](entropy_law.md).

## Why the spectator constrains a wholly-low input

For active charges $`q<r`$ separated by at least $`g`$, prepare the spectators
with charge $`a-q`$. The two total charges become $`a`$ and $`a+r-q`$, which
require opposite answers. The placement conditions above ensure that this
spectator preparation exists. Nonsignalling transports the constraint on the
active coherence back to the vacuum-spectator setting. Consequently the
purified meter vectors for those active charges must be orthogonal. The
[causal converse](causal_converse.md) proves this for $`0\le q,r\le m`$.

Preservation within sectors is essential to this argument. It protects every
state in each degenerate global charge sector, including internal coherences,
and forces the exact Kraus operators to be scalar functions of charge.
Conservation of charge probabilities alone is a weaker condition. The proof
does not silently extend to that weaker measurement class.
[Scalar-Kraus derivation](causal_converse.md).

At $`g=1`$, every pair of distinct charges in the supported input family is
separated. The output therefore loses all intercharge coherence in that family,
and its entropy is exactly $`H(Q_{\mathrm{in}})`$. This is an active-input
statement under the specified cut and placement conditions. States inside each
global charge sector remain preserved. For wider gaps, separated charges remain
distinguishable in the complement, while nearby charges can retain coherence.
[Sharp threshold and general bound](entropy_law.md).

## Resolution is measured against charge uncertainty

For an arbitrary prior, the useful comparison is the entropy of
$`J=\lfloor Q_{\mathrm{in}}/g\rfloor`$. The optimal cost follows $`H(J)`$ to
universal additive accuracy. This does not identify the physical output with a
projective measurement of those particular bins. A prior concentrated on two
adjacent charges across a bin boundary can have $`H(J)=1`$ while the window
detector causes arbitrarily little entropy as $`g`$ grows. The one-bit lower
correction accommodates precisely this boundary effect.
[Universal theorem and boundary example](entropy_law.md).

For the product input, the charge distribution is binomial, with standard
deviation $`\sqrt m/2`$. A gap small compared with that spread leaves many
distinguishable charge ranges, and the cost grows as
$`\log_2(\sqrt m/g)+O(1)`$. When the gap is comparable with the spread, the
window cost stays bounded. When $`g/\sqrt m\to\infty`$, its cost tends to
zero. That last conclusion has a separate common-core and concentration proof;
it cannot be obtained by dropping the additive constant from the general
entropy bound. All limits retain the model's feasibility conditions.
[Fluctuation regimes](fluctuation_regimes.md).

## The retained state, the records, and the interaction time

For a pure input, the nonselective output entropy equals the entropy of the
full Stinespring complement. The complement includes unobserved degrees of
freedom and any purification of an initially mixed apparatus. Its charge
dependence can therefore create system entropy even when the binary display
has zero entropy. This equality does not turn the entropy bound into a claim
about readable classical bits, dissipated heat, or required probe entanglement.
[Entropy definition](model.md).

The explicit instrument translates a coherent window by the charge. Local
couplings and Fourier readouts produce a fine record whose conditional
distribution is $`s=q+Z`$, with $`Z`$ uniform on $`0,\ldots,g-1`$. Classical
grouping turns that record into the binary answer. Grouping sums the fine
completely positive maps and leaves their nonselective channel unchanged;
coherently uncomputing an intermediate register can instead define a different
state update. The [apparatus derivation](distributed_apparatus.md) specifies
the full instrument, including conditional states.

The probes are prepared and distributed in advance. Each laboratory interacts
and measures locally; the global answer becomes available after classical
records reach a common future location. The theorem constrains the retained
channel at that local stage. Later outcome-dependent feedback or quantum
communication need not preserve its nonsignalling condition, even though those
later operations respect ordinary causal timing. The construction uses finite
registers with $`D\ge N+g`$ and needs no quantum reunion or QRAM. Its resource
accounting is an achievable implementation, without an optimality claim.
[Timing and resources](distributed_apparatus.md).

## The parity comparison

Define

```math
P=(-1)^Q=\bigotimes_{j=1}^{N}Z_j,
\qquad
P_{\pm}=\frac{I\pm P}{2}.
```

The projective parity instrument has nonselective channel

```math
P_+\rho P_+ + P_-\rho P_-
=\frac12(\rho+P\rho P).
```

Both terms are product-unitary channels, so their mixture is nonsignalling across all cuts. On sector $`q`$, $`P`$ is the scalar $`(-1)^q`$, and the channel fixes every state in that sector.

For a pure input $`|\phi\rangle`$, the output is

```math
\frac12|\phi\rangle\langle\phi|
+\frac12P|\phi\rangle\langle\phi|P.
```

Its rank is at most two and its entropy is at most one bit. The readout is the parity of the charge, so this example has a different calibration function from the ordered threshold.

The comparison isolates the role of the ordered threshold: a binary nonlocal readout and exact sector preservation can coexist with a uniformly bounded causal entropy cost.

## What survives under imperfect operation

The [robust theorem](robustness.md) allows general instruments and replaces
exact preservation by survival bounds on specified baseline states. It does
not assume approximately scalar Kraus operators. Its entropy conclusion is an
average over known pure preparation phases; the preparation label is retained.
A phase achieving the entropy bound may depend on the instrument. With both
nonzero survival loss and nonzero sectorwise calibration error, the proof does
not guarantee that this same phase has individual readout error below the
calibration parameter. Exact readout does guarantee low for every wholly-low
phase.

Small fixed errors retain logarithmic growth at fixed $`g`$ when the stated
coefficient is positive. The formulas do not assert a uniform noisy counterpart
of the entire exact crossover for growing $`g`$. The error parameters control
the specified global states and channels; a fixed error probability per local
component is not automatically such a bound. Approximate causality requires
the full, unhalved diamond norm with a reference. These qualifications are
part of the [robust statements](robustness.md), not assumptions supplied by
the finite numerical examples.

## How the pieces fit existing measurement theory

Causal restrictions on measurement, a fine meter behind a coarse answer,
translated noisy charge meters, entangled distributed probes, and the
square-root fluctuation scale all have established antecedents. The
[related-work comparison](../references/RELATED_WORK.md) credits these ideas
and the imported information inequalities. The contribution developed here is
the universal entropy necessity under the stated operational promises together
with an apparatus attaining that cost to additive accuracy, and the separately
qualified general-instrument bounds.

The physical question is therefore how global calibration constrains the
retained spins even when the eventual displayed answer is certain. The cost
depends on the input's coherent charge uncertainty and the detector's resolution. The
[worked examples](../learning/WORKED_EXAMPLES.md) show this mechanism on small
systems; the [proof map](proof_map.md) locates each step that turns it into the
entropy law.
