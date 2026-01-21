---
description: >-
  The purge process is a garbage collection mechanism that removes old row
  versions from the undo log that are no longer required for MVCC.
---

# InnoDB Purge

When a transaction updates a row in an InnoDB table, InnoDB's MVCC implementation keeps old versions of the row in the [InnoDB undo log](innodb-undo-log.md). The old versions are kept at least until all transactions older than the transaction that updated the row are no longer open. At that point, the old versions can be deleted. InnoDB has purge process that is used to delete these old versions.

## InnoDB Purge Threads

In MariaDB Enterprise Server, the InnoDB storage engine uses Purge Threads to perform garbage collection in the background. The Purge Threads are related to multi-version concurrency control (MVCC).

The Purge Threads perform garbage collection of various items:

* The Purge Threads perform garbage collection of the [InnoDB Undo Log](innodb-undo-log.md). When a row is updated in the clustered index, InnoDB updates the values in the clustered index, and the old row version is added to the Undo Log. The Purge Threads scan the Undo Log for row versions that are not needed by open transactions and permanently delete them. In ES 10.5 and later, if the remaining clustered index record is the oldest possible row version, the Purge Thread resets the record's hidden `DB_TRX_ID` field to 0.
* The Purge Threads perform garbage collection of index records. When an indexed column is updated, InnoDB creates a new index record for the updated value in each affected index, and the old index records are delete-marked. When the primary key column is updated, InnoDB creates a new index record for the updated value in every index, and each old index record is delete-marked. The Purge Threads scan for delete-marked index records and permanently delete them.
* The Purge Threads perform garbage collection of freed overflow pages. [BLOB](../../../reference/data-types/string-data-types/blob.md), [CHAR](../../../reference/data-types/string-data-types/char.md), [TEXT](../../../reference/data-types/string-data-types/text.md), [VARCHAR](../../../reference/data-types/string-data-types/varchar.md), [VARBINARY](../../../reference/data-types/string-data-types/varbinary.md), and related types are sometimes stored on overflow pages. When the value on the overflow page is deleted or updated, the overflow page is no longer needed. The Purge Threads delete these freed overflow pages.

### Feature Summary

