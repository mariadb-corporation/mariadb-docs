---
description: >-
  Display the internal instruction representation of a stored procedure. This
  debug statement shows the low-level opcodes of the routine.
---

# SHOW PROCEDURE CODE

## Syntax

```sql
SHOW PROCEDURE CODE proc_name
```

## Description

This statement is a MariaDB extension that is available only for servers that have been built with debugging support. It displays a representation of the internal implementation of the named [stored procedure](../../../../server-usage/stored-routines/stored-procedures/). A similar statement, [SHOW FUNCTION CODE](show-function-code.md), displays information about [stored functions](../../../../server-usage/stored-routines/stored-functions/).

Both statements require that you be the owner of the routine or have [SELECT](../../account-management-sql-statements/grant.md) access to the [mysql.proc](../../../system-tables/the-mysql-database-tables/mysql-proc-table.md) table.

If the named routine is available, each statement produces a result set. Each row in the result set corresponds to one "instruction" in the routine. The first column is Pos, which is an ordinal number beginning with 0. The second column is Instruction, which contains an SQL statement (usually changed from the original source), or a directive which has meaning only to the stored-routine handler.

## Examples

```sql
DELIMITER //

CREATE PROCEDURE p1 ()
  BEGIN
    DECLARE fanta INT DEFAULT 55;
    DROP TABLE t2;
    LOOP
      INSERT INTO t3 VALUES (fanta);
      END LOOP;
  END//
Query OK, 0 rows affected (0.00 sec)

SHOW PROCEDURE CODE p1//
+-----+----------------------------------------+
| Pos | Instruction                            |
+-----+----------------------------------------+
|   0 | set fanta@0 55                         |
|   1 | stmt 9 "DROP TABLE t2"                 |
|   2 | stmt 5 "INSERT INTO t3 VALUES (fanta)" |
|   3 | jump 2                                 |
+-----+----------------------------------------+
```

## See Also

* [Stored Procedure Overview](../../../../server-usage/stored-routines/stored-procedures/stored-procedure-overview.md)
* [CREATE PROCEDURE](../../../../server-usage/stored-routines/stored-procedures/create-procedure.md)
* [ALTER PROCEDURE](../../../../server-usage/stored-routines/stored-procedures/alter-procedure.md)
* [DROP PROCEDURE](../../../../server-usage/stored-routines/stored-procedures/drop-procedure.md)
* [SHOW CREATE PROCEDURE](show-create-procedure.md)
* [SHOW PROCEDURE STATUS](show-procedure-status.md)
* [Stored Routine Privileges](../../../../server-usage/stored-routines/stored-functions/stored-routine-privileges.md)
* [Information Schema ROUTINES Table](../../../system-tables/information-schema/information-schema-tables/information-schema-routines-table.md)

<sub>_This page is licensed: GPLv2, originally from_</sub> [<sub>_fill\_help\_tables.sql_</sub>](https://github.com/MariaDB/server/blob/main/scripts/fill_help_tables.sql)

{% @marketo/form formId="4316" %}
