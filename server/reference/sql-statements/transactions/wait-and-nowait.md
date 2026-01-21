---
description: >-
  Control lock wait behavior. These clauses allow statements to wait for a
  specific timeout or fail immediately if a lock cannot be acquired.
---

# WAIT and NOWAIT

Extended syntax so that it is possible to set [innodb\_lock\_wait\_timeout](../../../server-usage/storage-engines/innodb/innodb-system-variables.md#innodb_lock_wait_timeout) and [lock\_wait\_timeout](../../../ha-and-performance/optimization-and-tuning/system-variables/server-system-variables.md#lock_wait_timeout) for the following statements:

## Syntax

```sql
ALTER TABLE tbl_name [WAIT n|NOWAIT] ...
CREATE ... INDEX ON tbl_name (index_col_name, ...) [WAIT n|NOWAIT] ...
DROP INDEX ... [WAIT n|NOWAIT]
DROP TABLE tbl_name [WAIT n|NOWAIT] ...
LOCK TABLE ... [WAIT n|NOWAIT]
OPTIMIZE TABLE tbl_name [WAIT n|NOWAIT]
RENAME TABLE tbl_name [WAIT n|NOWAIT] ...
SELECT ... FOR UPDATE [WAIT n|NOWAIT]
SELECT ... LOCK IN SHARE MODE [WAIT n|NOWAIT]
TRUNCATE TABLE tbl_name [WAIT n|NOWAIT]
```

## Description

The lock wait timeout can be explicitly set in the statement by using either `WAIT n` (to set the wait in seconds) or `NOWAIT`, in which case the statement will immediately fail if the lock cannot be obtained. `WAIT 0` is equivalent to `NOWAIT`.

## See Also

* [Query Limits and Timeouts](../../../ha-and-performance/optimization-and-tuning/query-optimizations/query-limits-and-timeouts.md)
* [ALTER TABLE](../data-definition/alter/alter-table/)
* [CREATE INDEX](../data-definition/create/create-index.md)
* [DROP INDEX](../data-definition/drop/drop-index.md)
* [DROP TABLE](../data-definition/drop/drop-table.md)
* [LOCK TABLES and UNLOCK TABLES](lock-tables.md)
* [OPTIMIZE TABLE](../../../ha-and-performance/optimization-and-tuning/optimizing-tables/optimize-table.md)
* [RENAME TABLE](../data-definition/rename-table.md)
* [SELECT](../data-manipulation/selecting-data/select.md)
* [TRUNCATE TABLE](../table-statements/truncate-table.md)

<sub>_This page is licensed: CC BY-SA / Gnu FDL_</sub>

{% @marketo/form formId="4316" %}
