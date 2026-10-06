# Help — Parquet and explicit storage schemas

## First hint

Construct using an explicit column list before applying the dtype mapping.

## Detailed approach

Use DataFrame(rows, columns=[...]).astype({...}). Call to_parquet then read_parquet and to_dict('records'). Do not convert cents to a display string. The checker independently reads your file, so returning input without a correct write does not pass.

## Troubleshooting

Missing pyarrow is a setup error. An index column means index=False was omitted. Empty frames need the same casts before writing.

Read the first failing check, compare input/type/output and side effects, then make one focused change. The checker is an executable specification.
