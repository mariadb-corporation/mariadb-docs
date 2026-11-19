#!/usr/bin/env bash
#
# gitbook-edit-digest.sh — list the GitBook-UI commits in a revision range and run the content
# gates on each one. Called by .github/workflows/nightly-gitbook-edits.yml (DOCS-6914).
#
# WHY THIS EXISTS
#   An edit merged in the GitBook app reaches `main` as a `GITBOOK-<n>: <title>` commit whose
#   committer is gitbook-bot and whose author is the editor. It never goes through a pull
#   request, so none of the PR gates run on it and nobody reviews it. Blocking those merges is
#   not practical, so the docs team reviews them after the fact instead: this script produces
#   the list, and the workflow posts it to #docs-notifications. It lists EVERY GitBook commit,
#   not only the failing ones, because the point is that a human looks at each diff.
#
# WHY EACH COMMIT IS GATED ON ITS OWN
#   Gating the window as one diff would blame a failure on whichever commit happened to touch
#   the file last, and would miss a defect that a later commit in the same window repaired. So
#   each commit is checked out into a throwaway worktree and gated against its own parent, the
#   same way run-doc-gates.sh gates a bot branch against its base.
#
# WHY THE TOOLING IS COPIED IN FROM THIS CHECKOUT
#   The commits being checked can be weeks old on a dispatched run, and they carry whatever
#   version of the gates existed then -- for anything before DOCS-6675, no run-doc-gates.sh at
#   all. The gates must come from the ref that defines this digest, never from the content
#   being gated (the rule doc-gates.yml learned the hard way). So .claude/hooks and
#   run-doc-gates.sh are copied from the checkout this script runs in into every worktree.
#
# Usage:  gitbook-edit-digest.sh <base-rev> <head-rev> <out-dir>
#           Gates every commit in <base-rev>..<head-rev> whose committer is gitbook-bot.
# Output: <out-dir>/commits.jsonl   one JSON object per commit, oldest first
#         <out-dir>/logs/<sha>.log  the full gate output for that commit
#         <out-dir>/complete        written only once every commit has its entry
# Exit:   0 = the digest ran (gate FINDINGS are data in commits.jsonl, not a failure)
#         2 = the digest could not run, or a gate could not run on at least one commit
#
# Env:    DIGEST_MAX_PAGES   commits changing more Markdown/HTML files than this are listed but
#                            not gated (default 150). A GitBook "Export content" commit can
#                            rewrite a whole space -- 655 files on 2026-09-15 -- and lychee
#                            would spend the job's timeout on external links.

set -uo pipefail

die() { echo "::error::$*" >&2; exit 2; }

[ "$#" -eq 3 ] || { echo "usage: $0 <base-rev> <head-rev> <out-dir>" >&2; exit 2; }
base="$1"; head="$2"; out="$3"
max_pages="${DIGEST_MAX_PAGES:-150}"

[ -f .codespellignore ] || die "run from the repo root (.codespellignore not found in $PWD)."
[ -f .github/scripts/run-doc-gates.sh ] || die ".github/scripts/run-doc-gates.sh not found — broken checkout."
[ -d .claude/hooks ] || die ".claude/hooks not found — broken checkout."
command -v jq >/dev/null 2>&1 || die "jq is required."

for rev in "$base" "$head"; do
  git rev-parse --verify -q "$rev^{commit}" >/dev/null 2>&1 \
    || die "revision '$rev' is not in this clone. Check that fetch-depth: 0 is set on the checkout step."
done

