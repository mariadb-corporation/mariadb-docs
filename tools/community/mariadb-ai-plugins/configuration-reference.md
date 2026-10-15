---
description: >-
  Environment variables, file locations, and configuration files used by
  MariaDB AI Plugins, the mariadb-mcp-launcher scripts, and the mariadb-shell
  MCP server.
---

# Configuration Reference

## Launcher Environment Variables

The launcher scripts, `mariadb-mcp-launcher.sh` and `mariadb-mcp-launcher.cmd`, read these variables. The harness passes `MARIADB_SHELL_VERSION` from the plugin's MCP configuration; the others are unset unless you set them.

| Variable | Default | Description |
| --- | --- | --- |
| `MARIADB_SHELL_VERSION` | `26.9.5` | The minimum acceptable MariaDB Shell version. A binary on the `PATH` or in the local install directory is used when it is this version or later; otherwise the newest release is installed. |
| `MARIADB_SHELL_BIN` | — | The path of a MariaDB Shell binary to use. Skips all other resolution. |
| `MARIADB_SHELL_BINDIR` | `~/.local/bin` | Where the installer links the binary, and where the launcher looks for a local install. On Windows: `%LOCALAPPDATA%\Programs\mariadb-shell\bin`. |
| `MARIADB_SHELL_PREFIX` | — | Passed to the installer: where it unpacks releases. |
| `MARIADB_SHELL_TAG` | — | Passed to the installer: install this release tag rather than the newest. |
| `MARIADB_SHELL_PRERELEASE` | — | Unset: prefer a stable release, and install a prerelease only when no stable release exists. `1`: install a prerelease. `0`: never install a prerelease. |
| `MARIADB_SHELL_REPO` | `mariadb-corporation/mariadb-shell` | Passed to the installer: the GitHub repository to install from. |
| `MARIADB_SHELL_TOKEN` | — | A GitHub token for a private repository. The launcher also checks `GH_TOKEN`, `GITHUB_TOKEN`, and `gh auth token`, in that order. |

## Harness-Specific Variables

| Variable | Harness | Description |
| --- | --- | --- |
| `MARIADB_DEV_PLUGIN` | OpenCode | The plugin directory, referenced by the `mcp` block in `opencode.json`. |

## File Locations

| What | Linux and macOS | Windows |
| --- | --- | --- |
| MariaDB Shell, installed by the launcher | `~/.local/bin/mariadb-shell` | `%LOCALAPPDATA%\Programs\mariadb-shell\bin\mariadb-shell.cmd` |
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

## MCP Server Configuration

The connections and allowed paths are set with `mariadb-shell -- mcp setup` and stored in the MariaDB Shell configuration directory. See [Configuring the MCP Server](configuring-the-mcp-server/README.md) and the [MCP server documentation](https://github.com/mariadb-corporation/mariadb-shell-plugins/blob/main/mcp_plugin/README.md#configuration-mcpsetup).
