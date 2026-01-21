---
description: >-
  List scheduled events. View metadata such as the event name, schedule, status,
  and timing for events in a database.
---

# SHOW EVENTS

## Syntax

```sql
SHOW EVENTS [{FROM | IN} schema_name]
    [LIKE 'pattern' | WHERE expr]
```

## Description

Shows information about Event Manager [events](../../../../server-usage/triggers-events/event-scheduler/events.md) (created with [CREATE EVENT](../../data-definition/create/create-event.md)). Requires the [EVENT](../../account-management-sql-statements/grant.md) privilege. Without any arguments, `SHOW EVENTS` lists all of the events in the current schema:

```sql
SELECT CURRENT_USER(), SCHEMA();
+----------------+----------+
| CURRENT_USER() | SCHEMA() |
+----------------+----------+
| jon@ghidora    | myschema |
+----------------+----------+

SHOW EVENTS\G
*************************** 1. row ***************************
                  Db: myschema
                Name: e_daily
             Definer: jon@ghidora
           Time zone: SYSTEM
                Type: RECURRING
          Execute at: NULL
      Interval value: 10
      Interval field: SECOND
              Starts: 2006-02-09 10:41:23
                Ends: NULL
              Status: ENABLED
          Originator: 0
character_set_client: latin1
collation_connection: latin1_swedish_ci
  Database Collation: latin1_swedish_ci
```

To see the event action, use [SHOW CREATE EVENT](show-create-event.md) instead, or look at the [information\_schema.EVENTS](../../../system-tables/information-schema/information-schema-tables/information-schema-events-table.md) table.

To see events for a specific schema, use the `FROM` clause. For example, to see events for the test schema, use the following statement:

```sql
SHOW EVENTS FROM test;
```

The `LIKE` clause, if present, indicates which event names to match. The `WHERE` clause can be given to select rows using more general conditions, as discussed in [Extended Show](extended-show.md).

<sub>_This page is licensed: GPLv2, originally from_</sub> [<sub>_fill\_help\_tables.sql_</sub>](https://github.com/MariaDB/server/blob/main/scripts/fill_help_tables.sql)

{% @marketo/form formId="4316" %}
