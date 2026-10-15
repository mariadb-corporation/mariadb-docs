---
description: >-
  The option files and groups that MariaDB Shell reads at startup, the options
  that control them, and how MariaDB Shell uses the ~/.mylogin.cnf file.
---

# Option Files and Login Paths

Like the other MariaDB clients, MariaDB Shell reads default options from `my.cnf`-style option files when it starts. You can keep the connection settings that you use every day, such as the user, the socket, or the TLS files, in an option file instead of typing them each time.

## Files

On Linux and macOS, MariaDB Shell reads the following files, in this order. Files that don't exist are skipped.

1. `/etc/my.cnf`
2. `/etc/mysql/my.cnf`
3. `my.cnf` in the directory named by the `MARIADB_HOME` environment variable or, if that is unset, by `MYSQL_HOME`
4. The file named by `--defaults-extra-file`
5. `~/.my.cnf`

On Windows, MariaDB Shell looks for `my.ini` and `my.cnf` in the Windows directory, in `C:\`, and in the installation directory.

To see the list for your build, run `mariadb-shell --help`. The end of the output names the files and the groups.

The usual option-file syntax applies, including the `!include` and `!includedir` directives.

## Groups

MariaDB Shell reads options from three groups:

| Group | Purpose |
| --- | --- |
| `[mariadb-shell]` | Options for MariaDB Shell only. |
| `[mysqlsh]` | Options written for MySQL Shell. MariaDB Shell reads this group so that existing files keep working. |
| `[client]` | Options shared by all MariaDB and MySQL clients. |

Other client groups, such as `[mysql]`, `[mariadb-client]`, and `[client-server]`, are ignored.

The groups don't have a priority over each other. MariaDB Shell applies the options in the order in which they appear, file by file, and a later setting overrides an earlier one. If `~/.my.cnf` sets `port` in `[client]` after `[mariadb-shell]`, the `[client]` value wins. To give a MariaDB Shell setting the last word, put the `[mariadb-shell]` group at the end of the file.

{% code title="~/.my.cnf" %}
```ini
[client]
user = dba
socket = /run/mysqld/mysqld.sock

[mariadb-shell]
ssl-mode = VERIFY_IDENTITY
ssl-ca = /etc/mysql/certs/ca.pem
connect-timeout = 5000
```
{% endcode %}

With this file, `mariadb-shell --sql` connects to the local server through the socket as `dba`, and `mariadb-shell -h db1.example.com --sql` connects to `db1.example.com` over TCP with the same account and TLS settings.

## What an Option File Can Contain

MariaDB Shell treats each option from a file like a command-line option of the same name, so you can use any option that `mariadb-shell --help` lists, not only the connection options. For example, `sql` or `py` selects the startup mode. Underscores in option names are converted to dashes, so `ssl_ca` and `ssl-ca` are equivalent.

{% hint style="warning" %}
An option that MariaDB Shell doesn't know stops the startup, even in the shared `[client]` group:

```text
While processing defaults options:
mariadb-shell: unknown option --default-character-set
```

To keep an option in `[client]` for other clients, prefix it with `loose-`, as in `loose-default-character-set = utf8mb4`. MariaDB Shell then ignores it.
{% endhint %}

When an option file supplies connection settings, and nothing else picks the session type, MariaDB Shell opens a classic session with them at startup.

## Precedence

Options from files have the lowest priority. Any option on the command line, including the parts of a URI, overrides the value from a file. A password from an option file is used only if the command line supplies no password and doesn't request a prompt with `-p`.

For the precedence of the command-line options among themselves, see [Connection URIs and Options](connection-uris-and-options.md#precedence).

## Controlling Which Files Are Read

The following options change which files MariaDB Shell reads. They must come before any other option on the command line.

| Option | Description |
| --- | --- |
| `--no-defaults` | Don't read any option file. |
| `--defaults-file=<file>` | Read only the given file. |
| `--defaults-extra-file=<file>` | Read the given file after the system-wide files and before `~/.my.cnf`. |
| `--defaults-group-suffix=<suffix>` | Also read the groups whose names end with the suffix, such as `[client_prod]` and `[mariadb-shell_prod]` for `--defaults-group-suffix=_prod`. |
| `--print-defaults` | Print the options that MariaDB Shell would take from the option files, and exit. |

Group suffixes let you keep the settings for several environments in one file:

{% code title="~/.my.cnf" %}
```ini
[client]
user = dba

[client_prod]
host = db1.example.com
ssl-mode = VERIFY_IDENTITY

[client_test]
host = test-db.example.com
```
{% endcode %}

```sh
mariadb-shell --defaults-group-suffix=_prod --sql
```

To check what the files contribute, use `--print-defaults`. MariaDB Shell masks any password in the output as `--password=*****`.

```sh
$ mariadb-shell --defaults-group-suffix=_prod --print-defaults
mariadb-shell would have been started with the following arguments:
--user=dba --host=db1.example.com --ssl-mode=VERIFY_IDENTITY
```

## Login Paths

MariaDB Shell doesn't support the `--login-path` option. Although `mariadb-shell --help` lists it among the option-file options, the shell rejects it at startup with `unknown option --login-path`. To switch between sets of connection settings, use `--defaults-group-suffix` or `--defaults-file`.

The file `~/.mylogin.cnf` has a different role in MariaDB Shell: on Linux, it is where the default credential store keeps the passwords that you save. MariaDB Shell reads and writes the file itself, in the format that MySQL's `mysql_config_editor` uses, so it needs no external tool. The connection settings in that file aren't applied at startup. See [Credential Store](credential-store.md) and [Credential Helpers](../appendix/credential-helpers.md#the-login-path-file).

{% hint style="warning" %}
The passwords in `~/.mylogin.cnf` are obfuscated, not encrypted: anyone who can read the file can recover them. Keep the file readable only by you.
{% endhint %}
