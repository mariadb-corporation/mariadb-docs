---
description: >-
  Pause query execution. This function pauses the script for a specified number
  of seconds, returning 0 if successful or 1 if interrupted.
---

# SLEEP

## Syntax

```sql
SLEEP(duration)
```

## Description

Sleeps (pauses) for the number of seconds given by the duration argument, then returns `0`. If `SLEEP()` is interrupted, it returns `1`. The duration may have a fractional part given in microseconds.

Statements using the SLEEP() function are not [safe for statement-based replication](../../../../ha-and-performance/standard-replication/unsafe-statements-for-statement-based-replication.md).

## Example

```sql
SELECT SLEEP(5.5);
+------------+
| SLEEP(5.5) |
+------------+
|          0 |
+------------+
1 row in set (5.50 sec)
```

<sub>_This page is licensed: GPLv2, originally from_</sub> [<sub>_fill\_help\_tables.sql_</sub>](https://github.com/MariaDB/server/blob/main/scripts/fill_help_tables.sql)

{% @marketo/form formId="4316" %}
