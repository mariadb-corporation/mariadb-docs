---
description: >-
  TIME_TO_SEC() converts a time value to the number of seconds, returning a
  DOUBLE that preserves microseconds.
---

# TIME\_TO\_SEC

## Syntax

```bnf
TIME_TO_SEC(time)
```

## Description

Returns the time argument, converted to seconds.

The value returned by `TIME_TO_SEC` is of type [DOUBLE](../../../../data-types/data-types-numeric-data-types/double.md). The returned value preserves microseconds of the argument. See also [Microseconds in MariaDB](microseconds-in-mariadb.md).

## Examples

```sql
SELECT TIME_TO_SEC('22:23:00');
+-------------------------+
| TIME_TO_SEC('22:23:00') |
+-------------------------+
|                   80580 |
+-------------------------+
```

```sql
SELECT TIME_TO_SEC('00:39:38');
+-------------------------+
| TIME_TO_SEC('00:39:38') |
+-------------------------+
|                    2378 |
+-------------------------+
```

```sql
SELECT TIME_TO_SEC('09:12:55.2355');
+------------------------------+
| TIME_TO_SEC('09:12:55.2355') |
+------------------------------+
|                   33175.2355 |
+------------------------------+
1 row in set (0.000 sec)
```

<sub>_This page is licensed: GPLv2, originally from_</sub> [<sub>_fill\_help\_tables.sql_</sub>](https://github.com/MariaDB/server/blob/main/scripts/fill_help_tables.sql)

{% @marketo/form formId="4316" %}
