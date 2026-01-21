---
description: >-
  View the status variables used to monitor replication health. Learn how to
  interpret metrics regarding log positions, connection status, and event
  counts.
---

# Replication and Binary Log Status Variables

{% hint style="info" %}
The terms _master_ and _slave_ have historically been used in replication, and MariaDB has begun the process of adding _primary_ and _replica_ synonyms. The old terms will continue to be used to maintain backward compatibility - see [MDEV-18777](https://jira.mariadb.org/browse/MDEV-18777) to follow progress on this effort.
{% endhint %}

The following status variables are useful in [binary logging](../../server-management/server-monitoring-logs/binary-log/) and [replication](./). See [Server Status Variables](../optimization-and-tuning/system-variables/server-status-variables.md) for a complete list of status variables that can be viewed with [SHOW STATUS](../../reference/sql-statements/administrative-sql-statements/show/show-status.md).

See also the [Full list of MariaDB options, system and status variables](../../reference/full-list-of-mariadb-options-system-and-status-variables.md).

#### `Binlog_bytes_written`

* Description: The number of bytes written to the [binary log](../../server-management/server-monitoring-logs/binary-log/).
* Scope: Global
* Data Type: `numeric`

#### `Binlog_cache_disk_use`

* Description: Number of transactions which used a temporary disk cache because they could not fit in the regular [binary log](../../server-management/server-monitoring-logs/binary-log/) cache, being larger than [binlog\_cache\_size](../optimization-and-tuning/system-variables/server-system-variables.md#binlog_cache_size). The global value can be flushed by [FLUSH STATUS](../../reference/sql-statements/administrative-sql-statements/flush-commands/flush.md).
* Scope: Global
* Data Type: `numeric`

#### `Binlog_cache_use`

* Description: Number of transaction which used the regular [binary log](../../server-management/server-monitoring-logs/binary-log/) cache, being smaller than [binlog\_cache\_size](../optimization-and-tuning/system-variables/server-system-variables.md#binlog_cache_size). The global value can be flushed by [FLUSH STATUS](../../reference/sql-statements/administrative-sql-statements/flush-commands/flush.md).
* Scope: Global
* Data Type: `numeric`

#### `Binlog_commits`

* Description: Total number of transactions committed to the binary log.
* Scope: Global
* Data Type: `numeric`

#### `Binlog_disk_use`

* Description: If [max-binlog-total\_size](replication-and-binary-log-system-variables.md#max_binlog_total_size) is not set to zero, shows the space usage of the binary log in bytes.
* Scope: Global
* Data Type: `numeric`
* Introduced: [MariaDB 11.4](https://app.gitbook.com/s/aEnK0ZXmUbJzqQrTjFyb/community-server/mariadb-11-4-series/what-is-mariadb-114)

#### `Binlog_group_commit_trigger_count`

* Description: Total number of group commits triggered because of the number of binary log commits in the group reached the limit set by the variable [binlog\_commit\_wait\_count](replication-and-binary-log-system-variables.md). See [Group commit for the binary log](../../server-management/server-monitoring-logs/binary-log/group-commit-for-the-binary-log.md).
* Scope: Global
* Data Type: `numeric`

#### `Binlog_group_commit_trigger_lock_wait`

* Description: Total number of group commits triggered because a binary log commit was being delayed because of a lock wait where the lock was held by a prior binary log commit. When this happens the later binary log commit is placed in the next group commit. See [Group commit for the binary log](../../server-management/server-monitoring-logs/binary-log/group-commit-for-the-binary-log.md).
* Scope: Global
* Data Type: `numeric`

#### `Binlog_group_commit_trigger_timeout`

* Description: Total number of group commits triggered because of the time since the first binary log commit reached the limit set by the variable [binlog\_commit\_wait\_usec](replication-and-binary-log-system-variables.md). See [Group commit for the binary log](../../server-management/server-monitoring-logs/binary-log/group-commit-for-the-binary-log.md).
* Scope: Global
* Data Type: `numeric`

#### `Binlog_group_commits`

* Description: Total number of group commits done to the binary log. See [Group commit for the binary log](../../server-management/server-monitoring-logs/binary-log/group-commit-for-the-binary-log.md).
* Scope: Global
* Data Type: `numeric`

#### `Binlog_gtid_index_hit`

* Description: Incremented for each successful lookup in a [GTID index](gtid.md#binlog-indexing).
* Scope: Global
* Data Type: `numeric`
* Introduced: [MariaDB 11.4](https://app.gitbook.com/s/aEnK0ZXmUbJzqQrTjFyb/community-server/mariadb-11-4-series/what-is-mariadb-114)

#### `Binlog_gtid_index_miss`

* Description: Incremented when a [GTID index](gtid.md#binlog-indexing) lookup is not possible, which indicates that the index file is missing (eg. binlog written by old server version without GTID index support), or corrupt.
* Scope: Global
* Data Type: `numeric`
* Introduced: [MariaDB 11.4](https://app.gitbook.com/s/aEnK0ZXmUbJzqQrTjFyb/community-server/mariadb-11-4-series/what-is-mariadb-114)

#### `Binlog_snapshot_file`

* Description: The binary log file. Unlike [SHOW MASTER STATUS](../../reference/sql-statements/administrative-sql-statements/show/show-binlog-status.md), can be queried in a transactionally consistent way, irrespective of which other transactions have been committed since the snapshot was taken. See [Enhancements for START TRANSACTION WITH CONSISTENT SNAPSHOT](enhancements-for-start-transaction-with-consistent-snapshot.md).
* Scope: Global
* Data Type: `string`

#### `Binlog_snapshot_position`

* Description: The binary log position. Unlike [SHOW MASTER STATUS](../../reference/sql-statements/administrative-sql-statements/show/show-binlog-status.md), can be queried in a transactionally consistent way, irrespective of which other transactions have been committed since the snapshot was taken. See [Enhancements for START TRANSACTION WITH CONSISTENT SNAPSHOT](enhancements-for-start-transaction-with-consistent-snapshot.md).
* Scope: Global
* Data Type: `numeric`

#### `Binlog_stmt_cache_disk_use`

* Description: Number of non-transaction statements which used a temporary disk cache because they could not fit in the regular [binary log](../../server-management/server-monitoring-logs/binary-log/) cache, being larger than [binlog\_stmt\_cache\_size](../optimization-and-tuning/system-variables/server-system-variables.md#binlog_stmt_cache_size). The global value can be flushed by [FLUSH STATUS](../../reference/sql-statements/administrative-sql-statements/flush-commands/flush.md).
* Scope: Global
* Data Type: `numeric`

#### `Binlog_stmt_cache_use`

* Description: Number of non-transaction statement which used the regular [binary log](../../server-management/server-monitoring-logs/binary-log/) cache, being smaller than [binlog\_stmt\_cache\_size](../optimization-and-tuning/system-variables/server-system-variables.md#binlog_stmt_cache_size). The global value can be flushed by [FLUSH STATUS](../../../reference/sql-statements-and-structure/sql-statements/administrative-sql-statements/flush-commands/flush.md).
* Scope: Global
* Data Type: `numeric`

#### `Com_change_master`

* Description: Number of [CHANGE MASTER TO](../../reference/sql-statements/administrative-sql-statements/replication-statements/change-master-to.md) statements executed.
* Scope: Global, Session
* Data Type: `numeric`

#### `Com_show_binlog_status`

* Description:
* Scope: Global, Session
* Data Type: `numeric`
* Introduced: [MariaDB 10.5.2](https://app.gitbook.com/s/aEnK0ZXmUbJzqQrTjFyb/community-server/old-releases/mariadb-10-5-series/mariadb-1052-release-notes)

#### `Com_show_master_status`

* Description: Number of [SHOW MASTER STATUS](../../reference/sql-statements/administrative-sql-statements/show/show-binlog-status.md) commands executed.
* Scope: Global, Session
* Data Type: `numeric`
* Removed: [MariaDB 10.5.2](https://app.gitbook.com/s/aEnK0ZXmUbJzqQrTjFyb/community-server/old-releases/mariadb-10-5-series/mariadb-1052-release-notes)

#### `Com_show_new_master`

* Description:
* Scope: Global, Session
* Data Type: `numeric`
* Removed: [MariaDB 5.5](https://app.gitbook.com/s/aEnK0ZXmUbJzqQrTjFyb/community-server/old-releases/release-notes-mariadb-5-5-series/changes-improvements-in-mariadb-5-5)

#### `Com_show_slave_hosts`

* Description: Number of [SHOW SLAVE HOSTS](../../reference/sql-statements/administrative-sql-statements/show/show-replica-hosts.md) commands executed.
* Scope: Global, Session
* Data Type: `numeric`

#### `Com_show_slave_status`

* Description: Number of [SHOW SLAVE STATUS](../../reference/sql-statements/administrative-sql-statements/show/show-replica-status.md) commands executed.
* Scope: Global, Session
* Data Type: `numeric`

#### `Com_slave_start`

* Description: Number of [START SLAVE](../../reference/sql-statements/administrative-sql-statements/replication-statements/start-replica.md) commands executed. Removed in [MariaDB 10.0](https://app.gitbook.com/s/aEnK0ZXmUbJzqQrTjFyb/community-server/old-releases/release-notes-mariadb-10-0-series/changes-improvements-in-mariadb-10-0), see [Com\_start\_slave](replication-and-binary-log-status-variables.md#com_start_slave).
* Scope: Global, Session
* Data Type: `numeric`
* Removed: [MariaDB 10.0](https://app.gitbook.com/s/aEnK0ZXmUbJzqQrTjFyb/community-server/old-releases/release-notes-mariadb-10-0-series/changes-improvements-in-mariadb-10-0)

#### `Com_slave_stop`

* Description: Number of [STOP SLAVE](../../reference/sql-statements/administrative-sql-statements/replication-statements/stop-replica.md) commands executed. Removed in [MariaDB 10.0](https://app.gitbook.com/s/aEnK0ZXmUbJzqQrTjFyb/community-server/old-releases/release-notes-mariadb-10-0-series/changes-improvements-in-mariadb-10-0), see [Com\_stop\_slave](replication-and-binary-log-status-variables.md#com_stop_slave).
* Scope: Global, Session
* Data Type: `numeric`
* Removed: [MariaDB 10.0](https://app.gitbook.com/s/aEnK0ZXmUbJzqQrTjFyb/community-server/old-releases/release-notes-mariadb-10-0-series/changes-improvements-in-mariadb-10-0)

#### `Com_start_all_slaves`

* Description: Number of [START ALL SLAVES](../../reference/sql-statements/administrative-sql-statements/replication-statements/start-replica.md) commands executed.
* Scope: Global, Session
* Data Type: `numeric`

#### `Com_start_slave`

* Description: Number of [START SLAVE](../../reference/sql-statements/administrative-sql-statements/replication-statements/start-replica.md) commands executed. Replaces the old [Com\_slave\_start](replication-and-binary-log-status-variables.md#com_slave_start).
* Scope: Global, Session
* Data Type: `numeric`

#### `Com_stop_all_slaves`

* Description: Number of [STOP ALL SLAVES](../../reference/sql-statements/administrative-sql-statements/replication-statements/stop-replica.md) commands executed.
* Scope: Global, Session
* Data Type: `numeric`

#### `Com_stop_slave`

* Description: Number of [STOP SLAVE](../../reference/sql-statements/administrative-sql-statements/replication-statements/stop-replica.md) commands executed. Replaces the old [Com\_slave\_stop](replication-and-binary-log-status-variables.md#com_slave_stop).
* Scope: Global, Session
* Data Type: `numeric`

#### `Master_gtid_wait_count`

* Description: Number of times MASTER\_GTID\_WAIT called.
* Scope: Global, Session
* Data Type: `numeric`

#### `Master_gtid_wait_time`

* Description: Total number of time spent in MASTER\_GTID\_WAIT.
* Scope: Global, Session
* Data Type: `numeric`

#### `Master_gtid_wait_timeouts`

* Description: Number of timeouts occurring in MASTER\_GTID\_WAIT.
* Scope: Global, Session
* Data Type: `numeric`

#### `Rpl_status`

* Description: For showing the status of fail-safe replication. Removed in MySQL 5.6, still present in [MariaDB 10.0](https://app.gitbook.com/s/aEnK0ZXmUbJzqQrTjFyb/community-server/old-releases/release-notes-mariadb-10-0-series/changes-improvements-in-mariadb-10-0).

#### `Rpl_transactions_multi_engine`

* Description: Number of replicated transactions that involved changes in multiple (transactional) storage engines, before considering the update of `mysql.gtid_slave_pos`. These are transactions that were already cross-engine, independent of the GTID position update introduced by replication. The global value can be flushed by [FLUSH STATUS](../../reference/sql-statements/administrative-sql-statements/flush-commands/flush.md).
* Scope: Global
* Data Type: `numeric`

#### `Slave_connections`

* Description: Number of REGISTER\_SLAVE attempts. In practice the number of times slaves has tried to connect to the master.
* Scope: Global
* Data Type: `numeric`

#### `Slave_heartbeat_period`

* Description: Time in seconds that a heartbeat packet is requested from the master by a slave.
* Scope: Global
* Data Type: `numeric`

#### `Slave_open_temp_tables`

* Description: Number of temporary tables the slave has open.
* Scope: Global
* Data Type: `numeric`

#### `Slave_received_heartbeats`

* Description: Number of heartbeats the slave has received from the master.
* Scope: Global
* Data Type: `numeric`

#### `Slave_retried_transactions`

* Description: Number of times the slave has retried transactions since the server started. The global value can be flushed by [FLUSH STATUS](../../reference/sql-statements/administrative-sql-statements/flush-commands/flush.md).
* Scope: Global
* Data Type: `numeric`

#### `Slave_running`

* Description: Whether the [default connection](replication-and-binary-log-system-variables.md#default_master_connection) slave is running (both I/O and SQL threads are running) or not.
* Scope: Global
* Data Type: `numeric`

#### `Slave_skipped_errors`

* Description: The number of times a slave has skipped errors defined by [slave-skip-errors](replication-and-binary-log-system-variables.md).
* Scope: Global
* Data Type: `numeric`

#### `Slaves_connected`

* Description: Number of slaves connected.
* Scope: Global
* Data Type: `numeric`

#### `Slaves_running`

* Description: Number of slave SQL threads running.
* Scope: Global
* Data Type: `numeric`

#### `Transactions_gtid_foreign_engine`

* Description: Number of replicated transactions where the update of the `gtid_slave_pos` table had to choose a storage engine that did not otherwise participate in the transaction. This can indicate that setting [gtid\_pos\_auto\_engines](gtid.md) might be useful. The global value can be flushed by [FLUSH STATUS](../../reference/sql-statements/administrative-sql-statements/flush-commands/flush.md).
* Scope: Global
* Data Type: `numeric`

#### `Transactions_multi_engine`

* Description: Number of transactions that changed data in multiple (transactional) storage engines. If this is significantly larger than [Rpl\_transactions\_multi\_engine](replication-and-binary-log-status-variables.md#rpl_transactions_multi_engine), it indicates that setting [gtid\_pos\_auto\_engines](https://mariadb.com/kb/en/gtid_pos_auto_engines) could reduce the need for cross-engine transactions. The global value can be flushed by [FLUSH STATUS](../../reference/sql-statements/administrative-sql-statements/flush-commands/flush.md).
* Scope: Global
* Data Type: `numeric`

<sub>_This page is licensed: CC BY-SA / Gnu FDL_</sub>

{% @marketo/form formId="4316" %}
