---
description: >-
  Return the largest of two or more values. The arguments are compared using
  the same rules as for LEAST().
---

# GREATEST

## Syntax

```bnf
GREATEST(value1,value2,...)
```

## Description

With two or more arguments, returns the largest (maximum-valued) argument. The arguments are compared using the same rules as for [LEAST()](least.md). This includes how `NULL` and invalid temporal arguments such as `DATE('')` are handled.

## Examples

```sql
SELECT GREATEST(2,0);
+---------------+
| GREATEST(2,0) |
+---------------+
|             2 |
+---------------+
```

```sql
SELECT GREATEST(34.0,3.0,5.0,767.0);
+------------------------------+
| GREATEST(34.0,3.0,5.0,767.0) |
+------------------------------+
|                        767.0 |
+------------------------------+
```

```sql
SELECT GREATEST('B','A','C');
+-----------------------+
| GREATEST('B','A','C') |
+-----------------------+
| C                     |
+-----------------------+
```

`DATE('')` is `NULL` on its own, but `GREATEST()` compares it as the zero date, so the other argument wins:

```sql
SELECT GREATEST(DATE(''), '2026-10-05');
+----------------------------------+
| GREATEST(DATE(''), '2026-10-05') |
+----------------------------------+
| 2026-10-05                       |
+----------------------------------+
```

<sub>_This page is licensed: GPLv2, originally from_</sub> [<sub>_fill\_help\_tables.sql_</sub>](https://github.com/MariaDB/server/blob/main/scripts/fill_help_tables.sql)

{% @marketo/form formId="4316" %}
