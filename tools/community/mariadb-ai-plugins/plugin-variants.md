---
description: >-
  The dev, sql, and contributor variants of MariaDB AI Plugins, the skills
  they include, and which of them include the mariadb-shell MCP server.
---

# Plugin Variants

<!--
  SYNCED: this page is maintained in mariadb-corporation/ai-plugins, under docs-ref/content/,
  and copied one way into mariadb-docs (tools/community/mariadb-ai-plugins/).
  Make every change in mariadb-corporation/ai-plugins. A change made in mariadb-docs or in the
  GitBook editor is overwritten by the next sync.
-->

MariaDB AI Plugins are available in three variants. They differ in the skills they include and in whether they include the MCP server. All variants are built from the same sources.

| Variant | Skills | MCP server |
| --- | --- | --- |
| `dev` | All skills, covering SQL statements, built-in functions, command-line tools, connectors, and general topics, plus all [additional skills](skills-reference/additional-skills.md) of the repository. | Yes |
| `sql` | A subset for SQL development, covering SQL statements, built-in functions, and general topics, plus the repository's skill for SQL scripts. | Yes |
| `contributor` | Skills for developing MariaDB Shell and its plugins, taken from the MariaDB Shell repository. | No |

In most cases, install the `dev` plugin.

## Availability by Harness

| Harness | `dev` | `sql` | `contributor` |
| --- | --- | --- | --- |
| Claude Code | Yes | Yes | Yes |
| Codex | Yes | Yes | Yes |
| OpenCode | Yes | Yes | Yes |
| Pi | Yes | No | No |
| Hermes Agent | Yes | Yes | Yes |

## Skill Counts

| Variant | Skills |
| --- | --- |
| `dev` | 85 |
| `sql` | 47 |
| `contributor` | 3 |

The [Skills Reference](skills-reference/) lists every skill and the variants that ship it.

## Directory Layout

In the repository, each variant lives in `<harness>/<variant>-plugin/`, for example `claude/dev-plugin/` or `codex/sql-plugin/`. Pi's plugin lives in `pi/dev-plugin/`, with the repository-root `package.json` as its manifest. In Hermes Agent, the plugin names are `mariadb-dev`, `mariadb-sql`, and `mariadb-contributor`.

<sub>_This page is licensed: GPLv2_</sub>
