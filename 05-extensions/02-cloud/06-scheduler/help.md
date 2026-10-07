# CL06 — Progressive help

Attempt the smallest case and write its expected result first. Open one section only when you can name the obstacle; record the highest hint used in notes.md.

<details>
<summary>After an attempt — supporting explanation</summary>

Attempt the task before opening each hint. These hints describe the method; implement the final solution yourself.

### Hint 1 — validate components separately

Use full regex matches on each string. For email, split at @ and require the exact expected project domain.

### Hint 2 — match the API, not a website URL

Build the v2 job :run endpoint. Put the email under oauthToken, not oidcToken.

### Hint 3 — test the real caller

Run the scheduler trigger, inspect Cloud Run execution/logs, then pause the owned schedule. Do not infer success only from creating the scheduler resource.

[Return to the assignment](exercise.md)

</details>
