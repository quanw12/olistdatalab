# LAB05 — Acceptance and evidence

The task's acceptance contract remains in the assignment. Attempt it before opening worked results or reflection explanations.

<details>
<summary>After your attempt — results and explanations</summary>

Starting p01=10, p02=5: [{"item_id":"p01","delta":-3},{"item_id":"p02","delta":2}] produces 7/7, total 14, one ledger row. Replay leaves 7/7 and one ledger. Crash after the first adjustment leaves 10/5 and no ledger; retry yields 7/7. Same batch ID with altered changes fails without modifying either table.

## Reflection

1. Why must the ledger and data share a commit?

2. What happens if a caller gives you an active transaction?

<details>
<summary>After your reflection: compare the reasoning</summary>

If data and ledger commit separately, retry may repeat a write or skip missing work. An active caller transaction must be rejected without rolling it back or committing it. The borrowed connection stays open; your function owns only the transaction it began.

</details>

</details>
