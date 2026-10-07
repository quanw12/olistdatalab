# Help — Exceptions and deliberate validation

Attempt the smallest case and write its expected result first. Open one section only when you can name the obstacle; record the highest hint used in notes.md.

<details>
<summary>First hint</summary>

Separate input type, character format, conversion and range checks.

</details>

<details>
<summary>Detailed approach</summary>

Use isinstance(value, str), value.strip(), isascii(), and isdecimal(). Only call int after checking the format. A failed business rule should raise ValueError explicitly. The ordinary conversion exception may propagate for exceptionally long digit strings; it already has the required ValueError type. Keep TypeError for non-text input.

</details>

<details>
<summary>Troubleshooting</summary>

If True passes, your type guard is too broad. If '-1' is parsed first, you are accepting a format outside the stated contract.

For a failed assertion, compare the input, expected type and value, and any side effect. Rerun the checker after one focused change. If stuck, read the test case in check.py; it is an executable specification.

</details>
