---
description: >-
  Session-scoped user-defined variables (@var), and how to set and use them.
---

# User-Defined Variables

User-defined variables are variables which can be created by the user and exist in the session. This means that no one can access user-defined variables that have been set by another user, and when the session is closed these variables expire. However, these variables can be shared between several queries and [stored programs](../../../server-usage/stored-routines/).

User-defined variables names must be preceded by a single _at_ character (`@`). While it is safe to use a reserved word as a user-variable name, the only allowed characters are ASCII letters, digits, dollar sign (`$`), underscore (`_`) and dot (`.`). If other characters are used, the name can be quoted in one of the following ways:

* @`var_name`
* @'var\_name'
* @"var\_name"

These characters can be escaped as usual.

User-variables names are case insensitive.

User-defined variables cannot be declared. They can be read even if no value has been set yet; in that case, they are `NULL`. To set a value for a user-defined variable you can use:

* [SET](../../sql-statements/administrative-sql-statements/set-commands/set.md) statement;
* [:=](../operators/assignment-operators/assignment-operator.md) operator within a SQL statement;
* [SELECT ... INTO](../../sql-statements/programmatic-compound-statements/selectinto.md).

Since user-defined variables type cannot be declared, the only way to force their type is using [CAST()](../../sql-functions/string-functions/cast.md) or [CONVERT()](../../sql-functions/string-functions/convert.md):

```sql
SET @str = CAST(123 AS CHAR(5));
```

If a variable has not been used yet, its value is `NULL`:

```sql
SELECT @x IS NULL;
+------------+
| @x IS NULL |
+------------+
|          1 |
+------------+
```

It is unsafe to read a user-defined variable and set its value in the same statement (unless the command is `SET`), because the order of these actions is undefined.

User-defined variables can be used in most MariaDB's statements and clauses which accept an SQL expression. However there are some exceptions, like the [LIMIT](../../sql-statements/data-manipulation/selecting-data/select.md#limit) clause.

They must be used to [PREPARE](../../sql-statements/prepared-statements/prepare-statement.md) a prepared statement:

```sql
@sql = 'DELETE FROM my_table WHERE c>1;';
PREPARE stmt FROM @sql;
EXECUTE stmt;
DEALLOCATE PREPARE stmt;
```

Another common use is to include a counter in a query:

```sql
SET @var = 0;
SELECT a, b, c, (@var:=@var+1) AS counter FROM my_table;
```

## Viewing

User-defined variables can be viewed by either querying the [USER\_VARIABLES](../../system-tables/information-schema/information-schema-tables/information-schema-user_variables-table.md), or by running `SHOW USER_VARIABLES`.

## Flushing User-Defined Variables

User-defined variables are reset and the [Information Schema table](../../system-tables/information-schema/information-schema-tables/information-schema-user_variables-table.md) emptied with the [FLUSH USER\_VARIABLES](../../sql-statements/administrative-sql-statements/flush-commands/flush.md) statement.

## Examples

```sql
SET @v1 = 0;
SET @v2 = 'abc';
SET @v3 = CAST(123 AS CHAR(5));

SHOW USER_VARIABLES;
+---------------+-------+
| Variable_name | Value |
+---------------+-------+
| v3            | 123   |
| v2            | abc   |
| v1            | 0     |
+---------------+-------+

SELECT * FROM information_schema.USER_VARIABLES ORDER BY VARIABLE_NAME;
+---------------+----------------+---------------+--------------------+
| VARIABLE_NAME | VARIABLE_VALUE | VARIABLE_TYPE | CHARACTER_SET_NAME |
+---------------+----------------+---------------+--------------------+
| v1            | 0              | INT           | latin1             |
| v2            | abc            | VARCHAR       | utf8               |
| v3            | 123            | VARCHAR       | utf8               |
+---------------+----------------+---------------+--------------------+

FLUSH USER_VARIABLES;

SELECT * FROM information_schema.USER_VARIABLES ORDER BY VARIABLE_NAME;
Empty set (0.000 sec)
```

## See Also

* [DECLARE VARIABLE](../../sql-statements/programmatic-compound-statements/declare-variable.md)
* [Performance Schema user\_variables\_by\_thread Table](../../system-tables/performance-schema/performance-schema-tables/performance-schema-user_variables_by_thread-table.md)
* [Information Schema USER\_VARIABLES Table](../../system-tables/information-schema/information-schema-tables/information-schema-user_variables-table.md)

<sub>_This page is licensed: CC BY-SA / Gnu FDL_</sub>

{% @marketo/form formId="4316" %}
