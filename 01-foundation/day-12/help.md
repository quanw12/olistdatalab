> Refreshed workflow: write DDL in schema.sql, run it on weather_day09, then run the provided fixture.sql once. The fixture load is now separate from your table definitions. Follow guide.md for this order.

# Day 12 — Syntax hints and troubleshooting

Use the matching hint after trying for 15–20 minutes. schema.sql specifies the required columns; this file explains how to express them.

Attempt the smallest case and write its expected result first. Open one section only when you can name the obstacle; record the highest hint used in notes.md.

<details>
<summary>1. I do not know where to write my answers</summary>

- model.md: design explanations, diagram, dictionary, assumptions, and reflections.
- schema.sql: complete CREATE TABLE statements under TODO 1–3.
- queries.sql: your three SELECT reports and their explanations.
- checks.sql: execute the provided statements; there are no answers to write.

Save the workspace file before opening or copying it into pgAdmin. If you change a query there, copy the final version back to the workspace.

</details>

<details>
<summary>2. CREATE TABLE syntax</summary>

Use the unrelated table shape in lesson.md's Required SQL syntax section. Choose each weather table's columns and constraints from schema.sql:

```text
CREATE TABLE schema_name.table_name (
    first_column TYPE constraints,
    second_column TYPE constraints,
    table_constraint
);
```

This is a syntax shape, not executable SQL. Replace the placeholders with schema.sql's actual names and types.

Useful executable fragments **inside a table definition**:

```sql
city_key INTEGER GENERATED ALWAYS AS IDENTITY PRIMARY KEY,
source_city_id INTEGER NOT NULL UNIQUE,
city_name TEXT NOT NULL UNIQUE CHECK (btrim(city_name) <> ''),
timezone_name TEXT NOT NULL CHECK (btrim(timezone_name) <> '')
```

Those are dim_city's column definitions. Supply CREATE TABLE and the surrounding parentheses yourself. btrim removes outside spaces; the CHECK rejects an empty or whitespace-only value.

For the fact, a reference has this shape:

```sql
city_key INTEGER NOT NULL
    REFERENCES day12_mart.dim_city (city_key),
observation_date DATE NOT NULL
    REFERENCES day12_mart.dim_date (calendar_date)
```

Put a comma after each definition except the final definition or constraint. After the other fact columns, add this **table constraint**:

```sql
UNIQUE (city_key, observed_at)
```

Both columns form one combination. It does not mean city_key must be unique by itself.

</details>

<details>
<summary>3. Which key goes where?</summary>

| Purpose | Column |
|---|---|
| Identify a mart city | dim_city.city_key |
| Find that city using a source ID | dim_city.source_city_id |
| Reference the mart city from a fact | fact_weather.city_key |
| Identify a calendar date | dim_date.calendar_date |
| Reference that date from a fact | fact_weather.observation_date |
| Identify a stored fact row | fact_weather.observation_key |
| Prevent repeating the observation | UNIQUE (city_key, observed_at) |

A column's numeric value is not proof that it refers to the same thing as another column. Follow the keys and the mapping.

</details>

<details>
<summary>4. A relation or schema does not exist</summary>

Check which phase you are in:

1. Before building, only checks.sql B1–B2 can run.
2. Fill all three schema.sql TODOs before running its full transaction.
3. After DDL succeeds, run fixture.sql once; then A1–A6 and queries.sql.

If public.cities is missing, inspect the selected database. It should be weather_day09.

Refresh the Schemas node in pgAdmin after a successful build. Refreshing the tree does not create tables; it only updates the displayed object list.

</details>

<details>
<summary>5. The transaction failed</summary>

Common follow-on error:

```text
current transaction is aborted, commands ignored until end of transaction block
```

1. Find the **first error** in Messages; later errors may be consequences.
2. In that same Query Tool connection, execute this by itself:

```sql
ROLLBACK;
```

3. Run this read-only inspection:

