"""Lab 01 — Python basics on Olist-shaped data.

Replace each `raise NotImplementedError` with your code until `pytest labs/01-python` is green.
Use only the standard library. Read the hint in each docstring first; read the reference code
(src/olist_platform) only after your version passes.
"""

from __future__ import annotations

from datetime import datetime
from pathlib import Path


def normalize_status(raw: str | None) -> str:
    """Return the status trimmed and lowercased: " Delivered " -> "delivered".

    Raise ValueError when raw is None or only spaces, so a bad row fails loudly instead of
    becoming an empty status.
    Hint: two string methods, one `if`.
    """
    raise NotImplementedError


def parse_olist_time(text: str) -> datetime | None:
    """Parse "YYYY-MM-DD HH:MM:SS" (Sao Paulo local time) and return it as a UTC datetime.

    - "" or "   " -> None (the step has not happened yet)
    - unparseable text -> ValueError whose message contains the bad text
    Hint: datetime.strptime, ZoneInfo("America/Sao_Paulo"), .astimezone(timezone.utc)
    """
    raise NotImplementedError


def find_duplicates(ids: list[str]) -> set[str]:
    """Return every id that appears more than once.

    Must handle 200,000 ids in well under a second (one pass).
    Hint: two sets — `seen` and `duplicates`.
    """
    raise NotImplementedError


def read_orders(path: Path) -> list[tuple[int, dict]]:
    """Read the orders CSV and return (line_number, row_dict) pairs.

    The header is line 1, so the first data row is line 2. Accept files saved with a UTF-8 BOM.
    Raise FileNotFoundError with the path in the message if the file is missing.
    Hint: csv.DictReader + enumerate(..., start=2); encoding="utf-8-sig"
    """
    raise NotImplementedError


def summarize_status(rows: list[tuple[int, dict]]) -> dict[str, int]:
    """Count orders per normalized status: {"delivered": 1234, "shipped": 12, ...}.

    Hint: reuse normalize_status; a dict or collections.Counter.
    """
    raise NotImplementedError
