# LAB04 — Progressive help

Attempt the smallest case and write its expected result first. Open one section only when you can name the obstacle; record the highest hint used in notes.md.

<details>
<summary>After an attempt — supporting explanation</summary>

Attempt the task before opening each hint. These hints describe the method; implement the final solution yourself.

### Hint 1 — normalize both ends

Parse, inspect tzinfo/utcoffset, convert to UTC, then inspect hour/minute/second/microsecond. Reject rather than guessing a timezone.

### Hint 2 — stop at the actual end

Maintain a cursor. The next boundary is the smaller of cursor + timedelta(days=chunk_days) and end.

### Hint 3 — prove coverage

Append one tuple, advance the cursor to that tuple's end, and continue while cursor < end. Verify first start, last end and adjacency of every pair.

[Return to the assignment](exercise.md)

</details>
