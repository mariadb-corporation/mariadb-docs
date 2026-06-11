---
description: >-
  mysql_stmt_fetch retrieves the next row from a prepared statement result set
  into the buffers bound by mysql_stmt_bind_result, returning MYSQL_NO_DATA at
  end of set.
---

# mysql\_stmt\_fetch

## Syntax

```c
int mysql_stmt_fetch(MYSQL_STMT * stmt);
```

## Parameter

* `stmt` - a statement handle, which was previously allocated by [mysql\_stmt\_init()](mysql_stmt_init.md).

## Description

Fetch the result from a prepared statement into the buffer bound by mysql\_stmt\_bind\_result().

## Return Value

Returns `0` for success, `MYSQL_NO_DATA` if the end of the result set has been reached, or `MYSQL_DATA_TRUNCATED` if one or more values are truncated.

{% hint style="info" %}
* Note that all columns must be bound by the application before calling mysql\_stmt\_fetch().
* Data are transferred unbuffered without calling [mysql\_stmt\_store\_result()](mysql_stmt_store_result.md) which can decrease performance (but reduces memory cost).
* Truncation reporting must be enabled by function [mysql\_optionsv()](../api-functions/mysql_optionsv.md) with option `MYSQL_REPORT_DATA_TRUNCATION`
{% endhint %}

## See Also

* [mysql\_stmt\_prepare()](mysql_stmt_prepare.md)
* [mysql\_stmt\_bind\_result()](mysql_stmt_bind_result.md)
* [mysql\_stmt\_execute()](mysql_stmt_execute.md)

{% @marketo/form formId="4316" %}
