# NOT IN

## Syntax

```bnf
expr NOT IN (value,...)
```

## Description

This is the same as `NOT` (`expr` [IN](in.md) (value,...)).

## Examples

```sql
SELECT 2 NOT IN (0,3,5,7);
+--------------------+
| 2 NOT IN (0,3,5,7) |
+--------------------+
|                  1 |
+--------------------+
```

```sql
SELECT 'wefwf' NOT IN ('wee','wefwf','weg');
+--------------------------------------+
| 'wefwf' NOT IN ('wee','wefwf','weg') |
+--------------------------------------+
|                                    0 |
+--------------------------------------+
```

```sql
SELECT 1 NOT IN ('1', '2', '3');
+--------------------------+
| 1 NOT IN ('1', '2', '3') |
+--------------------------+
|                        0 |
+--------------------------+
```

`NULL`:

```sql
SELECT NULL NOT IN (1, 2, 3);
+-----------------------+
| NULL NOT IN (1, 2, 3) |
+-----------------------+
|                  NULL |
+-----------------------+

SELECT 1 NOT IN (1, 2, NULL);
+-----------------------+
| 1 NOT IN (1, 2, NULL) |
+-----------------------+
|                     0 |
+-----------------------+

SELECT 5 NOT IN (1, 2, NULL);
+-----------------------+
| 5 NOT IN (1, 2, NULL) |
+-----------------------+
|                  NULL |
+-----------------------+
```

<sub>_This page is licensed: GPLv2, originally from_</sub> [<sub>_fill\_help\_tables.sql_</sub>](https://github.com/MariaDB/server/blob/main/scripts/fill_help_tables.sql)

{% @marketo/form formId="4316" %}
