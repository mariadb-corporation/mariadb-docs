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
[Securing Communications](https://app.gitbook.com/o/diTpXxF5WsbHqTReoBsS/s/3VYeeVGUV4AMqrA3zwy7/galera-security/securing-communications-in-galera-cluster)
```

The `expand-gitbook-aliases.yml` Action rewrites `https://app.gitbook.com/o/diTpXxF5WsbHqTReoBsS/s/3VYeeVGUV4AMqrA3zwy7` to the full
`https://app.gitbook.com/...` URL on the PR branch automatically. The expansion is committed
back to the PR branch as `docs: expand GitBook aliases` from the `github-actions` bot — expect
that follow-up commit to appear shortly after opening or pushing to a PR.

## Available aliases

| Alias | Target space |
|-------|--------------|
| `https://app.gitbook.com/o/diTpXxF5WsbHqTReoBsS/s/gmXC0YXB3rRhXvpg5mb1` | Home / Landing |
| `https://app.gitbook.com/o/diTpXxF5WsbHqTReoBsS/s/SsmexDFPv2xG2OTyO5yV` | MariaDB Server |
| `https://app.gitbook.com/o/diTpXxF5WsbHqTReoBsS/s/0pSbu5DcMSW4KwAkUcmX` | MariaDB MaxScale |
| `https://app.gitbook.com/o/diTpXxF5WsbHqTReoBsS/s/3VYeeVGUV4AMqrA3zwy7` | Galera Cluster |
| `https://app.gitbook.com/o/diTpXxF5WsbHqTReoBsS/s/rBEU9juWLfTDcdwF3Q14` | Analytics (ColumnStore) |
| `https://app.gitbook.com/o/diTpXxF5WsbHqTReoBsS/s/2I4jZ8pGq8bT4w5n3q6r` | ColumnStore |
| `https://app.gitbook.com/o/diTpXxF5WsbHqTReoBsS/s/CjGYMsT2MVP4nd3IyW2L` | Connectors (Java, ODBC, etc.) |
| `https://app.gitbook.com/o/diTpXxF5WsbHqTReoBsS/s/aEnK0ZXmUbJzqQrTjFyb` | SkySQL |
| `https://app.gitbook.com/o/diTpXxF5WsbHqTReoBsS/s/JqgUabdZsoY5EiaJmqgn` | MariaDB Enterprise Platform |
| `https://app.gitbook.com/o/diTpXxF5WsbHqTReoBsS/s/vPz15Lz0Iw3P3yKR3Prd` | MariaDB Cloud |
| `https://app.gitbook.com/o/diTpXxF5WsbHqTReoBsS/s/kuTXWg0NDbRx6XUeYpGD` | Tools |
| `https://app.gitbook.com/o/diTpXxF5WsbHqTReoBsS/s/aEnK0ZXmUbJzqQrTjFyb` | Release Notes |
| `https://app.gitbook.com/o/diTpXxF5WsbHqTReoBsS/s/WCInJQ9cmGjq1lsTG91E/about/readme` | General Resources |

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
