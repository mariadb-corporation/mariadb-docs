# mariadbd-multi

Before using mariadbd-multi be sure that you understand the meanings of the options that are passed to the mariadbd servers and why you would want to have separate mariadbd processes. Beware of the dangers of using multiple mariadbd servers with the same data directory. Use separate data directories, unless you know what you are doing. Starting multiple servers with the same data directory does not give you extra performance in a threaded system.

The `mariadbd-multi` startup script is in MariaDB distributions on Linux and Unix. It is a wrapper that is designed to manage several `mariadbd` processes running on the same host.

Prior to [MariaDB 10.5](https://app.gitbook.com/s/aEnK0ZXmUbJzqQrTjFyb/mariadb-community-server-release-notes/mariadb-10-5-series/what-is-mariadb-105), the client was called `mysqld_multi`. It can still be accessed under this name, via a symlink in Linux, or an alternate binary in Windows.

In order for multiple `mariadbd` processes to work on the same host, these processes must:

* Use different Unix socket files for local connections.
* Use different TCP/IP ports for network connections.
* Use different data directories.
* Use different process ID files (specified by the `--pid-file` option) if using [mariadbd-safe](mariadbd-safe.md) to start `mariadbd`.

`mariadbd-multi` can start or stop servers, or report their current status.

## Using mariadbd-multi

The command to use `mariadbd-multi` and the general syntax is:

```
mariadbd-multi [options] {start|stop|report} [GNR[,GNR] ...]
```

`start`, `stop`, and `report` indicate which operation to perform.

You can specify which servers to perform the operation on by providing one or more `GNR` values. `GNR` refers to an option group number, and it is explained more in the [option groups](mariadbd-multi.md#option-groups) section below. If there is no `GNR` list, then `mariadbd-multi` performs the operation for all `GNR` values found in its option files.

Multiple `GNR` values can be specified as a comma-separated list. `GNR` values can also be specified as a range by separating the numbers by a dash. There must not be any whitespace characters in the `GNR` list.

For example:

This command starts a single server using option group `[mariadbd17]`:

```
mariadbd-multi start 17
```

This command stops several servers, using option groups `[mariadbd8]` and `[mariadbd10]` through `[mariadbd13]`:

```
mariadbd-multi stop 8,10-13
```

### Options

`mariadbd-multi` supports the following options:

| Option                  | Description                                                                                                                                                                                                                                                                                                                                                                                                                                                                                              |
| ----------------------- | -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| Option                  | Description                                                                                                                                                                                                                                                                                                                                                                                                                                                                                              |
| --example               | Give an example of a config file with extra information.                                                                                                                                                                                                                                                                                                                                                                                                                                                 |
| --help                  | Display help and exit.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                   |
| --log=filename          | Specify the path and name of the log file. If the file exists, log output is appended to it.                                                                                                                                                                                                                                                                                                                                                                                                             |
| --mysqladmin=prog\_name | The [mariadb-admin](../../clients-and-utilities/administrative-tools/mariadb-admin.md) binary to be used to stop servers. Can be given within groups \[mariadbd#].                                                                                                                                                                                                                                                                                                                                       |
| --mariadbd=prog\_name   | The mariadbd binary to be used. Note that you can also specify [mariadbd-safe](mariadbd-safe.md) as the value for this option. If you use mariadbd-safe to start the server, you can include the mariadbd or ledir options in the corresponding \[mariadbdN] option group. These options indicate the name of the server that mariadbd-safe should start and the path name of the directory where the server is located. Example:\[mariadbd38]mariadbd = mariadbd-debugledir = /opt/local/mysql/libexec. |
| --no-log                | Print to stdout instead of the log file. By default the log file is turned on.                                                                                                                                                                                                                                                                                                                                                                                                                           |
| --password=password     | The password of the MariaDB account to use when invoking [mariadb-admin](../../clients-and-utilities/administrative-tools/mariadb-admin.md). Note that the password value is not optional for this option, unlike for other MariaDB programs.                                                                                                                                                                                                                                                            |
| --silent                | Silent mode; disable warnings.                                                                                                                                                                                                                                                                                                                                                                                                                                                                           |
| --tcp-ip                | Connect to the MariaDB server(s) via the TCP/IP port instead of the UNIX socket. This affects stopping and reporting. If a socket file is missing, the server may still be running, but can be accessed only via the TCP/IP port. By default connecting is done via the UNIX socket. This option affects stop and report operations.                                                                                                                                                                     |
| --user=username         | The user name of the MariaDB account to use when invoking [mariadb-admin](../../clients-and-utilities/administrative-tools/mariadb-admin.md).                                                                                                                                                                                                                                                                                                                                                            |
| --verbose               | Be more verbose.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                         |
| --version               | Display version information and exit.                                                                                                                                                                                                                                                                                                                                                                                                                                                                    |
| --wsrep-new-cluster     | Bootstrap a cluster. Added in [MariaDB 10.1.15](https://app.gitbook.com/s/aEnK0ZXmUbJzqQrTjFyb/mariadb-community-server-release-notes/old-releases/release-notes-mariadb-10-1-series/mariadb-10115-release-notes).                                                                                                                                                                                                                                                                                       |

### Option Files

In addition to reading options from the command-line, `mariadbd-multi` can also read options from [option files](../install-and-upgrade-mariadb/configuring-mariadb/configuring-mariadb-with-option-files.md). If an unknown option is provided to `mariadbd-multi` in an option file, then it is ignored.

The following options relate to how MariaDB command-line tools handles option files. They must be given as the first argument on the command-line:

| Option                    | Description                                                                         |
| ------------------------- | ----------------------------------------------------------------------------------- |
| Option                    | Description                                                                         |
| --print-defaults          | Print the program argument list and exit.                                           |
| --no-defaults             | Don't read default options from any option file.                                    |
| --defaults-file=#         | Only read default options from the given file #.                                    |
| --defaults-extra-file=#   | Read this file after the global files are read.                                     |
| --defaults-group-suffix=# | In addition to the default option groups, also read option groups with this suffix. |

#### Option Groups

`mariadbd-multi` reads options from the following [option groups](../install-and-upgrade-mariadb/configuring-mariadb/configuring-mariadb-with-option-files.md#option-groups) from [option files](../install-and-upgrade-mariadb/configuring-mariadb/configuring-mariadb-with-option-files.md):

| Group            | Description                                                                         |
| ---------------- | ----------------------------------------------------------------------------------- |
| Group            | Description                                                                         |
| \[mysqld\_multi] | Options read by mysqld\_multi, which includes both MariaDB Server and MySQL Server. |

`mariadbd-multi` also searches [option files](../install-and-upgrade-mariadb/configuring-mariadb/configuring-mariadb-with-option-files.md) for [option groups](../install-and-upgrade-mariadb/configuring-mariadb/configuring-mariadb-with-option-files.md#option-groups) with names like `[mariadbdN]`, where `N` can be any positive integer. This number is referred to in the following discussion as the option group number, or `GNR`:

| Group      | Description                                                                                                                                          |
| ---------- | ---------------------------------------------------------------------------------------------------------------------------------------------------- |
| Group      | Description                                                                                                                                          |
| \[mysqldN] | Options read by a mysqld instance managed by mysqld\_multi, which includes both MariaDB Server and MySQL Server. The N refers to the instance's GNR. |

`GNR` values distinguish option groups from one another and are used as arguments to `mariadbd-multi` to specify which servers you want to start, stop, or obtain a status report for. The `GNR` value should be the number at the end of the option group name in the option file. For example, the `GNR` for an option group named `[mariadbd17]` is `17`.

Options listed in these option groups are the same that you would use in the regular server option groups used for configuring `mariadbd`. However, when using multiple servers, it is necessary that each one use its own value for options such as the Unix socket file and TCP/IP port number.

The `[mariadbd-multi]` option group can be used for options that are needed for `mariadbd-multi` itself. `[mariadbdN]` option groups can be used for options passed to specific `mariadbd` instances.

The regular server [option groups](../install-and-upgrade-mariadb/configuring-mariadb/configuring-mariadb-with-option-files.md#option-groups) can also be used for common options that are read by all instances:

| Group            | Description                                                                                                                                                                                                                                                                |
| ---------------- | -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| Group            | Description                                                                                                                                                                                                                                                                |
| \[mysqld]        | Options read by mysqld, which includes both MariaDB Server and MySQL Server.                                                                                                                                                                                               |
| \[server]        | Options read by MariaDB Server.                                                                                                                                                                                                                                            |
| \[mysqld-X.Y]    | Options read by a specific version of mysqld, which includes both MariaDB Server and MySQL Server. For example, \[mysqld-5.5].                                                                                                                                             |
| \[mariadb]       | Options read by MariaDB Server.                                                                                                                                                                                                                                            |
| \[mariadb-X.Y]   | Options read by a specific version of MariaDB Server.                                                                                                                                                                                                                      |
| \[client-server] | Options read by all MariaDB [client programs](https://github.com/mariadb-corporation/docs-server/blob/test/kb/en/clients-utilities/README.md) and the MariaDB Server. This is useful for options like socket and port, which is common between the server and the clients. |
| \[galera]        | Options read by a galera-capable MariaDB Server. Available on systems compiled with Galera support.                                                                                                                                                                        |

For an example of how you might set up an option file, use this command:

```
mariadbd-multi --example
```

### Authentication and Privileges

Make sure that the MariaDB account used for stopping the `mariadbd` processes (with the [mariadb-admin](../../clients-and-utilities/administrative-tools/mariadb-admin.md) utility) has the same user name and password for each server. Also, make sure that the account has the `SHUTDOWN` privilege. If the servers that you want to manage have different user names or passwords for the administrative accounts, you might want to create an account on each server that has the same user name and password. For example, you might set up a common `multi_admin` account by executing the following commands for each server:

```
shell> mysql -u root -S /tmp/mysql.sock -p
Enter password:
mysql> GRANT SHUTDOWN ON *.*
 -> TO ´multi_admin´@´localhost´ IDENTIFIED BY ´multipass´;
```

Change the connection parameters appropriately when connecting to each one. Note that the host name part of the account name must allow you to connect as `multi_admin` from the host where you want to run `mariadbd-multi`.

## User Account

Make sure that the data directory for each server is fully accessible to the Unix account that the specific `mariadbd` process is started as. If you run the `mariadbd-multi` script as the Unix `root` account, and if you want the `mariadbd` process to be started with another Unix account, then you can use the `--user` option with `mariadbd`. If you specify the `--user` option in an option file, and if you did not run the `mariadbd-multi` script as the Unix `root` account, then it will just log a warning and the `mariadbd` processes are started under the original Unix account.

Do not run the `mariadbd` process as the Unix `root` account, unless you know what you are doing.

## Example

The following example shows how you might set up an option file for use with mariadbd-multi. The order in which the mariadbd programs are started or stopped depends on the order in which they appear in the option file. Group numbers need not form an unbroken sequence. The first and fifth \[mariadbdN] groups were intentionally omitted from the example to illustrate that you can have “gaps” in the option file. This gives you more flexibility.

```
# This file should probably be in your home dir (~/.my.cnf)
           # or /etc/my.cnf
           # Version 2.1 by Jani Tolonen
           [mariadbd-multi]
           mariadbd     = /usr/local/bin/mariadbd-safe
           mysqladmin = /usr/local/bin/mysqladmin
           user       = multi_admin
           password   = multipass
           [mariadbd2]
           socket     = /tmp/mysql.sock2
           port       = 3307
           pid-file   = /usr/local/mysql/var2/hostname.pid2
           datadir    = /usr/local/mysql/var2
           language   = /usr/local/share/mysql/english
           user       = john
           [mariadbd3]
           socket     = /tmp/mysql.sock3
           port       = 3308
           pid-file   = /usr/local/mysql/var3/hostname.pid3
           datadir    = /usr/local/mysql/var3
           language   = /usr/local/share/mysql/swedish
           user       = monty
           [mariadbd4]
           socket     = /tmp/mysql.sock4
           port       = 3309
           pid-file   = /usr/local/mysql/var4/hostname.pid4
           datadir    = /usr/local/mysql/var4
           language   = /usr/local/share/mysql/estonia
           user       = tonu
           [mariadbd6]
           socket     = /tmp/mysql.sock6
           port       = 3311
           pid-file   = /usr/local/mysql/var6/hostname.pid6
           datadir    = /usr/local/mysql/var6
           language   = /usr/local/share/mysql/japanese
           user       = jani
```

<sub>_This page is licensed: CC BY-SA / Gnu FDL_</sub>

{% @marketo/form formId="4316" %}
