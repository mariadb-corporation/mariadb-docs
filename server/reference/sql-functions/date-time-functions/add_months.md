---
description: >-
  Add a specific number of months to a date. This Oracle-compatible function
  simplifies date calculations involving monthly intervals.
---

# ADD\_MONTHS

{% hint style="info" %}
`ADD_MONTHS` is available from [10.6.1](https://app.gitbook.com/s/aEnK0ZXmUbJzqQrTjFyb/community-server/mariadb-10-6-series/mariadb-1061-release-notes).
{% endhint %}

The `ADD_MONTHS` function was introduced to enhance Oracle compatibility. Similar functionality can be achieved with the [DATE\_ADD](date_add.md) function.

## Syntax

```sql
ADD_MONTHS(date, months)
```

## Description

`ADD_MONTHS` adds an integer _months_ to a given _date_ ([DATE](../../data-types/date-and-time-data-types/date.md), [DATETIME](../../data-types/date-and-time-data-types/datetime.md) or [TIMESTAMP](../../data-types/date-and-time-data-types/timestamp.md)), returning the resulting date.

_months_ can be positive or negative. If months is not a whole number, then it will be rounded to the nearest whole number (not truncated).

The resulting day component will remain the same as that specified in _date_, unless the resulting month has fewer days than the day component of the given date, in which case the day will be the last day of the resulting month.

Returns NULL if given an invalid date, or a `NULL` argument.

## Examples

```sql
SELECT ADD_MONTHS('2012-01-31', 2);
+-----------------------------+
| ADD_MONTHS('2012-01-31', 2) |
+-----------------------------+
| 2012-03-31                  |
+-----------------------------+

SELECT ADD_MONTHS('2012-01-31', -5);
+------------------------------+
| ADD_MONTHS('2012-01-31', -5) |
+------------------------------+
| 2011-08-31                   |
+------------------------------+

SELECT ADD_MONTHS('2011-01-31', 1);
+-----------------------------+
| ADD_MONTHS('2011-01-31', 1) |
+-----------------------------+
| 2011-02-28                  |
+-----------------------------+

SELECT ADD_MONTHS('2012-01-31', 1);
+-----------------------------+
| ADD_MONTHS('2012-01-31', 1) |
+-----------------------------+
| 2012-02-29                  |
+-----------------------------+

SELECT ADD_MONTHS('2012-01-31', 2);
+-----------------------------+
| ADD_MONTHS('2012-01-31', 2) |
+-----------------------------+
| 2012-03-31                  |
+-----------------------------+

SELECT ADD_MONTHS('2012-01-31', 3);
+-----------------------------+
| ADD_MONTHS('2012-01-31', 3) |
+-----------------------------+
| 2012-04-30                  |
+-----------------------------+

SELECT ADD_MONTHS('2011-01-15', 2.5);
+-------------------------------+
| ADD_MONTHS('2011-01-15', 2.5) |
+-------------------------------+
| 2011-04-15                    |
+-------------------------------+
1 row in set (0.001 sec)

SELECT ADD_MONTHS('2011-01-15', 2.6);
+-------------------------------+
| ADD_MONTHS('2011-01-15', 2.6) |
+-------------------------------+
| 2011-04-15                    |
+-------------------------------+
1 row in set (0.001 sec)

SELECT ADD_MONTHS('2011-01-15', 2.1);
+-------------------------------+
| ADD_MONTHS('2011-01-15', 2.1) |
+-------------------------------+
| 2011-03-15                    |
+-------------------------------+
1 row in set (0.004 sec)
```

## See Also

* [SQL\_MODE=ORACLE](https://app.gitbook.com/s/aEnK0ZXmUbJzqQrTjFyb/community-server/about/compatibility-and-differences/sql_modeoracle)

<sub>_This page is licensed: CC BY-SA / Gnu FDL_</sub>

{% @marketo/form formId="4316" %}
