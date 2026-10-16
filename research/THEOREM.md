# Exact entropy cost of a causal charge threshold

An exactly calibrated ordered threshold, combined with preservation of every charge-sector state and a nonsignalling nonselective channel, has an entropy cost determined by the input's coarse charge uncertainty. A single translated-window detector attains that cost within a universal additive constant.

The [model](MODEL.md) defines the instrument class, the direction of nonsignalling, and the entropy being minimized. [Complete proofs](EXACT_PROOFS.md) are provided separately.

## Universal theorem for an arbitrary pure input

Take integers

```math
g\ge1,\qquad 0\le a,\qquad a+g\le N,\qquad
0\le m\le\min(a,N-a).
```

Let

```math
|\Psi\rangle
  =\sum_{q=0}^{m}\sqrt{p_q}\,
    |a_q\rangle_A|0\rangle_B^{\otimes(N-m)}
```

be a pure input with normalized charge-$`q`$ vectors $`|a_q\rangle_A`$. Set

```math
J=\left\lfloor\frac{Q_{\mathrm{in}}}{g}\right\rfloor,
\qquad R=J\bmod2,
```

where $`Q_{\mathrm{in}}`$ has distribution $`p`$.

Define

```math
\mathcal H_g=\sum_{\ell=1}^{g}\frac1\ell,\qquad
C_g=\frac{2(1+\ln g-\mathcal H_g)}{\ln2},
\qquad
\delta_g=\log_2(2-1/g)+C_g.
```

Here $`\ln`$ is the natural logarithm. With $`\gamma`$ denoting Euler's constant,

```math
0\le C_g\le\frac{2(1-\gamma)}{\ln2}
  =1.2198977272\ldots,
\qquad
\delta_g\lt 2.2198977273.
```

For the exact admissible class in [MODEL.md](MODEL.md),

```math
\boxed{
\max\{0,H(J)-H(R)\}
\le
\mathsf D_{N,a,g,m}(\psi)
\le
S_{\mathrm{window}}(p)
\le
H(J)+\delta_g.
}
```

In particular,

```math
\boxed{
H(J)-1
\le
\mathsf D_{N,a,g,m}(\psi)
\le
H(J)+2.2198977273.
}
```

The window detector is the same apparatus for every input distribution and every set of within-sector vectors. It preserves all charge-sector states and is nonsignalling across all bipartitions. Its construction is given in [APPARATUS.md](APPARATUS.md).

The theorem also implies an input-independent approximation guarantee for that apparatus:

```math
0\le
S_{\mathrm{window}}(p)-\mathsf D_{N,a,g,m}(\psi)
\le H(R)+\delta_g
\lt 3.2198977273.
```

### Why coarse charge entropy appears

Nonsignalling lets the spectator charge move any comparison within the input range to the calibrated threshold. Exact calibration then forces

```math
\langle e_q|e_r\rangle=0
\quad\text{if }|q-r|\ge g,\qquad 0\le q,r\le m.
```

Bins of the same parity have orthogonal pointer supports. Their bin label must therefore be represented in the meter, up to the one-bit ambiguity of the parity class.

For the upper bound, each conditional mixture of translated windows within a bin has entropy at most $`\delta_g`$. Mixing the bins adds at most $`H(J)`$ bits. This argument imposes no smoothness, unimodality, or variance assumption on $`p`$.

### The sharp threshold

When $`g=1`$, distinct input charges have orthogonal pointers. The exact cost is

```math
\boxed{
\mathsf D_{N,a,1,m}(\psi)=H(Q_{\mathrm{in}}).
}
```

For the supported input family, the nonselective output loses every coherence between different charge sectors. It preserves the state within each sector.

### The one-bit lower correction is necessary

For $`g\ge2`$, choose $`N=2g`$, $`a=m=g`$, and the product input

```math
|1\rangle_A^{\otimes(g-1)}|+\rangle_A
  |0\rangle_B^{\otimes g}.
```

Its charges are $`g-1`$ and $`g`$ with equal probability, so $`H(J)=1`$. The window pointers overlap by $`1-1/g`$, giving

```math
S_{\mathrm{window}}
  =h_2\!\left(\frac1{2g}\right)\longrightarrow0.
```

Consequently, a uniform lower bound $`S_{\mathrm{out}}\ge H(J)-c`$ cannot hold with $`c<1`$. The ambiguity comes from a distribution straddling the chosen bin boundary.

## Spin-coherent product corollary

Consider

```math
|\Psi_m\rangle
  =|+\rangle_A^{\otimes m}|0\rangle_B^{\otimes(N-m)},
\qquad
|+\rangle=\frac{|0\rangle+|1\rangle}{\sqrt2}.
```

Its charge distribution is

```math
p_q=2^{-m}\binom mq.
```

For every feasible $`N,a,g,m`$,

