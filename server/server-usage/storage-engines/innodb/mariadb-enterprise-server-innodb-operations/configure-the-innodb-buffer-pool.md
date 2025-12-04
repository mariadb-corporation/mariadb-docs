---
description: >-
  A guide to configuring the size and instances of the InnoDB Buffer Pool to
  optimize memory usage and cache performance.
---

# Configure the InnoDB Buffer Pool

## Overview

In MariaDB Enterprise Server, the InnoDB storage engine uses the Buffer Pool as an in-memory cache. The Buffer Pool caches pages that were recently accessed. If a lot of pages are being accessed sequentially, the Buffer Pool also preemptively caches nearby pages. Pages are evicted using a least recently used (LRU) algorithm.

The contents of the Buffer Pool can be reloaded at startup, so that InnoDB does not have to function with a "cold" cache after a restart. To support this, the page numbers of all pages in the Buffer Pool can be dumped at shutdown. During startup, the page numbers are read from the dump, and InnoDB uses the page numbers to reload each page from its corresponding data file.

The size of each page in the Buffer Pool depends on the value of the [innodb\_page\_size](../../../../ha-and-performance/optimization-and-tuning/system-variables/innodb-status-variables.md#innodb_page_size) system variable.

Starting with ES 10.5 and CS 10.5, the [Buffer Pool](../innodb-system-variables.md#innodb_buffer_pool_instances) always has a single instance.

For additional information, see "[InnoDB Buffer Pool](../innodb-buffer-pool.md)".

This page describes how to configure the InnoDB Buffer Pool.

## Configure the InnoDB Buffer Pool Size

The size of the InnoDB Buffer Pool can be configured by setting the [innodb\_buffer\_pool\_size](../innodb-system-variables.md#innodb_buffer_pool_size) system variable. On ES nodes that exclusively use the InnoDB storage engine, the InnoDB Buffer Pool should usually be between 50%-75% of the memory available.

| Available Memory | Recommended InnoDB Buffer Pool Size |
| ---------------- | ----------------------------------- |
| 4 GB             | 2 GB                                |
| 8 GB             | 4-8 GB                              |
| 16 GB            | 8-12 GB                             |
| 32 GB            | 16-24 GB                            |
| 64 GB            | 32-56 GB                            |
| 128 GB           | 64-96 GB                            |
| 256 GB           | 128-192 GB                          |

The method to configure the Buffer Pool size depends on whether a server restart are performed:

| Product Versions | Server Restart? | Method                                                                      |
| ---------------- | --------------- | --------------------------------------------------------------------------- |
| Any ES Any CS    | No              | [Configure size with SET GLOBA](configure-the-innodb-buffer-pool.md).       |
| Any ES Any CS    | No              | [Configure size in configuration file](configure-the-innodb-buffer-pool.md) |

## Configure the InnoDB Buffer Pool Size with SET GLOBAL

The size of the InnoDB buffer pool can be changed dynamically by setting the [innodb\_buffer\_pool\_size](../innodb-system-variables.md#innodb_buffer_pool_size) system variable using the [SET GLOBAL](../../../../reference/sql-statements/administrative-sql-statements/set-commands/set.md) statement. The [SET GLOBAL](../../../../reference/sql-statements/administrative-sql-statements/set-commands/set.md) statement requires the SUPER privilege.

To ensure that the change survives server restarts, the [innodb\_buffer\_pool\_size](../innodb-system-variables.md#innodb_buffer_pool_size) system variable should also be set in a configuration file.

To configure the InnoDB Buffer Pool with the [SET GLOBAL](../../../../reference/sql-statements/administrative-sql-statements/set-commands/set.md) statement, use the following procedure:

1. Connect to the server using MariaDB Client as the `root@localhost` user account or another user account with the SUPER privilege:

```
$ mariadb --user=root
```

2. Set the [innodb\_buffer\_pool\_size](../innodb-system-variables.md#innodb_buffer_pool_size) system variable to the new size using the [SET GLOBAL](../../../../reference/sql-statements/administrative-sql-statements/set-commands/set.md) statement.

For example, to set the size to 2 GB:

```sql
SET GLOBAL innodb_buffer_pool_size=(2 * 1024 * 1024 * 1024);
```

3. Confirm that the resize operation has been completed by querying the [Innodb\_buffer\_pool\_resize\_status](../../../../ha-and-performance/optimization-and-tuning/system-variables/innodb-status-variables.md#innodb_buffer_pool_resize_status) status variable using the [SHOW GLOBAL STATUS](../../../../reference/sql-statements/administrative-sql-statements/show/show-status.md) statement:

```sql
SHOW GLOBAL STATUS
   LIKE 'Innodb_buffer_pool_resize_status';
```

```
+----------------------------------+----------------------------------------------------+
| Variable_name                    | Value                                              |
+----------------------------------+----------------------------------------------------+
| Innodb_buffer_pool_resize_status | Completed resizing buffer pool at 200904 17:49:48. |
+----------------------------------+----------------------------------------------------+
```

4. Choose a configuration file for custom changes to system variables and options.\
   It is not recommended to make custom changes to Enterprise Server's default configuration files, because your custom changes can be overwritten by other default configuration files that are loaded after.

Ensure that your custom changes are read last by creating a custom configuration file in one of the included directories. Configuration files in included directories are read in alphabetical order. Ensure that your custom configuration file is read last by using the z- prefix in the file name.

Some example configuration file paths for different distributions are shown in the following table:

| Distributions                | Example configuration file path                |
| ---------------------------- | ---------------------------------------------- |
| CentOS RHEL Rocky Linux SLES | /etc/my.cnf.d/z-custom-mariadb.cnf             |
| Debian Ubuntu                | /etc/mysql/mariadb.conf.d/z-custom-mariadb.cnf |

5. Set the [innodb\_buffer\_pool\_size](../innodb-system-variables.md#innodb_buffer_pool_size) system variable in the configuration file.\
   It needs to be set in a group that are read by MariaDB Server, such as \[mariadb] or \[server].\
   When set in a configuration file, the value supports units, such as "M", "G", etc.

For example, to set the size to 2 GB:

```
[mariadb]
...
innodb_buffer_pool_size=2G
```

## Configure the InnoDB Buffer Pool Size in a Configuration File

The size of the InnoDB Buffer Pool can be changed by setting the [innodb\_buffer\_pool\_size](../innodb-system-variables.md#innodb_buffer_pool_size) system variable in a configuration file.

To configure the InnoDB Buffer Pool in a configuration file, use the following procedure:

1. Choose a configuration file for custom changes to system variables and options.\
   It is not recommended to make custom changes to Enterprise Server's default configuration files, because your custom changes can be overwritten by other default configuration files that are loaded after.\
   Ensure that your custom changes are read last by creating a custom configuration file in one of the included directories. Configuration files in included directories are read in alphabetical order. Ensure that your custom configuration file is read last by using the z- prefix in the file name.

Some example configuration file paths for different distributions are shown in the following table:

| Distributions                | Example configuration file path                |
| ---------------------------- | ---------------------------------------------- |
| CentOS RHEL Rocky Linux SLES | /etc/my.cnf.d/z-custom-mariadb.cnf             |
| Debian Ubuntu                | /etc/mysql/mariadb.conf.d/z-custom-mariadb.cnf |

2. Set the [innodb\_buffer\_pool\_size](../innodb-system-variables.md#innodb_buffer_pool_size) system variable in the configuration file.

It needs to be set in a group that are read by MariaDB Server, such as \[mariadb] or \[server].

When set in a configuration file, the value supports units, such as "M", "G", etc.

For example, to set the size to 2 GB:

```
[mariadb]
...
innodb_buffer_pool_size=2G
```

3. Restart the server:

```bash
$ sudo systemctl restart mariadb
```

The server can use the configuration change without a restart if you use [SET GLOBAL](../../../../reference/sql-statements/administrative-sql-statements/set-commands/set.md).

<sub>_This page is: Copyright © 2025 MariaDB. All rights reserved._</sub>

{% @marketo/form formId="4316" %}
