---
description: >-
  List stored procedures and their characteristics. View metadata like the
  database, name, type, and creator of stored procedures.
---

# SHOW PROCEDURE STATUS

## Syntax

```sql
SHOW PROCEDURE STATUS
    [LIKE 'pattern' | WHERE expr]
```

## Description

This statement is a MariaDB extension. It returns characteristics of a stored procedure, such as the database, name, type, creator, creation and modification dates, and character set information. A similar statement, [SHOW FUNCTION STATUS](show-function-status.md), displays information about stored functions.

The `LIKE` clause, if present, indicates which procedure or function names to match. The `WHERE` and `LIKE` clauses can be given to select rows using more general conditions, as discussed in [Extended SHOW](extended-show.md).

The [ROUTINES table](../../../system-tables/information-schema/information-schema-tables/information-schema-routines-table.md) in the INFORMATION\_SCHEMA database contains more detailed information.

## Examples

```sql
SHOW PROCEDURE STATUS LIKE 'p1'\G
*************************** 1. row ***************************
                  Db: test
                Name: p1
                Type: PROCEDURE
             Definer: root@localhost
            Modified: 2010-08-23 13:23:03
             Created: 2010-08-23 13:23:03
       Security_type: DEFINER
             Comment: 
character_set_client: latin1
collation_connection: latin1_swedish_ci
  Database Collation: latin1_swedish_ci
```

## See Also

* [Stored Procedure Overview](../../../../server-usage/stored-routines/stored-procedures/stored-procedure-overview.md)
* [CREATE PROCEDURE](../../../../server-usage/stored-routines/stored-procedures/create-procedure.md)
* [ALTER PROCEDURE](../../../../server-usage/stored-routines/stored-procedures/alter-procedure.md)
* [DROP PROCEDURE](../../../../server-usage/stored-routines/stored-procedures/drop-procedure.md)
* [SHOW CREATE PROCEDURE](show-create-procedure.md)
* [Stored Routine Privileges](../../../../server-usage/stored-routines/stored-functions/stored-routine-privileges.md)
* [Information Schema ROUTINES Table](../../../system-tables/information-schema/information-schema-tables/information-schema-routines-table.md)

<sub>_This page is licensed: GPLv2, originally from_</sub> [<sub>_fill\_help\_tables.sql_</sub>](https://github.com/MariaDB/server/blob/main/scripts/fill_help_tables.sql)

{% @marketo/form formId="4316" %}
