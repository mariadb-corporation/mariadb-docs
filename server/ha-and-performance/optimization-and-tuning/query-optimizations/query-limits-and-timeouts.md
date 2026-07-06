---
description: >-
  The methods MariaDB provides to limit or time out queries.
---

# Query Limits and Timeouts

This article describes the different methods MariaDB provides to limit/timeout a query:

## [LIMIT](../../../reference/sql-statements/data-manipulation/selecting-data/select.md#limit)

```sql
SELECT ... LIMIT row_count
OR
SELECT ... LIMIT OFFSET, row_count
OR
SELECT ... LIMIT row_count OFFSET OFFSET
```

The [LIMIT](../../../reference/sql-statements/data-manipulation/selecting-data/select.md#limit) clause restricts the number of returned rows.

## [LIMIT ROWS EXAMINED](limit-rows-examined.md)

```sql
SELECT ... LIMIT ROWS EXAMINED rows_limit;
```

Stops the query after 'rows\_limit' number of rows have been examined.

## sql\_safe\_updates

If the [sql\_safe\_updates](../system-variables/server-system-variables.md#sql_safe_updates) variable is set, one can't execute an [UPDATE](../../../reference/sql-statements/data-manipulation/changing-deleting-data/update.md) or [DELETE](../../../reference/sql-statements/data-manipulation/changing-deleting-data/delete.md)\
statement unless one specifies a key constraint in the `WHERE` clause or provide a `LIMIT` clause (or both).

```sql
SET @@SQL_SAFE_UPDATES=1
UPDATE tbl_name SET not_key_column=val;
-> ERROR 1175 (HY000): You are using safe update mode 
  and you tried to update a table without a WHERE that uses a KEY column
```

## sql\_select\_limit

[sql\_select\_limit](../system-variables/server-system-variables.md#sql_select_limit) acts as an automatic `LIMIT row_count` to any [SELECT](../../../reference/sql-statements/data-manipulation/selecting-data/select.md) query.

```sql
SET @@SQL_SELECT_LIMIT=1000
SELECT * FROM big_table;
```

The above is the same as:

```
SELECT * FROM big_table LIMIT 1000;
```

## max\_join\_size

If the [max\_join\_size](../system-variables/server-system-variables.md#max_join_size) variable (also called `sql_max_join_size`) is set, then it will limit\
any SELECT statements that probably need to examine more than`MAX_JOIN_SIZE` rows.

```sql
SET @@MAX_JOIN_SIZE=1000;
->ERROR 1104 (42000): The SELECT would examine more than MAX_JOIN_SIZE ROWS; 
SELECT COUNT(null_column) FROM big_table;
  CHECK your WHERE AND USE SET SQL_BIG_SELECTS=1 OR SET MAX_JOIN_SIZE=# IF the SELECT IS okay
```

## max\_statement\_time

If the [max\_statement\_time](../system-variables/server-system-variables.md#max_statement_time) variable is set, any query (excluding stored procedures) taking longer than the value of `max_statement_time` (specified in seconds) to execute will be aborted. This can be set globally, by session, as well as per user and per query. See [Aborting statements that take longer than a certain time to execute](aborting-statements.md).

## See Also

* [WAIT and NOWAIT](../../../reference/sql-statements/transactions/wait-and-nowait.md)
* [Aborting statements that take longer than a certain time to execute](aborting-statements.md)
* [lock\_wait\_timeout](../system-variables/server-system-variables.md#lock_wait_timeout) variable

<sub>_This page is licensed: CC BY-SA / Gnu FDL_</sub>

{% @marketo/form formId="4316" %}
