# Help — Imports, modules, and entry points

## First hint

Keep transformation in main and printing under the guard.

## Detailed approach

Use from text_rules import normalize_city. Loop through arguments, normalize, and append nonempty values. sys.argv[0] is the script path; actual arguments begin at index 1. An importable function should receive inputs explicitly rather than reading global sys.argv itself.

## Troubleshooting

If a checker waits for input, input() is probably at module scope. A ModuleNotFoundError may indicate an incorrect sibling filename.

Read the first failing check, compare input/type/output and side effects, then make one focused change. The checker is an executable specification.
