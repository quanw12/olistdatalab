# Expected results — CSV, JSON, JSON Lines, and schema boundaries

Reading the shared orders.csv returns eight raw dictionaries. A header-only valid CSV returns []. Quoted commas round-trip. Two supplied rows produce two JSONL lines; writing [] again clears them.

When every included check passes, check.py prints PASS and the lesson folder name. A FAIL message points to the first unmet contract. A missing function means the exercise is not implemented yet.

## Reflection and answer key

Why keep CSV strings separate from typed clean records?

<details>
<summary>Reveal the reasoning after answering</summary>

Parsing the container format does not establish business validity. A separate transformation can preserve raw values, apply explicit types, and record precise rejection reasons.

</details>
