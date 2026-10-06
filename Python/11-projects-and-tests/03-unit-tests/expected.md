# Expected results — Tests that detect meaningful defects

The correct callable passes; four defective variants fail. At least four test cases are required.

check.py prints PASS when all included cases succeed. Missing functions are expected until implemented.

## Reflection

Why test the tests against bad implementations?

<details>
<summary>Reveal reasoning after answering</summary>

It shows they distinguish the behavior they claim to protect. Merely running without errors is not sufficient evidence.

</details>
