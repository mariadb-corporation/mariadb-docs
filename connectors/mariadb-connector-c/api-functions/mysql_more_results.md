---
description: >-
  mysql_more_results indicates whether additional result sets remain from a
  previous multi-statement query, returning 1 if more results are available.
---

# mysql\_more\_results

## Syntax

```c
my_bool mysql_more_results(MYSQL * mysql);
```

## Parameter

* `mysql` - a mysql handle, which was previously allocated by [mysql\_init()](mysql_init.md) or [mysql\_real\_connect()](mysql_real_connect.md).

## Description

Indicates if one or more result sets are available from a previous call to [mysql\_real\_query()](mysql_real_query.md).&#x20;

## Return Value

Returns 1 if more result sets are available, otherwise zero..

{% hint style="info" %}
* The function [mysql\_set\_server\_option()](mysql_set_server_option.md) enables or disables multi statement support.
* Multiple result sets can be obtained either by calling a stored procedure or by executing concatenated statements, e.g. `SELECT a FROM t1;SELECT b, c FROM t2`.
{% endhint %}

## See Also

* [mysql\_real\_query()](mysql_real_query.md)
* [mysql\_use\_result()](mysql_use_result.md)
* [mysql\_store\_result()](mysql_store_result.md)
* [mysql\_next\_result()](mysql_next_result.md)

{% @marketo/form formId="4316" %}
