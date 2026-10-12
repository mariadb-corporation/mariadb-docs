# gitbook-edit-digest.jq — build the Slack payload for nightly-gitbook-edits.yml (DOCS-6914).
#
#   jq -n --slurpfile commits commits.jsonl
#         --arg repo --arg server --arg run --arg base --arg basedate --arg compare
#         -f gitbook-edit-digest.jq
#
# Kept in its own file rather than inline in the workflow so it can be run locally against a
# commits.jsonl from gitbook-edit-digest.sh -- the payload is the part a reviewer sees, and it
# should be testable without a workflow run.
#
# ESCAPING. Valid JSON is not the same as safe mrkdwn. Every string here except the URLs this
# file builds itself comes from a commit that reached `main` with NO review -- that is the whole
# reason the digest exists -- so a GitBook title reading
#   <https://evil.example|github.com/.../commit/abc>
# would otherwise render as a trusted bot's link whose visible text lies about its target.
# `esc` neutralizes <, > and &. `*`, `_` and backticks are deliberately not escaped, the same
# decision as nightly-fragcheck.yml and nightly-unlabeled-prs.yml.
#
# SIZE. Slack rejects an incoming-webhook payload over 4,000 characters with msg_too_long, and
# the workflow posts with `errors: true`, so an oversize night would be a red run that delivers
# nothing -- on exactly the night with the most to review. Entries are therefore added whole
# until the budget runs out, and the rest are counted, never cut mid-entry. Each entry's gate
# excerpt is capped on its own so one noisy commit cannot crowd out the others.

def esc: gsub("&"; "&amp;") | gsub("<"; "&lt;") | gsub(">"; "&gt;");
# The gate excerpt for Slack: finding lines only, cut at a whole line. doc-lint.sh follows most
# findings with a deeply indented paragraph of advice ("A renamed heading breaks every inbound
# link...") that is the same every time; it stays in the run summary, where the full log is.
def excerpt($n):
  (split("\n") | map(select(test("^ {6,}") | not))) as $lines
  | (reduce $lines[] as $l ({out: [], len: 0, cut: false};
      if .cut or (.len + ($l | length) + 1 > $n) then .cut = true
      else .out += [$l] | .len += ($l | length) + 1 end))
  | (.out | join("\n")) + (if .cut then "\n… more in the workflow run summary" else "" end);

def status_word:
  {"A": "added", "M": "edited", "D": "deleted", "R": "renamed", "C": "copied", "T": "edited"}[.]
  // "changed";

def page_lines:
  . as $pages
  | ($pages[0:4] | map("    `\(.path | esc)` (\(.status | status_word))"))
    + (if ($pages | length) > 4 then ["    … and \(($pages | length) - 4) more"] else [] end);

def verdict_line:
  if .verdict == "pass" then "  :white_check_mark: Gates passed."
  elif .verdict == "pass-preexisting" then
    # Some gate also failed on the parent, so none of it is this commit's. On a weeks-old commit
    # that is mostly today's registers disagreeing with an old tree, not anything on the page.
    "  :white_check_mark: No new gate findings."
  elif .verdict == "fail" then
    "  :warning: *New gate findings:*\n```\n\(.findings | excerpt(600) | esc)\n```"
  elif .verdict == "too-large" then
    "  :mag: Not gated: \(.pages | length) pages changed. Review the diff by hand."
  elif .verdict == "no-pages" then
    "  No pages added or edited, so nothing to gate."
  else "  :x: The gates could not run on this commit. See the workflow run." end;

def entry:
  # A sync with no CR number ("GitBook: Export content from Release Notes") shows its subject
  # as the title, so it gets no label of its own.
  (if .cr then "GITBOOK-\(.cr) " else "" end) as $cr
  | ([.spaces[] | esc] | join(", ")) as $spaces
  | (["• *\(.author | esc)* — \($cr)in `\($spaces)`: \(.title | esc)",
      "  <\($server)/\($repo)/commit/\(.sha)|diff \(.short)>"
        + (if .other_files > 0 then " · \(.other_files) non-page file(s) too" else "" end)]
     + (.pages | page_lines)
     + [verdict_line])
  | join("\n");

($commits | length) as $n
| ([$commits[] | select(.verdict == "fail")] | length) as $failing
| if $n == 0 then
    { text: (
        ":coffee: *No GitBook-UI edits* reached \($repo) since \($base) (\($basedate)), so there is nothing to review."
        + "\n\n<\($run)|workflow run>") }
  else
    (":pencil2: *\($n) GitBook-UI edit\(if $n == 1 then "" else "s" end) to review* in \($repo) since \($base) (\($basedate))"
     + (if $failing > 0 then " — \($failing) with new gate findings" else "" end)) as $head
    | ("These merged in the GitBook app with no pull request, so no PR check ran and nobody reviewed them."
       + " Reply in the thread or react :white_check_mark: once you have looked."
       + " Fixes go in a normal PR that names the commit."
       + "\n<\($compare)|all commits in this window> · <\($run)|workflow run and full gate logs>") as $foot
    | ([$commits[] | entry]) as $entries
    | (3600 - ($head | length) - ($foot | length)) as $budget
    | (reduce $entries[] as $e ({kept: [], used: 0};
        if .used + ($e | length) + 2 <= $budget and (.dropped // 0) == 0
        then .kept += [$e] | .used += ($e | length) + 2
        else .dropped = ((.dropped // 0) + 1) end)) as $fit
    | { text: (
          $head + "\n\n" + ($fit.kept | join("\n\n"))
          + (if ($fit.dropped // 0) > 0
             then "\n\n… and \($fit.dropped) more, listed in the workflow run summary."
             else "" end)
          + "\n\n" + $foot) }
  end
