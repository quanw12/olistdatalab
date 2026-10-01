# Day 8 — SQL hints and pgAdmin troubleshooting

Read only the section you need. Type your changes into `schema.sql`, save it, and run the updated SQL using [guide.md](guide.md).

## TODO 1 — Unique city names

After `timezone_name TEXT NOT NULL`, add a comma and:

```sql
CONSTRAINT uq_cities_city_name UNIQUE (city_name)
```

The name labels the rule in error messages. UNIQUE rejects a second row with the same name. This exercise assumes consistent city names; it does not normalize spelling or letter case.

## TODO 2 — Reject blank strings

After TODO 1, add a comma and:

```sql
CONSTRAINT ck_cities_city_name_nonempty CHECK (btrim(city_name) <> ''),
CONSTRAINT ck_cities_timezone_nonempty CHECK (btrim(timezone_name) <> '')
```

`btrim` removes spaces from both ends; `<>` means "not equal"; `''` is an empty string. Thus `'   '` fails. `NOT NULL` rejects NULL, but alone does not reject empty strings.

## TODO 3 — Reference an existing city

In `weather_observations`, add a comma after `source TEXT NOT NULL`, then:

```sql
CONSTRAINT fk_weather_city FOREIGN KEY (city_id) REFERENCES cities(city_id)
```

The observation's city must exist in `cities`. Create and populate that table before inserting observations.

## TODO 4 — One observation per city and time

After TODO 3, add a comma and:

```sql
CONSTRAINT pk_weather_observations PRIMARY KEY (city_id, observed_at)
```

The **pair** must be unique. A city can have different observation times; different cities can share an observation time.

## TODO 5 — Ranges and a nonblank source

After TODO 4, add a comma and these rules. The last item has no trailing comma:

```sql
CONSTRAINT ck_weather_temperature CHECK (temperature_c BETWEEN -50 AND 60),
CONSTRAINT ck_weather_humidity CHECK (humidity_pct BETWEEN 0 AND 100),
CONSTRAINT ck_weather_source_nonempty CHECK (btrim(source) <> '')
```

`BETWEEN` includes both endpoints. The temperature limits are this learning pipeline's chosen rules, not a universal range for all weather.

## SQL syntax errors

- Error near `CONSTRAINT`: check for a missing comma immediately before it.
- Error near `)`: check for an extra comma after the last item.
- `--` starts a comment, which does not create a rule. Replace TODOs with SQL.
- Strings use single quotes, such as `'Hanoi'`. Statements end with `;`.

## Connection problems

**Connection refused / timeout:** check that `postgresql-x64-18` is running in Windows Services. Confirm host `localhost` and your installation's port, normally `5432`. Registering a connection in pgAdmin does not install or start the server.

**Password authentication failed:** use the PostgreSQL `postgres` account password chosen during installation. A pgAdmin master password, if configured, has a different purpose. Do not reinstall PostgreSQL or delete data to fix this error.

**Database missing from the tree:** right-click **Databases → Refresh**. Create `weather_day08` using the guide if it does not exist.

Reference: [pgAdmin connection settings](https://www.pgadmin.org/docs/pgadmin4/latest/server_dialog.html).

## Wrong database or missing results

Run:

```sql
SELECT current_database();
```

It must show `weather_day08`. Otherwise, open a new Query Tool from that database. Existing tabs keep their own connections.

**Data Output** shows SELECT results; **Messages** shows success and errors. Highlight one complete SELECT, including `;`, and execute it to see that result clearly. Refresh **Tables** after creating them. Terminal commands are not SQL and should not be pasted into Query Tool.

## A transaction is aborted

If a later query says `current transaction is aborted`, execute this statement alone in the same Query Tool tab:

```sql
ROLLBACK;
```

It discards uncommitted changes in that transaction. Enable **Auto commit?** in the execution dropdown before continuing the separate error experiments. Already committed sample data stays saved. If you had disabled Auto commit while loading sample data, check the counts again: rollback may have undone that uncommitted load.

Reference: [pgAdmin execution and transaction controls](https://www.pgadmin.org/docs/pgadmin4/latest/query_tool_toolbar.html).

## Tables already exist / seed duplicates

`schema.sql` and `seed.sql` each run once. Read the error before retrying; do not delete the database as a shortcut.

Editing the saved creation script does **not** change tables already created. If your first execution created incomplete tables, send the error and current structure for help applying the missing constraints. Do not load sample data until both tables have their required rules.

Run `verify.sql` to inspect the current state; it is safe to repeat. A failed INSERT may consume an identity number, so gaps in IDs are normal; the row count is what matters.

Reference: [PostgreSQL sequence behavior after failed transactions](https://www.postgresql.org/docs/current/functions-sequence.html).
