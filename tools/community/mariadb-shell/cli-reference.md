---
description: >-
  Reference of the mariadb-shell command: usage forms and every command-line
  option, grouped by purpose, with aliases and option-file behavior.
icon: terminal
---

# CLI Reference

This page lists the command-line options of `mariadb-shell` 26.9.5. The short alias `msh` accepts the same options. For the options of your installed build, run `mariadb-shell --help`.

## Synopsis

```text
mariadb-shell [OPTIONS] [URI]
mariadb-shell [OPTIONS] [URI] -f <path> [<script-args>...]
mariadb-shell [OPTIONS] [URI] -- <object> <method> [<method-args>...]
```

* The first form starts an interactive session or, with `-e` or `-c`, runs one command and exits.
* The second form runs a SQL or Python script in batch mode. Everything after the file name is passed to the script as arguments. See [Batch Execution](using-mariadb-shell/batch-execution.md).
* The third form calls a function of a global object, such as `util`, `shell`, or `sandbox`, directly from the operating system shell. See [Command Line Integration](using-mariadb-shell/command-line-integration.md).

`URI` is a connection string such as `app@db1.example.com:3306/shop`, `mariadb://app@db1.example.com/shop` (`mysql://` is a synonym), or `mariadb+ssh://app@db1.internal?ssh-host=bastion.example.com`. A URI given as the first argument without an option name is the same as `--uri`. For the full syntax, see [Connection URIs and Options](connecting/connection-uris-and-options.md).

Examples:

```sh
mariadb-shell root@localhost/shop
mariadb-shell dba@db1.example.com --sql
mariadb-shell --uri app@db1.example.com --py -f report.py --month=2026-09
mariadb-shell app@db1.example.com -- util dump-schemas shop --output-url=/backups/shop
```

## Option Syntax

