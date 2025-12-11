---
description: >-
  Convert a value to a specific data type. This function explicitly converts a
  value from one type to another, such as string to integer.
---

# CAST

## Syntax

```sql
CAST(expr AS type)
```

## Description

The `CAST()` function takes a value of one [type](../../data-types/) and produces a value of another type, similar to the [CONVERT()](convert.md) function.

The type can be one of the following values:

* [BINARY](../../data-types/string-data-types/binary.md)
* [CHAR](../../data-types/string-data-types/char.md)
* [DATE](../../data-types/date-and-time-data-types/date.md)
* [DATETIME](../../data-types/date-and-time-data-types/datetime.md)
* \[DECIMAL [(M\[,D\])](../../data-types/numeric-data-types/decimal.md)]
* [DOUBLE](../../data-types/numeric-data-types/double.md)
* [FLOAT](../../data-types/numeric-data-types/float.md)
* [INTEGER](../../data-types/numeric-data-types/int.md)
  * Short for `SIGNED INTEGER`
* SIGNED \[INTEGER]
* UNSIGNED \[INTEGER]
* [TIME](../../data-types/date-and-time-data-types/time.md)
* [VARCHAR](../../data-types/string-data-types/varchar.md)

The main difference between `CAST` and [CONVERT()](convert.md) is that [CONVERT(expr,type)](convert.md) is ODBC syntax while `CAST(expr as type)` and [CONVERT(... USING ...)](convert.md) are SQL92 syntax.

You can use the `CAST()` function with the `INTERVAL` keyword.

This introduced an incompatibility with previous versions of MariaDB, and all versions of MySQL (see the example below).

## Examples

### Simple Casts

```sql
SELECT CAST("abc" AS BINARY);
SELECT CAST("1" AS UNSIGNED INTEGER);
SELECT CAST(123 AS CHAR CHARACTER SET utf8)
```

{% hint style="warning" %}
Note that when one casts to [CHAR](../../data-types/string-data-types/char.md) without specifying the character set, the [collation\_connection](../../../ha-and-performance/optimization-and-tuning/system-variables/server-system-variables.md#collation_connection) character set collation will be used. When used with `CHAR CHARACTER SET`, the default collation for that character set will be used.
{% endhint %}

```sql
SELECT COLLATION(CAST(123 AS CHAR));
+------------------------------+
| COLLATION(CAST(123 AS CHAR)) |
+------------------------------+
| latin1_swedish_ci            |
+------------------------------+

SELECT COLLATION(CAST(123 AS CHAR CHARACTER SET utf8));
+-------------------------------------------------+
| COLLATION(CAST(123 AS CHAR CHARACTER SET utf8)) |
+-------------------------------------------------+
| utf8_general_ci                                 |
+-------------------------------------------------+
```

If you also want to change the collation, you have to use the `COLLATE` operator:

```sql
SELECT COLLATION(CAST(123 AS CHAR CHARACTER SET utf8) 
  COLLATE utf8_unicode_ci);
+-------------------------------------------------------------------------+
| COLLATION(CAST(123 AS CHAR CHARACTER SET utf8) COLLATE utf8_unicode_ci) |
+-------------------------------------------------------------------------+
| utf8_unicode_ci                                                         |
+-------------------------------------------------------------------------+
```

Using `CAST()` to order an [ENUM](../../data-types/string-data-types/enum.md) field as a [CHAR](../../data-types/string-data-types/char.md) rather than the internal numerical value:

```sql
CREATE TABLE enum_list (enum_field enum('c','a','b'));

INSERT INTO enum_list (enum_field) 
VALUES('c'),('a'),('c'),('b');

SELECT * FROM enum_list 
ORDER BY enum_field;
+------------+
| enum_field |
+------------+
| c          |
| c          |
| a          |
| b          |
+------------+

SELECT * FROM enum_list 
ORDER BY CAST(enum_field AS CHAR);
+------------+
| enum_field |
+------------+
| a          |
| b          |
| c          |
| c          |
+------------+
```

The following will trigger warnings, since `x'aa'` and `'X'aa'` doesn't behave as a number. In all versions of MySQL, no warnings are triggered since they did erroneously behave as a number:

```sql
SELECT CAST(0xAA AS UNSIGNED), CAST(x'aa' AS UNSIGNED), CAST(X'aa' AS UNSIGNED);
+------------------------+-------------------------+-------------------------+
| CAST(0xAA AS UNSIGNED) | CAST(x'aa' AS UNSIGNED) | CAST(X'aa' AS UNSIGNED) |
+------------------------+-------------------------+-------------------------+
|                    170 |                       0 |                       0 |
+------------------------+-------------------------+-------------------------+
1 row in set, 2 warnings (0.00 sec)

Warning (Code 1292): Truncated incorrect INTEGER value: '\xAA'
Warning (Code 1292): Truncated incorrect INTEGER value: '\xAA'
```

### Casting to Intervals

```sql
SELECT CAST(2019-01-04 AS INTERVAL DAY_SECOND(2)) AS "Cast";

+-------------+
| Cast        |
+-------------+
| 00:20:14.00 |
+-------------+
```

## See Also

* [Supported data types](../../data-types/)
* [Microseconds in MariaDB](../date-time-functions/microseconds-in-mariadb.md)
* [String literals](../../sql-structure/sql-language-structure/string-literals.md)
* [COLLATION()](../secondary-functions/information-functions/collation.md)
* [CONVERT()](convert.md)

<sub>_This page is licensed: GPLv2, originally from_</sub> [<sub>_fill\_help\_tables.sql_</sub>](https://github.com/MariaDB/server/blob/main/scripts/fill_help_tables.sql)

{% @marketo/form formId="4316" %}
