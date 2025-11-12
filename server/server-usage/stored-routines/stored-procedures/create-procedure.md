# CREATE PROCEDURE

## Syntax

{% tabs %}
{% tab title="Current" %}
```sql
CREATE
    [OR REPLACE]
    [DEFINER = { user | CURRENT_USER | role | CURRENT_ROLE }]
    PROCEDURE [IF NOT EXISTS] sp_name ([proc_parameter[,...]])
    [characteristic ...] routine_body

proc_parameter:
    [ IN | OUT | INOUT ] param_name type [DEFAULT value or expression]

type:
    Any valid MariaDB data type

characteristic:
    LANGUAGE SQL
  | [NOT] DETERMINISTIC
  | { CONTAINS SQL | NO SQL | READS SQL DATA | MODIFIES SQL DATA }
  | SQL SECURITY { DEFINER | INVOKER }
  | COMMENT 'string'

routine_body:
    Valid SQL procedure statement
```
{% endtab %}

{% tab title="< 11.8" %}
```sql
CREATE
    [OR REPLACE]
    [DEFINER = { user | CURRENT_USER | role | CURRENT_ROLE }]
    PROCEDURE [IF NOT EXISTS] sp_name ([proc_parameter[,...]])
    [characteristic ...] routine_body

proc_parameter:
    [ IN | OUT | INOUT ] param_name type

type:
    Any valid MariaDB data type

characteristic:
    LANGUAGE SQL
  | [NOT] DETERMINISTIC
  | { CONTAINS SQL | NO SQL | READS SQL DATA | MODIFIES SQL DATA }
  | SQL SECURITY { DEFINER | INVOKER }
  | COMMENT 'string'

routine_body:
    Valid SQL procedure statement
```
{% endtab %}
{% endtabs %}

## Description

Creates a [stored procedure](./). By default, a routine is associated with the default database. To associate the routine explicitly with a given database, specify the name as db\_name.sp\_name when you create it.

When the routine is invoked, an implicit `USE`` `_`db_name`_ is performed (and undone when the routine terminates). The causes the routine to have the given default database while it executes. USE statements within stored routines are disallowed.

When a stored procedure has been created, you invoke it by using the `CALL` statement (see [CALL](../../../reference/sql-statements/stored-routine-statements/call.md)).

To execute the `CREATE PROCEDURE` statement, it is necessary to have the `CREATE ROUTINE` privilege. By default, MariaDB automatically grants the `ALTER ROUTINE` and `EXECUTE` privileges to the routine creator. See also [Stored Routine Privileges](../stored-functions/stored-routine-privileges.md).

