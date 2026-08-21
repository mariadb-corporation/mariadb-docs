#!/usr/bin/env bash
#
# doc-lint.sh — the SINGLE SOURCE OF TRUTH for the codespell + lychee invocations that mirror
# CI (.github/workflows/codespell.yml and link-check-pr.yml), plus three checks that have no CI
# counterpart (see below): a GitBook include resolver, a heading-anchor gate, and a net
# line-loss guard.
#
# The pre-commit hook, the /precommit command, the docs-check skill, and dev-docs/cookbook-pre-pr.md
# all delegate here instead of re-spelling the flags, so the CI-mirroring options live in exactly
# one place. If CI changes its codespell flags or lychee excludes, update THIS file only.
#
# Usage:   .claude/hooks/doc-lint.sh <file> [<file> ...]
#          (paths are filtered to existing *.md / *.html; run from the repo root so that
#           .codespellignore resolves)
# Exit:    0 = all runnable checks passed (a check whose tool is missing is SKIPPED, not failed)
#          1 = a real failure (misspelling, broken link, unresolvable include, or a heading
#              anchor this change killed)
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

# Revision the working tree is compared against, shared by the two history-aware checks
# below (the heading-anchor gate and the line-loss guard).
LINT_BASE="${DOC_LINT_BASE:-HEAD}"

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
      --exclude 'github\.com/codership/(galera|mysql-wsrep)/issues/' \
      --exclude 'github\.com/MariaDB/mariadb-docker/' \
      --exclude 'github\.com/MariaDB/mariadb_kernel/' \
      --exclude 'github\.com/mysql/mysql-utilities/' \
      --exclude 'github\.com/Perl/perl5/issues/' \
      --exclude 'www\.fsf\.org' \
      --exclude 'dba\.stackexchange\.com' \
      --exclude 'askubuntu\.com' \
      --exclude 'valentina-db\.com' \
      --exclude 'docs\.moodle\.org' \
      --exclude 'www\.sqlmaestro\.com' \
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
# Use a positional template, not `-t <prefix>`: GNU coreutils rejects a `-t` template with no
# X's ("too few X's in template"), which made this exit 2 on every Linux run — and since it sits
# before the checks below, it took the include resolver and the shrink guard down with it. The
# positional form works on both GNU and BSD/macOS mktemp. (Regression from DOCS-6372, f2b5e332c.)
inc_fail="$(mktemp "${TMPDIR:-/tmp}/doclint-inc.XXXXXX")" || { echo "doc-lint: mktemp failed" >&2; exit 2; }
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

# --- GitBook heading anchors — NO CI counterpart --------------------------------------------
# A link to `page.md#some-heading` can rot in two ways that every other gate here is blind
# to: the heading is renamed, or the anchor was hand-written in the wrong dialect. CI passes
# no `--include-fragments`, and enabling it would not help — lychee's slugger is
# GitHub-flavoured, so on this repo it is wrong in BOTH directions: 386 of its 1,129 fragment
# errors are false positives (the anchor resolves live), and it misses 213 anchors that really
# are dead. `.claude/hooks/fragcheck.py` implements GitBook's rules instead, validated at
# 4,599/4,599 anchors against the rendered pages (DOCS-6491).
#
# It also gates a third rot that no link checker can see at all — including fragcheck itself
# when it is only looking for dead anchors. A heading line duplicated for a new section keeps
# the original's `<a href="#x" id="x">`, GitBook honours the explicit id over the text slug, and
# the two sections then share one anchor: the second dedupes to `-1` and neither owns the anchor
# a reader expects. Every link still resolves, just to the wrong section, so this is a semantic
# mismatch rather than a broken link (DOCS-6492). A heading whose explicit id is a deliberate
# historical KB alias for its own text is NOT flagged — only an id that belongs to a different
# heading on the same page. That distinction is the whole check: 48 headings differ from their
# text slug, but only 8 were defects, so flagging the wide class would be a 6x overstatement.
#
# Two deliberate design choices:
#   1. It reports only anchors that are dead NOW but resolved at $LINT_BASE. The repo carries
#      ~1,272 pre-existing dead anchors, so a plain check would turn every unrelated PR red on
#      breakage it did not introduce (the `broken-reference` trap — see the lychee section). The
#      stolen-id class is diffed against $LINT_BASE for the same reason: it stands at 0 today,
#      but this repo is also edited from the GitBook UI, so an absolute check would fail
#      unrelated PRs the moment a GITBOOK-* commit introduced one case.
#   2. It scans the whole tree, not just "${files[@]}". Renaming a heading breaks inbound links
#      from pages the commit never touched, and a changed-files check cannot see those. The two
#      passes cost ~14s; set DOC_LINT_SKIP_FRAGMENTS=1 to skip when iterating.
#
# Needs python3 (no third-party modules) and a git work tree; missing either is a SKIP, and a
# base revision that cannot be checked out is a SKIP too — never a silent pass into failure.
if [ "${DOC_LINT_SKIP_FRAGMENTS:-}" = "1" ]; then
  : # explicitly skipped by the caller
elif [ ! -f .claude/hooks/fragcheck.py ]; then
  echo "doc-lint: .claude/hooks/fragcheck.py not found — anchor check SKIPPED" >&2
elif ! command -v python3 >/dev/null 2>&1; then
  echo "doc-lint: python3 not installed — anchor check SKIPPED (no CI counterpart, so nothing" >&2
  echo "          else will catch a dead heading anchor). Install: brew install python3" >&2
