---
description: >-
  Load history that already exists, such as a change log or an audit table,
  into a system-versioned table so that FOR SYSTEM_TIME queries answer with the
  original dates.
---

# Loading Existing History

A [system-versioned table](system-versioned-tables.md) records changes from the moment versioning is turned on. This page covers the other case: you already have the history, for example in a change log, an audit table, or another database, and you want `FOR SYSTEM_TIME AS OF` to return the rows as they were at the original dates.

{% hint style="info" %}
Writing `row_start` and `row_end` directly requires MariaDB 10.11 or later and the [system\_versioning\_insert\_history](system-versioned-tables.md#system_versioning_insert_history) system variable.
{% endhint %}

The examples load this change log:

```sql
CREATE TABLE price_log (
  product    VARCHAR(20),
  price      DECIMAL(8,2),
  changed_at TIMESTAMP(6)
);

INSERT INTO price_log VALUES
  ('tea',    10.00, '2019-03-01 00:00:00'),
  ('tea',    12.50, '2021-06-01 00:00:00'),
  ('tea',    14.00, '2024-01-15 00:00:00'),
  ('coffee', 20.00, '2020-05-10 00:00:00'),
  ('coffee', 22.00, '2023-02-01 00:00:00');
```

## Load the History

### 1. Create the Table

Declare the period columns. This is optional, because the implicit `row_start` and `row_end` columns can be written too, but it makes the column names and types explicit:

```sql
CREATE TABLE price (
  product   VARCHAR(20)  NOT NULL PRIMARY KEY,
  price     DECIMAL(8,2) NOT NULL,
  row_start TIMESTAMP(6) AS ROW START INVISIBLE,
  row_end   TIMESTAMP(6) AS ROW END INVISIBLE,
  PERIOD FOR SYSTEM_TIME (row_start, row_end)
) WITH SYSTEM VERSIONING;
```

Use `TIMESTAMP(6)` columns. A table versioned by transaction ID (`BIGINT UNSIGNED` columns) does not accept written values.

If the table is partitioned by `SYSTEM_TIME`, create the history partitions before the load. See [Partitioned Tables](#partitioned-tables).

### 2. Load the Old Versions

Set the time zone that the dates are in, then enable `system_versioning_insert_history` for the session. Without it, a value for `row_start` or `row_end` fails with error 1906.

Each version ends when the next change to the same key starts. The `LEAD()` window function returns that moment:

```sql
SET time_zone = '+00:00';
SET @@system_versioning_insert_history = 1;

INSERT INTO price (product, price, row_start, row_end)
SELECT product, price, changed_at, next_change
FROM (SELECT product, price, changed_at,
             LEAD(changed_at) OVER (PARTITION BY product ORDER BY changed_at) AS next_change
      FROM price_log) AS steps
WHERE next_change IS NOT NULL;
```

### 3. Load the Current Rows

The last change of each key is the current row. Leave `row_end` out, and the server marks the row as current:

```sql
INSERT INTO price (product, price, row_start)
SELECT product, price, changed_at
FROM (SELECT product, price, changed_at,
             LEAD(changed_at) OVER (PARTITION BY product ORDER BY changed_at) AS next_change
      FROM price_log) AS steps
WHERE next_change IS NULL;

SET @@system_versioning_insert_history = 0;
```

`LOAD DATA` works the same way, with `row_start` and `row_end` in the column list.

### 4. Check for Gaps and Overlaps

The server refuses a version that ends before it starts (error 4112), but it does not compare versions of the same key with each other. Two versions that cover the same time are both stored, and `AS OF` then returns two rows for one primary key. This query must return `0`:

```sql
SELECT COUNT(*) AS gaps_or_overlaps
FROM (SELECT row_end,
             LEAD(row_start) OVER (PARTITION BY product ORDER BY row_end) AS next_start
      FROM price FOR SYSTEM_TIME ALL) AS v
WHERE next_start IS NOT NULL AND next_start <> row_end;
```

After the load, the table is an ordinary system-versioned table:

```sql
SELECT * FROM price FOR SYSTEM_TIME AS OF TIMESTAMP '2022-01-01 00:00:00';
+---------+-------+
| product | price |
+---------+-------+
| coffee  | 20.00 |
| tea     | 12.50 |
+---------+-------+
```

A change made today is stamped by the server clock, and the server closes the last loaded version of that row.

## Partitioned Tables

`AUTO` creates history partitions when the server clock needs them. It does not create partitions for the dates of loaded rows, so without partitions for those dates every loaded version goes into the first history partition. After the first live change, `AUTO` adds the missing partitions, the loaded rows stay where they are, and partition pruning can then skip them: `AS OF` returns no row for a date that had one before.

Create the partitions before the load. Set `STARTS` before the oldest change and enough `PARTITIONS` to reach the present:

```sql
CREATE TABLE price (
  ...
) WITH SYSTEM VERSIONING
  PARTITION BY SYSTEM_TIME INTERVAL 1 YEAR STARTS '2019-01-01 00:00:00' AUTO PARTITIONS 9;
```

[CHECK TABLE](../../sql-statements/table-statements/check-table.md) reports rows that are in the wrong partition ("Found a misplaced row"), and [REPAIR TABLE](../../sql-statements/table-statements/repair-table.md) moves them.

## Replaying Changes Instead

If the changes can be run again in time order, you can set the session clock before each one and let the server write the history. This needs no `system_versioning_insert_history` and no period columns:

```sql
SET @@timestamp = UNIX_TIMESTAMP('2019-03-01 00:00:00');
INSERT INTO price VALUES ('tea', 10.00);
SET @@timestamp = UNIX_TIMESTAMP('2021-06-01 00:00:00');
UPDATE price SET price = 12.50 WHERE product = 'tea';
SET @@timestamp = DEFAULT;
```

{% hint style="warning" %}
The changes for each key must be in time order. An `UPDATE` with a timestamp earlier than the `row_start` of the current row is accepted without an error or a warning. The current version is not kept, and the new version overlaps older versions.
{% endhint %}

Replay runs one statement per change. For large histories, the bulk load above is faster, and the order of the statements does not matter.

## Limitations

* `row_start` cannot be earlier than `1970-01-01 00:00:01` UTC (error 1292). Keep older dates in an [application-time period](application-time-periods.md).
* Dates are read in the session time zone. Set `time_zone` before the load and before queries.
* Nothing can be loaded when [secure\_timestamp](../../../ha-and-performance/optimization-and-tuning/system-variables/server-system-variables.md#secure_timestamp) is `YES`. Load first, then enable it, so that sessions cannot write history afterwards.
* A plain [mariadb-dump](../../../clients-and-utilities/backup-restore-and-import-clients/mariadb-dump.md) includes current rows only. Use `--dump-history` to include the history.

## See Also

* [System-Versioned Tables](system-versioned-tables.md)
* [Application-Time Periods](application-time-periods.md)
* [Bitemporal Tables](bitemporal-tables.md)

<sub>_This page is licensed: CC BY-SA / Gnu FDL_</sub>

{% @marketo/form formId="4316" %}
