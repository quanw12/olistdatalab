# LAB03 — Learn

## A migration changes a live contract

The operations team now wants a warehouse zone. Existing rows have no zone. An additive column with a documented default can preserve old inserts while new code begins supplying it. This is a teaching SQLite migration; native PostgreSQL locking and rollout behavior must be tested separately.

## Syntax — SQLite

~~~sql
ALTER TABLE shipments
ADD COLUMN label TEXT NOT NULL DEFAULT 'unassigned';
~~~
This unrelated example shows ADD COLUMN, a type, a null constraint and a default. The default applies to inserts that omit the column; it does not make an explicit NULL valid. A transaction can roll back an uncommitted DDL change in this SQLite lab. After commit, a rollback command cannot undo it: use a tested reverse migration or restore strategy.

Do not drop/recreate the table just to gain a column. Review DE05–DE06 for constraints, transactions and connection ownership. Plan expand → update writer → verify → later retire old behavior.

[Assignment](exercise.md) · [Hints](help.md)
