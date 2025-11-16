---
description: >-
  Boost MariaDB Server replication performance with parallel replication. This
  section explains how to configure replicas to apply events concurrently,
  reducing lag and improving throughput.
---

# Parallel Replication

{% hint style="info" %}
The terms _master_ and _slave_ have historically been used in replication, and MariaDB has begun the process of adding _primary_ and _replica_ synonyms. The old terms will continue to be used to maintain backward compatibility - see [MDEV-18777](https://jira.mariadb.org/browse/MDEV-18777) to follow progress on this effort.
{% endhint %}

Some writes, [replicated](./) from the primary can be executed in parallel (simultaneously) on the replica. Note that for parallel replication to work, both the primary and replica need to be [MariaDB 10.0.5](https://app.gitbook.com/s/aEnK0ZXmUbJzqQrTjFyb/community-server/old-releases/release-notes-mariadb-10-0-series/mariadb-1005-release-notes) or later.

## Parallel Replication Overview

MariaDB replication in general takes place in three parts:

* Replication events are read from the primary by the IO thread and queued in\
  the [relay log](../../server-management/server-monitoring-logs/binary-log/relay-log.md).
* Replication events are fetched one at a time by the SQL thread from the relay log
* Each event is applied on the replica to replicate all changes done on the\
  primary.

Before MariaDB 10, the third step was also performed by the SQL thread; this\
meant that only one event could execute at a time, and replication was\
essentially single-threaded. Since MariaDB 10, the third step can optionally be\
performed by a pool of separate replication worker threads, and thereby\
potentially increase replication performance by applying multiple events in parallel.

## How to Enable Parallel Replica

To enable, specify [slave-parallel-threads=#](replication-and-binary-log-system-variables.md) in your [my.cnf](../optimization-and-tuning/system-variables/sample-mycnf-files.md) file as an argument to mysql.\
Parallel replication can in addition be disabled on a per-multi-source\
connection by setting [@@connection\_name.slave-parallel-mode](replication-and-binary-log-system-variables.md) to "none".

The value (#) of slave\_parallel\_threads specifies how many threads will be created in a pool of worker\
threads used to apply events in parallel for _all_ your replicas (this includes [multi-source replication](multi-source-replication.md)). If the value is zero,\
then no worker threads are created, and old-style replication is used where events are applied inside the SQL thread. Usually the value, if non-zero, should be at least two times the number of multi-source primary connections used. It makes little sense to use only a single worker thread for one connection; this will incur some overhead in inter-thread communication between the SQL thread and the worker thread, but with just a single worker thread event cannot be applied in parallel anyway.

`slave-parallel-threads=#` is a dynamic variable that can be changed without restarting mysqld. All replicas' connections must however be stopped when changing the value.

## Configuring the Replica Parallel Mode

Parallel replication can be in-order or out-of-order:

* In-order executes transactions in parallel but orders the commit step of the transactions to happen in the exact same order as on the primary. Transactions are only executed in parallel to the extent that this can be automatically verified to be possible without any conflicts. This means\
  that the use of parallelism is completely transparent to the application.
* Out-of-order can execute and commit transactions in different order on the replica than originally on the primary. This means that the application must be tolerant to seeing updates occur in different order. The application is also responsible for ensuring that there are no conflicts between transactions that are replicated out-of-order. Out-of-order is only used in GTID mode and only\
  when explicitly enabled by the application, using the replication domain that\
  is part of the GTID.

### In-Order Parallel Replication

#### Optimistic Mode of In-Order Parallel Replication

Optimistic mode of in-order parallel replication provides a lot of opportunities for parallel apply on the replica while still preserving exact transaction semantics from the point of view of applications. It is the default mode from [MariaDB 10.5.1](https://app.gitbook.com/s/aEnK0ZXmUbJzqQrTjFyb/community-server/old-releases/mariadb-10-5-series/mariadb-1051-release-notes).

Optimistic mode of in-order parallel replication can be configured by setting the [slave\_parallel\_mode](replication-and-binary-log-system-variables.md) system variable to `optimistic` on the replica.

Any transactional DML (INSERT/UPDATE/DELETE) is allowed to run in parallel, up to the limit of [@@slave\_domain\_parallel\_threads](replication-and-binary-log-system-variables.md). This may cause conflicts on the replica, e.g. if two transactions try to modify the same row. Any such conflict is detected, and the latter of the two transactions is rolled back, allowing the former to proceed. The latter transaction is then re-tried once\
the former has completed.&#x20;

The term "optimistic" is used for this mode, because the server optimistically assumes that few conflicts will occur, and that the extra work spent rolling back and retrying conflicting transactions is justified from the gain from running most transactions in parallel.

There are a few heuristics to try to avoid needless conflicts. If a transaction executed a row lock wait on the primary, it will not be run in parallel on the replica. Transactions can also be marked explicitly as potentially conflicting on the primary, by setting the variable [@@skip\_parallel\_replication](replication-and-binary-log-system-variables.md). More such heuristics may be added in later MariaDB versions. There is a further [--slave-parallel-mode](replication-and-binary-log-system-variables.md) called "aggressive", where these heuristics are disabled, allowing even more transactions to be applied in parallel.

Non-transactional DML and DDL is not safe to optimistically apply in parallel, as it cannot be rolled back in case of conflicts. Thus, in optimistic mode, non-transactional (such as MyISAM) updates are not applied in parallel with earlier events (it is however possible to apply a MyISAM update in parallel\
with a later InnoDB update). DDL statements are not applied in parallel with any other transactions, earlier or later.

The different kind of transactions can be identified in the output of [mariadb-binlog](../../clients-and-utilities/logging-tools/mariadb-binlog/). For example:

```
#150324 13:06:26 server id 1  end_log_pos 6881 	GTID 0-1-42 ddl
...
#150324 13:06:26 server id 1  end_log_pos 7816 	GTID 0-1-47
...
#150324 13:06:26 server id 1  end_log_pos 8177  GTID 0-1-49 trans
/*!100101 SET @@session.skip_parallel_replication=1*//*!*/;
...
#150324 13:06:26 server id 1  end_log_pos 9836 	GTID 0-1-59 trans waited
```

GTID 0-1-42 is marked as being DDL. GTID 0-1-47 is marked as being non-transactional DML, while GTID 0-1-49 is transactional DML (seen on the "trans" keyword). GTID 0-1-49 was additionally run with [@@skip\_parallel\_replication](replication-and-binary-log-system-variables.md) set on the primary. GTID 0-1-59 is transactional DML that had a row lock wait when run on the primary (the "waited" keyword).

#### Aggressive Mode of In-Order Parallel Replication

Aggressive mode of in-order parallel replication is very similar to optimistic mode. The main difference is that the replica does not consider whether transactions conflicted on the primary when deciding whether to apply the transactions in parallel.

Aggressive mode of in-order parallel replication can be configured by setting the [slave\_parallel\_mode](replication-and-binary-log-system-variables.md) system variable to `aggressive` on the replica.

#### Conservative Mode of In-Order Parallel Replication

Conservative mode of in-order parallel replication uses the [group commit](../../server-management/server-monitoring-logs/binary-log/group-commit-for-the-binary-log.md) on the primary to discover potential for parallel apply of events on the replica. If two transactions commit together in a [group commit](../../server-management/server-monitoring-logs/binary-log/group-commit-for-the-binary-log.md) on the primary, they are written into the binlog with the same commit id. Such events are certain to not conflict with each other, and they can be scheduled by the parallel replication to run in different worker threads.

Conservative mode of in-order parallel replication is the default mode until [MariaDB 10.5.0](https://app.gitbook.com/s/aEnK0ZXmUbJzqQrTjFyb/community-server/old-releases/mariadb-10-5-series/mariadb-1050-release-notes), but it can also be configured by setting the [slave\_parallel\_mode](replication-and-binary-log-system-variables.md) system variable to `conservative` on the replica.

Two transactions that were committed separately on the primary can potentially conflict (eg. modify the same row of a table). Thus, the worker that applies the second transaction will not start immediately but wait until the first transaction begins the commit step; at this point it is safe to start the second transaction, as it can no longer disrupt the execution of the first one.

Here is example output from [mariadb-binlog](../../clients-and-utilities/logging-tools/mariadb-binlog/) that shows how GTID events are marked with commit id. The GTID 0-1-47 has no commit id and cannot run in parallel. The GTIDs 0-1-48 and 0-1-49 have the same commit id 630, and can thus replicate in parallel with one another on a replica:

```
#150324 12:54:24 server id 1  end_log_pos 20052 	GTID 0-1-47 trans
...
#150324 12:54:24 server id 1  end_log_pos 20212 	GTID 0-1-48 cid=630 trans
...
#150324 12:54:24 server id 1  end_log_pos 20372 	GTID 0-1-49 cid=630 trans
```

In either case, when the two transactions reach the point where the low-level commit happens and commit order is determined, the two commits are sequenced to happen in the same order as on the primary, so that operation is transparent to applications.

The opportunities for parallel replication on replicas can be highly increased if more transactions are committed in a [group commit](../../server-management/server-monitoring-logs/binary-log/group-commit-for-the-binary-log.md) on the primary. This can be tuned using the [binlog\_commit\_wait\_count](replication-and-binary-log-system-variables.md) and [binlog\_commit\_wait\_usec](replication-and-binary-log-system-variables.md) variables. If for example the application can tolerate up to 50 milliseconds extra delay for transactions on the primary, one can set `binlog_commit_wait_usec=50000` and`binlog_commit_wait_count=20` to get up to 20 transactions at\
a time available for replication in parallel. Care must however be taken to not set `binlog_commit_wait_usec` too high, as this could cause significant slowdown for applications that run a lot of small transactions serially one after the other.

Note that even if there is no parallelism available from the primary [group commit](../../server-management/server-monitoring-logs/binary-log/group-commit-for-the-binary-log.md), there is still an opportunity for speedup from in-order parallel replication, since the actual commit steps of different transactions can run in parallel. This can be particularly effective on a replica with binlog enabled\
([log\_slave\_updates=1](replication-and-binary-log-system-variables.md)), and more so if replica is configured to be crash-safe ([sync\_binlog=1](replication-and-binary-log-system-variables.md) and [innodb\_flush\_log\_at\_trx\_commit=1](../../server-usage/storage-engines/innodb/innodb-system-variables.md#innodb_flush_log_at_trx_commit)), as this makes [group commit](../../server-management/server-monitoring-logs/binary-log/group-commit-for-the-binary-log.md) possible on the replica.

#### Minimal Mode of In-Order Parallel Replication

Minimal mode of in-order parallel replication _onl&#x79;_&#x61;llows the commit step of transactions to be applied in parallel; all other steps are applied serially.

Minimal mode of in-order parallel replication can be configured by setting the [slave\_parallel\_mode](replication-and-binary-log-system-variables.md) system variable to `minimal` on the replica.

### Out-of-Order Parallel Replication

Out-of-order parallel replication happens (only) when using GTID mode, when GTIDs with different replication domains are used. The replication domain is set by the DBA/application using the variable `gtid_domain_id`.

Two transactions having GTIDs with different domain\_id are scheduled to different worker threads by parallel replication and are allowed to execute completely independently from each other. It is the responsibility of the application to only set different domain\_ids for transactions that are truly\
independent, and are guaranteed to not conflict with each other. The application must also be able to work correctly even though the transactions with different domain\_id are seen as committing in different order between the replica and the primary, and between different replicas.

Out-of-order parallel replication can potentially give more performance gain than in-order parallel replication, since the application can explicitly give more opportunities for running transactions in parallel than what the server can determine on its own automatically.

One simple but effective usage is to run long-running statements, such as ALTER TABLE, in a separate replication domain. This allows replication of other transactions to proceed uninterrupted:

```sql
SET SESSION gtid_domain_id=1
ALTER TABLE t ADD INDEX myidx(b)
SET SESSION gtid_domain_id=0
```

Normally, a long-running ALTER TABLE or other query will stall all following transactions, causing the replica to become behind the primary as least as long time as it takes to run the long-running query. By using out-of-order parallel replication by setting the replication domain id, this can be avoided. The\
DBA/application must ensure that no conflicting transactions will be replicated while the ALTER TABLE runs.

Another common opportunity for out-of-order parallel replication comes in connection with multi-source replication. Suppose we have two different primaries M1 and M2, and we are using multi-source replication to have S1 as a replica of both M1 and M2. S1 will apply events received from M1 in parallel with events received from M2. If we now have a third-level replica S2 that replicates from S1 as primary, we want S2 to also be able to apply events that originated on M1 in parallel with events that originated on M2. This can be achieved with out-of-order parallel replication, by setting `gtid_domain_id` different on M1 and M2.

Note that there are no special restrictions on what operations can be replicated in parallel using out-of-order; such operations can be on the same database/schema or even on the same table. The only restriction is that the operations must not conflict, that is they must be able to be applied in any\
order and still end up with the same result.

When using out-of-order parallel replication, the current replica position in the primary's binlog becomes multi-dimensional - each replication domain can have reached a different point in the primary binlog at any one time. The current position can be seen from the variable`gtid_slave_pos`. When the replica is stopped, restarted, or switched to replicate from a different primary using CHANGE MASTER, MariaDB automatically handles restarting each replication domain at the appropriate point in the binlog.

Out-of-order parallel replication is disabled when [--slave-parallel-mode=minimal](replication-and-binary-log-system-variables.md) (or none).

## Checking Worker Thread Status in SHOW PROCESSLIST

The worker threads will be listed as "system user" in [SHOW PROCESSLIST](../../reference/sql-statements/administrative-sql-statements/show/show-processlist.md). Their state will show the query they are currently working on, or it can show one of these:

* "Waiting for work from main SQL threads". This means that the worker thread is idle, no work is available for it at the moment.
* "Waiting for prior transaction to start commit before starting next transaction". This means that the previous batch of transactions that committed together on the primary primary has to complete first. This worker thread is waiting for that to happen before it can start working on the\
  following batch.
* "Waiting for prior transaction to commit". This means that the transaction has been executed by the worker thread. In order to ensure in-order commit, the worker thread is waiting to commit until the previous transaction is ready to commit before it.

## Expected Performance Gain

Here is an article showing up to ten times improvement when using parallel replication: [18435.html](https://kristiannielsen.livejournal.com/18435.html).

## Configuring the Maximum Size of the Parallel Replica Queue

The [slave\_parallel\_max\_queued](replication-and-binary-log-system-variables.md) system variable can be used to configure the maximum size of the parallel replica queue. This system variable is only meaningful when parallel\
replication is configured (i.e. when [slave\_parallel\_threads](replication-and-binary-log-system-variables.md) > `0`).

When parallel replication is used, the [SQL thread](replication-threads.md#slave-sql-thread) will read ahead in the relay logs, queueing events in memory while looking for opportunities for executing events in parallel. The [slave\_parallel\_max\_queued](replication-and-binary-log-system-variables.md) system variable sets a\
limit for how much memory it will use for this.

The configured value of the [slave\_parallel\_max\_queued](replication-and-binary-log-system-variables.md) system variable is actually allocated for each [worker thread](replication-threads.md#worker-threads), so the total allocation is actually equivalent to the following:

[slave\_parallel\_max\_queued](replication-and-binary-log-system-variables.md) \* [slave\_parallel\_threads](replication-and-binary-log-system-variables.md)

If this value is set too high, and the replica is far (eg. gigabytes of binlog)\
behind the primary, then the [SQL thread](replication-threads.md#slave-sql-thread) can quickly read all of that and fill up memory with huge amounts of binlog events faster than the [worker threads](replication-threads.md#worker-threads) can consume them.

On the other hand, if set too low, the [SQL thread](replication-threads.md#slave-sql-thread) might not have sufficient space for queuing enough events to keep the worker threads busy, which could reduce performance. In this case, the [SQL thread](replication-threads.md#slave-sql-thread) will have the [thread state](../optimization-and-tuning/buffers-caches-and-threads/thread-states/) that states `Waiting for room in worker thread event queue`. For example:

```
+----+-------------+-----------+------+---------+--------+-----------------------------------------------+------------------+----------+
| Id | User        | Host      | db   | Command | Time   | State                                         | Info             | Progress |
+----+-------------+-----------+------+---------+--------+-----------------------------------------------+------------------+----------+
|  3 | system user |           | NULL | Connect |    139 | closing tables                                | NULL             |    0.000 |
|  4 | system user |           | NULL | Connect |    139 | Waiting for work from SQL thread              | NULL             |    0.000 |
|  6 | system user |           | NULL | Connect | 264274 | Waiting for master to send event              | NULL             |    0.000 |
| 10 | root        | localhost | NULL | Sleep   |     43 |                                               | NULL             |    0.000 |
| 21 | system user |           | NULL | Connect |     45 | Waiting for room in worker thread event queue | NULL             |    0.000 |
| 54 | root        | localhost | NULL | Query   |      0 | init                                          | SHOW PROCESSLIST |    0.000 |
+----+-------------+-----------+------+---------+--------+-----------------------------------------------+------------------+----------+
```

The [slave\_parallel\_max\_queued](replication-and-binary-log-system-variables.md) system variable does not define a hard limit, since the [binary log](../../server-management/server-monitoring-logs/binary-log/) events that are currently executing always need to be held in-memory. This means that at least two events per [worker thread](replication-threads.md#worker-threads) can always be queued in-memory, regardless of the value of [slave\_parallel\_threads](replication-and-binary-log-system-variables.md).

Usually, the [slave\_parallel\_threads](replication-and-binary-log-system-variables.md) system variable should be set large enough that the [SQL thread](replication-threads.md#slave-sql-thread) is able to read far enough ahead in the [binary log](../../server-management/server-monitoring-logs/binary-log/) to exploit all possible parallelism. In normal operation, the replica will hopefully not be too far behind, so there will not be a need to queue much data in-memory. The [slave\_parallel\_max\_queued](replication-and-binary-log-system-variables.md) system variable could be set fairly high (e.g. a few hundred kilobytes) to not limit throughput. It should just be set low enough that total allocation of the parallel replica queue will not cause the server to run out of memory.

## Configuration Variable slave\_domain\_parallel\_threads

The pool of replication worker threads is shared among all multi-source primary connections, and among all replication domains that can replicate in parallel using out-of-order.

If one primary connection or replication domain is currently processing a long-running query, it is possible that it will allocate all the worker threads in the pool, only to have them wait for the long-running query to complete, stalling any other primary connection or replication domain, which\
will have to wait for a worker thread to become free.

This can be avoided by setting [slave\_domain\_parallel\_threads](replication-and-binary-log-system-variables.md) to a number that is lower than `slave_parallel_threads`. When set different from zero, each replication domain in one primary connection can reserve at most that many worker threads at any one time, leaving the rest (up to the value of [slave\_parallel\_threads](replication-and-binary-log-system-variables.md)) free for other primary connections or replication domains to use in parallel.

The `slave_domain_parallel_threads` variable is dynamic and can be changed without restarting the server; all replicas must be stopped while changing it, though.

## Implementation Details

The implementation is described in [MDEV-4506](https://jira.mariadb.org/browse/MDEV-4506).

## See Also

* [Better Parallel Replication for MariaDB and MySQL](https://mariadb.com/blog/better-parallel-replication-mariadb-and-mysql) (MariaDB.com blog)
* [Evaluating MariaDB & MySQL Parallel Replication Part 2: Slave Group Commit](https://mariadb.com/blog/evaluating-mariadb-mysql-parallel-replication-part-2-slave-group-commit) (MariaDB.com blog)

<sub>_This page is licensed: CC BY-SA / Gnu FDL_</sub>

{% @marketo/form formId="4316" %}
