---
description: >-
  Install the MariaDB AI Plugins into Claude Code from the MariaDB plugin
  marketplace.
---

# Claude Code

<!--
  SYNCED: this page is maintained in mariadb-corporation/ai-plugins, under docs-ref/content/,
  and copied one way into mariadb-docs (tools/community/mariadb-ai-plugins/).
  Make every change in mariadb-corporation/ai-plugins. A change made in mariadb-docs or in the
  GitBook editor is overwritten by the next sync.
-->

## Install the Plugin

Add the MariaDB marketplace and install the `dev` plugin from inside Claude Code:

```text
/plugin marketplace add mariadb/ai-plugins
/plugin install dev@mariadb
```

To install a different variant, replace `dev` with `sql` or `contributor`. See [Plugin Variants](../plugin-variants.md).

## First Start

When no suitable MariaDB Shell is installed, the first start of the MCP server downloads and installs it. Claude Code waits 30 seconds for an MCP server to connect. If the download takes longer, `/mcp` lists the `mariadb` server as failed, but the installation continues in the background. When it is complete, reconnect the server from `/mcp`, or start a new session.

To give the first start more time, set `MCP_TIMEOUT` to the number of milliseconds Claude Code should wait. Set it in the environment, or in `~/.claude/settings.json`:

```json
{ "env": { "MCP_TIMEOUT": "120000" } }
```

A plugin can't change this timeout, because Claude Code reads it only from the environment.

## SQL Language Server

The `dev` and `sql` plugins also register the MariaDB SQL language server for `.sql` files, which requires MariaDB Shell 26.10.3 or later. Claude Code then receives the diagnostics of the language server after each edit of a SQL file. To also give the agent the `LSP` tool, for document symbols, hover, definitions, and references, set `ENABLE_LSP_TOOL=1` in the environment. See [SQL Language Server](../features/sql-language-server.md).

## Configure the MCP Server

The `dev` and `sql` plugins register the MCP server with Claude Code automatically. Before the agent can use the server, you must configure the connections and directories it may access. See [Configuring the MCP Server](../configuring-the-mcp-server/README.md).

## Verify the Installation

To list the installed plugins, run:

```text
/plugin
```

To check that the `mariadb` MCP server is connected, run:

```text
/mcp
```

## Update or Remove the Plugin

Use `/plugin` to update or uninstall the plugin. Removing the plugin doesn't remove MariaDB Shell or its configuration in `~/.mariadb-shell`.

<sub>_This page is licensed: GPLv2_</sub>
