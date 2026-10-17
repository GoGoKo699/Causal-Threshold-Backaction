# Entropy of the translated-window instrument

A translated window retains only partially distinguishable charge records.
This page defines its causal channel and proves the uniform entropy upper
bound in the [exact entropy law](entropy_law.md). The [distributed apparatus](distributed_apparatus.md)
realizes the full instrument using local interactions and pre-shared probes.
The lower bound for all admissible instruments is in the [causal converse](causal_converse.md).

## 1. A causal instrument with translated-window pointers

Use meter positions $`w=0,\ldots,N+g-1`$ and define

```math
K_w=\frac1{\sqrt g}
\sum_{q=0}^{N}
\mathbf 1_{\{q\le w\le q+g-1\}}\Pi_q.
```

Each charge contributes to exactly $`g`$ positions, so $`\sum_wK_w^\dagger K_w=I`$. These Kraus operators are scalar on each charge sector and preserve every state in that sector.

Display the bit

```math
y(w)=\mathbf 1_{\{w\ge a+g\}}.
```

If $`q\le a`$, every possible position satisfies $`w\le a+g-1`$. If $`q\ge a+g`$, every possible position satisfies $`w\ge a+g`$. Calibration is exact.

The purified pointer is

```math
|e_q\rangle=\frac1{\sqrt g}\sum_{z=0}^{g-1}|q+z\rangle,
```

and the overlap is

```math
C_{qr}=\left(1-\frac{|q-r|}{g}\right)_+,
\qquad (x)_+=\max\{x,0\}.
```

Define the nonnegative Fejér kernel

```math
F_g(\theta)
=\frac1g\left|\sum_{z=0}^{g-1}e^{iz\theta}\right|^2
=\sum_{d=-(g-1)}^{g-1}
  \left(1-\frac{|d|}{g}\right)e^{id\theta}.
```

It integrates to one with respect to $`d\theta/(2\pi)`$. The nonselective channel is

```math
\mathcal E_{\mathrm{window}}(\rho)
=\int_0^{2\pi}
F_g(\theta)e^{i\theta Q}\rho e^{-i\theta Q}
\frac{d\theta}{2\pi}.
```

For every $`\theta`$,

```math
e^{i\theta Q}
=\bigotimes_{j=1}^{N}
\left(|0\rangle\langle0|_j
      +e^{i\theta}|1\rangle\langle1|_j\right).
```

This is a product unitary. Its local output depends only on the corresponding local input. Averaging with an input-independent probability measure preserves that property. The channel is therefore nonsignalling across every bipartition.

This verifies that the exact admissible class is nonempty. The [distributed apparatus](distributed_apparatus.md) derives the full instrument and its local implementation.

## 2. An exact Fourier entropy bound for the window mixture

This section applies to any finite integer-valued charge distribution. Let

```math
\tau=\sum_qp_q|e_q\rangle\langle e_q|,
\qquad
|e_q\rangle=\frac1{\sqrt g}\sum_{z=0}^{g-1}|q+z\rangle.
```

Let $`Z`$ be independent and uniform on $`\{0,\ldots,g-1\}`$. We will prove

```math
\boxed{
S(\tau)
\le H(Q_{\mathrm{in}}+Z)-\log_2g+C_g,
\qquad
C_g=\frac{2(1+\ln g-\mathcal H_g)}{\ln2}.
}
```

### 2.1 A finite-dimensional entropy inequality

After translating the support if necessary, embed the meter into a cyclic position space of any dimension $`D`$ large enough to contain it. For support $`q=0,\ldots,m`$, it suffices that $`D\ge m+g`$. The extra basis states are unoccupied and do not change $`S(\tau)`$.

Let $`\Delta_P`$ and $`\Delta_F`$ dephase in the position and discrete Fourier bases. Since these bases are mutually unbiased,

```math
\Delta_F\Delta_P(\tau)=I/D.
```

Relative-entropy data processing implies

```math
\begin{aligned}
H(P)-S(\tau)
&=D_{\mathrm{rel}}(\tau\Vert\Delta_P\tau)\\
&\ge
D_{\mathrm{rel}}(\Delta_F\tau\Vert I/D)\\
&=\log_2D-H(F).
\end{aligned}
```

Consequently,

```math
S(\tau)\le H(P)+H(F)-\log_2D.
```

The position distribution is that of $`Q_{\mathrm{in}}+Z`$. The Fourier probabilities do not depend on the translation $`q`$:

