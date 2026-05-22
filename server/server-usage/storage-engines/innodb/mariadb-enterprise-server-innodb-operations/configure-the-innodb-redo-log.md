---
description: >-
  A guide to configuring the size and number of InnoDB redo log files in MariaDB
  Enterprise Server to balance write performance and crash recovery time.
---

# Configure the InnoDB Redo Log

## Overview

In MariaDB Enterprise Server, the InnoDB storage engine uses a Redo Log. The Redo Log is a transaction log that InnoDB uses to write data to disk in a crash-safe manner.

Redo Log records are identified using the Log Sequence Number (LSN). The Redo Log is a circular log file that is a constant size. Old Redo Log records are frequently overwritten by new Redo Log records. InnoDB regularly performs checkpoints. During a checkpoint, InnoDB flushes Redo Log records to the InnoDB tablespace files.

When the server crashes, InnoDB performs crash recovery during server startup using the Redo Log. During crash recovery, InnoDB finds the last checkpoint in the Redo Log and flushes the Redo Log records since the last checkpoint to the InnoDB tablespace files.

For additional information, see "[InnoDB Redo Log](configure-the-innodb-redo-log.md)".

This page describes how to configure the InnoDB Redo Log.

## Configure the InnoDB Redo Log Size

{% hint style="warning" %}
**Do not delete the `ib_logfile` files before startup to resize the redo log.** Starting with **MariaDB 10.8** — and **MariaDB Enterprise Server 11.4**, the first Enterprise Server with this behavior — the server fails to start if its existing redo log files are missing. The server must always be started with its existing redo log files. To resize the redo log, start the server normally, then use `SET GLOBAL innodb_log_file_size=…` (see below). Once the change is applied in the running instance, update the configuration file so the new size persists across restarts. This is part of the InnoDB redo log redesign tracked under [MDEV-27199](https://jira.mariadb.org/browse/MDEV-27199). Manual deletion of `ib_logfile` files was discouraged as early as MySQL 5.6.11 and became a hard startup failure in MariaDB 10.8 / Enterprise Server 11.4.
{% endhint %}

The size of the InnoDB Redo Log is configurable. If your server writes data at a very high frequency, then you may need to increase the redo log size, so that InnoDB does not have to perform checkpoints as frequently.

For the maximum capacity in the Redo Log, the Redo Log size should be the same as the [innodb\_buffer\_pool\_size](../innodb-system-variables.md#innodb_buffer_pool_size), which is configured by the [innodb\_buffer\_pool\_size](../innodb-system-variables.md#innodb_buffer_pool_size) system variable.

The method to configure the Redo Log size depends on the server version and whether a server restart are performed:

| Product Versions                    | Server Restart? | Method                               |
| ----------------------------------- | --------------- | ------------------------------------ |
| ES 10.5 and Later                   | No              | Configure size with SET GLOBAL       |
| ES 10.5 and Later CS 10.5 and Later | Yes             | Configure size in configuration file |

## Configure the InnoDB Redo Log Size with SET GLOBAL (ES 10.5 and Later)

Starting in MariaDB Enterprise Server 10.5, the size of the InnoDB Redo Log can be changed dynamically by setting the [innodb\_log\_file\_size](../innodb-system-variables.md#innodb_log_file_size) system variable using the [SET GLOBAL](../../../../reference/sql-statements/administrative-sql-statements/set-commands/set.md) statement. The [SET GLOBAL](../../../../reference/sql-statements/administrative-sql-statements/set-commands/set.md) statement requires the SUPER privilege.

The resize operation is performed asynchronously in the background. If the server is restarted before the operation completes, the request may be ignored. To ensure that the change survives server restarts, the [innodb\_log\_file\_size](../innodb-system-variables.md#innodb_log_file_size) system variable should also be set in a configuration file.

To configure the InnoDB Redo Log with the [SET GLOBAL](../../../../reference/sql-statements/administrative-sql-statements/set-commands/set.md) statement, use the following procedure:

1. Connect to the server using MariaDB Client as the `root@localhost` user account or another user account with the SUPER privilege:

```
$ mariadb --user=root
```

2. Set the [innodb\_log\_file\_size](../innodb-system-variables.md#innodb_log_file_size) system variable to the new size using the [SET GLOBAL](../../../../reference/sql-statements/administrative-sql-statements/set-commands/set.md) statement.

For example, to set the size to 512 MB:

```sql
SET GLOBAL innodb_log_file_size=(512 * 1024 * 1024);
```

And to set the size to 2 GB:

```sql
SET GLOBAL innodb_log_file_size=(2 * 1024 * 1024 * 1024);
```

3. The resize operation is performed asynchronously in the background. Confirm that the resize operation is complete by querying the [innodb\_log\_file\_size](../innodb-system-variables.md#innodb_log_file_size) system variable using the [SHOW GLOBAL VARIABLES](../../../../reference/sql-statements/administrative-sql-statements/show/show-variables.md) statement. The resize operation is complete when the output shows the new size as the value of the system variable.

Execute the following statement until it shows the new size:

```sql
SHOW GLOBAL VARIABLES
   LIKE 'innodb_log_file_size';
```

4. Choose a configuration file for custom changes to system variables and options.\
   It is not recommended to make custom changes to Enterprise Server's default configuration files, because your custom changes can be overwritten by other default configuration files that are loaded after.

Ensure that your custom changes are read last by creating a custom configuration file in one of the included directories. Configuration files in included directories are read in alphabetical order. Ensure that your custom configuration file is read last by using the `z-` prefix in the file name.

Some example configuration file paths for different distributions are shown in the following table:

| Distributions                | Example configuration file path                |
| ---------------------------- | ---------------------------------------------- |
| CentOS RHEL Rocky Linux SLES | /etc/my.cnf.d/z-custom-mariadb.cnf             |
| Debian Ubuntu                | /etc/mysql/mariadb.conf.d/z-custom-mariadb.cnf |

5. Set the [innodb\_log\_file\_size](../innodb-system-variables.md#innodb_log_file_size) system variable in the configuration file.

It needs to be set in a group that are read by MariaDB Server, such as \[mariadb] or \[server].

When set in a configuration file, the value supports units, such as "M", "G", etc.

For example, to set the size to 512 MB:

```
[mariadb]
...
innodb_log_file_size=512M
```

And to set the size to 2 GB:

```
[mariadb]
...
innodb_log_file_size=2G
```

## Configure the InnoDB Redo Log Size in a Configuration File (ES 10.5) and Later

Starting in MariaDB Enterprise Server 10.5, the size of the InnoDB Redo Log can be changed by setting the [innodb\_log\_file\_size](../innodb-system-variables.md#innodb_log_file_size) system variable in a configuration file.

To configure the InnoDB Redo Log in a configuration file, use the following procedure:

1. Choose a configuration file for custom changes to system variables and options.

It is not recommended to make custom changes to Enterprise Server's default configuration files, because your custom changes can be overwritten by other default configuration files that are loaded after.

Ensure that your custom changes are read last by creating a custom configuration file in one of the included directories. Configuration files in included directories are read in alphabetical order. Ensure that your custom configuration file is read last by using the `z-` prefix in the file name.

Some example configuration file paths for different distributions are shown in the following table:

| Distributions                | Example configuration file path                |
| ---------------------------- | ---------------------------------------------- |
| CentOS RHEL Rocky Linux SLES | /etc/my.cnf.d/z-custom-mariadb.cnf             |
| Debian Ubuntu                | /etc/mysql/mariadb.conf.d/z-custom-mariadb.cnf |

2. Set the [innodb\_log\_file\_size](../innodb-system-variables.md#innodb_log_file_size) system variable in the configuration file.\
   It needs to be set in a group that are read by MariaDB Server, such as \[mariadb] or \[server].\
   When set in a configuration file, the value supports units, such as "M", "G", etc.

For example, to set the size to 512 MB:

```
[mariadb]
...
innodb_log_file_size=512M
```

And to set the size to 2 GB:

```
[mariadb]
...
innodb_log_file_size=2G
```

3. Starting in MariaDB Community Server 10.5, the server must be restarted for the configuration change to take effect:

```bash
$ sudo systemctl restart mariadb
```

4. Starting in MariaDB Enterprise Server 10.5, the server can use the configuration change without a restart if you use [SET GLOBAL](../../../../reference/sql-statements/administrative-sql-statements/set-commands/set.md).

## Emergency Recovery Across Major Versions

In MariaDB 11.x (and the corresponding MariaDB Enterprise Server releases), starting the server with data files from MariaDB 10.x is permitted **only** when [innodb\_force\_recovery](../innodb-system-variables.md#innodb_force_recovery) is set to `6`. This path is intended exclusively as a last-resort mechanism for extracting a logical dump from a corrupted or otherwise incompatible database; it is **not** a substitute for the normal upgrade path.

{% hint style="danger" %}
`innodb_force_recovery=6` places the database in a highly restricted state intended only for data salvage. Do not use it as a standard operational approach or a shortcut for the normal upgrade path.
{% endhint %}

When this emergency path is in effect:

* The database accepts no new writes or modifications.
* Use [mariadb-dump](../../../../clients-and-utilities/backup-restore-and-import-clients/mariadb-dump.md) (or another logical export tool) to extract the data, then re-import it into a fresh, supported instance.

For the standard upgrade procedure between major versions, see [Upgrading Between Major MariaDB Versions](../../../../server-management/install-and-upgrade-mariadb/upgrading/upgrading-between-major-mariadb-versions.md).

This capability was added under [MDEV-39303](https://jira.mariadb.org/browse/MDEV-39303), available in MariaDB 11.4.11, MariaDB 11.8.7, and later releases.

<sub>_This page is: Copyright © 2025 MariaDB. All rights reserved._</sub>

{% @marketo/form formId="4316" %}
