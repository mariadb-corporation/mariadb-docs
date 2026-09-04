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
- **Aliases are not expanded on a pull request from a fork** — the `expand-links` check
  reports every alias in a link target, with its file and line, and fails. Two things stop the
  auto-commit there: `GITHUB_TOKEN` is read-only on a `pull_request` from a fork whatever the
  workflow's `permissions` block says, and `origin` is this repository rather than the fork, so
  a push would create a contributor-named branch here and leave the fork branch untouched
  (DOCS-6589). If you work from a fork, either write the full
  `https://app.gitbook.com/o/<org>/s/<space>/...` URL yourself, or push the branch to this
  repository instead, where expansion runs normally.
