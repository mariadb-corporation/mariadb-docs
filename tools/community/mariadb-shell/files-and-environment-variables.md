---
description: >-
  Where MariaDB Shell keeps its configuration, history, logs, and installed
  files, and the environment variables it reads.
---

# Files and Environment Variables

## User Configuration Directory

MariaDB Shell keeps per-user files in its user configuration directory. The shell creates the directory the first time it runs.

| Platform | Default location |
| --- | --- |
| Linux and macOS | `~/.mariadb-shell` |
| Windows | `%AppData%\MariaDB\mariadb-shell` |

To use a different directory, set the `MARIADB_SHELL_USER_CONFIG_HOME` environment variable. This is useful to keep separate configurations, for example for testing:

```sh
MARIADB_SHELL_USER_CONFIG_HOME=/tmp/msh-test mariadb-shell --py
```

The directory can contain the following files and subdirectories:

| Name | Contents |
| --- | --- |
| `history.sql`, `history.py` | Command history of SQL mode and Python mode. The shell saves the history when it exits while the `history.autoSave` option is enabled, which is the default. See [Editing and History](using-mariadb-shell/editing-and-history.md). |
| `options.json` | Configuration options that you saved with `\option --persist` or `shell.options.set_persist()`. See [Configuration Options](customizing/configuration-options.md). |
| `prompt.json` | A custom prompt theme. When present, it replaces the default theme. See [Prompt](customizing/prompt.md). |
| `mariadb-shellrc.py` | A Python startup script. It runs when Python mode is first initialized, either at startup or at the first switch to Python mode. See [Startup Scripts](customizing/startup-scripts.md). |
| `init.d/` | Python files that the shell loads at startup, for example to register [reports](extending-mariadb-shell/reports.md). |
| `plugins/` | User plugins, one subdirectory per plugin. See [Plugins](extending-mariadb-shell/plugins.md). |
| `plugin_data/` | Data that plugins store, one subdirectory per plugin. `plugin_data/mcp_plugin/settings.json` holds the allowed paths of the [MCP server](mcp-server/configuring-access.md); `plugin_data/msm_plugin/` holds the [Schema Management](schema-management/schema-projects.md#where-msm-stores-its-own-files) working directory, deployment log, and backups. |
| `mariadb-shell.log` | The shell log. Use `--log-file` to write it elsewhere. See [Logging and Debugging](logging-and-debugging.md). |

### Sandbox Directory

By default, [sandbox instances](sandbox-instances.md) are created in the `sandboxes` subdirectory of the default user configuration directory:

| Platform | Default location |
| --- | --- |
| Linux and macOS | `~/.mariadb-shell/sandboxes` |
| Windows | `%USERPROFILE%\MariaDB\mariadb-shell\sandboxes` |

This location is controlled by the `sandboxDir` configuration option. Its default follows `MARIADB_SHELL_USER_CONFIG_HOME`: with the variable set, sandboxes go to `$MARIADB_SHELL_USER_CONFIG_HOME/sandboxes`.

## Other Files

| File | Description |
| --- | --- |
| `/etc/my.cnf`, `/etc/mysql/my.cnf`, `~/.my.cnf` | Option files, read in this order. The shell reads the `[mariadb-shell]`, `[mysqlsh]`, and `[client]` groups. To list the files that a build reads, run `mariadb-shell --help`. See [Option Files and Login Paths](connecting/option-files-and-login-paths.md). |
| `~/.mylogin.cnf` | The login file, where the `login-path` credential store helper keeps passwords. On Windows, the file is `%AppData%\MySQL\.mylogin.cnf`. See [Credential Store](connecting/credential-store.md). |
| `/etc/mysql/mariadb-shell/mariadb-shellrc.py` | A system-wide startup script, run before the user's own. Windows ignores system-wide startup scripts. |

## Installation Directories

The [installation scripts](installation/) place each version in its own directory:

| Platform | Installation directory | Commands |
| --- | --- | --- |
| Linux and macOS | `~/.local/share/mariadb-shell/<version>` | Links `mariadb-shell` and `msh` in `~/.local/bin` |
| Windows | `%LOCALAPPDATA%\Programs\mariadb-shell\<version>` | `mariadb-shell.cmd` and `msh.cmd` in `%LOCALAPPDATA%\Programs\mariadb-shell\bin` |

Inside an installation directory, `bin/` holds the executables, `lib/` the private libraries, the bundled Python runtime, and the built-in plugins, and `share/mariadb-shell/` the data files, such as the sample prompt themes and a startup script location for all users of that installation. The shell locates these directories relative to its executable; you can override the installation root with `MARIADB_SHELL_HOME`.

## Environment Variables

MariaDB Shell reads the following environment variables. Each variable is also accepted under its MySQL Shell name, with the `MYSQLSH_` prefix instead of `MARIADB_SHELL_`, for example `MYSQLSH_PROMPT_THEME`. The shell reads the `MYSQLSH_` name only when the `MARIADB_SHELL_` name is not set. A variable that is set to an empty value counts as set.

| Variable | Description |
| --- | --- |
| `MARIADB_SHELL_USER_CONFIG_HOME` | The [user configuration directory](#user-configuration-directory). |
| `MARIADB_SHELL_HOME` | The root of the installation, the directory that contains `bin`, `lib`, and `share`. When it is not set, the shell derives it from the location of its executable. |
| `MARIADB_SHELL_PROMPT_THEME` | The path to a prompt theme file. It takes precedence over `prompt.json`. If the file does not exist, the shell prints a note and uses the default prompt. An empty value selects the default prompt. See [Prompt](customizing/prompt.md). |
| `MARIADB_SHELL_TERM_COLOR_MODE` | The color capability of the terminal: `rgb`, `256`, `16`, or `nocolor`. When it is not set, the shell detects the capability from the terminal. |
| `MARIADB_SHELL_CREDENTIAL_STORE_HELPER` | The credential store helper, equivalent to `--credential-store-helper`. See [Credential Store](connecting/credential-store.md). |
| `MARIADB_SHELL_CREDENTIAL_STORE_SAVE_PASSWORDS` | When to save passwords: `always`, `prompt`, or `never`. Equivalent to `--save-passwords`. |
| `MARIADB_SHELL_CREDENTIAL_STORE_KEYCHAIN` | On macOS, the keychain that the `keychain` helper uses. When it is not set, the helper uses the default keychain. |
| `MARIADB_SHELL_MMAP` | Whether the shell memory-maps local files that it reads, such as dump files: `on` (default), `off`, or `required`. |

The shell also reads these variables:

| Variable | Description |
| --- | --- |
| `PAGER` | The default value of the `pager` option. See [Pager](using-mariadb-shell/pager.md). |
| `EDITOR`, `VISUAL` | The editor that `\edit` starts. When neither is set, the shell uses `vi`, or `notepad.exe` on Windows. |
| `MARIADB_SANDBOX_BOILERPLATE_DIR`, `MARIADB_SANDBOX_NO_SYNC` | Settings for sandbox deployment. See [Sandbox Instances](sandbox-instances.md). |

The installation scripts read their own `MARIADB_SHELL_TAG`, `MARIADB_SHELL_PREFIX`, `MARIADB_SHELL_BINDIR`, and related variables, which the shell itself ignores. See [Linux and macOS](installation/linux-and-macos.md#installation-options) and [Windows](installation/windows.md#installation-options).
