---
description: >-
  Build a resilient replication cluster. This guide explains how to combine
  MaxScale's failover with semi-synchronous replication to minimize data loss
  during crashes.
---

# Failure-tolerant replication and failover

## Introduction

The goal of this guide is to set up a replication cluster managed by MaxScale that is reasonably tolerant of failures. That is, even if one part fails, the cluster continues to work. Additionally, transaction data are preserved whenever possible. All of this works automatically.

This guide assumes that the reader is familiar with MariaDB replication and GTIDs, [MariaDB Monitor](../reference/maxscale-monitors/mariadb-monitor.md), and [failover](automatic-failover-with-mariadb-monitor.md).

## The Problem with Normal Replication

The basic problem of replication is that the primary and the replica are not always in the same state. When a commit is performed on the primary, the primary updates both the actual database file and the binary log. These items are updated in a transactional manner, either both succeed or fail. Then, the primary sends the binary log event to the replicas and they update their own databases and logs.

A replica may crash or lose connection to the primary. Fortunately, this is not a big issue, because once the replica returns, it can simply resume replication from where it left off. The replica cannot diverge as it is always either in the same state as the primary, or behind. Only if the primary lacks the binary logs from the moment the replica went down, the replica is lost.

If the primary crashes or loses network connection, failover may lose data. This depends on the point in time at which the crash happens:

1. If the primary managed to send all committed transactions to a replica, all is still well. The replica has all the data, and can be promoted to primary e.g. by MaxScale (which, in that case, promotes the most up-to-date replica). Once the old primary returns, it can rejoin the cluster.
2. If the primary crashes just after it committed a transaction and updated its binary log, but before it sent the binary log event to a replica, failover loses data and the old primary can no longer rejoin the cluster.

Let’s look at situation B in more detail. _server1_ is the original primary as and its replicas are _server2_ and _server3_, with server ids 1,2 and 3, respectively. _server1_ is at gtid 1-1-101 when it crashes, while the others have replicated to the previous event 1-1-100. The example server status output below is for demonstration only, since in reality it would be unlikely that the monitor would manage to update the gtid-position of _server1_ right at the moment of crash.

```bash
$ maxctrl list servers
┌──────────┬─────────────────┬──────┬─────────────┬────────┬────────────────────┬─────────┬──────────┐
│ Server   │ Address         │ Port │ Connections │ Status │ Status Info        │ GTID    │ Monitor  │
├──────────┼─────────────────┼──────┼─────────────┼────────┼────────────────────┼─────────┼──────────┤
│ server1  │ 192.168.121.51  │ 3306 │ 0           │ Write  │ Down               │ 1-1-101 │ Monitor1 │
├──────────┼─────────────────┼──────┼─────────────┼────────┼────────────────────┼─────────┼──────────┤
│ server2  │ 192.168.121.190 │ 3306 │ 0           │ Read   │ Replica, read_only │ 1-1-100 │ Monitor1 │
├──────────┼─────────────────┼──────┼─────────────┼────────┼────────────────────┼─────────┼──────────┤
│ server3  │ 192.168.121.112 │ 3306 │ 0           │ Read   │ Replica, read_only │ 1-1-100 │ Monitor1 │
└──────────┴─────────────────┴──────┴─────────────┴────────┴────────────────────┴─────────┴──────────┘
```

_server1_ stays down long enough for failover to activate. (In MaxScale, the time is roughly _monitor\_interval_ \* _failcount_.) _server2_ gets promoted, and MaxScale routes any new writes to it. _server2_ starts generating binary log events with gtids 1-2-101, 1-2-102 and so on. If _server1_ now comes back online, it can no longer rejoin as it is at gtid 1-1-101, which conflicts with 1-2-101.

```bash
$ maxctrl list servers
┌──────────┬─────────────────┬──────┬─────────────┬────────┬────────────────────┬─────────┬──────────┐
│ Server   │ Address         │ Port │ Connections │ Status │ Status Info        │ GTID    │ Monitor  │
├──────────┼─────────────────┼──────┼─────────────┼────────┼────────────────────┼─────────┼──────────┤
│ server1  │ 192.168.121.51  │ 3306 │ 0           │ Up     │                    │ 1-1-101 │ Monitor1 │
├──────────┼─────────────────┼──────┼─────────────┼────────┼────────────────────┼─────────┼──────────┤
│ server2  │ 192.168.121.190 │ 3306 │ 0           │ Write  │ Primary            │ 1-2-102 │ Monitor1 │
├──────────┼─────────────────┼──────┼─────────────┼────────┼────────────────────┼─────────┼──────────┤
│ server3  │ 192.168.121.112 │ 3306 │ 0           │ Read   │ Replica, read_only │ 1-2-102 │ Monitor1 │
└──────────┴─────────────────┴──────┴─────────────┴────────┴────────────────────┴─────────┴──────────┘
```

