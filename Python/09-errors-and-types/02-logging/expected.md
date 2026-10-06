# Expected results — Logging and observable failures

Details {'run_id':'r1','accepted':3,'token':'secret'} produce {'event':'complete','run_id':'r1','accepted':3}. The same object value is passed once to logger.info. Input remains unchanged.

When every included check passes, check.py prints PASS and the lesson folder name. A FAIL message points to the first unmet contract. A missing function means the exercise is not implemented yet.

## Reflection and answer key

Why configure log handlers at the entry point?

<details>
<summary>Reveal the reasoning after answering</summary>

Repeated configuration inside reusable functions can create duplicate handlers/output and makes library behavior depend on how often a function is called.

</details>
