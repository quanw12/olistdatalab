# Day 8 — PostgreSQL tables with pgAdmin 4

Today you will create two tables, load sample weather data, and check that PostgreSQL rejects invalid data. Use **pgAdmin 4 and your local PostgreSQL server**. Docker will be introduced in Day 18, with its own setup and explanations.

## 1. Understand the tools

- **PostgreSQL server** stores data and executes SQL. It runs as a Windows service.
- **pgAdmin 4** is the interface you use to connect to that server and send SQL.
- **Database** is a named place for your tables. Today it is `weather_day08`.
- **Query Tool** is the SQL editor inside pgAdmin.

Your machine had `postgresql-x64-18` in the **Running** state when this guide was updated. You already have the server; you do not need another installation. If it stops later, open Windows Services (`Win + R`, enter `services.msc`), find that service, and start it.

## 2. Connect to your local server

Open pgAdmin 4 and look at **Servers** in the left Object Explorer. If a local PostgreSQL server is already listed, double-click it and enter the database password you chose during installation. Once it connects and shows **Databases**, skip registering another server.

If there is no local server entry:

1. Right-click **Servers → Register → Server…**.
2. In **General**, set **Name** to `Local PostgreSQL`. This is only a display label.
3. In **Connection**, enter:

| Field | Value | Meaning |
|---|---|---|
| Host name/address | `localhost` | Server on this computer |
| Port | `5432` | Default; use your installation's port if you changed it |
| Maintenance database | `postgres` | Existing database for the initial connection |
| Username | `postgres` | Account created by the usual Windows installer |
| Password | Your installation password | Password for that PostgreSQL account |

4. Click **Save**, then expand the server and **Databases**.

The PostgreSQL account password is separate from a pgAdmin master password, if pgAdmin asks for one. Do not put your password in SQL files or Git. For connection errors, see [help.md](help.md).

