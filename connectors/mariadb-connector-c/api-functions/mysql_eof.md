# mysql\_eof

## Syntax

```bnf
#include <mysql.h>

my_bool mysql_eof(MYSQL_RES *result);
```

## Parameter

| Parameter | Description                                                                      |
| --------- | -------------------------------------------------------------------------------- |
| `result`  | A result set handle returned by [`mysql_store_result()`](mysql_store_result.md). |

## Description

`mysql_eof` determines whether the final row in a result set has already been retrieved.

## Return Value

Returns non-zero (true) if the entire result set has been read, or zero (false) if rows are still available.

{% hint style="info" %}
**Deprecated.** `mysql_eof` is deprecated. To determine the end of a result set, check the return value of [`mysql_fetch_row`](mysql_fetch_row.md) instead: a `NULL` return indicates that all rows have been fetched.

When the result set was acquired via [`mysql_store_result()`](mysql_store_result.md), `mysql_eof` always returns true because the entire result is buffered in memory at retrieval time.
{% endhint %}

## See Also

* [`mysql_fetch_row()`](mysql_fetch_row.md)
* [`mysql_store_result()`](mysql_store_result.md)
