---
description: >-
  Store time values. This type handles time durations or time of day, ranging
  from '-838:59:59' to '838:59:59' with optional microsecond precision.
---

# TIME

## Syntax

```sql
TIME [(<microsecond precision>)]
```

## Description

A time. The range is `'-838:59:59.999999'` to `'838:59:59.999999'`. [Microsecond precision](../../sql-functions/date-time-functions/microseconds-in-mariadb.md) can be from 0-6; if not specified 0 is used.

MariaDB displays `TIME` values in `'HH:MM:SS.ssssss'` format, but allows assignment of times in looser formats, including 'D HH:MM:SS', 'HH:MM:SS', 'HH:MM', 'D HH:MM', 'D HH', 'SS', or 'HHMMSS', as well as permitting dropping of any leading zeros when a delimiter is provided, for example '3:9:10'. For details, see [date and time literals](../../sql-structure/sql-language-structure/date-and-time-literals.md).

The [--mysql56-temporal-format](../../../ha-and-performance/optimization-and-tuning/system-variables/server-system-variables.md#mysql56_temporal_format) option, on by default, allows MariaDB to store `TIME` values using the same low-level format MySQL 5.6 uses.

### Internal Format

A new temporal format was introduced from MySQL 5.6 that alters how the `TIME`, `DATETIME` and `TIMESTAMP` columns operate at lower levels. These changes allow these temporal data types to have fractional parts and negative values. You can disable this feature using the [mysql56\_temporal\_format](../../../ha-and-performance/optimization-and-tuning/system-variables/server-system-variables.md#mysql56_temporal_format) system variable.

Tables that include `TIMESTAMP` values that were created on an older version of MariaDB or that were created while the [mysql56\_temporal\_format](../../../ha-and-performance/optimization-and-tuning/system-variables/server-system-variables.md#mysql56_temporal_format) system variable was disabled continue to store data using the older data type format.

In order to update table columns from the older format to the newer format, execute an [ALTER TABLE... MODIFY COLUMN](../../sql-statements/data-definition/alter/alter-table/#modify-column) statement that changes the column to the _same_ data type. This change may be needed if you want to export the table's tablespace and import it onto a server that has `mysql56_temporal_format=ON` set (see [MDEV-15225](https://jira.mariadb.org/browse/MDEV-15225)).

For instance, if you have a `TIME` column in your table:

```sql
SHOW VARIABLES LIKE 'mysql56_temporal_format';

+-------------------------+-------+
| Variable_name           | Value |
+-------------------------+-------+
| mysql56_temporal_format | ON    |
+-------------------------+-------+

ALTER TABLE example_table MODIFY ts_col TIME;
```

When MariaDB executes the [ALTER TABLE](../../sql-statements/data-definition/alter/alter-table/) statement, it converts the data from the older temporal format to the newer one.

In the event that you have several tables and columns using temporal data types that you want to switch over to the new format, make sure the system variable is enabled, then perform a dump and restore using `mariadb-dump`. The columns using relevant temporal data types are restored using the new temporal format.

Columns with old temporal formats are marked with a `/* mariadb-5.3 */` comment in the output of [SHOW CREATE TABLE](../../sql-statements/administrative-sql-statements/show/show-create-table.md), [SHOW COLUMNS](../../sql-statements/administrative-sql-statements/show/show-columns.md), [DESCRIBE](../../sql-statements/administrative-sql-statements/describe.md) statements, as well as in the `COLUMN_TYPE` column of the [INFORMATION\_SCHEMA.COLUMNS Table](../../system-tables/information-schema/information-schema-tables/information-schema-columns-table.md).

```sql
SHOW CREATE TABLE mariadb5312_time\G
*************************** 1. row ***************************
       Table: mariadb5312_time
Create Table: CREATE TABLE `mariadb5312_time` (
  `t0` time /* mariadb-5.3 */ DEFAULT NULL,
  `t6` time(6) /* mariadb-5.3 */ DEFAULT NULL
) ENGINE=MyISAM DEFAULT CHARSET=latin1
```

{% hint style="warning" %}
Columns with the current format are not marked with a comment.
{% endhint %}

## Examples

```sql
INSERT INTO time VALUES ('90:00:00'), ('800:00:00'), (800), (22), (151413), ('9:6:3'), ('12 09');

SELECT * FROM time;
+-----------+
| t         |
+-----------+
| 90:00:00  |
| 800:00:00 |
| 00:08:00  |
| 00:00:22  |
| 15:14:13  |
| 09:06:03  |
| 297:00:00 |
+-----------+
```

Time example:

```sql
CREATE TABLE time_example (
  description VARCHAR(30),
  example TIME(6)
);
```

```sql
INSERT INTO time_example VALUES
  ('HH:MM:SS', '12:34:56'),
  ('HHMMSS', '123456'),
  ('SS.microsec', '42.123456');
```

The resulting data look like this:

```sql
SELECT * FROM time_example;
```

```sql
+-------------+-----------------+
| description | example         |
+-------------+-----------------+
| HH:MM:SS    | 12:34:56.000000 |
| HHMMSS      | 12:34:56.000000 |
| SS.microsec | 00:00:42.123456 |
+-------------+-----------------+
```

## See Also

* [Data Type Storage Requirements](../data-type-storage-requirements.md)

<sub>_This page is licensed: GPLv2, originally from_</sub> [<sub>_fill\_help\_tables.sql_</sub>](https://github.com/MariaDB/server/blob/main/scripts/fill_help_tables.sql)

{% @marketo/form formId="4316" %}
