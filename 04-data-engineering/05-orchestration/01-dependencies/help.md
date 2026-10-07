# Help — Dependency graphs, parameters and run boundaries

Attempt the smallest case and write its expected result first. Open one section only when you can name the obstacle; record the highest hint used in notes.md.

<details>
<summary>First hint</summary>

Ready means prerequisites satisfied, not just a smaller name.

</details>

<details>
<summary>Detailed approach</summary>

Copy prerequisite sets; validate names exist. Repeatedly sort currently ready tasks and choose the first, then mark completed. If tasks remain but none are ready, raise a cycle error. In the real pipeline, quality failure blocks publish. Keep cursor commit in the loader's transaction.

</details>

<details>
<summary>Troubleshooting</summary>

Insertion order is not execution order. A cycle must raise rather than hang.

</details>
