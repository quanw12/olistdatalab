# DE03 expected behavior

The task's acceptance contract remains in the assignment. Attempt it before opening worked results or reflection explanations.

<details>
<summary>After your attempt — results and explanations</summary>

The original buggy script prints {" c1 ": 10, "c1": 20, "c2": 5}. It uses the raw whitespace-containing ID and replaces a customer's previous amount. The provided small fixture visibly demonstrates the normalization defect; a regression input with identical repeated keys also exposes overwrite.

The correct result for data.json is {"c1": 30, "c2": 5}. Empty input returns {}. Reordered valid rows and non-adjacent repeated customers keep the same totals. Zero amounts remain valid, and input rows/dictionaries are unchanged.

Required evidence:

- A debugger trace showing the key and aggregate state before/after writes.
- At least one meaningful failing regression test against buggy.build_report, then passing tests against exercise.build_report.
- PASS from the DE03 checker, plus your own changed-input case.
- A real profile observation for five calls over 50,000 rows; do not copy a made-up duration. Each call produces 100 customers and a 350000-cent total.
- A bug report with cause, repair, verification and the prevalidated-input scope.

<details><summary>Reflection explanation — reveal after answering</summary>

A reproduction confirms the symptom and gives you a way to distinguish causes. A failing regression test captures the intended behavior and can reject an incomplete repair later. Making a change without either can hide the original issue, create unrelated changes or leave another variation broken.

</details>

</details>
