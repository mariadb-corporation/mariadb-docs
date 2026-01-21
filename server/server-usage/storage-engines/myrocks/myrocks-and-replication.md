---
description: >-
  This page details how MyRocks integrates with MariaDB replication,
  specifically addressing limitations with statement-based replication and lack
  of Gap Lock support.
---

# MyRocks and Replication

Details about how MyRocks works with [replication](../../../ha-and-performance/standard-replication/).

## MyRocks and Statement-Based Replication

[Statement-based](../../../server-management/server-monitoring-logs/binary-log/binary-log-formats.md#statement-based) replication (SBR) works as follows: SQL statements are executed on the master (possibly concurrently). They are written into the binlog (this fixes their ordering, "a serialization"). The slave then reads the binlog and executes the statements in their binlog order.

In order to prevent data drift, serial execution of statements on the slave must have the same effect as concurrent execution of these statements on the master. In other words, transaction isolation on the master must be close to `SERIALIZABLE` transaction isolation level (This is not a strict mathematical proof but shows the idea).

InnoDB achieves this by (almost) supporting `SERIALIZABLE` transactional isolation level. It does so by supporting "Gap Locks". MyRocks doesn't support `SERIALIZABLE` isolation, and it doesn't support gap locks.

Because of that, generally one cannot use MyRocks and statement-based replication.

Updating a MyRocks table while having SBR on, will result in an error as follow:

```sql
ERROR 4056 (HY000): Can't execute updates on master with binlog_format != ROW.
```

### Can One Still Use SBR with MyRocks?

Yes. In many cases, database applications run a restricted set of SQL statements, and it's possible to prove that lack of Gap Lock support is not a problem and data skew will not occur.

In that case, one can set `@@rocksdb_unsafe_for_binlog=1` and MyRocks will work with SBR. The user is however responsible for making sure their queries are not causing a data skew.

## Differences From Upstream MyRocks

MyRocks upstream (that is, Facebook's MySQL branch) has a number of unique replication enhancements. These are available in upstream's version of MyRocks but not in MariaDB's version of MyRocks.

* Read-Free Replication (see [Read-Free-Replication](https://github.com/facebook/mysql-5.6/wiki/Read-Free-Replication)) TODO
* `<<unique_check_lag_threshold>>`. This is FB/MySQL-5.6 feature where unique checks are disabled if replication lag exceeds a certain threshold.
* `<<slave_gtid_info=OPTIMIZED>>`. This is said to be:

```
<<quote>>
"Whether SQL threads update mysql.slave_gtid_info table. If this value "
"is OPTIMIZED, updating the table is done inside storage engines to "
"avoid MySQL layer's performance overhead",
<</quote>>
```

<sub>_This page is licensed: CC BY-SA / Gnu FDL_</sub>

{% @marketo/form formId="4316" %}
