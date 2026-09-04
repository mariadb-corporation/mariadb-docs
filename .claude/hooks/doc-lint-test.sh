#!/usr/bin/env bash
#
# doc-lint-test.sh — regression suite for doc-lint.sh.
#
# Usage:   .claude/hooks/doc-lint-test.sh [--keep] [--verbose]
#          --keep     leave the sandbox behind and print its path
#          --verbose  print the captured stdout/stderr of every case
# Exit:    0 = every case passed, 1 = at least one case failed,
#          2 = the suite could not set itself up (missing doc-lint.sh, no git, ...)
#
# WHY THIS EXISTS
#   Nothing used to run doc-lint.sh outside the Claude Code pre-commit hook, and that hook
#   "only gates commits that Claude Code makes via the Bash tool" (pre-commit.sh header) — so
#   human, IDE and GitBook-UI commits never invoked it. DOCS-6409 is what that costs: a mktemp
#   template with no X characters made the script exit 2 on every GNU-coreutils run from
#   f2b5e332c (2026-08-05) until 2026-08-18 — 135 commits — and because the failing line sat
#   BEFORE the checks, it silently took the include resolver down with it. On macOS/BSD mktemp
#   the same line worked fine, so the only machine that could have noticed was a Linux one, and
#   no Linux ever ran the script.
#
#   That is the failure class this suite is aimed at: the script's own plumbing, on a platform
#   the author is not using. It is wired into CI by .github/workflows/doc-lint-test.yml, which
#   runs it on ubuntu-latest on every PR — deliberately NOT only when the hooks change, because
#   DOCS-6409 was not caused by an edit to the script. It was caused by the script meeting
#   different coreutils.
#
# WHAT IT COVERS AND WHAT IT DOES NOT
#   It exercises the two checks in doc-lint.sh that have no CI counterpart — the GitBook
#   `{% include %}` resolver (DOCS-6372) and the net line-loss "gutted page" guard (DOCS-6470,
#   for the DOCS-6442 class) — plus the plumbing every check sits behind: the repo-root config
#   guard, the argument filter, the env-var knobs, and the tool-missing SKIP branches.
#
#   codespell and lychee are gated separately by codespell.yml and link-check-pr.yml, so their
#   flag sets are not what this suite guards. What it does guard is that doc-lint REACHES them:
#   the two cases marked "needs codespell" / "needs lychee" run only when the tool is on PATH,
#   and prove the present-branch fires at all. That is the assertion DOCS-6409 would have failed.
#
#   The heading-anchor check is not covered here. It has its own CI gate (fragcheck-pr.yml,
#   DOCS-6524) and fragcheck.py is absent from the sandbox, so what this suite asserts about it
#   is only that its absence is a SKIP rather than a crash.
#
# TWO RULES THAT COME STRAIGHT FROM HOW DOCS-6409 HID
#   1. NEVER PIPE THE SCRIPT UNDER TEST. Per DOCS-6409 impact note 4, `doc-lint.sh ... | tail`
#      returns the PIPE's status, so a hard exit-2 failure reads as a clean 0 — which is how the
#      regression stayed hidden. Every invocation here redirects to files and reads $? directly.
#   2. ASSERT THE SKIP BRANCHES. A missing tool must print a notice and still exit 0. A
#      regression there would either turn advisory notices into hard failures or, worse, turn a
#      real failure into a silent pass.
#
# Determinism: every case runs with PATH trimmed to /usr/bin:/bin, where codespell and lychee are
# absent on both ubuntu-latest and macOS, so the baseline behaviour is identical on the runner
# and on a laptop. The two tool-dependent cases put the ambient tool's directory back on the
# front of that PATH. On macOS /bin/bash is 3.2, which is the portability floor doc-lint.sh
# claims in its own header — so running this locally tests that claim for free.
#
# Portability: no mapfile, no associative arrays, no `local -n` — bash 3.2 safe, like the script
# it tests.

set -uo pipefail

KEEP=0
VERBOSE=0
for arg in "$@"; do
  case "$arg" in
    --keep)    KEEP=1 ;;
    --verbose) VERBOSE=1 ;;
    -h|--help) sed -n '3,8p' "$0"; exit 0 ;;
    *) echo "doc-lint-test: unknown option '$arg'" >&2; exit 2 ;;
  esac
done

SCRIPT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
DOC_LINT="$SCRIPT_DIR/doc-lint.sh"

[ -x "$DOC_LINT" ] || { echo "doc-lint-test: $DOC_LINT not found or not executable" >&2; exit 2; }
command -v git >/dev/null 2>&1 || { echo "doc-lint-test: git is required" >&2; exit 2; }

# The minimal PATH the cases run under. codespell and lychee are never here; git, awk, wc, tr,
# grep, basename and mktemp always are (verified on ubuntu-latest and macOS).
MIN_PATH='/usr/bin:/bin'

# Ambient locations of the optional tools, resolved BEFORE PATH is trimmed, so a tool-dependent
# case can put just that one back.
CODESPELL_DIR=''
LYCHEE_DIR=''
if p="$(command -v codespell 2>/dev/null)"; then CODESPELL_DIR="$(dirname "$p")"; fi
if p="$(command -v lychee 2>/dev/null)";    then LYCHEE_DIR="$(dirname "$p")"; fi

# --- sandbox ---------------------------------------------------------------------------------
SANDBOX="$(mktemp -d "${TMPDIR:-/tmp}/doclint-test.XXXXXX")" || {
  echo "doc-lint-test: mktemp -d failed" >&2; exit 2; }
NAVBOX=''
OUT="$SANDBOX/.stdout"
ERR="$SANDBOX/.stderr"

cleanup() {
  if [ "$KEEP" = "1" ]; then
    echo "Sandbox kept at: $SANDBOX" >&2
    [ -n "$NAVBOX" ] && echo "Orphan sandbox kept at: $NAVBOX" >&2
  else
    rm -rf "$SANDBOX"
    [ -n "$NAVBOX" ] && rm -rf "$NAVBOX"
  fi
}
trap cleanup EXIT

