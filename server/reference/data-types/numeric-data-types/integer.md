---
description: Synonym for INT. This keyword declares a standard 4-byte integer column.
---

# INTEGER

## Syntax

```sql
INTEGER[(M)] [SIGNED | UNSIGNED | ZEROFILL]
```

## Description

This type is a synonym for [INT](int.md).

## EXAMPLES

```sql
CREATE TABLE integer_example (
  example INTEGER
);
```

```sql
SHOW CREATE TABLE integer_example\G

*************************** 1. row ***************************
       Table: integer_example
Create Table: CREATE TABLE `integer_example` (
  `example` int(11) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=latin1
```

<sub>_This page is licensed: GPLv2, originally from_</sub> [<sub>_fill\_help\_tables.sql_</sub>](https://github.com/MariaDB/server/blob/main/scripts/fill_help_tables.sql)

{% @marketo/form formId="4316" %}
