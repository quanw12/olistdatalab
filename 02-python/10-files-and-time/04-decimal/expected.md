# Expected results — Decimal parsing and exact money

The task's acceptance contract remains in the assignment. Attempt it before opening worked results or reflection explanations.

<details>
<summary>After your attempt — results and explanations</summary>

'20.50' -> 2050; ' 1.2300 ' -> 123; '0' -> 0; '1000000' -> 100000000. '1.001', '-0.01', 'NaN', 'Infinity', 'oops', '' and '1000001' fail.

When every included check passes, check.py prints PASS and the lesson folder name. A FAIL message points to the first unmet contract. A missing function means the exercise is not implemented yet.

## Reflection and answer key

Why reject sub-cent values rather than silently round them in this exercise?

<details>
<summary>Reveal the reasoning after answering</summary>

The contract chooses exact source precision. Silent rounding would alter data while reporting it as accepted. A different business rounding rule must be explicit and tested.

</details>

</details>
