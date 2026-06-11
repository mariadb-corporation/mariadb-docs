---
description: >-
  mysql_send_query dispatches a query asynchronously on a MariaDB connection;
  each call must be followed by mysql_read_query_result to consume the response.
---

# mysql\_send\_query

## Syntax

```c
int mysql_send_query(MYSQL * mysql,
                     const char * query,
                     unsigned long length);
```

## Parameters

* `mysql` - a mysql handle, which was previously allocated by [mysql\_init()](mysql_init.md) or [mysql\_real\_connect()](mysql_real_connect.md).
* `query` - the query to execute.
* `length` - length of `query`.

Returns zero on success, otherwise non-zero.

## Description

`mysql_send_query()` executes a SQL statement without waiting for the Server OK packet and/or resultset. The main purpose of this function is to perform batch execution of DML statements.

{% hint style="info" %}
* The OK and result set package need to be retrieved by mysql\_read\_query\_result() function
* `mysql_send_query()` can be used for semi asynchronous operation. While the function itself is blocking, an event driven application can do other tasks until result set is available.
{% endhint %}

## Example

For an example how to use 'mysql\_send\_query()\` in an event driven model, please check Jan Kneschke's article ["Async MySQL Queries with C-API"](https://jan.kneschke.de/projects/mysql/async-mysql-queries-with-c-api/).

## See Also

* [mysql\_read\_query\_result()](mysql_read_query_result.md)

{% @marketo/form formId="4316" %}