```math
\boxed{
\log_2\!\left(1+\frac{\sqrt m}{g}\right)-1
\le
\mathsf D_{N,a,g,m}(+^{\otimes m})
\le
\log_2\!\left(1+\frac{\sqrt m}{g}\right)+C_*,
}
```

where

```math
C_*=
\frac12\log_2\frac{\pi e}{2}
+\frac{2(1-\gamma)}{\ln2}
=2.2669933124\ldots.
```

Thus $`2.267`$ bits is a safely rounded uniform upper margin. For $`m=0`$, the exact cost is zero.

A stronger lower bound, useful at finite $`m`$, is

```math
\mathsf D_{N,a,g,m}(+^{\otimes m})
\ge
\max\left\{
0,\,
H\!\left(\mathrm{Bin}(m,\tfrac12)\right)-\log_2g
\right\}.
```

The lower bound follows by conditioning on charge modulo $`g`$. The upper bound uses an exact Fourier entropy integral for the translated window and the variance of the binomial distribution. See [the product-corollary proof](EXACT_PROOFS.md#7-the-binomial-product-corollary).

The entire product input is in $`Q\le m\le a`$. Exact calibration therefore displays the low result with probability one. An ideal global Lüders measurement of the low-versus-high threshold would leave this input unchanged.

### Resolution regimes

When $`\sqrt m/g\to\infty`$, the cost grows as

```math
\log_2(\sqrt m/g)+O(1).
```

When $`g`$ is proportional to or larger than $`\sqrt m`$, the translated-window cost is bounded independently of $`m`$.

The stronger statement that the cost tends to zero for $`g/\sqrt m\to\infty`$ follows from the additional estimate below. It is not an inference from an additive-constant bound.

## Vanishing cost at broad resolution

The window apparatus also admits a variance-based estimate for any finite integer-valued charge distribution. Let

```math
\sigma^2=\mathrm{Var}(Q_{\mathrm{in}}),\qquad
C_0=1+\frac{2(1-\gamma)}{\ln2}.
```

For any integer $`1\le L\le\lfloor g/2\rfloor`$, put $`u=2\sigma/L`$ and define

```math
b(u)=(1+u)\log_2(1+u)-u\log_2u,\qquad b(0)=0.
```

Then

```math
\boxed{
S_{\mathrm{window}}(p)
\le
b(u)+u+h_2(L/g)+C_0 L/g.
}
```

This bound comes from two facts. Nearby translated windows have a large common pure component. A charge distribution with small variance also has little entropy in sufficiently wide, centered bins.

There is a uniform consequence that includes the integer-rounding cases. If $`\sigma=0`$, the output is pure. If

```math
0\lt r=\frac{\sigma}{g}\le\frac14,
```

then

```math
\boxed{
S_{\mathrm{window}}(p)
\le
b(4\sqrt r)+4\sqrt r
+h_2(\sqrt r)+C_0\sqrt r.
}
```

The right-hand side is $`O(\sqrt r\log(1/r))`$ as $`r\downarrow0`$. Hence

```math
\frac{\sigma}{g}\longrightarrow0
\quad\Longrightarrow\quad
S_{\mathrm{window}}(p)\longrightarrow0.
```

For the binomial product input, $`\sigma=\sqrt m/2`$. Thus its optimal admissible cost tends to zero when $`g/\sqrt m\to\infty`$. The displayed rate is an upper bound; no optimal vanishing rate is asserted.

The [common-core and centered-bin proof](EXACT_PROOFS.md#8-a-common-core-bound-for-nearby-windows) contains the exact integer conditions and the case where $`\sqrt{\sigma g}<1`$.

## Parity provides a useful comparison

Let

```math
P=(-1)^Q=\bigotimes_{j=1}^{N}Z_j.
```

The sharp even-versus-odd parity instrument has projectors $`(I+P)/2`$ and $`(I-P)/2`$. Its nonselective channel is

```math
\mathcal E_{\mathrm{parity}}(\rho)
  =\frac12\left(\rho+P\rho P\right).
```

It is a mixture of product unitaries, so it is nonsignalling across every cut. It preserves each charge-sector state. For a pure input, the output is a mixture of two pure states and has entropy at most one bit.

Parity asks whether the charge is even or odd; the theorem asks whether an ordered threshold has been crossed. The distinction in the readout function is essential to the growing entropy cost. A binary nonlocal measurement alone does not imply that cost.

## Scope and supporting material

The theorem assumes exact preservation, exact calibration, and exact nonsignalling. Approximate versions and their conventions are developed in [ROBUSTNESS.md](ROBUSTNESS.md).

The result is an additive characterization of the optimal entropy for pure inputs. It does not identify a multiplicative law in the regime where the entropy tends to zero. The [apparatus](APPARATUS.md), [complete proofs](EXACT_PROOFS.md), and [attribution](../literature/ATTRIBUTION.md) give the construction, derivations, and literature context.
