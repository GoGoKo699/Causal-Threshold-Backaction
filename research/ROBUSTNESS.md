# Robustness for general measurement instruments

This chapter proves entropy bounds for a general quantum instrument with imperfect nondisturbance and imperfect threshold calibration. The argument uses operational assumptions on the instrument. It does not require its Kraus operators to be functions of total charge, to commute with charge, or to have a common pointer throughout a degenerate charge sector.

The entropy conclusion concerns a finite ensemble of specified pure inputs with different preparation phases. Its mean output entropy is bounded below, so at least one phase attains the bound. At nonzero calibration error, the phase with large entropy is not automatically a phase with small readout error. Section 11 states the available readout guarantees precisely.

All logarithms and entropies are in bits. Natural logarithms appear only where explicitly written as $`\ln`$. We use

```math
h_2(t)=-t\log_2t-(1-t)\log_2(1-t),
\qquad
h_2(0)=h_2(1)=0,
```

and the half trace distance

```math
D(\rho,\sigma)=\frac12\|\rho-\sigma\|_1.
```

## 1. Operational assumptions

### System, threshold, and active block

The system consists of $`N`$ qubits, with total charge

```math
Q=\sum_{i=1}^{N}|1\rangle\langle1|_i.
```

Write $`\Pi_q`$ for the projector onto its charge-$`q`$ sector. Fix integers

```math
N\ge1,\qquad g\ge1,\qquad 0\le a,\qquad a+g\le N.
```

The displayed result is low below the lower endpoint $`a`$ and high above the upper endpoint $`a+g`$. The intermediate charges $`a<q<a+g`$ are unconstrained. This interval contains no integer charge when $`g=1`$.

Choose an active block $`A`$ of $`m`$ qubits and a complementary block $`B`$ of $`N-m`$ qubits, with

```math
0\le m\le\min(a,N-a).
```

For each $`q\in\{0,\ldots,m\}`$, choose a normalized charge-$`q`$ state $`|a_q\rangle_A`$ and define the baseline state

```math
|\chi_q\rangle
=
|a_q\rangle_A|0\rangle_B.
```

Here $`|0\rangle_B`$ is the all-zero state. Distinct $`|\chi_q\rangle`$ are orthogonal because they have different charges. For each $`b\in\{0,\ldots,N-m\}`$, also fix a normalized state $`|\beta_b\rangle_B`$ of charge $`b`$, with $`|\beta_0\rangle=|0\rangle_B`$.

The case $`m=0`$ is allowed. Its charge prior is a point mass, and the entropy lower bounds reduce to their nonnegative cap, zero.

### General instrument and sectorwise calibration

Let $`\{\mathcal I_0,\mathcal I_1\}`$ be an arbitrary binary quantum instrument on the system, where result $`0`$ means low and result $`1`$ means high. Its nonselective channel is

```math
\mathcal E=\mathcal I_0+\mathcal I_1.
```

Fix $`0\le\eta\le1/2`$. Calibration means that, for every density operator supported in an individual charge sector,

```math
\begin{aligned}
\mathrm{tr}\,\mathcal I_1(\rho)&\le\eta
&&\text{if }\rho=\Pi_q\rho\Pi_q,\quad q\le a,\\
\mathrm{tr}\,\mathcal I_0(\rho)&\le\eta
&&\text{if }\rho=\Pi_q\rho\Pi_q,\quad q\ge a+g.
\end{aligned}
```

This condition is uniform within each sector. At $`\eta>0`$, it is not a calibration condition for arbitrary coherent superpositions of different low-charge sectors. If that stronger condition is imposed separately, it supplies a stronger readout guarantee in Section 11.

### Selected baseline survival

Fix $`0\le\varepsilon<1`$. The proof only needs

```math
f_q
:=
\langle\chi_q|
\mathcal E(|\chi_q\rangle\langle\chi_q|)
|\chi_q\rangle
\ge1-\varepsilon
\qquad
(0\le q\le m).
```

The quantity $`f_q`$ is a survival probability, not a root fidelity.

The stronger operational assumption

```math
D(\mathcal E(\rho),\rho)\le\varepsilon
```

for every state $`\rho`$ supported in any individual total-charge sector implies these inequalities. Indeed, the two-outcome measurement containing $`|\chi_q\rangle\langle\chi_q|`$ distinguishes that input from its output with probability difference $`1-f_q`$, so $`1-f_q\le D`$.

Thus the theorem applies under uniform approximate sector preservation, while requiring preservation only on the selected baseline states. It imposes no preservation requirement on the shifted calibration inputs introduced below.

### One direction of nonsignalling

For the exact-causality results, assume that the reduced output on $`A`$ is independent of the input on $`B`$: there is a channel $`\mathcal T_A`$ such that

```math
\mathrm{tr}_{B_{\mathrm{out}}}\,\mathcal E
=
\mathcal T_A\circ\mathrm{tr}_{B_{\mathrm{in}}}.
```

This is equality of channels, including on inputs correlated with a reference system. Only this direction of nonsignalling across the chosen cut is used. A channel that is nonsignalling across every bipartition satisfies this assumption.

Section 10 replaces exact equality by a full diamond-norm bound.

## 2. Baseline pointers from a fixed instrument dilation

Choose one Stinespring isometry for the complete instrument,

