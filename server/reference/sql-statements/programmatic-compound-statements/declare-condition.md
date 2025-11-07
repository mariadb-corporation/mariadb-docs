# DECLARE CONDITION

## Syntax

```sql
DECLARE condition_name CONDITION FOR condition_value

condition_value:
    SQLSTATE [VALUE] sqlstate_value
  | mysql_error_code
```

## Description

The `DECLARE ... CONDITION` statement defines a named error condition. It specifies a condition that needs specific handling and associates a name with that condition. Later, the name can be used in a [DECLARE ... HANDLER](declare-handler.md), [SIGNAL](signal.md) or [RESIGNAL](resignal.md) statement (as long as the statement is located in the same [BEGIN ... END](begin-end.md) block).

Conditions must be declared after [local variables](declare-variable.md), but before [CURSORs](programmatic-compound-statements-cursors/) and [HANDLERs](declare-handler.md).

A condition\_value for `DECLARE ... CONDITION` can be an [SQLSTATE](programmatic-compound-statements-diagnostics/sqlstate.md) value (a 5-character string literal) or a MySQL error code (a number). You should not use `SQLSTATE` value '00000' or MySQL error code 0, because those indicate success rather than an error condition. If you try, or if you specify an invalid `SQLSTATE` value, an error like this is produced:

```sql
ERROR 1407 (42000): Bad SQLSTATE: '00000'
```

For a list of `SQLSTATE` values and MariaDB error codes, see [MariaDB Error Codes](../../error-codes/mariadb-error-code-reference.md).

<sub>_This page is licensed: GPLv2, originally from_</sub> [<sub>_fill\_help\_tables.sql_</sub>](https://github.com/MariaDB/server/blob/main/scripts/fill_help_tables.sql)

{% @marketo/form formId="4316" %}
