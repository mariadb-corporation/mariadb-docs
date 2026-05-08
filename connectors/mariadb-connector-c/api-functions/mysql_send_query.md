---
description: >-
  mysql_send_query dispatches a query asynchronously on a MariaDB
  connection; each call must be followed by mysql_read_query_result to
  consume the response.
---

# mysql\_send\_query

## Syntax

```c
int mysql_send_query(MYSQL * mysql,
                     const char * query,
                     unsigned long length);
```

* `mysql` - a mysql handle, which was previously allocated by [mysql\_init()](mysql_init.md) or [mysql\_real\_connect()](mysql_real_connect.md).
* `query` - the query to execute.
* `length` - length of `query`.

Returns zero on success, otherwise non-zero.

## Description

`mysql_send_query()` executes a SQL statement without waiting for the result. The main purpose of this function is to perform batch execution of DML statements.

Each successful call to`mysql_send_query()` must be followed by a call to [mysql\_read\_query\_result()](mysql_read_query_result.md). Multiple calls to `mysql_send_query()` can be made before the calls to [mysql\_read\_query\_result()](mysql_read_query_result.md) are done.


{% @marketo/form formId="4316" %}
