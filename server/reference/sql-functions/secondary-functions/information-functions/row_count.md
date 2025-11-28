---
description: >-
  Count rows affected by the last statement. This function returns the number of
  rows inserted, updated, or deleted by the previous DML operation.
---

# ROW\_COUNT

## Syntax

```sql
ROW_COUNT()
```

## Description

`ROW_COUNT()` returns the number of rows updated, inserted or deleted by the preceding statement. This is the same as the row count that the mariadb client displays and the value from the [mysql\_affected\_rows()](https://app.gitbook.com/s/CjGYMsT2MVP4nd3IyW2L/mariadb-connector-c/api-functions/mysql_affected_rows) C API function.

Generally:

* For statements which return a result set (such as [SELECT](../../../sql-statements/data-manipulation/selecting-data/select.md), [SHOW](../../../sql-statements/administrative-sql-statements/show/), [DESC](../../../sql-statements/administrative-sql-statements/describe.md) or [HELP](../../../sql-statements/administrative-sql-statements/help-command.md)), returns -1, even when the result set is empty. This is also true for administrative statements, such as [OPTIMIZE](../../../../ha-and-performance/optimization-and-tuning/optimizing-tables/optimize-table.md).
* For DML statements other than [SELECT](../../../sql-statements/data-manipulation/selecting-data/select.md) and for [ALTER TABLE](../../../sql-statements/data-definition/alter/), returns the number of affected rows.
* For DDL statements (including [TRUNCATE](../../numeric-functions/truncate.md)) and for other statements which don't return any result set (such as [USE](../../../sql-statements/administrative-sql-statements/use-database.md), [DO](../../../sql-statements/stored-routine-statements/do.md), [SIGNAL](../../../sql-statements/programmatic-compound-statements/signal.md) or [DEALLOCATE PREPARE](../../../sql-statements/prepared-statements/deallocate-drop-prepare.md)), returns 0.

For [UPDATE](../../../sql-statements/data-manipulation/changing-deleting-data/update.md), affected rows is by default the number of rows that were actually changed. If the CLIENT\_FOUND\_ROWS flag to [mysql\_real\_connect()](https://app.gitbook.com/s/CjGYMsT2MVP4nd3IyW2L/mariadb-connector-c/api-functions/mysql_real_connect) is specified when connecting to mariadbd, affected rows is instead the number of rows matched by the WHERE clause.

For [REPLACE](../../../sql-statements/data-manipulation/changing-deleting-data/replace.md), deleted rows are also counted. So, if REPLACE deletes a row and adds a new row, `ROW_COUNT()` returns 2.

For [INSERT ... ON DUPLICATE KEY](../../../sql-statements/data-manipulation/inserting-loading-data/insert-on-duplicate-key-update.md), values returned are as follows:

* 0: an existing row is set to its current values, and the `CLIENT_FOUND_ROWS` is not set.
* 1: the values are inserted as a new row, or an existing row is set to its current values, and the `CLIENT_FOUND_ROWS` is set.
* 2: an existing row is updated with new values.

`ROW_COUNT()` does not take into account rows that are not directly deleted/updated by the last statement. This means that rows deleted by foreign keys or triggers are not counted.

**Warning:** You can use `ROW_COUNT()` with prepared statements, but you need to call it after `EXECUTE`, not after [DEALLOCATE PREPARE](../../../sql-statements/prepared-statements/deallocate-drop-prepare.md), because the row count for allocate prepare is always 0.

**Warning:** When used after a [CALL](../../../sql-statements/stored-routine-statements/call.md) statement, this function returns the number of rows affected by the last statement in the procedure, not by the whole procedure.

**Warning:** After [INSERT DELAYED](../../../sql-statements/data-manipulation/inserting-loading-data/insert-delayed.md), `ROW_COUNT()` returns the number of the rows you tried to insert, not the number of the successful writes.

This information can also be found in the [diagnostics area](../../../sql-statements/programmatic-compound-statements/programmatic-compound-statements-diagnostics/diagnostics-area.md).

Statements using the `ROW_COUNT()` function are not [safe for statement-based replication](../../../../ha-and-performance/standard-replication/unsafe-statements-for-statement-based-replication.md).

## Examples

```sql
CREATE TABLE t (A INT);

INSERT INTO t VALUES(1),(2),(3);

SELECT ROW_COUNT();
+-------------+
| ROW_COUNT() |
+-------------+
|           3 |
+-------------+

DELETE FROM t WHERE A IN(1,2);

SELECT ROW_COUNT(); 
+-------------+
| ROW_COUNT() |
+-------------+
|           2 |
+-------------+
```

Example with prepared statements:

```sql
SET @q = 'INSERT INTO t VALUES(1),(2),(3);';

PREPARE stmt FROM @q;

EXECUTE stmt;
Query OK, 3 rows affected (0.39 sec)
Records: 3  Duplicates: 0  Warnings: 0

SELECT ROW_COUNT();
+-------------+
| ROW_COUNT() |
+-------------+
|           3 |
+-------------+
```

## See Also

* [FOUND\_ROWS()](found_rows.md)

<sub>_This page is licensed: GPLv2, originally from_</sub> [<sub>_fill\_help\_tables.sql_</sub>](https://github.com/MariaDB/server/blob/main/scripts/fill_help_tables.sql)

{% @marketo/form formId="4316" %}