# gen_lines <n> <path> — a file of n numbered lines, spelling-clean and link-free.
gen_lines() {
  local n="$1" path="$2" i=1
  mkdir -p "$(dirname "$path")"
  : > "$path"
  while [ "$i" -le "$n" ]; do
    printf 'Paragraph %d of the fixture page.\n\n' "$i" >> "$path"
    i=$((i + 1))
  done
}

build_sandbox() {
  mkdir -p "$SANDBOX/server/includes" "$SANDBOX/maxscale" \
           "$SANDBOX/.gitbook/includes" "$SANDBOX/dev-docs" "$SANDBOX/.claude"

  # The repo-root marker doc-lint.sh insists on. Carries one ignore word so the
  # "-I .codespellignore is honoured" case has something to be ignored. Spliced for the same
  # reason as the fixtures below.
  printf '%s\n' "reci""eve" > "$SANDBOX/.codespellignore"

  printf '# Clean Page\n\nNothing here trips any check.\n' > "$SANDBOX/server/clean.md"
  printf '# No Links\n\nA page with no links at all.\n'     > "$SANDBOX/server/nolinks.md"
  printf '# Target\n\nInclude target.\n'                    > "$SANDBOX/server/includes/real.md"
  printf '# Cross Space Target\n\nIn another space.\n'      > "$SANDBOX/maxscale/included.md"

  # Include fixtures.
  printf '# Good Include\n\n{%% include "includes/real.md" %%}\n' \
    > "$SANDBOX/server/ok-include.md"
  printf '# Dead Include\n\n{%% include "../.gitbook/includes/nope.md" %%}\n' \
    > "$SANDBOX/server/dead-include.md"
  printf '# Cross Space Include\n\n{%% include "../maxscale/included.md" %%}\n' \
    > "$SANDBOX/server/cross-space.md"
  printf '# Remote Include\n\n{%% include "https://app.gitbook.com/s/x/~/reusable/y/" %%}\n' \
    > "$SANDBOX/server/remote-include.md"
  # Both directories are exempt from the include resolver: they document the syntax with
  # placeholders that are not meant to resolve.
  # A path with a space in it, for the --stdin0 case. The whole point of NUL-delimiting is that
  # this cannot split into two arguments, and a space is the cheapest way to prove it.
  printf '# Spaced Name\n\n{%% include "../.gitbook/includes/nope.md" %%}\n' \
    > "$SANDBOX/server/dead include with spaces.md"
  printf '# Docs About Includes\n\n{%% include "nope.md" %%}\n' > "$SANDBOX/dev-docs/exempt.md"
  printf '# Hook Notes\n\n{%% include "nope.md" %%}\n'          > "$SANDBOX/.claude/exempt.md"

  # Files the shrink guard needs a base revision for. Sizes are picked to isolate one
  # threshold each; see the cases.
  gen_lines 120 "$SANDBOX/server/gutted.md"      # 240 lines -> well over every threshold
  gen_lines  10 "$SANDBOX/server/tiny.md"        #  20 lines -> under SHRINK_FLOOR (30)
  gen_lines  20 "$SANDBOX/server/small-loss.md"  #  40 lines -> can lose <SHRINK_MIN net
  gen_lines  50 "$SANDBOX/server/modest.md"      # 100 lines -> 25% loss: under PCT, over MIN

  # codespell fixtures. The misspellings are spliced across a quote boundary on purpose: written
  # whole, they would make this file itself a permanent false positive in every repo-wide
  # codespell sweep. codespell tokenizes on word characters, so it only ever sees the halves.
  typo="te""h"           # a misspelling of "the"
  ignored="reci""eve"    # a misspelling of "receive" -- the word in the sandbox .codespellignore
  printf '# Typo\n\nPlease %s file.\n' "$typo"    > "$SANDBOX/server/typo.md"
  printf '# Nav\n\n* [%s](clean.md)\n'  "$typo"    > "$SANDBOX/server/SUMMARY.md"
  printf '# Ignored\n\nPlease %s.\n'    "$ignored" > "$SANDBOX/server/ignored-word.md"

  # lychee fixture: a relative target that does not exist. No network needed.
  printf '# Bad Link\n\n[gone](./does-not-exist.md)\n' > "$SANDBOX/server/badlink.md"

  # A stub lychee, for the one branch no installed lychee can reach any more. doc-lint.sh
  # swallows lychee's "No links were found" to mirror the workflow's failIfEmpty: false
  # (DOCS-6272) -- but failIfEmpty is a lychee-ACTION option: the action runs its own emptiness
  # check, while the lychee BINARY has exited 0 on a link-free file since ~0.16 (verified on
  # 0.24.2). So the carve-out is a compatibility shim for older local binaries, inert against a
  # current one, and a real-lychee fixture cannot exercise it. The stub can, which keeps the shim
  # from rotting into dead code that a future cleanup deletes by accident rather than on purpose.
  mkdir -p "$SANDBOX/stub"
  printf '#!/bin/sh\necho "No links were found"\nexit 2\n' > "$SANDBOX/stub/lychee"
  chmod +x "$SANDBOX/stub/lychee"

  # Not a Markdown/HTML path, so the argument filter must drop it.
  printf 'not markdown\n' > "$SANDBOX/server/notes.txt"

  (
    cd "$SANDBOX" || exit 1
    git init -q -b main . >/dev/null 2>&1 || git init -q . >/dev/null 2>&1
    git config user.name  'doc-lint test'
    git config user.email 'doc-lint-test@example.invalid'
    git config commit.gpgsign false
    git add -A >/dev/null
    git commit -q -m 'fixtures' >/dev/null
  ) || return 1

  # Post-commit edits, so the working tree differs from HEAD for the shrink guard.
  gen_lines  10 "$SANDBOX/server/gutted.md"       # 240 -> 20: net 220 of 240 (92%)
  gen_lines   1 "$SANDBOX/server/tiny.md"         #  20 ->  2: pre-image under the floor
  gen_lines  11 "$SANDBOX/server/small-loss.md"   #  40 -> 22: net 18, under SHRINK_MIN (20)
  gen_lines  37 "$SANDBOX/server/modest.md"       # 100 -> 74: net 26, 26% — under PCT (40)
  # Never committed, so the guard has no pre-image to compare against.
  gen_lines 120 "$SANDBOX/server/brand-new.md"
}

