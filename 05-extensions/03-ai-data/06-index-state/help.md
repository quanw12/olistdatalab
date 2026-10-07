# AI06 — Progressive help

Attempt the smallest case and write its expected result first. Open one section only when you can name the obstacle; record the highest hint used in notes.md.

<details>
<summary>After an attempt — supporting explanation</summary>

Attempt the task before opening each hint. These hints describe the method; implement the final solution yourself.

### Hint 1 — validate complete evidence

Check every field and list element in both state/event, even when the event is stale. A missing digest is not an identical replay.

### Hint 2 — branch on revision once

No state → new. Older → unchanged. Equal → compare the complete canonical state. Higher → replacement, including deletes.

### Hint 3 — plan first, commit later

Copy returned nested lists. In the real indexer, execute removals/additions/state change in one local transaction; do not mark the document current before chunks are replaced.

[Return to the assignment](exercise.md)

</details>
