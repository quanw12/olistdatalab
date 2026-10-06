# Exit status, conditions and deliberate failure

## Concept and purpose

Zero conventionally means success; nonzero means another outcome. $? holds the last command's status. && runs the next command on success; || runs it on failure. Use if command; then ... else ... fi to inspect expected failure.

[[ -f "$path" ]] tests a regular file; -r tests readability. A missing source must not be replaced silently with empty data. set -u detects unset variables and pipefail propagates failed pipeline components. set -e has exceptions in conditions and compound commands; explicit handling remains necessary.

A grep with no matches exits 1, which differs from a source-processing error. Interpret statuses under each program's contract.

## Syntax example — Bash in Ubuntu

~~~bash
if grep 'not-present' "$LE_COURSE_ROOT/data/runs.log"; then
    printf 'matched\n'
else
    result=$?
    printf 'grep status=%s\n' "$result"
fi
~~~

## Trace the example

No match returns 1. Save that value before printf changes the last status.

## Apply it to Data Engineering

Schedulers cannot detect a failure if a wrapper exits successfully.

[Reference](https://www.gnu.org/software/bash/manual/bash.html#Exit-Status). These explanations and exercises are original course material.
