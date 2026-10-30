#!/usr/bin/env bash
#
# run-doc-gates.sh — run this repo's content gates against a bot-generated branch.
#
# WHY THIS EXISTS
#   A pull request opened by a GitHub Action using the default GITHUB_TOKEN triggers NO
#   `on: pull_request` workflows at all. GitHub suppresses them deliberately, to stop a
#   workflow recursively triggering itself. The consequence here is that every PR our
#   generating workflows open arrives with zero content gates having run: no codespell, no
#   link-check, no fragcheck, no includecheck. Only the GitBook space checks run, and those
#   check publishability, not content.
#
#   DOCS-6618 is what that costs. PR #1052 merged a freshly generated Plugin API tree; running
#   these same gates by hand on the merge commit afterwards found 344 dead in-page anchors and
#   14 pages with no frontmatter. The ticket was filed in place of a red check. DOCS-6675 is
#   the fix: the generating workflow runs the gates itself, before anyone reviews the PR, and
#   publishes the verdict as a commit status so it shows up in the PR's checks list.
#
# WHY IT CALLS doc-lint.sh AND NOTHING ELSE
#   .claude/hooks/doc-lint.sh is the repo's declared single source of truth for the codespell
#   and lychee invocations, and it already delegates to includecheck.sh, fragcheck.py and
#   navcheck.py plus its own shrink and retired-KB guards. So one call runs every gate with the
#   flags CI uses, and there is nothing here to drift out of sync with the PR workflows — which
#   is the whole constraint DOCS-6586 imposes ("one parser or none"). The PR workflows call
#   fragcheck.py and includecheck.sh directly instead, for the opposite reason: routing through
#   doc-lint.sh there would re-run codespell and lychee, which have their own workflows. Here
#   nothing else runs, so doc-lint.sh is exactly the right entry point.
#
# WHY IT SELF-TESTS FIRST
#   DOCS-6618's real lesson is not that a gate was missing, it is that a gate reporting success
#   on content it never examined is indistinguishable from a gate that works. doc-lint.sh
#   SKIPs any check whose tool is absent and still exits 0, so on a runner without codespell or
#   lychee this script would pass every bot PR while checking almost nothing.
#
#   So before gating real content it writes one deliberately broken page and asserts that
#   doc-lint.sh fails on it AND names every defect class. Every marker below was read off an
#   actual run, not guessed. The negative guard (no "SKIPPED" in the real run's output)
#   catches the same class from the other side.
#
#   Not covered by the canary: the net line-loss / gutted-page guard, which needs a pre-existing
#   file to shrink and so cannot be provoked by adding one new page. It is still run against the
#   real content below.
#
# Usage:  run-doc-gates.sh <base-ref> <pathspec> [<pathspec> ...]
#           base-ref   revision the branch is diffed against, e.g. origin/main
#           pathspec   git pathspecs limiting which changed files are gated; these should
#                      match the generating workflow's `add-paths`
# Exit:   0 = every gate passed
#         1 = a gate found a defect in the generated content
#         2 = this script or its environment is misconfigured (bad args, wrong CWD,
#             unresolvable base, no files to gate, or a gate that silently skipped)
#
# Env:    DOC_GATES_SKIP_SELFTEST=1   skip the canary (for iterating on this script only;
#                                     never set it in a workflow — it is the proof)
#         DOC_GATES_LOG               where to write the real run's output
#                                     (default: doc-gates.log in the CWD)

set -uo pipefail

CANARY='server/doc-gates-canary.md'
LOG="${DOC_GATES_LOG:-doc-gates.log}"

die() { echo "::error::$*" >&2; exit 2; }

if [ "$#" -lt 2 ]; then
  echo "usage: $0 <base-ref> <pathspec> [<pathspec> ...]" >&2
  exit 2
fi
base="$1"; shift

# doc-lint.sh resolves .codespellignore and every path relative to the repo root, and reports a
# wrong CWD as a config error rather than a finding. Fail here instead, with a clearer message.
[ -f .codespellignore ] || die "run-doc-gates.sh must run from the repo root (.codespellignore not found in $PWD)."
[ -x .claude/hooks/doc-lint.sh ] || [ -f .claude/hooks/doc-lint.sh ] \
  || die ".claude/hooks/doc-lint.sh not found — broken checkout, so no gate can run."

# A base revision that is not in the clone would make doc-lint.sh's history-aware checks SKIP
# and still exit 0. In CI a check that cannot run must not report success, so this is fatal.
git rev-parse --verify -q "$base^{commit}" >/dev/null 2>&1 \
  || die "base revision '$base' is not in this clone, so the history-aware gates would SKIP and report success. Check that fetch-depth: 0 is set on the checkout step."

