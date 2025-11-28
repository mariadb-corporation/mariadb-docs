# Trigger Limitations

The following restrictions apply to [triggers](./).

* All of the restrictions listed in [Stored Routine Limitations](../../stored-routines/stored-routine-limitations.md).
* All of the restrictions listed in [Stored Function Limitations](../../stored-routines/stored-functions/stored-function-limitations.md).
* Triggers are always executed for each row. MariaDB does not support the standard `FOR EACH STATEMENT` option.
* Triggers cannot operate on any tables in the mysql, `information_schema` or `performance_schema` database.
* Cannot return a result set.
* The [RETURN](../../../reference/sql-statements/programmatic-compound-statements/return.md) statement is not permitted, since triggers don't return any values. Use [LEAVE](../../../reference/sql-statements/programmatic-compound-statements/leave.md) to immediately exit a trigger.
* Triggers are not activated by [foreign key](../../../ha-and-performance/optimization-and-tuning/optimization-and-indexes/foreign-keys.md) actions.
* If a trigger is loaded into cache, it is not automatically reloaded when the table metadata changes. In this case a trigger can operate using the outdated metadata.
* By default, with row-based replication, triggers run on the master, and the effects of their executions are replicated to the slaves. It is possible to run triggers on slaves. See [Running triggers on the slave for Row-based events](../../../ha-and-performance/standard-replication/running-triggers-on-the-replica-for-row-based-events.md).

## See Also

* [Trigger Overview](trigger-overview.md)
* [CREATE TRIGGER](create-trigger.md)
* [DROP TRIGGER](../../../reference/sql-statements/data-definition/drop/drop-trigger.md)
* [Information Schema TRIGGERS Table](../../../reference/system-tables/information-schema/information-schema-tables/information-schema-triggers-table.md)
* [SHOW TRIGGERS](../../../reference/sql-statements/administrative-sql-statements/show/show-triggers.md)
* [SHOW CREATE TRIGGER](../../../reference/sql-statements/administrative-sql-statements/show/show-create-trigger.md)

<sub>_This page is licensed: CC BY-SA / Gnu FDL_</sub>

{% @marketo/form formId="4316" %}
