---
description: >-
  Understand how group commit works with InnoDB to improve performance by
  reducing the number of disk syncs required during transaction commits.
---

# Binary Log Group Commit and InnoDB Flushing Performance

## Overview

When both [innodb\_flush\_log\_at\_trx\_commit=1](innodb-system-variables.md#innodb_flush_log_at_trx_commit) (the default) is set and the [binary log](../../../server-management/server-monitoring-logs/binary-log/) is enabled, there is now one less sync to disk inside InnoDB during commit (2 syncs shared between a group of transactions instead of 3).

Durability of commits is not decreased — this is because even if the server crashes before the commit is written to disk by InnoDB, it are recovered from the binary log at next server startup (and it is guaranteed that sufficient information is synced to disk so that such a recovery is always possible).

## Switching to Old Flushing Behavior

The old behavior, with 3 syncs to disk per (group) commit (and consequently lower performance), can be selected with the new [innodb\_flush\_log\_at\_trx\_commit=3](innodb-system-variables.md#innodb_flush_log_at_trx_commit) option. There is normally no\
benefit to doing this, however there are a couple of edge cases to be aware of.

### Non-durable Binary Log Settings

If [innodb\_flush\_log\_at\_trx\_commit=1](innodb-system-variables.md#innodb_flush_log_at_trx_commit) is set and the [binary log](../../../server-management/server-monitoring-logs/binary-log/) is enabled, but [sync\_binlog=0](../../../ha-and-performance/standard-replication/replication-and-binary-log-system-variables.md) is set, then commits are not guaranteed durable inside InnoDB after commit. This is because if [sync\_binlog=0](../../../ha-and-performance/standard-replication/replication-and-binary-log-system-variables.md) is set and if the server crashes, then transactions that were not flushed to the binary log prior to the crash are missing from the binary log.

In this specific scenario, [innodb\_flush\_log\_at\_trx\_commit=3](innodb-system-variables.md#innodb_flush_log_at_trx_commit) can be set to ensure that transactions are durable in InnoDB, even if they are not necessarily durable from the perspective of the binary log.

One should be aware that if [sync\_binlog=0](../../../ha-and-performance/standard-replication/replication-and-binary-log-system-variables.md) is set, then a crash is nevertheless likely to cause transactions to be missing from the binary log. This will cause the binary log and InnoDB to be inconsistent with each other. This is also likely to cause any [replication slaves](../../../ha-and-performance/standard-replication/) to become inconsistent, since transactions are replicated through the [binary log](../../../server-management/server-monitoring-logs/binary-log/). Thus it is recommended to set [sync\_binlog=1](../../../ha-and-performance/standard-replication/replication-and-binary-log-system-variables.md). With the [group commit](../../../server-management/server-monitoring-logs/binary-log/group-commit-for-the-binary-log.md) improvements introduced in [MariaDB 5.3](https://app.gitbook.com/s/aEnK0ZXmUbJzqQrTjFyb/community-server/old-releases/release-notes-mariadb-5-3-series/changes-improvements-in-mariadb-5-3), this setting has much less penalty in recent versions compared to older versions of MariaDB and MySQL.

### Recent Transactions Missing from Backups

[mariadb-backup](../../backup-and-restore/mariadb-backup/mariadb-backup-overview.md) and [Percona XtraBackup](../../../clients-and-utilities/legacy-clients-and-utilities/backing-up-and-restoring-databases-percona-xtrabackup/percona-xtrabackup-overview.md) only see transactions that have been flushed to the [redo log](innodb-redo-log.md). With the [group commit](../../../server-management/server-monitoring-logs/binary-log/group-commit-for-the-binary-log.md) improvements, there may be a small delay (defined by the [binlog\_commit\_wait\_usec](../../../ha-and-performance/standard-replication/replication-and-binary-log-system-variables.md#binlog_commit_wait_usec) system variable) between when a commit happens and when the commit are included in a backup.

Note that the backup will still be fully consistent with itself and the [binary log](../../../server-management/server-monitoring-logs/binary-log/). This problem is normally not an issue in practice. A backup usually takes a long time to complete (relative to the 1 second or so that [binlog\_commit\_wait\_usec](../../../ha-and-performance/standard-replication/replication-and-binary-log-system-variables.md#binlog_commit_wait_usec) is normally set to), and a backup usually includes a lot of transactions that were committed during the backup. With this in mind, it is not generally noticeable if the backup does not include transactions that were committed during the last 1 second or so of the backup process. It is just mentioned here for completeness.

<sub>_This page is licensed: CC BY-SA / Gnu FDL_</sub>

{% @marketo/form formId="4316" %}
