# Causality forces a coarse-charge entropy cost

The lower bound in the [exact entropy law](entropy_law.md) follows from three
steps: preserving each charge sector fixes the Kraus structure, calibrated
background shifts force separated pointers to be orthogonal, and bin parity
turns that orthogonality into an entropy bound. The [model](model.md) specifies
the input family and the one-way nonsignalling condition used throughout.

All entropies and unqualified logarithms in entropy expressions use base two.
Natural logarithms are written $`\ln`$. Zero-probability terms have the convention
$`0\log_2 0=0`$. The standard information-theoretic ingredients are discussed in
[attribution and literature](../references/RELATED_WORK.md).

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

This lower bound applies to every instrument in the stated exact class.
The [window entropy bound](window_entropy.md) supplies a single admissible
instrument whose cost stays within a universal additive constant for all priors.
