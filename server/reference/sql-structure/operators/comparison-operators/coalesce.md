# COALESCE

## Syntax

```bnf
COALESCE(value,...)
```

## Description

Returns the first non-`NULL` value in the list, or `NULL` if there are no non-`NULL` values. At least one parameter must be passed.

The function is useful when substituting a default value for null values when displaying data.

See also [NULL Values in MariaDB](../../../data-types/null-values.md).

## Examples

```sql
SELECT COALESCE(NULL,1);
+------------------+
| COALESCE(NULL,1) |
+------------------+
|                1 |
+------------------+
```

```sql
SELECT COALESCE(NULL,NULL,NULL);
+--------------------------+
| COALESCE(NULL,NULL,NULL) |
+--------------------------+
|                     NULL |
+--------------------------+
```

When two arguments are given, `COALESCE()` is the same as [IFNULL()](../../../sql-functions/control-flow-functions/ifnull.md):

```sql
SET @a=NULL, @b=1;

SELECT COALESCE(@a, @b), IFNULL(@a, @b);
+------------------+----------------+
| COALESCE(@a, @b) | IFNULL(@a, @b) |
+------------------+----------------+
|                1 |              1 |
+------------------+----------------+
```

Hex type confusion:

```sql
CREATE TABLE t1 (a INT, b VARCHAR(10));
INSERT INTO t1 VALUES (0x31, 0x61),(COALESCE(0x31), COALESCE(0x61));

SELECT * FROM t1;
+------+------+
| a    | b    |
+------+------+
|   49 | a    |
|    1 | a    |
+------+------+
```

The reason for the differing results above is that when `0x31` is inserted directly to the column, it's treated as a number (see [Hexadecimal Literals](../../sql-language-structure/hexadecimal-literals.md)), while when `0x31` is passed to `COALESCE()`, it's treated as a string, because:

* `HEX` values have a string data type by default.
* `COALESCE()` has the same data type as the argument.

Substituting zero for `NULL` (in this case when the aggregate function returns `NULL` after finding no rows):

```sql
SELECT SUM(score) FROM student;
+------------+
| SUM(score) |
+------------+
|       NULL |
+------------+

SELECT COALESCE(SUM(score),0) FROM student;
+------------------------+
| COALESCE(SUM(score),0) |
+------------------------+
|                      0 |
+------------------------+
```

## See also

* [NULL values](../../../data-types/null-values.md)
* [IS NULL operator](is-null.md)
* [IS NOT NULL operator](is-not-null.md)
* [IFNULL function](../../../sql-functions/control-flow-functions/ifnull.md)
* [NULLIF function](../../../sql-functions/control-flow-functions/nullif.md)
* [CONNECT data types](../../../../server-usage/storage-engines/connect/connect-data-types.md#null-handling)

<sub>_This page is licensed: GPLv2, originally from_</sub> [<sub>_fill\_help\_tables.sql_</sub>](https://github.com/MariaDB/server/blob/main/scripts/fill_help_tables.sql)

{% @marketo/form formId="4316" %}
