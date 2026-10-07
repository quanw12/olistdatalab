# Logical backups and verified recovery

A rollback protects an uncommitted transaction. A durable batch ledger helps replay.
Neither recovers a lost database. A backup is useful only when you can restore and
verify it within an acceptable loss/time window.

pg_dump creates a consistent logical dump of one database. -Fc selects a custom
archive, restored by pg_restore. pg_restore --list inspects its contents without a
database connection. A logical database dump is not a whole-cluster backup; roles
and other global objects are separate. This exercise does not teach continuous
archiving or point-in-time recovery.

## Required commands and SQL

| Syntax | Purpose |
|---|---|
| pg_dump -d source -Fc -f archive.dump | Write a custom-format logical archive. |
| pg_restore --list archive.dump | Inspect archived tables/data/constraints. |
| pg_restore -d empty_target --single-transaction --exit-on-error archive.dump | Restore atomically or fail. Specify the target deliberately. |
| psql -v ON_ERROR_STOP=1 -f file.sql | Make an SQL script failure stop command execution. |
| COUNT(*), SUM(...), ORDER BY key | Compare counts, units and complete key/value state. |
| information_schema.table_constraints | Inspect primary/check/foreign-key constraint evidence. |
| BEGIN; ... ROLLBACK; | Test an invalid write in a disposable transaction without retaining it. |

Use a pg_dump client at least as new as the server it dumps; an older client cannot
dump a newer server. For this lab use the installed PostgreSQL 18 tool set throughout.
Restoring across versions needs compatibility testing, not an assumed guarantee.

**RPO** is the acceptable data-loss window. An isolated dump cannot contain changes
committed afterward. **RTO** is the acceptable recovery duration, including making
the restored application/data usable. Distinguish your measured drill time from a
promised service objective.

Verify row/key/value state, relationships, constraints and report meaning. A matching
row count can hide changed units or a missing tombstone. The supplied source mutation
after backup deliberately demonstrates what this recovery point excludes.

The guide gives operational syntax. Your own verification queries and recovery note
are the exercise. Use pgAdmin with native PostgreSQL; no Docker is needed.

References: [pg_dump](https://www.postgresql.org/docs/18/app-pgdump.html),
[pg_restore](https://www.postgresql.org/docs/18/app-pgrestore.html).
