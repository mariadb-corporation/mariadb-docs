---
description: >-
  Logical exclusive OR. XOR returns 1 if an odd number of operands is
  non-zero, 0 otherwise, and NULL if any operand is NULL.
---

# XOR

## Syntax

```bnf
XOR
```

## Description

`XOR` stands for eXclusive OR. Returns `NULL` if either operand is `NULL`. For non-`NULL` operands, evaluates to `1` if an odd number of operands is non-zero, otherwise `0` is returned.

## Examples

```sql
SELECT 1 XOR 1;
+---------+
| 1 XOR 1 |
+---------+
|       0 |
+---------+

SELECT 1 XOR 0;
+---------+
| 1 XOR 0 |
+---------+
|       1 |
+---------+

SELECT 1 XOR NULL;
+------------+
| 1 XOR NULL |
+------------+
|       NULL |
+------------+
```

`XOR` is evaluated from left to right. In the following example, the left `1 XOR 1` is evaluated first, and returns `0`. Then, `0 XOR 1` is evaluated, and `1` is returned.

```sql
SELECT 1 XOR 1 XOR 1;
+---------------+
| 1 XOR 1 XOR 1 |
+---------------+
|             1 |
+---------------+
```

## See Also

* [Operator Precedence](../operator-precedence.md)

<sub>_This page is licensed: GPLv2, originally from_</sub> [<sub>_fill\_help\_tables.sql_</sub>](https://github.com/MariaDB/server/blob/main/scripts/fill_help_tables.sql)

{% @marketo/form formId="4316" %}
