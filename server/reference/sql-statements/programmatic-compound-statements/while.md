---
description: >-
  Execute a block while a condition is true. This loop construct checks a
  condition before each iteration and repeats the block as long as the condition
  holds.
---

# WHILE

## Syntax

```sql
[begin_label:] WHILE search_condition DO
    statement_list
END WHILE [end_label]
```

## Description

The statement list within a `WHILE` statement is repeated as long as the`search_condition` is true. statement\_list consists of one or more statements. If the loop must be executed at least once, [REPEAT ... LOOP](repeat-loop.md) can be used instead.

A `WHILE` statement can be [labeled](labels.md). `end_label` cannot be given unless `begin_label` also is present. If both are present, they must be the same.

## Examples

```sql
CREATE PROCEDURE dowhile()
BEGIN
  DECLARE v1 INT DEFAULT 5;

  WHILE v1 > 0 DO
    ...
    SET v1 = v1 - 1;
  END WHILE;
END
```

<sub>_This page is licensed: GPLv2, originally from_</sub> [<sub>_fill\_help\_tables.sql_</sub>](https://github.com/MariaDB/server/blob/main/scripts/fill_help_tables.sql)

{% @marketo/form formId="4316" %}
