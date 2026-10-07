# Day 29 — Rehearse end to end and recover from failures

Keep this closed until the timed/independent attempt ends. Reading an approach first makes the attempt guided practice; record that honestly.

<details>
<summary>After an attempt — supporting explanation</summary>

1. Create weather_course_demo, configure the intended host/port/user, then set PGDATABASE. Bootstrap all three schemas from your saved files. SELECT current_database() before the first write.
2. Run normalized base load twice, next twice, old base once. Query counts and the corrected identity after each step.
3. Run raw_batch_with_errors through run fixture mode. On the now-updated DB it still reports accepted 8/rejected 2 but stored 10, because old inputs must not reverse newer state.
4. Use integration tests against their dedicated test database for rollback; use injected HTTP fakes for retry exhaustion. Keep their evidence labeled as tests, not live outages.
5. Force a manifest publication failure after a successful DB commit in a controlled test. Verify the committed state and replay behavior; do not claim the database rolled back.
6. For a clean venv, use Python 3.13 -m venv .venv-rehearsal at repository root, then its python.exe to install documented requirements and execute from capstone. Add that venv name to .gitignore first. Do not replace your working environment.
7. Fix the precise missing import/dependency/path or README step, then repeat the affected scenario. A result is verified only when observed, not because it is listed in expected.md.

</details>
