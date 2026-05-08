---
description: >-
  mysql_select_db changes the default database on an active connection; the
  current default can also be queried with the SELECT DATABASE() SQL
  function.
---

# mysql\_select\_db

## Syntax

```c
int mysql_select_db(MYSQL * mysql,
                    const char * db);
```

* `mysql` - a mysql handle, which was previously allocated by [mysql\_init()](mysql_init.md) or [mysql\_real\_connect()](mysql_real_connect.md).
* `db` - the default database name

## Description

Selects a database as default. Returns zero on success, non-zero on failure

{% hint style="info" %}
The SQL command [SELECT DATABASE()](https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/reference/sql-functions/secondary-functions/information-functions/database) will return the name of the default database.

The default database can also be set by the db parameter in [mysql\_real\_connect()](mysql_real_connect.md).
{% endhint %}

{% @marketo/form formId="4316" %}
