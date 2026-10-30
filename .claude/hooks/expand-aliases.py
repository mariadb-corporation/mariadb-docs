#!/usr/bin/env python3
"""
expand-aliases.py — run the GitBook alias expansion locally.

WHY THIS EXISTS: .github/workflows/expand-gitbook-aliases.yml is `on: pull_request`, so a
commit that goes straight to `main` is never seen by it (the workflow's own comments say as
much). This repo's docs are frequently committed directly to main, which means the alias
expansion — and, more importantly, the *check* that catches an alias nothing can expand —
simply never runs for them. GitBook then publishes the unexpanded target as a plausible
github.com URL that 404s, and lychee cannot catch it because link-check-pr.yml excludes any
URL containing a brace. This script closes that gap for the direct-to-main path.

NOT A SECOND SOURCE OF TRUTH: the alias table is *parsed out of the workflow file* at runtime
rather than copied here, so the workflow stays canonical and this cannot silently drift from
CI. If the workflow's sed lines are reformatted beyond recognition, this exits non-zero saying
so — loudly wrong rather than quietly stale.

Usage:
    expand-aliases.py [--write] [--base REF] [paths ...]

    (no args)     Check staged + unstaged Markdown. Read-only. Exit 1 if anything needs
                  expanding or an unknown alias is found.
    --write       Actually rewrite the files, expanding every known alias.
    --base REF    Scope to files changed against REF (e.g. --base origin/main) instead of
                  the working tree's staged+unstaged set. nightly-aliascheck.yml runs exactly
                  this with a rolling 24-hour base, which is how an alias that reached main
                  outside a PR -- a GitBook-UI edit, a direct push -- still gets reported
                  (DOCS-6588).
    paths         Check/expand exactly these files, skipping discovery.

Deliberately NOT wired into pre-commit.sh as an auto-rewrite. Files changing underneath a
commit you have already staged is exactly the kind of surprise the push-by-hand review gate
exists to prevent. Run it, look at the diff, then commit.

Exit: 0 = nothing to do. 1 = aliases need expanding (check mode) or unknown alias found.
      2 = could not parse the workflow / bad invocation.
"""

import argparse
import os
import pathlib
import re
import subprocess
import sys

WORKFLOW = ".github/workflows/expand-gitbook-aliases.yml"

# The link-target positions the workflow rewrites, translated from POSIX ERE to Python:
# directly after a Markdown link's "](", after a reference-style definition's "]:", after a
# content-ref's url=", or after an HTML href=". An alias-looking string anywhere else in the
# prose is left alone — the ColumnStore CMAPI pages document
# https://{server}:{port}/cmapi/{version}/... where {server} is a hostname placeholder.
PREFIX = r'(^[ \t]*\[[^\]]*\]:[ \t]*|\]\(|url="|href=")'

# Mirrors the workflow's git pathspec exclusions: these files hold aliases as documentation
# examples. Every other README.md is fair game (DOCS-6481).
EXCLUDE_DIRS = ("dev-docs/", ".claude/")
EXCLUDE_EXACT = ("README.md", "pdf/README.md")
EXCLUDE_SUFFIX = ("/CONTRIBUTING.md", "/general-resources/about/readme/about-links.md")


def die(msg):
    """Exit 2, as the docstring promises. A bare sys.exit(msg) exits 1 -- the "found
    something" code -- so the nightly digest would have reported a parse failure as a
    finding and stayed green (DOCS-6588)."""
    print(msg, file=sys.stderr)
    sys.exit(2)


def repo_root():
    try:
        out = subprocess.run(["git", "rev-parse", "--show-toplevel"],
                             capture_output=True, text=True, check=True)
        return pathlib.Path(out.stdout.strip())
    except (subprocess.CalledProcessError, FileNotFoundError):
        die("expand-aliases: not inside a git work tree.")


def load_aliases(root):
    """Parse the alias table out of the workflow's sed expressions."""
    wf = root / WORKFLOW
    if not wf.is_file():
        die(f"expand-aliases: {WORKFLOW} not found — cannot read the alias table.")
    text = wf.read_text(encoding="utf-8")
    # Matches:  [{]server[}]#\1https://app.gitbook.com/o/.../s/...#g
    pairs = re.findall(r"\[\{\]([A-Za-z0-9_-]+)\[\}\]#\\1([^#]+)#g", text)
    if not pairs:
        die(f"expand-aliases: found no alias definitions in {WORKFLOW}. The workflow's "
                 "sed lines may have been reformatted; update this parser rather than "
                 "hardcoding the table.")
    return dict(pairs)


