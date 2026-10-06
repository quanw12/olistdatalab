# Day 11 — Analyze weather with SQL window functions

Today you will calculate values across related observations while keeping each observation visible. You will number rows, rank temperatures, compare consecutive observations, and calculate rolling averages. The final exercise combines these into a latest-weather report for every city.

Use your local PostgreSQL server and **pgAdmin 4**, connected to **weather_day09**. Day 11 reuses the existing four cities and eight fixed observations. Read the tutorials before writing the exercises.

## 1. Files and learning order

| File | Purpose | When to open it |
|---|---|---|
| [guide.md](guide.md) | Learning order, completion criteria, submission, and Git commands | First |
| [checks.sql](checks.sql) | Ready-made checks of the existing database and observations | Before and after the lesson |
| [lesson.md](lesson.md) | Step-by-step tutorials with runnable examples | One section at a time |
| [queries.sql](queries.sql) | Eight exercises and five reflection questions | After the matching tutorial |
| [help.md](help.md) | Exact syntax hints and common errors | If stuck for 15–20 minutes |
| [expected.md](expected.md) | Expected values, columns, and ordering | After running your own SQL |

The starter queries.sql contains comments only. Write complete SQL under each TODO, ending each statement with a semicolon. Keep one explanation in your own English after every `-- Explanation:`.

Results appear in pgAdmin's Data Output. The lesson examples and checks do not insert, update, or delete observations. There is no new database, setup script, output folder, or software installation today.

## 2. Confirm the dataset

1. Right-click **weather_day09 → Query Tool** in pgAdmin.
2. Open `C:\DE Courses\day-11\checks.sql`, or copy its saved contents into the editor.
3. Highlight and execute one complete statement at a time, including its semicolon. Use the Execute script button, normally F5; confirm the tooltip if your toolbar differs.
4. Compare the result with the expectation above that statement.

Expected checks:

- Database name: weather_day09.
- Four cities and eight observations; temperature sum 251.0.
- City observation counts: Da Nang 2, Hanoi 3, Ho Chi Minh City 3, Hue 0.
- First and last timestamps match the comments in checks.sql.

If a check differs, inspect the connection and data before starting. Do not reload Day 9 setup over existing tables. If the database is missing, return to Day 9's setup instructions first.

Run this in every new Query Tool tab for consistent timestamp display:

```sql
SET TIME ZONE 'Asia/Ho_Chi_Minh';
```

This displays observed_at with the expected +07 offset. The ranking and chronology still use the stored instants.

## 3. Study in small stages

Allow about 3–4 hours, or use two sessions. Do not try to memorize every window function today.

| Stage | Reading and practice | Suggested time |
|---|---|---|
| Prepare | checks.sql and review the Day 10 CTE shape | 15 minutes |
| Keep the rows | lesson sections 1–2; Q1 | 25 minutes |
| Number and select | sections 3–4; Q2–Q3 | 40 minutes |
| Ties | section 5; Q4 | 25 minutes |
| Previous observation | section 6; Q5 | 30 minutes |
| Rolling and running | sections 7–8; Q6–Q7 | 40 minutes |
| Combine | section 9; Q8 and reflections | 45 minutes |

For each stage:

1. Type and run the tutorial example.
2. Explain what one output row represents.
3. Make the suggested small change and predict its result.
4. Write the exercise yourself in queries.sql.
5. Compare the result with expected.md.

Save your answers in `C:\DE Courses\day-11\queries.sql`. Changes made in pgAdmin must be copied back into that file before review.

## 4. What each exercise builds

| Exercise | Skill | Expected rows |
|---|---|---:|
| Q1 | AVG OVER PARTITION BY: full city average beside each observation | 8 |
| Q2 | ROW_NUMBER: chronological sequence inside each city | 8 |
| Q3 | CTE + ROW_NUMBER: latest observation for each observed city | 3 |
| Q4 | RANK and DENSE_RANK: equal temperatures share a rank | 8 |
| Q5 | LAG + CTE: previous temperature and its change | 8 |
| Q6 | Explicit ROWS frame: average of up to three observations | 8 |
| Q7 | Running maximum: highest temperature seen so far per city | 8 |
| Q8 | Latest record + history features + LEFT JOIN: all-city trend report | 4 |

Important distinctions:

- PARTITION BY separates calculations by city without collapsing observations.
- The ORDER BY inside OVER controls a calculation; the final ORDER BY controls display.
- ROWS BETWEEN 2 PRECEDING AND CURRENT ROW includes up to three observations, not three hours or days.
- LAG refers to the previous available observation in the chosen order. The first observation has no predecessor.
- Q8 must calculate history features before selecting the latest record, and must keep Hue visible.

The warming/cooling labels compare two available measurements. They are exercise labels, not a forecast or an official weather classification.

## 5. Complete and submit

- [ ] All eight queries match expected.md, including output names and ordering.
- [ ] Each has a short explanation in your own English.
- [ ] Q1 has no ORDER BY inside its average window: it needs the full city average.
- [ ] Q3 filters row_number in an outer query over a CTE.
- [ ] Q4 ranks by temperature only inside OVER; tied temperatures share ranks.
- [ ] Q5's first previous temperature and change are NULL for each city.
- [ ] Q6 and Q8 explicitly use ROWS BETWEEN 2 PRECEDING AND CURRENT ROW for the rolling average.
- [ ] You ran the four-row rolling-average tutorial: its fourth rolling result is 30.00, not 25.00.
- [ ] Q8 returns Hue with NULL measurements and trend_status = no data.
- [ ] All five reflections are answered.
- [ ] checks.sql still reports four cities and eight observations.

Send:

1. `Review day-11/queries.sql` — I can read your saved file directly.
2. Q3, Q4, Q5, Q6, and Q8 results, copied from Data Output or shown in screenshots.
3. Any unresolved error and its complete SQL statement.
4. Your reflection answers at the bottom of queries.sql.

## 6. Git checkpoint

When this lesson was prepared, the checkout was on main, tracking origin/main, and included the merged Day 10 work. Create a branch for Day 11 before committing.

Run in PowerShell now:

```powershell
Set-Location "C:\DE Courses"
git branch --show-current
git status
git switch -c codex/day11
```

If codex/day11 already exists, use `git switch codex/day11`. If you already chose another lesson branch, stay on it and use its actual name when pushing.

After completing the exercises and reviewing their results:

```powershell
Set-Location "C:\DE Courses"
git branch --show-current
git status
git add day-11 README.md
git diff --cached --stat
git commit -m "feat(day-11): analyze weather with SQL window functions"
git push -u origin codex/day11
```

The new branch initially has no upstream; -u sets it. Later pushes from that branch can use `git push`. Replace codex/day11 with your actual branch name if you chose another one. The learner runs these commands after review.

References: [pgAdmin Query Tool](https://www.pgadmin.org/docs/pgadmin4/latest/query_tool.html), [PostgreSQL window tutorial](https://www.postgresql.org/docs/18/tutorial-window.html). More specific references appear in lesson.md.
