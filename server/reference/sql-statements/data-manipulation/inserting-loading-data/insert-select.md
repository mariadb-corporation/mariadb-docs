---
description: >-
  Copy data between tables. This statement inserts the result set of a SELECT
  query directly into a target table, enabling efficient bulk data transfer.
---

# INSERT SELECT

## Syntax

```sql
INSERT [LOW_PRIORITY | HIGH_PRIORITY] [IGNORE]
    [INTO] tbl_name [(col_name,...)]
    SELECT ...
    [ ON DUPLICATE KEY UPDATE col_name=expr, ... ]
```

## Description

With `INSERT ... SELECT`, you can quickly insert many rows into a table from one or more other tables. For example:

```sql
INSERT INTO tbl_temp2 (fld_id)
  SELECT tbl_temp1.fld_order_id
  FROM tbl_temp1 WHERE tbl_temp1.fld_order_id > 100;
```

`tbl_name` can also be specified in the form `db_name`.`tbl_name` (see [Identifier Qualifiers](../../../sql-structure/sql-language-structure/identifier-qualifiers.md)). This allows to copy rows between different databases.

If the new table has a primary key or UNIQUE indexes, you can use [IGNORE](ignore.md) to handle duplicate key errors during the query. The newer values will not be inserted if an identical value already exists.

[REPLACE](../changing-deleting-data/replace.md) can be used instead of `INSERT` to prevent duplicates on `UNIQUE` indexes by deleting old values. In that case, `ON DUPLICATE KEY UPDATE` cannot be used.

`INSERT ... SELECT` works for tables which already exist. To create a table for a given resultset, you can use [CREATE TABLE ... SELECT](../../data-definition/create/create-table.md).

## See Also

* [INSERT](insert.md)
* [INSERT DELAYED](insert-delayed.md)
* [HIGH\_PRIORITY and LOW\_PRIORITY](../changing-deleting-data/high_priority-and-low_priority.md)
* [Concurrent Inserts](concurrent-inserts.md)
* [INSERT - Default & Duplicate Values](insert-default-duplicate-values.md)
* [INSERT IGNORE](insert-ignore.md)
* [INSERT ON DUPLICATE KEY UPDATE](insert-on-duplicate-key-update.md)

<sub>_This page is licensed: GPLv2, originally from_</sub> [<sub>_fill\_help\_tables.sql_</sub>](https://github.com/MariaDB/server/blob/main/scripts/fill_help_tables.sql)

{% @marketo/form formId="4316" %}
