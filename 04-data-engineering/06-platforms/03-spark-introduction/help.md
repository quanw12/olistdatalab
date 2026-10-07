# Help — Spark schemas, plans and distributed-processing decisions

Attempt the smallest case and write its expected result first. Open one section only when you can name the obstacle; record the highest hint used in notes.md.

<details>
<summary>First hint</summary>

An action's output and a plan are different evidence.

</details>

<details>
<summary>Detailed approach</summary>

The inspected latest installation docs require Java 17 or later; verify the exact selected release rather than treating a latest page as a pin. Use explicit schema and built-in sum. Do not install this into the dbt environment. Check NULL behavior and join keys. Record before/after row counts. Explain which operation introduces a shuffle and how a skewed key could concentrate work. Keep collect limited to tiny demonstrated output.

</details>

<details>
<summary>Troubleshooting</summary>

A Java gateway error is environment setup, not a SQL logic failure. local[2] is two local worker threads, not two cluster machines.

</details>
