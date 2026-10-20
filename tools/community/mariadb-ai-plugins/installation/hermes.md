---
description: >-
  Install the MariaDB AI Plugins into Hermes Agent as portable Agent Plugins
  packages, directly from the plugin folders of the repository.
---

# Hermes Agent

<!--
  SYNCED: this page is maintained in mariadb-corporation/ai-plugins, under docs-ref/content/,
  and copied one way into mariadb-docs (tools/community/mariadb-ai-plugins/).
  Make every change in mariadb-corporation/ai-plugins. A change made in mariadb-docs or in the
  GitBook editor is overwritten by the next sync.
-->

Hermes Agent has no MariaDB plugin marketplace, so you install each plugin directly from its folder in the repository. Every plugin folder is a portable Agent Plugins v1 package with a root `plugin.json` and a `skills/` directory. The `dev` and `sql` plugins also contain a root `mcp.json` that declares the `mariadb-shell` MCP server. Hermes loads these packages without any additional code.

| Variant | Folder | Hermes plugin name |
| ------- | ------ | ------------------ |
| `dev` | `hermes/dev-plugin` | `mariadb-dev` |
| `sql` | `hermes/sql-plugin` | `mariadb-sql` |
| `contributor` | `hermes/contributor-plugin` | `mariadb-contributor` |

## Install the Plugin

Install the `dev` plugin from GitHub:

```bash
hermes plugins install mariadb/ai-plugins#hermes/dev-plugin --enable
```

To install the `sql` or `contributor` plugin, replace `#hermes/dev-plugin` with `#hermes/sql-plugin` or `#hermes/contributor-plugin`.

See [Plugin Variants](../plugin-variants.md) for the differences between the variants.

The `--enable` option enables the plugin after installation. Hermes installs portable packages disabled. If you omit the option, enable the plugin afterwards with `hermes plugins enable mariadb-dev`.

After the installation, start a new Hermes session. Hermes connects MCP servers when a session starts.

## Configure the MCP Server

The `mcp.json` file of the `dev` and `sql` plugins registers the MCP server under the name `mariadb`, so you don't need to register it separately. Hermes runs the launcher script of the plugin, which starts MariaDB Shell as the MCP server. The tools are available to the model as `mcp__mariadb__<tool>`, for example `mcp__mariadb__db_list_connections`.

Before the agent can use the server, you must configure the connections and directories it may access. See [Configuring the MCP Server](../configuring-the-mcp-server/README.md).

### Windows

The `mcp.json` file can't select a launcher per operating system, and its `.sh` launcher requires a POSIX shell. On native Windows, add a server with the same name to the Hermes `config.yaml` file in `%LOCALAPPDATA%\hermes`. A server in `config.yaml` replaces the plugin's server of the same name. The `command` is the `mariadb-mcp-launcher.cmd` script of the installed plugin. The following example is for the `dev` plugin; replace `<you>` with your user name:

```yaml
mcp_servers:
  mariadb:
    command: "C:\\Users\\<you>\\AppData\\Local\\hermes\\plugins\\mariadb-dev\\scripts\\mariadb-mcp-launcher.cmd"
    args: []
```

## Verify the Installation

To check that the plugin is installed and enabled, run:

```bash
hermes plugins list
```

Hermes makes the skills available through its `skills_list` and `skill_view` tools, under a namespace that it derives from the plugin, for example `agent-plugin-mariadb-dev-<hash>:mariadb-create-table`. The skills are read-only.

## Update or Remove the Plugin

To update the plugin, run:

```bash
hermes plugins update mariadb-dev
```

To remove the plugin, run:

```bash
hermes plugins remove mariadb-dev
```

Removing the plugin doesn't remove MariaDB Shell or its configuration in `~/.mariadb-shell`.

<sub>_This page is licensed: GPLv2_</sub>
