---
description: >-
  Details the `mariadbd-safe` wrapper script, which adds safety features like
  auto-restart upon crash and error logging to syslog.
---

# mariadbd-safe

The `mariadbd-safe` startup script is in MariaDB distributions on Linux and Unix. It is a wrapper that starts `mariadbd` with some extra safety features. For example, if `mariadbd-safe` notices that `mariadbd` has crashed, then `mariadbd-safe` automatically restarts `mariadbd`.

`mariadbd-safe` is the recommended way to start `mariadbd` on Linux and Unix distributions that do not support [systemd](systemd.md). Additionally, the [mysql.server](mysql-server.md) init script used by [sysVinit](sysvinit.md) starts `mariadbd` with `mariadbd-safe` by default.

{% hint style="info" %}
Previously, the client used to be called `mysqld_safe`, and can still be accessed under this name, via a symlink in Linux, or an alternate binary in Windows.
{% endhint %}

## Using mariadbd-safe

The command to use `mariadbd-safe` and the general syntax is:

{% code overflow="wrap" %}
```
mariadbd-safe [ --no-defaults | --defaults-file | --defaults-extra-file | --defaults-group-suffix | --print-defaults ] <options> <mariadbd_options>
```
{% endcode %}

### Options

Many of the options supported by `mariadbd-safe` are identical to\
options supported by [mariadbd](mariadbd-options.md). If an unknown option is provided to `mariadbd-safe` on the command-line, then it is passed to `mariadbd`.

`mariadbd-safe` supports the following options:

