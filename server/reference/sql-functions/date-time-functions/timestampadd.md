---
description: >-
  Add an interval to a timestamp. This function adds a specified integer number
  of units (like MONTH or SECOND) to a datetime expression.
---

# TIMESTAMPADD

## Syntax

```sql
TIMESTAMPADD(unit,interval,datetime_expr)
```

## Description

Adds the integer expression interval to the date or datetime expression datetime\_expr. The unit for interval is given by the unit argument, which should be one of the following values: `MICROSECOND`, `SECOND`, `MINUTE`, `HOUR`, `DAY`, `WEEK`, `MONTH`, `QUARTER`, or `YEAR`.

The unit value may be specified using one of keywords as shown, or with a prefix of `SQL_TSI_`. For example, `DAY` and `SQL_TSI_DAY` both are allowed.

## Examples

```sql
SELECT TIMESTAMPADD(MINUTE,1,'2003-01-02');
+-------------------------------------+
| TIMESTAMPADD(MINUTE,1,'2003-01-02') |
+-------------------------------------+
| 2003-01-02 00:01:00                 |
+-------------------------------------+

SELECT TIMESTAMPADD(WEEK,1,'2003-01-02');
+-----------------------------------+
| TIMESTAMPADD(WEEK,1,'2003-01-02') |
+-----------------------------------+
| 2003-01-09                        |
+-----------------------------------+
```

<sub>_This page is licensed: GPLv2, originally from_</sub> [<sub>_fill\_help\_tables.sql_</sub>](https://github.com/MariaDB/server/blob/main/scripts/fill_help_tables.sql)

{% @marketo/form formId="4316" %}
