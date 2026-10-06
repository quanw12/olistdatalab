# Checking your work

Fixture -> status 0 and LE06 counts, JSON in run.log, empty error.log. Missing input ->2 and an error event on error.log. Wrong arity ->64, missing interpreter ->127. Another cwd and spaced paths work.

## Reflection answer — reveal after your attempt

<details>
<summary>Show the explanation</summary>

pwd belongs to the invoking terminal/scheduler. BASH_SOURCE[0] identifies the script independently of where it was invoked.

</details>

Completion requires your own work and an explanation. Creating materials does not mark the lesson complete.
