---
description: >-
  Understand the DUAL table. This dummy table allows selecting values without
  referencing a real table, often used for calculations or retrieving system
  variables.
---

# DUAL

## Description

You can use `DUAL` instead of a table name in situations where no tables are referenced, such as the following [SELECT](select.md) statement:

```sql
SELECT 1 + 1 FROM DUAL;
+-------+
| 1 + 1 |
+-------+
|     2 |
+-------+
```

`DUAL` is purely for the convenience of people who require that all `SELECT` statements should have`FROM` and possibly other clauses. MariaDB ignores the clauses. MariaDB does not require `FROM DUAL` if no tables are referenced.

FROM DUAL could be used when you only SELECT computed values, but require a `WHERE` clause, perhaps to test that a script correctly handles empty resultsets:

```sql
SELECT 1 FROM DUAL WHERE FALSE;
Empty set (0.00 sec)
```

## See Also

* [SELECT](select.md)

<sub>_This page is licensed: GPLv2, originally from_</sub> [<sub>_fill\_help\_tables.sql_</sub>](https://github.com/MariaDB/server/blob/main/scripts/fill_help_tables.sql)

{% @marketo/form formId="4316" %}
