#!/usr/bin/env bash
#
# doc-lint.sh — the SINGLE SOURCE OF TRUTH for the codespell + lychee invocations that mirror
# CI (.github/workflows/codespell.yml and link-check-pr.yml).
#
# The pre-commit hook, the /precommit command, the docs-check skill, and dev-docs/cookbook-pre-pr.md
# all delegate here instead of re-spelling the flags, so the CI-mirroring options live in exactly
# one place. If CI changes its codespell flags or lychee excludes, update THIS file only.
#
# Usage:   .claude/hooks/doc-lint.sh <file> [<file> ...]
#          (paths are filtered to existing *.md / *.html; run from the repo root so that
#           .codespellignore resolves)
# Exit:    0 = all runnable checks passed (a check whose tool is missing is SKIPPED, not failed)
#          1 = a real failure (misspelling or broken link)
# Output:  failures and "tool missing / SKIPPED" notices go to stderr.
#
# Portability: no `mapfile` here — takes files as args — so it runs under bash 3.2 (macOS) too.

set -uo pipefail

# Keep only existing Markdown/HTML paths.
files=()
for f in "$@"; do
  case "$f" in
    *.md|*.html) [ -f "$f" ] && files+=("$f") ;;
  esac
done
[ "${#files[@]}" -eq 0 ] && exit 0

# Must run from the repo root so `.codespellignore` and the repo-relative file paths resolve.
# Guard explicitly so a wrong-CWD invocation reports a config error (exit 2), not a bogus
# "misspellings found" failure.
if [ ! -f .codespellignore ]; then
  echo "doc-lint: must be run from the repo root (.codespellignore not found in $PWD)." >&2
  exit 2
fi

rc=0

# --- codespell — mirrors codespell.yml (--check-filenames, ignore_words_file -> -I) ---------
# Every SUMMARY.md (in any space/folder, at any depth) is excluded from codespell — mirrors
# codespell.yml's files_ignore. GitBook truncates SUMMARY.md link labels to 100 chars, often
# mid-word, producing false positives; real misspellings still surface in the page titles
# codespell checks. SUMMARY.md files are still link-checked by lychee below.
spell_files=()
for f in "${files[@]}"; do
  case "$(basename "$f")" in
    SUMMARY.md) ;;
    *) spell_files+=("$f") ;;
  esac
done
if command -v codespell >/dev/null 2>&1; then
  if [ "${#spell_files[@]}" -gt 0 ] && ! out="$(codespell --check-filenames -I .codespellignore "${spell_files[@]}" 2>&1)"; then
    echo "codespell found possible misspellings:" >&2
    printf '%s\n' "$out" >&2
    rc=1
  fi
else
  echo "doc-lint: codespell not installed — SKIPPED (CI will run it). Install: pipx install codespell" >&2
fi

# --- lychee — mirrors link-check-pr.yml excludes EXACTLY -----------------------------------
# (--max-concurrency only bounds load; it does not change which links pass/fail, so CI fidelity
#  is preserved. Keep the --exclude set character-for-character identical to the workflow.)
if command -v lychee >/dev/null 2>&1; then
  if ! out="$(lychee --no-progress --max-concurrency 8 \
      --exclude 'dev\.mysql\.com' \
      --exclude 'docs\.oracle\.com' \
      --exclude 'kubernetes\.io\/docs' \
      --exclude '.*\{.*' \
      --exclude '.*%7B.*' \
      --exclude 'localhost' \
      --exclude '127\.0\.0\.1' \
      --exclude 'http://localhost:[0-9]+.*' \
      --exclude 'https://localhost:[0-9]+.*' \
      --exclude 'access\.redhat\.com' \
      --exclude 'docs\.redhat\.com' \
      --exclude 'blogs\.oracle\.com' \
      --exclude 'bugs\.mysql\.com' \
      --exclude 'forums\.mysql\.com' \
      --exclude 'www\.mysql\.com' \
      --exclude 'en\.opensuse\.org' \
      --exclude 'www\.cyberciti\.biz' \
      --exclude 'linux\.die\.net' \
      --exclude 'mariadb\.org\/feedback_plugin' \
      --exclude 'r\.mariadb\.com' \
      --exclude 'security-certs\.docs\.ubuntu\.com' \
      --exclude 'www\.linux-pam\.org' \
      --exclude 'www\.bzip\.org' \
      --exclude 'selinuxproject\.org' \
      --exclude 'www\.gnu\.org' \
      --exclude 'manpages\.ubuntu\.com' \
      --exclude 'packages\.ubuntu\.com' \
      --exclude 'www\.canonware\.com' \
      --exclude 'www\.npmjs\.com' \
      --exclude 'npmjs\.org' \
      "${files[@]}" 2>&1)"; then
    # Mirror the workflow's failIfEmpty: false — lychee exits non-zero with
    # "No links were found" when the changed files contain no links, which is a
    # false failure for link-free pages (e.g. nav stubs). See DOCS-6272.
    if printf '%s' "$out" | grep -q "No links were found"; then
      : # no links to check — not a failure
    else
      echo "lychee found broken links:" >&2
      printf '%s\n' "$out" >&2
      rc=1
    fi
  fi
else
  echo "doc-lint: lychee not installed — SKIPPED (CI will run it). Install: https://github.com/lycheeverse/lychee" >&2
fi

exit "$rc"