* Options that take a value accept `--option=value`. Short options take the value as the next argument, for example `-u root` or `-P 3307`.
* Options shown with `[=<value>]` have an optional value. Without the value, they use the default stated for the option.
* Boolean options, shown as `[=<bool>]`, accept `true`, `false`, `1`, and `0`. Without a value, they mean `true`.
* Options read from an option file use the same names without the leading dashes. See [Option Files](#option-files).

## Aliases

Several options have more than one name:

| Option | Aliases |
| --- | --- |
| `--help` | `-?` |
| `--version` | `-V` |
| `--execute` | `-e` |
| `--pyc` | `-c` |
| `--file` | `-f` |
| `--host` | `-h` |
| `--port` | `-P` |
| `--socket` | `-S` |
| `--user` | `-u` |
| `--password` (prompt) | `-p` |
| `--schema` | `-D`, `--database` |
| `--compress` | `-C` |
| `--mysql` | `--mc` |
| `--python` | `--py` |
| `--vertical` | `-E` |
| `--interactive` | `-i` |
| `--no-name-cache` | `-A` |
| `--no-wizard` | `--nw` |

## General Options

| Option | Description |
| --- | --- |
| `-?`, `--help` | Show the option list and exit. |
| `-V`, `--version` | Show the version of MariaDB Shell, its platform, and the version of MariaDB Connector/C it was built with, and exit. |
| `--` | Start [command line integration](using-mariadb-shell/command-line-integration.md). The arguments that follow are `<object> <method> [arguments]`. In the shell, `\? cmdline` describes the argument syntax. |
| `--execution-context=<id>` | Set a custom execution context, an identifier that is reported with option values. Intended for tools that run the shell. |

## Execution and Batch Options

| Option | Description |
| --- | --- |
| `-e`, `--execute=<cmd>` | Run the command in the startup mode, SQL or Python, and exit. |
| `-c`, `--pyc=<cmd>` | Run a Python command and exit. All arguments after the command are passed to it in `sys.argv`. |
| `-f`, `--file=<file>` | Run the file in batch mode and exit. All arguments after the file name are passed to the script. |
| `--pym <module>` | Run a Python library module as a script, like `python -m`. The remaining arguments are passed to the module. |
| `-i`, `--interactive[=full]` | In batch mode, process each input line as if it were typed interactively. With `full`, the shell also shows the prompt and the input lines. |
| `--force` | In SQL batch mode, continue with the next statement after an error. |
| `--passwords-from-stdin` | Read passwords from standard input instead of the terminal. Useful when a script or another program supplies the password. |

## Mode Options

| Option | Description |
| --- | --- |
| `--sql` | Start in SQL mode. |
| `--sqlc` | Start in SQL mode with a classic session. In MariaDB Shell, all sessions are classic sessions, so this is the same as `--sql`. |
| `--py`, `--python` | Start in Python mode. |
| `--mc`, `--mysql` | Create a classic session from the connection data. All sessions are classic sessions, so the option has no further effect. |

Without a mode option, the shell starts in the mode set by the `defaultMode` [configuration option](customizing/configuration-options.md), which is SQL unless you change it. See [SQL and Python Modes](using-mariadb-shell/sql-and-python-modes.md).

## Connection Options

| Option | Description |
| --- | --- |
| `--uri=<uri>` | Connect with a connection URI in the form `[user[:password]@]host[:port][/schema]`, or any other URI form described in [Connection URIs and Options](connecting/connection-uris-and-options.md). |
| `-h`, `--host=<name>` | Host name or IP address of the server. |
| `-P`, `--port=<number>` | TCP port of the server. The default is 3306. |
| `-S`, `--socket[=<path>]` | On Linux and macOS, connect through a Unix socket file. Without a value, the default socket path is used. On Windows, the option requires a value and names a named pipe. See [Sockets and Named Pipes](connecting/sockets-and-named-pipes.md). |
| `-u`, `--user=<name>` | Account name. |
| `--password[=<password>]` | Password of the account. An empty value, `--password=`, connects without a password. Giving a password on the command line is insecure, and the shell warns about it. |
| `-p`, `--password` | Prompt for the password. |
| `--no-password` | Connect with an empty password and don't prompt. |
| `-D`, `--schema=<name>`, `--database=<name>` | Default schema of the session. |
| `--connect-timeout=<ms>` | Connection timeout in milliseconds. |
| `-C`, `--compress[=<value>]` | Compress the client/server protocol. The values are `REQUIRED`, `PREFERRED`, `DISABLED`, and the Booleans `true`, `false`, `1`, and `0`, which mean `REQUIRED` and `DISABLED`. Without a value, the option means `REQUIRED`. The default is `DISABLED`. See [Compressed Connections](connecting/compressed-connections.md). |
| `--local-infile[=<bool>]` | Allow `LOAD DATA LOCAL INFILE` statements in the session. |
| `--auth-method=<plugin>` | Client authentication plugin to start with, such as `client_ed25519` or `caching_sha2_password`. The server can still switch the connection to another plugin. |
| `--mysql-plugin-dir[=<path>]` | Directory with the client authentication plugins. |
| `--get-server-public-key` | Request the server's RSA public key for password exchange with `caching_sha2_password` or `sha256_password` over an unencrypted connection. |
| `--server-public-key-path=<file>` | File with a local copy of the server's RSA public key, for the same purpose. |

## SSL/TLS Options

| Option | Description |
| --- | --- |
| `--ssl-mode=<mode>` | Required security of the connection: `DISABLED`, `PREFERRED`, `REQUIRED`, `VERIFY_CA`, or `VERIFY_IDENTITY`. |
| `--ssl-ca=<file>` | File with the trusted certificate authority certificates, in PEM format. |
| `--ssl-capath=<dir>` | Directory with trusted certificate authority certificates in PEM format. |
| `--ssl-cert=<file>` | Client certificate in PEM format. |
| `--ssl-key=<file>` | Private key of the client certificate in PEM format. |
| `--ssl-crl=<file>` | File with certificate revocation lists in PEM format. |
| `--ssl-crlpath=<dir>` | Directory with certificate revocation list files in PEM format. |
| `--ssl-cipher=<list>` | Permitted ciphers. With OpenSSL, the list also selects the TLS 1.3 cipher suites. |
| `--tls-version=<version>` | TLS version to use: `TLSv1.2` or `TLSv1.3`. |
| `--tls-ciphersuites=<list>` | Accepted, but has no effect: Connector/C has no setting for TLS 1.3 cipher suites. Use `--ssl-cipher`. |

See [Encrypted Connections](connecting/encrypted-connections.md).

## SSH Tunnel Options

| Option | Description |
| --- | --- |
| `--ssh=<target>` | Connect to the server through an SSH tunnel to `[user@]host[:port]`. |
| `--ssh-identity-file=<file>` | Private key for SSH public key authentication. The file must exist and be readable. |
| `--ssh-config-file=<file>` | OpenSSH configuration file to use instead of `~/.ssh/config`. Sets the `ssh.configFile` option for the session. |

You can also describe the tunnel in a `mariadb+ssh://` URI. See [SSH Tunnels](connecting/ssh-tunnels.md).

## Output Options

| Option | Description |
| --- | --- |
| `--result-format=<format>` | Format of query results: `table`, `tabbed`, `vertical`, `json` (same as `json/pretty`), `ndjson` (same as `json/raw`), `json/raw`, `json/array`, or `json/pretty`. |
| `--table` | Use the table format, the default in interactive mode. Same as `--result-format=table`. |
| `--tabbed` | Use tab-separated output, the default in batch mode. Same as `--result-format=tabbed`. |
| `-E`, `--vertical` | Print each row vertically, one column per line. Same as `--result-format=vertical`. |
| `--json[=<format>]` | Print all shell output, including messages, as JSON. The values are `pretty` (the default), `raw`, and `off`. |
| `--column-type-info` | In SQL mode, print the metadata of each result column before the result. |
| `--show-warnings[=<bool>]` | In SQL mode, show warnings after each statement that produces them. Enabled by default. |
| `--pager=<command>` | External program that pages the output in SQL mode and of some commands, for example `less -S`. Without the option, the `PAGER` environment variable is used. Interactive mode only. See [Pager](using-mariadb-shell/pager.md). |

See [Output Formats](using-mariadb-shell/output-formats.md).

## Interactive Behavior Options

| Option | Description |
| --- | --- |
| `--quiet-start[=<level>]` | Don't print startup information. `1`, the default value, suppresses the version banner. `2` suppresses everything except errors. |
| `--histignore=<patterns>` | Colon-separated glob patterns for SQL statements that are not saved in the command history and not sent to the system log. The default is `*IDENTIFIED*:*PASSWORD*`. |
| `--name-cache[=<bool>]` | Cache schema, table, and column names automatically for autocompletion. Enabled by default. |
| `-A`, `--no-name-cache` | Don't load names for autocompletion automatically. Load them on demand with `\rehash`. |
| `--wizard[=<bool>]` | Allow interactive prompts, such as password prompts and confirmations. Enabled by default. |
| `--nw`, `--no-wizard` | Disable interactive prompts. Use it in scripts, where no one can answer a prompt. |

## Logging Options

| Option | Description |
| --- | --- |
| `--log-file=<path>` | Write the application log to this file instead of the default `mariadb-shell.log` in the configuration directory. |
| `--log-level=<level>` | Log level, `1` to `8` or `none`, `internal`, `error`, `warning`, `info`, `debug`, `debug2`, `debug3`. Prefix the value with `@` to also log to standard error. The default is `info`. |
| `--log-sql=<value>` | Which SQL statements to log: `off`, `error` (the default), `on`, `all`, or `unfiltered`. |
| `--verbose[=<level>]` | Print diagnostic messages to the console. `1`, the default value, prints errors, warnings, and informational messages; `2` to `4` add debug messages. |
| `--syslog[=<bool>]` | Send interactively entered statements to the system log, except those that match `--histignore`. |

See [Logging and Debugging](logging-and-debugging.md).

## Plugin Options

| Option | Description |
| --- | --- |
| `--disable-plugins` | Don't load user plugins, the plugins in the `plugins` directory of the configuration directory. |
| `--disable-builtin-plugins` | Don't load the plugins that ship with MariaDB Shell. They provide the `sandbox` and `plugins` global objects, `util.change_password()`, and the `util.debug` collectors. |

See [Plugins](extending-mariadb-shell/plugins.md).

## Credential Store Options

| Option | Description |
| --- | --- |
| `--credential-store-helper=<helper>` | Helper that stores passwords: `default` for the platform default, a helper name such as `keychain`, `windows-credential`, `login-path`, or `secret-service`, or `<disabled>` to turn the credential store off. Sets the `credentialStore.helper` option for the session. |
| `--save-passwords=<value>` | When to store passwords after a successful connection: `always`, `prompt` (ask each time), or `never`. Sets the `credentialStore.savePasswords` option for the session. |

See [Credential Store](connecting/credential-store.md).

## Option Files

MariaDB Shell reads default options from the standard MariaDB option files before it processes the command line. On Linux and macOS, it reads `/etc/my.cnf`, `/etc/mysql/my.cnf`, and `~/.my.cnf`, in that order. Within each file, it reads the groups `[mariadb-shell]`, `[mysqlsh]`, and `[client]`. The `[mysqlsh]` group is read so that option files written for earlier versions keep working. Options on the command line take precedence over options from files.

```ini
[mariadb-shell]
user=dba
host=db1.example.com
ssl-ca=/etc/ssl/certs/company-ca.pem
```

The following options control which files are read. Each must be the first option on the command line:

| Option | Description |
| --- | --- |
| `--print-defaults` | Print the arguments that the shell would receive from the option files, and exit. Passwords are masked. |
| `--no-defaults` | Don't read any option file. |
| `--defaults-file=<file>` | Read only this option file. |
| `--defaults-extra-file=<file>` | Read this file after the global option files. |
| `--defaults-group-suffix=<suffix>` | Also read the groups whose names end with this suffix, such as `[mariadb-shell_prod]` and `[client_prod]` for `_prod`. |

See [Option Files and Login Paths](connecting/option-files-and-login-paths.md).

## Exit Status

`mariadb-shell` exits with status `0` when the session, command, script, or command line integration call completes successfully, and with a non-zero status when an error occurs, for example when the connection fails, a statement in a SQL script fails without `--force`, or a called function raises an error.

## Related Pages

* [Files and Environment Variables](files-and-environment-variables.md) lists the files and the `MARIADB_SHELL_*` environment variables that the shell uses.
* [Configuration Options](customizing/configuration-options.md) describes the options that you set with `shell.options` and persist in the configuration file.