```math
P_{D,k}=\frac1D F_g(2\pi k/D).
```

It follows that

```math
H(F)-\log_2D
=-\frac1D\sum_{k=0}^{D-1}
F_g(2\pi k/D)\log_2F_g(2\pi k/D).
```

For fixed $`p,g`$, take $`D\to\infty`$. The function $`F_g\ln F_g`$ is continuous after defining its value to be zero at zeros of $`F_g`$. The Riemann sums therefore converge, giving

```math
S(\tau)
\le H(Q_{\mathrm{in}}+Z)
-\frac1{2\pi\ln2}
\int_0^{2\pi}F_g(\theta)\ln F_g(\theta)\,d\theta.
```

The argument uses finite-dimensional inequalities followed by a Riemann-sum limit. No uniform finite-$`D`$ estimate is needed.

### 2.2 Evaluation of the Fejér entropy integral

Write

```math
L(\theta)=\ln|1-e^{i\theta}|.
```

Its Fourier series is

```math
L(\theta)=-\sum_{n=1}^{\infty}\frac{\cos(n\theta)}n.
```

For a direct justification under integration, first replace it by $`\ln|1-r e^{i\theta}|`$ with $`0<r<1`$, integrate its absolutely convergent Fourier series, and then take $`r\uparrow1`$. The limit is valid against the bounded trigonometric polynomial $`F_g`$; the logarithmic singularities are integrable.

The Fourier support of $`F_g`$ is $`|n|<g`$. Thus

```math
\frac1{2\pi}\int_0^{2\pi}F_g(\theta)L(g\theta)\,d\theta=0,
```

because every nonconstant Fourier frequency of $`L(g\theta)`$ is a multiple of $`g`$. Also,

```math
\frac1{2\pi}\int_0^{2\pi}F_g(\theta)L(\theta)\,d\theta
=-\sum_{n=1}^{g-1}\frac{1-n/g}{n}.
```

Using

```math
\ln F_g(\theta)
=-\ln g+2L(g\theta)-2L(\theta),
```

with the removable cases interpreted by limits, we obtain

```math
\begin{aligned}
\frac1{2\pi}\int_0^{2\pi}F_g\ln F_g
&=-\ln g+
  2\sum_{n=1}^{g-1}\left(\frac1n-\frac1g\right)\\
&=2\mathcal H_g-2-\ln g.
\end{aligned}
```

Substitution proves the claimed entropy inequality. Since

```math
\gamma\le\mathcal H_g-\ln g\le1,
```

the constants obey

```math
0\le C_g\le\frac{2(1-\gamma)}{\ln2}.
```

The upper endpoint is the limit as $`g\to\infty`$. At $`g=1`$, $`C_g=0`$.

## 3. Completion of the universal upper bound

Partition the input charges into the bins of

```math
J=\left\lfloor Q_{\mathrm{in}}/g\right\rfloor.
```

The entropy-of-mixture inequality gives

```math
S(\tau)\le H(J)+\sum_jP(j)S(\tau_j),
```

where $`\tau_j`$ is the normalized conditional window mixture. This follows, for example, by writing the Holevo information of the bin ensemble and using $`I(J:E)\le H(J)`$.

Within one bin, the charge takes at most $`g`$ consecutive values. Adding $`Z`$ produces a position distribution supported on at most $`2g-1`$ integers. Section 2 therefore gives

```math
\begin{aligned}
S(\tau_j)
&\le H(Q_{\mathrm{in}}+Z\mid J=j)-\log_2g+C_g\\
&\le\log_2(2g-1)-\log_2g+C_g\\
&=\log_2(2-1/g)+C_g.
\end{aligned}
```

Thus

```math
S_{\mathrm{window}}(p)
\le H(J)+\log_2(2-1/g)+C_g.
```

Together with the [coarse-bin converse](causal_converse.md#3-lower-bounds-from-coarse-bins-and-residues) and admissibility of the window instrument, this proves the universal optimal-cost theorem.

The necessity of the one-bit lower correction follows from equal weights at charges $`g-1`$ and $`g`$. The two window pointers have overlap $`1-1/g`$, so their equal mixture has eigenvalues

```math
1-\frac1{2g},\qquad\frac1{2g}.
```

Its entropy tends to zero, whereas $`H(J)=1`$.

The [fluctuation analysis](fluctuation_regimes.md) now specializes these bounds
to product inputs and treats the broad-resolution limit. The latter requires
an additional common-core argument because the additive upper correction
does not itself tend to zero.
