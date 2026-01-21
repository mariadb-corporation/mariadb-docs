---
description: >-
  Extract a specific part of a date. This function retrieves components like
  YEAR, MONTH, DAY, or HOUR from a date or datetime expression.
---

# EXTRACT

## Syntax

```sql
EXTRACT(unit FROM date)
```

## Description

The EXTRACT() function extracts the required unit from the date. See [Date and Time Units](date-and-time-units.md) for a complete list of permitted units.

[HOUR()](hour.md) is not a standard SQL function, so continues to adhere to the old behavior inherited from MySQL.

## Examples

```sql
SELECT EXTRACT(YEAR FROM '2009-07-02');
+---------------------------------+
| EXTRACT(YEAR FROM '2009-07-02') |
+---------------------------------+
|                            2009 |
+---------------------------------+

SELECT EXTRACT(YEAR_MONTH FROM '2009-07-02 01:02:03');
+------------------------------------------------+
| EXTRACT(YEAR_MONTH FROM '2009-07-02 01:02:03') |
+------------------------------------------------+
|                                         200907 |
+------------------------------------------------+

SELECT EXTRACT(DAY_MINUTE FROM '2009-07-02 01:02:03');
+------------------------------------------------+
| EXTRACT(DAY_MINUTE FROM '2009-07-02 01:02:03') |
+------------------------------------------------+
|                                          20102 |
+------------------------------------------------+

SELECT EXTRACT(MICROSECOND FROM '2003-01-02 10:30:00.000123');
+--------------------------------------------------------+
| EXTRACT(MICROSECOND FROM '2003-01-02 10:30:00.000123') |
+--------------------------------------------------------+
|                                                    123 |
+--------------------------------------------------------+
```

`EXTRACT (HOUR FROM...)` returns a value from 0 to 23, as per the SQL standard. `HOUR` is not a standard function, so continues to adhere to the old behaviour inherited from MySQL.

```sql
SELECT EXTRACT(HOUR FROM '26:30:00'), HOUR('26:30:00');
+-------------------------------+------------------+
| EXTRACT(HOUR FROM '26:30:00') | HOUR('26:30:00') |
+-------------------------------+------------------+
|                             2 |               26 |
+-------------------------------+------------------+
```

## See Also

* [Date and Time Units](date-and-time-units.md)
* [Date and Time Literals](../../sql-structure/sql-language-structure/date-and-time-literals.md)
* [HOUR()](hour.md)

<sub>_This page is licensed: GPLv2, originally from_</sub> [<sub>_fill\_help\_tables.sql_</sub>](https://github.com/MariaDB/server/blob/main/scripts/fill_help_tables.sql)

{% @marketo/form formId="4316" %}
