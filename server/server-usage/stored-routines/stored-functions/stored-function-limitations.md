# Stored Function Limitations

The following restrictions apply to [stored functions](./).

* All of the restrictions listed in [Stored Routine Limitations](../stored-routine-limitations.md).
* Any statements that return a result set are not permitted. For example, a regular [SELECTs](../../../reference/sql-statements/data-manipulation/selecting-data/select.md) is not permitted, but a [SELECT INTO](../../../reference/sql-statements/programmatic-compound-statements/selectinto.md) is. A cursor and [FETCH](../../../reference/sql-statements/programmatic-compound-statements/programmatic-compound-statements-cursors/fetch.md) statement is permitted.
* [FLUSH](../../../reference/sql-statements/administrative-sql-statements/flush-commands/flush.md) statements are not permitted.
* Statements that perform explicit or implicit commits or rollbacks are not permitted.
* Cannot be used recursively.
* Cannot make changes to a table that is already in use (reading or writing) by the statement invoking the stored function.
* Cannot refer to a temporary table multiple times under different aliases, even in different statements.
* ROLLBACK TO SAVEPOINT and RELEASE SAVEPOINT statement which are in a stored function cannot refer to a savepoint which has been defined out of the current function.
* Prepared statements ([PREPARE](../../../reference/sql-statements/prepared-statements/prepare-statement.md), [EXECUTE](../../../reference/sql-statements/prepared-statements/execute-statement.md), [DEALLOCATE PREPARE](../../../reference/sql-statements/prepared-statements/deallocate-drop-prepare.md)) cannot be used, and therefore nor can statements be constructed as strings and then executed.

<sub>_This page is licensed: CC BY-SA / Gnu FDL_</sub>

{% @marketo/form formId="4316" %}
