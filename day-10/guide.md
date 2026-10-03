# Day 10 — Build reports with dates, CASE, subqueries, and CTEs

Today you will turn individual weather observations into useful reports. You will learn how to select a local calendar day, assign labels, compare a row with a calculated value, and split a report into named SQL steps.

Use your existing local PostgreSQL server and pgAdmin 4. The database is still **weather_day09**: Day 10 reuses its four cities and eight fixed observations. The folder name and database name can differ.

## 1. Follow this learning order

| File | Purpose | When to use it |
|---|---|---|
| [guide.md](guide.md) | Learning order, database checks, submission, and commit commands | Start here |
| [checks.sql](checks.sql) | Ready-made, read-only checks of the existing dataset | Before studying and after finishing |
| [lesson.md](lesson.md) | Runnable tutorials with explanations and small changes to try | Read one section at a time |
| [queries.sql](queries.sql) | Ten exercises for you to write, plus reflections | After the relevant tutorial |
| [help.md](help.md) | Syntax hints and debugging steps | If stuck for 15–20 minutes |
| [expected.md](expected.md) | Expected values and ordering | After running your own query |

There is no setup script today. Query results appear in pgAdmin's Data Output; you do not need an output folder or exported files.

Allow about 3–4 hours, or split the lesson into two sessions:

| Stage | Work | Suggested time |
|---|---|---|
| Prepare | Check the database and review Day 9 counting | 15 minutes |
| Dates | Lesson sections 1–3, then Q1–Q3 | 45 minutes |
| Conditions | Sections 4–5, then Q4–Q5 | 35 minutes |
| Comparisons | Sections 6–7, then Q6–Q8 | 45 minutes |
| Named steps | Section 8, then Q9 | 30 minutes |
| Report | Section 9, then Q10 and reflections | 45 minutes |

## 2. Check the existing database

1. In pgAdmin, expand your server's Databases.
2. Right-click **weather_day09 → Query Tool**.
3. Open `C:\DE Courses\day-10\checks.sql`, or copy its contents into the editor.
4. Highlight and execute **one complete statement at a time**, including its final semicolon. Use the Execute script button, normally F5; hover over the button to confirm its tooltip.
5. Compare each result with the expectation written above the statement.

You should see:

- Database: `weather_day09`.
- City count: **4**; observation count: **8**.
- Temperature sum: **251.0**.
- Two local dates: **2026-09-18: 6 observations**, **2026-09-19: 2 observations**.
- City counts: Da Nang **2**, Hanoi **3**, Ho Chi Minh City **3**, Hue **0**.

If a check differs, inspect the connection and existing data before proceeding. Do not reload Day 9 setup over tables that already exist. If the database is missing, follow Day 9's setup guide once, then return here.

In each new Query Tool tab, run this separately:

```sql
SET TIME ZONE 'Asia/Ho_Chi_Minh';
```

It makes the original timestamps display with the expected +07 offset. Today's report-date expressions also name the timezone explicitly.

## 3. Learn by changing a working example

For every tutorial:

1. Type and run the example from lesson.md.
2. Explain what one output row represents.
3. Change the date, threshold, or selected column suggested below it.
4. Predict the result before executing the change.
5. Write the exercise yourself in queries.sql.

Keep the saved workspace file as your submission. If you change SQL in pgAdmin, copy it back into `C:\DE Courses\day-10\queries.sql` and save it. Saving in one editor does not automatically update the other.

The starter queries.sql contains only comments. Replace the TODOs with complete queries. Add your own English sentence after each `-- Explanation:` and end every statement with `;`.

## 4. The ten exercises

The exact columns, rules, and sort order are specified in queries.sql.

| Query | Main skill | Expected size |
|---|---|---|
| Q1 | Convert an instant to local time and date | 8 rows |
| Q2 | Filter one day with an inclusive start and exclusive end | 6 rows |
| Q3 | Group observations by local date | 2 rows |
| Q4 | CASE labels for each observation | 8 rows |
| Q5 | SUM(CASE ...) for conditional counts, including Hue | 4 rows |
| Q6 | Scalar subquery: above the overall mean | 4 rows |
| Q7 | Scalar subquery: every observation equal to the maximum | 1 row in this dataset |
| Q8 | NOT EXISTS: cities with no observations | 1 row |
| Q9 | CTE: summarize cities, then filter the summary | 2 rows |
| Q10 | CTE + date filter + LEFT JOIN + CASE daily report | 4 rows |

The labels in Q4 and Q10 are exercise rules, not official weather classifications.

## 5. Finish and send for review

- [ ] All ten queries are saved and match expected.md, including column names and ordering.
- [ ] Each query has one explanation written in your own English.
- [ ] Q2 excludes the next day's midnight boundary.
- [ ] Q5 and Q10 retain Hue; missing temperatures remain NULL.
- [ ] Q6 compares with the actual average, not a rounded or hard-coded number.
- [ ] Q7 uses MAX in a subquery and can return tied maximum rows.
- [ ] Q9 and Q10 include the complete WITH block and final SELECT in one statement.
- [ ] The four reflection questions at the end of queries.sql are answered.
- [ ] checks.sql still shows four cities and eight observations.

Send:

1. `Review day-10/queries.sql` — I can read your saved file directly.
2. Results for **Q3, Q5, Q6, and Q10**, copied from pgAdmin or shown in screenshots.
3. Any unresolved error and the query that caused it.
4. Your reflection answers at the bottom of queries.sql.

## 6. Git checkpoint

When this lesson was prepared, the checkout was on main, tracking origin/main. Create a branch for the lesson before committing. You can create it now, even if the new lesson files already appear as untracked files.

Run in PowerShell:

```powershell
Set-Location "C:\DE Courses"
git branch --show-current
git status
git switch -c codex/day10
```

If you already created `codex/day10`, use `git switch codex/day10` instead of creating it again. If you have chosen a different lesson branch, stay on it and use its name in the push command.

After completing the exercises and reviewing your results:

```powershell
Set-Location "C:\DE Courses"
git branch --show-current
git status
git add day-10 README.md
git diff --cached --stat
git commit -m "feat(day-10): add daily weather reports with CTEs and subqueries"
git push -u origin codex/day10
```

The new branch has no upstream initially, so `-u` sets one. Later pushes from that branch can use `git push`. If the current branch has another name, replace `codex/day10` with that exact name. Run the commit commands yourself after review.

Reference: [pgAdmin Query Tool](https://www.pgadmin.org/docs/pgadmin4/latest/query_tool.html). SQL references are linked beside their topics in lesson.md.
