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
  the MaxScale settings reference (`dev-docs/cookbook-maxscale-settings-reference.md`), the
  Plugin API pages under `server/reference/plugins/api-plugin/`, and the Community Tools pages
  synced into `tools/community/mariadb-ai-plugins/` and `tools/community/mariadb-shell/`
  (`dev-docs/cookbook-community-tools-sync.md`). The gates can't catch this,
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

**Who reviews.** The person on docs duty reviews every entry, their own GitBook edits included
([runbook-docs-duty.md](runbook-docs-duty.md)). Anyone else may still review an entry, by marking
it as described below.

**The recommended way: ask Claude.** In Claude Code, in your mariadb-docs clone, run
`/gitbook-review` (or ask it to "review the GitBook edits in today's digest"). The
`gitbook-review` skill reads the digest, sorts each commit's changes, checks the content, and
proposes what to fix. It asks before it opens a PR, merges or posts in Slack. Check its sorting
before you accept it. The rest of this section is what it does, so you can follow it, check it,
or do it by hand.

### Most of a GitBook diff isn't the author's change

Every time the GitBook editor saves a page, it rewrites the whole page in its own Markdown.
Readers see none of it. A one-image edit (GITBOOK-199, `35914be5a`) showed up as 27 files and
about 430 changed lines. What a save does:

- links rewritten as `file.md#anchor`, and `app.gitbook.com/o/<org>/s/<space>/…` shortened to
  `app.gitbook.com/s/<space>/…` (same target; that's GitBook's own form for cross-space links);
- `-` list markers turned into `*`, `__x__` into `**x**`, trailing `&#x20;` removed, table rows
  re-padded;
- `{% hint %}` inside tables or lists turned into `<div data-gb-custom-block data-tag="hint">`;
- the H1 set to the page's navigation title from `SUMMARY.md`;
- H5 and H6 headings turned into bold text;
- HTML comments deleted;
- byte-identical images merged into one file, so an image path can change while the picture
  doesn't.

Reverting any of this gains nothing: the next editor save of the page writes it again. A few
have side effects worth a fix: a heading change that drops an anchor another page links to, a
deleted comment that held a TODO, and alt text that came back empty.

**So the review sorts each change; it doesn't revert the commit.** Revert only the specific
change that's wrong.

### 1. Find the commit's SHA

`<sha>` in the commands below is the commit's ID: 40 hexadecimal characters, of which the first
9 are enough. In each digest entry, the second line is a link that reads `diff <short-sha>`, for
example `diff 35914be5a`. The full SHA is at the end of the link's URL.

Don't search by `GITBOOK-<n>`: each GitBook space numbers its edits separately. The 19 Nov digest
has two GITBOOK-199 entries, `704c331a8` in `mariadb-cloud` and `35914be5a` in `tools`.

Run the commands in your mariadb-docs clone, from any folder inside it. `origin` has to be
`mariadb-corporation/mariadb-docs`, not your own fork (`git remote -v`). Without the digest, list
the latest GitBook commits. GitBook commits every save as its bot, so the *committer* finds GitBook
edits; the person who made the edit is the *author*:

```bash
git fetch origin
git log --oneline --committer=ghost@gitbook.com -5 origin/main
git log --oneline --committer=ghost@gitbook.com --author=<part of an email address> -5 origin/main
git show --stat <sha>
```

### 2. Read the diff without the noise

```bash
git show -w --word-diff=color <sha>              # whole commit
git show -w --word-diff=color <sha> -- <file>    # one page
```

Sort each change into **reformatting** (the list above: accept it) or **content** (new or
changed text, images, code, link targets). Review content like a PR: the
[style guide](style-guide.md), Title Case headings, version facts against the source, and links
that resolve. A cross-space link GitBook wrote as `https://app.gitbook.com/s/…` is fine; a link to
an unmerged GitBook change request isn't. A ⚠️ entry's findings are the minimum to fix,
not the whole review. For a deleted page, look for inbound links
(`git grep -n '<file-name>' origin/main`).