# --- the orphan sandbox ----------------------------------------------------------------------
# A SECOND throwaway repo, and it has to be separate. navcheck.py is deliberately absent from
# the main sandbox, which is what makes its SKIP branch testable there -- but the deeper reason
# is cross-talk. `spaces_for()` scans every space that the named paths belong to, not just the
# named files, so one unlisted page anywhere in `server/` is reported by EVERY case that passes
# a server/ path. Measured before writing this: dropping navcheck.py into the main sandbox makes
# it report server/brand-new.md -- a shrink-guard fixture, created post-commit and so newly
# orphaned -- and most of the suite goes red. (DOCS-6586's description predicted the opposite
# problem, that the main sandbox has no SUMMARY.md and orphan cases would vacuously pass;
# server/SUMMARY.md has existed since the codespell exclusion case was added.)
#
# This one installs navcheck.py at .claude/hooks/ so doc-lint.sh's delegation is exercised too.
NAVBOX=''

build_navbox() {
  NAVBOX="$(mktemp -d "${TMPDIR:-/tmp}/doclint-nav.XXXXXX")" || return 1

  mkdir -p "$NAVBOX/.claude/hooks" "$NAVBOX/alpha/sub" "$NAVBOX/alpha/.gitbook/includes" \
           "$NAVBOX/beta" "$NAVBOX/notaspace"

  # doc-lint.sh's repo-root marker, and the scripts it delegates to. navcheck.py is copied
  # rather than symlinked so the fixture keeps working if the checkout moves.
  : > "$NAVBOX/.codespellignore"
  cp "$SCRIPT_DIR/navcheck.py"     "$NAVBOX/.claude/hooks/navcheck.py"
  cp "$SCRIPT_DIR/includecheck.sh" "$NAVBOX/.claude/hooks/includecheck.sh"

  # Ignored paths, for the enumeration case. `scratch/` is the shape that motivated the fix:
  # /graphify writes GRAPH_REPORT.md into the tree, git ignores it, and os.walk did not.
  printf 'scratch/\n*.tmp.md\n' > "$NAVBOX/.gitignore"

  # alpha: a space (it has a SUMMARY.md). Two listed pages, one nested, one committed orphan.
  printf '# Alpha\n\n* [Listed](listed.md)\n* [Nested](sub/nested-listed.md)\n* [Nav To Delete](deleted-nav.md)\n' \
    > "$NAVBOX/alpha/SUMMARY.md"
  printf '# Listed\n\nListed in nav.\n'        > "$NAVBOX/alpha/listed.md"
  printf '# Nested\n\nListed in nav.\n'        > "$NAVBOX/alpha/sub/nested-listed.md"
  printf '# Nav To Delete\n\nListed now.\n'    > "$NAVBOX/alpha/deleted-nav.md"
  # Committed and unlisted: the 219-orphan backlog in miniature. Must stay quiet.
  printf '# Old Orphan\n\nUnlisted since the base revision.\n' \
    > "$NAVBOX/alpha/preexisting-orphan.md"
  # Never a page: pulled in by {% include %}, never nav-listed.
  printf '# Snippet\n\nIncluded, not published.\n' \
    > "$NAVBOX/alpha/.gitbook/includes/snippet.md"

  # beta: a second space, to prove one space's orphan is not reported for another's paths.
  printf '# Beta\n\n* [Listed](listed.md)\n' > "$NAVBOX/beta/SUMMARY.md"
  printf '# Beta Listed\n\nListed in nav.\n' > "$NAVBOX/beta/listed.md"

  # Not a space: no SUMMARY.md. This is what keeps dev-docs/, .claude/ and help-tables/ out
  # without navcheck.py having to name them, so it must never be reported.
  printf '# Not A Space\n\nNo SUMMARY.md beside me.\n' > "$NAVBOX/notaspace/page.md"

  (
    cd "$NAVBOX" || exit 1
    git init -q -b main . >/dev/null 2>&1 || git init -q . >/dev/null 2>&1
    git config user.name  'doc-lint test'
    git config user.email 'doc-lint-test@example.invalid'
    git config commit.gpgsign false
    git add -A >/dev/null
    git commit -q -m 'nav fixtures' >/dev/null
  ) || return 1
}

# --- assertions ------------------------------------------------------------------------------
PASSES=0
FAILURES=0
SKIPS=0
CURRENT=''
CASE_OK=1

# lint <cwd> <path-additions|-> <env-assignments...> -- <doc-lint args...>
# Runs doc-lint.sh with PATH trimmed to MIN_PATH (plus any additions), capturing stdout and
# stderr to separate files and $? into RC. Redirection, never a pipe — see rule 1 above.
RC=0
LINT_ROOT=''
lint() {
  local cwd="$1" path_add="$2"; shift 2
  local root="${LINT_ROOT:-$SANDBOX}"

  local use_path="$MIN_PATH"
  [ "$path_add" != '-' ] && use_path="$path_add:$MIN_PATH"

  # `env -i` so the case sees exactly the variables it names and nothing the caller's shell
  # happens to export -- a DOC_LINT_* left over in the ambient environment would otherwise make
  # results depend on who ran the suite.
  #
  # Built as ONE array rather than expanding a separate envs[] array, because expanding an empty
  # array under `set -u` is an error on bash 3.2 (macOS) -- the same trap this suite just found
  # in doc-lint.sh's norm_path.
  local cmd=(env -i "PATH=$use_path" "HOME=$SANDBOX" "TMPDIR=${TMPDIR:-/tmp}")
  while [ "$#" -gt 0 ] && [ "$1" != '--' ]; do cmd+=("$1"); shift; done
  shift  # drop the --
  cmd+=("$DOC_LINT" "$@")

  set +e
  ( cd "$root/$cwd" && "${cmd[@]}" ) > "$OUT" 2> "$ERR"
  RC=$?
  set -e

  if [ "$VERBOSE" = "1" ]; then
    echo "    stdout: $(wc -c < "$OUT" | tr -d ' ') bytes"
    sed 's/^/      | /' < "$ERR"
  fi
}

