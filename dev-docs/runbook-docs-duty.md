# Runbook: docs duty

The repo runs on a lot of automation: 29 workflows, three bot PRs that sync content from other
repos, five nightly digests and a release announcer. Someone has to read what it reports and act
on it, and someone has to merge the PRs that come from outside the docs team. This runbook is
for **the person on docs duty** that week.

It covers what to do, and when. The *why* stays in the cookbooks and in each workflow's header
comment, and this page links to them instead of repeating them.

## Before your first duty week

Check each of these once. If one fails, sort it out before your week starts, not on day one.

| Check | How | If it fails |
|-------|-----|-------------|
| You can merge PRs on mariadb-docs | `gh api repos/mariadb-corporation/mariadb-docs --jq .permissions` shows `"push": true` (`"maintain": true` is better) | Ask a repo admin |
| You can approve parked workflow runs | Same as above: approving needs write access | Same |
| You are in **#docs-notifications** | Open it in Slack and turn on notifications for all messages | Join the channel |
| You can open PRs on the Community Tools repos | You're in the `documentation-team` GitHub team, which has write access to `mariadb-corporation/ai-plugins` and `mariadb-corporation/mariadb-shell` | Ask the Community Tools owner (see [Contacts](#contacts)) |
| You can see the GitBook site's **Link audit** page | `app.gitbook.com/o/<org>/sites/<site>/link-audit` (the site's Broken links page) | Ask the GitBook admin (see [Contacts](#contacts)) |
| `gh` is logged in | `gh auth status` | `gh auth login` |
| You have the source repos cloned | See [Source repos for fact-checking](#source-repos-for-fact-checking) | Clone them, or ask for access |

### Source repos for fact-checking

Reviewing a GitBook edit or an outside PR often means checking a claim against the source. Clone
the repos for the products you may have to check, next to `mariadb-docs`, and register them for the
`/doc-ticket` and `/verify-claims` skills (they ask for the paths on first run and store them in the
gitignored `.claude/doc-sources.local.json`). If you open Claude Code from the parent folder, see
[cookbook-multi-repo-workspace.md](cookbook-multi-repo-workspace.md).

Public repos:

- `MariaDB/server`: Community Server. The authority for anything that isn't Enterprise-only.
- `mariadb-corporation/mariadb-connector-c`, `-j`, `-python`, `-nodejs`, `-odbc`, `-r2dbc` and
  `-cpp`: the connectors.
- `mariadb-corporation/ai-plugins`, `mariadb-shell` and `mariadb-shell-plugins`: the Community
  Tools. Their reference docs are synced into this repo, so a doc fix goes into these repos.

MaxScale, Enterprise Server and the Enterprise Operator are checked against **internal** repos.
Ask in #docs-internal for their names and for access. Use them for fact-checking only: never quote
their URLs, file paths or unreleased code in a PR, a public Jira comment or any other public text.

Credentials. The workflows use three repo secrets: `NOTIFICATIONS_WEBHOOK_URL` (the digests and
all failure notices → #docs-notifications), `SLACK_PRODUCT_RELEASES_WEBHOOK_URL` (release
announcements → #mariadb-product-releases) and `SLACK_WEBHOOK_URL` (the help-tables failure
notice, also → #docs-notifications; it rarely fires). Slack incoming webhooks don't expire, and every other workflow uses the built-in
`GITHUB_TOKEN`, so nothing here needs renewing on a schedule. If a webhook stops working (the
digests go silent, *including the Monday heartbeat*), ask in #helpdesk: IT created them.

## The weekly rhythm

| When | What | Section |
|------|------|---------|
| Every weekday morning | Read #docs-notifications and act on each bot post | [Daily](#daily-docs-notifications) |
| Every weekday | Look at the open bot PRs and outside PRs | [PRs](#prs-that-come-from-outside-the-docs-team) |
| Monday | Check that every digest posted its heartbeat | [Heartbeats](#monday-the-heartbeats) |
| First working day of the month | GitBook link audit | [Monthly](#monthly-the-gitbook-link-audit) |
| Around the 1st of the month | Dependabot's GitHub Actions PR | [Dependabot](#dependabot) |
| The 15th of the month | PDF snapshot release | [PDFs](#the-monthly-pdf-snapshot) |
| Whenever it happens | A workflow fails, GitBook doesn't sync, a skill bug is filed | [When something breaks](#when-something-breaks) |

The digests post between 06:15 and 06:40 UTC on weekdays, so they are waiting for you at the
start of the CET day. A full pass usually takes 15 to 30 minutes.

## Daily: #docs-notifications

The channel also carries Jira transition notices. Ignore those. The posts that need you are the
bot posts below. **Read only the posts since the end of the last person's pass** (the last ✅ or
thread reply is the marker).

### ✏️ "N GitBook-UI edits to review" (nightly-gitbook-edits.yml)

Every edit merged in the GitBook app lands on `main` without a PR. This digest lists each one.
**Review every entry.** The recommended way is Claude Code: in your mariadb-docs clone, run
`/gitbook-review`, or ask it to "review the GitBook edits in today's digest". It sorts GitBook's
reformatting from real changes, checks the content and proposes fixes, and asks before it opens a
PR, merges or posts in the thread. The full routine, by hand included, is in
[cookbook-gitbook-edit-review.md](cookbook-gitbook-edit-review.md). In short:

1. Find each commit by the SHA in its `diff <sha>` link, never by `GITBOOK-<n>`, which repeats
   across spaces.
2. Most of the diff is GitBook re-saving the page in its own Markdown (link forms, list markers,
   the H1, dropped HTML comments). Accept that. Review only the content changes, against the
   [style guide](style-guide.md), Title Case headings and version facts. ⚠️ findings are the
   minimum to fix, not the whole review.
3. A small mistake: **fix it forward** in a normal PR whose description names the commit
   (`Fixes 9f0b0f243 (GITBOOK-2399)`). Never fix an edit with another GitBook edit.
4. Wrong in substance: revert **that page**, never the whole commit, or correct it in a PR. Tell
   the author in the thread.
5. 🚨 **"Generated page edited by hand"**: for the MaxScale settings reference, revert that file
   and make the change in the setting's module page. For a synced Community Tools page or a
   Plugin API page, **don't revert**: the next sync PR restores it. A change meant seriously goes
   upstream. Tell the author either way.
6. Mark it done: react ✅ to the post when you have looked at all its entries, or reply in the
   thread naming the commit (`9f0b0f243 reviewed: …`), with the PR link if there is one.

### 🔗 "Heading anchors broke" (nightly-fragcheck.yml)

A heading was renamed or removed, and links to its old anchor are now dead, often from pages in
other spaces. The post lists each dead link with its file and line. Fix it in a PR: either retarget
the links or restore the heading text. If the rename was in a GitBook edit, mention it in that
edit's digest thread too.

### Unexpanded aliases (nightly-aliascheck.yml)

A `{server}/…`-style alias reached `main` without being expanded, usually through a GitBook edit or
a direct push. It publishes as a broken link. Fix it with
`python3 .claude/hooks/expand-aliases.py --write <file>` in a PR. See [link-aliases.md](link-aliases.md).

### Undated product claims (nightly-timeless.yml)

Advisory only. Someone added "currently", "coming soon" or similar. Decide whether it needs a date
("As of 13.1, …") or is fine as it is ("the currently connected clients"). The rule is "Timeless
wording" in the [style guide](style-guide.md). No action is a valid outcome.

### Release notes without a Post Download page (nightly-postdownload.yml)

A published release has no Post Download page. **This post repeats every weekday until it's fixed,
on purpose.** Add the page and its `platform/SUMMARY.md` entry, or, if that version has no
standalone package, add a `no-standalone:` register entry (the workflow header explains the
register). Usually the release-notes author owns this, so ping them first.

### 🏷️ "N open PRs with no label" (nightly-unlabeled-prs.yml)

A PR nobody has routed yet. For each one:

- Add a label: `documentation`, `release-notes`, `doc-tools` (tooling and workflows),
  `doc-infrastructure`, `cloud`, or `gridgain`.
- If it's from outside the docs team, it now belongs to you. See the next section.
- Drafts can wait until they're ready.

### ❌ Failure notices

A workflow failed. See [When something breaks](#when-something-breaks).

### Release announcements held back (announce-release-notes.yml)

`announce-release-notes.yml` posts each newly **published** release note to
#mariadb-product-releases on its own. It holds back, and reports here instead, any note that looks
like a backfill (stated release date more than 30 days old), any push with more than 10 notes, and
placeholder titles such as `<YYYY.MM.DD>`. When you see such a report:

- A placeholder title: the note went live unfinished. Tell the author.
- A genuine release that was held back by mistake: dispatch the workflow by hand with
  `before`/`after` set to the push (full SHAs) and `max_notes` or `max_age_days` raised. Leave
  `post` off first: that's a dry run that prints the messages to the run summary. Set `post` only
  once the summary looks right.
- A migration or backfill: nothing to do. That's the guard working.

Watch out for these: hiding a note and later unhiding it announces it again, and re-running a
failed run re-posts any note that run had already posted. Don't re-run it blindly.

## PRs that come from outside the docs team

The docs team reviews its own PRs as usual. The person on duty owns the rest: bot PRs,
colleagues from engineering, and outside contributors.

**Before you merge any PR:**

- Merge with `--rebase` by default (squash is allowed too):
  `gh pr merge <n> -R mariadb-corporation/mariadb-docs --rebase --delete-branch`.
- Confirm it really merged: `gh pr view <n> --json state,mergedAt`.
- If the PR is tied to a DOCS ticket, check the ticket's **"blocks" / "is blocked by"** links,
  including remote links to jira.mariadb.org. If any linked item isn't closed, don't merge: the
  docs must not go live before the release they describe.

### Bot PRs

A PR opened by a workflow triggers **none** of the `on: pull_request` checks, so its checks list
looks thin and shows `UNSTABLE`. That is expected. The verdict that counts is the **`doc-gates`**
commit status, which the generating workflow posts onto the PR.

| PR (branch) | From | Schedule | What to do |
|-------------|------|----------|------------|
| Community Tools sync (`automated/sync-community-tools-docs`) | `sync-community-tools-docs.yml`: AI Plugins and MariaDB Shell docs from their own repos | Weekdays 05:47 UTC | Skim the diff, merge if `doc-gates` is green. **Never edit a synced page in mariadb-docs, not even in this PR:** the next sync overwrites it. A fix goes upstream as a PR to `ai-plugins` or `mariadb-shell` under `docs-ref/content/`, titled `[bypass-ci] docs: …`; the Community Tools owner reviews. Full routine: [cookbook-community-tools-sync.md](cookbook-community-tools-sync.md). |
| Plugin API sync (`automated/sync-server-api-plugin-docs`) | `sync-server-api-plugin-docs.yml`: generated from the server source with doxygen | Daily 05:17 UTC | Opens when the generated pages differ from `main`: after an API change in the server, or to undo a hand edit. Merge if `doc-gates` is green. Red: look at which gate failed. A dead anchor in generated pages is usually a generator change, so ask the Plugin API owner (they have no write access here, so we merge their PRs). |
| Function skills (`agent-skills/regen-tier2-functions`) | `extract-function-skills.yml` regenerates the Tier 2 agent skills from the function reference | Mondays 04:17 UTC | Only the parts between `BEGIN/END GENERATED` markers change. Merge if `doc-gates` is green. See [agent-skills-maintenance.md](agent-skills-maintenance.md). |
| Topical skills (`agent-skills/sync-topical`) | `sync-topical-skills.yml`: vendored from MariaDB/skills | Mondays 04:37 UTC | No `doc-gates` on purpose: the content is vendored verbatim, and every gate excludes it. Check that the diff stays inside `agent-skills/topical/` and the manifest, then merge. Content bugs go upstream to MariaDB/skills. |

The error-page sync (`nightly-error-sync.yml`, 00:00 UTC) opens no PR. It pushes the regenerated
`server/reference/error-codes/` pages straight to `main`, and it posts nothing when it fails. Look
at its last run in the Actions tab once a week.

### MaxScale release docs (`maxscale-develop`)

MaxScale release docs arrive as a PR from the `maxscale-develop` branch, from the MaxScale team.
**It stays unmerged until the release is public**, which its description says. Before merging:

- Diff the pages `main` has edited since the last MaxScale release against the branch. The
  branch's "Merge branch 'main' into maxscale-develop" commits have silently reverted fixes from
  `main` before.
- You may push fixes directly to `maxscale-develop`, and that's quicker than asking the MaxScale
  team.
- `maxscale/reference/maxscale-configuration-settings.md` is **generated**. Never hand-edit it.
  See [cookbook-maxscale-settings-reference.md](cookbook-maxscale-settings-reference.md).

### PRs from colleagues and outside contributors

- **Route it.** Find the reviewer who knows the subject (Jira ticket, `git log` on the page,
  the server component owners sheet). Engineers' PRs are usually reviewed for docs form only;
  they own the facts.
- **Fork PRs.** Outside contributors work from forks. The alias workflow can't push to a fork,
  so on a fork PR **`expand-links` fails on any `{server}`-style alias**, by design. Write
  cross-space links fully expanded when you amend a fork PR. To push to the contributor's branch:
  `gh pr view <n> --json headRepository,maintainerCanModify`, then push to the fork URL. That needs
  `maintainerCanModify: true`.
- **First-time contributors** need their workflow runs approved before CI runs: the **Approve and
  run** button on the PR.
- **Help-tables PRs.** `help-tables/` feeds the server's `HELP` command. Changes there need the
  server team to agree. The generated SQL is the server team's to download and
  ship. Docs duty doesn't hand it over.
- Docs PRs from colleagues outside the team (for example a GridGain writer touching a shared page)
  just need a docs-team reviewer. Ask in #docs-internal.

### Parked runs after the alias bot pushes

When a PR contains an alias, `expand-gitbook-aliases.yml` pushes a `docs: expand GitBook aliases`
commit. GitHub's recursion guard then parks the re-triggered checks as **`action_required`**:
they sit at 0 seconds, and `gh pr checks` says *no checks reported*. That is not a CI failure,
and an empty commit is not the fix. Approve them:

```bash
gh run list -R mariadb-corporation/mariadb-docs -b <BRANCH> -L 8   # the action_required runs
gh api -X POST /repos/mariadb-corporation/mariadb-docs/actions/runs/<ID>/approve
```

A parked run that was never approved turns red with **zero jobs** once its PR is closed. That run
never ran, so don't chase it.

### Dependabot

Once a month (usually around the 1st), Dependabot opens one grouped PR that bumps the GitHub
Actions versions in `.github/workflows/`. Merge it if every check is green. Two majors are held
back on purpose in `.github/dependabot.yml`; **never delete an `ignore:` entry to make a PR go
green.** If a bump breaks a workflow, close the PR and file a DOCS ticket with the failing run.

## Monday: the heartbeats

Most nights have nothing to report, so the digests stay silent Tuesday to Friday. On Monday each
one posts even when there is nothing ("Weekend was quiet", ☕ "Weekly check-in"). **A missing
Monday post is the signal that a schedule stopped running.** Expect one from each of: unlabeled
PRs, heading anchors, timeless wording, aliases, GitBook edits and Post Download pages. If one is
missing, open the workflow in the Actions tab: a failed run, a disabled schedule (GitHub disables
crons after 60 days without a push) or no run at all.

## Monthly: the GitBook link audit

GitBook's **Link audit** ("Broken links") page lists URLs that visitors and crawlers **request**
and that return 404, ranked by hits. These aren't links in our content, so lychee can never see
them: they're mostly old KB-era URL schemes, truncated URLs, and pages moved without a redirect.

On the first working day of the month:

1. Open the Link audit page (or, with the gitbook-api MCP server, `listSiteFindings` with
   `type: ["broken-link"]`, `status: "open"`).
2. Look only at findings created since the last review.
3. **Treat GitBook's suggested redirect target as a guess, not an answer.** About one in ten was
   wrong last time: a target that 404'd itself, a hidden page with a similar name, an old-version
   page where a current one existed. Open each target before you accept it, and check it against
   `SUMMARY.md` (the URL follows the nav position, not the file path).
4. Add the redirects you accept. See [cookbook-gitbook-redirects.md](cookbook-gitbook-redirects.md).
   A finding resolves itself once a redirect for its path is live.
5. Post a one-line summary in #docs-internal: how many new findings, how many redirected.

Two warnings. The scan lags badly, so "no new findings" does not mean "no new 404s". And right
after you publish a redirect, the live URL may still 404 for a few minutes, depending on the CDN
edge you hit. Check the rule through GitBook, not the URL.

## The monthly PDF snapshot

`generate-pdfs.yml` runs at 04:00 UTC on the 15th and publishes one PDF per space as the
`docs-pdf-YYYY-MM` GitHub release. The Offline Downloads page links to the latest one. If the run
fails, re-dispatch it once. If it fails again, file a DOCS ticket with the run link. The current
month's PDFs just stay a month old meanwhile, which is not urgent.

## When something breaks

### A workflow failed (❌ in #docs-notifications)

1. Open the run. Read the failing step's log:
   `gh run view --job <job-id> --log` (`--log-failed` sometimes truncates).
2. **Tooling failure or content finding?** A content finding on a PR is the author's to fix. A
   tooling failure (a crashed script, a network timeout, a missing tool) is yours.
3. A network blip or a runner hiccup: re-run it once. **Exception:** don't blindly re-run
   `announce-release-notes.yml`, because it would re-post announcements.
4. Anything you can't fix in half an hour: file a DOCS ticket with the run link, label it
   `doc-tools`, and leave it for the next docs-team meeting. **Don't edit a workflow under time pressure.**
   Most workflow headers explain choices that look wrong but aren't.

### A merged change doesn't show up on the site

GitBook imports each space from `main` within about a minute; a full import of a large space can
take 15 to 20 minutes. If it's still missing after that:

- Look at the merge commit's **GitBook (`<space>`)** commit status. `success` means GitBook
  imported it. No status at all usually means GitBook dropped the event.
- **The only reliable fix is another real content commit to the same space's directory.** A
  commit that touches only `.github/` or `dev-docs/` doesn't trigger GitBook at all.
- **Never call the GitBook `importGitRepository` API.** Without the exact project directory it
  imports the whole repo into the space, and once it emptied the Server space.
- **A failed import rolls the whole space back to its previous revision.** It's stale, not half
  applied. GitBook's error names a file, but that file is usually innocent.
- Escalate to GitBook in #ext-docs-gitbook (a Slack Connect channel) with the commit, the time and
  the status, if a new commit doesn't fix it.

### A cross-space link goes to the GitBook login page

A PR that adds a page *and* links to it from another space in the same merge can publish that link
unresolved. Check after any such merge:

```bash
curl -s https://mariadb.com/docs/<page> | grep -o 'href="https://app.gitbook.com[^"]*"'
```

Any hit is broken. Fix it with a small real change to the *linking* file in a follow-up PR: for
example, change the URL form from `/o/<org>/s/<space>/…` to `/s/<space>/…`. GitBook resolves it
on the next import.

### A Claude skill bug is filed

Skill bugs arrive as DOCS tickets labeled `claude-skill-bug` (via `/skill-bug`). They are rare.

- **Reproduce it first.** Most "bugs" are an unconfigured MCP connection or a missing local tool.
- **A one-line fix** (a wrong path, a stale flag): fix it in a PR, as with any other change.
- **Anything bigger:** comment on the ticket with what you found, and leave it for the next docs-team meeting.
  Nobody's work is blocked by a skill: the manual way still works.

## Escalation

Most things can wait for the next docs-team meeting. Collect them during the week. Raise it at once
in #docs-internal, and mention the team, only if:

- the site, or a whole space, is down or serving wrong content, or
- a workflow is posting to a company-wide channel when it shouldn't (for example a wrong release
  announcement).

### Contacts

People change roles, so this table is the only place in the runbook that names anyone. Last
checked: 2026-11-23.

| For | Ask |
|-----|-----|
| GitBook site settings, admin-gated actions | Daniel Bartholomew (GitBook admin) |
| Community Tools repos (`ai-plugins`, `mariadb-shell`) | Mike Zinner |
| The generated Plugin API docs (`sync-server-api-plugin-docs.yml`) | Georgi Kodinov |
| MaxScale release docs (`maxscale-develop`), the MaxScale settings generator | Johan Wikman |
| Help tables (`help-tables/`, the SQL shipped with the server) | the server team, usually Oleksandr Byelkin |
| Release announcements to #mariadb-product-releases | Adam Luciano (requested them) |
| Webhooks, repo secrets | #helpdesk |

## Handing over

At the end of your week, post in #docs-internal:

- digest posts still waiting for review (with links),
- PRs you're in the middle of, and what each one is waiting for,
- anything you filed or escalated.

The next person starts from that post and the last ✅ in #docs-notifications.

## Keeping this runbook current

This page is only useful while it matches the workflows. Three rules keep it that way:

1. **Same PR.** A PR that adds, removes or renames a workflow, or changes what one posts or when,
   updates this page and the [workflow index](#workflow-index) below. Reviewers: ask for it.
2. **Roles, not names.** The body talks about "the person on duty" and "the GitBook admin". Names
   live only in [Contacts](#contacts), with the date they were last checked.
3. **Fix it on duty.** If something here was wrong or missing during your week, fix it in a PR
   before you hand over. You're the one who just found out.

Once a quarter, the docs team lead asks someone to re-check the contacts table and the index
against `.github/workflows/`:

```bash
ls .github/workflows/*.yml | xargs -n1 basename | while read -r f; do
  grep -q "$f" dev-docs/runbook-docs-duty.md || echo "not in the runbook: $f"
done
```

## Workflow index

Every workflow in `.github/workflows/`, and whether docs duty has to act on it.

| Workflow | Runs | Docs duty |
|----------|------|-----------|
| `announce-release-notes.yml` | Push to `main` | Held-back notes and failures land in #docs-notifications |
| `codespell.yml` | PR | No: the PR author fixes it |
| `community-tools-guard.yml` | PR touching `tools/community/` | No: tells the author to fix upstream |
| `desccheck-pr.yml` | PR | No: the PR author fixes it |
| `doc-gates.yml` | Called by the bot-PR workflows | Its `doc-gates` status is what you merge bot PRs on |
| `doc-lint-test.yml` | PR | Only when it fails on a PR that didn't touch tooling |
| `expand-gitbook-aliases.yml` | PR | Approve parked runs after its push |
| `extract-function-skills.yml` | Mondays 04:17 UTC | Merge its bot PR |
| `fragcheck-pr.yml` | PR | No: the PR author fixes it |
| `generate-help-tables.yml` | Push to `main`, PR | Failures in #docs-notifications (rare) |
| `generate-pdfs.yml` | The 15th, 04:00 UTC | Re-dispatch once on failure |
| `includecheck-pr.yml` | PR | No: the PR author fixes it |
| `link-check-pr.yml` | PR | No: the PR author fixes it |
| `mermaidcheck-pr.yml` | PR | No: the PR author fixes it |
| `navcheck-pr.yml` | PR | No: the PR author fixes it |
| `nightly-aliascheck.yml` | Weekdays 06:30 UTC | Fix reported aliases |
| `nightly-error-sync.yml` | Daily 00:00 UTC | Check its last run once a week: it posts nothing |
| `nightly-fragcheck.yml` | Weekdays 06:20 UTC | Fix reported anchors |
| `nightly-gitbook-edits.yml` | Weekdays 06:35 UTC | Review every entry |
| `nightly-postdownload.yml` | Weekdays 06:40 UTC | Chase the missing pages |
| `nightly-timeless.yml` | Weekdays 06:25 UTC | Judge each hit |
| `nightly-unlabeled-prs.yml` | Weekdays 06:15 UTC | Label and route |
| `postdownload-pr.yml` | PR | No: the PR author fixes it |
| `railroadcheck-pr.yml` | PR | No: the PR author fixes it |
| `shrinkcheck-pr.yml` | PR | No: the PR author fixes it |
| `sync-community-tools-docs.yml` | Weekdays 05:47 UTC | Merge its bot PR |
| `sync-server-api-plugin-docs.yml` | Daily 05:17 UTC | Merge its bot PR |
| `sync-topical-skills.yml` | Mondays 04:37 UTC | Merge its bot PR |
| `versioncheck-pr.yml` | PR | No: the PR author fixes it |
