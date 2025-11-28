# Triggers and Implicit Locks

A [trigger](./) may reference multiple tables, and if a [LOCK TABLES](../../../reference/sql-statements/transactions/lock-tables.md) statement is used on one of the tables, other tables may at the same time also implicitly be locked due to the trigger.

If the trigger only reads from the other table, that table are read locked. If the trigger writes to the other table, it is write-locked. If a table is read-locked for reading via `LOCK TABLES`, but needs to be write-locked because it could be modified by a trigger, a write lock is taken.

All locks are acquired together when the `LOCK TABLES` statement is issued, and released together on `UNLOCK TABLES`.

## Example

```sql
LOCK TABLE table1 WRITE
```

Assume `table1` contains the following trigger:

```sql
CREATE TRIGGER trigger1 AFTER INSERT ON table1 FOR EACH ROW
BEGIN
  INSERT INTO table2 VALUES (1);
  UPDATE table3 SET writes = writes+1
    WHERE id = NEW.id AND EXISTS (SELECT id FROM table4);
END;
```

Not only is `table1` write locked, `table2` and `table3` are also write locked, due to the possible [INSERT](../../../reference/sql-statements/data-manipulation/inserting-loading-data/insert.md) and [UPDATE](../../../reference/sql-statements/data-manipulation/changing-deleting-data/update.md), while `table4` is read locked due to the [SELECT](../../../reference/sql-statements/data-manipulation/selecting-data/select.md).

<sub>_This page is licensed: CC BY-SA / Gnu FDL_</sub>

{% @marketo/form formId="4316" %}