```math
V:\mathcal H_A\otimes\mathcal H_B
\longrightarrow
\mathcal H_{A_{\mathrm{out}}}
\otimes\mathcal H_{B_{\mathrm{out}}}
\otimes\mathcal H_E,
```

such that

```math
\mathcal E(\rho)=\mathrm{tr}_E\,V\rho V^\dagger.
```

The environment can include an orthogonal record of the instrument outcome. Thus there are orthogonal projectors $`P_0,P_1`$ on $`E`$, summing to the identity, for which

```math
\mathrm{tr}\,\mathcal I_y(\rho)
=
\mathrm{tr}\!\left[
(I_{A_{\mathrm{out}}B_{\mathrm{out}}}\otimes P_y)
V\rho V^\dagger
\right].
```

For example, take a Kraus dilation that stores both the outcome and the Kraus index. An initially mixed apparatus can be included by purifying it into $`E`$. Any information statement about $`E`$ then concerns this full complementary system; it need not concern an accessible classical display.

For each baseline state, define the normalized pure pointer

```math
|e_q\rangle
=
\frac{
(\langle\chi_q|\otimes I_E)V|\chi_q\rangle
}{\sqrt{f_q}}.
```

This is well defined because $`f_q\ge1-\varepsilon>0`$. Its phase is fixed by this equation. There is a decomposition

```math
V|\chi_q\rangle
=
\sqrt{f_q}\,|\chi_q\rangle|e_q\rangle
+
\sqrt{1-f_q}\,|\xi_q\rangle,
\qquad
(\langle\chi_q|\otimes I_E)|\xi_q\rangle=0.
```

When $`f_q=1`$, the second term is absent. In particular,

```math
\langle\chi_q|\langle e_q|V|\chi_q\rangle
=
\sqrt{f_q},
\qquad
D\!\left(
V|\chi_q\rangle\langle\chi_q|V^\dagger,
|\chi_q\rangle\langle\chi_q|\otimes|e_q\rangle\langle e_q|
\right)
=
\sqrt{1-f_q}
\le\sqrt{\varepsilon}.
```

The actual complementary state for the baseline input is

```math
\rho_{E,q}
=
f_q|e_q\rangle\langle e_q|
+
(1-f_q)\tau_{E,q}.
```

The cross terms vanish after tracing out the system because of the displayed orthogonality condition. Consequently,

```math
\rho_{E,q}\ge(1-\varepsilon)|e_q\rangle\langle e_q|.
```

No assertion has been made that different vectors within the same degenerate charge sector share a pointer.

## 3. Semicausality gives common Stinespring intertwiners

Set

```math
\mathcal K=\mathcal H_{B_{\mathrm{out}}}\otimes\mathcal H_E,
\qquad
V_b|\varphi\rangle
=
V(|\varphi\rangle_A|\beta_b\rangle_B).
```

Each $`V_b`$ is an isometry from $`A`$ into $`A_{\mathrm{out}}\otimes\mathcal K`$. By nonsignalling,

```math
\mathrm{tr}_{\mathcal K}\,V_b\rho_A V_b^\dagger
=
\mathcal T_A(\rho_A)
```

for every $`b`$. They therefore dilate the same channel.

Stinespring uniqueness gives a unitary $`W_b`$ on the complementary space such that

```math
V_b=(I_{A_{\mathrm{out}}}\otimes W_b)V_0.
```

If necessary, append a fixed unused ancilla to the environment first. To see the unitary statement directly in finite dimension, express both dilations through one minimal dilation. The two environmental embeddings define an isometry between equal-dimensional support subspaces; extend that isometry to a unitary on the common padded space.

