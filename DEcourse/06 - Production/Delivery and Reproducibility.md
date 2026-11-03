---
tags: [decourse, delivery, reproducibility]
module: 21
---

# Delivery and Reproducibility

> [!info] Learning goals
> After this note you can: define what "reproducible" means for a data pipeline (code, environment, input, configuration); write a release manifest; separate dev, sample and prod environments; prove a fresh clone works; version releases semantically; make schema changes backward-compatible; and plan rollbacks for code, schema and data separately.

## 1. Reproducibility has four parts

A result is reproducible when someone else can produce it again from the repository. That requires pinning all four:

| Part | Pin it with |
|---|---|
| **Code** | Git commit SHA, release tag |
| **Environment** | Python version, lock/constraints file, dbt + adapter versions, container image digest, OS |
| **Input** | Input snapshot hash / version, data interval |
| **Configuration** | Env vars and config files (non-secret), recorded per run |

"It runs on my machine" must become commands, configuration and evidence.

## 2. The release manifest

```yaml
# Pattern: fill in with values you measured; never copy placeholders as results.
release:
  version: "1.2.0"
  git_commit: "fill-in-sha"
  python: "fill-in-version"
  os: "fill-in-os"
  dependencies_lock: "fill-in-file-and-hash"
  dbt_adapter: "fill-in-version"
  image_digest: "fill-in-digest-if-any"
  input_snapshot_sha256: "fill-in-hash"
  data_interval: "fill-in-start-end"
  checks: {tests: "passed", reconciliation: "passed"}
```

Generate it automatically at the end of a successful run and store it with the outputs. It answers "exactly what produced this table?" months later.

```python
# runnable
import hashlib
import json
import platform
import sys

def manifest(commit: str, inputs: dict[str, bytes], interval: tuple[str, str]) -> dict:
    return {
        "git_commit": commit,
        "python": sys.version.split()[0],
        "os": platform.system(),
        "inputs": {name: hashlib.sha256(data).hexdigest() for name, data in sorted(inputs.items())},
        "data_interval": list(interval),
    }

m = manifest("abc1234", {"orders.csv": b"order_id\no1\n"}, ("2018-01-01", "2018-02-01"))
assert json.loads(json.dumps(m)) == m
assert len(m["inputs"]["orders.csv"]) == 64
```

## 3. Environments

| Environment | Data | Purpose | Who writes |
|---|---|---|---|
| sample/dev | generated or small sample | development, fast tests | you |
| staging | copy of real, possibly masked | integration, drills | CI / you |
| prod | real | consumers | pipeline service account only |

Separate them with configuration (`OLIST_DATA_DIR`, `DUCKDB_PATH`, dbt targets, cloud projects), never by editing code. Make it impossible for sample runs to overwrite real data (see [[Python Environments and Packaging]]).

## 4. The fresh-clone test

1. Create a clean venv, install pinned dependencies, run `pip check`.
2. Run unit + integration tests and the sample batch; record any skips or errors.
3. Clone into another folder (or WSL / another machine) and run again from the README only.
4. Check counts, keys, money, outputs and permissions — not just exit codes.
5. Save the manifest and commit; review before publishing.

Record the OS you actually tested; a Windows success says nothing about Linux paths, line endings or case sensitivity.

## 5. Versioning and compatible changes

Semantic versioning for data products: **MAJOR** = breaking change (column removed/renamed/type changed, grain changed), **MINOR** = backward-compatible addition (new nullable column, new table), **PATCH** = fixes with no contract change.

Safe change patterns:

- **Expand → migrate → contract:** add the new column alongside the old, move consumers, then remove the old one after a deprecation window.
- **Versioned tables or views:** `fct_orders_v2` next to `fct_orders_v1`; a view `fct_orders` points to the current version.
- **Never change the meaning of a column in place** — create a new column with a new name.

## 6. Rollback

Rolling back code does **not** roll back schema or data.

| What changed | Rollback path |
|---|---|
| Code/config only | Redeploy the previous tag; rerun affected intervals |
| Compatible schema addition | Old code ignores the new column; consumers move gradually |
| Breaking schema change | Migration with a down path, versioned tables/views, or a forward fix |
| Data already published wrong | Restore last good version or rebuild from raw with the old code |

Keep raw inputs and versions so any release can be rebuilt. Practise the rollback before you need it.

> [!warning] Reference implementation limits
> Publishing each table with DROP/RENAME has limits around grants, indexes, dependent views and multi-table consistency. In production drills, verify the reader after each publish and choose a serving strategy that fits.

## 7. CI/CD for data

- **CI** on every PR: lint, tests, dbt build on sample data, docs.
- **CD** on merge/tag: build the image, deploy DAGs/config, run migrations, publish the manifest.
- Data-aware checks before switching consumers: reconciliation and contract tests on the new version (blue/green or write-audit-publish).

## 8. Applying it to Olist

Module 21: add an optional column, deploy v2, roll back to v1 and prove the consumer still reads; then design the safe path for a breaking type change. Produce a manifest from a fresh clone.

## 9. Common mistakes

| Mistake | Effect | Fix |
|---|---|---|
| Unpinned dependencies | "Same code, different result" | Lock/constraints, image digests |
| No input version recorded | Cannot reproduce outputs | Manifest with input hashes |
| Renaming columns in place | Consumers break | Expand → migrate → contract |
| Assuming code rollback restores data | Wrong data stays | Separate data rollback plan |
| Testing only on the author's machine | Hidden environment assumptions | Fresh-clone test on a second environment |

## 10. Exercises

1. Generate a manifest at the end of your pipeline run and store it beside the outputs.
2. Add a non-required column, deploy v2, roll back to v1, prove the consumer still reads.
3. Change a column type in a breaking way and write the safe migration plan.
4. List three environment differences that can cause "same code, different result".

> [!example]- Possible answers for 4
> Different library versions (pandas/dbt adapter), different timezone or locale settings, different input data (sample vs real, different snapshot), different OS behaviour (paths, line endings, case sensitivity), different default encodings.

## 11. Review questions

> [!question]- What four things must be pinned for reproducibility?
> Code, environment, input data version and configuration.

> [!question]- Why doesn't a code rollback fix wrong published data?
> The data was already written; you must restore the last good version or rebuild it from raw with the correct code.

> [!question]- How do you rename a column without breaking consumers?
> Add the new column, keep the old one (or a compatibility view), migrate consumers, then remove the old column after a deprecation window.

Related: [[Python Environments and Packaging]], [[Git Branches PRs and Review]], [[Architecture Decision Record]], [[Module 21 - Security and Delivery]]. Sources: [pip repeatable installs](https://pip.pypa.io/en/stable/topics/repeatable-installs/), [Semantic Versioning](https://semver.org/).
