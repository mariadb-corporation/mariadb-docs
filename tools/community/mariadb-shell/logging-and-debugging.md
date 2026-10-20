---
description: >-
  Where MariaDB Shell writes its application log, how to set the log level and
  SQL statement logging, and how to show diagnostic output on the console or
  send interactive statements to the system log.
icon: file-lines
---

# Logging and Debugging

<!--
  SYNCED: this page is maintained in mariadb-corporation/mariadb-shell, under docs-ref/content/,
  and copied one way into mariadb-docs (tools/community/mariadb-shell/).
  Make every change in mariadb-corporation/mariadb-shell. A change made in mariadb-docs or in the
  GitBook editor is overwritten by the next sync.
-->

MariaDB Shell writes an application log that records what the shell does: startup, connections, plugin loading, errors, and, if you ask for it, the SQL statements it runs. The log is the first place to look when a connection fails, a plugin doesn't load, or a utility reports `Check mariadb-shell.log for more warnings`.

Three independent outputs are available:

| Output | Controlled by | Content |
| --- | --- | --- |
| Application log file | `--log-file`, `--log-level`, `--log-sql` | Shell events and, optionally, SQL statements. |
| Console | `--verbose`, or `--log-level` with an `@` prefix | The same kind of messages, printed while the shell runs. |
| System log | `--syslog` | The statements you enter interactively. |

## Log File Location

| Platform | Default log file |
| --- | --- |
| Linux and macOS | `~/.mariadb-shell/mariadb-shell.log` |
| Windows | `%APPDATA%\MariaDB\mariadb-shell\mariadb-shell.log` |

The log file is in the per-user configuration directory. If you set the `MARIADB_SHELL_USER_CONFIG_HOME` environment variable to move that directory, the log file moves with it. To write the log somewhere else for one session, use `--log-file`:

```sh
mariadb-shell --log-file=/tmp/msh-debug.log --log-level=debug root@db1.example.com
```

The shell appends to the file and never rotates it. Delete or truncate it yourself when it grows too large.

In the shell, `shell.options.logFile` shows the file in use. The option is read-only; change it only with `--log-file` at startup.

```text
MariaDB localhost:3306 ssl  Py > shell.options.logFile
/home/dev/.mariadb-shell/mariadb-shell.log
```

Each line has a timestamp, the process and thread IDs, the level, and the message:

```text
2026-10-05 16:52:39 [76714:20558725]: Info: Connecting to MySQL at: root@localhost:4406
2026-10-05 16:52:39 [76714:20558725]: Info: main: tid=0: CONNECTED: localhost:4406
```

The log text "Connecting to MySQL" refers to the client protocol and appears for MariaDB Server too.

## Log Level

`--log-level` sets how much detail the log contains. The default is `info` (5). Each level includes the levels above it.

| Value | Name | Logs |
| --- | --- | --- |
| `1` | `none` | Nothing. |
| `2` | `internal` | Internal errors of the shell. |
| `3` | `error` | Errors. |
| `4` | `warning` | Warnings. |
| `5` | `info` | Informational messages, such as connections and loaded plugins. This is the default. |
| `6` | `debug` | Debugging information, such as plugin search paths and credential store activity. |
| `7` | `debug2` | More detailed debugging information. |
| `8` | `debug3` | The most detailed debugging information. |

You can give the number or the name. Prefix the value with `@` to also write the log messages to standard error:

```sh
mariadb-shell --log-level=@debug --sql -e "SELECT 1" root@localhost
```

The same values work for the `logLevel` option, which you can change at runtime or persist in the [configuration](customizing/configuration-options.md). Reading the option returns the number:

```text
MariaDB localhost:3306 ssl  Py > shell.options.logLevel = "debug2"
MariaDB localhost:3306 ssl  Py > shell.options.logLevel
7
MariaDB localhost:3306 ssl  Py > shell.options.set_persist("logLevel", "debug")
```

## Verbose Console Output

`--verbose` prints diagnostic messages to the console as they happen, without changing what goes into the log file. This is convenient when you test a connection from the command line.

| Value | Prints |
| --- | --- |
| `0` | Nothing. This is the default. |
| `1` | Errors, warnings, and informational messages. `--verbose` without a value means `1`. |
| `2`, `3`, `4` | Increasingly detailed debug messages. |

```text
$ mariadb-shell --verbose root@localhost:3306 --sql -e "SELECT 1"
verbose: 2026-10-05T18:52:39Z: Loading startup files...
verbose: 2026-10-05T18:52:39Z: Loading plugins...
verbose: 2026-10-05T18:52:39Z: Connecting to MySQL at: root@localhost:3306
verbose: 2026-10-05T18:52:39Z: main: tid=0: CONNECTED: localhost:3306
1
1
```

