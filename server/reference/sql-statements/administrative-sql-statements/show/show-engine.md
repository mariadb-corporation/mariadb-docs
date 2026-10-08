---
description: >-
  Display status information for a storage engine. This statement retrieves
  operational logs or status details for a specific engine.
---

# SHOW ENGINE

## Syntax

```bnf
SHOW ENGINE [engine-name] {STATUS | MUTEX}
```

## Description

`SHOW ENGINE` displays operational information about a storage engine. The following statements are supported:

```sql
SHOW ENGINE INNODB STATUS
SHOW ENGINE INNODB MUTEX
SHOW ENGINE PERFORMANCE_SCHEMA STATUS
SHOW ENGINE ROCKSDB STATUS
```

If the [Sphinx Storage Engine](../../../../server-usage/storage-engines/sphinx-storage-engine/) is installed, the following is also supported:

```sql
SHOW ENGINE SPHINX STATUS
```

### SHOW ENGINE INNODB STATUS

`SHOW ENGINE INNODB STATUS` displays extensive information from the standard InnoDB Monitor about the state of the InnoDB storage engine. See [SHOW ENGINE INNODB STATUS](show-engine-innodb-status.md) for more.

### SHOW ENGINE INNODB MUTEX

`SHOW ENGINE INNODB MUTEX` is accepted for compatibility, but InnoDB returns no rows. To monitor InnoDB mutex and rw-lock waits, use the [Performance Schema](../../../system-tables/performance-schema/).

### SHOW ENGINE PERFORMANCE\_SCHEMA STATUS

This statement shows how much memory is used for [performance\_schema](../../../system-tables/performance-schema/) tables and internal buffers.

The output contains the following fields:

* Type: Always `performance_schema`.
* Name: The name of a table, the name of an internal buffer, or the `performance_schema` word, followed by a dot and an attribute. Internal buffers names are enclosed by parenthesis. `performance_schema` means that the attribute refers to the whole database (it is a total).
* Status: The value for the attribute.

The following attributes are shown, in this order, for all tables:

* row\_size: The memory used for an individual record. This value will never change.
* row\_count: The number of rows in the table or buffer. For some tables, this value depends on a server system variable.
* memory: For tables and `performance_schema`, this is the result of `row_size` \* `row_count`.

For internal buffers, the attributes are:

* count
* size

### SHOW ENGINE ROCKSDB STATUS

See also [MyRocks Performance Troubleshooting](../../../../server-usage/storage-engines/myrocks/myrocks-performance-troubleshooting.md)

<sub>_This page is licensed: GPLv2, originally from_</sub> [<sub>_fill\_help\_tables.sql_</sub>](https://github.com/MariaDB/server/blob/main/scripts/fill_help_tables.sql)

{% @marketo/form formId="4316" %}