# inc <cwd> -- <includecheck args...>
# The same contract as lint(), against includecheck.sh directly. It exists because the script is
# now a CI entry point in its own right (includecheck-pr.yml), so its argument handling, its
# --stdin0 mode and its exit codes are a public surface, not internals reachable only through
# doc-lint.sh. Reads stdin from $INC_STDIN when that is set, so the --stdin0 branch is testable.
INCLUDECHECK="$SCRIPT_DIR/includecheck.sh"
INC_STDIN=''
inc() {
  local cwd="$1"; shift
  [ "$1" = '--' ] && shift

  set +e
  if [ -n "$INC_STDIN" ]; then
    ( cd "$SANDBOX/$cwd" && env -i "PATH=$MIN_PATH" "HOME=$SANDBOX" \
        bash "$INCLUDECHECK" "$@" < "$INC_STDIN" ) > "$OUT" 2> "$ERR"
  else
    ( cd "$SANDBOX/$cwd" && env -i "PATH=$MIN_PATH" "HOME=$SANDBOX" \
        bash "$INCLUDECHECK" "$@" < /dev/null ) > "$OUT" 2> "$ERR"
  fi
  RC=$?
  set -e
}

# nul_list <path> <name...> — write NUL-delimited names, the way `git ls-files -z` emits them.
nul_list() {
  local out="$1"; shift
  : > "$out"
  local n
  for n in "$@"; do printf '%s\0' "$n" >> "$out"; done
}

# nav <env-assignments...> -- <navcheck args...>
# navcheck.py driven directly, in the orphan sandbox. Its findings go to stderr and only the
# clean line to stdout, which is the contract doc-lint.sh's `>/dev/null` relies on, so both are
# captured separately here the same way lint() does it.
nav() {
  local cmd=(env -i "PATH=$MIN_PATH" "HOME=$NAVBOX")
  while [ "$#" -gt 0 ] && [ "$1" != '--' ]; do cmd+=("$1"); shift; done
  shift  # drop the --
  cmd+=(python3 "$NAVBOX/.claude/hooks/navcheck.py" "$@")

  set +e
  ( cd "$NAVBOX" && "${cmd[@]}" ) > "$OUT" 2> "$ERR"
  RC=$?
  set -e

  if [ "$VERBOSE" = "1" ]; then sed 's/^/      | /' < "$ERR"; fi
}

# Restore the orphan sandbox to its base revision: tracked files back, untracked AND ignored
# files gone. Each case builds only what it needs, so cases stay order-independent -- which
# matters more here than in the main sandbox, because these cases mutate SUMMARY.md.
navreset() {
  ( cd "$NAVBOX" && git checkout -q -- . && git clean -fdxq \
      -e .claude -e .codespellignore ) || return 1
}

begin() { CURRENT="$1"; CASE_OK=1; }

problem() {
  [ "$CASE_OK" = "1" ] && printf 'FAIL: %s\n' "$CURRENT" >&2
  CASE_OK=0
  printf '      %s\n' "$1" >&2
}

end() {
  if [ "$CASE_OK" = "1" ]; then
    PASSES=$((PASSES + 1))
    printf 'ok   %s\n' "$CURRENT"
  else
    FAILURES=$((FAILURES + 1))
    printf '      --- stderr ---\n' >&2
    sed 's/^/      /' < "$ERR" >&2
    printf '      --------------\n' >&2
  fi
}

skip() {
  SKIPS=$((SKIPS + 1))
  printf 'SKIP %s (%s)\n' "$1" "$2"
}

want_rc() {
  [ "$RC" = "$1" ] || problem "expected exit $1, got $RC"
}

# Patterns are matched against stderr, because that is where doc-lint.sh contracts to put both
# failures and SKIP notices.
want_err() {
  grep -qF -- "$1" "$ERR" || problem "expected \"$1\" on stderr"
}

want_no_err() {
  grep -qF -- "$1" "$ERR" && problem "did NOT expect \"$1\" on stderr"
  return 0
}

want_out() {
  grep -qF -- "$1" "$OUT" || problem "expected \"$1\" on stdout"
}

want_empty_stdout() {
  [ -s "$OUT" ] && problem "expected empty stdout, got $(wc -c < "$OUT" | tr -d ' ') bytes"
  return 0
}

# --- run -------------------------------------------------------------------------------------
build_sandbox || { echo "doc-lint-test: could not build the sandbox" >&2; exit 2; }
build_navbox  || { echo "doc-lint-test: could not build the orphan sandbox" >&2; exit 2; }

echo "doc-lint-test: sandbox $SANDBOX"
echo "doc-lint-test: bash $BASH_VERSION, script under test $DOC_LINT"
echo

NOFRAG='DOC_LINT_SKIP_FRAGMENTS=1'

# ---- argument handling and the repo-root guard ----------------------------------------------

begin 'no arguments at all exits 0'
lint . - "$NOFRAG" --
want_rc 0
end

begin 'a non-Markdown argument is filtered out, exits 0'
lint . - "$NOFRAG" -- server/notes.txt
want_rc 0
end

begin 'a Markdown path that does not exist is filtered out, exits 0'
lint . - "$NOFRAG" -- server/absent.md
want_rc 0
end

begin 'wrong working directory is a config error, exits 2'
# From server/ there is no .codespellignore. The path must still resolve from that CWD, or the
# argument filter would empty the list and return 0 before the guard is ever reached.
lint server - "$NOFRAG" -- clean.md
want_rc 2
want_err 'must be run from the repo root'
end

begin 'a clean page passes every check, exits 0'
lint . - "$NOFRAG" -- server/clean.md
want_rc 0
want_no_err 'unresolvable include'
want_no_err 'gutted page'
end

