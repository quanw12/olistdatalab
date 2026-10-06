# Day 11 tutorial — SQL window functions

Use pgAdmin on **weather_day09**. Keep the eight fixed observations unchanged. Run one complete example at a time. Examples using VALUES create a small result inside a query; they do not insert records into your tables.

## 1. Summarize while keeping each observation — Q1

You already know how to summarize several observations into one row per city:

```sql
SELECT city_id, ROUND(AVG(humidity_pct), 1) AS city_avg_humidity_pct
FROM weather_observations
GROUP BY city_id
ORDER BY city_id;
```

This returns three rows: Hanoi's city ID 1 averages 75.0, Da Nang's ID 2 averages 82.5, and Ho Chi Minh City's ID 3 averages 65.0.

Now keep the original observations and put the average beside each one:

```sql
SELECT
    city_id,
    observed_at,
    humidity_pct,
    ROUND(AVG(humidity_pct) OVER (PARTITION BY city_id), 1)
        AS city_avg_humidity_pct
FROM weather_observations
ORDER BY city_id, observed_at;
```

This returns eight rows. Hanoi's three observations each show the same city average of 75.0, alongside their individual humidity values 80, 70, and 75.

| Method | Meaning of one output row | Result size here |
|---|---|---:|
| GROUP BY city_id with AVG | One city summary | 3 |
| AVG OVER (PARTITION BY city_id) | One observation, with a city average attached | 8 |

PARTITION BY separates rows for the calculation without merging them into a single output row. Without PARTITION BY, OVER () uses all the input observations together.

**Try:** run AVG(humidity_pct) OVER () instead. Every row should display the overall average 73.125 before rounding. Then complete Q1 using temperature and the city-name join.

