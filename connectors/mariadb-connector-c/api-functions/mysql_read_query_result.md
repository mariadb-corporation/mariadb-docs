---
description: >-
  mysql_read_query_result reads the result of a statement previously sent with
  mysql_send_query, and must be called once for each successful mysql_send_query
  call.
---

# mysql\_read\_query\_result

## Syntax

```c
int mysql_read_query_result(MYSQL * mysql);
```

## Parameter

* `mysql` - a mysql handle, which was previously allocated by [mysql\_init()](mysql_init.md) or [mysql\_real\_connect()](mysql_real_connect.md).

## Description

`mysql_read_query_result()` reads the result of a SQL statement executed with [mysql\_send\_query()](mysql_send_query.md). If the SQL statement returned a result set, it must be freed before the next call to `mysql_read_query_result()` is made. This is similar to how results from [mysql\_query()](mysql_query.md) must be processed before another call can be made.

## Return Value

Returns zero on success, otherwise non-zero.

## Example

For an example how to use [`mysql_send_query()`](mysql_send_query.md) in an event driven model, please check Jan Kneschke's Blog entry ["Async MySQL Queries with C-API"](https://jan.kneschke.de/projects/mysql/async-mysql-queries-with-c-api/).

## See Also

* [mysql\_real\_query()](mysql_real_query.md)
* [mysql\_send\_query()](mysql_send_query.md)



{% @marketo/form formId="4316" %}
