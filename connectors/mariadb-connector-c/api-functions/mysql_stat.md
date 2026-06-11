---
description: >-
  mysql_stat returns a status string from the MariaDB server covering uptime,
  active threads, query count, open tables, and queries per second.
---

# mysql\_stat

## Syntax

```c
const char * mysql_stat(MYSQL * mysql);
```

## Parameter

* `mysql` - a mysql handle, which was previously allocated by [mysql\_init()](mysql_init.md) or [mysql\_real\_connect()](mysql_real_connect.md).

## Description

`mysql_stat()` returns a string with the current server status for uptime, threads, queries, open tables, flush tables and queries per second.

{% hint style="info" %}
For a complete list of other status variables, you have to use the [SHOW STATUS](https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/reference/sql-statements/administrative-sql-statements/show/show-status) SQL command.
{% endhint %}

## See Also

* [mysql\_get\_server\_info()](mysql_get_server_info.md)

{% @marketo/form formId="4316" %}
