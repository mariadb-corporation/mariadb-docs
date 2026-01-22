---
description: >-
  The Information Schema TRIGGERS table contains detailed information about
  triggers, including the event, timing, and action statement.
---

# Information Schema TRIGGERS Table

The [Information Schema](../) `TRIGGERS` table contains information about [triggers](../../../../server-usage/triggers-events/triggers/).

It has the following columns:

| Column                        | Description                                                                                                                                                                                                                                                                                                      |
| ----------------------------- | ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| TRIGGER\_CATALOG              | Always def.                                                                                                                                                                                                                                                                                                      |
| TRIGGER\_SCHEMA               | Database name in which the trigger occurs.                                                                                                                                                                                                                                                                       |
| TRIGGER\_NAME                 | Name of the trigger.                                                                                                                                                                                                                                                                                             |
| EVENT\_MANIPULATION           | The event that activates the trigger. Prior to MariaDB 12.0, one of `INSERT`, `UPDATE` or `DELETE`. From MariaDB 12.0, can contain multiple values, comma-separated.                                                                                                                                             |
| EVENT\_OBJECT\_CATALOG        | Always def.                                                                                                                                                                                                                                                                                                      |
| EVENT\_OBJECT\_SCHEMA         | Database name on which the trigger acts.                                                                                                                                                                                                                                                                         |
| EVENT\_OBJECT\_TABLE          | Table name on which the trigger acts.                                                                                                                                                                                                                                                                            |
| ACTION\_ORDER                 | Indicates the order that the action will be performed in (of the list of a table's triggers with identical `EVENT_MANIPULATION` and `ACTION_TIMING` values). See the [FOLLOWS/PRECEDES](../../../../server-usage/triggers-events/triggers/create-trigger.md#follows-precedes-other_trigger_name) clauses.        |
| ACTION\_CONDITION             | `NULL`                                                                                                                                                                                                                                                                                                           |
| ACTION\_STATEMENT             | Trigger body, UTF-8 encoded.                                                                                                                                                                                                                                                                                     |
| ACTION\_ORIENTATION           | Always ROW.                                                                                                                                                                                                                                                                                                      |
| ACTION\_TIMING                | Whether the trigger acts `BEFORE` or `AFTER` the event that triggers it.                                                                                                                                                                                                                                         |
| ACTION\_REFERENCE\_OLD\_TABLE | Always `NULL`.                                                                                                                                                                                                                                                                                                   |
| ACTION\_REFERENCE\_NEW\_TABLE | Always `NULL`.                                                                                                                                                                                                                                                                                                   |
| ACTION\_REFERENCE\_OLD\_ROW   | Always `OLD`.                                                                                                                                                                                                                                                                                                    |
| ACTION\_REFERENCE\_NEW\_ROW   | Always `NEW`.                                                                                                                                                                                                                                                                                                    |
| CREATED                       | Always `NULL`.                                                                                                                                                                                                                                                                                                   |
| SQL\_MODE                     | The [SQL\_MODE](../../../../server-management/variables-and-modes/sql_mode.md) when the trigger was created, and which it uses for execution.                                                                                                                                                                    |
| DEFINER                       | The account that created the trigger, in the form user\_name@host\_name                                                                                                                                                                                                                                          |
| CHARACTER\_SET\_CLIENT        | The client [character set](../../../data-types/string-data-types/character-sets/) when the trigger was created, from the session value of the [character\_set\_client](../../../../ha-and-performance/optimization-and-tuning/system-variables/server-system-variables.md#character_set_client) system variable. |
| COLLATION\_CONNECTION         | The client [collation](../../../data-types/string-data-types/character-sets/) when the trigger was created, from the session value of the [collation\_connection](../../../../ha-and-performance/optimization-and-tuning/system-variables/server-system-variables.md#collation_connection) system variable.      |
| DATABASE\_COLLATION           | [Collation](../../../data-types/string-data-types/character-sets/) of the associated database.                                                                                                                                                                                                                   |

Queries to the `TRIGGERS` table will return information if the user has `non-SELECT` [privileges](../../../sql-statements/account-management-sql-statements/grant.md#column-privileges) on the columns. The columns `ACTION_CONDITION`, `ACTION_STATEMENT` and `DEFINER` are `NULL` unless the user has `TRIGGER` [privilege](../../../sql-statements/account-management-sql-statements/grant.md#table-privileges). Similar information is returned by the [SHOW TRIGGERS](../../../sql-statements/administrative-sql-statements/show/show-triggers.md) statement.

## See also

* [Trigger Overview](../../../../server-usage/triggers-events/triggers/trigger-overview.md)
* [CREATE TRIGGER](../../../../server-usage/triggers-events/triggers/create-trigger.md)
* [DROP TRIGGER](../../../sql-statements/data-definition/drop/drop-trigger.md)
* [SHOW TRIGGERS](../../../sql-statements/administrative-sql-statements/show/show-triggers.md)
* [SHOW CREATE TRIGGER](../../../sql-statements/administrative-sql-statements/show/show-create-trigger.md)
* [Trigger Limitations](../../../../server-usage/triggers-events/triggers/trigger-limitations.md)

<sub>_This page is licensed: CC BY-SA / Gnu FDL_</sub>

{% @marketo/form formId="4316" %}
