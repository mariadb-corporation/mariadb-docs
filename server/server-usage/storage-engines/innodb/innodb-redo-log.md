---
description: >-
  The redo log is a disk-based transaction log used during crash recovery to
  replay incomplete transactions and ensure data durability.
---

# InnoDB Redo Log

Directly editing or moving the redo logs can cause corruption, and should never normally be attempted.

## Overview

The InnoDB storage engine in MariaDB Enterprise Server employs a **Redo Log** to ensure data is written to disk reliably, even in the event of a crash. This is achieved by the Redo Log acting as a transaction log.

Redo Log records are uniquely identified by a **Log Sequence Number (LSN)**. The Redo Log consists of circular log files of a fixed size, where older records are routinely overwritten by newer ones.

InnoDB periodically performs **checkpoints**. During a checkpoint operation, InnoDB writes (flushes) the Redo Log records to the InnoDB tablespace files.

In the event of a server crash, InnoDB utilizes the Redo Log for **crash recovery** during the subsequent server startup. It locates the last checkpoint within the Redo Log and then replays the Redo Log records generated since that checkpoint, effectively flushing these pending changes to the InnoDB tablespace files.

The redo log files are typically named `ib_logfileN`, where `N` is an integer. However, starting with [MariaDB 10.5](https://app.gitbook.com/s/aEnK0ZXmUbJzqQrTjFyb/community-server/old-releases/10.5/what-is-mariadb-105), there is a single redo log file, consistently named `ib_logfile0`. The location of these redo log files is determined by the `innodb_log_group_home_dir` system variable, if configured. If this variable is not set, the redo log files are created in the directory specified by the `datadir` system variable. The redo log plays a crucial role during crash recovery and in the background process of flushing transactions to the tablespaces.

## Feature Summary

| Feature         | Detail                                                                                                                                                                                                                        | Resources                                                                                                     |
| --------------- | ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ------------------------------------------------------------------------------------------------------------- |
| Transaction Log | InnoDB Redo Log                                                                                                                                                                                                               |                                                                                                               |
| Storage Engine  | InnoDB                                                                                                                                                                                                                        |                                                                                                               |
| Purpose         | Crash Safety                                                                                                                                                                                                                  |                                                                                                               |
| Availability    | All ES and CS versions                                                                                                                                                                                                        | [MariaDB Enterprise Server](https://app.gitbook.com/o/diTpXxF5WsbHqTReoBsS/s/JqgUabdZsoY5EiaJmqgn/)           |
| Location        | Set by [innodb\_log\_group\_home\_dir](innodb-system-variables.md#innodb_log_group_home_dir) (Defaults to [datadir](../../../ha-and-performance/optimization-and-tuning/system-variables/server-system-variables.md#datadir)) |                                                                                                               |
| Quantity        | 1 (ES 10.5+, CS 10.5+)                                                                                                                                                                                                        | [Configure the InnoDB Redo Log](mariadb-enterprise-server-innodb-operations/configure-the-innodb-redo-log.md) |
| Size            | Set by [innodb\_log\_file\_size](innodb-system-variables.md#innodb_log_file_size) (default varies)                                                                                                                            | [Configure the InnoDB Redo Log](mariadb-enterprise-server-innodb-operations/configure-the-innodb-redo-log.md) |

## Basic Configuration

```
[mariadb]
...
innodb_log_file_size=2G
```

```sql
SET GLOBAL innodb_log_file_size=(2 * 1024 * 1024 * 1024);

SHOW GLOBAL VARIABLES
   LIKE 'innodb_log_file_size';
```

```
+----------------------+------------+
| Variable_name        | Value      |
+----------------------+------------+
| innodb_log_file_size | 2147483648 |
+----------------------+------------+
```

## Flushing Effects on Performance and Consistency

The [innodb\_flush\_log\_at\_trx\_commit](innodb-system-variables.md#innodb_flush_log_at_trx_commit) system variable determines how often the transactions are flushed to the redo log, and it is important to achieve a good balance between speed and reliability.

### Binary Log Group Commit and Redo Log Flushing

When both [innodb\_flush\_log\_at\_trx\_commit=1](innodb-system-variables.md#innodb_flush_log_at_trx_commit) (the default) is set and the [binary log](../../../server-management/server-monitoring-logs/binary-log/) is enabled, there is one less sync to disk inside InnoDB during commit (2 syncs shared between a group of transactions instead of 3). See [Binary Log Group Commit and InnoDB Flushing Performance](binary-log-group-commit-and-innodb-flushing-performance.md) for more information.

## Redo Log Group Capacity

The redo log group capacity is the total combined size of all InnoDB redo logs. The relevant factors are:

* From [MariaDB 10.5](https://app.gitbook.com/s/aEnK0ZXmUbJzqQrTjFyb/community-server/old-releases/10.5/what-is-mariadb-105), there is 1 redo log.
* The size of each redo log file is configured by the [innodb\_log\_file\_size](innodb-system-variables.md#innodb_log_file_size) system variable. This can safely be set to a much higher value from [MariaDB 10.5](https://app.gitbook.com/s/aEnK0ZXmUbJzqQrTjFyb/community-server/old-releases/10.5/what-is-mariadb-105). Before [MariaDB 10.9](https://app.gitbook.com/s/aEnK0ZXmUbJzqQrTjFyb/community-server/old-releases/10.9/what-is-mariadb-109), resizing required the server to be restarted. From [MariaDB 10.9](https://app.gitbook.com/s/aEnK0ZXmUbJzqQrTjFyb/community-server/old-releases/10.9/what-is-mariadb-109) the variable can be set dynamically.

The redo log group capacity is determined by the following calculation:

`innodb_log_group_capacity` = [innodb\_log\_file\_size](innodb-system-variables.md#innodb_log_file_size) \* [innodb\_log\_files\_in\_group](innodb-system-variables.md#innodb_log_files_in_group)

For example, if [innodb\_log\_file\_size](innodb-system-variables.md#innodb_log_file_size) is set to `2G` and [innodb\_log\_files\_in\_group](innodb-system-variables.md#innodb_log_files_in_group) is set to `2`, then we would have the following:

* `innodb_log_group_capacity` = [innodb\_log\_file\_size](innodb-system-variables.md#innodb_log_file_size) \* [innodb\_log\_files\_in\_group](innodb-system-variables.md#innodb_log_files_in_group)
* \= `2G` \* `2`
* \= `4G`

### Changing the Redo Log Group Capacity

**MariaDB starting with** [**10.5**](https://app.gitbook.com/s/aEnK0ZXmUbJzqQrTjFyb/community-server/old-releases/10.5/what-is-mariadb-105)

The number of redo log files is fixed.

The size of redo log files can be changed with the following process:

* Stop the server.
* To change the log file size, configure [innodb\_log\_file\_size](innodb-system-variables.md#innodb_log_file_size).
* Start the server.

## Log Sequence Number (LSN)

Records within the InnoDB redo log are identified via a log sequence number (LSN).

## Checkpoints

When InnoDB performs a checkpoint, it writes the LSN of the oldest dirty page in the [InnoDB buffer pool](innodb-buffer-pool.md) to the InnoDB redo log. If a page is the oldest dirty page in the [InnoDB buffer pool](innodb-buffer-pool.md), then that means that all pages with lower LSNs have been flushed to the physical InnoDB tablespace files. If the server were to crash, then InnoDB would perform crash recovery by only applying log records with LSNs that are greater than or equal to the LSN of the oldest dirty page written in the last checkpoint.

Checkpoints are one of the tasks performed by the InnoDB master background thread. This thread schedules checkpoints 7 seconds apart when the server is very active, but checkpoints can happen more frequently when the server is less active.

Dirty pages are not actually flushed from the buffer pool to the physical InnoDB tablespace files during a checkpoint. That process happens asynchronously on a continuous basis by InnoDB's write I/O background threads configured by the [innodb\_write\_io\_threads](innodb-system-variables.md#innodb_write_io_threads) system variable. If you want to make this process more aggressive, then you can decrease the value of the [innodb\_max\_dirty\_pages\_pct](innodb-system-variables.md#innodb_max_dirty_pages_pct) system variable. You may also need to better tune InnoDB's I/O capacity on your system by setting the [innodb\_io\_capacity](innodb-system-variables.md#innodb_io_capacity) system variable.

### Determining the Checkpoint Age

The checkpoint age is the amount of data written to the InnoDB redo log since the last checkpoint.

#### Determining the Checkpoint Age in InnoDB

**MariaDB starting with** [**10.5**](https://app.gitbook.com/s/aEnK0ZXmUbJzqQrTjFyb/community-server/old-releases/10.5/what-is-mariadb-105)

[MariaDB 10.5](https://app.gitbook.com/s/aEnK0ZXmUbJzqQrTjFyb/community-server/old-releases/10.5/what-is-mariadb-105) reintroduced the [Innodb\_checkpoint\_age](../../../ha-and-performance/optimization-and-tuning/system-variables/innodb-status-variables.md#innodb_checkpoint_age) status variable for determining the checkpoint age.

The checkpoint age can also be determined by the process shown below.

To determine the InnoDB checkpoint age, do the following:

* Query [SHOW ENGINE INNODB STATUS](../../../reference/sql-statements/administrative-sql-statements/show/show-engine-innodb-status.md).
* Find the `LOG` section:

```
---
LOG
---
Log sequence number 252794398789379
Log flushed up to 252794398789379
Pages flushed up to 252792767756840
Last checkpoint at 252792767756840
0 pending log flushes, 0 pending chkp writes
23930412 log i/o's done, 2.03 log i/o's/second
```

* Perform the following calculation:

`innodb_checkpoint_age` = `Log sequence number` - `Last checkpoint at`

In the example above, that would be:

* `innodb_checkpoint_age` = `Log sequence number` - `Last checkpoint at`
* \= 252794398789379 - 252792767756840
* \= 1631032539 bytes
* \= 1631032539 byes / (1024 \* 1024 \* 1024) (GB/bytes)
* \= 1.5 GB of redo log written since last checkpoint

## Determining the Redo Log Occupancy

The redo log occupancy is the percentage of the InnoDB redo log capacity that is taken up by dirty pages that have not yet been flushed to the physical InnoDB tablespace files in a checkpoint. Therefore, it's determined by the following calculation:

`innodb_log_occupancy` = [innodb\_checkpoint\_age](innodb-redo-log.md#determining-the-checkpoint-age) / [innodb\_log\_group\_capacity](innodb-redo-log.md#redo-log-group-capacity)

For example, if [innodb\_checkpoint\_age](innodb-redo-log.md#determining-the-checkpoint-age) is `1.5G` and [innodb\_log\_group\_capacity](innodb-redo-log.md#redo-log-group-capacity) is `4G`, then we would have the following:

* `innodb_log_occupancy` = [innodb\_checkpoint\_age](innodb-redo-log.md#determining-the-checkpoint-age) / [innodb\_log\_group\_capacity](innodb-redo-log.md#redo-log-group-capacity)
* \= `1.5G` / `4G`
* \= `0.375`

If the calculated value for redo log occupancy is too close to `1.0`, then the InnoDB redo log capacity may be too small for the current workload.

## [MariaDB 10.8](https://app.gitbook.com/s/aEnK0ZXmUbJzqQrTjFyb/community-server/old-releases/10.8/what-is-mariadb-108) Updates

A number of redo log improvements were made in [MariaDB 10.8](https://app.gitbook.com/s/aEnK0ZXmUbJzqQrTjFyb/community-server/old-releases/10.8/what-is-mariadb-108):

* Autosize innodb\_buffer\_pool\_chunk\_size ([MDEV-25342](https://jira.mariadb.org/browse/MDEV-25342)).
* Improve the redo log for concurrency ([MDEV-14425](https://jira.mariadb.org/browse/MDEV-14425)).
* Remove FIL\_PAGE\_FILE\_FLUSH\_LSN ([MDEV-27199](https://jira.mariadb.org/browse/MDEV-27199)).

Before [MariaDB 10.8.1](https://app.gitbook.com/s/aEnK0ZXmUbJzqQrTjFyb/community-server/old-releases/10.8/10.8.1), [mariadb-backup --prepare](../../backup-and-restore/mariadb-backup/mariadb-backup-options.md#prepare) created a zero-length ib\_logfile0 as a dummy placeholder. From [MariaDB 10.8.1](https://app.gitbook.com/s/aEnK0ZXmUbJzqQrTjFyb/community-server/old-releases/10.8/10.8.1) ([MDEV-14425](https://jira.mariadb.org/browse/MDEV-14425)), the size of that dummy file was increased to 12304 (0x3010) bytes, and all updates of FIL\_PAGE\_FILE\_FLUSH\_LSN in the first page of the system tablespace are removed.

From [MariaDB 10.8.1](https://app.gitbook.com/s/aEnK0ZXmUbJzqQrTjFyb/community-server/old-releases/10.8/10.8.1), if the server is started up with a zero-sized ib\_logfile0, it is assumed that an upgrade is being performed after a backup had been prepared. The start LSN will then be read from FIL\_PAGE\_FILE\_FLUSH\_LSN, and a new log file are created starting from exactly that LSN.

Manually creating a zero-sized ib\_logfile0 without manually updating the FIL\_PAGE\_FILE\_FLUSH\_LSN in the system tablespace to a recent enough LSN may result in error messages such as "page LSN is in the future". If a log was discarded while some changes had already been written to data pages, all sort of corruption may occur.

If the database was initialized with a server that never updates the FIL\_PAGE\_FILE\_FLUSH\_LSN field, then any server startup attempts with a zero-size ib\_logfile0 are refused because of an invalid LSN. If that field was ever updated with a valid LSN by an older server, this safety mechanism cannot work, and the server may "rewind" to an earlier LSN.

<sub>_This page is licensed: CC BY-SA / Gnu FDL_</sub>

{% @marketo/form formId="4316" %}
