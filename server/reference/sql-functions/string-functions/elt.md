---
description: >-
  Return the string at a specific index. This function returns the N-th string
  from a list of arguments.
---

# ELT

## Syntax

```sql
ELT(N, str1[, str2, str3,...])
```

## Description

Takes a numeric argument and a series of string arguments. Returns the string that corresponds to the given numeric position. For instance, it returns `str1` if `N` is 1, `str2` if `N` is 2, and so on. If the numeric argument is a [FLOAT](../../data-types/numeric-data-types/float.md), MariaDB rounds it to the nearest [INTEGER](../../data-types/numeric-data-types/integer.md). If the numeric argument is less than 1, greater than the total number of arguments, or not a number, `ELT()` returns `NULL`. It must have at least two arguments.

It is complementary to the [FIELD()](field.md) function.

## Examples

```sql
SELECT ELT(1, 'ej', 'Heja', 'hej', 'foo');
+------------------------------------+
| ELT(1, 'ej', 'Heja', 'hej', 'foo') |
+------------------------------------+
| ej                                 |
+------------------------------------+

SELECT ELT(4, 'ej', 'Heja', 'hej', 'foo');
+------------------------------------+
| ELT(4, 'ej', 'Heja', 'hej', 'foo') |
+------------------------------------+
| foo                                |
+------------------------------------+
```

## See also

* [FIND\_IN\_SET()](find_in_set.md) function. Returns the position of a string in a set of strings.
* [FIELD()](field.md) function. Returns the index position of a string in a list.

<sub>_This page is licensed: GPLv2, originally from_</sub> [<sub>_fill\_help\_tables.sql_</sub>](https://github.com/MariaDB/server/blob/main/scripts/fill_help_tables.sql)

{% @marketo/form formId="4316" %}
