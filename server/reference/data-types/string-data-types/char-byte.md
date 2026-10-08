---
description: >-
  Fixed-length binary string type. This type stores a fixed number of bytes,
  padding with zero bytes if the data is shorter.
---

# CHAR BYTE

## Description

The `CHAR BYTE` data type is an alias for the [BINARY](binary.md) data type. This is a compatibility feature.

## EXAMPLES

```sql
CREATE TABLE char_byte_example (
  example CHAR BYTE
);
```

```sql
SHOW CREATE TABLE char_byte_example\G
```

```sql
*************************** 1. row ***************************
       Table: char_byte_example
Create Table: CREATE TABLE `char_byte_example` (
  `example` binary(1) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=latin1
```

<sub>_This page is licensed: GPLv2, originally from_</sub> [<sub>_fill\_help\_tables.sql_</sub>](https://github.com/MariaDB/server/blob/main/scripts/fill_help_tables.sql)

{% @marketo/form formId="4316" %}