# ---- GitBook include resolver (DOCS-6372; gated in CI by includecheck-pr.yml, DOCS-6586) -----
# These first cases go through doc-lint.sh, which is how the pre-commit hook reaches the
# resolver. The block below them drives includecheck.sh directly, which is how CI does.

begin 'a resolvable same-space include passes'
lint . - "$NOFRAG" -- server/ok-include.md
want_rc 0
end

begin 'a dead include fails with "unresolvable include"'
lint . - "$NOFRAG" -- server/dead-include.md
want_rc 1
want_err 'unresolvable include'
want_err '.gitbook/includes/nope.md'
end

begin 'a cross-space include fails with "cross-space include"'
lint . - "$NOFRAG" -- server/cross-space.md
want_rc 1
want_err 'cross-space include'
want_err 'reusable'   # the by-ID form the message tells the author to use instead
end

begin 'an https include target is not resolved on disk'
lint . - "$NOFRAG" -- server/remote-include.md
want_rc 0
end

begin 'dev-docs/ and .claude/ are exempt from the include resolver'
lint . - "$NOFRAG" -- dev-docs/exempt.md .claude/exempt.md
want_rc 0
want_no_err 'unresolvable include'
end

begin 'every include failure on one run is reported, not just the first'
lint . - "$NOFRAG" -- server/dead-include.md server/cross-space.md
want_rc 1
want_err 'unresolvable include'
want_err 'cross-space include'
end

# ---- includecheck.sh as its own entry point (DOCS-6586) --------------------------------------
# The resolver moved out of doc-lint.sh so that CI could run it WITHOUT the checks either side
# of it. That makes the script's own CLI a contract: includecheck-pr.yml depends on --stdin0
# reading the tree from `git ls-files -z`, and on exit 2 meaning "misconfigured workflow" rather
# than "the PR is fine".

begin 'includecheck.sh with no arguments is a usage error, not a silent pass'
inc . --
want_rc 2
want_err 'usage:'
end

begin 'a dead include found through --stdin0'
nul_list "$SANDBOX/.list" 'server/dead-include.md'
INC_STDIN="$SANDBOX/.list" inc . -- --stdin0
INC_STDIN=''
want_rc 1
want_err 'unresolvable include'
end

begin '--stdin0 does not split a path containing a space'
nul_list "$SANDBOX/.list" 'server/dead include with spaces.md'
INC_STDIN="$SANDBOX/.list" inc . -- --stdin0
INC_STDIN=''
want_rc 1
# The whole name, in one piece. Split on the space, each half would be a nonexistent path,
# get filtered out, and the run would pass green with nothing checked.
want_err 'server/dead include with spaces.md'
end

begin '--stdin0 on clean input reports the counts on stdout'
nul_list "$SANDBOX/.list" 'server/ok-include.md' 'server/clean.md'
INC_STDIN="$SANDBOX/.list" inc . -- --stdin0
INC_STDIN=''
want_rc 0
# A gate has to be able to prove it did something: "1 include across 2 files" and "0 includes
# across 0 files" are the same exit code and must not be the same output.
want_out '1 relative include(s) across 2 file(s)'
end

begin '--stdin0 on empty input says so rather than claiming a clean tree'
nul_list "$SANDBOX/.list"
INC_STDIN="$SANDBOX/.list" inc . -- --stdin0
INC_STDIN=''
want_rc 0
want_out 'no Markdown or HTML files'
end

begin '--stdin0 rejects extra arguments'
inc . -- --stdin0 server/clean.md
want_rc 2
want_err 'usage:'
end

begin 'a missing includecheck.sh fails doc-lint.sh — it is not a SKIP'
# Every other dependency doc-lint.sh delegates to is an external TOOL a contributor may
# legitimately not have, so those are SKIPs. This one is checked in beside it, so its absence
# is a broken checkout, and a check that cannot run must not report success. Exercised by
# copying doc-lint.sh somewhere with no sibling next to it.
mkdir -p "$SANDBOX/lonely"
cp "$DOC_LINT" "$SANDBOX/lonely/doc-lint.sh"
set +e
( cd "$SANDBOX" && env -i "PATH=$MIN_PATH" "HOME=$SANDBOX" "TMPDIR=${TMPDIR:-/tmp}" \
    DOC_LINT_SKIP_FRAGMENTS=1 \
    bash "$SANDBOX/lonely/doc-lint.sh" server/clean.md ) > "$OUT" 2> "$ERR"
RC=$?
set -e
want_rc 1
want_err 'cannot resolve GitBook includes'
want_err 'broken checkout'
end

# ---- orphaned pages / navcheck.py (DOCS-6567; fixtures added in DOCS-6586) -------------------
# Runs in the orphan sandbox (see build_navbox). Asserts the exit code AND the message, per
# DOCS-6471's rule that a gate whose wording is untested is a gate nobody can act on.

begin 'a new page with no nav entry is reported as newly orphaned'
printf '# Unlisted\n\nAdded without a nav entry.\n' > "$NAVBOX/alpha/unlisted-new.md"
nav -- new HEAD alpha/unlisted-new.md
want_rc 1
want_err 'but not listed in SUMMARY.md'
want_err 'alpha/unlisted-new.md'
want_err 'DOCS-6566'          # the message points at the case it exists for
navreset
end

begin 'the same new page, listed in SUMMARY.md, is not reported'
printf '# Unlisted\n\nAdded with a nav entry.\n' > "$NAVBOX/alpha/unlisted-new.md"
printf '* [Now Listed](unlisted-new.md)\n' >> "$NAVBOX/alpha/SUMMARY.md"
nav -- new HEAD alpha/unlisted-new.md
want_rc 0
want_out 'no newly orphaned pages'
navreset
end

begin 'a deleted nav entry with the page surviving is reported'
# The quieter direction: the file still works locally and only vanishes from the built site.
grep -v 'deleted-nav.md' "$NAVBOX/alpha/SUMMARY.md" > "$NAVBOX/alpha/.sm" \
  && mv "$NAVBOX/alpha/.sm" "$NAVBOX/alpha/SUMMARY.md"
