# Day 10 tutorial — From observations to reports

Run the examples on **weather_day09** in pgAdmin. All examples read data or calculate results; they do not change the tables. Read the matching section before attempting an exercise.

## 1. Start with a question and a row meaning

An observation row means **one city at one observation instant**. A city summary row means **one city across several observations**. A daily report row means **one city on one chosen local date**.

Before writing SQL, ask:

1. What should one result row represent?
2. Which rows contribute to it?
3. Which values should I calculate?
4. Should cities with missing data still appear?

For example, Hue exists in cities but has no observations. An INNER JOIN omits it. A LEFT JOIN preserves it with NULL observation fields. COUNT(*) then counts its unmatched joined row; COUNT(o.observed_at) counts zero real observations.

This matters in Data Engineering: a report should distinguish missing data from a measured zero. Today's final report practices that distinction.

## 2. Local time, calendar dates, and casts — Q1

observed_at is TIMESTAMPTZ: it represents an instant. A calendar date depends on the timezone in which you view that instant.

Type and run this small example first. It does not need a table:

```sql
SELECT
    TIMESTAMPTZ '2026-09-18 17:30:00+00:00'
        AT TIME ZONE 'Asia/Ho_Chi_Minh' AS local_time,
    (TIMESTAMPTZ '2026-09-18 17:30:00+00:00'
        AT TIME ZONE 'Asia/Ho_Chi_Minh')::date AS local_date,
    (TIMESTAMPTZ '2026-09-18 17:30:00+00:00'
        AT TIME ZONE 'UTC')::date AS utc_date;
```

Expected: local_time **2026-09-19 00:30:00**, local_date **2026-09-19**, utc_date **2026-09-18**.

Read the expression from the inside out:

| Syntax | Meaning here |
|---|---|
| TIMESTAMPTZ '...' | A timestamp literal with an explicit offset |
| AT TIME ZONE 'Asia/Ho_Chi_Minh' | View this instant as a Vietnam local clock reading |
| (...) | Keep the conversion together before the next operation |
| ::date | Convert that local timestamp to its date part |
| AS local_date | Label the result column |

For a TIMESTAMPTZ input, AT TIME ZONE returns a timestamp without timezone: the wall-clock reading in the chosen zone. It does not rewrite observed_at in the database. Keep the original instant when storing observations.

`CAST(expression AS date)` is another way to write `expression::date`.

Now apply the pattern to a column:

```sql
SELECT
    city_id,
    observed_at,
    (observed_at AT TIME ZONE 'Asia/Ho_Chi_Minh')::date AS local_date
FROM weather_observations
ORDER BY city_id, observed_at;
```

There are eight rows. Notice the two different local dates.

In Q1, join cities and use c.timezone_name instead of the fixed timezone text. An alias such as local_time is an output label, not a Python variable available to the next SELECT expression. Repeat the conversion when calculating local_date.

**Try:** change the first example's timezone to UTC and predict its date. Then write Q1.

