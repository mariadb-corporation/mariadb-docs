# DROP FUNCTION

## Syntax

```sql
DROP FUNCTION [IF EXISTS] f_name
```

## Description

The `DROP FUNCTION` statement is used to drop a [stored function](./) or a user-defined function (UDF). That is, the specified routine is removed from the server, along with all privileges specific to the function. You must have the `ALTER ROUTINE` [privilege](../../../reference/sql-statements/account-management-sql-statements/grant.md) for the routine in order to drop it. If the [automatic\_sp\_privileges](../../../ha-and-performance/optimization-and-tuning/system-variables/server-system-variables.md#automatic_sp_privileges) server system variable is set, both the `ALTER ROUTINE` and `EXECUTE` privileges are granted automatically to the routine creator - see [Stored Routine Privileges](stored-routine-privileges.md).

#### IF EXISTS

The `IF EXISTS` clause is a MySQL/MariaDB extension. It prevents an error from occurring if the function does not exist. A`NOTE` is produced that can be viewed with [SHOW WARNINGS](../../../reference/sql-statements/administrative-sql-statements/show/show-warnings.md).

For dropping a [user-defined functions](../../user-defined-functions/) (UDF), see [DROP FUNCTION UDF](../../user-defined-functions/drop-function-udf.md).

## Examples

```sql
DROP FUNCTION hello;
Query OK, 0 rows affected (0.042 sec)

DROP FUNCTION hello;
ERROR 1305 (42000): FUNCTION test.hello does not exist

DROP FUNCTION IF EXISTS hello;
Query OK, 0 rows affected, 1 warning (0.000 sec)

SHOW WARNINGS;
+-------+------+------------------------------------+
| Level | Code | Message                            |
+-------+------+------------------------------------+
| Note  | 1305 | FUNCTION test.hello does not exist |
+-------+------+------------------------------------+
```

## See Also

* [DROP PROCEDURE](../stored-procedures/drop-procedure.md)
* [Stored Function Overview](stored-function-overview.md)
* [CREATE FUNCTION](../../../reference/sql-statements/data-definition/create/create-function.md)
* [CREATE FUNCTION UDF](../../user-defined-functions/create-function-udf.md)
* [ALTER FUNCTION](../../../reference/sql-statements/data-definition/alter/alter-function.md)
* [SHOW CREATE FUNCTION](../../../reference/sql-statements/administrative-sql-statements/show/show-create-function.md)
* [SHOW FUNCTION STATUS](../../../reference/sql-statements/administrative-sql-statements/show/show-function-status.md)
* [Stored Routine Privileges](stored-routine-privileges.md)
* [INFORMATION\_SCHEMA ROUTINES Table](../../../reference/system-tables/information-schema/information-schema-tables/information-schema-routines-table.md)

<sub>_This page is licensed: GPLv2, originally from_</sub> [<sub>_fill\_help\_tables.sql_</sub>](https://github.com/MariaDB/server/blob/main/scripts/fill_help_tables.sql)

{% @marketo/form formId="4316" %}
