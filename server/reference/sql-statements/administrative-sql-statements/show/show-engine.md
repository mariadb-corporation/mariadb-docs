---
description: >-
  Display status information for a storage engine. This statement retrieves
  operational logs or status details for a specific engine.
---

# SHOW ENGINE

## Syntax

```sql
SHOW ENGINE [engine-name] {STATUS | MUTEX}
```

## Description

`SHOW ENGINE` displays operational information about a storage engine. The following statements currently are supported:

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

`SHOW ENGINE INNODB MUTEX` displays InnoDB mutex statistics.

The statement displays the following output fields:

* Type: Always InnoDB.
* Name: The source file where the mutex is implemented, and the line number in the file where the mutex is created. The line number is dependent on the MariaDB version.
* Status: This field displays the following values if `UNIV_DEBUG` was defined at compilation time (for example, in include/univ.h in the InnoDB part of the source tree). Only the `os_waits` value is displayed if `UNIV_DEBUG` was not defined. Without `UNIV_DEBUG`, the information on which the output is based is insufficient to distinguish regular mutexes and mutexes that protect rw-locks (which allow multiple readers or a single writer). Consequently, the output may appear to contain multiple rows for the same mutex.
  * count indicates how many times the mutex was requested.
  * spin\_waits indicates how many times the spinlock had to run.
  * spin\_rounds indicates the number of spinlock rounds. (spin\_rounds divided by spin\_waits provides the average round count.)
  * os\_waits indicates the number of operating system waits. This occurs when the spinlock did not work (the mutex was not locked during the spinlock and it was necessary to yield to the operating system and wait).
  * os\_yields indicates the number of times a the thread trying to lock a mutex gave up its timeslice and yielded to the operating system (on the presumption that allowing other threads to run will free the mutex so that it can be locked).
  * os\_wait\_times indicates the amount of time (in ms) spent in operating system waits, if the timed\_mutexes system variable is 1 (ON). If timed\_mutexes is 0 (OFF), timing is disabled, so os\_wait\_times is 0. timed\_mutexes is off by default.

Information from this statement can be used to diagnose system problems. For example, large values of spin\_waits and spin\_rounds may indicate scalability problems.

The [information\_schema](../../../system-tables/information-schema/).[INNODB\_MUTEXES](../../../system-tables/information-schema/information-schema-tables/information-schema-innodb-tables/information-schema-innodb_mutexes-table.md) table provides similar information.

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
