# Expected results — CLI options, configuration, and environments

--input a.csv gives limit=100; --limit 0 exits. {'source':' fixture ','batch_size':2,'token':'x'} returns only source='fixture' and batch_size=2.

check.py prints PASS when all included cases succeed. Missing functions are expected until implemented.

## Reflection

Why install with the selected interpreter's -m pip?

<details>
<summary>Reveal reasoning after answering</summary>

It ensures the package goes into that interpreter's environment instead of a different Python installation.

</details>
