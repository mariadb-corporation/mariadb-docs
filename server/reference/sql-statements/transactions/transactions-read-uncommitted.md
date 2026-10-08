---
description: >-
  Set the transaction isolation level to READ UNCOMMITTED. This lowest isolation
  level allows dirty reads, where a transaction can see uncommitted changes.
---

# READ UNCOMMITTED

`READ UNCOMMITTED` is one of the transaction isolation levels. `SELECT` statements are performed in a non-locking fashion, but a possible earlier version of a row might be used.

See [Isolation Levels](set-transaction.md#isolation-levels) for details.

<sub>_This page is licensed: CC BY-SA / Gnu FDL_</sub>

{% @marketo/form formId="4316" %}
