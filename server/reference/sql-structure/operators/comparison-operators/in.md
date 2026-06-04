# IN

## Syntax

```bnf
expr IN (value,...)
```

## Description

Returns `1` if _`expr`_ is equal to any of the values in the `IN` list, else returns `0`. If all values are constants, they are evaluated according to the type of _`expr`_ and sorted. The search for the item then is done\
using a binary search. This means IN is very quick if the IN value list consists entirely of constants. Otherwise, type conversion takes place according to the rules described at [Type Conversion](../../../sql-functions/string-functions/type-conversion.md), but\
applied to all the arguments.

If _`expr`_ is `NULL`, `IN` always returns `NULL`. If at least one of the values in the list is `NULL`, and one of the comparisons is true, the result is `1`. If at least one of the values in the list is `NULL` and none of the comparisons is true, the result is `NULL`.

## Examples

```sql
SELECT 2 IN (0,3,5,7);
+----------------+
| 2 IN (0,3,5,7) |
+----------------+
|              0 |
+----------------+
```

```sql
SELECT 'wefwf' IN ('wee','wefwf','weg');
+----------------------------------+
| 'wefwf' IN ('wee','wefwf','weg') |
+----------------------------------+
|                                1 |
+----------------------------------+
```

Type conversion:

```sql
SELECT 1 IN ('1', '2', '3');
+----------------------+
| 1 IN ('1', '2', '3') |
+----------------------+
|                    1 |
+----------------------+
```

```sql
SELECT NULL IN (1, 2, 3);
+-------------------+
| NULL IN (1, 2, 3) |
+-------------------+
|              NULL |
+-------------------+

SELECT 1 IN (1, 2, NULL);
+-------------------+
| 1 IN (1, 2, NULL) |
+-------------------+
|                 1 |
+-------------------+

SELECT 5 IN (1, 2, NULL);
+-------------------+
| 5 IN (1, 2, NULL) |
+-------------------+
|              NULL |
+-------------------+
```

## See Also

* [Conversion of Big IN Predicates Into Subqueries](../../../../ha-and-performance/optimization-and-tuning/query-optimizations/subquery-optimizations/conversion-of-big-in-predicates-into-subqueries.md)
* [Operator Precedence](../operator-precedence.md)

<sub>_This page is licensed: GPLv2, originally from_</sub> [<sub>_fill\_help\_tables.sql_</sub>](https://github.com/MariaDB/server/blob/main/scripts/fill_help_tables.sql)

{% @marketo/form formId="4316" %}
