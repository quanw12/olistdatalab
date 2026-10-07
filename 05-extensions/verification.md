# Author verification and evidence limits

[Course](README.md) · [Checks](checks/README.md) · [Sources](sources.md)

Prepared/checked October 7, 2026. This reports author validation, not learner completion. All 32 extension progress entries remain unchecked. Days 1–11 and unfinished Day 12 stay in their existing course locations.

## Executed offline checks

| Check | Result |
|---|---|
| Private reference implementations, outside the study repository | 25 contracts passed, 270 assertions |
| Unfinished student starters | All 25 checked starters rejected as intended |
| Deliberately flawed implementations | 15/15 rejected: join fanout, lost final window, partial commit, retry misclassification, bool config, wrong token type, extra chunk, negative cosine clamp, ignored equal-revision digest, premature metric slicing, skipped validation, unsafe offsets, early sink commit, full-before delete assumption and resurrected deletes |
| SQLite/FTS5 | Actual isolated in-memory queries, migration, lexical ranking, transaction rollback/replay and constraints executed |
| Bounded enrichment workload | 20,000 rows/400 dimension entries; baseline and reference outputs matched; timing and cProfile executed |
| Prior course preservation | All 933 files in the current pre-edit course snapshot remained byte-identical |
| Material structure | 32 lessons, each with guide/concepts/assignment/help/acceptance/notes, commit commands and self-review reasoning |
| Python parsing | 34 new source files and 22 teaching examples parsed |
| PowerShell parsing | 80 new command blocks parsed without syntax errors |
| Compose | docker compose config --quiet passed; corrected CONNECT_ replication settings checked against the image entrypoint |
| Dependencies | Four pinned direct wheels downloaded for the author Windows/Python 3.13 environment; registry image tags/digests checked |

The enrichment baseline took about 0.49s and the private reference about 0.014s in one author run. These are observations, not an acceptance threshold or promised performance on your machine. Your submission needs its own profile/measurement and correctness evidence.

## Not executed during preparation

No GCP resources/accounts/billing were provisioned and no cloud load/job/scheduler/IAM enforcement was demonstrated. No Kafka/Connect/PostgreSQL stack ran: the installed Docker client could validate Compose, but its Linux engine was unavailable. No real embedding model was downloaded/executed. Direct wheel availability is not a full dependency install/lock or a live SDK test.

Seven lessons (LAB08, CL01, CL08, AI08, ST01, ST07, ST08) use manual concept/integration evidence. Their checklists are prepared; their student implementations and live demonstrations remain your work. The CLI examples describe target interfaces that you implement before running.

Offline contracts prove supplied cases only. Add your own changed-input regressions. Real cloud operation, model quality, source capture, broker acknowledgement and consumer restart require the separately described evidence. The local transaction examples do not establish distributed exactly-once semantics or production-scale operations.

## Final navigation check

All 2,636 active course/local links passed the final navigation check. Use the master roadmap for overall order and each track README for its eight units. Keep source/check fixtures unchanged; private reference implementations are not placed into your student files.