nav -- new HEAD alpha/SUMMARY.md
want_rc 1
want_err 'alpha/deleted-nav.md'
navreset
end

begin 'DOC_LINT_ALLOW_ORPHAN naming the path acknowledges it, exits 0'
printf '# Unlisted\n\nDeliberate.\n' > "$NAVBOX/alpha/unlisted-new.md"
nav DOC_LINT_ALLOW_ORPHAN=alpha/unlisted-new.md -- new HEAD alpha/unlisted-new.md
want_rc 0
want_no_err 'but not listed in SUMMARY.md'
navreset
end

begin 'DOC_LINT_ALLOW_ORPHAN=all skips the check entirely, exits 0'
printf '# Unlisted\n\nDeliberate.\n' > "$NAVBOX/alpha/unlisted-new.md"
nav DOC_LINT_ALLOW_ORPHAN=all -- new HEAD alpha/unlisted-new.md
want_rc 0
navreset
end

begin 'a committed unlisted page is pre-existing, not newly orphaned'
# The 219-orphan backlog in miniature. This is the whole reason the gate is history-aware:
# absolute checking would fail every unrelated PR on breakage it did not introduce.
nav -- new HEAD alpha/listed.md
want_rc 0
want_out 'pre-existing, unchanged'
end

begin 'a file under .gitbook/ is not a page, so an unlisted one is not reported'
printf '# New Snippet\n\nIncluded, never nav-listed.\n' \
  > "$NAVBOX/alpha/.gitbook/includes/new-snippet.md"
nav -- new HEAD alpha/.gitbook/includes/new-snippet.md
want_rc 0
navreset
end

begin "a new space's own SUMMARY.md is not reported as an orphan"
mkdir -p "$NAVBOX/gamma"
printf '# Gamma\n\n* [Page](page.md)\n' > "$NAVBOX/gamma/SUMMARY.md"
printf '# Gamma Page\n\nListed.\n'      > "$NAVBOX/gamma/page.md"
nav -- new HEAD gamma/page.md
want_rc 0
want_no_err 'SUMMARY.md:'
navreset
end

begin 'a directory with no SUMMARY.md is not a space'
# What keeps dev-docs/, .claude/ and help-tables/ out without navcheck.py naming any of them.
# Note when mutation-testing this one: the requirement is enforced TWICE -- in all_spaces() and
# again in orphans_now() -- so breaking either alone leaves the case green. Both have to go
# before it fails, which is a property of the script, not a weakness of the fixture.
printf '# Loose\n\nNo SUMMARY.md beside me.\n' > "$NAVBOX/notaspace/new-page.md"
nav -- new HEAD notaspace/new-page.md
want_rc 0
want_no_err 'notaspace'
navreset
end

begin "an orphan in one space is not reported for another space's paths"
printf '# Unlisted\n\nIn alpha.\n' > "$NAVBOX/alpha/unlisted-new.md"
nav -- new HEAD beta/listed.md
want_rc 0
want_no_err 'alpha/unlisted-new.md'
navreset
end

begin 'an ignored stray page is not reported, but a genuinely new one is'
# The DOCS-6586 fixture for PR #1024's enumeration change. The base side is read with
# `git ls-tree`, so enumerating the working tree with os.walk compared a set that includes
# ignored litter against one that structurally cannot -- and a /graphify GRAPH_REPORT.md then
# reported as newly orphaned for whichever PR ran the gate next, irreproducibly, since CI runs
# on a clean checkout. `git ls-files --cached --others --exclude-standard` keeps the case the
# gate exists for and drops what .gitignore covers. Both halves are asserted: dropping the
# ignored file is worthless if it also drops the real finding.
mkdir -p "$NAVBOX/alpha/scratch"
printf '# Graph Report\n\n/graphify output.\n' > "$NAVBOX/alpha/scratch/GRAPH_REPORT.md"
printf '# Editor Litter\n\nnope.\n'            > "$NAVBOX/alpha/notes.tmp.md"
printf '# Real New Page\n\nUnlisted for real.\n' > "$NAVBOX/alpha/genuinely-new.md"
nav -- new HEAD alpha/genuinely-new.md
want_rc 1
want_err 'alpha/genuinely-new.md'
want_no_err 'GRAPH_REPORT.md'
want_no_err 'notes.tmp.md'
navreset
end

begin 'an unresolvable base revision SKIPs rather than failing'
printf '# Unlisted\n\nWould be a finding with a real base.\n' > "$NAVBOX/alpha/unlisted-new.md"
nav -- new refs/heads/no-such-branch alpha/unlisted-new.md
want_rc 0
want_err 'SKIPPED'
navreset
end

begin 'the new mode with no revision is a usage error, not a pass'
nav -- new
want_rc 2
want_err 'needs a revision'
end

begin 'an unknown mode is a usage error'
nav -- sideways HEAD
want_rc 2
want_err 'unknown mode'
end

begin 'the check mode reports the standing inventory, pre-existing orphans included'
# The triage mode, which is absolute where `new` is history-aware.
nav -- check alpha
want_rc 1
want_err 'alpha/preexisting-orphan.md'
end

begin 'the check mode honours DOC_LINT_ALLOW_ORPHAN=all'
nav DOC_LINT_ALLOW_ORPHAN=all -- check alpha
want_rc 0
end

# ---- navcheck.py through doc-lint.sh (the delegation, not the checker) -----------------------

begin 'doc-lint.sh fails when navcheck.py reports a newly orphaned page'
printf '# Unlisted\n\nAdded without a nav entry.\n' > "$NAVBOX/alpha/unlisted-new.md"
LINT_ROOT="$NAVBOX" lint . - "$NOFRAG" DOC_LINT_BASE=HEAD -- alpha/unlisted-new.md
LINT_ROOT=''
want_rc 1
want_err 'but not listed in SUMMARY.md'
want_empty_stdout       # navcheck's clean line is swallowed; findings go to stderr
navreset
end

