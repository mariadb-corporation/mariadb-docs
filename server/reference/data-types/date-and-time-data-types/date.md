---
description: >-
  Complete DATE type reference: YYYY-MM-DD format, YYMMDD input literals, date
  range 1000-01-01 to 9999-12-31, and zero-date SQL_MODE handling.
---

# DATE

## Syntax

```sql
DATE
```

## Description

A date. The supported range is '`1000-01-01`' to '`9999-12-31`'. MariaDB displays `DATE` values in '`YYYY-MM-DD`' format, but can be assigned dates in looser formats, including strings or numbers, as long as they make sense. These include a short year, `YY-MM-DD`, no delimiters, `YYMMDD`, or any other acceptable delimiter, for example `YYYY/MM/DD`. For details, see [date and time literals](../../sql-structure/sql-language-structure/date-and-time-literals.md).

'`0000-00-00`' is a permitted special value (zero-date), unless the [NO\_ZERO\_DATE](../../../server-management/variables-and-modes/sql_mode.md#no_zero_date) [SQL\_MODE](../../../server-management/variables-and-modes/sql_mode.md) is used. Also, individual components of a date can be set to 0 (for example: '`2015-00-12`'), unless the [NO\_ZERO\_IN\_DATE](../../../server-management/variables-and-modes/sql_mode.md#no_zero_in_date) [SQL\_MODE](../../../server-management/variables-and-modes/sql_mode.md) is used. In many cases, the result of en expression involving a zero-date, or a date with zero-parts, is `NULL`. If the [ALLOW\_INVALID\_DATES](../../../server-management/variables-and-modes/sql_mode.md#allow_invalid_dates) `SQL_MODE` is enabled, if the day part is in the range between 1 and 31, the date does not produce any error, even for months that have less than 31 days.

### Oracle Mode

In [Oracle mode](../../../server-usage/stored-routines/stored-procedures/create-procedure.md#oracle-mode), `DATE` with a time portion is a synonym for [DATETIME](datetime.md). See also [mariadb\_schema](../../system-tables/mariadb_schema.md).

## Examples

```sql
CREATE TABLE t1 (d DATE);

INSERT INTO t1 VALUES ("2010-01-12"), ("2011-2-28"), ('120314'),('13*04*21');

SELECT * FROM t1;
+------------+
| d          |
+------------+
| 2010-01-12 |
| 2011-02-28 |
| 2012-03-14 |
| 2013-04-21 |
+------------+
```

### DATE Format

```sql
CREATE TABLE date_formats_example (
   description VARCHAR(30),
   example DATE
);
```

```sql
INSERT INTO date_formats_example VALUES
   ('Full year', '2022-12-30'),
   ('Short year', '22-12-30'),
   ('Short year no delimiters', '221230'),
   ('No delimiters', '20221230'),
   ('Pipe delimiters', '22|2|3'),
   ('Forward slash delimiter', '22/12/30'),
   ('Backward slash delimiter', '22\12\30'),
   ('Asterisk delimiter', '22*12*30'),
   ('Comma delimiter', '22,2,3');
```

The resulting data look like this:

```sql
SELECT * FROM date_formats_example;
```

```sql
+--------------------------+------------+
| description              | example    |
+--------------------------+------------+
| Full year                | 2022-12-30 |
| Short year               | 2022-12-30 |
| Short year no delimiters | 2022-12-30 |
| No delimiters            | 2022-12-30 |
| Pipe delimiters          | 2022-02-03 |
| Forward slash delimiter  | 2022-12-30 |
| Backward slash delimiter | 2022-12-30 |
| Asterisk delimiter       | 2022-12-30 |
| Comma delimiter          | 2022-02-03 |
+--------------------------+------------+
```

### DATE Range

```sql
CREATE TABLE date_range_example (
   description VARCHAR(30),
   example DATE
);
```

```sql
INSERT INTO date_range_example VALUES
   ('Minimum date', '0001-01-01'),
   ('Maximum date', '9999-12-31'),
   ('Below minimum range', '0000*1*1'),
   ('Above maximum range', '10000,12,31');
```

If `SQL_MODE` is strict (the default), the example above generates the following error and no values are inserted:

```sql
ERROR 1292 (22007): Incorrect date value: '10000,12,31' for column `test`.`date_range_example`.`example` at row 4
```

If `SQL_MODE` is not strict, the example above generates a warning and (possibly modified) values are inserted. The Below minimum range value is accepted because it contains a zero component. The Above maximum range value is truncated since it is an unacceptable date.

```sql
Warning (Code 1265): Data truncated for column 'example' at row 4
```

The resulting data would look like this:

```sql
SELECT * FROM date_range_example;
```

```sql
+---------------------+------------+
| description         | example    |
+---------------------+------------+
| Minimum date        | 0001-01-01 |
| Maximum date        | 9999-12-31 |
| Below minimum range | 0000-01-01 |
| Above maximum range | 0000-00-00 |
+---------------------+------------+
```

### Date Expressions

When using a date value in an expression, such as `DATE_ADD()`, the following illustrates that a `NULL` is generated when a date value is not a real date and when a real date overflows:

```sql
SELECT example, DATE_ADD(example, INTERVAL 1 DAY)
   FROM date_range_example;
```

```sql
+------------+-----------------------------------+
| example    | DATE_ADD(example, INTERVAL 1 DAY) |
+------------+-----------------------------------+
| 0001-01-01 | 0001-01-02                        |
| 9999-12-31 | NULL                              |
| 0000-01-01 | NULL                              |
| 0000-00-00 | NULL                              |
+------------+-----------------------------------+
```

```sql
Warning (Code 1441): Datetime function: datetime field overflow
Warning (Code 1441): Datetime function: datetime field overflow
Warning (Code 1292): Incorrect datetime value: '0000-00-00'
```

### Invalid Dates

The following example enhances the `SQL_MODE` to ensure that `ALLOW_INVALID_DATES` is set and illustrates the difference between a day that is outside the range of 1 to 31 and one that is just too large for its month:

```sql
-- Disable STRICT_TRANS_TABLES and enable ALLOW_INVALID_DATES
SET sql_mode=(SELECT REPLACE(@@sql_mode, 'STRICT_TRANS_TABLES', ''));
SET sql_mode=(SELECT CONCAT(@@sql_mode, ',ALLOW_INVALID_DATES'));
<</code>>

<<sql>>
INSERT INTO date_range_example VALUES
  ('day is invalid for all months', '2019-12-32'),
  ('day is just large for February', '2019-02-31');
```

```sql
Warning (Code 1265): Data truncated for column 'example' at row 1
```

The resulting data would look like this:

```sql
SELECT * FROM date_range_example;
```

```sql
+--------------------------------+------------+
| description                    | example    |
+--------------------------------+------------+
| day is invalid for all months  | 0000-00-00 |
| day is just large for February | 2019-02-31 |
+--------------------------------+------------+
```

## See Also

* [mariadb\_schema](../../system-tables/mariadb_schema.md) data type qualifier

<sub>_This page is licensed: GPLv2, originally from_</sub> [<sub>_fill\_help\_tables.sql_</sub>](https://github.com/MariaDB/server/blob/main/scripts/fill_help_tables.sql)

{% @marketo/form formId="4316" %}
