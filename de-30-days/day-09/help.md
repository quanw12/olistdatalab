# Day 9 hints and troubleshooting

Try each query yourself first. If stuck for 15–20 minutes, read its hint, then type the SQL. The runnable examples in [lesson.md](lesson.md) provide the full syntax patterns.

## Q1 — Columns and order

Use SELECT for the three requested columns, FROM cities, then ORDER BY city_name. Columns are separated with commas, not AND. ASC is optional because it is the default.

## Q2 — Observations

Use FROM weather_observations. The ORDER BY clause needs two columns: city_id first, observed_at second. It must not sort all cities only by time.

## Q3 — Filter rows

Put this after FROM and before ORDER BY:

```sql
WHERE temperature_c >= 32 AND humidity_pct <= 70
```

Sort temperature descending, then city ID and observation time ascending. Expect four rows; both conditions must hold.

## Q4 — Unique IDs

Start with `SELECT DISTINCT city_id`. Use weather_observations as the source. Hue is in cities but absent from observations, so its ID should not appear.

## Q5 — Hottest two

Use the specified ORDER BY, ending the statement with `LIMIT 2;`. ASC would select the coolest rows. LIMIT without sorting does not mean hottest.

## Q6 — Match IDs

Use this FROM/JOIN block beneath the selected output columns:

```sql
FROM cities AS c
INNER JOIN weather_observations AS o
    ON c.city_id = o.city_id
```

Use c.city_name for the name, and o for observation columns. Both tables have city_id, so qualify it with the appropriate table alias.

## Q7 — One summary row

Use the four aggregate expressions requested in queries.sql, separated by commas, then FROM weather_observations. Do not add GROUP BY: the question asks for one overall summary. Write `ROUND(AVG(temperature_c), 2)`.

## Q8 — Summary per observed city

Use the Q6 join. In SELECT, use c.city_name plus COUNT(*), ROUND(AVG(o.temperature_c), 1), MIN(o.temperature_c), and MAX(o.temperature_c). Label each expression using AS and the requested output names.

After the join, write:

```sql
GROUP BY c.city_id, c.city_name
ORDER BY c.city_name
```

Add the semicolon after the final clause. Hue is excluded by the INNER JOIN.

## Q9 — Filter groups

Start with the joined, grouped city count. Between GROUP BY and ORDER BY, add:

```sql
HAVING COUNT(*) >= 3
```

Use COUNT(*) directly here, not the output alias observation_count. Do not put aggregate conditions in WHERE.

## Q10 — Include Hue

Start from cities AS c and change the join to LEFT JOIN. Count real observations with:

```sql
COUNT(o.observed_at) AS observation_count
```

Group by both city ID and name. AVG ignores the unmatched NULL temperature, leaving a NULL result for Hue. Do not add a WHERE condition that removes unmatched observations.

## Common query errors

| Error/symptom | What to inspect |
|---|---|
| relation does not exist | Run SELECT current_database(); it should be weather_day09. Confirm setup succeeded and Tables contains both tables. |
| column reference city_id is ambiguous | Both joined tables have that column. Use c.city_id or o.city_id. |
| column must appear in GROUP BY | Add selected nonaggregate columns to GROUP BY; do not group by temperature when seeking one summary per city. |
| aggregate functions are not allowed in WHERE | Move the aggregate condition to HAVING. |
| Q6 returns 32 rows | Four cities multiplied by eight observations: inspect the join condition. |
| Q10 reports Hue count = 1 | COUNT(*) counts its unmatched joined row. Use COUNT(o.observed_at). |
| Q10 omits Hue | Check for INNER JOIN or a WHERE condition on observation values. |
| Only the last result is visible | Highlight and execute one query at a time. |
| Nothing happens when running queries.sql | The starter contains comments only. Write a SELECT statement below a TODO. |
| Wrong table counts | Confirm the database name and inspect data; do not rerun setup or delete data to hide the difference. |

## Setup errors

If setup fails inside its transaction, execute this statement alone in the same Query Tool tab:

```sql
ROLLBACK;
```

Correct the reported problem before trying again. The database-name guard means you opened Query Tool on the wrong database. A table-already-exists error means you should inspect the existing lesson tables rather than rerun creation. The setup file has no deletion commands.

## Same instant, different timestamp display

Run this in the Query Tool tab displaying a different offset:

```sql
SET TIME ZONE 'Asia/Ho_Chi_Minh';
```

It affects the current connection. Reopening Query Tool may require setting it again. Leave observed_at as a timestamp in today's exercises; formatting and date transformations come in Day 10.
