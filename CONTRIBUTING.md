# Contributing

Begin with the [model](research/MODEL.md), [theorem](research/THEOREM.md), and
[proof map](research/PROOF_MAP.md). A useful scientific change identifies the
statement being affected, the exact assumptions, and the complete argument.
Provide a concrete counterexample for a failed implication or a derivation for
a strengthened bound. Preserve the distinction between an explicit detector's
performance and a lower bound over all admissible detectors.

For implementation changes, run the commands in [VERIFICATION](VERIFICATION.md).
Tests should check independently specified mathematical properties, not merely
repeat the implementation. State which input sizes and error regimes were
checked. Numeric agreement is evidence about the calculation; it does not
replace a proof of a universal quantifier.

For exposition changes, keep the specialist and [learning](docs/LEARNING.md)
routes consistent. Preserve load-bearing qualifications and primary attribution,
check local links, and inspect rendered mathematics. The
[30-milestone map](docs/MILESTONES.md) may change when the scientific story
changes, not in response to an individual learner's mistakes.

Use a focused branch and pull request. Explain the scientific or reader-facing
problem, the change, and the resulting behavior. Follow [AGENTS](AGENTS.md) for
repository scope and validation. The owner's original [MIT license](LICENSE)
applies to the repository; linked third-party works retain their own terms.
