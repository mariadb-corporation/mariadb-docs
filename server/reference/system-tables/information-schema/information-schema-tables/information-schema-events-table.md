---
description: >-
  The Information Schema EVENTS table stores information about scheduled events
  on the server, including their timing, definition, and status.
---

# Information Schema EVENTS Table

The [Information Schema](../) `EVENTS` table stores information about [Events](../../../../server-usage/triggers-events/event-scheduler/) on the server.

It contains the following columns:

<table data-header-hidden="false" data-header-sticky><thead><tr><th>Column</th><th>Description</th></tr></thead><tbody><tr><td>EVENT_CATALOG</td><td>Always def.</td></tr><tr><td>EVENT_SCHEMA</td><td>Database where the event was defined.</td></tr><tr><td>EVENT_NAME</td><td>Event name.</td></tr><tr><td>DEFINER</td><td>Event definer.</td></tr><tr><td>TIME_ZONE</td><td>Time zone used for the event's scheduling and execution, by default SYSTEM.</td></tr><tr><td>EVENT_BODY</td><td>SQL.</td></tr><tr><td>EVENT_DEFINITION</td><td>The SQL defining the event.</td></tr><tr><td>EVENT_TYPE</td><td>Either ONE TIME or RECURRING.</td></tr><tr><td>EXECUTE_AT</td><td><a href="../../../data-types/date-and-time-data-types/datetime.md">DATETIME</a> when the event is set to execute, or NULL if recurring.</td></tr><tr><td>INTERVAL_VALUE</td><td>Numeric interval between event executions for a recurring event, or NULL if not recurring.</td></tr><tr><td>INTERVAL_FIELD</td><td>Interval unit (e.g., HOUR)</td></tr><tr><td>SQL_MODE</td><td>The <a href="../../../../server-management/variables-and-modes/sql_mode.md">SQL_MODE</a> at the time the event was created.</td></tr><tr><td>STARTS</td><td>Start <a href="../../../data-types/date-and-time-data-types/datetime.md">DATETIME</a> for a recurring event, NULL if not defined or not recurring.</td></tr><tr><td>ENDS</td><td>End <a href="../../../data-types/date-and-time-data-types/datetime.md">DATETIME</a> for a recurring event, NULL if not defined or not recurring.</td></tr><tr><td>STATUS</td><td>One of ENABLED, DISABLED or /SLAVESIDE_DISABLED.</td></tr><tr><td>ON_COMPLETION</td><td>The ON COMPLETION clause, either PRESERVE or NOT PRESERVE .</td></tr><tr><td>CREATED</td><td>When the event was created.</td></tr><tr><td>LAST_ALTERED</td><td>When the event was last changed.</td></tr><tr><td>LAST_EXECUTED</td><td>When the event was last run.</td></tr><tr><td>EVENT_COMMENT</td><td>The comment provided in the <a href="../../../sql-statements/data-definition/create/create-event.md">CREATE EVENT</a> statement, or an empty string if none.</td></tr><tr><td>ORIGINATOR</td><td>MariaDB server ID on which the event was created.</td></tr><tr><td>CHARACTER_SET_CLIENT</td><td><a href="../../../../ha-and-performance/optimization-and-tuning/system-variables/server-system-variables.md#character_set_client">character_set_client</a> system variable session value at the time the event was created.</td></tr><tr><td>COLLATION_CONNECTION</td><td><a href="../../../../ha-and-performance/optimization-and-tuning/system-variables/server-system-variables.md#collation_connection">collation_connection</a> system variable session value at the time the event was created.</td></tr><tr><td>DATABASE_COLLATION</td><td>Database <a href="../../../data-types/string-data-types/character-sets/">collation</a> with which the event is linked.</td></tr></tbody></table>

The [SHOW EVENTS](../../../sql-statements/administrative-sql-statements/show/show-events.md) and [SHOW CREATE EVENT](../../../sql-statements/administrative-sql-statements/show/show-create-event.md) statements provide similar information.

<sub>_This page is licensed: CC BY-SA / Gnu FDL_</sub>

{% @marketo/form formId="4316" %}
