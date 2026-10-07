# ST05 — Progressive help

Attempt the smallest case and write its expected result first. Open one section only when you can name the obstacle; record the highest hint used in notes.md.

<details>
<summary>After an attempt — supporting explanation</summary>

Attempt the task before opening each hint. These hints describe the method; implement the final solution yourself.

### Hint 1 — preserve an audit identity

Copy the validated position fields and digest the exact bytes, not a decoded/normalized replacement.

### Hint 2 — keep reasons safe and bounded

Use a fixed validation message rather than echoing a credential-bearing payload. Reject embedded newlines.

### Hint 3 — do not conflate outbox and broker

Commit the local rejection before acknowledging its input. An outbox dispatcher can retry publishing; receivers must deduplicate repeated rejection IDs.

[Return to the assignment](exercise.md)

</details>
