# Help — CLI options, configuration, and environments

## First hint

Validate CLI ranges after parsing and JSON schema after loading.

## Detailed approach

Use parser.error for invalid CLI values. For configuration use isinstance(data,dict), get on required keys, and type(size) is int to reject bool. Keep reading the config separate from starting the job.

## Troubleshooting

If missing options return None, you swallowed SystemExit. If True passes as a size, your type check is too broad.

Read the first failing check, compare input/type/output and side effects, then make one focused change. The checker is an executable specification.
