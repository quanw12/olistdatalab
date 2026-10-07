# DE02 review checklist

The task's acceptance contract remains in the assignment. Attempt it before opening worked results or reflection explanations.

<details>
<summary>After your attempt — results and explanations</summary>

- Four documents exist and distinguish confirmed lab requirements from unknown production facts.
- Output grain is customer + UTC event day; source update time is not used as the business grouping day.
- b1 has two active orders totaling 2500 cents. After b2, latest active state has A and C, both for c1, totaling 2000 cents; B is deleted. Replaying the same changes does not add another 2000.
- The plan is small and dependency-aware. It includes baseline reproduction, independent verification and a handoff.
- Test cases detect actual wrong behaviors, including checkpoint/publication failure boundaries. “No exception” alone is not a success criterion.
- Handoff results are marked not executed. No pipeline implementation or stakeholder answer is fabricated.

<details><summary>Reflection explanation — reveal after answering</summary>

You can inspect code, fixtures, schema, existing tests and a reproducible error independently. Business metric meaning, source guarantees, currency policy, permitted access and required freshness may need the relevant owner's answer. State a lab assumption when permitted; do not silently convert it into a confirmed production fact.

</details>

</details>
