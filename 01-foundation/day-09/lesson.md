# Day 9 lesson — Read, filter, join, and summarize

Day 8 taught the database's structure and rules. Today you ask questions of stored data. SQL is useful for DE pipeline checks and DA reports: the same tables can support both.

## 1. Understand the sample tables

The table grain is unchanged:

- `cities`: one row per city.
- `weather_observations`: one row per `(city_id, observed_at)`.

| City | ID in this fresh dataset | Observation count |
|---|---:|---:|
| Hanoi | 1 | 3 |
| Da Nang | 2 | 2 |
| Ho Chi Minh City | 3 | 3 |
| Hue | 4 | 0 |

Hue is a known city without weather data, not a city with temperature zero. Keep that distinction when reporting.

## 2. SELECT, FROM, and aliases

Run this example in pgAdmin after setup:

```sql
SELECT city_name, timezone_name
FROM cities
ORDER BY city_name;
```

- SELECT names the output columns.
- FROM names the source table.
- ORDER BY defines result ordering.
- Commas separate output expressions; `;` ends the statement.

SQL keywords are written in uppercase here for readability. Text values use single quotes; `city_name` is a column, while `'Hanoi'` is a text value.

An output alias labels a result column:

```sql
SELECT city_name AS city
FROM cities
ORDER BY city_name;
```

AS changes this output's label; it does not rename the stored column. Later, `cities AS c` gives a table a short name inside one query.

