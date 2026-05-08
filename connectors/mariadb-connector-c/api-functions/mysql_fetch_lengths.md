---
description: >-
  mysql_fetch_lengths returns an array of byte lengths for each column in
  the current row of a MariaDB result set, valid only after mysql_fetch_row
  is called.
---

# mysql\_fetch\_lengths

## Syntax

```c
unsigned long * mysql_fetch_lengths(MYSQL_RES * result);
```

* `result` - a result set identifier returned by [mysql\_store\_result()](mysql_store_result.md) or [mysql\_use\_result()](mysql_use_result.md).

## Description

The mysql\_fetch\_lengths() function returns an array containing the lengths of every column of the current row within the result set (not including terminating zero character) or NULL if an error occurred.

{% hint style="info" %}
mysql\_fetch\_lengths() is valid only for the current row of the result set. It returns NULL if you call it before calling [mysql\_fetch\_row()](mysql_fetch_row.md) or after retrieving all rows in the result.
{% endhint %}

## See also

* [mysql\_fetch\_row()](mysql_fetch_row.md)


{% @marketo/form formId="4316" %}
