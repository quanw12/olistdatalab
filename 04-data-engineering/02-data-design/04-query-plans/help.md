# Help — Query plans, indexes and measured optimization

## First hint

Change one design choice while holding query results constant.

## Detailed approach

Create benchmark_events rather than modifying source-course tables. Use generate_series(1,50000) with a timestamp base plus numbered intervals. Measure a narrow range and a broad range. Use CREATE INDEX on observed_at, then ANALYZE benchmark_events. Run the same EXPLAIN SELECT again. If plans do not change, discuss selectivity/table size/cache rather than disabling the planner to force your preferred result.

## Troubleshooting

A faster wrong query is not an improvement. Repeated tests warm caches. Costs are planner units, not milliseconds. An index does not guarantee ordered output without ORDER BY.

If stuck, write the smallest input, expected result and actual result. Check interpreter, cwd, schema and units before changing multiple things. Preserve the error; do not silently return success.

