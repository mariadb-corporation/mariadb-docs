---
description: >-
  Release explicit table locks. This statement releases all locks acquired by
  the current session with LOCK TABLES.
---

# UNLOCK TABLES

## Syntax

```sql
UNLOCK TABLES
```

## Description

`UNLOCK TABLES` explicitly releases any table locks held by the current session. See [LOCK TABLES](lock-tables.md) for more information.

In addition to releasing table locks acquired by the [LOCK TABLES](lock-tables.md) statement, the `UNLOCK TABLES` statement also releases the global read lock acquired by the `FLUSH TABLES WITH READ LOCK` statement. The `FLUSH TABLES WITH READ LOCK` statement is very useful for performing backups. See [FLUSH](../administrative-sql-statements/flush-commands/flush.md) for more information about `FLUSH TABLES WITH READ LOCK`.

<sub>_This page is licensed: CC BY-SA / Gnu FDL_</sub>

{% @marketo/form formId="4316" %}
