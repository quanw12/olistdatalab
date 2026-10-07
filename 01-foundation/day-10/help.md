# Day 10 hints and troubleshooting

Try the tutorial example first, change it once, then attempt the exercise. The snippets below are patterns, not ten finished answers.

Attempt the smallest case and write its expected result first. Open one section only when you can name the obstacle; record the highest hint used in notes.md.

<details>
<summary>Q1 — Convert before taking the date</summary>

Use the Day 9 INNER JOIN on city_id. Select the original observed_at too, so you can compare it with the converted local clock reading.

```sql
o.observed_at AT TIME ZONE c.timezone_name AS local_time,
(o.observed_at AT TIME ZONE c.timezone_name)::date AS local_date
```

Do not write local_time::date in the same SELECT list. Repeat the expression. All four configured city timezones are Asia/Ho_Chi_Minh.

</details>

<details>
<summary>Q2 — Select a complete calendar day</summary>

Put this WHERE block after the join and before ORDER BY:

```sql
WHERE o.observed_at >= TIMESTAMPTZ '2026-09-18 00:00:00+07:00'
  AND o.observed_at < TIMESTAMPTZ '2026-09-19 00:00:00+07:00'
```

Use AND because both bounds must hold. The explicit +07:00 identifies the timezone offset for these sample dates. A filter on only the day number 18 would ignore month and year.

</details>

<details>
<summary>Q3 — One row per local date</summary>

Use the same date expression in SELECT and GROUP BY:

```sql
(observed_at AT TIME ZONE 'Asia/Ho_Chi_Minh')::date
```

Add COUNT(*), ROUND(AVG(temperature_c), 2), MIN, and MAX. Grouping by city_id would answer a different question; grouping by the full timestamp would produce several rows per date.

</details>

<details>
<summary>Q4 — Three CASE branches</summary>

For ascending temperature thresholds, test the smallest band first:

```sql
CASE
    WHEN o.temperature_c < 30 THEN 'cool'
    WHEN o.temperature_c < 33 THEN 'warm'
    ELSE 'hot'
END AS temperature_band
```

The second branch implicitly starts at 30 because the first branch already handled lower values. Expected band totals: cool 1, warm 5, hot 2. These are exercise categories.

</details>

<details>
<summary>Q5 — Count condition matches, not all non-NULL flags</summary>

Use a LEFT JOIN from cities and group by its city ID and name. Select both:

```sql
COUNT(o.observed_at) AS observation_count,
SUM(CASE WHEN o.temperature_c >= 32 THEN 1 ELSE 0 END)
    AS hot_observation_count
```

Do not put the temperature condition in WHERE: that would remove nonmatching observations and Hue before aggregation. In this exercise, COUNT(*) would also give Hue the wrong total count.

</details>

<details>
<summary>Q6 — Run the inner average first</summary>

```sql
SELECT AVG(temperature_c)
FROM weather_observations;
```

It returns 31.375, possibly with extra decimal places. Put this query, without its semicolon, inside the outer comparison's parentheses. Use >, not >=, and compare with the calculated value without rounding it or typing a literal number.

</details>

<details>
<summary>Q7 — Equality preserves ties</summary>

Change the scalar aggregate to MAX and compare with =. The maximum is 34.0. A LIMIT 1 solution does not satisfy the requirement to return every tied maximum. Do not insert extra rows into the lesson tables to test ties; explain the behavior in words or use a small VALUES example separately.

</details>

<details>
<summary>Q8 — Correlate the subquery</summary>

The predicate inside the outer WHERE has this form:

```sql
NOT EXISTS (
    SELECT 1
    FROM weather_observations AS o
    WHERE o.city_id = c.city_id
)
```

c belongs to the outer query. Removing the inner WHERE changes the question to whether the whole observations table is empty. Today it is not empty, but Hue individually has no matching rows.

</details>

<details>
<summary>Q9 — Inspect the CTE before the final filter</summary>

1. Write and run a joined, grouped city summary alone. It should return three cities.
2. Wrap that SELECT, without its semicolon, inside WITH city_summary AS (...).
3. After the closing parenthesis, write the outer SELECT FROM city_summary.
4. Filter using the CTE's avg_temperature_c column, and round only the displayed average.

The aliases c and o exist inside the CTE's inner query. They are not available in the outer SELECT. Refer to the CTE output columns there.

</details>

<details>
<summary>Q10 — Build the report in layers</summary>

First finish the grouped daily_summary query using Q2's date bounds. It should return city IDs 1, 2, and 3, each with count 2.

Then wrap it as a CTE and use this final FROM block:

```sql
FROM cities AS c
LEFT JOIN daily_summary AS d
    ON d.city_id = c.city_id
```

Use COALESCE(d.observation_count, 0), but leave d.avg_temperature_c and d.max_temperature_c missing for Hue. The status expression is:

```sql
CASE
    WHEN d.observation_count IS NULL THEN 'no data'
    WHEN d.max_temperature_c >= 33 THEN 'hot'
    ELSE 'normal'
END AS report_status
```

A missing group creates no daily_summary row for Hue, so its joined count is NULL before COALESCE. The CTE already produces one row per city; the final join does not need another GROUP BY.

</details>

<details>
<summary>Common problems</summary>

| Symptom | What to check |
|---|---|
| relation does not exist | Run SELECT current_database(); open Query Tool from weather_day09 and confirm the existing tables. |
| local_time does not exist | An output alias cannot be reused in another expression of the same SELECT list; repeat the conversion. |
| Syntax error near SELECT after a CTE | Remove the semicolon between the closing CTE parenthesis and the final SELECT. |
| city_summary does not exist | Execute the complete WITH block and final SELECT as one statement. |
| missing FROM-clause entry for c or o | Those aliases may exist only inside the CTE. The outer SELECT reads CTE columns. |
| more than one row returned by a subquery used as an expression | A scalar subquery must return at most one row; use the requested aggregate without GROUP BY. |
| column must appear in GROUP BY | Include the selected date expression or requested city columns; do not add observation timestamps to city summaries. |
| aggregate functions are not allowed in WHERE | In a grouped query, aggregate filtering belongs in HAVING. In an outer query over a CTE summary, its columns can be filtered with WHERE. |
| Q5 reports Hue as 1 | Use COUNT(o.observed_at) for total observations, not COUNT(*). |
| Q5 hot count equals total count | Use SUM for the 1/0 CASE flags, not COUNT of those flags. |
| Q10 omits Hue | Check that cities is on the left and no final WHERE removes missing d values. |
| Q10 reports zero as Hue's temperature | Apply COALESCE only to the count. Missing measurements remain NULL. |
| Q10 marks Hue normal | Put the missing-data CASE branch first. |
| Timestamp display uses +00 | Run SET TIME ZONE 'Asia/Ho_Chi_Minh'; in this Query Tool tab. |
| No output from queries.sql | The starter contains comments only; write a real query under each TODO. |

If you are stuck, send the complete statement and the error text. For a CTE, include both the WITH block and final SELECT.

</details>
