---
description: >-
  Bitemporal tables combine system-versioning and application-time periods,
  versioning data at both levels.
---

# Bitemporal Tables

Bitemporal tables are tables that use versioning both at the [system](system-versioned-tables.md) and [application-time period](application-time-periods.md) levels.

## Using Bitemporal Tables

To create a bitemporal table, use:

```sql
CREATE TABLE test.t3 (
   date_1 DATE,
   date_2 DATE,
   row_start TIMESTAMP(6) AS ROW START INVISIBLE,
   row_end TIMESTAMP(6) AS ROW END INVISIBLE,
   PERIOD FOR application_time(date_1, date_2),
   PERIOD FOR system_time(row_start, row_end))
WITH SYSTEM VERSIONING;
```

Note that, while `system_time` here is also a time period, it cannot be used in `DELETE FOR PORTION` or `UPDATE FOR PORTION` statements:

```sql
DELETE FROM test.t3 
FOR PORTION OF system_time 
    FROM '2000-01-01' TO '2018-01-01';
ERROR 42000: You have an error in your SQL syntax; check the manual that corresponds 
  to your MariaDB server version for the right syntax to use near
  'of system_time from '2000-01-01' to '2018-01-01'' at line 1
```

## See Also

* [System-versioned Tables](system-versioned-tables.md)
* [Application-time Periods](application-time-periods.md)

<sub>_This page is licensed: CC BY-SA / Gnu FDL_</sub>

{% @marketo/form formId="4316" %}
