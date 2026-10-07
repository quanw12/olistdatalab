# Day 11 hints and troubleshooting

Use lesson.md for complete runnable examples. This file gives the exact expressions and shapes to use when you get stuck. Keep your full answers in queries.sql.

Attempt the smallest case and write its expected result first. Open one section only when you can name the obstacle; record the highest hint used in notes.md.

<details>
<summary>Q1 — Full average beside each observation</summary>

Use the normal INNER JOIN to select city names. The added expression is:

```sql
ROUND(AVG(o.temperature_c) OVER (PARTITION BY o.city_id), 1)
    AS city_avg_temperature_c
```

Do not GROUP BY: that would collapse observations. Do not put ORDER BY inside this OVER clause: the exercise needs the average of all the city's observations. Only the final SELECT needs display ordering.

</details>

<details>
<summary>Q2 — Chronological numbering</summary>

```sql
ROW_NUMBER() OVER (
    PARTITION BY o.city_id
    ORDER BY o.observed_at ASC
) AS observation_number
```

ROW_NUMBER() has no value argument. It resets to 1 at each city. DESC would number the newest observation first, which is useful in Q3 but is not Q2's instruction.

</details>

<details>
<summary>Q3 — Number first, filter second</summary>

The inner joined SELECT returns the requested fields plus:

```sql
ROW_NUMBER() OVER (
    PARTITION BY o.city_id
    ORDER BY o.observed_at DESC
) AS latest_number
```

Wrap that SELECT, without a semicolon, inside WITH numbered AS (...). The outer query reads numbered and uses WHERE latest_number = 1. Do not place the window call or its alias directly in the inner WHERE. Hue is intentionally absent from this query.

</details>

<details>
<summary>Q4 — Keep equal temperatures tied</summary>

```sql
RANK() OVER (ORDER BY o.temperature_c DESC) AS temperature_rank,
DENSE_RANK() OVER (ORDER BY o.temperature_c DESC) AS temperature_dense_rank
```

No city partition is requested. Do not add observed_at or city_id inside these ranking windows, because equal temperatures would no longer be peers. Add the requested city-name/time tie breakers only to the final ORDER BY.

For 34, 33, 32, 32, 31, 30, 30, 29, ranks are 1, 2, 3, 3, 5, 6, 6, 8. Dense ranks are 1, 2, 3, 3, 4, 5, 5, 6.

</details>

<details>
<summary>Q5 — Use a CTE to subtract the previous value</summary>

Calculate this in the inner SELECT:

```sql
LAG(o.temperature_c) OVER (
    PARTITION BY o.city_id
    ORDER BY o.observed_at ASC
) AS previous_temperature_c
```

The outer SELECT can then use:

```sql
temperature_c - previous_temperature_c AS temperature_change_c
```

Subtraction is current minus previous. A positive value means an increase between those two observations. Keep the first previous value and first difference NULL. Do not apply COALESCE(..., 0).

</details>

<details>
<summary>Q6 — Exactly the requested observation frame</summary>

Type the same partition/order/frame for both AVG and COUNT:

```sql
PARTITION BY o.city_id
ORDER BY o.observed_at ASC
ROWS BETWEEN 2 PRECEDING AND CURRENT ROW
```

Write ROUND(AVG(...) OVER (...), 2), putting OVER next to AVG and ROUND around the completed window expression. Use COUNT(*) OVER (...) for frame_row_count. Do not round temperatures before averaging.

Two preceding positions plus the current position means up to three rows. Use the four-row tutorial to verify the difference from an unbounded running average; this small weather fixture alone cannot expose that mistake.

</details>

<details>
<summary>Q7 — Maximum so far</summary>

Use MAX(o.temperature_c), then OVER with a city partition, ascending observation order, and:

```sql
ROWS BETWEEN UNBOUNDED PRECEDING AND CURRENT ROW
```

This retains all earlier observations in the city's frame. Ordering DESC would look toward newer measurements instead and answer a different question.

</details>

<details>
<summary>Q8 — Build features before keeping the latest row</summary>

Start with a SELECT from weather_observations AS o that returns the three base columns and all three features:

- previous_temperature_c: LAG, city partition, ascending time.
- rolling_avg_3_c: AVG, city partition, ascending time, explicit trailing three-row frame.
- latest_number: ROW_NUMBER, city partition, descending time.

Run that inner SELECT alone. It should still have eight rows, including the full history for the three observed cities. Only then wrap it as observation_features.

The final SELECT starts with cities AS c and joins:

```sql
LEFT JOIN observation_features AS f
    ON c.city_id = f.city_id
   AND f.latest_number = 1
```

Its CASE is:

```sql
CASE
    WHEN f.observed_at IS NULL THEN 'no data'
    WHEN f.previous_temperature_c IS NULL THEN 'first observation'
    WHEN f.temperature_c > f.previous_temperature_c THEN 'warming'
    WHEN f.temperature_c < f.previous_temperature_c THEN 'cooling'
    ELSE 'stable'
END AS trend_status
```

Do not GROUP BY in the outer query. The row-number condition already limits the right-side match to at most one record per city. Keep missing fields as NULL, and round only the displayed rolling average.

</details>

<details>
<summary>Common problems</summary>

| Symptom | What to inspect |
|---|---|
| relation does not exist | Confirm current_database() is weather_day09 and the two tables exist. |
| Syntax error around OVER | Put OVER directly after AVG, ROW_NUMBER, RANK, DENSE_RANK, or LAG. For rounding, use ROUND(AVG(...) OVER (...), 2). |
| function row_number(integer) does not exist | Use ROW_NUMBER() with empty parentheses. |
| window functions are not allowed in WHERE | Compute the window column in a CTE, then filter it in the outer query. |
| latest_number or previous_temperature_c does not exist | Do not reuse a newly defined alias within the same SELECT; use the CTE output in another SELECT. |
| missing FROM-clause entry for o or c | Inner aliases are scoped to the CTE's inner SELECT. Use its output columns, or f in Q8's outer query. |
| Q1 produces three rows | Remove GROUP BY; the window result must retain each observation. |
| Q1 averages change within a city | Remove ORDER BY from that full-partition AVG window. |
| Q3 selects the earliest record | Use DESC inside the ROW_NUMBER window. |
| Q4 ties get different ranks | Rank by temperature only inside OVER; keep display tie breakers outside it. |
| LAG crosses city boundaries | Add PARTITION BY city_id. |
| LAG returns a newer measurement | Use ASC observation order. |
| First differences look like 29, 30, or 33 | Do not replace missing predecessors with zero. |
| Q6 counts more than three rows | Give COUNT the same trailing ROWS frame as AVG. |
| Q6 accidentally matches without its frame | The fixture has at most three rows per city; run the fourth-row tutorial and inspect the explicit syntax. |
| Q8 previous values are all NULL | Compute features on the full history before selecting latest rows. |
| Q8 omits Hue | Keep the latest-number condition in LEFT JOIN's ON clause, not final WHERE. |
| Only the last result appears | Highlight and execute one complete query at a time. |
| Starter queries.sql gives no results | It contains comments until you write the queries. |

</details>

<details>
<summary>Window calculations see filtered input</summary>

A WHERE inside the feature SELECT removes observations before its windows are calculated. Filtering to only September 19 there would discard the September 18 predecessors. Q8 needs all existing observations, so do not add that filter.

Today's exercises use observation positions. Irregular intervals do not become regular simply because LAG or ROWS is used. Check timestamps when interpreting a change.

If you need help, send the complete statement and the exact error. For a CTE, include its WITH block and final SELECT together.

</details>
