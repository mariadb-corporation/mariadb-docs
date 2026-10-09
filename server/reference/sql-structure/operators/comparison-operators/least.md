---
description: >-
  Return the smallest of two or more values. The arguments are compared as
  integers, reals, or strings depending on context, and NULL is returned if
  any is NULL.
---

# LEAST

## Syntax

```bnf
LEAST(value1,value2,...)
```

## Description

With two or more arguments, returns the smallest (minimum-valued) argument. The arguments are compared using the following rules:

* If the return value is used in an `INTEGER` context or all arguments are integer-valued, they are compared as integers.
* If the return value is used in a `REAL` context or all arguments are real-valued, they are compared as reals.
* If any argument is a case-sensitive string, the arguments are compared as case-sensitive strings.
* In all other cases, the arguments are compared as case-insensitive strings.

`LEAST()` returns `NULL` if any argument is `NULL`.

Invalid temporal arguments are an exception. An argument such as `DATE('')` returns `NULL` when selected on its own. Inside `LEAST()`, it is compared the same way as with the other [comparison operators](README.md):

* A string that cannot be read as a date, such as `''` or `'abc'`, is compared as the zero date `'0000-00-00'`.
* A date with an impossible day, such as `'2026-02-30'`, is compared as written.

Such an argument does not make the result `NULL`. The result is `NULL` only if the chosen value is not a valid date in the current [SQL mode](../../../../server-management/variables-and-modes/sql_mode.md). For example, `'0000-00-00'` is not valid when `NO_ZERO_DATE` is set.

## Examples

```sql
SELECT LEAST(2,0);
+------------+
| LEAST(2,0) |
+------------+
|          0 |
+------------+
```

```sql
SELECT LEAST(34.0,3.0,5.0,767.0);
+---------------------------+
| LEAST(34.0,3.0,5.0,767.0) |
+---------------------------+
|                       3.0 |
+---------------------------+
```

```sql
SELECT LEAST('B','A','C');
+--------------------+
| LEAST('B','A','C') |
+--------------------+
| A                  |
+--------------------+
```

`DATE('')` is `NULL` on its own, but `LEAST()` compares it as the zero date:

```sql
SELECT DATE(''), LEAST(DATE(''), '2026-10-05');
+----------+-------------------------------+
| DATE('') | LEAST(DATE(''), '2026-10-05') |
+----------+-------------------------------+
| NULL     | 0000-00-00                    |
+----------+-------------------------------+
```

An argument that is actually `NULL` makes the result `NULL`:

```sql
SELECT LEAST(NULL, '2026-10-05');
+---------------------------+
| LEAST(NULL, '2026-10-05') |
+---------------------------+
| NULL                      |
+---------------------------+
```

<sub>_This page is licensed: GPLv2, originally from_</sub> [<sub>_fill\_help\_tables.sql_</sub>](https://github.com/MariaDB/server/blob/main/scripts/fill_help_tables.sql)

{% @marketo/form formId="4316" %}
