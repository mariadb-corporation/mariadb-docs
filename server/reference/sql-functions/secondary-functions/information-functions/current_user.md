---
description: >-
  Return the authenticated user name. This function displays the user name and
  host name combination used by the server to authenticate the current client.
---

# CURRENT\_USER

## Syntax

```sql
CURRENT_USER, CURRENT_USER()
```

## Description

Returns the user name and host name combination for the MariaDB account that the server used to authenticate the current client. This account determines your access privileges. The return value is a string in the utf8 [character set](../../../data-types/string-data-types/character-sets/).

The value of `CURRENT_USER()` can differ from the value of [USER()](user.md). [CURRENT\_ROLE()](current_role.md) returns the current active role.

Statements using the `CURRENT_USER` function are not [safe for statement-based replication](../../../../ha-and-performance/standard-replication/unsafe-statements-for-statement-based-replication.md).

## Examples

```sql
shell> mysql --user="anonymous"

SELECT USER(),CURRENT_USER();
+---------------------+----------------+
| USER()              | CURRENT_USER() |
+---------------------+----------------+
| anonymous@localhost | @localhost     |
+---------------------+----------------+
```

When calling `CURRENT_USER()` in a stored procedure, it returns the owner of the stored procedure, as defined with `DEFINER`.

## See Also

* [USER()](user.md)
* [SESSION\_USER()](session_user.md)
* [CREATE PROCEDURE](../../../../server-usage/stored-routines/stored-procedures/create-procedure.md)

<sub>_This page is licensed: GPLv2, originally from_</sub> [<sub>_fill\_help\_tables.sql_</sub>](https://github.com/MariaDB/server/blob/main/scripts/fill_help_tables.sql)

{% @marketo/form formId="4316" %}
