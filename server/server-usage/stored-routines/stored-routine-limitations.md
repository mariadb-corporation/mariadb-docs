---
description: >-
  Stored routines have specific restrictions, such as prohibiting certain SQL
  statements (e.g., LOAD DATA) and disallowing result sets in functions.
---

# Stored Routine Limitations

The following SQL statements are not permitted inside any [stored routines](./) ([stored functions](stored-functions/), [stored procedures](stored-procedures/), [events](../triggers-events/event-scheduler/events.md) or [triggers](../triggers-events/triggers/)).

* [ALTER VIEW](../views/alter-view.md); you can use [CREATE OR REPLACE VIEW](../views/create-view.md) instead.
* [LOAD DATA](../../reference/sql-statements/data-manipulation/inserting-loading-data/load-data-into-tables-or-index/load-data-infile.md) and [LOAD TABLE](../../ha-and-performance/standard-replication/obsolete-replication-information/load-table-from-master-removed.md).
* [CHANGE MASTER TO](../../reference/sql-statements/administrative-sql-statements/replication-statements/change-master-to.md)
* [INSERT DELAYED](../../reference/sql-statements/data-manipulation/inserting-loading-data/insert-delayed.md) is permitted, but the statement is handled as a regular [INSERT](../../reference/sql-statements/data-manipulation/inserting-loading-data/insert.md).
* [LOCK TABLES](../../reference/sql-statements/transactions/lock-tables.md) and [UNLOCK TABLES](../../reference/sql-statements/transactions/lock-tables.md).
* References to [local variables](../../reference/sql-statements/programmatic-compound-statements/declare-variable.md) within prepared statements inside a stored routine (use [user-defined variables](../../reference/sql-structure/sql-language-structure/user-defined-variables.md) instead).
* [BEGIN (WORK)](../../reference/sql-statements/transactions/start-transaction.md) is treated as the beginning of a [BEGIN END](../../reference/sql-statements/programmatic-compound-statements/begin-end.md) block, not a transaction, so [START TRANSACTION](../../reference/sql-statements/transactions/start-transaction.md) needs to be used instead.
* The number of permitted recursive calls is limited to [max\_sp\_recursion\_depth](../../ha-and-performance/optimization-and-tuning/system-variables/server-system-variables.md#max_sp_recursion_depth). If this variable is 0 (default), recursivity is disabled. The limit does not apply to stored functions.
* Most statements that are not permitted in prepared statements are not permitted in stored programs. See [Prepare Statement:Permitted statements](../../reference/sql-statements/prepared-statements/prepare-statement.md#permitted-statements) for a list of statements that can be used. [SIGNAL](../../reference/sql-statements/programmatic-compound-statements/signal.md), [RESIGNAL](../../reference/sql-statements/programmatic-compound-statements/resignal.md) and [GET DIAGNOSTICS](../../reference/sql-statements/programmatic-compound-statements/programmatic-compound-statements-diagnostics/get-diagnostics.md) are exceptions, and may be used in stored routines.

There are also further limitations specific to the kind of stored routine.

Note that, if a stored program calls another stored program, the latter will inherit the caller's limitations. So, for example, if a stored procedure is called by a stored function, that stored procedure will not be able to produce a result set, because stored functions can't do this.

## See Also

* [Stored Function Limitations](stored-functions/stored-function-limitations.md)
* [Trigger Limitations](../triggers-events/triggers/trigger-limitations.md)
* [Event Limitations](../triggers-events/event-scheduler/event-limitations.md)

<sub>_This page is licensed: CC BY-SA / Gnu FDL_</sub>

{% @marketo/form formId="4316" %}
