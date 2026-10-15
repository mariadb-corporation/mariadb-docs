---
description: >-
  Common MariaDB AI Plugins error messages and symptoms, what causes them, and
  how to fix them.
---

# Troubleshooting

## Error Messages

| Message or symptom | Cause | Fix |
| --- | --- | --- |
| *not a configured connection* | The URI isn't on the allow-list, or asks for more than was configured, such as a default schema or an option. | Add the connection with `mariadb-shell -- mcp setup`, or remove the extra part from the URI. |
| A tool call that never returns | A path isn't on the allowed-paths list, and the MCP server is waiting for a confirmation the agent can't give. | Add the directory with `mcp setup`. |
| *There is no object registered under name 'mcp'* | MariaDB Shell can't find its plugins, usually because its configuration directory was moved or is unreadable. | Check `~/.mariadb-shell/plugins/`. |
| No `migrator.*` tools | The migration tooling isn't installed, or the MCP server hasn't restarted since it was. | Run `mariadb-shell -- mcp setup --installMigrator`, then restart the MCP server. |
| *No module named 'pywintypes'* on Windows | The Windows MariaDB Shell packages don't bundle pywin32. | Install `pywin32` into MariaDB Shell's bundled Python. |

## The Plugin Doesn't Load

Check that the harness loaded the plugin:

* Claude Code: run the following command:

  ```text
  /plugin
  ```
* Codex: run the following command:

  ```text
  /plugins
  ```
* Pi: a project-local package must be approved at run time with `--approve`, or it is configured but never loaded.
* Hermes Agent: Hermes installs portable packages disabled. Check that the plugin is enabled:

  ```bash
  hermes plugins list
  ```

  To enable it, run `hermes plugins enable mariadb-dev`.

## The MCP Server Doesn't Start

* The first start downloads MariaDB Shell, which can take a minute. Check the harness's MCP log; the launcher writes all of its messages to standard error.
* To use a MariaDB Shell you installed yourself, set `MARIADB_SHELL_BIN`. See [Configuration Reference](configuration-reference.md).
* For Codex, register the server manually. See [Codex](installation/codex.md#register-the-mcp-server-manually).
* For Pi, the server requires Pi 1.0 or later and the built-in MCP support of Pi. An installed `pi-mcp-adapter` replaces the built-in support, so the `mariadb` server never connects. Remove the adapter and turn the built-in `mcp` back on. See [Pi](installation/pi.md#upgrade-from-pi-mcp-adapter).
* For Hermes Agent, start a new session after the installation, because Hermes connects MCP servers when a session starts. On native Windows, the plugin's `.sh` launcher can't run, so add a `mariadb` server with the `.cmd` launcher to `config.yaml`. See [Hermes Agent](installation/hermes.md#windows).

## A Sandbox Doesn't Work

| Symptom | Cause |
| --- | --- |
| `sandbox.deploy` doesn't return. | The sandbox directory isn't on the allowed-paths list. |
| The deploy succeeds, but the connection is refused. | The password was blank. |
| The deploy fails on TLS. | TLS was requested and `openssl` isn't installed. |
| `sandbox.stop` fails for a downloaded server. | The binary isn't on the `PATH`. Use `sandbox.kill`. |

## A Migration Reports Success but Migrates Nothing

The run was pointed at the output directory of an earlier run. See [migrator Tools](mcp-tool-reference/migrator-tools.md#avoiding-a-false-success).