The corresponding option is `verbose`, with the values `0` to `4`.

## Logging SQL Statements

`--log-sql` controls whether the SQL statements that the shell sends to the server are written to the application log. This covers statements you type in SQL mode, statements run by `session.run_sql()` in Python, and statements run by the utilities. Statements are logged at the `info` level, so the log level must be `info` or higher.

| Value | Logs |
| --- | --- |
| `off` | No statements. |
| `error` | Only statements that fail, together with the error. This is the default. |
| `on` | All statements, except those that match a pattern in `logSql.ignorePattern` or `logSql.ignorePatternUnsafe`. |
| `all` | All statements, except those that match a pattern in `logSql.ignorePatternUnsafe`. |
| `unfiltered` | All statements, without exceptions. |

The two pattern options hold colon-separated lists of glob patterns, matched against the whole statement:

| Option | Default | Purpose |
| --- | --- | --- |
| `logSql.ignorePattern` | `*SELECT*:*SHOW*` | Keeps read-only statements out of the log with `--log-sql=on`. |
| `logSql.ignorePatternUnsafe` | `*IDENTIFIED*:*PASSWORD*` | Keeps statements that can contain passwords out of the log with `on` and `all`. |

For example, the following command logs every statement except those that can contain passwords:

```sh
mariadb-shell --log-sql=all --sql root@localhost -f migrate.sql
```

With the default patterns, the log then contains a `DROP USER` statement from the script but not the `CREATE USER ... IDENTIFIED BY` statement before it. A failing statement is logged together with its error:

```text
2026-10-05 16:52:39 [76714:20558725]: Info: main: tid=71: SQL: SELECT nosuchcol FROM shop.customers
2026-10-05 16:52:39 [76714:20558725]: Info: main: tid=71: MySQL Error 1054 (42S22): Unknown column 'nosuchcol' in 'SELECT'
```

`tid` is the connection ID on the server, which helps you match log entries with the server's process list or general query log.

{% hint style="warning" %}
`--log-sql=unfiltered` writes every statement to the log, including statements that contain passwords in clear text. Use it only for short troubleshooting sessions, and delete the log afterward.
{% endhint %}

To change SQL logging at runtime, set the `logSql` option:

```python
shell.options.logSql = "on"
shell.options["logSql.ignorePattern"] = "*SELECT*:*SHOW*:SET *"
```

## Logging to the System Log

`--syslog` sends the statements that you enter interactively to the operating system log: to syslog with the identifier `mariadb-shell` and the `user` facility on Linux and macOS, or to the Windows Event Log on Windows. This supports auditing of what administrators run by hand. Statements run from a script with `-f` or `-e` are not logged.

The shell logs SQL statements and the `\source` and `\.` commands. Each entry has the following fields:

```text
SYSTEM_USER=dev MYSQL_USER=root CONNECTION_ID=71 DB_SERVER=localhost DB=shop QUERY=DELETE FROM orders WHERE id = 42
```

A field without a value shows `--`. Entries are cut at 1024 characters.

The same filter as for the command history applies: statements that match a pattern in the `history.sql.ignorePattern` option are not sent to the system log. The default pattern, `*IDENTIFIED*:*PASSWORD*`, keeps statements that can contain passwords out of the system log. You can also set the patterns with `--histignore`.

To enable system logging permanently, persist the `history.sql.syslog` option:

```python
shell.options.set_persist("history.sql.syslog", True)
```

On Windows, the shell needs a registry key for its Event Log source. Run the shell once with administrator rights, or with sufficient privileges to create the key, before you use `--syslog` as a regular user.

## Troubleshooting Tips

* **Connection problems.** Run the failing command with `--verbose=4`, or with `--log-level=@debug3`, to see each step of the connection, including SSH tunnel setup.
* **Plugins that don't load.** Plugin errors are written to the log at startup. Start with `--log-level=debug` to also see where the shell looks for plugins. See [Plugins](extending-mariadb-shell/plugins.md).
* **Utility warnings.** When a utility such as `util.import_table()` produces many warnings, it prints the first few and writes all of them to the log.
* **Credential store problems.** Start with `--log-level=debug` and search the log for `helper`. See [Credential Store](connecting/credential-store.md).
* **Support requests.** Include the relevant part of the log. Check it for host names, user names, and statement text you don't want to share before you send it.

<sub>_This page is licensed: GPLv2_</sub>
