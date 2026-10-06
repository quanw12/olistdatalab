# Day 30 — Package the portfolio and explain your decisions


## A portfolio demonstrates understanding

The capstone is a weather data pipeline with reproducible fixtures, optional live extraction, validation/quarantine, version-aware loading, a dimensional mart, orchestration, tests and reporting. Your value is in being able to explain and verify those choices, not just naming tools.

This final day finishes presentation and checks. Do not start another framework. A 30-day foundation does not guarantee internship readiness; it gives concrete work to discuss and exposes the skills to deepen next.

## Prepare a short demo

Plan a three-to-five-minute explanation: problem and architecture; fresh fixture load; replay/correction; one handled failure; report and limitations. Have an offline path ready. Display only relevant commands and sanitized output. Do not depend on the live API returning a particular temperature.

A clear spoken explanation uses cause and effect: 'The provider can resend an observation, so this key and version comparison make replay safe.' Avoid claiming exactly-once processing when the implementation actually achieves idempotent effects from retries.

## Reproducible dependency records

Keep a small requirements list describing intentional dependencies. Also record exact versions from the environment that passed rehearsal. pip freeze captures installed versions, including transitive packages; a dump of an unrelated global environment is not a clean project dependency design.

~~~powershell
python --version
python -m pip freeze
git diff --check
git status
~~~

Review the freeze output before saving a lock/snapshot file. Explain which Python/OS route was tested. Docker tags may move; record image details if you claim exact image reproducibility.

## Final review rubric

Score each area with evidence, not confidence:

| Area | Points |
|---|---:|
| Reproducible setup and honest documentation | 20 |
| Correct identity/time/version/transaction behavior | 25 |
| Validation, tests and failure recovery | 25 |
| Clear analytics and observable runs | 15 |
| Explanation of decisions and limitations | 15 |

A score is a self-review aid, not an industry certificate. Fix a missing core behavior before polishing screenshots.

## What to deepen after this course

Python: functions/modules, exceptions, typing, iterators, context managers, packaging, profiling and testing. SQL: query plans/indexes, complex windows, transactions/isolation, incremental transformations and modeling changes. Engineering: Linux, Git collaboration, API contracts, observability, cloud access/cost controls and orchestration operations. Later ML: leakage-free feature pipelines, evaluation and reproducibility. Spark becomes useful when a measured workload needs distribution, not because a roadmap lists it.

Write these gaps down; we will create the deeper study track separately after this foundation is complete.
