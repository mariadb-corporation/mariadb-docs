---
description: >-
  Generate a random number. This function returns a random floating-point value
  between 0 and 1.
---

# RAND

## Syntax

```
RAND(), RAND(N)
```

## Description

Returns a random [DOUBLE](../../data-types/numeric-data-types/double-precision.md) precision floating point value v in the range 0 <= v < 1.0. If a constant integer argument N is specified, it is used as the seed value, which produces a repeatable sequence of column values. In the example below, note that the sequences of values produced by `RAND(3)` is the same both places where it occurs.

In a `WHERE` clause, `RAND()` is evaluated each time the `WHERE` is executed.

Statements using the `RAND()` function are not [safe for statement-based replication](../../../ha-and-performance/standard-replication/unsafe-statements-for-statement-based-replication.md).

## Practical uses

The expression to get a random integer from a given range is the following:

```sql
FLOOR(min_value + RAND() * (max_value - min_value +1))
```

`RAND()` is often used to read random rows from a table, as follows:

```sql
SELECT * FROM my_table ORDER BY RAND() LIMIT 10;
```

{% hint style="warning" %}
Note, however, that this technique should never be used **on a large table** as it will be extremely slow. MariaDB will read all rows in the table, generate a random value for each of them, order them, and finally will apply the `LIMIT` clause.
{% endhint %}

## Examples

```sql
CREATE TABLE t (i INT);

INSERT INTO t VALUES(1),(2),(3);

SELECT i, RAND() FROM t;
+------+-------------------+
| i    | RAND()            |
+------+-------------------+
|    1 | 0.255651095188829 |
|    2 | 0.833920199269355 |
|    3 |  0.40264774151393 |
+------+-------------------+

SELECT i, RAND(3) FROM t;
+------+-------------------+
| i    | RAND(3)           |
+------+-------------------+
|    1 |  0.90576975597606 |
|    2 | 0.373079058130345 |
|    3 | 0.148086053457191 |
+------+-------------------+

SELECT i, RAND() FROM t;
+------+-------------------+
| i    | RAND()            |
+------+-------------------+
|    1 | 0.511478140495232 |
|    2 | 0.349447508668012 |
|    3 | 0.212803152588013 |
+------+-------------------+
```

Using the same seed, the same sequence will be returned:

```
SELECT i, RAND(3) FROM t;
+------+-------------------+
| i    | RAND(3)           |
+------+-------------------+
|    1 |  0.90576975597606 |
|    2 | 0.373079058130345 |
|    3 | 0.148086053457191 |
+------+-------------------+
```

Generating a random number from 5 to 15:

```
SELECT FLOOR(5 + (RAND() * 11));
```

## See Also

* [Techniques for Efficiently Finding a Random Row](../../../ha-and-performance/optimization-and-tuning/query-optimizations/data-sampling-techniques-for-efficiently-finding-a-random-row.md)
* [rand\_seed1 and rand\_seed2 system variables](../../../ha-and-performance/optimization-and-tuning/system-variables/server-system-variables.md#rand_seed1)

<sub>_This page is licensed: GPLv2, originally from_</sub> [<sub>_fill\_help\_tables.sql_</sub>](https://github.com/MariaDB/server/blob/main/scripts/fill_help_tables.sql)

{% @marketo/form formId="4316" %}
