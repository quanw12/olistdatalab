# Author verification — October 6, 2026

## Passed checks

- 27 lesson folders each contain guide, concepts/syntax, assignment, detailed help and expected evidence. Every guide includes manual commit/push commands.
- Python exercise/startup files are prompt-only; supplied checks/configuration/fixtures are labeled infrastructure. Private reference solutions were not placed in the course.
- Nine offline contracts passed against private author references after the folder migration: DE03, DE04, DE08, DE09, DE10, DE12, DE16, DE22 and DE24.
- All nine unfinished prompts were rejected by their checks.
- DE03's checker rejected the original bug and separate overwrite, untrimmed-key and hard-coded-result variants. The documented pdb sequence ran against buggy.py; the bounded cProfile workload ran against a private corrected reference.
- The moved Linux supplied app passed its six behavior tests; all four Bash contracts passed against private references using Git Bash. The moved Python checker imported its shared infrastructure and correctly rejected an unfinished learner function.
- Folder/file audit retained all original nonredundant files, including byte-for-byte checks for saved submissions, Day 12 schema, and SQL/data fixtures. Foundation progress still records 11 completed and 19 open lessons.
- All active local Markdown links resolved; 120 active Python files parsed and 271 PowerShell examples parsed without errors. Historical submission text was preserved separately rather than rewritten.
- Local dbt seed/staging/latest/mart/incremental reference build and data tests ran with synthetic fixtures.
- Initial b1 mart: c1 one/1000, c2 one/1500.
- Corrections/deletion/late b2: c1 two/2000; latest state retains B's tombstone.
- Repeated build and full-refresh matched entity and mart state.
- A deliberately wrong mart total failed its singular reconciliation test; restored build passed.
- The provided warehouse output checker accepted the fixture and rejected wrong mart/incremental state.
- Python source/teaching examples and Bash teaching snippets parsed; PowerShell teaching/commit blocks parsed; project YAML parsed; local Markdown links were checked.
- Installed warehouse reference dependencies passed pip check.

## Actual environment

Windows Python 3.13.5, isolated temporary author venv, DuckDB 1.5.6, dbt-duckdb 1.11.0, dbt-core 1.12.5. Bash syntax used Git Bash, not native Ubuntu. The learner's normal environments were not replaced.

## Not claimed

Native PostgreSQL loading/rollback and the integrated capstone remain learner implementations requiring live evidence. The Prefect snippet/assignment was researched and syntax checked, not executed as a real orchestration service. Docker delivery, active GitHub Actions and optional Airflow/Spark/cloud were not deployed by this task.

A reference model's success does not mean your unfinished models are completed. Fixture tests certify only stated cases, not every input or a production guarantee. Progress remains unchecked except your separately confirmed foundation Days 1–11.

## Reproduce your own evidence

Follow setup and each guide. Run the nine offline checks, actual dbt seed/build/tests/output check, then the capstone contract and assessment gates. Save actual failure/recovery evidence and version/environment details. Use optional technology only when role fit justifies it.

