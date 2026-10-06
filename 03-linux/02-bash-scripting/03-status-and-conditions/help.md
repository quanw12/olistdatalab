# Help — Exit status, conditions and deliberate failure

## First hint

The final successful command can determine the wrapper's status.

## Detailed approach

Check $# before reading $1. Test [[ -f "$1" && -r "$1" ]]. For failure use printf to >&2, then exit the chosen code. For success print ready only. Strict mode is optional; expected outcomes still need explicit branches. Run as a normal account so permission behavior is meaningful.

## Troubleshooting

An error message alone does not fail a script. Using only -e allows directories and violates the input contract.

Change one thing at a time. Preserve the complete error message and confirm your shell, working directory, input path and interpreter before guessing.
