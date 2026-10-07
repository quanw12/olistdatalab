# CL06 — Acceptance and evidence

The task's acceptance contract remains in the assignment. Attempt it before opening worked results or reflection explanations.

<details>
<summary>After your attempt — results and explanations</summary>

For a valid project/region/job/email, the target contains POST, e30=, application/json and oauthToken. A slash in job or an email belonging to another project fails. Live evidence shows the intended job actually ran and explains stable input identity and schedule pause.

## Reflection

1. Why does this endpoint need OAuth?

2. What could two simultaneous executions do to publication?

<details>
<summary>After your reflection: compare the reasoning</summary>

The target is a Google API endpoint, which uses the documented OAuth flow. Overlapping writers can race staging/state/report publication even with one task each; stable batch identities and an explicit concurrency policy are necessary.

</details>

</details>
