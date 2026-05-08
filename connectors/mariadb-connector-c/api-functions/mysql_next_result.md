---
description: >-
  mysql_next_result advances to the next result set from a multi-statement
  query, making it available for retrieval via mysql_store_result or
  mysql_use_result.
---

# mysql\_next\_result

## Syntax

```c
int mysql_next_result(MYSQL * mysql);
```

* `mysql` - a mysql handle, which was previously allocated by [mysql\_init()](mysql_init.md) or [mysql\_real\_connect()](mysql_real_connect.md).

## Description

Prepares next result set from a previous call to [mysql\_real\_query()](mysql_real_query.md) which can be retrieved by [mysql\_store\_result()](mysql_store_result.md) or [mysql\_use\_result()](mysql_use_result.md). Returns zero on success, nonzero if an error occurred.

{% hint style="info" %}
If a multi query contains errors the return value of [mysql\_errno](mysql_errno.md)/error() might change and there will be no result set available.
{% endhint %}

## See also

* [mysql\_real\_query()](mysql_real_query.md)
* [mysql\_store\_result()](mysql_store_result.md)
* [mysql\_use\_result()](mysql_use_result.md)
* [mysql\_more\_results()](mysql_more_results.md)


{% @marketo/form formId="4316" %}
