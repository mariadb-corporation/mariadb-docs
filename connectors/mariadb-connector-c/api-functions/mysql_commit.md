---
description: >-
  mysql_commit commits the current transaction on a MariaDB Connector/C
  connection, returning zero on success without affecting autocommit mode.
---

# mysql\_commit

## Syntax

```c
my_bool mysql_commit(MYSQL * mysql);
```

## Parameter

* `mysql` - a `mysql` handle, which was previously allocated by [mysql\_init()](mysql_init.md) or [mysql\_real\_connect()](mysql_real_connect.md).

## Description

Commits the current transaction for the specified database connection.&#x20;

## Return Value

Returns zero on success, nonzero if an error occurred.

{% hint style="info" %}
Executing mysql\_commit() will not affected the behaviour of [autocommit](https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/server-management/variables-and-modes/server-system-variables#autocommit). This means, any update or insert statements following mysql\_commit() will be rolled back when the connection gets closed.
{% endhint %}

## See Also

* [mysql\_rollback()](mysql_rollback.md)
* [mysql\_autocommit()](mysql_autocommit.md)

{% @marketo/form formId="4316" %}
