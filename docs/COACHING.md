# Coaching protocol

Use the settled [30-milestone map](MILESTONES.md). Its two phases and understanding
targets describe the project and remain the same for every learner. Adapt the
explanations, examples, and remediation within a milestone. This file specifies
how to run an explicitly requested tutorial; repository maintenance does not
start a lesson or mark any milestone complete.

## Every round: Revise → Learn → Test

**Revise** supplies the relevant definitions, notation, assumptions, and earlier
results. Include it on the initial attempt, every learning round, and every retry.
**Learn** explains the idea or corrects a misconception. **Test** asks for an
inference, interpretation, or changed-condition prediction. Keep preparation
compact on a challenge attempt and avoid disclosing its answers.

All questions have **four selectable options and exactly one correct answer**.
Prefer native clickable quiz controls. Plain Markdown lists are not functioning
answer controls. If selection controls are unavailable, briefly state that and
use a minimal option-letter fallback. Do not require free-text derivations.

Questions test concepts with at most minimal mental calculation. Include
physical meaning, resources, causal conditions, examples, and limitations where
they belong. Supply necessary prerequisites, use plausible conceptual
distractors, and repair ambiguous or unreadable questions without counting the
presentation problem as a conceptual error.

## One milestone, one challenge

The initial attempt contains a compact Revise → Learn introduction followed by
a **two-question challenge**. Passing requires both answers to be correct.
The whole challenge is one Test, even when its questions are presented separately.

The working presentation default is one question at a time, with correctness
judgments and explanations withheld until the full challenge is answered.
Finish the set even after a wrong answer, then give the result and explain the
misconceptions. This avoids revealing later answers through earlier feedback.

## Learning after a failed challenge

Conduct **1–3 learning rounds**, guided by the milestone's conceptual load and
the actual errors. Each round has Revise → Learn → Test with **one question**.
Give correctness feedback and an explanation **immediately after each learning
answer**. Correct a wrong final learning answer before moving to a retry.

This is a bounded block of teaching, not a second pass requirement. A learning
test does not pass the milestone. A wrong learning answer does not increase the
next challenge size. Address remaining misconceptions in the retry preparation;
do not silently add an unlimited remedial loop.

## Retrying the challenge

Only a completed failed challenge increases the next challenge size. If f
challenges have failed in the current milestone, the next size is min(2+f, 6).

| Failed challenges | Next challenge | Passing condition |
|---:|---:|---|
| 0 | 2 questions | All correct |
| 1 | 3 questions | All correct |
| 2 | 4 questions | All correct |
| 3 | 5 questions | All correct |
| 4 or more | 6 questions | All correct |

Each failure is followed by another 1–3-round learning block and a fresh
challenge. At six questions the size stays at six; there is no automatic pass,
lowered threshold, or seventh question. Retry questions are fresh applications,
not the same questions with permuted answer labels. Correct responses from
different failed attempts cannot be pooled into a pass.

An interrupted challenge is unfinished, not automatically failed. After a pass,
the next milestone starts with a new two-question challenge and zero failures.

## Session state and completion

Track the current milestone, phase (challenge or learning), failed-challenge
count, question position, pending answers, and completed milestone IDs. Keep
these learner records separate from the common map. Do not commit personal
attempts during ordinary research maintenance. Do not reinterpret older answers
under a newly settled map without evidence.

Passing all 30 milestones completes the project-understanding tutorial, and the
tutor should state that explicitly. The shortest route is **60 challenge
questions**. Repeated failures can increase the total without a fixed maximum.
Do not append another examination or reset completed milestones to prolong it.

Completion records the conceptual evidence gathered here. It does not prove the
research independently, certify mastery of every specialist detail, or guarantee
readiness for every possible collaborator question. Accepting an explanation,
requesting continuation, or completing the repository does not count as a pass.
