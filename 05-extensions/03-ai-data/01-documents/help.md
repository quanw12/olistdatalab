# AI01 — Progressive help

Attempt the smallest case and write its expected result first. Open one section only when you can name the obstacle; record the highest hint used in notes.md.

<details>
<summary>After an attempt — supporting explanation</summary>

Attempt the task before opening each hint. These hints describe the method; implement the final solution yourself.

### Hint 1 — validate before indexing/search

Reject malformed structure at the ingestion boundary. Do not convert True or "2" into a document revision.

### Hint 2 — clean identifiers, preserve raw text

Strip id/source_uri as documented. Preserve text unchanged here so text normalization has its own explicit boundary.

### Hint 3 — test a revision change

Two versions of the same id represent an edit, not two unrelated documents. Test missing provenance and check that the input retains its extra keys after your call.

[Return to the assignment](exercise.md)

</details>
