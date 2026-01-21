---
description: >-
  Calculate population standard deviation. This function is a synonym for STD()
  and STDDEV_POP(), returning the square root of the population variance.
---

# STDDEV

## Syntax

```sql
STDDEV(expr)
```

## Description

Returns the population standard deviation of _`expr`_. This function is provided for compatibility with Oracle. The standard SQL function [STDDEV\_POP()](stddev_pop.md) can be used instead.

It is an [aggregate function](./), and so can be used with the [GROUP BY](../../sql-statements/data-manipulation/selecting-data/group-by.md) clause.

`STDDEV()` can be used as a [window function](../special-functions/window-functions/).

This function returns `NULL` if there were no matching rows.

## Examples

As an [aggregate function](./):

```sql
CREATE OR REPLACE TABLE stats (category VARCHAR(2), x INT);

INSERT INTO stats VALUES 
  ('a',1),('a',2),('a',3),
  ('b',11),('b',12),('b',20),('b',30),('b',60);

SELECT category, STDDEV_POP(x), STDDEV_SAMP(x), VAR_POP(x) 
  FROM stats GROUP BY category;
+----------+---------------+----------------+------------+
| category | STDDEV_POP(x) | STDDEV_SAMP(x) | VAR_POP(x) |
+----------+---------------+----------------+------------+
| a        |        0.8165 |         1.0000 |     0.6667 |
| b        |       18.0400 |        20.1693 |   325.4400 |
+----------+---------------+----------------+------------+
```

As a [window function](../special-functions/window-functions/):

```sql
CREATE OR REPLACE TABLE student_test (name CHAR(10), test CHAR(10), score TINYINT);

INSERT INTO student_test VALUES 
    ('Chun', 'SQL', 75), ('Chun', 'Tuning', 73), 
    ('Esben', 'SQL', 43), ('Esben', 'Tuning', 31), 
    ('Kaolin', 'SQL', 56), ('Kaolin', 'Tuning', 88), 
    ('Tatiana', 'SQL', 87);

SELECT name, test, score, STDDEV_POP(score) 
  OVER (PARTITION BY test) AS stddev_results FROM student_test;
+---------+--------+-------+----------------+
| name    | test   | score | stddev_results |
+---------+--------+-------+----------------+
| Chun    | SQL    |    75 |        16.9466 |
| Chun    | Tuning |    73 |        24.1247 |
| Esben   | SQL    |    43 |        16.9466 |
| Esben   | Tuning |    31 |        24.1247 |
| Kaolin  | SQL    |    56 |        16.9466 |
| Kaolin  | Tuning |    88 |        24.1247 |
| Tatiana | SQL    |    87 |        16.9466 |
+---------+--------+-------+----------------+
```

## See Also

* [STDDEV\_POP](stddev_pop.md) (equivalent, standard SQL)
* [STD](std.md) (equivalent, non-standard SQL)
* [VAR\_POP](var_pop.md) (variance)
* [STDDEV\_SAMP](stddev_samp.md) (sample standard deviation)

<sub>_This page is licensed: GPLv2, originally from_</sub> [<sub>_fill\_help\_tables.sql_</sub>](https://github.com/MariaDB/server/blob/main/scripts/fill_help_tables.sql)

{% @marketo/form formId="4316" %}
