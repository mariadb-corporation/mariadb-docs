---
description: >-
  Execute expressions without returning a result set. This statement runs
  functions or expressions, often used for side effects like releasing locks.
---

# DO

## Syntax

```sql
DO expr [, expr] ...
```

## Description

`DO` executes the expressions but does not return any results. In most respects, `DO` is shorthand for`SELECT expr, ...,` but has the advantage that it is slightly faster when you do not care about the result.

`DO` is useful primarily with functions that have side effects, such as [RELEASE\_LOCK()](../../sql-functions/secondary-functions/miscellaneous-functions/release_lock.md).

<sub>_This page is licensed: GPLv2, originally from_</sub> [<sub>_fill\_help\_tables.sql_</sub>](https://github.com/MariaDB/server/blob/main/scripts/fill_help_tables.sql)

{% @marketo/form formId="4316" %}