```sql
SELECT to_regnamespace('day12_mart') AS existing_schema;
```

4. If it returns NULL, fix the saved file and rerun the complete build.
5. If it returns day12_mart, inspect A1–A6. A prior build may already have succeeded, or objects may have been created separately. Share the first error and saved SQL if the model is incomplete.

If pgAdmin already rolled the transaction back, ROLLBACK may say there is no transaction in progress. The namespace inspection determines what exists.

DDL and fixture loading use separate transactions. A failed load leaves earlier committed tables in place. Inspect the first error before retrying fixture.sql; do not drop source tables or skip transaction completion.

</details>

<details>
<summary>6. day12_mart already exists</summary>

CREATE SCHEMA fails if the schema exists. The fixture guard stops a second load if target rows exist. Inspect the model before deciding what remains necessary:

```sql
SELECT table_name
FROM information_schema.tables
WHERE table_schema = 'day12_mart'
  AND table_type = 'BASE TABLE'
ORDER BY table_name;
```

Expected table names: dim_city, dim_date, fact_weather.

If the model is not correct, save your SQL and request a review before deciding how to repair existing objects.

</details>

<details>
<summary>7. A duplicate or foreign-key error occurs during the first build</summary>

- A duplicate on (city_key, observation_date) often means you chose a daily key for an observation table. Use the required city/observed_at pair.
- A foreign-key error can mean you referenced a source ID rather than the mart city key, or loaded facts before dimensions.
- A duplicate generated-key error can occur if you manually supplied generated keys. The provided load omits those columns.
- Check the table definition and the first failing statement before changing the data.

The provided load is for an empty, newly built model. Day 13 introduces loading from Python and handling existing observations.

</details>

<details>
<summary>8. Report syntax hints</summary>

### Q1: join using actual keys

```sql
FROM day12_mart.fact_weather AS f
INNER JOIN day12_mart.dim_city AS c
    ON c.city_key = f.city_key
INNER JOIN day12_mart.dim_date AS d
    ON d.calendar_date = f.observation_date
```

Supply the selected columns and final sort from queries.sql. Eight facts should produce eight joined rows because the dimension keys are unique and the references exist.

### Q2: report grain

Use the same joins. Your grouping must identify a city and date:

```sql
GROUP BY c.city_key, c.city_name, d.calendar_date
ORDER BY c.city_name ASC, d.calendar_date ASC;
```

For the measures:

```sql
COUNT(*) AS observation_count,
ROUND(AVG(f.temperature_c), 2) AS avg_temperature_c,
ROUND(AVG(f.humidity_pct), 2) AS avg_humidity_pct
```

Do not group by observed_at here; that would retain separate observations instead of daily groups.

### Q3: keep Hue

Start from the dimension:

```sql
FROM day12_mart.dim_city AS c
LEFT JOIN day12_mart.fact_weather AS f ON f.city_key = c.city_key
```

COUNT(f.observation_key) ignores the NULL fact key for Hue. AVG also ignores NULL input and returns NULL when there are no measurements. A final WHERE condition requiring a fact value would remove Hue.

</details>

<details>
<summary>9. Reflection prompts</summary>

Use examples rather than memorized definitions:

- R1: compare Hanoi's 09:00 and 12:00 observations on the same date.
- R2: imagine inserting the same city/instant twice while letting PostgreSQL generate a new observation_key each time.
- R3: use the example mapping source_city_id 8 → city_key 100.
- R4: compare two times on one date and the UTC/local midnight example.
- R5: compare Ho Chi Minh City's two-observation day and one-observation day.
- R6: ask whether a missing observation provides evidence of a 0 C measurement.

Reference: [PostgreSQL constraints](https://www.postgresql.org/docs/18/ddl-constraints.html), [transactions](https://www.postgresql.org/docs/18/tutorial-transactions.html), [aggregate functions](https://www.postgresql.org/docs/18/functions-aggregate.html).

</details>