| Option                                   | Description                                                                                                                                                                                                                                                                                                                                                                                |
| ---------------------------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ |
| --help                                   | Display a help message and exit.                                                                                                                                                                                                                                                                                                                                                           |
| --autoclose                              | (NetWare only) On NetWare, mariadbd-safe provides a screen presence. When you unload (shut down) the mariadbd-safe NLM, the screen does not by default go away. Instead, it prompts for user input: NLM has terminated; Press any key to close the screen. If you want NetWare to close the screen automatically instead, use the --autoclose option to mariadbd-safe.                     |
| --basedir=path                           | The path to the MariaDB installation directory.                                                                                                                                                                                                                                                                                                                                            |
| --core-file-size=size                    | The size of the core file that mariadbd should be able to create. The option value is passed to ulimit -c.                                                                                                                                                                                                                                                                                 |
| --crash-script=file                      | Script to call in the event of mariadbd crashing.                                                                                                                                                                                                                                                                                                                                          |
| --datadir=path                           | The path to the data directory.                                                                                                                                                                                                                                                                                                                                                            |
| --defaults-extra-file=path               | The name of an option file to be read in addition to the usual option files. This must be the first option on the command line if it is used. If the file does not exist or is otherwise inaccessible, the server will exit with an error.                                                                                                                                                 |
| --defaults-file=file\_name               | The name of an option file to be read instead of the usual option files. This must be the first option on the command line if it is used.                                                                                                                                                                                                                                                  |
| --defaults-group-suffix=#                | In addition to the default option groups, also read option groups with this suffix.                                                                                                                                                                                                                                                                                                        |
| --flush-caches                           | Flush and purge buffers/caches before starting the server.                                                                                                                                                                                                                                                                                                                                 |
| --ledir=path                             | If mariadbd-safe cannot find the server, use this option to indicate the path name to the directory where the server is located.                                                                                                                                                                                                                                                           |
| --log-error=file\_name                   | Write the error log to the given file.                                                                                                                                                                                                                                                                                                                                                     |
| --malloc-lib=lib                         | Preload shared library lib if available. See [debugging MariaDB](https://app.gitbook.com/s/WCInJQ9cmGjq1lsTG91E/development-articles/debugging-mariadb/debugging-a-running-server-on-linux) for an example.                                                                                                                                                                                |
| --mysqld=prog\_nam                       | The name of the server program (in the ledir directory) that you want to start. This option is needed if you use the MariaDB binary distribution but have the data directory outside of the binary distribution. If mariadbd-safe cannot find the server, use the --ledir option to indicate the path name to the directory where the server is located.                                   |
| --mysqld-version=suffix                  | This option is similar to the --mysqld option, but you specify only the suffix for the server program name. The basename is assumed to be mysqld. For example, if you use--mysqld-version=debug, mariadbd-safe starts the mariadbd-debug program in the ledir directory. If the argument to --mysqld-version is empty, mariadbd-safe uses mysqld in the ledir directory.                   |
| --nice=priority                          | Use the nice program to set the server´s scheduling priority to the given value.                                                                                                                                                                                                                                                                                                           |
| --no-defaults                            | Do not read any option files. This must be the first option on the command line if it is used.                                                                                                                                                                                                                                                                                             |
| --no-watch, --nowatch, --no-auto-restart | Exit after starting mariadbd.                                                                                                                                                                                                                                                                                                                                                              |
| --numa-interleave                        | Run mariadbd with its memory interleaved on all NUMA nodes.                                                                                                                                                                                                                                                                                                                                |
| --open-files-limit=count                 | The number of files that mariadbd should be able to open. The option value is passed to ulimit -n. Note that you need to start mariadbd-safe as root for this to work properly.                                                                                                                                                                                                            |
| --pid-file=file\_name                    | The path name of the process ID file.                                                                                                                                                                                                                                                                                                                                                      |
| --plugin-dir=dir\_name                   | Directory for client-side plugins.                                                                                                                                                                                                                                                                                                                                                         |
| --port=port\_num                         | The port number that the server should use when listening for TCP/IP connections. The port number must be 1024 or higher unless the server is started by the root system user.                                                                                                                                                                                                             |
| --print-defaults                         | Print the program argument list and exit.                                                                                                                                                                                                                                                                                                                                                  |
| --skip-kill-mysqld                       | Do not try to kill stray mariadbd processes at startup. This option works only on Linux.                                                                                                                                                                                                                                                                                                   |
| --socket=path                            | The Unix socket file that the server should use when listening for local connections.                                                                                                                                                                                                                                                                                                      |
| --syslog, --skip-syslog                  | --syslog causes error messages to be sent to syslog on systems that support the logger program. --skip-syslog suppresses the use of syslog; messages are written to an error log file.                                                                                                                                                                                                     |
| --syslog-tag=tag                         | For logging to syslog, messages from mariadbd-safe and mariadbd are written with a tag of mariadbd-safe and mariadbd, respectively. To specify a suffix for the tag, use --syslog-tag=tag, which modifies the tags to be mariadbd-safe-tag and mariadbd-tag.                                                                                                                               |
| --timezone=timezone                      | Set the TZ time zone [environment variable](../install-and-upgrade-mariadb/configuring-mariadb/mariadb-environment-variables.md) to the given option value. Consult your operating system documentation for legal time zone specification formats. Also see [Time Zones](../../reference/data-types/string-data-types/character-sets/internationalization-and-localization/time-zones.md). |
| --user={user\_name or user\_id}          | Run the mariadbd server as the user having the name user\_name or the numeric user ID user\_id. (“User” in this context refers to a system login account, not a MariaDB user listed in the grant tables.)                                                                                                                                                                                  |

### Option Files

In addition to reading options from the command-line, `mariadbd-safe` can also read options from [option files](../install-and-upgrade-mariadb/configuring-mariadb/configuring-mariadb-with-option-files.md). If an unknown option is provided to `mariadbd-safe` in an option file, then it is ignored.

The following options relate to how MariaDB command-line tools handles option files. They must be given as the **first argument** on the command-line:

| Option                    | Description                                                                         |
| ------------------------- | ----------------------------------------------------------------------------------- |
| --print-defaults          | Print the program argument list and exit.                                           |
| --no-defaults             | Don't read default options from any option file.                                    |
| --defaults-file=#         | Only read default options from the given file #.                                    |
| --defaults-extra-file=#   | Read this file after the global files are read.                                     |
| --defaults-group-suffix=# | In addition to the default option groups, also read option groups with this suffix. |

#### Option Groups

`mariadbd-safe` reads options from the following [option groups](../install-and-upgrade-mariadb/configuring-mariadb/configuring-mariadb-with-option-files.md#option-groups) from [option files](../install-and-upgrade-mariadb/configuring-mariadb/configuring-mariadb-with-option-files.md):

| Group            | Description                                                                                                                                                                                                                                    |
| ---------------- | ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| \[mysqld\_safe]  | Options read by mysqld\_safe, which includes both MariaDB Server and MySQL Server.                                                                                                                                                             |
| \[safe\_mysqld]  | Options read by mysqld\_safe, which includes both MariaDB Server and MySQL Server.                                                                                                                                                             |
| \[mariadbd-safe] | Options read by mariadbd\_safe\_safe from MariaDB Server. Available starting with [MariaDB 10.4.6](https://app.gitbook.com/s/aEnK0ZXmUbJzqQrTjFyb/community-server/old-releases/release-notes-mariadb-10-4-series/mariadb-1046-release-notes). |
| \[mariadb-safe]  | Options read by mysqld\_safe from MariaDB Server. Deprecated, please avoid using this.                                                                                                                                                         |

The `[safe_mariadbd]` option group is primarily supported for backward compatibility. You should rename such option groups to `[mariadbd-safe]` in MariaDB installations to prevent breakage in the future if this compatibility is removed.

`mariadbd-safe` also reads options from the following server [option groups](../install-and-upgrade-mariadb/configuring-mariadb/configuring-mariadb-with-option-files.md#option-groups) from [option files](../install-and-upgrade-mariadb/configuring-mariadb/configuring-mariadb-with-option-files.md):

| Group            | Description                                                                                                                                                                                                             |
| ---------------- | ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| \[mysqld]        | Options read by mysqld, which includes both MariaDB Server and MySQL Server.                                                                                                                                            |
| \[server]        | Options read by MariaDB Server.                                                                                                                                                                                         |
| \[mysqld-X.Y]    | Options read by a specific version of mysqld, which includes both MariaDB Server and MySQL Server. For example, \[mysqld-5.5].                                                                                          |
| \[mariadb]       | Options read by MariaDB Server.                                                                                                                                                                                         |
| \[mariadb-X.Y]   | Options read by a specific version of MariaDB Server.                                                                                                                                                                   |
| \[client-server] | Options read by all MariaDB [client programs](../../clients-and-utilities/mariadb-client/) and the MariaDB Server. This is useful for options like socket and port, which is common between the server and the clients. |
| \[galera]        | Options read by a galera-capable MariaDB Server. Available on systems compiled with Galera support.                                                                                                                     |

For example, if you specify the [log\_error](../../ha-and-performance/optimization-and-tuning/system-variables/server-system-variables.md#log_error) option in a server option group in an option file, like this:

```ini
[mariadb]
log_error=error.log
```

Then `mariadbd-safe` also uses this value for its own `--log-error` option:

### Configuring the Open Files Limit

When using `mariadbd-safe`, the system's open files limit can be changed by providing the `--open-files-limit` option either on the command-line or in an option file. For example:

```ini
[mariadbd-safe]
open_files_limit=4294967295
```

The option value is passed to `ulimit -n`. Note that you need to start `mariadbd-safe` as root for this to work properly. However, you can't currently set this to `unlimited`. See [MDEV-18410](https://jira.mariadb.org/browse/MDEV-18410) about that.

When `mariadbd-safe` starts `mariadbd`, it also uses this option to set the value of the [open\_files\_limit](../../ha-and-performance/optimization-and-tuning/system-variables/server-system-variables.md#open_files_limit) system variable for `mariadbd`.

### Configuring the Core File Size

When using `mariadbd-safe`, if you would like to [enable core dumps](https://app.gitbook.com/s/WCInJQ9cmGjq1lsTG91E/development-articles/debugging-mariadb/enabling-core-dumps), the system's core file size limit can be changed by providing the `--core-file-size` option either on the command-line or in an option file. For example:

```ini
[mariadbd-safe]
core_file_size=unlimited
```

The option value is passed to `ulimit -c`. Note that you need to start `mariadbd-safe` as root for this to work properly.

### Configuring MariaDB to Write the Error Log to Syslog

When using `mariadbd-safe`, if you would like to redirect the error log to the [syslog](https://linux.die.net/man/8/rsyslogd), then that can easily be done by using the `--syslog` option. `mariadbd-safe` redirects two types of log messages to the syslog--its own log messages, and log messages for `mariadbd`.

* `mariadbd-safe` configures its own log messages to go to the `daemon` syslog facility. The log level for these messages is either `notice` or `error`, depending on the specific type of log message. The default tag is `mariadbd-safe`.
* `mariadbd-safe` also configures the log messages for `mariadbd` to go to the `daemon` syslog facility. The log level for these messages is `error`. The default tag is `mariadbd`.

Sometimes it can be helpful to add a suffix to the syslog tag, such as if you are running multiple instances of MariaDB on the same host. To add a suffix to each syslog tag, use the `--syslog-tag` option.

## Specifying mariadbd

By default, `mariadbd-safe` tries to start an executable named `mariadbd`.

You can also specify another executable for `mariadbd-safe` to start instead of `mariadbd` by providing the `--mariadbd` or `--mariadbd-version` options either on the command-line or in an option file.

By default, it will look for `mariadbd` in the following locations in the following order:

* `$BASEDIR/libexec/mysqld`
* `$BASEDIR/sbin/mysqld`
* `$BASEDIR/bin/mysqld`
* `$PWD/bin/mysqld`
* `$PWD/libexec/mysqld`
* `$PWD/sbin/mysqld`
* `@libexecdir@/mysql`

Where `$BASEDIR` is set by the `--basedir` option, `$PWD` is the current working directory where `mariadbd-safe` was invoked, and `@libexecdir@` is set at compile-time by the `INSTALL_BINDIR` option for [cmake](../compiling-mariadb-from-source/generic-build-instructions.md#using-cmake).

You can also specify where the executable is located by providing the `--ledir` option either on the command-line or in an option file.

## Specifying datadir

By default, `mariadbd-safe` will look for the `datadir` in the following locations in the following order:

* `$BASEDIR/data/mysql`
* `$BASEDIR/data`
* `$BASEDIR/var/mysql`
* `$BASEDIR/var`
* `@localstatedir@`

Where `$BASEDIR` is set by the `--basedir` option, and `@localstatedir@` is set at compile-time by the `INSTALL_MYSQLDATADIR` option for [cmake](../compiling-mariadb-from-source/generic-build-instructions.md#using-cmake).

You can also specify where the `datadir` is located by providing the `--datadir` option either on the command-line or in an option file.

## Logging

When you use `mariadbd-safe` to start `mariadbd`, `mariadbd-safe` logs to the same destination as `mariadbd`.

`mariadbd-safe` has several log-related options:

* `--syslog`: Write error messages to syslog on systems that\
  support the logger program.
* `--skip-syslog`: Do not write error messages to syslog.\
  Messages are written to the default error log file (host\_name.err in the data\
  directory), or to a named file if the `--log-error` option\
  is given.
* `--log-error=file_name`: Write error messages to the named\
  error file.

If none of these options is provided, then the default is `--skip-syslog`.

If `--syslog` and `--log-error` are both provided, then a warning is issued and `--log-error` takes precedence.

`mariadbd-safe` also writes notices to `stdout` and errors to `stderr`.

## Editing mariadbd-safe

`mariadbd-safe` is a `sh` script, so if you need to change its behavior, then it can easily be edited. However, you should not normally edit the script. A lot of behavior can be changed by providing options either on the command-line or in an option file.

If you do edit `mariadbd-safe`, then you should be aware of the fact that a package upgrade can overwrite your changes. If you would like to preserve your changes, be sure to have a backup.

## NetWare

On NetWare, mariadbd-safe is a NetWare Loadable Module (NLM)\
that is ported from the original Unix shell script. It starts the server as\
follows:

1. Runs a number of system and option checks.
2. Runs a check on MyISAM tables.
3. Provides a screen presence for the MariaDB server.
4. Starts mariadbd, monitors it, and restarts it if it terminates in error.
5. Sends error messages from mariadbd to the host\_name.err file in the data directory.
6. Sends mariadbd-safe screen output to the host\_name.safe file\
   in the data directory.

## See Also

* [How to increase max number of open files on Linux](https://www.cyberciti.biz/faq/linux-increase-the-maximum-number-of-open-files). This can be used to solve issues like this warning from mariadbd: `Changed limits: max_open_files: 1024 (requested 5000)"`
* [mariadbd Options](mariadbd-options.md)
* [systemd](systemd.md)

<sub>_This page is licensed: CC BY-SA / Gnu FDL_</sub>

{% @marketo/form formId="4316" %}