Reference: [PostgreSQL window tutorial](https://www.postgresql.org/docs/18/tutorial-window.html).

## 2. Read the OVER clause in pieces

An aggregate window expression can specify three things:

```sql
AVG(temperature_c) OVER (
    PARTITION BY city_id
    ORDER BY observed_at ASC
    ROWS BETWEEN 2 PRECEDING AND CURRENT ROW
)
```

| Part | Question it answers | Meaning in this example |
|---|---|---|
| AVG(temperature_c) | What do I calculate? | Mean temperature |
| OVER (...) | Which window specification applies? | The rules inside the parentheses |
| PARTITION BY city_id | Which rows belong together? | Separate history for each city |
| ORDER BY observed_at ASC | In which order do I process them? | Earlier observations first |
| ROWS BETWEEN ... | Which positions contribute to this aggregate? | Current row and up to two earlier rows |

This is an expression to put inside a SELECT list, not a complete statement by itself. You will run its full form in section 7.

For Q1, there is no ordering requirement inside AVG's OVER clause: the question needs the entire city's average. Adding ORDER BY changes the default aggregate frame and can produce a running result instead. Use explicit ROWS frames when you mean trailing or running calculations.

There are two separate ORDER BY roles:

```text
Inside OVER: controls the calculation's order.
At the end of SELECT: controls the displayed result's order.
```

Sorting the final output does not make LAG chronological by itself. Its own OVER clause needs the correct order.

ROW_NUMBER, ranking functions, and LAG use the partition and ordering rules. The ROWS frames taught below control the aggregate functions AVG, COUNT, and MAX.

Reference: [Window-call syntax and frames](https://www.postgresql.org/docs/18/sql-expressions.html#SYNTAX-WINDOW-FUNCTIONS).

## 3. ROW_NUMBER numbers rows inside a partition — Q2

Type this complete example:

```sql
SELECT
    city_id,
    observed_at,
    humidity_pct,
    ROW_NUMBER() OVER (
        PARTITION BY city_id
        ORDER BY observed_at ASC
    ) AS observation_number
FROM weather_observations
ORDER BY city_id, observed_at;
```

The number starts at 1 for each city. Hanoi gets 1, 2, 3; Da Nang gets 1, 2; Ho Chi Minh City gets 1, 2, 3.

ROW_NUMBER() has empty parentheses because its partition and order determine the numbering. The primary key prevents two observations for the same city at the same instant, so observed_at gives a unique order within each city's history here. In other datasets, tied ordering values need a suitable extra key for deterministic numbering.

**Try:** change the window order to DESC, while keeping the final display order ASC. The earliest Hanoi row now displays number 3 and the latest displays 1. The calculation and display orders are independent. Then complete Q2.

Reference: [ROW_NUMBER](https://www.postgresql.org/docs/18/functions-window.html).

## 4. Filter a window result through a CTE — Q3

A useful pattern is to number observations and then select one per city. This runnable example selects the **earliest**, not latest, observation:

```sql
WITH numbered AS (
    SELECT
        city_id,
        observed_at,
        temperature_c,
        ROW_NUMBER() OVER (
            PARTITION BY city_id
            ORDER BY observed_at ASC
        ) AS observation_number
    FROM weather_observations
)
SELECT city_id, observed_at, temperature_c
FROM numbered
WHERE observation_number = 1
ORDER BY city_id;
```

Expected: Hanoi at 30.0, Da Nang at 29.0, Ho Chi Minh City at 33.0, all at September 18 09:00+07.

The inner query computes the number as a column. The outer query can then filter that column. PostgreSQL does not permit window calls directly in WHERE, and an output alias is not available to WHERE in the same SELECT.

Highlight the entire WITH block and final SELECT together. The semicolon ends the final SELECT; do not place one between the CTE and its consumer.

**Try:** change only the window order to DESC and predict each city's selected temperature. Then complete Q3 with city names and latest observations.

References: [Filtering after window calculations](https://www.postgresql.org/docs/18/tutorial-window.html), [WITH queries](https://www.postgresql.org/docs/18/queries-with.html).

## 5. RANK versus DENSE_RANK when values tie — Q4

Use this small demo before ranking the real weather rows:

```sql
WITH demo_readings(reading_id, temperature_c) AS (
    VALUES ('A', 35.0), ('B', 35.0), ('C', 32.0), ('D', 31.0)
)
SELECT
    reading_id,
    temperature_c,
    ROW_NUMBER() OVER (ORDER BY temperature_c DESC, reading_id) AS row_position,
    RANK() OVER (ORDER BY temperature_c DESC) AS temperature_rank,
    DENSE_RANK() OVER (ORDER BY temperature_c DESC) AS temperature_dense_rank
FROM demo_readings
ORDER BY temperature_c DESC, reading_id;
```

demo_readings is a CTE. Its header names the two columns supplied by each VALUES pair. No weather table is changed.

Expected:

| reading_id | temperature_c | row_position | temperature_rank | temperature_dense_rank |
|---|---:|---:|---:|---:|
| A | 35.0 | 1 | 1 | 1 |
| B | 35.0 | 2 | 1 | 1 |
| C | 32.0 | 3 | 3 | 2 |
| D | 31.0 | 4 | 4 | 3 |

ROW_NUMBER assigns distinct positions. RANK gives ties the same position and leaves a gap afterward. DENSE_RANK gives ties the same position and advances to the next distinct-value rank without a gap.

For temperature ties, RANK and DENSE_RANK order by temperature only inside OVER. Adding reading_id there would make A and B different ordering combinations and break their tie. The final ORDER BY can still include reading_id for stable display.

**Try:** change B to 34.0. Predict all three number columns. Then complete Q4: it ranks all observations together, with no city partition. The real dataset has ties at 32.0 and 30.0.

References: [Ranking definitions and peers](https://www.postgresql.org/docs/18/functions-window.html), [VALUES](https://www.postgresql.org/docs/18/queries-values.html).

## 6. LAG reads the previous available observation — Q5

Run this example using humidity:

```sql
WITH previous_readings AS (
    SELECT
        city_id,
        observed_at,
        humidity_pct,
        LAG(humidity_pct) OVER (
            PARTITION BY city_id
            ORDER BY observed_at ASC
        ) AS previous_humidity_pct
    FROM weather_observations
)
SELECT
    city_id,
    observed_at,
    humidity_pct,
    previous_humidity_pct,
    humidity_pct - previous_humidity_pct AS humidity_change_pct_points
FROM previous_readings
ORDER BY city_id, observed_at;
```

For Hanoi's three rows, the previous humidity values are NULL, 80, 70. The changes are NULL, -10, +5 percentage points.

LAG(value) defaults to one row backward. Its first result is NULL because the partition has no earlier row. Replacing that with zero would invent a previous measurement and a misleading change.

The CTE also lets you use previous_humidity_pct as an input column in the outer subtraction. You cannot reuse a newly defined SELECT alias in another expression of that same SELECT list.

"Previous" means the previous available row in the window order. Here the noon observation on September 18 and the 09:00 observation on September 19 are 21 hours apart. LAG does not create missing hourly observations or guarantee a one-hour difference.

**Try:** inspect Da Nang's second humidity change: it should be -5. Then complete Q5 for temperature. Leave unavailable previous values and changes as NULL.

Reference: [LAG](https://www.postgresql.org/docs/18/functions-window.html).

## 7. Explicit frames for a trailing average — Q6

For a trailing average, specify exactly which rows contribute. Run this four-row demo:

```sql
WITH demo_readings(reading_number, temperature_c) AS (
    VALUES (1, 10.0), (2, 20.0), (3, 30.0), (4, 40.0)
)
SELECT
    reading_number,
    temperature_c,
    ROUND(AVG(temperature_c) OVER (
        ORDER BY reading_number
        ROWS BETWEEN 2 PRECEDING AND CURRENT ROW
    ), 2) AS rolling_avg_3_c,
    COUNT(*) OVER (
        ORDER BY reading_number
        ROWS BETWEEN 2 PRECEDING AND CURRENT ROW
    ) AS frame_row_count,
    ROUND(AVG(temperature_c) OVER (
        ORDER BY reading_number
        ROWS BETWEEN UNBOUNDED PRECEDING AND CURRENT ROW
    ), 2) AS running_avg_c
FROM demo_readings
ORDER BY reading_number;
```

Expected:

| reading_number | temperature_c | rolling_avg_3_c | frame_row_count | running_avg_c |
|---:|---:|---:|---:|---:|
| 1 | 10.0 | 10.00 | 1 | 10.00 |
| 2 | 20.0 | 15.00 | 2 | 15.00 |
| 3 | 30.0 | 20.00 | 3 | 20.00 |
| 4 | 40.0 | 30.00 | 3 | 25.00 |

At row 4:

```text
Trailing three-row frame: [20, 30, 40] -> 30
Running frame from the start: [10, 20, 30, 40] -> 25
```

2 PRECEDING means up to two positions before the current row; CURRENT ROW includes the current position. There is no padding at the beginning: the first frame contains one row and the second contains two.

ROWS counts observations, not elapsed time. For the real weather data, a three-observation frame can span 24 hours. A three-day interval would require different window semantics; we will not introduce those today.

In Q6, add PARTITION BY o.city_id so each city has its own history. AVG and COUNT must use the same frame. ROUND applies after the window AVG is calculated.

Because every real city has at most three observations, an incorrect unbounded average could accidentally match Q6's numbers. The explicit frame is still required; the four-row demo shows why it matters.

**Try:** use 1 PRECEDING instead. The fourth rolling mean should become 35.00 with a frame count of 2. Then complete Q6 with 2 PRECEDING.

Reference: [ROWS frame boundaries](https://www.postgresql.org/docs/18/sql-expressions.html#SYNTAX-WINDOW-FUNCTIONS).

## 8. A running maximum retains the peak so far — Q7

UNBOUNDED PRECEDING starts at the partition's first row. CURRENT ROW ends at the current observation. Run this example using humidity:

```sql
SELECT
    city_id,
    observed_at,
    humidity_pct,
    MAX(humidity_pct) OVER (
        PARTITION BY city_id
        ORDER BY observed_at ASC
        ROWS BETWEEN UNBOUNDED PRECEDING AND CURRENT ROW
    ) AS running_max_humidity_pct
FROM weather_observations
ORDER BY city_id, observed_at;
```

Hanoi's running maximum is 80, 80, 80. Ho Chi Minh City's is 65, 65, 70. A lower current measurement does not reduce the previous maximum.

For a historical feature, this frame includes only measurements up to the current row. MAX(...) OVER (PARTITION BY city_id) would instead use the entire city's input history, including later observations.

**Try:** change MAX to MIN and predict Hanoi's sequence: 80, 70, 70. Then complete Q7 using temperature and MAX.

References: [Aggregate windows](https://www.postgresql.org/docs/18/functions-window.html), [frame syntax](https://www.postgresql.org/docs/18/sql-expressions.html#SYNTAX-WINDOW-FUNCTIONS).

## 9. Combine history features with the latest record — Q8

The final question is: **For every city, what is the latest temperature, how did it change, and what is its trailing mean?**

Build this in stages:

1. Read all observations and calculate LAG in chronological order per city.
2. Calculate the trailing three-observation AVG on the same full history.
3. Separately number each city's rows newest first using ROW_NUMBER.
4. Put those results inside the observation_features CTE.
5. Start the final SELECT from cities so Hue can appear.
6. LEFT JOIN the features, matching only latest_number = 1.
7. Calculate the change and trend label in the outer SELECT.

Different features can have different window orders in the same statement. LAG and the rolling average use ASC to look backward in time. Latest numbering uses DESC so the newest observation gets 1.

Use this final join shape:

```sql
FROM cities AS c
LEFT JOIN observation_features AS f
    ON f.city_id = c.city_id
   AND f.latest_number = 1
```

Do not put f.latest_number = 1 in a final WHERE: Hue's joined number is NULL, so that condition would remove it. The condition in ON limits the match while preserving the left-side city.

Calculate the history features before selecting only the latest row. If the window input contains just one row per city, LAG has no predecessor and the rolling average becomes just the latest temperature.

For the final CASE, check missing data first, then a missing predecessor, then compare the current and previous temperatures. The available data should produce Da Nang warming, Hanoi cooling, Ho Chi Minh City cooling, Hue no data. Keep Hue's measurements as NULL.

These labels describe the change between available measurements. They do not establish a long-term trend or predict future weather.

This exercise creates a report in memory. Later lessons will teach how to model and load reports into an analytics table.

References: [LEFT JOIN behavior](https://www.postgresql.org/docs/18/queries-table-expressions.html#QUERIES-JOIN), [window inputs after filtering](https://www.postgresql.org/docs/18/tutorial-window.html).

## 10. Technical English and a syntax checklist

| Term | Meaning in this lesson |
|---|---|
| Partition | Rows belonging to one calculation group |
| Peer | Another row with equal values for the window's ordering expressions |
| Preceding | Earlier position in the specified order |
| Trailing | Current position and some earlier positions |
| Running | From the beginning up to the current position |
| Frame | Positions contributing to an aggregate window calculation |
| Predecessor | The previous available row |

Before running a query, check:

- Every window function has its OVER clause.
- Each city calculation has PARTITION BY city_id.
- The window order answers the actual question.
- Aggregate frame boundaries are explicit when required.
- A CTE surrounds a calculation whose output needs further filtering or alias reuse.
- The final ORDER BY makes the displayed result predictable.

Begin explanations with simple sentences such as: "This query keeps each humidity observation and shows the average for its city." Use your own words for the exercise explanations.
