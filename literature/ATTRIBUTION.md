# Attribution and scope of the contribution

This note identifies the closest primary sources and the established mathematical ingredients of the results. The comparisons refer to the specific papers and passages listed below. Source details were checked on 16 October 2026. Full bibliographic entries are in [references.bib](../references.bib).

## 1. Universal entropy necessity and attainability

The exact theorem concerns an ordered threshold for the additive charge $`Q=\sum_jn_j`$. Calibration is exact on every state with $`q\leq a`$ or $`q\geq a+g`$. The nonselective channel preserves every state in every global charge sector, including all degeneracies, and is nonsignalling from the spectator block $`B`$ to the active block $`A`$.

For any pure input in the [model's](../research/MODEL.md) family, let $`p`$ be its charge distribution and let $`J=\lfloor Q_{\mathrm{in}}/g\rfloor`$. With $`\mathsf D`$ denoting the infimum of output entropy over all admissible instruments for that fixed input, the [arbitrary-prior theorem](../research/THEOREM.md) gives

```math
H(J)-1
\leq \mathsf D
\leq S_{\mathrm{window}}(p)
\leq H(J)+\log_2(2-1/g)+C_g,
```

where

```math
C_g=\frac{2}{\ln2}\left(1+\ln g-\sum_{\ell=1}^g\frac1\ell\right)
\leq 1.2198977273.
```

The same finite distributed detector attains the upper bound for every prior and every choice of within-sector vectors. There is no smoothness assumption on the prior. The result identifies the optimal entropy to a universal additive constant, and the one-bit lower correction is necessary for priors straddling a bin boundary.

For $`|+\rangle^{\otimes m}`$ the charge prior is binomial. Its product-state corollary identifies the optimum, to an additive constant, at the scale

```math
\left[\log_2\!\left(\frac{\sqrt m}{g}\right)\right]_+.
```

The placement conditions $`m\leq\min(a,N-a)`$ and $`a+g\leq N`$ ensure that the input is wholly in the low region and that the spectator shifts used by the converse exist. The theorem does not remove these conditions at endpoint thresholds.

The separate [robust results](../research/ROBUSTNESS.md) allow general instruments. Their preservation input is the stated survival condition on baseline states; they do not require approximate preservation of every global charge-sector state or assume scalar Kraus operators. The results retain their explicitly stated calibration and exact or approximate nonsignalling conditions.

The entropy in this statement is the system's nonselective output entropy for a pure input. It is not the number of displayed answer bits, the entropy of all local readout records, or the entanglement consumed to build a probe. The apparatus note explicitly separates these quantities.

The following are established ingredients or motivations and are not claimed as new: causal restrictions on nonlocal measurement updates and causality-forced loss of local information; a coarse question answered through a finer measurement; coherent noisy charge meters; entangled probes with local interactions and later classical processing; the square-root charge-fluctuation scale of product states; semicausal dilation, entropic uncertainty, and serial-encoding bounds.

## 2. Closest physical and measurement antecedents

### Popescu–Vaidman: causal state verification erases local information

**Source:** Sandu Popescu and Lev Vaidman, *Causality constraints on nonlocal quantum measurements*, Physical Review A **49**, 4331–4338 (1994), [DOI](https://doi.org/10.1103/PhysRevA.49.4331), [arXiv:hep-th/9306087](https://arxiv.org/abs/hep-th/9306087), especially Theorems 1–2 on page 4333 of the [author's published copy](https://www.tau.ac.il/~vaidman/lvhp/m32.pdf). Bibliography key: `popescu1994causality`.

For reliable verification of one entangled pure state, their theorems show that subsequent local measurement probabilities lose their dependence on the initial state within the appropriate Schmidt-support subspace. This is direct prior art for causality-forced loss of local information. The ordered-threshold problem has a different calibration premise: its ideal decision effects are sums of computational-basis product projectors. The result here quantifies the minimum nonselective output entropy for arbitrary pure charge priors at finite resolution, including product inputs, and supplies a common apparatus attaining the upper bound. The entangled-state verification premise does not directly apply to these threshold effects.

### Albertini–Jubb: causality constrains the Kraus kernel

**Source:** Emma Albertini and Ian Jubb, *Are Ideal Measurements of Real Scalar Fields Causal?* (2023), [arXiv:2306.12980](https://arxiv.org/abs/2306.12980), especially Claim 6.1 and the following discussion. Bibliography key: `albertini2023ideal`.

Their real-scalar-field analysis derives a causality condition on a general family of functions of a smeared field, and uses it to diagnose ideal measurements and exhibit causal alternatives. The kernel condition is a close structural antecedent of a translation-invariant charge-coherence kernel. The preceding causal-update framework and Gaussian examples appear in I. Jubb, *Causal state updates in real scalar quantum field theory*, Physical Review D **105**, 025003 (2022), [DOI](https://doi.org/10.1103/PhysRevD.105.025003), [arXiv:2106.09027v2](https://arxiv.org/pdf/2106.09027), Sections II and IV; bibliography key: `jubb2022causal`. Their spacetime assumptions and continuous field spectrum differ from the finite-spin model. These causal-update results do not establish the finite-spin threshold entropy optimization or the general-instrument robust theorem developed here. The structural proximity concerns the causal-kernel step.

### Oeckl: a coarse question can extract fine information

**Source:** Robert Oeckl, *Causal measurement in quantum field theory: Spacetime*, Physical Review D **113**, 085002 (2026), [DOI](https://doi.org/10.1103/5gl8-3j6p), [arXiv:2511.06566v2](https://arxiv.org/html/2511.06566v2), particularly Sections 3.2 and 4.7. Bibliography key: `oeckl2026causal`.

Section 3.2 explicitly distinguishes a binary question about a spectral subset from a regularized measurement that extracts a finer value and then answers that question. It discusses the independence of the nonselective update from the chosen grouping. Section 4.7 revisits the distinction for functions of observables. The earlier instantaneous-observable construction appears in R. Oeckl, *Spectral decomposition of field operators and causal measurement in quantum field theory*, Journal of Mathematical Physics **66**, 042302 (2025), [DOI](https://doi.org/10.1063/5.0245368), [arXiv:2409.08748v2](https://arxiv.org/html/2409.08748v2), Sections 4–5; bibliography key: `oeckl2025spectral`. These are direct antecedents of the qualitative physical story and regularized-measurement construction. They do not give a universal finite-spin lower bound on the minimum entropy needed by every causal threshold detector. The distinction here is the quantitative necessity and attainability theorem.

### Kwon–Park–Tan–Jeong: resolution and disturbance of product states

**Source:** Hyukjoon Kwon, Chae-Yeun Park, Kok Chuan Tan, and Hyunseok Jeong, *Disturbance-Based Measure of Macroscopic Coherence*, New Journal of Physics **19**, 043024 (2017), [DOI](https://doi.org/10.1088/1367-2630/aa68f5), [arXiv:1608.01122](https://arxiv.org/pdf/1608.01122), especially Sections 2.2–3.2. Bibliography key: `kwon2017disturbance`.

They study disturbance from a prescribed coarse collective measurement, including total magnetization on spin-product states, and explicitly identify the relevance of resolution compared with $`\sqrt N`$. Their product-state calculation uses a Gaussian approximation to the binomial distribution; their general analysis relates disturbance to skew information. Thus neither product-state sensitivity nor the fluctuation scale is a new observation here. The project instead optimizes entropy backaction over a causally constrained detector class with threshold calibration, and supplies finite, uniform bounds and a matching apparatus.

### Aaronson–Rothblum: coherent noisy Hamming-weight meters

**Source:** Scott Aaronson and Guy N. Rothblum, *Gentle Measurement of Quantum States and Differential Privacy*, STOC 2019, pp. 322–333, [DOI](https://doi.org/10.1145/3313276.3316378), [full preprint](https://arxiv.org/pdf/1904.08747), especially Sections 1.1, 1.3, and 7.1. Bibliography key: `aaronson2019gentle`.

Section 1.1 already constructs a meter coherently translated by the Hamming weight, using Laplace noise, and explains gentleness when the noise dominates the product-state fluctuation width. Their results relate differential privacy to gentle measurement. Section 7.1 discusses binary threshold processing with garbage uncomputation. This is direct prior art for noisy translated meters and gentle counting. The unbounded Laplace distribution does not give our exact zero-error promise calibration at a finite gap. Our bounded window, classical grouping of fine outcomes, and universal nonsignalling entropy lower bound are distinct requirements. Neither the noisy-meter idea nor a general noise–gentleness connection is claimed as new.

### Beckman–Gottesman–Nielsen–Preskill: causal and localizable operations

**Source:** David Beckman, Daniel Gottesman, M. A. Nielsen, and John Preskill, *Causal and localizable quantum operations*, Physical Review A **64**, 052309 (2001), [DOI](https://doi.org/10.1103/PhysRevA.64.052309), [preprint](https://arxiv.org/pdf/quant-ph/0102043), particularly Section II. Bibliography key: `beckman2001causal`.

This paper distinguishes nonsignalling operations from operations implementable locally using preshared resources. It establishes measurement structure results and explains distributed stabilizer measurements. For CSS measurements, it describes the sequence of shared entangled ancilla, local gates, local readout, and classical processing, crediting Steane. The present apparatus belongs to this established framework. Its explicit construction proves local implementability of this particular instrument; it does not assume that every nonsignalling operation is locally implementable.

### Vidil–Edamatsu: weighted GHZ probes and identical record Kraus operators

**Source:** Pierre Vidil and Keiichi Edamatsu, *Nonlocal Variable-Strength Measurements of N Qubits Using GHZ-like Entanglement* (2021), [arXiv:2103.00443](https://arxiv.org/pdf/2103.00443), Sections III–V, especially equations (8)–(14) and (28). Bibliography key: `vidil2021nonlocal`.

Their protocol uses weighted GHZ probes, local controlled product-observable gates, local Fourier readout for qubits, and classical parity. It explicitly counts identical Kraus operators for records with the same parity. Their quantitative resource relation concerns the tangle of a selected probe family and measurement strength. The cyclic-register Fourier construction adapts this apparatus architecture. Their result does not provide the universal ordered-threshold entropy cost. In particular, the two-outcome product-observable channel has at most two unitary branches, so it can have bounded pure-input output entropy for arbitrarily many spins.

## 3. Established mathematical ingredients

### Eggeling–Schlingemann–Werner: semicausal dilation

**Source:** T. Eggeling, D. Schlingemann, and R. F. Werner, *Semicausal operations are semilocalizable*, Europhysics Letters **57**, 782–788 (2002), [DOI](https://doi.org/10.1209/epl/i2002-00579-4), [preprint](https://arxiv.org/pdf/quant-ph/0104027), Section III. Bibliography key: `eggeling2002semicausal`.

Their theorem and proof use uniqueness of Stinespring dilation to factor a semicausal operation. This is the structural principle behind transferring a remote control into a complementary output in the robust proof. The use of an environment isometry or, after adequate padding, a unitary, is an established tool. The specific reduction from threshold calibration and approximate preservation to decodable information in that output is the task-specific step.

### Nayak: serial encoding lower bounds

**Source:** Ashwin Nayak, *Optimal lower bounds for quantum automata and random access codes*, FOCS 1999, pp. 369–376, [DOI](https://doi.org/10.1109/SFFCS.1999.814608), [preprint](https://arxiv.org/pdf/quant-ph/9904093), Theorem 2.3 and its proof. Bibliography key: `nayak1999optimal`.

The lower bound explicitly includes serial encodings, in which a decoder may depend on the appropriate already specified bits. Its entropy argument is the relevant information bound for the serial comparison construction. The threshold application specifies the decoders, their side information, their common encoded ensemble, and their error bound. A list of distinguishable pairs alone would not supply a serial encoding. The encoding bound is an established ingredient.

### Berta et al.: entropic uncertainty with quantum memory

**Source:** Mario Berta, Matthias Christandl, Roger Colbeck, Joseph M. Renes, and Renato Renner, *The uncertainty principle in the presence of quantum memory*, Nature Physics **6**, 659–662 (2010), [DOI](https://doi.org/10.1038/nphys1734), [preprint and supplement](https://arxiv.org/pdf/0909.0950). Bibliography key: `berta2010uncertainty`.

Supplementary Corollary 2 gives the uncertainty relation with separate quantum memories used in the complementary-information argument. Supplementary Theorem 1 also gives $`H(X)+H(Z)\geq\log_2d+S(\rho)`$ for trivial memory and mutually unbiased bases. The exact upper-bound proof derives this latter relation directly using finite-dimensional position and Fourier dephasing and relative-entropy data processing. The uncertainty relations are established ingredients; the reduction from threshold calibration to complementary information is the application.

### Kretschmann–Schlingemann–Werner: robust dilation comparison

**Sources:** Dennis Kretschmann, Dirk Schlingemann, and Reinhard F. Werner, *The Information-Disturbance Tradeoff and the Continuity of Stinespring's Representation*, IEEE Transactions on Information Theory **54**, 1708–1717 (2008), [DOI](https://doi.org/10.1109/TIT.2008.917696), [preprint](https://arxiv.org/pdf/quant-ph/0605009), Theorem 1; and *A continuity theorem for Stinespring's dilation*, Journal of Functional Analysis **255**, 1889–1904 (2008), [DOI](https://doi.org/10.1016/j.jfa.2008.07.023), [preprint](https://arxiv.org/abs/0710.2495). Bibliography keys: `ksw2008information` and `ksw2008continuity`.

The continuity theorem supplies dimension-independent control of dilations from completely bounded channel distance. In Schrödinger-picture conventions, full diamond-norm error at most $`\kappa`$ permits dilation operator-norm error at most $`\sqrt\kappa`$ after suitable common padding and environment alignment. This is an established robustness ingredient. The approximate-causality result retains the full, unhalved diamond norm on the stated active input space. Closeness only on unentangled inputs is not a dimension-independent substitute. The combination with threshold calibration and entropy transfer is the application.

## 4. Historical and educational anchors

[Aharonov–Albert–Vaidman (1986)](https://doi.org/10.1103/PhysRevD.34.1805) is a historical primary source for nondemolition measurement of separated composite systems under relativistic constraints. The publisher abstract and bibliographic metadata were checked; this note does not rely on an inspection of its full text. Bibliography key: `aharonov1986measurement`.

[Steane (1997)](https://doi.org/10.1103/PhysRevLett.78.2252) is the earlier ancilla-based stabilization reference explicitly credited by Beckman et al. Its bibliographic record is provided for that attribution chain. Bibliography key: `steane1997active`.

[John Watrous, *The Theory of Quantum Information* (2018)](https://cs.uwaterloo.ca/~watrous/TQI/) is an educational reference for channels, state and channel distances, and entropy. The official author page provides chapters 2, 3, and 5; the [publisher DOI](https://doi.org/10.1017/9781316848142) confirms the book record. Bibliography key: `watrous2018theory`. The repository links to these resources and does not redistribute the textbook or research papers.

## 5. Scientific scope of the comparison

The exact result is a universal entropy converse and a matching construction for arbitrary pure charge priors under the stated operational conditions. The product-state fluctuation law is a corollary. The robust result uses general instruments and the stated baseline-survival and causal assumptions.

The earlier physical ideas, mathematical tools, and apparatus architecture remain attributed to the sources above. A construction for one chosen instrument supplies an upper bound; the lower bound applies to every admissible instrument. These different quantifiers explain why a known causal meter or fluctuation-scale analysis does not by itself establish the entropy optimization theorem.

The scope comparison above is based on the cited papers and the specific passages identified. It does not establish absence of equivalent results elsewhere. Publication metadata for Albertini–Jubb and Vidil–Edamatsu is recorded using their verified arXiv preprints; no journal assignment has been inferred.