At this point, the DBA could forcefully alter the gtid of _server1_, setting it to 1-1-100, which is in _server2_’s binary log, enabling rejoin. This is usually ill-advised, as changing the gtid does not roll back the actual data in _server2_’s database, meaning that data conflicts can still happen, perhaps days later. A more reliable way to handle this case is to rebuild _server1_ from one of the other servers. (MaxScale can help with this process, but it requires configuration and [manual launching](../reference/maxscale-monitors/mariadb-monitor.md#backup-operations).)

If the old primary returns before failover activates, replication can continue regardless of what exact moment the crash happened. **This means that the DBA should configure automatic failover to happen only after the primary has been down so long that the downsides of service outage outweigh the threat of losing data and the need of having to rebuild the old primary.** _monitor\_interval_ \* _failcount_ should at a minimum be large enough that failover does not trigger due to a momentary network failure.

## Semi-Synchronous Replication

[Semi-synchronous replication](https://mariadb.com/docs/server/ha-and-performance/standard-replication/semisynchronous-replication) offers a more reliable, but also a more complicated way to keep the cluster in sync. Semi-sync replication means that after the primary commits a transaction, it does not immediately return an OK to the client. Instead, the primary sends the binary log update to the replicas and waits for an acknowledgement from at least one replica before sending the OK message back to the client. This means that once the client gets the OK, the transaction data is typically on at least two servers. This is not absolutely certain, though, as the primary does not wait forever for the replica acknowledgement. If no replica responds in time, the primary switches to normal replication and returns OK to the client. This timeout is controlled by MariaDB Server setting **rpl\_semi\_sync\_master\_timeout**. If this limit is being hit, the client should notice it by the transaction visibly stalling. Even if this limit is not hit, throughput suffers compared to normal replication, due to the additional waiting.

Semi-synchronous replication by itself does not remove the possibility of the primary diverging after a crash. The scenario B presented in the previous section can still happen if the primary crashes after applying the transaction but before sending it to replicas. To increase crash safety, a few settings need to be tuned to change the behavior of the primary server both during replication and during startup after a crash (crash recovery).

### Enable Semi-Synchronous Replication

To enable semi semi-synchronous replication, add the following to the configuration files of all servers:

```ini
rpl_semi_sync_master_enabled=ON
rpl_semi_sync_slave_enabled=ON
```

These settings allow the servers to act as both semi-sync primary and replica, which is useful when combined with automatic failover. Restart the servers and run `SHOW STATUS LIKE 'rpl%';`, a statement that shows semi-sync related status variables. Check the values of `Rpl_semi_sync_master_clients`, `Rpl_semi_sync_master_status` and `Rpl_semi_sync_slave_status`. On the primary, their values should be:

1. `Rpl_semi_sync_master_clients`: \<number of replicas>
2. `Rpl_semi_sync_master_status`: ON
3. `Rpl_semi_sync_slave_status`: OFF

On the replicas, the values should be:

1. `Rpl_semi_sync_master_clients`: 0
2. `Rpl_semi_sync_master_status`: ON
3. `Rpl_semi_sync_slave_status`: ON

### Configure Wait Point and Startup Role

Next, change the point at which the primary server waits for the replica acknowledgement. By default, this is after the transaction is written to storage, which is not much different compared to normal replication. Set the following in the server configuration files:

```ini
rpl_semi_sync_master_wait_point=AFTER_SYNC
```

`AFTER_SYNC` means that the primary sends the binary log event to replicas, after writing it to the binary log but before committing the actual transaction to its own storage. The primary only updates its internal storage when at least one replica gives the reply or when the `rpl_semi_sync_master_timeout` is reached. More importantly, this means that if the primary crashes while waiting for the reply, its binary log and storage engine will be out of sync. On startup, the server must thus decide what to do: either consider the binary log correct and apply the missing transactions to storage, or discard the unverified binary log events.

As of MariaDB Server 10.6.19, 10.11.9, 11.1.6, 11.2.5, 11.4.3 and 11.5.2, this decision is controlled by the startup option [init-rpl-role](https://mariadb.com/docs/server/ha-and-performance/standard-replication/semisynchronous-replication#init-rpl-role). If set to `MASTER`, the server applies the transactions during startup, as it assumes to still be the primary. If `init-rpl-role` is set to `SLAVE`, the server discards the transactions. The former option does not improve the situation after a failover, as the primary could apply transactions that never made it to a replica. The latter option, on the other hand, ensures that, when the old primary comes back online, it does not have conflicting transactions and can rejoin the cluster as a replica. So, add the following to all server configurations:

```ini
init-rpl-role=SLAVE
```

### Configure Service Restart Delay

This scheme is not entirely without issues. `init-rpl-role=SLAVE` means that the old primary (_server1_) always discards the unverified transactions during startup, even if the data did successfully replicate to a replica before the crash (_server1_ crashed after sending the data but before receiving the reply). This is not an issue if failover has already occurred by this point, as _server1_ can just fetch the same writes from the new primary (_server2_). However, if _server1_ comes back online quickly, before failover, it could be behind _server2_: _server1_ at gtid 1-1-100 and _server2_ at 1-1-101.

```bash
$ maxctrl list servers
┌──────────┬─────────────────┬──────┬─────────────┬────────┬────────────────────┬─────────┬──────────┐
│ Server   │ Address         │ Port │ Connections │ Status │ Status Info        │ GTID    │ Monitor  │
├──────────┼─────────────────┼──────┼─────────────┼────────┼────────────────────┼─────────┼──────────┤
│ server1  │ 192.168.121.51  │ 3306 │ 0           │ Write  │ Primary            │ 1-1-100 │ Monitor1 │
├──────────┼─────────────────┼──────┼─────────────┼────────┼────────────────────┼─────────┼──────────┤
│ server2  │ 192.168.121.190 │ 3306 │ 0           │ Read   │ Replica, read_only │ 1-1-101 │ Monitor1 │
├──────────┼─────────────────┼──────┼─────────────┼────────┼────────────────────┼─────────┼──────────┤
│ server3  │ 192.168.121.112 │ 3306 │ 0           │ Read   │ Replica, read_only │ 1-1-101 │ Monitor1 │
└──────────┴─────────────────┴──────┴─────────────┴────────┴────────────────────┴─────────┴──────────┘
```

As _server1_ is still the primary, MaxScale sends any new writes to it. The next write will get gtid 1-1-101, meaning that both servers are on the same gtid but their actual contents likely differ. This will cause a replication error at some point.

This means that if a primary server crashes, it must stay down long enough for failover to occur, and to ensure MaxScale does not treat it as the primary once it returns. This can be enforced by changing the service settings. Run `sudo systemctl edit mariadb.service` on all server machines and add the following:

```ini
[Service]
RestartSec=1min
```

The configured time needs to be comfortably longer than _monitor\_interval_ \* _failcount_ configured to the MariaDB Monitor in MaxScale.

### Failure Scenarios

The setup described above protects against a primary server crashing and its diversion from the rest of the cluster. It does not protect from data loss due to network outages. If the connection to the primary server is lost during a transaction commit (before the data was replicated), the primary will eventually apply the transaction to its storage. If a failover occurred during the network outage, the rest of the cluster has already continued under a new primary, leaving the old one diverged. This is similar to normal replication.

Some queries are not transactional and may still risk diverging replication. These are typically DDL queries such as `CREATE TABLE`, `ALTER TABLE`, and so on. DDL queries can be transactional if the changes they do are “small”, such as renaming a column. Large-scale DDL queries (e.g. `ADD COLUMN` to a table with a billion rows) are more vulnerable. The settings presented in this document were only tested against simple DML queries that updated a single row.

### Client Perspective

If the client gets an OK to its commit command, then it knows that (assuming no semi-sync timeout happened) the transaction is in at least two servers. Only the primary has with certainty processed the update at this point; the replica may just have the event in its relay log. This means that `SELECT` queries routed to a replica (e.g. by the ReadWriteSplit router) may see old data.

If the client does not get an OK due to primary crash, the situation is more ambiguous:

1. Primary crashed before starting the commit
2. Primary crashed just before receiving the replica acknowledgement
3. Primary crashed just as it was about to send the OK

In case A, the transaction is lost. In case B, the transaction is present on the replica and will become visible at some point. In case C, the transaction is present on both servers. Since MaxScale cannot know which case is in effect, it does not attempt transaction replay (even if configured) and disconnects the client. It’s up to the client to then reconnect and figure out the status of the transaction.

### Test Summary

The server settings used during testing are below. `rpl_semi_sync_master_timeout` is given in milliseconds, `rpl_semi_sync_slave_kill_conn_timeout` in seconds.

```ini
rpl_semi_sync_master_enabled=ON
rpl_semi_sync_slave_enabled=ON
rpl_semi_sync_master_wait_point=AFTER_SYNC
rpl_semi_sync_master_timeout=6000
rpl_semi_sync_slave_kill_conn_timeout=5
init-rpl-role=SLAVE
gtid_strict_mode=1
log_slave_updates=1
```

The MariaDB Monitor in MaxScale was configured with both _auto\_failover_ and _auto\_rejoin_ enabled. Hundreds of failovers with continuous write traffic succeeded without a diverging old primary. When _init-rpl-role_ was changed to `MASTER`, replication eventually broke, although this could take some time.

<sub>_This page is licensed: CC BY-SA / Gnu FDL_</sub>

{% @marketo/form formId="4316" %}
