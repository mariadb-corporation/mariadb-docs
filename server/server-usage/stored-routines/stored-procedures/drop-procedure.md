# DROP PROCEDURE

## Syntax

```sql
DROP PROCEDURE [IF EXISTS] sp_name
```

## Description

This statement is used to drop a [stored procedure](./). That is, the specified routine is removed from the server along with all privileges specific to the [procedure](../../../reference/sql-statements/account-management-sql-statements/grant.md). You must have the `ALTER ROUTINE` privilege for the routine. If the [automatic\_sp\_privileges](../../../reference/sql-statements/account-management-sql-statements/grant.md) server system variable is set, that privilege and `EXECUTE` are granted automatically to the routine creator - see [Stored Routine Privileges](../stored-functions/stored-routine-privileges.md).

The `IF EXISTS` clause is a MySQL/MariaDB extension. It prevents an error from occurring if the procedure or function does not exist. A`NOTE` is produced that can be viewed with [SHOW WARNINGS](../../../reference/sql-statements/administrative-sql-statements/show/show-warnings.md).

While this statement takes effect immediately, threads which are executing a procedure can continue execution.

## Examples

```sql
DROP PROCEDURE simpleproc;
```

IF EXISTS:

```sql
DROP PROCEDURE simpleproc;
ERROR 1305 (42000): PROCEDURE test.simpleproc does not exist

DROP PROCEDURE IF EXISTS simpleproc;
Query OK, 0 rows affected, 1 warning (0.00 sec)

SHOW WARNINGS;
+-------+------+------------------------------------------+
| Level | Code | Message                                  |
+-------+------+------------------------------------------+
| Note  | 1305 | PROCEDURE test.simpleproc does not exist |
+-------+------+------------------------------------------+
```

## See Also

* [DROP FUNCTION](../stored-functions/drop-function.md)
* [Stored Procedure Overview](stored-procedure-overview.md)
* [CREATE PROCEDURE](create-procedure.md)
* [ALTER PROCEDURE](drop-procedure.md)
* [SHOW CREATE PROCEDURE](../../../reference/sql-statements/administrative-sql-statements/show/show-create-procedure.md)
* [SHOW PROCEDURE STATUS](../../../reference/sql-statements/administrative-sql-statements/show/show-procedure-status.md)
* [Information Schema ROUTINES Table](../../../reference/system-tables/information-schema/information-schema-tables/information-schema-routines-table.md)

<sub>_This page is licensed: GPLv2, originally from_</sub> [<sub>_fill\_help\_tables.sql_</sub>](https://github.com/MariaDB/server/blob/main/scripts/fill_help_tables.sql)

{% @marketo/form formId="4316" %}
