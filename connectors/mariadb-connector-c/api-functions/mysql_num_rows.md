---
description: >-
  mysql_num_rows returns the number of rows in a MariaDB result set; for
  unbuffered results the count is only accurate after all rows have been
  fetched.
---

# mysql\_num\_rows

## Syntax

```c
my_ulonglong mysql_num_rows(MYSQL_RES * );
```

* `MYSQL_RES` - a result set identifier returned by [mysql\_store\_result()](mysql_store_result.md) or [mysql\_use\_result()](mysql_use_result.md).

## Description

Returns number of rows in a result set.

{% hint style="info" %}
The behavior of `mysql_num_rows()` depends on whether buffered or unbuffered result sets are being used. For unbuffered result sets, `mysql_num_rows()` will not return the correbct number of rows until all the rows in the result have been retrieved.
{% endhint %}

## See also

* [mysql\_affected\_rows()](mysql_affected_rows.md)
* [mysql\_use\_result()](mysql_use_result.md)
* [mysql\_store\_result()](mysql_store_result.md)

{% @marketo/form formId="4316" %}
