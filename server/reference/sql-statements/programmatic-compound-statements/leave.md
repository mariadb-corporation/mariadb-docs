---
description: >-
  Exit a labeled block or loop immediately. This statement terminates the
  execution of the current loop or compound statement and continues after the
  block.
---

# LEAVE

## Syntax

```sql
LEAVE label
```

This statement is used to exit the flow control construct that has the given [label](labels.md). The label must be in the same stored program, not in a caller procedure. `LEAVE` can be used within [BEGIN ... END](begin-end.md) or loop constructs ([LOOP](loop.md), [REPEAT](repeat-loop.md), [WHILE](while.md)). In [Stored Procedures](../../../server-usage/stored-routines/stored-procedures/), [Triggers](../../../server-usage/triggers-events/triggers/) and [Events](../../../server-usage/triggers-events/event-scheduler/events.md), LEAVE can refer to the outmost `BEGIN ... END` construct; in that case, the program exits the procedure. In [Stored Functions](../../../server-usage/stored-routines/stored-functions/), [RETURN](return.md) can be used instead.

{% hint style="info" %}
`LEAVE` cannot be used to exit a [DECLARE HANDLER](declare-handler.md) block.
{% endhint %}

If you try to `LEAVE` a non-existing label, or if you try to `LEAVE` a `HANDLER` block, the following error will be produced:

```sql
ERROR 1308 (42000): LEAVE with no matching label: <label_name>
```

The following example uses `LEAVE` to exit the procedure if a condition is true:

```sql
CREATE PROCEDURE proc(IN p TINYINT)
CONTAINS SQL
`whole_proc`:
BEGIN
   SELECT 1;
   IF p < 1 THEN
      LEAVE `whole_proc`;
   END IF;
   SELECT 2;
END;

CALL proc(0);
+---+
| 1 |
+---+
| 1 |
+---+
```

## See Also

* [ITERATE](iterate.md) - Repeats a loop execution

<sub>_This page is licensed: GPLv2, originally from_</sub> [<sub>_fill\_help\_tables.sql_</sub>](https://github.com/MariaDB/server/blob/main/scripts/fill_help_tables.sql)

{% @marketo/form formId="4316" %}
