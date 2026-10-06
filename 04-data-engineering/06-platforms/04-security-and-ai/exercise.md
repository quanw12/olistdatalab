# DE22 assignment

Implement validate_enrichment(payload,allowed_ids): accept only a dict with exactly id and label; id must be a nonblank string present in allowed_ids, label exactly standard or priority. Do not trim/alter the ID. Return a new dict; otherwise raise ValueError. Use fixed simulated responses, no paid model calls. Write ai-workflow.md with one suggested edge case, your verified result and a rejected bad suggestion. Write secrets.md explaining env/config, Git hygiene and handling an accidentally exposed credential.

## Deliverables

exercise.py, ai-workflow.md, secrets.md and changed-input tests.

## Reflection

What does this schema validator not establish?

Write your answer before opening expected.md. Keep teaching examples in scratch files; your final implementation belongs in the requested starter.

