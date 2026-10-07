# DE27 assignment

Ticket: determine whether fixtures/source.csv can support a current stock report
by site. Identify questions and defects before building a production loader.

## Discover

Write discovery.md with at least five observations and five focused owner questions.
Propose row grain and candidate identities. Then read [owner-brief.md](fixtures/owner-brief.md)
and mark which questions it resolves and which guarantees remain unconfirmed.

## Implement a profile

Implement profile_source(csv_path) -> dict in profile.py; accept a Path or path string.
Required header, in order: item_id, site_id, observed_at, units, version, contact_email.
Missing/duplicate/reordered headers, extra cells or missing cells fail the whole file
with ValueError. File-system failures propagate.

Preserve all rows. For measurements, strip each cell's surrounding whitespace.
Return this structure:

~~~text
row_count: all data rows, including defective/duplicate rows
column_stats: entry per column, containing blank_count and distinct_nonblank_count
candidate_keys: these two entries in order:
  {"columns": ["item_id"], "duplicate_excess": ...}
  {"columns": ["item_id", "site_id", "version"], "duplicate_excess": ...}
parse_failures: observed_at, units, version counts
~~~

duplicate_excess counts rows beyond the first for identical keys, including keys
with blanks. Distinct counts compare stripped raw text, not normalized time.
Header-only input returns zero counts with the same structure.

Diagnostic rules: observed_at parses as an offset-aware ISO datetime; units is
nonempty ASCII decimal digits for a nonnegative integer; version is nonempty ASCII
decimal digits for an integer >= 1. Blanks fail parsing. Count each field independently;
one row can fail several. These are declared diagnostics, not inferred production rules.

Add --input and --output CLI options. Write the dictionary as UTF-8 JSON, create
the output parent if needed, and return nonzero on failure. Imports must not execute
the CLI. No third-party package is needed.

## Hand off meaning

Write catalog.md: source/owner, grain, keys, field types/units/null meaning, refresh,
sensitivity, lab retention/access and unresolved guarantees.
Write lineage.md mapping source fields through latest-state selection to a proposed
site-stock report. Define report grain, units, invalid/conflicting-version treatment
and when publication must stop. Do not implement another loader.
Give the consumer a 100–150 word handoff with evidence, confirmed rules, unresolved
risks and next action.

## Independent variation

Use a scratch source with a conflicting repeated composite key and two offset
strings representing one instant. Predict raw counts versus semantic identity.
Keep the supplied fixture unchanged.
