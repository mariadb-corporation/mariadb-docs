---
description: >-
  mariadb_stmt_execute_direct prepares and executes a statement in a single
  call using a pre-allocated MYSQL_STMT handle, available in Connector/C 3.0
  with MariaDB 10.2 or later.
---

# mariadb\_stmt\_execute\_direct

## Syntax

```c
int mariadb_stmt_execute_direct(MYSQL_STMT * stmt, const char *query, size_t length);
```

* `stmt` - A statement handle, which was previously allocated by [mysql\_stmt\_init()](mysql_stmt_init.md).
* `query` SQL statement
* `length` Length of SQL statement

## Description

Prepares and executes a statement which was previously allocated by [mysql\_stmt\_init()](mysql_stmt_init.md), using the current values of the parameter variables if any parameters exist in the statement.

Returns zero on success, non-zero on failure.

This function was added in Connector/C 3.0 and requires [MariaDB 10.2](https://app.gitbook.com/s/aEnK0ZXmUbJzqQrTjFyb/community-server/old-releases/release-notes-mariadb-10-2-series/what-is-mariadb-102) or later versions.

{% hint style="info" %}
* Since the number of parameter of the statement is unknown before execution it is mandatory to set the number of parameters via the [mysql\_stmt\_attr\_set()](mysql_stmt_attr_set.md) function.
* If the SQL statement is a zero-terminated string, you can also pass -1 as length.
* The statement handle is intended for one-time execution. Reusing the statement handle might lead to unexpected behavior.
{% endhint %}

## See Also

* [mysql\_stmt\_attr\_set()](mysql_stmt_attr_set.md)
* [mysql\_stmt\_bind\_param()](mysql_stmt_bind_param.md)

## Example

```c
static int execute_direct_example(MYSQL *mysql)
{
  MYSQL_STMT *stmt= mysql_stmt_init(mysql);
  MYSQL_BIND bind[2];
  int intval= 1;
  int param_count= 2;
  char *strval= "execute_direct_example";

  /* Direct execution without parameters */
  if (mariadb_stmt_execute_direct(stmt, "CREATE TABLE execute_direct (a int, b varchar(30))", -1))
    goto error;

  memset(&bind, 0, sizeof(MYSQL_BIND) * 2);
  bind[0].buffer_type= MYSQL_TYPE_SHORT;
  bind[0].buffer= &intval;
  bind[1].buffer_type= MYSQL_TYPE_STRING;
  bind[1].buffer= strval;
  bind[1].buffer_length= strlen(strval);

  /* set number of parameters */
  if (mysql_stmt_attr_set(stmt, STMT_ATTR_PREBIND_PARAMS, &param_count))
    goto error;

  /* bind parameters */
  if (mysql_stmt_bind_param(stmt, bind))
    goto error;

  if (mariadb_stmt_execute_direct(stmt, "INSERT INTO execute_direct VALUES (?,?)", -1))
    goto error;

  mysql_stmt_close(stmt);
  return 0;
error:
  printf("Error: %s\n", mysql_stmt_error(stmt));
  mysql_stmt_close(stmt);
  return 1;
}
```

{% @marketo/form formId="4316" %}
