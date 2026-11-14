---
description: >-
  Install the MariaDB AI Plugins into Hermes Agent from the Hermes plugin
  catalog, or directly from the plugin folders of the repository.
---

# Hermes Agent

<!--
  SYNCED: this page is maintained in mariadb-corporation/ai-plugins, under docs-ref/content/,
  and copied one way into mariadb-docs (tools/community/mariadb-ai-plugins/).
  Make every change in mariadb-corporation/ai-plugins. A change made in mariadb-docs or in the
  GitBook editor is overwritten by the next sync.
-->

The `dev` plugin is listed in the [Hermes plugin catalog](https://hermes-agent.nousresearch.com/docs/plugins/mariadb-dev), together with `mariadb-guard`, a companion plugin that keeps database passwords off the command line. Every plugin folder in the repository is a portable Agent Plugins v1 package with a root `plugin.json` and a `skills/` directory. The `dev` and `sql` plugins also contain a root `mcp.json` that declares the `mariadb-shell` MCP server. Hermes loads these packages without any additional code.

| Variant | Folder | Hermes plugin name | In the catalog |
| ------- | ------ | ------------------ | -------------- |
| `dev` | `hermes/dev-plugin` | `mariadb-dev` | Yes |
| `sql` | `hermes/sql-plugin` | `mariadb-sql` | No |
| `contributor` | `hermes/contributor-plugin` | `mariadb-contributor` | No |
| Guard | `hermes/guard-plugin` | `mariadb-guard` | Yes |

See [Plugin Variants](../plugin-variants.md) for the differences between the variants.

## Install the Plugin

Install the `dev` plugin and the guard from the Hermes plugin catalog:

```bash
hermes plugins install mariadb-dev --enable
hermes plugins install mariadb-guard --enable
```

The catalog lists one package per product, so the `sql` plugin, a subset of `dev`, isn't in it. Install it from the repository, as described in [Install from the Repository](#install-from-the-repository). In Hermes Desktop, the plugins are also available under **Capabilities** → **Plugins** → **Browse**; search for `mariadb`.

The `--enable` option enables the plugin after installation. Hermes installs portable packages disabled. If you omit the option, enable the plugin afterwards with `hermes plugins enable mariadb-dev`.

The `mariadb-guard` plugin blocks the MariaDB and MySQL command-line clients wherever an MCP tool does the same job, so that no database password appears on a command line. It is a separate plugin because Hermes runs hooks only from Python plugins.

After the installation, start a new Hermes session. Hermes connects MCP servers when a session starts.

### Install from the Repository

A catalog install checks out the release that the catalog pins. To install the latest state of the `main` branch instead, or the `sql` or `contributor` plugin, which aren't in the catalog, install the plugin from its folder in the repository:

```bash
hermes plugins install mariadb/ai-plugins#hermes/dev-plugin --enable
```

To install another plugin, replace `#hermes/dev-plugin` with `#hermes/sql-plugin`, `#hermes/contributor-plugin` or `#hermes/guard-plugin`.

## Configure the MCP Server

The `mcp.json` file of the `dev` and `sql` plugins registers the MCP server under the name `mariadb`, so you don't need to register it separately. Hermes runs the launcher script of the plugin, which starts MariaDB Shell as the MCP server. The tools are available to the model as `mcp__mariadb__<tool>`, for example `mcp__mariadb__db_list_connections`.

When no suitable MariaDB Shell is installed, the launcher installs the release that the plugin was tested with and verifies it against checksums that the plugin carries. Unlike the plugins for the other harnesses, it doesn't install the newest release. See [Configuration Reference](../configuration-reference.md#hermes-agent).

Before the agent can use the server, you must configure the connections and directories it may access. See [Configuring the MCP Server](../configuring-the-mcp-server/README.md).

### Windows

The `mcp.json` file can't select a launcher per operating system, and its `.sh` launcher requires a POSIX shell. On native Windows, add a server with the same name to the Hermes `config.yaml` file in `%LOCALAPPDATA%\hermes`. A server in `config.yaml` replaces the plugin's server of the same name. The `command` is the `mariadb-mcp-launcher.cmd` script of the installed plugin. The following example is for the `dev` plugin; replace `<you>` with your user name:

```yaml
mcp_servers:
  mariadb:
    command: "C:\\Users\\<you>\\AppData\\Local\\hermes\\plugins\\mariadb-dev\\scripts\\mariadb-mcp-launcher.cmd"
    args: []
```

## Register the Language Server

A Hermes plugin can't register a language server. To use the MariaDB SQL language server for `.sql` files, add it to the Hermes `config.yaml` file. The language server requires MariaDB Shell 26.10.3 or later. See [SQL Language Server](../features/sql-language-server.md). The following example is for the `dev` plugin:

```yaml
lsp:
  warmup_timeout: 240
  servers:
    mariadb:
      command: ["~/.hermes/plugins/mariadb-dev/scripts/mariadb-lsp-launcher.sh"]
      extensions: [".sql"]
      language_id: "sql"
```

On native Windows, the `command` is the `mariadb-lsp-launcher.cmd` script of the installed plugin.

The `warmup_timeout` setting gives the language server time to start the first time, when it waits for the MCP server's launcher to install MariaDB Shell. Without it, Hermes waits five seconds and then skips the language server for the rest of the session. Hermes runs language servers only in git repositories, and custom ones only in trusted workspaces: the worktree that you start Hermes in, and the directories listed under `lsp.trusted_workspaces`.

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

A plugin installed from the catalog updates to the release that the catalog pins next. In Hermes Desktop, the **Plugins** tab shows an **Update** button when a new release is pinned.

To remove the plugin, run:

```bash
hermes plugins remove mariadb-dev
```

Removing the plugin doesn't remove MariaDB Shell or its configuration in `~/.mariadb-shell`.

<sub>_This page is licensed: GPLv2_</sub>
