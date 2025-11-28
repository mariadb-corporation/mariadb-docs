---
description: >-
  The mysql.gtid_slave_pos table tracks the Global Transaction ID (GTID) of the
  last applied transaction on a replica to ensure replication consistency.
---

# mysql.gtid\_slave\_pos Table

The `mysql.gtid_slave_pos` table is used in [replication](../../../server-usage/storage-engines/myrocks/myrocks-and-replication.md) by replica servers to keep track of their current position (the [global transaction ID](../../../ha-and-performance/standard-replication/gtid.md) of the last transaction applied). Using the table allows the replica to maintain a consistent value for the [gtid\_slave\_pos](../../../ha-and-performance/standard-replication/gtid.md) system variable across server restarts. See [Global Transaction ID](../../../ha-and-performance/standard-replication/gtid.md).

You should never attempt to modify the table directly. If you do need to change the global `gtid_slave_pos` value, use `SET GLOBAL gtid_slave_pos = ...` instead.

The table is updated with the new position as part of each transaction committed during replication. This makes it preferable that the table is using the same storage engine as the tables otherwise being modified in the transaction, since otherwise a multi-engine transaction is needed that can reduce performance.

Multiple versions of this table are supported, each using a different storage engine. This is selected with the [gtid\_pos\_auto\_engines option](../../../ha-and-performance/standard-replication/gtid.md), by giving a comma-separated list of engine names. The server will then on-demand create an extra version of the table using the appropriate storage engine, and select the table version using the same engine as the rest of the transaction, avoiding multi-engine transactions.

When `gtid_pos_auto_engines=innodb,rocksdb` is set, the tables `mysql.gtid_slave_pos_InnoDB` and `mysql.gtid_slave_pos_RocksDB` are created and used, if needed. If there is no match to the storage engine, the default `mysql.gtid_slave_pos` table is used; this also happens if non-transactional updates (like MyISAM) are replicated, since there is then no active transaction at the time of the `mysql.gtid_slave_pos` table update.

The default `mysql.gtid_slave_pos` table is initially created using the default storage engine set for the server (which itself defaults to InnoDB). If the application load is primarily non-transactional MyISAM or Aria tables, it can be beneficial to change the storage engine to avoid including\
an InnoDB update with every operation:

```sql
ALTER TABLE mysql.gtid_slave_pos ENGINE=MyISAM;
```

The `mysql.gtid_slave_pos` table should not be changed manually in any other way. It is preferable to use the `gtid_pos_auto_engines` server variable to get the GTID position updates to use the TokuDB or\
RocksDB storage engine.

Note that, for scalability reasons, the automatic creation of a new`mysql.gtid_slave_posXXX` table happens asynchronously when the first transaction with the new storage engine is committed. So the very first few transactions will update the old version of the table, until the new version is created and available.

The table `mysql.gtid_slave_pos` contains the following fields:

| Field      | Type                | Null | Key | Default | Description                                                                                                                                                                                                              |
| ---------- | ------------------- | ---- | --- | ------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ |
| domain\_id | int(10) unsigned    | NO   | PRI | NULL    | Domain id (see [Global Transaction ID domain ID](../../../ha-and-performance/standard-replication/gtid.md).                                                                                                              |
| sub\_id    | bigint(20) unsigned | NO   | PRI | NULL    | This field enables multiple parallel transactions within same domain\_id to update this table without contention. At any instant, the replication state corresponds to records with largest sub\_id for each domain\_id. |
| server\_id | int(10) unsigned    | NO   |     | NULL    | [Server id](../../../ha-and-performance/standard-replication/gtid.md).                                                                                                                                                   |
| seq\_no    | bigint(20) unsigned | NO   |     | NULL    | Sequence number, an integer that is monotonically increasing for each new event group logged into the binlog.                                                                                                            |

Some status variables are available to monitor the use of the different `gtid_slave_pos` table versions:

[Transactions\_gtid\_foreign\_engine](../../../ha-and-performance/standard-replication/replication-and-binary-log-status-variables.md#transactions_gtid_foreign_engine)

Number of replicated transactions where the update of the `gtid_slave_pos` table had to choose a storage engine that did not otherwise participate in the transaction. This can indicate that setting `gtid_pos_auto_engines` might be useful.

[Rpl\_transactions\_multi\_engine](../../../ha-and-performance/standard-replication/replication-and-binary-log-status-variables.md#rpl_transactions_multi_engine)

Number of replicated transactions that involved changes in multiple (transactional) storage engines, before considering the update of`gtid_slave_pos`. These are transactions that were already cross-engine, independent of the GTID position update introduced by replication

[Transactions\_multi\_engine](../../../ha-and-performance/standard-replication/replication-and-binary-log-status-variables.md#transactions_multi_engine)

Number of transactions that changed data in multiple (transactional) storage engines. If this is significantly larger than `Rpl_transactions_multi_engine`, it indicates that setting `gtid_pos_auto_engines` could reduce the need for cross-engine transactions.

<sub>_This page is licensed: CC BY-SA / Gnu FDL_</sub>

{% @marketo/form formId="4316" %}
