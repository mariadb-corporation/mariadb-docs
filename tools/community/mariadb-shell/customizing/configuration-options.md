---
description: >-
  Reference of the MariaDB Shell configuration options, and how to change
  them for one session or permanently with the option command, shell.options, and
  options.json.
---

# Configuration Options

Configuration options control how MariaDB Shell behaves: the result format, the pager, history, logging, the credential store, timeouts, and more. You can change most of them while the shell runs, and store the ones you want to keep in a configuration file.

## Viewing and Changing Options

### The \option Command

The `\option` command works in SQL and Python mode:

| Command | Effect |
| --- | --- |
| `\option -l`, `\option --list` | Lists all options and their current values. |
| `\option -l --show-origin` | Also shows where each value comes from: `Compiled default`, `Environment variable`, `Configuration file`, `Command line`, or `User defined`. |
| `\option -h [<filter>]`, `\option --help [<filter>]` | Shows the description of the options whose names start with the filter. |
| `\option <name>` | Shows the value of an option. |
| `\option <name> [=] <value>` | Sets an option for the current session. |
| `\option --persist <name> [=] <value>` | Sets an option and saves it in `options.json`, so it also applies to future sessions. |
| `\option --unset <name>` | Resets an option to its default for the current session. |
| `\option --unset --persist <name>` | Resets an option and removes it from `options.json`. |

```text
MariaDB localhost:3306 ssl  SQL > \option --persist history.maxSize 5000
MariaDB localhost:3306 ssl  SQL > \option resultFormat = vertical
MariaDB localhost:3306 ssl  SQL > \option --unset resultFormat
```

`\option` can't parse list values. To set `credentialStore.excludeFilters`, use Python.

### The shell.options Object

In Python mode, the `shell.options` object reads and changes the same options. Option names contain dots, so use the subscript form to read them:

```python
shell.options["resultFormat"]                    # read
shell.options["resultFormat"] = "json/pretty"    # set for this session
shell.options.set("showColumnTypeInfo", True)    # set with a method call
shell.options.unset("resultFormat")              # back to the default
shell.options.set_persist("credentialStore.excludeFilters", ["*@prod.example.com:*"])
shell.options.unset_persist("credentialStore.excludeFilters")
```

| Method | Effect |
| --- | --- |
| `set(name, value)` | Sets an option for the current session. |
| `set_persist(name, value)` | Sets an option and saves it in `options.json`. |
| `unset(name)` | Resets an option to its default for the current session. |
| `unset_persist(name)` | Resets an option and removes it from `options.json`. |

## The options.json File

Persisted options are stored in `options.json` in the user configuration directory:

* Linux and macOS: `~/.mariadb-shell/options.json`
* Windows: `%AppData%\MariaDB\mariadb-shell\options.json`

The file is a JSON object that maps option names to values. The shell writes the values as strings:

```json
{
    "history.maxSize": "5000",
    "pager": "less -S",
    "credentialStore.excludeFilters": "[\"*@prod.example.com:*\"]"
}
```

You can edit the file by hand while the shell isn't running. Prefer `\option --persist` or `shell.options.set_persist()`, which validate the value before they save it. To use a different configuration directory, and therefore a different `options.json`, set `MARIADB_SHELL_USER_CONFIG_HOME`.

## Precedence

When several sources set the same option, the later one in this list wins:

1. The compiled default.
2. An environment variable, for the options that have one, such as `PAGER` for `pager`.
3. The value persisted in `options.json`.
4. A command line option, such as `--pager` or `--result-format`.
5. A change made at run time with `\option` or `shell.options`.

For example, if `options.json` sets `pager` to `less -S`, starting the shell with `--pager=cat` uses `cat` for that session only. `\option -l --show-origin` shows which source supplied each value.

## Option Reference

Options marked read-only can only be set with the command line option shown.

