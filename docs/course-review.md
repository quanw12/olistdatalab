# Course review — 7 October 2026

[Home](../README.md) · [Roadmap](../roadmap.md)

## Findings and changes

Most central intern foundations were present. Teaching depth was uneven: early
tutorials sometimes supplied the task algorithm, while later lessons exposed
important APIs only in help. The revision keeps syntax/contracts visible and
reveals approaches/results after an attempt. Difficulty labels are teaching
estimates, not measurements of your performance.

- Reviewed 167 existing lesson units; added two, for **169 across five courses**.
- Preserve completed Days 1–11, learner implementations/fixtures and unfinished Day 12.
- Shorten Day 12 into grain/key concepts and unrelated SQL shapes instead of a
  worked weather model/report. Correct its stale stash-only description.
- Remove answer-shaped set/dictionary, PostgreSQL, incremental dbt and retrieval
  examples. Keep required syntax visible and stronger help available after effort.
- Remove repeated generic Python hint/debug paragraphs in favor of the shared
  study method. Shorten Linux CI help; show multiline YAML in the lecture.
- Label Learn/Apply/Integrate/Assess. Add focused variations and four Python
  checkpoints, so repeated weather practice is not mistaken for transfer.
- Retain Part 5 as later specialization. CL04's offline query is a refresher;
  deployment/MERGE is new. LAB03's one-line ALTER is only its syntax drill;
  compatibility/rollback evidence is required.
- Add DE27 source profiling/catalog/lineage and DE28 native backup/verified restore.
  The former applications lesson becomes DE29. Completed day numbering is unchanged.

## Coverage and boundaries

Python, SQL, Git/review, Linux, modeling, APIs, ETL/ELT, state, orchestration,
testing/quality, containers, warehouse work, observability and handoff are core.
Discovery and verified restoration now have concrete exercises rather than being
implied. Cloud deployment/streaming/ML-specific data remain optional or later work.

Use Gates A–G and fresh role eligibility requirements. A BI-heavy role may need
its dashboard tool; a Spark/cloud-heavy role may need the optional track. Course
completion cannot establish independent competence in every company system.

## Research basis

