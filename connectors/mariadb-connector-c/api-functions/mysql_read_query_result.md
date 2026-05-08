---
description: >-
  mysql_read_query_result reads the result of a statement previously sent
  with mysql_send_query, and must be called once for each successful
  mysql_send_query call.
---

# mysql\_read\_query\_result

## Syntax

```c
int mysql_read_query_result(MYSQL * mysql);
```

* `mysql` - a mysql handle, which was previously allocated by [mysql\_init()](mysql_init.md) or [mysql\_real\_connect()](mysql_real_connect.md).

Returns zero on success, otherwise non-zero.

## Description

`mysql_read_query_result()` reads the result of a SQL statement executed with [mysql\_send\_query()](mysql_send_query.md). If the SQL statement returned a resultset, it must be freed before the next call to `mysql_read_query_result()` is made. This is similar to how results from [mysql\_query()](mysql_query.md) must be processed before another call can be made.


{% @marketo/form formId="4316" %}