# ---------------------------------------------------------------------------------------------
# Self-test: prove the gates are live on THIS runner before trusting them on real content.
# ---------------------------------------------------------------------------------------------
if [ "${DOC_GATES_SKIP_SELFTEST:-}" = "1" ]; then
  echo "run-doc-gates: canary SKIPPED by DOC_GATES_SKIP_SELFTEST — the gates below are unproven."
else
  [ -e "$CANARY" ] && die "$CANARY already exists; refusing to overwrite it. Pick another canary path."
  # Removed on every exit path, so a failed assertion cannot leave it behind for
  # create-pull-request to pick up. The callers' `add-paths` is a second backstop: the canary
  # sits outside every path they commit.
  trap 'rm -f "$CANARY"' EXIT

  # Six defects, one per gate. The misspelling must sit outside the paths codespell's
  # files_ignore covers (server/reference/plugins/api-plugin/**, agent-skills/topical/**, the
  # changelogs and every SUMMARY.md), which is why the canary lives at the top of server/.
  cat > "$CANARY" <<'CANARY_CONTENT'
---
description: Deliberately broken page written and deleted by run-doc-gates.sh.
---

# Doc Gates Canary

This sentence contains an occurence of a misspelling.

See [nowhere](#no-such-heading) and [gone](./no-such-file-at-all.md).

{% include "./no-such-include.md" %}

Retired: https://mariadb.com/kb/en/some-page/

## Real Heading
CANARY_CONTENT

  canary_log="$(mktemp)"
  DOC_LINT_BASE="$base" bash .claude/hooks/doc-lint.sh "$CANARY" >"$canary_log" 2>&1
  canary_rc=$?
  rm -f "$CANARY"
  trap - EXIT

  # Marker strings, each read off a real doc-lint.sh run. Left-hand side is the gate, so a
  # failure names which one went quiet.
  missing=''
  while IFS='|' read -r gate marker; do
    [ -n "$gate" ] || continue
    grep -qF -- "$marker" "$canary_log" || missing="$missing $gate"
  done <<'MARKERS'
codespell|codespell found possible misspellings:
lychee|lychee found broken links:
includecheck|doc-lint: unresolvable include at
fragcheck|now dead:
navcheck|not listed in SUMMARY.md:
retired-kb|doc-lint: retired mariadb.com/kb/ link in
MARKERS

  if [ "$canary_rc" -eq 0 ] || [ -n "$missing" ]; then
    echo "----- canary output -----"
    cat "$canary_log"
    echo "-------------------------"
    [ "$canary_rc" -eq 0 ] \
      && die "doc-lint.sh PASSED a page seeded with six separate defects. The gate is not working, so nothing below can be trusted."
    die "doc-lint.sh failed the canary but never mentioned:${missing}. Those gates are not running on this runner (a missing tool is a SKIP that still exits 0 — see DOCS-6618), or their output wording changed and these markers need updating with it."
  fi
  rm -f "$canary_log"
  echo "run-doc-gates: canary caught all six defect classes — the gates are live on this runner."
fi

# ---------------------------------------------------------------------------------------------
# The real run.
# ---------------------------------------------------------------------------------------------
# Deletions are excluded (ACMR): a removed file cannot be linted, and the gates that care about
# a disappearing page -- navcheck's de-listed direction and the shrink guard -- read the base
# side out of git themselves.
files=()
while IFS= read -r -d '' f; do
  case "$f" in *.md|*.html) files+=("$f") ;; esac
done < <(git diff -z --name-only --diff-filter=ACMR "$base"...HEAD -- "$@")

if [ "${#files[@]}" -eq 0 ]; then
  die "no Markdown or HTML changed between $base and HEAD under: $*. A branch with nothing to gate should not have reached this gate, so either the pathspecs no longer match what the generating workflow commits, or the diff is empty. Passing here would mean nothing."
fi

echo "run-doc-gates: gating ${#files[@]} changed file(s) against $base:"
printf '  %s\n' "${files[@]}"
echo

DOC_LINT_BASE="$base" bash .claude/hooks/doc-lint.sh "${files[@]}" >"$LOG" 2>&1
rc=$?
cat "$LOG"

# A SKIPPED check exits 0, so a green run whose log says "SKIPPED" is the DOCS-6618 failure
# wearing a pass. The canary above would normally have caught it; this is the backstop for a
# check that has no canary, or one that skips only on the real file set.
if grep -q 'SKIPPED' "$LOG"; then
  echo
  die "a gate reported SKIPPED, so part of the generated content was never examined. A skipped check still exits 0, which is exactly how DOCS-6618's 344 dead anchors reached main."
fi

if [ "$rc" -eq 0 ]; then
  echo "run-doc-gates: all gates passed."
else
  echo "::error::A content gate failed on the generated documentation. Details above."
fi
exit "$rc"
