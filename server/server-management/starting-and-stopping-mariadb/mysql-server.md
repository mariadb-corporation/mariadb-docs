---
description: >-
  Documentation for the `mysql.server` script, a SysVinit-style wrapper used to
  start and stop `mariadbd-safe`.
---

# mysql.server

The [mysql.server](mysql-server.md) startup script is in MariaDB distributions on Linux and Unix. It is a wrapper that works as a standard [sysVinit](sysvinit.md) script. However, it can be used independently of [sysVinit](sysvinit.md) as a regular `sh` script. The script starts the [mariadbd](mariadbd-options.md) server process by first changing its current working directory to the MariaDB install directory and then starting [mariadbd-safe](mariadbd-safe.md). The script requires the standard [sysVinit](sysvinit.md) arguments, such as `start`, `stop`, `restart`, and `status`. For example:

```bash
mysql.server start
mysql.server restart
mysql.server stop
mysql.server status
```

It can be used on systems such as Linux, Solaris, and Mac OS X.

The `mysql.server` script starts [mariadbd](mariadbd-options.md) by first changing to the MariaDB install directory and then calling [mariadbd-safe](mariadbd-safe.md).

## Using mysql.server

The command to use `mysql.server` and the general syntax is:

{% code overflow="wrap" %}
```bash
mysql.server [ start | stop | restart | status ] <options> <mariadbd_options>
```
{% endcode %}

### Options

If an unknown option is provided to `mariadbd-safe` on the command-line, it is passed to `mariadbd-safe`.

`mysql.server` supports the following options:

| Option                               | Description                                                                                                                                                                                                                                                                      |
| ------------------------------------ | -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| --basedir=path                       | The path to the MariaDB installation directory.                                                                                                                                                                                                                                  |
| --datadir=path                       | The path to the MariaDB data directory.                                                                                                                                                                                                                                          |
| --pid-file=file\_name                | The path name of the file in which the server should write its process ID. If not provided, the default, host\_name.pid is used.                                                                                                                                                 |
| --service-startup-timeout=file\_name | How long in seconds to wait for confirmation of server startup. If the server does not start within this time, mysql.server exits with an error. The default value is 900. A value of 0 means not to wait at all for startup. Negative values mean to wait forever (no timeout). |
| --use-mysqld\_safe                   | Use [mariadbd-safe](mariadbd-safe.md) to start the server. This is the default.                                                                                                                                                                                                  |
| --use-manager                        | Use Instance Manager to start the server.                                                                                                                                                                                                                                        |
| --user=user\_name                    | The login user name to use for running mariadbd.                                                                                                                                                                                                                                 |

### Option Files

In addition to reading options from the command-line, `mysql.server` can also read options from [option files](../install-and-upgrade-mariadb/configuring-mariadb/configuring-mariadb-with-option-files.md).

The following options relate to how MariaDB command-line tools handles option files. They must be given as the first argument on the command-line:

| Option                  | Description                                      |
| ----------------------- | ------------------------------------------------ |
| --print-defaults        | Print the program argument list and exit.        |
| --no-defaults           | Don't read default options from any option file. |
| --defaults-file=#       | Only read default options from the given file #. |
| --defaults-extra-file=# | Read this file after the global files are read.  |

#### Option Groups

