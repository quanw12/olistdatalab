# Help — Query plans, indexes and measured optimization

Attempt the smallest case and write its expected result first. Open one section only when you can name the obstacle; record the highest hint used in notes.md.

<details>
<summary>First hint</summary>

Change one design choice while holding query results constant.

</details>

<details>
<summary>Detailed approach</summary>

Create benchmark_events rather than modifying source-course tables. Use generate_series(1,50000) with a timestamp base plus numbered intervals. Measure a narrow range and a broad range. Use CREATE INDEX on observed_at, then ANALYZE benchmark_events. Run the same EXPLAIN SELECT again. If plans do not change, discuss selectivity/table size/cache rather than disabling the planner to force your preferred result.

</details>

<details>
<summary>Troubleshooting</summary>

A faster wrong query is not an improvement. Repeated tests warm caches. Costs are planner units, not milliseconds. An index does not guarantee ordered output without ORDER BY.

</details>
