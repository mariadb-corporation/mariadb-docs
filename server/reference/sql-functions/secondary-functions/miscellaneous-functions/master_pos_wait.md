---
description: >-
  Wait for a replica to reach a log position. This function blocks until the
  replica has read and applied updates up to a specified position in the
  master's binary log.
---

# MASTER\_POS\_WAIT

## Syntax

```sql
MASTER_POS_WAIT(log_name,log_pos[,timeout,["connection_name"]])
```

## Description

This function is useful in [replication](../../../../server-usage/storage-engines/myrocks/myrocks-and-replication.md) for controlling primary/replica synchronization. It blocks until the replica has read and applied all updates up to the specified position (`log_name,log_pos`) in the primary log. The return value is the number of log events the replica had to wait for to advance to the specified position. The function returns `NULL` if the replica SQL thread is not started, the replica's primary information is not initialized, the arguments are incorrect, or an error occurs. It returns -1 if\
the timeout has been exceeded. If the replica SQL thread stops while`MASTER_POS_WAIT()` is waiting, the function returns `NULL`. If the replica is past the specified position, the function returns immediately.

If a `timeout` value is specified, `MASTER_POS_WAIT()` stops waiting when `timeout` seconds have elapsed. `timeout` must be greater than 0; a zero or negative `timeout` means no `timeout`.

The `connection_name` is used when you are using [multi-source-replication](../../../../ha-and-performance/standard-replication/multi-source-replication.md). If you don't specify it, it's set to the value of the [default\_master\_connection](../../../../ha-and-performance/standard-replication/replication-and-binary-log-system-variables.md) system variable.

Statements using the `MASTER_POS_WAIT()` function are not [safe for statement-based replication](../../../../ha-and-performance/standard-replication/unsafe-statements-for-statement-based-replication.md).

<sub>_This page is licensed: GPLv2, originally from_</sub> [<sub>_fill\_help\_tables.sql_</sub>](https://github.com/MariaDB/server/blob/main/scripts/fill_help_tables.sql)

{% @marketo/form formId="4316" %}
