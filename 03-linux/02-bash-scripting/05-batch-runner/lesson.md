# A reusable batch runner with logs

## Concept and purpose

A wrapper coordinates paths, configuration, status and logs. It should not duplicate the data transformation. Resolve app.py from the runner's location using BASH_SOURCE[0], not the caller's pwd.

Keep stdout/stderr logs separate and propagate the child's exact status. Guard expected failures in an if so strict mode does not skip your error handling. Validate arity before positional access.

The lab is single-writer. Each invocation overwrites its run.log/error.log; it does not pretend that concurrent jobs have safe shared outputs.

## Syntax example — Bash in Ubuntu

~~~bash
if python3 -c 'raise SystemExit(2)'; then
    printf 'success\n'
else
    result=$?
    printf 'child failed with %s\n' "$result" >&2
fi
~~~

## Trace the example

Python returns 2, saved before the diagnostic print.

## Apply it to Data Engineering

An honest wrapper exposes application failures to scheduling and CI.

[Reference](https://www.gnu.org/software/bash/manual/bash.html#Bash-Variables). These explanations and exercises are original course material.
