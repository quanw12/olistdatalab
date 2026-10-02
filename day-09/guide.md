# Day 9 — Query weather data with SQL

Today you will write **ten SELECT queries** in PostgreSQL: read columns, filter rows, sort results, join tables, and summarize observations. Use **pgAdmin 4**, as in Day 8. No Python, Docker, or live API is needed today.

## 1. Know what each file does

| File | Purpose |
|---|---|
| [guide.md](guide.md) | Learning order, setup, running queries, submission, and commit commands |
| [lesson.md](lesson.md) | Explanations and runnable SQL examples |
| [setup.sql](setup.sql) | Ready-made tables and sample data; no TODOs |
| [queries.sql](queries.sql) | Your ten query exercises and explanations |
| [help.md](help.md) | Hints for each exercise and common mistakes |
| [expected.md](expected.md) | Expected results for checking your work |

Budget about 3–4 hours. Take a break after Q5. Work through one query at a time rather than writing all ten at once.

## 2. Create a separate practice database in pgAdmin

1. Open pgAdmin and connect to your existing local PostgreSQL server.
2. Right-click **Databases → Create → Database…**.
3. Set **Database** to `weather_day09`, keep **Owner** as `postgres`, and click **Save**.
4. Right-click **weather_day09 → Query Tool**.
5. Highlight and execute:

```sql
SELECT current_database();
```

The result must be `weather_day09`. Selecting a database in the tree does not change an existing Query Tool tab's connection. Open a new tab from the correct database if necessary.

If `weather_day09` already exists, inspect its tables before running setup. Use the existing lesson data if it already has four cities and eight observations; do not rerun setup over existing tables. Day 8's database is separate.

## 3. Load the sample data once

1. Click **Open File** in Query Tool (normally `Ctrl + O`). Open `C:\DE Courses\day-09\setup.sql`.
2. Alternatively, copy the entire saved file into the SQL editor.
3. Select **all of setup.sql**, then click **Execute script** (normally `F5`). Read the tooltip if your toolbar looks different.
4. Read **Messages**: there should be no error. Refresh `Schemas → public → Tables` to see the two tables.

Run setup **once on an empty weather_day09 database**. It creates `cities` and `weather_observations` with the Day 8 rules. The initial safety block checks the database name; BEGIN/COMMIT keep the setup together. You do not need to edit that block. We will study transactions in Day 13.

Check the data with these two queries, executed separately:

```sql
SELECT COUNT(*) AS city_count FROM cities;
```

```sql
SELECT COUNT(*) AS observation_count FROM weather_observations;
```

Expected: **4 cities and 8 observations**. Hue intentionally has no observations. If setup reports an error, stop and read [help.md](help.md).

In every Query Tool tab used for this lesson, run:

```sql
SET TIME ZONE 'Asia/Ho_Chi_Minh';
```

This makes the displayed timestamps match the examples. It changes that connection's display setting, not the stored observation instants.

## 4. Learn, then practise

1. Read lesson sections 1–4 and run their small examples.
2. Open `C:\DE Courses\day-09\queries.sql` in your code editor.
3. Write Q1–Q5 under their TODO comments. Add one English sentence after each `-- Explanation:` describing the query.
4. Save the file, then copy **one complete query** into Query Tool. Highlight it, including `;`, and execute it.
5. Check **Data Output**, then compare with the matching section in [expected.md](expected.md).
6. Read lesson sections 5–8, then complete Q6–Q10 in the same way.

The starter `queries.sql` contains only comments, so running it before writing SQL produces no query results. Never paste TODO text as SQL. Keep the comments and put your real SELECT statement on the blank line below each TODO.

Saving code in Query Tool does not automatically save your workspace file. Keep your completed queries in `day-09/queries.sql`. If you edit a query in pgAdmin, copy it back and save it before submitting.

## 5. What you will build

| Exercise | Skill | Result size |
|---|---|---|
| Q1 | SELECT columns + ORDER BY | 4 rows |
| Q2 | Read observations in a stable order | 8 rows |
| Q3 | WHERE with two conditions | 4 rows |
| Q4 | DISTINCT city IDs | 3 rows |
| Q5 | ORDER BY DESC + LIMIT | 2 rows |
| Q6 | INNER JOIN for city names | 8 rows |
| Q7 | COUNT, MIN, MAX, AVG | 1 summary row |
| Q8 | JOIN + GROUP BY | 3 city summaries |
| Q9 | HAVING on group counts | 2 city summaries |
| Q10 | LEFT JOIN + correct counting | 4 city summaries, including Hue |

No INSERT, UPDATE, DELETE, or schema changes are part of your query exercises. After finishing, the base tables should still have four cities and eight observations.

## 6. Completion checklist and submission

- [ ] All ten queries run without errors and match the expected values and ordering.
- [ ] Each query has a short explanation in your own English.
- [ ] Q6 contains an explicit matching condition, not a cross join.
- [ ] Q10 includes Hue with a count of 0 and a NULL average.
- [ ] You can explain how WHERE differs from HAVING.

Send:

1. A message saying `Review day-09/queries.sql`; I can read the saved file directly.
2. Q7, Q8, Q9, and Q10 results, copied from Data Output or shown in screenshots.
3. Any errors you cannot resolve, including the query that caused them.
4. Short answers to these questions (include them at the bottom of queries.sql):
   - Why does an INNER JOIN omit Hue, while a LEFT JOIN includes it?
   - Why does COUNT(*) give the wrong observation count for Hue after a LEFT JOIN?
   - Why filter group counts with HAVING rather than WHERE?
   - Is a NULL average the same as a temperature of zero? Explain.

## 7. Git checkpoint

After completing the queries and reviewing the results, run in PowerShell:

```powershell
Set-Location "C:\DE Courses"
git branch --show-current
git status
git add day-09 README.md
git commit -m "feat(day-09): add weather SQL query exercises"
git push -u origin feature/day09
```

The branch was `feature/day09` with no upstream when this guide was created. Use this push command while on that branch. `-u` sets its upstream; later pushes from the same branch can use `git push`. If you switch branches, use the actual branch name instead. This pushes the feature branch without merging it into main.

## References

- [pgAdmin Query Tool](https://www.pgadmin.org/docs/pgadmin4/latest/query_tool.html) — opening files, executing selections, and reading output.
- SQL references are linked beside the relevant topics in [lesson.md](lesson.md).
