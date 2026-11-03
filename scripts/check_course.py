"""Validate the course vault and run explicitly marked, local teaching examples.

Run from any directory: python scripts/check_course.py
Requires the project's core dependencies (DuckDB, pandas, pyarrow, PyYAML).
Only blocks marked '# runnable' / '-- runnable' are executed; service/cloud/CLI
patterns are intentionally excluded. No calls to real APIs or cloud resources.
"""

from __future__ import annotations

import json
import math
import re
from datetime import date, datetime
from decimal import Decimal
from pathlib import Path
from urllib.parse import unquote, urlsplit

import duckdb
import yaml

ROOT = Path(__file__).resolve().parents[1]
VAULT = ROOT / "DEcourse"
# Letters used by Vietnamese but not Portuguese (Olist reviews), plus common unaccented words.
VIETNAMESE = re.compile(
    r"[\u0102\u0103\u0110\u0111\u01a0\u01a1\u01af\u01b0\u1ea0-\u1ef9]"
    r"|\b(?:va|cua|khong|nhung|duoc|nguoi|bat dau|chuyen sau|ghi chu|nhat ky)\b",
    re.IGNORECASE,
)


def equivalent(actual, expected) -> bool:
    if isinstance(actual, (date, datetime)):
        actual = actual.isoformat()
    if isinstance(actual, (int, float, Decimal)) and isinstance(expected, (int, float)):
        return math.isclose(float(actual), float(expected), rel_tol=1e-9, abs_tol=1e-12)
    if isinstance(actual, (list, tuple)) and isinstance(expected, (list, tuple)):
        return len(actual) == len(expected) and all(
            equivalent(left, right) for left, right in zip(actual, expected, strict=True)
        )
    return actual == expected


def main() -> None:
    notes = sorted(VAULT.rglob("*.md"))
    stems: dict[str, Path] = {}
    for path in notes:
        if path.stem in stems:
            raise AssertionError(f"Ambiguous wikilink name: {path.stem}")
        stems[path.stem] = path

    python_examples = sql_examples = wiki_links = 0
    for path in notes:
        content = path.read_text(encoding="utf-8-sig")
        if content.startswith("---\n"):
            properties = yaml.safe_load(content.split("---", 2)[1])
            assert isinstance(properties, dict), path
        assert len(re.findall(r"^```", content, re.MULTILINE)) % 2 == 0, path
        prose = re.sub(r"^```[^\n]*\n.*?^```[ \t]*$", "", content,
                       flags=re.MULTILINE | re.DOTALL)
        for target in re.findall(r"\[\[([^\]]+)\]\]", prose):
            name = target.split("|", 1)[0].split("#", 1)[0].removesuffix(".md")
            if name:
                assert name in stems, f"Broken wikilink {target} in {path}"
            wiki_links += 1

        for language, code in re.findall(
            r"^```(python|sql)\n(.*?)^```\s*$", content, re.MULTILINE | re.DOTALL
        ):
            if language == "python" and code.startswith("# runnable\n"):
                exec(compile(code, str(path), "exec"), {"__name__": "__course_example__"})
                python_examples += 1
            elif language == "sql" and code.startswith("-- runnable\n"):
                specification = re.search(r"^-- expect: (.+)$", code, re.MULTILINE)
                assert specification, f"Missing expected result in {path}"
                with duckdb.connect() as connection:
                    actual = connection.execute(code).fetchall()
                expected = json.loads(specification.group(1))
                assert equivalent(actual, expected), (path, actual, expected)
                sql_examples += 1

    # The vault holds every lesson and stays self-contained: English only, no links into the repo.
    for path in notes:
        text = path.read_text(encoding="utf-8-sig")
        match = VIETNAMESE.search(text)
        assert not match, f"Vietnamese text {match.group()!r} in {path}"
        for target in re.findall(r"(?<!!)\[[^\]]+\]\(([^)]+)\)", text):
            if not urlsplit(target).scheme and not target.startswith("#"):
                resolved = (path.parent / unquote(urlsplit(target).path)).resolve()
                assert resolved.is_relative_to(VAULT.resolve()), (
                    f"Link leaves the vault: {target} in {path}")

    # Check ordinary relative Markdown links in the vault and the repo entry points.
    paths = [*notes, ROOT / "README.md", ROOT / "labs" / "README.md"]
    for path in paths:
        for target in re.findall(r"(?<!!)\[[^\]]+\]\(([^)]+)\)",
                                 path.read_text(encoding="utf-8-sig")):
            parsed = urlsplit(target)
            if parsed.scheme or target.startswith("#"):
                continue
            linked = path.parent / unquote(parsed.path)
            assert linked.exists(), f"Broken Markdown link {target} in {path}"

    for path in (VAULT / ".obsidian").glob("*.json"):
        json.loads(path.read_text(encoding="utf-8"))

    print(f"Validated {len(notes)} vault notes, {wiki_links} wikilinks, relative links and config")
    print(f"Executed {python_examples} Python and {sql_examples} SQL examples with assertions")


if __name__ == "__main__":
    main()
