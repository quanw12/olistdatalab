# AI01 — Assignment

Implement canonical_document(raw). Require a dict with id, version, source_uri, text. Return exactly these four fields. id is a trimmed ASCII [A-Za-z0-9_-]{1,64} string; version is an exact positive int; source_uri is a trimmed nonempty string beginning https:// or local:// and has content after that prefix. This is a course provenance label, not a complete URL/security validator. text is a string with nonempty stripped content and length <=100000; preserve its original whitespace for AI02. Ignore extra keys. Missing/invalid fields raise ValueError; never mutate raw.

Read the supplied documents.json and explain which fields belong to source identity, revision and payload.

## Deliver

Submit your implementation, your own regression tests and the evidence listed in [expected.md](expected.md). Explain one changed input before committing.
