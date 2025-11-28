---
description: >-
  Extract the year. This function returns the year portion of a date as a number
  from 1000 to 9999.
---

# YEAR

## Syntax

```sql
YEAR(date)
```

## Description

Returns the year for the given date, in the range 1000 to 9999, or 0 for the "zero" date.

`SQL_TSI_YEAR` is a synonym for `YEAR`:

## Examples

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
SELECT * FROM t1;
+---------------------+
| d                   |
+---------------------+
| 2007-01-30 21:31:07 |
| 1983-10-15 06:42:51 |
| 2011-04-21 12:34:56 |
| 2011-10-30 06:31:41 |
| 2011-01-30 14:03:25 |
| 2004-10-07 11:19:34 |
+---------------------+

SELECT * FROM t1 WHERE YEAR(d) = 2011;
+---------------------+
| d                   |
+---------------------+
| 2011-04-21 12:34:56 |
| 2011-10-30 06:31:41 |
| 2011-01-30 14:03:25 |
+---------------------+
```

```sql
SELECT YEAR('1987-01-01');
+--------------------+
| YEAR('1987-01-01') |
+--------------------+
|               1987 |
+--------------------+
```

### YEAR Format

```sql
CREATE TABLE year_format_example (
  description VARCHAR(30),
  example YEAR
);
```

```sql
INSERT INTO year_format_example VALUES
  ('4-digit numeric year', 1966),
  ('2-digit numeric year', 66),
  ('4-digit string year', '1966'),
  ('2-digit string year', '66');
```

The resulting output would look like this:

```sql
SELECT * FROM year_format_example;

+----------------------+---------+
| description          | example |
+----------------------+---------+
| 4-digit numeric year |    1966 |
| 2-digit numeric year |    2066 |
| 4-digit string year  |    1966 |
| 2-digit string year  |    2066 |
+----------------------+---------+
```

### YEAR Range

```sql
CREATE TABLE year_range_example (
  description VARCHAR(30),
  example YEAR
);
```

```sql
INSERT INTO year_range_example VALUES
  ('minimum', 1901),
  ('maximum', 2155),
  ('below minimum', 1900),
  ('above maximum', 2156);
```

If `SQL_MODE` is strict (the default), the example above generates the following error and no values are inserted:

```sql
ERROR 1264 (22003): Out of range value for column 'example' at row 3
```

If `SQL_MODE` is not strict, the example above generates a warning and (possibly modified) values are inserted:

```sql
Warning (sql 1264): Out of range value for column 'example' at row 3
Warning (sql 1264): Out of range value for column 'example' at row 4
The resulting data would look like this:
```

```sql
SELECT * FROM year_range_example;

+---------------+---------+
| description   | example |
+---------------+---------+
| minimum       |    1901 |
| maximum       |    2155 |
| below minimum |    0000 |
| above maximum |    0000 |
+---------------+---------+
```

### Zero YEAR

```sql
CREATE TABLE year_zero_example (
  description VARCHAR(30),
  example YEAR
);
```

```sql
INSERT INTO year_zero_example VALUES
  ('4-digit numeric zero', 0000),
  ('3-digit numeric zero', 000),
  ('2-digit numeric zero', 00),
  ('1-digit numeric zero', 0),
  ('4-digit string zero', '0000'),
  ('3-digit string zero', '000'),
  ('2-digit string zero', '00'),
  ('1-digit string zero', '0');
```

The resulting data would look like this:

```sql
SELECT * FROM year_zero_example;

+----------------------+---------+
| description          | example |
+----------------------+---------+
| 4-digit numeric zero |    0000 |
| 3-digit numeric zero |    0000 |
| 2-digit numeric zero |    0000 |
| 1-digit numeric zero |    0000 |
| 4-digit string zero  |    0000 |
| 3-digit string zero  |    2000 |
| 2-digit string zero  |    2000 |
| 1-digit string zero  |    2000 |
+----------------------+---------+
```

## See Also

* [YEAR data type](../../data-types/date-and-time-data-types/year-data-type.md)

<sub>_This page is licensed: GPLv2, originally from_</sub> [<sub>_fill\_help\_tables.sql_</sub>](https://github.com/MariaDB/server/blob/main/scripts/fill_help_tables.sql)

{% @marketo/form formId="4316" %}
