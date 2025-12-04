---
description: MyRocks storage engine transactions with consistent snapshot.
---

# MyRocks START TRANSACTION WITH CONSISTENT SNAPSHOT

FB/MySQL has added new syntax:

```sql
START TRANSACTION WITH CONSISTENT ROCKSDB|INNODB SNAPSHOT;
```

The statement returns the binlog coordinates pointing at the snapshot.

MariaDB (and Percona Server) support extension to the regular

```sql
START TRANSACTION WITH CONSISTENT SNAPSHOT;
```

syntax as documented in [Enhancements for START TRANSACTION WITH CONSISTENT SNAPSHOT](../../../ha-and-performance/standard-replication/enhancements-for-start-transaction-with-consistent-snapshot.md).

After issuing the statement, one can examine the [binlog\_snapshot\_file](../../../ha-and-performance/standard-replication/replication-and-binary-log-status-variables.md#binlog_snapshot_file) and [binlog\_snapshot\_position](../../../ha-and-performance/standard-replication/replication-and-binary-log-status-variables.md#binlog_snapshot_position) status variables to see the binlog position that corresponds to the snapshot.

## See Also

* [START TRANSACTION](../../../reference/sql-statements/transactions/start-transaction.md)
* [Enhancements for START TRANSACTION WITH CONSISTENT SNAPSHOT](../../../ha-and-performance/standard-replication/enhancements-for-start-transaction-with-consistent-snapshot.md)

<sub>_This page is licensed: CC BY-SA / Gnu FDL_</sub>

{% @marketo/form formId="4316" %}
