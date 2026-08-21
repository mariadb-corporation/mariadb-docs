---
description: >-
  Enhance data consistency with semisynchronous replication. Ensure that the
  primary waits for at least one replica to acknowledge receipt of a transaction
  before committing.
---

# Semisynchronous Replication

## Description

[Standard MariaDB replication](./) is asynchronous, but MariaDB also provides a semisynchronous replication option. The feature is built into the server and is always available; nothing needs to be installed to use it.

With regular asynchronous replication, replicas request events from the primary's binary log whenever the replicas are ready. The primary does not wait for a replica to confirm that an event has been received.

With fully synchronous replication, all replicas are required to respond that they have received the events. See [Galera Cluster](https://app.gitbook.com/o/diTpXxF5WsbHqTReoBsS/s/3VYeeVGUV4AMqrA3zwy7/).

Semisynchronous replication waits for just one replica to acknowledge that it has received and logged the events.

Semisynchronous replication therefore comes with some negative performance impact, but increased data integrity. Since the delay is based on the roundtrip time to the replica and back, this delay is minimized for servers in close proximity over fast networks.

The guarantee is about the replica's [relay log](../../server-management/server-monitoring-logs/binary-log/relay-log.md), not about the replica's data: an acknowledged transaction has been written to a replica's relay log, but it has not necessarily been applied there yet. How durable that relay log entry is depends on the replica's configuration, so read [Relay Log Durability](semisynchronous-replication.md#relay-log-durability) before relying on semisynchronous replication to prevent data loss.

## Enabling Semisynchronous Replication

Semisynchronous replication can be enabled by setting the relevant system variables on the primary and the replica.

If a server needs to be able to switch between acting as a primary and a replica, then you can enable both the primary and replica system variables on the server. For example, you might need to do this if [MariaDB MaxScale](https://app.gitbook.com/o/diTpXxF5WsbHqTReoBsS/s/0pSbu5DcMSW4KwAkUcmX/) is being used to enable auto-failover or switchover with MariaDB Monitor.

### Enabling Semisynchronous Replication on the Primary

Semisynchronous replication can be enabled on the primary by setting the [rpl\_semi\_sync\_master\_enabled](semisynchronous-replication.md#rpl_semi_sync_master_enabled) system variable to `ON`. It can be set dynamically with [SET GLOBAL](../../reference/sql-statements/administrative-sql-statements/set-commands/set.md#global-session). For example:

```sql
SET GLOBAL rpl_semi_sync_master_enabled=ON;
```

It can also be set in a server [option group](../../server-management/install-and-upgrade-mariadb/configuring-mariadb/configuring-mariadb-with-option-files.md#option-groups) in an [option file](../../server-management/install-and-upgrade-mariadb/configuring-mariadb/configuring-mariadb-with-option-files.md) prior to starting up the server. For example:

```
[mariadb]
...
rpl_semi_sync_master_enabled=ON
```

### Enabling Semisynchronous Replication on the Replica

Semisynchronous replication can be enabled on the replica by setting the [rpl\_semi\_sync\_slave\_enabled](semisynchronous-replication.md#rpl_semi_sync_slave_enabled) system variable to `ON`. It can be set dynamically with [SET GLOBAL](../../reference/sql-statements/administrative-sql-statements/set-commands/set.md#global-session). For example:

```sql
SET GLOBAL rpl_semi_sync_slave_enabled=ON;
```

It can also be set in a server [option group](../../server-management/install-and-upgrade-mariadb/configuring-mariadb/configuring-mariadb-with-option-files.md#option-groups) in an [option file](../../server-management/install-and-upgrade-mariadb/configuring-mariadb/configuring-mariadb-with-option-files.md) prior to starting up the server. For example:

```
[mariadb]
...
rpl_semi_sync_slave_enabled=ON
```

When switching between semisynchronous replication and asynchronous replication on a replica with [replica IO threads](replication-threads.md#threads-on-the-replica) already running, the replica I/O thread will need to be restarted. For example:

```sql
STOP SLAVE IO_THREAD;
START SLAVE IO_THREAD;
```

If this is not done, then the replica IO thread will continue to use the previous setting.

## Configuring the Primary Timeout

In semisynchronous replication, the replica acknowledges receipt of a transaction's events only after it has written them to its relay log. Whether they have also been synced to disk at that point depends on [sync\_relay\_log](replication-and-binary-log-system-variables.md#sync_relay_log). If the replica does not acknowledge the transaction before a certain amount of time has passed, then a timeout occurs and the primary switches to asynchronous replication. This will be reflected in the primary's [error log](../../server-management/server-monitoring-logs/error-log.md) with messages like the following:

```
[Warning] Timeout waiting for reply of binlog (file: mariadb-1-bin.000002, pos: 538), semi-sync up to file , position 0.
[Note] Semi-sync replication switched OFF.
```

When this occurs, the [Rpl\_semi\_sync\_master\_status](../optimization-and-tuning/system-variables/semisynchronous-replication-plugin-status-variables.md#rpl_semi_sync_master_status) status variable will be switched to `OFF`.

When at least one semisynchronous replica catches up, semisynchronous replication is resumed. This will be reflected in the primary's [error log](../../server-management/server-monitoring-logs/error-log.md) with messages like the following:

```
[Note] Semi-sync replication switched ON with replica (server_id: 184137206) at (mariadb-1-bin.000002, 215076)
```

When this occurs, the [Rpl\_semi\_sync\_master\_status](../optimization-and-tuning/system-variables/semisynchronous-replication-plugin-status-variables.md#rpl_semi_sync_master_status) status variable will be switched to `ON`.

The number of times that semisynchronous replication has been switched off can be checked by looking at the value of the [Rpl\_semi\_sync\_master\_no\_times](../optimization-and-tuning/system-variables/semisynchronous-replication-plugin-status-variables.md#rpl_semi_sync_master_no_times) status variable.

If you see a lot of timeouts like this in your environment, then you may want to change the timeout period. The timeout period can be changed by setting the [rpl\_semi\_sync\_master\_timeout](semisynchronous-replication.md#rpl_semi_sync_master_timeout) system variable. It can be set dynamically with [SET GLOBAL](../../reference/sql-statements/administrative-sql-statements/set-commands/set.md#global-session). For example:

```sql
SET GLOBAL rpl_semi_sync_master_timeout=20000;
```

It can also be set in a server [option group](../../server-management/install-and-upgrade-mariadb/configuring-mariadb/configuring-mariadb-with-option-files.md#option-groups) in an [option file](../../server-management/install-and-upgrade-mariadb/configuring-mariadb/configuring-mariadb-with-option-files.md) prior to starting up the server. For example:

```
[mariadb]
...
rpl_semi_sync_master_timeout=20000
```

To determine a good value for the [rpl\_semi\_sync\_master\_timeout](semisynchronous-replication.md#rpl_semi_sync_master_timeout) system variable, you may want to look at the values of the [Rpl\_semi\_sync\_master\_net\_avg\_wait\_time](../optimization-and-tuning/system-variables/semisynchronous-replication-plugin-status-variables.md#rpl_semi_sync_master_net_avg_wait_time) and [Rpl\_semi\_sync\_master\_tx\_avg\_wait\_time](../optimization-and-tuning/system-variables/semisynchronous-replication-plugin-status-variables.md#rpl_semi_sync_master_tx_avg_wait_time) status variables.

## Configuring the Primary Wait Point

In semisynchronous replication, there are two potential points at which the primary can wait for the replica acknowledge the receipt of a transaction's events. These two wait points have different advantages and disadvantages.

The wait point is configured by the [rpl\_semi\_sync\_master\_wait\_point](semisynchronous-replication.md#rpl_semi_sync_master_wait_point) system variable. The supported values are:

* `AFTER_SYNC`
* `AFTER_COMMIT`&#x20;

> When using the [InnoDB-based Binary Log](innodb-based-binary-log.md) (`--binary-storage-engine=innodb`), the `AFTER_SYNC` wait point is not supported. Only `AFTER_COMMIT` is available, since the traditional two-phase commit between the binary log and the InnoDB storage engine is no longer used.

It can be set dynamically with [SET GLOBAL](../../reference/sql-statements/administrative-sql-statements/set-commands/set.md#global-session). For example:

```sql
SET GLOBAL rpl_semi_sync_master_wait_point='AFTER_SYNC';
```

It can also be set in a server [option group](../../server-management/install-and-upgrade-mariadb/configuring-mariadb/configuring-mariadb-with-option-files.md#option-groups) in an [option file](../../server-management/install-and-upgrade-mariadb/configuring-mariadb/configuring-mariadb-with-option-files.md) prior to starting up the server. For example:

```
[mariadb]
...
rpl_semi_sync_master_wait_point=AFTER_SYNC
```

When this variable is set to `AFTER_SYNC`, the primary performs the following steps:

> The `AFTER_SYNC` wait point is only supported with the traditional binlog implementation and is not available when the
> \
> InnoDB-based Binary Log is enabled.

1. Prepares the transaction in the storage engine.
2. Syncs the transaction to the [binary log](../../server-management/server-monitoring-logs/binary-log/).
3. Waits for acknowledgement from the replica.
4. Commits the transaction to the storage engine.
5. Returns an acknowledgement to the client.

The effects of the `AFTER_SYNC` wait point are:

* All clients see the same data on the primary at the same time; after acknowledgement by the replica and after being committed to the storage engine on the primary.
* If the primary crashes, then failover should be lossless, because all transactions committed on the primary would have been replicated to the replica.
* However, if the primary crashes, then its [binary log](../../server-management/server-monitoring-logs/binary-log/) may also contain events for transactions that were prepared by the storage engine and written to the binary log, but that were never actually committed by the storage engine. As part of the server's [automatic crash recovery](../../server-management/server-monitoring-logs/transaction-coordinator-log/heuristic-recovery-with-the-transaction-coordinator-log.md) process, the server may recover these prepared transactions when the server is restarted. This could cause the "old" crashed primary to become inconsistent with its former replicas when they have
  been reconfigured to replace the old primary with a new one.
  The old primary in such a scenario can be re-introduced only as a [semisync replica](semisynchronous-replication.md#rpl_semi_sync_slave_enabled).
  To recover it safely, start the server with `--init-rpl-role=SLAVE`. This tells the server its
  role in the replication topology, so that post-crash recovery discards transactions proven not
  to be committed and the server will not have extra transactions ([MDEV-21117](https://jira.mariadb.org/browse/MDEV-21117),
  [MDEV-33465](https://jira.mariadb.org/browse/MDEV-33465)). Before MDEV-33465, this recovery was
  instead deduced from the semisync variables (`rpl_semi_sync_slave_enabled = ON`), which did not
  work reliably in mixed topologies; setting `--init-rpl-role=SLAVE` is now required.
  The server's binlog gets truncated to discard transactions proven
  not to be committed, in any of their branches if they are multi-engine.
  Truncation does not occur though when there exists a non-transactional group of events beyond the truncation position in which case recovery reports an error.
  When the semisync replica recovery can't be carried out, the crashed primary may need to be rebuilt.

When this variable is set to `AFTER_COMMIT`, the primary performs the following steps:

1. Prepares the transaction in the storage engine.
2. Syncs the transaction to the [binary log](../../server-management/server-monitoring-logs/binary-log/).
3. Commits the transaction to the storage engine.
4. Waits for acknowledgement from the replica.
5. Returns an acknowledgement to the client.

The effects of the `AFTER_COMMIT` wait point are:

* Other clients may see the committed transaction before the committing client.
* If the primary crashes, then failover may involve some data loss, because the primary may have committed transactions that had not yet been acknowledged by the replicas.

### Failover Implications

System administrators implementing a semi-synchronous replication
fail-over strategy must understand the distinction between the
`AFTER_SYNC` and `AFTER_COMMIT` wait points. This choice has
irreversible implications for the server recovery process: if a
pre-crash semi-sync master is brought back online as a post-crash
semi-sync slave, the recovery process will truncate any transactions
from the binary log that were not committed in the storage engine.

Conceptually, the two configurations differ in which server may be
logically ahead of the other:

* `AFTER_SYNC`: The slave may be ahead of the master.
* `AFTER_COMMIT`: The master will always be ahead of the slave.

In either configuration, data loss is possible if the logically behind
server is promoted to master after a crash.


#### Recommended Fail-Over Strategy

To prevent data loss, the fail-over strategy should align with the
configured wait point:

* `AFTER_COMMIT` configurations: Always wait for a failed master to be
  brought back online to resume its role as master.

* `AFTER_SYNC` configurations: Demote the failed master to a slave of a
  newly-promoted master.


####  Recovery Procedure for Guaranteed Consistency

If neither of the above strategies is feasible, the following procedure
ensures data consistency after a crash:

1. Configure all servers in the topology with `SET GLOBAL read_only=1`.
   This prevents the failed master from accidentally resuming its master
role
2. After the master fails, select any node (hereafter node A) as the new
master candidate. Choosing the most up-to-date node will minimize the
time required to complete this process
3. On another node (hereafter node B), run `SELECT @@gtid_current_pos`.
4. Configure node A as a slave of node B using `CHANGE MASTER TO` (if
   this replication channel does not already exist).
5. On node A, run `START SLAVE UNTIL` with the GTID value retrieved in
step 3
6. Repeat steps 3–5 for each remaining node in the topology, using node
A as the slave in each iteration.
7. Once all nodes have been processed, node A is guaranteed to be the
furthest-progressed node in the topology and is safe to promote as the
new master.
8. On node A, run `SET GLOBAL read_only=0`.
9. Configure all other nodes as slaves of node A using
   `CHANGE MASTER TO` followed by `START SLAVE`.


## Relay Log Durability

The guarantee semisynchronous replication provides is that a committed transaction has reached at least one replica's [relay log](../../server-management/server-monitoring-logs/binary-log/relay-log.md) before the commit is acknowledged to the client. That guarantee is only as strong as that relay log entry: it holds if the entry survives a crash and a restart of the replica.

Two settings on the replica determine that, and one case cannot be covered by any replica-side setting.

### Syncing the Relay Log

A replica acknowledges a transaction as soon as the transaction's events have been written to its relay log file. Writing is not the same as syncing. By default, the relay log is only synced to disk after every 10,000 events, as set by [sync\_relay\_log](replication-and-binary-log-system-variables.md#sync_relay_log). If the replica's operating system or host crashes in between, the replica loses events that the primary has already counted as safely replicated.

With `sync_relay_log=1`, each event is synced to disk before the replica acknowledges it, so an acknowledged transaction is durable on the replica at the moment the primary is told so. That is the value at which semisynchronous replication delivers the durability it appears to promise, at the cost of one sync per event rather than one per 10,000.

### Surviving a Replica Restart

Whether an acknowledged transaction is still in the relay log after the replica restarts is controlled by [relay\_log\_recovery](replication-and-binary-log-system-variables.md#relay_log_recovery), which defaults to `0` (`OFF`). When it is set to `1`, the replica discards the relay logs it has not yet applied on startup and fetches those events from the primary again.

Normally that is harmless, because the primary still has the events. It stops being harmless when the primary has lost them: transactions that existed only in the replica's relay log are then lost, which defeats the purpose of semisynchronous replication. This is worth checking in an existing configuration, since `relay_log_recovery=1` is often enabled for crash safety without this interaction in mind.

Leaving [relay\_log\_purge](replication-and-binary-log-system-variables.md#relay_log_purge) at its default of `1` is safe with semisynchronous replication. A relay log is only purged once the [replica's SQL thread](replication-threads.md#replica-sql-thread) has applied all of its events, so purging never discards an acknowledged transaction that has not been applied yet. Do not combine `relay_log_purge=0` with `relay_log_recovery=1`, which can cause the replica to read relay logs that were not purged, leading to data inconsistencies.

### The Case That Cannot Be Covered

{% hint style="warning" %}
A replica that connects using [GTIDs](gtid.md), with `MASTER_USE_GTID` set to `slave_pos` or `current_pos`, purges its relay logs every time the replication threads start, including after a restart of the replica, regardless of `relay_log_recovery`. Transactions that reached only the replica's relay log therefore do not survive a restart of that replica. If the primary lost them as well, they are gone, and no setting on the replica closes that window. The server-side work on this limitation is tracked in [MDEV-4698](https://jira.mariadb.org/browse/MDEV-4698).
{% endhint %}

Losing the primary and a replica at the same time is unlikely, so in practice the exposure is narrow. It is worth stating plainly, though, because GTID-based replication is the recommended configuration, so this is the case most deployments are in. What keeps the exposure small there is the primary's own durability, rather than anything on the replica: a crashed primary that has not lost committed transactions can supply them again once it is back.

From MariaDB 12.3, the [InnoDB-based binary log](innodb-based-binary-log.md) (`binlog_storage_engine=innodb`) is the better way to get that durability, because the binary log is written through InnoDB's own crash recovery. With it, `sync_binlog` is not needed and is effectively ignored, and commit durability is controlled solely by [innodb\_flush\_log\_at\_trx\_commit](../../server-usage/storage-engines/innodb/innodb-system-variables.md#innodb_flush_log_at_trx_commit). On a traditional file-based binary log, [sync\_binlog](replication-and-binary-log-system-variables.md#sync_binlog)`=1` is what provides it.

### Recommended Settings

On every semisynchronous replica:

* `sync_relay_log=1`, so that events acknowledged to the primary are durable on the replica.

On semisynchronous replicas that connect using binary log file and position coordinates:

* `relay_log_recovery=0`, so that relay logs survive a restart of the replica and the transactions semisynchronous replication placed there are not discarded.
* `relay_log_purge=1` (the default). `relay_log_purge=0` also preserves the guarantee, but only combine it with `relay_log_recovery=0`.

On the primary:

* From MariaDB 12.3, the [InnoDB-based binary log](innodb-based-binary-log.md) (`binlog_storage_engine=innodb`), with [innodb\_flush\_log\_at\_trx\_commit](../../server-usage/storage-engines/innodb/innodb-system-variables.md#innodb_flush_log_at_trx_commit)`=1` (the default). `sync_binlog` does not apply here and is effectively ignored.
* On a traditional file-based binary log, [sync\_binlog](replication-and-binary-log-system-variables.md#sync_binlog)`=1` together with `innodb_flush_log_at_trx_commit=1`.

Either way, the point is that the primary can supply transactions again after a crash. This is what limits the exposure for replicas that connect using GTIDs, where relay logs are always purged when the replication threads start.

## System Variables

#### `rpl_semi_sync_master_enabled`

* Description: Set to `ON` to enable semi-synchronous replication primary. Disabled by default.
* Command line: `--rpl-semi-sync-master-enabled[={0|1}]`
* Scope: Global
* Dynamic: Yes
* Data Type: `boolean`
* Default Value: `OFF`

#### `rpl_semi_sync_master_timeout`

* Description: The timeout value, in milliseconds, for semi-synchronous replication in the primary. If this timeout is exceeded in waiting on a commit for acknowledgement from a replica, the primary will revert to asynchronous replication.
  * When a timeout occurs, the [Rpl\_semi\_sync\_master\_status](../optimization-and-tuning/system-variables/semisynchronous-replication-plugin-status-variables.md#rpl_semi_sync_master_status) status variable will also be switched to `OFF`.
  * See [Configuring the Primary Timeout](semisynchronous-replication.md#configuring-the-primary-timeout) for more information.
* Command line: `--rpl-semi-sync-master-timeout[=#]`
* Scope: Global
* Dynamic: Yes
* Data Type: `numeric`
* Default Value: `10000` (10 seconds)
* Range: `0` to `18446744073709551615`

#### `rpl_semi_sync_master_trace_level`

* Description: The tracing level for semi-sync replication. Four levels are defined:
  * `1`: General level, including for example time function failures.
  * `16`: More detailed level, with more verbose information.
  * `32`: Net wait level, including more information about network waits.
  * `64`: Function level, including information about function entries and exits.
* Command line: `--rpl-semi-sync-master-trace-level[=#]`
* Scope: Global
* Dynamic: Yes
* Data Type: `numeric`
* Default Value: `32`
* Range: `0` to `18446744073709551615`

#### `rpl_semi_sync_master_wait_no_slave`

* Description: If all replicas have disconnected from the primary (i.e. [Rpl\_semi\_sync\_master\_clients](../optimization-and-tuning/system-variables/semisynchronous-replication-plugin-status-variables.md#rpl_semi_sync_master_clients) is 0), this variable controls whether or not the primary will still suspend the next transaction's (and any others that commit within [Rpl\_semi\_sync\_master\_timeout](../optimization-and-tuning/system-variables/semisynchronous-replication-plugin-status-variables.md#rpl_semi_sync_master_clients) duration) commit phase to wait for a replica to connect or reconnect, and send an ACK. If set to `ON`, the default, the replica count may drop to zero, and the primary will still wait for the timeout period for the next transaction, and any more that commit after this transaction within the semi-sync timeout duration. If no ACK is received in this time, the primary will revert to asynchronous replication. If set to `OFF`, the primary will revert to asynchronous replication as soon as the replica count drops to zero.
* Command line: `--rpl-semi-sync-master-wait-no-slave[={0|1}]`
* Scope: Global
* Dynamic: Yes
* Data Type: `boolean`
* Default Value: `ON`

#### `rpl_semi_sync_master_wait_point`

* Description: Whether the transaction should wait for semi-sync acknowledgement after having synced the binlog (`AFTER_SYNC`), or after having committed in storage engine (`AFTER_COMMIT`, the default).
  * When this variable is set to `AFTER_SYNC`, the primary performs the following steps:
    1. Prepares the transaction in the storage engine.
    2. Syncs the transaction to the [binary log](../../server-management/server-monitoring-logs/binary-log/).
    3. Waits for acknowledgement from the replica.
    4. Commits the transaction to the storage engine.
    5. Returns an acknowledgement to the client.
  * When this variable is set to `AFTER_COMMIT`, the primary performs the following steps:
    1. Prepares the transaction in the storage engine.
    2. Syncs the transaction to the [binary log](../../server-management/server-monitoring-logs/binary-log/).
    3. Commits the transaction to the storage engine.
    4. Waits for acknowledgement from the replica.
    5. Returns an acknowledgement to the client.
  * In [MariaDB 10.1.2](https://app.gitbook.com/s/aEnK0ZXmUbJzqQrTjFyb/community-server/old-releases/10.1/10.1.2) and before, this system variable does not exist. However, in those versions, the primary waits for the acknowledgement from replicas at a point that is equivalent to `AFTER_COMMIT`.
  * See [Configuring the Primary Wait Point](semisynchronous-replication.md#configuring-the-primary-wait-point) for more information.
* Command line: `--rpl-semi-sync-master-wait-point=value`
* Scope: Global
* Dynamic: Yes
* Data Type: `enum`
* Default Value: `AFTER_COMMIT`
* Valid Values: `AFTER_SYNC`, `AFTER_COMMIT`

#### `rpl_semi_sync_slave_delay_master`

* Description: Only write primary info file when ack is needed.
* Command line: `--rpl-semi-sync-slave-delay-master[={0|1}]`
* Scope: Global
* Dynamic: Yes
* Data Type: `boolean`
* Default Value: `OFF`

#### `rpl_semi_sync_slave_enabled`

* Description: Set to `ON` to enable semi-synchronous replication replica. Disabled by default.
* Command line: `--rpl-semi-sync-slave-enabled[={0|1}]`
* Scope: Global
* Dynamic: Yes
* Data Type: `boolean`
* Default Value: `OFF`

#### `rpl_semi_sync_slave_kill_conn_timeout`

* Description: Timeout for the mysql connection used to kill the replica io\_thread's connection on primary. This timeout comes into play when stop slave is executed.
* Command line: `--rpl-semi-sync-slave-kill-conn-timeout[={0|1}]`
* Scope: Global
* Dynamic: Yes
* Data Type: `numeric`
* Default Value: `5`
* Range: `0` to `4294967295`

#### `rpl_semi_sync_slave_trace_level`

* Description: The tracing level for semi-sync replication. The levels are the same as for [rpl\_semi\_sync\_master\_trace\_level](semisynchronous-replication.md#rpl_semi_sync_master_trace_level).
* Command line: `--rpl-semi-sync-slave-trace_level[=#]`
* Scope: Global
* Dynamic: Yes
* Data Type: `numeric`
* Default Value: `32`
* Range: `0` to `18446744073709551615`

## Options

### `init-rpl-role`

* From [MariaDB 10.6.19](https://app.gitbook.com/s/aEnK0ZXmUbJzqQrTjFyb/community-server/10.6/10.6.19), [MariaDB 10.11.9](https://app.gitbook.com/s/aEnK0ZXmUbJzqQrTjFyb/community-server/10.11/10.11.9), [MariaDB 11.1.6](https://app.gitbook.com/s/aEnK0ZXmUbJzqQrTjFyb/community-server/old-releases/11.1/11.1.6), [MariaDB 11.2.5](https://app.gitbook.com/s/aEnK0ZXmUbJzqQrTjFyb/community-server/old-releases/11.2/11.2.5), [MariaDB 11.4.3](https://app.gitbook.com/s/aEnK0ZXmUbJzqQrTjFyb/community-server/11.4/11.4.3) and [MariaDB 11.5.2](https://app.gitbook.com/s/aEnK0ZXmUbJzqQrTjFyb/community-server/old-releases/11.5/11.5.2), changes the condition for semi-sync recovery to truncate the [binlog](../../server-management/server-monitoring-logs/binary-log/) to instead use this option, when set to SLAVE. This avoids a possible error state where the replica’s state is ahead of the primaries. See [-init-rpl-role](../../server-management/starting-and-stopping-mariadb/mariadbd-options.md#init-rpl-role).

## Status Variables

For a list of the status variables that report on semisynchronous replication, see [Semisynchronous Replication Status Variables](../optimization-and-tuning/system-variables/semisynchronous-replication-plugin-status-variables.md).

<sub>_This page is licensed: CC BY-SA / Gnu FDL_</sub>

{% @marketo/form formId="4316" %}
