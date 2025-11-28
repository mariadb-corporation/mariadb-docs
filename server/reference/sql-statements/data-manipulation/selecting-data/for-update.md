---
description: >-
  Lock rows for write operations. This clause prevents other transactions from
  modifying or reading the selected rows until the current transaction ends.
---

# FOR UPDATE

InnoDB supports row-level locking. Selected rows can be locked using [LOCK IN SHARE MODE](lock-in-share-mode.md) or FOR UPDATE. In both cases, a lock is acquired on the rows read by the query, and it will be released when the current transaction is committed.

The `FOR UPDATE` clause of [SELECT](select.md) applies only when [autocommit](../../../../ha-and-performance/optimization-and-tuning/system-variables/server-system-variables.md#autocommit) is set to 0 or the `SELECT` is enclosed in a transaction. A lock is acquired on the rows, and other transactions are prevented from writing the rows, acquire locks, and from reading them (unless their isolation level is [READ UNCOMMITTED](../../transactions/set-transaction.md)).

If `autocommit` is set to 1, the [LOCK IN SHARE MODE](lock-in-share-mode.md) and `FOR UPDATE` clauses have no effect in InnoDB. For non-transactional storage engines like MyISAM and ARIA, a table level lock will be taken even if autocommit is set to 1.

If the isolation level is set to [SERIALIZABLE](../../transactions/set-transaction.md), all plain `SELECT` statements are converted to `SELECT ... LOCK IN SHARE MODE`.

## Example

```sql
SELECT * FROM trans WHERE period=2001 FOR UPDATE;
```

## See Also

* [SELECT](select.md)
* [LOCK IN SHARE MODE](lock-in-share-mode.md)
* [InnoDB Lock Modes](../../../../server-usage/storage-engines/innodb/innodb-lock-modes.md)

<sub>_This page is licensed: CC BY-SA / Gnu FDL_</sub>

{% @marketo/form formId="4316" %}
