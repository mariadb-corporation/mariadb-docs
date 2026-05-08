---
description: >-
  mysql_use_result initiates unbuffered retrieval of a query result set row
  by row from the MariaDB server, blocking the connection until all rows are
  fetched or freed.
---

# mysql\_use\_result

## Syntax

```c
MYSQL_RES * mysql_use_result(MYSQL * mysql);
```

* `mysql` - a mysql handle, which was previously allocated by [mysql\_init()](mysql_init.md) or [mysql\_real\_connect()](mysql_real_connect.md).

## Description

Used to initiate the retrieval of a result set from the last query executed using the `mysql_real_query()` function on the database connection. Either this or the [mysql\_store\_result()](mysql_store_result.md) function must be called before the results of a query can be retrieved, and one or the other must be called to prevent the next query on that database connection from failing.

Returns an unbuffered result set or NULL if an error occurred.

{% hint style="info" %}
The `mysql_use_result()` function does not transfer the entire result set. Hence, several functions like [mysql\_num\_rows()](mysql_num_rows.md) or [mysql\_data\_seek()](mysql_data_seek.md) cannot be used.

`mysql_use_result()` will block the current connection until all result sets are retrieved, or result set was released by [mysql\_free\_result()](mysql_free_result.md).
{% endhint %}

## See also

* [mysql\_store\_result()](mysql_store_result.md)
* [mysql\_free\_result()](mysql_free_result.md)

{% @marketo/form formId="4316" %}
