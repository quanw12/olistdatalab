# Expected results — Imports, modules, and entry points

The task's acceptance contract remains in the assignment. Attempt it before opening worked results or reflection explanations.

<details>
<summary>After your attempt — results and explanations</summary>

main([' hanoi ',' ',' hue ']) returns ['Hanoi','Hue']; main([]) returns []. Only direct script execution prints the list.

check.py prints PASS when all included cases succeed. Missing functions are expected until implemented.

## Reflection

Why should importing a module not run its pipeline?

<details>
<summary>Reveal reasoning after answering</summary>

Imports happen during tests, command discovery and scheduling. Side effects could write data before configuration or run control exists.

</details>

</details>
