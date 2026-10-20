# Verification and reproduction

The mathematical results are proved in the [causal converse](../science/causal_converse.md),
[window entropy bound](../science/window_entropy.md),
[fluctuation regimes](../science/fluctuation_regimes.md),
[distributed apparatus](../science/distributed_apparatus.md), and
[robustness](../science/robustness.md). The [proof map](../science/proof_map.md)
locates their dependencies and the parity comparison.
The code independently checks finite identities and evaluates the explicit
window apparatus. It does not optimize over all causal instruments or establish
a universal converse by sampling.

## Run the checks

From the repository root:

```sh
python -m pip install -r requirements.txt
python -m unittest discover -s tests -v
OPENBLAS_NUM_THREADS=1 OMP_NUM_THREADS=1 python tools/verify.py --output build/verification
python tools/check_repository.py
```

The implementation uses Python, NumPy, SciPy, and Matplotlib. The reference run
used Python 3.12.14, NumPy 2.3.5, SciPy 1.17.0, and Matplotlib 3.10.8. The package
is imported directly from the repository root; no external data, credentials,
quantum hardware, or package installation of this repository is needed.

The verification command writes `entropy_values.csv` and `summary.json` in the
chosen output directory. Generated reports and interpreter caches are excluded
from version control. The report includes the actual Python, NumPy, and SciPy
versions so later runs retain their own environment information.

## Scientific assertions checked

The 12 test methods in [test_science.py](../tests/test_science.py) include
11 scientific checks of the identities below and one input-domain regression:

| Check | Independent comparison |
|---|---|
| Pointer spectrum | Direct position-space pointer mixture versus the weighted triangular Gram matrix |
| Sharp threshold | At g=1 the output entropy equals the full charge entropy |
| Spaced coherent code | Mutually separated windows yield entropy exactly log₂M |
| Bin-boundary case | The two-pointer spectrum gives h₂(1/(2g)) |
| General priors | Deterministic sampled priors satisfy coarse-bin, convolution, and variance inequalities |
| Binomial examples | Explicit apparatus entropy lies between the analytic product lower bound and variance upper bound |
| Common core | Narrow-support priors obey the span-dependent vanishing estimate |
| Fejér integral | Midpoint quadrature independently agrees with the evaluated harmonic-number expression |
| Robust coefficients | The angular error and exact-readout constants agree with reference values |
| Full distributed record | Direct Fourier sums reproduce every Kraus amplitude for N=3, g=2, D=8, including binary calibration |
| Channel and transcripts | Equality on every matrix unit, all proper local-record subsets, and the random-product-unitary representation |

Several related assertions share a test method. The transcript checks enumerate
all 512 full local records in the finite example. Equality of the Schur kernel
on every system matrix unit establishes equality of those finite channels,
including their action with untouched references. The small example does not
replace the apparatus proof for arbitrary N and D.

The general-prior checks use fixed random seeds, including sharply concentrated
and broadly spread priors. Spectral comparisons use a tolerance that accommodates
floating-point roundoff; a materially negative eigenvalue is an error, not
silently interpreted as a probability.

The input-domain regression checks that a complex NumPy prior is rejected
before conversion to real floating-point values.

## Reference entropy values

All entries are bits. The lower bound is
$`\max\{0,H(\mathrm{Bin}(m,1/2))-\log_2g\}`$. The upper bound is

```math
\frac12\log_2\!\left[2\pi e\left(\frac{m}{4g^2}+\frac1{12}\right)\right]+C_g.
```

The ambient parameters must satisfy the [theorem's placement conditions](../science/model.md).
They do not enter the window spectrum once the active prior and gap are fixed.

| m | g | Product lower bound | Window entropy | Variance upper bound |
|---:|---:|---:|---:|---:|
| 1 | 1 | 1.00000000 | 1.00000000 | 1.25461433 |
| 8 | 1 | 2.54419751 | 2.54419751 | 2.57654243 |
| 8 | 3 | 0.95923501 | 1.83815031 | 1.95728216 |
| 8 | 32 | 0.00000000 | 0.37491454 | 1.44637413 |
| 64 | 2 | 3.04706527 | 3.61135178 | 3.61927422 |
| 64 | 8 | 1.04706527 | 2.20239048 | 2.29792637 |
| 64 | 32 | 0.00000000 | 0.92004005 | 1.55362639 |
| 256 | 4 | 3.04709374 | 3.92996481 | 3.93613000 |
| 256 | 16 | 1.04709374 | 2.29097330 | 2.38528251 |
| 256 | 128 | 0.00000000 | 0.54990709 | 1.49630028 |

The universal constants evaluate to

```math
C_\infty=1.2198977272241924\ldots,\qquad
C_*=2.2669933124048334\ldots.
```

At η=ε=0.01, the general noisy-readout calculation gives
ζ=0.0396, A=0.7519493630703731, and γ=0.7419493630703731. In the separate
exact-readout theorem at ε=0.01, the leading coefficient is 0.98 and
$`b_\varepsilon=0.09514770989407512`$. These are different assumptions, not two
estimates for the same noisy-readout setting.

## Regenerate the explanatory figure

```sh
OPENBLAS_NUM_THREADS=1 OMP_NUM_THREADS=1 python tools/verify.py --output build/verification --figures assets
```

This writes [threshold_entropy.svg](../assets/threshold_entropy.svg) and
[threshold_entropy.png](../assets/threshold_entropy.png). The figure is generated
from the analytic probability response and finite matrix spectra. Its SVG uses
outlined glyphs and fixed metadata. The [worked-example caption](../learning/WORKED_EXAMPLES.md)
states the ambient parameters and the meaning of the shaded bounds.

The figure's large-g variance upper bound approaches a nonzero constant.
The separate analytic common-core argument proves that the actual window
entropy vanishes; this distinction is visible in the text and must be retained.

## Structural and scientific review

[check_repository.py](../tools/check_repository.py) verifies local file links,
fenced-block balance, portable document content, and exactly 30 ordered
milestones with routes from the entry points. It is a structural check, not a
mathematical renderer or proof checker. Changes to substantial mathematics
also require inspection in GitHub's actual renderer.

The exact theorem and apparatus were checked independently of their initial
write-up. The robustness review included the arbitrary-prior alphabetic code,
the cq chain rule, the signs in the split-memory entropy relation, and the
survival-to-entropy transfer. The broad-resolution proof includes the integer
case where the naive square-root bin width would fall below one. These reviews
support the written arguments; they are not a claim of external peer review,
formal proof-assistant certification, or a literature priority guarantee.

## Numerical scope

The window calculation diagonalizes an (m+1)-by-(m+1) weighted Gram matrix,
using quadratic storage and a dense eigensolver. This avoids enumerating the
full 2^N-dimensional system for entropy evaluation, but it is a finite numerical
method, not a claimed optimal algorithm. Explicit local-record enumeration is
restricted to the small apparatus test because its size grows as D^N.

The robustness tests evaluate theorem coefficients; they do not search over
arbitrary noisy instruments. The universal exact and robust lower bounds, all
large-size statements, and the scope of every error model are justified by
the analytical proofs and their stated imported ingredients.
