# Hints for DE02

Attempt the smallest case and write its expected result first. Open one section only when you can name the obstacle; record the highest hint used in notes.md.

<details>
<summary>First hint</summary>

Underline each ambiguous noun: daily, customer, total, reject, rerun, fails. Write an observable meaning using the lab clarification card.

</details>

<details>
<summary>Document structure</summary>

In task.md use Goal / Inputs / Outputs and grain / Confirmed requirements / Assumptions / Open questions / Acceptance / Out of scope. A requirement such as “reliable” needs a behavior: identical replay should leave counts and amounts unchanged.

In plan.md separate validation, durable latest state, the reporting transformation and output publication. A checkpoint and a report file are different resources; a database commit does not automatically publish a file. DE11 handles that recovery boundary.

For tests, choose a defect each row catches. A delete case detects resurrection; a correction case detects append-only totals; an equal-version conflict detects arbitrary tie-breaking. Use a fixed clock for freshness questions. Include a failure before durable commit and one after commit/before publication.

Make the handoff template easy to fill after implementation: problem / behavior / run command / actual checks / data assumptions / remaining limits. Leave results unclaimed now. Keep questions short enough that a teammate can answer them.

</details>
