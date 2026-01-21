---
description: >-
  Set the transaction isolation level to SERIALIZABLE. This highest level
  ensures total isolation by converting plain SELECTs to locking reads.
---

# SERIALIZABLE

`SERIALIZABLE` is one of the transaction isolation levels. Similar to `REPEATABLE READ`, but InnoDB implicitly converts all plain `SELECT` statements to `SELECT ... LOCK IN SHARE MODE` if autocommit is disabled.

See [Isolation Levels](set-transaction.md#isolation-levels) for details.

<sub>_This page is licensed: CC BY-SA / Gnu FDL_</sub>

{% @marketo/form formId="4316" %}