| Feature        | Detail                                                                                                  | Resources                                                                                                               |
| -------------- | ------------------------------------------------------------------------------------------------------- | ----------------------------------------------------------------------------------------------------------------------- |
| Thread         | InnoDB Purge Threads                                                                                    |                                                                                                                         |
| Storage Engine | InnoDB                                                                                                  |                                                                                                                         |
| Purpose        | Garbage Collection of: • InnoDB Undo Log • Delete-marked secondary index records • Freed overflow pages |                                                                                                                         |
| Availability   | All ES and CS versions                                                                                  | [MariaDB Enterprise Server](https://app.gitbook.com/o/diTpXxF5WsbHqTReoBsS/s/JqgUabdZsoY5EiaJmqgn/)                     |
| Quantity       | Set by [innodb\_purge\_threads](innodb-system-variables.md#innodb_purge_threads)                        | [Configure the InnoDB Purge Threads](mariadb-enterprise-server-innodb-operations/configure-the-innodb-purge-threads.md) |

### Configuring the Purge Threads

The number of purge threads can be set by configuring the [innodb\_purge\_threads](innodb-system-variables.md#innodb_purge_threads) system variable. This system variable can be specified as a command-line argument to [mariadbd](../../../server-management/starting-and-stopping-mariadb/mariadbd-options.md) or it can be specified in a relevant server [option group](../../../server-management/install-and-upgrade-mariadb/configuring-mariadb/configuring-mariadb-with-option-files.md#option-groups) in an [option file](../../../server-management/install-and-upgrade-mariadb/configuring-mariadb/configuring-mariadb-with-option-files.md):

```
[mariadb]
...
innodb_purge_threads=8
```

```sql
SET GLOBAL innodb_purge_threads=8;

SHOW GLOBAL VARIABLES
   LIKE 'innodb_purge_threads';
```

```
+----------------------+-------+
| Variable_name        | Value |
+----------------------+-------+
| innodb_purge_threads | 8     |
+----------------------+-------+
```

## Optimizing Purge Performance

### Configuring the Purge Batch Size

The purge batch size is defined as the number of [InnoDB undo log](innodb-undo-log.md) records that must be written before triggering purge. The purge batch size can be set by configuring the [innodb\_purge\_batch\_size](innodb-system-variables.md#innodb_purge_batch_size) system variable. This system variable can be specified as a command-line argument to [mariadbd](../../../server-management/starting-and-stopping-mariadb/mariadbd-options.md) or it can be specified in a relevant server [option group](../../../server-management/install-and-upgrade-mariadb/configuring-mariadb/configuring-mariadb-with-option-files.md#option-groups) in an [option file](../../../server-management/install-and-upgrade-mariadb/configuring-mariadb/configuring-mariadb-with-option-files.md):

```
[mariadb]
...
innodb_purge_batch_size = 50
```

### Configuring the Max Purge Lag

If purge operations are lagging on a busy server, then this can be a tough situation to recover from. As a solution, InnoDB allows you to set the max purge lag. The max purge lag is defined as the maximum number of [InnoDB undo log](innodb-undo-log.md) that can be waiting to be purged from the history until InnoDB begins delaying DML statements.

The max purge lag can be set by configuring the [innodb\_max\_purge\_lag](innodb-system-variables.md#innodb_max_purge_lag) system variable. This system variable can be changed dynamically with [SET GLOBAL](../../../reference/sql-statements/administrative-sql-statements/set-commands/set.md#global-session):

```sql
SET GLOBAL innodb_max_purge_lag=1000;
```

This system variable can also be specified as a command-line argument to [mariadbd](../../../server-management/starting-and-stopping-mariadb/mariadbd-options.md) or it can be specified in a relevant server [option group](../../../server-management/install-and-upgrade-mariadb/configuring-mariadb/configuring-mariadb-with-option-files.md#option-groups) in an [option file](../../../server-management/install-and-upgrade-mariadb/configuring-mariadb/configuring-mariadb-with-option-files.md):

```
[mariadb]
...
innodb_max_purge_lag = 1000
```

The maximum delay can be set by configuring the [innodb\_max\_purge\_lag\_delay](innodb-system-variables.md#innodb_max_purge_lag_delay) system variable. This system variable can be changed dynamically with [SET GLOBAL](../../../reference/sql-statements/administrative-sql-statements/set-commands/set.md#global-session):

```sql
SET GLOBAL innodb_max_purge_lag_delay=100;
```

This system variable can also be specified as a command-line argument to [mariadbd](../../../server-management/starting-and-stopping-mariadb/mariadbd-options.md) or it can be specified in a relevant server [option group](../../../server-management/install-and-upgrade-mariadb/configuring-mariadb/configuring-mariadb-with-option-files.md#option-groups) in an [option file](../../../server-management/install-and-upgrade-mariadb/configuring-mariadb/configuring-mariadb-with-option-files.md):

```
[mariadb]
...
innodb_max_purge_lag_delay = 100
```

### Configuring the Purge Rollback Segment Truncation Frequency

The purge rollback segment truncation frequency is defined as the number of purge loops that are run before unnecessary rollback segments are truncated. The purge rollback segment truncation frequency can be set by configuring the [innodb\_purge\_rseg\_truncate\_frequency](innodb-system-variables.md#innodb_purge_rseg_truncate_frequency) system variable. This system variable can be changed dynamically with [SET GLOBAL](../../../reference/sql-statements/administrative-sql-statements/set-commands/set.md#global-session):

```sql
SET GLOBAL innodb_purge_rseg_truncate_frequency=64;
```

This system variable can also be specified as a command-line argument to [mariadbd](../../../server-management/starting-and-stopping-mariadb/mariadbd-options.md) or it can be specified in a relevant server [option group](../../../server-management/install-and-upgrade-mariadb/configuring-mariadb/configuring-mariadb-with-option-files.md#option-groups) in an [option file](../../../server-management/install-and-upgrade-mariadb/configuring-mariadb/configuring-mariadb-with-option-files.md):

```
[mariadb]
...
innodb_purge_rseg_truncate_frequency = 64
```

### Configuring the Purge Undo Log Truncation

Purge undo log truncation occurs when InnoDB truncates an entire [InnoDB undo log](innodb-undo-log.md) tablespace, rather than deleting individual [InnoDB undo log](innodb-undo-log.md) records.

Purge undo log truncation can be enabled by configuring the [innodb\_undo\_log\_truncate](innodb-system-variables.md#innodb_undo_log_truncate) system variable. This system variable can be changed dynamically with [SET GLOBAL](../../../reference/sql-statements/administrative-sql-statements/set-commands/set.md#global-session):

```sql
SET GLOBAL innodb_undo_log_truncate=ON;
```

This system variable can also be specified as a command-line argument to [mariadbd](../../../server-management/starting-and-stopping-mariadb/mariadbd-options.md) or it can be specified in a relevant server [option group](../../../server-management/install-and-upgrade-mariadb/configuring-mariadb/configuring-mariadb-with-option-files.md#option-groups) in an [option file](../../../server-management/install-and-upgrade-mariadb/configuring-mariadb/configuring-mariadb-with-option-files.md):

```
[mariadb]
...
innodb_undo_log_truncate = ON
```

An [InnoDB undo log](innodb-undo-log.md) tablespace is truncated when it exceeds the maximum size that is configured for [InnoDB undo log](innodb-undo-log.md) tablespaces. The maximum size can be set by configuring the [innodb\_max\_undo\_log\_size](innodb-system-variables.md#innodb_max_undo_log_size) system variable. This system variable can be changed dynamically with [SET GLOBAL](../../../reference/sql-statements/administrative-sql-statements/set-commands/set.md#global-session):

```sql
SET GLOBAL innodb_max_undo_log_size='64M';
```

This system variable can also be specified as a command-line argument to [mariadbd](../../../server-management/starting-and-stopping-mariadb/mariadbd-options.md) or it can be specified in a relevant server [option group](../../../server-management/install-and-upgrade-mariadb/configuring-mariadb/configuring-mariadb-with-option-files.md#option-groups) in an [option file](../../../server-management/install-and-upgrade-mariadb/configuring-mariadb/configuring-mariadb-with-option-files.md):

```
[mariadb]
...
innodb_max_undo_log_size = 64M
```

## Purge's Effect on Row Metadata

An InnoDB table's clustered index has three hidden system columns that are automatically generated. These hidden system columns are:

* `DB_ROW_ID` - If the table has no other `PRIMARY KEY` or no other `UNIQUE KEY` defined as `NOT NULL` that can be promoted to the table's `PRIMARY KEY`, then InnoDB will use a hidden system column called `DB_ROW_ID`. InnoDB will automatically generated the value for the column from a global InnoDB-wide 48-bit sequence (instead of being table-local).
* `DB_TRX_ID` - The transaction ID of either the transaction that last changed the row or the transaction that currently has the row locked.
* `DB_ROLL_PTR` - A pointer to the [InnoDB undo log](innodb-undo-log.md) that contains the row's previous record. The value of `DB_ROLL_PTR` is only valid if `DB_TRX_ID` belongs to the current read view. The oldest valid read view is the purge view.

If a row's last [InnoDB undo log](innodb-undo-log.md) record is purged, this can obviously effect the value of the row's `DB_ROLL_PTR` column, because there would no longer be any [InnoDB undo log](innodb-undo-log.md) record for the pointer to reference.

The purge process will set a row's `DB_TRX_ID` column to `0` after all of the row's associated [InnoDB undo log](innodb-undo-log.md) records have been deleted. This change allows InnoDB to perform an optimization: if a query wants to read a row, and if the row's `DB_TRX_ID` column is set to `0`, then it knows that no other transaction has the row locked. Usually, InnoDB needs to lock the transaction system's mutex in order to safely check whether a row is locked, but this optimization allows InnoDB to confirm that the row can be safely read without any heavy internal locking.

This optimization can speed up reads, but it come at a noticeable cost at other times. For example, it can cause the purge process to use more I/O after inserting a lot of rows, since the value of each row's `DB_TRX_ID` column will have to be reset.

<sub>_This page is licensed: CC BY-SA / Gnu FDL_</sub>

{% @marketo/form formId="4316" %}
