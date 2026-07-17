---
description: >-
  Release a prepared statement to free resources. This command removes the
  statement definition and its name from the current session.
---

# DEALLOCATE / DROP PREPARE

## Syntax

```bnf
{DEALLOCATE | DROP} PREPARE [LOCAL] stmt_name
```

## Description

To deallocate a prepared statement produced with [PREPARE](prepare-statement.md), use a`DEALLOCATE PREPARE` statement that refers to the prepared statement name.

A prepared statement is implicitly deallocated when a new `PREPARE` command is issued. In that case, there is no need to use `DEALLOCATE`.

Attempting to execute a prepared statement after deallocating it results in an error, as if it was not prepared at all:

```sql
ERROR 1243 (HY000): Unknown prepared statement handler (stmt_name) given to EXECUTE
```

If the specified statement has not been PREPAREd, an error similar to the following will be produced:

```sql
ERROR 1243 (HY000): Unknown prepared statement handler (stmt_name) given to DEALLOCATE PREPARE
```

### LOCAL Statement Names

{% hint style="info" %}
`{DEALLOCATE | DROP} PREPARE LOCAL` is available from MariaDB 13.1.1.
{% endhint %}

Inside a stored procedure, `LOCAL` deallocates the prepared statement whose name is the _value_ of the stored-procedure variable `spvar`:

```sql
{DEALLOCATE | DROP} PREPARE LOCAL spvar;
```

It is only valid inside a stored procedure, and like the plain form is not permitted in stored functions or triggers.

**Example:**

```sql
CREATE PROCEDURE p1()
BEGIN
  DECLARE spvar_with_ps_name VARCHAR(64) DEFAULT 'my_stmt';

  PREPARE my_stmt FROM 'SELECT 1';
  DEALLOCATE PREPARE LOCAL spvar_with_ps_name;
END;
```

## Example

See [example in PREPARE](prepare-statement.md#example).

## See Also

* [PREPARE Statement](prepare-statement.md)
* [EXECUTE Statement](execute-statement.md)
* [EXECUTE IMMEDIATE](execute-immediate.md)

<sub>_This page is licensed: GPLv2, originally from_</sub> [<sub>_fill\_help\_tables.sql_</sub>](https://github.com/MariaDB/server/blob/main/scripts/fill_help_tables.sql)

{% @marketo/form formId="4316" %}
