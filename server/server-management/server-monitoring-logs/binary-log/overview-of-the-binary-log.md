---
description: >-
  Introduction to the purpose and structure of the binary log, explaining how it
  records data changes (DML) and structure changes (DDL) for replication and
  recovery.
---

# Overview of the Binary Log

The binary log contains a record of all changes to the databases, both data and structure, as well as how long each statement took to execute. It consists of a set of binary log files and an index.

This means that statements such as [CREATE](../../../reference/sql-statements/data-definition/create/), [ALTER](../../../reference/sql-statements/data-definition/alter/), [INSERT](../../../reference/sql-statements/data-manipulation/inserting-loading-data/insert.md), [UPDATE](../../../reference/sql-statements/data-manipulation/changing-deleting-data/update.md) and [DELETE](../../../reference/sql-statements/data-manipulation/changing-deleting-data/delete.md) are logged, whereas statements that have no effect on the data, such as `SELECT` and `SHOW`, are not be logged. If you want to log these, too (at a cost in performance), use the [general query log](../general-query-log.md).

If a statement may potentially have an effect, but doesn't, such as an `UPDATE` or `DELETE` that returns no rows, it is still logged (this applies to the default statement-based logging, not to row-based logging - see [Binary Log Formats](binary-log-formats.md)).

The purpose of the binary log is:

* To enable [replication](../../../ha-and-performance/standard-replication/), where data is sent from one or more primary servers to one or more replica servers based on the contents of the binary log.
* To assist in backup operations.

A MariaDB server with the binary log enabled runs slightly more slowly.

It is important to protect the binary log, as it may contain sensitive information, including passwords.

Binary logs are stored in a binary, not plain text, format, and so are not readable with a regular editor. However, MariaDB includes [mariadb-binlog](../../../clients-and-utilities/logging-tools/mariadb-binlog/), a command-line tool for plain-text processing of binary logs.

{% if  %}
{% hint style="info" %}
From MariaDB 12.3, InnoDB-based binary logs can be used. (This is configurable, and not the default.)

If configured, binary logs are stored in InnoDB tablespaces, rather than binary files. This removes the need of protecting binary logs separately, since they'll "inherit" the same protection as other MariaDB database tables. Also, any other information about log **files** doesn't apply – for example, you cannot specify a storage location for binary logs stored in an InnoDB tablespace.

InnoDB-based binary logs are enabled by setting `binlog_storage_engine=innodb` in the server configuration. See [InnoDB-Based Binary Log](../../../ha-and-performance/standard-replication/innodb-based-binary-log.md) for more information.
{% endhint %}
{% endif %}

## Binary Log Checkpoints

When the binary log is enabled, it acts as the transaction coordinator for two-phase commit between the binary log and transactional storage engines such as InnoDB. Each such transaction gets an internal XID, which is written to the binary log when the transaction commits. This applies to ordinary transactions, not only to XA transactions started with [XA START](../../../reference/sql-statements/transactions/xa-transactions.md).

If the server crashes, InnoDB may hold transactions that are prepared but not yet committed. During crash recovery, the server scans the binary log for the XIDs of those transactions: a prepared transaction whose XID is in the binary log is committed, and one whose XID is missing is rolled back.

A binary log checkpoint records the oldest binary log file that crash recovery still needs to scan. A file is no longer needed once the storage engines have durably committed, in their own logs, all transactions written to it. Crash recovery starts from the checkpointed file instead of scanning every binary log file.

The server records checkpoints as `Binlog_checkpoint` events:

* Every new binary log file starts with a `Binlog_checkpoint` event, written after the `Format_desc` and `Gtid_list` events.
* After a rotation, the server asks the storage engines to make their commits durable in the background. When all transactions in the oldest still-needed file are durable, the server writes a new `Binlog_checkpoint` event naming the next file still needed. A single binary log file can therefore contain more than one checkpoint event.
* During crash recovery, the server uses the last `Binlog_checkpoint` event in the most recent binary log file and scans from the file it names onward.

A binary log file that crash recovery may still need cannot be purged. [PURGE BINARY LOGS](../../../reference/sql-statements/administrative-sql-statements/purge-binary-logs.md) stops at such a file and returns a note, for example:

```
Binary log 'master-bin.000003' is not purged because it may be needed for crash recovery (XID)
```

Automatic purging stops at the same point and writes the message to the error log.

`Binlog_checkpoint` events are used only for crash recovery on the server that wrote them; replication does not use them. They appear in [SHOW BINLOG EVENTS](../../../reference/sql-statements/administrative-sql-statements/show/show-binlog-events.md) output:

```
+-------------------------------+-----+-------------------+-----------+-------------+-------------------------------+
| Log_name                      | Pos | Event_type        | Server_id | End_log_pos | Info                          |
+-------------------------------+-----+-------------------+-----------+-------------+-------------------------------+
| mysql_sandbox10019-bin.000002 | 273 | Binlog_checkpoint |         1 |         325 | mysql_sandbox10019-bin.000002 |
+-------------------------------+-----+-------------------+-----------+-------------+-------------------------------+
```

The `Info` column shows the file that crash recovery would start from.

In [mariadb-binlog](../../../clients-and-utilities/logging-tools/mariadb-binlog/) output, a checkpoint event appears as a line ending in `Binlog checkpoint <file_name>`.

{% hint style="info" %}
Binary log checkpoints apply to file-based binary logs. They are not written when the binary log is stored in InnoDB (`binlog_storage_engine=innodb`, available from MariaDB 12.3). See [InnoDB-Based Binary Log](../../../ha-and-performance/standard-replication/innodb-based-binary-log.md).
{% endhint %}

## See Also

* [Group Commit for the Binary Log](group-commit-for-the-binary-log.md)
* [BINLOG\_CHECKPOINT\_EVENT](../../../reference/clientserver-protocol/replication-protocol/binlog_checkpoint_event.md) (replication protocol)

<sub>_This page is licensed: CC BY-SA / Gnu FDL_</sub>

{% @marketo/form formId="4316" %}
