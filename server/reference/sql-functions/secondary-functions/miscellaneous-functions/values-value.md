---
description: >-
  Access values in ON DUPLICATE KEY UPDATE. This function retrieves the value
  that would have been inserted into a column if no key conflict occurred.
---

# VALUES / VALUE

## Syntax

```sql
VALUE(col_name)
```

## Description

In an [INSERT ... ON DUPLICATE KEY UPDATE](../../../sql-statements/data-manipulation/inserting-loading-data/insert-on-duplicate-key-update.md) statement, you can use the `VALUES(col_name)` function in the [UPDATE](../../../sql-statements/data-manipulation/changing-deleting-data/update.md) clause to refer to column values from the [INSERT](../../../sql-statements/data-manipulation/inserting-loading-data/insert.md) portion of the statement. In other words, `VALUES(col_name)` in the `UPDATE` clause refers to the value of col\_name that would be inserted, had no duplicate-key conflict occurred. This function is especially useful in multiple-row inserts.

The `VALUES()` function is meaningful only in `INSERT ... ON DUPLICATE KEY UPDATE` statements and returns `NULL` otherwise.

This function was renamed to `VALUE()`, because it's incompatible with the standard Table Value Constructors syntax.

The `VALUES()` function can still be used but only in `INSERT ... ON DUPLICATE KEY UPDATE` statements; it's a syntax error otherwise.

## Examples

```sql
INSERT INTO t (a,b,c) VALUES (1,2,3),(4,5,6)
    ON DUPLICATE KEY UPDATE c=VALUE(a)+VALUE(b);
```

<sub>_This page is licensed: GPLv2, originally from_</sub> [<sub>_fill\_help\_tables.sql_</sub>](https://github.com/MariaDB/server/blob/main/scripts/fill_help_tables.sql)

{% @marketo/form formId="4316" %}
