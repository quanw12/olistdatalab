# LAB02 — Progressive help

Attempt the smallest case and write its expected result first. Open one section only when you can name the obstacle; record the highest hint used in notes.md.

<details>
<summary>After an attempt — supporting explanation</summary>

Attempt the task before opening each hint. These hints describe the method; implement the final solution yourself.

### Hint 1 — validate structure before conversion

Check payload is a dict, validate api_version, then choose the appropriate nested path. A missing key is an external contract error, not zero stock.

### Hint 2 — branch only at the boundary

Extract the two candidate fields for the selected version. For v1 strip and validate digits before int(); for v2 validate type before comparisons.

### Hint 3 — converge on one result

Both branches should reach the same SKU/range validation and return two named fields. Write one test per version plus a malformed case for each.

[Return to the assignment](exercise.md)

</details>
