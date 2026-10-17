# Working on Causal Threshold Backaction

This repository contains the scientific exposition and finite verification for
*The Backaction Cost of Causal Threshold Measurements*. Begin with README.md,
science/model.md, science/entropy_law.md, and science/proof_map.md. Current user
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

The canonical exact arguments are science/causal_converse.md,
science/window_entropy.md, and science/fluctuation_regimes.md. The full
instrument is science/distributed_apparatus.md; general-instrument errors are
in science/robustness.md. science/interpretation.md connects their physical
meaning and gives the parity comparison. Keep references/RELATED_WORK.md and
references/references.bib aligned with the claims.
Credit inherited causal measurement frameworks, noisy translated meters, GHZ-like
apparatus designs, fluctuation scales, and imported information inequalities.

Write the repository as a complete bounded scientific work. Keep one
authoritative home for each result in the topic-based science/ account, with
connected introductions, proof dependencies, and physical interpretation.
Keep learning/, references/, and verification/ easy to navigate from README.md
and llms.txt. Retain useful implementation structure and reproduction commands.
Use GitHub-supported mathematical syntax: inline $`...`$ and fenced math blocks.
Write named operators with supported roman notation such as `\mathrm{Tr}\,` and `\mathrm{Var}`.
Use `\lt` for strict less-than comparisons in fenced math; literal `<` can
interfere with GitHub's processing of otherwise valid formulas.
In Markdown table formulas, use `\lvert`/`\rvert` or `\lVert`/`\rVert` instead
of pipe characters, which the table parser can treat as cell separators.
Do not introduce custom TeX macros. Inspect the actual hosting renderer for
math-heavy changes; source checks alone cannot certify display quality.
Keep private publication assessments and exploration transcripts out of the
reader-facing files. Preserve the owner's license and exact Purpose and contact
paragraph unless the owner requests a change.

## Learning

learning/MILESTONES.md is the settled, project-intrinsic map of exactly M01–M30:
14 background/preliminaries milestones and 16 narrative/innovation milestones.
Preserve its questions, targets, dependencies, conceptual connections, and
scientific source pointers. learning/WATROUS_BRIDGE.md uses one educational
anchor, Watrous's *The Theory of Quantum Information*.
learning/WORKED_EXAMPLES.md bridges the physical task to the theorem.
Personal teaching procedures and learner records belong outside this repository.

## Validation and repository scope

Run from the repository root:

```sh
python -m unittest discover -s tests -v
OPENBLAS_NUM_THREADS=1 OMP_NUM_THREADS=1 python tools/verify.py --output build/verification
python tools/check_repository.py
```

For figure changes, add `--figures assets` to the verification command and
inspect the generated image. See verification/README.md for the assertion coverage and
limits. Record only checks actually performed.

Work on a branch, inspect the actual diff, resolve scientific and validation
findings, and merge when authorized. Recheck the remote base and head before
merging; reconcile concurrent changes instead of overwriting them. A scoped
authorization already given in the session does not need a second confirmation.
No repository file grants access or write permission to another project.
Other repositories used as references remain read-only in this project.
