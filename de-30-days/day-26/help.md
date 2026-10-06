# Day 26 — Continuous integration with GitHub Actions


1. Create the .github/workflows directories at C:\DE Courses, not inside capstone. YAML indentation must use spaces.
2. Copy the small syntax shape, replace the demo step with dependency/test commands, and set the job run directory.
3. Install from the requirements files you created. If you kept pytest separate, install that development file or pytest explicitly.
4. Use the same -m "not integration" selection locally and remotely. If collection still connects to DB, move that connection into a marked fixture/test body.
5. Run git diff and inspect .github/workflows/ci.yml. Stage it explicitly in addition to the usual daily files:
   git add -- .github/workflows/ci.yml
6. Push your current feature branch, open Actions on GitHub, inspect the failing step if red. A missing file usually means wrong path or an uncommitted dependency file; ModuleNotFoundError may mean wrong working directory or installation.
7. Do not claim the remote run succeeded from local pytest output alone.
