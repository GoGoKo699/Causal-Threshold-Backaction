# Contributing

Begin with the [model](science/model.md), [theorem](science/entropy_law.md), and
[proof map](science/proof_map.md). A useful scientific change identifies the
statement being affected, the exact assumptions, and the complete argument.
Provide a concrete counterexample for a failed implication or a derivation for
a strengthened bound. Preserve the distinction between an explicit detector's
performance and a lower bound over all admissible detectors.

For implementation changes, run the commands in [VERIFICATION](verification/README.md).
Tests should check independently specified mathematical properties, not merely
repeat the implementation. State which input sizes and error regimes were
checked. Numeric agreement is evidence about the calculation; it does not
replace a proof of a universal quantifier.

For exposition changes, keep the specialist and [learning](learning/WATROUS_BRIDGE.md)
routes consistent. Preserve load-bearing qualifications and primary attribution,
check local links, and inspect rendered mathematics. The
[30-milestone map](learning/MILESTONES.md) follows the scientific story. Revise
its targets and dependencies when a substantive scientific change requires it.

Use a focused branch and pull request. Explain the scientific or reader-facing
problem, the change, and the resulting behavior. Follow [AGENTS](AGENTS.md) for
repository scope and validation. The owner's original [MIT license](LICENSE)
applies to the repository; linked third-party works retain their own terms.
