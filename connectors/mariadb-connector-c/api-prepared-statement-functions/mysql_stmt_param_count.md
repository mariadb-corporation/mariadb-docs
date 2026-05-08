---
description: >-
  mysql_stmt_param_count reports how many placeholder parameters a prepared
  statement contains, indicating the size of the MYSQL_BIND array required
  for binding.
---

# mysql\_stmt\_param\_count

## Syntax

```c
unsigned long mysql_stmt_param_count(MYSQL_STMT * stmt);
```

* `stmt` - a statement handle, which was previously allocated by [mysql\_stmt\_init()](mysql_stmt_init.md).

## Description

Returns the number of parameter markers present in the prepared statement.

{% hint style="info" %}
This function will not deliver a valid result until [mysql\_stmt\_prepare()](mysql_stmt_prepare.md) was called.
{% endhint %}

## See Also

* [mysql\_stmt\_prepare()](https://github.com/mariadb-corporation/docs-connectors/blob/test/mariadb-connector-c/mariadb-connectorc-api-prepared-statement-functions/mysql_stmt_prepare\(\)/README.md)
* [mysql\_stmt\_field\_count()](mysql_stmt_field_count.md)

{% @marketo/form formId="4316" %}
