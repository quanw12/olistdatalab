from __future__ import annotations

import re
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
FOUNDATION = ROOT / "01-foundation"

PACE = {
    "01": "15–45 minutes of coding; allow extra time for first setup.",
    "02": "15–45 minutes of coding; allow extra time for first setup.",
    "03": "15–45 minutes of coding; allow extra time for first setup.",
    "04": "15–45 minutes of coding; allow extra time for first setup.",
    "05": "15–45 minutes of coding; allow extra time for first setup.",
    "06": "15–45 minutes of coding; allow extra time for first setup.",
    "07": "2–6 hours across several sessions.",
    "08": "45–120 minutes of coding/checking; environment setup may take longer.",
    "09": "45–120 minutes of coding/checking; environment setup may take longer.",
    "10": "45–120 minutes of coding/checking; environment setup may take longer.",
    "11": "45–120 minutes of coding/checking; environment setup may take longer.",
    "12": "45–120 minutes of coding/checking; environment setup may take longer.",
}

DIFF_LINE = re.compile(r"^\*\*Difficulty:.*$", re.MULTILINE)
SUBMISSIONS = re.compile(
    r"^Use the existing fixtures; your old attempt is in \.\./submissions/[^\n]+\n\n",
    re.MULTILINE,
)
GIT_SECTION = re.compile(r"## Git checkpoint\n\n.*?(?=\n\n\[Course index\])", re.DOTALL)


def git_block(day: str) -> str:
    folder = f"01-foundation/day-{day}"
    return f"""## Git checkpoint

Work on `main`. Stage only this lesson (plus shared project files you changed on purpose).

~~~powershell
Set-Location "C:\\DE Courses"
git checkout main
git pull origin main
git status
git add -- {folder}
git diff --cached --stat
git commit -m "feat(day-{day}): complete the daily DE exercise"
git push origin main
~~~

Generated output stays ignored; put selected evidence in `evidence/` when a guide asks for it.

"""


def main() -> None:
    for guide in sorted(FOUNDATION.glob("day-*/guide.md")):
        day = guide.parent.name.split("-")[1]
        text = guide.read_text(encoding="utf-8")
        dm = re.search(r"\*\*Difficulty: (\w+)\.\*\*", text)
        level = dm.group(1) if dm else "Apply"
        pace = PACE.get(day, "45–120 minutes; split across sessions if needed.")
        text = DIFF_LINE.sub(
            f"**Difficulty: {level}.** {pace} Syntax documentation is allowed; keep approach hints closed until you try.",
            text,
            count=1,
        )
        text = SUBMISSIONS.sub("", text)
        text = re.sub(
            r"Completed reference: your saved work stays completed\. Use this only to repair a demonstrated gap\.\n\n",
            "",
            text,
        )
        if GIT_SECTION.search(text):
            replacement = git_block(day)
            text = GIT_SECTION.sub(lambda _m: replacement, text)
        guide.write_text(text, encoding="utf-8")
    print("Refreshed foundation day guides")


if __name__ == "__main__":
    main()
