---
description: >-
  mysql_rollback undoes the current transaction for a database connection; it
  has no effect if autocommit is enabled or the engine is non-transactional.
---

# mysql\_rollback

## Syntax

```c
my_bool mysql_rollback(MYSQL * mysql);
```

## Parameter

* `mysql` - a mysql handle, which was previously allocated by [mysql\_init()](mysql_init.md) or [mysql\_real\_connect()](mysql_real_connect.md).

## Description

Rolls back the current transaction for the database.&#x20;

## Return Value

Returns zero on success, nonzero if an error occurred.

{% hint style="info" %}
`mysql_rollback()` will not work as expected if [autocommit](https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/server-management/variables-and-modes/server-system-variables#autocommit) mode was set or the storage engine does not support transactions.
{% endhint %}

## See Also

* [mysql\_commit()](mysql_commit.md)
* [mysql\_autocommit()](mysql_autocommit.md)

{% @marketo/form formId="4316" %}
