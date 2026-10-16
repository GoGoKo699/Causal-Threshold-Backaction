# Proofs of the exact entropy bounds

This document proves the results in [THEOREM.md](THEOREM.md). The instrument class and its integer feasibility conditions are defined in [MODEL.md](MODEL.md).

All entropies and unqualified logarithms in entropy expressions use base two. Natural logarithms are written $`\ln`$. Zero-probability terms have the convention $`0\log_2 0=0`$. The standard information-theoretic ingredients are discussed in [attribution and literature](../literature/ATTRIBUTION.md).

## 1. Exact sector preservation forces scalar Kraus operators

Write the nonselective channel as

```math
\mathcal E(\rho)=\sum_{\alpha}K_\alpha\rho K_\alpha^\dagger,
```

where the index includes the displayed outcome and any hidden Kraus label.

Let $`|\phi\rangle`$ be a unit vector in one charge sector. Exact preservation gives

```math
\sum_\alpha
K_\alpha|\phi\rangle\langle\phi|K_\alpha^\dagger
=|\phi\rangle\langle\phi|.
```

For any vector orthogonal to $`|\phi\rangle`$, its expectation in the left-hand side is a sum of nonnegative squared amplitudes and is zero. Each Kraus image is therefore collinear with $`|\phi\rangle`$:

```math
K_\alpha|\phi\rangle=f_{\alpha,\phi}|\phi\rangle.
```

Apply this statement to two linearly independent vectors in the same sector and to their sum. Linearity forces their scalars to agree. Thus, throughout that sector, the Kraus operator is a scalar multiple of the identity. The statement also holds for a one-dimensional sector. Consequently,

```math
K_\alpha=f_\alpha(Q)
  =\sum_{q=0}^{N}f_\alpha(q)\Pi_q,
\qquad
\sum_\alpha|f_\alpha(q)|^2=1.
```

Define normalized meter vectors

```math
|e_q\rangle=\sum_\alpha f_\alpha(q)|\alpha\rangle.
```

The Stinespring isometry satisfies

```math
V|\phi_q\rangle=|\phi_q\rangle|e_q\rangle
```

for every vector in sector $`q`$. In particular, the nonselective channel multiplies a charge coherence by

```math
C_{qr}=\langle e_r|e_q\rangle,\qquad
\mathcal E(|\phi_q\rangle\langle\phi_r|)
  =C_{qr}|\phi_q\rangle\langle\phi_r|.
```

For a pure input $`\sum_q\sqrt{p_q}|a_q0_B\rangle`$, the joint output is pure and its meter marginal is

```math
\sigma_E=\sum_qp_q|e_q\rangle\langle e_q|.
```

The system and meter have the same nonzero Schmidt eigenvalues, so

```math
S_{\mathrm{out}}=S(\sigma_E).
```

Every Kraus operator commutes with $`e^{i\theta Q}`$. Thus

```math
\mathcal E(e^{i\theta Q}\rho e^{-i\theta Q})
  =e^{i\theta Q}\mathcal E(\rho)e^{-i\theta Q}.
```

The entropy is unchanged by a common charge phase. More generally, its expression through $`\sigma_E`$ shows that it depends only on $`p`$ for the supported pure input.

## 2. Nonsignalling and calibration force pointer orthogonality

Let $`A`$ contain $`m`$ spins and $`B`$ contain $`N-m`$ spins. Take normalized charge vectors $`|a_q\rangle_A`$ and $`|a_r\rangle_A`$, with $`0\le q,r\le m`$. For any spectator basis state $`|b\rangle_B`$ of charge $`b`$, the scalar-Kraus form gives

```math
\mathrm{Tr}_{B_{\mathrm{out}}}\,
\mathcal E\!\left(
|a_q\rangle\langle a_r|\otimes|b\rangle\langle b|
\right)
=C_{q+b,r+b}|a_q\rangle\langle a_r|.
```

Nonsignalling from $`B`$ to $`A`$ makes this reduced map independent of the spectator state. Comparing with the vacuum gives

```math
C_{q+b,r+b}=C_{qr},
\qquad
0\le q,r\le m,\quad 0\le b\le N-m.
```

The nonsignalling identity is stated for density operators, but extends to all operators by linearity; this justifies its use on a coherence.

Suppose $`q<r`$ and $`r-q\ge g`$. Choose

```math
b=a-q.
```

This is feasible because

```math
0\le a-q\le a\le N-m,
\qquad
a+r-q\le a+m\le N.
```

These are precisely the uses of $`m\le a`$ and $`m\le N-a`$.

The shifted charges are $`a`$ and $`a+r-q\ge a+g`$. Exact calibration puts their meter vectors in orthogonal outcome subspaces. Therefore

```math
C_{qr}=C_{a,a+r-q}=0.
```

We have proved

```math
\boxed{
\langle e_q|e_r\rangle=0
\quad\text{whenever }|q-r|\ge g,
\quad q,r\in\{0,\ldots,m\}.
}
```

