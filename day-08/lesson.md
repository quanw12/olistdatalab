# Day 8 — How a database protects your data contract

## 1. From Day 7's JSON to tables

Day 7 produced a clean weather record. Today you design the database that will store many such records. Define the **grain** first: what does one row represent?

| Table | One row represents | Key |
|---|---|---|
| `cities` | One city | `city_id` |
| `weather_observations` | One observation for a city at a time | `(city_id, observed_at)` |

A city has many observations. Store the city's name once in `cities`; each observation uses `city_id` to refer to it.

| Day 7 field | Database column | Purpose |
|---|---|---|
| `city` | `cities.city_name` | City name |
| `timezone` | `cities.timezone_name` | City's local timezone |
| `requested_at` | `weather_observations.requested_at` | Time the pipeline called the API |
| `observed_at` | `weather_observations.observed_at` | Time the weather was observed |
| `temperature_c`, `humidity_pct`, `source` | Same names in `weather_observations` | Values for this observation |

Later, Python will look up a city ID before inserting weather data. Today `seed.sql` uses IDs 1 and 2 in a fresh database so you can focus on the schema.

The word **schema** has two uses here. Your `schema.sql` file defines the table structure. PostgreSQL also has named schemas such as `public`, which group tables inside a database. The default connection for this exercise creates your tables in `public`.

## 2. Choose column types

| Column | PostgreSQL type | Meaning |
|---|---|---|
| `city_id` in `cities` | `INTEGER GENERATED ALWAYS AS IDENTITY` | Server generates an integer ID |
| `city_id` in observations | `INTEGER` | Existing city's ID, not a new generated ID |
| Names and source | `TEXT` | Text values |
| Observation/request times | `TIMESTAMPTZ` | A specific instant in time |
| Temperature | `NUMERIC(4,1)` | Four total digits, one after the decimal point |
| Humidity | `SMALLINT` | Small integer |

`NUMERIC(4,1)` can hold the exercise's range of -50.0 to 60.0. The type alone does not enforce that range; a CHECK constraint does.

`TIMESTAMPTZ` normalizes instants internally and displays them in the session's timezone. It does **not** retain the original timezone name such as `Asia/Ho_Chi_Minh`, so keep that name separately.

Day 7's API time `2026-09-18T11:30` has no offset. Before real ingestion, attach the correct timezone; otherwise PostgreSQL interprets it using the connection's timezone. The sample SQL explicitly includes `+07:00`. For example, `11:30+07:00` and `04:30+00:00` on the same date represent the same instant.

## 3. Constraints: rules enforced by PostgreSQL

| Constraint | Rule | Invalid example |
|---|---|---|
| PRIMARY KEY | Identifies a row; no NULL or duplicates | Same city/time pair inserted twice |
| UNIQUE | Values must not duplicate | Two rows named `Hanoi` |
| FOREIGN KEY | References a row in another table | Observation for nonexistent city 999 |
| NOT NULL | Value is required | NULL source |
| CHECK | Value must satisfy a condition | Humidity 130 |

A table has one primary key, but it can include multiple columns. The observation key is the **pair** `(city_id, observed_at)`.

CHECK alone does not reject NULL: `CHECK (humidity_pct BETWEEN 0 AND 100)` needs `NOT NULL` as well when humidity is mandatory. A nonblank CHECK also differs from NOT NULL: `''`, `'   '`, and NULL are different values.

These database rules protect data even if another Python script skips Day 7's validation. They do not replace all pipeline checks: for example, this exercise's nonblank timezone rule does not verify that a timezone name actually exists.

## 4. Read CREATE TABLE syntax

This small example demonstrates the syntax; it is not the complete answer to the exercise:

```sql
CREATE TABLE cities (
    city_id INTEGER GENERATED ALWAYS AS IDENTITY PRIMARY KEY,
    city_name TEXT NOT NULL,
    timezone_name TEXT NOT NULL,
    CONSTRAINT uq_cities_city_name UNIQUE (city_name),
    CONSTRAINT ck_cities_city_name_nonempty CHECK (btrim(city_name) <> '')
);
```

- `CREATE TABLE cities` asks PostgreSQL to create the table.
- Parentheses contain columns and table rules, separated by commas.
- Each column has a name, a type, and optional rules such as NOT NULL.
- `CONSTRAINT name ...` names a rule so errors are easier to interpret.
- `btrim(city_name)` removes spaces at both ends; `<> ''` means not empty.
- There is no comma after the final item. `;` ends the statement.

Read this example, then complete the five TODOs in your saved `schema.sql`. Do not execute the example separately before the exercise, because it would create an incomplete `cities` table with the same name.

## 5. How to practise

For each rule, think of one valid value and one value it should reject. Follow [guide.md](guide.md) to execute your completed schema in pgAdmin, insert `seed.sql`, and read the results with `verify.sql`.

Then run the guide's separate invalid INSERT examples. Successful sample loading proves valid data is accepted; expected errors prove invalid data is rejected. Inspect constraints in pgAdmin's tree and match their names to the errors.

Saving SQL changes the file. Executing SQL changes the database. Editing a CREATE TABLE script after execution does not update an existing table; stop and ask for help if your table structure and saved script differ.

## References for today's topics

- [PostgreSQL: creating tables](https://www.postgresql.org/docs/current/tutorial-table.html)
- [PostgreSQL: constraints](https://www.postgresql.org/docs/current/ddl-constraints.html)
- [PostgreSQL: date/time types](https://www.postgresql.org/docs/current/datatype-datetime.html)
- [pgAdmin: Query Tool](https://www.pgadmin.org/docs/pgadmin4/latest/query_tool.html)

Read the relevant sections rather than the entire manuals. Index tuning and Python database connections come later.
