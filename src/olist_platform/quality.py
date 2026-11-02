"""Contract checks that run against a bronze table before it is published.

Each check is one SQL query that counts failing rows, so it scales to the full dataset and the
result is a number you can log, store and alert on.
"""

from __future__ import annotations

from dataclasses import dataclass

import duckdb

from olist_platform.contracts import TableContract


@dataclass(frozen=True)
class CheckResult:
    table: str
    check: str
    severity: str  # "error" stops the run, "warn" is logged
    failed_rows: int

    @property
    def passed(self) -> bool:
        return self.failed_rows == 0


def _q(name: str) -> str:
    return '"' + name.replace('"', '""') + '"'


def _blank(column: str) -> str:
    return f"NULLIF(TRIM({_q(column)}), '') IS NULL"


def build_checks(
    contract: TableContract, relation: str, timestamp_format: str
) -> list[tuple[str, str, str]]:
    """Return (check name, severity, SQL that counts failing rows) for one table."""
    checks: list[tuple[str, str, str]] = []
    if contract.primary_key:
        key = ", ".join(_q(c) for c in contract.primary_key)
        any_blank = " OR ".join(_blank(c) for c in contract.primary_key)
        checks.append((f"primary_key_not_null({key})", "error",
                       f"SELECT count(*) FROM {relation} WHERE {any_blank}"))
        checks.append((f"primary_key_unique({key})", "error",
                       f"SELECT coalesce(sum(n - 1), 0) FROM "
                       f"(SELECT count(*) AS n FROM {relation} GROUP BY {key} HAVING n > 1)"))
    for column in contract.not_null:
        checks.append((f"not_null({column})", "error",
                       f"SELECT count(*) FROM {relation} WHERE {_blank(column)}"))
    for column, values in contract.accepted_values.items():
        allowed = ", ".join("'" + v.replace("'", "''") + "'" for v in values)
        checks.append((f"accepted_values({column})", "error",
                       f"SELECT count(*) FROM {relation} WHERE NOT {_blank(column)} "
                       f"AND lower(trim({_q(column)})) NOT IN ({allowed})"))
    for column in contract.timestamps:
        checks.append((f"parseable_timestamp({column})", "error",
                       f"SELECT count(*) FROM {relation} WHERE NOT {_blank(column)} "
                       f"AND try_strptime(trim({_q(column)}), '{timestamp_format}') IS NULL"))
    for column in contract.numeric:
        checks.append((f"numeric({column})", "error",
                       f"SELECT count(*) FROM {relation} WHERE NOT {_blank(column)} "
                       f"AND try_cast(trim({_q(column)}) AS DOUBLE) IS NULL"))
    if contract.name == "orders":
        # Odd but real: kept, counted, explained in docs/data-contract.md.
        checks.append(("delivered_without_delivery_date", "warn",
                       f"SELECT count(*) FROM {relation} WHERE lower(trim(order_status)) = "
                       f"'delivered' AND {_blank('order_delivered_customer_date')}"))
        checks.append(("status_needs_normalizing", "warn",
                       f"SELECT count(*) FROM {relation} "
                       f"WHERE order_status <> lower(trim(order_status))"))
    return checks


def run_checks(
    con: duckdb.DuckDBPyConnection,
    contract: TableContract,
    relation: str,
    timestamp_format: str,
) -> list[CheckResult]:
    results = []
    for name, severity, sql in build_checks(contract, relation, timestamp_format):
        failed = con.execute(sql).fetchone()[0]
        results.append(CheckResult(contract.name, name, severity, int(failed)))
    return results
