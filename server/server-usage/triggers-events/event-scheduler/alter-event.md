# ALTER EVENT

Modifies one or more characteristics of an existing event.

## Syntax

```
ALTER
    [DEFINER = { user | CURRENT_USER }]
    EVENT event_name
    [ON SCHEDULE schedule]
    [ON COMPLETION [NOT] PRESERVE]
    [RENAME TO new_event_name]
    [ENABLE | DISABLE | DISABLE ON SLAVE]
    [COMMENT 'comment']
    [DO sql_statement]
```

## Description

The `ALTER EVENT` statement is used to change one or more of the\
characteristics of an existing [event](events.md) without the need to drop and recreate it.\
The syntax for each of the `DEFINER`, `ON SCHEDULE`, `ON COMPLETION`,`COMMENT`, `ENABLE` `/` `DISABLE`, and `DO` clauses is exactly the\
same as when used with [CREATE EVENT](../../../reference/sql-statements/data-definition/create/create-event.md).

This statement requires the [EVENT](../../../reference/sql-statements/account-management-sql-statements/grant.md#database-privileges) privilege.\
When a user executes a successful `ALTER EVENT` statement, that user becomes\
the definer for the affected event.

(In MySQL 5.1.11 and earlier, an event could be altered only by its definer, or\
by a user having the [SUPER](../../../reference/sql-statements/account-management-sql-statements/grant.md#global-privileges) privilege.)

`ALTER EVENT` works only with an existing event:

```sql
ALTER EVENT no_such_event ON SCHEDULE EVERY '2:3' DAY_HOUR;
ERROR 1539 (HY000): Unknown event 'no_such_event'
```

## Examples

```sql
ALTER EVENT myevent 
  ON SCHEDULE AT CURRENT_TIMESTAMP + INTERVAL 2 HOUR 
  DO 
    UPDATE myschema.mytable SET mycol = mycol + 1;
```

## See Also

* [Events Overview](events.md)
* [CREATE EVENT](../../../reference/sql-statements/data-definition/create/create-event.md)
* [SHOW CREATE EVENT](../../../reference/sql-statements/administrative-sql-statements/show/show-create-event.md)
* [DROP EVENT](../../../reference/sql-statements/data-definition/drop/drop-event.md)

<sub>_This page is licensed: GPLv2, originally from [fill\_help\_tables.sql](https://github.com/MariaDB/server/blob/main/scripts/fill_help_tables.sql)_</sub>

{% @marketo/form formId="4316" %}
