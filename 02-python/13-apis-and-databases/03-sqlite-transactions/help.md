# Help — Parameterized SQL and transaction rollback

## First hint

Use ? placeholders and bind ordered tuples separately.

## Detailed approach

Build tuples in field order. Enter with connection, call executemany once, save rowcount and return after the context succeeds. A failed operation must leave the block through an exception so rollback happens. Do not commit each row.

## Troubleshooting

Apostrophes breaking your SQL indicate interpolation. If a valid first row remains after a later bad row, transaction boundaries are wrong.

Read the first failing check, compare input/type/output and side effects, then make one focused change. The checker is an executable specification.