def excluded(rel):
    if rel.startswith(EXCLUDE_DIRS) or rel in EXCLUDE_EXACT:
        return True
    # Match against "/" + rel so a suffix also matches at the repo root: the workflow's
    # ':(exclude,glob)**/CONTRIBUTING.md' covers the top-level CONTRIBUTING.md (** matches
    # zero directories), and a bare endswith("/CONTRIBUTING.md") did not (DOCS-6588).
    return any(("/" + rel).endswith(s) for s in EXCLUDE_SUFFIX)


def discover(root, base):
    # R as well as ACM: git diff detects renames by default, and a renamed page carrying an
    # alias would otherwise drop out of scope. The workflow's own list uses
    # --diff-filter=d (everything but deletions), which includes renames.
    if base:
        cmds = [["git", "diff", "--name-only", "--diff-filter=ACMR", f"{base}...HEAD"]]
    else:
        cmds = [["git", "diff", "--name-only", "--diff-filter=ACMR"],
                ["git", "diff", "--cached", "--name-only", "--diff-filter=ACMR"]]
    seen = []
    for cmd in cmds:
        out = subprocess.run(cmd + ["--", "*.md"], capture_output=True, text=True, cwd=root)
        # A bad --base makes git diff fail with empty stdout, which used to read as "no
        # Markdown files in scope" and exit 0 -- a silent pass on exactly the input a
        # scheduled job gets wrong.
        if out.returncode:
            die(f"expand-aliases: {' '.join(cmd)} failed: {out.stderr.strip()}")
        for line in out.stdout.splitlines():
            if line and line not in seen:
                seen.append(line)
    return [f for f in seen if not excluded(f)]


def main():
    ap = argparse.ArgumentParser(add_help=False)
    ap.add_argument("--write", action="store_true")
    ap.add_argument("--base")
    ap.add_argument("paths", nargs="*")
    ap.add_argument("-h", "--help", action="store_true")
    args = ap.parse_args()
    if args.help:
        print(__doc__)
        return 0

    root = repo_root()
    aliases = load_aliases(root)
    known = re.compile(PREFIX + r"\{(" + "|".join(map(re.escape, aliases)) + r")\}",
                       re.MULTILINE)
    # Any brace-alias still in a link target that is NOT in the table: a typo, or a new space
    # nobody added to the workflow. Nothing downstream catches it.
    any_alias = re.compile(PREFIX + r"\{([A-Za-z0-9_-]+)\}", re.MULTILINE)

    if args.paths:
        files = [os.path.relpath(os.path.abspath(p), root) for p in args.paths]
        skipped = [f for f in files if excluded(f)]
        for f in skipped:
            print(f"skip (holds aliases as examples): {f}")
        files = [f for f in files if not excluded(f)]
    else:
        files = discover(root, args.base)

    if not files:
        print("expand-aliases: no Markdown files in scope.")
        return 0

    expanded_total = 0
    touched, known_hits, unknown_hits = [], [], []

    for rel in files:
        path = root / rel
        if not path.is_file():
            continue
        text = path.read_text(encoding="utf-8")

        new, n = known.subn(lambda m: m.group(1) + aliases[m.group(2)], text)
        for m in known.finditer(text):
            line = text[:m.start()].count("\n") + 1
            known_hits.append(f"{rel}:{line}: {{{m.group(2)}}}")
        if n:
            expanded_total += n
            touched.append((rel, n))
            if args.write:
                path.write_text(new, encoding="utf-8")

        # Report unknown aliases against the post-expansion text, exactly as the workflow's
        # check step runs after its expansion step.
        for m in any_alias.finditer(new):
            if m.group(2) not in aliases:
                line = new[:m.start()].count("\n") + 1
                unknown_hits.append(f"{rel}:{line}: unknown alias {{{m.group(2)}}}")

    if touched:
        verb = "Expanded" if args.write else "Needs expanding"
        print(f"{verb}: {expanded_total} alias link target(s)")
        # file:line for each one, so a report someone reads in Slack points at the line.
        for h in known_hits:
            print(f"  {h}")
        if not args.write:
            print("\nRe-run with --write to expand, then review the diff before committing.")
    else:
        print("expand-aliases: no known aliases in link targets.")

    if unknown_hits:
        # stdout is block-buffered when piped, as the nightly digest pipes it; without this
        # the error lands ABOVE the summary it belongs under.
        sys.stdout.flush()
        print("\nERROR: alias left unexpanded — not a name the workflow knows:",
              file=sys.stderr)
        for h in unknown_hits:
            print(f"  {h}", file=sys.stderr)
        print("\nFix the typo, or add the space to " + WORKFLOW + " (and CI will agree).",
              file=sys.stderr)
        return 1

    return 1 if (touched and not args.write) else 0


if __name__ == "__main__":
    sys.exit(main())
