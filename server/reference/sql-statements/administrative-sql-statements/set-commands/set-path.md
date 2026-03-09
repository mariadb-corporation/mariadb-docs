# SET PATH

{% hint style="info" %}
This functionality is available from MariaDB 12.3.
{% endhint %}

## Syntax

```sql
SET PATH 'db1 [, db2 [, ...]]'
```

## Description

Sets the list of schemas (databases) that MariaDB uses to search for stored routines to invoke. Such a search happens in the `CALL` statement and when stored function are used in expressions.

The value of the path is a **string** which contains comma-separated schema names. A schema name can be quoted with backticks (or double quotes, as appropriate). A special name `CURRENT_SCHEMA` means to look in the current schema. Spaces are ignored, unless they are part of a quoted schema name. A path cannot contain two equivalent schema names.

The following two commands invoke the same stored procedure:

```sql
CALL sys.optimizer_switch_on();
```
and
```sql
SET PATH 'sys';
CALL optimizer_switch_on();
```

A default value of the path is `'CURRENT_SCHEMA'` which provides the traditional behavior — stored routines must be in the current database.

Also the path is used to look up packages in package routine invocations. Assuming there is a package `UTL_ENCODE` in the `sys` schema, and it contains the function `BASE64_DECODE()`, one can write

```sql
SELECT sys.UTL_ENCODE.BASE64_DECODE('data');
```
or
```sql
SET PATH='sys'; 
SELECT UTL_ENCODE.BASE64_DECODE('data');
```

### Notes

* This functionality introduces the `@@path` system variable (session and global).
* The `SET PATH` statement sets the `@@session.path` variable. It is also possible to assign a new value to the `@@path` variable directory, using a statement like this: `SET @@path='sys'`.
* Prepared statements, stored routines, and views remember the value of the path when they are created. The value of the path at the time of the execution does not apply.

## See Also

* [Preparable statements](../../prepared-statements/prepare-statement.md)

