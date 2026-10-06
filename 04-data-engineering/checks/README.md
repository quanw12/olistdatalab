# Verification scope

Eight offline contracts have checks: DE04, DE08, DE09, DE10, DE12, DE16, DE22 and optional DE24. The check infrastructure is provided; exercise implementations are not. DE12 needs the warehouse environment; other checks use standard Python. Each checker exits 1 for unfinished or incorrect work and 0 for the stated cases. Use --file to test a separate mutation copy.

Native PostgreSQL transactions, Prefect states, Docker delivery and optional platform labs require actual runtime evidence. No offline assertion certifies those environments. dbt commands are documented in DE13–DE15. The final assessment includes changed-input tests and explanation rather than treating fixture success as mastery.

After DE13's build, run check_dbt.py from the Engineering environment to inspect actual fixture tables. After DE15 add --incremental to compare the incremental entity table against latest_changes. This is an additional warehouse-output check, not a substitute for dbt data tests, changed-input experiments or live PostgreSQL integration.
