---
description: >-
  mysql_fetch_row retrieves the next row from a MariaDB result set as an array
  of char pointers, returning NULL when no more rows are available.
---

# mysql\_fetch\_row

## Syntax

```c
MYSQL_ROW mysql_fetch_row(MYSQL_RES * result);
```

## Parameter

* `result` - a result set identifier returned by [mysql\_store\_result()](mysql_store_result.md) or [mysql\_use\_result()](mysql_use_result.md).

## Description

Fetches one row of data from the result set and returns it as an array of char pointers (MYSQL\_ROW), where each column is stored in an offset starting from 0 (zero). Each subsequent call to this function will return the next row within the result set, or NULL if there are no more rows.

{% hint style="info" %}
If a column contains a NULL value the corresponding char pointer will be set to NULL.

Memory associated to MYSQL\_ROW will be freed when calling [mysql\_free\_result()](mysql_free_result.md) function.
{% endhint %}

## See Also

* [mysql\_use\_result()](mysql_use_result.md)
* [mysql\_store\_result()](mysql_store_result.md)

{% @marketo/form formId="4316" %}
