# Expected results — Dependency injection and mocked HTTP

{'count':0} -> 0. Missing, negative, Boolean and string counts fail. A status failure prevents JSON parsing.

check.py prints PASS when all included cases succeed. Missing functions are expected until implemented.

## Reflection

What does a passing mocked API test not prove?

<details>
<summary>Reveal reasoning after answering</summary>

It cannot verify real authentication, network connectivity, actual provider schema or service availability.

</details>