| Option | Type | Default | Description |
| --- | --- | --- | --- |
| `autocomplete.nameCache` | bool | `true` | Loads the names of schemas, tables, and columns when you connect or change the default schema, for [autocompletion](../using-mariadb-shell/autocompletion.md). Refresh the cache manually with `\rehash`. The shell turns it off when input or output isn't a terminal. Command line: `--name-cache`, `--no-name-cache` (`-A`). |
| `batchContinueOnError` | bool | `false` | Read-only. Continues an SQL script in batch mode after an error. Command line: `--force`. |
| `connectTimeout` | float | `10` | The connection timeout, in seconds, for the sessions the shell opens. |
| `credentialStore.excludeFilters` | array | `[]` | Connection URLs for which the shell never stores passwords, such as `"*@prod.example.com:*"`. The wildcards `*` and `?` are allowed. See [Credential Store](../connecting/credential-store.md). |
| `credentialStore.helper` | string | `default` | The credential helper: `default` for the platform default, a helper name such as `keychain`, `login-path`, `secret-service`, `windows-credential`, or `plaintext`, or `<disabled>` to turn off the credential store. Command line: `--credential-store-helper`. Environment variable: `MARIADB_SHELL_CREDENTIAL_STORE_HELPER`. |
| `credentialStore.savePasswords` | string | `prompt` | When to store passwords: `always`, `prompt`, or `never`. Command line: `--save-passwords`. Environment variable: `MARIADB_SHELL_CREDENTIAL_STORE_SAVE_PASSWORDS`. |
| `defaultCompress` | bool | `false` | Requests protocol compression for the global session by default. See [Compressed Connections](../connecting/compressed-connections.md). |
| `defaultMode` | string | none | The mode the shell starts in: `sql` or `py`. Without a value, the shell starts in SQL mode. A command line option such as `--py` or `--sql` overrides it. |
| `history.autoSave` | bool | `true` | Saves the command history when the shell exits. See [Editing and History](../using-mariadb-shell/editing-and-history.md). |
| `history.maxSize` | integer | `1000` | The number of entries to keep in the history. |
| `history.sql.ignorePattern` | string | `*IDENTIFIED*:*PASSWORD*` | Colon-separated glob patterns. SQL statements that match aren't added to the history. Command line: `--histignore`. |
| `history.sql.syslog` | bool | `false` | Writes interactive SQL statements that don't match `history.sql.ignorePattern` to the system log. Command line: `--syslog`. |
| `interactive` | bool | | Read-only. Whether the shell runs in interactive mode. Command line: `--interactive` (`-i`) forces interactive mode. |
| `logFile` | string | `mariadb-shell.log` in the user configuration directory | Read-only. The path to the log file. Command line: `--log-file`. See [Logging and Debugging](../logging-and-debugging.md). |
| `logLevel` | integer or string | `5` (`info`) | The log level: `1` to `8`, or `none`, `internal`, `error`, `warning`, `info`, `debug`, `debug2`, `debug3`. With a leading `@`, such as `@debug`, log messages also go to standard error. Command line: `--log-level`. |
| `logSql` | string | `error` | Which SQL statements to log: `off`; `error`, statements that fail, with the error; `on`, all statements except those that match `logSql.ignorePattern` or `logSql.ignorePatternUnsafe`; `all`, all except those that match `logSql.ignorePatternUnsafe`; `unfiltered`, all statements. Command line: `--log-sql`. |
| `logSql.ignorePattern` | string | `*SELECT*:SHOW*` | Colon-separated glob patterns of statements that `logSql=on` doesn't log. |
| `logSql.ignorePatternUnsafe` | string | `*IDENTIFIED*:*PASSWORD*` | Colon-separated glob patterns of statements that only `logSql=unfiltered` logs. |
| `mysqlPluginDir` | string | `lib/mariadb/plugins` in the installation directory | The directory of client-side authentication plugins. Command line: `--mysql-plugin-dir`. |
| `oci.configFile` | string | `~/.oci/config` | The Oracle Cloud Infrastructure configuration file, used to access OCI Object Storage. See [Object Storage](../utilities/dump-and-load/object-storage.md). |
| `oci.profile` | string | `DEFAULT` | The profile in `oci.configFile` to use. |
| `pager` | string | empty | The command that pages output in interactive mode, such as `less -S`. Empty means no pager. See [Pager](../using-mariadb-shell/pager.md). Command line: `--pager`. Environment variable: `PAGER`. |
| `passwordsFromStdin` | bool | `false` | Reads passwords from standard input instead of the terminal, for scripted use. Command line: `--passwords-from-stdin`. |
| `resultFormat` | string | `table` | The format of query results: `table`, `tabbed`, `vertical`, `json` (same as `json/pretty`), `ndjson` (same as `json/raw`), `json/array`, `json/pretty`, or `json/raw`. In batch mode, the default is `tabbed`. See [Output Formats](../using-mariadb-shell/output-formats.md). Command line: `--result-format`, `--table`, `--tabbed`, `--vertical` (`-E`). |
| `sandboxDir` | string | `~/.mariadb-shell/sandboxes`; on Windows, `%userprofile%\MariaDB\mariadb-shell\sandboxes`; `<MARIADB_SHELL_USER_CONFIG_HOME>/sandboxes` when that variable is set | The default directory for instances that the `sandbox` object deploys. See [Sandbox Instances](../sandbox-instances.md). |
| `showColumnTypeInfo` | bool | `false` | Shows column metadata, such as types and lengths, before SQL results. Command line: `--column-type-info`. |
| `showWarnings` | bool | `true` | Shows the warnings of an SQL statement after its result in SQL mode. Command line: `--show-warnings`. |
| `slashCommands` | bool | `true` | Also accepts shell commands with a `/` prefix in place of `\`, such as `/quit` or `/status`. See [The Slash Prefix](../using-mariadb-shell/shell-commands.md#the-slash-prefix). |
| `ssh.bufferSize` | integer | `10240` | The buffer size, in bytes, for data transfer through [SSH tunnels](../connecting/ssh-tunnels.md). |
| `ssh.configFile` | string | empty | A custom SSH configuration file. Empty means the standard locations, such as `~/.ssh/config`. Command line: `--ssh-config-file`. |
| `useWizards` | bool | `true` | Read-only. Whether functions may prompt interactively for missing information and confirmations. Command line: `--no-wizard` (`--nw`) turns it off. |
| `verbose` | integer | `0` | Prints diagnostic messages to the console: `0` for none, `1` for errors, warnings, and information, and `2` to `4` for increasing levels of debug detail. Command line: `--verbose`. |

