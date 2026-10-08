---
description: >-
  DROP SEQUENCE removes one or more sequence objects.
---

# DROP SEQUENCE

## Syntax

```bnf
DROP [TEMPORARY] SEQUENCE [IF EXISTS] [/*COMMENT TO SAVE*/]
    sequence_name [, sequence_name] ...
```

## Description

`DROP SEQUENCE` removes one or more [sequences](./) created with [CREATE SEQUENCE](create-sequence.md). You must have the `DROP` privilege for each sequence. MariaDB returns an error indicating by name which non-existing tables it was unable to drop, but it also drops all of the tables in the list that do exist.

Important: When a table is dropped, user privileges on the table are not automatically dropped. See [GRANT](../../sql-statements/account-management-sql-statements/grant.md).

If another connection is using the sequence, a metadata lock is active, and this statement will wait until the lock is released. This is also true for non-transactional tables.

For each referenced sequence, DROP SEQUENCE drops a temporary sequence with that name, if it exists. If it does not exist, and the `TEMPORARY` keyword is not used, it drops a non-temporary sequence with the same name, if it exists. The `TEMPORARY` keyword ensures that a non-temporary sequence will not accidentally be dropped.

Use `IF EXISTS` to prevent an error from occurring for sequences that do not exist. A `NOTE` is generated for each non-existent sequence when using `IF EXISTS`. See [SHOW WARNINGS](../../sql-statements/administrative-sql-statements/show/show-warnings.md).

`DROP SEQUENCE` requires the [DROP privilege](../../sql-statements/account-management-sql-statements/grant.md).

## Notes

`DROP SEQUENCE` only removes sequences, not tables. However, [DROP TABLE](../../sql-statements/data-definition/drop/drop-table.md) can remove both sequences and tables.

## See Also

* [Sequence Overview](sequence-overview.md)
* [CREATE SEQUENCE](create-sequence.md)
* [ALTER SEQUENCE](alter-sequence.md)
* [DROP TABLE](../../sql-statements/data-definition/drop/drop-table.md)
* [Information Schema SEQUENCES Table](../../system-tables/information-schema/information-schema-tables/information-schema-sequences-table.md)

<sub>_This page is licensed: CC BY-SA / Gnu FDL_</sub>

{% @marketo/form formId="4316" %}
