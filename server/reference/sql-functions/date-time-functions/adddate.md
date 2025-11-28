---
description: >-
  Add a time interval to a date. This function performs date arithmetic, adding
  a specified value like days or hours to a starting date.
---

# ADDDATE

## Syntax

```sql
ADDDATE(date,INTERVAL expr unit), ADDDATE(expr,days)
```

## Description

When invoked with the `INTERVAL` form of the second argument, `ADDDATE()` is a synonym for [DATE\_ADD()](date_add.md). The related function [SUBDATE()](subdate.md) is a synonym for [DATE\_SUB()](date_sub.md). For information on the `INTERVAL` unit argument, see the discussion for [DATE\_ADD()](date_add.md).

When invoked with the days form of the second argument, MariaDB treats it as an integer number of days to be added to _expr_.

## Examples

```sql
SELECT DATE_ADD('2008-01-02', INTERVAL 31 DAY);
+-----------------------------------------+
| DATE_ADD('2008-01-02', INTERVAL 31 DAY) |
+-----------------------------------------+
| 2008-02-02                              |
+-----------------------------------------+

SELECT ADDDATE('2008-01-02', INTERVAL 31 DAY);
+----------------------------------------+
| ADDDATE('2008-01-02', INTERVAL 31 DAY) |
+----------------------------------------+
| 2008-02-02                             |
+----------------------------------------+
```

```sql
SELECT ADDDATE('2008-01-02', 31);
+---------------------------+
| ADDDATE('2008-01-02', 31) |
+---------------------------+
| 2008-02-02                |
+---------------------------+
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
SELECT d, ADDDATE(d, 10) from t1;
+---------------------+---------------------+
| d                   | ADDDATE(d, 10)      |
+---------------------+---------------------+
| 2007-01-30 21:31:07 | 2007-02-09 21:31:07 |
| 1983-10-15 06:42:51 | 1983-10-25 06:42:51 |
| 2011-04-21 12:34:56 | 2011-05-01 12:34:56 |
| 2011-10-30 06:31:41 | 2011-11-09 06:31:41 |
| 2011-01-30 14:03:25 | 2011-02-09 14:03:25 |
| 2004-10-07 11:19:34 | 2004-10-17 11:19:34 |
+---------------------+---------------------+

SELECT d, ADDDATE(d, INTERVAL 10 HOUR) from t1;
+---------------------+------------------------------+
| d                   | ADDDATE(d, INTERVAL 10 HOUR) |
+---------------------+------------------------------+
| 2007-01-30 21:31:07 | 2007-01-31 07:31:07          |
| 1983-10-15 06:42:51 | 1983-10-15 16:42:51          |
| 2011-04-21 12:34:56 | 2011-04-21 22:34:56          |
| 2011-10-30 06:31:41 | 2011-10-30 16:31:41          |
| 2011-01-30 14:03:25 | 2011-01-31 00:03:25          |
| 2004-10-07 11:19:34 | 2004-10-07 21:19:34          |
+---------------------+------------------------------+
```

<sub>_This page is licensed: GPLv2, originally from_</sub> [<sub>_fill\_help\_tables.sql_</sub>](https://github.com/MariaDB/server/blob/main/scripts/fill_help_tables.sql)

{% @marketo/form formId="4316" %}