Employer pages, job searches, community discussion and learning resources were
inspected. Hard technical claims were verified with primary documentation.
[TCData's intern/trainee description](https://tcdata.vn/career/intern-trainee-data-engineer/)
emphasizes SQL, scripting, modeling/testing and communication.
[Data Impact](https://dataimpact.vn/recruiter/detail/intern-data-engineer) includes
validation, requirements, governance/privacy. These undated pages do not establish
currently open vacancies.

[Pizza Hut's 2026 description](https://pizzahut.talent.vn/job/hcm-data-engineer-intern-53453)
includes Python/SQL, ETL/modeling and documentation/governance; its June deadline
has passed. [Norrin's integration internship](https://careers.norrin.com/o/azure-data-integration-engineer-intern-1?lang=en)
mentions programming/SQL, English and problem solving; its August 2026 start is
past and present availability is unconfirmed. These examples are not a
representative market survey or guaranteed hiring syllabus.

[Community entry-project discussion](https://www.reddit.com/r/dataengineeringjobs/comments/1wwq9xd/fresher_data_engineer_what_2_projects_tech_stack/)
is anecdotal. Core-first sequencing is a teaching judgment based on your gaps and
the inspected examples. [PostgreSQL pg_dump](https://www.postgresql.org/docs/18/app-pgdump.html)
and [pg_restore](https://www.postgresql.org/docs/18/app-pgrestore.html) establish
DE28's logical recovery boundary. [dbt documentation](https://docs.getdbt.com/docs/build/documentation)
supports documenting model/column meaning; the course also requires manual lineage.

## Lesson decisions

Common change: approach help and worked results are closed; required contracts and
setup/run commands stay visible. Completed lessons remain references.

| Lesson | Difficulty | Decision |
|---|---|---|
| [Day 01 — Python and CSV cleaning](../01-foundation/day-01/guide.md) | Learn | Preserve completed work and original teaching; label as reference, do not restart. |
| [Day 02 — Functions, lists, dictionaries, and sets](../01-foundation/day-02/guide.md) | Learn | Preserve completed work and original teaching; label as reference, do not restart. |
| [Day 03 — JSON, configuration, and datetime](../01-foundation/day-03/guide.md) | Learn | Preserve completed work and original teaching; label as reference, do not restart. |
| [Day 04 — Clean tabular data with pandas](../01-foundation/day-04/guide.md) | Learn | Preserve completed work and original teaching; label as reference, do not restart. |
| [Day 05 — Join and aggregate with pandas](../01-foundation/day-05/guide.md) | Learn | Preserve completed work and original teaching; label as reference, do not restart. |
| [Day 06 — CLI, environment variables, and HTTP APIs](../01-foundation/day-06/guide.md) | Learn | Preserve completed work and original teaching; label as reference, do not restart. |
| [Day 07 — Mini-project 1: a reproducible weather snapshot](../01-foundation/day-07/guide.md) | Integrate | Preserve completed work and original teaching; label as reference, do not restart. |
| [Day 08 — PostgreSQL tables, keys, and constraints](../01-foundation/day-08/guide.md) | Apply | Preserve completed work and original teaching; label as reference, do not restart. |
| [Day 09 — SQL joins, grouping, and NULL](../01-foundation/day-09/guide.md) | Apply | Preserve completed work and original teaching; label as reference, do not restart. |
| [Day 10 — CTEs, CASE, dates, and subqueries](../01-foundation/day-10/guide.md) | Apply | Preserve completed work and original teaching; label as reference, do not restart. |
| [Day 11 — Window functions and time comparisons](../01-foundation/day-11/guide.md) | Apply | Preserve completed work and original teaching; label as reference, do not restart. |
| [Day 12 — Data modeling: grain, dimensions, and facts](../01-foundation/day-12/guide.md) | Apply | Replace answer-shaped DDL/report tutorial with concepts and unrelated SQL shapes; preserve current schema. |
| [Day 13 — Load PostgreSQL from Python](../01-foundation/day-13/guide.md) | Apply | Use a scratch copy of input with a changed measurement for an existing key. Prove an identical rerun adds no observation, then show a failed batch leaves prior data intact. |
| [Day 14 — Mini-project 2: a reusable loader and SQL mart](../01-foundation/day-14/guide.md) | Integrate | Run from another current directory and replace the input path with a new fixture. Prove the package, not the shell location, determines its behavior. |
| [Day 15 — Reliable HTTP extraction and bounded retries](../01-foundation/day-15/guide.md) | Apply | Use injected responses with a transient failure followed by success, and a permanent failure. Explain call count and why no delay follows the last attempt. |
| [Day 16 — ETL, file layers, and a complete batch pipeline](../01-foundation/day-16/guide.md) | Integrate | Reconcile accepted plus rejected rows against raw row count on a changed fixture. Demonstrate a failure before publication preserves the last complete output. |
| [Day 17 — Incremental loads, corrections, and backfills](../01-foundation/day-17/guide.md) | Integrate | Introduce a correction to an older observation and replay it. Compare the result with a rebuild rather than relying only on row counts. |
| [Day 18 — Docker and Linux CLI from the beginning](../01-foundation/day-18/guide.md) | Learn | Concise syntax drill; group with adjacent drills once a changed example is explainable. |
| [Day 19 — Package the pipeline with Docker Compose](../01-foundation/day-19/guide.md) | Integrate | Run a batch twice with the same input. Identify which files survive container removal and which environment setting selects the database. |
| [Day 20 — Orchestration with Prefect flows and tasks](../01-foundation/day-20/guide.md) | Apply | Keep explicit task contracts; hide approaches and compare a changed/failing case. |
| [Day 21 — Mini-project 3: schedule and observe repeated runs](../01-foundation/day-21/guide.md) | Integrate | Keep explicit task contracts; hide approaches and compare a changed/failing case. |
| [Day 22 — Meaningful automated tests with pytest](../01-foundation/day-22/guide.md) | Apply | Change one behavior in an isolated copy. Demonstrate that a relevant assertion fails, then restore the copy; a syntax failure does not count. |
| [Day 23 — Data quality and deterministic freshness checks](../01-foundation/day-23/guide.md) | Apply | Use a fixed clock with a record exactly at the freshness boundary and just beyond it. State the empty-source policy separately. |
| [Day 24 — Warehouses, query plans, and a small cloud lab](../01-foundation/day-24/guide.md) | Learn | Concise syntax drill; group with adjacent drills once a changed example is explainable. |
| [Day 25 — Analytics: turn clean data into an honest report](../01-foundation/day-25/guide.md) | Apply | Add a city with no measurements to a scratch fixture. Keep missing data distinct from zero and state what the chart can support. |
| [Day 26 — Continuous integration with GitHub Actions](../01-foundation/day-26/guide.md) | Integrate | Keep explicit task contracts; hide approaches and compare a changed/failing case. |
| [Day 27 — Use AI assistance with deterministic verification](../01-foundation/day-27/guide.md) | Apply | Create a plausible but false generated claim. Show your deterministic check rejects it and preserves evidence of the rejection. |
| [Day 28 — Capstone architecture, contracts, and runbook](../01-foundation/day-28/guide.md) | Integrate | Keep explicit task contracts; hide approaches and compare a changed/failing case. |
| [Day 29 — Rehearse end to end and recover from failures](../01-foundation/day-29/guide.md) | Assess | Keep explicit task contracts; hide approaches and compare a changed/failing case. |
| [Day 30 — Package the portfolio and explain your decisions](../01-foundation/day-30/guide.md) | Assess | Keep explicit task contracts; hide approaches and compare a changed/failing case. |
| [C01-L01 — Run a script, comments, and print](../02-python/01-fundamentals/01-run-print/guide.md) | Learn | Concise syntax drill; group with adjacent drills once a changed example is explainable. |
| [C01-L02 — Variables and input conversion](../02-python/01-fundamentals/02-variables-input/guide.md) | Learn | Concise syntax drill; group with adjacent drills once a changed example is explainable. |
| [C01-L03 — Data types and explicit conversion](../02-python/01-fundamentals/03-types/guide.md) | Learn | Concise syntax drill; group with adjacent drills once a changed example is explainable. |
| [C02-L01 — Clean and format strings](../02-python/02-strings/01-normalize/guide.md) | Learn | Concise syntax drill; group with adjacent drills once a changed example is explainable. |
| [C02-L02 — Indexing and slicing without off-by-one errors](../02-python/02-strings/02-slicing/guide.md) | Learn | Concise syntax drill; group with adjacent drills once a changed example is explainable. |
| [C02-L03 — Search strings and define validation limits](../02-python/02-strings/03-search-validation/guide.md) | Learn | Concise syntax drill; group with adjacent drills once a changed example is explainable. |
| [C03-L01 — Integers, floats, and arithmetic](../02-python/03-numbers/01-arithmetic/guide.md) | Learn | Concise syntax drill; group with adjacent drills once a changed example is explainable. |
| [C03-L02 — Rounding, display precision, and randomness](../02-python/03-numbers/02-round-random/guide.md) | Learn | Concise syntax drill; group with adjacent drills once a changed example is explainable. |
| [C04-L01 — Boolean values and truthiness](../02-python/04-logic/01-truthiness/guide.md) | Learn | Concise syntax drill; group with adjacent drills once a changed example is explainable. |
| [C04-L02 — Comparisons and combined rules](../02-python/04-logic/02-combined-rules/guide.md) | Learn | Concise syntax drill; group with adjacent drills once a changed example is explainable. |
| [C04-L03 — Membership, equality, and identity](../02-python/04-logic/03-membership-identity/guide.md) | Learn | Concise syntax drill; group with adjacent drills once a changed example is explainable. |
| [C05-L01 — if, elif, else, and boundary order](../02-python/05-conditions/01-branches/guide.md) | Learn | Concise syntax drill; group with adjacent drills once a changed example is explainable. |
| [C05-L02 — Nested conditions and validation order](../02-python/05-conditions/02-nested-validation/guide.md) | Apply | Keep explicit task contracts; hide approaches and compare a changed/failing case. |
| [C05-L03 — Conditional expressions and match](../02-python/05-conditions/03-inline-match/guide.md) | Learn | Concise syntax drill; group with adjacent drills once a changed example is explainable. |
| [C06-L01 — for loops and accumulators](../02-python/06-loops/01-for/guide.md) | Learn | Concise syntax drill; group with adjacent drills once a changed example is explainable. |
| [C06-L02 — break, continue, and pass](../02-python/06-loops/02-control/guide.md) | Learn | Concise syntax drill; group with adjacent drills once a changed example is explainable. |
| [C06-L03 — Search with for-else](../02-python/06-loops/03-loop-else/guide.md) | Apply | Keep explicit task contracts; hide approaches and compare a changed/failing case. |
| [C06-L04 — Nested loops and pairs](../02-python/06-loops/04-nested/guide.md) | Apply | Keep explicit task contracts; hide approaches and compare a changed/failing case. |
| [C06-L05 — while loops and guaranteed progress](../02-python/06-loops/05-while/guide.md) | Apply | Keep explicit task contracts; hide approaches and compare a changed/failing case. |
| [C07-L01 — Create and access lists](../02-python/07-data-structures/01-lists/guide.md) | Learn | Concise syntax drill; group with adjacent drills once a changed example is explainable. |
| [C07-L02 — Unpack rows and analyze lists](../02-python/07-data-structures/02-unpack-analyze/guide.md) | Learn | Concise syntax drill; group with adjacent drills once a changed example is explainable. |
| [C07-L03 — Add, remove, and update list elements](../02-python/07-data-structures/03-mutation/guide.md) | Learn | Concise syntax drill; group with adjacent drills once a changed example is explainable. |
| [C07-L04 — Aliases, shallow copies, and nested data](../02-python/07-data-structures/04-copying/guide.md) | Apply | Keep explicit task contracts; hide approaches and compare a changed/failing case. |
| [C07-L05 — Sort, reverse, and combine lists](../02-python/07-data-structures/05-sort-combine/guide.md) | Apply | Keep explicit task contracts; hide approaches and compare a changed/failing case. |
| [C07-L06 — Iterables, enumerate, zip, and filtering](../02-python/07-data-structures/06-iteration-filtering/guide.md) | Apply | Keep explicit task contracts; hide approaches and compare a changed/failing case. |
| [C07-L07 — Comprehensions and small lambda expressions](../02-python/07-data-structures/07-comprehension-lambda/guide.md) | Apply | Keep explicit task contracts; hide approaches and compare a changed/failing case. |
| [C07-L08 — Tuples and fixed-shape records](../02-python/07-data-structures/08-tuples/guide.md) | Learn | Concise syntax drill; group with adjacent drills once a changed example is explainable. |
| [C07-L09 — Sets, membership, and stable deduplication](../02-python/07-data-structures/09-sets/guide.md) | Apply | Use an input whose first-seen order differs from alphabetical order, with a normalized duplicate. Explain the role of each collection. |
| [C07-L10 — Dictionaries, nested records, and aggregation](../02-python/07-data-structures/10-dictionaries/guide.md) | Apply | Use interleaved repeated groups plus empty input. Explain whether the number of groups equals the number of source records. |
| [C08-L01 — Define and call small functions](../02-python/08-functions/01-define-call/guide.md) | Learn | Concise syntax drill; group with adjacent drills once a changed example is explainable. |
| [C08-L02 — Positional, keyword, and default arguments](../02-python/08-functions/02-parameters/guide.md) | Learn | Concise syntax drill; group with adjacent drills once a changed example is explainable. |
| [C08-L03 — Return values, early return, and scope](../02-python/08-functions/03-return-scope/guide.md) | Learn | Concise syntax drill; group with adjacent drills once a changed example is explainable. |
| [C08-L04 — Collect and unpack arguments with * and **](../02-python/08-functions/04-flexible-arguments/guide.md) | Apply | Keep explicit task contracts; hide approaches and compare a changed/failing case. |
| [C08-L05 — Built-ins, named functions, and lambdas](../02-python/08-functions/05-callables/guide.md) | Apply | Keep explicit task contracts; hide approaches and compare a changed/failing case. |
| [C08-L06 — Clean functions and a weather-report mini-project](../02-python/08-functions/06-clean-functions/guide.md) | Integrate | Complete checkpoint 3 in the Python checkpoint file on a different subject before calling this independent programming. |
| [C09-L01 — Exceptions and deliberate validation](../02-python/09-errors-and-types/01-exceptions/guide.md) | Apply | Use a value of the wrong type and one with the right type but invalid value. Explain which exception represents each boundary. |
| [C09-L02 — Logging and observable failures](../02-python/09-errors-and-types/02-logging/guide.md) | Apply | Keep explicit task contracts; hide approaches and compare a changed/failing case. |
| [C09-L03 — Type hints, dataclasses, and simple objects](../02-python/09-errors-and-types/03-dataclasses/guide.md) | Apply | Try True where an exact integer is required. Explain why an annotation and frozen fields do not validate external values. |
| [C10-L01 — Paths, context managers, and safe file replacement](../02-python/10-files-and-time/01-paths-atomic/guide.md) | Apply | Cause serialization to fail after an existing output is present. Prove that output is unchanged and no owned temporary file is leaked. |
| [C10-L02 — CSV, JSON, JSON Lines, and schema boundaries](../02-python/10-files-and-time/02-csv-jsonl/guide.md) | Apply | Try a quoted comma, a duplicate header and an extra cell. Distinguish a whole-file schema defect from an individual value defect. |
| [C10-L03 — Aware time, UTC, and deterministic clocks](../02-python/10-files-and-time/03-datetime/guide.md) | Apply | Use two offset representations of the same instant and one naive value. Require equivalent UTC results and rejection of the naive value. |
| [C10-L04 — Decimal parsing and exact money](../02-python/10-files-and-time/04-decimal/guide.md) | Apply | Compare 1.2300, 1.001 and a nonfinite value. Preserve exact cents; do not make an invalid amount acceptable by rounding. |
| [C11-L01 — Imports, modules, and entry points](../02-python/11-projects-and-tests/01-modules/guide.md) | Apply | Keep explicit task contracts; hide approaches and compare a changed/failing case. |
| [C11-L02 — CLI options, configuration, and environments](../02-python/11-projects-and-tests/02-cli-config/guide.md) | Apply | Keep explicit task contracts; hide approaches and compare a changed/failing case. |
| [C11-L03 — Tests that detect meaningful defects](../02-python/11-projects-and-tests/03-unit-tests/guide.md) | Apply | Demonstrate the published meaningful mutations fail with assertion errors, rather than test-discovery/import errors. |
| [C11-L04 — Dependency injection and mocked HTTP](../02-python/11-projects-and-tests/04-mocks/guide.md) | Apply | Change the fake response sequence. Prove status validation occurs before decoding and that an unexpected call fails the test. |
| [C12-L01 — Generators, batching, and memory](../02-python/12-data-processing/01-generators/guide.md) | Apply | Use a one-shot generator with a partial final batch. Verify each item is consumed once; explain when you materialize the input. |
| [C12-L02 — pandas joins, types, and trustworthy totals](../02-python/12-data-processing/02-pandas/guide.md) | Apply | Add a duplicate dimension key, then an unmatched fact key in separate fixtures. Require explicit failure instead of inflated or silently missing totals. |
| [C12-L03 — Parquet and explicit storage schemas](../02-python/12-data-processing/03-parquet/guide.md) | Apply | Round-trip a changed valid dataset and compare values and dtypes. Demonstrate the out-of-range case is rejected before publication. |
| [C13-L01 — HTTP responses, pagination, and bounded extraction](../02-python/13-apis-and-databases/01-pagination/guide.md) | Apply | Use a repeated continuation token and a sequence exceeding max_pages. Prove no extra request is made; separately reject a malformed next value. |
| [C13-L02 — Retry only transient failures](../02-python/13-apis-and-databases/02-retries/guide.md) | Apply | Measure fake request/delay calls for permanent failure, transient recovery and attempt exhaustion. No real sleeping is needed. |
| [C13-L03 — Parameterized SQL and transaction rollback](../02-python/13-apis-and-databases/03-sqlite-transactions/guide.md) | Apply | Inject a failure after one attempted write and compare durable state before/after rollback; a successful happy path is insufficient. |
| [C13-L04 — Native PostgreSQL with Psycopg](../02-python/13-apis-and-databases/04-postgresql/guide.md) | Apply | Run the live checker, then explain transaction ownership. Offline binding checks alone do not prove PostgreSQL rollback. |
| [C14-L01 — Incremental state, replays, and corrections](../02-python/14-reliable-pipelines/01-incremental/guide.md) | Apply | Shuffle different-version arrival order and replay a deletion followed by stale data. Preserve state and reject an equal-version conflict. |
| [C14-L02 — Data-quality checks and fixed-clock freshness](../02-python/14-reliable-pipelines/02-data-quality/guide.md) | Apply | Hold now fixed and vary only data at a boundary. Explain whether each defect is a batch failure or a counted quality issue. |
| [C14-L03 — Capstone: reproducible retail ingestion](../02-python/14-reliable-pipelines/03-capstone/guide.md) | Integrate | Keep explicit task contracts; hide approaches and compare a changed/failing case. |
| [LE01 — Ubuntu, shells and path navigation](../03-linux/01-linux-basics/01-shell-navigation/guide.md) | Learn | Concise syntax drill; group with adjacent drills once a changed example is explainable. |
| [LE02 — Files, directories, inspection and scoped cleanup](../03-linux/01-linux-basics/02-files-and-find/guide.md) | Learn | Concise syntax drill; group with adjacent drills once a changed example is explainable. |
| [LE03 — Standard streams, pipes and text inspection](../03-linux/01-linux-basics/03-streams-and-text/guide.md) | Learn | Concise syntax drill; group with adjacent drills once a changed example is explainable. |
| [LE04 — Users, permissions and executable files](../03-linux/01-linux-basics/04-permissions/guide.md) | Learn | Concise syntax drill; group with adjacent drills once a changed example is explainable. |
| [LE05 — Variables, quoting and arguments](../03-linux/02-bash-scripting/01-variables-quoting/guide.md) | Apply | Keep explicit task contracts; hide approaches and compare a changed/failing case. |
| [LE06 — Run Python in Linux with an explicit environment](../03-linux/02-bash-scripting/02-python-environment/guide.md) | Apply | Keep explicit task contracts; hide approaches and compare a changed/failing case. |
| [LE07 — Exit status, conditions and deliberate failure](../03-linux/02-bash-scripting/03-status-and-conditions/guide.md) | Apply | Keep explicit task contracts; hide approaches and compare a changed/failing case. |
| [LE08 — Loops, functions and numeric validation](../03-linux/02-bash-scripting/04-loops-and-functions/guide.md) | Apply | Keep explicit task contracts; hide approaches and compare a changed/failing case. |
| [LE09 — A reusable batch runner with logs](../03-linux/02-bash-scripting/05-batch-runner/guide.md) | Integrate | Run from a directory containing spaces and use an input that makes the app fail. Preserve its nonzero exit code and logs. |
| [LE10 — Processes, jobs and graceful stopping](../03-linux/03-processes-network/01-processes-signals/guide.md) | Apply | Keep explicit task contracts; hide approaches and compare a changed/failing case. |
| [LE11 — Ports, HTTP and local network diagnosis](../03-linux/03-processes-network/02-http-network/guide.md) | Apply | Keep explicit task contracts; hide approaches and compare a changed/failing case. |
| [LE12 — Logs, resource checks and a useful runbook](../03-linux/03-processes-network/03-diagnosis-runbook/guide.md) | Apply | Reproduce an unfamiliar failure before consulting the runbook. Record evidence that distinguishes environment failure from bad input. |
| [LE13 — Git states, branches, diffs and scoped undo](../03-linux/04-git-collaboration/01-branches-and-diffs/guide.md) | Learn | Concise syntax drill; group with adjacent drills once a changed example is explainable. |
| [LE14 — Merge conflicts and preserving both intentions](../03-linux/04-git-collaboration/02-merge-conflicts/guide.md) | Apply | Explain both intentions before resolving the conflict. Show the final behavior and diff, not just the absence of conflict markers. |
| [LE15 — Local remotes, pull requests and review evidence](../03-linux/04-git-collaboration/03-local-team-and-review/guide.md) | Apply | Keep explicit task contracts; hide approaches and compare a changed/failing case. |
| [LE16 — Docker images, containers and the engine](../03-linux/05-docker/01-images-and-containers/guide.md) | Learn | Concise syntax drill; group with adjacent drills once a changed example is explainable. |
| [LE17 — Bind mounts, named volumes and persistent artifacts](../03-linux/05-docker/02-storage/guide.md) | Apply | Keep explicit task contracts; hide approaches and compare a changed/failing case. |
| [LE18 — Build an image and control its command](../03-linux/05-docker/03-dockerfile/guide.md) | Integrate | Keep explicit task contracts; hide approaches and compare a changed/failing case. |
| [LE19 — Container networks, service names and published ports](../03-linux/05-docker/04-container-network/guide.md) | Apply | Keep explicit task contracts; hide approaches and compare a changed/failing case. |
| [LE20 — Compose for a batch job and report viewer](../03-linux/05-docker/05-compose/guide.md) | Integrate | Remove an owned stopped batch container and run the viewer again. Identify the persistence boundary and avoid deleting the output volume. |
| [LE21 — CI that catches a real regression](../03-linux/06-delivery/01-ci-and-regression/guide.md) | Apply | Keep explicit task contracts; hide approaches and compare a changed/failing case. |
| [LE22 — Capstone: deliver and recover a Linux batch pipeline](../03-linux/06-delivery/02-capstone/guide.md) | Assess | Keep explicit task contracts; hide approaches and compare a changed/failing case. |
| [DE01 — Data systems and the lifecycle](../04-data-engineering/01-workflow/01-systems/guide.md) | Learn | Concise syntax drill; group with adjacent drills once a changed example is explainable. |
| [DE02 — From an assigned task to a checked delivery](../04-data-engineering/01-workflow/02-tasks/guide.md) | Apply | List observed source facts before writing your plan. Separate source guarantees requiring confirmation from assumptions you can test. |
| [DE03 — Read, debug and profile unfamiliar code](../04-data-engineering/01-workflow/03-debugging/guide.md) | Apply | Keep explicit task contracts; hide approaches and compare a changed/failing case. |
| [DE04 — Data contracts, types and evolution](../04-data-engineering/02-data-design/01-contracts/guide.md) | Apply | Keep explicit task contracts; hide approaches and compare a changed/failing case. |
| [DE05 — Grain, dimensions and historical meaning](../04-data-engineering/02-data-design/02-grain-and-history/guide.md) | Apply | Place an event exactly at a dimension boundary, then introduce overlapping intervals. Prove the first maps once and the second is rejected. |
| [DE06 — Transactions, upserts and checkpoint atomicity](../04-data-engineering/02-data-design/03-transactions/guide.md) | Apply | Demonstrate the supplied mid-batch failure on native PostgreSQL. A mock connection is not evidence of durable atomicity. |
| [DE07 — Query plans, indexes and measured optimization](../04-data-engineering/02-data-design/04-query-plans/guide.md) | Apply | Change predicate selectivity and measure both plans. Explain why an index may help one query and not another. |
| [DE08 — Corrections, tombstones and deterministic replay](../04-data-engineering/03-pipelines/01-corrections-and-deletes/guide.md) | Apply | Use a reordered fixture with a tombstone and later stale replay. Reject equal-version differing content rather than selecting it arbitrarily. |
| [DE09 — Event time, extraction cursors and backfills](../04-data-engineering/03-pipelines/02-windows-and-cursors/guide.md) | Apply | Place several records at the same extraction timestamp and one on the exclusive end. Prove no tied ID is skipped. |
| [DE10 — Quality checks, reconciliation and fixed-clock freshness](../04-data-engineering/03-pipelines/03-quality-and-reconciliation/guide.md) | Apply | Keep explicit task contracts; hide approaches and compare a changed/failing case. |
| [DE11 — Batch evidence, publication state and recovery](../04-data-engineering/03-pipelines/04-observability-and-recovery/guide.md) | Apply | Fail after database commit but before file publication. Recover without reapplying durable changes or falsely claiming publication. |
| [DE12 — Warehouse layers and a local analytical engine](../04-data-engineering/04-warehouse/01-layers-and-duckdb/guide.md) | Apply | Keep explicit task contracts; hide approaches and compare a changed/failing case. |
| [DE13 — dbt models, refs and dependency structure](../04-data-engineering/04-warehouse/02-dbt-models/guide.md) | Integrate | Keep explicit task contracts; hide approaches and compare a changed/failing case. |
| [DE14 — dbt data tests and transformation evidence](../04-data-engineering/04-warehouse/03-dbt-tests/guide.md) | Apply | Keep explicit task contracts; hide approaches and compare a changed/failing case. |
| [DE15 — Incremental transformations and correctness before pruning](../04-data-engineering/04-warehouse/04-incremental-models/guide.md) | Apply | Remove the model SELECT answer; require old-day correction/delete versus full rebuild. |
| [DE16 — Dependency graphs, parameters and run boundaries](../04-data-engineering/05-orchestration/01-dependencies/guide.md) | Apply | Use an unknown dependency and a cycle. Fail explicitly rather than returning a partial valid-looking ordering. |
| [DE17 — Prefect runs, retry ownership and backfill rehearsal](../04-data-engineering/05-orchestration/02-prefect-runs/guide.md) | Integrate | Keep explicit task contracts; hide approaches and compare a changed/failing case. |
| [DE18 — Airflow concepts and orchestration transfer](../04-data-engineering/05-orchestration/03-airflow-transfer/guide.md) | Learn | Concise syntax drill; group with adjacent drills once a changed example is explainable. |
| [DE19 — Cloud storage, IAM and cost-aware design](../04-data-engineering/06-platforms/01-cloud-design/guide.md) | Learn | Concise syntax drill; group with adjacent drills once a changed example is explainable. |
| [DE20 — An optional BigQuery sandbox lab](../04-data-engineering/06-platforms/02-bigquery-sandbox/guide.md) | Integrate | Keep explicit task contracts; hide approaches and compare a changed/failing case. |
| [DE21 — Spark schemas, plans and distributed-processing decisions](../04-data-engineering/06-platforms/03-spark-introduction/guide.md) | Apply | Keep explicit task contracts; hide approaches and compare a changed/failing case. |
| [DE22 — Credentials, privacy and verified AI assistance](../04-data-engineering/06-platforms/04-security-and-ai/guide.md) | Apply | Keep explicit task contracts; hide approaches and compare a changed/failing case. |
| [DE23 — Metric definitions and honest analytics](../04-data-engineering/07-internship/01-metrics-and-communication/guide.md) | Apply | Give the consumer a data dictionary and source-to-report column mapping; ask them to identify the grain and one unsafe interpretation. |
| [DE24 — Point-in-time feature data and leakage](../04-data-engineering/07-internship/02-ml-feature-data/guide.md) | Apply | Keep explicit task contracts; hide approaches and compare a changed/failing case. |
| [DE25 — A complete retail pipeline portfolio](../04-data-engineering/07-internship/03-integrated-capstone/guide.md) | Integrate | Keep explicit task contracts; hide approaches and compare a changed/failing case. |
| [DE26 — An independent take-home and debugging rehearsal](../04-data-engineering/07-internship/04-unseen-assignment/guide.md) | Assess | Keep explicit task contracts; hide approaches and compare a changed/failing case. |
| [DE27 — Source discovery](../04-data-engineering/07-internship/05-source-discovery/guide.md) | Apply | Add changed-source profiling, owner questions, catalog and consumer lineage; no cleaning algorithm supplied. |
| [DE28 — Verified restore](../04-data-engineering/07-internship/06-backup-and-restore/guide.md) | Integrate | Add native logical dump/restore and complete state/constraint checks; verification SQL is learner work. |
| [DE29 — Readiness, CV evidence and internship applications](../04-data-engineering/07-internship/07-applications-and-interviews/guide.md) | Assess | Keep explicit task contracts; hide approaches and compare a changed/failing case. |
| [LAB01 — Repair a report with inflated totals](../05-extensions/01-labs/01-joins/guide.md) | Apply | Keep explicit task contracts; hide approaches and compare a changed/failing case. |
| [LAB02 — Adapt a changed API contract](../05-extensions/01-labs/02-api-change/guide.md) | Apply | Keep explicit task contracts; hide approaches and compare a changed/failing case. |
| [LAB03 — Extend a schema without losing existing data](../05-extensions/01-labs/03-migration/guide.md) | Apply | Demonstrate old-writer omission versus explicit NULL and a pre-commit failure in a disposable database. The one-line checker is only a drill. |
| [LAB04 — Repair missing backfill intervals](../05-extensions/01-labs/04-backfill/guide.md) | Apply | Keep explicit task contracts; hide approaches and compare a changed/failing case. |
| [LAB05 — Repair a partial commit with a durable batch ledger](../05-extensions/01-labs/05-recovery/guide.md) | Apply | Keep explicit task contracts; hide approaches and compare a changed/failing case. |
| [LAB06 — Measure and improve dimension enrichment](../05-extensions/01-labs/06-performance/guide.md) | Apply | Keep explicit task contracts; hide approaches and compare a changed/failing case. |
| [LAB07 — Interpret retries without reporting recovered runs as failures](../05-extensions/01-labs/07-logs/guide.md) | Apply | Keep explicit task contracts; hide approaches and compare a changed/failing case. |
| [LAB08 — Complete an independent maintenance ticket](../05-extensions/01-labs/08-handoff/guide.md) | Assess | Keep explicit task contracts; hide approaches and compare a changed/failing case. |
| [CL01 — Plan one cloud pipeline and its ownership](../05-extensions/02-cloud/01-boundaries/guide.md) | Learn | Concise syntax drill; group with adjacent drills once a changed example is explainable. |
| [CL02 — Create stable object keys and immutable raw input](../05-extensions/02-cloud/02-storage/guide.md) | Apply | Keep explicit task contracts; hide approaches and compare a changed/failing case. |
| [CL03 — Package a bounded batch job](../05-extensions/02-cloud/03-jobs/guide.md) | Integrate | Keep explicit task contracts; hide approaches and compare a changed/failing case. |
| [CL04 — Load history and materialize current state](../05-extensions/02-cloud/04-warehouse/guide.md) | Integrate | Keep explicit task contracts; hide approaches and compare a changed/failing case. |
| [CL05 — Grant permissions at the right scope](../05-extensions/02-cloud/05-iam/guide.md) | Apply | Keep explicit task contracts; hide approaches and compare a changed/failing case. |
| [CL06 — Authenticate a schedule and preserve batch identity](../05-extensions/02-cloud/06-scheduler/guide.md) | Integrate | Keep explicit task contracts; hide approaches and compare a changed/failing case. |
| [CL07 — Bound query work and own cleanup](../05-extensions/02-cloud/07-costs/guide.md) | Apply | Keep explicit task contracts; hide approaches and compare a changed/failing case. |
| [CL08 — Deliver the cloud inventory batch pipeline](../05-extensions/02-cloud/08-capstone/guide.md) | Integrate | Keep explicit task contracts; hide approaches and compare a changed/failing case. |
| [AI01 — Define document identity and provenance](../05-extensions/03-ai-data/01-documents/guide.md) | Apply | Keep explicit task contracts; hide approaches and compare a changed/failing case. |
| [AI02 — Normalize text without losing paragraph structure](../05-extensions/03-ai-data/02-text/guide.md) | Apply | Keep explicit task contracts; hide approaches and compare a changed/failing case. |
| [AI03 — Create deterministic overlapping chunks](../05-extensions/03-ai-data/03-chunks/guide.md) | Apply | Keep explicit task contracts; hide approaches and compare a changed/failing case. |
| [AI04 — Build a local lexical retrieval baseline](../05-extensions/03-ai-data/04-lexical/guide.md) | Apply | Keep explicit task contracts; hide approaches and compare a changed/failing case. |
| [AI05 — Rank vectors and distinguish fixtures from embeddings](../05-extensions/03-ai-data/05-vectors/guide.md) | Apply | Keep explicit task contracts; hide approaches and compare a changed/failing case. |
| [AI06 — Propagate document edits and deletes](../05-extensions/03-ai-data/06-index-state/guide.md) | Apply | Keep explicit task contracts; hide approaches and compare a changed/failing case. |
| [AI07 — Evaluate retrieval before trusting generated answers](../05-extensions/03-ai-data/07-evaluation/guide.md) | Apply | Include repeated chunks from one document before k and a no-relevant-document query. Explain the metric denominator and corpus revision. |
| [AI08 — Deliver a reproducible document search pipeline](../05-extensions/03-ai-data/08-capstone/guide.md) | Integrate | Keep explicit task contracts; hide approaches and compare a changed/failing case. |
| [ST01 — Understand topics, partitions and a local broker](../05-extensions/04-streaming/01-broker/guide.md) | Learn | Concise syntax drill; group with adjacent drills once a changed example is explainable. |
| [ST02 — Publish keyed records and confirm delivery](../05-extensions/04-streaming/02-producer/guide.md) | Apply | Keep explicit task contracts; hide approaches and compare a changed/failing case. |
| [ST03 — Commit only the safe processed prefix](../05-extensions/04-streaming/03-offsets/guide.md) | Apply | Keep explicit task contracts; hide approaches and compare a changed/failing case. |
| [ST04 — Make a transactional sink tolerate replay](../05-extensions/04-streaming/04-sink/guide.md) | Apply | Keep explicit task contracts; hide approaches and compare a changed/failing case. |
| [ST05 — Quarantine poison data without hiding infrastructure failures](../05-extensions/04-streaming/05-rejections/guide.md) | Apply | Keep explicit task contracts; hide approaches and compare a changed/failing case. |
| [ST06 — Interpret real PostgreSQL change envelopes](../05-extensions/04-streaming/06-cdc/guide.md) | Apply | Keep explicit task contracts; hide approaches and compare a changed/failing case. |
| [ST07 — Capture changes and recover after a consumer crash](../05-extensions/04-streaming/07-restart/guide.md) | Integrate | Keep explicit task contracts; hide approaches and compare a changed/failing case. |
| [ST08 — Deliver a streaming and CDC recovery demo](../05-extensions/04-streaming/08-capstone/guide.md) | Integrate | Keep explicit task contracts; hide approaches and compare a changed/failing case. |

## Verification

- All 169 lesson guides/indexes checked; 2,824 local links resolved at the initial validation pass.
- All 272 original non-Markdown files matched the pre-audit hashes, including learner code, fixtures/configuration and Day 12 schema. Completed progress remains 11 days.
- The new profiler passed 27 behavioral assertions; its blank starter and four deliberately faulty implementations were rejected. Author solutions stay outside the course.
- The new restore drill executed on an isolated PostgreSQL 18.6 cluster: baseline and changed-fixture archives restored with matching complete data/constraint state. Six invalid writes were rejected; the owned test server was stopped afterward.
- All 358 PowerShell command blocks and 52 changed Python examples were syntax checked. Existing executables were preserved, so unrelated runtime checks were not repeated.

This is a teaching-content audit. Existing Docker/cloud/streaming/CI labs were not
newly executed here. Native restore validation is author evidence, not learner
completion; your progress remains unchecked.
