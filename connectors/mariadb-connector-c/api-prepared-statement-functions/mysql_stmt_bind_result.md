---
description: >-
  mysql_stmt_bind_result maps result-set columns to application variables
  via an array of MYSQL_BIND structures, enabling mysql_stmt_fetch to
  populate those variables.
---

# mysql\_stmt\_bind\_result

## Syntax

```c
my_bool mysql_stmt_bind_result(MYSQL_STMT * stmt,
                               MYSQL_BIND * bind);
```

* `stmt` - a statement handle, which was previously allocated by [mysql\_stmt\_init()](mysql_stmt_init.md).
* `bind` - an array of [MYSQL\_BIND](connector-c-data-structures-and-definitions/mysql_bind.md) structures. The size of this array must be equal to the number of columns in result set.

## Description

Binds columns in the result set to variables. Returns zero on success, non-zero on failure.

{% hint style="info" %}
To determine the number of columns in result set use [mysql\_stmt\_field\_count()](mysql_stmt_field_count.md).

A column can be bound or rebound at any time, even after a result set has been partially retrieved. The new binding takes effect the next time [mysql\_stmt\_fetch()](mysql_stmt_fetch.md) is called.
{% endhint %}

## See Also

* [mysql\_stmt\_field\_count()](mysql_stmt_field_count.md)
* [mysql\_stmt\_execute()](mysql_stmt_execute.md)
* [mysql\_stmt\_fetch()](mysql_stmt_fetch.md)


{% @marketo/form formId="4316" %}
