---
description: >-
  Handle default and duplicate values during insertion. Learn how MariaDB
  manages missing columns and how to resolve duplicate key conflicts using
  various strategies.
---

# INSERT - Default & Duplicate Values

## Default Values

If the [SQL\_MODE](../../../../server-management/variables-and-modes/sql_mode.md) contains `STRICT_TRANS_TABLES` and you are [inserting](insert.md) into a transactional table (like InnoDB), or if the SQL\_MODE contains `STRICT_ALL_TABLES`, all `NOT NULL` columns which do not have a `DEFAULT` value (and are not [AUTO\_INCREMENT](../../../data-types/auto_increment.md)) must be explicitly referenced in `INSERT` statements. If not, an error like this is produced:

```
ERROR 1364 (HY000): Field 'col' doesn't have a default value
```

In all other cases, if a `NOT NULL` column without a `DEFAULT` value is not referenced, an empty value will be inserted (for example, 0 for `INTEGER` columns and '' for `CHAR` columns). See [NULL Values in MariaDB:Inserting](../../../data-types/null-values.md) for examples.

If a `NOT NULL` column having a `DEFAULT` value is not referenced, `NULL` will be inserted.

If a `NULL` column having a `DEFAULT` value is not referenced, its default value will be inserted. It is also possible to explicitly assign the default value using the `DEFAULT` keyword or the [DEFAULT()](../../../sql-functions/secondary-functions/information-functions/default.md) function.

If the `DEFAULT` keyword is used but the column does not have a `DEFAULT` value, an error like this is produced:

```
ERROR 1364 (HY000): Field 'col' doesn't have a default value
```

## Duplicate Values

By default, if you try to insert a duplicate row and there is a `UNIQUE` index, `INSERT` stops and an error like this is produced:

```
ERROR 1062 (23000): Duplicate entry 'dup_value' for key 'col'
```

To handle duplicates you can use the [IGNORE](ignore.md) clause, [INSERT ON DUPLICATE KEY UPDATE](insert-on-duplicate-key-update.md) or the [REPLACE](../changing-deleting-data/replace.md) statement. Note that the IGNORE and DELAYED options are ignored when you use [ON DUPLICATE KEY UPDATE](insert-on-duplicate-key-update.md).

## See Also

* [INSERT](insert.md)
* [INSERT DELAYED](insert-delayed.md)
* [INSERT SELECT](insert-select.md)
* [HIGH\_PRIORITY and LOW\_PRIORITY](../changing-deleting-data/high_priority-and-low_priority.md)
* [Concurrent Inserts](concurrent-inserts.md)
* [INSERT IGNORE](insert-ignore.md)
* [INSERT ON DUPLICATE KEY UPDATE](insert-on-duplicate-key-update.md)

<sub>_This page is licensed: CC BY-SA / Gnu FDL_</sub>

{% @marketo/form formId="4316" %}
