---
description: >-
  The Information Schema EVENTS table stores information about scheduled events
  on the server, including their timing, definition, and status.
---

# Information Schema EVENTS Table

The [Information Schema](../) `EVENTS` table stores information about [Events](../../../../server-usage/triggers-events/event-scheduler/) on the server.

It contains the following columns:

| Column                 | Description                                                                                                                                                                                                        |
| ---------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ |
| EVENT\_CATALOG         | Always def.                                                                                                                                                                                                        |
| EVENT\_SCHEMA          | Database where the event was defined.                                                                                                                                                                              |
| EVENT\_NAME            | Event name.                                                                                                                                                                                                        |
| DEFINER                | Event definer.                                                                                                                                                                                                     |
| TIME\_ZONE             | Time zone used for the event's scheduling and execution, by default SYSTEM.                                                                                                                                        |
| EVENT\_BODY            | SQL.                                                                                                                                                                                                               |
| EVENT\_DEFINITION      | The SQL defining the event.                                                                                                                                                                                        |
| EVENT\_TYPE            | Either ONE TIME or RECURRING.                                                                                                                                                                                      |
| EXECUTE\_AT            | [DATETIME](../../../data-types/date-and-time-data-types/datetime.md) when the event is set to execute, or NULL if recurring.                                                                                       |
| INTERVAL\_VALUE        | Numeric interval between event executions for a recurring event, or NULL if not recurring.                                                                                                                         |
| INTERVAL\_FIELD        | Interval unit (e.g., HOUR)                                                                                                                                                                                         |
| SQL\_MODE              | The [SQL\_MODE](../../../../server-management/variables-and-modes/sql_mode.md) at the time the event was created.                                                                                                  |
| STARTS                 | Start [DATETIME](../../../data-types/date-and-time-data-types/datetime.md) for a recurring event, NULL if not defined or not recurring.                                                                            |
| ENDS                   | End [DATETIME](../../../data-types/date-and-time-data-types/datetime.md) for a recurring event, NULL if not defined or not recurring.                                                                              |
| STATUS                 | One of ENABLED, DISABLED or /SLAVESIDE\_DISABLED.                                                                                                                                                                  |
| ON\_COMPLETION         | The ON COMPLETION clause, either PRESERVE or NOT PRESERVE .                                                                                                                                                        |
| CREATED                | When the event was created.                                                                                                                                                                                        |
| LAST\_ALTERED          | When the event was last changed.                                                                                                                                                                                   |
| LAST\_EXECUTED         | When the event was last run.                                                                                                                                                                                       |
| EVENT\_COMMENT         | The comment provided in the [CREATE EVENT](../../../sql-statements/data-definition/create/create-event.md) statement, or an empty string if none.                                                                  |
| ORIGINATOR             | MariaDB server ID on which the event was created.                                                                                                                                                                  |
| CHARACTER\_SET\_CLIENT | [character\_set\_client](../../../../ha-and-performance/optimization-and-tuning/system-variables/server-system-variables.md#character_set_client) system variable session value at the time the event was created. |
| COLLATION\_CONNECTION  | [collation\_connection](../../../../ha-and-performance/optimization-and-tuning/system-variables/server-system-variables.md#collation_connection) system variable session value at the time the event was created.  |
| DATABASE\_COLLATION    | Database [collation](../../../data-types/string-data-types/character-sets/) with which the event is linked.                                                                                                        |

The [SHOW EVENTS](../../../sql-statements/administrative-sql-statements/show/show-events.md) and [SHOW CREATE EVENT](../../../sql-statements/administrative-sql-statements/show/show-create-event.md) statements provide similar information.

<sub>_This page is licensed: CC BY-SA / Gnu FDL_</sub>

{% @marketo/form formId="4316" %}
