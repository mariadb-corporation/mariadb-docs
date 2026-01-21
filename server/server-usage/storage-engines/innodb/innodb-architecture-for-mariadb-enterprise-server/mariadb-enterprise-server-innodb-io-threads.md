---
description: >-
  Learn about the specialized I/O threads in MariaDB Enterprise Server's InnoDB
  engine that handle asynchronous read and write operations efficiently.
---

# MariaDB Enterprise Server InnoDB I/O Threads

## Overview

Starting with MariaDB Enterprise Server 10.5 and MariaDB Community Server 10.5, the InnoDB I/O Threads were replaced by the asynchronous I/O functionality in the [InnoDB Background Thread Pool](mariadb-enterprise-server-innodb-background-thread-pool.md).

## Feature Summary

| Feature        | Detail                                                                                                                                                                           | Resources                                                                                                             |
| -------------- | -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | --------------------------------------------------------------------------------------------------------------------- |
| Thread         | InnoDB I/O Threads                                                                                                                                                               |                                                                                                                       |
| Storage Engine | InnoDB                                                                                                                                                                           |                                                                                                                       |
| Purpose        | Reading data from disk / Writing data to disk                                                                                                                                    |                                                                                                                       |
| Availability   |                                                                                                                                                                                  | [MariaDB Enterprise Server](https://app.gitbook.com/o/diTpXxF5WsbHqTReoBsS/s/JqgUabdZsoY5EiaJmqgn/)                   |
| Quantity       | Set by [innodb\_read\_io\_threads](../innodb-system-variables.md#innodb_read_io_threads) and [innodb\_write\_io\_threads](../innodb-system-variables.md#innodb_write_io_threads) | [Configure the InnoDB I/O Threads](../mariadb-enterprise-server-innodb-operations/configure-the-innodb-io-threads.md) |

## Basic Configuration

```ini
[mariadb]
...
innodb_read_io_threads=8
innodb_write_io_threads=8
```

```sql
SET GLOBAL innodb_read_io_threads=8;
SET GLOBAL innodb_write_io_threads=8;

SHOW GLOBAL VARIABLES
   LIKE 'innodb_%_io_threads';
```

```
+-------------------------+-------+
| Variable_name           | Value |
+-------------------------+-------+
| innodb_read_io_threads  | 8     |
| innodb_write_io_threads | 8     |
+-------------------------+-------+
```

<sub>_This page is: Copyright © 2025 MariaDB. All rights reserved._</sub>

{% @marketo/form formId="4316" %}
