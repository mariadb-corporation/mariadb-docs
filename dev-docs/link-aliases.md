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

The `expand-gitbook-aliases.yml` Action rewrites `{galera}` to the full
`https://app.gitbook.com/...` URL on the PR branch automatically. The expansion is committed
back to the PR branch as `docs: expand GitBook aliases` from the `github-actions` bot — expect
that follow-up commit to appear shortly after opening or pushing to a PR.

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
  after a Markdown link's `](`, after a content-ref's `url="`, or after an HTML `href="`.
  An alias-looking string anywhere else — in prose, in a table cell, in a code sample — is
  left exactly as written. So `` `{server}` `` in a sentence is safe, and the ColumnStore
  CMAPI pages can keep documenting `https://{server}:{port}/cmapi/{version}/{route}/{command}`,
  where `{server}` is a hostname placeholder rather than a docs alias.
- Aliases **do work on landing pages.** Every space and section landing page is a
  `README.md`, and the Action used to skip those by filename, so an alias written there was
  silently left unexpanded — GitBook then read it as a repository path and emitted a
  plausible-looking `github.com/...` URL that 404s. Fixed in DOCS-6481.
- A few files are intentionally **excluded from alias expansion** by the Action, because they
  discuss the alias mechanism rather than use it: the repository's own `README.md` and
  `pdf/README.md`, `CONTRIBUTING.md`, everything under `dev-docs/` and `.claude/`, and
  `general-resources/about/readme/about-links.md`. Don't rely on alias expansion in those —
  write the raw `https://app.gitbook.com/o/<org>/s/<space>/path` URL instead.
