---
description: >-
  An overview of MariaDB AI Plugins, the coding agents they support, and the
  versions of MariaDB and MariaDB Shell they work with.
---

# About MariaDB AI Plugins

<!--
  SYNCED: this page is maintained in mariadb-corporation/ai-plugins, under docs-ref/content/,
  and copied one way into mariadb-docs (tools/community/mariadb-ai-plugins/).
  Make every change in mariadb-corporation/ai-plugins. A change made in mariadb-docs or in the
  GitBook editor is overwritten by the next sync.
-->

MariaDB AI Plugins extend AI coding agents with knowledge about MariaDB and with access to MariaDB databases. You install a plugin through the plugin system of your coding agent. In this documentation, the coding agent is called the _harness_.

## What a Plugin Provides

Each plugin consists of the following components:

| Part | What it is | What it needs |
| --- | --- | --- |
| Skills | Reference documents that the agent reads when a request concerns MariaDB, for example on the behavior of `ALTER TABLE`, on vector indexes, on choosing a connector for Python or Java, or on moving an application from MySQL. | Nothing. Skills also work offline. |
| MCP server | A server through which the agent connects to MariaDB, for example to read your schema, run queries, analyze a slow query with `EXPLAIN`, or start a test instance. | A one-time configuration with `mcp setup`, and a MariaDB server. |
| MariaDB Shell | The MariaDB command-line shell, a port of MySQL Shell. The MCP server runs as a plugin inside it. You can also use the shell directly as a SQL client. | Installed automatically when the agent starts the MCP server for the first time. |

{% hint style="info" %}
The Model Context Protocol (MCP) is a standard interface through which AI agents call external tools. In MariaDB AI Plugins, these tools access MariaDB. You don't need to know the protocol to use the plugins.
{% endhint %}

## Supported Harnesses

| Harness | Plugin variants | Installation |
| --- | --- | --- |
| [Claude Code](https://claude.com/claude-code) | `dev`, `sql`, `contributor` | Plugin marketplace |
| [Codex](https://openai.com/codex) | `dev`, `sql`, `contributor` | Plugin marketplace |
| [OpenCode](https://opencode.ai) | `dev`, `sql`, `contributor` | Manual configuration |
| [Pi](https://pi.dev) | `dev` | Pi package |
| [Hermes Agent](https://hermes-agent.nousresearch.com/) | `dev`, `sql`, `contributor` | Agent Plugins package |
| [Cursor](https://cursor.com) | `dev`, `sql`, `contributor` | Claude Code plugin marketplace |

See [Plugin Variants](plugin-variants.md) for what each variant contains.

## MariaDB Version Baseline

The skills are written and verified against MariaDB 11.8 LTS.

## Plugin and MariaDB Shell Versions

The version number of a plugin release matches the MariaDB Shell release it requires. For example, version 26.9.5 of the plugins requires MariaDB Shell 26.9.5 or later. If no suitable version of MariaDB Shell is installed, the plugin installs the latest release. See [Release Notes](release-notes.md).

## Next Steps

{% content-ref url="installation/" %}
[installation](installation/)
{% endcontent-ref %}

<sub>_This page is licensed: GPLv2_</sub>
