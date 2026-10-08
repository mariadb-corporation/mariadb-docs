---
description: >-
  Read rows with a shared lock. This clause ensures rows remain unchanged by
  other transactions while allowing other sessions to read them.
---

# LOCK IN SHARE MODE

InnoDB supports row-level locking. Selected rows can be locked using `LOCK IN SHARE MODE` or [FOR UPDATE](for-update.md). In both cases, a lock is acquired on the rows read by the query, and it will be released when the current transaction is committed.

When `LOCK IN SHARE MODE` is specified in a [SELECT](select.md) statement, MariaDB will wait until all transactions that have modified the rows are committed. Then, a read lock is acquired. All transactions can read the rows, but if they want to modify them, they have to wait until your transaction is committed.

InnoDB locks index records rather than logical rows. If a `SELECT` is satisfied by a secondary index (a covering index read), it just locks that index. Instead, the primary key records will be locked if a concurrent `UPDATE` modifies columns outside of that index. These locks do not overlap under `READ COMMITTED` isolation level, so the update can proceed. To ensure a block is used, the `SELECT` query must reference columns from the primary index.

For further information and an example, see [InnoDB Lock Modes](../../../../server-usage/storage-engines/innodb/innodb-lock-modes.md).

If [autocommit](../../../../ha-and-performance/optimization-and-tuning/system-variables/server-system-variables.md#autocommit) is set to 1 (the default), the LOCK IN SHARE MODE and [FOR UPDATE](for-update.md) clauses have no effect in InnoDB. For non-transactional storage engines like MyISAM and ARIA, a table level lock will be taken even if autocommit is set to 1.

## See Also

* [SELECT](select.md)
* [FOR UPDATE](for-update.md)
* [InnoDB Lock Modes](../../../../server-usage/storage-engines/innodb/innodb-lock-modes.md)

<sub>_This page is licensed: CC BY-SA / Gnu FDL_</sub>

{% @marketo/form formId="4316" %}