References: [Date/time types](https://www.postgresql.org/docs/18/datatype-datetime.html), [AT TIME ZONE](https://www.postgresql.org/docs/18/functions-datetime.html#FUNCTIONS-DATETIME-ZONECONVERT), [type casts](https://www.postgresql.org/docs/18/sql-expressions.html#SQL-SYNTAX-TYPE-CASTS).

## 3. Filter a day and group by date — Q2–Q3

A complete day starts at midnight and ends just before the next midnight. Use an inclusive start and an exclusive end:

```sql
SELECT city_id, observed_at, temperature_c
FROM weather_observations
WHERE observed_at >= TIMESTAMPTZ '2026-09-19 00:00:00+07:00'
  AND observed_at < TIMESTAMPTZ '2026-09-20 00:00:00+07:00'
ORDER BY city_id, observed_at;
```

Expected: two observations, Hanoi at **31.0** and Ho Chi Minh City at **32.0**. This example selects September 19; Q2 asks for September 18 and city names.

BETWEEN includes both endpoints. Including the next midnight would count the first instant of the following day. Avoid guessing an end such as 23:59:59, because timestamps can include fractional seconds.

For a daily summary, calculate the local-date expression in SELECT and GROUP BY:

```sql
SELECT
    (observed_at AT TIME ZONE 'Asia/Ho_Chi_Minh')::date AS local_date,
    COUNT(*) AS observation_count
FROM weather_observations
GROUP BY (observed_at AT TIME ZONE 'Asia/Ho_Chi_Minh')::date
ORDER BY local_date;
```

Expected: **2026-09-18 → 6**, **2026-09-19 → 2**. The result now has one row per date. Grouping by the full observed_at would keep separate observation times instead.

**Try:** add MAX(humidity_pct) to the daily summary. Predict the two values: 85 and 75. Then write Q2 and Q3.

References: [BETWEEN and comparison predicates](https://www.postgresql.org/docs/18/functions-comparison.html), [GROUP BY](https://www.postgresql.org/docs/18/queries-table-expressions.html#QUERIES-GROUP).

## 4. CASE creates a value for each row — Q4

Think of CASE as an expression that chooses a result, similar to Python if/elif/else:

```sql
SELECT
    city_id,
    humidity_pct,
    CASE
        WHEN humidity_pct >= 80 THEN 'humid'
        WHEN humidity_pct >= 70 THEN 'moderate'
        ELSE 'lower'
    END AS humidity_band
FROM weather_observations
ORDER BY city_id, observed_at;
```

WHEN supplies a condition, THEN its result, ELSE the fallback, and END closes CASE. The first true condition wins. For humidity 85, the output is humid. For 75, it is moderate. With no ELSE and no matching WHEN, the result would be NULL.

Put specific thresholds before broader overlapping ones. If >= 70 came first here, 85 would match moderate before reaching humid.

**Try:** predict the labels for 65, 70, 79, and 80. Then change the first threshold to 85 and run the example. Q4 applies a similar pattern to temperature, using its specified exercise thresholds.

Reference: [CASE](https://www.postgresql.org/docs/18/functions-conditional.html#FUNCTIONS-CASE).

## 5. Conditional counts and missing values — Q5

CASE can turn each matching row into 1 and each other row into 0. SUM then adds the flags:

```sql
SELECT
    c.city_name,
    COUNT(o.observed_at) AS observation_count,
    SUM(CASE WHEN o.humidity_pct >= 80 THEN 1 ELSE 0 END)
        AS humid_observation_count
FROM cities AS c
LEFT JOIN weather_observations AS o
    ON o.city_id = c.city_id
GROUP BY c.city_id, c.city_name
ORDER BY c.city_name;
```

Expected humid counts: Da Nang **2**, Hanoi **1**, Ho Chi Minh City **0**, Hue **0**. For Hue's unmatched row, the condition is not true and ELSE supplies 0.

Do not write COUNT(CASE WHEN ... THEN 1 ELSE 0 END) for this task: both 1 and 0 are non-NULL, so COUNT would count both. SUM adds their values.

Another tool, COALESCE, chooses the first non-NULL argument:

```sql
SELECT
    COALESCE(NULL::bigint, 0) AS missing_count,
    COALESCE(3::bigint, 0) AS known_count;
```

Expected: 0 and 3. In Q10, a city missing from the summary has a NULL joined count, so COALESCE can report zero observations. A missing temperature stays NULL; replacing it with zero would invent a measurement.

**Try:** change the humidity threshold to 85. Only Da Nang should have one matching observation. Then write Q5 using temperature >= 32.

References: [COUNT and SUM](https://www.postgresql.org/docs/18/functions-aggregate.html), [COALESCE](https://www.postgresql.org/docs/18/functions-conditional.html#FUNCTIONS-COALESCE-NVL-IFNULL).

## 6. Scalar subqueries supply a calculated value — Q6–Q7

Sometimes you need to compare a row with a value calculated from many rows. Run the inner calculation first:

```sql
SELECT AVG(humidity_pct) AS overall_avg_humidity_pct
FROM weather_observations;
```

The average is **73.125**, possibly displayed with additional decimal places. Now use that SELECT inside parentheses:

```sql
SELECT city_id, observed_at, humidity_pct
FROM weather_observations
WHERE humidity_pct > (
    SELECT AVG(humidity_pct)
    FROM weather_observations
)
ORDER BY humidity_pct DESC, city_id, observed_at;
```

Four rows qualify: humidity values 85, 80, 80, and 75. The scalar subquery supplies one comparison value. Do not add a semicolon inside the parentheses; the semicolon belongs at the end of the complete statement.

A scalar subquery must have one column and at most one returned row. Multiple rows cause an error; no rows produce NULL. AVG without GROUP BY produces one summary row, making it appropriate here. The database chooses how to execute the query; the inner-then-outer explanation describes its meaning.

For an overall maximum, use the same pattern with MAX and equality. Equality to a maximum retains every tied maximum observation. ORDER BY ... LIMIT 1 selects only one row.

**Try:** change AVG(humidity_pct) to MAX(humidity_pct) and > to =. The result should identify Da Nang's 85% observation. Then write Q6 and Q7 for temperature.

Reference: [Scalar subqueries](https://www.postgresql.org/docs/18/sql-expressions.html#SQL-SYNTAX-SCALAR-SUBQUERIES).

## 7. EXISTS asks whether a matching row exists — Q8

Use EXISTS when the question is about the presence of data, rather than a calculated number:

```sql
SELECT c.city_name
FROM cities AS c
WHERE EXISTS (
    SELECT 1
    FROM weather_observations AS o
    WHERE o.city_id = c.city_id
)
ORDER BY c.city_name;
```

Expected: Da Nang, Hanoi, Ho Chi Minh City. Each city appears once, even if it has several observations.

The inner query refers to the outer c.city_id. This is a correlated subquery: it asks whether an observation belongs to the city being considered. SELECT 1 is a conventional way to show that the selected value does not matter; the presence of a row matters.

NOT EXISTS reverses the condition: keep the city only when there is no matching observation. Do not remove the matching condition, or the question becomes whether any observation exists anywhere.

**Try:** predict the result with NOT EXISTS. Then write Q8.

Reference: [EXISTS](https://www.postgresql.org/docs/18/functions-subquery.html#FUNCTIONS-SUBQUERY-EXISTS).

## 8. A CTE gives a query step a name — Q9

CTE means Common Table Expression. WITH gives an intermediate query result a name within one statement:

```sql
WITH city_counts AS (
    SELECT city_id, COUNT(*) AS observation_count
    FROM weather_observations
    GROUP BY city_id
)
SELECT city_id, observation_count
FROM city_counts
WHERE observation_count >= 3
ORDER BY city_id;
```

Expected: city IDs **1 and 3**, each with count **3**.

| Part | Purpose |
|---|---|
| WITH city_counts AS (...) | Name the result of the inner SELECT |
| Inner GROUP BY | Produce one row per city ID |
| FROM city_counts | Read those summary rows |
| Outer WHERE | Filter the already-calculated observation_count column |

The outer WHERE is valid because observation_count is now an input column from city_counts. In the inner grouped SELECT, filtering COUNT(*) would require HAVING. A CTE does not create a permanent table, and its name is unavailable to a later statement.

Highlight the entire WITH block **and** final SELECT together. End the full statement with one semicolon after ORDER BY. Do not put a semicolon after the closing CTE parenthesis.

A CTE helps organize reasoning; it does not automatically make a query faster. Focus on clear steps today.

**Try:** run the inner SELECT alone to inspect all three groups. Change the outer threshold to 2. Then write Q9 using city names and average temperature.

Reference: [SELECT in WITH](https://www.postgresql.org/docs/18/queries-with.html#QUERIES-WITH-SELECT).

## 9. Combine the steps into a report — Q10

You now know the building blocks. The final report asks: **What happened in each city on September 18, including cities without observations?**

Build it in this order:

1. Write a SELECT from weather_observations with the day's timestamp bounds. Verify that six rows qualify.
2. Group those rows by city_id. Calculate count, average, and maximum. Verify three summary rows.
3. Put that grouped query inside WITH daily_summary AS (...).
4. Read cities AS c in the final SELECT, and LEFT JOIN daily_summary AS d on city_id. The report should now have four rows.
5. Apply COALESCE to the count, ROUND to the average, and CASE to the report status.
6. Check Hue carefully: count 0, average NULL, maximum NULL, status no data.

This small example shows the summarize-then-join shape using all dates and a different metric:

```sql
WITH humidity_summary AS (
    SELECT city_id, MAX(humidity_pct) AS max_humidity_pct
    FROM weather_observations
    GROUP BY city_id
)
SELECT c.city_name, h.max_humidity_pct
FROM cities AS c
LEFT JOIN humidity_summary AS h
    ON h.city_id = c.city_id
ORDER BY c.city_name;
```

Expected maxima: Da Nang **85**, Hanoi **80**, Ho Chi Minh City **70**, Hue **NULL**.

Q10's CTE selects a day before aggregation. Its final CASE checks missing data first, then the hot threshold, then uses normal as the fallback. Without the missing-data condition, Hue could incorrectly receive normal.

Avoid adding a final WHERE on d's values that discards Hue. Filtering the observations inside the CTE lets the final LEFT JOIN preserve every city.

This pattern will return later when your pipeline builds an analytics table: select the relevant raw rows, summarize them at a defined grain, and expose a report with explicit missing-data behavior.

## 10. Practise technical English

| Term | Meaning today |
|---|---|
| Boundary | Where a date range begins or ends |
| Inclusive | The boundary value is included |
| Exclusive | The boundary value is excluded |
| Scalar | One value |
| Correlated | The inner query refers to the outer query |
| Intermediate | A result used by a later step in the same statement |
| Fallback | A value used when another choice is unavailable |

Use simple sentences for explanations: "This query compares each humidity value with the overall average." Write your exercise explanations in your own words.
