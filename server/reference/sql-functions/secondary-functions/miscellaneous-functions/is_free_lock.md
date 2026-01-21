---
description: >-
  Check if a named lock is free. This function returns 1 if the specified lock
  is available (not currently held), and 0 if it is in use.
---

# IS\_FREE\_LOCK

## Syntax

```sql
IS_FREE_LOCK(str)
```

## Description

Checks whether the lock named `str` is free to use (that is, not locked). Returns `1` if the lock is free (no one is using the lock),`0` if the lock is in use, and `NULL` if an error occurs (such as an incorrect argument, like an empty string or `NULL`). `str` is case insensitive.

If the [metadata\_lock\_info](../../../plugins/other-plugins/metadata-lock-info-plugin.md) plugin is installed, the [Information Schema](../../../system-tables/information-schema/) [metadata\_lock\_info](../../../system-tables/information-schema/information-schema-tables/information-schema-metadata_lock_info-table.md) table contains information about locks of this kind (as well as [metadata locks](../../../sql-statements/transactions/metadata-locking.md)).

Statements using the `IS_FREE_LOCK` function are [not safe for statement-based replication](../../../../ha-and-performance/standard-replication/unsafe-statements-for-statement-based-replication.md).

## See Also

* [GET\_LOCK](get_lock.md)
* [RELEASE\_LOCK](release_lock.md)
* [IS\_USED\_LOCK](is_used_lock.md)
* [RELEASE\_ALL\_LOCKS](release_all_locks.md)

<sub>_This page is licensed: GPLv2, originally from_</sub> [<sub>_fill\_help\_tables.sql_</sub>](https://github.com/MariaDB/server/blob/main/scripts/fill_help_tables.sql)

{% @marketo/form formId="4316" %}
