---
description: >-
  Install the MariaDB AI Plugins into OpenCode by registering the MCP server
  and linking the skills directory.
---

# OpenCode

<!--
  SYNCED: this page is maintained in mariadb-corporation/ai-plugins, under docs-ref/content/,
  and copied one way into mariadb-docs (tools/community/mariadb-ai-plugins/).
  Make every change in mariadb-corporation/ai-plugins. A change made in mariadb-docs or in the
  GitBook editor is overwritten by the next sync.
-->

OpenCode doesn't have a plugin marketplace. Instead, you register the MCP server in your OpenCode configuration and make the skills available to OpenCode yourself.

## Get the Plugin

Clone the repository, or copy its `opencode/dev-plugin/` directory, to a stable location:

```bash
git clone https://github.com/mariadb/ai-plugins.git
```

## Register the MCP Server

1. Merge the `mcp` block from `opencode/dev-plugin/opencode.json` into your project's `opencode.json`, or into the global `~/.config/opencode/opencode.json`.
2. Point `MARIADB_DEV_PLUGIN` at the plugin directory:

   ```bash
   export MARIADB_DEV_PLUGIN=/path/to/ai-plugins/opencode/dev-plugin
   ```

   On Windows, write the path with forward slashes, for example `C:/path/to/ai-plugins/opencode/dev-plugin`. OpenCode inserts the value into the JSON text of the configuration before it parses it, so backslashes make the configuration invalid.

## Make the Skills Discoverable

OpenCode loads skills one directory deep from `.opencode/skills/`, `~/.config/opencode/skills/`, `.claude/skills/`, and `.agents/skills/`. Link the plugin's `skills/` directory into one of them:

{% tabs %}
{% tab title="Global" %}
```bash
ln -s "$MARIADB_DEV_PLUGIN/skills" ~/.config/opencode/skills/mariadb
```
{% endtab %}

{% tab title="Project" %}
```bash
ln -s "$MARIADB_DEV_PLUGIN/skills" .opencode/skills/mariadb
```
{% endtab %}
{% endtabs %}

## Register the Language Server

The `lsp` block of `opencode/dev-plugin/opencode.json` registers the MariaDB SQL language server for `.sql` files. Merge it into your `opencode.json` next to the `mcp` block. The language server requires MariaDB Shell 26.10.3 or later. See [SQL Language Server](../features/sql-language-server.md).

OpenCode turns off all language servers while its configuration has no `lsp` key. Adding the block also turns on the built-in language servers of OpenCode. To keep them off, don't merge the block.

OpenCode gives a language server 45 seconds to start, and skips a server that doesn't start in time for the rest of the session. The limit can't be configured. On the first start, the language server waits for the MCP server's launcher to download MariaDB Shell. If the download takes longer than 45 seconds, restart OpenCode when it's complete.

## Configure the MCP Server

Before the agent can use the MCP server, you must configure the connections and directories it may access. See [Configuring the MCP Server](../configuring-the-mcp-server/README.md).

<sub>_This page is licensed: GPLv2_</sub>
