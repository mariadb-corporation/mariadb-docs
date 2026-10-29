---
description: >-
  Install the MariaDB AI Plugins into Cursor from the MariaDB plugin
  marketplace, which Cursor shares with Claude Code.
---

# Cursor

<!--
  SYNCED: this page is maintained in mariadb-corporation/ai-plugins, under docs-ref/content/,
  and copied one way into mariadb-docs (tools/community/mariadb-ai-plugins/).
  Make every change in mariadb-corporation/ai-plugins. A change made in mariadb-docs or in the
  GitBook editor is overwritten by the next sync.
-->

Cursor installs Claude Code plugins, so it uses the same MariaDB plugin marketplace and the same plugins as [Claude Code](claude-code.md). Cursor installs the plugins into its own directory. Claude Code doesn't need to be installed.

## Install the Plugin

1. In Cursor, click **Customize**, and then click **+ Add Marketplace**.
2. Enter the marketplace URL, and add the marketplace:

   ```text
   https://github.com/mariadb/ai-plugins
   ```
3. Click **Add** next to the `dev` plugin.

To install a different variant, add `sql` or `contributor` instead of `dev`. See [Plugin Variants](../plugin-variants.md).

## Configure the MCP Server

The `dev` and `sql` plugins register the MCP server with Cursor automatically. Before the agent can use the server, you must configure the connections and directories it may access. See [Configuring the MCP Server](../configuring-the-mcp-server/README.md).

## Verify the Installation

To check that the plugin is installed, click **Customize** and look for the plugin in the list. To check that the skills are loaded, see [Verify the Skills Are Loaded](README.md#verify-the-skills-are-loaded).

## Remove the Plugin

Removing the plugin from Cursor doesn't remove MariaDB Shell or its configuration in `~/.mariadb-shell`.

<sub>_This page is licensed: GPLv2_</sub>