begin 'DOC_LINT_ALLOW_ORPHAN reaches navcheck.py through doc-lint.sh'
printf '# Unlisted\n\nDeliberate.\n' > "$NAVBOX/alpha/unlisted-new.md"
LINT_ROOT="$NAVBOX" lint . - "$NOFRAG" DOC_LINT_BASE=HEAD \
  DOC_LINT_ALLOW_ORPHAN=alpha/unlisted-new.md -- alpha/unlisted-new.md
LINT_ROOT=''
want_rc 0
want_no_err 'but not listed in SUMMARY.md'
navreset
end

begin 'a missing navcheck.py is a SKIP notice, exits 0'
# In the MAIN sandbox, which deliberately has no .claude/hooks/navcheck.py.
lint . - "$NOFRAG" DOC_LINT_BASE=HEAD -- server/clean.md
want_rc 0
want_err 'navcheck.py not found'
want_err 'orphan check SKIPPED'
end

begin 'a tree that is not a git work tree SKIPs the orphan check'
# doc-lint.sh needs a base revision, so outside a work tree the check cannot run -- and must
# say so rather than pass silently. The copy has to live OUTSIDE any repository: putting it
# under $NAVBOX (a git repo) does not test this branch at all, it tests the nested-repo one
# below, because git happily answers for the enclosing repo.
NOGIT="$(mktemp -d "${TMPDIR:-/tmp}/doclint-nogit.XXXXXX")"
( cd "$NAVBOX" && git archive HEAD ) | ( cd "$NOGIT" && tar xf - ) || problem 'archive failed'
LINT_ROOT="$NOGIT" lint . - "$NOFRAG" -- alpha/listed.md
LINT_ROOT=''
want_rc 0
want_err 'not a git work tree'
want_err 'orphan check SKIPPED'
rm -rf "$NOGIT"
end

begin 'a docs tree nested inside an unrelated repo SKIPs instead of reporting everything'
# Found by getting the fixture above wrong. doc-lint.sh's work-tree guard runs from the CWD
# while navcheck.py computes its own root from .codespellignore, so in a nested checkout the
# two disagree: git answers for the OUTER repo, `orphans_at` comes back empty, and every
# long-unlisted page is reported as NEWLY orphaned -- the history-awareness that keeps the
# 219-page backlog quiet collapses in the false-positive direction. Guarded in navcheck.py by
# comparing its root against `git rev-parse --show-toplevel`.
NESTED="$NAVBOX/nested"
mkdir -p "$NESTED"
( cd "$NAVBOX" && git archive HEAD ) | ( cd "$NESTED" && tar xf - ) || problem 'archive failed'
# preexisting-orphan.md has been unlisted since the base revision, so a correct run says
# nothing about it; an unguarded one calls it newly orphaned.
LINT_ROOT="$NESTED" lint . - "$NOFRAG" DOC_LINT_BASE=HEAD -- alpha/listed.md
LINT_ROOT=''
want_rc 0
want_err 'is not the top of its git repository'
want_no_err 'alpha/preexisting-orphan.md'
rm -rf "$NESTED"
end

# ---- net line-loss guard (DOCS-6470 / DOCS-6442; no CI counterpart) --------------------------

begin 'a gutted page fails with "possible gutted page"'
lint . - "$NOFRAG" DOC_LINT_BASE=HEAD -- server/gutted.md
want_rc 1
want_err 'possible gutted page'
want_err 'server/gutted.md'
end

begin 'DOC_LINT_ALLOW_SHRINK naming the path acknowledges it, exits 0'
lint . - "$NOFRAG" DOC_LINT_BASE=HEAD DOC_LINT_ALLOW_SHRINK=server/gutted.md -- server/gutted.md
want_rc 0
want_no_err 'possible gutted page'
end

begin 'DOC_LINT_ALLOW_SHRINK=all skips the guard entirely, exits 0'
lint . - "$NOFRAG" DOC_LINT_BASE=HEAD DOC_LINT_ALLOW_SHRINK=all -- server/gutted.md
want_rc 0
want_no_err 'possible gutted page'
end

begin 'a comma-separated DOC_LINT_ALLOW_SHRINK list is accepted'
lint . - "$NOFRAG" DOC_LINT_BASE=HEAD \
     DOC_LINT_ALLOW_SHRINK=server/other.md,server/gutted.md -- server/gutted.md
want_rc 0
want_no_err 'possible gutted page'
end

begin 'a file absent from the base revision has nothing to have lost, exits 0'
lint . - "$NOFRAG" DOC_LINT_BASE=HEAD -- server/brand-new.md
want_rc 0
want_no_err 'possible gutted page'
end

begin 'a pre-image under DOC_LINT_SHRINK_FLOOR is not considered'
lint . - "$NOFRAG" DOC_LINT_BASE=HEAD -- server/tiny.md
want_rc 0
want_no_err 'possible gutted page'
end

begin 'a net loss under DOC_LINT_SHRINK_MIN is not flagged'
# 40 lines -> 22: 45% of the pre-image, which is over DOC_LINT_SHRINK_PCT. Only the absolute
# floor of 20 net lines keeps this green, so it isolates that knob.
lint . - "$NOFRAG" DOC_LINT_BASE=HEAD -- server/small-loss.md
want_rc 0
want_no_err 'possible gutted page'
end

begin 'a net loss under DOC_LINT_SHRINK_PCT is not flagged'
# 100 lines -> 74: 26 net lines, over DOC_LINT_SHRINK_MIN, so only the percentage keeps it green.
lint . - "$NOFRAG" DOC_LINT_BASE=HEAD -- server/modest.md
want_rc 0
want_no_err 'possible gutted page'
end

begin 'lowering DOC_LINT_SHRINK_PCT flags the same modest loss'
# The mirror of the case above: proves the threshold is really read from the environment rather
# than the guard happening to be inert on this fixture.
lint . - "$NOFRAG" DOC_LINT_BASE=HEAD DOC_LINT_SHRINK_PCT=10 -- server/modest.md
want_rc 1
want_err 'possible gutted page'
end

