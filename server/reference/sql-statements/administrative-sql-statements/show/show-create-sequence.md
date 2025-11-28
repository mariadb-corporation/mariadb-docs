---
description: >-
  View the SQL used to create a sequence. This statement displays the CREATE
  SEQUENCE statement with current parameter values.
---

# SHOW CREATE SEQUENCE

## Syntax

```sql
SHOW CREATE SEQUENCE sequence_name;
```

## Description

Shows the [CREATE SEQUENCE](../../../sql-structure/sequences/create-sequence.md) statement that creates the given [sequence](../../../sql-structure/sequences/). The statement requires the `SELECT` privilege for the table.

`SHOW CREATE SEQUENCE` quotes identifiers according to the value of the [sql\_quote\_show\_create](../../../../ha-and-performance/optimization-and-tuning/system-variables/server-system-variables.md#sql_quote_show_create) system variable.

## Example

```sql
CREATE SEQUENCE s1 START WITH 50;
SHOW CREATE SEQUENCE s1\G;
*************************** 1. row ***************************
       Table: s1
Create Table: CREATE SEQUENCE `s1` start with 50 minvalue 1 maxvalue 9223372036854775806 
  increment by 1 cache 1000 nocycle ENGINE=InnoDB
```

## Notes

If you want to see the underlying table structure used for the `SEQUENCE` you can use [SHOW CREATE TABLE](show-create-table.md) on the `SEQUENCE`. You can also use `SELECT` to read the current recorded state of the `SEQUENCE`:

```sql
SHOW CREATE TABLE s1\G
*************************** 1. row ***************************
       Table: s1
Create Table: CREATE TABLE `s1` (
  `next_not_cached_value` bigint(21) NOT NULL,
  `minimum_value` bigint(21) NOT NULL,
  `maximum_value` bigint(21) NOT NULL,
  `start_value` bigint(21) NOT NULL COMMENT 'start value when sequences is created 
     or value if RESTART is used',
  `increment` bigint(21) NOT NULL COMMENT 'increment value',
  `cache_size` bigint(21) unsigned NOT NULL,
  `cycle_option` tinyint(1) unsigned NOT NULL COMMENT '0 if no cycles are allowed, 
     1 if the sequence should begin a new cycle when maximum_value is passed',
  `cycle_count` bigint(21) NOT NULL COMMENT 'How many cycles have been done'
) ENGINE=InnoDB SEQUENCE=1

SELECT * FROM s1\G
*************************** 1. row ***************************
next_not_cached_value: 50
        minimum_value: 1
        maximum_value: 9223372036854775806
          start_value: 50
            increment: 1
           cache_size: 1000
         cycle_option: 0
          cycle_count: 0
```

The [Information Schema SEQUENCES Table](../../../system-tables/information-schema/information-schema-tables/information-schema-sequences-table.md) also provides information about available sequences:

```sql
SELECT * FROM INFORMATION_SCHEMA.SEQUENCES\G
*************************** 1. row ***************************
       SEQUENCE_CATALOG: def
        SEQUENCE_SCHEMA: test
          SEQUENCE_NAME: s1
              DATA_TYPE: bigint
      NUMERIC_PRECISION: 64
NUMERIC_PRECISION_RADIX: 2
          NUMERIC_SCALE: 0
            START_VALUE: 50
          MINIMUM_VALUE: 1
          MAXIMUM_VALUE: 9223372036854775806
              INCREMENT: 1
           CYCLE_OPTION: 0
```

## See Also

* [CREATE SEQUENCE](../../../sql-structure/sequences/create-sequence.md)
* [ALTER SEQUENCE](../../../sql-structure/sequences/alter-sequence.md)
* [Information Schema SEQUENCES Table](../../../system-tables/information-schema/information-schema-tables/information-schema-sequences-table.md)

<sub>_This page is licensed: CC BY-SA / Gnu FDL_</sub>

{% @marketo/form formId="4316" %}
