---
description: >-
  Execute an expression repeatedly. This function runs a scalar expression a
  specified number of times, primarily for measuring query execution speed.
---

# BENCHMARK

## Syntax

```sql
BENCHMARK(count,expr)
```

## Description

The BENCHMARK() function executes the expression `expr` repeatedly `count` times. It may be used to time how quickly MariaDB processes the expression. The result value is always 0. The intended use is from within the [mariadb client](../../../../clients-and-utilities/mariadb-client/mariadb-command-line-client.md), which reports query execution times.

## Examples

```sql
SELECT BENCHMARK(1000000,ENCODE('hello','goodbye'));
+----------------------------------------------+
| BENCHMARK(1000000,ENCODE('hello','goodbye')) |
+----------------------------------------------+
|                                            0 |
+----------------------------------------------+
1 row in set (0.21 sec)
```

<sub>_This page is licensed: GPLv2, originally from_</sub> [<sub>_fill\_help\_tables.sql_</sub>](https://github.com/MariaDB/server/blob/main/scripts/fill_help_tables.sql)

{% @marketo/form formId="4316" %}
