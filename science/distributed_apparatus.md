# A finite distributed apparatus for the window instrument

This note gives an exact implementation of the complete instrument using an entangled probe prepared in advance, local system–probe interactions, local readouts, and subsequent classical communication. The global answer is available only after the records have reached a common future location. No quantum system needs to be reunited after the local interactions.

The distributed-meter architecture has established antecedents in [Beckman et al., Section II](https://arxiv.org/pdf/quant-ph/0102043) and [Vidil–Edamatsu, Section III](https://arxiv.org/pdf/2103.00443). The present construction adapts that architecture to a finite cyclic register and a bounded window of additive-charge outcomes. The [attribution note](../references/RELATED_WORK.md) separates these ingredients from the entropy necessity and attainability claims.

## 1. Target instrument and conventions

There are $`N\geq1`$ system qubits, with local number operators $`n_j=|1\rangle\langle1|_j`$ and total charge

```math
Q=\sum_{j=1}^N n_j=\sum_{q=0}^N q\Pi_q.
```

Choose an integer resolution $`g\geq1`$ and an integer probe dimension

```math
D\geq N+g,\qquad \omega=e^{2\pi i/D}.
```

All cyclic indices below are represented by $`0,\ldots,D-1`$. Define a normalized window on the cyclic register,

```math
w_z=
\begin{cases}
g^{-1/2},&0\leq z\leq g-1,\\
0,&g\leq z\leq D-1,
\end{cases}
\qquad
\sum_{z=0}^{D-1}|w_z|^2=1.
```

The desired fine-outcome Kraus operators are

```math
K_s=w_{(s-Q)\bmod D}
    =\sum_{q=0}^N w_{(s-q)\bmod D}\Pi_q,
\qquad
\mathcal I_s(\rho)=K_s\rho K_s^\dagger.
```

The notation $`w_{(s-Q)\bmod D}`$ denotes this spectral functional calculus. It is a scalar on each entire charge sector, including its degeneracy.

Since $`q+z\leq N+g-1<D`$, no physical outcome wraps around the register. The corresponding pointer states are exactly

```math
|e_q\rangle=\sum_{s=0}^{D-1}w_{(s-q)\bmod D}|s\rangle
           =\frac1{\sqrt g}\sum_{z=0}^{g-1}|q+z\rangle.
```

For a threshold with both promise regions present, take integers $`0\leq a\leq N-g`$. The calibration requirements are low for $`q\leq a`$ and high for $`q\geq a+g`$. The apparatus itself is defined for every $`g\geq1`$, independently of whether a chosen threshold has two nonempty promise regions.

## 2. Preparation and local measurement protocol

Use the positive Fourier-sign convention

```math
\alpha_k=\frac1{\sqrt D}\sum_{z=0}^{D-1}w_z\omega^{kz},
\qquad
w_z=\frac1{\sqrt D}\sum_{k=0}^{D-1}\alpha_k\omega^{-kz}.
```

Parseval's identity gives $`\sum_k|\alpha_k|^2=1`$. Prepare and distribute one $`D`$-level probe to each laboratory, in the joint state

```math
|A_w\rangle=\sum_{k=0}^{D-1}\alpha_k|k\rangle_1\cdots|k\rangle_N.
```

The coefficients can be complex. For the window,

```math
\alpha_k=\frac1{\sqrt{Dg}}\sum_{z=0}^{g-1}\omega^{kz},
\qquad
\alpha_0=\sqrt{\frac gD}.
```

Each laboratory performs the following two local operations.

1. Couple its system qubit to its probe through

   ```math
   U_j=\sum_{n=0}^1\sum_{k=0}^{D-1}
       \omega^{kn}|n\rangle\langle n|_j\otimes|k\rangle\langle k|_j.
   ```

2. Measure the probe in the positive-sign Fourier basis

   ```math
   |r_j\rangle_F=\frac1{\sqrt D}\sum_{k=0}^{D-1}
                       \omega^{kr_j}|k\rangle,
   \qquad r_j\in\{0,\ldots,D-1\}.
   ```

There is no feedforward between laboratories. At a later location where all classical records are available, calculate

```math
s=\left(\sum_{j=1}^N r_j\right)\bmod D.
```

The binary answer is low for $`s<a+g`$ and high for $`s\geq a+g`$.

## 3. Derivation of the full instrument

For an arbitrary system vector $`|\psi\rangle`$, the local couplings produce

```math
\left(\bigotimes_{j=1}^N U_j\right)
\bigl(|\psi\rangle\otimes|A_w\rangle\bigr)
=\sum_{k=0}^{D-1}\alpha_k\,\omega^{kQ}|\psi\rangle
                    \otimes|k\rangle^{\otimes N}.
```

The amplitude of a full record $`\mathbf r=(r_1,\ldots,r_N)`$ is therefore the system operator

```math
\begin{aligned}
M_{\mathbf r}
&=D^{-N/2}\sum_{k=0}^{D-1}
       \alpha_k\omega^{k(Q-\sum_jr_j)}\\
&=D^{-(N-1)/2}w_{(s-Q)\bmod D}\\
&=D^{-(N-1)/2}K_s.
\end{aligned}
```

The second equality is the inverse Fourier transform. It fixes all phases and normalization factors.

For each fixed $`s`$, there are exactly $`D^{N-1}`$ records: the first $`N-1`$ entries are arbitrary and the last is fixed by their sum. Grouping those records gives

```math
\sum_{\mathbf r:\,\sum_jr_j=s\ {\rm mod}\ D}
M_{\mathbf r}\rho M_{\mathbf r}^\dagger
=D^{N-1}D^{-(N-1)}K_s\rho K_s^\dagger
=\mathcal I_s(\rho).
```

Thus the equality holds for the complete instrument, including conditional system states. All formulas remain valid when the system is entangled with an untouched reference.

There is also a direct identification of the pointer dilation. The distributed pointer for charge $`q`$ is

```math
|\widetilde e_q\rangle=
\sum_{k=0}^{D-1}\alpha_k\omega^{kq}|k\rangle^{\otimes N}.
```

The fixed isometry on the span of the repeated basis vectors,

```math
J|k\rangle^{\otimes N}
=\frac1{\sqrt D}\sum_{s=0}^{D-1}\omega^{-ks}|s\rangle,
```

sends $`|\widetilde e_q\rangle`$ to $`|e_q\rangle`$. This is a mathematical identification of dilations. The physical protocol implements the readout through local measurements and classical addition, without applying $`J`$ as a joint operation.

## 4. Exact calibration and sector preservation

Normalization of the window implies

```math
\sum_sK_s^\dagger K_s
=\sum_{q=0}^N\left(\sum_s|w_{(s-q)\bmod D}|^2\right)\Pi_q=I.
```

If $`\rho=\Pi_q\rho\Pi_q`$, then

```math
\mathcal I_s(\rho)=|w_{(s-q)\bmod D}|^2\rho.
```

Consequently every state within a definite-charge sector is preserved exactly, nonselectively and in each outcome with nonzero probability. In particular, coherences inside degenerate sectors are preserved.

On such a state, the outcome distribution is $`s=q+Z`$, where $`Z`$ is uniform on $`0,\ldots,g-1`$. Hence

```math
\Pr({\rm high}\mid q)=
\begin{cases}
0,&q\leq a,\\
(q-a)/g,&a\lt q\lt a+g,\\
1,&q\geq a+g.
\end{cases}
```

Both promised calibration errors are zero. The intermediate charges are unconstrained by the promise and have the displayed linear transition. For $`g=1`$, the apparatus makes the exact decision high if and only if $`q>a`$.

The reported binary instrument is

```math
\begin{aligned}
\mathcal I_{\rm low}(\rho)
  &=\sum_{s=0}^{a+g-1}K_s\rho K_s^\dagger,\\
\mathcal I_{\rm high}(\rho)
  &=\sum_{s=a+g}^{D-1}K_s\rho K_s^\dagger.
\end{aligned}
```

These are classical coarse-grainings of the fine instrument. The sums are over completely positive maps, not over Kraus amplitudes. In general they differ from the binary Lüders instrument formed by taking the square roots of the two binary POVM effects. Forgetting a fine outcome does not erase its backaction.

## 5. Causality and the coherence kernel

Tracing out the probes immediately after the local couplings gives

```math
\mathcal E(\rho)=\sum_sK_s\rho K_s^\dagger
=\sum_{k=0}^{D-1}|\alpha_k|^2
       \omega^{kQ}\rho\omega^{-kQ}.
```

Since

```math
\omega^{kQ}=\bigotimes_{j=1}^N\omega^{kn_j},
```

this is a mixture of product unitaries with shared classical randomness. For any partition into systems $`A`$ and $`B`$, with corresponding charges $`Q_A`$ and $`Q_B`$,

```math
\mathrm{Tr}_B\,\mathcal E(\rho_{AB})
=\sum_k|\alpha_k|^2\omega^{kQ_A}
       \bigl(\mathrm{Tr}_B\,\rho_{AB}\bigr)\omega^{-kQ_A}.
```

The marginal depends only on the input marginal on $`A`$. The same argument works with reference systems, and with either side of every partition. The nonselective channel is exactly nonsignalling.

The local realization proves this property also when local records are retained as part of each laboratory's output. Shared randomness alone reproduces the nonselective system channel; the coherent preshared probe in the protocol supplies the full measurement instrument.

In charge blocks, the channel acts as

```math
\Pi_q\mathcal E(\rho)\Pi_r=C_{qr}\Pi_q\rho\Pi_r,
```

where the overlap of the two translated windows gives

```math
\begin{aligned}
C_{qr}
&=\langle e_r|e_q\rangle
 =\sum_s w_{s-q}w_{s-r}^*\\
&=\left(1-\frac{|q-r|}{g}\right)_+,
\qquad (x)_+=\max\{x,0\}.
\end{aligned}
```

The condition $`D\geq N+g`$ removes additional overlaps around the cyclic boundary.

## 6. Complete and partial classical transcripts

For every input,

```math
\Pr(\mathbf r)=D^{-(N-1)}\Pr(s).
```

Whenever $`\Pr(s)>0`$, the complete record conditioned on $`s`$ is uniform over its $`D^{N-1}`$ possibilities. Every such record gives the same normalized system state.

More formally, relabel the complete record by $`(s,t)`$, with $`t=(r_1,\ldots,r_{N-1})`$. This is a bijection. After that classical relabelling, the full classical–quantum output is

```math
\left(\sum_s|s\rangle\langle s|\otimes K_s\rho K_s^\dagger\right)
\otimes
\frac1{D^{N-1}}\sum_t|t\rangle\langle t|.
```

The extra record is independent randomness, not additional information about the input or extra system backaction.

For a proper subset $`J`$ of $`\ell<N`$ laboratories, fix arbitrary values of their records. For each $`s`$, there are $`D^{N-\ell-1}`$ completions. Therefore the conditional, unnormalized global-system map is

```math
\begin{aligned}
\sum_{\mathbf r:\,\mathbf r_J\ {\rm fixed}}
M_{\mathbf r}\rho M_{\mathbf r}^\dagger
&=D^{N-\ell-1}D^{-(N-1)}
  \sum_sK_s\rho K_s^\dagger\\
&=D^{-\ell}\mathcal E(\rho).
\end{aligned}
```

It follows that every proper subset of records is uniform and independent of both the input and the complete postmeasurement system. The global sum can contain information although every such proper subset does not.

## 7. Spacetime ordering and resource accounting

Prepare and distribute the probe before the system–probe couplings. The couplings and Fourier readouts may occur in mutually spacelike separated laboratories. Each laboratory sends only its classical record afterward. A collector computes the sum and the binary answer in their common causal future.

Conditioning on the globally reconstructed outcome describes the appropriate selective state after that information is available. It does not make the global outcome locally available during the interaction interval.

One convenient finite choice is

```math
t=\lceil\log_2(N+g)\rceil,\qquad D=2^t.
```

The apparatus then uses $`Nt`$ probe qubits. Each local phase coupling decomposes into $`t`$ controlled phase rotations between the system qubit and the bits of its probe register. A Fourier readout can use a $`t`$-qubit inverse Fourier transform and a computational-basis measurement. There is no quantum random-access memory.

The preshared state can be prepared before distribution by first preparing $`\sum_k\alpha_k|k\rangle`$ in one register, then copying its computational-basis label into $`N-1`$ initially zero registers by controlled additions. This entangles the registers; it does not copy an arbitrary unknown quantum state. The protocol assumes the required finite state preparation and local gates. No optimal preparation cost or noise tolerance is asserted here.

Across every nontrivial bipartition of the probes, the Schmidt probabilities are $`|\alpha_k|^2`$. Thus the initial entanglement entropy across that cut is

```math
H(\{|\alpha_k|^2\})\leq\log_2D=t.
```

The raw classical transcript contains $`Nt`$ bits; its redundancy at fixed $`s`$ is $`(N-1)t`$ bits. These resource counts are distinct from the output entropy used to quantify backaction on the system. The construction proves attainability of the target instrument, not optimality of its entanglement, communication, or hardware resources.

## 8. Checks that matter when reusing the construction

- Use the positive Fourier sign in both $`\alpha_k`$ and the measured Fourier kets. The bra then provides the negative sign in the record amplitude.
- Retain $`D\geq N+g`$ to avoid physical wraparound.
- Group the $`D^{N-1}`$ identical record Kraus operators before comparing with $`K_s`$.
- Form binary outcomes by summing the fine completely positive maps.
- Distinguish local completion of the interaction from later availability of the global classical answer.
- Keep the independent transcript randomness separate from the system entropy.

Bibliographic records are in [references.bib](../references/references.bib).
