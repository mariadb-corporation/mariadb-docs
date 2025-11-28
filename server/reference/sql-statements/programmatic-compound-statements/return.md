---
description: >-
  Exit a stored function and return a value. This statement terminates function
  execution and sends the specified result back to the caller.
---

# RETURN

## Syntax

```sql
RETURN expr
```

The `RETURN` statement terminates execution of a [stored function](../../../server-usage/stored-routines/stored-functions/) and returns the value _`expr`_ to the function caller. There must be at least one `RETURN` statement in a stored function. If the function has multiple exit points, all exit points must have a `RETURN`.

This statement is not used in [stored procedures](../../../server-usage/stored-routines/stored-procedures/), [triggers](../../../server-usage/triggers-events/triggers/), or [events](../../../server-usage/triggers-events/event-scheduler/events.md). [LEAVE](leave.md) can be used instead.

The following example shows that `RETURN` can return the result of a [scalar subquery](../data-manipulation/selecting-data/joins-subqueries/subqueries/subqueries-scalar-subqueries.md):

```sql
CREATE FUNCTION users_count() RETURNS BOOL
   READS SQL DATA
BEGIN
   RETURN (SELECT COUNT(DISTINCT User) FROM mysql.user);
END;
```

<sub>_This page is licensed: GPLv2, originally from_</sub> [<sub>_fill\_help\_tables.sql_</sub>](https://github.com/MariaDB/server/blob/main/scripts/fill_help_tables.sql)

{% @marketo/form formId="4316" %}
