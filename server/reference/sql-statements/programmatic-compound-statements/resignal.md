# RESIGNAL

## Syntax

```sql
RESIGNAL [error_condition]
    [SET error_property
    [, error_property] ...]

error_condition:
    SQLSTATE [VALUE] 'sqlstate_value'
  | condition_name

error_property:
    error_property_name = <error_property_value>

error_property_name:
    CLASS_ORIGIN
  | SUBCLASS_ORIGIN
  | MESSAGE_TEXT
  | MYSQL_ERRNO
  | CONSTRAINT_CATALOG
  | CONSTRAINT_SCHEMA
  | CONSTRAINT_NAME
  | CATALOG_NAME
  | SCHEMA_NAME
  | TABLE_NAME
  | COLUMN_NAME
  | CURSOR_NAME
```

## Description

The syntax of `RESIGNAL` and its semantics are very similar to [SIGNAL](signal.md). This statement can only be used within an error [HANDLER](declare-handler.md). It produces an error, like [SIGNAL](signal.md). `RESIGNAL` clauses are the same as `SIGNAL`, except that they all are optional, even [SQLSTATE](programmatic-compound-statements-diagnostics/sqlstate.md). All the properties which are not specified in `RESIGNAL`, will be identical to the properties of the error that was received by the error [HANDLER](../../sql-structure/nosql/handler/). For a description of the clauses, see [diagnostics area](programmatic-compound-statements-diagnostics/diagnostics-area.md).

{% hint style="info" %}
`RESIGNAL` does not empty the diagnostics area. It just appends another error condition.
{% endhint %}

`RESIGNAL`, without any clauses, produces an error which is identical to the error that was received by [HANDLER](../../sql-structure/nosql/handler/).

If used out of a [HANDLER](../../sql-structure/nosql/handler/) construct, RESIGNAL produces the following error:

```sql
ERROR 1645 (0K000): RESIGNAL when handler not active
```

{% tabs %}
{% tab title="Current" %}
If a [HANDLER](../../sql-structure/nosql/handler/) contains a [CALL](../stored-routine-statements/call.md) to another procedure, that procedure can use `RESIGNAL`, but trying to do this raises the above error.
{% endtab %}

{% tab title="< 5.6" %}
If a [HANDLER](../../sql-structure/nosql/handler/) contains a [CALL](../stored-routine-statements/call.md) to another procedure, that procedure can use `RESIGNAL`.
{% endtab %}
{% endtabs %}

For a list of `SQLSTATE` values and MariaDB error codes, see [MariaDB Error Codes](../../error-codes/mariadb-error-code-reference.md).

The following procedure tries to query two tables which don't exist, producing a 1146 error in both cases. Those errors will trigger the [HANDLER](../../sql-structure/nosql/handler/). The first time the error will be ignored, and the client will not receive it, but the second time, the error is re-signaled, so the client will receive it.

```sql
CREATE PROCEDURE test_error( )
BEGIN
   DECLARE CONTINUE HANDLER
      FOR 1146
   BEGIN
   IF @hide_errors IS FALSE THEN
      RESIGNAL;
   END IF;
   END;
   SET @hide_errors = TRUE;
   SELECT 'Next error will be ignored' AS msg;
   SELECT `c` FROM `temptab_one`;
   SELECT 'Next error won''t be ignored' AS msg;
   SET @hide_errors = FALSE;
   SELECT `c` FROM `temptab_two`;
END;

CALL test_error( );

+----------------------------+
| msg                        |
+----------------------------+
| Next error will be ignored |
+----------------------------+

+-----------------------------+
| msg                         |
+-----------------------------+
| Next error won't be ignored |
+-----------------------------+

ERROR 1146 (42S02): Table 'test.temptab_two' doesn't exist
```

The following procedure re-signals an error, modifying only the error message to clarify the cause of the problem.

```sql
CREATE PROCEDURE test_error()
BEGIN
   DECLARE CONTINUE HANDLER
   FOR 1146
   BEGIN
      RESIGNAL SET
      MESSAGE_TEXT = '`temptab` does not exist';
   END;
   SELECT `c` FROM `temptab`;
END;

CALL test_error( );
ERROR 1146 (42S02): `temptab` does not exist
```

```sql
CREATE PROCEDURE handle_error()
BEGIN
  RESIGNAL;
END;
CREATE PROCEDURE p()
BEGIN
  DECLARE EXIT HANDLER FOR SQLEXCEPTION CALL p();
  SIGNAL SQLSTATE '45000';
END;
```

## See Also

* [Diagnostics Area](programmatic-compound-statements-diagnostics/diagnostics-area.md)
* [SIGNAL](signal.md)
* [HANDLER](../../sql-structure/nosql/handler/)
* [Stored Routines](../../../server-usage/stored-routines/)
* [MariaDB Error Codes](../../error-codes/mariadb-error-code-reference.md)

<sub>_This page is licensed: CC BY-SA / Gnu FDL_</sub>

{% @marketo/form formId="4316" %}
