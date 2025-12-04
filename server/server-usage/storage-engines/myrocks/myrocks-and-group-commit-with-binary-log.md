---
description: >-
  Understand how MyRocks implements group commit to coordinate with the binary
  log, ensuring data consistency and crash safety for replicated transactions.
---

# MyRocks Group Commit with Binary log

MyRocks supports group commit with the [binary log](../../../server-management/server-monitoring-logs/binary-log/) ([MDEV-11934](https://jira.mariadb.org/browse/MDEV-11934)).

## Counter Values to Watch

(The following is only necessary if you are studying MyRocks internals)

MariaDB's group commit counters are:

[Binlog\_commits](../../../ha-and-performance/standard-replication/replication-and-binary-log-status-variables.md#binlog_commits) - how many transactions were written to the binary log

[Binlog\_group\_commits](../../../ha-and-performance/standard-replication/replication-and-binary-log-status-variables.md#binlog_group_commits) - how many group commits happened. (e.g. if each group had two transactions, this is twice as small as [Binlog\_commits](../../../ha-and-performance/standard-replication/replication-and-binary-log-status-variables.md#binlog_commits))

On the RocksDB side, there is one relevant counter:[Rocksdb\_wal\_synced](myrocks-status-variables.md#rocksdb_wal_synced) - How many times RocksDB's WAL file was synced. (TODO: this is after group commit happened, right?)

## On the Value of rocksdb\_wal\_group\_syncs

FB/MySQL-5.6 has a [rocksdb\_wal\_group\_syncs](myrocks-status-variables.md#rocksdb_wal_group_syncs) counter (The counter is provided by MyRocks, it is not a view of a RocksDB counter). It is increased in rocksdb\_flush\_wal() when doing the rdb->FlushWAL() call.

rocksdb\_flush\_wal() is called by MySQL's Group Commit when it wants to make the effect of several rocksdb\_prepare() calls persistent.

So, the value of [rocksdb\_wal\_group\_syncs](myrocks-status-variables.md#rocksdb_wal_group_syncs) in FB/MySQL-5.6 is similar to [Binlog\_group\_commits](../../../ha-and-performance/standard-replication/replication-and-binary-log-status-variables.md#binlog_group_commits) in MariaDB.

MariaDB doesn't have that call, each rocksdb\_prepare() call takes care of being persistent on its own.

Because of that, [rocksdb\_wal\_group\_syncs](myrocks-status-variables.md#rocksdb_wal_group_syncs) is zero for MariaDB. (Currently, it is only incremented when the binlog is rotated).

## Examples

So for a workload with concurrency=50, n\_queries=10K, one gets

* Binlog\_commits=10K
* Binlog\_group\_commits=794
* Rocksdb\_wal\_synced=8362

This is on a RAM disk

For a workload with concurrency=50, n\_queries=10K, rotating laptop hdd, one gets

* Binlog\_commits= 10K
* Binlog\_group\_commits=1403
* Rocksdb\_wal\_synced=400

The test took 38 seconds, Number of syncs was 1400+400=1800, which gives 45 syncs/sec which looks normal for this slow rotating desktop hdd.

Note that the WAL was synced fewer times than there were binlog commit groups (?)

<sub>_This page is licensed: CC BY-SA / Gnu FDL_</sub>

{% @marketo/form formId="4316" %}
