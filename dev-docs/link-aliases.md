# Cross-space link aliases

Linking between GitBook spaces by raw URL is brittle — the URLs contain opaque GitBook IDs.
This repo uses **link aliases** instead: write `{alias}/path/to/page` and a CI Action expands it
to the real URL when the PR is merged.

## Syntax

```
[Link Text]({alias}/path/to/page)
```

Example:

```
[Securing Communications]({galera}/galera-security/securing-communications-in-galera-cluster)
```

A reference-style link definition works the same way:

```
[Securing Communications]: {galera}/galera-security/securing-communications-in-galera-cluster
```

The `expand-gitbook-aliases.yml` Action rewrites `{galera}` to the full
`https://app.gitbook.com/...` URL on the PR branch automatically. The expansion is committed
back to the PR branch as `docs: expand GitBook aliases` from the `github-actions` bot — expect
that follow-up commit to appear shortly after opening or pushing to a PR. It touches only the
Markdown files your own PR changes, so that follow-up commit never edits a file you didn't.

## Available aliases

| Alias | Target space |
|-------|--------------|
| `{home}` | Home / Landing |
| `{server}` | MariaDB Server |
| `{maxscale}` | MariaDB MaxScale |
| `{galera}` | Galera Cluster |
| `{analytics}` | Analytics (ColumnStore) |
| `{columnstore}` | ColumnStore |
| `{connectors}` | Connectors (Java, ODBC, etc.) |
| `{skysql}` | MariaDB Cloud (legacy alias — SkySQL was renamed MariaDB Cloud) |
| `{platform}` | MariaDB Enterprise Platform |
| `{mariadb-cloud}` | MariaDB Cloud |
| `{tools}` | Tools |
| `{release-notes}` | Release Notes |
| `{general-resources}` | General Resources |

## Rules for agents

- **Use an alias for any cross-space link.** Use a relative `.md` path for links within the
  same space.
- **Never expand an alias by hand**, and never rewrite an already-expanded
  `app.gitbook.com` URL back into the source. The Action owns that transform.
- **Aliases don't resolve in a local editor, the GitHub UI, or the GitHub app** — that's
  expected. They work on the published site after expansion.
- **Don't validate aliased links locally.** The link-checker (lychee) is configured to skip
  anything containing `{` (and its `%7B` encoding), so aliases never trip CI.
- **Only a link target is expanded.** The Action rewrites an alias when it appears directly
  after a Markdown link's `](`, after a reference-style link definition's `]:`, after a
  content-ref's `url="`, or after an HTML `href="`. An alias-looking string anywhere else — in
  prose, in a table cell, in a code sample — is left exactly as written. So `` `{server}` ``
  in a sentence is safe, and the ColumnStore CMAPI pages can keep documenting
  `https://{server}:{port}/cmapi/{version}/{route}/{command}`, where `{server}` is a hostname
  placeholder rather than a docs alias.
- **Use one of the aliases in the table above — a name the Action doesn't know now fails CI.**
  Anything still sitting in a link target after the expansion runs is reported by the
  `expand-links` check with its file and line, because an unknown alias cannot be caught later:
  GitBook publishes it as a plausible-looking `github.com/...` URL that 404s, and lychee skips
  it. If a new space needs an alias, add it to `expand-gitbook-aliases.yml`.
- Aliases **do work on landing pages.** Every space and section landing page is a
  `README.md`, and the Action used to skip those by filename, so an alias written there was
  silently left unexpanded — GitBook then read it as a repository path and emitted a
  plausible-looking `github.com/...` URL that 404s. Fixed in DOCS-6481.
- A few files are intentionally **excluded from alias expansion** by the Action, because they
  discuss the alias mechanism rather than use it: the repository's own `README.md` and
  `pdf/README.md`, `CONTRIBUTING.md`, everything under `dev-docs/` and `.claude/`, and
  `general-resources/about/readme/about-links.md`. Don't rely on alias expansion in those —
  write the raw `https://app.gitbook.com/o/<org>/s/<space>/path` URL instead.
- **Expansion is scoped to your PR's own changed Markdown files.** It used to walk the whole
  tree, so any alias that had reached `main` unexpanded was rewritten by whichever PR opened
  next, handing that author a collateral edit to someone else's file (DOCS-6401). Two things
  follow. Your PR is never blamed for an alias elsewhere in the repo — and, conversely, an
  alias that lands on `main` without passing through a PR is never expanded and never
  reported, because no PR changed that file. **So don't commit an aliased link directly to
  `main`**: GitBook will publish the alias verbatim as a `github.com/...` URL that 404s. If
  one gets there anyway, touching the file in any PR expands it.
- **The bot's own expansion commit is never checked automatically, and that needs a manual
  approve.** The push fires a `synchronize` event, GitHub attributes the resulting runs to
  `github-actions[bot]`, and parks every one of them in `action_required` — created, but not
  started. So the green checks on a PR whose last commit is `docs: expand GitBook aliases`
  belong to the commit *before* it. Unblock them by hand:

  ```sh
  gh run list -R mariadb-corporation/mariadb-docs -b <BRANCH> -L 8
  gh api -X POST /repos/mariadb-corporation/mariadb-docs/actions/runs/<ID>/approve
  ```

  This is GitHub's recursion guard on `GITHUB_TOKEN`-triggered events, **not** a repository
  setting, so there is no dropdown that turns it off. The repository's approval option is
  *Require approval for first-time contributors*, which governs fork pull requests and cannot
  reach a same-repository push; and the parking hits 100% of bot-triggered `pull_request` runs
  across every branch and month on record, where a contributor policy would spare an identity
  that has commits merged — which `github-actions[bot]` does (DOCS-6593). Two symptoms not to
  misread. `gh pr checks` prints **no checks reported on the branch** and `statusCheckRollup`
  comes back `[null, null]`; that is the parked state, not a tooling glitch. And a parked run
  that is never approved flips to **failure with zero jobs** once the PR is closed or the branch
  deleted, so a red run of that shape on an abandoned branch never ran and is nothing to chase.
