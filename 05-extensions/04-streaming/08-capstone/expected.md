# ST08 — Acceptance and evidence

The task's acceptance contract remains in the assignment. Attempt it before opening worked results or reflection explanations.

<details>
<summary>After your attempt — results and explanations</summary>

Checklist: both real paths run; active total 13 after updates/delete; unfamiliar M4 raises it to 15; synthetic replay/stale/conflict rules hold; CDC deletion survives restart; sink/ledger rollback verified; poison data is durably quarantined; environment failure does not advance offset; runbook states limits and source epoch; owned services stop. Each live claim has actual commands/results.

## Reflection

1. Which rules can the two adapters safely share?

2. What would need redesign for several CDC partitions or source epoch replacement?

3. How would a reviewer reproduce the restart proof?

<details>
<summary>After your reflection: compare the reasoning</summary>

Transport validation/logging/manual acknowledgement can share explicit interfaces; domain revision semantics cannot be silently shared with native CDC. More partitions/source epochs require a documented ordering and state-rebuild strategy. A reviewable restart proof includes real positions, pre/post state and exact rerun commands.

</details>

</details>
