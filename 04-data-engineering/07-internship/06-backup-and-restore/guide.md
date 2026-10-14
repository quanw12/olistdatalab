# DE28 — Back up and prove a database restore

**Difficulty: Integrate.** Allow 2–4 hours. Prerequisites: native PostgreSQL, DE06 and DE11.

[Module](../README.md) · [Previous: DE27](../05-source-discovery/guide.md)

1. Read [lesson.md](lesson.md) and [exercise.md](exercise.md).
2. In pgAdmin, create **two new empty disposable databases**, de_restore_source
   and de_restore_target. Use the same lab owner. If either name already exists,
   inspect it and choose a new owned lab name; do not drop/reset an existing database.
3. Use [bootstrap.sql](bootstrap.sql) only on the new source. Finish your own
   [checks.sql](checks.sql) and record the baseline before dumping.
4. Dump, inspect, change the source, and restore into the empty target.
5. Verify with your SQL, record recovery evidence and compare [expected.md](expected.md).
   Open [help.md](help.md) only for a specific problem.

## Commands — Windows PowerShell, PostgreSQL 18

Confirm your installation path/port. These are operational syntax, not a finished
verification solution. Use -W for a password prompt; do not put passwords in commands.
Substitute your two owned lab names consistently if changed.

~~~powershell
Set-Location "C:\DE Courses\04-data-engineering\07-internship\06-backup-and-restore"
$pgLabBin = "C:\Program Files\PostgreSQL\18\bin"
& "$pgLabBin\pg_dump.exe" --version
& "$pgLabBin\psql.exe" -h localhost -p 5432 -U postgres -W -d de_restore_source -v ON_ERROR_STOP=1 -f .\bootstrap.sql
# Run your checks.sql on the source and save a sanitized baseline in notes.md.
New-Item -ItemType Directory -Path .\output -Force
& "$pgLabBin\pg_dump.exe" -h localhost -p 5432 -U postgres -W -d de_restore_source -Fc -f .\output\restore.dump
# Continue only if the exit code is 0 and inspect the archive:
& "$pgLabBin\pg_restore.exe" --list .\output\restore.dump
# NOW run after-backup.sql only on de_restore_source.
& "$pgLabBin\psql.exe" -h localhost -p 5432 -U postgres -W -d de_restore_source -v ON_ERROR_STOP=1 -f .\after-backup.sql
$restoreTimer = [System.Diagnostics.Stopwatch]::StartNew()
& "$pgLabBin\pg_restore.exe" -h localhost -p 5432 -U postgres -W -d de_restore_target --no-owner --no-acl --exit-on-error --single-transaction .\output\restore.dump
# Inspect $LASTEXITCODE before verification.
~~~

Keep the timer running while you execute your checks.sql on the target in pgAdmin.
After the data and constraint checks finish, return to the same PowerShell session:

~~~powershell
$restoreTimer.Stop()
$restoreTimer.Elapsed.TotalSeconds
~~~

For a measured RTO, include your verification time: leave the timer running while
you run checks in pgAdmin, and stop it afterward. A dump file or zero restore exit
code alone does not prove a usable recovery.

Do not use --clean or --create in this drill. Restore into the empty target selected
explicitly. These lab commands omit restored ownership/grants; they do not reproduce
a production access policy. Keep binary dumps and generated evidence in ignored output/.

## Commit after verification

~~~powershell
Set-Location "C:\DE Courses"
git status
git branch --show-current
git add -- "04-data-engineering/07-internship/06-backup-and-restore"
git diff --cached
git commit -m "feat(engineering): complete de28 restore rehearsal"
git push origin main
~~~

Work on `main`; record sanitized conclusions in notes.md.
[Next: DE29](../07-applications-and-interviews/guide.md)
