# Expected results — Paths, context managers, and safe file replacement

The task's acceptance contract remains in the assignment. Attempt it before opening worked results or reflection explanations.

<details>
<summary>After your attempt — results and explanations</summary>

Writing {'city':'Huế'} yields valid UTF-8 JSON. Writing a set or NaN raises a serialization error and leaves an existing file untouched. No helper temporary files remain after success.

When every included check passes, check.py prints PASS and the lesson folder name. A FAIL message points to the first unmet contract. A missing function means the exercise is not implemented yet.

## Reflection and answer key

Why must the temporary file be a sibling, and what guarantee is still missing?

<details>
<summary>Reveal the reasoning after answering</summary>

Same-directory replacement avoids a cross-filesystem move. It does not make multiple separate output files or a database-plus-file update one atomic transaction.

</details>

</details>