The argument needs only the stated fixed-cut nonsignalling condition. It does not require a characterization of the channel at charge differences outside the supported input range.

## 3. Lower bounds from coarse bins and residues

Let $`Q_{\mathrm{in}}`$ have distribution $`p`$, and set

```math
J=\left\lfloor\frac{Q_{\mathrm{in}}}{g}\right\rfloor,
\qquad R=J\bmod2.
```

Let $`\sigma_j`$ be the normalized conditional meter mixture in bin $`j`$. If two bins have the same parity and different indices, their closest possible charges differ by at least $`g+1`$. Section 2 makes every pointer in one bin orthogonal to every pointer in the other. Their spans are therefore orthogonal.

For each parity with nonzero probability, the conditional meter is a direct sum:

```math
S(\sigma_{E|R=r})
  =H(J|R=r)
   +\sum_{j:\,j\bmod2=r}P(j|r)S(\sigma_j)
  \ge H(J|R=r).
```

Entropy concavity gives

```math
\begin{aligned}
S(\sigma_E)
&\ge\sum_rP(r)S(\sigma_{E|R=r})\\
&\ge H(J|R)\\
&=H(J)-H(R)\\
&\ge H(J)-1.
\end{aligned}
```

There is also a useful residue bound. Put $`T=Q_{\mathrm{in}}\bmod g`$. Distinct charges in a fixed residue class differ by at least $`g`$, so their pointer vectors are orthogonal. Hence

```math
\begin{aligned}
S(\sigma_E)
&\ge\sum_tP(t)S(\sigma_{E|T=t})\\
&=H(Q_{\mathrm{in}}|T)\\
&=H(Q_{\mathrm{in}})-H(T)\\
&\ge H(Q_{\mathrm{in}})-\log_2g.
\end{aligned}
```

All these bounds may be combined with nonnegativity of entropy. When $`g=1`$, the pointers for all distinct supported charges are orthogonal, giving the exact equality

```math
S_{\mathrm{out}}=H(Q_{\mathrm{in}}).
```

## 4. A causal instrument with translated-window pointers

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

This verifies that the exact admissible class is nonempty. Additional apparatus details are collected in [APPARATUS.md](APPARATUS.md).

## 5. An exact Fourier entropy bound for the window mixture

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

### 5.1 A finite-dimensional entropy inequality

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

### 5.2 Evaluation of the Fejér entropy integral

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

## 6. Completion of the universal upper bound

Partition the input charges into the bins of

```math
J=\left\lfloor Q_{\mathrm{in}}/g\right\rfloor.
```

The entropy-of-mixture inequality gives

```math
S(\tau)\le H(J)+\sum_jP(j)S(\tau_j),
```

where $`\tau_j`$ is the normalized conditional window mixture. This follows, for example, by writing the Holevo information of the bin ensemble and using $`I(J:E)\le H(J)`$.

Within one bin, the charge takes at most $`g`$ consecutive values. Adding $`Z`$ produces a position distribution supported on at most $`2g-1`$ integers. Section 5 therefore gives

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

Together with Section 3 and admissibility of the window instrument, this proves the universal optimal-cost theorem.

The necessity of the one-bit lower correction follows from equal weights at charges $`g-1`$ and $`g`$. The two window pointers have overlap $`1-1/g`$, so their equal mixture has eigenvalues

```math
1-\frac1{2g},\qquad\frac1{2g}.
```

Its entropy tends to zero, whereas $`H(J)=1`$.

## 7. The binomial product corollary

The product input on $`m`$ active spins expands as

```math
|+\rangle^{\otimes m}
=\sum_{q=0}^{m}
\sqrt{2^{-m}\binom mq}\,|D_q^{(m)}\rangle.
```

Hence $`Q_{\mathrm{in}}\sim\mathrm{Bin}(m,\tfrac12)`$. Section 3 gives

```math
S_{\mathrm{out}}
\ge
\max\{0,H(Q_{\mathrm{in}})-\log_2g\}.
```

### 7.1 An elementary entropy lower bound

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

### 7.2 A uniform upper bound from the variance

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

Combining this with Section 5 yields

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

## 8. A common-core bound for nearby windows

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

These are length-$`L`$ windows with shifts $`0,\ldots,L`$. Their position distribution has at most $`2L`$ values. Applying Section 5 with window length $`L`$ gives

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

## 9. Centered bins and a uniform vanishing bound

Let the finite integer-valued charge have mean $`\mu`$ and standard deviation $`\sigma`$. Define

```math
b(u)=(1+u)\log_2(1+u)-u\log_2u,\qquad b(0)=0.
```

### 9.1 Entropy of the centered bin label

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

### 9.2 Combining the centered bins with the common core

For fixed $`K`$, the possible charges lie in a half-open interval of width $`L`$. Their integer span is at most $`L`$. If

```math
1\le L\le\lfloor g/2\rfloor,
```

Section 8 and monotonicity of $`h_2(t)`$ on $`[0,1/2]`$ imply

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

### 9.3 Integer rounding and the limit of broad resolution

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

## 10. The parity comparison

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
