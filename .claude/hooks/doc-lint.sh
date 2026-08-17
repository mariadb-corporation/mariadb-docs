#!/usr/bin/env bash
#
# doc-lint.sh — the SINGLE SOURCE OF TRUTH for the codespell + lychee invocations that mirror
# CI (.github/workflows/codespell.yml and link-check-pr.yml), plus a GitBook include resolver
# that has no CI counterpart (see below).
#
# The pre-commit hook, the /precommit command, the docs-check skill, and dev-docs/cookbook-pre-pr.md
# all delegate here instead of re-spelling the flags, so the CI-mirroring options live in exactly
# one place. If CI changes its codespell flags or lychee excludes, update THIS file only.
#
# Usage:   .claude/hooks/doc-lint.sh <file> [<file> ...]
#          (paths are filtered to existing *.md / *.html; run from the repo root so that
#           .codespellignore resolves)
# Exit:    0 = all runnable checks passed (a check whose tool is missing is SKIPPED, not failed)
#          1 = a real failure (misspelling, broken link, or unresolvable include)
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
      --exclude 'bazaar\.launchpad\.net' \
      --exclude 'github\.com/mariadb-corporation/mariadb-connector-[a-z0-9]+/commit/' \
      --exclude 'github\.com/MariaDB/server/commit/' \
      --exclude 'downloads\.askmonty\.org' \
      --exclude 'montyprogram\.com' \
      --exclude 'forge\.mysql\.com' \
      --exclude 'lists\.mysql\.com' \
      --exclude 'blogs\.msdn\.com' \
      --exclude 'lists\.askmonty\.org' \
      --exclude 'support2\.microsoft\.com' \
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
      --exclude 'mcs1' \
      --exclude 's\.petrunia\.net' \
      --exclude 'mysql\.taobao\.org' \
      --exclude 'www\.shannon-sys\.com' \
      --exclude 'www\.hashicorp\.com' \
      --exclude 'blogspot\.com' \
      --exclude 'www\.poliarch\.org' \
      --exclude 'www\.reddit\.com' \
      --exclude 'csm\.mariadb\.com' \
      --exclude 'stackoverflow\.com' \
      --exclude 'gitlab\.kitware\.com' \
      --exclude 'www\.freedesktop\.org' \
      --exclude 'azuremarketplace\.microsoft\.com' \
      --exclude 'console\.cloud\.google\.com' \
      --exclude 'partedmagic\.com' \
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

# --- GitBook include resolver — NO CI counterpart -------------------------------------------
# `{% include "../.gitbook/includes/foo.md" %}` is GitBook template syntax, not a Markdown link,
# so lychee cannot see it: a dead include renders as *nothing* and the page silently loses a
# section. DOCS-6372 found two live cases that way (a 13.1 post-download page missing its
# "most recent release" bullet, and a MaxScale CVE page missing its copyright footnote).
#
# Two failure modes are checked:
#   1. target does not exist;
#   2. target exists but lies in a different space. Each top-level directory is a separate
#      GitBook space with its own Git-sync root, so a relative include may not cross that
#      boundary even though the path resolves fine on disk. Cross-space reuse must instead use
#      the by-ID form, `{% include "https://app.gitbook.com/s/<space>/~/reusable/<id>/" %}`.
#
# Needs no external tool, so unlike the two checks above it can never be silently SKIPPED.
# `.claude/` and `dev-docs/` are exempt: they document the syntax with deliberate placeholders
# (`<snippet>.md`, `rc12345`) that are not meant to resolve.

# Normalize a path's `.` and `..` segments textually — the target need not exist, which rules
# out `realpath` (BSD realpath has no portable `-m`). A `..` that climbs above the repo root is
# left in place, so the path simply fails the existence test below.
norm_path() {
  local seg out=() n
  local IFS='/'
  for seg in $1; do
    case "$seg" in
      ''|.) ;;
      ..) n=${#out[@]}
          if [ "$n" -gt 0 ] && [ "${out[$((n-1))]}" != ".." ]; then
            unset "out[$((n-1))]"; out=("${out[@]}")   # compact: bash 3.2 leaves a hole
          else
            out+=("..")
          fi ;;
      *) out+=("$seg") ;;
    esac
  done
  printf '%s' "${out[*]}"
}

# Space = first path component (`server/...` -> `server`); a file at the repo root has none.
space_of() {
  case "$1" in
    */*) printf '%s' "${1%%/*}" ;;
    *)   printf '%s' '<root>' ;;
  esac
}

# `grep | while` puts the loop body in a subshell, so it cannot set `rc` directly — failures are
# tallied in a temp file instead.
inc_fail="$(mktemp -t doclint-inc.XXXXXX)" || { echo "doc-lint: mktemp failed" >&2; exit 2; }
trap 'rm -f "$inc_fail"' EXIT

for f in "${files[@]}"; do
  f="${f#./}"
  case "$f" in .claude/*|dev-docs/*) continue ;; esac
  grep -n -o '{%[[:space:]]*include[[:space:]]*"[^"]*"' "$f" 2>/dev/null | while IFS= read -r hit; do
    lineno="${hit%%:*}"
    target="${hit#*\"}"; target="${target%\"}"   # strip both quotes, not just the opening one
    case "$target" in http*) continue ;; esac
    dir="${f%/*}"; [ "$dir" = "$f" ] && dir='.'
    resolved="$(norm_path "$dir/$target")"
    if [ ! -f "$resolved" ]; then
      echo "doc-lint: unresolvable include at $f:$lineno -> $target (no such file: $resolved)" >&2
      echo x >>"$inc_fail"
    elif [ "$(space_of "$resolved")" != "$(space_of "$f")" ]; then
      echo "doc-lint: cross-space include at $f:$lineno -> $target" >&2
      echo "          resolves into space '$(space_of "$resolved")' but the page is in '$(space_of "$f")';" >&2
      echo "          use the by-ID form instead: {% include \"https://app.gitbook.com/s/<space>/~/reusable/<id>/\" %}" >&2
      echo x >>"$inc_fail"
    fi
  done
done
[ -s "$inc_fail" ] && rc=1

exit "$rc"