Reference: [pgAdmin server connection fields](https://www.pgadmin.org/docs/pgadmin4/latest/server_dialog.html).

## 3. Create the practice database and open Query Tool

1. Right-click **Databases → Create → Database…** under your connected server.
2. Set **Database** to `weather_day08`; keep **Owner** as `postgres`.
3. Click **Save**. If this database already exists, use it.
4. Right-click **weather_day08 → Query Tool**.
5. Type this into its SQL editor:

```sql
SELECT current_database();
```

Highlight the complete statement, including `;`, and click **Execute script** (normally `F5`). Hover over the toolbar icon to check its tooltip if your version labels it differently. Use this **highlight → execute** method throughout the lesson so you control exactly which SQL runs.

Read **Data Output** below the editor: it must show `weather_day08`. If it shows `postgres`, close this Query Tool tab and open Query Tool from `weather_day08`. Selecting another database in the tree does not switch an existing Query Tool tab's connection.

Open the execution button's dropdown and enable **Auto commit?** for this exercise. Successful executions will be saved in the database. Saving a `.sql` file is a separate action: it saves the instructions, not their results.

References: [database dialog](https://www.pgadmin.org/docs/pgadmin4/latest/database_dialog.html), [Query Tool buttons](https://www.pgadmin.org/docs/pgadmin4/latest/query_tool_toolbar.html).

## 4. Learn the SQL and complete the exercise

1. Read [lesson.md](lesson.md) for table types, keys, and constraints.
2. Open `C:\DE Courses\day-08\schema.sql` in your code editor.
3. Complete its five TODOs yourself. Use the matching section in [help.md](help.md) when stuck.
4. Save the file. This is the file you will submit and commit.

| File | Job | When to run |
|---|---|---|
| `schema.sql` | Creates tables and their rules | Once, after completing TODOs, in the empty practice database |
| `seed.sql` | Inserts valid sample data | Once, after both tables exist with the required rules |
| `verify.sql` | Reads data and checks results | As often as needed |

## 5. Run the completed schema

1. In Query Tool connected to `weather_day08`, click **Open File** (folder icon, normally `Ctrl + O`). Choose `C:\DE Courses\day-08\schema.sql`.
2. Alternatively, copy the saved file's entire contents from your editor into Query Tool.
3. Click inside the SQL editor, press `Ctrl + A` to highlight the file's SQL, and execute it.
4. Read **Messages** for successful completion with no `ERROR`.
5. Expand `weather_day08 → Schemas → public → Tables`. Right-click **Tables → Refresh** if necessary. Both `cities` and `weather_observations` should appear.

Opening a file does not execute it. Changes typed into Query Tool do not automatically update your original exercise file. Keep the final SQL in the workspace file, then reopen or paste the updated contents before executing.

If creation fails, stop before inserting data and read [help.md](help.md). Do not repeatedly execute the entire creation script after tables already exist.

## 6. Insert and verify sample data

Open `C:\DE Courses\day-08\seed.sql` using the same method. Highlight the entire script and execute it **once**. Both INSERT statements should succeed: two cities and three observations.

Next open `C:\DE Courses\day-08\verify.sql`. **Highlight and execute one SELECT at a time**, including its semicolon. Read Data Output before moving to the next SELECT.

| Result | Expected |
|---|---|
| `city_count` | `2` |
| `observation_count` | `3` |
| `bad_temperature_count` | `0` |
| `bad_humidity_count` | `0` |
| Final observation query | Three rows |

The sample cities are Hanoi and Da Nang. Dates may display in your connection's timezone; an equivalent time with another offset is not an error.

`schema.sql` and `seed.sql` are for one initial run. Repeating schema creation reports existing tables; repeating the seed violates a unique constraint. `verify.sql` only reads and is safe to repeat.

## 7. Inspect constraints using the interface

Under **Tables**, expand each table's **Constraints** node. Refresh the table if needed. Look for:

- `cities`: a primary key, UNIQUE on `city_name`, and two nonblank CHECK constraints.
- `weather_observations`: PRIMARY KEY on `(city_id, observed_at)`, FOREIGN KEY to `cities`, and three CHECK constraints.

Right-click a constraint → **Properties** to inspect its columns or condition. Under **Columns**, column properties show whether NULL is allowed.

## 8. Test rejected data

Open a separate Query Tool tab on **weather_day08**. Copy and execute **one block at a time**. Each must produce an error and add no row. Keep these experiments out of `seed.sql`.

### A. Duplicate city — expected UNIQUE error

```sql
INSERT INTO cities (city_name, timezone_name)
VALUES ('Hanoi', 'Asia/Ho_Chi_Minh');
```

### B. Invalid humidity — expected CHECK error

This uses a new observation time so the test targets humidity instead of a duplicate key.

```sql
INSERT INTO weather_observations
    (city_id, observed_at, requested_at, temperature_c, humidity_pct, source)
VALUES
    (1, '2026-09-18T13:30:00+07:00', '2026-09-18T06:31:00+00:00', 30.0, 130, 'open-meteo');
```

### C. Missing city — expected FOREIGN KEY error

```sql
INSERT INTO weather_observations
    (city_id, observed_at, requested_at, temperature_c, humidity_pct, source)
VALUES
    (999, '2026-09-18T13:30:00+07:00', '2026-09-18T06:31:00+00:00', 30.0, 75, 'open-meteo');
```

### D. Existing city/time pair — expected PRIMARY KEY error

```sql
INSERT INTO weather_observations
    (city_id, observed_at, requested_at, temperature_c, humidity_pct, source)
VALUES
    (1, '2026-09-18T11:30:00+07:00', '2026-09-18T04:31:14+00:00', 30.7, 72, 'open-meteo');
```

Read the constraint name in **Messages**. If a test succeeds, that rule is missing or incorrect; stop and inspect it. If you see `current transaction is aborted`, follow [help.md](help.md).

Repeat the two count queries afterward: they should still show **2 cities and 3 observations**.

## 9. Send these results for review

1. Your completed `schema.sql`.
2. The four counts and three observation rows from `verify.sql`.
3. The constraint names/properties for `weather_observations` from pgAdmin.
4. At least two expected errors, including the FOREIGN KEY or PRIMARY KEY test.
5. Your explanation: why use `TIMESTAMPTZ` for `observed_at`, and why keep `timezone_name` separately?

Budget about 2.5–4 hours. Python connections come in Day 13. After review, commit the lesson files and completed SQL. Keep passwords and the server's data directory out of Git.
