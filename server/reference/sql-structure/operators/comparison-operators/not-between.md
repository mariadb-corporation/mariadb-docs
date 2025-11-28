# NOT BETWEEN

## Syntax

```sql
expr NOT BETWEEN min AND max
```

## Description

This is the same as `NOT` (`expr` [BETWEEN](between-and.md) `min` `AND` `max`).

Note that the meaning of the alternative form `NOT expr BETWEEN min AND max` is affected by the `HIGH_NOT_PRECEDENCE` [SQL\_MODE](../../../../server-management/variables-and-modes/sql_mode.md) flag.

## Examples

```sql
SELECT 1 NOT BETWEEN 2 AND 3;
+-----------------------+
| 1 NOT BETWEEN 2 AND 3 |
+-----------------------+
|                     1 |
+-----------------------+
```

```sql
SELECT 'b' NOT BETWEEN 'a' AND 'c';
+-----------------------------+
| 'b' NOT BETWEEN 'a' AND 'c' |
+-----------------------------+
|                           0 |
+-----------------------------+
```

`NULL`:

```sql
SELECT 1 NOT BETWEEN 1 AND NULL;
+--------------------------+
| 1 NOT BETWEEN 1 AND NULL |
+--------------------------+
|                     NULL |
+--------------------------+
```

<sub>_This page is licensed: GPLv2, originally from_</sub> [<sub>_fill\_help\_tables.sql_</sub>](https://github.com/MariaDB/server/blob/main/scripts/fill_help_tables.sql)

{% @marketo/form formId="4316" %}
