# Product fluctuations and the broad-resolution limit

For product inputs, the charge width is set by binomial fluctuations. The
[window entropy bound](window_entropy.md) and [causal converse](causal_converse.md)
give a uniform logarithmic law. A separate common-core argument proves
vanishing output entropy when the resolution is broader than the charge
fluctuations. The precise statements and feasibility conditions are in the
[entropy law](entropy_law.md) and [model](model.md).

## 1. The binomial product corollary

The product input on $`m`$ active spins expands as

```math
|+\rangle^{\otimes m}
=\sum_{q=0}^{m}
\sqrt{2^{-m}\binom mq}\,|D_q^{(m)}\rangle.
```

Hence $`Q_{\mathrm{in}}\sim\mathrm{Bin}(m,\tfrac12)`$. The [residue-class converse](causal_converse.md#3-lower-bounds-from-coarse-bins-and-residues) gives

```math
S_{\mathrm{out}}
\ge
\max\{0,H(Q_{\mathrm{in}})-\log_2g\}.
```

### 1.1 An elementary entropy lower bound

Shannon entropy is at least collision entropy:

```math
H(Q_{\mathrm{in}})
\ge-\log_2\sum_qp_q^2.
```

Vandermonde's identity gives

```math
\sum_qp_q^2=\frac{\binom{2m}{m}}{4^m}.
```

For completeness, put $`c_m=\binom{2m}{m}/4^m`$. Then

```math
c_0=1,\qquad
\frac{c_{m+1}}{c_m}=\frac{2m+1}{2m+2}.
```

Induction yields $`c_m\le(2m+1)^{-1/2}`$: the inductive step follows from

```math
\frac{\sqrt{2m+1}}{2m+2}
\le\frac1{\sqrt{2m+3}},
```

whose squared form is $`(2m+1)(2m+3)\le(2m+2)^2`$. In particular, for $`m\ge1`$,

```math
H(Q_{\mathrm{in}})\ge\frac12\log_2m.
```

Writing $`r=\sqrt m/g`$,

```math
\max\{0,H(Q_{\mathrm{in}})-\log_2g\}
\ge\max\{0,\log_2r\}
\ge\log_2(1+r)-1.
```

The last inequality is $`1+r\le2\max\{1,r\}`$. The case $`m=0`$ has zero cost directly.

### 1.2 A uniform upper bound from the variance

Let $`Y=Q_{\mathrm{in}}+Z`$ and add independent $`U\sim\mathrm{Unif}[-1/2,1/2]`$. The unit intervals associated with distinct integer values of $`Y`$ have disjoint interiors. Therefore

```math
h(Y+U)=H(Y).
```

For any finite-variance integer charge distribution with variance $`\sigma^2`$,

```math
\mathrm{Var}(Y+U)
=\sigma^2+\frac{g^2-1}{12}+\frac1{12}
=\sigma^2+\frac{g^2}{12}.
```

The Gaussian maximum-entropy bound gives

```math
H(Y)\le
\frac12\log_2\!\left[
2\pi e\left(\sigma^2+\frac{g^2}{12}\right)
\right].
```

Combining this with the [Fourier entropy bound](window_entropy.md#2-an-exact-fourier-entropy-bound-for-the-window-mixture) yields

```math
S_{\mathrm{window}}(p)
\le
\frac12\log_2\!\left[
2\pi e\left(\frac{\sigma^2}{g^2}+\frac1{12}\right)
\right]+C_g.
```

For the binomial distribution, $`\sigma^2=m/4`$. Since

```math
\frac{r^2}{4}+\frac1{12}
\le\frac{(1+r)^2}{4},
\qquad r=\frac{\sqrt m}{g},
```

we obtain

```math
S_{\mathrm{window}}
\le\log_2(1+r)
+\frac12\log_2\frac{\pi e}{2}
+\frac{2(1-\gamma)}{\ln2}.
```

The additive constant is $`2.2669933124\ldots`$ bits, and hence is less than $`2.267`$.

## 2. A common-core bound for nearby windows

Suppose a conditional charge distribution is supported in an integer interval of span $`L`$, with $`0\le L\le g`$. After translation, take its charges to be $`r=0,\ldots,L`$.

If $`L=0`$, every pointer is the same pure state and the entropy is zero. Assume first that $`0<L<g`$. The common intersection of all windows is

```math
\{L,\ldots,g-1\},
```

which has size $`g-L`$. Let $`|c\rangle`$ be the normalized constant vector on this core. Each pointer has the decomposition

```math
|e_r\rangle
=\sqrt{1-L/g}\,|c\rangle
 +\sqrt{L/g}\,|b_r\rangle,
```

where the normalized boundary vector is

```math
|b_r\rangle
=\frac1{\sqrt L}
\left(
\sum_{x=r}^{L-1}|x\rangle
+\sum_{x=g}^{g+r-1}|x\rangle
\right).
```

Empty sums are zero. The boundary and core are orthogonal. Pinching between their supports cannot decrease entropy, so

```math
S(\tau)
\le h_2(L/g)+\frac Lg S(\tau_{\mathrm{boundary}}).
```

Relabel the lower boundary positions $`0,\ldots,L-1`$ unchanged, and relabel $`g+s`$ as $`L+s`$. Under this unitary relabelling,

```math
|b_r\rangle
\longmapsto
\frac1{\sqrt L}\sum_{z=0}^{L-1}|r+z\rangle.
```

These are length-$`L`$ windows with shifts $`0,\ldots,L`$. Their position distribution has at most $`2L`$ values. Applying the [Fourier entropy bound](window_entropy.md#2-an-exact-fourier-entropy-bound-for-the-window-mixture) with window length $`L`$ gives

```math
S(\tau_{\mathrm{boundary}})
\le\log_2(2L)-\log_2L+C_L
=1+C_L
\le C_0,
```

where

```math
C_0=1+\frac{2(1-\gamma)}{\ln2}.
```

When $`L=g`$, the core has zero weight and the same boundary argument applies directly. We have proved, including both endpoints,

```math
\boxed{
S(\tau)\le h_2(L/g)+C_0 L/g.
}
```

The span counts the difference between the largest and smallest charge, so a span-$`L`$ interval may contain $`L+1`$ integer charges. This is why the boundary support bound here is $`2L`$, rather than $`2L-1`$.

## 3. Centered bins and a uniform vanishing bound

Let the finite integer-valued charge have mean $`\mu`$ and standard deviation $`\sigma`$. Define

```math
b(u)=(1+u)\log_2(1+u)-u\log_2u,\qquad b(0)=0.
```

### 3.1 Entropy of the centered bin label

For an integer width $`L\ge1`$, set

```math
K=\left\lfloor\frac{Q_{\mathrm{in}}-\mu}{L}+\frac12\right\rfloor.
```

This fixes a nearest-integer convention at ties. If $`K\ne0`$, then $`|Q_{\mathrm{in}}-\mu|/L\ge1/2`$, and consequently

```math
|K|\le2\,\frac{|Q_{\mathrm{in}}-\mu|}{L}.
```

The inequality also holds when $`K=0`$. By Cauchy--Schwarz,

```math
\mathbb E|K|\le\frac{2\sigma}{L}=u.
```

Let $`M_K=|K|`$. A nonnegative integer random variable of mean $`v`$ has entropy at most $`b(v)`$. To see this, compare its distribution with the geometric law

```math
G_v(k)=\frac1{1+v}\left(\frac v{1+v}\right)^k,
\qquad k=0,1,\ldots,
```

and use nonnegativity of classical relative entropy. The case $`v=0`$ is deterministic. Since $`b`$ is increasing,

```math
H(M_K)\le b(u).
```

The sign requires at most one bit when $`M_K>0`$ and no bit when $`M_K=0`$. Therefore

```math
H(K)
\le H(M_K)+P(M_K>0)
\le b(u)+u.
```

### 3.2 Combining the centered bins with the common core

For fixed $`K`$, the possible charges lie in a half-open interval of width $`L`$. Their integer span is at most $`L`$. If

```math
1\le L\le\lfloor g/2\rfloor,
```

Section 2 and monotonicity of $`h_2(t)`$ on $`[0,1/2]`$ imply

```math
S(\tau_{K=k})\le h_2(L/g)+C_0 L/g.
```

The entropy-of-mixture inequality now gives

```math
\boxed{
S_{\mathrm{window}}(p)
\le b(2\sigma/L)+2\sigma/L
+h_2(L/g)+C_0 L/g.
}
```

No ambient Hilbert-space dimension enters this estimate.

### 3.3 Integer rounding and the limit of broad resolution

First, a useful bound holds without choosing a window-bin width. At $`L=1`$,

```math
K=Q_{\mathrm{in}}+
  \left\lfloor\frac12-\mu\right\rfloor
```

is an integer translation of the charge itself. Hence

```math
H(Q_{\mathrm{in}})=H(K)\le b(2\sigma)+2\sigma.
```

Since the meter is a mixture of pure pointers, $`S_{\mathrm{window}}(p)\le H(Q_{\mathrm{in}})`$.

If $`\sigma=0`$, the charge and pointer are deterministic, and the entropy is zero. Otherwise set

```math
r=\frac{\sigma}{g},\qquad 0\lt r\le\frac14.
```

If $`\sigma g\ge1`$, choose

```math
L=\left\lfloor\sqrt{\sigma g}\right\rfloor.
```

This is at least one, and

```math
\frac12\sqrt{\sigma g}\le L
\le\sqrt{\sigma g}
=g\sqrt r
\le\frac g2.
```

Therefore $`2\sigma/L\le4\sqrt r`$ and $`L/g\le\sqrt r`$. Applying the preceding bound and monotonicity gives

```math
S_{\mathrm{window}}(p)
\le
b(4\sqrt r)+4\sqrt r
+h_2(\sqrt r)+C_0\sqrt r.
```

If $`\sigma g<1`$, then $`\sigma^2=r\,\sigma g<r`$. The charge-entropy bound instead gives

```math
S_{\mathrm{window}}(p)
\le b(2\sigma)+2\sigma
\le b(2\sqrt r)+2\sqrt r,
```

which is no larger than the previous displayed upper bound. Thus, in both cases,

```math
\boxed{
S_{\mathrm{window}}(p)
\le
b(4\sqrt r)+4\sqrt r
+h_2(\sqrt r)+C_0\sqrt r,
\qquad 0\lt r\le1/4.
}
```

As $`r\downarrow0`$, this is $`O(\sqrt r\log(1/r))`$. It proves that the window entropy vanishes whenever $`\sigma/g\to0`$, including sequences with bounded $`g`$ and shrinking variance.

For the binomial product input, $`\sigma=\sqrt m/2`$. Its optimal entropy cost is nonnegative and at most the window cost, so it also tends to zero when $`g/\sqrt m\to\infty`$.

These estimates distinguish a uniform additive entropy law from a separate
vanishing-cost limit. The [physical interpretation](interpretation.md) relates
them to the detector records, timing, and the parity comparison.
