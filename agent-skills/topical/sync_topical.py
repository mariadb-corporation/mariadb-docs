#!/usr/bin/env python3
"""
Re-vendor the topical agent-skills from MariaDB/skills.

Downloads each keeper's SKILL.md plus the upstream LICENSE at a resolved ref,
writes them into agent-skills/topical/, and updates:
  - topical/VENDORED.md       (pinned ref + last-synced date)
  - .skills-manifest.json     (topical.vendored_ref)

Run by .github/workflows/sync-topical-skills.yml; that workflow opens a PR only
if anything actually changed (i.e. upstream moved). Vendored verbatim — file
content bugs upstream, do not hand-edit the downloaded files.

Usage:
    sync_topical.py [--ref <branch|tag|sha>] [--date YYYY-MM-DD]

--ref defaults to "main"; it is resolved to the exact commit SHA, which is what
gets recorded (reproducible pin). --date defaults to today (UTC).
"""
from __future__ import annotations

import argparse
import datetime
import json
import re
import sys
import urllib.request
from pathlib import Path

UPSTREAM = "MariaDB/skills"

# The application-developer "keepers" vendored per DOCS-6206. Keep in sync with
# the topical layer in .skills-manifest.json.
KEEPERS = [
    "mariadb-features",
    "mariadb-query-optimization",
    "mariadb-system-versioned-tables",
    "mysql-to-mariadb",
    "mariadb-vector",
]

HERE = Path(__file__).resolve().parent          # agent-skills/topical
SKILLS_ROOT = HERE.parent                        # agent-skills
MANIFEST = SKILLS_ROOT / ".skills-manifest.json"
VENDORED = HERE / "VENDORED.md"

UA = {"User-Agent": "mariadb-docs-sync-topical"}   # GitHub API requires a UA


def fetch(url: str) -> bytes:
    req = urllib.request.Request(url, headers=UA)
    with urllib.request.urlopen(req, timeout=30) as resp:
        return resp.read()


def resolve_sha(ref: str) -> str:
    data = json.loads(fetch(f"https://api.github.com/repos/{UPSTREAM}/commits/{ref}"))
    return data["sha"]


def raw_url(sha: str, path: str) -> str:
    return f"https://raw.githubusercontent.com/{UPSTREAM}/{sha}/{path}"


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--ref", default="main",
                        help="upstream branch/tag/sha to vendor (default: main)")
    parser.add_argument("--date", help="last-synced date (default: today, UTC)")
    args = parser.parse_args()

    sha = resolve_sha(args.ref)
    date = args.date or datetime.datetime.now(datetime.timezone.utc).date().isoformat()

    # Download the keeper SKILL.md files + the upstream LICENSE, verbatim.
    for name in KEEPERS:
        dest = HERE / name / "SKILL.md"
        dest.parent.mkdir(parents=True, exist_ok=True)
        dest.write_bytes(fetch(raw_url(sha, f"{name}/SKILL.md")))
    (HERE / "LICENSE").write_bytes(fetch(raw_url(sha, "LICENSE")))

    # Update the VENDORED.md provenance table (line-oriented, robust to spacing).
    v = VENDORED.read_text(encoding="utf-8")
    v = re.sub(r"^\| Pinned ref \(commit\) \|.*$",
               f"| Pinned ref (commit) | `{sha}` |", v, flags=re.M)
    v = re.sub(r"^\| Last synced \|.*$",
               f"| Last synced | {date} |", v, flags=re.M)
    VENDORED.write_text(v, encoding="utf-8")

    # Update the manifest's topical.vendored_ref.
    m = MANIFEST.read_text(encoding="utf-8")
    m = re.sub(r'("vendored_ref": ")[^"]*(")', lambda x: x.group(1) + sha + x.group(2), m)
    json.loads(m)   # validate before writing
    MANIFEST.write_text(m, encoding="utf-8")

    print(f"vendored {UPSTREAM}@{sha} ({date})")
    return 0


if __name__ == "__main__":
    sys.exit(main())
