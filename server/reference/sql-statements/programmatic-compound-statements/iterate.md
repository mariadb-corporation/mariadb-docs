---
description: >-
  Restart the current loop. This statement jumps back to the beginning of a
  LOOP, REPEAT, or WHILE block, skipping any remaining statements in the current
  iteration.
---

# ITERATE

## Syntax

```sql
ITERATE label
```

`ITERATE` can appear only within [LOOP](loop.md), [REPEAT](repeat-loop.md), and [WHILE](while.md) statements.`ITERATE` means "do the loop again", and uses the statement's [label](labels.md) to determine which statements to repeat. The label must be in the same stored program, not in a caller procedure.

If you try to use `ITERATE` with a non-existing label, or if the label is associated to a construct which is not a loop, the following error will be produced:

```sql
ERROR 1308 (42000): ITERATE with no matching label: <label_name>
```

Below is an example of how `ITERATE` might be used:

```sql
CREATE PROCEDURE doiterate(p1 INT)
BEGIN
  label1: LOOP
    SET p1 = p1 + 1;
    IF p1 < 10 THEN ITERATE label1; END IF;
    LEAVE label1;
  END LOOP label1;
  SET @x = p1;
END
```

## See Also

* [LEAVE](leave.md) - Exits a loop (or any labeled code block)

<sub>_This page is licensed: GPLv2, originally from_</sub> [<sub>_fill\_help\_tables.sql_</sub>](https://github.com/MariaDB/server/blob/main/scripts/fill_help_tables.sql)

{% @marketo/form formId="4316" %}
