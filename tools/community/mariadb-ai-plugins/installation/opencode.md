---
description: >-
  Install the MariaDB AI Plugins into OpenCode by registering the MCP server
  and linking the skills directory.
---

# OpenCode

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

## Configure the MCP Server

Before the agent can use the MCP server, you must configure the connections and directories it may access. See [Configuring the MCP Server](../configuring-the-mcp-server/README.md).