Reference: [PostgreSQL tutorial: querying a table](https://www.postgresql.org/docs/18/tutorial-select.html).

## 3. WHERE: select rows

```sql
SELECT city_id, temperature_c, humidity_pct
FROM weather_observations
WHERE temperature_c < 30
ORDER BY city_id;
```

This returns Da Nang's 29.0-degree observation. WHERE keeps rows whose condition is true.

| Operator | Meaning | Example |
|---|---|---|
| `=` | Equal | `city_id = 1` |
| `<>` | Not equal | `city_id <> 1` |
| `>=`, `<=` | Inclusive comparison | `temperature_c >= 32` |
| AND | Both conditions must be true | `temperature_c >= 32 AND humidity_pct <= 70` |
| OR | At least one condition must be true | `city_id = 1 OR city_id = 2` |
| BETWEEN | Inclusive range | `temperature_c BETWEEN 30 AND 32` |

Use parentheses when mixing AND and OR to make your meaning clear. SQL equality uses `=`, unlike Python's `==`.

## 4. ORDER BY, LIMIT, and DISTINCT

Ascending order is the default; DESC reverses it. Multiple sort columns resolve ties:

```sql
SELECT city_id, observed_at, temperature_c
FROM weather_observations
ORDER BY temperature_c ASC, city_id ASC, observed_at ASC
LIMIT 3;
```

This selects the three coolest observations in a defined order. LIMIT controls the number of result rows, not which rows are hottest or coolest. Without an appropriate ORDER BY, LIMIT does not guarantee a predictable selection.

DISTINCT removes duplicate output values:

```sql
SELECT DISTINCT source
FROM weather_observations
ORDER BY source;
```

Eight observations share one source, so this returns one row. DISTINCT applies to the entire selected combination when selecting multiple columns. It does not delete data or fix an incorrect join.

Reference: [PostgreSQL: LIMIT and ordering](https://www.postgresql.org/docs/18/queries-limit.html).

## 5. JOIN: connect observations to city names

An observation contains city_id, not city_name. Match its ID to the city's ID:

```sql
SELECT c.city_name, o.temperature_c
FROM cities AS c
INNER JOIN weather_observations AS o
    ON c.city_id = o.city_id
WHERE c.city_name = 'Da Nang'
ORDER BY o.observed_at;
```

| Part | Meaning |
|---|---|
| `cities AS c` | c is a short name for cities |
| `weather_observations AS o` | o is a short name for observations |
| `c.city_id` | city_id from cities |
| `ON c.city_id = o.city_id` | Match rows belonging to the same city |
| INNER JOIN | Keep matching pairs |

The example returns two rows: Da Nang at 29.0 and 30.0 degrees. One city row matches two observation rows; this is the one-to-many relationship from Day 8.

INNER JOIN excludes Hue because there is no matching observation. LEFT JOIN preserves all rows from the left table, with NULL values on the right for unmatched cities:

```sql
SELECT c.city_name, o.observed_at
FROM cities AS c
LEFT JOIN weather_observations AS o
    ON c.city_id = o.city_id
ORDER BY c.city_name, o.observed_at;
```

This returns nine rows: eight observations plus Hue's unmatched row. A missing or incorrect matching condition can multiply rows and distort reports. Join on the IDs, not unrelated fields.

Reference: [PostgreSQL tutorial: joins](https://www.postgresql.org/docs/18/tutorial-join.html).

## 6. Aggregates: summarize values

```sql
SELECT
    COUNT(*) AS observation_count,
    ROUND(AVG(humidity_pct), 1) AS avg_humidity_pct
FROM weather_observations;
```

This returns one row: count 8, average humidity 73.1. With no GROUP BY, you summarize the whole selected input.

| Function | Meaning |
|---|---|
| COUNT(*) | Count input rows |
| COUNT(column) | Count non-NULL values in that column |
| AVG(column) | Mean of non-NULL values |
| MIN(column), MAX(column) | Smallest/largest non-NULL values |
| ROUND(value, 1) | Round this numeric result to one decimal place |

For this dataset's numeric temperature values, `ROUND(AVG(temperature_c), 2)` rounds the computed mean to two places. Compute the mean before rounding it.

Reference: [PostgreSQL aggregate function definitions](https://www.postgresql.org/docs/18/functions-aggregate.html).

## 7. GROUP BY and HAVING

Grouping changes the output grain from one observation to one city summary:

```sql
SELECT city_id, COUNT(*) AS observation_count
FROM weather_observations
GROUP BY city_id
ORDER BY city_id;
```

This produces IDs 1, 2, 3 with counts 3, 2, 3. If you select a normal column alongside an aggregate, include it in GROUP BY. In the joined exercises, explicitly group by both c.city_id and c.city_name.

WHERE filters input rows; HAVING filters groups after aggregation:

```sql
SELECT city_id, COUNT(*) AS observation_count
FROM weather_observations
WHERE temperature_c >= 30
GROUP BY city_id
HAVING COUNT(*) >= 2
ORDER BY city_id;
```

First the 29.0-degree row is removed. The remaining city counts are 3, 1, 3. HAVING then keeps only IDs 1 and 3.

For this lesson, think in this order:

```text
FROM / JOIN -> WHERE -> GROUP BY -> HAVING -> SELECT -> ORDER BY -> LIMIT
```

This is a learning model for query meaning, not a promise about the database's physical execution plan. Write clauses in their normal SQL order, with SELECT first. Use `HAVING COUNT(*) >= 3`, not `WHERE COUNT(*) >= 3` or `HAVING observation_count >= 3`.

Reference: [PostgreSQL tutorial: WHERE and HAVING](https://www.postgresql.org/docs/18/tutorial-agg.html).

## 8. LEFT JOIN, NULL, and counting

For Hue, LEFT JOIN creates one result row with no observation values:

| city_name | observed_at | temperature_c |
|---|---|---|
| Hue | NULL | NULL |

Therefore COUNT(*) counts **one joined row**, while COUNT(o.observed_at) counts **zero actual observations**. observed_at is mandatory for real observations, making it suitable for this count.

AVG(o.temperature_c) is NULL for Hue because no temperature is available. Zero would mean a known temperature of 0 degrees, which is different. Do not replace missing weather with zero.

To test a missing value, use `IS NULL`, not `= NULL`:

```sql
SELECT c.city_name
FROM cities AS c
LEFT JOIN weather_observations AS o
    ON c.city_id = o.city_id
WHERE o.observed_at IS NULL
ORDER BY c.city_name;
```

This returns Hue. A WHERE condition such as `o.temperature_c >= 30` would exclude the unmatched row; remember this when preserving all cities.

Reference: [PostgreSQL table expressions and outer joins](https://www.postgresql.org/docs/18/queries-table-expressions.html).

## 9. Practise technical English

| Word | Meaning in this lesson |
|---|---|
| Retrieve | Read data from a table |
| Filter | Keep rows or groups meeting a condition |
| Match | Connect rows using equal keys |
| Aggregate | Summarize several values |
| Unmatched | No corresponding row in the other table |
| Grain | What one row represents |

Write simple explanations, such as: "This query keeps observations below 30 degrees." You do not need complicated English. Explain the input, condition, and output clearly.
