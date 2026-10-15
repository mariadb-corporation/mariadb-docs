---
description: >-
  Reference for the built-in backslash commands of MariaDB Shell, such as
  connect, use, option, source, and history, with their aliases and syntax,
  and the slash prefix that also runs them.
---

# Shell Commands

Shell commands control MariaDB Shell itself rather than the server. Each one starts with a backslash, or with a slash in its place (see [The Slash Prefix](#the-slash-prefix)), works the same way in SQL and Python mode, and is processed by the shell before anything reaches the server or the Python interpreter.

A shell command must be the only thing on its line and doesn't take a statement terminator. Arguments follow the command name, separated by spaces.

```text
MariaDB localhost:3306 ssl  shop  SQL > \use sakila
Default schema set to `sakila`.
MariaDB localhost:3306 ssl  sakila  SQL > \option resultFormat vertical
```

To list all commands, type `\?` or `\help`. To show the help for one command, pass its name, for example `\? \history` or `\? history`.

{% hint style="info" %}
Shell commands are interactive features. In batch mode, when you run a file with `-f` or pipe input into the shell, a line such as `\use mysql` is sent to the server as SQL and fails. Add `-i` (`--interactive`) to process shell commands in batch input. The statement terminators `\G` and `\g` work in both modes. See [Batch Execution](batch-execution.md#shell-commands-in-scripts).
{% endhint %}

## The Slash Prefix

Every shell command can also be typed with a slash in place of the backslash, so `/quit`, `/status`, `/connect`, `/sql`, and `/?` run `\quit`, `\status`, `\connect`, `\sql`, and `\?`. Aliases work the same way: `/q` exits and `/.` runs a script file.

```text
MariaDB localhost:3306 ssl  shop  SQL > /use sakila
Default schema set to `sakila`.
```

The shell runs a line as a slash command only when the word after the `/` is a shell command of the current mode and the line starts a new statement. Any other line that starts with `/` goes to SQL or Python unchanged, so SQL comments such as `/* ... */` and `/*M! ... */`, a `/` used as the statement delimiter, Python code, and the continuation lines of a multi-line statement keep working. For the same reason, a mistyped command such as `/stauts` isn't reported as an unknown command: it goes to the server or the Python interpreter, which reports the error.

Some commands keep the backslash only:

* The statement terminators `\G` and `\g`, and `\w` and `\W` used inside a statement, because a `/` there is division or the start of a comment.
* The `\` command that starts multi-line input in SQL mode.

A slash command behaves like its backslash form in the rest of the shell. It's saved in the history with the same filters, so a password in `/connect` or `/sql` is kept out as it is for `\connect` or `\sql`, and it completes with **Tab** the same way: `/co` completes to `/connect`, and `/use ` completes schema names. Help finds it too, so `/help /quit` shows the help of `\quit`.

The `slashCommands` option, `true` by default, controls the slash prefix. To accept the backslash form only:

```text
MariaDB localhost:3306 ssl  SQL > \option --persist slashCommands false
```

## Command Reference

| Command | Alias | Syntax | Description |
| --- | --- | --- | --- |
| `\` | | `\` | Starts a block of SQL lines that runs only after an empty line. SQL mode only. See [Multi-Line Input](sql-and-python-modes.md#multi-line-input). |
| `\connect` | `\c` | `\connect [--mc] <URI>` | Opens a new global session and closes the current one. |
| `\disconnect` | | `\disconnect` | Closes the global session. |
| `\edit` | `\e` | `\edit [text]` | Opens the last statement, or the given text, in an external editor. See [\edit](#edit). |
| `\exit` | | `\exit` | Exits MariaDB Shell. Same as `\quit`. |
| `\help` | `\?`, `\h` | `\help [pattern]` | Shows help on a command, object, function, or SQL topic. |
| `\history` | | `\history [del <range> \| clear \| save]` | Lists or edits the command history. See [\history](#history). |
| `\nopager` | | `\nopager` | Turns off the pager. |
| `\nowarnings` | `\w` | `\nowarnings` | Stops showing warnings after each statement. See [\warnings](#warnings). |
| `\option` | | `\option [args]` | Lists, shows, sets, and persists shell options. See [\option](#option). |
| `\pager` | `\P` | `\pager [command]` | Sets the program that pages output. See [Pager](pager.md). |
| `\py` | | `\py` | Switches to Python mode. |
| `\quit` | `\q` | `\quit` | Exits MariaDB Shell. |
| `\reconnect` | | `\reconnect` | Reopens the global session with the same connection data. |
| `\rehash` | | `\rehash` | Reloads the object name cache used by autocompletion. See [\rehash](#rehash). |
| `\show` | | `\show [report] [options] [args]` | Runs a report once. See [\show and \watch](#show-and-watch). |
| `\source` | `\.` | `\source [--sql\|--py] <path> [args]` | Runs a script file. See [\source](#source). |
| `\sql` | | `\sql [statement]` | Switches to SQL mode, or runs one SQL statement from Python mode. |
| `\status` | `\s` | `\status` | Shows information about the global session. See [\status](#status). |
| `\system` | `\!` | `\system <command> [args]` | Runs an operating system command. See [\system](#system). |
| `\use` | `\u` | `\use <schema>` | Sets the default schema. See [\use](#use). |
| `\warnings` | `\W` | `\warnings` | Shows warnings after each statement. See [\warnings](#warnings). |
| `\watch` | | `\watch [report] [options] [args]` | Runs a report repeatedly. See [\show and \watch](#show-and-watch). |

## Help

`\help`, `\h`, and `\?` take an optional pattern. The pattern can be a command, a global object, a class, a function, or an SQL keyword, and can contain the wildcards `?` (one character) and `*` (any sequence):

```text
MariaDB localhost:3306 ssl  SQL > \? \source
MariaDB localhost:3306 ssl  SQL > \? util.dump_schemas
MariaDB localhost:3306 ssl  SQL > \? *sandbox*
MariaDB localhost:3306 ssl  SQL > \? SELECT
```

Help on SQL statements comes from the server's help tables, so it needs an open session. In Python mode, every global object and class also has a `help()` method, for example `util.help("dump_schemas")`.

## Connect, Reconnect, and Disconnect

`\connect` takes the same URI formats as the command line, including `mariadb://`, `mariadb+ssh://`, and socket paths. The optional `--mc` (or `--mysql`) flag requests a classic protocol session, which is the only session type in MariaDB Shell, so you can leave it out:

```text
MariaDB localhost:3306 ssl  SQL > \connect mariadb://dba@db1.example.com:3306/shop
```

`\reconnect` reopens the global session after the server closed it, for example after a restart or a timeout. `\disconnect` closes the global session and leaves the shell running.

See [Connection URIs and Options](../connecting/connection-uris-and-options.md) for the URI syntax.

## \option

`\option` reads and changes the shell options that `shell.options` exposes in Python. The forms are:

| Form | Effect |
| --- | --- |
| `\option -l` or `\option --list` | Lists all options with their current values. |
| `\option -l --show-origin` | Also shows where each value comes from, such as `Compiled default`, the configuration file, or the command line. |
| `\option -h [filter]` or `\option --help [filter]` | Describes the options whose names match the filter. |
| `\option <name>` | Shows the value of one option. |
| `\option <name> [=] <value>` | Sets an option for the current session. The `=` is optional. |
| `\option --persist <name> [=] <value>` | Sets an option and saves it in `options.json` in the configuration directory. |
| `\option --unset <name>` | Resets an option to its default for the current session. |
| `\option --unset --persist <name>` | Resets an option and removes it from `options.json`. |

```text
MariaDB localhost:3306 ssl  shop  SQL > \option resultFormat
table
MariaDB localhost:3306 ssl  shop  SQL > \option resultFormat = vertical
MariaDB localhost:3306 ssl  shop  SQL > \option --persist history.maxSize 5000
MariaDB localhost:3306 ssl  shop  SQL > \option --unset --persist history.maxSize
```

See [Configuration Options](../customizing/configuration-options.md) for the list of options.

## \show and \watch

`\show` runs a report and prints its result. `\watch` runs the same report in a loop and refreshes the screen until you press **Ctrl+C**. Without a report name, both commands list the available reports:

```text
MariaDB localhost:3306 ssl  shop  SQL > \show
Available reports: query, thread, threads.
```

The built-in reports are:

| Report | Description |
| --- | --- |
| `query` | Runs the SQL statement given as its arguments and shows the result. |
| `thread` | Shows details about one thread of the server. |
| `threads` | Lists the threads that belong to the current user. |

The `threads` report needs `performance_schema=ON`. See [Reports](../extending-mariadb-shell/reports.md#threads).

Report names are case-insensitive, and `-` and `_` are interchangeable in them. Every report accepts `--help`, which describes its options and columns. Reports of type list also accept `--vertical` (`-E`), which prints each row as a block of `name: value` lines.

`\watch` adds two options:

| Option | Description |
| --- | --- |
| `--interval=<seconds>`, `-i <seconds>` | Seconds between two runs, from `0.1` to `86400`. The default is `2`. |
| `--nocls` | Doesn't clear the screen between runs, so the results scroll. |

The following command shows the number of running threads every second:

```text
MariaDB localhost:3306 ssl  SQL > \watch query --interval=1 SHOW GLOBAL STATUS LIKE 'Threads_running'
```

You can register your own reports in Python. See [Reports](../extending-mariadb-shell/reports.md).

## \source

`\source` (or `\.`) reads a script file and runs it in the current mode. To run the file in another mode without switching, put `--sql` or `--py` before the path. Arguments after the path are passed to a Python script in `sys.argv`:

```text
MariaDB localhost:3306 ssl  shop  SQL > \source /home/dba/sql/create_views.sql
MariaDB localhost:3306 ssl  shop  SQL > \. --py /home/dba/py/price_report.py 20
```

SQL files can contain `DELIMITER` lines, so you can source files that define stored procedures and triggers. An error in an SQL file stops the file at the failing statement unless the shell runs with `--force`.

In SQL mode, the shell also accepts `source <path>` without the backslash, as the `mariadb` client does, so existing scripts that include other files keep working.

## \system

`\system` (or `\!`) passes the rest of the line to the operating system shell and shows the output. Redirection and environment variables work as in the operating system shell. Without arguments, it shows its help.

```text
MariaDB localhost:3306 ssl  shop  SQL > \! ls /backups
MariaDB localhost:3306 ssl  shop  SQL > \system df -h /var/lib/mysql > /tmp/disk.txt
```

## \edit

`\edit` (or `\e`) writes a statement to a temporary file and opens it in an external editor. When you save the file and quit the editor, the edited text appears at the prompt, where you can review it and press **Enter** to run it. The editor doesn't run the statement by itself.

Without an argument, `\edit` opens the most recent entry of the history. With an argument, it opens that text. The key sequence **Ctrl+X Ctrl+E** does the same as `\edit` with no argument.

The editor is taken from the `EDITOR` environment variable, then from `VISUAL`. If neither is set, the shell uses `vi` on Linux and macOS and `notepad.exe` on Windows.

See [Editing and History](editing-and-history.md#external-editor).

## \history

`\history` without an argument lists the history of the current mode with entry numbers. The following options change it:

| Option | Effect |
| --- | --- |
| `del <range>` (or `delete <range>`) | Deletes entries. The range is a number (`42`), a closed range (`10-20`), an open range to the end (`10-`), or the last *n* entries (`-5`). |
| `clear` | Deletes all entries. |
| `save` | Writes the history of the current mode to its history file. |

See [Editing and History](editing-and-history.md#command-history) for the history files and the `history.*` options.

## \use

`\use` (or `\u`) sets the default schema of the global session, like the SQL statement `USE`, in both modes. Unless name caching is turned off, it also refreshes the autocompletion cache for the new schema.

```text
MariaDB localhost:3306 ssl  shop  SQL > \use sakila
Default schema set to `sakila`.
```

## \status

`\status` (or `\s`) prints information about the shell and the global session: the connection ID, the current user and schema, TLS cipher and protocol, server version, connection type, character sets, compression, server uptime, and a line of server counters.

```text
MariaDB localhost:3306 ssl  shop  SQL > \status
MariaDB Shell version 26.9.5

Connection Id:                21
Current schema:               shop
Current user:                 root@localhost
SSL:                          Cipher in use: TLS_AES_256_GCM_SHA384 TLSv1.3
Using delimiter:              ;
Server version:               12.3.2-MariaDB
Protocol version:             Classic 10
Client library:               3.4.10
Connection:                   localhost via TCP/IP
TCP port:                     3306
Server characterset:          utf8mb4
Schema characterset:          utf8mb4
Client characterset:          utf8mb4
Conn. characterset:           utf8mb4
Result characterset:          utf8mb4
Compression:                  Disabled
Uptime:                       1 min 14.0000 sec

Threads: 2  Questions: 166  Slow queries: 0  Opens: 30  Open tables: 23  Queries per second avg: 2.243
```

The same information is available from the command line with `mariadb-shell <URI> -- shell status`.

## \rehash

`\rehash` reloads the cache of database object names that SQL autocompletion uses. The shell fills the cache when it connects and whenever you change the default schema. Run `\rehash` after you create or drop tables and want the new names to complete, or after you started the shell with `-A` (`--no-name-cache`). On a server with many objects, reloading takes a while; press **Ctrl+C** to stop it.

See [Autocompletion](autocompletion.md#name-cache).

## \warnings

`\warnings` (or `\W`) and `\nowarnings` (or `\w`) turn the automatic display of warnings on and off for the rest of the session. When it's on, the shell prints each warning that a statement raises right after the result:

```text
MariaDB localhost:3306 ssl  shop  SQL > SELECT CAST('abc' AS INT);
+--------------------+
| CAST('abc' AS INT) |
+--------------------+
|                  0 |
+--------------------+
1 row in set, 1 warning (0.0001 sec)
Warning (code 1292): Truncated incorrect INTEGER value: 'abc'
```

Warnings are shown by default. The commands change the `showWarnings` option, which you can also set with `--show-warnings=false` on the command line or persist with `\option --persist showWarnings false`.
