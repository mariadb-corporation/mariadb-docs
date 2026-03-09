---
description: >-
  Gain insight into the background threads that drive replication. Understand
  the roles of the I/O thread, SQL thread, and binlog dump thread in moving data
  between servers.
---

# Replication Threads

{% hint style="info" %}
The terms _master_ and _slave_ have historically been used in replication, and MariaDB has begun the process of adding _primary_ and _replica_ synonyms. The old terms will continue to be used to maintain backward compatibility - see [MDEV-18777](https://jira.mariadb.org/browse/MDEV-18777) to follow progress on this effort.
{% endhint %}

MariaDB's [replication](./) implementation requires several types of threads.

## Threads on the Primary

The primary usually only has one type of replication-related thread: the binary log dump thread.

If [semisynchronous replication](semisynchronous-replication.md) is enabled, then the primary also has an ACK receiver thread.

### Binary Log Dump Thread

The binary log dump thread runs on the primary and dumps the [binary log](../../server-management/server-monitoring-logs/binary-log/) to the replica. This thread can be identified by running the [SHOW PROCESSLIST](../../reference/sql-statements/administrative-sql-statements/show/show-processlist.md) statement and finding the thread where the [thread command](../optimization-and-tuning/buffers-caches-and-threads/thread-command-values.md) is `"Binlog Dump"`.

The primary creates a separate binary log dump thread for each replica connected to the primary. You can identify which replicas are connected to the primary by executing the [SHOW SLAVE HOSTS](../../reference/sql-statements/administrative-sql-statements/show/show-replica-hosts.md) statement.

#### Binary Log Dump Threads and the Shutdown Process

When a primary server is shut down and it goes through the normal shutdown process, the primary kills client threads in random order. By default, the primary also considers its binary log dump threads to be regular client threads. As a consequence, the binary log dump threads can be killed while client threads still exist, and this means that data can be written on the primary during a normal shutdown that won't be replicated. This is true even if [semi-synchronous replication](semisynchronous-replication.md) is being used. Data is not lost; it is stored in the primary server's binary log. The replicas on reconnection, after the primary server restarts, will resume at the exact position they were killed off during the primary shutdown. No data is lost.

In [MariaDB 10.4](https://app.gitbook.com/s/aEnK0ZXmUbJzqQrTjFyb/community-server/old-releases/10.4/what-is-mariadb-104) and later, this problem can be solved by shutting down the server using either the [mariadb-admin](../../clients-and-utilities/administrative-tools/mariadb-admin.md) utility or the [SHUTDOWN](../../reference/sql-statements/administrative-sql-statements/shutdown.md) command and providing a special option.

For example, this problem can be solved by shutting down the server with the [mariadb-admin](../../clients-and-utilities/administrative-tools/mariadb-admin.md) utility and by providing the `--wait-for-all-slaves` option to the utility and by executing the `shutdown` command with the utility:

```
mariadb-admin --wait-for-all-slaves shutdown
```

Or this problem can be solved by shutting down the server with the [SHUTDOWN](../../reference/sql-statements/administrative-sql-statements/shutdown.md) command and by providing the `WAIT FOR ALL SLAVES` option to the command:

```sql
SHUTDOWN WAIT FOR ALL SLAVES;
```

When one of these special options is provided, the server only kills its binary log dump threads after all client threads have been killed, and it only completes the shutdown after the last [binary log](../../server-management/server-monitoring-logs/binary-log/) has been sent to all connected replicas.

In [MariaDB 10.4](https://app.gitbook.com/s/aEnK0ZXmUbJzqQrTjFyb/community-server/old-releases/10.4/what-is-mariadb-104) and later, it is still not possible to enable this behavior by default. This means that this behavior is currently inaccessible when shutting down the server using tools like [systemd](../../server-management/starting-and-stopping-mariadb/systemd.md) or [sysVinit](../../server-management/starting-and-stopping-mariadb/sysvinit.md).

In [MariaDB 10.3](https://app.gitbook.com/s/aEnK0ZXmUbJzqQrTjFyb/community-server/old-releases/10.3/what-is-mariadb-103) and before, it is recommended to manually switchover replicas to a new primary before shutting down the old primary.

### ACK Receiver Thread

When [semisynchronous replication](semisynchronous-replication.md) is enabled, semisynchronous replicas send acknowledgements (ACKs) to their primary to confirm that they have received some transaction. The primary creates an ACK receiver thread to receive these ACKs.

## Threads on the Replica

The replica has three types of replication-related threads: the replica I/O thread, the replica SQL thread, and worker threads, which are only applicable when [parallel replication](parallel-replication.md) is in use.

When [multi-source replication](multi-source-replication.md) is in use, each independent replication connection has its own replica threads of each type.

### Replica I/O Thread

The replica's I/O thread receives the [binary log](../../server-management/server-monitoring-logs/binary-log/) events from the primary and writes them to its [relay log](../../server-management/server-monitoring-logs/binary-log/relay-log.md).

#### Binary Log Position

The [binary log](../../server-management/server-monitoring-logs/binary-log/) position of the replica's I/O thread can be checked by executing the [SHOW SLAVE STATUS](../../reference/sql-statements/administrative-sql-statements/show/show-replica-status.md) statement. It will be shown as the `Master_Log_File` and `Read_Master_Log_Pos` columns.

The [binary log](../../server-management/server-monitoring-logs/binary-log/) position of the replica's I/O thread can be set by setting the [MASTER\_LOG\_FILE](../../reference/sql-statements/administrative-sql-statements/replication-statements/change-master-to.md#master_log_file) and [MASTER\_LOG\_POS](../../reference/sql-statements/administrative-sql-statements/replication-statements/change-master-to.md#master_log_pos) options with the [CHANGE MASTER](../../reference/sql-statements/administrative-sql-statements/replication-statements/change-master-to.md) statement.

The [binary log](../../server-management/server-monitoring-logs/binary-log/) position of the replica's I/O thread and the values of most other [CHANGE MASTER](../../reference/sql-statements/administrative-sql-statements/replication-statements/change-master-to.md) options are written to either the default `master.info` file or the file that is configured by the [master\_info\_file](../../server-management/starting-and-stopping-mariadb/mariadbd-options.md) option. The replica's I/O thread keeps this [binary log](../../server-management/server-monitoring-logs/binary-log/) position updated as it downloads events only when the [MASTER\_USE\_GTID](replication-threads.md#master_use_gtid) option is set to `NO`. Otherwise the file is not updated on a per event basis. See [CHANGE MASTER TO: Option Persistence](../../reference/sql-statements/administrative-sql-statements/replication-statements/change-master-to.md#option-persistence) for more information.

### Replica SQL Thread

The replica's SQL thread reads events from the [relay log](../../server-management/server-monitoring-logs/binary-log/relay-log.md). What it does with them depends on whether [parallel replication](parallel-replication.md) is in use. If [parallel replication](parallel-replication.md) is not in use, then the SQL thread applies the events to its local copy of the data. If [parallel replication](parallel-replication.md) is in use, then the SQL thread hands off the events to its worker threads to apply in parallel.

#### Relay Log Position

The [relay log](../../server-management/server-monitoring-logs/binary-log/relay-log.md) position of the replica's SQL thread can be checked by executing the [SHOW SLAVE STATUS](../../reference/sql-statements/administrative-sql-statements/show/show-replica-status.md) statement. It will be shown as the `Relay_Log_File` and `Relay_Log_Pos` columns.

The [relay log](../../server-management/server-monitoring-logs/binary-log/relay-log.md) position of the replica's SQL thread can be set by setting the [RELAY\_LOG\_FILE](../../reference/sql-statements/administrative-sql-statements/replication-statements/change-master-to.md#relay_log_file) and [RELAY\_LOG\_POS](../../reference/sql-statements/administrative-sql-statements/replication-statements/change-master-to.md#relay_log_pos) options with the [CHANGE MASTER](../../reference/sql-statements/administrative-sql-statements/replication-statements/change-master-to.md) statement.

The [relay log](../../server-management/server-monitoring-logs/binary-log/relay-log.md) position of the replica's SQL thread is written to either the default `relay-log.info` file or the file that is configured by the [relay\_log\_info\_file](replication-and-binary-log-system-variables.md#relay_log_info_file) system variable. The replica's SQL thread keeps this [relay log](../../server-management/server-monitoring-logs/binary-log/relay-log.md) position updated as it applies events. See [CHANGE MASTER TO: Option Persistence](../../reference/sql-statements/administrative-sql-statements/replication-statements/change-master-to.md#option-persistence) for more information.

#### Binary Log Position

The corresponding [binary log](../../server-management/server-monitoring-logs/binary-log/) position of the current [relay log](../../server-management/server-monitoring-logs/binary-log/relay-log.md) position of the replica's SQL thread can be checked by executing the [SHOW SLAVE STATUS](../../reference/sql-statements/administrative-sql-statements/show/show-replica-status.md) statement. It will be shown as the `Relay_Master_Log_File` and `Exec_Master_Log_Pos` columns.

#### GTID Position

If the replica is replicating [binary log](../../server-management/server-monitoring-logs/binary-log/) events that contain [GTIDs](gtid.md), then the [replica's's SQL thread](replication-threads.md#replica-sql-thread) will write every GTID that it applies to the [mysql.gtid\_slave\_pos](../../reference/system-tables/the-mysql-database-tables/mysqlgtid_slave_pos-table.md) table. This GTID can be inspected and modified through the [gtid\_slave\_pos](gtid.md#gtid_slave_pos) system variable.

If the replica has the [log\_slave\_updates](replication-and-binary-log-system-variables.md#log_slave_updates) system variable enabled and if the replica has the [binary log](../../server-management/server-monitoring-logs/binary-log/) enabled, then every write by the [replica's SQL thread](replication-threads.md#replica-sql-thread) will also go into the replica's [binary log](../../server-management/server-monitoring-logs/binary-log/). This means that [GTIDs](gtid.md) of replicated transactions would be reflected in the value of the [gtid\_binlog\_pos](gtid.md#gtid_binlog_pos) system variable.

See [CHANGE MASTER TO: GTID Persistence](../../reference/sql-statements/administrative-sql-statements/replication-statements/change-master-to.md#gtid-persistence) for more information.

### Worker Threads

When [parallel replication](parallel-replication.md) is in use, then the SQL thread hands off the events to its worker threads to apply in parallel.

<sub>_This page is licensed: CC BY-SA / Gnu FDL_</sub>

{% @marketo/form formId="4316" %}
