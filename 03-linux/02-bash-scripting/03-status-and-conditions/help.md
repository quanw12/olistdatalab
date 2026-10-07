# Help — Exit status, conditions and deliberate failure

Attempt the smallest case and write its expected result first. Open one section only when you can name the obstacle; record the highest hint used in notes.md.

<details>
<summary>First hint</summary>

The final successful command can determine the wrapper's status.

</details>

<details>
<summary>Detailed approach</summary>

Check $# before reading $1. Test [[ -f "$1" && -r "$1" ]]. For failure use printf to >&2, then exit the chosen code. For success print ready only. Strict mode is optional; expected outcomes still need explicit branches. Run as a normal account so permission behavior is meaningful.

</details>

<details>
<summary>Troubleshooting</summary>

An error message alone does not fail a script. Using only -e allows directories and violates the input contract.

</details>
