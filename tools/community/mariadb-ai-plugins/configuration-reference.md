---
description: >-
  Environment variables, file locations, and configuration files used by
  MariaDB AI Plugins, the mariadb-mcp-launcher scripts, and the mariadb-shell
  MCP server.
---

# Configuration Reference

<!--
  SYNCED: this page is maintained in mariadb-corporation/ai-plugins, under docs-ref/content/,
  and copied one way into mariadb-docs (tools/community/mariadb-ai-plugins/).
  Make every change in mariadb-corporation/ai-plugins. A change made in mariadb-docs or in the
  GitBook editor is overwritten by the next sync.
-->

## Launcher Environment Variables

The launcher scripts, `mariadb-mcp-launcher.sh` and `mariadb-mcp-launcher.cmd`, read these variables. The harness passes `MARIADB_SHELL_VERSION` from the plugin's MCP configuration; the others are unset unless you set them.

| Variable | Default | Description |
| --- | --- | --- |
| `MARIADB_SHELL_VERSION` | `26.10.3` | The minimum acceptable MariaDB Shell version. A binary on the `PATH` or in the local install directory is used when it is this version or later; otherwise the newest release is installed. |
| `MARIADB_SHELL_BIN` | — | The path of a MariaDB Shell binary to use. Skips all other resolution. |
| `MARIADB_SHELL_BINDIR` | `~/.local/bin` | Where the installer links the binary, and where the launcher looks for a local install. On Windows: `%LOCALAPPDATA%\Programs\mariadb-shell\bin`. |
| `MARIADB_SHELL_PREFIX` | — | Passed to the installer: where it unpacks releases. |
| `MARIADB_SHELL_TAG` | — | Passed to the installer: install this release tag rather than the newest. |
| `MARIADB_SHELL_PRERELEASE` | — | Unset: prefer a stable release, and install a prerelease only when no stable release exists. `1`: install a prerelease. `0`: never install a prerelease. |
| `MARIADB_SHELL_REPO` | `mariadb-corporation/mariadb-shell` | Passed to the installer: the GitHub repository to install from. |
| `MARIADB_SHELL_TOKEN` | — | A GitHub token for a private repository. The launcher also checks `GH_TOKEN`, `GITHUB_TOKEN`, and `gh auth token`, in that order. |

## LSP Launcher Environment Variables

The launcher scripts of the SQL language server, `mariadb-lsp-launcher.sh` and `mariadb-lsp-launcher.cmd`, start `mariadb-lsp`, which ships in MariaDB Shell 26.10.3 and later. They never install MariaDB Shell. They use the MariaDB Shell that the MCP launcher resolves with `MARIADB_SHELL_VERSION`, `MARIADB_SHELL_BIN`, and `MARIADB_SHELL_BINDIR`, and run the `mariadb-lsp` installed next to it. When no suitable MariaDB Shell is installed yet, they wait for the MCP launcher to install it. They also read these variables:

| Variable | Default | Description |
| --- | --- | --- |
| `MARIADB_LSP_BIN` | — | The path of a `mariadb-lsp` binary to use. Skips all other resolution. |
| `MARIADB_LSP_WAIT` | `180` | How many seconds to wait for the MCP launcher to install MariaDB Shell. `0` doesn't wait. |

## Harness-Specific Variables

| Variable | Harness | Description |
| --- | --- | --- |
| `MARIADB_DEV_PLUGIN` | OpenCode | The plugin directory, referenced by the `mcp` block in `opencode.json`. |
| `MCP_TIMEOUT` | Claude Code | How long Claude Code waits for an MCP server to connect, in milliseconds. The default is `30000`. Raise it when the first start downloads MariaDB Shell over a slow connection. Set it in the environment or in the `env` block of `~/.claude/settings.json`; a plugin can't set it. |

## File Locations

| What | Linux and macOS | Windows |
| --- | --- | --- |
| MariaDB Shell, installed by the launcher | `~/.local/bin/mariadb-shell` | `%LOCALAPPDATA%\Programs\mariadb-shell\bin\mariadb-shell.cmd` |
| The SQL language server, installed with MariaDB Shell | `~/.local/bin/mariadb-lsp` | `%LOCALAPPDATA%\Programs\mariadb-shell\bin\mariadb-lsp.cmd` |
| MariaDB Shell configuration, plugins, and secret store | `~/.mariadb-shell/` | |
| Sandbox instances | `~/.mariadb-shell/sandboxes/<port>/` | `%USERPROFILE%\MariaDB\mariadb-shell\sandboxes\<port>\` |
| Downloaded sandbox servers | `~/.local/share/mariadb-sandbox-server/` | `%LOCALAPPDATA%\Programs\mariadb-sandbox-server\` |
| Migration tooling | `~/.local/share/mariadb-migrator/<version>/` | Not available |

## MCP Registration Files

| Harness | File |
| --- | --- |
| Claude Code | The plugin's `.mcp.json`, installed with the plugin. |
| Codex | The plugin's `.mcp.json`, installed with the plugin. |
| OpenCode | The `mcp` block you merge into `opencode.json`. |
| Pi | None. The extension registers the server when it loads. A `mariadb` entry in `~/.pi/agent/mcp.json` or `.pi/mcp.json` overrides it. |
| Hermes Agent | The plugin's `mcp.json`, installed with the plugin. A `mariadb` entry under `mcp_servers` in the Hermes `config.yaml` overrides it; native Windows requires such an entry. |

## LSP Registration Files

| Harness | File |
| --- | --- |
| Claude Code | The plugin's `.lsp.json`, installed with the plugin. |
| OpenCode | The `lsp` block you merge into `opencode.json`. Adding it also turns on the built-in language servers of OpenCode. |
| Hermes Agent | An entry under `lsp.servers` that you add to the Hermes `config.yaml`, because a Hermes plugin can't register a language server. |
| Codex, Pi | None. Neither harness supports language servers. |

## MCP Server Configuration

The connections and allowed paths are set with `mariadb-shell -- mcp setup` and stored in the MariaDB Shell configuration directory. See [Configuring the MCP Server](configuring-the-mcp-server/README.md) and the [MCP server documentation](https://github.com/mariadb-corporation/mariadb-shell-plugins/blob/main/mcp_plugin/README.md#configuration-mcpsetup).

<sub>_This page is licensed: GPLv2_</sub>
