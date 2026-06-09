---
description: >-
  mysql_stmt_bind_param binds an array of MYSQL_BIND variables to the parameter
  markers in a prepared statement before it is executed via mysql_stmt_execute.
---

# mysql\_stmt\_bind\_param

## Syntax

```c
my_bool mysql_stmt_bind_param(MYSQL_STMT * stmt,
                              MYSQL_BIND * bnd);
```

## Parameters

* `stmt` - a statement handle, which was previously allocated by [mysql\_stmt\_init()](mysql_stmt_init.md).
* `bind` - an array of `MYSQL_BIND` structures. The size of this array must be equal to the number of parameters.

## Description

Binds variables for parameter markers in the prepared statement that was passed to [mysql\_stmt\_prepare()](mysql_stmt_prepare.md). Returns zero on success, non-zero on failure.

## Notes

* The number of parameters can be obtained by [mysql\_stmt\_param\_count()](mysql_stmt_param_count.md).
* If the number of parameters is unknown, for example when using [mariadb\_stmt\_execute\_direct()](mariadb_stmt_execute_direct.md), the number of parameters have to be specified with the [mysql\_stmt\_attr\_set()](mysql_stmt_attr_set.md) function.

## See Also

* [mariadb\_stmt\_execute\_direct()](mariadb_stmt_execute_direct.md)
* [mysql\_stmt\_prepare()](mysql_stmt_prepare.md)
* [mysql\_stmt\_bind\_result()](mysql_stmt_bind_result.md)
* [mysql\_stmt\_execute()](mysql_stmt_execute.md)
* [mysql\_stmt\_param\_count()](mysql_stmt_param_count.md)
* [mysql\_stmt\_send\_long\_data()](mysql_stmt_send_long_data.md)

{% @marketo/form formId="4316" %}