The `DEFINER` and SQL SECURITY clauses specify the security context to be used when checking access privileges at routine execution time, as described [here](../stored-functions/stored-routine-privileges.md). Requires the [SET USER](../../../reference/sql-statements/account-management-sql-statements/grant.md#set-user) privilege.

If the routine name is the same as the name of a built-in SQL function, you must use a space between the name and the following parenthesis when defining the routine, or a syntax error occurs. This is also true when you invoke the routine later. For this reason, we suggest that it is better to avoid re-using the names of existing SQL functions for your own stored routines.

The `IGNORE_SPACE` SQL mode applies to built-in functions, not to stored routines. It is always allowable to have spaces after a routine name, regardless of whether `IGNORE_SPACE` is enabled.

The parameter list enclosed within parentheses must always be present. If there are no parameters, an empty parameter list of `()` should be used. Parameter names are not case sensitive.

Each parameter can be declared to use any valid data type, except that the `COLLATE` attribute cannot be used.

For valid identifiers to use as procedure names, see [Identifier Names](../../../reference/sql-structure/sql-language-structure/identifier-names.md).

### Things to be Aware of With CREATE OR REPLACE

* One can't use `OR REPLACE` together with `IF EXISTS`.

## CREATE PROCEDURE IF NOT EXISTS

If the `IF NOT EXISTS` clause is used, then the procedure will only be created if a procedure with the same name does not already exist. If the procedure already exists, then a warning are triggered by default.

### IN/OUT/INOUT/IN OUT

Each parameter is an `IN` parameter by default. To specify otherwise for a parameter, use the keyword `OUT` or `INOUT` before the parameter name.

An `IN` parameter passes a value into a procedure. The procedure might modify the value, but the modification is not visible to the caller when the procedure returns. An `OUT` parameter passes a value from the procedure back to the caller. Its initial value is `NULL` within the procedure, and its value is visible to the caller when the procedure returns. An `INOUT` parameter is initialized by the caller, can be\
modified by the procedure, and any change made by the procedure is visible to the caller when the procedure returns.

For each `OUT` or `INOUT` parameter, pass a user-defined variable in the`CALL` statement that invokes the procedure so that you can obtain its value when the procedure returns. If you are calling the procedure\
from within another stored procedure or function, you can also pass a routine parameter or local routine variable as an `IN` or `INOUT` parameter.

### DEFAULT value or expression

As of [MariaDB 11.8](https://app.gitbook.com/s/aEnK0ZXmUbJzqQrTjFyb/community-server/11.8), each parameter can be defined as having a default value or expression. This can be useful if needing to add extra parameters to a procedure which is already in use.

### DETERMINISTIC/NOT DETERMINISTIC

`DETERMINISTIC` and `NOT DETERMINISTIC` apply only to [functions](../stored-functions/). Specifying `DETERMINISTC` or `NON-DETERMINISTIC` in procedures has no effect. The default value is `NOT DETERMINISTIC`. Functions are `DETERMINISTIC` when they always return the same value for the same input. For example, a truncate or substring function. Any function involving data, therefore, is always `NOT DETERMINISTIC`.

### CONTAINS SQL/NO SQL/READS SQL DATA/MODIFIES SQL DATA

`CONTAINS SQL`, `NO SQL`, `READS SQL DATA`, and `MODIFIES SQL DATA` are informative clauses that tell the server what the function does. MariaDB does not check in any way whether the specified clause is correct. If none of these clauses are specified, `CONTAINS SQL` is used by default.

`MODIFIES SQL DATA` means that the function contains statements that may modify data stored in databases. This happens if the function contains statements like [DELETE](../../../reference/sql-statements/data-manipulation/changing-deleting-data/delete.md), [UPDATE](../../../reference/sql-statements/data-manipulation/changing-deleting-data/update.md), [INSERT](../../../reference/sql-statements/data-manipulation/inserting-loading-data/insert.md), [REPLACE](../../../reference/sql-statements/data-manipulation/changing-deleting-data/replace.md) or DDL.

`READS SQL DATA` means that the function reads data stored in databases but does not modify any data. This happens if [SELECT](../../../reference/sql-statements/data-manipulation/selecting-data/select.md) statements are used, but there no write operations are executed.

`CONTAINS SQL` means that the function contains at least one SQL statement, but it does not read or write any data stored in a database. Examples include [SET](../../../reference/sql-statements/administrative-sql-statements/set-commands/set.md) or [DO](../../../reference/sql-statements/stored-routine-statements/do.md).

`NO SQL` means nothing, because MariaDB does not currently support any language other than SQL.

The routine\_body consists of a valid SQL procedure statement. This can be a simple statement such as [SELECT](../../../reference/sql-statements/data-manipulation/selecting-data/select.md) or [INSERT](../../../reference/sql-statements/data-manipulation/inserting-loading-data/insert.md), or it can be a compound statement written using [BEGIN and END](../../../reference/sql-statements/programmatic-compound-statements/begin-end.md). Compound statements can contain declarations, loops, and other control structure statements. See [Programmatic and Compound Statements](../../../reference/sql-statements/programmatic-compound-statements/) for syntax details.

MariaDB allows routines to contain DDL statements, such as `CREATE` and `DROP`. MariaDB also allows [stored procedures](./) (but not [stored functions](../stored-functions/)) to contain SQL transaction statements such as `COMMIT`.

For additional information about statements that are not allowed in stored routines, see [Stored Routine Limitations](../stored-routine-limitations.md).

### Invoking stored procedure from within programs

For information about invoking [stored procedures](./) from within programs written in a language that has a MariaDB/MySQL interface, see [CALL](../../../reference/sql-statements/stored-routine-statements/call.md).

### OR REPLACE

If the optional `OR REPLACE` clause is used, it acts as a shortcut for the following statements, with the exception that any existing [privileges](../stored-functions/stored-routine-privileges.md) for the procedure are not dropped:

```sql
DROP PROCEDURE IF EXISTS name;
CREATE PROCEDURE name ...;
```

### sql\_mode

MariaDB stores the [sql\_mode](../../../ha-and-performance/optimization-and-tuning/system-variables/server-system-variables.md#sql_mode) system variable setting that is in effect at the time a routine is created and always executes the routine with this setting in force, regardless of the server [SQL mode](../../../server-management/variables-and-modes/sql_mode.md) in effect when the routine is invoked.

### Character Sets and Collations

Procedure parameters can be declared with any character set/collation. If the character set and collation are not specifically set, the database defaults at the time of creation are used. If the database defaults change at a later stage, the stored procedure character set/collation will not be changed at the same time; the stored procedure needs to be dropped and recreated to ensure the same character set/collation as the database is used.

### Oracle Mode

A subset of Oracle's PL/SQL language is supported in addition to the traditional SQL/PSM-based MariaDB syntax. See [Oracle mode](https://app.gitbook.com/s/aEnK0ZXmUbJzqQrTjFyb/community-server/about/compatibility-and-differences/sql_modeoracle) for details on changes when running Oracle mode.

## Examples

The following example shows a simple stored procedure that uses an `OUT` parameter. It uses the `DELIMITER` command to set a new delimiter for the duration of the process — see [Delimiters in the mariadb client](../../../clients-and-utilities/mariadb-client/mariadb-command-line-client.md#delimiters).

```sql
DELIMITER //

CREATE PROCEDURE simpleproc (OUT param1 INT)
 BEGIN
  SELECT COUNT(*) INTO param1 FROM t;
 END;
//

DELIMITER ;

CALL simpleproc(@a);

SELECT @a;
+------+
| @a   |
+------+
|    1 |
+------+
```

Character set and collation:

```sql
DELIMITER //

CREATE PROCEDURE simpleproc2 (
  OUT param1 CHAR(10) CHARACTER SET 'utf8' COLLATE 'utf8_bin'
)
 BEGIN
  SELECT CONCAT('a'),f1 INTO param1 FROM t;
 END;
//

DELIMITER ;
```

`CREATE OR REPLACE`:

```sql
DELIMITER //

CREATE PROCEDURE simpleproc2 (
  OUT param1 CHAR(10) CHARACTER SET 'utf8' COLLATE 'utf8_bin'
)
 BEGIN
  SELECT CONCAT('a'),f1 INTO param1 FROM t;
 END;
//
ERROR 1304 (42000): PROCEDURE simpleproc2 already exists

DELIMITER ;

DELIMITER //

CREATE OR REPLACE PROCEDURE simpleproc2 (
  OUT param1 CHAR(10) CHARACTER SET 'utf8' COLLATE 'utf8_bin'
)
 BEGIN
  SELECT CONCAT('a'),f1 INTO param1 FROM t;
 END;
//
ERROR 1304 (42000): PROCEDURE simpleproc2 already exists

DELIMITER ;
Query OK, 0 rows affected (0.03 sec)
```

## See Also

* [Identifier Names](../../../reference/sql-structure/sql-language-structure/identifier-names.md)
* [Stored Procedure Overview](stored-procedure-overview.md)
* [ALTER PROCEDURE](alter-procedure.md)
* [DROP PROCEDURE](drop-procedure.md)
* [SHOW CREATE PROCEDURE](../../../reference/sql-statements/administrative-sql-statements/show/show-create-procedure.md)
* [SHOW PROCEDURE STATUS](../../../reference/sql-statements/administrative-sql-statements/show/show-procedure-status.md)
* [Stored Routine Privileges](../stored-functions/stored-routine-privileges.md)
* [Information Schema ROUTINES Table](../../../reference/system-tables/information-schema/information-schema-tables/information-schema-routines-table.md)

<sub>_This page is licensed: CC BY-SA / Gnu FDL_</sub>

{% @marketo/form formId="4316" %}
