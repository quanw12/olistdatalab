# Help — Spark schemas, plans and distributed-processing decisions

## First hint

An action's output and a plan are different evidence.

## Detailed approach

The inspected latest installation docs require Java 17 or later; verify the exact selected release rather than treating a latest page as a pin. Use explicit schema and built-in sum. Do not install this into the dbt environment. Check NULL behavior and join keys. Record before/after row counts. Explain which operation introduces a shuffle and how a skewed key could concentrate work. Keep collect limited to tiny demonstrated output.

## Troubleshooting

A Java gateway error is environment setup, not a SQL logic failure. local[2] is two local worker threads, not two cluster machines.

If stuck, write the smallest input, expected result and actual result. Check interpreter, cwd, schema and units before changing multiple things. Preserve the error; do not silently return success.

