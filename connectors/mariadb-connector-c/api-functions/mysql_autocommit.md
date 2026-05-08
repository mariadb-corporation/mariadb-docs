---
description: >-
  mysql_autocommit enables or disables autocommit mode for the current
  database connection, returning zero on success or nonzero on failure.
---

# mysql\_autocommit

## Syntax

```c
my_bool mysql_autocommit(MYSQL * mysql, my_bool auto_mode);
```

* `mysql` - a mysql handle, identifier, which was previously allocated by [mysql\_init()](mysql_init.md) or [mysql\_real\_connect()](mysql_real_connect.md).
* `auto_mode` - whether to turn [autocommit](https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/server-management/variables-and-modes/server-system-variables#autocommit) on or not.

## Description

Toggles autocommit mode on or off for the current database connection. Autocommit mode will be set if mode=1 or unset if mode=0. Returns zero on success, or nonzero if an error occurred.\
Parameters

{% hint style="info" %}
[Autocommit](https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/server-management/variables-and-modes/server-system-variables#autocommit) mode only affects operations on transactional table types. To determine the current state of autocommit mode use the SQL command `SELECT @@autocommit`. Be aware: the [mysql\_rollback()](mysql_rollback.md) function will not work if autocommit mode is switched on.
{% endhint %}

## Turning off autocommit in sql

```sql
SET AUTOCOMMIT=0;
```

{% @marketo/form formId="4316" %}
