---
description: >-
  Complete guide to MariaDB option files. Complete my.cnf reference with
  configuration groups, parameter syntax, and file hierarchy for production use.
---

# Configuring MariaDB with Option Files

You can configure MariaDB to run the way you want by configuring the server with MariaDB's option files. The default MariaDB option file is called `my.cnf` on Unix-like operating systems and `my.ini` on Windows. Depending on how you've [installed](../) MariaDB, the default option file may be in a number of places, or it may not exist at all.

## Global Options Related to Option Files

The following options relate to how MariaDB handles option files. These options can be used with most of MariaDB's command-line tools, not just [mariadbd](../../starting-and-stopping-mariadb/mariadbd-options.md). They must be given as the first argument on the command-line:

| Option                                                                                                            | Description                                                                              |
| ----------------------------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------- |
| [--print-defaults](../../starting-and-stopping-mariadb/mariadbd-options.md#-print-defaults)                       | Read options from option files, print all option values, and then exit the program.      |
| [--no-defaults](../../starting-and-stopping-mariadb/mariadbd-options.md#-no-defaults)                             | Don't read options from any option file.                                                 |
| [--defaults-file](../../starting-and-stopping-mariadb/mariadbd-options.md#-defaults-file) =path                   | Only read options from the given option file.                                            |
| [--defaults-extra-file](../../starting-and-stopping-mariadb/mariadbd-options.md#-defaults-extra-file) =path       | Read this extra option file after all other option files are read.                       |
| [--defaults-group-suffix](../../starting-and-stopping-mariadb/mariadbd-options.md#-defaults-group-suffix) =suffix | In addition to the default option groups, also read option groups with the given suffix. |

## Default Option File Locations

MariaDB reads option files from many different directories by default. See the sections below to find out which directories are checked for which system.

For an exact list of option files read on your system by a specific program, you can execute a command like this (`$program` stands for any MariaDB program, including the Server):

```bash
$program --help --verbose
```

For example:

```bash
$ mariadbd --help --verbose
mariadbd  Ver 10.11.2-MariaDB for linux-systemd on x86_64 (MariaDB Server)
Copyright (c) 2000, 2018, Oracle, MariaDB Corporation Ab and others.

Starts the MariaDB database server.

Usage: mariadbd [OPTIONS]

Default options are read from the following files in the given order:
/etc/my.cnf ~/.my.cnf
The following groups are read: mysqld server mysqld-10.11 mariadb mariadb-10.11 mariadbd mariadbd-10.11 client-server galera
....
```

The option files are each scanned once, in the order given by `--help --verbose`. The effect of the configuration options is the same as if they would have been given as command-line options in the order they are found.

### Default Option File Locations on Linux, Unix, Mac

On Linux, Unix, or Mac OS X, the default option file is called `my.cnf`. MariaDB looks for the MariaDB option file in the locations and orders listed below.

The locations are dependent on whether the `DEFAULT_SYSCONFDIR` [cmake](../installing-mariadb/compiling-mariadb-from-source/generic-build-instructions.md#using-cmake) option was defined when MariaDB was built. This option is usually defined as `/etc` when building [RPM packages](../installing-mariadb/binary-packages/rpm/), but it is usually not defined when building [DEB packages](../installing-mariadb/binary-packages/installing-mariadb-deb-files.md) or [binary tarballs](../installing-mariadb/binary-packages/installing-mariadb-binary-tarballs.md).

* If the `DEFAULT_SYSCONFDIR` `cmake` option is **undefined**, MariaDB looks for the MariaDB option file in the following locations, and in the following order:

| Location               | Scope                                                                                                                             |
| ---------------------- | --------------------------------------------------------------------------------------------------------------------------------- |
| `/etc/my.cnf`          | Global                                                                                                                            |
| `/etc/mysql/my.cnf`    | Global                                                                                                                            |
| `$MARIADB_HOME/my.cnf` | Server (from MariaDB 10.6)                                                                                                        |
| `$MYSQL_HOME/my.cnf`   | Server (before MariaDB 10.6)                                                                                                      |
| `defaults-extra-file`  | File specified with [--defaults-extra-file](../../starting-and-stopping-mariadb/mariadbd-options.md#-defaults-extra-file), if any |
| `~/.my.cnf`            | User                                                                                                                              |

* If the `DEFAULT_SYSCONFDIR` `cmake` option is **defined**, MariaDB looks for the MariaDB option file in the following locations in the following order:

| Location                    | Scope                                                                                                                             |
| --------------------------- | --------------------------------------------------------------------------------------------------------------------------------- |
| `DEFAULT_SYSCONFDIR/my.cnf` | Global                                                                                                                            |
| `$MARIADB_HOME/my.cnf`      | Server (from MariaDB 10.6)                                                                                                        |
| `$MYSQL_HOME/my.cnf`        | Server (before MariaDB 10.6)                                                                                                      |
| `defaults-extra-file`       | File specified with [--defaults-extra-file](../../starting-and-stopping-mariadb/mariadbd-options.md#-defaults-extra-file), if any |
| `~/.my.cnf`                 | User                                                                                                                              |

* `MARIADB_HOME` or `MYSQL_HOME` is the [environment variable](mariadb-environment-variables.md) containing the path to the directory holding the server-specific `my.cnf` file. If `MYSQL_HOME` is not set, and the server is started with [mysqld\_safe](../../../clients-and-utilities/legacy-clients-and-utilities/mariadbd_safe.md), `MYSQL_HOME` is set as follows:
  * If there is a `my.cnf` file in the MariaDB data directory, but not in the MariaDB base directory, `MYSQL_HOME` is set to the MariaDB data directory.
  * Else, `MYSQL_HOME` is set to the MariaDB base directory.

{% hint style="warning" %}
Note that if `MARIADB_HOME` is set, `MYSQL_HOME` is not used, even if set.
{% endhint %}

### Default Option File Locations on Windows

On Windows, the option file can be called either `my.ini` or `my.cnf`. MariaDB looks for option files in the following locations, and in the following order:

| Location                        | Scope                                                                                                                             |
| ------------------------------- | --------------------------------------------------------------------------------------------------------------------------------- |
| System Windows Directory\my.ini | Global                                                                                                                            |
| System Windows Directory\my.cnf | Global                                                                                                                            |
| Windows Directory\my.ini        | Global                                                                                                                            |
| Windows Directory\my.cnf        | Global                                                                                                                            |
| `c:\my.ini`                     | Global                                                                                                                            |
| `c:\my.cnf`                     | Global                                                                                                                            |
| `installdir\my.ini`             | Server                                                                                                                            |
| `installdir\my.cnf`             | Server                                                                                                                            |
| `installdir\data\my.ini`        | Server                                                                                                                            |
| `installdir\data\my.cnf`        | Server                                                                                                                            |
| `%mariadb_home%\my.ini`         | Server (from MariaDB 10.6)                                                                                                        |
| `%mariadb_home%\my.cnf`         | Server (from MariaDB 10.6)                                                                                                        |
| `%mysql_home%\my.ini`           | Server                                                                                                                            |
| `%mysql_home%\my.cnf`           | Server                                                                                                                            |
| `defaults-extra-file`           | File specified with [--defaults-extra-file](../../starting-and-stopping-mariadb/mariadbd-options.md#-defaults-extra-file), if any |

* The `System Windows Directory` is the directory returned by the [GetSystemWindowsDirectory](https://docs.microsoft.com/en-us/windows/desktop/api/sysinfoapi/nf-sysinfoapi-getsystemwindowsdirectorya) function. The value is usually `C:\Windows`. To find its specific value on your system, open [cmd.exe](https://docs.microsoft.com/en-us/windows-server/administration/windows-commands/cmd) and execute:

```batch
echo %WINDIR%
```

* The `Windows Directory` is the directory returned by the `GetWindowsDirectory` function. The value may be a private `Windows Directory` for the application, or it may be the same as the `System Windows Directory` returned by the `GetSystemWindowsDirectory` function.
* `INSTALLDIR` is the parent directory of the directory where `mysqld.exe` is located. For example, if `mysqld.exe` is in `C:\Program Files\` , `INSTALLDIR` is `C:\Program Files\`.
* `MARIADB_HOME` or `MYSQL_HOME` is the [environment variable](mariadb-environment-variables.md) containing the path to the directory holding the server-specific `my.cnf` file.

{% hint style="warning" %}
Note that if `MARIADB_HOME` is set, `MYSQL_HOME` is not used, even if set.
{% endhint %}

## Default Option File Hierarchy

MariaDB looks in all of the above locations, in order, even if it has already found an option file, and it's possible for more than one option file to exist. For example, you could have an option file in `/etc/my.cnf` with global settings for all servers, and another option file in `~/.my.cnf` (that is, your user account's home directory) which specifies additional settings (or override previously specified settings) that are specific only to that user.

Option files are usually optional. However, if the [--defaults-file](../../starting-and-stopping-mariadb/mariadbd-options.md#defaults-file) option is set, but the file does not exist, MariaDB raises an error. If the `--defaults-file` option is set, MariaDB _only_ reads the option file referred to by this option.

If an option or system variable is not explicitly set, then it will be set to its default value. See [Server System Variables](../../../ha-and-performance/optimization-and-tuning/system-variables/server-system-variables.md) for a full list of all server system variables and their default values.

{% hint style="warning" %}
If an option is set multiple times, the later setting will override the earlier setting.
{% endhint %}

If [--log-basename](../../starting-and-stopping-mariadb/mariadbd-options.md#-log-basename) is set, there are various other log file naming options that, if set, should be placed **later** in the configuration file hierarchy. Later settings override earlier settings, so `log-basename` overrides any earlier log file name settings. See [--log-basename](../../starting-and-stopping-mariadb/mariadbd-options.md#-log-basename) for details.

## Custom Option File Locations

MariaDB can be configured to read options from custom options files with the following command-line arguments. These command-line arguments can be used with most of MariaDB's command-line tools, not just [mariadbd](../../starting-and-stopping-mariadb/mariadbd-options.md). They must be given as the first argument on the command line:

| Option                                                                                                      | Description                                                        |
| ----------------------------------------------------------------------------------------------------------- | ------------------------------------------------------------------ |
| [--defaults-file](../../starting-and-stopping-mariadb/mariadbd-options.md#-defaults-file) =path             | Only read options from the given option file.                      |
| [--defaults-extra-file](../../starting-and-stopping-mariadb/mariadbd-options.md#-defaults-extra-file) =path | Read this extra option file after all other option files are read. |

## Option File Syntax

The syntax of MariaDB option files is as follows:

* Lines starting with `#` are comments.
* Empty lines are ignored.
* Option groups use the syntax `[group-name]`. See the [Option Groups](configuring-mariadb-with-option-files.md#option-groups) section below for more information on available option groups.
* The same option group can appear multiple times.
* The `!include` directive can be used to include other option files. See the [Including Option Files](configuring-mariadb-with-option-files.md#including-option-files) section below for more information on this syntax.
* The `!includedir` directive can be used to include all `.cnf` files (and potentially `.ini` files) in a given directory. The option files within the directory are read in alphabetical order. See the [Including Option File Directories](configuring-mariadb-with-option-files.md#including-option-file-directories) section below for more information on this syntax.
* The `?includedir` (introduced in MariaDB 11.4.10 and 11.8.6) directive works like `!includedir` but skips unreadable files, instead of failing with an error.
* Dashes (`-`) and underscores (`_`) in options are interchangeable.
* Double quotes can be used to quote values
* `\n`, `\r`, `\t`, `\b`, `\s`, `\"`, `\'`, and `\\` are recognized as character escapes for new line, carriage return, tab, backspace, space, double quote, single quote, and backslash respectively.
* Certain option prefixes are supported. See the [Option Prefixes](configuring-mariadb-with-option-files.md#option-prefixes) section below for information about available option prefixes.
* See the [Options](configuring-mariadb-with-option-files.md#options) section below for information about available options.

## Option Groups

A MariaDB program can read options from one or many option groups. For an exact list of option groups read on your system by a specific program, you can execute (`$program` is a placeholder for any MariaDB program):

```bash
$program --help --verbose
```

For example:

```bash
$ mariadbd --help --verbose
mariadbd  Ver 10.11.2-MariaDB for linux-systemd on x86_64 (MariaDB Server)
Copyright (c) 2000, 2018, Oracle, MariaDB Corporation Ab and others.

Starts the MariaDB database server.

Usage: mariadbd [OPTIONS]

Default options are read from the following files in the given order:
/etc/my.cnf ~/.my.cnf
The following groups are read: mysqld server mysqld-10.11 mariadb mariadb-10.11 mariadbd mariadbd-10.11 client-server galera
....
```

### Server Option Groups

MariaDB programs reads server options from the following server option groups:

| Group            | Description                                                                                                                                                                                                                                                                                                                                                      |
| ---------------- | ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| \[client-server] | Options read by all MariaDB [client programs](../../../clients-and-utilities/) and the MariaDB Server. This is useful for options like socket and port, which is common between the server and the clients.                                                                                                                                                      |
| \[server]        | Options read by MariaDB Server.                                                                                                                                                                                                                                                                                                                                  |
| \[mysqld]        | Options read by mysqld, including both MariaDB Server and MySQL Server.                                                                                                                                                                                                                                                                                          |
| \[mysqld-X.Y]    | Options read by a specific version of mysqld, including both MariaDB Server and MySQL Server. For example, `[mariadb-11.4]`.                                                                                                                                                                                                                                     |
| \[mariadb]       | Options read by MariaDB Server.                                                                                                                                                                                                                                                                                                                                  |
| \[mariadb-X.Y]   | Options read by a specific version of MariaDB Server. For example, `[mariadb-11.4]`.                                                                                                                                                                                                                                                                             |
| \[mariadbd]      | Options read by MariaDB Server.                                                                                                                                                                                                                                                                                                                                  |
| \[mariadbd-X.Y]  | Options read by a specific version of MariaDB Server. For example, `[mariadbd-11.4]`.                                                                                                                                                                                                                                                                            |
| \[galera]        | Options read by MariaDB Server, but only if it is compiled with [Galera Cluster](https://app.gitbook.com/o/diTpXxF5WsbHqTReoBsS/s/3VYeeVGUV4AMqrA3zwy7/) support. All builds on Linux are compiled with Galera Cluster support. When using one of these builds, options from this option group are read even if the Galera Cluster functionality is not enabled. |

_X.Y_ in the examples above refer to the base (major.minor) version of the server. For example, MariaDB 11.4 would read from `[mariadb-11.4]`. By using the `mariadb-X.Y` syntax, you can create option files that have MariaDB-only options in the MariaDB-specific option groups. That would allow the option file to work for both MariaDB and MySQL.

### Client Option Groups

MariaDB programs reads client options from the following option groups:

| Group             | Description                                                                                                                                                              |
| ----------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------ |
| \[client]         | Options read by all MariaDB and MySQL [client programs](../../../clients-and-utilities/), including both MariaDB and MySQL clients. For example, mariadb-dump.           |
| \[client-server]  | Options read by all MariaDB client programs and the MariaDB Server. This is useful for options like socket and port, which is common between the server and the clients. |
| \[client-mariadb] | Options read by all MariaDB client programs.                                                                                                                             |

### Tool-Specific Option Groups

Many MariaDB tools reads options from their own option groups as well:

| Group              | Description                                                                                                                                                                                                                                                       |
| ------------------ | ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| \[mysqld\_safe]    | Options read by [mysqld\_safe](../../../clients-and-utilities/legacy-clients-and-utilities/mariadbd_safe.md), including both MariaDB Server and MySQL Server.                                                                                                     |
| \[safe\_mysqld]    | Options read by [mysqld\_safe](../../../clients-and-utilities/legacy-clients-and-utilities/mariadbd_safe.md), including both MariaDB Server and MySQL Server.                                                                                                     |
| \[mariadbd-safe]   | Options read by [mysqld\_safe](../../../clients-and-utilities/legacy-clients-and-utilities/mariadbd_safe.md) from MariaDB Server.                                                                                                                                 |
| \[mariadb\_safe]   | Options read by [mysqld\_safe](../../../clients-and-utilities/legacy-clients-and-utilities/mariadbd_safe.md) from MariaDB Server. Deprecated, please avoid using this.                                                                                            |
| \[mariadb-backup]  | Options read by [mariadb-backup](../../../server-usage/backup-and-restore/mariadb-backup/).                                                                                                                                                                       |
| \[xtrabackup]      | Options read by [mariadb-backup](../../../server-usage/backup-and-restore/mariadb-backup/) and Percona XtraBackup.                                                                                                                                                |
| \[mysql\_upgrade]  | Options read by [mysql\_upgrade](../../../clients-and-utilities/legacy-clients-and-utilities/mysql_upgrade.md), including both MariaDB Server and MySQL Server.                                                                                                   |
| \[mariadb-upgrade] | Options read by [mariadb-upgrade](../../../clients-and-utilities/deployment-tools/mariadb-upgrade.md).                                                                                                                                                            |
| \[sst]             | Specific options read by the [mariadb-backup SST method](https://app.gitbook.com/s/3VYeeVGUV4AMqrA3zwy7/high-availability/state-snapshot-transfers-ssts-in-galera-cluster/mariadb-backup-sst-method) and the xtrabackup-v2 SST method.                            |
| \[mysql]           | Options read by [mysql](../../../clients-and-utilities/mariadb-client/), including both MariaDB Server and MySQL Server.                                                                                                                                          |
| \[mariadb-client]  | Options read by [mariadb](../../../clients-and-utilities/mariadb-client/).                                                                                                                                                                                        |
| \[mysqldump]       | Options read by [mysqldump](../../../clients-and-utilities/legacy-clients-and-utilities/mysqldump.md), including both MariaDB Server and MySQL Server.                                                                                                            |
| \[mariadb-dump]    | Options read by [mariadb-dump](../../../clients-and-utilities/backup-restore-and-import-clients/mariadb-dump.md).                                                                                                                                                 |
| \[mysqlimport]     | Options read by [mysqlimport](../../../clients-and-utilities/legacy-clients-and-utilities/mysqlimport.md), including both MariaDB Server and MySQL Server.                                                                                                        |
| \[mariadb-import]  | Options read by [mariadb-import](../../../clients-and-utilities/backup-restore-and-import-clients/mariadb-import.md).                                                                                                                                             |
| \[mysqlbinlog]     | Options read by [mysqlbinlog](../../../clients-and-utilities/logging-tools/mariadb-binlog/), including both MariaDB Server and MySQL Server.                                                                                                                      |
| \[mariadb-binlog]  | Options read by [mariadb-binlog](../../../clients-and-utilities/logging-tools/mariadb-binlog/).                                                                                                                                                                   |
| \[mysqladmin]      | Options read by [mysqladmin](../../../clients-and-utilities/legacy-clients-and-utilities/mysqladmin.md), including both MariaDB Server and MySQL Server.                                                                                                          |
| \[mariadb-admin]   | Options read by [mariadb-admin](../../../clients-and-utilities/administrative-tools/mariadb-admin.md).                                                                                                                                                            |
| \[mysqlshow]       | Options read by [mysqlshow](../../../clients-and-utilities/legacy-clients-and-utilities/mysqlshow.md), including both MariaDB Server and MySQL Server.                                                                                                            |
| \[mariadb-show]    | Options read by [mariadb-show](../../../clients-and-utilities/administrative-tools/mariadb-show.md). Note that this program reads `[client]` group options, too.                                                                                                  |
| \[mysqlcheck]      | Options read by [mariadb-check](../../../clients-and-utilities/table-tools/mariadb-check.md), including both MariaDB Server and MySQL Server.                                                                                                                     |
| \[mariadb-check]   | Options read by [mariadb-check](../../../clients-and-utilities/table-tools/mariadb-check.md).                                                                                                                                                                     |
| \[mysqlslap]       | Options read by [mysqlslap](../../../clients-and-utilities/legacy-clients-and-utilities/mysqlslap.md), including both MariaDB Server and MySQL Server.                                                                                                            |
| \[mariadb-slap]    | Options read by [mariadb-slap](../../../clients-and-utilities/testing-tools/mariadb-slap.md).                                                                                                                                                                     |
| \[odbc]            | Options read by [MariaDB Connector/ODBC](https://app.gitbook.com/s/CjGYMsT2MVP4nd3IyW2L/mariadb-connector-odbc), but only if the [USE\_MYCNF](https://app.gitbook.com/s/CjGYMsT2MVP4nd3IyW2L/connectors-quickstart-guides/connector-odbc-guide) parameter is set. |

## Custom Option Group Suffixes

MariaDB can be configured to read options from option groups with a custom suffix by providing the following command-line argument. This command-line argument can be used with most of MariaDB's command-line tools, not just [mariadbd](../../starting-and-stopping-mariadb/mariadbd.md). It must be given as the first argument on the command line:

| Option                                                                                                            | Description                                                                              |
| ----------------------------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------- |
| [--defaults-group-suffix](../../starting-and-stopping-mariadb/mariadbd-options.md#-defaults-group-suffix) =suffix | In addition to the default option groups, also read option groups with the given suffix. |

The default group suffix can also be specified via the `MYSQL_GROUP_SUFFIX` [environment variable](mariadb-environment-variables.md).

**Example:** To create a custom prompt for the `mariadb` command-line client via a custom group, add this to the option file (for instance, `/etc/my.cnf`):

```ini
[client_custom_group]
prompt='(custom prompt for mariadb client)'
```

Then, launch `mariadb` like this:

```shellscript
mariadb --defaults-group-suffix=_custom_group
```

## Including Option Files

It is possible to include additional option files from another option file. For example, to include `/etc/mysql/dbserver1.cnf`, an option file could contain:

```ini
[mariadb]
...
!include /etc/mysql/dbserver1.cnf
```

## Including Option File Directories

It is also possible to include all option files in a directory from another option file. For example, to include all option files in `/etc/my.cnf.d/`, an option file could contain:

```ini
[mariadb]
...
!includedir /etc/my.cnf.d/
```

The option files within the directory are read in alphabetical order.

All option file names must end in `.cnf` on Unix-like operating systems. On Windows, all option file names must end in `.cnf` or `.ini`.

{% tabs %}
{% tab title="Current" %}
If a `.cnf` file cannot be read an executable (a MariaDB server or a client tool) will exit with an error. One can use `?includedir` to skip unreadable files without failing out.
{% endtab %}

{% tab title="< 11.4.10, < 11.8.6" %}
If a `.cnf` file cannot be read an executable (a MariaDB server or a client tool) will exit with an error.
{% endtab %}
{% endtabs %}

## Checking Program Options

You can check which options a given program is going to use by using the [--print-defaults](../../starting-and-stopping-mariadb/mariadbd-options.md#defaults-file) command-line argument:

| Option                                                                                      | Description                                                                         |
| ------------------------------------------------------------------------------------------- | ----------------------------------------------------------------------------------- |
| [--print-defaults](../../starting-and-stopping-mariadb/mariadbd-options.md#-print-defaults) | Read options from option files, print all option values, and then exit the program. |

This command-line argument can be used with most of MariaDB's command-line tools, not just [mariadbd](starting-and-stopping-mariadb/mariadbd-options.md). It must be given as the first argument on the command-line:

```bash
$ mariadb-dump --print-defaults
mariadb-dump would have been started with the following arguments:
--ssl_cert=/etc/my.cnf.d/certificates/client-cert.pem --ssl_key=/etc/my.cnf.d/certificates/client-key.pem --ssl_ca=/etc/my.cnf.d/certificates/ca.pem --ssl-verify-server-cert --max_allowed_packet=1G
```

You can also check which options a given program is going to use by using the [my\_print\_defaults](../../../clients-and-utilities/administrative-tools/my_print_defaults.md) utility, and providing the names of the option groups that the program reads:

```bash
$ my_print_defaults mariadb-dump client client-server client-mariadb
--ssl_cert=/etc/my.cnf.d/certificates/client-cert.pem
--ssl_key=/etc/my.cnf.d/certificates/client-key.pem
--ssl_ca=/etc/my.cnf.d/certificates/ca.pem
--ssl-verify-server-cert
--max_allowed_packet=1GB
```

The `my_print_defaults` utility's `--mariadbd` command-line option provides a shortcut to refer to all of the [server option groups](configuring-mariadb-with-option-files.md#server-option-groups):

```bash
$ my_print_defaults --mysqld
--log_bin=mariadb-bin
--log_slave_updates=ON
--ssl_cert=/etc/my.cnf.d/certificates/server-cert.pem
--ssl_key=/etc/my.cnf.d/certificates/server-key.pem
--ssl_ca=/etc/my.cnf.d/certificates/ca.pem
```

## Obfuscated Authentication Credential Option File

MySQL supports an obfuscated authentication credential option file called `.mylogin.cnf` that is created with [mysql\_config\_editor](https://dev.mysql.com/doc/refman/5.6/en/mysql-config-editor.html).

MariaDB does not support this. The passwords in MySQL's `.mylogin.cnf` are only obfuscated, rather than encrypted, so the feature does not really add much from a security perspective. It is more likely to give users a false sense of security, rather than to seriously protect them.

## Option Prefixes

MariaDB supports certain prefixes that can be used with options. The supported option prefixes are:

| Option Prefix                                                                | Description                                                                                     |
| ---------------------------------------------------------------------------- | ----------------------------------------------------------------------------------------------- |
| [autoset](../../starting-and-stopping-mariadb/mariadbd-options.md#-autoset-) | Sets the option value automatically. Only supported for certain options.                        |
| [disable](../../starting-and-stopping-mariadb/mariadbd-options.md#-disable-) | For all boolean options, disables the setting (equivalent to setting it to 0). Same as skip.    |
| [enable](../../starting-and-stopping-mariadb/mariadbd-options.md#-enable-)   | For all boolean options, enables the setting (equivalent to setting it to 1).                   |
| [loose](../../starting-and-stopping-mariadb/mariadbd-options.md#-loose-)     | Don't produce an error if the option doesn't exist.                                             |
| [maximum](../../starting-and-stopping-mariadb/mariadbd-options.md#-maximum-) | Sets the maximum value for the option.                                                          |
| [skip](../../starting-and-stopping-mariadb/mariadbd-options.md#-skip-)       | For all boolean options, disables the setting (equivalent to setting it to 0). Same as disable. |

For example:

```ini
[mariadb]
...
# determine a good value for open_files_limit automatically
autoset_open_files_limit

# disable the unix socket plugin
disable_unix_socket

# enable the slow query log
enable_slow_query_log

# don't produce an error if these options don't exist
loose_file_key_management_filename = /etc/mysql/encryption/keyfile.enc
loose_file_key_management_filekey = FILE:/etc/mysql/encryption/keyfile.key
loose_file_key_management_encryption_algorithm = AES_CTR

# set max_allowed_packet to maximum value
maximum_max_allowed_packet

# disable external locking for MyISAM
skip_external_locking
```

## Dashes and Underscores

Dashes (`-`) and underscores (`_`) **in option names** are interchangeable. Both variants can be used, for example:

```ini
[mariadbd]
debug-no-sync
debug_no_sync
```

The same is true for specifying **options on the command line**, for example:

```bash
mariadbd --debug-no-sync
mariadbd --debug_no_sync
```

{% hint style="info" %}
In option files, however, you must omit the leading double-dash (`--`).
{% endhint %}

This is only different when referring to system variables at runtime. Here, only underscores can be used, for example:

```sql
MariaDB [(none)]> SELECT @debug_no_sync;
+----------------+
| @debug_no_sync |
+----------------+
| NULL           |
+----------------+
1 row in set (0.002 sec)

MariaDB [(none)]> SELECT @debug-no-sync;
ERROR 1054 (42S22): Unknown column 'no' in 'SELECT'
```

If an option is not explicitly set, the server or client uses the default value for that option.

## MariaDB Server Options

MariaDB Server options can be set in [server option groups](configuring-mariadb-with-option-files.md#server-option-groups).

For a list of options that can be set for MariaDB Server, see the list of options available for [mariadbd](../../starting-and-stopping-mariadb/mariadbd-options.md).

Most of the [server system variables](../../../ha-and-performance/optimization-and-tuning/system-variables/server-system-variables.md) can also be set in MariaDB's option file.

## MariaDB Client Options

MariaDB client options can be set in [client option groups](configuring-mariadb-with-option-files.md#client-option-groups).

See the specific page for each [client program](../../../clients-and-utilities/) to determine what options are available for that program.

## Example Option Files

Most MariaDB installations include a sample MariaDB option file called `my-default.cnf`.

In source distributions, the sample option files are usually found in the `support-files` directory, and in other distributions, in the `share/mysql` directory that is relative to the MariaDB base installation directory.

You can copy one of these sample MariaDB option files and use it as the basis for building your server's primary MariaDB option file.

### Example Minimal Option File

Minimal `my.cnf` file that you can use to test MariaDB:

```ini
[client-server]
# Uncomment these if you want to use a nonstandard connection to MariaDB
#socket=/tmp/mysql.sock
#port=3306

# This will be passed to all MariaDB clients
[client]
#password=my_password

# The MariaDB server
[mysqld]
# Directory where you want to put your data
data=/usr/local/mysql/var
# Directory for the errmsg.sys file in the language you want to use
language=/usr/local/share/mysql/english

# This is the prefix name to be used for all log, error and replication files
log-basename=mysqld

# Enable logging by default to help find problems
general-log
log-slow-queries
```

### Example Hybrid Option File

The following is an extract of an option file that one can use if one wants to work with both MySQL and MariaDB.

```ini
# Example mysql config file.

[client-server]
socket=/tmp/mysql-dbug.sock
port=3307

# This will be passed to all mariadb clients
[client]
password=my_password

# Here are entries for some specific programs
# The following values assume you have at least 32M ram

# The MariaDB server
[mysqld]
temp-pool
key_buffer_size=16M
datadir=/my/mysqldata
loose-innodb_file_per_table

[mariadb]
datadir=/my/data
default-storage-engine=aria
loose-mutex-deadlock-detector
max-connections=20

[mariadb-5.5]
language=/my/maria-5.5/sql/share/english/
socket=/tmp/mysql-dbug.sock
port=3307

[mariadb-10.1]
language=/my/maria-10.1/sql/share/english/
socket=/tmp/mysql2-dbug.sock

[mysqldump]
quick
max_allowed_packet=16M

[mysql]
no-auto-rehash
loose-abort-source-on-error
```

## See Also

* [Configuring MariaDB Connector/C with Option Files](https://app.gitbook.com/s/CjGYMsT2MVP4nd3IyW2L/mariadb-connector-c/configuring-mariadb-connectorc-with-option-files)
* [Troubleshooting Connection Issues](../../../mariadb-quickstart-guides/mariadb-connection-troubleshooting-guide.md)
* [Configuring MariaDB for Remote Client Access](../../../server-usage/connecting/mariadb-remote-connection-guide-1.md)

<sub>_This page is licensed: CC BY-SA / Gnu FDL_</sub>

{% @marketo/form formId="4316" %}
