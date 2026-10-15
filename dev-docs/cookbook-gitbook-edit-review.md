# Cookbook: reviewing GitBook-UI edits

An edit merged in the GitBook app reaches `main` as a `GITBOOK-<n>: <title>` commit. The
committer is `gitbook-bot <ghost@gitbook.com>` and the author is whoever made the edit. There is
no pull request, so **no PR check runs and nobody reviews it**. Blocking those merges isn't
practical, so the docs team reviews them after they land. This page describes how (DOCS-6914).

## The digest

`.github/workflows/nightly-gitbook-edits.yml` runs on weekdays at 06:35 UTC and posts to
**#docs-notifications**. Each GitBook commit since the previous run gets one entry:

- the author, the `GITBOOK-<n>` number, the top-level directory it touched, and the title
  (CR numbers are per GitBook space, so `GITBOOK-1640` and `GITBOOK-2399` are in different
  spaces);
- a link to the commit diff;
- up to four changed pages, each marked added, edited, deleted or renamed;
- a :rotating_light: warning if the commit changed a **generated page**, which the next run of
  its generator overwrites, so the edit has to be reverted and made in the page's source. The
  list lives in `generated_pages` in `.github/scripts/gitbook-edit-digest.jq`. Today it holds
  the MaxScale settings reference (`dev-docs/cookbook-maxscale-settings-reference.md`) and the
  Plugin API pages under `server/reference/plugins/api-plugin/`. The gates can't catch this,
  because a hand edit to a generated page usually passes all of them;
- the content-gate result.

It lists **every** GitBook commit, including clean ones, because the goal is for a person to
look at each diff. The gate results are there to help.

Each run starts where the last successful scheduled run ended, so consecutive posts cover
`main` with no gap between them. A run that failed or never started is caught up by the next
one, which can list a few entries again but never drops one. Only when there is no usable
previous run does it fall back to the last 24 hours (72 on Mondays) and warn about it. The run
summary says which way the window start was chosen.

Tuesday to Friday it stays silent when there were no GitBook edits. Monday covers the weekend,
and posts even when there was nothing. That message is the heartbeat: it shows the schedule is
still running.

### What the gate result means

The gates are the ones `run-doc-gates.sh` runs on bot PRs: codespell, lychee, includes, heading
anchors, nav coverage, page descriptions, Mermaid contrast, line loss, version includes, the
Post Download checks, and the retired-KB guard. They run on each commit separately, against its
own parent, using the tooling from the commit that runs the digest. The tooling never comes from
the commit being checked.

| Result | Meaning |
|--------|---------|
| ✅ Gates passed | The commit introduced no finding. |
| ✅ No new gate findings | Some gate failed, but it failed the same way on the parent commit, so the edit did not cause it. |
| ⚠️ New gate findings | The commit introduced these findings. The excerpt lists them, and the workflow run summary has the full log. |
| 🔍 Not gated | More than 150 pages changed (a GitBook "Export content" commit, typically). Review the diff by hand. |
| No pages to gate | Only deletions or non-page files (images, `.gitbook/` assets). |
| ❌ Could not run | A tooling failure, not a content finding. The run is red, and a failure notice follows. |

The digest reports only what the commit introduced, not every finding on the page. codespell and
lychee check whole files, and the tree-wide checks read the whole tree. Without this filter, an
edit to one line would be blamed for a typo that was already on the page, so the same gates run
on the parent as well and their findings are subtracted. Line-number shifts are ignored.

Two limits to keep in mind:

- An external link that times out once can show up as new. Open it before you file anything.
- A commit that only deletes pages is not gated, and no other check looks for links that still
  point at the deleted page. Search for inbound links by hand (`grep -rn '<page-file-name>'`).

## The routine

**Who reviews.** Stefan Hinz reviews every entry, including his own GitBook edits, which are
rare. If the volume grows, he asks other writers to share the work. Anyone else may still review
an entry, by marking it as described below.

**How to mark an entry as reviewed.** Reply in the post's thread naming the commit (for example
`9f0b0f243 looks good`), or react ✅ to the post when you have looked at all of its entries. An
entry with no reply and no ✅ is still waiting.

**What to look at.** Open the diff and check it against the house rules the PR gates cannot
enforce: the [style guide](style-guide.md), Title Case headings, version facts against the
source, and cross-space links written as [aliases](link-aliases.md) rather than literal GitBook
URLs. A ⚠️ entry's findings are the minimum to fix, not the whole review.

**How to file a correction.** Never fix it in place with another unreviewed GitBook edit. Open a
normal pull request:

1. If the fix needs a ticket (anything beyond a typo), file a DOCS ticket that names the commit.
2. Name the original commit in the PR description, for example `Fixes 9f0b0f243 (GITBOOK-2399)`.
3. Reply in the digest thread with the PR link, so the next reviewer sees it is handled.

If the edit was wrong in substance rather than form, tell its author in the thread as well, so
the same thing doesn't come back in the next edit.

## Running it by hand

Dispatch the workflow from the Actions tab. `base_rev` and `head_rev` select any window, for
example `9f0b0f243^` and `9f0b0f243`. Set `always_post` to post a window with no GitBook commits.

Locally, from the repo root (needs codespell, lychee, jq and Python 3):

```bash
bash .github/scripts/gitbook-edit-digest.sh 9f0b0f243^ 9f0b0f243 /tmp/digest
jq -n --slurpfile commits /tmp/digest/commits.jsonl \
  --arg repo mariadb-corporation/mariadb-docs --arg server https://github.com \
  --arg run RUN --arg base BASE --arg basedate DATE --arg compare COMPARE \
  -f .github/scripts/gitbook-edit-digest.jq | jq -r .text
```

The first command writes one JSON line per commit plus each commit's full gate log. The second
renders the Slack message exactly as it would be posted.
