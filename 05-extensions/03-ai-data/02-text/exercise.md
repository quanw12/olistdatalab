# AI02 — Assignment

Implement normalize_text(text). Reject non-strings with ValueError. Apply NFC; convert CRLF and CR to LF; strip whitespace from each line; collapse consecutive empty lines into at most one empty line (at most two newline characters between nonempty lines); strip the overall leading/trailing whitespace. Return a string. All-blank input returns "". Preserve internal spaces within a nonempty line. The function must be idempotent.

Write regressions for Windows newlines, decomposed accents, repeated blank lines and a paragraph with two internal spaces.

## Deliver

Submit your implementation, your own regression tests and the evidence listed in [expected.md](expected.md). Explain one changed input before committing.