### 3. Decide what to do with each content change

| Finding | Action |
|---|---|
| Fine | Nothing. |
| A small mistake: typo, wrong version, broken link | **Fix it forward** in a normal PR (below). Don't revert. |
| Wrong in substance | Revert that page (step 4), or correct it in a PR. Tell the author. |
| 🚨 Synced Community Tools page (`tools/community/mariadb-ai-plugins/`, `tools/community/mariadb-shell/`) | **Don't revert**, even though the digest says to: the next weekday sync copies the page again and restores it (check with `git log -1 -- <file>`). If the change was meant seriously, make it upstream under `docs-ref/content/` ([cookbook-community-tools-sync.md](cookbook-community-tools-sync.md)). Tell the author. |
| 🚨 Other generated page (MaxScale settings reference, Plugin API) | Revert that file (step 4) and make the change in the source page or the generator. Tell the author. |
| Lost alt text, a lost anchor, or a deleted HTML comment that held a TODO | Restore it in a PR, or file a ticket for the page owner. |

**Fixing it forward in the GitHub web editor.** "Fix forward" means correcting the page as it is
now on `main`, instead of undoing the GitBook commit:

1. Open `github.com/mariadb-corporation/mariadb-docs/blob/main/<path>`, with the page's path from
   the digest entry. Not from the diff link: that page shows the file as it was in that commit.
2. Click the pencil icon (**Edit this file**), find the mistake with Cmd+F (Ctrl+F) inside the
   editor, and fix only that. Leave GitBook's reformatting alone.
3. Click **Commit changes…**, write a message such as `Fix typo from 35914be5a (GITBOOK-199)`,
   and pick **Create a new branch for this commit and start a pull request**. Don't commit
   directly to `main`: GitHub allows it, but then no PR check runs.
4. Click **Propose changes**, then **Create pull request**. Name the GitBook commit in the
   description: `Fixes 35914be5a (GITBOOK-199)`.
5. When `doc-gates` is green, choose **Rebase and merge** from the merge button's menu, confirm,
   and delete the branch.

If the fix needs a ticket (anything beyond a typo), file a DOCS ticket that names the commit.
Never fix an edit with another unreviewed GitBook edit.

### 4. Revert one page by hand

Only when step 3 says so, and one page at a time:

```bash
git switch main && git pull
git switch -c revert-<sha>-<page>
git log --oneline <sha>..HEAD -- <file>          # has anything changed the page since?
git restore --source=<sha>^ -- <file>            # no: put back the version before the edit
git show <sha> -- <file> | git apply -R --3way   # yes: undo only this commit's change
git diff HEAD                                    # --3way stages its result; plain git diff shows nothing
git commit -m "Revert <file> from <sha> (GITBOOK-<n>)"
git push -u origin HEAD
gh pr create -R mariadb-corporation/mariadb-docs --title "Revert …" \
  --body "Reverts <file> from <sha> (GITBOOK-<n>): <why>"
```

**Don't `git revert <sha>` the whole commit.** It also reverts the reformatting, which the next
editor save writes back, and any good content in the same commit. GITBOOK-198 was reverted whole
in #1625: two Enterprise Manager pages had to be restored in #1627, and GITBOOK-199 put the
reformatting back anyway. On GITBOOK-199, a whole-commit revert applies without a conflict and
still rolls the synced `license.md` back to an old version, which the Community Tools guard then
fails.

### 5. Close the loop

**Mark the entry as reviewed.** Reply in the post's thread naming the commit (for example
`9f0b0f243 reviewed: typo fixed in #1700`), or react ✅ to the post when you have looked at all
of its entries. An entry with no reply and no ✅ is still waiting.

If the edit was wrong in substance rather than form, tell its author in the thread as well, and
ask them not to re-apply it from an open GitBook change request.

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
