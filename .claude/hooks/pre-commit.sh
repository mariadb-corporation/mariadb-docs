#!/usr/bin/env bash
#
# Pre-commit doc check for mariadb-docs.
#
# Wired as a Claude Code PreToolUse(Bash) hook in .claude/settings.json. It only acts when the
# Bash command being run is a `git commit`; for anything else it exits 0 immediately.
#
# SCOPE (important): this only gates commits that *Claude Code* makes via the Bash tool. Human
# `git commit`, IDE commits, and GitBook-UI edits bypass it entirely. CI is the authoritative
# gate. See .claude/README.md for the trust model and the hook-vs-CI scope caveat.
#
# The actual checks (codespell + lychee, mirroring CI) live in ONE place: doc-lint.sh. This
# script only handles commit detection, collecting staged files, and translating a failure into
# an exit-2 block:
#   - real spelling or link failure   -> exit 2 (blocks the commit, feedback shown to Claude)
#   - a checker not installed locally -> warn only, exit 0 (CI is the hard gate)
#   - nothing staged / not a commit   -> exit 0

set -uo pipefail

SCRIPT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"

# Matches `git ... commit` only at a command boundary (start, ;, &&, ||, |, "("), so it does
# not misfire on the literal text "git commit" appearing inside an echo/string/heredoc.
is_git_commit() {
  printf '%s' "$1" \
    | grep -qE '(^|[;&|(]|&&|\|\|)[[:space:]]*git([[:space:]]+[^;&|]*)?[[:space:]]commit([[:space:]]|$)'
}

# --- read hook payload (JSON on stdin) and decide whether this is a git commit --------------
payload="$(cat || true)"

if command -v jq >/dev/null 2>&1; then
  cmd="$(printf '%s' "$payload" | jq -r '.tool_input.command // ""' 2>/dev/null || true)"
  is_git_commit "$cmd" || exit 0
else
  # No jq: can't parse the JSON precisely. Fall back to a substring scan of the raw payload
  # and warn loudly, rather than silently disabling the check on machines without jq.
  case "$payload" in
    *"git commit"*) ;;
    *) exit 0 ;;
  esac
  echo "pre-commit hook: jq not installed - commit detection is imprecise; install jq for accuracy." >&2
fi

cd "${CLAUDE_PROJECT_DIR:-.}" || exit 0

# --- collect staged Markdown / HTML files (portable: no mapfile, bash 3.2-safe) ------------
files=()
while IFS= read -r f; do
  [ -n "$f" ] && files+=("$f")
done < <(git diff --cached --name-only --diff-filter=ACM -- '*.md' '*.html' 2>/dev/null)
[ "${#files[@]}" -eq 0 ] && exit 0

# --- delegate to the canonical linter ------------------------------------------------------
if ! out="$("$SCRIPT_DIR/doc-lint.sh" "${files[@]}" 2>&1)"; then
  {
    echo "Pre-commit doc check failed on staged files. Fix these before committing"
    echo "(see dev-docs/cookbook-pre-pr.md), or commit from a shell to bypass:"
    echo
    printf '%s\n' "$out"
  } >&2
  exit 2
fi

# Passed — but doc-lint may have emitted "tool missing / SKIPPED" notices; surface them
# without blocking.
[ -n "$out" ] && printf '%s\n' "$out" >&2
exit 0