begin 'an unresolvable DOC_LINT_BASE disables the history-aware checks rather than failing'
lint . - "$NOFRAG" DOC_LINT_BASE=refs/heads/no-such-branch -- server/gutted.md
want_rc 0
want_no_err 'possible gutted page'
end

# ---- SKIP branches: a missing tool is a notice, never a failure ------------------------------

begin 'codespell absent is a SKIP notice on stderr, exits 0'
lint . - "$NOFRAG" -- server/typo.md
want_rc 0
want_err 'codespell not installed'
want_err 'SKIPPED'
end

begin 'lychee absent is a SKIP notice on stderr, exits 0'
lint . - "$NOFRAG" -- server/badlink.md
want_rc 0
want_err 'lychee not installed'
want_err 'SKIPPED'
end

begin 'a missing fragcheck.py is a SKIP notice, exits 0'
# Reached only because the sandbox has no .claude/hooks/fragcheck.py; DOC_LINT_SKIP_FRAGMENTS is
# deliberately NOT set here, so this exercises the absent-script branch rather than the opt-out.
lint . - -- server/clean.md
want_rc 0
want_err 'fragcheck.py not found'
want_err 'SKIPPED'
end

begin 'DOC_LINT_SKIP_FRAGMENTS=1 suppresses the anchor check silently'
lint . - "$NOFRAG" -- server/clean.md
want_rc 0
want_no_err 'fragcheck.py not found'
end

begin 'diagnostics go to stderr; stdout stays empty even on failure'
lint . - "$NOFRAG" -- server/dead-include.md
want_rc 1
want_empty_stdout
end

# ---- the tool-present branches: proof doc-lint actually REACHES its checkers -----------------
# This is the assertion DOCS-6409 would have failed: the script died at line 209, before either
# checker ran, and every SKIP-branch test above would still have passed.

if [ -n "$CODESPELL_DIR" ]; then
  begin 'codespell present: a misspelling fails with "possible misspellings" [needs codespell]'
  lint . "$CODESPELL_DIR" "$NOFRAG" -- server/typo.md
  want_rc 1
  want_err 'possible misspellings'
  want_no_err 'codespell not installed'
  end

  begin 'codespell present: -I .codespellignore is honoured [needs codespell]'
  lint . "$CODESPELL_DIR" "$NOFRAG" -- server/ignored-word.md
  want_rc 0
  end

  begin 'codespell present: SUMMARY.md is excluded, mirroring codespell.yml [needs codespell]'
  # SUMMARY.md carries the same misspelling as typo.md. GitBook truncates its link labels at 100
  # chars, often mid-word, so codespell.yml's files_ignore drops it — and doc-lint must match.
  lint . "$CODESPELL_DIR" "$NOFRAG" -- server/SUMMARY.md
  want_rc 0
  want_no_err 'possible misspellings'
  end
else
  skip 'codespell present: three cases' 'codespell not on PATH'
fi

if [ -n "$LYCHEE_DIR" ]; then
  begin 'lychee present: a dead relative link fails with "broken links" [needs lychee]'
  lint . "$LYCHEE_DIR" "$NOFRAG" -- server/badlink.md
  want_rc 1
  want_err 'broken links'
  want_no_err 'lychee not installed'
  end

  begin 'lychee present: a stale path never reaches lychee [needs lychee]'
  # The `[ -f "$f" ]` test in the argument filter is what makes this safe. Without it a path that
  # has been deleted or renamed since it was staged reaches lychee, which exits 1 with "Input
  # not found as file and not a valid URL" -- reported to the author as a broken LINK, on a page
  # that no longer exists. Only a tool-present case can catch that: with both checkers absent
  # the unfiltered path is inert, which is why the plain filter case above passes either way.
  lint . "$LYCHEE_DIR" "$NOFRAG" -- server/absent.md
  want_rc 0
  want_no_err 'broken links'
  end

  begin 'lychee present: a page with no links is not a failure [needs lychee]'
  # Pins the OUTCOME for a link-free page (a nav stub must never fail), not the carve-out branch
  # — a current lychee exits 0 here, so the branch is not reached. The stub case below covers it.
  lint . "$LYCHEE_DIR" "$NOFRAG" -- server/nolinks.md
  want_rc 0
  want_no_err 'broken links'
  end
else
  skip 'lychee present: two cases' 'lychee not on PATH'
fi

begin 'lychee "No links were found" is swallowed, not reported as broken links'
# Uses the stub lychee built above, because no current lychee binary can produce this. See the
# comment on the stub in build_sandbox.
lint . "$SANDBOX/stub" "$NOFRAG" -- server/nolinks.md
want_rc 0
want_no_err 'broken links'
want_no_err 'lychee not installed'
end

# --- report ----------------------------------------------------------------------------------
# A case group that opted out because its tool was missing is reported, not counted as a pass.
# CI sets DOC_LINT_TEST_REQUIRE_ALL=1 on the runner where it installs codespell and lychee, so a
# botched install turns into a red run instead of a green one that quietly tested less. Without
# it, "31 passed, 0 failed, 1 skipped" is indistinguishable from full coverage at a glance --
# the same trap as an empty-list guard that proves nothing about the path that fires (DOCS-6401).
if [ "${DOC_LINT_TEST_REQUIRE_ALL:-}" = "1" ] && [ "$SKIPS" -gt 0 ]; then
  printf 'FAIL: DOC_LINT_TEST_REQUIRE_ALL=1, but %d case group(s) opted out for a missing tool.\n' \
    "$SKIPS" >&2
  printf '      Every optional tool is expected on PATH here. Check the install steps.\n' >&2
  FAILURES=$((FAILURES + 1))
fi

echo
printf '%d passed, %d failed, %d skipped\n' "$PASSES" "$FAILURES" "$SKIPS"
# No trailing `exit 0`: falling off the end yields the status of the test below, which is 0 when
# nothing failed. Written this way because shellcheck 0.11 reports SC2329 ("this function is
# never invoked") for the EXIT-trap cleanup above when a script ends in an unconditional `exit`.
[ "$FAILURES" -eq 0 ] || exit 1
