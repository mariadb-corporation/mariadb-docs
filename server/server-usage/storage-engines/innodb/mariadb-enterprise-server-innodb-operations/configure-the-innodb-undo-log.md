---
description: >-
  Learn how to manage InnoDB undo logs in MariaDB Enterprise Server, including
  moving them to separate tablespaces and enabling truncation.
---

# Configure the InnoDB Undo Log

## Overview

The InnoDB undo log is a transaction log used by InnoDB to keep track of multiple row versions for multi-version concurrency control (MVCC). When a row's value changes, InnoDB stores old versions of the row in the Undo Log.

When transactions are committed and the old row versions are no longer necessary, the InnoDB Purge Threads asynchronously delete old row versions from the Undo Log in the background.

When a transaction is rolled back, InnoDB uses the Undo Log to rollback the transaction's changes.

For additional information, see "[InnoDB Undo Log](configure-the-innodb-undo-log.md)".

This page describes how to configure the InnoDB Undo Log.

## Configure InnoDB Undo Log Tablespaces

By default, the InnoDB undo log is located in the InnoDB system tablespace, which is defined by the [innodb\_data\_file\_path](../innodb-system-variables.md#innodb_data_file_path) system variable. However, it can be helpful to configure separate undo log tablespaces to spread out I/O load between different files or storage devices.

InnoDB can be configured to use separate undo log tablespaces by setting the [innodb\_undo\_tablespaces](../innodb-system-variables.md#innodb_undo_tablespaces) system variable. The separate undo log tablespaces will have file names of the format undoN, where N is an integer.

When you configure separate undo log tablespaces, you can also configure the separate undo log tablespaces to go to a specific directory by setting the [innodb\_undo\_directory](../innodb-system-variables.md#innodb_undo_directory) system variable. This is most helpful if you want to put the undo log tablespaces on a separate storage device.

Separate InnoDB undo log tablespaces must be configured prior to the initialization of the server's InnoDB data directory. If you try to configure separate InnoDB undo log tablespaces when the InnoDB data directory has already been initializes, you will see errors in the error log during startup similar to the following:

```sql
[ERROR] InnoDB: Expected to open innodb_undo_tablespaces=8 but was able to find only 0
[ERROR] InnoDB: Plugin initialization aborted with error Generic error
```

To safely configure separate InnoDB undo log tablespaces:

1. If you have preexisting data, backup your data with [MariaDB Dump](../../../../clients-and-utilities/backup-restore-and-import-clients/mariadb-dump.md).
2. Ensure that the server is stopped:

```bash
$ sudo systemctl stop mariadb
```

3. Choose a configuration file for custom changes to system variables and options.

It is not recommended to make custom changes to Enterprise Server's default configuration files, because your custom changes can be overwritten by other default configuration files that are loaded after.

Ensure that your custom changes are read last by creating a custom configuration file in one of the included directories. Configuration files in included directories are read in alphabetical order. Ensure that your custom configuration file is read last by using the `z-` prefix in the file name.

Some example configuration file paths for different distributions are shown in the following table:

| Distributions                | Example configuration file path                |
| ---------------------------- | ---------------------------------------------- |
| CentOS RHEL Rocky Linux SLES | /etc/my.cnf.d/z-custom-mariadb.cnf             |
| Debian Ubuntu                | /etc/mysql/mariadb.conf.d/z-custom-mariadb.cnf |

4. Set the [innodb\_undo\_tablespaces](../innodb-system-variables.md#innodb_undo_tablespaces) system variable in the configuration file.

It needs to be set in a group that are read by MariaDB Server, such as \[mariadb] or \[server].

For example, to set the number of tablespaces to 8:

```
[mariadb]
...
innodb_undo_tablespaces=8
```

5. If you want your InnoDB undo log tablespaces to be in a specific directory, then also set the [innodb\_undo\_directory](../innodb-system-variables.md#innodb_undo_directory) system variable in the configuration file:

For example, to set the directory to /innodb/undo:

```
[mariadb]
...
innodb_undo_directory=/innodb/undo
```

6. If you want your InnoDB undo log tablespaces to be in a specific directory, then also create the directory, and give it the proper permissions:

```bash
$ sudo mkdir -p /innodb/undo
$ sudo chown mysql:mysql /innodb/undo
```

7. Delete the current contents of the datadir and innodb\_data\_home\_dir.

For example, if the default value of /var/lib/mysql is used for both:

```bash
$ sudo rm -fr /var/lib/mysql/*
```

8. Reinitialize the data directory using the MariaDB Install DB command.
9. Start the server:

```bash
$ sudo systemctl start mariadb
```

10. Connect to the server using MariaDB Client:

```bash
$ mariadb --user=root
```

11. If your server had preexisting data, then reload the backup taken at the beginning of the procedure.
12. Confirm that the configuration changes were properly applied by checking the values of the system variables using the [SHOW GLOBAL VARIABLES](../../../../reference/sql-statements/administrative-sql-statements/show/show-variables.md) statement:

```sql
SHOW GLOBAL VARIABLES
   WHERE Variable_name IN (
      'innodb_undo_tablespaces',
      'innodb_undo_directory'
   );
```

```
+-------------------------+--------------+
| Variable_name           | Value        |
+-------------------------+--------------+
| innodb_undo_directory   | /innodb/undo |
| innodb_undo_tablespaces | 8            |
+-------------------------+--------------+
```

13. Consider also enabling undo log truncation to increase performance of the InnoDB Purge Threads.

## Enable InnoDB Undo Log Truncation

If a server is configured to have 2 or more separate InnoDB undo log files, then InnoDB undo log truncation can be enabled by setting the [innodb\_undo\_log\_truncate](../innodb-system-variables.md#innodb_undo_log_truncate) system variable using the [SET GLOBAL](../../../../reference/sql-statements/administrative-sql-statements/set-commands/set.md) statement. The [SET GLOBAL](../../../../reference/sql-statements/administrative-sql-statements/set-commands/set.md) statement requires the SUPER privilege.

When InnoDB undo log truncation is enabled, the InnoDB purge threads can truncate an entire undo log at once, rather than individually freeing each rollback segment within the undo log.

An undo log is truncated when its size exceeds the [innodb\_max\_undo\_log\_size](../innodb-system-variables.md#innodb_max_undo_log_size) system variable.

The frequency at which the InnoDB purge threads check for undo logs to truncate is configured by setting the innodb\_purge\_rseg\_truncate\_frequency system variable using the [SET GLOBAL](../../../../reference/sql-statements/administrative-sql-statements/set-commands/set.md) statement.

To ensure that the changes survive server restarts, the system variables should also be set in a configuration file.

To enable InnoDB undo log truncation:

1. Connect to the server using MariaDB Client as the `root@localhost` user account or another user account with the SUPER privilege:

```
$ mariadb --user=root
```

2. Set the [innodb\_undo\_log\_truncate](../innodb-system-variables.md#innodb_undo_log_truncate) system variable to ON using the [SET GLOBAL](../../../../reference/sql-statements/administrative-sql-statements/set-commands/set.md) statement.

For example:

```
SET GLOBAL innodb_undo_log_truncate=ON;
```

3. If you would like to change the size at which undo logs are truncated, then also set the [innodb\_max\_undo\_log\_size](../innodb-system-variables.md#innodb_max_undo_log_size) system variable to the new size using the [SET GLOBAL](../../../../reference/sql-statements/administrative-sql-statements/set-commands/set.md) statement.

For example, to set the size to 2 GB:

```
SET GLOBAL innodb_max_undo_log_size=(2 * 1024 * 1024 * 1024);
```

4. If you would like the InnoDB purge threads to check the undo logs more frequently, then also set the [innodb\_purge\_rseg\_truncate\_frequency](../innodb-system-variables.md#innodb_purge_rseg_truncate_frequency) system variable to a lower value using the [SET GLOBAL](../../../../reference/sql-statements/administrative-sql-statements/set-commands/set.md) statement.

For example, to configure the purge threads to check the undo logs for truncation every 64 iterations:

```
SET GLOBAL innodb_purge_rseg_truncate_frequency=64;
```

5. Choose a configuration file for custom changes to system variables and options.\
   It is not recommended to make custom changes to Enterprise Server's default configuration files, because your custom changes can be overwritten by other default configuration files that are loaded after.

Ensure that your custom changes are read last by creating a custom configuration file in one of the included directories. Configuration files in included directories are read in alphabetical order. Ensure that your custom configuration file is read last by using the `z-` prefix in the file name.

Some example configuration file paths for different distributions are shown in the following table:

| Distributions                | Example configuration file path                |
| ---------------------------- | ---------------------------------------------- |
| CentOS RHEL Rocky Linux SLES | /etc/my.cnf.d/z-custom-mariadb.cnf             |
| Debian Ubuntu                | /etc/mysql/mariadb.conf.d/z-custom-mariadb.cnf |

6. Set the system variables in the configuration file.\
   It needs to be set in a group that are read by MariaDB Server, such as \[mariadb] or \[server].\
   When set in a configuration file, the [innodb\_max\_undo\_log\_size](../innodb-system-variables.md#innodb_max_undo_log_size) value supports units, such as "M", "G", etc.

For example:

```
[mariadb]
...
innodb_undo_log_truncate=ON
innodb_max_undo_log_size=2G
innodb_purge_rseg_truncate_frequency=64
```

<sub>_This page is: Copyright © 2025 MariaDB. All rights reserved._</sub>

{% @marketo/form formId="4316" %}
