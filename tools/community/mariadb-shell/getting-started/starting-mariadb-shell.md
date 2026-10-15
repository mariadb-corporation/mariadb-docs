---
description: >-
  Start MariaDB Shell, connect to a server when it starts, choose SQL or Python
  mode, get help, and exit.
---

# Starting MariaDB Shell

## Start the Shell

Run `mariadb-shell`, or its short alias `msh`, from a terminal:

```sh
mariadb-shell
```

The shell prints a welcome message and an SQL prompt. Without connection data, the shell starts without a session, and the prompt shows only the vendor name and the current mode:

```text
Welcome to the MariaDB Shell 26.9.5.

Copyright (c) 2016, 2026, Oracle, MariaDB plc and others.

Type '\help' or '\?' for help; '\quit' to exit.
MariaDB  SQL >
```

To suppress the welcome message, start the shell with `--quiet-start`. With `--quiet-start=2`, the shell prints only errors at startup.

## Connect When the Shell Starts

To open a session at startup, pass a connection URI as the first argument. The URI has the form `[scheme://][user[:password]@]host[:port][/schema]`, and the `mariadb://` scheme is optional:

```sh
mariadb-shell mariadb://app_user@db1.example.com:3306/shop
```

You can also use individual options:

```sh
mariadb-shell --user=app_user --host=db1.example.com --port=3306 --schema=shop
```

When the connection data has no password, the shell prompts for it:

```text
Please provide the password for 'app_user@db1.example.com:3306':
```

After a successful login, the shell can offer to save the password in the platform's credential store, so that later connections to the same account don't prompt again. See [Credential Store](../connecting/credential-store.md).

The following options control how the shell obtains the password:

| Option | Description |
| --- | --- |
| `-p`, `--password` | Prompt for the password. |
| `--password=<password>` | Use the given password. Other users of the system may be able to see it in the process list, so prefer a prompt, the credential store, or an option file. |
| `--no-password` | Connect with an empty password and don't prompt. |
| `--passwords-from-stdin` | Read passwords from standard input instead of the terminal, for example in scripts. |

The shell also reads connection options from the `[mariadb-shell]`, `[mysqlsh]`, and `[client]` groups of your option files. See [Option Files and Login Paths](../connecting/option-files-and-login-paths.md).

For all connection methods, including sockets, TLS, and SSH tunnels, see [Connecting to a Server](../connecting/). For working with the session once it is open, see [Sessions](sessions.md).

## Choose SQL or Python Mode

MariaDB Shell has two modes:

* **SQL mode** sends what you type to the server as SQL statements. This is the default mode.
* **Python mode** runs Python code that uses the shell's [global objects](global-objects.md), such as `session`, `shell`, and `util`.

To choose the mode at startup, use `--sql` or `--py`:

```sh
mariadb-shell --py root@localhost
```

To change the default mode for every start, set the `defaultMode` configuration option to `sql` or `py` and save it in your configuration. In the shell, run:

```text
MariaDB  SQL > \option --persist defaultMode py
```

From the operating system shell, the same setting is:

```sh
mariadb-shell -- shell options set-persist defaultMode py
```

See [Configuration Options](../customizing/configuration-options.md).

To switch modes in a running shell, use the `\sql` and `\py` commands. The prompt shows the active mode:

```text
MariaDB localhost:3306 ssl  SQL > \py
Switching to Python mode...
MariaDB localhost:3306 ssl  Py > session.server_vendor
MariaDB
MariaDB localhost:3306 ssl  Py > \sql
Switching to SQL mode... Commands end with ;
MariaDB localhost:3306 ssl  SQL >
```

In Python mode, `\sql` followed by a statement runs that one statement without switching modes:

```text
MariaDB localhost:3306 ssl  Py > \sql SELECT COUNT(*) FROM sakila.film;
```

For more about the modes, see [SQL and Python Modes](../using-mariadb-shell/sql-and-python-modes.md). To run commands or script files without an interactive session, see [Batch Execution](../using-mariadb-shell/batch-execution.md).

## Get Help

The built-in help describes every shell command, global object, function, and option of this build. Use `\help`, or its shortcuts `\?` and `\h`:

| Command | Shows |
| --- | --- |
| `\?` | The help categories, the shell commands, and the global objects. |
| `\? <command>` | Help for a shell command, for example `\? \connect`. |
| `\? <object>` | Help for a global object or class, for example `\? util` or `\? ClassicSession`. |
| `\? <object>.<function>` | Help for a function, for example `\? util.dump_schemas`. |
| `\? <keyword>` | Help for an SQL statement or function, read from the connected server's help tables, for example `\? CREATE SEQUENCE`. |
| `\? cmdline` | The rules for calling the shell's APIs from the operating system command line. |

The pattern after `\?` can contain the wildcards `*` (any sequence of characters) and `?` (one character). In Python mode, every object also has a `help()` method, for example `util.help("dump_schemas")`.

The `mariadb-shell --help` command lists the command-line options. On Linux and macOS, the `mariadb-shell(1)` manual page describes the options, files, and environment variables. All command-line options are listed in the [CLI Reference](../cli-reference.md).

## Exit the Shell

To exit, use `\quit`, its shortcut `\q`, or `\exit`. On Linux and macOS, you can also press Ctrl+D on an empty line. The shell closes its sessions and prints `Bye!`.
