# 21 · Access control, reproducibility and releases

> **Theory notes:** [[Security and Governance]] · [[Delivery and Reproducibility]] · [[Python Environments and Packaging]] · **Route:** [[Roadmap]] · **Labs:** [[Labs Guide]]

**Week:** 23 · **Mandatory** · **Prerequisites:** 10, 20

## Goal

Someone else can deploy from the repo; analysts can read only the data they are allowed to; every change has a rollback path.

## Lab · `labs/21-delivery` (create it in the code repo)

1. Separate sample/dev/real with environment variables; sample must never overwrite real.
2. Postgres reader/writer roles. Connect **as the reader** to prove that SELECT on the mart works and that INSERT and SELECT on raw are denied. Re-check after a publish: drop/recreate can lose grants and indexes.
3. Put a fake PII column into raw, drop or mask it before the mart and the logs. Only send data you have permission to share to hosted AI.
4. Record Python, dependencies, dbt/adapter, image tag/digest, and Java if you use Spark. Save a lock/constraints file from a clean environment that ran successfully.
5. Clean clone: create a venv, install from the lock, run tests, dbt on sample, export. Record the OS you actually tested; do not assume Windows results hold on Linux.
6. Release v1; add a backward-compatible column; try a breaking change and write the consumer migration plan.
7. Roll back code/configuration; migrated data needs its own restore or forward fix. Prove that the reader still uses a valid dataset.

## Done when

- [ ] Permission tests cover both allowed and denied actions.
- [ ] A fresh clone reproduces the run with a version manifest.
- [ ] The PR states problem, change, verification and rollback; it is reviewed, or self-reviewed after 48 hours.
