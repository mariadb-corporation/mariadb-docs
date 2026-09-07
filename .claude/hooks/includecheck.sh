#!/usr/bin/env bash
#
# includecheck.sh — resolve every relative GitBook `{% include %}` and fail on a dead or
# cross-space target. Extracted from .claude/hooks/doc-lint.sh (DOCS-6586) so that CI can run
# THIS check without running the ones next to it; doc-lint.sh now delegates here, so the
# resolver still lives in exactly one place.
#
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
# Needs no external tool — no python3, no network, no git — so unlike codespell, lychee,
# fragcheck and navcheck it can never be SKIPPED, in CI or locally. That is why it is the half
# of DOCS-6586 that could ship on its own: it also has no legitimate exceptions (a dead include
# is always a bug), so it needs no acknowledgment path, which is the open design question
# holding up the orphan and shrink guards.
#
# `.claude/` and `dev-docs/` are exempt: they document the syntax with deliberate placeholders
# (`<snippet>.md`, `rc12345`) that are not meant to resolve.
#
# Usage:   .claude/hooks/includecheck.sh <file> [<file> ...]
#          .claude/hooks/includecheck.sh --stdin0     # NUL-delimited paths on stdin
#          Paths are repo-root-relative and the check must be run FROM the repo root — the
#          space-boundary test reads the first path component as the space name.
#
#          Use --stdin0 for a whole-tree run: `git ls-files -z -- '*.md' '*.html'` is ~9,700
#          paths, which is over ARG_MAX once xargs gets it, and xargs then splits the run into
#          several invocations. That is not just cosmetic — each invocation prints its own
#          summary line and returns its own status, so the counts stop being the tree's counts
#          and a caller reading `$?` off a pipeline sees only the LAST batch. One invocation,
#          one verdict.
# Exit:    0 = every relative include resolves inside its own space
#          1 = at least one dead or cross-space include
#          2 = usage error (no arguments)
# Output:  findings on stderr; a single "all resolve" line on stdout, so a caller can tell
#          "nothing to check" apart from "checked and clean". Mirrors navcheck.py.
#
# Portability: no `mapfile` — takes files as args — so it runs under bash 3.2 (macOS) too.

set -uo pipefail

if [ "$#" -eq 0 ]; then
  echo "usage: $0 <file> [<file> ...]" >&2
  exit 2
fi

# Collect the candidate paths, from stdin or from the argument list. No `mapfile` in the stdin
# branch — bash 3.2 does not have it.
raw=()
if [ "$1" = '--stdin0' ]; then
  if [ "$#" -ne 1 ]; then
    echo "usage: $0 --stdin0   (reads NUL-delimited paths on stdin; takes no other arguments)" >&2
    exit 2
  fi
  while IFS= read -r -d '' p; do
    raw+=("$p")
  done
else
  raw=("$@")
fi

# Keep only existing Markdown/HTML paths. A path that was deleted by the commit under test is
# dropped here rather than reported: its includes went with it.
files=()
if [ "${#raw[@]}" -gt 0 ]; then
  for f in "${raw[@]}"; do
    case "$f" in
      *.md|*.html) [ -f "$f" ] && files+=("$f") ;;
    esac
  done
fi
if [ "${#files[@]}" -eq 0 ]; then
  echo "includecheck: no Markdown or HTML files to check."
  exit 0
fi

# Normalize a path's `.` and `..` segments textually — the target need not exist, which rules
# out `realpath` (BSD realpath has no portable `-m`). A `..` that climbs above the repo root is
# left in place, so the path simply fails the existence test below.
#
# Every array expansion below is guarded by a length test on purpose. Expanding "${arr[@]}" or
# "${arr[*]}" on an EMPTY array is an "unbound variable" error under `set -u` before bash 4.4 —
# i.e. on the bash 3.2 that stock macOS still ships, which is the portability floor this script
# claims in its header. Unguarded, norm_path returned the EMPTY STRING for any include that
# climbs out of its own directory ("server/../maxscale/x.md"): the `..` emptied the array, the
# recompaction died, and every such include was then misreported as *unresolvable* while the
# cross-space branch below became unreachable. The mirror image of DOCS-6409, which only bit on
# Linux — same class, opposite platform. Found by doc-lint-test.sh (DOCS-6471).
norm_path() {
  local seg out=() n
  local IFS='/'
  for seg in $1; do
    case "$seg" in
      ''|.) ;;
      ..) n=${#out[@]}
          if [ "$n" -gt 0 ] && [ "${out[$((n-1))]}" != ".." ]; then
            unset "out[$((n-1))]"                      # bash 3.2 leaves a hole
            if [ "${#out[@]}" -gt 0 ]; then
              out=("${out[@]}")                        # compact it, but only if anything is left
            fi
          else
            out+=("..")
          fi ;;
      *) out+=("$seg") ;;
    esac
  done
  if [ "${#out[@]}" -eq 0 ]; then
    return 0                                           # nothing left: the empty path
  fi
  printf '%s' "${out[*]}"
}

# Space = first path component (`server/...` -> `server`); a file at the repo root has none.
space_of() {
  case "$1" in
    */*) printf '%s' "${1%%/*}" ;;
    *)   printf '%s' '<root>' ;;
  esac
}

# Read the grep output through a process substitution rather than a pipe, so the loop body runs
# in THIS shell and can tally straight into a variable. The pipe form could not — it put the
# body in a subshell — and needed a `mktemp` scratch file to carry the count back out, which is
# where DOCS-6372's f2b5e332c regression lived: a `-t` template with no X's is rejected by GNU
# coreutils but accepted by BSD, so every Linux run exited 2 before reaching this check at all.
# No temp file, no platform-specific mktemp contract.
findings=0
checked=0

for f in "${files[@]}"; do
  f="${f#./}"
  case "$f" in .claude/*|dev-docs/*) continue ;; esac
  while IFS= read -r hit; do
    [ -n "$hit" ] || continue
    lineno="${hit%%:*}"
    target="${hit#*\"}"; target="${target%\"}"   # strip both quotes, not just the opening one
    case "$target" in http*) continue ;; esac
    checked=$((checked + 1))
    dir="${f%/*}"; [ "$dir" = "$f" ] && dir='.'
    resolved="$(norm_path "$dir/$target")"
    if [ ! -f "$resolved" ]; then
      echo "doc-lint: unresolvable include at $f:$lineno -> $target (no such file: $resolved)" >&2
      findings=$((findings + 1))
    elif [ "$(space_of "$resolved")" != "$(space_of "$f")" ]; then
      echo "doc-lint: cross-space include at $f:$lineno -> $target" >&2
      echo "          resolves into space '$(space_of "$resolved")' but the page is in '$(space_of "$f")';" >&2
      echo "          use the by-ID form instead: {% include \"https://app.gitbook.com/s/<space>/~/reusable/<id>/\" %}" >&2
      findings=$((findings + 1))
    fi
  done < <(grep -n -o '{%[[:space:]]*include[[:space:]]*"[^"]*"' "$f" 2>/dev/null)
done

if [ "$findings" -gt 0 ]; then
  exit 1
fi

# On stdout, and it names the counts. A gate needs to be able to prove it did something: an
# invocation whose file list turned out to hold no includes at all is indistinguishable from a
# clean one by exit code alone.
echo "includecheck: ${checked} relative include(s) across ${#files[@]} file(s), all resolve."
