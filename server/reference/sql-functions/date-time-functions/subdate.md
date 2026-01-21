---
description: >-
  Subtract a time interval from a date. This synonym for DATE_SUB calculates a
  past date by subtracting a specified unit from a starting value.
---

# SUBDATE

## Syntax

```sql
SUBDATE(date,INTERVAL expr unit), SUBDATE(expr,days)
```

## Description

When invoked with the `INTERVAL` form of the second argument, `SUBDATE()` is a synonym for [DATE\_SUB()](date_sub.md). See [Date and Time Units](date-and-time-units.md) for a complete list of permitted units.

The second form allows the use of an integer value for days. In such cases, it is interpreted as the number of days to be subtracted from the date or datetime expression expr.

## Examples

```sql
SELECT DATE_SUB('2008-01-02', INTERVAL 31 DAY);
+-----------------------------------------+
| DATE_SUB('2008-01-02', INTERVAL 31 DAY) |
+-----------------------------------------+
| 2007-12-02                              |
+-----------------------------------------+

SELECT SUBDATE('2008-01-02', INTERVAL 31 DAY);
+----------------------------------------+
| SUBDATE('2008-01-02', INTERVAL 31 DAY) |
+----------------------------------------+
| 2007-12-02                             |
+----------------------------------------+
```

```sql
SELECT SUBDATE('2008-01-02 12:00:00', 31);
+------------------------------------+
| SUBDATE('2008-01-02 12:00:00', 31) |
+------------------------------------+
| 2007-12-02 12:00:00                |
+------------------------------------+
```

```sql
CREATE TABLE t1 (d DATETIME);
INSERT INTO t1 VALUES
    ("2007-01-30 21:31:07"),
    ("1983-10-15 06:42:51"),
    ("2011-04-21 12:34:56"),
    ("2011-10-30 06:31:41"),
    ("2011-01-30 14:03:25"),
    ("2004-10-07 11:19:34");
```

```sql
SELECT d, SUBDATE(d, 10) from t1;
+---------------------+---------------------+
| d                   | SUBDATE(d, 10)      |
+---------------------+---------------------+
| 2007-01-30 21:31:07 | 2007-01-20 21:31:07 |
| 1983-10-15 06:42:51 | 1983-10-05 06:42:51 |
| 2011-04-21 12:34:56 | 2011-04-11 12:34:56 |
| 2011-10-30 06:31:41 | 2011-10-20 06:31:41 |
| 2011-01-30 14:03:25 | 2011-01-20 14:03:25 |
| 2004-10-07 11:19:34 | 2004-09-27 11:19:34 |
+---------------------+---------------------+

SELECT d, SUBDATE(d, INTERVAL 10 MINUTE) from t1;
+---------------------+--------------------------------+
| d                   | SUBDATE(d, INTERVAL 10 MINUTE) |
+---------------------+--------------------------------+
| 2007-01-30 21:31:07 | 2007-01-30 21:21:07            |
| 1983-10-15 06:42:51 | 1983-10-15 06:32:51            |
| 2011-04-21 12:34:56 | 2011-04-21 12:24:56            |
| 2011-10-30 06:31:41 | 2011-10-30 06:21:41            |
| 2011-01-30 14:03:25 | 2011-01-30 13:53:25            |
| 2004-10-07 11:19:34 | 2004-10-07 11:09:34            |
+---------------------+--------------------------------+
```

<sub>_This page is licensed: GPLv2, originally from_</sub> [<sub>_fill\_help\_tables.sql_</sub>](https://github.com/MariaDB/server/blob/main/scripts/fill_help_tables.sql)

{% @marketo/form formId="4316" %}
