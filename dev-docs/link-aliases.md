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
| `{skysql}` | SkySQL |
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
- A few files are intentionally **excluded from alias expansion** by the Action:
  `README.md`, `CONTRIBUTING.md`, and `general-resources/about/readme/about-links.md`.
  Don't rely on alias expansion in those.
