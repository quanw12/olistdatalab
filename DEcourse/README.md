# DEcourse · Data Engineering course vault

Everything you need to study lives here: the roadmap, module guides, theory lessons, lab instructions, project briefs and templates. The code repository next to this folder holds only code (the reference platform and the lab skeletons in `labs/`). No community plugins or Obsidian Sync account are needed.

## Open in Obsidian

1. Choose **Open folder as vault** in the vault manager.
2. Select the `DEcourse` folder (e.g. `C:\DE Courses\DEcourse`).
3. Open **00 - Start Here → Home**, then **Roadmap**. `Ctrl+O` finds notes, `Ctrl+P` runs commands, `Ctrl+E` toggles reading/editing on Windows.
4. Callouts, wikilinks, code highlighting and the graph are standard Obsidian Markdown. A CSS snippet ships in `.obsidian/snippets/decourse.css` (Appearance → CSS snippets).

The notes also read fine in any Markdown editor; wikilinks render best in Obsidian.

## Structure

| Folder | Contents |
|---|---|
| 00 - Start Here | Home, Roadmap (weeks, gates, branches), progress and evidence, review schedule, learning with AI, labs guide |
| 01 - Python | Modules 01 and 04; Python basics, functions/errors, files, datetime/decimal, DataFrames, environments |
| 02 - SQL | Module 03; NULL/CASE, joins and grain, aggregation/windows, CTE/dedup/incremental, transactions/indexes/plans |
| 03 - Git and Linux | Module 02; Git/PRs/review, shell (Bash and PowerShell) |
| 04 - Core DE | Modules 05–08 and 19; modelling/SCD2, ingestion/contracts, APIs, incremental/CDC, testing/CI |
| 05 - Modern Stack | Modules 09–11; dbt, Docker/Postgres, Airflow, BI/metrics |
| 06 - Production | Modules 20–21; observability/recovery, security/governance, delivery, performance |
| 07 - Cloud | Module 14; GCP, BigQuery, Terraform and cost |
| 08 - Specializations | Modules 12, 13, 15, 16; Spark, Kafka, ML features, LLM, RAG — pick one branch |
| 09 - Projects | Modules 17, 18, 22; Olist brief, failure drills, second project, interviews |
| 10 - Templates | Note, study log, incident report, ADR |

Every **module guide** (`Module NN - …`) says what to watch, read, practise and hand in. Every **theory note** is a full lesson: learning goals, concepts from first principles, runnable examples with expected output, application to Olist, common mistakes, exercises, and review questions with folded answers.

## Code conventions

- **Runnable:** blocks starting with `# runnable` (Python) or `-- runnable` (SQL) use tiny inline data and assertions/expected output. SQL is DuckDB unless marked PostgreSQL/BigQuery.
- **Patterns:** other blocks need real tables, paths, credentials or services; adapt them before running.
- **Environment commands:** run only after installing dependencies/services and checking your current folder. Cloud commands can cost money; nothing here runs Terraform for you.
- Snippets use `assert` for learning; production validation should raise explicit exceptions.

## Checking the vault

From the code repo with core dependencies installed, run `python scripts/check_course.py`. It validates wikilinks, relative links and config, rejects Vietnamese text and links that leave the vault, and executes every `runnable` block (SQL against its `-- expect:` result). Spark, Kafka, cloud and Airflow patterns are not executed and still need evidence from your own labs.