tooling="$PWD"
mkdir -p "$out/logs"
: > "$out/commits.jsonl"
wt_root="$(mktemp -d)"
# Invoked by the EXIT trap below, which shellcheck cannot see.
# shellcheck disable=SC2329
cleanup() {
  for wt in "$wt_root"/*; do
    [ -d "$wt" ] && git -C "$tooling" worktree remove --force "$wt" >/dev/null 2>&1
  done
  rm -rf "$wt_root"
  git -C "$tooling" worktree prune >/dev/null 2>&1
}
trap cleanup EXIT

# Matched on the committer EMAIL, which GitBook sets on every sync; the author is the editor and
# says nothing about where the commit came from. --reverse lists the window oldest first, the
# order a reviewer reads it in.
commits=()
while IFS= read -r c; do commits+=("$c"); done \
  < <(git rev-list --reverse --committer='<ghost@gitbook\.com>' "$base..$head")

echo "gitbook-edit-digest: ${#commits[@]} GitBook commit(s) in ${base:0:12}..${head:0:12}"

tool_errors=0
for c in "${commits[@]}"; do
  short="$(git rev-parse --short "$c")"
  # A root commit has no parent to diff against; GitBook never produces one, but say so rather
  # than gating against nothing.
  if ! parent="$(git rev-parse -q --verify "$c^" 2>/dev/null)"; then
    die "$short has no parent, so it cannot be gated."
  fi

  # Every changed path, with its status, for the "changed pages" line. Deleted pages are listed
  # (a reviewer wants to know a page went away) but cannot be gated.
  changed="$(git diff-tree --no-commit-id -r -M --name-status "$c" | jq -R -s '
    split("\n") | map(select(length > 0) | split("\t")
      | {status: .[0][0:1], path: .[-1]})')"
  pages="$(jq '[.[] | select(.path | test("\\.(md|html)$"))]' <<<"$changed")"
  gateable="$(jq '[.[] | select(.status != "D")] | length' <<<"$pages")"

  log="$out/logs/$c.log"
  if [ "$gateable" -eq 0 ]; then
    verdict="no-pages"; rc=0
    echo "No Markdown or HTML was added or modified, so there was nothing to gate." > "$log"
  elif [ "$gateable" -gt "$max_pages" ]; then
    verdict="too-large"; rc=0
    echo "$gateable pages changed, more than DIGEST_MAX_PAGES=$max_pages, so this commit was not gated. Review it by hand." > "$log"
  else
    wt="$wt_root/$short"
    git -C "$tooling" worktree add -q --detach "$wt" "$c" || die "could not check out $short into a worktree."
    # Replace, not merge: a hook file that exists only in the old commit must not run either.
    rm -rf "$wt/.claude/hooks"
    mkdir -p "$wt/.claude" "$wt/.github/scripts"
    cp -R "$tooling/.claude/hooks" "$wt/.claude/hooks"
    cp "$tooling/.github/scripts/run-doc-gates.sh" "$wt/.github/scripts/run-doc-gates.sh"
    rm -rf "$wt/.claude/hooks/__pycache__"

    echo "gitbook-edit-digest: gating $short ($gateable page(s))"
    after="$wt_root/$short.after.log"
    ( cd "$wt" && DOC_GATES_LOG="$after" \
        bash .github/scripts/run-doc-gates.sh "$parent" . ) > "$log" 2>&1
    rc=$?
    case "$rc" in
      0) verdict="pass" ;;
      1) verdict="fail" ;;
      *) verdict="error"; tool_errors=$((tool_errors + 1))
         echo "::error::run-doc-gates.sh exited $rc on $short — the gates could not run on it." ;;
    esac

    # A failure is not yet a finding ABOUT THIS COMMIT. Two kinds of output are not:
    #   * the tree-wide checks (versioncheck, the register audits) read the whole tree, and
    #     today's registers run against a weeks-old tree report entries that did not exist yet;
    #   * codespell and lychee read the whole changed FILE, so a typo or dead link that was
    #     already on the page fails the commit that merely edited a line near it.
    # Measured on 9f0b0f243: nine findings, none of them introduced by the commit. So the same
    # gates run once more on the parent, over the same files, with the same tooling, and only
    # the lines the parent did not already produce are reported. The history-aware checks
    # (fragcheck, navcheck, shrinkcheck) are deltas already and report nothing against
    # themselves, so they pass through unchanged.
    if [ "$verdict" = "fail" ]; then
      before="$wt_root/$short.before.log"
      git -C "$wt" checkout -q -f --detach "$parent" || die "could not check out the parent of $short."
      rm -rf "$wt/.claude/hooks"
      mkdir -p "$wt/.claude"
      cp -R "$tooling/.claude/hooks" "$wt/.claude/hooks"
      rm -rf "$wt/.claude/hooks/__pycache__"
      parent_files=()
      while IFS= read -r p; do
        [ -f "$wt/$p" ] && parent_files+=("$p")
      done < <(jq -r '.[] | select(.status != "D") | .path' <<<"$pages")
      : > "$before"
      if [ "${#parent_files[@]}" -gt 0 ]; then
        ( cd "$wt" && DOC_LINT_BASE="$parent" bash .claude/hooks/doc-lint.sh "${parent_files[@]}" ) \
          > "$before" 2>&1
      fi
      # Same backstop as run-doc-gates.sh: a gate that skipped on the parent would make every
      # one of its findings look new.
      if grep -q 'SKIPPED' "$before"; then
        verdict="error"; tool_errors=$((tool_errors + 1))
        echo "::error::a gate reported SKIPPED on the parent of $short, so its findings cannot be told apart from pre-existing ones."
      fi
      {
        echo
        echo "----- the same gates on the parent ${parent:0:12} (findings here are not new) -----"
        cat "$before"
      } >> "$log"
    fi
    git -C "$tooling" worktree remove --force "$wt" >/dev/null 2>&1
  fi

  findings=''
  if [ "$verdict" = "fail" ]; then
    findings="$(python3 "$tooling/.github/scripts/new-findings.py" "$before" "$after")"
    # Every line the commit failed on was already failing on the parent.
    [ -n "$findings" ] || verdict="pass-preexisting"
  fi

  jq -n -c \
    --arg sha "$c" --arg short "$short" \
    --arg author "$(git log -1 --format=%an "$c")" \
    --arg email "$(git log -1 --format=%ae "$c")" \
    --arg date "$(git log -1 --format=%cI "$c")" \
    --arg subject "$(git log -1 --format=%s "$c")" \
    --arg verdict "$verdict" --argjson rc "$rc" \
    --arg findings "$findings" \
    --argjson pages "$pages" \
    --argjson others "$(jq 'map(select(.path | test("\\.(md|html)$") | not)) | length' <<<"$changed")" '
    # GitBook CR numbers are per SPACE (GITBOOK-1640 and GITBOOK-2399 are different spaces), so
    # the number alone does not identify a change request; the space comes from the top-level
    # directory of the pages it touched. Commits titled "GitBook: Update content" have none.
    ($subject | capture("^GITBOOK-(?<n>[0-9]+): ?(?<t>.*)$") // {n: null, t: $subject}) as $m
    | {sha: $sha, short: $short, author: $author, email: $email, date: $date,
       subject: $subject, cr: $m.n, title: $m.t, verdict: $verdict, rc: $rc, findings: $findings,
       spaces: ([$pages[].path | split("/")[0]] | unique),
       pages: $pages, other_files: $others}' >> "$out/commits.jsonl"
done

# Every commit has its entry. The workflow posts only when this marker exists, so a run that
# died halfway can never post a partial list that reads as the whole night.
: > "$out/complete"
[ "$tool_errors" -eq 0 ] || die "the gates could not run on $tool_errors commit(s); see the logs above."
exit 0
