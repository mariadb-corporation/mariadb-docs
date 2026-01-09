---
description: >-
  Describes the group commit optimization, which improves performance by
  committing multiple transactions to the binary log in a single disk I/O
  operation.
---

# Group Commit for the Binary Log

## Overview

The server supports group commit. This is an important optimization that helps MariaDB reduce the number of expensive disk operations that are performed.

## Durability

In ACID terminology, the "D" stands for durability. In order to ensure durability with group commit, [innodb\_flush\_log\_at\_trx\_commit=1](../../../server-usage/storage-engines/innodb/innodb-system-variables.md#innodb_flush_log_at_trx_commit) and/or [sync\_binlog=1](../../../ha-and-performance/standard-replication/replication-and-binary-log-system-variables.md#sync_binlog) should be set. These settings are needed to ensure that if the server crashes, then any transaction that was committed prior to the time of crash will still be present in the database after crash recovery.

### Durable InnoDB Data and Binary Logs

Setting both [innodb\_flush\_log\_at\_trx\_commit=1](../../../server-usage/storage-engines/innodb/innodb-system-variables.md#innodb_flush_log_at_trx_commit) and [sync\_binlog=1](../../../ha-and-performance/standard-replication/replication-and-binary-log-system-variables.md#sync_binlog) provides the most durability and the best guarantee of [replication](../../../ha-and-performance/standard-replication/) consistency after a crash.

### Non-Durable InnoDB Data

If [sync\_binlog=1](../../../ha-and-performance/standard-replication/replication-and-binary-log-system-variables.md#sync_binlog) is set, but [innodb\_flush\_log\_at\_trx\_commit](../../../server-usage/storage-engines/innodb/innodb-system-variables.md#innodb_flush_log_at_trx_commit) is not set to `1` or `3`, then it is possible after a crash to end up in a state where a transaction present in a server's [binary log](./) is missing from the server's [InnoDB redo log](../../../server-usage/storage-engines/innodb/innodb-redo-log.md). If the server is a [replication primary](../../../ha-and-performance/standard-replication/), then that means that the server can become inconsistent with its replicas, since the replicas may have replicated transactions from the primary's [binary log](./) that are no longer present in the primary's local [InnoDB](../../../server-usage/storage-engines/innodb/) data.

### Non-Durable Binary Logs

If [innodb\_flush\_log\_at\_trx\_commit](../../../server-usage/storage-engines/innodb/innodb-system-variables.md) is set to `1` or `3`, but [sync\_binlog=1](../../../ha-and-performance/standard-replication/replication-and-binary-log-system-variables.md) is not set, then it is possible after a crash to end up in a state where a transaction present in a server's [InnoDB redo log](../../../server-usage/storage-engines/innodb/innodb-redo-log.md) is missing from the server's [binary log](./). If the server is a [replication primary](../../../ha-and-performance/standard-replication/), then that also means that the server can become inconsistent with its replicas, since the server's replicas would not be able to replicate the missing transactions from the server's [binary log](./).

### Non-Durable InnoDB Data and Binary Logs

Setting [innodb\_flush\_log\_at\_trx\_commit=1](../../../server-usage/storage-engines/innodb/innodb-system-variables.md#innodb_flush_log_at_trx_commit) when [sync\_binlog=1](../../../ha-and-performance/standard-replication/replication-and-binary-log-system-variables.md) is not set can also cause the transaction to be missing from the server's [InnoDB redo log](../../../server-usage/storage-engines/innodb/innodb-redo-log.md) due to some optimizations added in those versions. In that case, it is recommended to always set [sync\_binlog=1](../../../ha-and-performance/standard-replication/replication-and-binary-log-system-variables.md). If you can't do that, then it is recommended to set [innodb\_flush\_log\_at\_trx\_commit](../../../server-usage/storage-engines/innodb/innodb-system-variables.md) to `3`, rather than `1`. See [Non-durable Binary Log Settings](../../../server-usage/storage-engines/innodb/binary-log-group-commit-and-innodb-flushing-performance.md#non-durable-binary-log-settings) for more information.

## Amortizing Disk Flush Costs

After every transaction [COMMIT](../../../reference/sql-statements/transactions/commit.md), the server normally has to flush any changes the transaction made to the [InnoDB redo log](../../../server-usage/storage-engines/innodb/innodb-redo-log.md) and the [binary log](./) to disk (i.e. by calling system calls such as `fsync()` or `fdatasync()` or similar). This helps ensure that the data changes made by the transaction are stored durably on the disk. Disk flushing is a time-consuming operation, and can easily impose limits on throughput in terms of the number of transactions-per-second (TPS) which can be committed.

The idea with group commit is to amortize the costs of each flush to disk over multiple commits from multiple parallel transactions. For example, if there are 10 transactions trying to commit in parallel, then we can force all of them to be flushed disk at once with a single system call, rather than do one system call for each commit. This can greatly reduce the need for flush operations, and can consequently greatly improve the throughput of transactions-per-second (TPS).

However, to see the positive effects of group commit, the workload must have sufficient parallelism. A good rule of thumb is that at least three parallel transactions are needed for group commit to be effective. For example, while the first transaction is waiting for its flush operation to complete, the other two transactions will queue up waiting for their turn to flush their changes to disk. When the first transaction is done, a single system call can be used to flush the two queued-up transactions, saving in this case one of the three system calls.

In addition to sufficient parallelism, it is also necessary to have enough transactions per second wanting to commit that the flush operations are a bottleneck. If no such bottleneck exists (i.e. transactions never or rarely\
need to wait for the flush of another to complete), then group commit will provide little to no improvement.

## Changing Group Commit Frequency

The frequency of group commits can be changed by configuring the [binlog\_commit\_wait\_usec](../../../ha-and-performance/standard-replication/replication-and-binary-log-system-variables.md#binlog_commit_wait_usec) and [binlog\_commit\_wait\_count](../../../ha-and-performance/standard-replication/replication-and-binary-log-system-variables.md#binlog_commit_wait_count) system variables.

## Measuring Group Commit Ratio

Two status variables are available for checking how\
effective group commit is at reducing flush overhead. These are the [Binlog\_commits](../../../ha-and-performance/standard-replication/replication-and-binary-log-status-variables.md#binlog_commits) and [Binlog\_group\_commits](../../../ha-and-performance/standard-replication/replication-and-binary-log-status-variables.md#binlog_group_commits) status variables. We can obtain those values with the following query:

```
SHOW GLOBAL STATUS WHERE Variable_name IN('Binlog_commits', 'Binlog_group_commits');
```

[Binlog\_commits](../../../ha-and-performance/standard-replication/replication-and-binary-log-status-variables.md#binlog_commits) is the total number of transactions committed to the [binary log](./).

[Binlog\_group\_commits](../../../ha-and-performance/standard-replication/replication-and-binary-log-status-variables.md#binlog_group_commits) is the total number of groups committed to the [binary log](./). As explained in the previous sections of this page, a group commit is when a group of transactions is flushed to the [binary log](./) together by sharing a single flush system call. When [sync\_binlog=1](../../../ha-and-performance/standard-replication/replication-and-binary-log-system-variables.md#sync_binlog) is set, then this is also the total number of flush system calls executed in the process of flushing commits to the [binary log](./).

Thus the extent to which group commit is effective at reducing the number of flush system calls on the binary log can be determined by the ratio between these two status variables. [Binlog\_commits](../../../ha-and-performance/standard-replication/replication-and-binary-log-status-variables.md#binlog_commits) will always be as equal to or greater than [Binlog\_group\_commits](../../../ha-and-performance/standard-replication/replication-and-binary-log-status-variables.md#binlog_group_commits). The greater the difference is between these status variables, the more effective group commit was at reducing flush overhead.

To calculate the group commit ratio, we actually need the values of these status variables from two snapshots. Then we can calculate the ratio with the following formula:

`transactions/group commit` = (`Binlog_commits` (_snapshot2_) - `Binlog_commits` (_snapshot1_))/(`Binlog_group_commits` (_snapshot2_) - `Binlog_group_commits` (_snapshot1_))

For example, if we had the following first snapshot:

```sql
SHOW GLOBAL STATUS WHERE Variable_name IN('Binlog_commits', 'Binlog_group_commits');
+----------------------+-------+
| Variable_name        | Value |
+----------------------+-------+
| Binlog_commits       | 120   |
| Binlog_group_commits | 120   |
+----------------------+-------+
2 rows in set (0.00 sec)
```

And the following second snapshot:

```sql
SHOW GLOBAL STATUS WHERE Variable_name IN('Binlog_commits', 'Binlog_group_commits');
+----------------------+-------+
| Variable_name        | Value |
+----------------------+-------+
| Binlog_commits       | 220   |
| Binlog_group_commits | 145   |
+----------------------+-------+
2 rows in set (0.00 sec)
```

Then we would have:

`transactions/group commit` = (220 - 120) / (145 - 120) = 100 / 25 = 4 `transactions/group commit`

If your group commit ratio is too close to 1, then it may help to [change your group commit frequency](group-commit-for-the-binary-log.md#changing-group-commit-frequency).

## Use of Group Commit with Parallel Replication

Group commit is also used to enable [conservative mode of in-order parallel replication](../../../ha-and-performance/standard-replication/parallel-replication.md#conservative-mode-of-in-order-parallel-replication).

## Effects of Group Commit on InnoDB Performance

When both [innodb\_flush\_log\_at\_trx\_commit=1](../../../server-usage/storage-engines/innodb/innodb-system-variables.md#innodb_flush_log_at_trx_commit) (the default) is set and the [binary log](./) is enabled, there is now one less sync to disk inside InnoDB during commit (2 syncs shared between a group of transactions instead of 3). See [Binary Log Group Commit and InnoDB Flushing Performance](../../../server-usage/storage-engines/innodb/binary-log-group-commit-and-innodb-flushing-performance.md) for more information.

## Status Variables

[Binlog\_commits](../../../ha-and-performance/standard-replication/replication-and-binary-log-status-variables.md#binlog_commits) is the total number of transactions committed to the [binary log](./).

[Binlog\_group\_commits](../../../ha-and-performance/standard-replication/replication-and-binary-log-status-variables.md#binlog_group_commits) is the total number of groups committed to the [binary log](./).

[Binlog\_group\_commit\_trigger\_count](../../../ha-and-performance/standard-replication/replication-and-binary-log-status-variables.md#binlog_group_commit_trigger_count) is the total number of group commits triggered because of the number of [binary log](./) commits in the group reached the limit set by the system variable [binlog\_commit\_wait\_count](../../../ha-and-performance/standard-replication/replication-and-binary-log-system-variables.md#binlog_commit_wait_count).

[Binlog\_group\_commit\_trigger\_lock\_wait](../../../ha-and-performance/standard-replication/replication-and-binary-log-status-variables.md#binlog_group_commit_trigger_lock_wait) is the total number of group commits triggered because a [binary log](./) commit was being delayed because of a lock wait where the lock was held by a prior binary log commit. When this happens the later binary log commit is placed in the next group commit.

[Binlog\_group\_commit\_trigger\_timeout](../../../ha-and-performance/standard-replication/replication-and-binary-log-status-variables.md#binlog_group_commit_trigger_timeout) is the total number of group commits triggered because of the time since the first [binary log](./) commit reached the limit set by the system variable [binlog\_commit\_wait\_usec](../../../ha-and-performance/standard-replication/replication-and-binary-log-system-variables.md#binlog_commit_wait_usec).

To query these variables, use a statement such as:

```sql
SHOW GLOBAL STATUS LIKE 'Binlog_%commit%';
```

## See Also

* [Parallel Replication](../../../ha-and-performance/standard-replication/parallel-replication.md)
* [Binary Log Group Commit and InnoDB Flushing Performance](../../../server-usage/storage-engines/innodb/binary-log-group-commit-and-innodb-flushing-performance.md)
* [Group commit benchmark](https://www.facebook.com/note.php?note_id=10150211546215933)

<sub>_This page is licensed: CC BY-SA / Gnu FDL_</sub>

{% @marketo/form formId="4316" %}