`mysql.server` reads options from the following [option groups](../install-and-upgrade-mariadb/configuring-mariadb/configuring-mariadb-with-option-files.md#option-groups) from [option files](../install-and-upgrade-mariadb/configuring-mariadb/configuring-mariadb-with-option-files.md):

| Group           | Description                                                                        |
| --------------- | ---------------------------------------------------------------------------------- |
| \[mysql.server] | Options read by mysql.server, which includes both MariaDB Server and MySQL Server. |

`mysql.server` also reads options from the following server [option groups](../install-and-upgrade-mariadb/configuring-mariadb/configuring-mariadb-with-option-files.md#option-groups) from [option files](../install-and-upgrade-mariadb/configuring-mariadb/configuring-mariadb-with-option-files.md):

| Group            | Description                                                                                                                                                                                                                                                                |
| ---------------- | -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| \[mysqld]        | Options read by mysqld, which includes both MariaDB Server and MySQL Server.                                                                                                                                                                                               |
| \[server]        | Options read by MariaDB Server.                                                                                                                                                                                                                                            |
| \[mysqld-X.Y]    | Options read by a specific version of mysqld, which includes both MariaDB Server and MySQL Server. For example, \[mysqld-5.5].                                                                                                                                             |
| \[mariadbd]      | Options read by MariaDB Server.                                                                                                                                                                                                                                            |
| \[mariadbd-X.Y]  | Options read by a specific version of MariaDB Server.                                                                                                                                                                                                                      |
| \[client-server] | Options read by all MariaDB [client programs](https://github.com/mariadb-corporation/docs-server/blob/test/kb/en/clients-utilities/README.md) and the MariaDB Server. This is useful for options like socket and port, which is common between the server and the clients. |
| \[galera]        | Options read by a galera-capable MariaDB Server. Available on systems compiled with Galera support.                                                                                                                                                                        |

### Customizing mysql.server

If you have installed MariaDB to a non-standard location, then you may need to edit the `mysql.server` script to get it to work right.

If you do not want to edit the `mysql.server` script itself, then `mysql.server` also sources a few other `sh` scripts. These files can be used to set any variables that might be needed to make the script work in your specific environment. The files are:

* `/etc/default/mysql`
* `/etc/sysconfig/mysql`
* `/etc/conf.d/mysql`

## Installed Locations

`mysql.server` can be found in the `support-files` directory under your MariaDB installation directory or in a MariaDB source distribution.

### Installed SysVinit Locations

On systems that use [sysVinit](sysvinit.md), `mysql.server` may also be installed in other locations and with other names.

If you installed MariaDB on Linux using [RPMs](../install-and-upgrade-mariadb/installing-mariadb/binary-packages/rpm/), the `mysql.server` script is installed in the `/etc/init.d` directory with the name `mysql`. You need not install it manually.

#### Manually Installing with SysVinit

If you install MariaDB from [source](../install-and-upgrade-mariadb/installing-mariadb/compiling-mariadb-from-source/) or from a [binary tarball](../install-and-upgrade-mariadb/installing-mariadb/binary-packages/installing-mariadb-binary-tarballs.md) that does not install [mysql.server](mysql-server.md) automatically, and if you are on a system that uses [sysVinit](sysvinit.md), then you can manually install `mysql.server` with [sysVinit](sysvinit.md). This is usually done by copying it to `/etc/init.d/` and then creating specially named symlinks in the appropriate `/etc/rcX.d/` directories (where 'X' is a number between 0 and 6).

In the examples below we will follow the historical convention of renaming the `mysql.server` script to '`mysql`' when we copy it to `/etc/init.d/`.

The first step for most Linux distributions is to copy the `mysql.server` script to `/etc/init.d/` and make it executable:

```bash
cd /path/to/your/mariadb-version/support-files/
cp mysql.server /etc/init.d/mysql
chmod +x /etc/init.d/mysql
```

Now all that is needed is to create the specially-named symlinks. On both RPM and Debian-based Linux distributions there are tools which do this for you. Consult your distribution's documentation if neither of these work for you and follow their instructions for generating the symlinks or creating them manually.

On RPM-based distributions (like Fedora and CentOS), you use `chkconfig`:

```bash
chkconfig --add mysql
chkconfig --level 345 mysql on
```

On Debian-based distributions you use `update-rc.d`:

```bash
update-rc.d mysql defaults
```

On FreeBSD, the location for startup scripts is`/usr/local/etc/rc.d/` and when you copy the`mysql.server` script there you should rename it so that it matches the `*.sh` pattern, like so:

```bash
cd /path/to/your/mariadb/support-files/
cp mysql.server /usr/local/etc/rc.d/mysql.server.sh
```

As stated above, consult your distribution's documentation for more information on starting services like MariaDB at system startup.

See [mariadbd startup options](mariadbd-options.md) for information on configuration options for `mariadbd`.

<sub>_This page is licensed: GPLv2_</sub>

{% @marketo/form formId="4316" %}
