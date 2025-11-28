---
description: >-
  Test if a string matches a regex. This operator returns 1 if the pattern is
  found in the string, and 0 otherwise.
---

# REGEXP

## Syntax

```sql
expr REGEXP pat, expr RLIKE pat
```

## Description

Performs a pattern match of a string expression `expr` against a pattern`pat`. The pattern can be an extended regular expression. See [Regular Expressions Overview](regular-expressions-overview.md) for details on the syntax for\
regular expressions (see also [PCRE Regular Expressions](pcre.md)).

Returns `1` if `expr` matches `pat` or `0` if it doesn't match. If either `expr` or `pat` are `NULL`, the result is `NULL`.

The negative form [NOT REGEXP](../not-regexp.md) also exists, as an alias for `NOT (string REGEXP pattern)`. `RLIKE` and `NOT RLIKE` are synonyms for `REGEXP` and `NOT REGEXP`, originally provided for mSQL compatibility.

The pattern need not be a literal string. For example, it can be specified as a string expression or table column.

**Note:** Because MariaDB uses the C escape syntax in strings (for example, "\n" to represent the newline character), you must double any "" that you use in your `REGEXP` strings.

`REGEXP` is not case sensitive, except when used with binary strings.

The [default\_regex\_flags](../../../../ha-and-performance/optimization-and-tuning/system-variables/server-system-variables.md#default_regex_flags) variable addresses the remaining compatibilities between PCRE and the old regex library.

## Examples

```sql
SELECT 'Monty!' REGEXP 'm%y%%';
+-------------------------+
| 'Monty!' REGEXP 'm%y%%' |
+-------------------------+
|                       0 |
+-------------------------+

SELECT 'Monty!' REGEXP '.*';
+----------------------+
| 'Monty!' REGEXP '.*' |
+----------------------+
|                    1 |
+----------------------+

SELECT 'new*\n*line' REGEXP 'new\\*.\\*line';
+---------------------------------------+
| 'new*\n*line' REGEXP 'new\\*.\\*line' |
+---------------------------------------+
|                                     1 |
+---------------------------------------+

SELECT 'a' REGEXP 'A', 'a' REGEXP BINARY 'A';
+----------------+-----------------------+
| 'a' REGEXP 'A' | 'a' REGEXP BINARY 'A' |
+----------------+-----------------------+
|              1 |                     0 |
+----------------+-----------------------+

SELECT 'a' REGEXP '^[a-d]';
+---------------------+
| 'a' REGEXP '^[a-d]' |
+---------------------+
|                   1 |
+---------------------+
```

### default\_regex\_flags examples

MariaDB uses the [default\_regex\_flags](../../../../ha-and-performance/optimization-and-tuning/system-variables/server-system-variables.md#default_regex_flags) variable to address the remaining compatibilities between PCRE and the old regex library.

The default behavior (multiline match is off)

```sql
SELECT 'a\nb\nc' RLIKE '^b$';
+---------------------------+
| '(?m)a\nb\nc' RLIKE '^b$' |
+---------------------------+
|                         0 |
+---------------------------+
```

Enabling the multiline option using the PCRE option syntax:

```sql
SELECT 'a\nb\nc' RLIKE '(?m)^b$';
+---------------------------+
| 'a\nb\nc' RLIKE '(?m)^b$' |
+---------------------------+
|                         1 |
+---------------------------+
```

Enabling the multiline option using default\_regex\_flags

```sql
SET default_regex_flags='MULTILINE';
SELECT 'a\nb\nc' RLIKE '^b$';
+-----------------------+
| 'a\nb\nc' RLIKE '^b$' |
+-----------------------+
|                     1 |
+-----------------------+
```

## See Also

* [Operator Precedence](../../../sql-structure/operators/operator-precedence.md)

<sub>_This page is licensed: GPLv2, originally from_</sub> [<sub>_fill\_help\_tables.sql_</sub>](https://github.com/MariaDB/server/blob/main/scripts/fill_help_tables.sql)

{% @marketo/form formId="4316" %}
