---
description: >-
  Instructions on tuning the number of InnoDB read and write I/O threads to
  match your system's disk I/O capabilities.
---

# Configure the InnoDB I/O Threads

## Overview

The InnoDB Read I/O Threads handle completion of read I/O requests, and the InnoDB Write I/O Threads handle completion of write I/O requests.

Starting with MariaDB Enterprise Server 10.5 and MariaDB Community Server 10.5, the InnoDB I/O Threads were replaced by the asynchronous I/O functionality in the [InnoDB Background Thread Pool](../innodb-architecture-for-mariadb-enterprise-server/mariadb-enterprise-server-innodb-background-thread-pool.md).

For additional information, see "[InnoDB I/O Threads](../innodb-architecture-for-mariadb-enterprise-server/mariadb-enterprise-server-innodb-io-threads.md)".

This page describes how to configure the InnoDB I/O Threads.

## Configure the Number of InnoDB I/O Threads

Starting with ES 10.5 and CS 10.5, the InnoDB I/O Threads have been replaced by the asynchronous I/O functionality in the InnoDB Background Thread Pool. In these versions, the [innodb\_read\_io\_threads](../innodb-system-variables.md#innodb_read_io_threads) and [innodb\_write\_io\_threads](../innodb-system-variables.md#innodb_write_io_threads) system variables have been repurposed. The value of each system variable is multiplied by 256 to determine the maximum number of concurrent asynchronous I/O requests that can be completed by the Background Thread Pool.

For example, if `innodb_read_io_threads=2 and innodb_write_io_threads=4` are set, InnoDB are restricted to a maximum of 512 concurrent asynchronous read I/O requests and 1024 concurrent asynchronous write I/O requests.

## Interaction with Asynchronous I/O

When asynchronous I/O is enabled, the InnoDB I/O Threads do not receive the initial I/O request from query threads. Instead, the query threads submit asynchronous I/O requests directly to the operating system, and after the operating system performs the operation, the InnoDB I/O Threads handle completion of the request.

Asynchronous I/O is enabled by the [innodb\_use\_native\_aio](../innodb-system-variables.md#innodb_use_native_aio) system variable, which is enabled by default.

## Affected I/O Operations

The [innodb\_read\_io\_threads](../innodb-system-variables.md#innodb_read_io_threads) system variable affects completion of the following types of reads:

* Linear read-ahead (configured by [innodb\_read\_ahead\_threshold](../innodb-system-variables.md#innodb_read_ahead_threshold))
* Random read-ahead (configured by [innodb\_random\_read\_ahead](../innodb-system-variables.md#innodb_random_read_ahead))

The [innodb\_write\_io\_threads](../innodb-system-variables.md#innodb_write_io_threads) system variable affects completion of the following types of writes:

* Page flushing due to adaptive flushing (configured by [innodb\_adaptive\_flushing](../innodb-system-variables.md#innodb_adaptive_flushing) and [innodb\_adaptive\_flushing\_lwm](../innodb-system-variables.md#innodb_adaptive_flushing_lwm))
* Page flushing due to buffer pool capacity (configured by \[innodb\_max\_dirty\_pages\_pct] and \[[innodb-system-variables/#innodb\_max\_dirty\_pages\_pct\_lwm|innodb\_max\_dirty\_pages\_pct\_lwm](../innodb-system-variables.md#innodb_max_dirty_pages_pct))
* Page flushing due to LRU page evictions (configured by [innodb\_lru\_flush\_size](../innodb-system-variables.md#innodb_lru_flush_size) and [innodb\_lru\_scan\_depth](../innodb-system-variables.md#innodb_lru_scan_depth))

## Configuration Procedure

The method to configure the number of I/O threads depends on the server version and whether a server restart are performed:

| Product Versions  | Server Restart? | Method                                                                                                                                                                        |
| ----------------- | --------------- | ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| ES 10.5 and Later | No              | [Configure maximum number of asynchronous I/O requests with SET GLOBAL](configure-the-innodb-io-threads.md#configure-the-number-of-innodb-io-threads-in-a-configuration-file) |
| Any ES Any CS     | Yes.            | [Configure number of I/O threads in configuration file](configure-the-innodb-io-threads.md#configure-the-number-of-innodb-io-threads)                                         |

## Configure InnoDB's Maximum Number of Asynchronous I/O Requests with SET GLOBAL (ES 10.5) and Later

Starting with [MariaDB Enterprise Server 10.5](https://app.gitbook.com/s/aEnK0ZXmUbJzqQrTjFyb/enterprise-server/old-releases/10-5), InnoDB's maximum number of asynchronous I/O requests can be changed dynamically by setting the [innodb\_read\_io\_threads](../innodb-system-variables.md#innodb_read_io_threads)[innodb\_write\_io\_threads](../innodb-system-variables.md#innodb_write_io_threads) system variables using the [SET GLOBAL](../../../../reference/sql-statements/administrative-sql-statements/set-commands/set.md) statement. The [SET GLOBAL](../../../../reference/sql-statements/administrative-sql-statements/set-commands/set.md) statement requires the SUPER privilege.

The value of each system variable is multiplied by 256 to determine the maximum number of asynchronous I/O requests that can be performed by the Background Thread Pool. For example, if you want to allow a maximum of 1024 concurrent asynchronous write I/O requests, the [innodb\_write\_io\_threads](../innodb-system-variables.md#innodb_write_io_threads) system variable should be set to 4 (since 1024/256=4).

To ensure that the change survives server restarts, the [innodb\_read\_io\_threads](../innodb-system-variables.md#innodb_read_io_threads) [innodb\_write\_io\_threads](../innodb-system-variables.md#innodb_write_io_threads) system variables should also be set in a configuration file.

To configure InnoDB's maximum number of asynchronous I/O requests with the [SET GLOBAL](../../../../reference/sql-statements/administrative-sql-statements/set-commands/set.md) statement, use the following procedure:

1. Connect to the server using MariaDB Client as the `root@localhost` user account or another user account with the SUPER privilege:

```
$ mariadb --user=root
```

2. Set the [innodb\_read\_io\_threads](../innodb-system-variables.md#innodb_read_io_threads) and [innodb\_write\_io\_threads](../innodb-system-variables.md#innodb_write_io_threads) system variables to the new values using the [SET GLOBAL](../../../../reference/sql-statements/administrative-sql-statements/set-commands/set.md) statement.

For example:

```sql
SET GLOBAL innodb_read_io_threads=8;
SET GLOBAL innodb_write_io_threads=8;
```

3. Choose a configuration file for custom changes to system variables and options.

It is not recommended to make custom changes to Enterprise Server's default configuration files, because your custom changes can be overwritten by other default configuration files that are loaded after.

Ensure that your custom changes are read last by creating a custom configuration file in one of the included directories. Configuration files in included directories are read in alphabetical order. Ensure that your custom configuration file is read last by using the z- prefix in the file name.

Some example configuration file paths for different distributions are shown in the following table:

| Distributions                | Example configuration file path                |
| ---------------------------- | ---------------------------------------------- |
| CentOS RHEL Rocky Linux SLES | /etc/my.cnf.d/z-custom-mariadb.cnf             |
| Debian Ubuntu                | /etc/mysql/mariadb.conf.d/z-custom-mariadb.cnf |

4. Set the [innodb\_read\_io\_threads](../innodb-system-variables.md#innodb_read_io_threads) and [innodb\_write\_io\_threads](../innodb-system-variables.md#innodb_write_io_threads) system variables in the configuration file.

It needs to be set in a group that are read by MariaDB Server, such as \[mariadb] or \[server].

For example:

```
[mariadb]
...
innodb_read_io_threads=8
innodb_write_io_threads=8
```

## Configure the Number of InnoDB I/O Threads in a Configuration File

The number of I/O threads is configured by the [innodb\_read\_io\_threads](../innodb-system-variables.md#innodb_read_io_threads) and [innodb\_write\_io\_threads](../innodb-system-variables.md#innodb_write_io_threads) system variables.

To configure the number of InnoDB I/O Threads in a configuration file, use the following procedure:

1. Choose a configuration file for custom changes to system variables and options.

It is not recommended to make custom changes to Enterprise Server's default configuration files, because your custom changes can be overwritten by other default configuration files that are loaded after.

Ensure that your custom changes are read last by creating a custom configuration file in one of the included directories. Configuration files in included directories are read in alphabetical order. Ensure that your custom configuration file is read last by using the z- prefix in the file name.

Some example configuration file paths for different distributions are shown in the following table:

| Distributions                | Example configuration file path                |
| ---------------------------- | ---------------------------------------------- |
| CentOS RHEL Rocky Linux SLES | /etc/my.cnf.d/z-custom-mariadb.cnf             |
| Debian Ubuntu                | /etc/mysql/mariadb.conf.d/z-custom-mariadb.cnf |

2. Set the [innodb\_read\_io\_threads](../innodb-system-variables.md#innodb_read_io_threads) and [innodb\_write\_io\_threads](../innodb-system-variables.md#innodb_write_io_threads) system variables in the configuration file.

It needs to be set in a group that are read by [MariaDB Server](../../../), such as `[mariadb]` or `[server]`.

For example:

```
[mariadb]
...
innodb_read_io_threads=8
innodb_write_io_threads=8
```

3. Restart the server:

```
$ sudo systemctl restart mariadb
```

Starting with [MariaDB Enterprise Server 10.5](https://app.gitbook.com/s/aEnK0ZXmUbJzqQrTjFyb/enterprise-server/old-releases/10-5), the server can use the configuration change without a restart if you use [SET GLOBAL](../../../../reference/sql-statements/administrative-sql-statements/set-commands/set.md).

<sub>_This page is: Copyright © 2025 MariaDB. All rights reserved._</sub>

{% @marketo/form formId="4316" %}
