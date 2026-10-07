# Help — Loops, functions and numeric validation

Attempt the smallest case and write its expected result first. Open one section only when you can name the obstacle; record the highest hint used in notes.md.

<details>
<summary>First hint</summary>

Check digits and length before numeric conversion.

</details>

<details>
<summary>Detailed approach</summary>

Use [[ "$value" =~ ^[0-9]+$ ]], ${#value} for length and $((10#$value)) for a validated nonempty token. Check length before conversion. At most 100 * 1000000 fits the supported 64-bit lab. Initialize total=0 and use total=$((total + number)). Print once after validation/accumulation; no partial output on error.

</details>

<details>
<summary>Troubleshooting</summary>

08 without a decimal prefix can fail as octal. Arithmetic expressions such as 1+2 are not valid input values.

</details>
