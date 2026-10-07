# Help — Capstone: reproducible retail ingestion

Attempt the smallest case and write its expected result first. Open one section only when you can name the obstacle; record the highest hint used in notes.md.

<details>
<summary>First hint</summary>

Finish one stage at a time: parse, clean/reject, merge versions, transact, report, publish.

</details>

<details>
<summary>Detailed approach</summary>

1. Validate the four-field CSV header before touching the database. Keep raw dictionaries and enumerate parsed data records starting at 2.
2. Reject in order: blank order_id -> id; blank city -> city; invalid amount -> amount; invalid/naive updated_at -> time. Reuse exact cents and UTC conversion.
3. Hash original file bytes. Build accepted records and rejected records before loading.
4. Create schema if absent, then commit setup. Begin one transaction for data plus ledger. Read current clean state, apply the C14-L01 winner rules, upsert resulting state, and insert the batch ledger. A conflict must escape so rollback happens.
5. If this batch ID already exists, leave orders/ledger unchanged but continue to generate artifacts from current state and this input's rejection list.
6. Query current order count and SUM(amount_cents), using zero for an empty state. Build city totals sorted by name. Do not sum raw rows containing replays.
7. Write rejected JSONL and the report to unique temporary siblings then replace each destination. Finally write the manifest similarly. Cleanup only your own temporary files.
8. Prove replay after a newer correction does not revert that correction. Simulate publication failure using a file where an output directory is expected, then retry with a proper directory.
Keep run_pipeline as the coordinator. Helpers should not print. Use a finally block to close database connections even when publication fails.

</details>

<details>
<summary>Troubleshooting</summary>

Base total 5100 means the duplicate A2 was counted twice. Total 102850 after the second fixture means stale A1=999.00 overwrote its newer value. A missing report after replay means you returned early when seeing the ledger entry.

Read the first failing check, compare input/type/output and side effects, then make one focused change. The checker is an executable specification.

</details>

<details>
<summary>Suggested function boundaries</summary>

Design the program before joining its steps:

| Helper responsibility | Input | Output or effect |
|---|---|---|
| Read and verify shape | CSV path/bytes | Raw dictionaries |
| Validate one row | Raw dictionary | Clean record or a rejection reason |
| Apply version policy | Existing state + clean records | Proposed new state, or a conflict |
| Load one batch | Connection + proposed rows + batch ID | One committed transaction |
| Build report | Current stored rows | Sorted city totals and counts |
| Publish artifact | Destination + serialized content | Temporary-sibling replacement |
| Coordinate | Three paths | Manifest dictionary |

These are design suggestions, not required function names. Only run_pipeline is the public function checked directly. Begin with pure transformations so you can test them without file or database setup.

Test milestones in order: one valid CSV -> one rejected row -> duplicate -> correction -> stale row -> conflicting equal version -> failed output directory. After each milestone, run one small manual fixture and inspect counts. Then run the complete checker.

For the batch ledger, a parameterized SELECT can check whether the content hash exists. Do not mark a batch as complete before its row changes commit. Do not return early for a known batch: report generation must still use current database state.

</details>
