# Checking your work

Two CSV files remain. cmp confirms the raw copy matches the shared fixture. Header: event_id,amount_cents. Last rows: BAD,-1 and ,500. The disposable file no longer exists.

## Reflection answer — reveal after your attempt

<details>
<summary>Show the explanation</summary>

An unquoted wildcard can expand to filenames in the current directory. Quoting passes the pattern literally so find applies it throughout its search scope.

</details>

Completion requires your own work and an explanation. Creating materials does not mark the lesson complete.
