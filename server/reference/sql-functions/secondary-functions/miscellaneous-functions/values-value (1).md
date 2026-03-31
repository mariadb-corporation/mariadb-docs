---
description: >-
  Access values in ON DUPLICATE KEY UPDATE. This function retrieves the value
  that would have been inserted into a column if no key conflict occurred.
---

# OLD\_VALUE

{% hint style="info" %}
This function is available from MariaDB 13.0.
{% endhint %}

## Syntax

```sql
OLD_VALUE(val)
```

## Description

In the `RETURNING` clause of an [`UPDATE`](../../../sql-statements/data-manipulation/changing-deleting-data/update.md) statement, `OLD_VALUE()` returns the value before the update. The function is meaningful only in this context.

## Examples

```sql
UPDATE t SET a=a+1 RETURNING OLD_VALUE(a) AS old, a as new;
+------+------+
| old  | new  |
+------+------+
|    1 |    2 |
+------+------+
```

<sub>_This page is licensed: GPLv2, originally from_</sub> [<sub>_fill\_help\_tables.sql_</sub>](https://github.com/MariaDB/server/blob/main/scripts/fill_help_tables.sql)

{% @marketo/form formId="4316" %}
