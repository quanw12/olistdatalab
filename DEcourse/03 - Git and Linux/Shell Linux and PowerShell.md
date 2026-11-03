---
tags: [decourse, shell, linux]
module: 02
---

# Shell: Linux and PowerShell

> [!info] Learning goals
> After this note you can: navigate the filesystem and read files from a terminal in both Bash and PowerShell; search logs; chain commands with pipes; use environment variables and exit codes; inspect processes and ports; quote paths correctly; and write a small script that fails loudly when its input is missing.

## 1. Why the shell matters

Servers, containers and CI runners have no mouse. When a pipeline fails at 3 a.m. you will read logs, check whether a file arrived, see which process holds a port, and rerun a command — all from a terminal. Airflow tasks, Docker entrypoints and CI steps are shell commands.

Two shells matter for this course:

- **Bash** (Linux, macOS, WSL, Git Bash, most containers and CI runners). Pipes pass **text**.
- **PowerShell** (Windows). Pipes pass **objects** with properties, so you filter by property instead of cutting text.

Do not mix their syntax: quoting, variables and redirection differ.

## 2. Command cheat sheet

| Need | Bash / WSL | PowerShell |
|---|---|---|
| Where am I | `pwd` | `Get-Location` |
| List files (incl. hidden) | `ls -la` | `Get-ChildItem -Force` |
| Change folder | `cd data/landing` | `Set-Location data\landing` |
| First lines | `head -5 file.csv` | `Get-Content file.csv -TotalCount 5` |
| Last lines / follow | `tail -50 app.log`, `tail -f app.log` | `Get-Content app.log -Tail 50 -Wait` |
| Search text | `rg -n ERROR logs/` (or `grep -rn`) | `rg -n ERROR logs/` or `Select-String -Path logs\* -Pattern ERROR` |
| Find files | `find . -name "*.csv"` | `Get-ChildItem -Recurse -Filter *.csv` |
| Copy / move / delete | `cp`, `mv`, `rm` | `Copy-Item`, `Move-Item`, `Remove-Item` |
| Make folders | `mkdir -p a/b` | `New-Item -ItemType Directory -Force a\b` |
| Set env var (session) | `export MODE=dev` | `$env:MODE = 'dev'` |
| Read env var | `echo "$MODE"` | `$env:MODE` |
| Last exit code | `echo $?` | `$LASTEXITCODE` (native programs), `$?` (success flag) |
| Processes | `ps aux \| grep python` | `Get-Process python` |
| Who uses port 5432 | `ss -ltnp \| grep 5432` | `Get-NetTCPConnection -LocalPort 5432` |
| Disk usage | `du -sh data/*`, `df -h` | `Get-ChildItem data -Recurse \| Measure-Object Length -Sum` |

`rg` (ripgrep) works the same in both shells and is much faster than grep on large trees.

## 3. Pipes and redirection

```bash
# Count ERROR lines per run_id in the newest log (Bash)
latest=$(ls -t logs/*.log | head -1)
grep ERROR "$latest" | grep -o 'run_id=[a-z0-9-]*' | sort | uniq -c | sort -rn

command > out.txt        # stdout to a file (overwrite)
command >> out.txt       # append
command 2> errors.txt    # stderr to a file
command > all.txt 2>&1   # both
command1 && command2     # run command2 only if command1 succeeded
command1 || echo failed  # run on failure
```

```powershell
# The same idea in PowerShell, working with objects
$latest = Get-ChildItem logs\*.log | Sort-Object LastWriteTime -Descending | Select-Object -First 1
Select-String -Path $latest.FullName -Pattern 'ERROR' |
    ForEach-Object { if ($_.Line -match 'run_id=([a-z0-9-]+)') { $Matches[1] } } |
    Group-Object | Sort-Object Count -Descending
```

Windows PowerShell 5.1 has no `&&`/`||`; use `cmd1; if ($?) { cmd2 }`. PowerShell 7 supports them.

## 4. Exit codes: how programs report success

Every program returns an exit code: **0 = success**, anything else = failure. Schedulers, CI and `&&` chains rely on it. A Python script that catches an exception and returns normally exits 0 and looks successful. Make failures explicit:

```python
# runnable
import sys
from pathlib import Path

def main(argv: list[str]) -> int:
    if len(argv) != 1:
        print("usage: check_input.py <file>", file=sys.stderr)
        return 2
    path = Path(argv[0])
    if not path.exists() or path.stat().st_size == 0:
        print(f"input missing or empty: {path}", file=sys.stderr)
        return 1
    return 0

assert main([]) == 2
assert main(["definitely/not/here.csv"]) == 1
# in a real script: raise SystemExit(main(sys.argv[1:]))
```