Crucially, $`W_b`$ is independent of the input vector in $`A`$. It is available for every superposition of the selected charge states, not only for one state at a time. This is the standard Stinespring structure behind semicausal operations; see [Eggeling, Schlingemann, and Werner](https://arxiv.org/abs/quant-ph/0104027).

### Charge shifts and their endpoints

Suppose a comparison divides the selected charges into a lower set with largest charge $`t`$ and an upper set whose smallest charge is at least $`t+g`$. Choose

```math
b=a-t.
```

Because $`0\le t\le m\le a`$ and $`m\le N-a`$,

```math
0\le b\le a\le N-m.
```

Every lower charge then obeys $`q+b\le a`$, and every upper charge obeys $`q+b\ge a+g`$. All shifted inputs are valid physical inputs: their total charges lie between zero and $`N`$, since $`q+b\le m+a\le N`$.

These inequalities hold for every comparison used below. There is no endpoint assumption hidden in the encoding argument.

## 4. A threshold decoder for the normalized pointers

Given the pointer $`|e_q\rangle`$, a decoder for the comparison in Section 3 performs the following quantum channel and measurement:

1. Append $`|0\rangle_{B_{\mathrm{out}}}`$.
2. Apply $`W_b`$ to $`B_{\mathrm{out}}E`$.
3. Measure the actual instrument outcome projectors $`P_0,P_1`$ on $`E`$.

The decoder uses no copy of the unknown state $`|a_q\rangle`$. That state can be included as an untouched mathematical spectator when comparing output probabilities.

For exact nonsignalling, the actual shifted output and the simulated output are

```math
|v_{q,b}\rangle=V_b|a_q\rangle,
\qquad
|w_{q,b}\rangle
=
|a_q\rangle
W_b(|0\rangle_B|e_q\rangle),
```

and their overlap is exactly

```math
\langle w_{q,b}|v_{q,b}\rangle=\sqrt{f_q}.
```

The actual output has the correct threshold result with error at most $`\eta`$. The simulated output is at pure-state angle at most $`\arcsin\sqrt{\varepsilon}`$ from it.

For a projective binary measurement, if one pure state has wrong-outcome probability at most $`\eta`$ and another lies at angle at most $`\theta`$, the latter has wrong-outcome probability at most

```math
\sin^2\!\left(
\min\left\{\frac{\pi}{2},\arcsin\sqrt{\eta}+\theta\right\}
\right).
```

One proof decomposes both vectors into the correct and incorrect outcome subspaces. If their incorrect probabilities are $`u`$ and $`v`$, Cauchy–Schwarz bounds the overlap by $`\sqrt{uv}+\sqrt{(1-u)(1-v)}`$. Writing these probabilities as squared sines gives the angle inequality.

For entropy decoding, a fair independent guess is always available. Define the capped error

```math
\zeta
=
\sin^2\!\left(
\min\left\{
\frac{\pi}{4},
\arcsin\sqrt{\eta}+\arcsin\sqrt{\varepsilon}
\right\}
\right).
```

There is therefore a comparison decoder with error at most $`\zeta\le1/2`$ for every individual encoded charge. In the informative regime,

```math
\arcsin\sqrt{\eta}+\arcsin\sqrt{\varepsilon}<\frac{\pi}{4},
```

this becomes

```math
\zeta
=
\left(
\sqrt{\eta(1-\varepsilon)}
+
\sqrt{\varepsilon(1-\eta)}
\right)^2.
```

Outside that regime, the decoder used in the entropy proof is the independent fair guess. The cap is a statement about a chosen decoder; it does not claim that the instrument's actual displayed result has error at most one half on every superposition.

The simpler estimate $`\eta+\sqrt{\varepsilon}`$ follows from trace-distance contractivity and is also valid before capping. The angular expression gives the sharper exact-causality parameter.

## 5. Ordered quantum encodings with an arbitrary prior

This section proves the arbitrary-prior step explicitly. An ordered alphabet is important: its binary questions must be comparisons that the threshold decoder can implement.

### Tree entropy lemma

Let an ordered finite alphabet $`x`$ have prior $`p_x`$, and let $`\rho_x`$ be its quantum encoding. Suppose every comparison required by an alphabetic binary tree has a decoder whose error is at most $`\zeta\le1/2`$ for every symbol reaching that comparison. Let $`L`$ be the tree's mean leaf depth under $`p`$.

Then its Holevo information satisfies

```math
\chi(\{p_x,\rho_x\})
\ge
H(p)-h_2(\zeta)L.
```

**Proof.** At an internal node $`v`$, condition on the event that the symbol belongs to that node. Write $`B_v`$ for its left/right branch bit. The comparison decoder has conditional average error at most $`\zeta`$. Binary Fano and data processing therefore give

```math
I(B_v:E\mid v)
\ge
H(B_v\mid v)-h_2(\zeta).
```

The cq chain rule at the root is

```math
I(X:E)
=
I(B_{\mathrm{root}}:E)
+
\sum_{b=0}^{1}p_b I(X:E\mid B_{\mathrm{root}}=b).
```

Apply this identity recursively down the finite tree. With $`p_v`$ the probability of reaching node $`v`$,

```math
I(X:E)
=
\sum_{v\ \mathrm{internal}}p_v I(B_v:E\mid v).
```

The corresponding classical chain rule and the definition of mean depth give

```math
\sum_vp_v H(B_v\mid v)=H(p),
\qquad
\sum_vp_v=L.
```

Combining these equations proves the claim. The different comparisons are alternative measurements on the encoding. The proof does not require that they be performed successively without disturbing one copy. This is the entropy method used in random-access and serial-encoding lower bounds; see [Nayak](https://arxiv.org/abs/quant-ph/9904093).

### An alphabetic tree of mean depth less than entropy plus two

Remove zero-probability symbols and list the remaining probabilities in their prescribed order. Define

```math
F_x=\sum_{y<x}p_y,
\qquad
u_x=F_x+\frac{p_x}{2},
\qquad
\ell_x=\left\lceil\log_2\frac1{p_x}\right\rceil+1.
```

Use the first $`\ell_x`$ binary digits of $`u_x`$ as a codeword, choosing the terminating binary expansion at dyadic points. Its half-open dyadic interval has length $`2^{-\ell_x}\le p_x/2`$ and contains $`u_x`$. It lies within $`[F_x,F_x+p_x]`$: either endpoint is at distance at most $`2^{-\ell_x}`$ from the midpoint.

The code intervals are disjoint and occur in the specified order. They therefore form an alphabetic prefix code. Its binary trie has the symbols in that order, and every branch separates consecutive groups of symbols. Pruning any unary vertices produces an alphabetic binary tree with no larger depths. Its mean depth obeys

```math
L\le\sum_xp_x\ell_x<H(p)+2.
```

For a one-symbol alphabet, take the empty tree with $`L=0`$.

Combining this construction with the tree lemma gives

```math
\chi(\{p_x,\rho_x\})
\ge
(1-h_2(\zeta))H(p)-2h_2(\zeta).
```

The nonnegative lower bound zero may always replace a negative right-hand side. In particular, the argument does not assume uniform input symbols, balanced comparisons, or independently distributed binary digits.

## 6. Pointer entropy from residue classes

Let $`p_q`$ be any charge prior on $`\{0,\ldots,m\}`$, and define

```math
\sigma_E
=
\sum_{q=0}^{m}p_q|e_q\rangle\langle e_q|,
\qquad
R=Q\bmod g.
```

For each residue with positive probability, the supported charges in that residue form an ordered alphabet in which consecutive charges differ by at least $`g`$. Every internal comparison of its alphabetic tree can therefore be implemented by Section 4, using the physical shift checked in Section 3.

The conditional encoding states are pure, so their Holevo information equals the entropy of their average. Entropy concavity over the residue classes gives

```math
S(\sigma_E)
\ge
(1-h_2(\zeta))H(Q\mid R)-2h_2(\zeta).
```

Equivalently,

```math
S(\sigma_E)
\ge
(1-h_2(\zeta))
\bigl(H(p)-H(R)\bigr)
-2h_2(\zeta).
```

A convenient weaker form is

```math
S(\sigma_E)
\ge
(1-h_2(\zeta))
\bigl(H(p)-\log_2g\bigr)
-2h_2(\zeta).
```

One may use $`H(R)\le\log_2\min(g,m+1)`$ when this is sharper. The conditional-entropy form remains well defined and non-artificial when $`g>m`$.

More precisely, for any chosen alphabetic tree in each residue, with conditional mean depths $`L_r`$,

```math
S(\sigma_E)
\ge
H(Q\mid R)-h_2(\zeta)\sum_rp_rL_r.
```

This version removes the additive two when the code has an exact known tree. Each displayed pointer-entropy lower bound can be capped below by zero.

## 7. Transferring pointer entropy to actual output entropy

This step uses selected baseline survival only. It requires neither calibration nor causality.

Set $`d=m+1`$ and define the Fourier phase family

```math
|\psi_k\rangle
=
\sum_{q=0}^{m}
\sqrt{p_q}\,e^{2\pi i kq/d}|\chi_q\rangle,
\qquad
k=0,\ldots,d-1.
```

Each member is a normalized pure input. Let

```math
\overline S_{\mathrm{out}}
=
\frac1d\sum_{k=0}^{d-1}
S\!\left(
\mathcal E(|\psi_k\rangle\langle\psi_k|)
\right).
```

The transfer inequality is

```math
\boxed{
\overline S_{\mathrm{out}}
\ge
(1-\varepsilon)S(\sigma_E)
-h_2(\varepsilon)-\varepsilon H(p).
}
```

### 7.1 The average actual environment dominates the pointer mixture

Fourier averaging removes every off-diagonal term in the charge label. Thus the average complementary output is

```math
\overline\rho_E
=
\sum_qp_q\rho_{E,q}.
```

Section 2 gives

```math
\overline\rho_E\ge(1-\varepsilon)\sigma_E.
```

For $`\varepsilon>0`$, write the difference as $`\varepsilon\omega_E`$, where $`\omega_E`$ is a density operator. Entropy concavity gives

```math
S(\overline\rho_E)\ge(1-\varepsilon)S(\sigma_E).
```

The same statement holds directly at $`\varepsilon=0`$.

### 7.2 Split-memory uncertainty

Introduce a reference register $`C`$ and the pure state

```math
|\Omega\rangle_{CSE}
=
\sum_{q=0}^{m}\sqrt{p_q}\,
|q\rangle_C V|\chi_q\rangle,
\qquad
S=A_{\mathrm{out}}B_{\mathrm{out}}.
```

Because $`V`$ is an isometry and the baseline states are orthogonal, the reduced reference state is diagonal with probabilities $`p_q`$.

Let $`Z`$ be measurement of $`C`$ in the charge-label basis and $`X`$ measurement in its Fourier-conjugate basis. Their overlap is $`1/d`$. The split-memory uncertainty relation is

```math
H(Z\mid S)+H(X\mid E)\ge\log_2d.
```

This is the mutually unbiased special case of [Berta et al., Corollary 2](https://arxiv.org/abs/0909.0950). For completeness, it follows directly from relative entropy here. For the reduced state $`\rho_{CE}`$, let $`\Delta_Z`$ and $`\Delta_X`$ be dephasings on $`C`$. Data processing gives

```math
\begin{aligned}
H(Z\mid E)-H(C\mid E)
&=
D(\rho_{CE}\Vert\Delta_Z\rho_{CE})\\
&\ge
D\!\left(
\Delta_X\rho_{CE}\,\middle\Vert\,
\frac{I_C}{d}\otimes\rho_E
\right)\\
&=
\log_2d-H(X\mid E).
\end{aligned}
```

The middle reference state has the stated form because the bases are mutually unbiased. Purity of $`|\Omega\rangle`$ and of each post-$`Z`$ conditional state on $`SE`$ imply

```math
H(Z\mid S)=H(Z\mid E)-H(C\mid E).
```

This proves the split-memory inequality.

The Fourier outcome is uniform, even for nonuniform $`p`$. Conditional on outcome $`k`$, the state on $`SE`$ is $`V|\psi_k\rangle`$, up to the harmless Fourier sign convention. Therefore

```math
H(X\mid E)=\log_2d-\chi_X(E),
\qquad
\chi_X(E)\le H(Z\mid S).
```

### 7.3 Survival limits the missing charge information in the system

Measure $`S`$ with the orthogonal projectors $`|\chi_q\rangle\langle\chi_q|`$ and the remaining failure projector. Denote the outcome by $`\widehat Z`$. The induced classical channel obeys

```math
\Pr(\widehat Z=q\mid Z=q)=f_q\ge1-\varepsilon.
```

For $`\varepsilon>0`$, it can be decomposed exactly as

```math
P_{\widehat Z\mid Z}
=
(1-\varepsilon)\,\mathrm{Id}
+
\varepsilon W',
```

where $`W'`$ is a stochastic channel, including a possible failure outcome. The coefficient of the identity is the same for every input symbol, so the branch flag can be chosen independent of $`Z`$.

If that flag selects the identity branch, $`Z`$ is known from $`\widehat Z`$. If it selects $`W'`$, the remaining uncertainty is at most $`H(p)`$. Adding the flag can cost at most $`h_2(\varepsilon)`$. Thus

```math
H(Z\mid S)
\le
H(Z\mid\widehat Z)
\le
h_2(\varepsilon)+\varepsilon H(p).
```

At $`\varepsilon=0`$, the same inequality says $`H(Z\mid S)=0`$.

### 7.4 Finish the transfer

Each $`V|\psi_k\rangle`$ is pure, so its system and environment entropies agree. Hence

```math
\begin{aligned}
\overline S_{\mathrm{out}}
&=
S(\overline\rho_E)-\chi_X(E)\\
&\ge
S(\overline\rho_E)-H(Z\mid S)\\
&\ge
(1-\varepsilon)S(\sigma_E)
-h_2(\varepsilon)-\varepsilon H(p).
\end{aligned}
```

This proves the transfer inequality without a continuity penalty proportional to the full system dimension.

## 8. General robustness theorem and product inputs

Define

```math
A=(1-\varepsilon)(1-h_2(\zeta)),
\qquad
\gamma=A-\varepsilon.
```

Combining Sections 6 and 7 proves

```math
\boxed{
\overline S_{\mathrm{out}}
\ge
\gamma H(p)
-AH(Q\bmod g)
-2(1-\varepsilon)h_2(\zeta)
-h_2(\varepsilon).
}
```

In particular,

```math
\boxed{
\overline S_{\mathrm{out}}
\ge
\gamma H(p)
-A\log_2g
-2(1-\varepsilon)h_2(\zeta)
-h_2(\varepsilon).
}
```

A negative right-hand side is replaced by zero. At least one member of the prescribed Fourier family has output entropy at least this lower bound. The coefficient $`\gamma>0`$ is the informative regime for logarithmic growth at fixed $`g`$; positivity of this coefficient is a sufficient condition for this estimate, not a necessary condition for physical backaction.

### Product phase family

Choose the normalized symmetric Dicke state of charge $`q`$ on $`A`$,

```math
|a_q\rangle=|D_q^{(m)}\rangle,
\qquad
p_q=2^{-m}\binom mq.
```

Then the Fourier family consists entirely of product states:

```math
|\psi_k\rangle
=
|+_{\theta_k}\rangle_A^{\otimes m}
\otimes|0\rangle_B,
\qquad
|+_\theta\rangle
=
\frac{|0\rangle+e^{i\theta}|1\rangle}{\sqrt2},
\qquad
\theta_k=\frac{2\pi k}{m+1}.
```

Every component charge lies below or at $`a`$. With

```math
H_m=H(\mathrm{Bin}(m,1/2)),
```

the bound becomes

```math
\overline S_{\mathrm{out}}
\ge
\gamma H_m
-A\log_2g
-2(1-\varepsilon)h_2(\zeta)
-h_2(\varepsilon).
```

The exact entropy $`H_m`$ can be used at every finite $`m`$. Its familiar large-$`m`$ form is

```math
H_m=\frac12\log_2m+O(1).
```

For the scaling statement, the upper bound follows from the variance entropy bound for an integer random variable; the lower bound follows from $`H_m\ge-\log_2\max_qp_q`$ and the central binomial coefficient estimate. No Gaussian approximation is needed for the finite-size inequality above.

### Balanced spaced alphabet

There is no alphabetic-code overhead for a uniform binary alphabet of size $`M=2^r`$ at charges $`0,g,\ldots,g(M-1)`$. A valid integer choice is

```math
r=
\left\lfloor
\log_2\!\left(1+\left\lfloor\frac m g\right\rfloor\right)
\right\rfloor,
\qquad
M=2^r.
```

The balanced tree has mean depth exactly $`r`$, so

```math
S(\sigma_E)\ge(1-h_2(\zeta))r.
```

Applying the transfer argument with a reference register labeling these $`M`$ states gives

```math
\overline S_{\mathrm{out}}\ge\gamma r-h_2(\varepsilon).
```

When $`m<g`$, this choice gives $`r=0`$, $`M=1`$, and the nonnegative bound is zero. Every code charge fits in the active block, and all comparison shifts remain valid by Section 3.

## 9. Stronger theorem for exact readout

Assume now $`\eta=0`$ and exact nonsignalling, while retaining $`0\le\varepsilon<1`$. Exact outcome support yields a stronger entropy estimate than inserting $`\eta=0`$ into the approximate-decoder formula.

### 9.1 Condition on the active system only

Define

```math
\alpha_q
=
\left\|
(\langle a_q|_{A_{\mathrm{out}}}\otimes I_{\mathcal K})
V|\chi_q\rangle
\right\|^2,
\qquad
|u_q\rangle
=
\frac{
(\langle a_q|\otimes I_{\mathcal K})
V|\chi_q\rangle
}{\sqrt{\alpha_q}}.
```

Projection on the full baseline state is more restrictive than projection on its $`A`$ part, so

```math
1-\varepsilon\le f_q\le\alpha_q\le1.
```

For $`q<r`$ with $`r-q\ge g`$, use the same physical shift $`b=a-q`$ for both inputs. Their actual shifted outputs have opposite outcomes with probability one.

Conditioning on $`|a_q\rangle`$ or $`|a_r\rangle`$ in $`A_{\mathrm{out}}`$ commutes with both the complementary unitary $`W_b`$ and the outcome measurement. Consequently, $`W_b|u_q\rangle`$ lies entirely in the low-outcome subspace and $`W_b|u_r\rangle`$ entirely in the high-outcome subspace. Their inner product vanishes. Unitarity then gives

```math
\langle u_q|u_r\rangle=0
\qquad\text{whenever }|q-r|\ge g.
```

This conditioning step is valid because an event of probability one remains certain on every nonzero commuting postselection branch. The lower bound on $`\alpha_q`$ guarantees that the branches used here are nonzero.

### 9.2 Compression bounds the pointer Gram matrix

Let $`T=\langle0|_{B_{\mathrm{out}}}\otimes I_E`$, a contraction from $`\mathcal K`$ to $`E`$. Then

```math
T|u_q\rangle=\sqrt{r_q}\,|e_q\rangle,
\qquad
r_q=\frac{f_q}{\alpha_q}\ge1-\varepsilon.
```

Fix one residue class modulo $`g`$. Its distinct $`u_q`$ are orthonormal. If $`G`$ is the Gram matrix of its normalized $`e_q`$ and $`D_r`$ is diagonal with entries $`r_q`$, contraction of their synthesis map gives

```math
D_r^{1/2}GD_r^{1/2}\le I.
```

Therefore

```math
G\le D_r^{-1}\le\frac{I}{1-\varepsilon}.
```

### 9.3 Weighted Gram entropy

Let $`p`$ now denote the conditional prior in this residue, after removing its zero-probability entries, and let $`P=\mathrm{diag}(p)`$. The weighted Gram matrix

```math
B=P^{1/2}GP^{1/2}
```

has trace one, diagonal $`p`$, and the same nonzero eigenvalues as the conditional pointer mixture. It obeys

```math
B\le\frac{P}{1-\varepsilon}.
```

Operator monotonicity of the logarithm gives the entropy bound

```math
S(B)\ge H(p)+\log_2(1-\varepsilon).
```

For a possibly singular $`B`$, apply monotonicity to $`B+tI`$ and $`P/(1-\varepsilon)+tI`$, multiply by $`B`$, take the trace, and then let $`t\downarrow0`$. The diagonal identity $`B_{qq}=p_q`$ gives

```math
\mathrm{tr}\,B\log_2B
\le
\sum_qp_q\log_2p_q-\log_2(1-\varepsilon).
```

This proves the claim without any assumption that the projected pointers themselves remain orthogonal.

Concavity over the residue classes now gives

```math
\boxed{
S(\sigma_E)
\ge
H(Q\mid Q\bmod g)+\log_2(1-\varepsilon).
}
```

Again, zero is a valid cap.

### 9.4 Exact-readout output bound

Insert this estimate into the Fourier transfer inequality:

```math
\boxed{
\begin{aligned}
\overline S_{\mathrm{out}}
\ge{}&
(1-2\varepsilon)H(p)
-(1-\varepsilon)H(Q\bmod g)\\
&+(1-\varepsilon)\log_2(1-\varepsilon)
-h_2(\varepsilon).
\end{aligned}
}
```

Writing

```math
b_\varepsilon
=
h_2(\varepsilon)
-(1-\varepsilon)\log_2(1-\varepsilon),
```

a simpler form is

```math
\boxed{
\overline S_{\mathrm{out}}
\ge
(1-2\varepsilon)H(p)
-(1-\varepsilon)\log_2g
-b_\varepsilon.
}
```

For the binomial product prior, replace $`H(p)`$ by $`H_m`$. For the uniform spaced alphabet, all symbols have the same residue and the bound is

```math
\overline S_{\mathrm{out}}
\ge
(1-2\varepsilon)\log_2M-b_\varepsilon.
```

The leading entropy coefficient is positive for $`\varepsilon<1/2`$. The formulas remain valid outside that range after taking their nonnegative cap, but then they need not provide a useful lower bound proportional to the prior entropy.

Exact readout also makes the displayed result low with probability one for every member of the wholly-low Fourier family, as shown in Section 11. This stronger Gram argument requires exact nonsignalling as well as exact readout.

## 10. Approximate causality in full diamond norm

### 10.1 Definition and normalization

Define the induced reduced channels on the whole active input space by

```math
\Lambda_b(\rho_A)
=
\mathrm{tr}_{B_{\mathrm{out}}}\,
\mathcal E\!\left(
\rho_A\otimes|\beta_b\rangle\langle\beta_b|
\right).
```

Assume

```math
\kappa
=
\max_{0\le b\le N-m}
\|\Lambda_b-\Lambda_0\|_\diamond
\le2.
```

This is the full, unhalved diamond norm. For a difference of channels it includes optimization over states on $`A`$ together with a reference system of dimension $`\dim A`$:

```math
\|\Lambda_b-\Lambda_0\|_\diamond
=
\sup_{\rho_{AR}}
\left\|
\bigl((\Lambda_b-\Lambda_0)\otimes\mathrm{id}_R\bigr)
(\rho_{AR})
\right\|_1.
```

An estimate only on the selected charge basis inputs, or only on unreferenced reduced states, is not the assumption used by this theorem. The stated maximum is stronger than necessary: it suffices to include the baseline and all shifts used by the comparisons.

If a full reduced-channel causality estimate is supplied instead,

```math
\left\|
\mathrm{tr}_{B_{\mathrm{out}}}\,\mathcal E
-
\mathcal T_A\circ\mathrm{tr}_{B_{\mathrm{in}}}
\right\|_\diamond
\le\delta,
```

then composition with each fixed preparation of $`B`$ and the triangle inequality imply

```math
\kappa\le\min(2,2\delta).
```

If that last estimate is stated with a factor $`1/2`$ in front of its diamond norm, its numerical parameter must first be doubled; in that convention, $`\kappa\le\min(2,4\delta)`$.

### 10.2 Approximate Stinespring intertwiners

The continuity theorem for Stinespring dilations gives, after padding a common environment, unitaries $`W_b`$ satisfying

```math
\left\|
V_b-(I_{A_{\mathrm{out}}}\otimes W_b)V_0
\right\|_\infty
\le\sqrt{\kappa}.
```

The norm is the operator norm on the entire active input space. The dimension-independent square-root estimate is the Schrödinger-picture form of the [Kretschmann–Schlingemann–Werner continuity theorem](https://arxiv.org/abs/0710.2495).

One way to justify its use with the fixed instrument dilation is to first obtain close dilations of $`\Lambda_b`$ and $`\Lambda_0`$ from that theorem. Stinespring uniqueness identifies each of them with the fixed corresponding dilation after common padding. Composing the two environmental unitaries gives the displayed $`W_b`$. A sufficiently large finite padding can be chosen for all finitely many shifts at once. No claim about keeping a minimal environment unchanged is needed.

The padded outcome measurement is the original $`P_y`$ tensored with the identity on the unused ancilla. Thus the comparison decoder still reads the actual instrument outcome.

### 10.3 Decoder error and entropy bound

For each comparison and each encoded charge, the normalized pointer simulation is at trace distance at most $`\sqrt{\varepsilon}`$ from the transformed baseline output. The latter is at trace distance at most $`\sqrt{\kappa}`$ from the actual shifted output: for normalized vectors, pure-state trace distance is at most their vector norm difference.

The comparison error is consequently at most

```math
\eta+\sqrt{\varepsilon}+\sqrt{\kappa}.
```

Set

```math
\zeta_\kappa
=
\min\left\{
\frac12,\,
\eta+\sqrt{\varepsilon}+\sqrt{\kappa}
\right\},
```

using an independent fair guess if the second entry exceeds one half. This conservative expression is sufficient; at $`\kappa=0`$, the sharper angular parameter from Section 4 may be used instead.

Every step of Sections 5–8 now applies with $`\zeta`$ replaced by $`\zeta_\kappa`$. In particular, with

```math
A_\kappa=(1-\varepsilon)(1-h_2(\zeta_\kappa)),
\qquad
\gamma_\kappa=A_\kappa-\varepsilon,
```

one obtains

```math
\boxed{
\overline S_{\mathrm{out}}
\ge
\gamma_\kappa H(p)
-A_\kappa H(Q\bmod g)
-2(1-\varepsilon)h_2(\zeta_\kappa)
-h_2(\varepsilon).
}
```

Replacing the residue entropy by $`\log_2g`$ gives the simpler width-dependent form. There is no factor proportional to the number of charges, comparisons, or shifts: the operator-norm estimate is uniform on the active input space, and the serial entropy argument uses the average tree depth.

The exact-readout Gram improvement in Section 9 does not follow from nonzero $`\kappa`$. Approximate intertwiners yield approximate, rather than exact, orthogonality of the conditioned vectors, so the exact compression inequality cannot be imported unchanged.

## 11. What the preparation phases and readout guarantees mean

The entropy conclusions bound

```math
\frac1d\sum_k S(\mathcal E(|\psi_k\rangle\langle\psi_k|)),
```

the average of the entropies from known pure preparations. Operationally, the phase can be chosen uniformly from the stated finite set and its classical preparation label retained. This quantity is different from the entropy of the output obtained after forgetting the phase label.

There is at least one phase whose output entropy is at least the average lower bound. In general that phase may depend on the instrument. The proof does not establish the same bound for a predetermined phase such as $`\theta=0`$ when $`\varepsilon>0`$.

If $`\varepsilon=0`$, every baseline dilation factorizes exactly:

```math
V|\chi_q\rangle=|\chi_q\rangle|e_q\rangle.
```

For these exact baseline states, the complementary output of every phase input is the same $`\sigma_E`$. Its output entropy and its outcome distribution are therefore independent of the phase. In this special case, the entropy lower bound holds for each phase, and sectorwise calibration also bounds each phase's displayed-high probability by $`\eta`$.

### Nonzero sectorwise calibration error

All the baseline charges satisfy $`q\le m\le a`$. Averaging the actual displayed-high probabilities over the Fourier family removes the off-diagonal terms, giving

```math
\frac1d\sum_k
\mathrm{tr}\,\mathcal I_1(|\psi_k\rangle\langle\psi_k|)
=
\sum_qp_q
\mathrm{tr}\,\mathcal I_1(|\chi_q\rangle\langle\chi_q|)
\le\eta.
```

This is an average guarantee. When both $`\eta>0`$ and $`\varepsilon>0`$, the high-entropy phase obtained from the entropy average is not automatically a phase whose individual displayed-high probability is at most $`\eta`$. The entropy proof and the readout average must not be combined into an unsupported simultaneous per-phase claim.

If calibration is strengthened to require error at most $`\eta`$ on every state in the entire low-charge subspace, then every phase in this family has readout error at most $`\eta`$ by that stronger assumption.

### Exact readout

At $`\eta=0`$, let $`F_1=\mathcal I_1^*(I)`$ be the positive effect for result high. Calibration gives

```math
\langle\chi_q|F_1|\chi_q\rangle=0
\qquad
(0\le q\le m).
```

Positivity implies $`F_1^{1/2}|\chi_q\rangle=0`$, hence $`F_1|\chi_q\rangle=0`$. It therefore annihilates their whole span, and

```math
\mathrm{tr}\,\mathcal I_1(|\psi_k\rangle\langle\psi_k|)=0
\qquad\text{for every }k.
```

This conclusion needs neither exact survival nor exact causality. Under exact readout, the large-entropy phase supplied by either applicable entropy theorem is indeed a phase that displays low with certainty.

## 12. Scope and limiting cases

The assumptions enter at separate points:

| Assumption | Use in the proof |
| --- | --- |
| Survival on the selected baseline vectors | Normalized pointers, complementary-state domination, and Fourier entropy transfer |
| Sectorwise threshold calibration | Correct readout on the physically shifted charge inputs |
| Exact one-way nonsignalling | Input-independent complementary unitaries |
| Full diamond-norm approximate causality | Uniform approximate complementary unitaries with error $`\sqrt{\kappa}`$ |
| Exact readout and exact nonsignalling | Orthogonality of active-system-conditioned pointers and the stronger Gram bound |
| Ordered residue alphabets | Every tree branch can be implemented by a calibrated threshold shift |

All probabilities with zero prior are omitted from conditional alphabets. Residues of zero probability contribute zero. At $`\varepsilon=0`$, decompositions involving division by $`\varepsilon`$ are replaced by their exact limiting identities. The endpoint $`\varepsilon=1`$ is excluded because the normalized baseline pointers need not exist; without any survival guarantee, these theorems assert no nontrivial entropy lower bound.

Every entropy lower bound is interpreted together with $`S\ge0`$. Parameters for which a displayed coefficient is nonpositive are permitted but may yield only that trivial bound. The fair-guess cap must be applied before inserting a decoder error into $`h_2`$; binary entropy is not monotone beyond one half.

The proof bounds entropy created in the retained quantum system from pure inputs. It supplies an information statement about a Stinespring complement, including any apparatus purification. It does not by itself identify that entropy with accessible classical record length, apparatus dimension, thermodynamic work, or a physical cost of implementing the mathematical comparison decoders.

## Primary sources for the proof ingredients

- T. Eggeling, D. Schlingemann, and R. F. Werner, **Semicausal operations are semilocalizable**, *Europhysics Letters* **57**, 782–788 (2002). [arXiv:quant-ph/0104027](https://arxiv.org/abs/quant-ph/0104027). Source for the Stinespring structure of semicausal operations.
- A. Nayak, **Optimal lower bounds for quantum automata and random access codes**, *Proceedings of FOCS 1999*, 369–376. [arXiv:quant-ph/9904093](https://arxiv.org/abs/quant-ph/9904093). Source for the entropy method behind quantum encoding lower bounds; the ordered arbitrary-prior tree variant used here is proved in Section 5.
- M. Berta, M. Christandl, R. Colbeck, J. M. Renes, and R. Renner, **The uncertainty principle in the presence of quantum memory**, *Nature Physics* **6**, 659–662 (2010). [arXiv:0909.0950](https://arxiv.org/abs/0909.0950). Its Corollary 2 gives the split-memory uncertainty relation; Section 7 includes the mutually unbiased proof needed here.
- D. Kretschmann, D. Schlingemann, and R. F. Werner, **The information-disturbance tradeoff and the continuity of Stinespring's representation**, *IEEE Transactions on Information Theory* **54**, 1708–1717 (2008). [arXiv:quant-ph/0605009](https://arxiv.org/abs/quant-ph/0605009).
- D. Kretschmann, D. Schlingemann, and R. F. Werner, **A continuity theorem for Stinespring's dilation**, *Journal of Functional Analysis* **255**, 1889–1904 (2008). [arXiv:0710.2495](https://arxiv.org/abs/0710.2495). The common-environment form supplies the dimension-independent approximate-causality step.
