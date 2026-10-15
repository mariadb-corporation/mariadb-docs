---
description: >-
  Install the MariaDB AI Plugins into Pi 1.0 or later as a Pi package, which
  registers the MCP server with Pi's built-in MCP support.
---

# Pi

Pi has no plugin marketplace, so you install the MariaDB AI Plugins repository as a Pi package. The package contains an extension that registers the `mariadb-shell` MCP server with the built-in MCP support of Pi. This requires Pi 1.0 or later. Only the `dev` plugin is available for Pi.

## Install the Plugin

Install the plugin from GitHub:

```bash
pi install git:github.com/mariadb/ai-plugins
```

Alternatively, from a local checkout of the repository, run this at the repository root:

```bash
pi install .
```

To load the skills and the extension, restart Pi, or run the following in Pi:

```text
/reload
```

The extension registers the MCP server under the name `mariadb`, and Pi connects it when the session starts. To check the connection, run the following in Pi:

```text
/mcp
```

The server is listed with the extension as its source. The `pi mcp list` command doesn't show it, because it reads only the `mcp.json` files and doesn't load extensions.

Pi makes the MCP tools available through codemode by default. In codemode, the agent writes a short script that calls the tools, and only the output of the script is added to the context. To change how the tools are exposed, select the server in `/mcp`. Pi applies that change to the current session only.

## Override the Server Entry

A `mariadb` entry in `~/.pi/agent/mcp.json`, or in `.pi/mcp.json` of a trusted project, takes precedence over the server that the extension registers. Use such an entry to keep a tool exposure, or to set environment variables for the launcher. The following command adds a global entry. Replace `<plugin>` with the `pi/dev-plugin` directory of the installed package:

```bash
pi mcp add mariadb --exposure direct -- <plugin>/scripts/mariadb-mcp-launcher.sh
```

## Upgrade from pi-mcp-adapter

Before Pi 1.0, the plugin needed the community extension `pi-mcp-adapter` and the `/mariadb-mcp-setup` command. Both are no longer used. The adapter replaces the built-in MCP support of Pi, so the `mariadb` server doesn't connect while the adapter is installed. Remove the adapter:

```bash
pi remove npm:pi-mcp-adapter
```

When Pi 1.0 finds the adapter, it turns off its built-in MCP support by adding `-builtin:mcp` to the `extensions` setting in `~/.pi/agent/settings.json`. To turn it back on, enable `mcp` under Built-in in the following screen, or remove that entry from the settings file:

```bash
pi config
```

The adapter read the `mariadb` entry that `/mariadb-mcp-setup` wrote to `~/.config/mcp/mcp.json` or `./.mcp.json`. Pi doesn't read these files, so you can delete the entry.

## Configure the MCP Server

Registering the server with Pi doesn't configure which connections and directories it may access. For that step, see [Configuring the MCP Server](../configuring-the-mcp-server/README.md).

{% hint style="warning" %}
A project-local Pi package must be approved at run time with `--approve`. Without it, the package is configured but never loaded.
{% endhint %}
