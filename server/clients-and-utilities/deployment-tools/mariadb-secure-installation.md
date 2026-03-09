---
description: >-
  Complete MariaDB installation guide. Complete setup instructions for Linux,
  Windows, and macOS with configuration and verification for production use.
---

# mariadb-secure-installation

{% hint style="info" %}
Note that many of the reasons for the existence of this script no longer apply (and therefore the guidelines in many online tutorials. In particular, from MariaDB 10.4, [Unix socket authentication](../../reference/plugins/authentication-plugins/authentication-plugin-unix-socket.md) is applied by default, and there is usually no need to create a root password. See [Authentication from MariaDB 10.4](../../security/user-account-management/authentication-from-mariadb-10-4.md).
{% endhint %}

{% hint style="info" %}
Previously, the client was called `mysql_secure_installation`. It can still be accessed under this name, via a symlink in Linux, or an alternate binary in Windows.
{% endhint %}

## Description

`mariadb-secure-installation` is a shell script available on Unix systems, and enables you to improve the security of your MariaDB installation in the following ways:

* You can set a password for root accounts.
* You can remove root accounts that are accessible from outside the local host.
* You can remove anonymous-user accounts.
* You can remove the test database, which by default can be accessed by anonymous users.

`mariadb-secure-installation` can be invoked without arguments:

```bash
shell> mariadb-secure-installation
```

The script will prompt you to determine which actions to perform.

```bash
Example:
localhost:# mariadb-secure-installation
NOTE: RUNNING ALL PARTS OF THIS SCRIPT IS RECOMMENDED FOR ALL MariaDB
      SERVERS IN PRODUCTION USE!  PLEASE READ EACH STEP CAREFULLY!
In order to log into MariaDB to secure it, we'll need the current
password for the root user.  If you've just installed MariaDB, and
you haven't set the root password yet, the password is blank,
so you should just press enter here.
Enter current password for root (enter for none): 
OK, successfully used password, moving on...
Setting the root password ensures that nobody can log into the MariaDB
root user without the proper authorisation.
You already have a root password set, so you can safely answer 'n'.
Change the root password? [Y/n] n
 ... skipping.
By default, a MariaDB installation has an anonymous user, allowing anyone
to log into MariaDB without having to have a user account created for
them.  This is intended only for testing, and to make the installation
go a bit smoother.  You should remove them before moving into a
production environment.
Remove anonymous users? [Y/n] y
 ... Success!
Normally, root should only be allowed to connect from 'localhost'.  This
ensures that someone cannot guess at the root password from the network.
Disallow root login remotely? [Y/n] y
 ... Success!
By default, MariaDB comes with a database named 'test' that anyone can
access.  This is also intended only for testing, and should be removed
before moving into a production environment.
Remove test database and access to it? [Y/n] y
 - Dropping test database...
 ... Success!
 - Removing privileges on test database...
 ... Success!
Reloading the privilege tables will ensure that all changes made so far
will take effect immediately.
Reload privilege tables now? [Y/n] y
 ... Success!
Cleaning up...
All done!  If you've completed all of the above steps, your MariaDB
installation should now be secure.
Thanks for using MariaDB!
```

## Options

`mariadb-secure-installation` accepts some options:

| Option                  | Description                                      |
| ----------------------- | ------------------------------------------------ |
| --basedir=dir           | Base directory.                                  |
| --no-defaults           | Don't read default options from any option file. |
| --defaults-file=#       | Only read default options from the given file #. |
| --defaults-extra-file=# | Read this file after the global files are read.  |

Other unrecognized options is passed on to the server.

### Option Files

In addition to reading options from the command line, `mariadb-secure-installation` can also read options from [option files](../../server-management/install-and-upgrade-mariadb/configuring-mariadb/configuring-mariadb-with-option-files.md). If an unknown option is provided to `mariadb-secure-installation` in an option file, it is ignored.

The following options relate to how MariaDB command-line tools handle option files. They must be given as the first argument on the command line:

| Option                    | Description                                                                         |
| ------------------------- | ----------------------------------------------------------------------------------- |
| --no-defaults             | Don't read default options from any option file.                                    |
| --defaults-file=#         | Only read default options from the given file #.                                    |
| --defaults-extra-file=#   | Read this file after the global files are read.                                     |
| --defaults-group-suffix=# | In addition to the default option groups, also read option groups with this suffix. |

#### Option Groups

`mariadb-secure-installation` reads options from the following [option groups](../../server-management/install-and-upgrade-mariadb/configuring-mariadb/configuring-mariadb-with-option-files.md#option-groups) from [option files](../../server-management/install-and-upgrade-mariadb/configuring-mariadb/configuring-mariadb-with-option-files.md):

| Group             | Description                                                                                                                                                              |
| ----------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------ |
| \[client]         | Options read by all MariaDB and MySQL [client programs](../), which includes both MariaDB and MySQL clients like mysqldump.                                              |
| \[client-server]  | Options read by all MariaDB client programs and the MariaDB Server. This is useful for options like socket and port, which is common between the server and the clients. |
| \[client-mariadb] | Options read by all MariaDB client programs.                                                                                                                             |

## Use With Galera Cluster

{% hint style="warning" %}
This script is not completely safe for use with [Galera Cluster](https://app.gitbook.com/s/3VYeeVGUV4AMqrA3zwy7/readme/mariadb-galera-cluster-usage-guide) as it directly manipulates the [mysql.user](../../reference/system-tables/the-mysql-database-tables/mysql-user-table.md)/[mysql.global\_priv](../../reference/system-tables/the-mysql-database-tables/mysql-global_priv-table.md) table, which is not propagated by Galera to the other nodes.
{% endhint %}

You should run this script on the first node in the cluster before adding more nodes.

If you want to run this after the cluster is up and running, you should find alternative ways.

Anyone can vote for this to be fixed at [MDEV-10112](https://jira.mariadb.org/browse/MDEV-10112).

<sub>_This page is licensed: CC BY-SA / Gnu FDL_</sub>

{% @marketo/form formId="4316" %}