elif ! command -v git >/dev/null 2>&1 || ! git rev-parse --is-inside-work-tree >/dev/null 2>&1; then
  echo "doc-lint: not a git work tree — anchor check SKIPPED (needs a base revision)" >&2
elif ! git rev-parse --verify -q "$LINT_BASE" >/dev/null 2>&1; then
  echo "doc-lint: base revision '$LINT_BASE' not found — anchor check SKIPPED" >&2
else
  python3 .claude/hooks/fragcheck.py new "$LINT_BASE" >/dev/null || rc=1
fi

# --- net line-loss guard — NO CI counterpart ------------------------------------------------
# Catches the "silently gutted page" failure: a surviving page loses most of its body while the
# markup stays valid and every remaining link resolves, so codespell and lychee both PASS.
#
# DOCS-6442 is the case this exists for. A retirement campaign (DOCS-5976 Tier B, c6ea5549a)
# meant to delete ONE {% columns %} content-ref block from the Storage Engines landing page —
# the block pointing at a folder it was removing — and promote FEDERATED into its place. It
# deleted 23 of the 24 blocks instead: 298 lines -> 22, 24 content-refs -> 1. SUMMARY.md was
# untouched, so the nav still listed all 27 engines while the page listed one. Every gate passed;
# a reader found it two days later, and b36d939 rebuilt the page from SUMMARY.md.
#
# The metric is NET loss (pre - post, i.e. deletions minus additions), not raw deletions.
# Raw deletions flag every reformatting campaign — alias expansion, trailing-backslash removal,
# changelog normalization — because those rewrite lines rather than remove them. Measured over
# 300 commits of this repo: raw deletions >40% flags 17 files (mostly those campaigns), net loss
# >40% flags 4. On c6ea5549a itself the guard yields a ONE-item list at 94%, next-worst 16%.
#
# Thresholds and the acknowledgment path are env-overridable:
#   DOC_LINT_SHRINK_PCT   (40) percent of the pre-image lost, net, before flagging
#   DOC_LINT_SHRINK_MIN   (20) minimum net lines lost, so tiny files can't trip it
#   DOC_LINT_SHRINK_FLOOR (30) minimum pre-image size considered at all
#   DOC_LINT_BASE       (HEAD) revision the pre-image is read from
#   DOC_LINT_ALLOW_SHRINK     space/comma-separated paths to exempt, or "all"
#
# A deliberate large shrink is legitimate (Tier C's Debian README correctly went 70 -> 34 lines
# when three of its five children were retired), so this gate is meant to be acknowledged, not
# worked around: name the path in DOC_LINT_ALLOW_SHRINK and say why in the commit message.
#
# Compares the WORKING-TREE file against the base revision — the same content codespell and
# lychee above are checking. When the index and working tree differ, this reflects the working
# tree, not what is staged.

SHRINK_PCT="${DOC_LINT_SHRINK_PCT:-40}"
SHRINK_MIN="${DOC_LINT_SHRINK_MIN:-20}"
SHRINK_FLOOR="${DOC_LINT_SHRINK_FLOOR:-30}"
SHRINK_BASE="$LINT_BASE"
SHRINK_ALLOW=" ${DOC_LINT_ALLOW_SHRINK:-} "
SHRINK_ALLOW="${SHRINK_ALLOW//,/ }"

if command -v git >/dev/null 2>&1 \
   && git rev-parse --is-inside-work-tree >/dev/null 2>&1 \
   && git rev-parse --verify -q "$SHRINK_BASE" >/dev/null 2>&1; then
  case "$SHRINK_ALLOW" in
    *" all "*) : ;;   # globally acknowledged — skip the whole check
    *)
      for f in "${files[@]}"; do
        f="${f#./}"
        case "$SHRINK_ALLOW" in *" $f "*) continue ;; esac
        # absent from the base revision = a new file, so there is nothing to have lost
        git cat-file -e "$SHRINK_BASE:$f" 2>/dev/null || continue

        pre=$(git show "$SHRINK_BASE:$f" 2>/dev/null | wc -l | tr -d ' ')
        post=$(wc -l < "$f" | tr -d ' ')
        [ "$pre" -lt "$SHRINK_FLOOR" ] && continue

        net=$((pre - post))
        [ "$net" -lt "$SHRINK_MIN" ] && continue

        if [ "$(awk -v n="$net" -v p="$pre" -v t="$SHRINK_PCT" \
                    'BEGIN{print (n/p*100 > t) ? 1 : 0}')" = "1" ]; then
          pctv="$(awk -v n="$net" -v p="$pre" 'BEGIN{printf "%.0f", n/p*100}')"
          echo "doc-lint: possible gutted page — $f" >&2
          echo "          lost $net of $pre lines net (${pctv}%) vs $SHRINK_BASE." >&2
          echo "          Confirm the page still covers everything it should. For a landing page," >&2
          echo "          compare its content-ref count against the space's SUMMARY.md children —" >&2
          echo "          SUMMARY.md is authoritative for nav, so a page listing far fewer of its" >&2
          echo "          children than SUMMARY.md does is the signature of this bug (DOCS-6442)." >&2
          echo "          Intentional? Re-run with DOC_LINT_ALLOW_SHRINK='$f'" >&2
          echo "          and say why in the commit message." >&2
          rc=1
        fi
      done
      ;;
  esac
fi

exit "$rc"
