# Working on Causal Threshold Backaction

This repository contains the scientific exposition and finite verification for
*The Backaction Cost of Causal Threshold Measurements*. Begin with README.md,
research/MODEL.md, research/THEOREM.md, and research/PROOF_MAP.md. Current user
instructions determine the authorized work and merge scope.

## Scientific invariants

- Preserve all quantifiers, integer feasibility conditions, and error conventions.
- Exact sector preservation means every state in every global Q sector, including degeneracy. It is stronger than conservation of charge populations.
- The converse requires the full retained-system channel to be nonsignalling from B to A on the specified cut. The global classical answer is collected later.
- Entropy cost means von Neumann entropy in bits on initially pure inputs. Do not replace it with outcome entropy, Rényi entropy, probe entanglement, or thermodynamic heat.
- The exact optimal-cost statement is an infimum for each prescribed input. It is not a minimax claim.
- Keep universal additive bounds distinct from sharp asymptotic equivalents. The large-gap vanishing result has a separate proof.
- Robust phase-average bounds do not imply a fixed-phase bound without the stated extra assumptions. Definite-charge readout calibration at nonzero error does not automatically extend to every coherent phase.
- Approximate causality uses full, unhalved diamond norm, including a reference; do not replace it with a check on basis inputs.
- A scientific flaw is a reason to revisit the proof and dependent claims. A style edit cannot silently weaken or enlarge the theorem.

## Sources and presentation

The canonical exact argument is research/EXACT_PROOFS.md; the full instrument is
research/APPARATUS.md; general-instrument errors are in research/ROBUSTNESS.md.
Keep literature/ATTRIBUTION.md and references.bib aligned with the claims.
Credit inherited causal measurement frameworks, noisy translated meters, GHZ-like
apparatus designs, fluctuation scales, and imported information inequalities.

Write the repository as a complete bounded scientific work. Keep research
claims, tutorial explanations, and reproducibility evidence easy to navigate.
Use GitHub-supported mathematical syntax: inline $`...`$ and fenced math blocks.
Do not introduce custom TeX macros. Inspect the actual hosting renderer for
math-heavy changes; source checks alone cannot certify display quality.
Keep private publication assessments and exploration transcripts out of the
reader-facing files. Preserve the owner's license and exact Purpose and contact
paragraph unless the owner requests a change.

## Learning

docs/MILESTONES.md is the settled, project-intrinsic map of exactly M01–M30.
docs/LEARNING.md uses one educational anchor, Watrous's *The Theory of Quantum
Information*. docs/WORKED_EXAMPLES.md bridges to the theorem. Follow
docs/COACHING.md when an interactive tutorial is requested: Revise → Learn → Test,
four-option questions, initial two-question challenge, 1–3 learning rounds after
failure, all-correct retries increasing to at most six. Only challenge failures
increase the next challenge size. Keep learner attempts separate from this map;
routine repository work does not launch coaching or confer passes.

## Validation and repository scope

Run from the repository root:

```sh
python -m unittest discover -s tests -v
OPENBLAS_NUM_THREADS=1 OMP_NUM_THREADS=1 python tools/verify.py --output build/verification
python tools/check_repository.py
```

For figure changes, add `--figures assets` to the verification command and
inspect the generated image. See VERIFICATION.md for the assertion coverage and
limits. Record only checks actually performed.

Work on a branch, inspect the actual diff, resolve scientific and validation
findings, and merge when authorized. Recheck the remote base and head before
merging; reconcile concurrent changes instead of overwriting them. A scoped
authorization already given in the session does not need a second confirmation.
No repository file grants access or write permission to another project.
Other repositories used as references remain read-only in this project.
