---
description: >-
  Implement semi-synchronous replication in MariaDB Server. How to ensure data
  durability by requiring at least one replica to acknowledge receipt of
  transactions before the master commits.
---

# Semisynchronous Replication

## Description

[Standard MariaDB replication](./) is asynchronous, but MariaDB also provides a semisynchronous replication option. The feature is built into the server and is always available. In versions prior to [MariaDB 10.3](https://app.gitbook.com/s/aEnK0ZXmUbJzqQrTjFyb/community-server/old-releases/release-notes-mariadb-10-3-series/what-is-mariadb-103), it was a separate plugin that needed to be installed.

With regular asynchronous replication, replicas request events from the primary's binary log whenever the replicas are ready. The primary does not wait for a replica to confirm that an event has been received.

With fully synchronous replication, all replicas are required to respond that they have received the events. See [Galera Cluster](https://app.gitbook.com/o/diTpXxF5WsbHqTReoBsS/s/3VYeeVGUV4AMqrA3zwy7/).

Semisynchronous replication waits for just one replica to acknowledge that it has received and logged the events.

Semisynchronous replication therefore comes with some negative performance impact, but increased data integrity. Since the delay is based on the roundtrip time to the replica and back, this delay is minimized for servers in close proximity over fast networks.

Semisynchronous replication is built into the server. See [MDEV-13073](https://jira.mariadb.org/browse/MDEV-13073) for more information.

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

When switching between semisynchronous replication and asynchronous replication on a replica with [replica IO threads](replication-threads.md#threads-on-the-slave) already running, the replica I/O thread will need to be restarted. For example:

```sql
STOP SLAVE IO_THREAD;
START SLAVE IO_THREAD;
```

If this is not done, then the replica IO thread will continue to use the previous setting.

## Configuring the Primary Timeout

In semisynchronous replication, only after the events have been written to the relay log and flushed does the replica acknowledge receipt of a transaction's events. If the replica does not acknowledge the transaction before a certain amount of time has passed, then a timeout occurs and the primary switches to asynchronous replication. This will be reflected in the primary's [error log](../../server-management/server-monitoring-logs/error-log.md) with messages like the following:

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
* `AFTER_COMMIT`

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

1. Prepares the transaction in the storage engine.
2. Syncs the transaction to the [binary log](../../server-management/server-monitoring-logs/binary-log/).
3. Waits for acknowledgement from the replica.
4. Commits the transaction to the storage engine.
5. Returns an acknowledgement to the client.

The effects of the `AFTER_SYNC` wait point are:

* All clients see the same data on the primary at the same time; after acknowledgement by the replica and after being committed to the storage engine on the primary.
* If the primary crashes, then failover should be lossless, because all transactions committed on the primary would have been replicated to the replica.
* However, if the primary crashes, then its [binary log](../../server-management/server-monitoring-logs/binary-log/) may also contain events for transactions that were prepared by the storage engine and written to the binary log, but that were never actually committed by the storage engine. As part of the server's [automatic crash recovery](../../server-management/server-monitoring-logs/transaction-coordinator-log/heuristic-recovery-with-the-transaction-coordinator-log.md) process, the server may recover these prepared transactions when the server is restarted. This could cause the "old" crashed primary to become inconsistent with its former replicas when they have\
  been reconfigured to replace the old primary with a new one.\
  The old primary in such a scenario can be re-introduced only as a [semisync replica](semisynchronous-replication.md#rpl_semi_sync_slave_enabled).\
  The server post-crash recovery of the server configured with `rpl_semi_sync_slave_enabled = ON`\
  ensures through [MDEV-21117](https://jira.mariadb.org/browse/MDEV-21117) that the server will not have extra transactions.\
  The reconfigured as semisync replica server's binlog gets truncated to discard transactions proven\
  not to be committed, in any of their branches if they are multi-engine.\
  Truncation does not occur though when there exists a non-transactional group of events beyond the truncation position in which case recovery reports an error.\
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

## Versions

| Version | Status  | Introduced                                                                                                                                                                                                                  |
| ------- | ------- | --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| N/A     | N/A     | [MariaDB 10.3.3](https://app.gitbook.com/s/aEnK0ZXmUbJzqQrTjFyb/community-server/old-releases/release-notes-mariadb-10-3-series/mariadb-1033-release-notes) (feature is built-in, no longer available as a separate plugin) |
| 1.0     | Stable  | [MariaDB 10.1.13](https://app.gitbook.com/s/aEnK0ZXmUbJzqQrTjFyb/community-server/old-releases/release-notes-mariadb-10-1-series/mariadb-10113-release-notes)                                                               |
| 1.0     | Gamma   | [MariaDB 10.0.13](https://app.gitbook.com/s/aEnK0ZXmUbJzqQrTjFyb/community-server/old-releases/release-notes-mariadb-10-0-series/mariadb-10011-release-notes)                                                               |
| 1.0     | Unknown | [MariaDB 10.0.11](https://github.com/mariadb-corporation/docs-server/blob/test/server/ha-and-performance/standard-replication/broken-reference/README.md)                                                                   |
| 1.0     | N/A     | [MariaDB 5.5](https://app.gitbook.com/s/aEnK0ZXmUbJzqQrTjFyb/community-server/old-releases/release-notes-mariadb-5-5-series/changes-improvements-in-mariadb-5-5)                                                            |

## System Variables

#### `rpl_semi_sync_master_enabled`

* Description: Set to `ON` to enable semi-synchronous replication primary. Disabled by default.
* Commandline: `--rpl-semi-sync-master-enabled[={0|1}]`
* Scope: Global
* Dynamic: Yes
* Data Type: `boolean`
* Default Value: `OFF`

#### `rpl_semi_sync_master_timeout`

* Description: The timeout value, in milliseconds, for semi-synchronous replication in the primary. If this timeout is exceeded in waiting on a commit for acknowledgement from a replica, the primary will revert to asynchronous replication.
  * When a timeout occurs, the [Rpl\_semi\_sync\_master\_status](../optimization-and-tuning/system-variables/semisynchronous-replication-plugin-status-variables.md#rpl_semi_sync_master_status) status variable will also be switched to `OFF`.
  * See [Configuring the Primary Timeout](semisynchronous-replication.md#configuring-the-primary-timeout) for more information.
* Commandline: `--rpl-semi-sync-master-timeout[=#]`
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
* Commandline: `--rpl-semi-sync-master-trace-level[=#]`
* Scope: Global
* Dynamic: Yes
* Data Type: `numeric`
* Default Value: `32`
* Range: `0` to `18446744073709551615`

#### `rpl_semi_sync_master_wait_no_slave`

* Description: If all replicas have disconnected from the primary (i.e. [Rpl\_semi\_sync\_master\_clients](../optimization-and-tuning/system-variables/semisynchronous-replication-plugin-status-variables.md#rpl_semi_sync_master_clients) is 0), this variable controls whether or not the primary will still suspend the next transaction's (and any others that commit within [Rpl\_semi\_sync\_master\_timeout](../optimization-and-tuning/system-variables/semisynchronous-replication-plugin-status-variables.md#rpl_semi_sync_master_timeout) duration) commit phase to wait for a replica to (re-)connect and send an ACK. If set to `ON`, the default, the replica count may drop to zero, and the primary will still wait for the timeout period for the next transaction, and any more that commit after this transaction within the semi-sync timeout duration. If no ACK is received in this time, the primary will revert to asynchronous replication. If set to `OFF`, the primary will revert to asynchronous replication as soon as the replica count drops to zero.
* Commandline: `--rpl-semi-sync-master-wait-no-slave[={0|1}]`
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
  * In [MariaDB 10.1.2](https://app.gitbook.com/s/aEnK0ZXmUbJzqQrTjFyb/community-server/old-releases/release-notes-mariadb-10-1-series/mariadb-10-1-2-release-notes) and before, this system variable does not exist. However, in those versions, the primary waits for the acknowledgement from replicas at a point that is equivalent to `AFTER_COMMIT`.
  * See [Configuring the Primary Wait Point](semisynchronous-replication.md#configuring-the-primary-wait-point) for more information.
* Commandline: `--rpl-semi-sync-master-wait-point=value`
* Scope: Global
* Dynamic: Yes
* Data Type: `enum`
* Default Value: `AFTER_COMMIT`
* Valid Values: `AFTER_SYNC`, `AFTER_COMMIT`

#### `rpl_semi_sync_slave_delay_master`

* Description: Only write primary info file when ack is needed.
* Commandline: `--rpl-semi-sync-slave-delay-master[={0|1}]`
* Scope: Global
* Dynamic: Yes
* Data Type: `boolean`
* Default Value: `OFF`

#### `rpl_semi_sync_slave_enabled`

* Description: Set to `ON` to enable semi-synchronous replication replica. Disabled by default.
* Commandline: `--rpl-semi-sync-slave-enabled[={0|1}]`
* Scope: Global
* Dynamic: Yes
* Data Type: `boolean`
* Default Value: `OFF`

#### `rpl_semi_sync_slave_kill_conn_timeout`

* Description: Timeout for the mysql connection used to kill the replica io\_thread's connection on primary. This timeout comes into play when stop slave is executed.
* Commandline: `--rpl-semi-sync-slave-kill-conn-timeout[={0|1}]`
* Scope: Global
* Dynamic: Yes
* Data Type: `numeric`
* Default Value: `5`
* Range: `0` to `4294967295`

#### `rpl_semi_sync_slave_trace_level`

* Description: The tracing level for semi-sync replication. The levels are the same as for [rpl\_semi\_sync\_master\_trace\_level](semisynchronous-replication.md#rpl_semi_sync_master_trace_level).
* Commandline: `--rpl-semi-sync-slave-trace_level[=#]`
* Scope: Global
* Dynamic: Yes
* Data Type: `numeric`
* Default Value: `32`
* Range: `0` to `18446744073709551615`

## Options

### `init-rpl-rol`

* From [MariaDB 10.6.19](https://app.gitbook.com/s/aEnK0ZXmUbJzqQrTjFyb/community-server/mariadb-10-6-series/mariadb-10-6-19-release-notes), [MariaDB 10.11.9](https://app.gitbook.com/s/aEnK0ZXmUbJzqQrTjFyb/community-server/mariadb-10-11-series/mariadb-10-11-9-release-notes), [MariaDB 11.1.6](https://app.gitbook.com/s/aEnK0ZXmUbJzqQrTjFyb/community-server/old-releases/release-notes-mariadb-11-1-series/mariadb-11-1-6-release-notes), [MariaDB 11.2.5](https://app.gitbook.com/s/aEnK0ZXmUbJzqQrTjFyb/community-server/old-releases/release-notes-mariadb-11-2-series/mariadb-11-2-5-release-notes), [MariaDB 11.4.3](https://app.gitbook.com/s/aEnK0ZXmUbJzqQrTjFyb/community-server/mariadb-11-4-series/mariadb-11-4-3-release-notes) and [MariaDB 11.5.2](https://app.gitbook.com/s/aEnK0ZXmUbJzqQrTjFyb/community-server/old-releases/release-notes-mariadb-11-5-rolling-releases/mariadb-11-5-2-release-notes), changes the condition for semi-sync recovery to truncate the [binlog](../../server-management/server-monitoring-logs/binary-log/) to instead use this option, when set to SLAVE. This avoids a possible error state where the replica’s state is ahead of the primary’s. See [-init-rpl-role](../../server-management/starting-and-stopping-mariadb/mariadbd-options.md#-init-rpl-role).

### `rpl-semi-sync_master`

* Description: Controls how the server should treat the plugin when the server starts up.
  * Valid values are:
    * `OFF` - Disables the plugin without removing it from the [mysql.plugins](../../reference/system-tables/the-mysql-database-tables/mysql-plugin-table.md) table.
    * `ON` - Enables the plugin. If the plugin cannot be initialized, then the server will still continue starting up, but the plugin will be disabled.
    * `FORCE` - Enables the plugin. If the plugin cannot be initialized, then the server will fail to start with an error.
    * `FORCE_PLUS_PERMANENT` - Enables the plugin. If the plugin cannot be initialized, then the server will fail to start with an error. In addition, the plugin cannot be uninstalled with [UNINSTALL SONAME](../../reference/sql-statements/administrative-sql-statements/plugin-sql-statements/uninstall-soname.md) or [UNINSTALL PLUGIN](../../reference/sql-statements/administrative-sql-statements/plugin-sql-statements/uninstall-plugin.md) while the server is running.
  * See [Plugin Overview: Configuring Plugin Activation at Server Startup](../../reference/plugins/plugin-overview.md#configuring-plugin-activation-at-server-startup) for more information.
* Commandline: `--rpl-semi-sync-master=value`
* Data Type: `enumerated`
* Default Value: `ON`
* Valid Values: `OFF`, `ON`, `FORCE`, `FORCE_PLUS_PERMANENT`
* Removed: [MariaDB 10.3.3](https://app.gitbook.com/s/aEnK0ZXmUbJzqQrTjFyb/community-server/old-releases/release-notes-mariadb-10-3-series/mariadb-1033-release-notes)

### `rpl-semi-sync_slave`

* Description: Controls how the server should treat the plugin when the server starts up.
  * Valid values are:
    * `OFF` - Disables the plugin without removing it from the [mysql.plugins](../../reference/system-tables/the-mysql-database-tables/mysql-plugin-table.md) table.
    * `ON` - Enables the plugin. If the plugin cannot be initialized, then the server will still continue starting up, but the plugin will be disabled.
    * `FORCE` - Enables the plugin. If the plugin cannot be initialized, then the server will fail to start with an error.
    * `FORCE_PLUS_PERMANENT` - Enables the plugin. If the plugin cannot be initialized, then the server will fail to start with an error. In addition, the plugin cannot be uninstalled with [UNINSTALL SONAME](../../reference/sql-statements/administrative-sql-statements/plugin-sql-statements/uninstall-soname.md) or [UNINSTALL PLUGIN](../../reference/sql-statements/administrative-sql-statements/plugin-sql-statements/uninstall-plugin.md) while the server is running.
  * See [Plugin Overview: Configuring Plugin Activation at Server Startup](../../reference/plugins/plugin-overview.md#configuring-plugin-activation-at-server-startup) for more information.
* Commandline: `--rpl-semi-sync-slave=value`
* Data Type: `enumerated`
* Default Value: `ON`
* Valid Values: `OFF`, `ON`, `FORCE`, `FORCE_PLUS_PERMANENT`
* Removed: [MariaDB 10.3.3](https://app.gitbook.com/s/aEnK0ZXmUbJzqQrTjFyb/community-server/old-releases/release-notes-mariadb-10-3-series/mariadb-1033-release-notes)

## Status Variables

For a list of status variables added when the plugin is installed, see [Semisynchronous Replication Plugin Status Variables](../optimization-and-tuning/system-variables/semisynchronous-replication-plugin-status-variables.md).

<sub>_This page is licensed: CC BY-SA / Gnu FDL_</sub>

{% @marketo/form formId="4316" %}
