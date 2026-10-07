# Help — Imports, modules, and entry points

Attempt the smallest case and write its expected result first. Open one section only when you can name the obstacle; record the highest hint used in notes.md.

<details>
<summary>First hint</summary>

Keep transformation in main and printing under the guard.

</details>

<details>
<summary>Detailed approach</summary>

Use from text_rules import normalize_city. Loop through arguments, normalize, and append nonempty values. sys.argv[0] is the script path; actual arguments begin at index 1. An importable function should receive inputs explicitly rather than reading global sys.argv itself.

</details>

<details>
<summary>Troubleshooting</summary>

If a checker waits for input, input() is probably at module scope. A ModuleNotFoundError may indicate an incorrect sibling filename.

Read the first failing check, compare input/type/output and side effects, then make one focused change. The checker is an executable specification.

</details>
