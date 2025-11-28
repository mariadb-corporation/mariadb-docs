---
description: >-
  Understand Type Conversion in MariaDB. Learn the rules for implicit conversion
  during comparisons and arithmetic, and how to use CAST for predictable
  results.
---

# Type Conversion

Implicit type conversion takes place when MariaDB is using operands or different types, in order to make the operands compatible.

It is best practice not to rely upon implicit conversion; rather use [CAST](cast.md) to explicitly convert types.

### Rules for Conversion on Comparison

* If either argument is NULL, the result of the comparison is NULL unless the NULL-safe [<=>](../../sql-structure/operators/comparison-operators/null-safe-equal.md) equality comparison operator is used.
* If both arguments are integers, they are compared as integers.
* If both arguments are strings, they are compared as strings.
* If one argument is decimal and the other argument is decimal or integer, they are compared as decimals.
* If one argument is decimal and the other argument is a floating point, they are compared as floating point values.
* If one argument is string and the other argument is integer, they are compared as decimals.
* If a hexadecimal argument is not compared to a number, it is treated as a binary string.
* If a constant is compared to a TIMESTAMP or DATETIME, the constant is converted to a timestamp, unless used as an argument to the [IN](../../sql-structure/operators/comparison-operators/in.md) function.
* In other cases, arguments are compared as floating point, or real, numbers.

Note that if a string column is being compared with a numeric value, MariaDB will not use the index on the column, as there are numerous alternatives that may evaluate as equal (see examples below).

#### Comparison Examples

Converting a string to a number:

```sql
SELECT 15+'15';
+---------+
| 15+'15' |
+---------+
|      30 |
+---------+
```

Converting a number to a string:

```sql
SELECT CONCAT(15,'15');
+-----------------+
| CONCAT(15,'15') |
+-----------------+
| 1515            |
+-----------------+
```

Floating point number errors:

```sql
SELECT '9746718491924563214' = 9746718491924563213;
+---------------------------------------------+
| '9746718491924563214' = 9746718491924563213 |
+---------------------------------------------+
|                                           1 |
+---------------------------------------------+
```

Numeric equivalence with strings:

```sql
SELECT '5' = 5;
+---------+
| '5' = 5 |
+---------+
|       1 |
+---------+

SELECT '   5' = 5;
+------------+
| '   5' = 5 |
+------------+
|          1 |
+------------+

SELECT '   5  ' = 5;
+--------------+
| '   5  ' = 5 |
+--------------+
|            1 |
+--------------+
1 row in set, 1 warning (0.000 sec)

SHOW WARNINGS;
+-------+------+--------------------------------------------+
| Level | Code | Message                                    |
+-------+------+--------------------------------------------+
| Note  | 1292 | Truncated incorrect DOUBLE value: '   5  ' |
+-------+------+--------------------------------------------+
```

As a result of the above, MariaDB cannot use the index when comparing a string with a numeric value in the example below:

```sql
CREATE TABLE t (a VARCHAR(10), b VARCHAR(10), INDEX idx_a (a));

INSERT INTO t VALUES 
  ('1', '1'), ('2', '2'), ('3', '3'), 
  ('4', '4'), ('5', '5'), ('1', '5');

EXPLAIN SELECT * FROM t WHERE a = '3' \G
*************************** 1. row ***************************
           id: 1
  select_type: SIMPLE
        table: t
         type: ref
possible_keys: idx_a
          key: idx_a
      key_len: 13
          ref: const
         rows: 1
        Extra: Using index condition

EXPLAIN SELECT * FROM t WHERE a = 3 \G
*************************** 1. row ***************************
           id: 1
  select_type: SIMPLE
        table: t
         type: ALL
possible_keys: idx_a
          key: NULL
      key_len: NULL
          ref: NULL
         rows: 6
        Extra: Using where
```

### Rules for Conversion on Dyadic Arithmetic Operations

Implicit type conversion also takes place on dyadic arithmetic operations ([+](../../sql-structure/operators/arithmetic-operators/addition-operator.md),[-](../../sql-structure/operators/arithmetic-operators/subtraction-operator.md),[\*](../../sql-structure/operators/arithmetic-operators/multiplication-operator.md),[/](../../sql-structure/operators/arithmetic-operators/division-operator.md)). MariaDB chooses the minimum data type that is guaranteed to fit the result and converts both arguments to the result data type.

For [addition (+)](../../sql-structure/operators/arithmetic-operators/addition-operator.md), [subtraction (-)](../../sql-structure/operators/arithmetic-operators/subtraction-operator.md) and [multiplication (\*)](../../sql-structure/operators/arithmetic-operators/multiplication-operator.md), the result data type is chosen as follows:

* If either of the arguments is an approximate number (float, double), the result is double.
* If either of the arguments is a string (char, varchar, text), the result is double.
* If either of the arguments is a decimal number, the result is decimal.
* If either of the arguments is of a temporal type with a non-zero fractional second precision (time(N), datetime(N), timestamp(N)), the result is decimal.
* If either of the arguments is of a temporal type with a zero fractional second precision (time(0), date, datetime(0), timestamp(0)), the result may vary between int, int unsigned, bigint or bigint unsigned, depending on the exact data type combination.
* If both arguments are integer numbers (tinyint, smallint, mediumint, bigint), the result may vary between int, int unsigned, bigint or bigint unsigned, depending of the exact data types and their signs.

For [division (/)](../../sql-structure/operators/arithmetic-operators/division-operator.md), the result data type is chosen as follows:

* If either of the arguments is an approximate number (float, double), the result is double.
* If either of the arguments is a string (char, varchar, text), the result is double.
* Otherwise, the result is decimal.

#### Arithmetic Examples

Note, the above rules mean that when an argument of a temporal data type appears in addition or subtraction, it's treated as a number by default.

```sql
SELECT TIME'10:20:30' + 1;
+--------------------+
| TIME'10:20:30' + 1 |
+--------------------+
|             102031 |
+--------------------+
```

In order to do temporal addition or subtraction instead, use the [DATE\_ADD()](../date-time-functions/date_add.md) or [DATE\_SUB()](../date-time-functions/date_sub.md) functions, or an [INTERVAL](../date-time-functions/date-and-time-units.md) expression as the second argument:

```sql
SELECT TIME'10:20:30' + INTERVAL 1 SECOND;
+------------------------------------+
| TIME'10:20:30' + INTERVAL 1 SECOND |
+------------------------------------+
| 10:20:31                           |
+------------------------------------+
```

```sql
SELECT "2.2" + 3;
+-----------+
| "2.2" + 3 |
+-----------+
|       5.2 |
+-----------+

SELECT 2.2 + 3;
+---------+
| 2.2 + 3 |
+---------+
| 5.2     |
+---------+

SELECT 2.2 / 3;
+---------+
| 2.2 / 3 |
+---------+
| 0.73333 |
+---------+

SELECT "2.2" / 3;
+--------------------+
| "2.2" / 3          |
+--------------------+
| 0.7333333333333334 |
+--------------------+
```

<sub>_This page is licensed: CC BY-SA / Gnu FDL_</sub>

{% @marketo/form formId="4316" %}
