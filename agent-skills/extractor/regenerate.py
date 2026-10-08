#!/usr/bin/env python3
"""
Regenerate the GENERATED blocks of the Tier 2 function-category skills.

For each Tier 2 skill, runs extract_function_category.py against its canonical
source directory and splices the output between the skill's

    <!-- BEGIN GENERATED -->
    ...
    <!-- END GENERATED -->

markers, leaving the hand-written scaffold (frontmatter, intro, the
"What LLMs Often Miss" table, See Also) untouched.

Usage:
    regenerate.py            # rewrite stale skills in place
    regenerate.py --check    # report drift, write nothing, exit 1 if any stale

`--check` is for CI verification; the plain form is what the
extract-function-skills.yml workflow runs before opening a regeneration PR.

The skill -> source-directory map lives here (build config), not in
.skills-manifest.json (a consumer-facing index). Add a line when a new Tier 2
skill is created.
"""
from __future__ import annotations

import argparse
import re
import subprocess
import sys
from pathlib import Path

HERE = Path(__file__).resolve().parent          # agent-skills/extractor
SKILLS_ROOT = HERE.parent                        # agent-skills
REPO_ROOT = SKILLS_ROOT.parent                   # repo root
SQLF = REPO_ROOT / "server" / "reference" / "sql-functions"

# Tier 2 skill directory name -> source category dir (relative to sql-functions/).
CATEGORIES = {
    "mariadb-json-functions": "special-functions/json-functions",
    "mariadb-string-functions": "string-functions",
    "mariadb-date-time-functions": "date-time-functions",
    "mariadb-numeric-functions": "numeric-functions",
    "mariadb-aggregate-functions": "aggregate-functions",
    "mariadb-control-flow-functions": "control-flow-functions",
    "mariadb-window-functions": "special-functions/window-functions",
    "mariadb-information-functions": "secondary-functions/information-functions",
    "mariadb-vector-functions": "vector-functions",
    "mariadb-encryption-functions": "secondary-functions/encryption-hashing-and-compression-functions",
}

MARKER_RE = re.compile(
    r"(<!-- BEGIN GENERATED -->\n).*?(\n<!-- END GENERATED -->)", re.DOTALL
)


def generate(category: str) -> str:
    """Run the extractor for one category and return its Markdown, trimmed.

    Invoked with a repo-relative path and cwd=REPO_ROOT so the extractor's
    `<!-- Extracted from … -->` comment is stable regardless of where this
    script runs from (absolute paths would make the output non-reproducible).
    """
    rel = f"server/reference/sql-functions/{category}"
    result = subprocess.run(
        [sys.executable, "agent-skills/extractor/extract_function_category.py", rel],
        cwd=REPO_ROOT, capture_output=True, text=True, check=True,
    )
    return result.stdout.rstrip("\n")


def regen_skill(skill_name: str, category: str, check: bool) -> bool:
    """Regenerate one skill's GENERATED block. Returns True if it changed."""
    skill = SKILLS_ROOT / "granular" / "functions" / skill_name / "SKILL.md"
    text = skill.read_text(encoding="utf-8")
    if not MARKER_RE.search(text):
        raise SystemExit(f"{skill}: missing BEGIN/END GENERATED markers")
    entries = generate(category)
    new = MARKER_RE.sub(lambda m: m.group(1) + entries + m.group(2), text)
    changed = new != text
    if changed and not check:
        skill.write_text(new, encoding="utf-8")
    return changed


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--check", action="store_true",
                        help="report drift without writing; exit 1 if any stale")
    args = parser.parse_args()

    stale = [name for name, cat in CATEGORIES.items()
             if regen_skill(name, cat, args.check)]

    if stale:
        print(("stale: " if args.check else "regenerated: ") + ", ".join(stale))
    else:
        print("all Tier 2 function skills up to date")
    return 1 if (args.check and stale) else 0


if __name__ == "__main__":
    sys.exit(main())
