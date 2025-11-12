# Binary Logging of Stored Routines

Binary logging can be row-based, statement-based, or a mix of the two. See [Binary Log Formats](../../server-management/server-monitoring-logs/binary-log/binary-log-formats.md) for more details on the formats. If logging is statement-based, it is possible that a statement will have different effects on the master and on the slave.

Stored routines are particularly prone to this, for two main reasons:

* stored routines can be non-deterministic, in other words non-repeatable, and therefore have different results each time they are run.
* the slave thread executing the stored routine on the slave holds full privileges, while this may not be the case when the routine was run on the master.

The problems with replication will only occur with statement-based logging. If row-based logging is used, since changes are made to rows based on the master's rows, there is no possibility of the slave and master getting out of sync.

By default, with row-based replication, triggers run on the master, and the effects of their executions are replicated to the slaves. However, it is possible to run triggers on the slaves. See [Running triggers on the slave for Row-based events](../../ha-and-performance/standard-replication/running-triggers-on-the-replica-for-row-based-events.md).

## How MariaDB Handles Statement-Based Binary Logging of Routines

If the following criteria are met, then there are some limitations on whether stored routines can be created:

* The [binary log](../../server-management/server-monitoring-logs/binary-log/) is enabled, and the [binlog\_format](../../ha-and-performance/standard-replication/replication-and-binary-log-system-variables.md#binlog_format) system variable is set to `STATEMENT`. See [Binary Log Formats](../../server-management/server-monitoring-logs/binary-log/binary-log-formats.md) for more information.
* The [log\_bin\_trust\_function\_creators](../../ha-and-performance/standard-replication/replication-and-binary-log-system-variables.md#log_bin_trust_function_creators) is set to `OFF`, which is the default value.

If the above criteria are met, then the following limitations apply:

* When a [stored function](stored-functions/) is created, it must be declared as either `DETERMINISTIC`, `NO SQL` or `READS SQL DATA`, or else an error will occur. MariaDB cannot check whether a function is deterministic, and relies on the correct definition being used.
* To create or modify a stored function, a user requires the `SUPER` privilege as well as the regular privileges. See [Stored Routine Privileges](stored-functions/stored-routine-privileges.md) for these details.
* [Triggers](../triggers-events/triggers/) work in the same way, except that they are always assumed to be deterministic for logging purposes, even if this is obviously not the case, such as when they use the [UUID](../../reference/sql-functions/secondary-functions/miscellaneous-functions/uuid.md) function.
* [Triggers](../triggers-events/triggers/) can also update data. The slave uses the DEFINER attribute to determine which user is taken to have created the trigger.
* Note that the above limitations do no apply to [stored procedures](stored-procedures/) or to [events](../triggers-events/event-scheduler/events.md).

### Examples

A deterministic function:

```sql
DELIMITER //
 
CREATE FUNCTION trust_me(x INT)
RETURNS INT
DETERMINISTIC
READS SQL DATA
BEGIN
   RETURN (x);
END //
 
DELIMITER ;
```

A non-deterministic function, since it uses the [UUID\_SHORT](../../reference/sql-functions/secondary-functions/miscellaneous-functions/uuid_short.md) function:

```sql
DELIMITER //

CREATE FUNCTION dont_trust_me()
RETURNS INT
BEGIN
   RETURN UUID_SHORT();
END //

DELIMITER ;
```

<sub>_This page is licensed: CC BY-SA / Gnu FDL_</sub>

{% @marketo/form formId="4316" %}