Bash scripts should start with `set -euo pipefail`: stop on errors (`-e`), on unset variables (`-u`), and when any command in a pipe fails (`pipefail`).

## 5. Quoting and paths

- Paths with spaces must be quoted: `cd "C:\DE Courses"` / `cd "/c/DE Courses"`.
- Bash: double quotes expand variables (`"$HOME"`), single quotes are literal (`'$HOME'`). Always quote variables: `rm "$file"`, never `rm $file`.
- PowerShell: double quotes expand `$var`, single quotes are literal; use `-LiteralPath` for paths containing `[` `]` or other wildcard characters.

## 6. Environment variables

Environment variables configure programs without changing code (see [[Python Environments and Packaging]]). They are inherited by child processes and last only for the shell session (or the single command, in Bash: `MODE=dev python run.py`). Persistent settings go in profile files or a `.env` file loaded by the application — never committed with real secrets.

## 7. File hashes

A hash identifies exact bytes: same file → same hash. Pipelines use it to detect whether a new input version arrived.

```bash
sha256sum data/landing/olist/olist_orders_dataset.csv
```

```powershell
Get-FileHash -Algorithm SHA256 -LiteralPath data\landing\olist\olist_orders_dataset.csv
```

A different newline style (`\r\n` vs `\n`) or a BOM changes the hash even if the data is logically the same. Do not use byte hashes as the only test of business equivalence.

## 8. CSV pitfalls on the command line

`wc -l` counts newline characters, not CSV records — a quoted field containing a newline breaks the count. `cut -d,` is not a CSV parser and splits quoted commas. Use real parsers (`python -m csv`-based scripts, DuckDB: `duckdb -c "SELECT count(*) FROM 'file.csv'"`, or `csvkit`) for anything beyond a quick look ([[Files CSV JSON and Parquet]]).

## 9. Processes, ports and permissions

- "Port already in use" when starting Postgres or Airflow: find the process (`ss -ltnp`, `Get-NetTCPConnection -LocalPort 5432 | Select OwningProcess`) and decide whether it is an old container or a service you need.
- Stop a process: `kill <pid>` (polite) / `kill -9 <pid>` (forceful); PowerShell `Stop-Process -Id <pid>`.
- Linux permissions: `ls -l` shows `rwx` for owner/group/others; `chmod +x script.sh` makes a script executable. Containers often run as a non-root user, so mounted folders may be unwritable — a common Docker error.

## 10. Applying it to Olist

Daily operations: find the newest run log, extract ERROR lines and the run_id, check that the expected landing files exist and are non-empty, compute their hashes, and find what holds the DuckDB file or Postgres port when a run hangs.

## 11. Common mistakes

| Mistake | Effect | Fix |
|---|---|---|
| Unquoted paths/variables | Breaks on spaces, can delete the wrong files | Quote everything |
| Swallowing errors in scripts | Exit 0 on failure | `set -euo pipefail`; return non-zero |
| `wc -l` as a record count | Wrong counts | Parse the CSV |
| Bash syntax in PowerShell (or vice versa) | Confusing errors | Know which shell you are in |
| Env var set in one terminal, run in another | "It works here but not there" | Log effective config at start |

## 12. Exercises

1. Find the newest log, print its ERROR lines with run_id, and count errors per run — in both shells.
2. Write a script that exits non-zero if any of the 9 Olist CSVs is missing or empty, and prove it with a missing file.
3. Create a CSV with a newline inside quotes and compare `wc -l` with `csv.DictReader`.
4. Start a small server on port 8000 (`python -m http.server`), then find and stop it from another terminal.

## 13. Review questions

> [!question]- How long does an environment variable set in a shell last?
> For that shell session and its child processes only (or a single command with the Bash `VAR=x cmd` form).

> [!question]- How do you tell whether a failure is in the source, your code, or another process holding a lock?
> Check the input files (exist, size, hash, header), read the first traceback and exit code, and inspect processes/ports/locks (`ps`, `ss`, `pg_stat_activity`).

> [!question]- Why must a script return a non-zero exit code on failure?
> Schedulers, CI and shell chains decide success from the exit code; returning 0 hides failures.

> [!question]- What does `set -o pipefail` change?
> A pipeline fails if any command in it fails, not only the last one.

Related: [[Files CSV JSON and Parquet]], [[Observability and Recovery]], [[Module 02 - Git and Linux]]. Sources: [The Missing Semester — shell](https://missing.csail.mit.edu/2020/course-shell/), [PowerShell documentation](https://learn.microsoft.com/en-us/powershell/), [Bash manual](https://www.gnu.org/software/bash/manual/).
