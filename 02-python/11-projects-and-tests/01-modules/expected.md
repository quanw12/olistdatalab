# Expected results — Imports, modules, and entry points

main([' hanoi ',' ',' hue ']) returns ['Hanoi','Hue']; main([]) returns []. Only direct script execution prints the list.

check.py prints PASS when all included cases succeed. Missing functions are expected until implemented.

## Reflection

Why should importing a module not run its pipeline?

<details>
<summary>Reveal reasoning after answering</summary>

Imports happen during tests, command discovery and scheduling. Side effects could write data before configuration or run control exists.

</details>
