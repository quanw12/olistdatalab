"""One-off maintenance: reset study navigation and main-branch Git blocks."""
from __future__ import annotations

import re
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]

DIFFICULTY_OLD = re.compile(
    r"\*\*Difficulty: ([^*]+)\*\*\. [^\n]+\n(?:Completed reference:[^\n]+\n)?",
    re.MULTILINE,
)

BEFORE_STARTING_SUB = re.compile(
    r"Use the existing fixtures; your old attempt is in \.\./submissions/[^\n]+\n\n",
)

GIT_BLOCK = re.compile(
    r"## Git checkpoint\n\n.*?(?=\n\n(?:The curriculum|\[Course index\]|$))",
    re.DOTALL,
)

FEATURE_PUSH = re.compile(
    r"git push -u origin (?:HEAD|\$lessonBranch)\n",
)


def foundation_git_block(day: str) -> str:
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


def normalize_foundation_guide(path: Path) -> bool:
    text = path.read_text(encoding="utf-8")
    original = text
    m = re.match(r"# Day (\d{2})", text)
    if not m:
        return False
    day = m.group(1)

    text = DIFFICULTY_OLD.sub(r"**Difficulty: \1.**\n\n", text)
    text = BEFORE_STARTING_SUB.sub("", text)

    if "## Git checkpoint" in text:
        text = GIT_BLOCK.sub(foundation_git_block(day), text)

    if "The curriculum itself must be committed first" in text:
        text = text.replace(
            "The curriculum itself must be committed first using the repository README's commands. "
            "These daily commands stage only today's work and shared project changes. "
            "Generated output remains ignored; selected sanitized evidence belongs in evidence/.\n\n",
            "",
        )
    if text != original:
        path.write_text(text, encoding="utf-8")
        return True
    return False


def normalize_generic_guide(path: Path) -> bool:
    text = path.read_text(encoding="utf-8")
    original = text
    text = text.replace("Use your feature/... branch", "Work on `main`")
    text = text.replace("Use your current feature/... branch", "Work on `main`")
    text = text.replace("Keep your feature/... convention", "Commit on `main`")
    text = text.replace("feature/... branch convention", "`main` branch workflow")
    text = FEATURE_PUSH.sub("git push origin main\n", text)
    text = re.sub(
        r"If starting a later study session from an updated main branch, you may first create feature/[^\n]+\n",
        "",
        text,
    )
    text = re.sub(
        r"Stay on your current feature branch\. ",
        "",
        text,
    )
    text = re.sub(
        r"Use your existing feature/\.\.\. branch, or create feature/[^\n]+\n",
        "Work on `main`.\n",
        text,
    )
    if original != text:
        path.write_text(text, encoding="utf-8")
        return True
    return False


def main() -> None:
    changed = 0
    for guide in ROOT.rglob("guide.md"):
        if "submissions" in guide.parts:
            continue
        if (
            len(guide.parts) >= 2
            and guide.parts[0] == "01-foundation"
            and guide.parent.name.startswith("day-")
        ):
            if normalize_foundation_guide(guide):
                changed += 1
        elif normalize_generic_guide(guide):
            changed += 1
    print(f"Updated {changed} guide.md files")


if __name__ == "__main__":
    main()
