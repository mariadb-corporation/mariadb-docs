---
description: >-
  The undo log stores the "before" image of data modified by active
  transactions, supporting rollbacks and consistent read views.
---

# InnoDB Undo Log

## Overview

When a [transaction](../../../reference/sql-statements/transactions/) writes data, it always inserts them in the table indexes or data (in the buffer pool or in physical files). No private copies are created. The old versions of data being modified by active [InnoDB](./) transactions are stored in the undo log. The original data can then be restored, or viewed by a consistent read.

## Implementation Details

Before a row is modified, a diff is copied into the undo log. Each normal row contains a pointer to the most recent version of the same row in the undo log. Each row in the undo log contains a pointer to previous version, if any. So, each modified row has a history chain.

Rows are never physically deleted until a transaction ends. If they were deleted, the restore in `ROLLBACK` would be impossible. Thus, rows are simply marked for deletion.

Each transaction uses a _view_ of the records. The [transaction isolation level](../../../reference/sql-statements/transactions/set-transaction.md#isolation-levels) determines how this view is created. For example, `READ UNCOMMITTED` usually uses the current version of rows, even if they are not committed (_dirty reads_). Other isolation levels require that the most recent committed version of rows is searched in the undo log. `READ` `COMMITTED` uses a different view for each table, while `REPEATABLE READ` and `SERIALIZABLE` use the same view for all tables.

There is also a global history list of the data. When a transaction is committed, its history is added to this history list. The order of the list is the chronological order of the commits.

The purge thread deletes the rows in the undo log which are not needed by any existing view. The rows for which a most recent version exists are deleted, as well as the delete-marked rows.

If InnoDB needs to restore an old version, it will simply replace the newer version with the older one. When a transaction inserts a new row, there is no older version. However, in that case, the restore can be done by deleting the inserted rows.

## Effects of Long-Running Transactions

Understanding how the undo log works helps with understanding the negative effects long transactions.

* Long transactions generate several old versions of the rows in the undo log. Those rows will probably be needed for a longer time, because other long transactions will need them. Since those transactions will generate more modified rows, a sort of combinatorial explosion can be observed. Thus, the undo log requires more space.
* Transaction may need to read very old versions of the rows in the history list, thus their performance will degrade.

Of course read-only transactions do not write more entries in the undo log; however, they delay the purging of existing entries.

Also, long transactions can more likely result in deadlocks, but this problem is not related to the undo log.

## Feature Summary

| Feature         | Detail                                                                                                                               | Resources                                                                                                                                                                                                                                                                  |
| --------------- | ------------------------------------------------------------------------------------------------------------------------------------ | -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| Transaction Log | InnoDB Undo Log                                                                                                                      |                                                                                                                                                                                                                                                                            |
| Storage Engine  | InnoDB                                                                                                                               |                                                                                                                                                                                                                                                                            |
| Purpose         | Multi-Version Concurrency Control (MVCC)                                                                                             |                                                                                                                                                                                                                                                                            |
| Availability    | All ES and CS versions                                                                                                               | [MariaDB Enterprise Server](https://app.gitbook.com/o/diTpXxF5WsbHqTReoBsS/s/JqgUabdZsoY5EiaJmqgn/)                                                                                                                                                                        |
| Location        | By default, located in InnoDB system tablespace When [innodb\_undo\_tablespaces](innodb-system-variables.md#innodb_undo_tablespaces) | `innodb_undo_tablespaces` is set, located in directory set by [innodb\_undo\_directory](innodb-system-variables.md#innodb_undo_directory) (Defaults to [datadir](../../../ha-and-performance/optimization-and-tuning/system-variables/server-system-variables.md#datadir)) |
| Quantity        | Set by [innodb\_undo\_tablespaces](innodb-system-variables.md#innodb_undo_tablespaces)                                               | [Configure the InnoDB Undo Log](mariadb-enterprise-server-innodb-operations/configure-the-innodb-undo-log.md)                                                                                                                                                              |
| Size            | 10 MB per tablespace by default (grows as needed)                                                                                    |                                                                                                                                                                                                                                                                            |

## Configuration

System variables affecting undo logs include:

* [innodb\_max\_undo\_log\_size](innodb-system-variables.md#innodb_max_undo_log_size)
* [innodb\_undo\_directory](innodb-system-variables.md#innodb_undo_directory)
* [innodb\_undo\_log\_truncate](innodb-system-variables.md#innodb_undo_log_truncate)
* [innodb\_undo\_logs](innodb-system-variables.md#innodb_undo_logs)
* [innodb\_undo\_tablespaces](innodb-system-variables.md#innodb_undo_tablespaces)
* [innodb\_purge\_batch\_size](innodb-system-variables.md#innodb_purge_batch_size)
* [innodb\_purge\_rseg\_truncate\_frequency](innodb-system-variables.md#innodb_purge_rseg_truncate_frequency)

The undo log is not a log file that can be viewed on disk in the usual sense, such as the [error log](../../../server-management/server-monitoring-logs/error-log.md) or [slow query log](../../../server-management/server-monitoring-logs/slow-query-log/), but rather an area of storage.

Before [MariaDB 11.0](https://app.gitbook.com/s/aEnK0ZXmUbJzqQrTjFyb/community-server/old-releases/release-notes-mariadb-11-0-series/what-is-mariadb-110), the undo log is usually part of the physical system tablespace, but from [MariaDB 10.0](https://app.gitbook.com/s/aEnK0ZXmUbJzqQrTjFyb/community-server/old-releases/release-notes-mariadb-10-0-series/changes-improvements-in-mariadb-10-0), the [innodb\_undo\_directory](innodb-system-variables.md#innodb_undo_directory) and [innodb\_undo\_tablespaces](innodb-system-variables.md#innodb_undo_tablespaces) system variables can be used to split into different tablespaces and store in a different location (perhaps on a different storage device). From [MariaDB 11.0](https://app.gitbook.com/s/aEnK0ZXmUbJzqQrTjFyb/community-server/old-releases/release-notes-mariadb-11-0-series/what-is-mariadb-110), multiple undo tablespaces are enabled by default, and the [innodb\_undo\_tablespaces](innodb-system-variables.md#innodb_undo_tablespaces) default is changed to 3 so that the space occupied by possible bursts of undo log records can be reclaimed after [innodb\_undo\_log\_truncate](innodb-system-variables.md#innodb_undo_log_truncate) is set.

Each insert or update portion of the undo log is known as a rollback segment. The [innodb\_undo\_logs](innodb-system-variables.md#innodb_undo_logs) system variable allowed to reduce the number of rollback segments from the usual 128, to limit the number of concurrently active write transactions. [innodb\_undo\_logs](innodb-system-variables.md#innodb_undo_logs) was deprecated and ignored in [MariaDB 10.5](https://app.gitbook.com/s/aEnK0ZXmUbJzqQrTjFyb/community-server/old-releases/mariadb-10-5-series/what-is-mariadb-105) and removed in [MariaDB 10.6](https://app.gitbook.com/s/aEnK0ZXmUbJzqQrTjFyb/community-server/mariadb-10-6-series/what-is-mariadb-106), as it always makes sense to use the maximum number of rollback segments.

The related [innodb\_available\_undo\_logs](../../../ha-and-performance/optimization-and-tuning/system-variables/innodb-status-variables.md#innodb_available_undo_logs) status variable stores the total number of available InnoDB undo logs.

<sub>_This page is licensed: CC BY-SA / Gnu FDL_</sub>

{% @marketo/form formId="4316" %}
